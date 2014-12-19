<%@ WebHandler Language="C#" Class="proxy" %>
/*
  This proxy page does not have any security checks. It is highly recommended
  that a user deploying this proxy page on their web server, add appropriate
  security checks, for example checking request path, username/password, target
  url, etc.
*/
using System;
using System.Drawing;
using System.IO;
using System.Web;
using System.Collections.Generic;
using System.Text;
using System.Web.Helpers;
using System.Xml.Serialization;
using System.Web.Caching;
using System.Net;

/// <summary>
/// Forwards requests to an ArcGIS Server REST resource. Uses information in
/// the proxy.config file to determine properties of the server.
/// </summary>
public class proxy : IHttpHandler
{
    ProxyConfig config;

    public proxy()
    {
        config = ProxyConfig.GetCurrentConfig();
    }

    public void ProcessRequest(HttpContext context)
    {   
        HttpResponse response = context.Response;
        
        // Get the URL requested by the client (take the entire querystring at once
        //  to handle the case of the URL itself containing querystring parameters)
        string uri = Uri.UnescapeDataString(context.Request.QueryString.ToString());

        
        // Debug: Ping to make sure avaiable (ie. http://localhost/TestApp/proxy.ashx?ping)
        if (uri.StartsWith("ping"))
        {
            context.Response.Write("Hello proxy");
            return;
        }

        // Get token, if applicable, and append to the request
        string token = getTokenFromConfigFile(uri);
        System.Net.ICredentials credentials = null;

        if (string.IsNullOrEmpty(token))
            token = generateToken(uri);   

        if (!string.IsNullOrEmpty(token))
        {
            if (uri.Contains("?"))
                uri += "&token=" + token;
            else
                uri += "?token=" + token;
        }
        else if(!string.IsNullOrEmpty(config.GetUser(uri))) // if using Windows/HTTP authentication
        {
            credentials = getCredentials(uri);
        }

        System.Net.WebRequest req = System.Net.WebRequest.Create(new Uri(uri));
        req.Method = context.Request.HttpMethod;
        req.Proxy = GetInternetProxy();

        // Assign credentials if using Windows/HTTP authentication
        if (credentials != null)
        {
            req.PreAuthenticate = true;
            req.Credentials = credentials;
        }

        // Set body of request for POST requests
        if (context.Request.InputStream.Length > 0)
        {
            byte[] bytes = new byte[context.Request.InputStream.Length];
            context.Request.InputStream.Read(bytes, 0, (int)context.Request.InputStream.Length);
            req.ContentLength = bytes.Length;
            req.ContentType = "application/x-www-form-urlencoded";
            using (Stream outputStream = req.GetRequestStream())
            {
                outputStream.Write(bytes, 0, bytes.Length);
            }
        }
        
        // Send the request to the server
        System.Net.WebResponse serverResponse = null;
        try
        {
            serverResponse = req.GetResponse();
        }
        catch (System.Net.WebException webExc)
        {
            response.StatusCode = 500;
            response.StatusDescription = webExc.Status.ToString();
            response.Write(webExc.Response);
            response.End();
            return;
        }

        // Set up the response to the client
        if (serverResponse != null)
        {
            response.ContentType = serverResponse.ContentType;
            using (Stream byteStream = serverResponse.GetResponseStream())
            {
                if (serverResponse.ContentLength > 0)
                {
                    BinaryReader br = new BinaryReader(byteStream);
                    byte[] outb = br.ReadBytes((int)serverResponse.ContentLength);                    
                    br.Close();
                    response.OutputStream.Write(outb, 0, outb.Length);
                }
                else // If we don't have content-length, read stream to end
                {
                    byte[] outb = new byte[102400];
                    int count = 0;
                    while ((count = byteStream.Read(outb, 0, 102400)) > 0)
                        response.OutputStream.Write(outb, 0, count);
                }

                // Send the image to the client
                // (Note: if large images/files sent, could modify this to send in chunks)
                serverResponse.Close();
            }
        }
        response.End();
    }

    public bool IsReusable
    {
        get
        {
            return false;
        }
    }

    // Gets the token for a server URL from a configuration file
    private string getTokenFromConfigFile(string uri)
    {
        try
        {            
            if (config != null)
                return config.GetToken(uri);
            else
                throw new ApplicationException(
                    "Proxy.config file does not exist at application root, or is not readable.");
        }
        catch (InvalidOperationException)
        {
            // Proxy is being used for an unsupported service (proxy.config has mustMatch="true")
            HttpResponse response = HttpContext.Current.Response;
            response.StatusCode = (int)System.Net.HttpStatusCode.Forbidden;
            response.End();
        }
        catch (Exception e)
        {
            if (e is ApplicationException)
                throw e;

            // just return an empty string at this point
            // -- may want to throw an exception, or add to a log file
        }

        return string.Empty;
    }

    public System.Net.ICredentials getCredentials(string url)
    {
        try
        {
            if (config != null)
            {
                foreach (ServerItem si in config.ServerItems)
                {
                    if (url.StartsWith(si.Url, true, null))
                    {
                        //string url_401 = url.Substring(0, url.IndexOf("Server") + 6);
                        string url_401 = "";
                        if (url.IndexOf("Server") >= 0)
                            url_401 = url.Substring(0, url.IndexOf("Server") + 6);
                        else
                            url_401 = url;

                        if (HttpRuntime.Cache[url_401] == null)
                        {
                            HttpWebRequest webRequest_401 = null;
                            webRequest_401 = (HttpWebRequest)HttpWebRequest.Create(url_401);
                            webRequest_401.ContentType = "text/xml;charset=\"utf-8\"";
                            webRequest_401.Method = "POST";
                            webRequest_401.Accept = "text/xml";
                            webRequest_401.Proxy = GetInternetProxy();

                            HttpWebResponse webResponse_401 = null;
                            while (webResponse_401 == null || webResponse_401.StatusCode != HttpStatusCode.OK)
                            {
                                try
                                {
                                    webResponse_401 = (System.Net.HttpWebResponse)webRequest_401.GetResponse();
                                }
                                catch (System.Net.WebException webex)
                                {
                                    if (webex.Response == null)
                                        throw webex;

                                    System.Net.HttpWebResponse webexResponse = (HttpWebResponse)webex.Response;
                                    if (webexResponse.StatusCode == HttpStatusCode.Unauthorized)
                                    {
                                        if (webRequest_401.Credentials == null)
                                        {
                                            webRequest_401 = (HttpWebRequest)HttpWebRequest.Create(url_401);                                            
                                            webRequest_401.Credentials = new System.Net.NetworkCredential(si.Username, si.Password);
                                            webRequest_401.Proxy = GetInternetProxy();
                                        }
                                        else // if original credentials not accepted, throw exception
                                            throw webex;
                                    }
                                    else // if status code unrecognized, throw exception                                          
                                        throw webex;
                                }
                                catch (Exception ex) { throw ex; }
                            }                            

                            if (webResponse_401 != null)
                                webResponse_401.Close();

                            HttpRuntime.Cache.Insert(url_401, webRequest_401.Credentials);
                        }
                        return (ICredentials)HttpRuntime.Cache[url_401];
                    }
                }
            }
        }
        catch (InvalidOperationException e)
        {
            // Proxy is being used for an unsupported service (proxy.config has mustMatch="true")
            HttpResponse response = HttpContext.Current.Response;
            response.StatusCode = (int)System.Net.HttpStatusCode.Forbidden;
            response.End();
        }
        catch (Exception e)
        {
            if (e is ApplicationException)
                throw e;

            // just return an empty string at this point
            // -- may want to throw an exception, or add to a log file
        }

        return null;
    }

    public string generateToken(string url)
    {
        try
        {
            if (config != null)
            {
                foreach (ServerItem si in config.ServerItems)
                    if (url.StartsWith(si.Url, true, null))
                    {
                        string theToken = null;

                        // If a token has been generated, check the expire time
                        if (HttpRuntime.Cache[si.Url] != null)
                        {
                            string existingToken = (HttpRuntime.Cache[si.Url] as
                            Dictionary<string, object>)["token"] as string;

                            DateTime expireTime = (DateTime)((HttpRuntime.Cache[si.Url] as
                            Dictionary<string, object>)["timeout"]);

                            // If token not expired, return it
                            if (DateTime.Now.CompareTo(expireTime) < 0)
                                theToken = existingToken;
                        }

                        // If token not available or expired, generate one and store it in cache
                        if (theToken == null)
                        {
                            string tokenServiceUrl = string.Format("{0}?request=getToken&username={1}&password={2}&referer={3}&f=json",
                                si.TokenUrl, si.Username, si.Password, si.Referer);

                            int timeout = 60;
                            if (si.Timeout > 0)
                                timeout = si.Timeout;

                            tokenServiceUrl += string.Format("&expiration={0}", timeout);
                            DateTime endTime = DateTime.Now.AddMinutes(timeout);

                            System.Net.WebRequest request = System.Net.WebRequest.Create(tokenServiceUrl);
                            System.Net.WebResponse response = request.GetResponse();
                            System.IO.Stream responseStream = response.GetResponseStream();
                            System.IO.StreamReader readStream = new System.IO.StreamReader(responseStream);
                            var resp = readStream.ReadToEnd();
                            var fromJson = Json.Decode(resp);
                            theToken = fromJson.token;
                            
                            Dictionary<string, object> serverItemEntries = new Dictionary<string, object>();
                            serverItemEntries.Add("token", theToken);
                            serverItemEntries.Add("timeout", endTime);

                            HttpRuntime.Cache.Insert(si.Url, serverItemEntries);
                        }
                        return theToken;
                    }
            }
        }
        catch (InvalidOperationException)
        {
            // Proxy is being used for an unsupported service (proxy.config has mustMatch="true")
            HttpResponse response = HttpContext.Current.Response;
            response.StatusCode = (int)System.Net.HttpStatusCode.Forbidden;
            response.End();
        }
        catch (Exception e)
        {
            if (e is ApplicationException)
                throw e;

            // just return an empty string at this point
            // -- may want to throw an exception, or add to a log file
        }

        return string.Empty;
    }

    private IWebProxy GetInternetProxy()
    {        
        string proxyURL = config.ProxyURL;
        string proxyUser = config.ProxyUser;
        string proxyPassword = config.ProxyPassword;
        string proxyDomain = config.ProxyDomain;

        IWebProxy proxy = null;
        if (String.IsNullOrEmpty(proxyURL))
        {
            proxy = System.Net.WebRequest.GetSystemWebProxy();
            proxy.Credentials = CredentialCache.DefaultCredentials;
        }
        else
        {
            proxy = new WebProxy(proxyURL,true);
            if(!String.IsNullOrEmpty(proxyUser) && !String.IsNullOrEmpty(proxyPassword) && !String.IsNullOrEmpty(proxyDomain))
                proxy.Credentials = new NetworkCredential(proxyUser, proxyPassword, proxyDomain);
            else if (!String.IsNullOrEmpty(proxyUser) && !String.IsNullOrEmpty(proxyPassword))
                proxy.Credentials = new NetworkCredential(proxyUser, proxyPassword);
        }
        
        return proxy;
    }
}

[XmlRoot("ProxyConfig")]
public class ProxyConfig
{
    #region Static Members

    private static object _lockobject = new object();

    public static ProxyConfig LoadProxyConfig(string fileName)
    {
        ProxyConfig config = null;

        lock (_lockobject)
        {
            if (System.IO.File.Exists(fileName))
            {
                XmlSerializer reader = new XmlSerializer(typeof(ProxyConfig));
                using (System.IO.StreamReader file = new System.IO.StreamReader(fileName))
                {
                    config = (ProxyConfig)reader.Deserialize(file);
                }
            }
        }

        return config;
    }

    public static ProxyConfig GetCurrentConfig()
    {
        ProxyConfig config = HttpRuntime.Cache["proxyConfig"] as ProxyConfig;
        if (config == null)
        {
            string fileName = GetFilename(HttpContext.Current);
            config = LoadProxyConfig(fileName);

            if (config != null)
            {
                CacheDependency dep = new CacheDependency(fileName);
                HttpRuntime.Cache.Insert("proxyConfig", config, dep);
            }
        }

        return config;
    }

    // Location of the proxy.config file
    public static string GetFilename(HttpContext context)
    {
        return context.Server.MapPath("proxy.config");
    }
    #endregion

    ServerItem[] serverItems;
    bool mustMatch;
    string proxyURL;
    string proxyUser;
    string proxyPassword;
    string proxyDomain;    

    [XmlArray("serverItems")]
    [XmlArrayItem("serverItem")]
    public ServerItem[] ServerItems
    {
        get { return this.serverItems; }
        set { this.serverItems = value; }
    }

    [XmlAttribute("mustMatch")]
    public bool MustMatch
    {
        get { return mustMatch; }
        set { mustMatch = value; }
    }

    [XmlAttribute("proxyURL")]
    public string ProxyURL
    {
        get { return proxyURL; }
        set { proxyURL = value; }
    }

    [XmlAttribute("proxyUser")]
    public string ProxyUser
    {
        get { return proxyUser; }
        set { proxyUser = value; }
    }

    [XmlAttribute("proxyPassword")]
    public string ProxyPassword
    {
        get { return proxyPassword; }
        set { proxyPassword = value; }
    }

    [XmlAttribute("proxyDomain")]
    public string ProxyDomain
    {
        get { return proxyDomain; }
        set { proxyDomain = value; }
    }

    public string GetToken(string uri)
    {
        foreach (ServerItem su in serverItems)
        {
            if (su.MatchAll && uri.StartsWith(su.Url, StringComparison.InvariantCultureIgnoreCase))
            {
                return su.Token;
            }
            else
            {
                if (String.Compare(uri, su.Url, StringComparison.InvariantCultureIgnoreCase) == 0)
                    return su.Token;
            }
        }

        if (mustMatch)
            throw new InvalidOperationException();

        return string.Empty;
    }
    
    public string GetUser(string uri)
    {
        foreach (ServerItem su in serverItems)
        {
            if (su.MatchAll && uri.StartsWith(su.Url, StringComparison.InvariantCultureIgnoreCase))
            {
                return su.Username;
            }
            else
            {
                if (String.Compare(uri, su.Url, StringComparison.InvariantCultureIgnoreCase) == 0)
                    return su.Username;
            }
        }

        if (mustMatch)
            throw new InvalidOperationException();

        return string.Empty;
    }
}

public class ServerItem
{
    string url;
    bool matchAll;
    string token;
    string tokenUrl;
    string domain;
    string username;
    string password;
    int timeout;
    private string referer;

    [XmlAttribute("referer")]
    public string Referer
    {
        get { return referer; }
        set { referer = value; }
    }

    [XmlAttribute("url")]
    public string Url
    {
        get { return url; }
        set { url = value; }
    }

    [XmlAttribute("matchAll")]
    public bool MatchAll
    {
        get { return matchAll; }
        set { matchAll = value; }
    }

    [XmlAttribute("token")]
    public string Token
    {
        get { return token; }
        set { token = value; }
    }

    [XmlAttribute("tokenUrl")]
    public string TokenUrl
    {
        get { return tokenUrl; }
        set { tokenUrl = value; }
    }

    [XmlAttribute("domain")]
    public string Domain
    {
        get { return domain; }
        set { domain = value; }
    }

    [XmlAttribute("username")]
    public string Username
    {
        get { return username; }
        set { username = value; }
    }

    [XmlAttribute("password")]
    public string Password
    {
        get { return password; }
        set { password = value; }
    }

    [XmlAttribute("timeout")]
    public int Timeout
    {
        get { return timeout; }
        set { timeout = value; }
    }
}

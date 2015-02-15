using System;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;

namespace ImgurAPI
{
    class Imgur
    {

        private string apiKey;

        WebClient wc = new WebClient();

            public string getImgurStuff()
                {
                    NameValueCollection data = new NameValueCollection();
                data["section"] = "hot";
                data["sort"] = "viral";
                data["showViral"] = "true";
                    WebClient wc = new WebClient();
                    wc.Headers.Add("Authorization", "Client-ID fcbab01227cd957");
                    wc.UploadValues("https://api.imgur.com/3/gallery/", data);
                    return "HELLO";
                }
        
    }



}

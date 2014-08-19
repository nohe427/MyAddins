using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Net;
using System.Collections.Specialized;

namespace CreditQuest
{
    class AGOL
    {
        private string _token;
        private string _orgInfo;
        private string _urlKey;
        private string _username;
        private string _password;

        public string Token
        {
            get
            {
                return _token;
            }
        }

        public string OrgInfo
        {
            get
            {
                return _orgInfo;
            }
        }

        public string URLKey
        {
            get
            {
                return _urlKey;
            }
        }

        public string Username
        {
            get
            {
                return _username;
            }
            set
            {
                _username = value;
            }
        }

        public string Password
        {
            get
            {
                return _password;
            }
            set
            {
                _password = value;
            }
        }
        public AGOL(string UserName, string PassWord)
        {
            Username = UserName;
            Password = PassWord;

            var wb = new WebClient();
            
                var data = new NameValueCollection();
                data["username"] = Username;
                data["password"] = Password;
                data["referer"] = "https://www.arcgis.com";
                data["f"] = "json";

                var response = wb.UploadValues("", data);
            
        }
    }
}

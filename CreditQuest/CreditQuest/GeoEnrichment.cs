using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Text;

namespace CreditQuest
{
    class GeoEnrichment
    {
        public GeoEnrichment()
        {

        using(WebClient client = new WebClient())
            {
                client.DownloadFile("http://geoenrich.arcgis.com/arcgis/rest/services/World/geoenrichmentserver/GeoEnrichment/CreateReport?studyAreas=[{%22sourceCountry%22:%22US%22,%22layer%22:%22US.ZIP5%22,%22ids%22:[%2292373%22]}]&report=dandi&f=bin&token=0lAWRSlSqKQUaPvDGPxfPrk3rERU_7vXE_KYVXJunEyi0yZcKXIjk1F4IAkcgrJG99wMU3tTCuTkziSKI_rg1ESEY1xvgFwcuHZPOHM6-JIu1wK9pgyzUI8umadDiWF6dkhTpDy0zfOI4g0Ulj8LcQ..", @"C:\Users\AlexanderDT\Desktop\WalkingDead\Temp.pdf");
            }
    }
    }
}

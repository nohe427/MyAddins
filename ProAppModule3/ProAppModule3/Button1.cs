using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using ArcGIS.Desktop.Framework;
using ArcGIS.Desktop.Framework.Contracts;
using ArcGIS.Desktop.Core;
using ArcGIS.Desktop.Mapping;

namespace ProAppModule3
{
    internal class Button1 : Button
    {
        protected override void OnClick()
        {
            //System.Windows.MessageBox.Show("Hello World!");
            Project project = ProjectModule.CurrentProject;

            IProjectItemContainer projectContainer = project.GetProjectItemContainer("Map");

            foreach(var item in projectContainer.GetProjectItems())
            {
                System.Windows.MessageBox.Show(item.Name);
                ArcGIS.Desktop.Mapping.Map map = MappingModule.FindMap(item.Path);
            }

        }
    }
}

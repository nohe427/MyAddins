import arcpy

from Snippets import GetLibPath, InitStandalone
from comtypes.client import GetModule, CreateObject
m = GetModule(GetLibPath() + "esriCarto.olb")
#InitStandalone()
p = CreateObject(m.MapDocument, interface=m.IMapDocument)
p.New("D:\\MattPatt.mxd")
#print p.X, p.Y

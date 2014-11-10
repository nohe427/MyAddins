import arcpy

from Snippets import GetLibPath, InitStandalone
from comtypes.client import GetModule, CreateObject
m = GetModule(GetLibPath() + "esriCarto.olb")
#InitStandalone()
p = CreateObject(m.MapDocument, interface=m.IMapDocument)
p.New("D:\\MattPatt.mxd")
print "MXD created"
p.Close()
print "MXD closed"
#print p.X, p.Y

mxd = arcpy.mapping.MapDocument("D:\\MattPatt.mxd")
print mxd

df = arcpy.mapping.ListDataFrames(mxd)[0]
print df

lyr = arcpy.mapping.Layer("C:\\Users\\alex7370\\Documents\\ArcGIS\\imACreep.lyr")
print lyr

arcpy.mapping.AddLayer(df, lyr)
print "Done adding"

mxd.save()
print "Saved"

del mxd

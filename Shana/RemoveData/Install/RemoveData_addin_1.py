import arcpy
import pythonaddins

class DataDelete(object):
    """Implementation for RemoveData_addin.extension2 (Extension)"""
    def __init__(self):
        # For performance considerations, please remove all unused methods in this class.
        self.enabled = True
    def beforeCloseDocument(self):
        mxd = arcpy.mapping.MapDocument("CURRENT")
        for i in arcpy.mapping.ListDataFrames(mxd):
            for z in arcpy.mapping.ListLayers(mxd, "", i):
                arcpy.mapping.RemoveLayer(i, z)
        mxd.save()


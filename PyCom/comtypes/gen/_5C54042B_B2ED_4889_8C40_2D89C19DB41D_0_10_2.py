# -*- coding: mbcs -*-
typelib_path = u'C:\\Program Files (x86)\\ArcGIS\\Engine10.2\\com\\esriGeoAnalyst.olb'
_lcid = 0 # change this if required
from ctypes import *
import comtypes.gen._8F0541A3_D5BE_4B3F_A8D9_062D5579E19B_0_10_2
import comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2
import comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2
import comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2
import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0
from comtypes import GUID
from ctypes import HRESULT
from comtypes import helpstring
from comtypes import COMMETHOD
from comtypes import dispid
from comtypes import CoClass
from comtypes import BSTR
from ctypes.wintypes import VARIANT_BOOL
from comtypes.automation import VARIANT
from comtypes.automation import VARIANT
from comtypes import IUnknown


class IMathSupportOp(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the mathematical operations for support other products.'
    _iid_ = GUID('{8608E339-8743-11D4-B278-00508BCDC779}')
    _idlflags_ = ['oleautomation']
IMathSupportOp._methods_ = [
    COMMETHOD([helpstring(u'Divides the values of two inputs.')], HRESULT, 'Divide',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'geoDataset1' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'geoDataset2' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
    COMMETHOD([helpstring(u'Subtracts the values of two inputs.')], HRESULT, 'Minus',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'geoDataset1' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'geoDataset2' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
    COMMETHOD([helpstring(u'Adds the values of two inputs.')], HRESULT, 'Plus',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'geoDataset1' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'geoDataset2' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
    COMMETHOD([helpstring(u'Multiplies the values of two inputs.')], HRESULT, 'Times',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'geoDataset1' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'geoDataset2' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
    COMMETHOD([helpstring(u'Converts a raster to integer by truncation.')], HRESULT, 'Int',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'GeoDataset' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
    COMMETHOD([helpstring(u'Converts a raster into floating point representation.')], HRESULT, 'Float',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'GeoDataset' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
]
################################################################
## code template for IMathSupportOp implementation
##class IMathSupportOp_Impl(object):
##    def Divide(self, geoDataset1, geoDataset2):
##        u'Divides the values of two inputs.'
##        #return outGeoDataset
##
##    def Int(self, GeoDataset):
##        u'Converts a raster to integer by truncation.'
##        #return outGeoDataset
##
##    def Float(self, GeoDataset):
##        u'Converts a raster into floating point representation.'
##        #return outGeoDataset
##
##    def Times(self, geoDataset1, geoDataset2):
##        u'Multiplies the values of two inputs.'
##        #return outGeoDataset
##
##    def Plus(self, geoDataset1, geoDataset2):
##        u'Adds the values of two inputs.'
##        #return outGeoDataset
##
##    def Minus(self, geoDataset1, geoDataset2):
##        u'Subtracts the values of two inputs.'
##        #return outGeoDataset
##


# values for enumeration 'esriGeoAnalysisSliceEnum'
esriGeoAnalysisSliceEqualInterval = 1
esriGeoAnalysisSliceEqualArea = 2
esriGeoAnalysisSliceNatualBreaks = 3
esriGeoAnalysisSliceStandardDeviation = 4
esriGeoAnalysisSliceEnum = c_int # enum
class StringRemap(CoClass):
    u'GeoAnalyst String remap object.'
    _reg_clsid_ = GUID('{2B1E876B-0BE8-11D4-80D6-00C04FA0702C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5C54042B-B2ED-4889-8C40-2D89C19DB41D}', 10, 2)
class IRemap(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control reclassification of data.'
    _iid_ = GUID('{2B1E876D-0BE8-11D4-80D6-00C04FA0702C}')
    _idlflags_ = ['oleautomation']
class IStringRemap(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control reclassification of string data.'
    _iid_ = GUID('{2B1E876E-0BE8-11D4-80D6-00C04FA0702C}')
    _idlflags_ = ['oleautomation']
StringRemap._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRemap, IStringRemap, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

class IReclassOp(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Reclass Operation.'
    _iid_ = GUID('{CAD7BFEE-1DD7-11D3-9F45-00C04F8ED1D7}')
    _idlflags_ = ['oleautomation']
IReclassOp._methods_ = [
    COMMETHOD([helpstring(u'Reclassifies (or changes) the values of the input cells of a raster by using a remap table.')], HRESULT, 'Reclass',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'GeoDataset' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable), 'remapTable' ),
              ( ['in'], BSTR, 'fromField' ),
              ( ['in'], BSTR, 'toField' ),
              ( ['in'], BSTR, 'OutField' ),
              ( ['in'], VARIANT_BOOL, 'retainMissingValues' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
    COMMETHOD([helpstring(u'Slices a range of values of the input cells by zones of equal area or equal interval.')], HRESULT, 'Slice',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'GeoDataset' ),
              ( ['in'], esriGeoAnalysisSliceEnum, 'sliceType' ),
              ( ['in'], c_int, 'zoneCount' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'baseZone' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
    COMMETHOD([helpstring(u'Creates a new raster by looking up values found in another field in the table of the input raster.')], HRESULT, 'Lookup',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'GeoDataset' ),
              ( ['in'], BSTR, 'FieldName' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
    COMMETHOD([helpstring(u'Reclassifies (or changes) the values of the input cells of a raster by using a remap that is built programmatically.')], HRESULT, 'ReclassByRemap',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'GeoDataset' ),
              ( ['in'], POINTER(IRemap), 'Remap' ),
              ( ['in'], VARIANT_BOOL, 'retainMissingValues' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
    COMMETHOD([helpstring(u'Reclassifies (or changes) the values of the input cells of a raster by using an ascii remap file.')], HRESULT, 'ReclassByASCIIFile',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'inRaster' ),
              ( ['in'], BSTR, 'sRemapFile' ),
              ( ['in'], VARIANT_BOOL, 'retainMissingValues' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
]
################################################################
## code template for IReclassOp implementation
##class IReclassOp_Impl(object):
##    def ReclassByASCIIFile(self, inRaster, sRemapFile, retainMissingValues):
##        u'Reclassifies (or changes) the values of the input cells of a raster by using an ascii remap file.'
##        #return outGeoDataset
##
##    def Slice(self, GeoDataset, sliceType, zoneCount, baseZone):
##        u'Slices a range of values of the input cells by zones of equal area or equal interval.'
##        #return outGeoDataset
##
##    def Lookup(self, GeoDataset, FieldName):
##        u'Creates a new raster by looking up values found in another field in the table of the input raster.'
##        #return outGeoDataset
##
##    def Reclass(self, GeoDataset, remapTable, fromField, toField, OutField, retainMissingValues):
##        u'Reclassifies (or changes) the values of the input cells of a raster by using a remap table.'
##        #return outGeoDataset
##
##    def ReclassByRemap(self, GeoDataset, Remap, retainMissingValues):
##        u'Reclassifies (or changes) the values of the input cells of a raster by using a remap that is built programmatically.'
##        #return outGeoDataset
##


# values for enumeration 'esriGeoAnalysisStatisticsEnum'
esriGeoAnalysisStatsMajority = 1
esriGeoAnalysisStatsMaximum = 2
esriGeoAnalysisStatsMean = 3
esriGeoAnalysisStatsMedian = 4
esriGeoAnalysisStatsMinimum = 5
esriGeoAnalysisStatsMinority = 6
esriGeoAnalysisStatsRange = 7
esriGeoAnalysisStatsStd = 8
esriGeoAnalysisStatsSum = 9
esriGeoAnalysisStatsVariety = 10
esriGeoAnalysisStatsLength = 11
esriGeoAnalysisStatisticsEnum = c_int # enum
class IGeoDataDescriptor(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the GeoDataset descriptor.'
    _iid_ = GUID('{18BDBEC1-C45C-11D3-9F5E-00C04F8ED1D7}')
    _idlflags_ = ['oleautomation']
IGeoDataDescriptor._methods_ = [
    COMMETHOD([helpstring(u'Creates a GeoDataset descriptor with a SelectionSet.')], HRESULT, 'CreateFromSelectionSet',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ISelectionSet), 'SelectionSet' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IQueryFilter), 'filter' ),
              ( ['in'], BSTR, 'FieldName' )),
    COMMETHOD(['propget', helpstring(u'The query filter of the GeoDataset descriptor.')], HRESULT, 'QueryFilter',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IQueryFilter)), 'QueryFilter' )),
    COMMETHOD(['propget', helpstring(u'The SelectionSet of the GeoDataset descriptor.')], HRESULT, 'SelectionSet',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ISelectionSet)), 'SelectionSet' )),
    COMMETHOD(['propget', helpstring(u'The field of the GeoDataset descriptor.')], HRESULT, 'Field',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IField)), 'Field' )),
    COMMETHOD(['propget', helpstring(u'The field name of the GeoDataset descriptor.')], HRESULT, 'FieldName',
              ( ['retval', 'out'], POINTER(BSTR), 'FieldName' )),
]
################################################################
## code template for IGeoDataDescriptor implementation
##class IGeoDataDescriptor_Impl(object):
##    def CreateFromSelectionSet(self, SelectionSet, filter, FieldName):
##        u'Creates a GeoDataset descriptor with a SelectionSet.'
##        #return 
##
##    @property
##    def QueryFilter(self):
##        u'The query filter of the GeoDataset descriptor.'
##        #return QueryFilter
##
##    @property
##    def FieldName(self):
##        u'The field name of the GeoDataset descriptor.'
##        #return FieldName
##
##    @property
##    def SelectionSet(self):
##        u'The SelectionSet of the GeoDataset descriptor.'
##        #return SelectionSet
##
##    @property
##    def Field(self):
##        u'The field of the GeoDataset descriptor.'
##        #return Field
##

IStringRemap._methods_ = [
    COMMETHOD([helpstring(u'Maps a string entry to the remap object.')], HRESULT, 'MapString',
              ( ['in'], BSTR, 'inputString' ),
              ( ['in'], c_int, 'outputValue' )),
    COMMETHOD([helpstring(u'Maps a string entry to nodata.')], HRESULT, 'MapStringToNoData',
              ( ['in'], BSTR, 'inputString' )),
    COMMETHOD([helpstring(u'Returns string record information by index.')], HRESULT, 'QueryStringRecord',
              ( ['in'], c_int, 'index' ),
              ( ['out'], POINTER(BSTR), 'inString' ),
              ( ['out'], POINTER(c_int), 'outValue' ),
              ( ['out'], POINTER(VARIANT_BOOL), 'mappedToNoData' )),
    COMMETHOD([helpstring(u'Returns the mapped value for a string remap entry.')], HRESULT, 'QueryStringValue',
              ( ['in'], BSTR, 'inString' ),
              ( ['out'], POINTER(c_int), 'outValue' ),
              ( ['out'], POINTER(VARIANT_BOOL), 'isNodata' )),
    COMMETHOD([helpstring(u'Loads string remap records from a table object.')], HRESULT, 'LoadStringsFromTable',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable), 'remapTable' ),
              ( ['in'], BSTR, 'OutFieldName' ),
              ( ['in'], BSTR, 'inFieldName' ),
              ( ['in', 'optional'], VARIANT, 'mappingFieldName' )),
]
################################################################
## code template for IStringRemap implementation
##class IStringRemap_Impl(object):
##    def LoadStringsFromTable(self, remapTable, OutFieldName, inFieldName, mappingFieldName):
##        u'Loads string remap records from a table object.'
##        #return 
##
##    def MapStringToNoData(self, inputString):
##        u'Maps a string entry to nodata.'
##        #return 
##
##    def MapString(self, inputString, outputValue):
##        u'Maps a string entry to the remap object.'
##        #return 
##
##    def QueryStringRecord(self, index):
##        u'Returns string record information by index.'
##        #return inString, outValue, mappedToNoData
##
##    def QueryStringValue(self, inString):
##        u'Returns the mapped value for a string remap entry.'
##        #return outValue, isNodata
##


# values for enumeration 'esriRasterGDBCompressionEnum'
esriRasterGDBCompressionNone = 0
esriRasterGDBCompressionLZ77 = 1
esriRasterGDBCompressionJPEG = 2
esriRasterGDBCompressionJPEG2000 = 3
esriRasterGDBCompressionPackBits = 4
esriRasterGDBCompressionLZW = 5
esriRasterGDBCompressionRLE = 6
esriRasterGDBCompressionCCITTG3 = 7
esriRasterGDBCompressionCCITTG4 = 8
esriRasterGDBCompressionCCITTRLE = 9
esriRasterGDBCompressionJPEGYCbCr = 10
esriRasterGDBCompressionEnum = c_int # enum

# values for enumeration 'esriRasterNeighborhoodEnum'
esriRectangleNeighborhood = 1
esriCircleNeighborhood = 2
esriAnnulusNeighborhood = 3
esriWedgeNeighborhood = 4
esriIrregularNeighborhood = 5
esriWeightNeighborhood = 6
esriLowPassFilterNeighborhood = 7
esriHighPassFilterNeighborhood = 8
esriRasterNeighborhoodEnum = c_int # enum
class INumberRemap(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control reclassification of numerical data.'
    _iid_ = GUID('{2B1E876F-0BE8-11D4-80D6-00C04FA0702C}')
    _idlflags_ = ['oleautomation']
INumberRemap._methods_ = [
    COMMETHOD([helpstring(u'Maps a single value entry to the remap object.')], HRESULT, 'MapValue',
              ( ['in'], c_double, 'value' ),
              ( ['in'], c_int, 'outputValue' )),
    COMMETHOD([helpstring(u'Maps a range entry to the remap object.')], HRESULT, 'MapRange',
              ( ['in'], c_double, 'MinValue' ),
              ( ['in'], c_double, 'MaxValue' ),
              ( ['in'], c_int, 'outputValue' )),
    COMMETHOD([helpstring(u'Maps a single value entry to nodata.')], HRESULT, 'MapValueToNoData',
              ( ['in'], c_double, 'value' )),
    COMMETHOD([helpstring(u'Maps a range entry to nodata.')], HRESULT, 'MapRangeToNoData',
              ( ['in'], c_double, 'MinValue' ),
              ( ['in'], c_double, 'MaxValue' )),
    COMMETHOD([helpstring(u'Returns number record information by index.')], HRESULT, 'QueryNumberRecord',
              ( ['in'], c_int, 'index' ),
              ( ['out'], POINTER(c_double), 'MinValue' ),
              ( ['out'], POINTER(c_double), 'MaxValue' ),
              ( ['out'], POINTER(c_int), 'outValue' ),
              ( ['out'], POINTER(VARIANT_BOOL), 'mappedToNoData' )),
    COMMETHOD([helpstring(u'Returns the mapped value for a number remap entry.')], HRESULT, 'QueryNumberValue',
              ( ['in'], c_double, 'inValue' ),
              ( ['out'], POINTER(c_int), 'outValue' ),
              ( ['out'], POINTER(VARIANT_BOOL), 'isNodata' )),
    COMMETHOD([helpstring(u'Load number remap records from a table object.')], HRESULT, 'LoadNumbersFromTable',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable), 'remapTable' ),
              ( ['in'], BSTR, 'OutFieldName' ),
              ( ['in'], BSTR, 'fromFieldName' ),
              ( ['in', 'optional'], VARIANT, 'toFieldName' ),
              ( ['in', 'optional'], VARIANT, 'mappingFieldName' )),
    COMMETHOD([helpstring(u'Loads the information from an ArcGRID ASCII remap file into a remap object.')], HRESULT, 'LoadNumbersFromASCIIFile',
              ( ['in'], BSTR, 'remapFile' )),
]
################################################################
## code template for INumberRemap implementation
##class INumberRemap_Impl(object):
##    def LoadNumbersFromASCIIFile(self, remapFile):
##        u'Loads the information from an ArcGRID ASCII remap file into a remap object.'
##        #return 
##
##    def QueryNumberRecord(self, index):
##        u'Returns number record information by index.'
##        #return MinValue, MaxValue, outValue, mappedToNoData
##
##    def MapRange(self, MinValue, MaxValue, outputValue):
##        u'Maps a range entry to the remap object.'
##        #return 
##
##    def QueryNumberValue(self, inValue):
##        u'Returns the mapped value for a number remap entry.'
##        #return outValue, isNodata
##
##    def MapRangeToNoData(self, MinValue, MaxValue):
##        u'Maps a range entry to nodata.'
##        #return 
##
##    def LoadNumbersFromTable(self, remapTable, OutFieldName, fromFieldName, toFieldName, mappingFieldName):
##        u'Load number remap records from a table object.'
##        #return 
##
##    def MapValue(self, value, outputValue):
##        u'Maps a single value entry to the remap object.'
##        #return 
##
##    def MapValueToNoData(self, value):
##        u'Maps a single value entry to nodata.'
##        #return 
##

class IRasterRadius(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the radius used to determine a surface through interpolation.'
    _iid_ = GUID('{3297E9CD-93A1-11D2-9F33-00C04F8ED1D7}')
    _idlflags_ = ['oleautomation']
IRasterRadius._methods_ = [
    COMMETHOD([helpstring(u'Sets a fixed radius.')], HRESULT, 'SetFixed',
              ( ['in'], c_double, 'distance' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'minCount' )),
    COMMETHOD([helpstring(u'Sets a variable radius.')], HRESULT, 'SetVariable',
              ( ['in'], c_int, 'count' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'maxDistance' )),
]
################################################################
## code template for IRasterRadius implementation
##class IRasterRadius_Impl(object):
##    def SetVariable(self, count, maxDistance):
##        u'Sets a variable radius.'
##        #return 
##
##    def SetFixed(self, distance, minCount):
##        u'Sets a fixed radius.'
##        #return 
##


# values for enumeration 'esriGeoAnalysisEnforceEnum'
esriGeoAnalysisEnforceOff = 0
esriGeoAnalysisEnforceOn = 1
esriGeoAnalysisEnforceOnWithSink = 2
esriGeoAnalysisEnforceEnum = c_int # enum
class IRasterMakerOp(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Raster Maker operations.'
    _iid_ = GUID('{CC0B70D3-EA20-11D3-9F63-00C04F8ED1D7}')
    _idlflags_ = ['oleautomation']
IRasterMakerOp._methods_ = [
    COMMETHOD([helpstring(u'Makes a constant raster.')], HRESULT, 'MakeConstant',
              ( ['in'], c_double, 'value' ),
              ( ['in'], VARIANT_BOOL, 'treatAsInteger' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
    COMMETHOD([helpstring(u'Makes a normally distributed raster.')], HRESULT, 'MakeNormal',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
    COMMETHOD([helpstring(u'Makes a randomly distributed raster.')], HRESULT, 'MakeRandom',
              ( ['in', 'optional'], VARIANT, 'seed' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
]
################################################################
## code template for IRasterMakerOp implementation
##class IRasterMakerOp_Impl(object):
##    def MakeNormal(self):
##        u'Makes a normally distributed raster.'
##        #return outGeoDataset
##
##    def MakeConstant(self, value, treatAsInteger):
##        u'Makes a constant raster.'
##        #return outGeoDataset
##
##    def MakeRandom(self, seed):
##        u'Makes a randomly distributed raster.'
##        #return outGeoDataset
##

class IRasterNeighborhood(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the analytical region used when performing neighborhood analsis.'
    _iid_ = GUID('{3297E9CC-93A1-11D2-9F33-00C04F8ED1D7}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriGeoAnalysisUnitsEnum'
esriUnitsMap = 1
esriUnitsCells = 2
esriGeoAnalysisUnitsEnum = c_int # enum
IRasterNeighborhood._methods_ = [
    COMMETHOD([helpstring(u'Sets a default neighborhood object.')], HRESULT, 'SetDefault'),
    COMMETHOD([helpstring(u'Sets an annulus neighborhood object.')], HRESULT, 'SetAnnulus',
              ( ['in'], c_double, 'innerRadius' ),
              ( ['in'], c_double, 'outerRadius' ),
              ( ['in'], esriGeoAnalysisUnitsEnum, 'unitsType' )),
    COMMETHOD([helpstring(u'Sets a circle neighborhood object.')], HRESULT, 'SetCircle',
              ( ['in'], c_double, 'radius' ),
              ( ['in'], esriGeoAnalysisUnitsEnum, 'unitsType' )),
    COMMETHOD([helpstring(u'Sets a neighborhood object each of whose entries can be turned on or off.')], HRESULT, 'SetIrregular',
              ( ['in'], c_int, 'height' ),
              ( ['in'], c_int, 'width' ),
              ( ['in'], POINTER(VARIANT), 'entryValues' )),
    COMMETHOD([helpstring(u'Sets a rectangle neighborhood object.')], HRESULT, 'SetRectangle',
              ( ['in'], c_double, 'width' ),
              ( ['in'], c_double, 'height' ),
              ( ['in'], esriGeoAnalysisUnitsEnum, 'unitsType' )),
    COMMETHOD([helpstring(u'Sets a wedge neighborhood object.')], HRESULT, 'SetWedge',
              ( ['in'], c_double, 'radius' ),
              ( ['in'], c_double, 'startAngle' ),
              ( ['in'], c_double, 'endAngle' ),
              ( ['in'], esriGeoAnalysisUnitsEnum, 'unitsType' )),
    COMMETHOD([helpstring(u'Sets a neighborhood object each of whose entries can be assigned a weight.')], HRESULT, 'SetWeight',
              ( ['in'], c_int, 'height' ),
              ( ['in'], c_int, 'width' ),
              ( ['in'], POINTER(VARIANT), 'entryValues' )),
]
################################################################
## code template for IRasterNeighborhood implementation
##class IRasterNeighborhood_Impl(object):
##    def SetIrregular(self, height, width, entryValues):
##        u'Sets a neighborhood object each of whose entries can be turned on or off.'
##        #return 
##
##    def SetDefault(self):
##        u'Sets a default neighborhood object.'
##        #return 
##
##    def SetWedge(self, radius, startAngle, endAngle, unitsType):
##        u'Sets a wedge neighborhood object.'
##        #return 
##
##    def SetAnnulus(self, innerRadius, outerRadius, unitsType):
##        u'Sets an annulus neighborhood object.'
##        #return 
##
##    def SetCircle(self, radius, unitsType):
##        u'Sets a circle neighborhood object.'
##        #return 
##
##    def SetWeight(self, height, width, entryValues):
##        u'Sets a neighborhood object each of whose entries can be assigned a weight.'
##        #return 
##
##    def SetRectangle(self, width, height, unitsType):
##        u'Sets a rectangle neighborhood object.'
##        #return 
##

class IRasterModel(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Raster Model.'
    _iid_ = GUID('{4606F163-B47D-11D2-9F3B-00C04F8ED1D7}')
    _idlflags_ = ['oleautomation']
IRasterModel._methods_ = [
    COMMETHOD(['propput', helpstring(u'The model script.')], HRESULT, 'Script',
              ( ['in'], BSTR, 'rhs' )),
    COMMETHOD([helpstring(u'Binds a symbol to a Raster.')], HRESULT, 'BindRaster',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRaster), 'Raster' ),
              ( ['in'], BSTR, 'Symbol' )),
    COMMETHOD([helpstring(u'Binds a symbol to a FeatureClass.')], HRESULT, 'BindFeatureClass',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'FeatureClass' ),
              ( ['in'], BSTR, 'Symbol' )),
    COMMETHOD([helpstring(u'Binds a symbol to a Table.')], HRESULT, 'BindTable',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable), 'Table' ),
              ( ['in'], BSTR, 'Symbol' )),
    COMMETHOD([helpstring(u'Binds a symbol to a String.')], HRESULT, 'BindString',
              ( ['in'], BSTR, 'strName' ),
              ( ['in'], BSTR, 'Symbol' )),
    COMMETHOD([helpstring(u'Produces a Raster by executing a script.')], HRESULT, 'Execute'),
    COMMETHOD(['propget', helpstring(u'Finds the Raster corresponding to a symbol.')], HRESULT, 'BoundRaster',
              ( ['in'], BSTR, 'Symbol' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRaster)), 'Raster' )),
    COMMETHOD(['propget', helpstring(u'Finds the FeatureClass corresponding to a symbol.')], HRESULT, 'BoundFeatureClass',
              ( ['in'], BSTR, 'Symbol' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass)), 'FeatureClass' )),
    COMMETHOD(['propget', helpstring(u'Finds the Table corresponding to a symbol.')], HRESULT, 'BoundTable',
              ( ['in'], BSTR, 'Symbol' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable)), 'Table' )),
    COMMETHOD(['propget', helpstring(u'Finds the interface pointer corresponding to a symbol.')], HRESULT, 'BoundUnknown',
              ( ['in'], BSTR, 'Symbol' ),
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'whatever' )),
    COMMETHOD([helpstring(u'Unbinds a symbol.')], HRESULT, 'UnbindSymbol',
              ( ['in'], BSTR, 'Symbol' )),
]
################################################################
## code template for IRasterModel implementation
##class IRasterModel_Impl(object):
##    def BindRaster(self, Raster, Symbol):
##        u'Binds a symbol to a Raster.'
##        #return 
##
##    def Execute(self):
##        u'Produces a Raster by executing a script.'
##        #return 
##
##    @property
##    def BoundFeatureClass(self, Symbol):
##        u'Finds the FeatureClass corresponding to a symbol.'
##        #return FeatureClass
##
##    @property
##    def BoundRaster(self, Symbol):
##        u'Finds the Raster corresponding to a symbol.'
##        #return Raster
##
##    def _set(self, rhs):
##        u'The model script.'
##    Script = property(fset = _set, doc = _set.__doc__)
##
##    def BindString(self, strName, Symbol):
##        u'Binds a symbol to a String.'
##        #return 
##
##    @property
##    def BoundTable(self, Symbol):
##        u'Finds the Table corresponding to a symbol.'
##        #return Table
##
##    def UnbindSymbol(self, Symbol):
##        u'Unbinds a symbol.'
##        #return 
##
##    def BindTable(self, Table, Symbol):
##        u'Binds a symbol to a Table.'
##        #return 
##
##    @property
##    def BoundUnknown(self, Symbol):
##        u'Finds the interface pointer corresponding to a symbol.'
##        #return whatever
##
##    def BindFeatureClass(self, FeatureClass, Symbol):
##        u'Binds a symbol to a FeatureClass.'
##        #return 
##

class IRasterOpBase(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Interface of RasterOpBase object'
    _iid_ = GUID('{3A6957FC-A3F2-4A62-99DA-5362833777F3}')
    _idlflags_ = ['oleautomation']
IRasterOpBase._methods_ = [
    COMMETHOD([helpstring(u'Adds an output dataset name to the specified index.')], HRESULT, 'AddOutputDatasetName',
              ( ['in'], c_int, 'index' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetName), 'pOutName' )),
    COMMETHOD(['propputref', helpstring(u'Puts output name array.')], HRESULT, 'OutputDatasetNameArray',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IArray), 'rhs' )),
]
################################################################
## code template for IRasterOpBase implementation
##class IRasterOpBase_Impl(object):
##    def OutputDatasetNameArray(self, rhs):
##        u'Puts output name array.'
##        #return 
##
##    def AddOutputDatasetName(self, index, pOutName):
##        u'Adds an output dataset name to the specified index.'
##        #return 
##

class MLClassifyFunctionArguments(CoClass):
    u'The ML classification function arguments.'
    _reg_clsid_ = GUID('{C1570587-E9EA-43CC-B938-545B1EF289FE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5C54042B-B2ED-4889-8C40-2D89C19DB41D}', 10, 2)
class IMLClassifyFunctionArguments(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control ML classification function arguments.'
    _iid_ = GUID('{469A6FE2-0BBB-411B-BE0C-4BF2BA4D6346}')
    _idlflags_ = ['oleautomation']
MLClassifyFunctionArguments._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._8F0541A3_D5BE_4B3F_A8D9_062D5579E19B_0_10_2.IRasterFunctionArguments, comtypes.gen._8F0541A3_D5BE_4B3F_A8D9_062D5579E19B_0_10_2.IRasterFunctionArguments2, IMLClassifyFunctionArguments, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLVersionSupport]

class IGeoAnalysisSemiVariogram(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Interpolation semi-variogram object.'
    _iid_ = GUID('{4606F15F-B47D-11D2-9F3B-00C04F8ED1D7}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriGeoAnalysisSemiVariogramEnum'
esriGeoAnalysisNoneVariogram = 1
esriGeoAnalysisSphericalSemiVariogram = 2
esriGeoAnalysisCircularSemiVariogram = 3
esriGeoAnalysisExponentialSemiVariogram = 4
esriGeoAnalysisGaussianSemiVariogram = 5
esriGeoAnalysisLinearSemiVariogram = 6
esriGeoAnalysisUniversal1SemiVariogram = 7
esriGeoAnalysisUniversal2SemiVariogram = 8
esriGeoAnalysisSemiVariogramEnum = c_int # enum
IGeoAnalysisSemiVariogram._methods_ = [
    COMMETHOD([helpstring(u'Define Variogram.')], HRESULT, 'DefineVariogram',
              ( ['in'], esriGeoAnalysisSemiVariogramEnum, 'Type' ),
              ( ['in'], c_double, 'aRange' ),
              ( ['in'], c_double, 'sill' ),
              ( ['in'], c_double, 'aNugget' )),
    COMMETHOD(['propput', helpstring(u'Variogram Type.')], HRESULT, 'VariogramType',
              ( ['in'], esriGeoAnalysisSemiVariogramEnum, 'Type' )),
    COMMETHOD(['propget', helpstring(u'Variogram Type.')], HRESULT, 'VariogramType',
              ( ['retval', 'out'], POINTER(esriGeoAnalysisSemiVariogramEnum), 'Type' )),
    COMMETHOD(['propget', helpstring(u'Range value.')], HRESULT, 'Range',
              ( ['retval', 'out'], POINTER(c_double), 'Range' )),
    COMMETHOD(['propget', helpstring(u'Nugget value.')], HRESULT, 'Nugget',
              ( ['retval', 'out'], POINTER(c_double), 'Nugget' )),
    COMMETHOD(['propget', helpstring(u'Partial Sill value.')], HRESULT, 'PartialSill',
              ( ['retval', 'out'], POINTER(c_double), 'sill' )),
    COMMETHOD(['propput', helpstring(u'Lag value.')], HRESULT, 'Lag',
              ( ['in'], c_double, 'Lag' )),
    COMMETHOD(['propget', helpstring(u'Lag value.')], HRESULT, 'Lag',
              ( ['retval', 'out'], POINTER(c_double), 'Lag' )),
]
################################################################
## code template for IGeoAnalysisSemiVariogram implementation
##class IGeoAnalysisSemiVariogram_Impl(object):
##    def _get(self):
##        u'Variogram Type.'
##        #return Type
##    def _set(self, Type):
##        u'Variogram Type.'
##    VariogramType = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Nugget(self):
##        u'Nugget value.'
##        #return Nugget
##
##    def DefineVariogram(self, Type, aRange, sill, aNugget):
##        u'Define Variogram.'
##        #return 
##
##    def _get(self):
##        u'Lag value.'
##        #return Lag
##    def _set(self, Lag):
##        u'Lag value.'
##    Lag = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def PartialSill(self):
##        u'Partial Sill value.'
##        #return sill
##
##    @property
##    def Range(self):
##        u'Range value.'
##        #return Range
##

class IRasterNeighborhood2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to additional members that control the analytical region used when performing neighborhood analsis.'
    _iid_ = GUID('{FDD19DA5-0881-4D0A-B7DD-9A7C3EC24702}')
    _idlflags_ = ['oleautomation']
IRasterNeighborhood2._methods_ = [
    COMMETHOD([helpstring(u'Sets a default neighborhood object.')], HRESULT, 'SetDefault'),
    COMMETHOD([helpstring(u'Sets an annulus neighborhood object.')], HRESULT, 'SetAnnulus',
              ( ['in'], c_double, 'innerRadius' ),
              ( ['in'], c_double, 'outerRadius' ),
              ( ['in'], esriGeoAnalysisUnitsEnum, 'unitsType' )),
    COMMETHOD([helpstring(u'Sets a circle neighborhood object.')], HRESULT, 'SetCircle',
              ( ['in'], c_double, 'radius' ),
              ( ['in'], esriGeoAnalysisUnitsEnum, 'unitsType' )),
    COMMETHOD([helpstring(u'Sets a neighborhood object each of whose entries can be turned on or off.')], HRESULT, 'SetIrregular',
              ( ['in'], c_int, 'height' ),
              ( ['in'], c_int, 'width' ),
              ( ['in'], POINTER(VARIANT), 'entryValues' )),
    COMMETHOD([helpstring(u'Sets a rectangle neighborhood object.')], HRESULT, 'SetRectangle',
              ( ['in'], c_double, 'width' ),
              ( ['in'], c_double, 'height' ),
              ( ['in'], esriGeoAnalysisUnitsEnum, 'unitsType' )),
    COMMETHOD([helpstring(u'Sets a wedge neighborhood object.')], HRESULT, 'SetWedge',
              ( ['in'], c_double, 'radius' ),
              ( ['in'], c_double, 'startAngle' ),
              ( ['in'], c_double, 'endAngle' ),
              ( ['in'], esriGeoAnalysisUnitsEnum, 'unitsType' )),
    COMMETHOD([helpstring(u'Sets a neighborhood object each of whose entries can be assigned a weight.')], HRESULT, 'SetWeight',
              ( ['in'], c_int, 'height' ),
              ( ['in'], c_int, 'width' ),
              ( ['in'], POINTER(VARIANT), 'entryValues' )),
    COMMETHOD([helpstring(u'Sets a 3 x 3 high-pass filter neighborhood.')], HRESULT, 'SetHighPassFilter'),
    COMMETHOD([helpstring(u'Sets a 3 x 3 low-pass filter neighborhood.')], HRESULT, 'SetLowPassFilter'),
    COMMETHOD([helpstring(u'Sets an irregular neighborhood by a file.')], HRESULT, 'SetIrregularFile',
              ( ['in'], BSTR, 'fileName' )),
    COMMETHOD([helpstring(u'Sets a weight neighborhood by a file.')], HRESULT, 'SetWeightFile',
              ( ['in'], BSTR, 'fileName' )),
]
################################################################
## code template for IRasterNeighborhood2 implementation
##class IRasterNeighborhood2_Impl(object):
##    def SetIrregular(self, height, width, entryValues):
##        u'Sets a neighborhood object each of whose entries can be turned on or off.'
##        #return 
##
##    def SetIrregularFile(self, fileName):
##        u'Sets an irregular neighborhood by a file.'
##        #return 
##
##    def SetDefault(self):
##        u'Sets a default neighborhood object.'
##        #return 
##
##    def SetHighPassFilter(self):
##        u'Sets a 3 x 3 high-pass filter neighborhood.'
##        #return 
##
##    def SetWeightFile(self, fileName):
##        u'Sets a weight neighborhood by a file.'
##        #return 
##
##    def SetWedge(self, radius, startAngle, endAngle, unitsType):
##        u'Sets a wedge neighborhood object.'
##        #return 
##
##    def SetAnnulus(self, innerRadius, outerRadius, unitsType):
##        u'Sets an annulus neighborhood object.'
##        #return 
##
##    def SetCircle(self, radius, unitsType):
##        u'Sets a circle neighborhood object.'
##        #return 
##
##    def SetWeight(self, height, width, entryValues):
##        u'Sets a neighborhood object each of whose entries can be assigned a weight.'
##        #return 
##
##    def SetRectangle(self, width, height, unitsType):
##        u'Sets a rectangle neighborhood object.'
##        #return 
##
##    def SetLowPassFilter(self):
##        u'Sets a 3 x 3 low-pass filter neighborhood.'
##        #return 
##


# values for enumeration 'esriRasterVerifyEnum'
esriRasterVerifyOff = 1
esriRasterVerifyOn = 2
esriRasterVerifyError = 3
esriRasterVerifyEnum = c_int # enum
class ITransformationOp(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the transformation operations.'
    _iid_ = GUID('{640E4DB6-F223-11D3-A07F-00C04F68E699}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriGeoAnalysisResampleEnum'
esriGeoAnalysisResampleNearest = 1
esriGeoAnalysisResampleBilinear = 2
esriGeoAnalysisResampleCubic = 3
esriGeoAnalysisResampleSearch = 4
esriGeoAnalysisResampleEnum = c_int # enum
ITransformationOp._methods_ = [
    COMMETHOD([helpstring(u'Flips a raster along the horizontal axis.')], HRESULT, 'Flip',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'GeoDataset' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
    COMMETHOD([helpstring(u'Mirrors a raster along the vertical axis.')], HRESULT, 'Mirror',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'GeoDataset' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
    COMMETHOD([helpstring(u'Shifts the coordinates of a raster.')], HRESULT, 'Shift',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'GeoDataset' ),
              ( ['in'], c_double, 'xShift' ),
              ( ['in'], c_double, 'yShift' ),
              ( ['in'], POINTER(VARIANT), 'pSnapRasterData' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
    COMMETHOD([helpstring(u'Scales the coordinates of a raster.')], HRESULT, 'ReScale',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'inData' ),
              ( ['in'], c_double, 'xScale' ),
              ( ['in'], c_double, 'yScale' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outDataSet' )),
    COMMETHOD([helpstring(u'Rotates a raster around a point by a specified angle.')], HRESULT, 'Rotate',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'GeoDataset' ),
              ( ['in'], esriGeoAnalysisResampleEnum, 'resampleType' ),
              ( ['in'], c_double, 'angle' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'origin' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
    COMMETHOD([helpstring(u'Subsets a raster using a rectangle.')], HRESULT, 'Clip',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'GeoDataset' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'Rectangle' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
    COMMETHOD([helpstring(u'Resamples raster to a new cell size.')], HRESULT, 'Resample',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'GeoDataset' ),
              ( ['in'], c_double, 'newCellsize' ),
              ( ['in'], esriGeoAnalysisResampleEnum, 'resampleType' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
    COMMETHOD([helpstring(u'Transforms a raster along a set of links using a polynomial transformation.')], HRESULT, 'Warp',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'GeoDataset' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPointCollection), 'sourceControlPoints' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPointCollection), 'targetControlPoints' ),
              ( ['in'], comtypes.gen._8F0541A3_D5BE_4B3F_A8D9_062D5579E19B_0_10_2.esriGeoTransTypeEnum, 'transformType' ),
              ( ['in'], esriGeoAnalysisResampleEnum, 'resampleType' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
    COMMETHOD(['restricted', helpstring(u'Converts a raster between two coordinate systems with the option of method.')], HRESULT, 'Project',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'GeoDataset' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference), 'newSpatialReference' ),
              ( ['in'], esriGeoAnalysisResampleEnum, 'resampleType' ),
              ( ['in'], comtypes.gen._8F0541A3_D5BE_4B3F_A8D9_062D5579E19B_0_10_2.esriRasterPrjMethodTypeEnum, 'PrjMethodType' ),
              ( ['in'], comtypes.gen._8F0541A3_D5BE_4B3F_A8D9_062D5579E19B_0_10_2.esriGeoTransTypeEnum, 'transformType' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'blocksize' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'CellSize' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
    COMMETHOD([helpstring(u'Converts a raster between two coordinate systems on region bases.')], HRESULT, 'ProjectFast',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'GeoDataset' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference), 'newSpatialReference' ),
              ( ['in'], esriGeoAnalysisResampleEnum, 'resampleType' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'CellSize' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
    COMMETHOD([helpstring(u'Creates one raster from two or more adjacent rasters and makes a smooth transition over the overlapping areas of the neighboring rasters.')], HRESULT, 'Mosaic',
              ( ['in'], POINTER(comtypes.gen._8F0541A3_D5BE_4B3F_A8D9_062D5579E19B_0_10_2.IRasterBandCollection), 'collectionOfRasters' ),
              ( ['in'], comtypes.gen._8F0541A3_D5BE_4B3F_A8D9_062D5579E19B_0_10_2.rstMosaicOperatorType, 'MosaicType' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
]
################################################################
## code template for ITransformationOp implementation
##class ITransformationOp_Impl(object):
##    def Resample(self, GeoDataset, newCellsize, resampleType):
##        u'Resamples raster to a new cell size.'
##        #return outGeoDataset
##
##    def Rotate(self, GeoDataset, resampleType, angle, origin):
##        u'Rotates a raster around a point by a specified angle.'
##        #return outGeoDataset
##
##    def Clip(self, GeoDataset, Rectangle):
##        u'Subsets a raster using a rectangle.'
##        #return outGeoDataset
##
##    def ReScale(self, inData, xScale, yScale):
##        u'Scales the coordinates of a raster.'
##        #return outDataSet
##
##    def Shift(self, GeoDataset, xShift, yShift, pSnapRasterData):
##        u'Shifts the coordinates of a raster.'
##        #return outGeoDataset
##
##    def Flip(self, GeoDataset):
##        u'Flips a raster along the horizontal axis.'
##        #return outGeoDataset
##
##    def Warp(self, GeoDataset, sourceControlPoints, targetControlPoints, transformType, resampleType):
##        u'Transforms a raster along a set of links using a polynomial transformation.'
##        #return outGeoDataset
##
##    def Project(self, GeoDataset, newSpatialReference, resampleType, PrjMethodType, transformType, blocksize, CellSize):
##        u'Converts a raster between two coordinate systems with the option of method.'
##        #return outGeoDataset
##
##    def Mosaic(self, collectionOfRasters, MosaicType):
##        u'Creates one raster from two or more adjacent rasters and makes a smooth transition over the overlapping areas of the neighboring rasters.'
##        #return outGeoDataset
##
##    def Mirror(self, GeoDataset):
##        u'Mirrors a raster along the vertical axis.'
##        #return outGeoDataset
##
##    def ProjectFast(self, GeoDataset, newSpatialReference, resampleType, CellSize):
##        u'Converts a raster between two coordinate systems on region bases.'
##        #return outGeoDataset
##

class ISurfaceOp(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Surface Operation.'
    _iid_ = GUID('{4606F164-B47D-11D2-9F3B-00C04F8ED1D7}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriGeoAnalysisSlopeEnum'
esriGeoAnalysisSlopeDegrees = 1
esriGeoAnalysisSlopePercentrise = 2
esriGeoAnalysisSlopeEnum = c_int # enum

# values for enumeration 'esriGeoAnalysisVisibilityEnum'
esriGeoAnalysisVisibilityFrequency = 1
esriGeoAnalysisVisibilityObservers = 2
esriGeoAnalysisVisibilityFrequencyUseCurvature = 3
esriGeoAnalysisVisibilityObserversUseCurvature = 4
esriGeoAnalysisVisibilityEnum = c_int # enum
ISurfaceOp._methods_ = [
    COMMETHOD([helpstring(u'Calculates Hillshade.')], HRESULT, 'HillShade',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'GeoDataset' ),
              ( ['in'], c_double, 'azimuth' ),
              ( ['in'], c_double, 'altitude' ),
              ( ['in'], VARIANT_BOOL, 'inModelShadows' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'zFactor' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
    COMMETHOD([helpstring(u'Calculates Slope.')], HRESULT, 'Slope',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'GeoDataset' ),
              ( ['in'], esriGeoAnalysisSlopeEnum, 'slopeType' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'zFactor' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
    COMMETHOD([helpstring(u'Calculates Aspect.')], HRESULT, 'Aspect',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'GeoDataset' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
    COMMETHOD([helpstring(u'Calculates cut and fill areas.')], HRESULT, 'CutFill',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'beforeGeoDataset' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'afterGeoDataset' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'zFactor' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
    COMMETHOD([helpstring(u'Calculates curvature, optionally including profile and plan curvature.')], HRESULT, 'Curvature',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'GeoDataset' ),
              ( ['in'], VARIANT_BOOL, 'profile' ),
              ( ['in'], VARIANT_BOOL, 'plan' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
    COMMETHOD([helpstring(u'Creates contours or isolines based off of a constant interval from a base contour.')], HRESULT, 'Contour',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'GeoDataset' ),
              ( ['in'], c_double, 'interval' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'base' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
    COMMETHOD([helpstring(u'Creates contours or isolines based off a list of contour values.')], HRESULT, 'ContourList',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'GeoDataset' ),
              ( ['in'], POINTER(VARIANT), 'contoursArray' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
    COMMETHOD([helpstring(u'Creates multiple contours or isolines that pass through specified points on a surface.')], HRESULT, 'ContoursAsPolylines',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'GeoDataset' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPointCollection), 'inputPoints' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometryCollection)), 'contourLines' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPointCollection)), 'outputPointsWithElevations' )),
    COMMETHOD([helpstring(u'Creates a single contour or isoline that passes through a specified point on a surface.')], HRESULT, 'ContourAsPolyline',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'GeoDataset' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'inputPoint' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPolyline)), 'contourLine' ),
              ( ['out'], POINTER(c_double), 'elevation' )),
    COMMETHOD([helpstring(u'Performs visibility analysis on a surface based on a set of input observation points.')], HRESULT, 'Visibility',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'GeoDataset' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'observers' ),
              ( ['in'], esriGeoAnalysisVisibilityEnum, 'visType' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
]
################################################################
## code template for ISurfaceOp implementation
##class ISurfaceOp_Impl(object):
##    def Slope(self, GeoDataset, slopeType, zFactor):
##        u'Calculates Slope.'
##        #return outGeoDataset
##
##    def HillShade(self, GeoDataset, azimuth, altitude, inModelShadows, zFactor):
##        u'Calculates Hillshade.'
##        #return outGeoDataset
##
##    def ContourList(self, GeoDataset, contoursArray):
##        u'Creates contours or isolines based off a list of contour values.'
##        #return outGeoDataset
##
##    def ContourAsPolyline(self, GeoDataset, inputPoint):
##        u'Creates a single contour or isoline that passes through a specified point on a surface.'
##        #return contourLine, elevation
##
##    def Curvature(self, GeoDataset, profile, plan):
##        u'Calculates curvature, optionally including profile and plan curvature.'
##        #return outGeoDataset
##
##    def ContoursAsPolylines(self, GeoDataset, inputPoints):
##        u'Creates multiple contours or isolines that pass through specified points on a surface.'
##        #return contourLines, outputPointsWithElevations
##
##    def Visibility(self, GeoDataset, observers, visType):
##        u'Performs visibility analysis on a surface based on a set of input observation points.'
##        #return outGeoDataset
##
##    def Aspect(self, GeoDataset):
##        u'Calculates Aspect.'
##        #return outGeoDataset
##
##    def CutFill(self, beforeGeoDataset, afterGeoDataset, zFactor):
##        u'Calculates cut and fill areas.'
##        #return outGeoDataset
##
##    def Contour(self, GeoDataset, interval, base):
##        u'Creates contours or isolines based off of a constant interval from a base contour.'
##        #return outGeoDataset
##

class IGridTableOp(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that performs grid VAT operations.'
    _iid_ = GUID('{6171288B-7D1C-4328-9160-F39EBF7D542F}')
    _idlflags_ = ['oleautomation']
IGridTableOp._methods_ = [
    COMMETHOD([helpstring(u'Add a field to the fields collection.')], HRESULT, 'AddField',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRasterDataset), 'inputGrid' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IField), 'Field' )),
    COMMETHOD([helpstring(u'Delete a field from the fields collection.')], HRESULT, 'DeleteField',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRasterDataset), 'inputGrid' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IField), 'Field' )),
    COMMETHOD([helpstring(u'Returns a cursor that can be used to update Rows selected by the specified query.')], HRESULT, 'Update',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRasterDataset), 'inputGrid' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IQueryFilter), 'QueryFilter' ),
              ( ['in'], VARIANT_BOOL, 'recycling' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ICursor)), 'cursor' )),
]
################################################################
## code template for IGridTableOp implementation
##class IGridTableOp_Impl(object):
##    def DeleteField(self, inputGrid, Field):
##        u'Delete a field from the fields collection.'
##        #return 
##
##    def Update(self, inputGrid, QueryFilter, recycling):
##        u'Returns a cursor that can be used to update Rows selected by the specified query.'
##        #return cursor
##
##    def AddField(self, inputGrid, Field):
##        u'Add a field to the fields collection.'
##        #return 
##

class NumberRemap(CoClass):
    u'GeoAnalyst Number remap object.'
    _reg_clsid_ = GUID('{2B1E876C-0BE8-11D4-80D6-00C04FA0702C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5C54042B-B2ED-4889-8C40-2D89C19DB41D}', 10, 2)
NumberRemap._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRemap, INumberRemap, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

class IRasterImportOp2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to additional members that control the import of raster formats.'
    _iid_ = GUID('{A0C91FCD-43F4-4A9B-8541-FAB77B038C83}')
    _idlflags_ = ['oleautomation']
IRasterImportOp2._methods_ = [
    COMMETHOD([helpstring(u'Imports a USGS DEM file into a RasterDataset.')], HRESULT, 'ImportFromUSGSDEM',
              ( ['in'], BSTR, 'demFile' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspace), 'OutWorkspace' ),
              ( ['in'], BSTR, 'outRasterName' ),
              ( ['in'], BSTR, 'OutRasterFormat' ),
              ( ['in'], VARIANT_BOOL, 'isInteger' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'zFactor' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRasterDataset)), 'ppOut' )),
    COMMETHOD([helpstring(u'Imports a GRID ASCII file into a RasterDataset.')], HRESULT, 'ImportFromASCII',
              ( ['in'], BSTR, 'asciiFile' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspace), 'OutWorkspace' ),
              ( ['in'], BSTR, 'outRasterName' ),
              ( ['in'], BSTR, 'OutRasterFormat' ),
              ( ['in'], VARIANT_BOOL, 'isInteger' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRasterDataset)), 'ppOut' )),
    COMMETHOD([helpstring(u'Imports a Float GRID file into a RasterDataset.')], HRESULT, 'ImportFromFLOAT',
              ( ['in'], BSTR, 'floatFile' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspace), 'OutWorkspace' ),
              ( ['in'], BSTR, 'outRasterName' ),
              ( ['in'], BSTR, 'OutRasterFormat' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRasterDataset)), 'ppOut' )),
]
################################################################
## code template for IRasterImportOp2 implementation
##class IRasterImportOp2_Impl(object):
##    def ImportFromFLOAT(self, floatFile, OutWorkspace, outRasterName, OutRasterFormat):
##        u'Imports a Float GRID file into a RasterDataset.'
##        #return ppOut
##
##    def ImportFromUSGSDEM(self, demFile, OutWorkspace, outRasterName, OutRasterFormat, isInteger, zFactor):
##        u'Imports a USGS DEM file into a RasterDataset.'
##        #return ppOut
##
##    def ImportFromASCII(self, asciiFile, OutWorkspace, outRasterName, OutRasterFormat, isInteger):
##        u'Imports a GRID ASCII file into a RasterDataset.'
##        #return ppOut
##

class IFeatureClassDescriptor(IGeoDataDescriptor):
    _case_insensitive_ = True
    u'Provides access to members that control the FeatureClass descriptor.'
    _iid_ = GUID('{3297E9CE-93A1-11D2-9F33-00C04F8ED1D7}')
    _idlflags_ = ['oleautomation']
IFeatureClassDescriptor._methods_ = [
    COMMETHOD([helpstring(u'Creates a FeatureClass descriptor.')], HRESULT, 'Create',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'FeatureClass' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IQueryFilter), 'filter' ),
              ( ['in'], BSTR, 'FieldName' )),
    COMMETHOD(['propget', helpstring(u'The FeatureClass in the descriptor.')], HRESULT, 'FeatureClass',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass)), 'FeatureClass' )),
]
################################################################
## code template for IFeatureClassDescriptor implementation
##class IFeatureClassDescriptor_Impl(object):
##    def Create(self, FeatureClass, filter, FieldName):
##        u'Creates a FeatureClass descriptor.'
##        #return 
##
##    @property
##    def FeatureClass(self):
##        u'The FeatureClass in the descriptor.'
##        #return FeatureClass
##


# values for enumeration 'esriSpatialAnalystError'
E_SPATIAL_ANALYST_UNKNOWN_ERROR = -2147217408
E_SPATIAL_ANALYST_FILE_NOT_FOUND = -2147217407
E_SPATIAL_ANALYST_FILE_INVALID_EXTENSION = -2147217406
E_SPATIAL_ANALYST_RENDERER_INVALID_BAND_INDEX = -2147217405
E_SPATIAL_ANALYST_FILE_FAILED_TO_RENAME = -2147217404
E_SPATIAL_ANALYST_FILE_FAILED_TO_COPY = -2147217403
GRID_ERR_ARGTYPE = -2147217402
GRID_ERR_GRIDORNUMB = -2147217401
GRID_ERR_OBJTYPE = -2147217400
GRID_ERR_ZONEOBJ = -2147217400
GRID_ERR_SORTTYPE = -2147217398
GRID_ERR_SHAPETYPE = -2147217397
GRID_ERR_SLICETYPE = -2147217396
GRID_ERR_FIELDTYPE = -2147217395
GRID_ERR_NOTVALUEFD = -2147217394
GRID_ERR_NOVAT = -2147217393
GRID_ERR_BADSTA = -2147217392
GRID_ERR_READTABLE = -2147217391
GRID_ERR_READSTA = -2147217390
GRID_ERR_READVAT = -2147217389
GRID_ERR_READVTAB = -2147217388
GRID_ERR_ALLOCMEM = -2147217387
GRID_ERR_ALLOCLUT = -2147217386
GRID_ERR_CELLSIZE = -2147217385
GRID_ERR_CSIZETYPE = -2147217384
GRID_ERR_LUTRANGE = -2147217383
GRID_ERR_MAKEHASH = -2147217382
GRID_ERR_MAKEVTAB = -2147217381
GRID_ERR_LISTELEM = -2147217380
GRID_ERR_STRGRID = -2147217379
GRID_ERR_LEGCLASS = -2147217378
GRID_ERR_INFODIR = -2147217377
GRID_ERR_SEMIVARIO = -2147217376
GRID_ERR_CONTINUE = -2147217375
GRID_ERR_TIMEOUT = -2147217374
GRID_ERR_HASERR = -2147217373
GRID_ERR_LOADFAIL = -2147217372
GRID_ERR_NOLIBINIT = -2147217371
GRID_ERR_NOLIBEXIT = -2147217370
GRID_ERR_NOIRREGNBR = -2147217369
GRID_ERR_MISMATCHSPREF = -2147217368
E_SPATIAL_ANALYST_TREND_FIELD = -2147217367
E_SPATIAL_ANALYST_CONVERSION = -2147217366
E_SPATIAL_ANALYST_OPEN_WORKSPACE = -2147217365
E_SPATIAL_ANALYST_NO_FEATURE_CLASS = -2147217364
E_SPATIAL_ANALYST_NO_FIELD_NAME = -2147217363
E_SPATIAL_ANALYST_EVAL_TYPE = -2147217362
E_SPATIAL_ANALYST_NO_POINTS = -2147217361
E_SPATIAL_ANALYST_INVALID_RECLASS_FIELD = -2147217360
E_SPATIAL_ANALYST_FILE_FAILED_TO_WRITE = -2147217359
E_SPATIAL_ANALYST_INVALID_READ_INDEX = -2147217358
E_SPATIAL_ANALYST_INVALID_DELETE_INDEX = -2147217357
E_SPATIAL_ANALYST_TABLE_NOT_CREATED = -2147217356
E_SPATIAL_ANALYST_NO_DUPLICATES = -2147217355
E_SPATIAL_ANALYST_NO_CONVERTTOCOVERAGE = -2147217354
E_SPATIAL_ANALYST_NOT_FEATURE_CLASS = -2147217353
E_SPATIAL_ANALYST_NULL_OBJECT = -2147217352
E_SPATIAL_ANALYST_RECLASS_BY_SELECT = -2147217351
E_SPATIAL_ANALYST_FEAT_SEARCH_CURSOR = -2147217350
E_SPATIAL_ANALYST_EXTRACT_VARARR = -2147217349
E_SPATIAL_ANALYST_UNBIND_RASTER = -2147217348
E_SPATIAL_ANALYST_UNARY_OPERATION = -2147217347
E_SPATIAL_ANALYST_BINARY_OPERATION = -2147217346
E_SPATIAL_ANALYST_INVALID_FILTER_TYPE = -2147217345
E_SPATIAL_ANALYST_STRING_FIELD_NOT_ALLOWED = -2147217344
E_SPATIAL_ANALYST_BAD_FIELD_INDEX = -2147217343
E_SPATIAL_ANALYST_INVALID_GEOMETRY = -2147217342
E_SPATIAL_ANALYST_OPEN_RDS_FAIL = -2147217341
E_SPATIAL_ANALYST_REFERENCE_FAILED = -2147217340
E_SPATIAL_ANALYST_CREATE_WORKSPACENAME = -2147217339
E_SPATIAL_ANALYST_NO_STRING_FIELD = -2147217338
E_SPATIAL_ANALYST_REMAP_MIXED_FILE = -2147217337
E_SPATIAL_ANALYST_REMAP_BAD_SVALUE = -2147217336
E_SPATIAL_ANALYST_REMAP_FILL_SREMAP = -2147217335
E_SPATIAL_ANALYST_REMAP_NEED_STYPE = -2147217334
E_SPATIAL_ANALYST_REMAP_NEED_NTYPE = -2147217333
E_SPATIAL_ANALYST_REMAP_INVALID_FIND_INDEX = -2147217332
E_SPATIAL_ANALYST_REMAP_RECORD_NOT_FOUND = -2147217331
E_SPATIAL_ANALYST_REMAP_OVERLAP_CONFLICT = -2147217330
E_SPATIAL_ANALYST_REMAP_SIMPLE_CONFLICT = -2147217329
E_SPATIAL_ANALYST_REMAP_DUPLICATE_RECORD = -2147217328
E_SPATIAL_ANALYST_REMAP_FREE_RECORDS = -2147217327
E_SPATIAL_ANALYST_INVALID_NAME_FROM_PATH = -2147217326
E_SPATIAL_ANALYST_OUTPUT_EXISTS = -2147217325
E_SPATIAL_ANALYST_SAVEAS = -2147217324
E_SPATIAL_ANALYST_NO_SPREF = -2147217323
E_SPATIAL_ANALYST_NO_EXTENT = -2147217322
E_SPATIAL_ANALYST_NO_EVALEXP = -2147217321
E_SPATIAL_ANALYST_NOT_EVALUATED = -2147217320
E_SPATIAL_ANALYST_ADDITEM_FAILED = -2147217319
E_SPATIAL_ANALYST_NO_DATASET = -2147217318
E_SPATIAL_ANALYST_SAVEAS_FAILED = -2147217317
E_SPATIAL_ANALYST_NOT_INTEGER = -2147217316
E_SPATIAL_ANALYST_NO_POINT_FILE = -2147217315
E_SPATIAL_ANALYST_CREATE_GRID = -2147217314
E_SPATIAL_ANALYST_ANALYSIS_WINDOW = -2147217313
E_SPATIAL_ANALYST_INIT_SAMPLE_LIST = -2147217312
E_SPATIAL_ANALYST_ESTIMATE_SEMIVAR = -2147217311
E_SPATIAL_ANALYST_WRITE_UNABLE = -2147217310
E_SPATIAL_ANALYST_INVALID_FIELD = -2147217309
E_SPATIAL_ANALYST_INVALID_SEMIVAR_TYPE = -2147217308
E_SPATIAL_ANALYST_COMPOSE_EXPR = -2147217307
E_SPATIAL_ANALYST_FIELD_NOT_ADDED = -2147217306
E_SPATIAL_ANALYST_HIST_FREQUENCY = -2147217305
E_SPATIAL_ANALYST_LICENSENOTAVAILABLE = -2147217304
E_SPATIAL_ANALYST_WASNOTACTIVATED = -2147217303
E_SPATIAL_ANALYST_SHAREDLICENSENOTAVAILABLE = -2147217302
E_SPATIAL_ANALYST_SHAREDWASNOTACTIVATED = -2147217301
E_SPATIAL_ANALYST_EMPTY_RASTER = -2147217300
E_SPATIAL_ANALYST_BIND_SYMBOL_MISMATCH = -2147217299
E_SPATIAL_ANALYST_NULL_FEATURE_COUNT = -2147217298
E_SPATIAL_ANALYST_CANCEL_OP = -2147217297
E_SPATIAL_ANALYST_NODATA_RASTER = -2147217296
E_SPATIAL_ANALYST_INVALID_STATSTYPE = -2147217295
E_SPATIAL_ANALYST_NO_JOINEDFIELD = -2147217294
E_SPATIAL_ANALYST_NO_SUPPORT = -2147217293
E_SPATIAL_ANALYST_INVALID_OUTRFORMAT = -2147217292
E_SPATIAL_ANALYST_INVALID_GEODATASET = -2147217291
E_SPATIAL_ANALYST_INVALID_NAMEFORGRIDENG = -2147217290
E_SPATIAL_ANALYST_NO_BASETABLE = -2147217289
E_SPATIAL_ANALYST_NO_RECS_WITH_QFILTER = -2147217288
E_SPATIAL_ANALYST_INVALID_COMMAND = -2147217287
E_SPATIAL_ANALYST_UNSUPPORTED_FEAT_INPUT = -2147217286
E_SPATIAL_ANALYST_INVALID_PRJS_FOR_CURVATURE = -2147217285
E_SPATIAL_ANALYST_INVALID_BAND_COUNT = -2147217284
E_SPATIAL_ANALYST_NO_FILE_NAME = -2147217283
E_SPATIAL_ANALYST_OUT_FILE_EXISTS = -2147217282
E_SPATIAL_ANALYST_INVALID_REJECT_FRACTION = -2147217281
E_SPATIAL_ANALYST_INVALID_COMPONENT_COUNT = -2147217280
E_SPATIAL_ANALYST_SREMAP_NO_STRING_FIELD = -2147217279
E_SPATIAL_ANALYST_NREMAP_HAS_STRING_FIELD = -2147217278
E_SPATIAL_ANALYST_REMAP_UNSORTED = -2147217277
E_SPATIAL_ANALYST_TOPO_NOT_POSITIVE = -2147217276
E_SPATIAL_ANALYST_TOPO_NOT_NONNEGATIVE = -2147217275
E_SPATIAL_ANALYST_TOPO_UNKNOWN_KEYWORD = -2147217274
E_SPATIAL_ANALYST_TOPO_BAD_CONTOUR_OPTION = -2147217273
E_SPATIAL_ANALYST_TOPO_NO_ELEVDATA = -2147217272
E_SPATIAL_ANALYST_TOPO_MISS_VALUE = -2147217271
E_SPATIAL_ANALYST_TOPO_INVALID_ZLIMITS = -2147217270
E_SPATIAL_ANALYST_NOT_GRID = -2147217269
E_SPATIAL_ANALYST_OBSV_UNSUPPORTED_GEOMETRY = -2147217268
E_SPATIAL_ANALYST_OBSV_EXCESS_POINTS = -2147217267
E_SPATIAL_ANALYST_FIELD_EXISTS = -2147217266
E_SPATIAL_ANALYST_NO_COVERAGE_SUPPORT = -2147217265
E_SPATIAL_ANALYST_RESERVED_FIELD_EXISTS = -2147217264
E_SPATIAL_ANALYST_SIMPLE_POLY_SUPPORT = -2147217263
E_SPATIAL_ANALYST_HDR_FILE_NOT_FOUND = -2147217262
E_SPATIAL_ANALYST_READ_ERROR = -2147217261
E_SPATIAL_ANALYST_TOPO_CONTOUR_TOOMANY_POINTS = -2147217260
E_SPATIAL_ANALYST_TOPO_STREAM_TOOMANY_POINTS = -2147217259
E_SPATIAL_ANALYST_TOPO_BOUND_TOOMANY_POINTS = -2147217258
E_SPATIAL_ANALYST_TOPO_LAKE_TOOMANY_POINTS = -2147217257
E_SPATIAL_ANALYST_GRID_EXECUTE = -2147217256
E_SPATIAL_ANALYST_SYNTAX_ERROR = -2147217255
E_SPATIAL_ANALYST_MEMORY_ALLOC = -2147217254
E_SPATIAL_ANALYST_PRJ_NOTMACTH = -2147217253
E_SPATIAL_ANALYST_PRJ_COPY = -2147217252
E_SPATIAL_ANALYST_NO_ATTRIB_TABLE = -2147217251
E_SPATIAL_ANALYST_INVALID_OUTPUT_EXTENT = -2147217250
E_SPATIAL_ANALYST_EXPRESSION_TOO_LONG = -2147217249
E_SPATIAL_ANALYST_INVALID_NUMERIC_FIELD_LEN = -2147217248
E_SPATIAL_LOCALFUNCTION_ARGUMENTS_OVERSPECIFIED = -2147217247
E_SPATIAL_ANALYST_CANNOT_OBTAIN_STATS = -2147217246
esriSpatialAnalystError = c_int # enum
class RasterRadius(CoClass):
    u'GeoAnalyst Raster radius object.'
    _reg_clsid_ = GUID('{3297E9D2-93A1-11D2-9F33-00C04F8ED1D7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5C54042B-B2ED-4889-8C40-2D89C19DB41D}', 10, 2)
RasterRadius._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRasterRadius, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

class RasterConvertHelper(CoClass):
    u'Raster conversion helper class.'
    _reg_clsid_ = GUID('{DEBD302A-7F6F-11D4-B278-00508BCDC779}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5C54042B-B2ED-4889-8C40-2D89C19DB41D}', 10, 2)
class IRasterConvertHelper(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that convert geodatasets to rasters or feature classes.'
    _iid_ = GUID('{DEBD3029-7F6F-11D4-B278-00508BCDC779}')
    _idlflags_ = ['oleautomation']
RasterConvertHelper._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRasterConvertHelper, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

class IInterpolationOp3(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to additional members that control the Interpolating of a GeoDataset.'
    _iid_ = GUID('{4BC64B50-51EF-4D19-A56D-7C10521DFACE}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriGeoAnalysisSplineEnum'
esriGeoAnalysisTensionSpline = 1
esriGeoAnalysisRegularizedSpline = 2
esriGeoAnalysisSplineEnum = c_int # enum

# values for enumeration 'esriGeoAnalysisTrendEnum'
esriGeoAnalysisLinearTrend = 1
esriGeoAnalysisLogisticTrend = 2
esriGeoAnalysisTrendEnum = c_int # enum
IInterpolationOp3._methods_ = [
    COMMETHOD([helpstring(u'Interpolates using IDW.')], HRESULT, 'IDW',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'geoData' ),
              ( ['in'], c_double, 'power' ),
              ( ['in'], POINTER(IRasterRadius), 'radius' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'barrier' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'GeoDataset' )),
    COMMETHOD([helpstring(u'Interpolates using kriging.')], HRESULT, 'Krige',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'geoData' ),
              ( ['in'], esriGeoAnalysisSemiVariogramEnum, 'semiVariogramType' ),
              ( ['in'], POINTER(IRasterRadius), 'radius' ),
              ( ['in'], VARIANT_BOOL, 'outSemiVariance' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'barrier' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'interpolatedRaster' )),
    COMMETHOD([helpstring(u'Interpolates using Variogram.')], HRESULT, 'Variogram',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'geoData' ),
              ( ['in'], POINTER(IGeoAnalysisSemiVariogram), 'semiVariogram' ),
              ( ['in'], POINTER(IRasterRadius), 'radius' ),
              ( ['in'], VARIANT_BOOL, 'outSemiVariance' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'barrier' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'interpolatedRaster' )),
    COMMETHOD([helpstring(u'Interpolates using splining.')], HRESULT, 'Spline',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'geoData' ),
              ( ['in'], esriGeoAnalysisSplineEnum, 'splineType' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'weight' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'numPoints' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'interpolatedRaster' )),
    COMMETHOD([helpstring(u'Interpolates using trend surface.')], HRESULT, 'Trend',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'geoData' ),
              ( ['in'], esriGeoAnalysisTrendEnum, 'trendType' ),
              ( ['in'], c_int, 'order' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'interpolatedRaster' )),
    COMMETHOD([helpstring(u'Interpolates using natual neighbor.')], HRESULT, 'NaturalNeighbor',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'GeoDataset' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
    COMMETHOD([helpstring(u'Interpolates using AnuDem.')], HRESULT, 'TopoToRasterByFile',
              ( ['in'], BSTR, 'paramFile' ),
              ( ['out', 'optional'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass)), 'outStream' ),
              ( ['out', 'optional'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass)), 'outSink' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRasterDataset)), 'outSurface' )),
    COMMETHOD([helpstring(u'Interpolates using trend surface with optional rms file.')], HRESULT, 'TrendWithRms',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'geoData' ),
              ( ['in'], esriGeoAnalysisTrendEnum, 'trendType' ),
              ( ['in'], c_int, 'order' ),
              ( [], BSTR, 'out_rms_file' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'interpolatedRaster' )),
]
################################################################
## code template for IInterpolationOp3 implementation
##class IInterpolationOp3_Impl(object):
##    def TrendWithRms(self, geoData, trendType, order, out_rms_file):
##        u'Interpolates using trend surface with optional rms file.'
##        #return interpolatedRaster
##
##    def Variogram(self, geoData, semiVariogram, radius, outSemiVariance, barrier):
##        u'Interpolates using Variogram.'
##        #return interpolatedRaster
##
##    def Krige(self, geoData, semiVariogramType, radius, outSemiVariance, barrier):
##        u'Interpolates using kriging.'
##        #return interpolatedRaster
##
##    def Trend(self, geoData, trendType, order):
##        u'Interpolates using trend surface.'
##        #return interpolatedRaster
##
##    def IDW(self, geoData, power, radius, barrier):
##        u'Interpolates using IDW.'
##        #return GeoDataset
##
##    def NaturalNeighbor(self, GeoDataset):
##        u'Interpolates using natual neighbor.'
##        #return outGeoDataset
##
##    def TopoToRasterByFile(self, paramFile):
##        u'Interpolates using AnuDem.'
##        #return outStream, outSink, outSurface
##
##    def Spline(self, geoData, splineType, weight, numPoints):
##        u'Interpolates using splining.'
##        #return interpolatedRaster
##

class GeoAnalysisSemiVariogram(CoClass):
    u'Esri GeoAnalysis SemiVariogram object.'
    _reg_clsid_ = GUID('{E73C39EC-6F70-482C-9CDE-AFF5D4F003E9}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5C54042B-B2ED-4889-8C40-2D89C19DB41D}', 10, 2)
GeoAnalysisSemiVariogram._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGeoAnalysisSemiVariogram, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

class RasterInterpolationOp(CoClass):
    u'Raster interpolation operation class.'
    _reg_clsid_ = GUID('{D3CE7332-9546-11D2-9F34-00C04F8ED1D7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5C54042B-B2ED-4889-8C40-2D89C19DB41D}', 10, 2)
class IGeoAnalysisEnvironment(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the GeoAnalysis environment.'
    _iid_ = GUID('{3297E9C8-93A1-11D2-9F33-00C04F8ED1D7}')
    _idlflags_ = ['oleautomation']
class IRasterAnalysisEnvironment(IGeoAnalysisEnvironment):
    _case_insensitive_ = True
    u'Provides access to members that control the environment for raster analysis.'
    _iid_ = GUID('{3297E9C5-93A1-11D2-9F33-00C04F8ED1D7}')
    _idlflags_ = ['oleautomation']
class IRasterAnalysisGlobalEnvironment(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the global environment for raster analysis.'
    _iid_ = GUID('{5AA98A9D-7F47-4D69-AD97-0FE4893F5DEE}')
    _idlflags_ = ['oleautomation']
class IInterpolationOp(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Interpolating of a GeoDataset.'
    _iid_ = GUID('{D3CE7322-9546-11D2-9F34-00C04F8ED1D7}')
    _idlflags_ = ['oleautomation']
class IInterpolationOp2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to additional members that control the Interpolating of a GeoDataset.'
    _iid_ = GUID('{D91B6722-30A8-4663-B5C5-A3A76C522BAB}')
    _idlflags_ = ['oleautomation']
RasterInterpolationOp._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRasterAnalysisEnvironment, IRasterAnalysisGlobalEnvironment, IRasterOpBase, IInterpolationOp, IInterpolationOp2, IInterpolationOp3, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

class ISurfaceOp2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to additional members that control the Surface Operation.'
    _iid_ = GUID('{1B987743-5EC7-4722-8AE3-15D78AD1DD41}')
    _idlflags_ = ['oleautomation']
ISurfaceOp2._methods_ = [
    COMMETHOD([helpstring(u'Calculates Hillshade.')], HRESULT, 'HillShade',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'GeoDataset' ),
              ( ['in'], c_double, 'azimuth' ),
              ( ['in'], c_double, 'altitude' ),
              ( ['in'], VARIANT_BOOL, 'inModelShadows' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'zFactor' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
    COMMETHOD([helpstring(u'Calculates Slope.')], HRESULT, 'Slope',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'GeoDataset' ),
              ( ['in'], esriGeoAnalysisSlopeEnum, 'slopeType' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'zFactor' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
    COMMETHOD([helpstring(u'Calculates Aspect.')], HRESULT, 'Aspect',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'GeoDataset' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
    COMMETHOD([helpstring(u'Calculates cut and fill areas.')], HRESULT, 'CutFill',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'beforeGeoDataset' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'afterGeoDataset' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'zFactor' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
    COMMETHOD([helpstring(u'Creates contours or isolines based off of a constant interval from a base contour.')], HRESULT, 'Contour',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'GeoDataset' ),
              ( ['in'], c_double, 'interval' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'base' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'zFactor' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
    COMMETHOD([helpstring(u'Calculates curvature, optionally including profile and plan curvature.')], HRESULT, 'Curvature',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'GeoDataset' ),
              ( ['in'], VARIANT_BOOL, 'profile' ),
              ( ['in'], VARIANT_BOOL, 'plan' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'zFactor' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
    COMMETHOD([helpstring(u'Creates contours or isolines based off a list of contour values.')], HRESULT, 'ContourList',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'GeoDataset' ),
              ( ['in'], POINTER(VARIANT), 'contoursArray' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
    COMMETHOD([helpstring(u'Creates multiple contours or isolines that pass through specified points on a surface.')], HRESULT, 'ContoursAsPolylines',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'GeoDataset' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPointCollection), 'inputPoints' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometryCollection)), 'contourLines' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPointCollection)), 'outputPointsWithElevations' )),
    COMMETHOD([helpstring(u'Creates a single contour or isoline that passes through a specified point on a surface.')], HRESULT, 'ContourAsPolyline',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'GeoDataset' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'inputPoint' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPolyline)), 'contourLine' ),
              ( ['out'], POINTER(c_double), 'elevation' )),
    COMMETHOD([helpstring(u'Performs visibility analysis on a surface based on a set of input observation points.')], HRESULT, 'Visibility',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'GeoDataset' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'observers' ),
              ( ['in'], esriGeoAnalysisVisibilityEnum, 'visType' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'pZFactor' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'pRefractivityCoefficient' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
]
################################################################
## code template for ISurfaceOp2 implementation
##class ISurfaceOp2_Impl(object):
##    def Slope(self, GeoDataset, slopeType, zFactor):
##        u'Calculates Slope.'
##        #return outGeoDataset
##
##    def HillShade(self, GeoDataset, azimuth, altitude, inModelShadows, zFactor):
##        u'Calculates Hillshade.'
##        #return outGeoDataset
##
##    def ContourList(self, GeoDataset, contoursArray):
##        u'Creates contours or isolines based off a list of contour values.'
##        #return outGeoDataset
##
##    def ContourAsPolyline(self, GeoDataset, inputPoint):
##        u'Creates a single contour or isoline that passes through a specified point on a surface.'
##        #return contourLine, elevation
##
##    def Curvature(self, GeoDataset, profile, plan, zFactor):
##        u'Calculates curvature, optionally including profile and plan curvature.'
##        #return outGeoDataset
##
##    def ContoursAsPolylines(self, GeoDataset, inputPoints):
##        u'Creates multiple contours or isolines that pass through specified points on a surface.'
##        #return contourLines, outputPointsWithElevations
##
##    def Visibility(self, GeoDataset, observers, visType, pZFactor, pRefractivityCoefficient):
##        u'Performs visibility analysis on a surface based on a set of input observation points.'
##        #return outGeoDataset
##
##    def Aspect(self, GeoDataset):
##        u'Calculates Aspect.'
##        #return outGeoDataset
##
##    def CutFill(self, beforeGeoDataset, afterGeoDataset, zFactor):
##        u'Calculates cut and fill areas.'
##        #return outGeoDataset
##
##    def Contour(self, GeoDataset, interval, base, zFactor):
##        u'Creates contours or isolines based off of a constant interval from a base contour.'
##        #return outGeoDataset
##

class RasterReclassOp(CoClass):
    u'Raster Reclass operation class.'
    _reg_clsid_ = GUID('{FE6EC115-1E85-11D3-9F45-00C04F8ED1D7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5C54042B-B2ED-4889-8C40-2D89C19DB41D}', 10, 2)
RasterReclassOp._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRasterAnalysisEnvironment, IRasterAnalysisGlobalEnvironment, IRasterOpBase, IReclassOp, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]


# values for enumeration 'esriRasterEnvSettingEnum'
esriRasterEnvMaxOf = 1
esriRasterEnvMinOf = 2
esriRasterEnvValue = 3
esriRasterEnvSettingEnum = c_int # enum
class RasterTransformationOp(CoClass):
    u'Esri Transformation operations class.'
    _reg_clsid_ = GUID('{4606F169-B47D-11D2-9F3B-00C04F8ED1D7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5C54042B-B2ED-4889-8C40-2D89C19DB41D}', 10, 2)
class IRasterAnalysisGDBEnvironment(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the environment for Geodatabase raster analysis.'
    _iid_ = GUID('{823763C2-2855-43D2-88CF-321815C17685}')
    _idlflags_ = ['oleautomation']
RasterTransformationOp._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRasterAnalysisEnvironment, IRasterAnalysisGDBEnvironment, IRasterAnalysisGlobalEnvironment, IRasterOpBase, ITransformationOp, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

class RasterMathSupportOp(CoClass):
    u'Raster mathematic support operation class.'
    _reg_clsid_ = GUID('{2EF07B2A-8744-11D4-B278-00508BCDC779}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5C54042B-B2ED-4889-8C40-2D89C19DB41D}', 10, 2)
RasterMathSupportOp._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRasterAnalysisEnvironment, IRasterAnalysisGlobalEnvironment, IRasterOpBase, IMathSupportOp, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

class RasterNeighborhood(CoClass):
    u'Esri Raster neighborhood object.'
    _reg_clsid_ = GUID('{3297E9D1-93A1-11D2-9F33-00C04F8ED1D7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5C54042B-B2ED-4889-8C40-2D89C19DB41D}', 10, 2)
RasterNeighborhood._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRasterNeighborhood, IRasterNeighborhood2, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

class Library(object):
    u'Esri GeoAnalyst Object Library 10.2'
    name = u'esriGeoAnalyst'
    _reg_typelib_ = ('{5C54042B-B2ED-4889-8C40-2D89C19DB41D}', 10, 2)

class GridTableOp(CoClass):
    u'Esri grid VAT operations class.'
    _reg_clsid_ = GUID('{555A5E29-B23D-433A-B189-FFDE5DC03032}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5C54042B-B2ED-4889-8C40-2D89C19DB41D}', 10, 2)
GridTableOp._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRasterAnalysisEnvironment, IRasterAnalysisGlobalEnvironment, IRasterOpBase, IGridTableOp, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

class IRasterDescriptor(IGeoDataDescriptor):
    _case_insensitive_ = True
    u'Provides access to members that control the Raster descriptor.'
    _iid_ = GUID('{296E7F60-D1C8-11D2-9F3C-00C04F8ED1D7}')
    _idlflags_ = ['oleautomation']
IRasterDescriptor._methods_ = [
    COMMETHOD([helpstring(u'Create a Raster descriptor.')], HRESULT, 'Create',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRaster), 'Raster' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IQueryFilter), 'filter' ),
              ( ['in'], BSTR, 'FieldName' )),
    COMMETHOD(['propget', helpstring(u'The Raster in the descriptor.')], HRESULT, 'Raster',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRaster)), 'Raster' )),
]
################################################################
## code template for IRasterDescriptor implementation
##class IRasterDescriptor_Impl(object):
##    @property
##    def Raster(self):
##        u'The Raster in the descriptor.'
##        #return Raster
##
##    def Create(self, Raster, filter, FieldName):
##        u'Create a Raster descriptor.'
##        #return 
##

class RasterConversionOp(CoClass):
    u'Esri raster conversion and import operations class.'
    _reg_clsid_ = GUID('{B857257D-FA9C-11D3-9F65-00C04F8ED1D7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5C54042B-B2ED-4889-8C40-2D89C19DB41D}', 10, 2)
class IConversionOp(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that convert between raster and feature data.'
    _iid_ = GUID('{3297E9CA-93A1-11D2-9F33-00C04F8ED1D7}')
    _idlflags_ = ['oleautomation']
class IRasterImportOp(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the import of raster formats.'
    _iid_ = GUID('{90C52CFE-8E74-11D4-80F4-00C04FA0702C}')
    _idlflags_ = ['oleautomation']
class IRasterExportOp(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the export to raster formats.'
    _iid_ = GUID('{30A4A132-00AC-4F44-BDC6-A020EC43AD37}')
    _idlflags_ = ['oleautomation']
RasterConversionOp._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRasterAnalysisEnvironment, IRasterAnalysisGDBEnvironment, IRasterAnalysisGlobalEnvironment, IRasterOpBase, IConversionOp, IRasterImportOp, IRasterImportOp2, IRasterExportOp, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

class RasterMakerOp(CoClass):
    u'A mechanism for generating rasters.'
    _reg_clsid_ = GUID('{E965D7E7-EBE0-11D3-9F63-00C04F8ED1D7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5C54042B-B2ED-4889-8C40-2D89C19DB41D}', 10, 2)
RasterMakerOp._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRasterAnalysisEnvironment, IRasterAnalysisGlobalEnvironment, IRasterOpBase, IRasterMakerOp, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

IRasterExportOp._methods_ = [
    COMMETHOD([helpstring(u'Exports a raster dataset to a GRID ASCII file.')], HRESULT, 'ExportToASCII',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'dataset' ),
              ( ['in'], BSTR, 'asciiFile' )),
    COMMETHOD([helpstring(u'Exports a raster dataset to a Float GRID file.')], HRESULT, 'ExportToFloat',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'dataset' ),
              ( ['in'], BSTR, 'floatFile' )),
]
################################################################
## code template for IRasterExportOp implementation
##class IRasterExportOp_Impl(object):
##    def ExportToFloat(self, dataset, floatFile):
##        u'Exports a raster dataset to a Float GRID file.'
##        #return 
##
##    def ExportToASCII(self, dataset, asciiFile):
##        u'Exports a raster dataset to a GRID ASCII file.'
##        #return 
##

IGeoAnalysisEnvironment._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The output workspace of GeoAnalysis.')], HRESULT, 'OutWorkspace',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspace), 'Workspace' )),
    COMMETHOD(['propget', helpstring(u'The output workspace of GeoAnalysis.')], HRESULT, 'OutWorkspace',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspace)), 'Workspace' )),
    COMMETHOD(['propputref', helpstring(u'The output spatial reference of GeoAnalysis.')], HRESULT, 'OutSpatialReference',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference), 'SpatialReference' )),
    COMMETHOD(['propget', helpstring(u'The output spatial reference of GeoAnalysis.')], HRESULT, 'OutSpatialReference',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference)), 'SpatialReference' )),
]
################################################################
## code template for IGeoAnalysisEnvironment implementation
##class IGeoAnalysisEnvironment_Impl(object):
##    @property
##    def OutSpatialReference(self, SpatialReference):
##        u'The output spatial reference of GeoAnalysis.'
##        #return 
##
##    @property
##    def OutWorkspace(self, Workspace):
##        u'The output workspace of GeoAnalysis.'
##        #return 
##

IRasterAnalysisEnvironment._methods_ = [
    COMMETHOD([helpstring(u'Sets the type and value of cell size in the RasterAnalysis.')], HRESULT, 'SetCellSize',
              ( ['in'], esriRasterEnvSettingEnum, 'envType' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'cellSizeProvider' )),
    COMMETHOD([helpstring(u'Gets the type and value of cell size in the RasterAnalysis.')], HRESULT, 'GetCellSize',
              ( ['out'], POINTER(esriRasterEnvSettingEnum), 'envType' ),
              ( ['out'], POINTER(c_double), 'CellSize' )),
    COMMETHOD([helpstring(u'Sets the type and values of extent in the RasterAnalysis.')], HRESULT, 'SetExtent',
              ( ['in'], esriRasterEnvSettingEnum, 'envType' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'extentProvider' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'snapRasterData' )),
    COMMETHOD([helpstring(u'Gets the type and values of extent in the RasterAnalysis.')], HRESULT, 'GetExtent',
              ( ['out'], POINTER(esriRasterEnvSettingEnum), 'envType' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'Extent' )),
    COMMETHOD(['propputref', helpstring(u'Mask allows processing to occur only for a selected set of cells.')], HRESULT, 'Mask',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'Mask' )),
    COMMETHOD(['propget', helpstring(u'Mask allows processing to occur only for a selected set of cells.')], HRESULT, 'Mask',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'Mask' )),
    COMMETHOD(['propput', helpstring(u'The verify type of the RasterAnalysis.')], HRESULT, 'VerifyType',
              ( ['in'], esriRasterVerifyEnum, 'VerifyType' )),
    COMMETHOD(['propget', helpstring(u'The verify type of the RasterAnalysis.')], HRESULT, 'VerifyType',
              ( ['retval', 'out'], POINTER(esriRasterVerifyEnum), 'VerifyType' )),
    COMMETHOD(['propget', helpstring(u'The default output raster prefix.')], HRESULT, 'DefaultOutputRasterPrefix',
              ( ['retval', 'out'], POINTER(BSTR), 'rasterPrefix' )),
    COMMETHOD(['propput', helpstring(u'The default output raster prefix.')], HRESULT, 'DefaultOutputRasterPrefix',
              ( ['in'], BSTR, 'rasterPrefix' )),
    COMMETHOD(['propget', helpstring(u'The default output vector prefix.')], HRESULT, 'DefaultOutputVectorPrefix',
              ( ['retval', 'out'], POINTER(BSTR), 'vectorPrefix' )),
    COMMETHOD(['propput', helpstring(u'The default output vector prefix.')], HRESULT, 'DefaultOutputVectorPrefix',
              ( ['in'], BSTR, 'vectorPrefix' )),
    COMMETHOD([helpstring(u'Sets the raster analysis environment of the object as new default environment.')], HRESULT, 'SetAsNewDefaultEnvironment'),
    COMMETHOD([helpstring(u'Restores to the previous default raster analysis environment.')], HRESULT, 'RestoreToPreviousDefaultEnvironment'),
    COMMETHOD([helpstring(u'Remove all previously stored default rasteranalysis environments.')], HRESULT, 'Reset'),
]
################################################################
## code template for IRasterAnalysisEnvironment implementation
##class IRasterAnalysisEnvironment_Impl(object):
##    def GetCellSize(self):
##        u'Gets the type and value of cell size in the RasterAnalysis.'
##        #return envType, CellSize
##
##    def Reset(self):
##        u'Remove all previously stored default rasteranalysis environments.'
##        #return 
##
##    def RestoreToPreviousDefaultEnvironment(self):
##        u'Restores to the previous default raster analysis environment.'
##        #return 
##
##    def _get(self):
##        u'The default output vector prefix.'
##        #return vectorPrefix
##    def _set(self, vectorPrefix):
##        u'The default output vector prefix.'
##    DefaultOutputVectorPrefix = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Mask(self, Mask):
##        u'Mask allows processing to occur only for a selected set of cells.'
##        #return 
##
##    def SetCellSize(self, envType, cellSizeProvider):
##        u'Sets the type and value of cell size in the RasterAnalysis.'
##        #return 
##
##    def SetAsNewDefaultEnvironment(self):
##        u'Sets the raster analysis environment of the object as new default environment.'
##        #return 
##
##    def GetExtent(self):
##        u'Gets the type and values of extent in the RasterAnalysis.'
##        #return envType, Extent
##
##    def SetExtent(self, envType, extentProvider, snapRasterData):
##        u'Sets the type and values of extent in the RasterAnalysis.'
##        #return 
##
##    def _get(self):
##        u'The verify type of the RasterAnalysis.'
##        #return VerifyType
##    def _set(self, VerifyType):
##        u'The verify type of the RasterAnalysis.'
##    VerifyType = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The default output raster prefix.'
##        #return rasterPrefix
##    def _set(self, rasterPrefix):
##        u'The default output raster prefix.'
##    DefaultOutputRasterPrefix = property(_get, _set, doc = _set.__doc__)
##

class FeatureClassDescriptor(CoClass):
    u'GeoAnalyst FeatureClass descriptor object.'
    _reg_clsid_ = GUID('{3297E9D3-93A1-11D2-9F33-00C04F8ED1D7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5C54042B-B2ED-4889-8C40-2D89C19DB41D}', 10, 2)
FeatureClassDescriptor._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset, IFeatureClassDescriptor, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

class RasterModel(CoClass):
    u'A mechanism that allows scripting of operations, and inclusion of non-raster input/output formats (feature data, tables, etc).'
    _reg_clsid_ = GUID('{4606F162-B47D-11D2-9F3B-00C04F8ED1D7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5C54042B-B2ED-4889-8C40-2D89C19DB41D}', 10, 2)
RasterModel._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRasterAnalysisEnvironment, IRasterAnalysisGlobalEnvironment, IRasterOpBase, IRasterModel, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

IRasterImportOp._methods_ = [
    COMMETHOD([helpstring(u'Imports a USGS DEM file into a RasterDataset.')], HRESULT, 'ImportFromUSGSDEM',
              ( ['in'], BSTR, 'demFile' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspace), 'OutWorkspace' ),
              ( ['in'], BSTR, 'outRasterName' ),
              ( ['in'], BSTR, 'OutRasterFormat' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRasterDataset)), 'ppOut' )),
    COMMETHOD([helpstring(u'Imports a GRID ASCII file into a RasterDataset.')], HRESULT, 'ImportFromASCII',
              ( ['in'], BSTR, 'asciiFile' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspace), 'OutWorkspace' ),
              ( ['in'], BSTR, 'outRasterName' ),
              ( ['in'], BSTR, 'OutRasterFormat' ),
              ( ['in'], VARIANT_BOOL, 'isInteger' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRasterDataset)), 'ppOut' )),
    COMMETHOD([helpstring(u'Imports a Float GRID file into a RasterDataset.')], HRESULT, 'ImportFromFLOAT',
              ( ['in'], BSTR, 'floatFile' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspace), 'OutWorkspace' ),
              ( ['in'], BSTR, 'outRasterName' ),
              ( ['in'], BSTR, 'OutRasterFormat' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRasterDataset)), 'ppOut' )),
]
################################################################
## code template for IRasterImportOp implementation
##class IRasterImportOp_Impl(object):
##    def ImportFromFLOAT(self, floatFile, OutWorkspace, outRasterName, OutRasterFormat):
##        u'Imports a Float GRID file into a RasterDataset.'
##        #return ppOut
##
##    def ImportFromUSGSDEM(self, demFile, OutWorkspace, outRasterName, OutRasterFormat):
##        u'Imports a USGS DEM file into a RasterDataset.'
##        #return ppOut
##
##    def ImportFromASCII(self, asciiFile, OutWorkspace, outRasterName, OutRasterFormat, isInteger):
##        u'Imports a GRID ASCII file into a RasterDataset.'
##        #return ppOut
##

IInterpolationOp2._methods_ = [
    COMMETHOD([helpstring(u'Interpolates using IDW.')], HRESULT, 'IDW',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'geoData' ),
              ( ['in'], c_double, 'power' ),
              ( ['in'], POINTER(IRasterRadius), 'radius' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'barrier' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'GeoDataset' )),
    COMMETHOD([helpstring(u'Interpolates using kriging.')], HRESULT, 'Krige',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'geoData' ),
              ( ['in'], esriGeoAnalysisSemiVariogramEnum, 'semiVariogramType' ),
              ( ['in'], POINTER(IRasterRadius), 'radius' ),
              ( ['in'], VARIANT_BOOL, 'outSemiVariance' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'barrier' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'interpolatedRaster' )),
    COMMETHOD([helpstring(u'Interpolates using Variogram.')], HRESULT, 'Variogram',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'geoData' ),
              ( ['in'], POINTER(IGeoAnalysisSemiVariogram), 'semiVariogram' ),
              ( ['in'], POINTER(IRasterRadius), 'radius' ),
              ( ['in'], VARIANT_BOOL, 'outSemiVariance' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'barrier' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'interpolatedRaster' )),
    COMMETHOD([helpstring(u'Interpolates using splining.')], HRESULT, 'Spline',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'geoData' ),
              ( ['in'], esriGeoAnalysisSplineEnum, 'splineType' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'weight' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'numPoints' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'interpolatedRaster' )),
    COMMETHOD([helpstring(u'Interpolates using trend surface.')], HRESULT, 'Trend',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'geoData' ),
              ( ['in'], esriGeoAnalysisTrendEnum, 'trendType' ),
              ( ['in'], c_int, 'order' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'interpolatedRaster' )),
    COMMETHOD([helpstring(u'Interpolates using natual neighbor.')], HRESULT, 'NaturalNeighbor',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'GeoDataset' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'outGeoDataset' )),
    COMMETHOD([helpstring(u'Interpolates using AnuDem.')], HRESULT, 'TopoToRasterByFile',
              ( ['in'], BSTR, 'paramFile' ),
              ( ['out', 'optional'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass)), 'outStream' ),
              ( ['out', 'optional'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass)), 'outSink' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRasterDataset)), 'outSurface' )),
]
################################################################
## code template for IInterpolationOp2 implementation
##class IInterpolationOp2_Impl(object):
##    def Variogram(self, geoData, semiVariogram, radius, outSemiVariance, barrier):
##        u'Interpolates using Variogram.'
##        #return interpolatedRaster
##
##    def Krige(self, geoData, semiVariogramType, radius, outSemiVariance, barrier):
##        u'Interpolates using kriging.'
##        #return interpolatedRaster
##
##    def Trend(self, geoData, trendType, order):
##        u'Interpolates using trend surface.'
##        #return interpolatedRaster
##
##    def IDW(self, geoData, power, radius, barrier):
##        u'Interpolates using IDW.'
##        #return GeoDataset
##
##    def NaturalNeighbor(self, GeoDataset):
##        u'Interpolates using natual neighbor.'
##        #return outGeoDataset
##
##    def TopoToRasterByFile(self, paramFile):
##        u'Interpolates using AnuDem.'
##        #return outStream, outSink, outSurface
##
##    def Spline(self, geoData, splineType, weight, numPoints):
##        u'Interpolates using splining.'
##        #return interpolatedRaster
##

IRemap._methods_ = [
    COMMETHOD(['propget', helpstring(u'The number of remap records.')], HRESULT, 'RecordCount',
              ( ['retval', 'out'], POINTER(c_int), 'RecordCount' )),
    COMMETHOD(['propput', helpstring(u'The nodata value.')], HRESULT, 'NoDataTo',
              ( ['in'], c_int, 'rhs' )),
    COMMETHOD([helpstring(u'Returns info for a remap record by index.')], HRESULT, 'QueryRecord',
              ( ['in'], c_int, 'recordIndex' ),
              ( ['out'], POINTER(BSTR), 'sInValue' ),
              ( ['out'], POINTER(BSTR), 'sOutValue' )),
    COMMETHOD([helpstring(u'Returns whether nodata is mapped and if so, the mapped value.')], HRESULT, 'QueryNoDataTo',
              ( ['out'], POINTER(VARIANT_BOOL), 'isMapped' ),
              ( ['out'], POINTER(c_int), 'outValue' )),
    COMMETHOD([helpstring(u'Validates the remap records.')], HRESULT, 'Validate',
              ( ['out'], POINTER(VARIANT_BOOL), 'bIsValid' ),
              ( ['out'], POINTER(BSTR), 'sErrorInfo' )),
    COMMETHOD([helpstring(u'Deletes a remap record by index.')], HRESULT, 'DeleteRecord',
              ( ['in'], c_int, 'recordIndex' )),
    COMMETHOD([helpstring(u'Clears the remap object.')], HRESULT, 'Clear'),
    COMMETHOD([helpstring(u'Loads remap records from an ITable and creates the relevant remap object.')], HRESULT, 'LoadFromTable',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable), 'remapTable' )),
    COMMETHOD([helpstring(u'Saves the remap records to a table.')], HRESULT, 'SaveAsTable',
              ( ['in'], BSTR, 'tableName' )),
    COMMETHOD([helpstring(u'Stores the remap records in an ITable.')], HRESULT, 'RepresentAsTable',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable)), 'ppTable' )),
    COMMETHOD(['propget', helpstring(u'The minimum output value.')], HRESULT, 'MinOutputValue',
              ( ['retval', 'out'], POINTER(c_int), 'MinValue' )),
    COMMETHOD([helpstring(u'Returns whether any record is mapped to nodata.')], HRESULT, 'HasValueToNoData',
              ( ['out'], POINTER(VARIANT_BOOL), 'hasToNodata' )),
]
################################################################
## code template for IRemap implementation
##class IRemap_Impl(object):
##    def QueryRecord(self, recordIndex):
##        u'Returns info for a remap record by index.'
##        #return sInValue, sOutValue
##
##    def DeleteRecord(self, recordIndex):
##        u'Deletes a remap record by index.'
##        #return 
##
##    def RepresentAsTable(self):
##        u'Stores the remap records in an ITable.'
##        #return ppTable
##
##    def HasValueToNoData(self):
##        u'Returns whether any record is mapped to nodata.'
##        #return hasToNodata
##
##    @property
##    def RecordCount(self):
##        u'The number of remap records.'
##        #return RecordCount
##
##    def Clear(self):
##        u'Clears the remap object.'
##        #return 
##
##    def _set(self, rhs):
##        u'The nodata value.'
##    NoDataTo = property(fset = _set, doc = _set.__doc__)
##
##    def LoadFromTable(self, remapTable):
##        u'Loads remap records from an ITable and creates the relevant remap object.'
##        #return 
##
##    def SaveAsTable(self, tableName):
##        u'Saves the remap records to a table.'
##        #return 
##
##    def Validate(self):
##        u'Validates the remap records.'
##        #return bIsValid, sErrorInfo
##
##    @property
##    def MinOutputValue(self):
##        u'The minimum output value.'
##        #return MinValue
##
##    def QueryNoDataTo(self):
##        u'Returns whether nodata is mapped and if so, the mapped value.'
##        #return isMapped, outValue
##

class RasterDescriptor(CoClass):
    u'GeoAnalyst Raster descriptor object.'
    _reg_clsid_ = GUID('{296E7F5F-D1C8-11D2-9F3C-00C04F8ED1D7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5C54042B-B2ED-4889-8C40-2D89C19DB41D}', 10, 2)
RasterDescriptor._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset, IRasterDescriptor, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

IRasterAnalysisGDBEnvironment._methods_ = [
    COMMETHOD(['propput', helpstring(u'Indicates if the globe optimized type in the RasterAnalysis.')], HRESULT, 'GlobeOptimized',
              ( ['in'], VARIANT_BOOL, 'GlobeOptimized' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the globe optimized type in the RasterAnalysis.')], HRESULT, 'GlobeOptimized',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'GlobeOptimized' )),
    COMMETHOD(['propput', helpstring(u'The mosaic type in the RasterAnalysis.')], HRESULT, 'MosaicType',
              ( ['in'], comtypes.gen._8F0541A3_D5BE_4B3F_A8D9_062D5579E19B_0_10_2.rstMosaicOperatorType, 'MosaicType' )),
    COMMETHOD(['propget', helpstring(u'The mosaic type in the RasterAnalysis.')], HRESULT, 'MosaicType',
              ( ['retval', 'out'], POINTER(comtypes.gen._8F0541A3_D5BE_4B3F_A8D9_062D5579E19B_0_10_2.rstMosaicOperatorType), 'MosaicType' )),
    COMMETHOD(['propput', helpstring(u'The type and value of compression in the RasterAnalysis.')], HRESULT, 'CompressionType',
              ( ['in'], esriRasterGDBCompressionEnum, 'CompressionType' )),
    COMMETHOD(['propget', helpstring(u'The type and value of compression in the RasterAnalysis.')], HRESULT, 'CompressionType',
              ( ['retval', 'out'], POINTER(esriRasterGDBCompressionEnum), 'CompressionType' )),
    COMMETHOD(['propput', helpstring(u'Jpeg compression quality in the RasterAnalysis.')], HRESULT, 'JpegQuality',
              ( ['in'], c_int, 'JpegQuality' )),
    COMMETHOD(['propget', helpstring(u'Jpeg compression quality in the RasterAnalysis.')], HRESULT, 'JpegQuality',
              ( ['retval', 'out'], POINTER(c_int), 'JpegQuality' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the pyramid building in the RasterAnalysis.')], HRESULT, 'BuildPyramid',
              ( ['in'], VARIANT_BOOL, 'buildParamid' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the pyramid building in the RasterAnalysis.')], HRESULT, 'BuildPyramid',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'buildParamid' )),
    COMMETHOD(['propput', helpstring(u'The resample type in pyramid building in the RasterAnalysis.')], HRESULT, 'PyramidResampleType',
              ( ['in'], esriGeoAnalysisResampleEnum, 'resampleType' )),
    COMMETHOD(['propget', helpstring(u'The resample type in pyramid building in the RasterAnalysis.')], HRESULT, 'PyramidResampleType',
              ( ['retval', 'out'], POINTER(esriGeoAnalysisResampleEnum), 'resampleType' )),
    COMMETHOD(['propput', helpstring(u'The level in pyramid building in the RasterAnalysis.')], HRESULT, 'PyramidLevel',
              ( ['in'], c_int, 'level' )),
    COMMETHOD(['propget', helpstring(u'The level in pyramid building in the RasterAnalysis.')], HRESULT, 'PyramidLevel',
              ( ['retval', 'out'], POINTER(c_int), 'level' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the statistics calculation in the RasterAnalysis.')], HRESULT, 'CalculateStatistics',
              ( ['in'], VARIANT_BOOL, 'CalculateStatistics' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the statistics calculation in the RasterAnalysis.')], HRESULT, 'CalculateStatistics',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'CalculateStatistics' )),
    COMMETHOD(['propput', helpstring(u'The skip factor in X direction in statistics calculation in the RasterAnalysis.')], HRESULT, 'XSkipFactor',
              ( ['in'], c_int, 'XSkipFactor' )),
    COMMETHOD(['propget', helpstring(u'The skip factor in X direction in statistics calculation in the RasterAnalysis.')], HRESULT, 'XSkipFactor',
              ( ['retval', 'out'], POINTER(c_int), 'XSkipFactor' )),
    COMMETHOD(['propput', helpstring(u'The skip factor in Y direction in statistics calculation in the RasterAnalysis.')], HRESULT, 'YSkipFactor',
              ( ['in'], c_int, 'YSkipFactor' )),
    COMMETHOD(['propget', helpstring(u'The skip factor in Y direction in statistics calculation in the RasterAnalysis.')], HRESULT, 'YSkipFactor',
              ( ['retval', 'out'], POINTER(c_int), 'YSkipFactor' )),
    COMMETHOD(['propput', helpstring(u'The ignored value in statistics calculation in RasterAnalysis.')], HRESULT, 'IgnoredValue',
              ( ['in'], BSTR, 'IgnoredValue' )),
    COMMETHOD(['propget', helpstring(u'The ignored value in statistics calculation in RasterAnalysis.')], HRESULT, 'IgnoredValue',
              ( ['retval', 'out'], POINTER(BSTR), 'IgnoredValue' )),
    COMMETHOD(['propput', helpstring(u'The GeoDatabase tile width in the RasterAnalysis.')], HRESULT, 'TileWidth',
              ( ['in'], c_int, 'TileWidth' )),
    COMMETHOD(['propget', helpstring(u'The GeoDatabase tile width in the RasterAnalysis.')], HRESULT, 'TileWidth',
              ( ['retval', 'out'], POINTER(c_int), 'TileWidth' )),
    COMMETHOD(['propput', helpstring(u'The GeoDatabase tile height in the RasterAnalysis.')], HRESULT, 'TileHeight',
              ( ['in'], c_int, 'TileHeight' )),
    COMMETHOD(['propget', helpstring(u'The GeoDatabase tile height in the RasterAnalysis.')], HRESULT, 'TileHeight',
              ( ['retval', 'out'], POINTER(c_int), 'TileHeight' )),
    COMMETHOD(['propput', helpstring(u'The configuration keyword in the RasterAnalysis.')], HRESULT, 'ConfigurationKeyword',
              ( ['in'], BSTR, 'configKeyword' )),
    COMMETHOD(['propget', helpstring(u'The configuration keyword in the RasterAnalysis.')], HRESULT, 'ConfigurationKeyword',
              ( ['retval', 'out'], POINTER(BSTR), 'configKeyword' )),
    COMMETHOD(['propputref', helpstring(u'The XY, Z and M domains in the RasterAnalysis.')], HRESULT, 'GDBDomains',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference), 'domainsSpRef' )),
    COMMETHOD(['propget', helpstring(u'The XY, Z and M domains in the RasterAnalysis.')], HRESULT, 'GDBDomains',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference)), 'domainsSpRef' )),
]
################################################################
## code template for IRasterAnalysisGDBEnvironment implementation
##class IRasterAnalysisGDBEnvironment_Impl(object):
##    def _get(self):
##        u'The type and value of compression in the RasterAnalysis.'
##        #return CompressionType
##    def _set(self, CompressionType):
##        u'The type and value of compression in the RasterAnalysis.'
##    CompressionType = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Jpeg compression quality in the RasterAnalysis.'
##        #return JpegQuality
##    def _set(self, JpegQuality):
##        u'Jpeg compression quality in the RasterAnalysis.'
##    JpegQuality = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The GeoDatabase tile height in the RasterAnalysis.'
##        #return TileHeight
##    def _set(self, TileHeight):
##        u'The GeoDatabase tile height in the RasterAnalysis.'
##    TileHeight = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The skip factor in Y direction in statistics calculation in the RasterAnalysis.'
##        #return YSkipFactor
##    def _set(self, YSkipFactor):
##        u'The skip factor in Y direction in statistics calculation in the RasterAnalysis.'
##    YSkipFactor = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The GeoDatabase tile width in the RasterAnalysis.'
##        #return TileWidth
##    def _set(self, TileWidth):
##        u'The GeoDatabase tile width in the RasterAnalysis.'
##    TileWidth = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The mosaic type in the RasterAnalysis.'
##        #return MosaicType
##    def _set(self, MosaicType):
##        u'The mosaic type in the RasterAnalysis.'
##    MosaicType = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def GDBDomains(self, domainsSpRef):
##        u'The XY, Z and M domains in the RasterAnalysis.'
##        #return 
##
##    def _get(self):
##        u'Indicates if the statistics calculation in the RasterAnalysis.'
##        #return CalculateStatistics
##    def _set(self, CalculateStatistics):
##        u'Indicates if the statistics calculation in the RasterAnalysis.'
##    CalculateStatistics = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The configuration keyword in the RasterAnalysis.'
##        #return configKeyword
##    def _set(self, configKeyword):
##        u'The configuration keyword in the RasterAnalysis.'
##    ConfigurationKeyword = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the pyramid building in the RasterAnalysis.'
##        #return buildParamid
##    def _set(self, buildParamid):
##        u'Indicates if the pyramid building in the RasterAnalysis.'
##    BuildPyramid = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The skip factor in X direction in statistics calculation in the RasterAnalysis.'
##        #return XSkipFactor
##    def _set(self, XSkipFactor):
##        u'The skip factor in X direction in statistics calculation in the RasterAnalysis.'
##    XSkipFactor = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the globe optimized type in the RasterAnalysis.'
##        #return GlobeOptimized
##    def _set(self, GlobeOptimized):
##        u'Indicates if the globe optimized type in the RasterAnalysis.'
##    GlobeOptimized = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The level in pyramid building in the RasterAnalysis.'
##        #return level
##    def _set(self, level):
##        u'The level in pyramid building in the RasterAnalysis.'
##    PyramidLevel = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The resample type in pyramid building in the RasterAnalysis.'
##        #return resampleType
##    def _set(self, resampleType):
##        u'The resample type in pyramid building in the RasterAnalysis.'
##    PyramidResampleType = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The ignored value in statistics calculation in RasterAnalysis.'
##        #return IgnoredValue
##    def _set(self, IgnoredValue):
##        u'The ignored value in statistics calculation in RasterAnalysis.'
##    IgnoredValue = property(_get, _set, doc = _set.__doc__)
##

IMLClassifyFunctionArguments._methods_ = [
    COMMETHOD(['propget', helpstring(u'The input raster for conversion.')], HRESULT, 'Raster',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'ppRaster' )),
    COMMETHOD(['propputref', helpstring(u'The input raster for conversion.')], HRESULT, 'Raster',
              ( ['in'], POINTER(IUnknown), 'ppRaster' )),
    COMMETHOD(['propget', helpstring(u'The class signature file.')], HRESULT, 'SignatureFile',
              ( ['retval', 'out'], POINTER(BSTR), 'pFile' )),
    COMMETHOD(['propput', helpstring(u'The class signature file.')], HRESULT, 'SignatureFile',
              ( ['in'], BSTR, 'pFile' )),
]
################################################################
## code template for IMLClassifyFunctionArguments implementation
##class IMLClassifyFunctionArguments_Impl(object):
##    def Raster(self, ppRaster):
##        u'The input raster for conversion.'
##        #return 
##
##    def _get(self):
##        u'The class signature file.'
##        #return pFile
##    def _set(self, pFile):
##        u'The class signature file.'
##    SignatureFile = property(_get, _set, doc = _set.__doc__)
##

IInterpolationOp._methods_ = [
    COMMETHOD([helpstring(u'Interpolates using IDW.')], HRESULT, 'IDW',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'geoData' ),
              ( ['in'], c_double, 'power' ),
              ( ['in'], POINTER(IRasterRadius), 'radius' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'barrier' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'GeoDataset' )),
    COMMETHOD([helpstring(u'Interpolates using kriging.')], HRESULT, 'Krige',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'geoData' ),
              ( ['in'], esriGeoAnalysisSemiVariogramEnum, 'semiVariogramType' ),
              ( ['in'], POINTER(IRasterRadius), 'radius' ),
              ( ['in'], VARIANT_BOOL, 'outSemiVariance' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'barrier' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'interpolatedRaster' )),
    COMMETHOD([helpstring(u'Interpolates using Variogram.')], HRESULT, 'Variogram',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'geoData' ),
              ( ['in'], POINTER(IGeoAnalysisSemiVariogram), 'semiVariogram' ),
              ( ['in'], POINTER(IRasterRadius), 'radius' ),
              ( ['in'], VARIANT_BOOL, 'outSemiVariance' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'barrier' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'interpolatedRaster' )),
    COMMETHOD([helpstring(u'Interpolates using splining.')], HRESULT, 'Spline',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'geoData' ),
              ( ['in'], esriGeoAnalysisSplineEnum, 'splineType' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'weight' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'numPoints' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'interpolatedRaster' )),
    COMMETHOD([helpstring(u'Interpolates using trend surface.')], HRESULT, 'Trend',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'geoData' ),
              ( ['in'], esriGeoAnalysisTrendEnum, 'trendType' ),
              ( ['in'], c_int, 'order' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'interpolatedRaster' )),
]
################################################################
## code template for IInterpolationOp implementation
##class IInterpolationOp_Impl(object):
##    def Trend(self, geoData, trendType, order):
##        u'Interpolates using trend surface.'
##        #return interpolatedRaster
##
##    def IDW(self, geoData, power, radius, barrier):
##        u'Interpolates using IDW.'
##        #return GeoDataset
##
##    def Variogram(self, geoData, semiVariogram, radius, outSemiVariance, barrier):
##        u'Interpolates using Variogram.'
##        #return interpolatedRaster
##
##    def Krige(self, geoData, semiVariogramType, radius, outSemiVariance, barrier):
##        u'Interpolates using kriging.'
##        #return interpolatedRaster
##
##    def Spline(self, geoData, splineType, weight, numPoints):
##        u'Interpolates using splining.'
##        #return interpolatedRaster
##

class RasterAnalysis(CoClass):
    u'A collection of information about the raster analysis environment.'
    _reg_clsid_ = GUID('{3549C4F9-F9C2-11D3-9F64-00C04F8ED1D7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5C54042B-B2ED-4889-8C40-2D89C19DB41D}', 10, 2)
RasterAnalysis._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRasterAnalysisEnvironment, IRasterAnalysisGDBEnvironment, IRasterAnalysisGlobalEnvironment, IRasterOpBase, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

class MLClassifyFunction(CoClass):
    u'The The ML classification function.'
    _reg_clsid_ = GUID('{5803078B-AF97-4388-9B9E-7657AE76A310}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5C54042B-B2ED-4889-8C40-2D89C19DB41D}', 10, 2)
MLClassifyFunction._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._8F0541A3_D5BE_4B3F_A8D9_062D5579E19B_0_10_2.IRasterFunction, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLVersionSupport]


# values for enumeration 'esriGeoAnalysisFilterEnum'
esriGeoAnalysisFilter3x3LowPass = 1
esriGeoAnalysisFilter3x3HighPass = 2
esriGeoAnalysisFilterEnum = c_int # enum
IConversionOp._methods_ = [
    COMMETHOD([helpstring(u'Convert to a RasterDataset.')], HRESULT, 'ToRasterDataset',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'dataset' ),
              ( ['in'], BSTR, 'rasterFormat' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspace), 'pWorkspace' ),
              ( ['in'], BSTR, 'name' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRasterDataset)), 'rasterDataset' )),
    COMMETHOD([helpstring(u'Convert to feature data (FeatureClass or FeatureDataset).')], HRESULT, 'ToFeatureData',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'dataset' ),
              ( ['in'], comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.esriGeometryType, 'geometryType' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspace), 'pWorkspace' ),
              ( ['in'], BSTR, 'name' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'GeoDataset' )),
    COMMETHOD([helpstring(u'Convert raster data to feature data (FeatureClass or FeatureDataset).')], HRESULT, 'RasterDataToPointFeatureData',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'dataset' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspace), 'pWorkspace' ),
              ( ['in'], BSTR, 'name' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'GeoDataset' )),
    COMMETHOD([helpstring(u'Convert raster data to feature data (FeatureClass or FeatureDataset).')], HRESULT, 'RasterDataToPolygonFeatureData',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'dataset' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspace), 'pWorkspace' ),
              ( ['in'], BSTR, 'name' ),
              ( ['in'], VARIANT_BOOL, 'weeding' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'GeoDataset' )),
    COMMETHOD([helpstring(u'Convert raster data to feature data (FeatureClass or FeatureDataset).')], HRESULT, 'RasterDataToLineFeatureData',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'dataset' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspace), 'pWorkspace' ),
              ( ['in'], BSTR, 'name' ),
              ( ['in'], VARIANT_BOOL, 'zeroAsBackground' ),
              ( ['in'], VARIANT_BOOL, 'weeding' ),
              ( ['in'], POINTER(VARIANT), 'minDangle' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset)), 'GeoDataset' )),
]
################################################################
## code template for IConversionOp implementation
##class IConversionOp_Impl(object):
##    def RasterDataToPointFeatureData(self, dataset, pWorkspace, name):
##        u'Convert raster data to feature data (FeatureClass or FeatureDataset).'
##        #return GeoDataset
##
##    def RasterDataToPolygonFeatureData(self, dataset, pWorkspace, name, weeding):
##        u'Convert raster data to feature data (FeatureClass or FeatureDataset).'
##        #return GeoDataset
##
##    def ToRasterDataset(self, dataset, rasterFormat, pWorkspace, name):
##        u'Convert to a RasterDataset.'
##        #return rasterDataset
##
##    def ToFeatureData(self, dataset, geometryType, pWorkspace, name):
##        u'Convert to feature data (FeatureClass or FeatureDataset).'
##        #return GeoDataset
##
##    def RasterDataToLineFeatureData(self, dataset, pWorkspace, name, zeroAsBackground, weeding, minDangle):
##        u'Convert raster data to feature data (FeatureClass or FeatureDataset).'
##        #return GeoDataset
##

IRasterAnalysisGlobalEnvironment._methods_ = [
    COMMETHOD(['propput', helpstring(u'Indicates weather to avoid data conversion in the RasterAnalysis.')], HRESULT, 'AvoidDataConversion',
              ( ['in'], VARIANT_BOOL, 'bAvoid' )),
    COMMETHOD(['propget', helpstring(u'Indicates weather to avoid data conversion in the RasterAnalysis.')], HRESULT, 'AvoidDataConversion',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bAvoid' )),
]
################################################################
## code template for IRasterAnalysisGlobalEnvironment implementation
##class IRasterAnalysisGlobalEnvironment_Impl(object):
##    def _get(self):
##        u'Indicates weather to avoid data conversion in the RasterAnalysis.'
##        #return bAvoid
##    def _set(self, bAvoid):
##        u'Indicates weather to avoid data conversion in the RasterAnalysis.'
##    AvoidDataConversion = property(_get, _set, doc = _set.__doc__)
##

class RasterSurfaceOp(CoClass):
    u'Raster surface operation class.'
    _reg_clsid_ = GUID('{CD568B5F-CA31-11D2-9F3C-00C04F8ED1D7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5C54042B-B2ED-4889-8C40-2D89C19DB41D}', 10, 2)
RasterSurfaceOp._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRasterAnalysisEnvironment, IRasterAnalysisGlobalEnvironment, IRasterOpBase, ISurfaceOp, ISurfaceOp2, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

IRasterConvertHelper._methods_ = [
    COMMETHOD([helpstring(u'Converts a GeoDataset to a Raster.')], HRESULT, 'ToRaster1',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'pIn1' ),
              ( ['in'], BSTR, 'rasterFormat' ),
              ( ['in'], POINTER(IRasterAnalysisEnvironment), 'rasterEnv' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRaster)), 'ppOut' )),
    COMMETHOD([helpstring(u'Converts two GeoDatasets to two Rasters.')], HRESULT, 'ToRaster2',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'pIn1' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'pIn2' ),
              ( ['in'], BSTR, 'rasterFormat' ),
              ( ['in'], POINTER(IRasterAnalysisEnvironment), 'rasterEnv' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRaster)), 'ppOut1' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRaster)), 'ppOut2' )),
    COMMETHOD([helpstring(u'Converts three GeoDatasets to three Rasters.')], HRESULT, 'ToRaster3',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'pIn1' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'pIn2' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'pIn3' ),
              ( ['in'], BSTR, 'rasterFormat' ),
              ( ['in'], POINTER(IRasterAnalysisEnvironment), 'rasterEnv' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRaster)), 'ppOut1' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRaster)), 'ppOut2' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRaster)), 'ppOut3' )),
    COMMETHOD([helpstring(u'Converts a GeoDataset to a shapefile.')], HRESULT, 'ToShapefile',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset), 'pIn' ),
              ( ['in'], comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.esriGeometryType, 'geometryType' ),
              ( ['in'], POINTER(IRasterAnalysisEnvironment), 'rasterEnv' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass)), 'ppOut' )),
]
################################################################
## code template for IRasterConvertHelper implementation
##class IRasterConvertHelper_Impl(object):
##    def ToShapefile(self, pIn, geometryType, rasterEnv):
##        u'Converts a GeoDataset to a shapefile.'
##        #return ppOut
##
##    def ToRaster1(self, pIn1, rasterFormat, rasterEnv):
##        u'Converts a GeoDataset to a Raster.'
##        #return ppOut
##
##    def ToRaster3(self, pIn1, pIn2, pIn3, rasterFormat, rasterEnv):
##        u'Converts three GeoDatasets to three Rasters.'
##        #return ppOut1, ppOut2, ppOut3
##
##    def ToRaster2(self, pIn1, pIn2, rasterFormat, rasterEnv):
##        u'Converts two GeoDatasets to two Rasters.'
##        #return ppOut1, ppOut2
##

__all__ = ['GRID_ERR_ZONEOBJ', 'INumberRemap',
           'E_SPATIAL_ANALYST_NO_DATASET',
           'E_SPATIAL_ANALYST_REMAP_FREE_RECORDS',
           'E_SPATIAL_ANALYST_CREATE_WORKSPACENAME',
           'E_SPATIAL_ANALYST_PRJ_NOTMACTH', 'RasterConversionOp',
           'esriRasterGDBCompressionCCITTG3',
           'E_SPATIAL_ANALYST_EVAL_TYPE',
           'esriGeoAnalysisFilter3x3LowPass',
           'E_SPATIAL_ANALYST_OUT_FILE_EXISTS',
           'E_SPATIAL_ANALYST_NREMAP_HAS_STRING_FIELD',
           'esriGeoAnalysisUnitsEnum',
           'esriGeoAnalysisLinearSemiVariogram',
           'esriSpatialAnalystError',
           'esriGeoAnalysisUniversal2SemiVariogram',
           'GRID_ERR_BADSTA', 'E_SPATIAL_ANALYST_NULL_FEATURE_COUNT',
           'GRID_ERR_NOIRREGNBR', 'esriRasterGDBCompressionJPEG',
           'GRID_ERR_STRGRID', 'GRID_ERR_READVTAB',
           'esriGeoAnalysisResampleBilinear',
           'E_SPATIAL_ANALYST_NO_DUPLICATES',
           'esriGeoAnalysisResampleSearch', 'IRasterModel',
           'GRID_ERR_MAKEVTAB', 'esriGeoAnalysisStatsMajority',
           'esriGeoAnalysisCircularSemiVariogram',
           'esriRasterGDBCompressionEnum',
           'E_SPATIAL_ANALYST_TOPO_NOT_POSITIVE',
           'E_SPATIAL_ANALYST_TOPO_UNKNOWN_KEYWORD',
           'IRasterImportOp',
           'E_SPATIAL_ANALYST_RENDERER_INVALID_BAND_INDEX',
           'esriGeoAnalysisNoneVariogram',
           'E_SPATIAL_ANALYST_CONVERSION', 'RasterAnalysis',
           'E_SPATIAL_ANALYST_TABLE_NOT_CREATED',
           'esriRasterNeighborhoodEnum', 'RasterTransformationOp',
           'E_SPATIAL_ANALYST_CANNOT_OBTAIN_STATS', 'IReclassOp',
           'IGridTableOp', 'esriRasterGDBCompressionCCITTRLE',
           'E_SPATIAL_ANALYST_NO_SPREF',
           'E_SPATIAL_ANALYST_REMAP_BAD_SVALUE',
           'E_SPATIAL_ANALYST_RESERVED_FIELD_EXISTS',
           'E_SPATIAL_ANALYST_REMAP_SIMPLE_CONFLICT',
           'GRID_ERR_FIELDTYPE', 'GRID_ERR_SHAPETYPE',
           'E_SPATIAL_ANALYST_BINARY_OPERATION',
           'E_SPATIAL_ANALYST_TOPO_INVALID_ZLIMITS',
           'GRID_ERR_ARGTYPE',
           'E_SPATIAL_ANALYST_FILE_FAILED_TO_RENAME',
           'E_SPATIAL_ANALYST_READ_ERROR', 'E_SPATIAL_ANALYST_SAVEAS',
           'E_SPATIAL_ANALYST_TOPO_LAKE_TOOMANY_POINTS',
           'E_SPATIAL_ANALYST_WRITE_UNABLE',
           'esriGeoAnalysisEnforceOff', 'GRID_ERR_SORTTYPE',
           'esriRasterVerifyEnum', 'E_SPATIAL_ANALYST_OPEN_RDS_FAIL',
           'IInterpolationOp2', 'IRasterDescriptor',
           'E_SPATIAL_ANALYST_INVALID_FILTER_TYPE',
           'esriAnnulusNeighborhood', 'esriGeoAnalysisSliceEqualArea',
           'E_SPATIAL_ANALYST_TREND_FIELD',
           'esriGeoAnalysisFilter3x3HighPass',
           'E_SPATIAL_ANALYST_INVALID_STATSTYPE',
           'E_SPATIAL_ANALYST_REMAP_OVERLAP_CONFLICT',
           'esriRectangleNeighborhood',
           'esriGeoAnalysisEnforceOnWithSink', 'IStringRemap',
           'E_SPATIAL_ANALYST_FILE_NOT_FOUND', 'IConversionOp',
           'E_SPATIAL_ANALYST_INIT_SAMPLE_LIST',
           'E_SPATIAL_ANALYST_NO_FEATURE_CLASS',
           'esriGeoAnalysisTrendEnum',
           'E_SPATIAL_ANALYST_EMPTY_RASTER',
           'E_SPATIAL_ANALYST_WASNOTACTIVATED',
           'E_SPATIAL_ANALYST_SIMPLE_POLY_SUPPORT',
           'E_SPATIAL_ANALYST_INVALID_GEODATASET',
           'E_SPATIAL_ANALYST_UNKNOWN_ERROR',
           'E_SPATIAL_ANALYST_CANCEL_OP',
           'E_SPATIAL_ANALYST_NO_CONVERTTOCOVERAGE',
           'esriGeoAnalysisSliceEnum', 'GridTableOp',
           'GRID_ERR_SLICETYPE',
           'esriGeoAnalysisVisibilityObserversUseCurvature',
           'E_SPATIAL_ANALYST_INVALID_BAND_COUNT', 'RasterDescriptor',
           'E_SPATIAL_ANALYST_INVALID_NUMERIC_FIELD_LEN',
           'GRID_ERR_TIMEOUT', 'RasterModel',
           'esriGeoAnalysisResampleNearest',
           'E_SPATIAL_ANALYST_NOT_GRID',
           'E_SPATIAL_ANALYST_REFERENCE_FAILED', 'RasterRadius',
           'E_SPATIAL_ANALYST_MEMORY_ALLOC',
           'E_SPATIAL_ANALYST_ANALYSIS_WINDOW',
           'esriGeoAnalysisStatsMean', 'esriGeoAnalysisStatsMinimum',
           'GRID_ERR_SEMIVARIO', 'esriGeoAnalysisStatsStd',
           'E_SPATIAL_ANALYST_NO_COVERAGE_SUPPORT',
           'esriGeoAnalysisStatisticsEnum',
           'E_SPATIAL_ANALYST_EXPRESSION_TOO_LONG',
           'E_SPATIAL_ANALYST_ADDITEM_FAILED', 'RasterMakerOp',
           'E_SPATIAL_ANALYST_UNARY_OPERATION',
           'GRID_ERR_MISMATCHSPREF', 'StringRemap',
           'esriGeoAnalysisUniversal1SemiVariogram',
           'E_SPATIAL_ANALYST_SREMAP_NO_STRING_FIELD',
           'IFeatureClassDescriptor', 'GeoAnalysisSemiVariogram',
           'GRID_ERR_NOVAT', 'E_SPATIAL_ANALYST_FIELD_EXISTS',
           'NumberRemap',
           'E_SPATIAL_ANALYST_STRING_FIELD_NOT_ALLOWED',
           'esriGeoAnalysisLinearTrend', 'esriGeoAnalysisEnforceEnum',
           'E_SPATIAL_ANALYST_NOT_FEATURE_CLASS',
           'IGeoAnalysisEnvironment', 'IRasterConvertHelper',
           'IRemap', 'E_SPATIAL_ANALYST_UNBIND_RASTER',
           'esriGeoAnalysisEnforceOn',
           'esriGeoAnalysisGaussianSemiVariogram',
           'MLClassifyFunctionArguments', 'ISurfaceOp2',
           'E_SPATIAL_ANALYST_INVALID_OUTPUT_EXTENT', 'esriUnitsMap',
           'esriRasterGDBCompressionNone', 'GRID_ERR_ALLOCLUT',
           'esriRasterGDBCompressionJPEGYCbCr',
           'E_SPATIAL_ANALYST_TOPO_NO_ELEVDATA',
           'E_SPATIAL_ANALYST_REMAP_NEED_STYPE',
           'esriGeoAnalysisResampleCubic',
           'esriGeoAnalysisVisibilityEnum',
           'E_SPATIAL_ANALYST_OUTPUT_EXISTS', 'GRID_ERR_NOLIBEXIT',
           'E_SPATIAL_ANALYST_INVALID_PRJS_FOR_CURVATURE',
           'esriGeoAnalysisVisibilityFrequency',
           'esriGeoAnalysisStatsVariety', 'MLClassifyFunction',
           'GRID_ERR_READSTA',
           'E_SPATIAL_ANALYST_INVALID_COMPONENT_COUNT',
           'E_SPATIAL_ANALYST_NO_ATTRIB_TABLE',
           'E_SPATIAL_ANALYST_REMAP_FILL_SREMAP', 'ISurfaceOp',
           'E_SPATIAL_ANALYST_NO_RECS_WITH_QFILTER',
           'E_SPATIAL_ANALYST_TOPO_STREAM_TOOMANY_POINTS',
           'E_SPATIAL_ANALYST_ESTIMATE_SEMIVAR',
           'E_SPATIAL_ANALYST_NO_EXTENT',
           'E_SPATIAL_ANALYST_INVALID_SEMIVAR_TYPE',
           'GRID_ERR_READTABLE', 'E_SPATIAL_ANALYST_NULL_OBJECT',
           'E_SPATIAL_ANALYST_INVALID_FIELD',
           'E_SPATIAL_ANALYST_HIST_FREQUENCY',
           'E_SPATIAL_ANALYST_INVALID_COMMAND', 'GRID_ERR_OBJTYPE',
           'IGeoAnalysisSemiVariogram', 'RasterConvertHelper',
           'esriRasterGDBCompressionJPEG2000',
           'esriGeoAnalysisStatsLength',
           'esriGeoAnalysisVisibilityObservers',
           'E_SPATIAL_ANALYST_OBSV_UNSUPPORTED_GEOMETRY',
           'E_SPATIAL_ANALYST_SHAREDWASNOTACTIVATED',
           'IRasterNeighborhood', 'E_SPATIAL_ANALYST_TOPO_MISS_VALUE',
           'E_SPATIAL_ANALYST_REMAP_RECORD_NOT_FOUND',
           'E_SPATIAL_ANALYST_FILE_FAILED_TO_WRITE',
           'GRID_ERR_CSIZETYPE', 'esriUnitsCells',
           'E_SPATIAL_ANALYST_EXTRACT_VARARR',
           'E_SPATIAL_ANALYST_SYNTAX_ERROR',
           'esriRasterGDBCompressionRLE',
           'IRasterAnalysisGDBEnvironment', 'RasterNeighborhood',
           'E_SPATIAL_ANALYST_NOT_INTEGER', 'esriWeightNeighborhood',
           'E_SPATIAL_ANALYST_INVALID_REJECT_FRACTION',
           'E_SPATIAL_ANALYST_CREATE_GRID',
           'esriGeoAnalysisResampleEnum', 'ITransformationOp',
           'esriGeoAnalysisSliceNatualBreaks',
           'esriGeoAnalysisStatsMedian', 'esriGeoAnalysisSlopeEnum',
           'esriLowPassFilterNeighborhood',
           'esriRasterGDBCompressionLZ77',
           'esriIrregularNeighborhood',
           'E_SPATIAL_ANALYST_COMPOSE_EXPR',
           'E_SPATIAL_ANALYST_INVALID_DELETE_INDEX',
           'esriRasterVerifyOff', 'esriRasterEnvMinOf',
           'E_SPATIAL_ANALYST_REMAP_INVALID_FIND_INDEX',
           'E_SPATIAL_ANALYST_INVALID_RECLASS_FIELD',
           'GRID_ERR_LUTRANGE', 'IRasterExportOp',
           'GRID_ERR_NOTVALUEFD', 'IRasterOpBase',
           'IInterpolationOp3',
           'esriGeoAnalysisSliceStandardDeviation',
           'E_SPATIAL_ANALYST_NO_FILE_NAME', 'RasterMathSupportOp',
           'E_SPATIAL_ANALYST_FIELD_NOT_ADDED', 'IRasterMakerOp',
           'esriGeoAnalysisStatsMinority', 'esriGeoAnalysisStatsSum',
           'E_SPATIAL_ANALYST_SAVEAS_FAILED',
           'E_SPATIAL_ANALYST_FILE_FAILED_TO_COPY', 'RasterSurfaceOp',
           'E_SPATIAL_ANALYST_RECLASS_BY_SELECT',
           'esriRasterEnvSettingEnum',
           'E_SPATIAL_ANALYST_TOPO_NOT_NONNEGATIVE',
           'IInterpolationOp', 'esriGeoAnalysisStatsRange',
           'esriRasterVerifyOn',
           'E_SPATIAL_ANALYST_UNSUPPORTED_FEAT_INPUT',
           'esriGeoAnalysisTensionSpline',
           'esriGeoAnalysisSphericalSemiVariogram',
           'E_SPATIAL_ANALYST_NO_JOINEDFIELD',
           'esriGeoAnalysisSliceEqualInterval',
           'esriRasterGDBCompressionLZW', 'GRID_ERR_LEGCLASS',
           'esriGeoAnalysisSlopePercentrise',
           'FeatureClassDescriptor', 'esriGeoAnalysisLogisticTrend',
           'IGeoDataDescriptor',
           'E_SPATIAL_ANALYST_SHAREDLICENSENOTAVAILABLE',
           'E_SPATIAL_ANALYST_NO_POINTS',
           'E_SPATIAL_ANALYST_HDR_FILE_NOT_FOUND',
           'esriRasterGDBCompressionPackBits', 'GRID_ERR_MAKEHASH',
           'E_SPATIAL_ANALYST_NO_STRING_FIELD',
           'E_SPATIAL_LOCALFUNCTION_ARGUMENTS_OVERSPECIFIED',
           'E_SPATIAL_ANALYST_NO_EVALEXP',
           'esriGeoAnalysisStatsMaximum',
           'E_SPATIAL_ANALYST_INVALID_NAMEFORGRIDENG',
           'E_SPATIAL_ANALYST_TOPO_BAD_CONTOUR_OPTION',
           'GRID_ERR_NOLIBINIT', 'esriWedgeNeighborhood',
           'IRasterAnalysisEnvironment',
           'E_SPATIAL_ANALYST_NOT_EVALUATED',
           'esriHighPassFilterNeighborhood', 'GRID_ERR_CELLSIZE',
           'esriRasterGDBCompressionCCITTG4',
           'E_SPATIAL_ANALYST_NO_FIELD_NAME',
           'E_SPATIAL_ANALYST_INVALID_NAME_FROM_PATH',
           'IRasterRadius', 'E_SPATIAL_ANALYST_NO_SUPPORT',
           'IRasterAnalysisGlobalEnvironment',
           'E_SPATIAL_ANALYST_PRJ_COPY', 'esriRasterEnvValue',
           'E_SPATIAL_ANALYST_INVALID_READ_INDEX',
           'E_SPATIAL_ANALYST_REMAP_UNSORTED', 'GRID_ERR_INFODIR',
           'esriGeoAnalysisSplineEnum',
           'E_SPATIAL_ANALYST_NO_POINT_FILE',
           'E_SPATIAL_ANALYST_BIND_SYMBOL_MISMATCH',
           'IMLClassifyFunctionArguments',
           'E_SPATIAL_ANALYST_INVALID_OUTRFORMAT',
           'E_SPATIAL_ANALYST_LICENSENOTAVAILABLE',
           'IRasterNeighborhood2', 'GRID_ERR_CONTINUE',
           'IRasterImportOp2', 'IMathSupportOp',
           'esriCircleNeighborhood',
           'E_SPATIAL_ANALYST_TOPO_CONTOUR_TOOMANY_POINTS',
           'esriGeoAnalysisFilterEnum',
           'E_SPATIAL_ANALYST_OBSV_EXCESS_POINTS',
           'esriGeoAnalysisSlopeDegrees',
           'E_SPATIAL_ANALYST_INVALID_GEOMETRY', 'esriRasterEnvMaxOf',
           'E_SPATIAL_ANALYST_REMAP_NEED_NTYPE', 'GRID_ERR_LOADFAIL',
           'esriGeoAnalysisSemiVariogramEnum',
           'E_SPATIAL_ANALYST_GRID_EXECUTE', 'GRID_ERR_ALLOCMEM',
           'RasterReclassOp', 'E_SPATIAL_ANALYST_NO_BASETABLE',
           'E_SPATIAL_ANALYST_TOPO_BOUND_TOOMANY_POINTS',
           'GRID_ERR_HASERR',
           'E_SPATIAL_ANALYST_FILE_INVALID_EXTENSION',
           'esriGeoAnalysisRegularizedSpline',
           'E_SPATIAL_ANALYST_BAD_FIELD_INDEX',
           'E_SPATIAL_ANALYST_REMAP_DUPLICATE_RECORD',
           'GRID_ERR_READVAT', 'E_SPATIAL_ANALYST_OPEN_WORKSPACE',
           'esriGeoAnalysisVisibilityFrequencyUseCurvature',
           'E_SPATIAL_ANALYST_NODATA_RASTER', 'GRID_ERR_GRIDORNUMB',
           'RasterInterpolationOp', 'GRID_ERR_LISTELEM',
           'E_SPATIAL_ANALYST_REMAP_MIXED_FILE',
           'esriGeoAnalysisExponentialSemiVariogram',
           'esriRasterVerifyError',
           'E_SPATIAL_ANALYST_FEAT_SEARCH_CURSOR']
from comtypes import _check_version; _check_version('501')

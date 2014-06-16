# -*- coding: mbcs -*-
typelib_path = u'C:\\Program Files (x86)\\ArcGIS\\Engine10.2\\com\\esriGeoDatabaseExtensions.olb'
_lcid = 0 # change this if required
from ctypes import *
from comtypes import GUID
from comtypes import CoClass
import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0
import comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2
import comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2
import comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2
from ctypes import HRESULT
from comtypes import BSTR
from ctypes.wintypes import VARIANT_BOOL
from comtypes import helpstring
from comtypes import COMMETHOD
from comtypes import dispid
import comtypes.gen._8F0541A3_D5BE_4B3F_A8D9_062D5579E19B_0_10_2
from comtypes.automation import VARIANT
from comtypes import IUnknown
from comtypes.automation import _midlSAFEARRAY
import comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2


class LasFilter(CoClass):
    u'Esri LasFilter component.'
    _reg_clsid_ = GUID('{6AA74D41-734B-4BAD-87EA-245977E51EE1}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
class ILasAttributeFilter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides controls for accessing LAS points.'
    _iid_ = GUID('{2A37E73C-2B6D-4D82-9F32-72A2E268394D}')
    _idlflags_ = ['oleautomation']
class ILasPointFilter(ILasAttributeFilter):
    _case_insensitive_ = True
    _iid_ = GUID('{53BC0282-1396-450F-BCA9-0C3398550895}')
    _idlflags_ = ['oleautomation']
class ILasFilter(ILasPointFilter):
    _case_insensitive_ = True
    u'Provides access to members of LasFilter.'
    _iid_ = GUID('{9AE04CB6-3C51-4322-B5B5-E891E2DCAE0B}')
    _idlflags_ = ['oleautomation']
LasFilter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ILasPointFilter, ILasAttributeFilter, ILasFilter, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream]

class DynamicSurface(CoClass):
    u'Esri DynamicSurface object.'
    _reg_clsid_ = GUID('{7C3B1045-DFAD-4F31-9D55-BF743DA91648}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
class IDynamicSurface(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members used to derive raster and TIN surfaces from a terrain.'
    _iid_ = GUID('{36E5CBC7-14B3-4EA8-B19D-F084CB0911D9}')
    _idlflags_ = ['oleautomation']
class IDynamicSurface2(IDynamicSurface):
    _case_insensitive_ = True
    u'Provides access to members that utilize Terrain surfaces.'
    _iid_ = GUID('{D7DE4992-54F7-4F46-8310-C9D991937C3C}')
    _idlflags_ = ['oleautomation']
class IDynamicSurface3(IDynamicSurface2):
    _case_insensitive_ = True
    u'Provides access to members that utilize Terrain surfaces.'
    _iid_ = GUID('{9DC0A59E-494E-41B6-BE82-F283E3431577}')
    _idlflags_ = ['oleautomation']
DynamicSurface._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDynamicSurface, IDynamicSurface2, IDynamicSurface3]
DynamicSurface._outgoing_interfaces_ = [comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ISurfaceIntersectionEvents]

class ICadastralFabric3(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control a cadastral fabric and its associated cadastral jobs.'
    _iid_ = GUID('{5AFCE645-3C35-4A29-97D6-36C7524EE750}')
    _idlflags_ = ['oleautomation']
class ICadastralJob(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the properties of a cadastral job.'
    _iid_ = GUID('{B2AC22B9-4234-411E-9524-01D3BF296355}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriCadastralPacketSetting'
esriCadastralPacketNoSetting = 0
esriCadastralPacketNeighborsInPacket = 1
esriCadastralPacketSetting = c_int # enum
ICadastralFabric3._methods_ = [
    COMMETHOD([helpstring(u'Creates a cadastral packet without a linked job.')], HRESULT, 'CreateCadastralPacket',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IProjectedCoordinateSystem), 'OutputProjectedCoordSys' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFIDSet), 'PlanIDs' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'TrackCancel' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLStream)), 'XMLStream' )),
    COMMETHOD([helpstring(u'Saves the cadastral packet and creates a new job if there are new parcels..')], HRESULT, 'InsertCadastralPacket',
              ( ['in'], POINTER(ICadastralJob), 'NewCadastralJobDefinition' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLStream), 'XMLStream' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'CancelTracker' ),
              ( ['in'], esriCadastralPacketSetting, 'ePacketSetting' ),
              ( ['in', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFIDSet)), 'InsertedParcelOIDs' )),
    COMMETHOD([helpstring(u'Creates/Extracts a cadastral packet for the specified job.')], HRESULT, 'ExtractCadastralPacket',
              ( ['in'], BSTR, 'JobName' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IProjectedCoordinateSystem), 'OutputProjectedCoordSys' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'TrackCancel' ),
              ( ['in'], VARIANT_BOOL, 'IncludeWhiteSpace' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLStream)), 'XMLStream' )),
    COMMETHOD([helpstring(u'Saves the cadastral packet for the job.')], HRESULT, 'PostCadastralPacket',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLStream), 'XMLStream' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'CancelTracker' ),
              ( ['in'], esriCadastralPacketSetting, 'ePacketSetting' ),
              ( ['in', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFIDSet)), 'InsertedParcelOIDs' )),
]
################################################################
## code template for ICadastralFabric3 implementation
##class ICadastralFabric3_Impl(object):
##    def PostCadastralPacket(self, XMLStream, CancelTracker, ePacketSetting):
##        u'Saves the cadastral packet for the job.'
##        #return InsertedParcelOIDs
##
##    def ExtractCadastralPacket(self, JobName, OutputProjectedCoordSys, TrackCancel, IncludeWhiteSpace):
##        u'Creates/Extracts a cadastral packet for the specified job.'
##        #return XMLStream
##
##    def CreateCadastralPacket(self, OutputProjectedCoordSys, PlanIDs, TrackCancel):
##        u'Creates a cadastral packet without a linked job.'
##        #return XMLStream
##
##    def InsertCadastralPacket(self, NewCadastralJobDefinition, XMLStream, CancelTracker, ePacketSetting):
##        u'Saves the cadastral packet and creates a new job if there are new parcels..'
##        #return InsertedParcelOIDs
##

ILasAttributeFilter._methods_ = [
    COMMETHOD(['propput', helpstring(u'The return numbers.')], HRESULT, 'Returns',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray), 'ppReturns' )),
    COMMETHOD(['propget', helpstring(u'The return numbers.')], HRESULT, 'Returns',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray)), 'ppReturns' )),
    COMMETHOD(['propput', helpstring(u'The classification codes.')], HRESULT, 'ClassCodes',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray), 'ppCodes' )),
    COMMETHOD(['propget', helpstring(u'The classification codes.')], HRESULT, 'ClassCodes',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray)), 'ppCodes' )),
    COMMETHOD(['propput', helpstring(u'The classification flags.')], HRESULT, 'ClassFlags',
              ( ['in'], c_int, 'pFlags' )),
    COMMETHOD(['propget', helpstring(u'The classification flags.')], HRESULT, 'ClassFlags',
              ( ['retval', 'out'], POINTER(c_int), 'pFlags' )),
]
################################################################
## code template for ILasAttributeFilter implementation
##class ILasAttributeFilter_Impl(object):
##    def _get(self):
##        u'The return numbers.'
##        #return ppReturns
##    def _set(self, ppReturns):
##        u'The return numbers.'
##    Returns = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The classification flags.'
##        #return pFlags
##    def _set(self, pFlags):
##        u'The classification flags.'
##    ClassFlags = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The classification codes.'
##        #return ppCodes
##    def _set(self, ppCodes):
##        u'The classification codes.'
##    ClassCodes = property(_get, _set, doc = _set.__doc__)
##

ILasPointFilter._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The area of interest.')], HRESULT, 'AreaOfInterest',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'ppAOI' )),
    COMMETHOD(['propget', helpstring(u'The area of interest.')], HRESULT, 'AreaOfInterest',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry)), 'ppAOI' )),
]
################################################################
## code template for ILasPointFilter implementation
##class ILasPointFilter_Impl(object):
##    @property
##    def AreaOfInterest(self, ppAOI):
##        u'The area of interest.'
##        #return 
##

class ITerrainEmbeddedDataSource(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members associated with embedded data sources.'
    _iid_ = GUID('{36A1B4A5-D296-433D-AC4F-4DA50D020812}')
    _idlflags_ = ['oleautomation']
ITerrainEmbeddedDataSource._methods_ = [
    COMMETHOD(['propput', helpstring(u'Indicates the terrain will copy the data and not have a dependency on the data source after the terrain is built.')], HRESULT, 'ToBeEmbedded',
              ( ['in'], VARIANT_BOOL, 'pbToBeEmbedded' )),
    COMMETHOD(['propget', helpstring(u'Indicates the terrain will copy the data and not have a dependency on the data source after the terrain is built.')], HRESULT, 'ToBeEmbedded',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbToBeEmbedded' )),
    COMMETHOD(['propput', helpstring(u'The name of the embedded data source.')], HRESULT, 'Name',
              ( ['in'], BSTR, 'pName' )),
    COMMETHOD(['propget', helpstring(u'The name of the embedded data source.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pName' )),
    COMMETHOD([helpstring(u'Set the names of the database fields associated with the data source that will be copied into the terrain.')], HRESULT, 'SetReservedFields',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray), 'pFields' )),
    COMMETHOD([helpstring(u'Returns the names of the database fields associated with the data source that are copied into the terrain.')], HRESULT, 'GetReservedFields',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'ppFields' )),
]
################################################################
## code template for ITerrainEmbeddedDataSource implementation
##class ITerrainEmbeddedDataSource_Impl(object):
##    def SetReservedFields(self, pFields):
##        u'Set the names of the database fields associated with the data source that will be copied into the terrain.'
##        #return 
##
##    def GetReservedFields(self):
##        u'Returns the names of the database fields associated with the data source that are copied into the terrain.'
##        #return ppFields
##
##    def _get(self):
##        u'The name of the embedded data source.'
##        #return pName
##    def _set(self, pName):
##        u'The name of the embedded data source.'
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates the terrain will copy the data and not have a dependency on the data source after the terrain is built.'
##        #return pbToBeEmbedded
##    def _set(self, pbToBeEmbedded):
##        u'Indicates the terrain will copy the data and not have a dependency on the data source after the terrain is built.'
##    ToBeEmbedded = property(_get, _set, doc = _set.__doc__)
##

class ICadastralFabric2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control a cadastral fabric and its associated cadastral jobs.'
    _iid_ = GUID('{B6379408-3F07-4836-89F9-67610D2F74CE}')
    _idlflags_ = ['oleautomation', 'hidden']
ICadastralFabric2._methods_ = [
    COMMETHOD([helpstring(u'Creates a cadastral packet without a linked job.')], HRESULT, 'CreateCadastralPacket',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IProjectedCoordinateSystem), 'OutputProjectedCoordSys' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFIDSet), 'PlanIDs' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'TrackCancel' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLStream)), 'XMLStream' )),
    COMMETHOD([helpstring(u'Saves the cadastral packet and creates a new job if there are new parcels..')], HRESULT, 'InsertCadastralPacket',
              ( ['in'], POINTER(ICadastralJob), 'NewCadastralJobDefinition' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLStream), 'XMLStream' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'CancelTracker' ),
              ( ['in', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFIDSet)), 'InsertedParcelOIDs' )),
    COMMETHOD([helpstring(u'Creates/Extracts a cadastral packet for the specified job.')], HRESULT, 'ExtractCadastralPacket',
              ( ['in'], BSTR, 'JobName' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IProjectedCoordinateSystem), 'OutputProjectedCoordSys' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'TrackCancel' ),
              ( ['in'], VARIANT_BOOL, 'IncludeWhiteSpace' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLStream)), 'XMLStream' )),
    COMMETHOD([helpstring(u'Saves the cadastral packet for the job.')], HRESULT, 'PostCadastralPacket',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLStream), 'XMLStream' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'CancelTracker' ),
              ( ['in', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFIDSet)), 'InsertedParcelOIDs' )),
]
################################################################
## code template for ICadastralFabric2 implementation
##class ICadastralFabric2_Impl(object):
##    def PostCadastralPacket(self, XMLStream, CancelTracker):
##        u'Saves the cadastral packet for the job.'
##        #return InsertedParcelOIDs
##
##    def ExtractCadastralPacket(self, JobName, OutputProjectedCoordSys, TrackCancel, IncludeWhiteSpace):
##        u'Creates/Extracts a cadastral packet for the specified job.'
##        #return XMLStream
##
##    def CreateCadastralPacket(self, OutputProjectedCoordSys, PlanIDs, TrackCancel):
##        u'Creates a cadastral packet without a linked job.'
##        #return XMLStream
##
##    def InsertCadastralPacket(self, NewCadastralJobDefinition, XMLStream, CancelTracker):
##        u'Saves the cadastral packet and creates a new job if there are new parcels..'
##        #return InsertedParcelOIDs
##

class IGPTerrainMembership(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u"Provides access to members that describe the properties of a feature class' terrain membership."
    _iid_ = GUID('{718AD44A-B78F-43E3-8087-EE37CB18AC80}')
    _idlflags_ = ['oleautomation']
IGPTerrainMembership._methods_ = [
    COMMETHOD(['propget', helpstring(u'The name of the terrain this feature class participates in.')], HRESULT, 'TerrainName',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propput', helpstring(u'The name of the terrain this feature class participates in.')], HRESULT, 'TerrainName',
              ( ['in'], BSTR, 'Name' )),
]
################################################################
## code template for IGPTerrainMembership implementation
##class IGPTerrainMembership_Impl(object):
##    def _get(self):
##        u'The name of the terrain this feature class participates in.'
##        #return Name
##    def _set(self, Name):
##        u'The name of the terrain this feature class participates in.'
##    TerrainName = property(_get, _set, doc = _set.__doc__)
##

class TerrainToRasterFunction(CoClass):
    u'The TerrainToRasterFunction class.'
    _reg_clsid_ = GUID('{D4D3A0BB-3770-40EF-ACF1-BB3C1C98A38E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
TerrainToRasterFunction._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._8F0541A3_D5BE_4B3F_A8D9_062D5579E19B_0_10_2.IRasterFunction, comtypes.gen._8F0541A3_D5BE_4B3F_A8D9_062D5579E19B_0_10_2.IRasterFunction2, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLVersionSupport]


# values for enumeration 'esriTerrainLasReturnType'
esriTerrainLasReturn1 = 1
esriTerrainLasReturn2 = 2
esriTerrainLasReturn3 = 3
esriTerrainLasReturn4 = 4
esriTerrainLasReturn5 = 5
esriTerrainLasReturn6 = 6
esriTerrainLasReturn7 = 7
esriTerrainLasReturn8 = 8
esriTerrainLasReturnLast = 256
esriTerrainLasReturnSingle = 257
esriTerrainLasReturnFirstOfMany = 258
esriTerrainLasReturnLastOfMany = 259
esriTerrainLasReturnAll = -1
esriTerrainLasReturnType = c_int # enum

# values for enumeration 'enumPurgeRule'
enumOldest = 0
enumKeepLatest = 1
enumPurgeRule = c_int # enum

# values for enumeration 'esriTxFeatureClassCachingMode'
esriTFCMNone = 0
esriTFCMCacheAll = 3
esriTxFeatureClassCachingMode = c_int # enum
class ITxFeatureClass(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to tracking feature class.'
    _iid_ = GUID('{B7A65DDE-9218-4E42-8C62-299AC695A66A}')
    _idlflags_ = ['nonextensible', 'oleautomation']
ITxFeatureClass._methods_ = [
    COMMETHOD(['propget', helpstring(u'The internal feature class.')], HRESULT, 'FeatureClass',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass)), 'FeatureClass' )),
    COMMETHOD(['propputref', helpstring(u'The internal feature class.')], HRESULT, 'FeatureClass',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'FeatureClass' )),
    COMMETHOD(['propget', helpstring(u'The feature class caching mode.')], HRESULT, 'CachingMode',
              ( ['retval', 'out'], POINTER(esriTxFeatureClassCachingMode), 'CachingMode' )),
    COMMETHOD(['propput', helpstring(u'The feature class caching mode.')], HRESULT, 'CachingMode',
              ( ['in'], esriTxFeatureClassCachingMode, 'CachingMode' )),
    COMMETHOD(['propget', helpstring(u'The name of the field used to group features into tracks.')], HRESULT, 'TrackIDFieldName',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propput', helpstring(u'The name of the field used to group features into tracks.')], HRESULT, 'TrackIDFieldName',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD(['propget', helpstring(u'The feature start time field name.')], HRESULT, 'StartTimeFieldName',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propput', helpstring(u'The feature start time field name.')], HRESULT, 'StartTimeFieldName',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD(['propget', helpstring(u'The feature end time field name.')], HRESULT, 'EndTimeFieldName',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propput', helpstring(u'The feature end time field name.')], HRESULT, 'EndTimeFieldName',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD(['propget', helpstring(u'The format used to parse time fields.')], HRESULT, 'TimeFieldFormat',
              ( ['retval', 'out'], POINTER(BSTR), 'TimeFieldFormat' )),
    COMMETHOD(['propput', helpstring(u'The format used to parse time fields.')], HRESULT, 'TimeFieldFormat',
              ( ['in'], BSTR, 'TimeFieldFormat' )),
    COMMETHOD(['propget', helpstring(u'Custom string representation of the AM symbol.')], HRESULT, 'TimeFieldAmFormat',
              ( ['retval', 'out'], POINTER(BSTR), 'amFormat' )),
    COMMETHOD(['propput', helpstring(u'Custom string representation of the AM symbol.')], HRESULT, 'TimeFieldAmFormat',
              ( ['in'], BSTR, 'amFormat' )),
    COMMETHOD(['propget', helpstring(u'Custom string representation of the PM symbol.')], HRESULT, 'TimeFieldPmFormat',
              ( ['retval', 'out'], POINTER(BSTR), 'pmFormat' )),
    COMMETHOD(['propput', helpstring(u'Custom string representation of the PM symbol.')], HRESULT, 'TimeFieldPmFormat',
              ( ['in'], BSTR, 'pmFormat' )),
    COMMETHOD(['propget', helpstring(u'Language identifier to be used when parsing time fields from a custom time string.')], HRESULT, 'TimeFieldLocaleID',
              ( ['retval', 'out'], POINTER(c_int), 'localeID' )),
    COMMETHOD(['propput', helpstring(u'Language identifier to be used when parsing time fields from a custom time string.')], HRESULT, 'TimeFieldLocaleID',
              ( ['in'], c_int, 'localeID' )),
    COMMETHOD([helpstring(u'Re-build the temporal index and cache, according to the ITxFeatureClass properties and given parameters.')], HRESULT, 'IndexFeatureClass2',
              ( ['in'], VARIANT, 'startingTime' ),
              ( ['in'], VARIANT, 'endingTime' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ISelectionSet), 'selSet' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IQueryFilter), 'QueryFilter' )),
    COMMETHOD([helpstring(u'Re-build the temporal index and cache, according to the ITxFeatureClass properties.')], HRESULT, 'RebuildIndex'),
]
################################################################
## code template for ITxFeatureClass implementation
##class ITxFeatureClass_Impl(object):
##    def _get(self):
##        u'Language identifier to be used when parsing time fields from a custom time string.'
##        #return localeID
##    def _set(self, localeID):
##        u'Language identifier to be used when parsing time fields from a custom time string.'
##    TimeFieldLocaleID = property(_get, _set, doc = _set.__doc__)
##
##    def RebuildIndex(self):
##        u'Re-build the temporal index and cache, according to the ITxFeatureClass properties.'
##        #return 
##
##    def _get(self):
##        u'Custom string representation of the PM symbol.'
##        #return pmFormat
##    def _set(self, pmFormat):
##        u'Custom string representation of the PM symbol.'
##    TimeFieldPmFormat = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The feature class caching mode.'
##        #return CachingMode
##    def _set(self, CachingMode):
##        u'The feature class caching mode.'
##    CachingMode = property(_get, _set, doc = _set.__doc__)
##
##    def FeatureClass(self, FeatureClass):
##        u'The internal feature class.'
##        #return 
##
##    def IndexFeatureClass2(self, startingTime, endingTime, selSet, QueryFilter):
##        u'Re-build the temporal index and cache, according to the ITxFeatureClass properties and given parameters.'
##        #return 
##
##    def _get(self):
##        u'Custom string representation of the AM symbol.'
##        #return amFormat
##    def _set(self, amFormat):
##        u'Custom string representation of the AM symbol.'
##    TimeFieldAmFormat = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The feature start time field name.'
##        #return Name
##    def _set(self, Name):
##        u'The feature start time field name.'
##    StartTimeFieldName = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The feature end time field name.'
##        #return Name
##    def _set(self, Name):
##        u'The feature end time field name.'
##    EndTimeFieldName = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The format used to parse time fields.'
##        #return TimeFieldFormat
##    def _set(self, TimeFieldFormat):
##        u'The format used to parse time fields.'
##    TimeFieldFormat = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The name of the field used to group features into tracks.'
##        #return Name
##    def _set(self, Name):
##        u'The name of the field used to group features into tracks.'
##    TrackIDFieldName = property(_get, _set, doc = _set.__doc__)
##

class CadastralUnitConversion(CoClass):
    u'Converts distance values from one unit to another.'
    _reg_clsid_ = GUID('{C99A1138-F8B4-4113-862C-EC5407453301}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
class ICadastralUnitConversion(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods that allow a distance to be converted from one unit to another.'
    _iid_ = GUID('{F8B45123-3FD5-4F0B-BFA0-F81AE0A79DF9}')
    _idlflags_ = ['oleautomation']
CadastralUnitConversion._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ICadastralUnitConversion]

class ITemporalFeatureClassStatistics(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to properties and methods needed to manage message rate statistics.'
    _iid_ = GUID('{5F007F4D-9FAE-463C-A3D6-0AAD83EB59A5}')
    _idlflags_ = ['oleautomation']
ITemporalFeatureClassStatistics._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates the TemporalFeatureClass track count.')], HRESULT, 'TrackCount',
              ( ['retval', 'out'], POINTER(c_int), 'plTrackCount' )),
    COMMETHOD(['propget', helpstring(u'Indicates the TemporalFeatureClass message rate.')], HRESULT, 'MessageRate',
              ( ['retval', 'out'], POINTER(c_double), 'pdMessageRate' )),
    COMMETHOD(['propget', helpstring(u'Indicates the sample size used to calculate message rate.')], HRESULT, 'SampleSize',
              ( ['retval', 'out'], POINTER(c_int), 'plSampleSize' )),
    COMMETHOD(['propput', helpstring(u'Indicates the sample size used to calculate message rate.')], HRESULT, 'SampleSize',
              ( ['in'], c_int, 'plSampleSize' )),
    COMMETHOD(['propget', helpstring(u'Indicates the total number of features logged.')], HRESULT, 'TotalFeatureCount',
              ( ['retval', 'out'], POINTER(VARIANT), 'pvarTotalFeatureCount' )),
    COMMETHOD([helpstring(u'Resets total feature count.')], HRESULT, 'ResetFeatureCount'),
    COMMETHOD([helpstring(u'Resets message rate.')], HRESULT, 'ResetMessageRate'),
]
################################################################
## code template for ITemporalFeatureClassStatistics implementation
##class ITemporalFeatureClassStatistics_Impl(object):
##    @property
##    def TotalFeatureCount(self):
##        u'Indicates the total number of features logged.'
##        #return pvarTotalFeatureCount
##
##    def ResetMessageRate(self):
##        u'Resets message rate.'
##        #return 
##
##    def ResetFeatureCount(self):
##        u'Resets total feature count.'
##        #return 
##
##    @property
##    def TrackCount(self):
##        u'Indicates the TemporalFeatureClass track count.'
##        #return plTrackCount
##
##    def _get(self):
##        u'Indicates the sample size used to calculate message rate.'
##        #return plSampleSize
##    def _set(self, plSampleSize):
##        u'Indicates the sample size used to calculate message rate.'
##    SampleSize = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def MessageRate(self):
##        u'Indicates the TemporalFeatureClass message rate.'
##        #return pdMessageRate
##

class IDETerrainType(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the Terrain Data Element Type.'
    _iid_ = GUID('{6AF7C569-8EB6-491D-8623-4714A2F626B6}')
    _idlflags_ = ['oleautomation']
IDETerrainType._methods_ = [
]
################################################################
## code template for IDETerrainType implementation
##class IDETerrainType_Impl(object):

class IEnumEnvelope(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to envelopes.'
    _iid_ = GUID('{DBA7C9D4-ACE6-4973-89AA-3313A7D5D853}')
    _idlflags_ = ['oleautomation']
IEnumEnvelope._methods_ = [
    COMMETHOD(['propget', helpstring(u'The number of envelopes contained.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'pCount' )),
    COMMETHOD([helpstring(u'Resets the enumerator.')], HRESULT, 'Reset'),
    COMMETHOD([helpstring(u'Gets next envelope.')], HRESULT, 'Next',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'ppEnvelope' )),
    COMMETHOD([helpstring(u'Gets next envelope.')], HRESULT, 'QueryNext',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'pEnvelope' )),
]
################################################################
## code template for IEnumEnvelope implementation
##class IEnumEnvelope_Impl(object):
##    @property
##    def Count(self):
##        u'The number of envelopes contained.'
##        #return pCount
##
##    def Reset(self):
##        u'Resets the enumerator.'
##        #return 
##
##    def QueryNext(self, pEnvelope):
##        u'Gets next envelope.'
##        #return 
##
##    def Next(self):
##        u'Gets next envelope.'
##        #return ppEnvelope
##

class IAMSDatasetName(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetName):
    _case_insensitive_ = True
    u'Provides access to properties and methods needed to manage dataset names in the tracking workspace.'
    _iid_ = GUID('{A677AB64-2FB8-11D5-B7E2-00010265ADC5}')
    _idlflags_ = ['oleautomation']
class ITrackingServiceDef(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to properties that define a tracking service.'
    _iid_ = GUID('{1B9C2538-3B1D-11D5-B7E4-00010265ADC5}')
    _idlflags_ = ['oleautomation']
IAMSDatasetName._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates whether or not the dataset name is visible in the workspace dialog.')], HRESULT, 'Visible',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether or not the dataset name is visible in the workspace dialog.')], HRESULT, 'Visible',
              ( ['in'], VARIANT_BOOL, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Name of the column containing the time and date information.')], HRESULT, 'TemporalColumnName',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Defines a tracking service within the real-time data connection in the workspace.')], HRESULT, 'TrackingService',
              ( ['retval', 'out'], POINTER(POINTER(ITrackingServiceDef)), 'pVal' )),
    COMMETHOD(['hidden', helpstring(u'Defines a tracking service within the real-time data connection in the workspace.'), 'propputref'], HRESULT, 'TrackingService',
              ( ['in'], POINTER(ITrackingServiceDef), 'pVal' )),
    COMMETHOD(['propget', helpstring(u'The feature class shape type.')], HRESULT, 'ShapeType',
              ( ['retval', 'out'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.esriGeometryType), 'Type' )),
    COMMETHOD(['propput', helpstring(u'The feature class shape type.')], HRESULT, 'ShapeType',
              ( ['in'], comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.esriGeometryType, 'Type' )),
    COMMETHOD(['propget', helpstring(u'The Feature Dataset Name object.')], HRESULT, 'FeatureDatasetName',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetName)), 'FeatureDatasetName' )),
    COMMETHOD(['propputref', helpstring(u'The Feature Dataset Name object.')], HRESULT, 'FeatureDatasetName',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetName), 'FeatureDatasetName' )),
    COMMETHOD(['propget', helpstring(u'The feature type for this feature class name.')], HRESULT, 'FeatureType',
              ( ['retval', 'out'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriFeatureType), 'Type' )),
    COMMETHOD(['propput', helpstring(u'The feature type for this feature class name.')], HRESULT, 'FeatureType',
              ( ['in'], comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriFeatureType, 'Type' )),
    COMMETHOD(['propget', helpstring(u'The spatial column name for this feature class name.')], HRESULT, 'ShapeFieldName',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propput', helpstring(u'The spatial column name for this feature class name.')], HRESULT, 'ShapeFieldName',
              ( ['in'], BSTR, 'Name' )),
]
################################################################
## code template for IAMSDatasetName implementation
##class IAMSDatasetName_Impl(object):
##    def _get(self):
##        u'The feature type for this feature class name.'
##        #return Type
##    def _set(self, Type):
##        u'The feature type for this feature class name.'
##    FeatureType = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The spatial column name for this feature class name.'
##        #return Name
##    def _set(self, Name):
##        u'The spatial column name for this feature class name.'
##    ShapeFieldName = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The feature class shape type.'
##        #return Type
##    def _set(self, Type):
##        u'The feature class shape type.'
##    ShapeType = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def TemporalColumnName(self):
##        u'Name of the column containing the time and date information.'
##        #return pVal
##
##    def _get(self):
##        u'Indicates whether or not the dataset name is visible in the workspace dialog.'
##        #return pVal
##    def _set(self, pVal):
##        u'Indicates whether or not the dataset name is visible in the workspace dialog.'
##    Visible = property(_get, _set, doc = _set.__doc__)
##
##    def FeatureDatasetName(self, FeatureDatasetName):
##        u'The Feature Dataset Name object.'
##        #return 
##
##    def TrackingService(self, pVal):
##        u'Defines a tracking service within the real-time data connection in the workspace.'
##        #return 
##

class ITemporalQueryFilter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to properties and methods needed to manage temporal query filters.'
    _iid_ = GUID('{D0CEE203-56DA-11D5-AE49-00104BA2ABCC}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'enumTemporalOrder'
ASCENDING = 0
DESCENDING = 1
enumTemporalOrder = c_int # enum

# values for enumeration 'enumTemporalRelation'
enumTemporalRelationIntersects = 0
enumTemporalRelationContains = 1
enumTemporalRelation = c_int # enum

# values for enumeration 'enumTemporalConversion'
enumTemporalConversionNone = 0
enumTemporalConversionToString = 1
enumTemporalConversionToOLEDate = 2
enumTemporalConversion = c_int # enum
class ITemporalOperator(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods and properties used to identify and manage temporal playback settings.'
    _iid_ = GUID('{56AE7150-7BFC-11D6-B84D-00010265ADC5}')
    _idlflags_ = ['oleautomation']
ITemporalQueryFilter._methods_ = [
    COMMETHOD(['propget', helpstring(u'Defines order in which temporal records are sorted.')], HRESULT, 'TemporalOrder',
              ( ['retval', 'out'], POINTER(enumTemporalOrder), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Defines order in which temporal records are sorted.')], HRESULT, 'TemporalOrder',
              ( ['in'], enumTemporalOrder, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'The temporal relation used in the temporal query.')], HRESULT, 'TemporalRelationship',
              ( ['retval', 'out'], POINTER(enumTemporalRelation), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'The temporal relation used in the temporal query.')], HRESULT, 'TemporalRelationship',
              ( ['in'], enumTemporalRelation, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Indicates the earliest date included in the query.')], HRESULT, 'StartingDate',
              ( ['retval', 'out'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Indicates the earliest date included in the query.')], HRESULT, 'StartingDate',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Indicates the latest date included in the query.')], HRESULT, 'EndingDate',
              ( ['retval', 'out'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Indicates the latest date included in the query.')], HRESULT, 'EndingDate',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'The temporal conversion mode to use (if any) by the temporal query.')], HRESULT, 'TemporalConversion',
              ( ['retval', 'out'], POINTER(enumTemporalConversion), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'The temporal conversion mode to use (if any) by the temporal query.')], HRESULT, 'TemporalConversion',
              ( ['in'], enumTemporalConversion, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'The object that contains a relative time to offset the temporal values.')], HRESULT, 'RelativeTimeOperator',
              ( ['retval', 'out'], POINTER(POINTER(ITemporalOperator)), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'The object that contains a relative time to offset the temporal values.')], HRESULT, 'RelativeTimeOperator',
              ( ['in'], POINTER(ITemporalOperator), 'pVal' )),
]
################################################################
## code template for ITemporalQueryFilter implementation
##class ITemporalQueryFilter_Impl(object):
##    def _get(self):
##        u'Indicates the earliest date included in the query.'
##        #return pVal
##    def _set(self, pVal):
##        u'Indicates the earliest date included in the query.'
##    StartingDate = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Defines order in which temporal records are sorted.'
##        #return pVal
##    def _set(self, pVal):
##        u'Defines order in which temporal records are sorted.'
##    TemporalOrder = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates the latest date included in the query.'
##        #return pVal
##    def _set(self, pVal):
##        u'Indicates the latest date included in the query.'
##    EndingDate = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The temporal conversion mode to use (if any) by the temporal query.'
##        #return pVal
##    def _set(self, pVal):
##        u'The temporal conversion mode to use (if any) by the temporal query.'
##    TemporalConversion = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The object that contains a relative time to offset the temporal values.'
##        #return pVal
##    def _set(self, pVal):
##        u'The object that contains a relative time to offset the temporal values.'
##    RelativeTimeOperator = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The temporal relation used in the temporal query.'
##        #return pVal
##    def _set(self, pVal):
##        u'The temporal relation used in the temporal query.'
##    TemporalRelationship = property(_get, _set, doc = _set.__doc__)
##

class LasStatistics(CoClass):
    u'Esri LasStatistics object.'
    _reg_clsid_ = GUID('{A3CB49F5-6CDB-4911-BB7B-7E4B39C4D2EE}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
class ILasStatistics(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of LasFile.'
    _iid_ = GUID('{23AFC48E-4EFB-479F-9164-959E70E01918}')
    _idlflags_ = ['oleautomation']
LasStatistics._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ILasStatistics]

class IParcelConstructionData(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods that read and write a parcel contruction to the cadastral packet.'
    _iid_ = GUID('{FC722D60-D2DC-4DFE-8524-3AC3369BBE68}')
    _idlflags_ = ['oleautomation']
IParcelConstructionData._methods_ = [
    COMMETHOD(['propget', helpstring(u'The parcel network No.')], HRESULT, 'ParcelNo',
              ( ['retval', 'out'], POINTER(c_int), 'ParcelNo' )),
    COMMETHOD(['propput', helpstring(u'The parcel network No.')], HRESULT, 'ParcelNo',
              ( ['in'], c_int, 'ParcelNo' )),
    COMMETHOD([helpstring(u'Appends construction data as XML to parcel node.')], HRESULT, 'WriteToXML',
              ( ['in'], POINTER(IUnknown), 'pXMLDoc' )),
    COMMETHOD([helpstring(u'Populates the construction data object properties by reading the properties from the xml parcel node.')], HRESULT, 'LoadConstructionDataFromXML',
              ( ['in'], POINTER(IUnknown), 'pXMLParcelNode' )),
    COMMETHOD([helpstring(u'Writes construction data in XML format to a string.')], HRESULT, 'ExportToXMLString',
              ( ['retval', 'out'], POINTER(BSTR), 'XMLString' )),
    COMMETHOD([helpstring(u'Populates the construction data object properties by reading the xml string.')], HRESULT, 'LoadConstructionDataFromXMLString',
              ( ['in'], BSTR, 'XMLString' )),
]
################################################################
## code template for IParcelConstructionData implementation
##class IParcelConstructionData_Impl(object):
##    def LoadConstructionDataFromXMLString(self, XMLString):
##        u'Populates the construction data object properties by reading the xml string.'
##        #return 
##
##    def _get(self):
##        u'The parcel network No.'
##        #return ParcelNo
##    def _set(self, ParcelNo):
##        u'The parcel network No.'
##    ParcelNo = property(_get, _set, doc = _set.__doc__)
##
##    def ExportToXMLString(self):
##        u'Writes construction data in XML format to a string.'
##        #return XMLString
##
##    def LoadConstructionDataFromXML(self, pXMLParcelNode):
##        u'Populates the construction data object properties by reading the properties from the xml parcel node.'
##        #return 
##
##    def WriteToXML(self, pXMLDoc):
##        u'Appends construction data as XML to parcel node.'
##        #return 
##


# values for enumeration 'esriCadastralFabricType'
esriCadastralMap = 0
esriCadastralSurvey = 1
esriCadastralFabricType = c_int # enum
class ICadastralFabricLocks(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that assign object locks for a cadastral job.'
    _iid_ = GUID('{C8BE9A26-2FD5-4D41-A70B-7E000B644C41}')
    _idlflags_ = ['oleautomation']
ICadastralFabricLocks._methods_ = [
    COMMETHOD(['propput', helpstring(u'The name of the Job to apply locks on.')], HRESULT, 'LockingJob',
              ( ['in'], BSTR, 'rhs' )),
    COMMETHOD([helpstring(u'Acquire locks on the LockingJob. TakeSoftLocks allows locks to be transferred from other jobs in the same version.')], HRESULT, 'AcquireLocks',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray), 'pLocks' ),
              ( ['in'], VARIANT_BOOL, 'TakeSoftLocks' ),
              ( ['in', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray)), 'ppLocksInConflict' ),
              ( ['in', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray)), 'ppSoftLocksInConflict' )),
    COMMETHOD([helpstring(u'Rolls back most recent set of acquired locks, until last edit operation. Only effective once.')], HRESULT, 'UndoLastAcquiredLocks'),
    COMMETHOD([helpstring(u'Lock current job. An existing lock will cause failure.')], HRESULT, 'LockJob',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Succeed' )),
    COMMETHOD([helpstring(u"Release current job's lock.")], HRESULT, 'ReleaseJobLock',
              ( ['in'], VARIANT_BOOL, 'ForceRelease' )),
    COMMETHOD([helpstring(u'Correct orphan job locks for current machine, and return current lock information.')], HRESULT, 'ValidateJobLock',
              ( ['in', 'out'], POINTER(VARIANT_BOOL), 'Locked' ),
              ( ['in', 'out'], POINTER(BSTR), 'LockingMachine' ),
              ( ['in', 'out'], POINTER(c_int), 'LockingPID' )),
]
################################################################
## code template for ICadastralFabricLocks implementation
##class ICadastralFabricLocks_Impl(object):
##    def _set(self, rhs):
##        u'The name of the Job to apply locks on.'
##    LockingJob = property(fset = _set, doc = _set.__doc__)
##
##    def ReleaseJobLock(self, ForceRelease):
##        u"Release current job's lock."
##        #return 
##
##    def ValidateJobLock(self):
##        u'Correct orphan job locks for current machine, and return current lock information.'
##        #return Locked, LockingMachine, LockingPID
##
##    def AcquireLocks(self, pLocks, TakeSoftLocks):
##        u'Acquire locks on the LockingJob. TakeSoftLocks allows locks to be transferred from other jobs in the same version.'
##        #return ppLocksInConflict, ppSoftLocksInConflict
##
##    def UndoLastAcquiredLocks(self):
##        u'Rolls back most recent set of acquired locks, until last edit operation. Only effective once.'
##        #return 
##
##    def LockJob(self):
##        u'Lock current job. An existing lock will cause failure.'
##        #return Succeed
##

class _RGB32(Structure):
    pass
_RGB32._fields_ = [
    ('Red', c_int),
    ('Green', c_int),
    ('Blue', c_int),
]
assert sizeof(_RGB32) == 12, sizeof(_RGB32)
assert alignment(_RGB32) == 4, alignment(_RGB32)
class IConstructionJoinLinks(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manipulate the join point links for a parcel construction.'
    _iid_ = GUID('{646FCA02-4B1D-4844-A083-9911EF6CFA7B}')
    _idlflags_ = ['oleautomation']
IConstructionJoinLinks._methods_ = [
    COMMETHOD(['propget', helpstring(u'The number of join links for the parcel construction data.')], HRESULT, 'JoinLinkCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD([helpstring(u'Adds a join link to the parcel construction data.')], HRESULT, 'AddJoinLink',
              ( ['in'], c_int, 'JoinedPointNo' ),
              ( ['in'], c_int, 'UnjoinedPointNo' ),
              ( ['in'], c_int, 'fromPointNo' ),
              ( ['in'], c_int, 'toPointNo' ),
              ( ['in'], c_int, 'ParcelNo' )),
    COMMETHOD([helpstring(u'Retrieves the join link at the given index.')], HRESULT, 'GetJoinLink',
              ( ['in'], c_int, 'i' ),
              ( ['in', 'out'], POINTER(c_int), 'JoinedPointNo' ),
              ( ['in', 'out'], POINTER(c_int), 'UnjoinedPointNo' ),
              ( ['in', 'out'], POINTER(c_int), 'fromPointNo' ),
              ( ['in', 'out'], POINTER(c_int), 'toPointNo' ),
              ( ['in', 'out'], POINTER(c_int), 'ParcelNo' )),
    COMMETHOD([helpstring(u'Remove join link at the given index.')], HRESULT, 'RemoveJoinLink',
              ( ['in'], c_int, 'i' )),
    COMMETHOD([helpstring(u'Clears join links.')], HRESULT, 'ClearJoinLinks'),
]
################################################################
## code template for IConstructionJoinLinks implementation
##class IConstructionJoinLinks_Impl(object):
##    @property
##    def JoinLinkCount(self):
##        u'The number of join links for the parcel construction data.'
##        #return Count
##
##    def ClearJoinLinks(self):
##        u'Clears join links.'
##        #return 
##
##    def RemoveJoinLink(self, i):
##        u'Remove join link at the given index.'
##        #return 
##
##    def AddJoinLink(self, JoinedPointNo, UnjoinedPointNo, fromPointNo, toPointNo, ParcelNo):
##        u'Adds a join link to the parcel construction data.'
##        #return 
##
##    def GetJoinLink(self, i):
##        u'Retrieves the join link at the given index.'
##        #return JoinedPointNo, UnjoinedPointNo, fromPointNo, toPointNo, ParcelNo
##

class IDECadastralFabric3(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that describe cadastral fabric data elements.'
    _iid_ = GUID('{7620970C-AEF2-41EA-85A9-21C3829EA070}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriCadastralPropertySetType'
esriCadastralPropSetUserDefined = 0
esriCadastralPropSetImporterLoading = 1
esriCadastralPropSetCoordinateTolerances = 2
esriCadastralPropSetEditSettings = 3
esriCadastralPropSetCatalogDataset = 4
esriCadastralPropertySetType = c_int # enum
IDECadastralFabric3._methods_ = [
    COMMETHOD([helpstring(u'Property set of the parcel fabric data element.')], HRESULT, 'GetPropertySet',
              ( ['in'], esriCadastralPropertySetType, 'Type' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'propertySet' )),
    COMMETHOD([helpstring(u'Property set of the parcel fabric data element.')], HRESULT, 'SetPropertySet',
              ( ['in'], esriCadastralPropertySetType, 'Type' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'propertySet' )),
]
################################################################
## code template for IDECadastralFabric3 implementation
##class IDECadastralFabric3_Impl(object):
##    def SetPropertySet(self, Type, propertySet):
##        u'Property set of the parcel fabric data element.'
##        #return 
##
##    def GetPropertySet(self, Type):
##        u'Property set of the parcel fabric data element.'
##        #return propertySet
##

class ICadastralFabric(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control a cadastral fabric and its associated cadastral jobs.'
    _iid_ = GUID('{F9E240B1-D806-4388-AFDE-B1A5D354171F}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriCadastralJob'
esriCFJobAll = -1
esriCFJobActive = 0
esriCFJobCommitted = 1
esriCadastralJob = c_int # enum

# values for enumeration 'esriCadastralFabricTable'
esriCFTControl = 0
esriCFTPoints = 1
esriCFTLines = 2
esriCFTParcels = 3
esriCFTPlans = 4
esriCFTJobs = 5
esriCFTLinePoints = 6
esriCFTHistory = 7
esriCFTAdjustments = 8
esriCFTVectors = 9
esriCFTJobObjects = 10
esriCFTLevels = 11
esriCFTAccuracy = 12
esriCadastralFabricTable = c_int # enum
ICadastralFabric._methods_ = [
    COMMETHOD([helpstring(u'Creates a new cadastral job with the properties of the given CadastralJob object.')], HRESULT, 'CreateJob',
              ( ['in'], POINTER(ICadastralJob), 'Job' ),
              ( ['retval', 'out'], POINTER(c_int), 'JobID' )),
    COMMETHOD([helpstring(u'Retrieves a cadastral job given its name.')], HRESULT, 'GetJob',
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(POINTER(ICadastralJob)), 'Job' )),
    COMMETHOD([helpstring(u'Updates the existing job.')], HRESULT, 'UpdateJob',
              ( ['in'], POINTER(ICadastralJob), 'Job' )),
    COMMETHOD([helpstring(u'Deletes the existing job.')], HRESULT, 'DeleteJob',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD([helpstring(u'Creates/Extracts a cadastral packet for the specified job.')], HRESULT, 'ExtractCadastralPacket',
              ( ['in'], BSTR, 'JobName' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IProjectedCoordinateSystem), 'OutputProjectedCoordSys' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'TrackCancel' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLStream)), 'XMLStream' )),
    COMMETHOD([helpstring(u'Saves the cadastral packet for the job.')], HRESULT, 'PostCadastralPacket',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLStream), 'XMLStream' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'CancelTracker' )),
    COMMETHOD([helpstring(u'Commits the specified job to the cadastral fabric.')], HRESULT, 'CommitJob',
              ( ['in'], BSTR, 'JobName' )),
    COMMETHOD(['propget', helpstring(u'The cadastral jobs that have not been committed.')], HRESULT, 'CadastralJobs',
              ( ['in'], esriCadastralJob, 'cadastralJobType' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IEnumBSTR)), 'CadastralJobs' )),
    COMMETHOD(['propget', helpstring(u'The cadastral fabric class at the specified enumeration.')], HRESULT, 'CadastralTable',
              ( ['in'], esriCadastralFabricTable, 'TableID' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable)), 'Table' )),
]
################################################################
## code template for ICadastralFabric implementation
##class ICadastralFabric_Impl(object):
##    def UpdateJob(self, Job):
##        u'Updates the existing job.'
##        #return 
##
##    def CreateJob(self, Job):
##        u'Creates a new cadastral job with the properties of the given CadastralJob object.'
##        #return JobID
##
##    @property
##    def CadastralTable(self, TableID):
##        u'The cadastral fabric class at the specified enumeration.'
##        #return Table
##
##    def PostCadastralPacket(self, XMLStream, CancelTracker):
##        u'Saves the cadastral packet for the job.'
##        #return 
##
##    def ExtractCadastralPacket(self, JobName, OutputProjectedCoordSys, TrackCancel):
##        u'Creates/Extracts a cadastral packet for the specified job.'
##        #return XMLStream
##
##    @property
##    def CadastralJobs(self, cadastralJobType):
##        u'The cadastral jobs that have not been committed.'
##        #return CadastralJobs
##
##    def DeleteJob(self, Name):
##        u'Deletes the existing job.'
##        #return 
##
##    def GetJob(self, Name):
##        u'Retrieves a cadastral job given its name.'
##        #return Job
##
##    def CommitJob(self, JobName):
##        u'Commits the specified job to the cadastral fabric.'
##        #return 
##


# values for enumeration 'esriTerrainAsciiDataFormatType'
esriTerrainAsciiDataFormatXYZ = 0
esriTerrainAsciiDataFormatGenerate = 1
esriTerrainAsciiDataFormatXYZI = 2
esriTerrainAsciiDataFormatType = c_int # enum
class ITerrainLasDataInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that provide information about a LAS file.'
    _iid_ = GUID('{C1B7F6D6-4F81-4F5B-9922-5F74D3EB1E94}')
    _idlflags_ = ['oleautomation']
class ITerrainLasDataInfo2(ITerrainLasDataInfo):
    _case_insensitive_ = True
    u'Provides access to members that provide information about a LAS file.'
    _iid_ = GUID('{08AC58E1-F142-45DB-9847-0D28F6D7D241}')
    _idlflags_ = ['oleautomation']
ITerrainLasDataInfo._methods_ = [
    COMMETHOD([helpstring(u'Used to set the name of the LAS file for which information is to be retrieved.')], HRESULT, 'Init',
              ( ['in'], BSTR, 'lasFileName' )),
    COMMETHOD([helpstring(u'The version of the LAS file.')], HRESULT, 'GetVersion',
              ( ['out'], POINTER(c_int), 'pMajor' ),
              ( ['out'], POINTER(c_int), 'pMinor' )),
    COMMETHOD([helpstring(u'The hardware system used to collect the LiDAR data in the LAS file.')], HRESULT, 'GetSystemID',
              ( ['retval', 'out'], POINTER(BSTR), 'pID' )),
    COMMETHOD([helpstring(u'The software used to create the LAS file.')], HRESULT, 'GetGeneratingSoftware',
              ( ['retval', 'out'], POINTER(BSTR), 'pName' )),
    COMMETHOD([helpstring(u'The flight date based on the Julian calendar.')], HRESULT, 'GetFlightDateJulian',
              ( ['retval', 'out'], POINTER(c_int), 'pDate' )),
    COMMETHOD([helpstring(u'The year the data in the LAS file was collected.')], HRESULT, 'GetYear',
              ( ['retval', 'out'], POINTER(c_int), 'pYear' )),
    COMMETHOD([helpstring(u'The record format for points in the LAS file')], HRESULT, 'GetPointDataFormat',
              ( ['retval', 'out'], POINTER(c_int), 'pFormat' )),
    COMMETHOD([helpstring(u'The number of points in the LAS file.')], HRESULT, 'GetNumberOfPointRecords',
              ( ['retval', 'out'], POINTER(c_int), 'pcRecords' )),
    COMMETHOD([helpstring(u'The number of points in the LAS file based on the specified LiDAR return number.')], HRESULT, 'GetNumberOfPointsByReturn',
              ( ['in'], c_int, 'ReturnNumber' ),
              ( ['retval', 'out'], POINTER(c_int), 'pcPoints' )),
    COMMETHOD([helpstring(u'The XYZ extent of points in the LAS file.')], HRESULT, 'GetDataExtent',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'ppExt' )),
    COMMETHOD([helpstring(u'The spatial reference of the LAS file.')], HRESULT, 'GetSpatialReference',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference)), 'ppSpatialReference' )),
]
################################################################
## code template for ITerrainLasDataInfo implementation
##class ITerrainLasDataInfo_Impl(object):
##    def GetSpatialReference(self):
##        u'The spatial reference of the LAS file.'
##        #return ppSpatialReference
##
##    def GetNumberOfPointRecords(self):
##        u'The number of points in the LAS file.'
##        #return pcRecords
##
##    def GetSystemID(self):
##        u'The hardware system used to collect the LiDAR data in the LAS file.'
##        #return pID
##
##    def Init(self, lasFileName):
##        u'Used to set the name of the LAS file for which information is to be retrieved.'
##        #return 
##
##    def GetNumberOfPointsByReturn(self, ReturnNumber):
##        u'The number of points in the LAS file based on the specified LiDAR return number.'
##        #return pcPoints
##
##    def GetGeneratingSoftware(self):
##        u'The software used to create the LAS file.'
##        #return pName
##
##    def GetDataExtent(self):
##        u'The XYZ extent of points in the LAS file.'
##        #return ppExt
##
##    def GetYear(self):
##        u'The year the data in the LAS file was collected.'
##        #return pYear
##
##    def GetPointDataFormat(self):
##        u'The record format for points in the LAS file'
##        #return pFormat
##
##    def GetFlightDateJulian(self):
##        u'The flight date based on the Julian calendar.'
##        #return pDate
##
##    def GetVersion(self):
##        u'The version of the LAS file.'
##        #return pMajor, pMinor
##

ITerrainLasDataInfo2._methods_ = [
    COMMETHOD([helpstring(u"The LAS file's source ID.")], HRESULT, 'GetFileSourceID',
              ( ['retval', 'out'], POINTER(c_int), 'pID' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the GPS time is standard GPS Time.')], HRESULT, 'IsStandardGpsTime',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbIsAStandard' )),
    COMMETHOD([helpstring(u'Get the number of points corresponding to the specified class codes.')], HRESULT, 'GetPointInfoByClassCode',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( [], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray), 'pCodes' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDoubleArray)), 'ppCounts' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IArray)), 'ppExtents' )),
]
################################################################
## code template for ITerrainLasDataInfo2 implementation
##class ITerrainLasDataInfo2_Impl(object):
##    def GetFileSourceID(self):
##        u"The LAS file's source ID."
##        #return pID
##
##    def GetPointInfoByClassCode(self, pTrackCancel, pCodes):
##        u'Get the number of points corresponding to the specified class codes.'
##        #return ppCounts, ppExtents
##
##    @property
##    def IsStandardGpsTime(self):
##        u'Indicates if the GPS time is standard GPS Time.'
##        #return pbIsAStandard
##

class ICadastralAdjustmentVectors(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Create new feature adjustments'
    _iid_ = GUID('{889A386D-4D81-4F8C-8736-5383423DF188}')
    _idlflags_ = ['oleautomation']
ICadastralAdjustmentVectors._methods_ = [
    COMMETHOD([helpstring(u'Add a new vector.')], HRESULT, 'AddVector',
              ( ['in'], c_int, 'PointID' ),
              ( ['in'], c_double, 'fromX' ),
              ( ['in'], c_double, 'fromY' ),
              ( ['in'], c_double, 'toX' ),
              ( ['in'], c_double, 'toY' )),
    COMMETHOD([helpstring(u'Create a new adjustment from the vectors added.')], HRESULT, 'CreateNewAdjustment',
              ( ['retval', 'out'], POINTER(c_int), 'pNewAdjustmentLevel' )),
    COMMETHOD([helpstring(u'Clear all vector data.')], HRESULT, 'ClearVectors'),
]
################################################################
## code template for ICadastralAdjustmentVectors implementation
##class ICadastralAdjustmentVectors_Impl(object):
##    def CreateNewAdjustment(self):
##        u'Create a new adjustment from the vectors added.'
##        #return pNewAdjustmentLevel
##
##    def AddVector(self, PointID, fromX, fromY, toX, toY):
##        u'Add a new vector.'
##        #return 
##
##    def ClearVectors(self):
##        u'Clear all vector data.'
##        #return 
##


# values for enumeration 'enumTemporalOperatorUnits'
enumTemporalOperatorMilliseconds = 0
enumTemporalOperatorSeconds = 1
enumTemporalOperatorMinutes = 2
enumTemporalOperatorHours = 3
enumTemporalOperatorDays = 4
enumTemporalOperatorWeeks = 5
enumTemporalOperatorMonths = 6
enumTemporalOperatorYears = 7
enumTemporalOperatorUnits = c_int # enum

# values for enumeration 'enumTemporalOperatorType'
enumTemporalOperatorDateTime = 0
enumTemporalOperatorInterval = 1
enumTemporalOperatorType = c_int # enum
ITemporalOperator._methods_ = [
    COMMETHOD([helpstring(u'Sets the value for date and time information.')], HRESULT, 'SetDateTime',
              ( ['in'], c_int, 'lYear' ),
              ( ['in'], c_short, 'lMonth' ),
              ( ['in'], c_short, 'lDayOfMonth' ),
              ( ['in'], c_short, 'lHour' ),
              ( ['in'], c_short, 'lMinute' ),
              ( ['in'], c_short, 'lSecond' ),
              ( ['in'], c_short, 'lMillisecond' )),
    COMMETHOD([helpstring(u'Sets the playback time interval between events.')], HRESULT, 'SetInterval',
              ( ['in'], c_double, 'dQuantity' ),
              ( ['in'], enumTemporalOperatorUnits, 'enumUnits' )),
    COMMETHOD(['propget', helpstring(u'The type of temporal data used.')], HRESULT, 'Type',
              ( ['retval', 'out'], POINTER(enumTemporalOperatorType), 'pVal' )),
    COMMETHOD([helpstring(u'Resets the temporal operator.')], HRESULT, 'Reset'),
    COMMETHOD([helpstring(u'Adds a new temporal operator.')], HRESULT, 'Add',
              ( ['in'], POINTER(ITemporalOperator), 'piOtherOperator' )),
    COMMETHOD([helpstring(u'Subtracts a temporal operator.')], HRESULT, 'Subtract',
              ( ['in'], POINTER(ITemporalOperator), 'piOtherOperator' )),
    COMMETHOD(['propget', helpstring(u'Temporal information as a string.')], HRESULT, 'AsString',
              ( ['in'], BSTR, 'bstrFormat' ),
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Temporal information as a date field.')], HRESULT, 'AsDate',
              ( ['retval', 'out'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Temporal information as an interval value.')], HRESULT, 'AsInterval',
              ( ['in'], enumTemporalOperatorUnits, 'enumUnits' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Value of temporal information.')], HRESULT, 'Value',
              ( ['retval', 'out'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Number of intervals between events.')], HRESULT, 'IntervalQuantity',
              ( ['retval', 'out'], POINTER(c_double), 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Units used for interval.')], HRESULT, 'IntervalUnits',
              ( ['retval', 'out'], POINTER(enumTemporalOperatorUnits), 'pVal' )),
]
################################################################
## code template for ITemporalOperator implementation
##class ITemporalOperator_Impl(object):
##    def Reset(self):
##        u'Resets the temporal operator.'
##        #return 
##
##    def SetInterval(self, dQuantity, enumUnits):
##        u'Sets the playback time interval between events.'
##        #return 
##
##    def Subtract(self, piOtherOperator):
##        u'Subtracts a temporal operator.'
##        #return 
##
##    @property
##    def AsDate(self):
##        u'Temporal information as a date field.'
##        #return pVal
##
##    def SetDateTime(self, lYear, lMonth, lDayOfMonth, lHour, lMinute, lSecond, lMillisecond):
##        u'Sets the value for date and time information.'
##        #return 
##
##    @property
##    def Value(self):
##        u'Value of temporal information.'
##        #return pVal
##
##    def Add(self, piOtherOperator):
##        u'Adds a new temporal operator.'
##        #return 
##
##    @property
##    def IntervalQuantity(self):
##        u'Number of intervals between events.'
##        #return pVal
##
##    @property
##    def AsInterval(self, enumUnits):
##        u'Temporal information as an interval value.'
##        #return pVal
##
##    @property
##    def AsString(self, bstrFormat):
##        u'Temporal information as a string.'
##        #return pVal
##
##    @property
##    def Type(self):
##        u'The type of temporal data used.'
##        #return pVal
##
##    @property
##    def IntervalUnits(self):
##        u'Units used for interval.'
##        #return pVal
##

class ITerrainEmbeddedDataSource2(ITerrainEmbeddedDataSource):
    _case_insensitive_ = True
    u'Provides access to members associated with embedded data sources.'
    _iid_ = GUID('{7A0BB0B6-B097-4FBF-BE95-D32473B75AB1}')
    _idlflags_ = ['oleautomation']
class ITerrainFieldStatistics(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to TerrainFieldStatistics object.'
    _iid_ = GUID('{3F30B349-518B-41FA-9F2E-E00D6F81AF82}')
    _idlflags_ = ['oleautomation']
ITerrainEmbeddedDataSource2._methods_ = [
    COMMETHOD([helpstring(u'Returns the statistics of the specified Terrain blob field.')], HRESULT, 'GetFieldStatistics',
              ( ['in'], BSTR, 'FieldName' ),
              ( ['retval', 'out'], POINTER(POINTER(ITerrainFieldStatistics)), 'ppStatistics' )),
    COMMETHOD([helpstring(u'Returns the statistics of all the Terrain blob fields.')], HRESULT, 'GetReservedFieldStatistics',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IArray)), 'ppStatistics' )),
]
################################################################
## code template for ITerrainEmbeddedDataSource2 implementation
##class ITerrainEmbeddedDataSource2_Impl(object):
##    def GetFieldStatistics(self, FieldName):
##        u'Returns the statistics of the specified Terrain blob field.'
##        #return ppStatistics
##
##    def GetReservedFieldStatistics(self):
##        u'Returns the statistics of all the Terrain blob fields.'
##        #return ppStatistics
##

class TerrainWorkspaceExtension(CoClass):
    u'Esri TerrainWorkspaceExtension component.'
    _reg_clsid_ = GUID('{D472BD51-30DC-4E57-A5F6-469E92D934B3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
TerrainWorkspaceExtension._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceExtension, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceExtension3, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceExtensionControl]

class ILasPointInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to LAS point information.'
    _iid_ = GUID('{C4B222F6-C575-4F6B-B7EE-28E34FEA446C}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriLasAttributeType'
esriLasNone = 0
esriLasIntensity = 1
esriLasReturnNumber = 2
esriLasNumberOfReturns = 4
esriLasScanDirectionFlag = 8
esriLasEdgeOfFlightLine = 16
esriLasClassCode = 32
esriLasScanAngleRank = 64
esriLasUserData = 128
esriLasPointSourceID = 256
esriLasGpsTime = 512
esriLasColorRed = 1024
esriLasColorGreen = 2048
esriLasColorBlue = 4096
esriLasColorRGB = 8192
esriLasZ = 16384
esriLasAttributeType = c_int # enum
ILasPointInfo._methods_ = [
    COMMETHOD(['propput', helpstring(u'The 0-based associated file index.')], HRESULT, 'FileIndex',
              ( ['in'], c_int, 'pIndex' )),
    COMMETHOD(['propget', helpstring(u'The 0-based associated file index.')], HRESULT, 'FileIndex',
              ( ['retval', 'out'], POINTER(c_int), 'pIndex' )),
    COMMETHOD(['propput', helpstring(u"The 1-based point's record number.")], HRESULT, 'PointID',
              ( ['in'], c_double, 'pID' )),
    COMMETHOD(['propget', helpstring(u"The 1-based point's record number.")], HRESULT, 'PointID',
              ( ['retval', 'out'], POINTER(c_double), 'pID' )),
    COMMETHOD(['propput', helpstring(u'The return number.')], HRESULT, 'ReturnNumber',
              ( ['in'], c_ubyte, 'pNumber' )),
    COMMETHOD(['propget', helpstring(u'The return number.')], HRESULT, 'ReturnNumber',
              ( ['retval', 'out'], POINTER(c_ubyte), 'pNumber' )),
    COMMETHOD(['propput', helpstring(u'The number of returns.')], HRESULT, 'NumberOfReturns',
              ( ['in'], c_ubyte, 'pCount' )),
    COMMETHOD(['propget', helpstring(u'The number of returns.')], HRESULT, 'NumberOfReturns',
              ( ['retval', 'out'], POINTER(c_ubyte), 'pCount' )),
    COMMETHOD(['propput', helpstring(u'The scan direction flag.')], HRESULT, 'ScanDirectionFlag',
              ( ['in'], c_ubyte, 'pFlag' )),
    COMMETHOD(['propget', helpstring(u'The scan direction flag.')], HRESULT, 'ScanDirectionFlag',
              ( ['retval', 'out'], POINTER(c_ubyte), 'pFlag' )),
    COMMETHOD(['propput', helpstring(u'The edge of flight line.')], HRESULT, 'EdgeOfFlightLine',
              ( ['in'], c_ubyte, 'pEdge' )),
    COMMETHOD(['propget', helpstring(u'The edge of flight line.')], HRESULT, 'EdgeOfFlightLine',
              ( ['retval', 'out'], POINTER(c_ubyte), 'pEdge' )),
    COMMETHOD(['propput', helpstring(u'The class code.')], HRESULT, 'ClassCode',
              ( ['in'], c_ubyte, 'pCode' )),
    COMMETHOD(['propget', helpstring(u'The class code.')], HRESULT, 'ClassCode',
              ( ['retval', 'out'], POINTER(c_ubyte), 'pCode' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the point is marked withheld.')], HRESULT, 'IsWithheld',
              ( ['in'], VARIANT_BOOL, 'pbIsWithheld' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the point is marked withheld.')], HRESULT, 'IsWithheld',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbIsWithheld' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the point is a key point.')], HRESULT, 'IsKeyPoint',
              ( ['in'], VARIANT_BOOL, 'pbIsKey' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the point is a key point.')], HRESULT, 'IsKeyPoint',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbIsKey' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the point is a synthetic point.')], HRESULT, 'IsSyntheticPoint',
              ( ['in'], VARIANT_BOOL, 'pbIsSynthetic' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the point is a synthetic point.')], HRESULT, 'IsSyntheticPoint',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbIsSynthetic' )),
    COMMETHOD(['propput', helpstring(u'The intensity.')], HRESULT, 'Intensity',
              ( ['in'], c_int, 'pIntensity' )),
    COMMETHOD(['propget', helpstring(u'The intensity.')], HRESULT, 'Intensity',
              ( ['retval', 'out'], POINTER(c_int), 'pIntensity' )),
    COMMETHOD(['propput', helpstring(u'The scan angle rank.')], HRESULT, 'ScanAngleRank',
              ( ['in'], c_short, 'pAngle' )),
    COMMETHOD(['propget', helpstring(u'The scan angle rank.')], HRESULT, 'ScanAngleRank',
              ( ['retval', 'out'], POINTER(c_short), 'pAngle' )),
    COMMETHOD(['propput', helpstring(u'The user data.')], HRESULT, 'UserData',
              ( ['in'], c_short, 'pData' )),
    COMMETHOD(['propget', helpstring(u'The user data.')], HRESULT, 'UserData',
              ( ['retval', 'out'], POINTER(c_short), 'pData' )),
    COMMETHOD(['propput', helpstring(u'The point source ID.')], HRESULT, 'PointSourceID',
              ( ['in'], c_int, 'pID' )),
    COMMETHOD(['propget', helpstring(u'The point source ID.')], HRESULT, 'PointSourceID',
              ( ['retval', 'out'], POINTER(c_int), 'pID' )),
    COMMETHOD(['propput', helpstring(u'The GPS time.')], HRESULT, 'GpsTime',
              ( ['in'], c_double, 'pTime' )),
    COMMETHOD(['propget', helpstring(u'The GPS time.')], HRESULT, 'GpsTime',
              ( ['retval', 'out'], POINTER(c_double), 'pTime' )),
    COMMETHOD([helpstring(u'The red color component.')], HRESULT, 'SetColor',
              ( ['in'], c_int, 'Red' ),
              ( ['in'], c_int, 'Green' ),
              ( ['in'], c_int, 'Blue' )),
    COMMETHOD([helpstring(u'The red color component.')], HRESULT, 'GetColor',
              ( ['out'], POINTER(c_int), 'pRed' ),
              ( ['out'], POINTER(c_int), 'pGreen' ),
              ( ['out'], POINTER(c_int), 'pBlue' )),
    COMMETHOD(['propput', helpstring(u"The point's location.")], HRESULT, 'Location',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'ppPoint' )),
    COMMETHOD(['propget', helpstring(u"The point's location.")], HRESULT, 'Location',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint)), 'ppPoint' )),
    COMMETHOD(['propput', helpstring(u"The point's location.")], HRESULT, 'WksLocation',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.WKSPointZ), 'pPoint' )),
    COMMETHOD(['propget', helpstring(u"The point's location.")], HRESULT, 'WksLocation',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.WKSPointZ), 'pPoint' )),
    COMMETHOD([helpstring(u"The point's location.")], HRESULT, 'QueryLocation',
              ( [], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'pPoint' )),
    COMMETHOD(['propputref', helpstring(u"The spatial reference of the point's location.")], HRESULT, 'SpatialReference',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference), 'ppSpatialRef' )),
    COMMETHOD(['propget', helpstring(u"The spatial reference of the point's location.")], HRESULT, 'SpatialReference',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference)), 'ppSpatialRef' )),
    COMMETHOD(['propget', helpstring(u'The LAS attribute.')], HRESULT, 'AttributeValue',
              ( ['in'], esriLasAttributeType, 'Attribute' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'pValue' )),
]
################################################################
## code template for ILasPointInfo implementation
##class ILasPointInfo_Impl(object):
##    def SetColor(self, Red, Green, Blue):
##        u'The red color component.'
##        #return 
##
##    def _get(self):
##        u'The 0-based associated file index.'
##        #return pIndex
##    def _set(self, pIndex):
##        u'The 0-based associated file index.'
##    FileIndex = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The return number.'
##        #return pNumber
##    def _set(self, pNumber):
##        u'The return number.'
##    ReturnNumber = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def SpatialReference(self, ppSpatialRef):
##        u"The spatial reference of the point's location."
##        #return 
##
##    def _get(self):
##        u"The point's location."
##        #return ppPoint
##    def _set(self, ppPoint):
##        u"The point's location."
##    Location = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The GPS time.'
##        #return pTime
##    def _set(self, pTime):
##        u'The GPS time.'
##    GpsTime = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the point is a synthetic point.'
##        #return pbIsSynthetic
##    def _set(self, pbIsSynthetic):
##        u'Indicates if the point is a synthetic point.'
##    IsSyntheticPoint = property(_get, _set, doc = _set.__doc__)
##
##    def QueryLocation(self, pPoint):
##        u"The point's location."
##        #return 
##
##    def _get(self):
##        u'The number of returns.'
##        #return pCount
##    def _set(self, pCount):
##        u'The number of returns.'
##    NumberOfReturns = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The edge of flight line.'
##        #return pEdge
##    def _set(self, pEdge):
##        u'The edge of flight line.'
##    EdgeOfFlightLine = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u"The 1-based point's record number."
##        #return pID
##    def _set(self, pID):
##        u"The 1-based point's record number."
##    PointID = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the point is a key point.'
##        #return pbIsKey
##    def _set(self, pbIsKey):
##        u'Indicates if the point is a key point.'
##    IsKeyPoint = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The user data.'
##        #return pData
##    def _set(self, pData):
##        u'The user data.'
##    UserData = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def AttributeValue(self, Attribute):
##        u'The LAS attribute.'
##        #return pValue
##
##    def _get(self):
##        u'The class code.'
##        #return pCode
##    def _set(self, pCode):
##        u'The class code.'
##    ClassCode = property(_get, _set, doc = _set.__doc__)
##
##    def GetColor(self):
##        u'The red color component.'
##        #return pRed, pGreen, pBlue
##
##    def _get(self):
##        u'The point source ID.'
##        #return pID
##    def _set(self, pID):
##        u'The point source ID.'
##    PointSourceID = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The scan direction flag.'
##        #return pFlag
##    def _set(self, pFlag):
##        u'The scan direction flag.'
##    ScanDirectionFlag = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The intensity.'
##        #return pIntensity
##    def _set(self, pIntensity):
##        u'The intensity.'
##    Intensity = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The scan angle rank.'
##        #return pAngle
##    def _set(self, pAngle):
##        u'The scan angle rank.'
##    ScanAngleRank = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the point is marked withheld.'
##        #return pbIsWithheld
##    def _set(self, pbIsWithheld):
##        u'Indicates if the point is marked withheld.'
##    IsWithheld = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u"The point's location."
##        #return pPoint
##    def _set(self, pPoint):
##        u"The point's location."
##    WksLocation = property(_get, _set, doc = _set.__doc__)
##

class LasDatasetToRasterFunctionArguments(CoClass):
    u'The LasDatasetToRasterFunction arguments.'
    _reg_clsid_ = GUID('{67876AA0-40EB-470A-ABC9-036085756C53}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
LasDatasetToRasterFunctionArguments._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._8F0541A3_D5BE_4B3F_A8D9_062D5579E19B_0_10_2.IRasterFunctionArguments, comtypes.gen._8F0541A3_D5BE_4B3F_A8D9_062D5579E19B_0_10_2.IRasterCacheArguments, comtypes.gen._8F0541A3_D5BE_4B3F_A8D9_062D5579E19B_0_10_2.ILasDatasetToRasterFunctionArguments, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLVersionSupport, comtypes.gen._8F0541A3_D5BE_4B3F_A8D9_062D5579E19B_0_10_2.IItemPaths, comtypes.gen._8F0541A3_D5BE_4B3F_A8D9_062D5579E19B_0_10_2.IItemPaths2]


# values for enumeration 'esriCadastralLineCategory'
esriCadastralLineBoundary = 0
esriCadastralLineDependent = 1
esriCadastralLinePreciseConnection = 2
esriCadastralLineConnection = 3
esriCadastralLineRadial = 4
esriCadastralLineRoad = 5
esriCadastralLineOriginConnection = 6
esriCadastralLinePartConnection = 7
esriCadastralLineCategory = c_int # enum
class ITerrain(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members used to acquire information about a Terrain and to retrieve DynamicSurface objects from which raster and TIN surfaces are made.'
    _iid_ = GUID('{F657C7ED-FE73-493E-8CF7-845E20CB7D9B}')
    _idlflags_ = ['oleautomation']
IDynamicSurface._methods_ = [
    COMMETHOD(['hidden', helpstring(u'The pixel block allocation size used when creating a raster.'), 'propput'], HRESULT, 'RasterBlockSize',
              ( ['in'], c_int, 'pSize' )),
    COMMETHOD(['hidden', helpstring(u'The pixel block allocation size used when creating a raster.'), 'propget'], HRESULT, 'RasterBlockSize',
              ( ['retval', 'out'], POINTER(c_int), 'pSize' )),
    COMMETHOD(['propget', helpstring(u'The source terrain from which the DynamicSurface was derived.')], HRESULT, 'Terrain',
              ( ['retval', 'out'], POINTER(POINTER(ITerrain)), 'ppTerrain' )),
    COMMETHOD([helpstring(u'Returns a TIN for a given area of interest and terrain pyramid level.')], HRESULT, 'GetTin',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'pAreaOfInterest' ),
              ( ['in'], c_double, 'Resolution' ),
              ( ['in'], VARIANT_BOOL, 'bClipWithAOI' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITin)), 'ppTin' )),
    COMMETHOD([helpstring(u'Writes surface heights to a raster dataset for a given area of interest and terrain pyramid level.')], HRESULT, 'QueryRaster',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRasterDataset), 'pDataset' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'pAreaOfInterest' ),
              ( ['in'], c_double, 'Resolution' ),
              ( ['in'], comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriSurfaceInterpolationType, 'Method' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' )),
    COMMETHOD([helpstring(u'Writes terrain measurement points and breakline vertices to a multipoint feature class for a given area of interest and terrain pyramid level.')], HRESULT, 'QueryAsFeatureClass',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'pFeatureClass' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'pAreaOfInterest' ),
              ( ['in'], c_double, 'Resolution' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' )),
]
################################################################
## code template for IDynamicSurface implementation
##class IDynamicSurface_Impl(object):
##    def QueryRaster(self, pDataset, pAreaOfInterest, Resolution, Method, pTrackCancel):
##        u'Writes surface heights to a raster dataset for a given area of interest and terrain pyramid level.'
##        #return 
##
##    def GetTin(self, pAreaOfInterest, Resolution, bClipWithAOI, pTrackCancel):
##        u'Returns a TIN for a given area of interest and terrain pyramid level.'
##        #return ppTin
##
##    @property
##    def Terrain(self):
##        u'The source terrain from which the DynamicSurface was derived.'
##        #return ppTerrain
##
##    def QueryAsFeatureClass(self, pFeatureClass, pAreaOfInterest, Resolution, pTrackCancel):
##        u'Writes terrain measurement points and breakline vertices to a multipoint feature class for a given area of interest and terrain pyramid level.'
##        #return 
##
##    def _get(self):
##        u'The pixel block allocation size used when creating a raster.'
##        #return pSize
##    def _set(self, pSize):
##        u'The pixel block allocation size used when creating a raster.'
##    RasterBlockSize = property(_get, _set, doc = _set.__doc__)
##

class IDataMessage(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods and properties used to manage data messages.'
    _iid_ = GUID('{CC018A04-24FB-11D4-B34C-00104BA2ABCC}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'enumMessageType'
msgtypeCOMMAND = 10
msgtypeDATA = 11
msgtypeRESPONSE = 12
msgtypeSTATUS = 13
enumMessageType = c_int # enum
IDataMessage._methods_ = [
    COMMETHOD(['propget', helpstring(u"Indicates date of data message's creation.")], HRESULT, 'CreationDate',
              ( ['retval', 'out'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD(['propget', helpstring(u'ID value for the data message.')], HRESULT, 'ID',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Indicates type of data message.')], HRESULT, 'MessageType',
              ( ['retval', 'out'], POINTER(enumMessageType), 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Indictes priority of data message.')], HRESULT, 'Priority',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Indictes priority of data message.')], HRESULT, 'Priority',
              ( ['in'], c_int, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Indicates destination of the data message.')], HRESULT, 'Destination',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Indicates destination of the data message.')], HRESULT, 'Destination',
              ( ['in'], BSTR, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Number of arguments in the data message.')], HRESULT, 'ArgumentCount',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD([helpstring(u'Sets an argument for the data message.')], HRESULT, 'setArgument',
              ( ['in'], c_int, 'nIndex' ),
              ( ['in'], POINTER(VARIANT), 'pValue' )),
    COMMETHOD([helpstring(u'Adds an argument to the data message.')], HRESULT, 'addArgument',
              ( ['in'], POINTER(VARIANT), 'pValue' )),
    COMMETHOD([helpstring(u'Removes an argument from the data message.')], HRESULT, 'removeArgument',
              ( ['in'], c_int, 'nIndex' )),
    COMMETHOD([helpstring(u'Gets an argument for the data message.')], HRESULT, 'getArgument',
              ( ['in'], c_int, 'nIndex' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'pValue' )),
    COMMETHOD(['propget', helpstring(u'ID value for the data definition in the message.')], HRESULT, 'DataDefinitionID',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'ID value for the data definition in the message.')], HRESULT, 'DataDefinitionID',
              ( ['in'], BSTR, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Number of columns in data message.')], HRESULT, 'ColumnCount',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD([helpstring(u'Sets the number of columns in a data message.')], HRESULT, 'setColumn',
              ( ['in'], c_int, 'nIndex' ),
              ( ['in'], POINTER(VARIANT), 'pValue' )),
    COMMETHOD([helpstring(u'Adds a column to the data message.')], HRESULT, 'addColumn',
              ( ['in'], POINTER(VARIANT), 'pValue' )),
    COMMETHOD([helpstring(u'Removes a column from the data message.')], HRESULT, 'removeColumn',
              ( ['in'], c_int, 'nIndex' )),
    COMMETHOD([helpstring(u'Returns value for columns in the data message.')], HRESULT, 'getColumn',
              ( ['in'], c_int, 'nIndex' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'pValue' )),
    COMMETHOD([helpstring(u'Returns the Raw column info.  For Objects it is a array of bytes conforming to the IPersist Stream format.')], HRESULT, 'getRawColumn',
              ( ['in'], c_int, 'nIndex' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'pValue' )),
]
################################################################
## code template for IDataMessage implementation
##class IDataMessage_Impl(object):
##    @property
##    def ColumnCount(self):
##        u'Number of columns in data message.'
##        #return pVal
##
##    def addArgument(self, pValue):
##        u'Adds an argument to the data message.'
##        #return 
##
##    def removeColumn(self, nIndex):
##        u'Removes a column from the data message.'
##        #return 
##
##    def setColumn(self, nIndex, pValue):
##        u'Sets the number of columns in a data message.'
##        #return 
##
##    def _get(self):
##        u'Indicates destination of the data message.'
##        #return pVal
##    def _set(self, pVal):
##        u'Indicates destination of the data message.'
##    Destination = property(_get, _set, doc = _set.__doc__)
##
##    def getRawColumn(self, nIndex):
##        u'Returns the Raw column info.  For Objects it is a array of bytes conforming to the IPersist Stream format.'
##        #return pValue
##
##    @property
##    def MessageType(self):
##        u'Indicates type of data message.'
##        #return pVal
##
##    @property
##    def ArgumentCount(self):
##        u'Number of arguments in the data message.'
##        #return pVal
##
##    def _get(self):
##        u'Indictes priority of data message.'
##        #return pVal
##    def _set(self, pVal):
##        u'Indictes priority of data message.'
##    Priority = property(_get, _set, doc = _set.__doc__)
##
##    def getArgument(self, nIndex):
##        u'Gets an argument for the data message.'
##        #return pValue
##
##    def removeArgument(self, nIndex):
##        u'Removes an argument from the data message.'
##        #return 
##
##    def _get(self):
##        u'ID value for the data definition in the message.'
##        #return pVal
##    def _set(self, pVal):
##        u'ID value for the data definition in the message.'
##    DataDefinitionID = property(_get, _set, doc = _set.__doc__)
##
##    def setArgument(self, nIndex, pValue):
##        u'Sets an argument for the data message.'
##        #return 
##
##    def getColumn(self, nIndex):
##        u'Returns value for columns in the data message.'
##        #return pValue
##
##    def addColumn(self, pValue):
##        u'Adds a column to the data message.'
##        #return 
##
##    @property
##    def CreationDate(self):
##        u"Indicates date of data message's creation."
##        #return pVal
##
##    @property
##    def ID(self):
##        u'ID value for the data message.'
##        #return pVal
##

class CadastralFabricRegenerator(CoClass):
    u'Class for regenerating parcel fabric components.'
    _reg_clsid_ = GUID('{C3D97CE1-22F7-4F5A-942B-AA899F61AD34}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
class ICadastralFabricRegeneration(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members which regenerate the features of an existing parcel fabric'
    _iid_ = GUID('{98319C51-D6CF-45C9-B8E7-0CAE17D55476}')
    _idlflags_ = ['oleautomation']
CadastralFabricRegenerator._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ICadastralFabricRegeneration]

class ITerrainBlockCursor(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to TerrainBlockCursor object.'
    _iid_ = GUID('{3F4FE9AD-471B-4D67-8F8F-930A23A60305}')
    _idlflags_ = ['oleautomation']
ITerrainBlockCursor._methods_ = [
    COMMETHOD(['propget', helpstring(u'The number of blocks in the cursor.')], HRESULT, 'BlockCount',
              ( ['retval', 'out'], POINTER(c_int), 'pcBlocks' )),
    COMMETHOD([helpstring(u'Returns next block in the form of rows and columns.')], HRESULT, 'Next',
              ( ['out'], POINTER(c_int), 'pRowBegin' ),
              ( ['out'], POINTER(c_int), 'pRowEnd' ),
              ( ['out'], POINTER(c_int), 'pColBegin' ),
              ( ['out'], POINTER(c_int), 'pColEnd' ),
              ( ['out'], POINTER(VARIANT_BOOL), 'pbIsEnd' )),
    COMMETHOD([helpstring(u'Returns next block as a reference to a TIN object.')], HRESULT, 'NextAsTin',
              ( ['out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITin)), 'ppTin' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'ppExtent' )),
    COMMETHOD([helpstring(u'Resets the cursor to point to the first block.')], HRESULT, 'Reset'),
]
################################################################
## code template for ITerrainBlockCursor implementation
##class ITerrainBlockCursor_Impl(object):
##    def Reset(self):
##        u'Resets the cursor to point to the first block.'
##        #return 
##
##    @property
##    def BlockCount(self):
##        u'The number of blocks in the cursor.'
##        #return pcBlocks
##
##    def NextAsTin(self):
##        u'Returns next block as a reference to a TIN object.'
##        #return ppTin, ppExtent
##
##    def Next(self):
##        u'Returns next block in the form of rows and columns.'
##        #return pRowBegin, pRowEnd, pColBegin, pColEnd, pbIsEnd
##

class ITerrainName(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that set and return the associated feature dataset name object.'
    _iid_ = GUID('{FA7B8F6E-C012-4E16-AFB9-62B8CE0F9011}')
    _idlflags_ = ['oleautomation']
ITerrainName._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The Feature Dataset Name that the terrain belongs to.')], HRESULT, 'FeatureDatasetName',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetName), 'ppFeatureDatasetName' )),
    COMMETHOD(['propget', helpstring(u'The Feature Dataset Name that the terrain belongs to.')], HRESULT, 'FeatureDatasetName',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetName)), 'ppFeatureDatasetName' )),
]
################################################################
## code template for ITerrainName implementation
##class ITerrainName_Impl(object):
##    @property
##    def FeatureDatasetName(self, ppFeatureDatasetName):
##        u'The Feature Dataset Name that the terrain belongs to.'
##        #return 
##


# values for enumeration 'enumObjectSource'
sourceDynamic = 0
sourceShapeFile = 1
sourceLocalGeoDatabase = 2
sourceSDE = 3
enumObjectSource = c_int # enum
class TerrainName(CoClass):
    u'Esri Terrain Name object.'
    _reg_clsid_ = GUID('{4CED9311-6566-44F6-B135-657D6F48143E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
TerrainName._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetName, ITerrainName, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo]


# values for enumeration 'esriTerrainError'
E_TERRAIN_INVALID_DATA_SOURCE = -2147205120
E_TERRAIN_DATA_SOURCE_EXISTS = -2147205119
E_TERRAIN_INDEX_OUT_OF_RANGE = -2147205118
E_TERRAIN_NOT_INITIALIZED = -2147205117
E_TERRAIN_CANCELLED = -2147205116
E_TERRAIN_EDIT_SESSION_REQUIRED = -2147205115
E_TERRAIN_MUST_BE_ZLESS = -2147205114
E_TERRAIN_FILE_EXISTS = -2147205113
E_TERRAIN_FILE_NOT_EXISTS = -2147205112
E_TERRAIN_FILE_OPEN_ERROR = -2147205111
E_TERRAIN_FILE_READ_ERROR = -2147205110
E_TERRAIN_NOT_MATCH = -2147205109
E_TERRAIN_WRONG_FORMAT = -2147205108
E_TERRAIN_NO_RETURN = -2147205107
E_TERRAIN_BAD_SHAPE_SIZE = -2147205106
E_TERRAIN_NOT_MULTIPOINT = -2147205105
E_TERRAIN_UNKNOWN_FIELD = -2147205104
E_TERRAIN_FC_OUTSIDE = -2147205103
E_TERRAIN_ZTOLERANCE_EXISTS = -2147205102
E_TERRAIN_INVALID_TERRAIN = -2147205101
E_TERRAIN_INVALID_DEFINITION = -2147205100
E_TERRAIN_IN_EDIT_SESSION = -2147205099
E_TERRAIN_INVALID_BOUNDS = -2147205098
E_TERRAIN_BOUNDS_OVERLAP = -2147205097
E_TERRAIN_INCONSIST = -2147205096
E_TERRAIN_WRONG_GEOMETRY_TYPE = -2147205095
E_TERRAIN_MIXING_2D_AND_3D = -2147205094
E_TERRAIN_TOO_MANY_BASE = -2147205093
E_TERRAIN_MUST_NOT_BE_GROUPED = -2147205092
E_TERRAIN_WRONG_SF_TYPE = -2147205091
E_TERRAIN_INCONSIST_LOR = -2147205090
E_TERRAIN_CHANGE_CLASS_ID = -2147205089
E_TERRAIN_NOT_EMBEDDED = -2147205088
E_TERRAIN_NULL_FIELD_VALUE = -2147205087
E_TERRAIN_FIELD_NULLABLE = -2147205086
E_TERRAIN_TERRAIN_NOT_FOUND = -2147205085
E_TERRAIN_TERRAIN_NOT_SUPPORTED_IN_RELEASE = -2147205084
E_TERRAIN_TERRAIN_ALREADY_EXISTS = -2147205083
E_TERRAIN_INVALID_GEOMETRY_TYPE_FOR_TERRAIN = -2147205082
E_TERRAIN_CANNOT_ADD_REGISTERED_CLASS_TO_TERRAIN = -2147205081
E_TERRAIN_INVALID_TERRAIN_NAME = -2147205080
E_TERRAIN_WRONG_DATASET_TYPE = -2147205079
E_TERRAIN_WRONG_PYRAMID_TYPE = -2147205078
E_TERRAIN_CANNOT_CHANGE_SCHEMA = -2147205077
E_TERRAIN_NOT_MULTIPOINT_Z = -2147205076
E_TERRAIN_UNKNOWN_BLOB = -2147205075
E_TERRAIN_NEED_UPDATE = -2147205074
E_TERRAIN_OLD_VERSION = -2147205073
E_TERRAIN_CANNOT_PERFORM_SIMPLIFY_OVERVIEW = -2147205072
E_TERRAIN_NO_DATA = -2147205071
E_TERRAIN_EDIT_OPERATION_REQUIRED = -2147205070
E_TERRAIN_INVALID_EMBEDDED_FC_NAME = -2147205069
E_TERRAIN_TOO_MANY_CLIPPING_SOURCES = -2147205068
E_TERRAIN_INVALID_Z = -2147205067
E_TERRAIN_BAD_WINDOWSIZE = -2147205066
E_TERRAIN_NO_SPATIALREF_INFO = -2147205065
E_TERRAIN_NOT_PROJECTED_SYSTEM = -2147219400
E_TERRAIN_WRONG_TOPOLOGY = -2147219399
E_TERRAIN_VALUE_OVERFLOW = -2147219398
E_TERRAIN_DATA_TYPE_MISMATCH = -2147219397
E_TERRAIN_DIRTY_TERRAIN = -2147219396
E_TERRAIN_WINSIZE_NOT_SUPPORTED = -2147205059
E_TERRAIN_FIELD_TYPE_MISMATCH = -2147219394
E_TERRAIN_CANNOT_BE_ANCHORED = -2147219393
E_TERRAIN_ANCHOR_POINTS_NOT_SUPPORTED = -2147219392
E_TERRAIN_MUST_APPLY_TO_OVERVIEW = -2147219391
E_TERRAIN_VERSION_NOT_SUPPORTED = -2147219390
E_TERRAIN_FORMAT_NOT_SUPPORTED = -2147219389
E_TERRAIN_FILE_WRITE_ERROR = -2147205052
E_TERRAIN_INVALID_FILE = -2147205051
E_TERRAIN_WKT_NOT_SUPPORTED = -2147205050
esriTerrainError = c_int # enum

# values for enumeration 'enumTemporalFeatureType'
enumTimeStamp = 0
enumTemporalFeatureType = c_int # enum
class ILockedFeatureSearch(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods needed to select, search and lock MBDB records.'
    _iid_ = GUID('{6FB36881-6399-4BD6-BE3D-B07033A79114}')
    _idlflags_ = ['oleautomation']
ILockedFeatureSearch._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates the FIDs for all locked features.')], HRESULT, 'AllLockedFIDs',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFIDSet)), 'ppiAllLockedFIDs' )),
    COMMETHOD([helpstring(u'Searches records that satisfy the query filter and lockes them.')], HRESULT, 'SearchAndLock',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IQueryFilter), 'piQueryFilter' ),
              ( ['in'], VARIANT_BOOL, 'Recycling' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ICursor)), 'ppiCursor' )),
    COMMETHOD([helpstring(u'Selectes records that satisfy the query filter, selection type and selection option, and lockes them.')], HRESULT, 'SelectAndLock',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IQueryFilter), 'piQueryFilter' ),
              ( ['in'], comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriSelectionType, 'selType' ),
              ( ['in'], comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriSelectionOption, 'selOption' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspace), 'piSelectionContainer' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ISelectionSet)), 'ppiSelectionSet' )),
    COMMETHOD([helpstring(u'Unlocks all features that are locked.')], HRESULT, 'UnlockAllFeatures'),
]
################################################################
## code template for ILockedFeatureSearch implementation
##class ILockedFeatureSearch_Impl(object):
##    def UnlockAllFeatures(self):
##        u'Unlocks all features that are locked.'
##        #return 
##
##    @property
##    def AllLockedFIDs(self):
##        u'Indicates the FIDs for all locked features.'
##        #return ppiAllLockedFIDs
##
##    def SearchAndLock(self, piQueryFilter, Recycling):
##        u'Searches records that satisfy the query filter and lockes them.'
##        #return ppiCursor
##
##    def SelectAndLock(self, piQueryFilter, selType, selOption, piSelectionContainer):
##        u'Selectes records that satisfy the query filter, selection type and selection option, and lockes them.'
##        #return ppiSelectionSet
##

class ICadastralFabricSchemaEdit2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that modify the cadastral fabric schema.'
    _iid_ = GUID('{E2930C0E-DD54-4F12-8960-C44E6C08C395}')
    _idlflags_ = ['oleautomation']
ICadastralFabricSchemaEdit2._methods_ = [
    COMMETHOD([helpstring(u'Temporarily release the read-only property on system the fields of the given cadastral fabric table.')], HRESULT, 'ReleaseReadOnlyFields',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable), 'pTable' ),
              ( ['in'], esriCadastralFabricTable, 'Table' )),
    COMMETHOD([helpstring(u'Reset the read-only property on system the fields of the cadastral fabric tables.')], HRESULT, 'ResetReadOnlyFields',
              ( ['in'], esriCadastralFabricTable, 'Table' )),
]
################################################################
## code template for ICadastralFabricSchemaEdit2 implementation
##class ICadastralFabricSchemaEdit2_Impl(object):
##    def ResetReadOnlyFields(self, Table):
##        u'Reset the read-only property on system the fields of the cadastral fabric tables.'
##        #return 
##
##    def ReleaseReadOnlyFields(self, pTable, Table):
##        u'Temporarily release the read-only property on system the fields of the given cadastral fabric table.'
##        #return 
##


# values for enumeration 'esriTerrainBlobDataType'
esriTerrainChar = 1
esriTerrainUChar = 2
esriTerrainShort = 3
esriTerrainUShort = 4
esriTerrainLong = 5
esriTerrainULong = 6
esriTerrainFloat = 7
esriTerrainDouble = 9
esriTerrainBlobDataType = c_int # enum
ITerrainFieldStatistics._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if the object is empty.')], HRESULT, 'IsEmpty',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbIsEmpty' )),
    COMMETHOD(['propget', helpstring(u'Indicates if update is necessary.')], HRESULT, 'NeedsUpdate',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbNeedsUpdate' )),
    COMMETHOD(['propget', helpstring(u'The field name associated with the statistics.')], HRESULT, 'FieldName',
              ( ['retval', 'out'], POINTER(BSTR), 'pName' )),
    COMMETHOD(['propget', helpstring(u'The number of elements.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_double), 'pCount' )),
    COMMETHOD(['propget', helpstring(u'The minimum value.')], HRESULT, 'Minimum',
              ( ['retval', 'out'], POINTER(c_double), 'pMinimum' )),
    COMMETHOD(['propget', helpstring(u'The maximum value.')], HRESULT, 'Maximum',
              ( ['retval', 'out'], POINTER(c_double), 'pMaximum' )),
    COMMETHOD(['propget', helpstring(u'The mean value.')], HRESULT, 'Mean',
              ( ['retval', 'out'], POINTER(c_double), 'pMean' )),
    COMMETHOD(['propget', helpstring(u'The standard deviation.')], HRESULT, 'StandardDeviation',
              ( ['retval', 'out'], POINTER(c_double), 'pStandardDeviation' )),
    COMMETHOD(['propget', helpstring(u'Returns esriTerrainLong for integer-type data (except for unsigned long), and esriTerrainDouble for unsigned long and floating point data.')], HRESULT, 'UniqueValueType',
              ( ['retval', 'out'], POINTER(esriTerrainBlobDataType), 'pType' )),
    COMMETHOD([helpstring(u'Returns the unique values.')], HRESULT, 'GetUniqueValuesAsLong',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray)), 'ppValues' )),
    COMMETHOD([helpstring(u'Returns the unique values.')], HRESULT, 'GetUniqueValuesAsDouble',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDoubleArray)), 'ppValues' )),
    COMMETHOD([helpstring(u'Returns the number of unique values.')], HRESULT, 'GetUniqueValueCounts',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDoubleArray)), 'ppCounts' )),
]
################################################################
## code template for ITerrainFieldStatistics implementation
##class ITerrainFieldStatistics_Impl(object):
##    @property
##    def Count(self):
##        u'The number of elements.'
##        #return pCount
##
##    @property
##    def UniqueValueType(self):
##        u'Returns esriTerrainLong for integer-type data (except for unsigned long), and esriTerrainDouble for unsigned long and floating point data.'
##        #return pType
##
##    @property
##    def NeedsUpdate(self):
##        u'Indicates if update is necessary.'
##        #return pbNeedsUpdate
##
##    def GetUniqueValuesAsDouble(self):
##        u'Returns the unique values.'
##        #return ppValues
##
##    @property
##    def Maximum(self):
##        u'The maximum value.'
##        #return pMaximum
##
##    @property
##    def StandardDeviation(self):
##        u'The standard deviation.'
##        #return pStandardDeviation
##
##    def GetUniqueValuesAsLong(self):
##        u'Returns the unique values.'
##        #return ppValues
##
##    @property
##    def Minimum(self):
##        u'The minimum value.'
##        #return pMinimum
##
##    @property
##    def FieldName(self):
##        u'The field name associated with the statistics.'
##        #return pName
##
##    def GetUniqueValueCounts(self):
##        u'Returns the number of unique values.'
##        #return ppCounts
##
##    @property
##    def IsEmpty(self):
##        u'Indicates if the object is empty.'
##        #return pbIsEmpty
##
##    @property
##    def Mean(self):
##        u'The mean value.'
##        #return pMean
##

class ITerrainDataImporter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that handle importing terrain source data.'
    _iid_ = GUID('{36B3F42A-ABE0-440E-A266-8B8592C74C82}')
    _idlflags_ = ['oleautomation']
class ITerrainAsciiDataImporter(ITerrainDataImporter):
    _case_insensitive_ = True
    u'Provides access to members that handle importing terrain source data in ASCII format.'
    _iid_ = GUID('{8D2D47F1-75BB-4346-B245-4178E9EB9B38}')
    _idlflags_ = ['oleautomation']
ITerrainDataImporter._methods_ = [
    COMMETHOD([helpstring(u"Set source data's spatial reference.")], HRESULT, 'SetSourceDataSpatialReference',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference), 'pSpatialRef' )),
    COMMETHOD([helpstring(u'Clears all properties.')], HRESULT, 'SetEmpty'),
    COMMETHOD(['propget', helpstring(u'The maximum number of points loaded into individual multipoint shapes.')], HRESULT, 'MaxShapePointCount',
              ( ['retval', 'out'], POINTER(c_int), 'pCount' )),
    COMMETHOD([helpstring(u'Changes the default maximum number of points loaded into individual multipoint shapes.')], HRESULT, 'OverwriteMaxShapePointCount',
              ( ['in'], c_int, 'newCount' )),
    COMMETHOD([helpstring(u'Include a specific file to be loaded upon Import.')], HRESULT, 'AddFile',
              ( ['in'], BSTR, 'fileName' )),
    COMMETHOD([helpstring(u'Include a folder, and potentially subfolders, to be loaded upon import.')], HRESULT, 'AddFolder',
              ( ['in'], BSTR, 'folderName' ),
              ( ['in'], BSTR, 'fileExtension' ),
              ( ['in'], VARIANT_BOOL, 'bRecursive' )),
    COMMETHOD([helpstring(u'The XYZ extent of data contained in files/folders to be added.')], HRESULT, 'GetDataExtent',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference), 'pTargetSpatialReference' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'ppExt' )),
    COMMETHOD([helpstring(u'The number of points in the files/folders to be added.')], HRESULT, 'GetPointCount',
              ( ['retval', 'out'], POINTER(c_double), 'pCount' )),
    COMMETHOD([helpstring(u'Loads the specified data, based on the current properties, into the target feature class.')], HRESULT, 'Import',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'pOutputFeatureClass' ),
              ( ['in'], c_double, 'TileSize' ),
              ( ['in'], c_double, 'ZFactor' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'pAOI' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( ['out'], POINTER(c_int), 'pcOutsidePoints' )),
]
################################################################
## code template for ITerrainDataImporter implementation
##class ITerrainDataImporter_Impl(object):
##    def AddFolder(self, folderName, fileExtension, bRecursive):
##        u'Include a folder, and potentially subfolders, to be loaded upon import.'
##        #return 
##
##    def SetSourceDataSpatialReference(self, pSpatialRef):
##        u"Set source data's spatial reference."
##        #return 
##
##    def AddFile(self, fileName):
##        u'Include a specific file to be loaded upon Import.'
##        #return 
##
##    def OverwriteMaxShapePointCount(self, newCount):
##        u'Changes the default maximum number of points loaded into individual multipoint shapes.'
##        #return 
##
##    def SetEmpty(self):
##        u'Clears all properties.'
##        #return 
##
##    def GetDataExtent(self, pTargetSpatialReference):
##        u'The XYZ extent of data contained in files/folders to be added.'
##        #return ppExt
##
##    @property
##    def MaxShapePointCount(self):
##        u'The maximum number of points loaded into individual multipoint shapes.'
##        #return pCount
##
##    def Import(self, pOutputFeatureClass, TileSize, ZFactor, pAOI, pTrackCancel):
##        u'Loads the specified data, based on the current properties, into the target feature class.'
##        #return pcOutsidePoints
##
##    def GetPointCount(self):
##        u'The number of points in the files/folders to be added.'
##        #return pCount
##

ITerrainAsciiDataImporter._methods_ = [
    COMMETHOD(['propput', helpstring(u'The format of the data to be imported.')], HRESULT, 'FileFormat',
              ( ['in'], esriTerrainAsciiDataFormatType, 'pFormat' )),
    COMMETHOD(['propget', helpstring(u'The format of the data to be imported.')], HRESULT, 'FileFormat',
              ( ['retval', 'out'], POINTER(esriTerrainAsciiDataFormatType), 'pFormat' )),
]
################################################################
## code template for ITerrainAsciiDataImporter implementation
##class ITerrainAsciiDataImporter_Impl(object):
##    def _get(self):
##        u'The format of the data to be imported.'
##        #return pFormat
##    def _set(self, pFormat):
##        u'The format of the data to be imported.'
##    FileFormat = property(_get, _set, doc = _set.__doc__)
##

class ITerrainAsciiDataImporter2(ITerrainAsciiDataImporter):
    _case_insensitive_ = True
    u'Provides access to members that handle importing terrain source data in ASCII format.'
    _iid_ = GUID('{33F2E5C8-8E0E-4FC2-8B7B-D901C6E90ED8}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriTerrainDecimalSeparatorType'
esriTerrainDecimalSeparatorPoint = 0
esriTerrainDecimalSeparatorComma = 1
esriTerrainDecimalSeparatorType = c_int # enum
ITerrainAsciiDataImporter2._methods_ = [
    COMMETHOD(['propput', helpstring(u'ASCII data decimal point type.')], HRESULT, 'DecimalPointType',
              ( ['in'], esriTerrainDecimalSeparatorType, 'pType' )),
    COMMETHOD(['propget', helpstring(u'ASCII data decimal point type.')], HRESULT, 'DecimalPointType',
              ( ['retval', 'out'], POINTER(esriTerrainDecimalSeparatorType), 'pType' )),
]
################################################################
## code template for ITerrainAsciiDataImporter2 implementation
##class ITerrainAsciiDataImporter2_Impl(object):
##    def _get(self):
##        u'ASCII data decimal point type.'
##        #return pType
##    def _set(self, pType):
##        u'ASCII data decimal point type.'
##    DecimalPointType = property(_get, _set, doc = _set.__doc__)
##

class ICadastralFabricSchemaEdit(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that modify the cadastral fabric schema.'
    _iid_ = GUID('{8A932661-07B3-4D2E-B02C-CE6092A1B4AF}')
    _idlflags_ = ['oleautomation']
class IDECadastralFabric(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that describe cadastral fabric data elements.'
    _iid_ = GUID('{06C95FA1-8CF2-4563-8038-15FB592374B4}')
    _idlflags_ = ['oleautomation']
ICadastralFabricSchemaEdit._methods_ = [
    COMMETHOD([helpstring(u'Updates the schema for the cadastral fabric based upon the given data element.')], HRESULT, 'UpdateSchema',
              ( ['in'], POINTER(IDECadastralFabric), 'DataElement' )),
]
################################################################
## code template for ICadastralFabricSchemaEdit implementation
##class ICadastralFabricSchemaEdit_Impl(object):
##    def UpdateSchema(self, DataElement):
##        u'Updates the schema for the cadastral fabric based upon the given data element.'
##        #return 
##

class LasFile(CoClass):
    u'Esri LasFile object.'
    _reg_clsid_ = GUID('{767B20C5-40C4-4875-A3D8-D6DE321C62BF}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
class ILasFile(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of LasFile.'
    _iid_ = GUID('{36CCBFD3-8A6C-4C11-8551-96AE8629AAD9}')
    _idlflags_ = ['oleautomation']
LasFile._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset, ILasFile]

class DECadastralFabricType(CoClass):
    u'Esri Cadastral Fabric Data Element Type Object.'
    _reg_clsid_ = GUID('{931BF28C-B23D-4416-96ED-F653AA60524D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
class IDECadastralFabricType(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to an indicator interface for the Cadastral Fabric Data Element type object.'
    _iid_ = GUID('{29C69EB6-60AA-463D-9C25-0CBE856D6054}')
    _idlflags_ = ['oleautomation']
DECadastralFabricType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDECadastralFabricType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEGeoDatasetType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEDatasetType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElementType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGxFilterInfo, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDataType, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone]


# values for enumeration 'esriCadastralPointCategory'
esriCadastralPointStandard = 0
esriCadastralPointConstruction = 1
esriCadastralPointControl = 2
esriCadastralPointInterpolated = 3
esriCadastralPointReferenceMark = 4
esriCadastralPointBenchMark = 5
esriCadastralPointStation = 6
esriCadastralPointCategory = c_int # enum
class CadastralJob(CoClass):
    u'A container for the properties of a Cadastral Job.'
    _reg_clsid_ = GUID('{F8027B0A-A3FB-448A-8FE2-B1BEADCF672E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
CadastralJob._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ICadastralJob]


# values for enumeration 'esriTerrainLasDataPropertyType'
esriTerrainLasIntensity = 1
esriTerrainLasReturnNumber = 2
esriTerrainLasNumberOfReturns = 4
esriTerrainLasScanDirectionFlag = 8
esriTerrainLasEdgeOfFlightLine = 16
esriTerrainLasClassification = 32
esriTerrainLasScanAngleRank = 64
esriTerrainLasFileMarker = 128
esriTerrainLasUserBitField = 256
esriTerrainLasGpsTime = 512
esriTerrainLasColorRed = 1024
esriTerrainLasColorGreen = 2048
esriTerrainLasColorBlue = 4096
esriTerrainLasDataPropertyType = c_int # enum
class TerrainPyramidLevelZTolerance(CoClass):
    _reg_clsid_ = GUID('{211D08C6-6F1D-490D-BB84-68E699B54A15}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
class ITerrainPyramidLevel(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of Terrain Pyramid Level.'
    _iid_ = GUID('{9FF889CD-EE5D-4093-9BF2-8384002D01A4}')
    _idlflags_ = ['oleautomation']
TerrainPyramidLevelZTolerance._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ITerrainPyramidLevel]

class ITemporalCursor(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureCursor):
    _case_insensitive_ = True
    u'Provides access to methods needed to control the temporal cursor.'
    _iid_ = GUID('{CC018A66-24FB-11D4-B34C-00104BA2ABCC}')
    _idlflags_ = ['oleautomation']
ITemporalCursor._methods_ = [
    COMMETHOD([helpstring(u'Advances the position of the cursor by one and returns the feature object at that position.')], HRESULT, 'NextObject',
              ( ['in', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeature)), 'ppiFeature' ),
              ( ['in', 'out'], POINTER(VARIANT), 'pvarTimeSeries' ),
              ( ['in', 'out'], POINTER(c_longlong), 'phyTimeStamp' ),
              ( ['in', 'out'], POINTER(c_int), 'plOID' )),
    COMMETHOD([helpstring(u'Resets the cursor position.')], HRESULT, 'Reset'),
]
################################################################
## code template for ITemporalCursor implementation
##class ITemporalCursor_Impl(object):
##    def NextObject(self):
##        u'Advances the position of the cursor by one and returns the feature object at that position.'
##        #return ppiFeature, pvarTimeSeries, phyTimeStamp, plOID
##
##    def Reset(self):
##        u'Resets the cursor position.'
##        #return 
##


# values for enumeration 'esriCadastralDistanceUnits'
esriCDUMeter = 9001
esriCDUFoot = 9002
esriCDUChain = 9097
esriCDULink = 9098
esriCDURod = 109010
esriCDUUSSurveyFoot = 9003
esriCDUUSSurveyChain = 9033
esriCDUUSSurveyLink = 9034
esriCDUUSSurveyRod = 109011
esriCadastralDistanceUnits = c_int # enum
ICadastralUnitConversion._methods_ = [
    COMMETHOD(['propget', helpstring(u'Cadastral Distance Units for a particular linear unit.')], HRESULT, 'DistanceUnitType',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ILinearUnit), 'pLinearUnit' ),
              ( ['retval', 'out'], POINTER(esriCadastralDistanceUnits), 'pDistanceUnit' )),
    COMMETHOD([helpstring(u"Convert units of string value to double. Example: '55 ft'. If the unit suffix string is missing, the default unit is used.")], HRESULT, 'ConvertString',
              ( ['in'], BSTR, 'val' ),
              ( ['in'], esriCadastralDistanceUnits, 'defaultUnit' ),
              ( ['in'], esriCadastralDistanceUnits, 'outputUnit' ),
              ( ['retval', 'out'], POINTER(c_double), 'pVal' )),
    COMMETHOD([helpstring(u'Convert units of a double value.')], HRESULT, 'ConvertDouble',
              ( ['in'], c_double, 'val' ),
              ( ['in'], esriCadastralDistanceUnits, 'unit' ),
              ( ['in'], esriCadastralDistanceUnits, 'outputUnit' ),
              ( ['retval', 'out'], POINTER(c_double), 'pVal' )),
]
################################################################
## code template for ICadastralUnitConversion implementation
##class ICadastralUnitConversion_Impl(object):
##    def ConvertDouble(self, val, unit, outputUnit):
##        u'Convert units of a double value.'
##        #return pVal
##
##    @property
##    def DistanceUnitType(self, pLinearUnit):
##        u'Cadastral Distance Units for a particular linear unit.'
##        #return pDistanceUnit
##
##    def ConvertString(self, val, defaultUnit, outputUnit):
##        u"Convert units of string value to double. Example: '55 ft'. If the unit suffix string is missing, the default unit is used."
##        #return pVal
##

class ITemporalTable(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to properties and methods in which a temporal table can be controlled.'
    _iid_ = GUID('{18FB46E0-461A-11D5-B7E5-00010265ADC5}')
    _idlflags_ = ['oleautomation']
class ITemporalObservationsTable(ITemporalTable):
    _case_insensitive_ = True
    _iid_ = GUID('{A677AB5F-2FB8-11D5-B7E2-00010265ADC5}')
    _idlflags_ = ['oleautomation']
ITemporalTable._methods_ = [
    COMMETHOD([helpstring(u'The index of the field with the specified name.')], HRESULT, 'FindField',
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(c_int), 'FieldIndex' )),
    COMMETHOD(['propget', helpstring(u'The fields collection for this object class.')], HRESULT, 'Fields',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFields)), 'Fields' )),
    COMMETHOD([helpstring(u'Adds a field to this object class.')], HRESULT, 'AddField',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IField), 'Field' )),
    COMMETHOD([helpstring(u'Deletes a field from this object class.')], HRESULT, 'DeleteField',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IField), 'Field' )),
    COMMETHOD([helpstring(u'Creates a row in the database with a system assigned object ID and null property values.')], HRESULT, 'CreateRow',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRow)), 'Row' )),
    COMMETHOD([helpstring(u'The row from the database with the specified object ID.')], HRESULT, 'GetRow',
              ( ['in'], c_int, 'OID' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRow)), 'Row' )),
    COMMETHOD([helpstring(u'Creates a row buffer that can be used with an insert cursor.')], HRESULT, 'CreateRowBuffer',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRowBuffer)), 'Buffer' )),
    COMMETHOD([helpstring(u'The number of Rows selected by the specified query.')], HRESULT, 'RowCount',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IQueryFilter), 'QueryFilter' ),
              ( ['retval', 'out'], POINTER(c_int), 'NumRows' )),
    COMMETHOD([helpstring(u'An object cursor that can be used to fetch row objects selected by the specified query.')], HRESULT, 'Search',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IQueryFilter), 'QueryFilter' ),
              ( ['in'], VARIANT_BOOL, 'Recycling' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ICursor)), 'Cursor' )),
    COMMETHOD([helpstring(u'Returns a cursor that can be used to update Rows selected by the specified query.')], HRESULT, 'Update',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IQueryFilter), 'QueryFilter' ),
              ( ['in'], VARIANT_BOOL, 'Recycling' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ICursor)), 'Cursor' )),
    COMMETHOD([helpstring(u'Returns a  cursor that can be used to insert new Rows.')], HRESULT, 'Insert',
              ( ['in'], VARIANT_BOOL, 'useBuffering' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ICursor)), 'Cursor' )),
    COMMETHOD([helpstring(u'A selection that contains the object ids selected by the specified query.')], HRESULT, 'Select',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IQueryFilter), 'QueryFilter' ),
              ( ['in'], comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriSelectionType, 'selType' ),
              ( ['in'], comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriSelectionOption, 'selOption' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspace), 'selectionContainer' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ISelectionSet)), 'ppSelectionSet' )),
    COMMETHOD(['propget', helpstring(u'Identifies if the table contains a geometry field.')], HRESULT, 'HasGeometry',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD(['propget', helpstring(u"Column name of the table's field containing the geometry.")], HRESULT, 'GeometryColumnName',
              ( ['retval', 'out'], POINTER(BSTR), 'pbstrColumnName' )),
    COMMETHOD(['propput', helpstring(u"Column name of the table's field containing the geometry.")], HRESULT, 'GeometryColumnName',
              ( ['in'], BSTR, 'pbstrColumnName' )),
]
################################################################
## code template for ITemporalTable implementation
##class ITemporalTable_Impl(object):
##    def Insert(self, useBuffering):
##        u'Returns a  cursor that can be used to insert new Rows.'
##        #return Cursor
##
##    def Search(self, QueryFilter, Recycling):
##        u'An object cursor that can be used to fetch row objects selected by the specified query.'
##        #return Cursor
##
##    @property
##    def HasGeometry(self):
##        u'Identifies if the table contains a geometry field.'
##        #return pVal
##
##    def AddField(self, Field):
##        u'Adds a field to this object class.'
##        #return 
##
##    @property
##    def Fields(self):
##        u'The fields collection for this object class.'
##        #return Fields
##
##    def DeleteField(self, Field):
##        u'Deletes a field from this object class.'
##        #return 
##
##    def Update(self, QueryFilter, Recycling):
##        u'Returns a cursor that can be used to update Rows selected by the specified query.'
##        #return Cursor
##
##    def GetRow(self, OID):
##        u'The row from the database with the specified object ID.'
##        #return Row
##
##    def CreateRowBuffer(self):
##        u'Creates a row buffer that can be used with an insert cursor.'
##        #return Buffer
##
##    def FindField(self, Name):
##        u'The index of the field with the specified name.'
##        #return FieldIndex
##
##    def _get(self):
##        u"Column name of the table's field containing the geometry."
##        #return pbstrColumnName
##    def _set(self, pbstrColumnName):
##        u"Column name of the table's field containing the geometry."
##    GeometryColumnName = property(_get, _set, doc = _set.__doc__)
##
##    def CreateRow(self):
##        u'Creates a row in the database with a system assigned object ID and null property values.'
##        #return Row
##
##    def Select(self, QueryFilter, selType, selOption, selectionContainer):
##        u'A selection that contains the object ids selected by the specified query.'
##        #return ppSelectionSet
##
##    def RowCount(self, QueryFilter):
##        u'The number of Rows selected by the specified query.'
##        #return NumRows
##

ITemporalObservationsTable._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if the observation table will automatically purge observations that meet a specified criteria, Purge Rule,  when the high-water mark has been exceeded.')], HRESULT, 'AutoPurge',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the observation table will automatically purge observations that meet a specified criteria, Purge Rule,  when the high-water mark has been exceeded.')], HRESULT, 'AutoPurge',
              ( ['in'], VARIANT_BOOL, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'The high-water mark or the number of observations that should not be exceeded Threshold.')], HRESULT, 'Threshold',
              ( ['retval', 'out'], POINTER(VARIANT), 'pvarVal' )),
    COMMETHOD(['propput', helpstring(u'The high-water mark or the number of observations that should not be exceeded Threshold.')], HRESULT, 'Threshold',
              ( ['in'], VARIANT, 'pvarVal' )),
    COMMETHOD(['propget', helpstring(u'The percentage of the maximum allowed number of records to delete when the Purge method is called.')], HRESULT, 'PurgePercentage',
              ( ['retval', 'out'], POINTER(c_double), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'The percentage of the maximum allowed number of records to delete when the Purge method is called.')], HRESULT, 'PurgePercentage',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Reserved for future.')], HRESULT, 'Persistant',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Reserved for future.')], HRESULT, 'Persistant',
              ( ['in'], VARIANT_BOOL, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'The column that is responsible for providing the temporal information. This column must be a character (date/time string parsable) , date-time, timestamp, or time period.')], HRESULT, 'TemporalColumnName',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'The column that is responsible for providing the temporal information. This column must be a character (date/time string parsable) , date-time, timestamp, or time period.')], HRESULT, 'TemporalColumnName',
              ( ['in'], BSTR, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Identifies the purge rule to apply when PruneTable method is called (via user S/W or auto purge criteria).')], HRESULT, 'PurgeRule',
              ( ['retval', 'out'], POINTER(enumPurgeRule), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Identifies the purge rule to apply when PruneTable method is called (via user S/W or auto purge criteria).')], HRESULT, 'PurgeRule',
              ( ['in'], enumPurgeRule, 'pVal' )),
    COMMETHOD([helpstring(u'Apply the purge rule to the temporal table.')], HRESULT, 'PruneTable'),
    COMMETHOD([helpstring(u'Provides the time range of all records in the temporal table.')], HRESULT, 'QueryTemporalExtent',
              ( ['out'], POINTER(VARIANT), 'pvarStartTime' ),
              ( ['out'], POINTER(VARIANT), 'pvarEndTime' )),
]
################################################################
## code template for ITemporalObservationsTable implementation
##class ITemporalObservationsTable_Impl(object):
##    def _get(self):
##        u'The percentage of the maximum allowed number of records to delete when the Purge method is called.'
##        #return pVal
##    def _set(self, pVal):
##        u'The percentage of the maximum allowed number of records to delete when the Purge method is called.'
##    PurgePercentage = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Reserved for future.'
##        #return pVal
##    def _set(self, pVal):
##        u'Reserved for future.'
##    Persistant = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Identifies the purge rule to apply when PruneTable method is called (via user S/W or auto purge criteria).'
##        #return pVal
##    def _set(self, pVal):
##        u'Identifies the purge rule to apply when PruneTable method is called (via user S/W or auto purge criteria).'
##    PurgeRule = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The column that is responsible for providing the temporal information. This column must be a character (date/time string parsable) , date-time, timestamp, or time period.'
##        #return pVal
##    def _set(self, pVal):
##        u'The column that is responsible for providing the temporal information. This column must be a character (date/time string parsable) , date-time, timestamp, or time period.'
##    TemporalColumnName = property(_get, _set, doc = _set.__doc__)
##
##    def PruneTable(self):
##        u'Apply the purge rule to the temporal table.'
##        #return 
##
##    def QueryTemporalExtent(self):
##        u'Provides the time range of all records in the temporal table.'
##        #return pvarStartTime, pvarEndTime
##
##    def _get(self):
##        u'The high-water mark or the number of observations that should not be exceeded Threshold.'
##        #return pvarVal
##    def _set(self, pvarVal):
##        u'The high-water mark or the number of observations that should not be exceeded Threshold.'
##    Threshold = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the observation table will automatically purge observations that meet a specified criteria, Purge Rule,  when the high-water mark has been exceeded.'
##        #return pVal
##    def _set(self, pVal):
##        u'Indicates if the observation table will automatically purge observations that meet a specified criteria, Purge Rule,  when the high-water mark has been exceeded.'
##    AutoPurge = property(_get, _set, doc = _set.__doc__)
##

class TerrainToRasterFunctionArguments(CoClass):
    u'The TerrainToRasterFunction arguments.'
    _reg_clsid_ = GUID('{8BF576CA-96C8-4106-9020-A2D78D221DC4}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
TerrainToRasterFunctionArguments._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._8F0541A3_D5BE_4B3F_A8D9_062D5579E19B_0_10_2.IRasterFunctionArguments, comtypes.gen._8F0541A3_D5BE_4B3F_A8D9_062D5579E19B_0_10_2.IRasterCacheArguments, comtypes.gen._8F0541A3_D5BE_4B3F_A8D9_062D5579E19B_0_10_2.ITerrainToRasterFunctionArguments, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLVersionSupport, comtypes.gen._8F0541A3_D5BE_4B3F_A8D9_062D5579E19B_0_10_2.IItemPaths, comtypes.gen._8F0541A3_D5BE_4B3F_A8D9_062D5579E19B_0_10_2.IItemPaths2]

class ICadastralGroundToGridTools(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods that perform ground to grid conversions.'
    _iid_ = GUID('{69E2D388-48F1-407C-9F35-FC972034336A}')
    _idlflags_ = ['oleautomation']
ICadastralGroundToGridTools._methods_ = [
    COMMETHOD([helpstring(u'Inverse3D calculates the mark-to-mark distance between two points, using the z value on the points as ellipsoid height, and using the spatial reference parameters.')], HRESULT, 'Inverse3D',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference), 'pSR' ),
              ( ['in'], VARIANT_BOOL, 'argumentsInMeters' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'pPoint1' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'pPoint2' ),
              ( ['retval', 'out'], POINTER(c_double), 'pDistance' )),
    COMMETHOD([helpstring(u'Forward3D calculates a new point from an existing point, given the mark-to-mark distance and azimuth measured at the ellipsoid height of the source point. The z-value of the point is treated as an ellipsoid height, and the function uses the spatial reference p?s?\x08?&')], HRESULT, 'Forward3D',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference), 'pSR' ),
              ( ['in'], VARIANT_BOOL, 'argumentsInMeters' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'pPoint1' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'pPoint2Provisional' ),
              ( ['in'], c_double, 'markToMarkDistance' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint)), 'ppPoint' )),
]
################################################################
## code template for ICadastralGroundToGridTools implementation
##class ICadastralGroundToGridTools_Impl(object):
##    def Inverse3D(self, pSR, argumentsInMeters, pPoint1, pPoint2):
##        u'Inverse3D calculates the mark-to-mark distance between two points, using the z value on the points as ellipsoid height, and using the spatial reference parameters.'
##        #return pDistance
##
##    def Forward3D(self, pSR, argumentsInMeters, pPoint1, pPoint2Provisional, markToMarkDistance):
##        u'Forward3D calculates a new point from an existing point, given the mark-to-mark distance and azimuth measured at the ellipsoid height of the source point. The z-value of the point is treated as an ellipsoid height, and the function uses the spatial reference p?s?\x08?&'
##        #return ppPoint
##

class ITxEnumTrackId(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the list of unique Track IDs.'
    _iid_ = GUID('{057B4C30-5C61-4B6C-A24D-B02F98BE418F}')
    _idlflags_ = []
ITxEnumTrackId._methods_ = [
    COMMETHOD(['propget', helpstring(u'Retrives the first Track ID in the list.')], HRESULT, 'FirstTrackId',
              ( ['retval', 'out'], POINTER(BSTR), 'trackId' )),
    COMMETHOD(['propget', helpstring(u'Retrives the next Track ID in the list.')], HRESULT, 'NextTrackId',
              ( ['retval', 'out'], POINTER(BSTR), 'trackId' )),
    COMMETHOD(['propget', helpstring(u'Retrives the Track ID list.')], HRESULT, 'TrackIds',
              ( ['retval', 'out'], POINTER(_midlSAFEARRAY(BSTR)), 'TrackIds' )),
    COMMETHOD(['propget', helpstring(u'Returns a selection set of features in a given track.')], HRESULT, 'TrackFeatures',
              ( ['in'], BSTR, 'trackId' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ISelectionSet)), 'features' )),
    COMMETHOD(['propget', helpstring(u'Returns the time that a given track was last updated.')], HRESULT, 'LastUpdateTime',
              ( ['in'], BSTR, 'trackId' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITime)), 'LastUpdateTime' )),
    COMMETHOD([helpstring(u'Returns the start and end times of a given track.')], HRESULT, 'QueryTrackTimeExtent',
              ( ['in'], BSTR, 'trackId' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITime)), 'startTime' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITime)), 'endTime' )),
]
################################################################
## code template for ITxEnumTrackId implementation
##class ITxEnumTrackId_Impl(object):
##    @property
##    def TrackFeatures(self, trackId):
##        u'Returns a selection set of features in a given track.'
##        #return features
##
##    @property
##    def LastUpdateTime(self, trackId):
##        u'Returns the time that a given track was last updated.'
##        #return LastUpdateTime
##
##    @property
##    def NextTrackId(self):
##        u'Retrives the next Track ID in the list.'
##        #return trackId
##
##    def QueryTrackTimeExtent(self, trackId):
##        u'Returns the start and end times of a given track.'
##        #return startTime, endTime
##
##    @property
##    def TrackIds(self):
##        u'Retrives the Track ID list.'
##        #return TrackIds
##
##    @property
##    def FirstTrackId(self):
##        u'Retrives the first Track ID in the list.'
##        #return trackId
##

class IListener(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to enable notification to the display controller when data is added or removed.'
    _iid_ = GUID('{D890E524-DAB5-11D5-B811-00010265ADC5}')
    _idlflags_ = ['oleautomation']
IListener._methods_ = [
    COMMETHOD([helpstring(u'Adds data to the display controller.')], HRESULT, 'AddData',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'piFeatureClass' ),
              ( ['in'], c_double, 'dXMin' ),
              ( ['in'], c_double, 'dYMin' ),
              ( ['in'], c_double, 'dXMax' ),
              ( ['in'], c_double, 'dYMax' )),
    COMMETHOD([helpstring(u'Removes data from the display controller.')], HRESULT, 'RemoveData',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'piFeatureClass' ),
              ( ['in'], c_double, 'dXMin' ),
              ( ['in'], c_double, 'dYMin' ),
              ( ['in'], c_double, 'dXMax' ),
              ( ['in'], c_double, 'dYMax' )),
]
################################################################
## code template for IListener implementation
##class IListener_Impl(object):
##    def RemoveData(self, piFeatureClass, dXMin, dYMin, dXMax, dYMax):
##        u'Removes data from the display controller.'
##        #return 
##
##    def AddData(self, piFeatureClass, dXMin, dYMin, dXMax, dYMax):
##        u'Adds data to the display controller.'
##        #return 
##

class ITerrainDataSource(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of Terrain Data Source.'
    _iid_ = GUID('{4D228018-1EC1-4FCC-9646-9C6A67F9EF3C}')
    _idlflags_ = ['oleautomation']
class ITerrainDataSource2(ITerrainDataSource):
    _case_insensitive_ = True
    u'Provides access to members of Terrain Data Source.'
    _iid_ = GUID('{17B45AAF-FDB2-4492-87C6-9578B20001BD}')
    _idlflags_ = ['oleautomation']
ITerrainDataSource._methods_ = [
    COMMETHOD(['propput', helpstring(u'The unique database identifier for the feature class.')], HRESULT, 'FeatureClassID',
              ( ['in'], c_int, 'pClassID' )),
    COMMETHOD(['propget', helpstring(u'The unique database identifier for the feature class.')], HRESULT, 'FeatureClassID',
              ( ['retval', 'out'], POINTER(c_int), 'pClassID' )),
    COMMETHOD(['propput', helpstring(u"The identifier of the terrain's thematic group to which this feature class belongs.")], HRESULT, 'GroupID',
              ( ['in'], c_int, 'pGroupID' )),
    COMMETHOD(['propget', helpstring(u"The identifier of the terrain's thematic group to which this feature class belongs.")], HRESULT, 'GroupID',
              ( ['retval', 'out'], POINTER(c_int), 'pGroupID' )),
    COMMETHOD(['propput', helpstring(u'The database column providing heights for the features.')], HRESULT, 'HeightField',
              ( ['in'], BSTR, 'pFieldName' )),
    COMMETHOD(['propget', helpstring(u'The database column providing heights for the features.')], HRESULT, 'HeightField',
              ( ['retval', 'out'], POINTER(BSTR), 'pFieldName' )),
    COMMETHOD(['propput', helpstring(u'The database column providing tag values for TIN elements derived from the terrain.')], HRESULT, 'TagValueField',
              ( ['in'], BSTR, 'pFieldName' )),
    COMMETHOD(['propget', helpstring(u'The database column providing tag values for TIN elements derived from the terrain.')], HRESULT, 'TagValueField',
              ( ['retval', 'out'], POINTER(BSTR), 'pFieldName' )),
    COMMETHOD(['propput', helpstring(u'Indicates how the features are used to define the terrain surface.')], HRESULT, 'SurfaceFeatureType',
              ( ['in'], comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriTinSurfaceType, 'pType' )),
    COMMETHOD(['propget', helpstring(u'Indicates how the features are used to define the terrain surface.')], HRESULT, 'SurfaceFeatureType',
              ( ['retval', 'out'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriTinSurfaceType), 'pType' )),
    COMMETHOD(['propput', helpstring(u"Indicates if the 'breakline' data source should be added to the overview Terrain.")], HRESULT, 'ApplyToOverviewTerrain',
              ( ['in'], VARIANT_BOOL, 'pbApply' )),
    COMMETHOD(['propget', helpstring(u"Indicates if the 'breakline' data source should be added to the overview Terrain.")], HRESULT, 'ApplyToOverviewTerrain',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbApply' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether or not the data source is contained by the terrain.')], HRESULT, 'Embedded',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbEmbedded' )),
    COMMETHOD([helpstring(u'Sets the lower and upper resolution bounds in which the line/area data source participates in the triangulation.')], HRESULT, 'SetResolutionBounds',
              ( ['in'], c_double, 'lowerBound' ),
              ( ['in'], c_double, 'upperBound' )),
    COMMETHOD([helpstring(u'Returns the lower and upper resolution bounds in which the line/area data source participates in the triangulation.')], HRESULT, 'QueryResolutionBounds',
              ( ['out'], POINTER(c_double), 'pLowerBound' ),
              ( ['out'], POINTER(c_double), 'pUpperBound' )),
]
################################################################
## code template for ITerrainDataSource implementation
##class ITerrainDataSource_Impl(object):
##    def SetResolutionBounds(self, lowerBound, upperBound):
##        u'Sets the lower and upper resolution bounds in which the line/area data source participates in the triangulation.'
##        #return 
##
##    def _get(self):
##        u'The database column providing tag values for TIN elements derived from the terrain.'
##        #return pFieldName
##    def _set(self, pFieldName):
##        u'The database column providing tag values for TIN elements derived from the terrain.'
##    TagValueField = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Embedded(self):
##        u'Indicates whether or not the data source is contained by the terrain.'
##        #return pbEmbedded
##
##    def _get(self):
##        u"Indicates if the 'breakline' data source should be added to the overview Terrain."
##        #return pbApply
##    def _set(self, pbApply):
##        u"Indicates if the 'breakline' data source should be added to the overview Terrain."
##    ApplyToOverviewTerrain = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates how the features are used to define the terrain surface.'
##        #return pType
##    def _set(self, pType):
##        u'Indicates how the features are used to define the terrain surface.'
##    SurfaceFeatureType = property(_get, _set, doc = _set.__doc__)
##
##    def QueryResolutionBounds(self):
##        u'Returns the lower and upper resolution bounds in which the line/area data source participates in the triangulation.'
##        #return pLowerBound, pUpperBound
##
##    def _get(self):
##        u'The database column providing heights for the features.'
##        #return pFieldName
##    def _set(self, pFieldName):
##        u'The database column providing heights for the features.'
##    HeightField = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u"The identifier of the terrain's thematic group to which this feature class belongs."
##        #return pGroupID
##    def _set(self, pGroupID):
##        u"The identifier of the terrain's thematic group to which this feature class belongs."
##    GroupID = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The unique database identifier for the feature class.'
##        #return pClassID
##    def _set(self, pClassID):
##        u'The unique database identifier for the feature class.'
##    FeatureClassID = property(_get, _set, doc = _set.__doc__)
##

ITerrainDataSource2._methods_ = [
    COMMETHOD(['propput', helpstring(u'Indicates if this is an anchor-points data source.')], HRESULT, 'Anchored',
              ( ['in'], VARIANT_BOOL, 'pbAnchored' )),
    COMMETHOD(['propget', helpstring(u'Indicates if this is an anchor-points data source.')], HRESULT, 'Anchored',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbAnchored' )),
]
################################################################
## code template for ITerrainDataSource2 implementation
##class ITerrainDataSource2_Impl(object):
##    def _get(self):
##        u'Indicates if this is an anchor-points data source.'
##        #return pbAnchored
##    def _set(self, pbAnchored):
##        u'Indicates if this is an anchor-points data source.'
##    Anchored = property(_get, _set, doc = _set.__doc__)
##

class ITemporalWorkspaceStatistics(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to properties and methods needed to manage message rate statistics in workspace.'
    _iid_ = GUID('{052AC5B2-CDC1-479D-B69E-479E34A2C071}')
    _idlflags_ = ['oleautomation']
class ITemporalWorkspaceStatistics2(ITemporalWorkspaceStatistics):
    _case_insensitive_ = True
    u'Provides access to properties and methods needed to manage message rate statistics in workspace.'
    _iid_ = GUID('{F5677CCF-E3D7-4B9A-8803-670895AA262F}')
    _idlflags_ = ['oleautomation']
ITemporalWorkspaceStatistics._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates track count for each TemporalFeatureClass under the workspace or workspace factory.')], HRESULT, 'AllTrackCounts',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'ppiAllTrackCounts' )),
    COMMETHOD(['propget', helpstring(u'Indicates message rate for each TemporalFeatureClass under the workspace or workspace factory.')], HRESULT, 'AllMessageRates',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'ppiAllMessageRates' )),
    COMMETHOD(['propget', helpstring(u'Indicates sample size used for calculating message rate for each TemporalFeatureClass under the workspace or workspace factory.')], HRESULT, 'AllSampleSizes',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'ppiAllSampleSizes' )),
    COMMETHOD(['propget', helpstring(u'Indicates the total number of features logged for each TemporalFeatureClass under the workspace or workspace factory.')], HRESULT, 'AllTotalFeatureCounts',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'ppiAllTotalFeatureCounts' )),
    COMMETHOD(['propget', helpstring(u'Indicates the connection status of each workspace under the workspace factory')], HRESULT, 'ConnectionStatus',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'ppiConnectionStatus' )),
    COMMETHOD(['propget', helpstring(u'Indicates total number of messages received.')], HRESULT, 'ReceivedMessageCounts',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'ppiReceivedMsgCounts' )),
    COMMETHOD(['propget', helpstring(u'Indicates total number of messages pulled.')], HRESULT, 'PulledMessageCounts',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'ppiPulledMsgCounts' )),
    COMMETHOD(['propget', helpstring(u'Indicates total number of messages discarded.')], HRESULT, 'DiscardedMessageCounts',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'ppiDiscardedMsgCounts' )),
    COMMETHOD(['propget', helpstring(u'Indicates current number of messages discarded.')], HRESULT, 'CurrentDiscardedMessageCounts',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'ppiCurDiscardedMsgCounts' )),
    COMMETHOD(['propget', helpstring(u'Indicates total number of messages queued.')], HRESULT, 'QueuedMessageCounts',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'ppiQueuedMsgCounts' )),
    COMMETHOD([helpstring(u'Resets total feature count for each TemporalFeatureClass under the workspace or workspace factory.')], HRESULT, 'ResetAllFeatureCounts'),
    COMMETHOD([helpstring(u'Resets message rate for each TemporalFeatureClass under the workspace or workspace factory.')], HRESULT, 'ResetAllMessageRates'),
    COMMETHOD([helpstring(u'Sets sample size for each TemporalFeatureClass under the workspace or workspace factory.')], HRESULT, 'SetAllSampleSizes',
              ( ['in'], c_int, 'lSampleSize' )),
]
################################################################
## code template for ITemporalWorkspaceStatistics implementation
##class ITemporalWorkspaceStatistics_Impl(object):
##    @property
##    def AllTrackCounts(self):
##        u'Indicates track count for each TemporalFeatureClass under the workspace or workspace factory.'
##        #return ppiAllTrackCounts
##
##    def SetAllSampleSizes(self, lSampleSize):
##        u'Sets sample size for each TemporalFeatureClass under the workspace or workspace factory.'
##        #return 
##
##    @property
##    def DiscardedMessageCounts(self):
##        u'Indicates total number of messages discarded.'
##        #return ppiDiscardedMsgCounts
##
##    @property
##    def ConnectionStatus(self):
##        u'Indicates the connection status of each workspace under the workspace factory'
##        #return ppiConnectionStatus
##
##    @property
##    def CurrentDiscardedMessageCounts(self):
##        u'Indicates current number of messages discarded.'
##        #return ppiCurDiscardedMsgCounts
##
##    @property
##    def AllMessageRates(self):
##        u'Indicates message rate for each TemporalFeatureClass under the workspace or workspace factory.'
##        #return ppiAllMessageRates
##
##    @property
##    def AllSampleSizes(self):
##        u'Indicates sample size used for calculating message rate for each TemporalFeatureClass under the workspace or workspace factory.'
##        #return ppiAllSampleSizes
##
##    @property
##    def QueuedMessageCounts(self):
##        u'Indicates total number of messages queued.'
##        #return ppiQueuedMsgCounts
##
##    @property
##    def AllTotalFeatureCounts(self):
##        u'Indicates the total number of features logged for each TemporalFeatureClass under the workspace or workspace factory.'
##        #return ppiAllTotalFeatureCounts
##
##    def ResetAllMessageRates(self):
##        u'Resets message rate for each TemporalFeatureClass under the workspace or workspace factory.'
##        #return 
##
##    @property
##    def PulledMessageCounts(self):
##        u'Indicates total number of messages pulled.'
##        #return ppiPulledMsgCounts
##
##    def ResetAllFeatureCounts(self):
##        u'Resets total feature count for each TemporalFeatureClass under the workspace or workspace factory.'
##        #return 
##
##    @property
##    def ReceivedMessageCounts(self):
##        u'Indicates total number of messages received.'
##        #return ppiReceivedMsgCounts
##

ITemporalWorkspaceStatistics2._methods_ = [
    COMMETHOD(['propget', helpstring(u'The time the connection was established.')], HRESULT, 'ConnectionTime',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITime)), 'ConnectionTime' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether a service is currently subscribed to.')], HRESULT, 'Subscribed',
              ( ['in'], BSTR, 'serviceName' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Subscribed' )),
    COMMETHOD(['propget', helpstring(u'The time the subscription to the service was established.')], HRESULT, 'SubscriptionTime',
              ( ['in'], BSTR, 'serviceName' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITime)), 'SubscriptionTime' )),
]
################################################################
## code template for ITemporalWorkspaceStatistics2 implementation
##class ITemporalWorkspaceStatistics2_Impl(object):
##    @property
##    def SubscriptionTime(self, serviceName):
##        u'The time the subscription to the service was established.'
##        #return SubscriptionTime
##
##    @property
##    def ConnectionTime(self):
##        u'The time the connection was established.'
##        #return ConnectionTime
##
##    @property
##    def Subscribed(self, serviceName):
##        u'Indicates whether a service is currently subscribed to.'
##        #return Subscribed
##

class ITerrain2(ITerrain):
    _case_insensitive_ = True
    u'Provides access to members used to acquire information about a Terrain and to retrieve DynamicSurface objects from which raster and TIN surfaces are made.'
    _iid_ = GUID('{5D6D7322-D2D5-4C16-A52D-0B1199EFA98D}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriTerrainPyramidType'
esriTerrainPyramidZTolerance = 0
esriTerrainPyramidWindowSize = 1
esriTerrainPyramidType = c_int # enum
ITerrain._methods_ = [
    COMMETHOD(['propget', helpstring(u'The name of the terrain.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pName' )),
    COMMETHOD(['propget', helpstring(u'The database identifier of the terrain.')], HRESULT, 'ID',
              ( ['retval', 'out'], POINTER(c_int), 'pID' )),
    COMMETHOD(['propget', helpstring(u'The total number of points in the Terrain.')], HRESULT, 'Size',
              ( ['retval', 'out'], POINTER(c_double), 'pcPoints' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether or not a full build is required.')], HRESULT, 'IsValid',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbIsValid' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether or not a partial rebuild is needed.')], HRESULT, 'IsDirty',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbIsDirty' )),
    COMMETHOD(['propget', helpstring(u'The spatial reference of the terrain.')], HRESULT, 'SpatialReference',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference)), 'ppSpatialRef' )),
    COMMETHOD(['propget', helpstring(u'The approximate xyz extent of the terrain.')], HRESULT, 'Extent',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'ppExtent' )),
    COMMETHOD(['propget', helpstring(u'The feature dataset which contains the terrain.')], HRESULT, 'FeatureDataset',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureDataset)), 'ppDataset' )),
    COMMETHOD(['propget', helpstring(u'The number of data sources participating in the terrain.')], HRESULT, 'DataSourceCount',
              ( ['retval', 'out'], POINTER(c_int), 'pcDataSources' )),
    COMMETHOD(['propget', helpstring(u'Returns the data source specified by the index.')], HRESULT, 'DataSource',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(ITerrainDataSource)), 'ppDataSource' )),
    COMMETHOD(['propget', helpstring(u'The number of pyramid levels in the terrain.')], HRESULT, 'PyramidLevelCount',
              ( ['retval', 'out'], POINTER(c_int), 'pcPyramidLevels' )),
    COMMETHOD(['propget', helpstring(u'Returns the pyramid level specified by the index.')], HRESULT, 'PyramidLevel',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(ITerrainPyramidLevel)), 'ppPyramidLevel' )),
    COMMETHOD(['propget', helpstring(u'The horizontal distance used to spatially index and partition terrain data.')], HRESULT, 'TileSize',
              ( ['retval', 'out'], POINTER(c_double), 'pSize' )),
    COMMETHOD(['propget', helpstring(u'The pyramid type of this Terrain.')], HRESULT, 'PyramidType',
              ( ['retval', 'out'], POINTER(esriTerrainPyramidType), 'pType' )),
    COMMETHOD(['propget', helpstring(u'The maximum number of points in the most generalized representation of a Terrain.')], HRESULT, 'MaxOverviewTerrainPoints',
              ( ['retval', 'out'], POINTER(c_int), 'pcPoints' )),
    COMMETHOD(['propget', helpstring(u'The maximum number of vertices per multipoint.')], HRESULT, 'MaxPointsPerShape',
              ( ['retval', 'out'], POINTER(c_int), 'pcPoints' )),
    COMMETHOD([helpstring(u'Returns horizontal partitioning information about the terrain data.')], HRESULT, 'QueryTileInfo',
              ( ['out'], POINTER(c_int), 'pRowBegin' ),
              ( ['out'], POINTER(c_int), 'pRowEnd' ),
              ( ['out'], POINTER(c_int), 'pColBegin' ),
              ( ['out'], POINTER(c_int), 'pColEnd' ),
              ( ['out'], POINTER(c_double), 'pXMin' ),
              ( ['out'], POINTER(c_double), 'pYMin' ),
              ( ['out'], POINTER(c_double), 'pTileSize' ),
              ( ['out'], POINTER(c_int), 'pRowCountDomain' ),
              ( ['out'], POINTER(c_int), 'pColCountDomain' )),
    COMMETHOD([helpstring(u'Returns all dirty tiles.')], HRESULT, 'GetDirtyTiles',
              ( ['retval', 'out'], POINTER(POINTER(IEnumEnvelope)), 'ppTiles' )),
    COMMETHOD([helpstring(u'Returns the approximate number of points in the terrain within a given area and at a particular pyramid level.')], HRESULT, 'GetPointCount',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'pAOI' ),
              ( ['in'], c_double, 'Resolution' ),
              ( ['retval', 'out'], POINTER(c_double), 'pcPoints' )),
    COMMETHOD([helpstring(u'Returns an implicit surface from which TINs and rasters are derived.')], HRESULT, 'CreateDynamicSurface',
              ( ['retval', 'out'], POINTER(POINTER(IDynamicSurface)), 'ppDynamicSurface' )),
    COMMETHOD([helpstring(u'Copies features of an embedded data source to the specified feature class.')], HRESULT, 'ExtractFromEmbeddedDataSource',
              ( ['in'], c_int, 'index' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'pFeatureClass' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'pAOI' ),
              ( ['in'], c_double, 'Resolution' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' )),
]
################################################################
## code template for ITerrain implementation
##class ITerrain_Impl(object):
##    def CreateDynamicSurface(self):
##        u'Returns an implicit surface from which TINs and rasters are derived.'
##        #return ppDynamicSurface
##
##    @property
##    def PyramidLevelCount(self):
##        u'The number of pyramid levels in the terrain.'
##        #return pcPyramidLevels
##
##    def ExtractFromEmbeddedDataSource(self, index, pFeatureClass, pAOI, Resolution, pTrackCancel):
##        u'Copies features of an embedded data source to the specified feature class.'
##        #return 
##
##    @property
##    def Name(self):
##        u'The name of the terrain.'
##        #return pName
##
##    @property
##    def TileSize(self):
##        u'The horizontal distance used to spatially index and partition terrain data.'
##        #return pSize
##
##    @property
##    def IsValid(self):
##        u'Indicates whether or not a full build is required.'
##        #return pbIsValid
##
##    @property
##    def PyramidLevel(self, index):
##        u'Returns the pyramid level specified by the index.'
##        #return ppPyramidLevel
##
##    @property
##    def DataSourceCount(self):
##        u'The number of data sources participating in the terrain.'
##        #return pcDataSources
##
##    @property
##    def PyramidType(self):
##        u'The pyramid type of this Terrain.'
##        #return pType
##
##    @property
##    def MaxPointsPerShape(self):
##        u'The maximum number of vertices per multipoint.'
##        #return pcPoints
##
##    @property
##    def SpatialReference(self):
##        u'The spatial reference of the terrain.'
##        #return ppSpatialRef
##
##    def GetPointCount(self, pAOI, Resolution):
##        u'Returns the approximate number of points in the terrain within a given area and at a particular pyramid level.'
##        #return pcPoints
##
##    @property
##    def MaxOverviewTerrainPoints(self):
##        u'The maximum number of points in the most generalized representation of a Terrain.'
##        #return pcPoints
##
##    @property
##    def DataSource(self, index):
##        u'Returns the data source specified by the index.'
##        #return ppDataSource
##
##    @property
##    def Extent(self):
##        u'The approximate xyz extent of the terrain.'
##        #return ppExtent
##
##    def QueryTileInfo(self):
##        u'Returns horizontal partitioning information about the terrain data.'
##        #return pRowBegin, pRowEnd, pColBegin, pColEnd, pXMin, pYMin, pTileSize, pRowCountDomain, pColCountDomain
##
##    @property
##    def IsDirty(self):
##        u'Indicates whether or not a partial rebuild is needed.'
##        #return pbIsDirty
##
##    @property
##    def FeatureDataset(self):
##        u'The feature dataset which contains the terrain.'
##        #return ppDataset
##
##    @property
##    def ID(self):
##        u'The database identifier of the terrain.'
##        #return pID
##
##    def GetDirtyTiles(self):
##        u'Returns all dirty tiles.'
##        #return ppTiles
##
##    @property
##    def Size(self):
##        u'The total number of points in the Terrain.'
##        #return pcPoints
##

ITerrain2._methods_ = [
    COMMETHOD([helpstring(u"Returns the 'Shape' field name of the embedded data sources.")], HRESULT, 'GetEmbeddedDataSourceShapeFieldName',
              ( ['retval', 'out'], POINTER(BSTR), 'pName' )),
    COMMETHOD([helpstring(u'Returns a Search Cursor on the specified embedded data source.')], HRESULT, 'SearchFromEmbeddedDataSource',
              ( ['in'], c_int, 'index' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'pAOI' ),
              ( ['in'], c_double, 'Resolution' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray), 'pSubFields' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureCursor)), 'ppCursor' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray)), 'ppFieldIndices' )),
]
################################################################
## code template for ITerrain2 implementation
##class ITerrain2_Impl(object):
##    def GetEmbeddedDataSourceShapeFieldName(self):
##        u"Returns the 'Shape' field name of the embedded data sources."
##        #return pName
##
##    def SearchFromEmbeddedDataSource(self, index, pAOI, Resolution, pSubFields):
##        u'Returns a Search Cursor on the specified embedded data source.'
##        #return ppCursor, ppFieldIndices
##

IDynamicSurface2._methods_ = [
    COMMETHOD(['propput', helpstring(u'Indicates whether or not resource uasge should be minimized.')], HRESULT, 'MinimizeResourceUsage',
              ( ['in'], VARIANT_BOOL, 'pbMinimize' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether or not resource uasge should be minimized.')], HRESULT, 'MinimizeResourceUsage',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbMinimize' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether or not to refine boundary matching.')], HRESULT, 'RefineBoundaryMatching',
              ( ['in'], VARIANT_BOOL, 'pbRefine' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether or not to refine boundary matching.')], HRESULT, 'RefineBoundaryMatching',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbRefine' )),
    COMMETHOD([helpstring(u'Interpolates z values for a defined geometric shape.')], HRESULT, 'InterpolateShape',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'pInShape' ),
              ( ['in'], c_double, 'Resolution' ),
              ( ['in'], comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriSurfaceInterpolationType, 'Type' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry)), 'ppOutShape' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'pStepSize' )),
    COMMETHOD([helpstring(u'Interpolates z values for a defined geometric shape.')], HRESULT, 'InterpolateShapeVertices',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'pInShape' ),
              ( ['in'], c_double, 'Resolution' ),
              ( ['in'], comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriSurfaceInterpolationType, 'Type' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry)), 'ppOutShape' )),
    COMMETHOD([helpstring(u'Interpolates z values for features.')], HRESULT, 'InterpolateFeatureClass',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'pInFeatureClass' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IQueryFilter), 'pFilter' ),
              ( ['in'], c_double, 'Resolution' ),
              ( ['in'], comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriSurfaceInterpolationType, 'Type' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'pOutFeatureClass' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'pStepSize' )),
    COMMETHOD([helpstring(u'Interpolates z values for features.')], HRESULT, 'InterpolateFeatureCursor',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureCursor), 'pCursor' ),
              ( ['in'], c_double, 'Resolution' ),
              ( ['in'], comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriSurfaceInterpolationType, 'Type' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'pOutFeatureClass' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'pStepSize' )),
    COMMETHOD([helpstring(u'Interpolates z values for features.')], HRESULT, 'InterpolateFeatureClassVertices',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'pInFeatureClass' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IQueryFilter), 'pFilter' ),
              ( ['in'], c_double, 'Resolution' ),
              ( ['in'], comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriSurfaceInterpolationType, 'Type' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'pOutFeatureClass' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' )),
    COMMETHOD([helpstring(u'Interpolates z values for features.')], HRESULT, 'InterpolateFeatureCursorVertices',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureCursor), 'pCursor' ),
              ( ['in'], c_double, 'Resolution' ),
              ( ['in'], comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriSurfaceInterpolationType, 'Type' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'pOutFeatureClass' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' )),
    COMMETHOD(['propget', helpstring(u'Indicates if earth curvature can be applied.')], HRESULT, 'CanDoCurvature',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbCanDo' )),
    COMMETHOD([helpstring(u'Returns a line-of-sight.')], HRESULT, 'GetLineOfSight',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'pObserver' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'pTarget' ),
              ( ['in'], c_double, 'Resolution' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint)), 'ppObstruction' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPolyline)), 'ppVisibleLines' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPolyline)), 'ppInvisibleLines' ),
              ( ['out'], POINTER(VARIANT_BOOL), 'pbIsVisible' ),
              ( ['in'], VARIANT_BOOL, 'bApplyCurvature' ),
              ( ['in'], VARIANT_BOOL, 'bApplyRefraction' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'pRefractionFactor' )),
    COMMETHOD([helpstring(u'Get line-of-sight.')], HRESULT, 'GetLineOfSightFeatureCursor',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureCursor), 'pCursor' ),
              ( ['in'], c_double, 'Resolution' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'pOutputLines' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'pObstructionPoints' ),
              ( ['in'], VARIANT_BOOL, 'bApplyCurvature' ),
              ( ['in'], VARIANT_BOOL, 'bApplyRefraction' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'pRefractionFactor' )),
    COMMETHOD([helpstring(u"Get tile-based terrain's Data Area.")], HRESULT, 'GetTileBasedDataArea',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPolygon)), 'ppDataArea' )),
]
################################################################
## code template for IDynamicSurface2 implementation
##class IDynamicSurface2_Impl(object):
##    def InterpolateFeatureClass(self, pInFeatureClass, pFilter, Resolution, Type, pOutFeatureClass, pTrackCancel, pStepSize):
##        u'Interpolates z values for features.'
##        #return 
##
##    def InterpolateFeatureCursor(self, pCursor, Resolution, Type, pOutFeatureClass, pTrackCancel, pStepSize):
##        u'Interpolates z values for features.'
##        #return 
##
##    def InterpolateShapeVertices(self, pInShape, Resolution, Type, pTrackCancel):
##        u'Interpolates z values for a defined geometric shape.'
##        #return ppOutShape
##
##    def GetTileBasedDataArea(self, pTrackCancel):
##        u"Get tile-based terrain's Data Area."
##        #return ppDataArea
##
##    def GetLineOfSight(self, pObserver, pTarget, Resolution, pTrackCancel, bApplyCurvature, bApplyRefraction, pRefractionFactor):
##        u'Returns a line-of-sight.'
##        #return ppObstruction, ppVisibleLines, ppInvisibleLines, pbIsVisible
##
##    def InterpolateFeatureCursorVertices(self, pCursor, Resolution, Type, pOutFeatureClass, pTrackCancel):
##        u'Interpolates z values for features.'
##        #return 
##
##    def _get(self):
##        u'Indicates whether or not to refine boundary matching.'
##        #return pbRefine
##    def _set(self, pbRefine):
##        u'Indicates whether or not to refine boundary matching.'
##    RefineBoundaryMatching = property(_get, _set, doc = _set.__doc__)
##
##    def InterpolateFeatureClassVertices(self, pInFeatureClass, pFilter, Resolution, Type, pOutFeatureClass, pTrackCancel):
##        u'Interpolates z values for features.'
##        #return 
##
##    def InterpolateShape(self, pInShape, Resolution, Type, pTrackCancel, pStepSize):
##        u'Interpolates z values for a defined geometric shape.'
##        #return ppOutShape
##
##    def GetLineOfSightFeatureCursor(self, pCursor, Resolution, pTrackCancel, pOutputLines, pObstructionPoints, bApplyCurvature, bApplyRefraction, pRefractionFactor):
##        u'Get line-of-sight.'
##        #return 
##
##    def _get(self):
##        u'Indicates whether or not resource uasge should be minimized.'
##        #return pbMinimize
##    def _set(self, pbMinimize):
##        u'Indicates whether or not resource uasge should be minimized.'
##    MinimizeResourceUsage = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def CanDoCurvature(self):
##        u'Indicates if earth curvature can be applied.'
##        #return pbCanDo
##

IDynamicSurface3._methods_ = [
    COMMETHOD([helpstring(u'Create terrain block cursor.')], HRESULT, 'CreateBlockCursor',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'pAOI' ),
              ( ['in'], c_double, 'Resolution' ),
              ( ['in'], VARIANT_BOOL, 'bSingleTileOnly' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( ['out'], POINTER(POINTER(ITerrainBlockCursor)), 'pCursor' )),
    COMMETHOD([helpstring(u'Create terrain block cursor.')], HRESULT, 'ConvertToExtent',
              ( ['in'], c_int, 'rowBegin' ),
              ( ['in'], c_int, 'rowEnd' ),
              ( ['in'], c_int, 'colBegin' ),
              ( ['in'], c_int, 'colEnd' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'ppExtent' )),
    COMMETHOD([helpstring(u'Generate contours of the terrain surface.')], HRESULT, 'ContourList',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'pAOI' ),
              ( ['in'], c_double, 'Resolution' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDoubleArray), 'pBreaks' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'pOutFeatureClass' ),
              ( ['in'], BSTR, 'FieldName' ),
              ( ['in'], c_int, 'digitsAfterDecimalPoint' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' )),
    COMMETHOD([helpstring(u'Generate contours of the terrain surface based on a root value and an interval.')], HRESULT, 'Contour',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'pAOI' ),
              ( ['in'], c_double, 'Resolution' ),
              ( ['in'], c_double, 'referenceContourHeight' ),
              ( ['in'], c_double, 'interval' ),
              ( ['in'], BSTR, 'elevationFieldName' ),
              ( ['in'], c_int, 'indexContourFactor' ),
              ( ['in'], BSTR, 'indexContourFieldName' ),
              ( ['in'], c_int, 'digitsAfterDecimalPoint' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'pOutFeatureClass' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' )),
    COMMETHOD([helpstring(u'Returns volume and/or area above or below an input z value.')], HRESULT, 'GetVolumeAndArea',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'pAOI' ),
              ( ['in'], c_double, 'Resolution' ),
              ( ['in'], c_double, 'reference' ),
              ( ['in'], comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriPlaneReferenceType, 'Type' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( ['out'], POINTER(VARIANT_BOOL), 'pbIsOutsideDataArea' ),
              ( ['in', 'out', 'optional'], POINTER(VARIANT), 'pVolume' ),
              ( ['in', 'out', 'optional'], POINTER(VARIANT), 'pSurfaceArea' ),
              ( ['in', 'out', 'optional'], POINTER(VARIANT), 'pProjectedArea' )),
    COMMETHOD([helpstring(u'Intersect with another surface.')], HRESULT, 'Intersect',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'pAOI' ),
              ( ['in'], c_double, 'Resolution' ),
              ( ['in'], POINTER(IUnknown), 'pReferenceSurface' ),
              ( ['in'], c_double, 'referenceRsolution' ),
              ( ['in'], VARIANT_BOOL, 'bReverse' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'pOutFeatureClass' ),
              ( ['in'], BSTR, 'volumeFieldName' ),
              ( ['in'], BSTR, 'surfaceAreaFieldName' ),
              ( ['in'], BSTR, 'codeFieldName' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' )),
    COMMETHOD(['propput', helpstring(u'The profile weeding tolerance.')], HRESULT, 'ProfileWeedTolerance',
              ( ['in'], c_double, 'pTolerance' )),
    COMMETHOD(['propget', helpstring(u'The profile weeding tolerance.')], HRESULT, 'ProfileWeedTolerance',
              ( ['retval', 'out'], POINTER(c_double), 'pTolerance' )),
    COMMETHOD(['propget', helpstring(u'Multiplication factor applied to all z values to provide unit-congruency between coordinate components.')], HRESULT, 'ZFactor',
              ( ['retval', 'out'], POINTER(c_double), 'pFactor' )),
    COMMETHOD(['propput', helpstring(u'Multiplication factor applied to all z values to provide unit-congruency between coordinate components.')], HRESULT, 'ZFactor',
              ( ['in'], c_double, 'pFactor' )),
]
################################################################
## code template for IDynamicSurface3 implementation
##class IDynamicSurface3_Impl(object):
##    def _get(self):
##        u'The profile weeding tolerance.'
##        #return pTolerance
##    def _set(self, pTolerance):
##        u'The profile weeding tolerance.'
##    ProfileWeedTolerance = property(_get, _set, doc = _set.__doc__)
##
##    def ContourList(self, pAOI, Resolution, pBreaks, pOutFeatureClass, FieldName, digitsAfterDecimalPoint, pTrackCancel):
##        u'Generate contours of the terrain surface.'
##        #return 
##
##    def CreateBlockCursor(self, pAOI, Resolution, bSingleTileOnly, pTrackCancel):
##        u'Create terrain block cursor.'
##        #return pCursor
##
##    def ConvertToExtent(self, rowBegin, rowEnd, colBegin, colEnd):
##        u'Create terrain block cursor.'
##        #return ppExtent
##
##    def GetVolumeAndArea(self, pAOI, Resolution, reference, Type, pTrackCancel):
##        u'Returns volume and/or area above or below an input z value.'
##        #return pbIsOutsideDataArea, pVolume, pSurfaceArea, pProjectedArea
##
##    def _get(self):
##        u'Multiplication factor applied to all z values to provide unit-congruency between coordinate components.'
##        #return pFactor
##    def _set(self, pFactor):
##        u'Multiplication factor applied to all z values to provide unit-congruency between coordinate components.'
##    ZFactor = property(_get, _set, doc = _set.__doc__)
##
##    def Intersect(self, pAOI, Resolution, pReferenceSurface, referenceRsolution, bReverse, pOutFeatureClass, volumeFieldName, surfaceAreaFieldName, codeFieldName, pTrackCancel):
##        u'Intersect with another surface.'
##        #return 
##
##    def Contour(self, pAOI, Resolution, referenceContourHeight, interval, elevationFieldName, indexContourFactor, indexContourFieldName, digitsAfterDecimalPoint, pOutFeatureClass, pTrackCancel):
##        u'Generate contours of the terrain surface based on a root value and an interval.'
##        #return 
##

class DETerrain(CoClass):
    u'Esri Terrain data element object.'
    _reg_clsid_ = GUID('{546543B6-327A-4D3C-AC15-8122C8B6680A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
class IDETerrain(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of Terrain Data Element.'
    _iid_ = GUID('{0911F2FB-4B12-4012-AE6B-94FAD2D2084D}')
    _idlflags_ = ['oleautomation']
class IDETerrainWindowSize(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of Terrain Data Element.'
    _iid_ = GUID('{62B845F1-6B66-406D-870D-2AFD3C00DC48}')
    _idlflags_ = ['oleautomation']
DETerrain._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDETerrain, IDETerrainWindowSize, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEDataset, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElement, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPValue, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDescribe, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone]

class ILasDataset(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of LasDataset.'
    _iid_ = GUID('{3AC637A3-1671-4DFE-BABE-D7947D57F050}')
    _idlflags_ = ['oleautomation']
class ILasSurface(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of LasSurface.'
    _iid_ = GUID('{81792712-2296-4B3F-BA19-3D37BD0B245D}')
    _idlflags_ = ['oleautomation']
ILasDataset._methods_ = [
    COMMETHOD([helpstring(u'Empty the object.')], HRESULT, 'SetEmpty'),
    COMMETHOD([helpstring(u'Opens the specified dataset.')], HRESULT, 'Init',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD([helpstring(u'Saves the dataset to disk using the specified name.')], HRESULT, 'SaveAs',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], VARIANT_BOOL, 'bOverWrite' )),
    COMMETHOD(['propget', helpstring(u'The name of the dataset.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pName' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the dataset is saved with relative path.')], HRESULT, 'UsesRelativePath',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbUsesRelativePath' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the dataset has been changed since last save.')], HRESULT, 'IsDirty',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbIsDirty' )),
    COMMETHOD(['propget', helpstring(u'The spatial reference of the dataset.')], HRESULT, 'SpatialReference',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference)), 'ppSpatialRef' )),
    COMMETHOD(['propget', helpstring(u'The xyz extent of the dataset.')], HRESULT, 'Extent',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'ppExtent' )),
    COMMETHOD(['propget', helpstring(u'The number of LAS files contained in the dataset.')], HRESULT, 'FileCount',
              ( ['retval', 'out'], POINTER(c_int), 'pcFiles' )),
    COMMETHOD(['propget', helpstring(u'Returns the LAS file specified by the index.')], HRESULT, 'File',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(ILasFile)), 'ppFile' )),
    COMMETHOD(['propget', helpstring(u'The number of surface constraints contained in the dataset.')], HRESULT, 'SurfaceConstraintCount',
              ( ['retval', 'out'], POINTER(c_int), 'pcConstraints' )),
    COMMETHOD([helpstring(u'Gets surface constraint specified by the index.')], HRESULT, 'GetSurfaceConstraint',
              ( ['in'], c_int, 'index' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass)), 'ppClass' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IField)), 'ppHeightField' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IField)), 'ppTagField' ),
              ( ['out'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriTinSurfaceType), 'pType' )),
    COMMETHOD([helpstring(u'Gets surface constraint specified by the index.')], HRESULT, 'GetSurfaceConstraintName',
              ( ['in'], c_int, 'index' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClassName)), 'ppName' ),
              ( ['out'], POINTER(BSTR), 'pHeightField' ),
              ( ['out'], POINTER(BSTR), 'pTagField' ),
              ( ['out'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriTinSurfaceType), 'pType' )),
    COMMETHOD([helpstring(u'Gets surface constraint specified by the index.')], HRESULT, 'GetSurfaceConstraintID',
              ( ['in'], c_int, 'index' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID)), 'ppGuid' )),
    COMMETHOD([helpstring(u"Gets surface constraint's index identified by the ID.")], HRESULT, 'GetSurfaceConstraintIndexFromID',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID), 'pGuid' ),
              ( ['out'], POINTER(c_int), 'pIndex' )),
    COMMETHOD(['propget', helpstring(u'The number of points in the dataset.')], HRESULT, 'PointCount',
              ( ['retval', 'out'], POINTER(c_double), 'pCount' )),
    COMMETHOD(['propget', helpstring(u'The size of all the LAS files in bytes.')], HRESULT, 'SizeInBytes',
              ( ['retval', 'out'], POINTER(c_double), 'pcBytes' )),
    COMMETHOD(['propget', helpstring(u'Indicates if statistics is available.')], HRESULT, 'HasStatistics',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbHasStats' )),
    COMMETHOD(['propget', helpstring(u'Indicates if update is necessary.')], HRESULT, 'NeedsUpdateStatistics',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbNeedsUpdate' )),
    COMMETHOD([helpstring(u'Get statistics.')], HRESULT, 'GetStatistics',
              ( ['retval', 'out'], POINTER(POINTER(ILasStatistics)), 'ppStatistics' )),
    COMMETHOD([helpstring(u'Returns an implicit surface.')], HRESULT, 'CreateDynamicSurface',
              ( ['retval', 'out'], POINTER(POINTER(ILasSurface)), 'ppSurface' )),
    COMMETHOD([helpstring(u'Writes a new, optionally modified, version of the specified LAS file.')], HRESULT, 'Export',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( ['in'], c_int, 'FileIndex' ),
              ( ['in'], POINTER(ILasPointFilter), 'pFilter' ),
              ( ['in'], BSTR, 'newFileName' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference), 'pNewSpatialReference' ),
              ( ['in'], VARIANT_BOOL, 'bProject' ),
              ( ['in'], VARIANT_BOOL, 'bDropVLRs' )),
]
################################################################
## code template for ILasDataset implementation
##class ILasDataset_Impl(object):
##    @property
##    def SizeInBytes(self):
##        u'The size of all the LAS files in bytes.'
##        #return pcBytes
##
##    @property
##    def SpatialReference(self):
##        u'The spatial reference of the dataset.'
##        #return ppSpatialRef
##
##    def GetSurfaceConstraint(self, index):
##        u'Gets surface constraint specified by the index.'
##        #return ppClass, ppHeightField, ppTagField, pType
##
##    def Init(self, Name):
##        u'Opens the specified dataset.'
##        #return 
##
##    @property
##    def FileCount(self):
##        u'The number of LAS files contained in the dataset.'
##        #return pcFiles
##
##    @property
##    def UsesRelativePath(self):
##        u'Indicates if the dataset is saved with relative path.'
##        #return pbUsesRelativePath
##
##    def GetSurfaceConstraintIndexFromID(self, pGuid):
##        u"Gets surface constraint's index identified by the ID."
##        #return pIndex
##
##    def SetEmpty(self):
##        u'Empty the object.'
##        #return 
##
##    @property
##    def Extent(self):
##        u'The xyz extent of the dataset.'
##        #return ppExtent
##
##    def CreateDynamicSurface(self):
##        u'Returns an implicit surface.'
##        #return ppSurface
##
##    @property
##    def Name(self):
##        u'The name of the dataset.'
##        #return pName
##
##    @property
##    def SurfaceConstraintCount(self):
##        u'The number of surface constraints contained in the dataset.'
##        #return pcConstraints
##
##    def GetSurfaceConstraintID(self, index):
##        u'Gets surface constraint specified by the index.'
##        #return ppGuid
##
##    def SaveAs(self, Name, bOverWrite):
##        u'Saves the dataset to disk using the specified name.'
##        #return 
##
##    def GetStatistics(self):
##        u'Get statistics.'
##        #return ppStatistics
##
##    @property
##    def HasStatistics(self):
##        u'Indicates if statistics is available.'
##        #return pbHasStats
##
##    @property
##    def PointCount(self):
##        u'The number of points in the dataset.'
##        #return pCount
##
##    @property
##    def IsDirty(self):
##        u'Indicates if the dataset has been changed since last save.'
##        #return pbIsDirty
##
##    def Export(self, pTrackCancel, FileIndex, pFilter, newFileName, pNewSpatialReference, bProject, bDropVLRs):
##        u'Writes a new, optionally modified, version of the specified LAS file.'
##        #return 
##
##    def GetSurfaceConstraintName(self, index):
##        u'Gets surface constraint specified by the index.'
##        #return ppName, pHeightField, pTagField, pType
##
##    @property
##    def File(self, index):
##        u'Returns the LAS file specified by the index.'
##        #return ppFile
##
##    @property
##    def NeedsUpdateStatistics(self):
##        u'Indicates if update is necessary.'
##        #return pbNeedsUpdate
##

class LineResequencer(CoClass):
    u'Class for sorting lines to form parcel boundaries.'
    _reg_clsid_ = GUID('{DAE9512C-77A7-4857-8624-225FC5294F46}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
class ILineResequencer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that sort a set of lines so that they form the boundary of a parcel. Multipart/islands are supported.'
    _iid_ = GUID('{5D89097E-23DE-41AA-AD16-284F362BEF9A}')
    _idlflags_ = ['oleautomation']
LineResequencer._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ILineResequencer]

class ICadastralTableFieldEdits(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the field edits of the cadastral fabric table.'
    _iid_ = GUID('{3327D58A-2994-4FD9-A2FB-1F3A993F27AE}')
    _idlflags_ = ['oleautomation']
ICadastralTableFieldEdits._methods_ = [
    COMMETHOD(['propget', helpstring(u'The name of the cadastral table.')], HRESULT, 'TableName',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propput', helpstring(u'The enumeration for the table whose fields are being edited.')], HRESULT, 'CadastralTable',
              ( ['in'], esriCadastralFabricTable, 'Table' )),
    COMMETHOD(['propget', helpstring(u'The enumeration for the table whose fields are being edited.')], HRESULT, 'CadastralTable',
              ( ['retval', 'out'], POINTER(esriCadastralFabricTable), 'Table' )),
    COMMETHOD(['propget', helpstring(u'The extended attribute fields for the cadastral fabric table.')], HRESULT, 'ExtendedAttributeFields',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFields)), 'Fields' )),
    COMMETHOD(['propput', helpstring(u'The extended attribute fields for the cadastral fabric table.')], HRESULT, 'ExtendedAttributeFields',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFields), 'Fields' )),
]
################################################################
## code template for ICadastralTableFieldEdits implementation
##class ICadastralTableFieldEdits_Impl(object):
##    def _get(self):
##        u'The enumeration for the table whose fields are being edited.'
##        #return Table
##    def _set(self, Table):
##        u'The enumeration for the table whose fields are being edited.'
##    CadastralTable = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def TableName(self):
##        u'The name of the cadastral table.'
##        #return Name
##
##    def _get(self):
##        u'The extended attribute fields for the cadastral fabric table.'
##        #return Fields
##    def _set(self, Fields):
##        u'The extended attribute fields for the cadastral fabric table.'
##    ExtendedAttributeFields = property(_get, _set, doc = _set.__doc__)
##

class TerrainLasDataImporter(CoClass):
    u'Esri Terrain LAS Data Importer object.'
    _reg_clsid_ = GUID('{E0879549-CA26-41AB-A9C6-463EC3B1B1CA}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
class ITerrainLasDataImporter(ITerrainDataImporter):
    _case_insensitive_ = True
    u'Provides access to members that handle importing terrain source data in LAS format.'
    _iid_ = GUID('{80E83E8C-2EC1-4090-B399-411FA593B25B}')
    _idlflags_ = ['oleautomation']
TerrainLasDataImporter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ITerrainDataImporter, ITerrainLasDataImporter, ITerrainLasDataInfo, ITerrainLasDataInfo2]


# values for enumeration 'enumShapeSource'
shapefromObject = 0
shapefromObservation = 1
enumShapeSource = c_int # enum
class CadastralTransformationData(CoClass):
    u'CadastralTransformationData CoClass holding the information passed to the CadastralTransformation object.'
    _reg_clsid_ = GUID('{F0E92E5D-39FB-4EAD-8192-1A027FAB68C1}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
class ICadastralTransformationData(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manage the data used by the cadastral transformation.'
    _iid_ = GUID('{E1F5787F-B5E4-4E6C-B84F-86D621792BB8}')
    _idlflags_ = ['oleautomation']
CadastralTransformationData._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ICadastralTransformationData]

class ILasDatasetWorkspace(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of LasDataset workspace.'
    _iid_ = GUID('{EB2E798D-8154-41E9-A70F-53128DE11573}')
    _idlflags_ = ['oleautomation']
ILasDatasetWorkspace._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if the given BSTR name is a LasDataset.')], HRESULT, 'IsLasDataset',
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbIsDataset' )),
    COMMETHOD([helpstring(u'Opens an existing LasDataset.')], HRESULT, 'OpenLasDataset',
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(POINTER(ILasDataset)), 'ppLasDataset' )),
]
################################################################
## code template for ILasDatasetWorkspace implementation
##class ILasDatasetWorkspace_Impl(object):
##    @property
##    def IsLasDataset(self, Name):
##        u'Indicates if the given BSTR name is a LasDataset.'
##        #return pbIsDataset
##
##    def OpenLasDataset(self, Name):
##        u'Opens an existing LasDataset.'
##        #return ppLasDataset
##


# values for enumeration 'esriCadastralDensifiedType'
esriCadastralDensifiedNormal = 0
esriCadastralDensifiedGCS = 1
esriCadastralDensifiedCurve = 2
esriCadastralDensifiedLineString = 3
esriCadastralDensifiedType = c_int # enum
class ITemporalQueryFilter2(ITemporalQueryFilter):
    _case_insensitive_ = True
    u'Provides access to properties and methods needed to manage temporal query filters.'
    _iid_ = GUID('{6D3465E9-F6F4-43D6-BBA9-87EEE56C146E}')
    _idlflags_ = ['oleautomation']
ITemporalQueryFilter2._methods_ = [
    COMMETHOD(['propget', helpstring(u'Defines data time reference.')], HRESULT, 'TimeReference',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITimeReference)), 'TimeReference' )),
    COMMETHOD(['propputref', helpstring(u'Defines data time reference.')], HRESULT, 'TimeReference',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITimeReference), 'TimeReference' )),
]
################################################################
## code template for ITemporalQueryFilter2 implementation
##class ITemporalQueryFilter2_Impl(object):
##    def TimeReference(self, TimeReference):
##        u'Defines data time reference.'
##        #return 
##

class ITerrainBlobReader(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that provide information about an attribute blob.'
    _iid_ = GUID('{58CE4421-8073-464B-BF90-2EF70384C82E}')
    _idlflags_ = ['oleautomation']
ITerrainBlobReader._methods_ = [
    COMMETHOD([helpstring(u'Uninitialize the object.')], HRESULT, 'SetEmpty'),
    COMMETHOD([helpstring(u'Indicates if Terrain can recognize the blob.')], HRESULT, 'IsKnownBlob',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IMemoryBlobStream), 'pBlob' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbIsKnown' )),
    COMMETHOD([helpstring(u'Assigns a blob to the reader.')], HRESULT, 'SetBlob',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IMemoryBlobStream), 'pBlob' )),
    COMMETHOD([helpstring(u'Returns the data type of the blob.')], HRESULT, 'GetDataType',
              ( ['retval', 'out'], POINTER(esriTerrainBlobDataType), 'pType' )),
    COMMETHOD([helpstring(u'Returns the number of attribute values contained in the blob.')], HRESULT, 'GetItemCount',
              ( ['retval', 'out'], POINTER(c_int), 'pcItems' )),
    COMMETHOD([helpstring(u'Returns the value of the attribute specified by the index.')], HRESULT, 'GetValue',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'pValue' )),
]
################################################################
## code template for ITerrainBlobReader implementation
##class ITerrainBlobReader_Impl(object):
##    def GetValue(self, index):
##        u'Returns the value of the attribute specified by the index.'
##        #return pValue
##
##    def IsKnownBlob(self, pBlob):
##        u'Indicates if Terrain can recognize the blob.'
##        #return pbIsKnown
##
##    def SetBlob(self, pBlob):
##        u'Assigns a blob to the reader.'
##        #return 
##
##    def GetItemCount(self):
##        u'Returns the number of attribute values contained in the blob.'
##        #return pcItems
##
##    def SetEmpty(self):
##        u'Uninitialize the object.'
##        #return 
##
##    def GetDataType(self):
##        u'Returns the data type of the blob.'
##        #return pType
##

class TerrainDataSource(CoClass):
    u'Esri Terrain Data Source object.'
    _reg_clsid_ = GUID('{2FBEA8FD-19F5-4CC6-8D99-FB921FCAE57D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
TerrainDataSource._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ITerrainDataSource, ITerrainEmbeddedDataSource, ITerrainEmbeddedDataSource2]

class IConstructionBreakPoints(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manipulate the break lines for a parcel construction.'
    _iid_ = GUID('{1C66CB4E-8950-41B1-8896-E75C173870AA}')
    _idlflags_ = ['oleautomation']
IConstructionBreakPoints._methods_ = [
    COMMETHOD(['propget', helpstring(u'The number of break points for the parcel construction data.')], HRESULT, 'BreakPointCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD([helpstring(u'The break point at the given index.')], HRESULT, 'GetBreakPoint',
              ( ['in'], c_int, 'i' ),
              ( ['in', 'out'], POINTER(c_int), 'pointNo' ),
              ( ['in', 'out'], POINTER(c_int), 'fromPointNo' ),
              ( ['in', 'out'], POINTER(c_int), 'toPointNo' ),
              ( ['in', 'out'], POINTER(c_double), 'ratio' )),
    COMMETHOD([helpstring(u'The break point with the matching pointNo.')], HRESULT, 'FindBreakPoint',
              ( ['in'], c_int, 'pointNo' ),
              ( ['in', 'out'], POINTER(c_int), 'fromPointNo' ),
              ( ['in', 'out'], POINTER(c_int), 'toPointNo' ),
              ( ['in', 'out'], POINTER(c_double), 'ratio' )),
    COMMETHOD([helpstring(u'Adds a break point to the parcel construction data.')], HRESULT, 'AddBreakPoint',
              ( ['in'], c_int, 'pointNo' ),
              ( ['in'], c_int, 'fromPointNo' ),
              ( ['in'], c_int, 'toPointNo' ),
              ( ['in'], c_double, 'ratio' )),
    COMMETHOD([helpstring(u'Remove break point from parcel construction data.')], HRESULT, 'RemoveBreakPoint',
              ( ['in'], c_int, 'pointNo' )),
    COMMETHOD([helpstring(u'Clears all break points.')], HRESULT, 'ClearBreakPoints'),
]
################################################################
## code template for IConstructionBreakPoints implementation
##class IConstructionBreakPoints_Impl(object):
##    @property
##    def BreakPointCount(self):
##        u'The number of break points for the parcel construction data.'
##        #return Count
##
##    def AddBreakPoint(self, pointNo, fromPointNo, toPointNo, ratio):
##        u'Adds a break point to the parcel construction data.'
##        #return 
##
##    def ClearBreakPoints(self):
##        u'Clears all break points.'
##        #return 
##
##    def GetBreakPoint(self, i):
##        u'The break point at the given index.'
##        #return pointNo, fromPointNo, toPointNo, ratio
##
##    def FindBreakPoint(self, pointNo):
##        u'The break point with the matching pointNo.'
##        #return fromPointNo, toPointNo, ratio
##
##    def RemoveBreakPoint(self, pointNo):
##        u'Remove break point from parcel construction data.'
##        #return 
##

IDETerrain._methods_ = [
    COMMETHOD(['propput', helpstring(u'The name of the terrain.')], HRESULT, 'Name',
              ( ['in'], BSTR, 'pName' )),
    COMMETHOD(['propget', helpstring(u'The name of the terrain.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pName' )),
    COMMETHOD(['propput', helpstring(u'The horizontal distance used to spatially index and partition terrain data.')], HRESULT, 'TileSize',
              ( ['in'], c_double, 'pSize' )),
    COMMETHOD(['propget', helpstring(u'The horizontal distance used to spatially index and partition terrain data.')], HRESULT, 'TileSize',
              ( ['retval', 'out'], POINTER(c_double), 'pSize' )),
    COMMETHOD(['propput', helpstring(u'The kind of the pyramid as defined by the type of filter it uses to thin points.')], HRESULT, 'PyramidType',
              ( ['in'], esriTerrainPyramidType, 'pType' )),
    COMMETHOD(['propget', helpstring(u'The kind of the pyramid as defined by the type of filter it uses to thin points.')], HRESULT, 'PyramidType',
              ( ['retval', 'out'], POINTER(esriTerrainPyramidType), 'pType' )),
    COMMETHOD(['propput', helpstring(u'The maximum number of points in the most generalized representation of the Terrain.')], HRESULT, 'MaxOverviewTerrainPoints',
              ( ['in'], c_int, 'pcPoints' )),
    COMMETHOD(['propget', helpstring(u'The maximum number of points in the most generalized representation of the Terrain.')], HRESULT, 'MaxOverviewTerrainPoints',
              ( ['retval', 'out'], POINTER(c_int), 'pcPoints' )),
    COMMETHOD(['propput', helpstring(u'The maximum number of vertices per multipoint stored in the terrain pyramid.')], HRESULT, 'MaxPointsPerShape',
              ( ['in'], c_int, 'pcPoints' )),
    COMMETHOD(['propget', helpstring(u'The maximum number of vertices per multipoint stored in the terrain pyramid.')], HRESULT, 'MaxPointsPerShape',
              ( ['retval', 'out'], POINTER(c_int), 'pcPoints' )),
    COMMETHOD(['propput', helpstring(u'The storage parameter used with SDE databases.')], HRESULT, 'ConfigurationKeyword',
              ( ['in'], BSTR, 'pConfigKeyword' )),
    COMMETHOD(['propget', helpstring(u'The storage parameter used with SDE databases.')], HRESULT, 'ConfigurationKeyword',
              ( ['retval', 'out'], POINTER(BSTR), 'pConfigKeyword' )),
]
################################################################
## code template for IDETerrain implementation
##class IDETerrain_Impl(object):
##    def _get(self):
##        u'The name of the terrain.'
##        #return pName
##    def _set(self, pName):
##        u'The name of the terrain.'
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The kind of the pyramid as defined by the type of filter it uses to thin points.'
##        #return pType
##    def _set(self, pType):
##        u'The kind of the pyramid as defined by the type of filter it uses to thin points.'
##    PyramidType = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The horizontal distance used to spatially index and partition terrain data.'
##        #return pSize
##    def _set(self, pSize):
##        u'The horizontal distance used to spatially index and partition terrain data.'
##    TileSize = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The maximum number of vertices per multipoint stored in the terrain pyramid.'
##        #return pcPoints
##    def _set(self, pcPoints):
##        u'The maximum number of vertices per multipoint stored in the terrain pyramid.'
##    MaxPointsPerShape = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The maximum number of points in the most generalized representation of the Terrain.'
##        #return pcPoints
##    def _set(self, pcPoints):
##        u'The maximum number of points in the most generalized representation of the Terrain.'
##    MaxOverviewTerrainPoints = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The storage parameter used with SDE databases.'
##        #return pConfigKeyword
##    def _set(self, pConfigKeyword):
##        u'The storage parameter used with SDE databases.'
##    ConfigurationKeyword = property(_get, _set, doc = _set.__doc__)
##

class TerrainAsciiDataImporter(CoClass):
    u'Esri Terrain ASCII Data Importer object.'
    _reg_clsid_ = GUID('{EEB6B206-C144-496C-88D2-B6E2DA4D37E7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
TerrainAsciiDataImporter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ITerrainDataImporter, ITerrainAsciiDataImporter, ITerrainAsciiDataImporter2]

class IDECadastralFabric2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that describe cadastral fabric data elements.'
    _iid_ = GUID('{5BA64979-96C6-4E16-BAA1-AFF9E81CCBD3}')
    _idlflags_ = ['oleautomation']
IDECadastralFabric2._methods_ = [
    COMMETHOD(['propget', helpstring(u'The default accuracy category for compiled parcels.')], HRESULT, 'CompiledAccuracyCategory',
              ( ['retval', 'out'], POINTER(c_int), 'defaultAccuracy' )),
    COMMETHOD(['propput', helpstring(u'The default accuracy category for compiled parcels.')], HRESULT, 'CompiledAccuracyCategory',
              ( ['in'], c_int, 'defaultAccuracy' )),
    COMMETHOD(['propget', helpstring(u'The distance used to generate a buffer around the job parcels. This buffer defines the adjustment area.')], HRESULT, 'BufferDistanceForAdjustment',
              ( ['retval', 'out'], POINTER(c_double), 'distance' )),
    COMMETHOD(['propput', helpstring(u'The distance used to generate a buffer around the job parcels. This buffer defines the adjustment area.')], HRESULT, 'BufferDistanceForAdjustment',
              ( ['in'], c_double, 'distance' )),
    COMMETHOD(['propget', helpstring(u'The cadastral fabric type.')], HRESULT, 'Type',
              ( ['retval', 'out'], POINTER(esriCadastralFabricType), 'Type' )),
    COMMETHOD(['propput', helpstring(u'The cadastral fabric type.')], HRESULT, 'Type',
              ( ['in'], esriCadastralFabricType, 'Type' )),
    COMMETHOD(['propget', helpstring(u'The name of the surrogate version if applicable. Indicates if the cadastral fabric is a surrogate version.')], HRESULT, 'SurrogateVersion',
              ( ['retval', 'out'], POINTER(BSTR), 'surrogate' )),
    COMMETHOD(['propput', helpstring(u'The name of the surrogate version if applicable. Indicates if the cadastral fabric is a surrogate version.')], HRESULT, 'SurrogateVersion',
              ( ['in'], BSTR, 'surrogate' )),
    COMMETHOD(['propget', helpstring(u'The cadastral fabric version.')], HRESULT, 'Version',
              ( ['retval', 'out'], POINTER(c_int), 'Version' )),
    COMMETHOD(['propget', helpstring(u'Coordinate changes will be written if the shift is greater than this tolerance value.')], HRESULT, 'MaximumShiftThreshold',
              ( ['retval', 'out'], POINTER(c_double), 'Threshold' )),
    COMMETHOD(['propput', helpstring(u'Coordinate changes will be written if the shift is greater than this tolerance value.')], HRESULT, 'MaximumShiftThreshold',
              ( ['in'], c_double, 'Threshold' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether Cadastral Fabrics greater than one level below default can be edited.')], HRESULT, 'MultiGenerationEditing',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pAllow' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether Cadastral Fabrics greater than one level below default can be edited.')], HRESULT, 'MultiGenerationEditing',
              ( ['in'], VARIANT_BOOL, 'pAllow' )),
    COMMETHOD(['propget', helpstring(u'Indicates if reconciling and posting with an ancestor more than one generation above the working version is allowed.')], HRESULT, 'MultiLevelReconcile',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pAllow' )),
    COMMETHOD(['propput', helpstring(u'Indicates if reconciling and posting with an ancestor more than one generation above the working version is allowed.')], HRESULT, 'MultiLevelReconcile',
              ( ['in'], VARIANT_BOOL, 'pAllow' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether points on the adjustment area boundary should be pinned.')], HRESULT, 'PinAdjustmentBoundary',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pPinBoundary' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether points on the adjustment area boundary should be pinned.')], HRESULT, 'PinAdjustmentBoundary',
              ( ['in'], VARIANT_BOOL, 'pPinBoundary' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether non-adjusted points within the adjustment are should be pinned.')], HRESULT, 'PinAdjustmentPointsWithinBoundary',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pPinWithinBoundary' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether non-adjusted points within the adjustment are should be pinned.')], HRESULT, 'PinAdjustmentPointsWithinBoundary',
              ( ['in'], VARIANT_BOOL, 'pPinWithinBoundary' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether adjustment vectors should be written.')], HRESULT, 'WriteAdjustmentVectors',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pWriteAdjustmentVectors' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether adjustment vectors should be written.')], HRESULT, 'WriteAdjustmentVectors',
              ( ['in'], VARIANT_BOOL, 'pWriteAdjustmentVectors' )),
]
################################################################
## code template for IDECadastralFabric2 implementation
##class IDECadastralFabric2_Impl(object):
##    def _get(self):
##        u'Indicates whether non-adjusted points within the adjustment are should be pinned.'
##        #return pPinWithinBoundary
##    def _set(self, pPinWithinBoundary):
##        u'Indicates whether non-adjusted points within the adjustment are should be pinned.'
##    PinAdjustmentPointsWithinBoundary = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if reconciling and posting with an ancestor more than one generation above the working version is allowed.'
##        #return pAllow
##    def _set(self, pAllow):
##        u'Indicates if reconciling and posting with an ancestor more than one generation above the working version is allowed.'
##    MultiLevelReconcile = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The default accuracy category for compiled parcels.'
##        #return defaultAccuracy
##    def _set(self, defaultAccuracy):
##        u'The default accuracy category for compiled parcels.'
##    CompiledAccuracyCategory = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether Cadastral Fabrics greater than one level below default can be edited.'
##        #return pAllow
##    def _set(self, pAllow):
##        u'Indicates whether Cadastral Fabrics greater than one level below default can be edited.'
##    MultiGenerationEditing = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The distance used to generate a buffer around the job parcels. This buffer defines the adjustment area.'
##        #return distance
##    def _set(self, distance):
##        u'The distance used to generate a buffer around the job parcels. This buffer defines the adjustment area.'
##    BufferDistanceForAdjustment = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The name of the surrogate version if applicable. Indicates if the cadastral fabric is a surrogate version.'
##        #return surrogate
##    def _set(self, surrogate):
##        u'The name of the surrogate version if applicable. Indicates if the cadastral fabric is a surrogate version.'
##    SurrogateVersion = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Version(self):
##        u'The cadastral fabric version.'
##        #return Version
##
##    def _get(self):
##        u'Coordinate changes will be written if the shift is greater than this tolerance value.'
##        #return Threshold
##    def _set(self, Threshold):
##        u'Coordinate changes will be written if the shift is greater than this tolerance value.'
##    MaximumShiftThreshold = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether adjustment vectors should be written.'
##        #return pWriteAdjustmentVectors
##    def _set(self, pWriteAdjustmentVectors):
##        u'Indicates whether adjustment vectors should be written.'
##    WriteAdjustmentVectors = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether points on the adjustment area boundary should be pinned.'
##        #return pPinBoundary
##    def _set(self, pPinBoundary):
##        u'Indicates whether points on the adjustment area boundary should be pinned.'
##    PinAdjustmentBoundary = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The cadastral fabric type.'
##        #return Type
##    def _set(self, Type):
##        u'The cadastral fabric type.'
##    Type = property(_get, _set, doc = _set.__doc__)
##

ILasFilter._methods_ = [
    COMMETHOD(['propput', helpstring(u'The surface constraints to be applied.')], HRESULT, 'SurfaceConstraints',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IArray), 'ppConstraintIDs' )),
    COMMETHOD(['propget', helpstring(u'The surface constraints to be applied.')], HRESULT, 'SurfaceConstraints',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IArray)), 'ppConstraintIDs' )),
    COMMETHOD([helpstring(u'Make a clone.')], HRESULT, 'Clone',
              ( ['retval', 'out'], POINTER(POINTER(ILasFilter)), 'ppClone' )),
]
################################################################
## code template for ILasFilter implementation
##class ILasFilter_Impl(object):
##    def _get(self):
##        u'The surface constraints to be applied.'
##        #return ppConstraintIDs
##    def _set(self, ppConstraintIDs):
##        u'The surface constraints to be applied.'
##    SurfaceConstraints = property(_get, _set, doc = _set.__doc__)
##
##    def Clone(self):
##        u'Make a clone.'
##        #return ppClone
##

class CadastralWorkspaceDatasetExtension(CoClass):
    u"A container for describing this cadastral fabric's workspace extension properties."
    _reg_clsid_ = GUID('{BE58E469-F14D-49C6-8080-0B027271EF91}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
CadastralWorkspaceDatasetExtension._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceExtension3, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceExtensionControl, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetContainer3]
CadastralWorkspaceDatasetExtension._outgoing_interfaces_ = [comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceEvents, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IVersionEvents, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IVersionEvents2]

class LasSurface(CoClass):
    u'Esri LasSurface object.'
    _reg_clsid_ = GUID('{A83FB64E-0B76-43E0-B8AE-6C96A9913147}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
LasSurface._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ILasSurface]

class ICadastralUnitTools(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods that format data.'
    _iid_ = GUID('{0DC83354-E621-4C2D-9C2D-BAD65C0727D1}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriCadastralAreaUnits'
esriCAUImperial = 0
esriCAUMetric = 1
esriCAUSquareMeter = 2
esriCAUHectare = 3
esriCAUAcre = 4
esriCAUSquareRods = 5
esriCAURoods = 6
esriCAUPerches = 7
esriCAUSquareFoot = 8
esriCAUSquareUSFoot = 9
esriCAUQuarterSections = 10
esriCAUSections = 11
esriCadastralAreaUnits = c_int # enum
ICadastralUnitTools._methods_ = [
    COMMETHOD(['propget', helpstring(u'Converts a metric area value into a formated area string. isUSFoot applies to imperial output. If decimalPlaces = -1, the decimal places is automatically calculated from areaSQMeters.')], HRESULT, 'FormattedArea',
              ( ['in'], c_double, 'areaSQMeters' ),
              ( ['in'], esriCadastralAreaUnits, 'eOutputAreaTypeDisplay' ),
              ( ['in'], VARIANT_BOOL, 'isUSFoot' ),
              ( ['in'], c_int, 'decimalPlaces' ),
              ( ['retval', 'out'], POINTER(BSTR), 'formatedArea' )),
    COMMETHOD(['propget', helpstring(u'Converts a metric area value into a given area unit.')], HRESULT, 'ConvertArea',
              ( ['in'], c_double, 'areaSQMeters' ),
              ( ['in'], esriCadastralAreaUnits, 'eOutputAreaType' ),
              ( ['retval', 'out'], POINTER(c_double), 'pArea' )),
    COMMETHOD(['propget', helpstring(u'Direction type enum value as a string.')], HRESULT, 'DirectionType',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.esriDirectionType, 'eDirType' ),
              ( ['retval', 'out'], POINTER(BSTR), 'dirType' )),
    COMMETHOD(['propget', helpstring(u'Direction units enum value as a string.')], HRESULT, 'DirectionUnit',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.esriDirectionUnits, 'eDirUnit' ),
              ( ['retval', 'out'], POINTER(BSTR), 'dirUnit' )),
    COMMETHOD(['propget', helpstring(u'Distance units enum value as a string.')], HRESULT, 'DistanceUnit',
              ( ['in'], esriCadastralDistanceUnits, 'eDistanceType' ),
              ( ['in'], VARIANT_BOOL, 'shortNotation' ),
              ( ['retval', 'out'], POINTER(BSTR), 'distUnit' )),
    COMMETHOD(['propget', helpstring(u'Area type enum value as a string.')], HRESULT, 'AreaUnit',
              ( ['in'], esriCadastralAreaUnits, 'eAreaType' ),
              ( ['in'], VARIANT_BOOL, 'shortNotation' ),
              ( ['retval', 'out'], POINTER(BSTR), 'area' )),
]
################################################################
## code template for ICadastralUnitTools implementation
##class ICadastralUnitTools_Impl(object):
##    @property
##    def FormattedArea(self, areaSQMeters, eOutputAreaTypeDisplay, isUSFoot, decimalPlaces):
##        u'Converts a metric area value into a formated area string. isUSFoot applies to imperial output. If decimalPlaces = -1, the decimal places is automatically calculated from areaSQMeters.'
##        #return formatedArea
##
##    @property
##    def DirectionUnit(self, eDirUnit):
##        u'Direction units enum value as a string.'
##        #return dirUnit
##
##    @property
##    def AreaUnit(self, eAreaType, shortNotation):
##        u'Area type enum value as a string.'
##        #return area
##
##    @property
##    def ConvertArea(self, areaSQMeters, eOutputAreaType):
##        u'Converts a metric area value into a given area unit.'
##        #return pArea
##
##    @property
##    def DirectionType(self, eDirType):
##        u'Direction type enum value as a string.'
##        #return dirType
##
##    @property
##    def DistanceUnit(self, eDistanceType, shortNotation):
##        u'Distance units enum value as a string.'
##        #return distUnit
##

class LasToRasterFunctionArguments(CoClass):
    u'The LasToRasterFunction arguments.'
    _reg_clsid_ = GUID('{FB8E343B-8014-4CE9-B457-E72389D2B339}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
LasToRasterFunctionArguments._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._8F0541A3_D5BE_4B3F_A8D9_062D5579E19B_0_10_2.IRasterFunctionArguments, comtypes.gen._8F0541A3_D5BE_4B3F_A8D9_062D5579E19B_0_10_2.IRasterCacheArguments, comtypes.gen._8F0541A3_D5BE_4B3F_A8D9_062D5579E19B_0_10_2.ILasToRasterFunctionArguments, comtypes.gen._8F0541A3_D5BE_4B3F_A8D9_062D5579E19B_0_10_2.ILasToRasterFunctionArguments2, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLVersionSupport, comtypes.gen._8F0541A3_D5BE_4B3F_A8D9_062D5579E19B_0_10_2.IItemPaths, comtypes.gen._8F0541A3_D5BE_4B3F_A8D9_062D5579E19B_0_10_2.IItemPaths2]

ITerrainLasDataImporter._methods_ = [
    COMMETHOD([helpstring(u'Used to indicate which, if any, LiDAR properties to retain and load into the target feature class in a BLOB field.')], HRESULT, 'AddProperty',
              ( ['in'], esriTerrainLasDataPropertyType, 'property' ),
              ( ['in'], BSTR, 'FieldName' )),
    COMMETHOD([helpstring(u'Used to indicate which points to extract from the LAS files based on their LiDAR return number.')], HRESULT, 'AddReturnNumber',
              ( ['in'], esriTerrainLasReturnType, 'ReturnNumber' )),
    COMMETHOD([helpstring(u'Used to indicate which points to load based on one or more LAS classification codes.')], HRESULT, 'SetClassCodes',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray), 'pCodes' )),
]
################################################################
## code template for ITerrainLasDataImporter implementation
##class ITerrainLasDataImporter_Impl(object):
##    def AddReturnNumber(self, ReturnNumber):
##        u'Used to indicate which points to extract from the LAS files based on their LiDAR return number.'
##        #return 
##
##    def AddProperty(self, property, FieldName):
##        u'Used to indicate which, if any, LiDAR properties to retain and load into the target feature class in a BLOB field.'
##        #return 
##
##    def SetClassCodes(self, pCodes):
##        u'Used to indicate which points to load based on one or more LAS classification codes.'
##        #return 
##

class ILasDataset2(ILasDataset):
    _case_insensitive_ = True
    u'Provides access to members of LasDataset.'
    _iid_ = GUID('{3AF8A856-B6C2-41E4-8B51-8AC0E8777087}')
    _idlflags_ = ['oleautomation']
ILasDataset2._methods_ = [
    COMMETHOD([helpstring(u'Spatially rearrange points.')], HRESULT, 'Rearrange',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( ['in'], c_int, 'FileIndex' ),
              ( ['in'], BSTR, 'newFileName' ),
              ( ['in'], VARIANT_BOOL, 'bOverWrite' )),
]
################################################################
## code template for ILasDataset2 implementation
##class ILasDataset2_Impl(object):
##    def Rearrange(self, pTrackCancel, FileIndex, newFileName, bOverWrite):
##        u'Spatially rearrange points.'
##        #return 
##

class CadastralTableFieldEdits(CoClass):
    u'Esri Cadastral Table Field Edits Object.'
    _reg_clsid_ = GUID('{DEE35DFB-81A2-468E-ABA8-2414E757A0D9}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
CadastralTableFieldEdits._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ICadastralTableFieldEdits, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

class TerrainBlobWriter(CoClass):
    u'Esri Terrain blob writer.'
    _reg_clsid_ = GUID('{0EA06D19-AEEC-4110-A231-2705A08B9366}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
class ITerrainBlobWriter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that construct an attribute blob.'
    _iid_ = GUID('{6ED22878-8391-4EE1-999F-A9B6BE197BD9}')
    _idlflags_ = ['oleautomation']
TerrainBlobWriter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ITerrainBlobWriter]

class TerrainBlockCursor(CoClass):
    u'Esri TerrainBlockCursor object.'
    _reg_clsid_ = GUID('{AD220BB5-BD26-435E-9DBC-28FE5BAC9171}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
TerrainBlockCursor._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ITerrainBlockCursor]

IDECadastralFabric._methods_ = [
    COMMETHOD(['propget', helpstring(u'The database configuration keyword for the cadastral fabric.')], HRESULT, 'ConfigurationKeyword',
              ( ['retval', 'out'], POINTER(BSTR), 'configKeyword' )),
    COMMETHOD(['propput', helpstring(u'The database configuration keyword for the cadastral fabric.')], HRESULT, 'ConfigurationKeyword',
              ( ['in'], BSTR, 'configKeyword' )),
    COMMETHOD(['propget', helpstring(u'The default accuracy category for the cadastral fabric.')], HRESULT, 'DefaultAccuracyCategory',
              ( ['retval', 'out'], POINTER(c_int), 'defaultAccuracy' )),
    COMMETHOD(['propput', helpstring(u'The default accuracy category for the cadastral fabric.')], HRESULT, 'DefaultAccuracyCategory',
              ( ['in'], c_int, 'defaultAccuracy' )),
    COMMETHOD(['propputref', helpstring(u'Provides access to the field customizations for the cadastral fabric table.')], HRESULT, 'CadastralTableFieldEdits',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IArray), 'CadastralTableFieldEdits' )),
    COMMETHOD(['propget', helpstring(u'Provides access to the field customizations for the cadastral fabric table.')], HRESULT, 'CadastralTableFieldEdits',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IArray)), 'CadastralTableFieldEdits' )),
]
################################################################
## code template for IDECadastralFabric implementation
##class IDECadastralFabric_Impl(object):
##    @property
##    def CadastralTableFieldEdits(self, CadastralTableFieldEdits):
##        u'Provides access to the field customizations for the cadastral fabric table.'
##        #return 
##
##    def _get(self):
##        u'The default accuracy category for the cadastral fabric.'
##        #return defaultAccuracy
##    def _set(self, defaultAccuracy):
##        u'The default accuracy category for the cadastral fabric.'
##    DefaultAccuracyCategory = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The database configuration keyword for the cadastral fabric.'
##        #return configKeyword
##    def _set(self, configKeyword):
##        u'The database configuration keyword for the cadastral fabric.'
##    ConfigurationKeyword = property(_get, _set, doc = _set.__doc__)
##

class LasDatasetName(CoClass):
    u'The Esri LasDatasetName component.'
    _reg_clsid_ = GUID('{2029A994-9BC0-4094-A1C7-E5381869E4E3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
LasDatasetName._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetName, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo]

class CadastralDataTools(CoClass):
    u'Tools that assist in unit translation and storage.'
    _reg_clsid_ = GUID('{2FAF44E5-2951-4021-A6E9-209FE3125A12}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
CadastralDataTools._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ICadastralGroundToGridTools, ICadastralUnitTools]

class TerrainFieldStatistics(CoClass):
    u'Esri TerrainFieldStatistics object.'
    _reg_clsid_ = GUID('{CE7821B4-04AE-4518-842B-07D66FF6E605}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
TerrainFieldStatistics._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ITerrainFieldStatistics]

class ITrackingConnectionFolder(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Indicator interface used to identify an object as a trackingconnection folder.'
    _iid_ = GUID('{0AF38700-E779-11D6-B861-00010265ADC5}')
    _idlflags_ = ['oleautomation']
ITrackingConnectionFolder._methods_ = [
]
################################################################
## code template for ITrackingConnectionFolder implementation
##class ITrackingConnectionFolder_Impl(object):

class ITemporalFeature(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeature):
    _case_insensitive_ = True
    u'Provides access to properties specifying the temporal feature type.'
    _iid_ = GUID('{A677AB62-2FB8-11D5-B7E2-00010265ADC5}')
    _idlflags_ = ['oleautomation']
ITemporalFeature._methods_ = [
    COMMETHOD(['propget', helpstring(u'Specifies the type of feature used in a temporal workspace.')], HRESULT, 'TemporalFeatureType',
              ( ['retval', 'out'], POINTER(enumTemporalFeatureType), 'pVal' )),
]
################################################################
## code template for ITemporalFeature implementation
##class ITemporalFeature_Impl(object):
##    @property
##    def TemporalFeatureType(self):
##        u'Specifies the type of feature used in a temporal workspace.'
##        #return pVal
##

class ILasPointCloud(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to points.'
    _iid_ = GUID('{1928009D-9153-4EC0-A75C-4C24008D28D5}')
    _idlflags_ = ['oleautomation']
class IEnumLasPoint(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of LasPointEnumerator.'
    _iid_ = GUID('{41A9EA2B-B551-4987-A354-7FD3FE6DFC5E}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriLasPointStatsType'
esriLasPointStatsPointCount = 1
esriLasPointStatsPulseCount = 2
esriLasPointStatsRange = 4
esriLasPointStatsMostFrequent = 8
esriLasPointStatsType = c_int # enum
ILasPointCloud._methods_ = [
    COMMETHOD([helpstring(u'Estimate point count.')], HRESULT, 'EstimatePointCount',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'pAOI' ),
              ( ['retval', 'out'], POINTER(c_double), 'pcPoints' )),
    COMMETHOD([helpstring(u'Estimate point spacing.')], HRESULT, 'EstimatePointSpacing',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'pAOI' ),
              ( ['out'], POINTER(c_double), 'pMinSpacing' ),
              ( ['out'], POINTER(c_double), 'pMaxSpacing' ),
              ( ['out'], POINTER(c_double), 'pMeanSpacing' )),
    COMMETHOD([], HRESULT, 'GetLasPoints',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( ['in'], POINTER(ILasPointFilter), 'pFilter' ),
              ( ['in'], c_double, 'thinningFactor' ),
              ( ['in'], c_double, 'ZFactor' ),
              ( ['retval', 'out'], POINTER(POINTER(IEnumLasPoint)), 'ppPoints' )),
    COMMETHOD([], HRESULT, 'GetLasPointsByBudget',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( ['in'], POINTER(ILasPointFilter), 'pFilter' ),
              ( ['in'], c_double, 'maxPointCount' ),
              ( ['in'], c_double, 'ZFactor' ),
              ( ['retval', 'out'], POINTER(POINTER(IEnumLasPoint)), 'ppPoints' )),
    COMMETHOD([helpstring(u'Returns an array of ILasPointInfo(the 1-based pointID is optional).')], HRESULT, 'GetLasPointInfo',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'pLocation' ),
              ( ['in'], c_double, 'PointID' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IArray)), 'ppInfo' )),
    COMMETHOD([helpstring(u'Query point information associated with the 1-based point ID.')], HRESULT, 'QueryLasPointInfo',
              ( ['in'], c_int, 'FileIndex' ),
              ( ['in'], c_double, 'PointID' ),
              ( ['in'], POINTER(ILasPointInfo), 'pInfo' )),
    COMMETHOD([helpstring(u'Export to Raster.')], HRESULT, 'LasPointStatsAsRaster',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( ['in'], POINTER(ILasPointFilter), 'pFilter' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRasterDataset), 'pDataset' ),
              ( ['in'], esriLasPointStatsType, 'Type' ),
              ( ['in'], esriLasAttributeType, 'Attribute' )),
]
################################################################
## code template for ILasPointCloud implementation
##class ILasPointCloud_Impl(object):
##    def GetLasPoints(self, pTrackCancel, pFilter, thinningFactor, ZFactor):
##        '-no docstring-'
##        #return ppPoints
##
##    def QueryLasPointInfo(self, FileIndex, PointID, pInfo):
##        u'Query point information associated with the 1-based point ID.'
##        #return 
##
##    def GetLasPointInfo(self, pTrackCancel, pLocation, PointID):
##        u'Returns an array of ILasPointInfo(the 1-based pointID is optional).'
##        #return ppInfo
##
##    def EstimatePointSpacing(self, pAOI):
##        u'Estimate point spacing.'
##        #return pMinSpacing, pMaxSpacing, pMeanSpacing
##
##    def LasPointStatsAsRaster(self, pTrackCancel, pFilter, pDataset, Type, Attribute):
##        u'Export to Raster.'
##        #return 
##
##    def EstimatePointCount(self, pAOI):
##        u'Estimate point count.'
##        #return pcPoints
##
##    def GetLasPointsByBudget(self, pTrackCancel, pFilter, maxPointCount, ZFactor):
##        '-no docstring-'
##        #return ppPoints
##

class GPTerrainMembership(CoClass):
    u'The Terrain Membership object.'
    _reg_clsid_ = GUID('{242A9245-015F-4FDF-A16A-FAE4D24B45D6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
GPTerrainMembership._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPControllerMembership, IGPTerrainMembership, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

class DETerrainType(CoClass):
    u'Terrain Data Element object Type.'
    _reg_clsid_ = GUID('{2D9D8047-6490-41E5-85DA-ECB5926582A2}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
DETerrainType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDETerrainType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEGeoDatasetType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEDatasetType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElementType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGxFilterInfo, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDataType, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone]

ITrackingServiceDef._methods_ = [
    COMMETHOD(['propget', helpstring(u'Name of the tracking service.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Name of the tracking service.')], HRESULT, 'Name',
              ( ['in'], BSTR, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Metadata value for the tracking service.')], HRESULT, 'MetaData',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Metadata value for the tracking service.')], HRESULT, 'MetaData',
              ( ['in'], BSTR, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Name that defines the object in the tracking service.')], HRESULT, 'ObjectDefinitionName',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Name that defines the object in the tracking service.')], HRESULT, 'ObjectDefinitionName',
              ( ['in'], BSTR, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Name that defines the observation in the tracking service.')], HRESULT, 'ObservationDefinitionName',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Name that defines the observation in the tracking service.')], HRESULT, 'ObservationDefinitionName',
              ( ['in'], BSTR, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Source of the tracking object in the tracking service.')], HRESULT, 'ObjectSource',
              ( ['retval', 'out'], POINTER(enumObjectSource), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Source of the tracking object in the tracking service.')], HRESULT, 'ObjectSource',
              ( ['in'], enumObjectSource, 'pVal' )),
    COMMETHOD(['propget', helpstring(u"Connection string of the tracking object's source.")], HRESULT, 'ObjectSourceConnectionString',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propput', helpstring(u"Connection string of the tracking object's source.")], HRESULT, 'ObjectSourceConnectionString',
              ( ['in'], BSTR, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Source of the geometry included in tracking service.')], HRESULT, 'SourceOfGeometry',
              ( ['retval', 'out'], POINTER(enumShapeSource), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Source of the geometry included in tracking service.')], HRESULT, 'SourceOfGeometry',
              ( ['in'], enumShapeSource, 'pVal' )),
]
################################################################
## code template for ITrackingServiceDef implementation
##class ITrackingServiceDef_Impl(object):
##    def _get(self):
##        u"Connection string of the tracking object's source."
##        #return pVal
##    def _set(self, pVal):
##        u"Connection string of the tracking object's source."
##    ObjectSourceConnectionString = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Name of the tracking service.'
##        #return pVal
##    def _set(self, pVal):
##        u'Name of the tracking service.'
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Source of the tracking object in the tracking service.'
##        #return pVal
##    def _set(self, pVal):
##        u'Source of the tracking object in the tracking service.'
##    ObjectSource = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Source of the geometry included in tracking service.'
##        #return pVal
##    def _set(self, pVal):
##        u'Source of the geometry included in tracking service.'
##    SourceOfGeometry = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Name that defines the observation in the tracking service.'
##        #return pVal
##    def _set(self, pVal):
##        u'Name that defines the observation in the tracking service.'
##    ObservationDefinitionName = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Metadata value for the tracking service.'
##        #return pVal
##    def _set(self, pVal):
##        u'Metadata value for the tracking service.'
##    MetaData = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Name that defines the object in the tracking service.'
##        #return pVal
##    def _set(self, pVal):
##        u'Name that defines the object in the tracking service.'
##    ObjectDefinitionName = property(_get, _set, doc = _set.__doc__)
##

class LasClassCodeStatistics(CoClass):
    u'Esri LasClassCodeStatistics object.'
    _reg_clsid_ = GUID('{421E5140-A9BE-4215-9357-C4A9852F8CAB}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
class ILasClassCodeStatistics(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to LasClassCodeStatistics object.'
    _iid_ = GUID('{89E4489F-87E2-4690-8385-5143FE6D9753}')
    _idlflags_ = ['oleautomation']
LasClassCodeStatistics._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ILasClassCodeStatistics]

class ITemporalObjectTable(ITemporalTable):
    _case_insensitive_ = True
    _iid_ = GUID('{A677AB60-2FB8-11D5-B7E2-00010265ADC5}')
    _idlflags_ = ['oleautomation']
ITemporalObjectTable._methods_ = [
    COMMETHOD(['propget', helpstring(u"The column name used to 'join' the temporal observations with static features. Note, the column can only contain strings or numbers.")], HRESULT, 'TrackingColumnName',
              ( ['retval', 'out'], POINTER(BSTR), 'pbstrColumnName' )),
]
################################################################
## code template for ITemporalObjectTable implementation
##class ITemporalObjectTable_Impl(object):
##    @property
##    def TrackingColumnName(self):
##        u"The column name used to 'join' the temporal observations with static features. Note, the column can only contain strings or numbers."
##        #return pbstrColumnName
##

ILasClassCodeStatistics._methods_ = [
    COMMETHOD(['propget', helpstring(u'The class code associated with the statistics.')], HRESULT, 'ClassCode',
              ( ['retval', 'out'], POINTER(c_int), 'pCode' )),
    COMMETHOD(['propget', helpstring(u'The number of points associated with this class code (excluding withheld points).')], HRESULT, 'PointCount',
              ( ['retval', 'out'], POINTER(c_double), 'pCount' )),
    COMMETHOD(['propget', helpstring(u'The number of Synthetic points associated with this class code.')], HRESULT, 'SyntheticPointCount',
              ( ['retval', 'out'], POINTER(c_double), 'pCount' )),
    COMMETHOD(['propget', helpstring(u'The number of Key points associated with this class code.')], HRESULT, 'KeyPointCount',
              ( ['retval', 'out'], POINTER(c_double), 'pCount' )),
    COMMETHOD(['propget', helpstring(u'The XYZ extent of points associated with this class code (excluding withheld points).')], HRESULT, 'Extent',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'ppExt' )),
    COMMETHOD([helpstring(u'The minimum and maximum intensity values associated with this class code (excluding withheld points).')], HRESULT, 'GetIntensityRange',
              ( ['out'], POINTER(c_int), 'pMin' ),
              ( ['out'], POINTER(c_int), 'pMax' )),
]
################################################################
## code template for ILasClassCodeStatistics implementation
##class ILasClassCodeStatistics_Impl(object):
##    @property
##    def ClassCode(self):
##        u'The class code associated with the statistics.'
##        #return pCode
##
##    @property
##    def KeyPointCount(self):
##        u'The number of Key points associated with this class code.'
##        #return pCount
##
##    @property
##    def PointCount(self):
##        u'The number of points associated with this class code (excluding withheld points).'
##        #return pCount
##
##    def GetIntensityRange(self):
##        u'The minimum and maximum intensity values associated with this class code (excluding withheld points).'
##        #return pMin, pMax
##
##    @property
##    def SyntheticPointCount(self):
##        u'The number of Synthetic points associated with this class code.'
##        #return pCount
##
##    @property
##    def Extent(self):
##        u'The XYZ extent of points associated with this class code (excluding withheld points).'
##        #return ppExt
##

ILineResequencer._methods_ = [
    COMMETHOD([helpstring(u'Empty the line resequencer of stored lines.')], HRESULT, 'Empty'),
    COMMETHOD([helpstring(u'Add a single line to the resequencer. lineID needs to be unique.')], HRESULT, 'AddLine',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ICurve), 'pLine' ),
              ( ['in'], c_int, 'lineID' ),
              ( ['in'], esriCadastralLineCategory, 'eCategory' )),
    COMMETHOD([helpstring(u'Sort the stored lines and return an ordered array of line OIDs.')], HRESULT, 'Sort',
              ( ['in'], VARIANT_BOOL, 'presentation' ),
              ( ['in', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray)), 'ppLineOrder' ),
              ( ['in', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray)), 'ppReverse' ),
              ( ['in', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry)), 'ppParcel' ),
              ( ['in', 'out'], POINTER(VARIANT_BOOL), 'pFormsLoop' )),
]
################################################################
## code template for ILineResequencer implementation
##class ILineResequencer_Impl(object):
##    def Sort(self, presentation):
##        u'Sort the stored lines and return an ordered array of line OIDs.'
##        #return ppLineOrder, ppReverse, ppParcel, pFormsLoop
##
##    def AddLine(self, pLine, lineID, eCategory):
##        u'Add a single line to the resequencer. lineID needs to be unique.'
##        #return 
##
##    def Empty(self):
##        u'Empty the line resequencer of stored lines.'
##        #return 
##

class LasPointEnumerator(CoClass):
    u'Las Point Enumerator.'
    _reg_clsid_ = GUID('{DDB996E0-31DF-4D77-B903-5295E60AC459}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
LasPointEnumerator._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IEnumLasPoint]

class CadastralFabricName(CoClass):
    u'Esri Cadastral Fabric Name Object.'
    _reg_clsid_ = GUID('{5C947220-FFB5-4E71-A059-AF201AE081A6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
class ICadastralFabricName(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to properties of a cadastral fabric name.'
    _iid_ = GUID('{F7914F56-F87A-4E96-87F8-CBE368DA3C61}')
    _idlflags_ = ['oleautomation']
CadastralFabricName._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ICadastralFabricName, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetName2, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

RGB32 = _RGB32

# values for enumeration 'enumTemporalSource'
enumTemporalSourceField = 0
enumTemporalSource = c_int # enum
class ITemporalRecordSet(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods needed to set up and fill a temporally sorted record set.'
    _iid_ = GUID('{78C74302-17CF-11D5-B7CF-00010265ADC5}')
    _idlflags_ = ['oleautomation']
ITemporalRecordSet._methods_ = [
    COMMETHOD(['propget', helpstring(u'Identifies the column containing time and date information.')], HRESULT, 'TemporalColumnName',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propput', helpstring(u'Identifies the column containing time and date information.')], HRESULT, 'TemporalColumnName',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD(['propget', helpstring(u'A reference to the feature class of which this record set is a member.')], HRESULT, 'FeatureClass',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass)), 'FeatureClass' )),
    COMMETHOD(['propputref', helpstring(u'A reference to the feature class of which this record set is a member.')], HRESULT, 'FeatureClass',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'FeatureClass' )),
    COMMETHOD([helpstring(u'Re-builds the temporal index and caches features based on the supplied temporal parameters.')], HRESULT, 'IndexFeatureClass',
              ( ['in'], VARIANT, 'cacheStartingTime' ),
              ( ['in'], VARIANT, 'cacheEndingTime' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ISelectionSet), 'selSet' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IQueryFilter), 'QueryFilter' ),
              ( ['in'], c_int, 'localeLanguageID' ),
              ( ['in'], BSTR, 'dateFormat' ),
              ( ['in'], BSTR, 'timeFormat' ),
              ( ['in'], BSTR, 'amDesignator' ),
              ( ['in'], BSTR, 'pmDesignator' )),
    COMMETHOD(['propget', helpstring(u'Number of features contained by the cursor.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD([helpstring(u'Performs a query on the record set for the given time range, returning a feature cursor.')], HRESULT, 'Search',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IQueryFilter), 'QueryFilter' ),
              ( ['in'], VARIANT_BOOL, 'Recycling' ),
              ( ['in'], VARIANT_BOOL, 'forDrawing' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureCursor)), 'featureCursor' )),
    COMMETHOD(['propget', helpstring(u"Controls whether features are cached in the renderer's feature memory or are read from the feature class.")], HRESULT, 'CacheFeatures',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'cacheTheFeatures' )),
    COMMETHOD(['propput', helpstring(u"Controls whether features are cached in the renderer's feature memory or are read from the feature class.")], HRESULT, 'CacheFeatures',
              ( ['in'], VARIANT_BOOL, 'cacheTheFeatures' )),
    COMMETHOD(['propget', helpstring(u'Identifies column in the feature class containing temporal observations with time series.')], HRESULT, 'TimeSeriesColumnName',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propput', helpstring(u'Identifies column in the feature class containing temporal observations with time series.')], HRESULT, 'TimeSeriesColumnName',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD(['propget', helpstring(u'Determines the number of features to cache if FeaturesCached property is true.')], HRESULT, 'FeatureCacheWindow',
              ( ['retval', 'out'], POINTER(c_int), 'percent' )),
    COMMETHOD(['propput', helpstring(u'Determines the number of features to cache if FeaturesCached property is true.')], HRESULT, 'FeatureCacheWindow',
              ( ['in'], c_int, 'percent' )),
    COMMETHOD(['propget', helpstring(u'Returns success, but does nothing.')], HRESULT, 'OldestFeature',
              ( ['retval', 'out'], POINTER(VARIANT), 'feature' )),
    COMMETHOD(['propget', helpstring(u'Returns success, but does nothing.')], HRESULT, 'MostCurrentFeature',
              ( ['retval', 'out'], POINTER(VARIANT), 'feature' )),
    COMMETHOD([helpstring(u'Allows user to select record set by its date value.')], HRESULT, 'SelectByDate',
              ( ['in'], VARIANT, 'StartDate' ),
              ( ['in'], VARIANT, 'endDate' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ISelectionSet)), 'selectionSet' )),
]
################################################################
## code template for ITemporalRecordSet implementation
##class ITemporalRecordSet_Impl(object):
##    @property
##    def Count(self):
##        u'Number of features contained by the cursor.'
##        #return Count
##
##    def _get(self):
##        u'Determines the number of features to cache if FeaturesCached property is true.'
##        #return percent
##    def _set(self, percent):
##        u'Determines the number of features to cache if FeaturesCached property is true.'
##    FeatureCacheWindow = property(_get, _set, doc = _set.__doc__)
##
##    def Search(self, QueryFilter, Recycling, forDrawing):
##        u'Performs a query on the record set for the given time range, returning a feature cursor.'
##        #return featureCursor
##
##    def _get(self):
##        u'Identifies column in the feature class containing temporal observations with time series.'
##        #return Name
##    def _set(self, Name):
##        u'Identifies column in the feature class containing temporal observations with time series.'
##    TimeSeriesColumnName = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u"Controls whether features are cached in the renderer's feature memory or are read from the feature class."
##        #return cacheTheFeatures
##    def _set(self, cacheTheFeatures):
##        u"Controls whether features are cached in the renderer's feature memory or are read from the feature class."
##    CacheFeatures = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Identifies the column containing time and date information.'
##        #return Name
##    def _set(self, Name):
##        u'Identifies the column containing time and date information.'
##    TemporalColumnName = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def OldestFeature(self):
##        u'Returns success, but does nothing.'
##        #return feature
##
##    def FeatureClass(self, FeatureClass):
##        u'A reference to the feature class of which this record set is a member.'
##        #return 
##
##    @property
##    def MostCurrentFeature(self):
##        u'Returns success, but does nothing.'
##        #return feature
##
##    def SelectByDate(self, StartDate, endDate):
##        u'Allows user to select record set by its date value.'
##        #return selectionSet
##
##    def IndexFeatureClass(self, cacheStartingTime, cacheEndingTime, selSet, QueryFilter, localeLanguageID, dateFormat, timeFormat, amDesignator, pmDesignator):
##        u'Re-builds the temporal index and caches features based on the supplied temporal parameters.'
##        #return 
##


# values for enumeration 'esriTerrainWindowSizeMethod'
esriTerrainWindowSizeZmin = 0
esriTerrainWindowSizeZmax = 1
esriTerrainWindowSizeZminZmax = 2
esriTerrainWindowSizeZaverage = 3
esriTerrainWindowSizeMethod = c_int # enum

# values for enumeration 'esriTerrainZThresholdStrategy'
esriTerrainZThresholdMildThinning = 0
esriTerrainZThresholdModerateThinning = 1
esriTerrainZThresholdStrongThinning = 2
esriTerrainZThresholdStrategy = c_int # enum
IDETerrainWindowSize._methods_ = [
    COMMETHOD(['propput', helpstring(u'The method used by the windowsize filter to select points.')], HRESULT, 'Method',
              ( ['in'], esriTerrainWindowSizeMethod, 'pMethod' )),
    COMMETHOD(['propget', helpstring(u'The method used by the windowsize filter to select points.')], HRESULT, 'Method',
              ( ['retval', 'out'], POINTER(esriTerrainWindowSizeMethod), 'pMethod' )),
    COMMETHOD(['propput', helpstring(u'The maximum vertical displacement property associated with the secondary thinning filter.')], HRESULT, 'ZThreshold',
              ( ['in'], c_double, 'pThreshold' )),
    COMMETHOD(['propget', helpstring(u'The maximum vertical displacement property associated with the secondary thinning filter.')], HRESULT, 'ZThreshold',
              ( ['retval', 'out'], POINTER(c_double), 'pThreshold' )),
    COMMETHOD(['propput', helpstring(u'Controls how liberal secondary thinning is permitted to be.')], HRESULT, 'ZThresholdStrategy',
              ( ['in'], esriTerrainZThresholdStrategy, 'pStrategy' )),
    COMMETHOD(['propget', helpstring(u'Controls how liberal secondary thinning is permitted to be.')], HRESULT, 'ZThresholdStrategy',
              ( ['retval', 'out'], POINTER(esriTerrainZThresholdStrategy), 'pStrategy' )),
]
################################################################
## code template for IDETerrainWindowSize implementation
##class IDETerrainWindowSize_Impl(object):
##    def _get(self):
##        u'The maximum vertical displacement property associated with the secondary thinning filter.'
##        #return pThreshold
##    def _set(self, pThreshold):
##        u'The maximum vertical displacement property associated with the secondary thinning filter.'
##    ZThreshold = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Controls how liberal secondary thinning is permitted to be.'
##        #return pStrategy
##    def _set(self, pStrategy):
##        u'Controls how liberal secondary thinning is permitted to be.'
##    ZThresholdStrategy = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The method used by the windowsize filter to select points.'
##        #return pMethod
##    def _set(self, pMethod):
##        u'The method used by the windowsize filter to select points.'
##    Method = property(_get, _set, doc = _set.__doc__)
##

class ILasHeaderInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the header information of LAS files.'
    _iid_ = GUID('{89F48C7A-AC12-4371-92C3-194559BB354B}')
    _idlflags_ = ['oleautomation']
ILasHeaderInfo._methods_ = [
    COMMETHOD([helpstring(u'The version of the LAS file.')], HRESULT, 'GetVersion',
              ( ['out'], POINTER(c_int), 'pMajor' ),
              ( ['out'], POINTER(c_int), 'pMinor' )),
    COMMETHOD(['propget', helpstring(u'The record format for points in the LAS file')], HRESULT, 'PointDataFormat',
              ( ['retval', 'out'], POINTER(c_int), 'pFormat' )),
    COMMETHOD(['propget', helpstring(u'The hardware system used to collect the LiDAR data in the LAS file.')], HRESULT, 'SystemID',
              ( ['retval', 'out'], POINTER(BSTR), 'pID' )),
    COMMETHOD(['propget', helpstring(u'The software used to create the LAS file.')], HRESULT, 'GeneratingSoftware',
              ( ['retval', 'out'], POINTER(BSTR), 'pName' )),
    COMMETHOD(['propget', helpstring(u'The flight date based on the Julian calendar.')], HRESULT, 'FlightDateJulian',
              ( ['retval', 'out'], POINTER(c_int), 'pDate' )),
    COMMETHOD(['propget', helpstring(u'The year the data in the LAS file was collected.')], HRESULT, 'Year',
              ( ['retval', 'out'], POINTER(c_int), 'pYear' )),
    COMMETHOD(['propget', helpstring(u'The number of points in the LAS file.')], HRESULT, 'NumberOfPointRecords',
              ( ['retval', 'out'], POINTER(c_double), 'pcRecords' )),
    COMMETHOD([helpstring(u'The number of points in the LAS file based on the specified LiDAR return number.')], HRESULT, 'GetNumberOfPointsByReturn',
              ( ['in'], c_int, 'ReturnNumber' ),
              ( ['retval', 'out'], POINTER(c_double), 'pcPoints' )),
    COMMETHOD(['propget', helpstring(u"The LAS file's project ID.")], HRESULT, 'ProjectID',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID)), 'ppGuid' )),
    COMMETHOD(['propget', helpstring(u"The LAS file's source ID.")], HRESULT, 'FileSourceID',
              ( ['retval', 'out'], POINTER(c_int), 'pID' )),
    COMMETHOD(['propget', helpstring(u'Indicates if RGB is availabe.')], HRESULT, 'HasRGB',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbHasRGB' )),
    COMMETHOD(['propget', helpstring(u'Indicates GPS time is available.')], HRESULT, 'HasGpsTime',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbHasGpsTime' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the GPS time is standard GPS Time.')], HRESULT, 'IsStandardGpsTime',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbIsAStandard' )),
    COMMETHOD(['propget', helpstring(u'The XYZ extent of points in the LAS file.')], HRESULT, 'Extent',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'ppExt' )),
    COMMETHOD(['propget', helpstring(u'The spatial reference of the LAS file.')], HRESULT, 'SpatialReference',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference)), 'ppSpatialReference' )),
    COMMETHOD([helpstring(u'The coordinate offsets.')], HRESULT, 'GetOffsets',
              ( ['out'], POINTER(c_double), 'pOffsetX' ),
              ( ['out'], POINTER(c_double), 'pOffsetY' ),
              ( ['out'], POINTER(c_double), 'pOffsetZ' )),
    COMMETHOD([helpstring(u'The coordinate scale factors.')], HRESULT, 'GetScaleFactors',
              ( ['out'], POINTER(c_double), 'pFactorX' ),
              ( ['out'], POINTER(c_double), 'pFactorY' ),
              ( ['out'], POINTER(c_double), 'pFactorZ' )),
    COMMETHOD(['propget', helpstring(u'The number of variable length records in the LAS file.')], HRESULT, 'NumberOfVariableLengthRecords',
              ( ['retval', 'out'], POINTER(c_double), 'pcRecords' )),
    COMMETHOD([helpstring(u'The variable length record info.')], HRESULT, 'GetVariableLengthRecords',
              ( ['out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'ppUserIDs' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray)), 'recordIDs' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDoubleArray)), 'ppRecordLengths' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'ppDescriptions' ),
              ( ['out'], POINTER(VARIANT_BOOL), 'pbOverLimit' )),
]
################################################################
## code template for ILasHeaderInfo implementation
##class ILasHeaderInfo_Impl(object):
##    @property
##    def NumberOfVariableLengthRecords(self):
##        u'The number of variable length records in the LAS file.'
##        #return pcRecords
##
##    @property
##    def FlightDateJulian(self):
##        u'The flight date based on the Julian calendar.'
##        #return pDate
##
##    def GetOffsets(self):
##        u'The coordinate offsets.'
##        #return pOffsetX, pOffsetY, pOffsetZ
##
##    @property
##    def PointDataFormat(self):
##        u'The record format for points in the LAS file'
##        #return pFormat
##
##    @property
##    def ProjectID(self):
##        u"The LAS file's project ID."
##        #return ppGuid
##
##    @property
##    def IsStandardGpsTime(self):
##        u'Indicates if the GPS time is standard GPS Time.'
##        #return pbIsAStandard
##
##    def GetScaleFactors(self):
##        u'The coordinate scale factors.'
##        #return pFactorX, pFactorY, pFactorZ
##
##    @property
##    def SpatialReference(self):
##        u'The spatial reference of the LAS file.'
##        #return ppSpatialReference
##
##    @property
##    def SystemID(self):
##        u'The hardware system used to collect the LiDAR data in the LAS file.'
##        #return pID
##
##    def GetNumberOfPointsByReturn(self, ReturnNumber):
##        u'The number of points in the LAS file based on the specified LiDAR return number.'
##        #return pcPoints
##
##    @property
##    def Extent(self):
##        u'The XYZ extent of points in the LAS file.'
##        #return ppExt
##
##    @property
##    def Year(self):
##        u'The year the data in the LAS file was collected.'
##        #return pYear
##
##    @property
##    def NumberOfPointRecords(self):
##        u'The number of points in the LAS file.'
##        #return pcRecords
##
##    def GetVersion(self):
##        u'The version of the LAS file.'
##        #return pMajor, pMinor
##
##    def GetVariableLengthRecords(self):
##        u'The variable length record info.'
##        #return ppUserIDs, recordIDs, ppRecordLengths, ppDescriptions, pbOverLimit
##
##    @property
##    def HasGpsTime(self):
##        u'Indicates GPS time is available.'
##        #return pbHasGpsTime
##
##    @property
##    def GeneratingSoftware(self):
##        u'The software used to create the LAS file.'
##        #return pName
##
##    @property
##    def FileSourceID(self):
##        u"The LAS file's source ID."
##        #return pID
##
##    @property
##    def HasRGB(self):
##        u'Indicates if RGB is availabe.'
##        #return pbHasRGB
##

class LasToRasterFunction(CoClass):
    u'The LasToRasterFunction class.'
    _reg_clsid_ = GUID('{9889D8FB-93F6-49B1-B352-D8E2B331C797}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
LasToRasterFunction._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._8F0541A3_D5BE_4B3F_A8D9_062D5579E19B_0_10_2.IRasterFunction, comtypes.gen._8F0541A3_D5BE_4B3F_A8D9_062D5579E19B_0_10_2.IRasterFunction2, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLVersionSupport]

class IConstructionUnbuildableLines(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manipulate the unbuildable lines of a parcel construction.'
    _iid_ = GUID('{11EA4990-32F3-4AAC-B285-F70FF18C956F}')
    _idlflags_ = ['oleautomation']
IConstructionUnbuildableLines._methods_ = [
    COMMETHOD([helpstring(u'Mark a line as unbuildable for the parent parcel.')], HRESULT, 'AddUnbuildableLine',
              ( ['in'], c_int, 'parentParcelNo' ),
              ( ['in'], c_int, 'fromPointNo' ),
              ( ['in'], c_int, 'toPointNo' )),
    COMMETHOD([helpstring(u'Remove unbuildable line for the parent parcel.')], HRESULT, 'RemoveUnbuildableLine',
              ( ['in'], c_int, 'parentParcelNo' ),
              ( ['in'], c_int, 'fromPointNo' ),
              ( ['in'], c_int, 'toPointNo' )),
    COMMETHOD([helpstring(u'Input the from and to points for the unbuildable lines of the parent parcel.')], HRESULT, 'SetUnbuildableLines',
              ( ['in'], c_int, 'parentParcelNo' ),
              ( ['in'], c_int, 'Count' ),
              ( ['in'], POINTER(c_int), 'fromPointNos' ),
              ( ['in'], POINTER(c_int), 'toPointNos' )),
    COMMETHOD([helpstring(u'Retrieve the from and to points for the unbuildables lines of the parent parcel.')], HRESULT, 'GetUnbuildableLines',
              ( ['in'], c_int, 'parentParcelNo' ),
              ( ['in', 'out'], POINTER(c_int), 'Count' ),
              ( ['in', 'out'], POINTER(POINTER(c_int)), 'fromPointNos' ),
              ( ['in', 'out'], POINTER(POINTER(c_int)), 'toPointNos' )),
    COMMETHOD([helpstring(u'Clears the unbuildables lines of the parent parcel.')], HRESULT, 'ClearUnbuildableLines',
              ( ['in'], c_int, 'parentParcelNo' )),
]
################################################################
## code template for IConstructionUnbuildableLines implementation
##class IConstructionUnbuildableLines_Impl(object):
##    def AddUnbuildableLine(self, parentParcelNo, fromPointNo, toPointNo):
##        u'Mark a line as unbuildable for the parent parcel.'
##        #return 
##
##    def ClearUnbuildableLines(self, parentParcelNo):
##        u'Clears the unbuildables lines of the parent parcel.'
##        #return 
##
##    def SetUnbuildableLines(self, parentParcelNo, Count, fromPointNos, toPointNos):
##        u'Input the from and to points for the unbuildable lines of the parent parcel.'
##        #return 
##
##    def RemoveUnbuildableLine(self, parentParcelNo, fromPointNo, toPointNo):
##        u'Remove unbuildable line for the parent parcel.'
##        #return 
##
##    def GetUnbuildableLines(self, parentParcelNo):
##        u'Retrieve the from and to points for the unbuildables lines of the parent parcel.'
##        #return Count, fromPointNos, toPointNos
##

class TerrainFeatureDatasetExtension(CoClass):
    u'Esri TerrainFeatureDatasetExtension object.'
    _reg_clsid_ = GUID('{9A88D1B2-A418-4AD7-9107-FE41DE647FAF}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
TerrainFeatureDatasetExtension._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureDatasetExtension, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetContainer, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetContainer2, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetContainer3]

class IConstructionAdjustment(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manipulate the adjustment settings for the parcel construction.'
    _iid_ = GUID('{CB760247-E82A-4666-A79E-A6F1F6BF2845}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriParcelAdjustmentType'
esriParcelAdjustmentNone = -1
esriParcelAdjustmentCompass = 0
esriParcelAdjustmentTransit = 1
esriParcelAdjustmentCrandall = 2
esriParcelAdjustmentType = c_int # enum
IConstructionAdjustment._methods_ = [
    COMMETHOD(['propget', helpstring(u'The method for adjustment.')], HRESULT, 'AdjustmentMethod',
              ( ['retval', 'out'], POINTER(esriParcelAdjustmentType), 'Type' )),
    COMMETHOD(['propput', helpstring(u'The method for adjustment.')], HRESULT, 'AdjustmentMethod',
              ( ['in'], esriParcelAdjustmentType, 'Type' )),
    COMMETHOD([helpstring(u'The start point for the adjustment.')], HRESULT, 'GetStartPoint',
              ( ['in', 'out'], POINTER(c_int), 'UnjoinedPointNo' ),
              ( ['in', 'out'], POINTER(c_double), 'x' ),
              ( ['in', 'out'], POINTER(c_double), 'y' )),
    COMMETHOD([helpstring(u'The end point for the adjustment.')], HRESULT, 'GetEndPoint',
              ( ['in', 'out'], POINTER(c_int), 'UnjoinedPointNo' ),
              ( ['in', 'out'], POINTER(c_double), 'x' ),
              ( ['in', 'out'], POINTER(c_double), 'y' )),
    COMMETHOD([helpstring(u'The start point for the adjustment.')], HRESULT, 'SetStartPoint',
              ( ['in'], c_int, 'UnjoinedPointNo' ),
              ( ['in'], c_double, 'x' ),
              ( ['in'], c_double, 'y' )),
    COMMETHOD([helpstring(u'The start point for the adjustment.')], HRESULT, 'SetEndPoint',
              ( ['in'], c_int, 'UnjoinedPointNo' ),
              ( ['in'], c_double, 'x' ),
              ( ['in'], c_double, 'y' )),
]
################################################################
## code template for IConstructionAdjustment implementation
##class IConstructionAdjustment_Impl(object):
##    def SetEndPoint(self, UnjoinedPointNo, x, y):
##        u'The start point for the adjustment.'
##        #return 
##
##    def SetStartPoint(self, UnjoinedPointNo, x, y):
##        u'The start point for the adjustment.'
##        #return 
##
##    def GetEndPoint(self):
##        u'The end point for the adjustment.'
##        #return UnjoinedPointNo, x, y
##
##    def _get(self):
##        u'The method for adjustment.'
##        #return Type
##    def _set(self, Type):
##        u'The method for adjustment.'
##    AdjustmentMethod = property(_get, _set, doc = _set.__doc__)
##
##    def GetStartPoint(self):
##        u'The start point for the adjustment.'
##        #return UnjoinedPointNo, x, y
##

class Terrain(CoClass):
    u'The Esri Terrain component.'
    _reg_clsid_ = GUID('{EA9EB4A1-77B3-433C-A7DD-BB4436FA0E98}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
class ITerrainEdit(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members used to modify and build a terrain.'
    _iid_ = GUID('{8E9C9736-60B1-4DB5-AF18-ED40F41D4714}')
    _idlflags_ = ['oleautomation']
class ITerrainEdit2(ITerrainEdit):
    _case_insensitive_ = True
    u'Provides access to members used to modify and build a terrain.'
    _iid_ = GUID('{ED9009EB-18F0-436E-9385-0F0007DD1F90}')
    _idlflags_ = ['oleautomation']
class ITerrainEdit3(ITerrainEdit2):
    _case_insensitive_ = True
    u'Provides access to members used to modify and build a terrain.'
    _iid_ = GUID('{A7E67808-29D5-4DD9-8696-06993FA838B4}')
    _idlflags_ = ['oleautomation']
class ITerrainEditEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to events that occur with a Terrain dataset.'
    _iid_ = GUID('{F008BA42-5126-4DAF-88EC-005AF3A60083}')
    _idlflags_ = ['oleautomation']
Terrain._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataset, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset, ITerrain, ITerrain2, ITerrainEdit, ITerrainEdit2, ITerrainEdit3, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ISchemaLock, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetAnalyze, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetComponent, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetComponent2, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo]
Terrain._outgoing_interfaces_ = [ITerrainEditEvents]

class ITxWorkspaceEditor(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to properties and methods needed to edit a tracking workspace objects connection properties.'
    _iid_ = GUID('{A1FF9810-87A9-11D7-B87A-00010265ADC5}')
    _idlflags_ = ['oleautomation']
ITxWorkspaceEditor._methods_ = [
    COMMETHOD(['propput', helpstring(u'Connection properties to edit.')], HRESULT, 'ConnectionProperties',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'ppiConnectionProperties' )),
    COMMETHOD(['propget', helpstring(u'Connection properties to edit.')], HRESULT, 'ConnectionProperties',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'ppiConnectionProperties' )),
    COMMETHOD([helpstring(u'Invokes the workspace editor dialog.')], HRESULT, 'Invoke',
              ( ['in'], comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.OLE_HANDLE, 'hParentWnd' )),
]
################################################################
## code template for ITxWorkspaceEditor implementation
##class ITxWorkspaceEditor_Impl(object):
##    def _get(self):
##        u'Connection properties to edit.'
##        #return ppiConnectionProperties
##    def _set(self, ppiConnectionProperties):
##        u'Connection properties to edit.'
##    ConnectionProperties = property(_get, _set, doc = _set.__doc__)
##
##    def Invoke(self, hParentWnd):
##        u'Invokes the workspace editor dialog.'
##        #return 
##

ILasFile._methods_ = [
    COMMETHOD(['propget', helpstring(u'The (full) file name.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pName' )),
    COMMETHOD([helpstring(u'The version of the LAS file.')], HRESULT, 'GetVersion',
              ( ['out'], POINTER(c_int), 'pMajor' ),
              ( ['out'], POINTER(c_int), 'pMinor' )),
    COMMETHOD(['propget', helpstring(u'The record format for points in the LAS file')], HRESULT, 'PointDataFormat',
              ( ['retval', 'out'], POINTER(c_int), 'pFormat' )),
    COMMETHOD(['propget', helpstring(u'The number of points in the LAS file.')], HRESULT, 'NumberOfPointRecords',
              ( ['retval', 'out'], POINTER(c_double), 'pcRecords' )),
    COMMETHOD([helpstring(u'The number of points in the LAS file based on the specified LiDAR return number.')], HRESULT, 'GetNumberOfPointsByReturn',
              ( ['in'], c_int, 'ReturnNumber' ),
              ( ['retval', 'out'], POINTER(c_double), 'pcPoints' )),
    COMMETHOD(['propget', helpstring(u"The LAS file's size in bytes.")], HRESULT, 'SizeInBytes',
              ( ['retval', 'out'], POINTER(c_double), 'pcBytes' )),
    COMMETHOD(['propget', helpstring(u'Indicates if RGB is availabe.')], HRESULT, 'HasRGB',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbHasRGB' )),
    COMMETHOD(['propget', helpstring(u'Indicates GPS time is available.')], HRESULT, 'HasGpsTime',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbHasGpsTime' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the GPS time is standard GPS Time.')], HRESULT, 'IsStandardGpsTime',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbIsAStandard' )),
    COMMETHOD(['propget', helpstring(u'The XYZ extent of points in the LAS file.')], HRESULT, 'Extent',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'ppExt' )),
    COMMETHOD(['propget', helpstring(u'The spatial reference of the LAS file.')], HRESULT, 'SpatialReference',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference)), 'ppSpatialReference' )),
    COMMETHOD(['propget', helpstring(u'The spatial reference defined in the LAS file header.')], HRESULT, 'NativeSpatialReference',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference)), 'ppSpatialReference' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the LAS file is missing.')], HRESULT, 'IsFileMissing',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbIsMissing' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the LAS file exists and is valid.')], HRESULT, 'IsFileValid',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbIsValid' )),
    COMMETHOD(['propget', helpstring(u'Indicates if there is a corresponding PRJ file.')], HRESULT, 'HasPrjFile',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbHasPRJ' )),
    COMMETHOD(['propget', helpstring(u'Indicates if statistics is available.')], HRESULT, 'HasStatistics',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbHasStats' )),
    COMMETHOD(['propget', helpstring(u'Indicates if update is necessary.')], HRESULT, 'NeedsUpdateStatistics',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbNeedsUpdate' )),
    COMMETHOD([helpstring(u'Get statistics.')], HRESULT, 'GetStatistics',
              ( ['retval', 'out'], POINTER(POINTER(ILasStatistics)), 'ppStatistics' )),
    COMMETHOD([helpstring(u'Get LAS file header information.')], HRESULT, 'GetHeaderInfo',
              ( ['retval', 'out'], POINTER(POINTER(ILasHeaderInfo)), 'ppHeaderInfo' )),
    COMMETHOD([helpstring(u'Estimate point spacing.')], HRESULT, 'EstimatePointSpacing',
              ( ['in'], VARIANT_BOOL, 'bUseStatistics' ),
              ( ['retval', 'out'], POINTER(c_double), 'pSpacing' )),
    COMMETHOD([helpstring(u'Estimate point count.')], HRESULT, 'EstimatePointCount',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'pAOI' ),
              ( ['retval', 'out'], POINTER(c_double), 'pcPoints' )),
]
################################################################
## code template for ILasFile implementation
##class ILasFile_Impl(object):
##    @property
##    def SizeInBytes(self):
##        u"The LAS file's size in bytes."
##        #return pcBytes
##
##    @property
##    def IsFileMissing(self):
##        u'Indicates if the LAS file is missing.'
##        #return pbIsMissing
##
##    def EstimatePointSpacing(self, bUseStatistics):
##        u'Estimate point spacing.'
##        #return pSpacing
##
##    @property
##    def Name(self):
##        u'The (full) file name.'
##        #return pName
##
##    def GetHeaderInfo(self):
##        u'Get LAS file header information.'
##        #return ppHeaderInfo
##
##    @property
##    def IsFileValid(self):
##        u'Indicates if the LAS file exists and is valid.'
##        #return pbIsValid
##
##    @property
##    def PointDataFormat(self):
##        u'The record format for points in the LAS file'
##        #return pFormat
##
##    @property
##    def IsStandardGpsTime(self):
##        u'Indicates if the GPS time is standard GPS Time.'
##        #return pbIsAStandard
##
##    @property
##    def HasStatistics(self):
##        u'Indicates if statistics is available.'
##        #return pbHasStats
##
##    @property
##    def SpatialReference(self):
##        u'The spatial reference of the LAS file.'
##        #return ppSpatialReference
##
##    @property
##    def NeedsUpdateStatistics(self):
##        u'Indicates if update is necessary.'
##        #return pbNeedsUpdate
##
##    @property
##    def HasPrjFile(self):
##        u'Indicates if there is a corresponding PRJ file.'
##        #return pbHasPRJ
##
##    def GetNumberOfPointsByReturn(self, ReturnNumber):
##        u'The number of points in the LAS file based on the specified LiDAR return number.'
##        #return pcPoints
##
##    @property
##    def Extent(self):
##        u'The XYZ extent of points in the LAS file.'
##        #return ppExt
##
##    @property
##    def HasGpsTime(self):
##        u'Indicates GPS time is available.'
##        #return pbHasGpsTime
##
##    @property
##    def NumberOfPointRecords(self):
##        u'The number of points in the LAS file.'
##        #return pcRecords
##
##    def GetVersion(self):
##        u'The version of the LAS file.'
##        #return pMajor, pMinor
##
##    def EstimatePointCount(self, pAOI):
##        u'Estimate point count.'
##        #return pcPoints
##
##    @property
##    def NativeSpatialReference(self):
##        u'The spatial reference defined in the LAS file header.'
##        #return ppSpatialReference
##
##    def GetStatistics(self):
##        u'Get statistics.'
##        #return ppStatistics
##
##    @property
##    def HasRGB(self):
##        u'Indicates if RGB is availabe.'
##        #return pbHasRGB
##

class IExcludedEventIDs(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to Tracking Connection EventIDs to be permanently purged from cache and ignored in future.'
    _iid_ = GUID('{2EB7644E-63DD-4A25-9EF9-B794EC6BF691}')
    _idlflags_ = []
IExcludedEventIDs._methods_ = [
    COMMETHOD(['propget', helpstring(u'String array of EventIDs to be permanently purged and ignored.')], HRESULT, 'ExcludedTrackingEventIDs',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'String array of EventIDs to be permanently purged and ignored.')], HRESULT, 'ExcludedTrackingEventIDs',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray), 'pVal' )),
]
################################################################
## code template for IExcludedEventIDs implementation
##class IExcludedEventIDs_Impl(object):
##    def _get(self):
##        u'String array of EventIDs to be permanently purged and ignored.'
##        #return pVal
##    def _set(self, pVal):
##        u'String array of EventIDs to be permanently purged and ignored.'
##    ExcludedTrackingEventIDs = property(_get, _set, doc = _set.__doc__)
##


# values for enumeration 'esriLasDatasetError'
E_LAS_BAD_Z_SOURCE = -2147201024
E_LAS_DATASET_EXISTS = -2147201023
E_LAS_FAILED_TO_OVER_WRITE = -2147201022
E_LAS_FAILED_TO_SAVE = -2147201021
E_LAS_FAILED_TO_OPEN = -2147201020
E_LAS_NO_STATISTICS = -2147201019
E_LAS_FAILED_TO_COPY_FILE = -2147201018
E_LAS_IN_MEMORY_DATASET = -2147201017
E_LAS_CLASS_FLAG_NOT_SUPPORTED = -2147201016
E_LAS_BAD_CLASS_CODE = -2147201015
E_LAS_INVALID_VERSION = -2147201014
E_LAS_UNABLE_TO_EDIT_ZIP_FILE = -2147201013
E_LAS_OPERATION_NOT_SUPPORTED_ON_ZIP_FILE = -2147201012
esriLasDatasetError = c_int # enum
class ITemporalFeatureClass2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to server name info.'
    _iid_ = GUID('{4B026C0C-7189-4EDF-9EA0-568C9D092257}')
    _idlflags_ = ['oleautomation']
ITemporalFeatureClass2._methods_ = [
    COMMETHOD(['propget', helpstring(u'Return Server Name.')], HRESULT, 'ServerName',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'Return Connection Name.')], HRESULT, 'ConnectionName',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
]
################################################################
## code template for ITemporalFeatureClass2 implementation
##class ITemporalFeatureClass2_Impl(object):
##    @property
##    def ServerName(self):
##        u'Return Server Name.'
##        #return Name
##
##    @property
##    def ConnectionName(self):
##        u'Return Connection Name.'
##        #return Name
##

class ICadastralFabricEditControl(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to method that controls if insert and update cursors on fabric classes can bypass store events.'
    _iid_ = GUID('{A56B04A1-1748-40AB-BB7E-DFE95B34DD48}')
    _idlflags_ = ['oleautomation']
ICadastralFabricEditControl._methods_ = [
    COMMETHOD([helpstring(u'Indicates that insert and update cursors on fabric classes cannot bypass store events for the active edit session.')], HRESULT, 'SetStoreEventsRequired'),
]
################################################################
## code template for ICadastralFabricEditControl implementation
##class ICadastralFabricEditControl_Impl(object):
##    def SetStoreEventsRequired(self):
##        u'Indicates that insert and update cursors on fabric classes cannot bypass store events for the active edit session.'
##        #return 
##

class ILasPointEdit(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of LasDataset.'
    _iid_ = GUID('{5EA400DD-3AFA-4423-9BC7-4915F4292911}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriLasClassFlagEditType'
esriLasClassFlagNoChange = 0
esriLasClassFlagSet = 1
esriLasClassFlagClear = 2
esriLasClassFlagEditType = c_int # enum
ILasPointEdit._methods_ = [
    COMMETHOD([helpstring(u"Set points' classification flag.")], HRESULT, 'SetClassFlag',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( ['in'], c_int, 'FileIndex' ),
              ( ['in'], POINTER(IUnknown), 'pAOI' ),
              ( ['in'], c_double, 'bufferDistance' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDoubleArray), 'pZRange' ),
              ( ['in'], POINTER(ILasAttributeFilter), 'pFilter' ),
              ( ['in'], c_int, 'newFlags' ),
              ( ['in'], VARIANT_BOOL, 'bClear' ),
              ( ['in'], VARIANT_BOOL, 'bCalculateStats' )),
    COMMETHOD([helpstring(u"Set points' class code.")], HRESULT, 'SetClassCode',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( ['in'], c_int, 'FileIndex' ),
              ( ['in'], POINTER(IUnknown), 'pAOI' ),
              ( ['in'], c_double, 'bufferDistance' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDoubleArray), 'pZRange' ),
              ( ['in'], POINTER(ILasAttributeFilter), 'pFilter' ),
              ( ['in'], c_int, 'newCode' ),
              ( ['in'], VARIANT_BOOL, 'bCalculateStats' )),
    COMMETHOD([helpstring(u"Replace points' class code.")], HRESULT, 'ChangeClassCode',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( ['in'], c_int, 'FileIndex' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray), 'pExistingCodes' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray), 'pNewCodes' ),
              ( ['in'], VARIANT_BOOL, 'bCalculateStats' )),
    COMMETHOD([helpstring(u'Set class code and flags (negative classCode value indicates no code change).')], HRESULT, 'EditClassCodeByClass',
              ( ['in'], c_int, 'FileIndex' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDoubleArray), 'pPointIDs' ),
              ( ['in'], c_int, 'newCode' ),
              ( ['in'], esriLasClassFlagEditType, 'withheldFlag' ),
              ( ['in'], esriLasClassFlagEditType, 'keyPointFlag' ),
              ( ['in'], esriLasClassFlagEditType, 'syntheticFlag' ),
              ( ['out'], POINTER(VARIANT_BOOL), 'pbHasChange' )),
    COMMETHOD([helpstring(u"Set points' class code.")], HRESULT, 'EditClassCode',
              ( ['in'], c_int, 'FileIndex' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDoubleArray), 'pPointIDs' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray), 'pCodes' ),
              ( ['out'], POINTER(VARIANT_BOOL), 'pbHasChange' )),
]
################################################################
## code template for ILasPointEdit implementation
##class ILasPointEdit_Impl(object):
##    def ChangeClassCode(self, pTrackCancel, FileIndex, pExistingCodes, pNewCodes, bCalculateStats):
##        u"Replace points' class code."
##        #return 
##
##    def SetClassFlag(self, pTrackCancel, FileIndex, pAOI, bufferDistance, pZRange, pFilter, newFlags, bClear, bCalculateStats):
##        u"Set points' classification flag."
##        #return 
##
##    def SetClassCode(self, pTrackCancel, FileIndex, pAOI, bufferDistance, pZRange, pFilter, newCode, bCalculateStats):
##        u"Set points' class code."
##        #return 
##
##    def EditClassCodeByClass(self, FileIndex, pPointIDs, newCode, withheldFlag, keyPointFlag, syntheticFlag):
##        u'Set class code and flags (negative classCode value indicates no code change).'
##        #return pbHasChange
##
##    def EditClassCode(self, FileIndex, pPointIDs, pCodes):
##        u"Set points' class code."
##        #return pbHasChange
##


# values for enumeration 'esriPointToRasterVoidFillMethod'
esriPointToRasterVoidFillNoFill = 1
esriPointToRasterVoidFillSimple = 2
esriPointToRasterVoidFillInterpolation = 3
esriPointToRasterVoidFillMethod = c_int # enum

# values for enumeration 'esriPointToRasterMethod'
esriPointToRasterZmin = 1
esriPointToRasterZmax = 2
esriPointToRasterZaverage = 3
esriPointToRasterIDW = 4
esriPointToRasterNearest = 5
esriPointToRasterMethod = c_int # enum

# values for enumeration 'esriTinPointSelectionMethod'
esriTinPointSelectionRandom = 1
esriTinPointSelectionZmin = 2
esriTinPointSelectionZmax = 3
esriTinPointSelectionZaverage = 4
esriTinPointSelectionMethod = c_int # enum

# values for enumeration 'esriLasZSource'
esriLasZSourceZ = 0
esriLasZSourceIntensity = 1
esriLasZSourceColorRed = 2
esriLasZSourceColorGreen = 3
esriLasZSourceColorBlue = 4
esriLasZSourceColorRGB = 5
esriLasZSource = c_int # enum
ITerrainBlobWriter._methods_ = [
    COMMETHOD([helpstring(u'Initialize a new blob with the specified data type.')], HRESULT, 'BeginAddingValue',
              ( ['in'], esriTerrainBlobDataType, 'Type' )),
    COMMETHOD([helpstring(u'Adds an attribute value to the blob.')], HRESULT, 'AddValue',
              ( ['in'], VARIANT, 'Value' )),
    COMMETHOD([helpstring(u'Returns the number of attribute values contained in the blob.')], HRESULT, 'GetItemCount',
              ( ['retval', 'out'], POINTER(c_int), 'pcItems' )),
    COMMETHOD([helpstring(u'Completes writing the blob and returns a reference to the blob object.')], HRESULT, 'EndAddingValue',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IMemoryBlobStream)), 'ppBlob' )),
]
################################################################
## code template for ITerrainBlobWriter implementation
##class ITerrainBlobWriter_Impl(object):
##    def AddValue(self, Value):
##        u'Adds an attribute value to the blob.'
##        #return 
##
##    def EndAddingValue(self):
##        u'Completes writing the blob and returns a reference to the blob object.'
##        #return ppBlob
##
##    def GetItemCount(self):
##        u'Returns the number of attribute values contained in the blob.'
##        #return pcItems
##
##    def BeginAddingValue(self, Type):
##        u'Initialize a new blob with the specified data type.'
##        #return 
##

class IDatasetNames(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to properties and methods needed to manage dataset name information.'
    _iid_ = GUID('{10ED95D6-33F5-11D5-B7E3-00010265ADC5}')
    _idlflags_ = []
IDatasetNames._methods_ = [
]
################################################################
## code template for IDatasetNames implementation
##class IDatasetNames_Impl(object):

IEnumLasPoint._methods_ = [
    COMMETHOD(['propput', helpstring(u'The LAS attribute.')], HRESULT, 'Attribute',
              ( ['in'], esriLasAttributeType, 'pAttribute' )),
    COMMETHOD(['propget', helpstring(u'The LAS attribute.')], HRESULT, 'Attribute',
              ( ['retval', 'out'], POINTER(esriLasAttributeType), 'pAttribute' )),
    COMMETHOD([helpstring(u'Resets the enumerator.')], HRESULT, 'Reset'),
    COMMETHOD([helpstring(u'Populates an array of WKSPointZs, optional arrays of 0-based file indices and 1-based point IDs.')], HRESULT, 'Next',
              ( ['in'], c_int, 'arraySize' ),
              ( ['out'], POINTER(c_int), 'pPointCount' ),
              ( ['out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.WKSPointZ), 'pPoints' ),
              ( [], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray), 'pIntensity' ),
              ( [], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray), 'pFileIndices' ),
              ( [], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDoubleArray), 'pPointIDs' )),
    COMMETHOD([helpstring(u'Populates arrays of WKSPointZs and attributes, and optional arrays of 0-based file indices and 1-based point IDs.')], HRESULT, 'NextAttrLong',
              ( ['in'], c_int, 'arraySize' ),
              ( ['out'], POINTER(c_int), 'pPointCount' ),
              ( ['out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.WKSPointZ), 'pPoints' ),
              ( ['out'], POINTER(c_int), 'pAttribute' ),
              ( [], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray), 'pIntensity' ),
              ( [], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray), 'pFileIndices' ),
              ( [], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDoubleArray), 'pPointIDs' )),
    COMMETHOD([helpstring(u'Populates arrays of WKSPointZs and attributes, and optional arrays of 0-based file indices and 1-based point IDs.')], HRESULT, 'NextAttrDbl',
              ( ['in'], c_int, 'arraySize' ),
              ( ['out'], POINTER(c_int), 'pPointCount' ),
              ( ['out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.WKSPointZ), 'pPoints' ),
              ( ['out'], POINTER(c_double), 'pAttribute' ),
              ( [], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray), 'pIntensity' ),
              ( [], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray), 'pFileIndices' ),
              ( [], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDoubleArray), 'pPointIDs' )),
    COMMETHOD([helpstring(u'Populates arrays of WKSPointZs and RGB colors, and optional arrays of 0-based file indices and 1-based point IDs.')], HRESULT, 'NextAttrRGB32',
              ( ['in'], c_int, 'arraySize' ),
              ( ['out'], POINTER(c_int), 'pPointCount' ),
              ( ['out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.WKSPointZ), 'pPoints' ),
              ( ['out'], POINTER(RGB32), 'pAttribute' ),
              ( [], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray), 'pIntensity' ),
              ( [], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray), 'pFileIndices' ),
              ( [], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDoubleArray), 'pPointIDs' )),
    COMMETHOD([helpstring(u'Populates an array of ILasPointInfo.')], HRESULT, 'NextLasInfo',
              ( [], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IArray), 'pInfo' ),
              ( ['out'], POINTER(c_int), 'pPointCount' )),
]
################################################################
## code template for IEnumLasPoint implementation
##class IEnumLasPoint_Impl(object):
##    def Reset(self):
##        u'Resets the enumerator.'
##        #return 
##
##    def NextAttrDbl(self, arraySize, pIntensity, pFileIndices, pPointIDs):
##        u'Populates arrays of WKSPointZs and attributes, and optional arrays of 0-based file indices and 1-based point IDs.'
##        #return pPointCount, pPoints, pAttribute
##
##    def NextAttrLong(self, arraySize, pIntensity, pFileIndices, pPointIDs):
##        u'Populates arrays of WKSPointZs and attributes, and optional arrays of 0-based file indices and 1-based point IDs.'
##        #return pPointCount, pPoints, pAttribute
##
##    def NextLasInfo(self, pInfo):
##        u'Populates an array of ILasPointInfo.'
##        #return pPointCount
##
##    def _get(self):
##        u'The LAS attribute.'
##        #return pAttribute
##    def _set(self, pAttribute):
##        u'The LAS attribute.'
##    Attribute = property(_get, _set, doc = _set.__doc__)
##
##    def Next(self, arraySize, pIntensity, pFileIndices, pPointIDs):
##        u'Populates an array of WKSPointZs, optional arrays of 0-based file indices and 1-based point IDs.'
##        #return pPointCount, pPoints
##
##    def NextAttrRGB32(self, arraySize, pIntensity, pFileIndices, pPointIDs):
##        u'Populates arrays of WKSPointZs and RGB colors, and optional arrays of 0-based file indices and 1-based point IDs.'
##        #return pPointCount, pPoints, pAttribute
##

class ISimpleStatistics(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to Statistics.'
    _iid_ = GUID('{CF4000EC-9418-4DA3-9C2D-931ACE25889C}')
    _idlflags_ = ['oleautomation']
ISimpleStatistics._methods_ = [
    COMMETHOD(['propget', helpstring(u'Returns data type (defined by VARIANT::vt)')], HRESULT, 'DataType',
              ( ['retval', 'out'], POINTER(VARIANT), 'pType' )),
    COMMETHOD(['propget', helpstring(u'The number of elements.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_double), 'pCount' )),
    COMMETHOD(['propget', helpstring(u'The minimum value.')], HRESULT, 'Minimum',
              ( ['retval', 'out'], POINTER(c_double), 'pMinimum' )),
    COMMETHOD(['propget', helpstring(u'The maximum value.')], HRESULT, 'Maximum',
              ( ['retval', 'out'], POINTER(c_double), 'pMaximum' )),
    COMMETHOD(['propget', helpstring(u'The mean value.')], HRESULT, 'Mean',
              ( ['retval', 'out'], POINTER(c_double), 'pMean' )),
    COMMETHOD(['propget', helpstring(u'The standard deviation.')], HRESULT, 'StandardDeviation',
              ( ['retval', 'out'], POINTER(c_double), 'pStandardDeviation' )),
]
################################################################
## code template for ISimpleStatistics implementation
##class ISimpleStatistics_Impl(object):
##    @property
##    def Count(self):
##        u'The number of elements.'
##        #return pCount
##
##    @property
##    def DataType(self):
##        u'Returns data type (defined by VARIANT::vt)'
##        #return pType
##
##    @property
##    def StandardDeviation(self):
##        u'The standard deviation.'
##        #return pStandardDeviation
##
##    @property
##    def Maximum(self):
##        u'The maximum value.'
##        #return pMaximum
##
##    @property
##    def Minimum(self):
##        u'The minimum value.'
##        #return pMinimum
##
##    @property
##    def Mean(self):
##        u'The mean value.'
##        #return pMean
##

class IConstructionPoints(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manipulate the construction points for the parcel.'
    _iid_ = GUID('{ADC3412A-6EF7-41AC-BDC2-23E911C31280}')
    _idlflags_ = ['oleautomation']
IConstructionPoints._methods_ = [
    COMMETHOD(['propget', helpstring(u'The number of point constructions for the parcel.')], HRESULT, 'ConstructionPointCount',
              ( ['retval', 'out'], POINTER(c_int), 'pCount' )),
    COMMETHOD([helpstring(u'Retrieves the construction point at the given index. Coordinates are in meters.')], HRESULT, 'GetConstructionPoint',
              ( ['in'], c_int, 'i' ),
              ( ['in', 'out'], POINTER(c_int), 'pUnjoinedPointNo' ),
              ( ['in', 'out'], POINTER(c_double), 'pX' ),
              ( ['in', 'out'], POINTER(c_double), 'pY' )),
    COMMETHOD([helpstring(u'Adds a construction point to the parcel construction data. Coordinates are in meters.')], HRESULT, 'AddConstructionPoint',
              ( ['in'], c_int, 'UnjoinedPointNo' ),
              ( ['in'], c_double, 'x' ),
              ( ['in'], c_double, 'y' )),
    COMMETHOD([helpstring(u'The construction point with the matching point No. Coordinates are in meters.')], HRESULT, 'FindConstructionPoint',
              ( ['in'], c_int, 'UnjoinedPointNo' ),
              ( ['in', 'out'], POINTER(c_double), 'x' ),
              ( ['in', 'out'], POINTER(c_double), 'y' )),
    COMMETHOD([helpstring(u'Remove the construction point.')], HRESULT, 'RemoveConstructionPoint',
              ( ['in'], c_int, 'UnjoinedPointNo' )),
    COMMETHOD([helpstring(u'Clears the construction points.')], HRESULT, 'ClearConstructionPoints'),
]
################################################################
## code template for IConstructionPoints implementation
##class IConstructionPoints_Impl(object):
##    def FindConstructionPoint(self, UnjoinedPointNo):
##        u'The construction point with the matching point No. Coordinates are in meters.'
##        #return x, y
##
##    def GetConstructionPoint(self, i):
##        u'Retrieves the construction point at the given index. Coordinates are in meters.'
##        #return pUnjoinedPointNo, pX, pY
##
##    def RemoveConstructionPoint(self, UnjoinedPointNo):
##        u'Remove the construction point.'
##        #return 
##
##    def ClearConstructionPoints(self):
##        u'Clears the construction points.'
##        #return 
##
##    def AddConstructionPoint(self, UnjoinedPointNo, x, y):
##        u'Adds a construction point to the parcel construction data. Coordinates are in meters.'
##        #return 
##
##    @property
##    def ConstructionPointCount(self):
##        u'The number of point constructions for the parcel.'
##        #return pCount
##


# values for enumeration 'esriCadastralLineParameters'
esriCadastralLPBearingAndDistance = 0
esriCadastralLPAngleAndDistance = 1
esriCadastralLPChordBearingAndDeltaAndRadius = 2
esriCadastralLPDeltaAndRadius = 3
esriCadastralLPChordBearingAndChordLengthAndRadius = 4
esriCadastralLPChordLengthAndRadius = 5
esriCadastralLPChordBearingAndArcLengthAndRadius = 6
esriCadastralLPArcLengthAndRadius = 7
esriCadastralLPChordBearingAndDeltaAndArcLength = 8
esriCadastralLPDeltaAndArcLength = 9
esriCadastralLPRadialBearingAndDeltaAndRadius = 10
esriCadastralLPRadialBearingAndChordLengthAndRadius = 11
esriCadastralLPRadialBearingAndArcLengthAndRadius = 12
esriCadastralLPRadialBearingAndDeltaAndArcLength = 13
esriCadastralLPTangentBearingAndDeltaAndRadius = 14
esriCadastralLPTangentBearingAndChordLengthAndRadius = 15
esriCadastralLPTangentBearingAndArcLengthAndRadius = 16
esriCadastralLPTangentBearingAndDeltaAndArcLength = 17
esriCadastralLineParameters = c_int # enum

# values for enumeration 'esriLasClassFlag'
esriLasClassFlagNone = 1
esriLasClassFlagSynthetic = 2
esriLasClassFlagKey = 4
esriLasClassFlagWithheld = 8
esriLasClassFlag = c_int # enum
class ILasReturnStatistics(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to LasReturnStatistics object.'
    _iid_ = GUID('{15080791-5B91-4F28-9931-1FFE7E7DB33E}')
    _idlflags_ = ['oleautomation']
ILasStatistics._methods_ = [
    COMMETHOD(['propget', helpstring(u'The number of withheld points.')], HRESULT, 'WithheldPointCount',
              ( ['retval', 'out'], POINTER(c_double), 'pCount' )),
    COMMETHOD(['propget', helpstring(u'The XYZ extent of withheld points.')], HRESULT, 'WithheldExtent',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'ppExt' )),
    COMMETHOD([helpstring(u'Get statistics of the specified LAS attribute.')], HRESULT, 'GetAttributeStatistics',
              ( ['in'], esriLasAttributeType, 'Attribute' ),
              ( ['retval', 'out'], POINTER(POINTER(ISimpleStatistics)), 'ppStatistics' )),
    COMMETHOD([helpstring(u'Get unique returns (as esriTerrainLasReturnType).')], HRESULT, 'GetUniqueReturns',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray)), 'ppReturns' )),
    COMMETHOD([helpstring(u'Get unique class codes.')], HRESULT, 'GetUniqueClassCodes',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray)), 'ppCodes' )),
    COMMETHOD([helpstring(u'Get statistics associated with the specified return type.')], HRESULT, 'GetReturnStatistics',
              ( ['in'], esriTerrainLasReturnType, 'Type' ),
              ( ['retval', 'out'], POINTER(POINTER(ILasReturnStatistics)), 'ppStatistics' )),
    COMMETHOD([helpstring(u'Get statistics associated with the specified class code.')], HRESULT, 'GetClassCodeStatistics',
              ( ['in'], c_int, 'ClassCode' ),
              ( ['retval', 'out'], POINTER(POINTER(ILasClassCodeStatistics)), 'ppStatistics' )),
]
################################################################
## code template for ILasStatistics implementation
##class ILasStatistics_Impl(object):
##    @property
##    def WithheldPointCount(self):
##        u'The number of withheld points.'
##        #return pCount
##
##    def GetReturnStatistics(self, Type):
##        u'Get statistics associated with the specified return type.'
##        #return ppStatistics
##
##    @property
##    def WithheldExtent(self):
##        u'The XYZ extent of withheld points.'
##        #return ppExt
##
##    def GetClassCodeStatistics(self, ClassCode):
##        u'Get statistics associated with the specified class code.'
##        #return ppStatistics
##
##    def GetUniqueReturns(self):
##        u'Get unique returns (as esriTerrainLasReturnType).'
##        #return ppReturns
##
##    def GetAttributeStatistics(self, Attribute):
##        u'Get statistics of the specified LAS attribute.'
##        #return ppStatistics
##
##    def GetUniqueClassCodes(self):
##        u'Get unique class codes.'
##        #return ppCodes
##

IDECadastralFabricType._methods_ = [
]
################################################################
## code template for IDECadastralFabricType implementation
##class IDECadastralFabricType_Impl(object):

class DECadastralFabric(CoClass):
    u'Cadastral Fabric Data Element object.'
    _reg_clsid_ = GUID('{B0F868C0-BFBC-4669-B263-CD348D65D7AE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
DECadastralFabric._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEDataset, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEGeoDataset, IDECadastralFabric, IDECadastralFabric2, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElement, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPValue, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDescribe, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

class LasDataset(CoClass):
    u'Esri LasDataset component.'
    _reg_clsid_ = GUID('{711E7D01-2A82-4B7F-8D77-061C51BAF8DD}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
class ILasDatasetEdit(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of LasDataset.'
    _iid_ = GUID('{CA6228E2-EB8F-442F-88CB-5E40233E88E8}')
    _idlflags_ = ['oleautomation']
LasDataset._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataset, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDatasetSchemaEdit, ILasDataset, ILasDataset2, ILasDatasetEdit, ILasPointEdit, ILasPointCloud]

class ITemporalObservationsTable2(ITemporalObservationsTable):
    _case_insensitive_ = True
    u'Provides access to the Track ID.'
    _iid_ = GUID('{AEC7A38A-F684-40FC-B2F2-96000EBF22D8}')
    _idlflags_ = ['oleautomation']
ITemporalObservationsTable2._methods_ = [
    COMMETHOD(['hidden', helpstring(u'Receives the column index of the Track ID.'), 'propput'], HRESULT, 'TrackingColumnIndex',
              ( ['in'], c_int, 'rhs' )),
]
################################################################
## code template for ITemporalObservationsTable2 implementation
##class ITemporalObservationsTable2_Impl(object):
##    def _set(self, rhs):
##        u'Receives the column index of the Track ID.'
##    TrackingColumnIndex = property(fset = _set, doc = _set.__doc__)
##

class ICadastralFabricLocks2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to additional members that assign object locks for a cadastral job.'
    _iid_ = GUID('{882005E1-945F-46EB-80C8-2B7A3B0AFD4A}')
    _idlflags_ = ['oleautomation']
ICadastralFabricLocks2._methods_ = [
    COMMETHOD([helpstring(u'Acquire locks on the LockingJob. TakeSoftLocks allows locks to be transferred from other jobs in the same version.')], HRESULT, 'AcquireLocks',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray), 'pLocks' ),
              ( ['in'], VARIANT_BOOL, 'TakeSoftLocks' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray), 'pLocksInConflict' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray), 'pSoftLocksInConflict' )),
]
################################################################
## code template for ICadastralFabricLocks2 implementation
##class ICadastralFabricLocks2_Impl(object):
##    def AcquireLocks(self, pLocks, TakeSoftLocks, pLocksInConflict, pSoftLocksInConflict):
##        u'Acquire locks on the LockingJob. TakeSoftLocks allows locks to be transferred from other jobs in the same version.'
##        #return 
##


# values for enumeration 'esriCadastralRegeneratorSetting'
esriCadastralRegenRegenerateGeometries = 1
esriCadastralRegenRegenerateMissingRadials = 2
esriCadastralRegenRegenerateMissingPoints = 4
esriCadastralRegenRemoveOrphanPoints = 8
esriCadastralRegenRemoveInvalidLinePoints = 16
esriCadastralRegenSnapLinePoints = 32
esriCadastralRegenRepairLineSequencing = 64
esriCadastralRegeneratorSetting = c_int # enum
ICadastralJob._methods_ = [
    COMMETHOD(['propget', helpstring(u'The ObjectID of the Cadastral Job.')], HRESULT, 'ID',
              ( ['retval', 'out'], POINTER(c_int), 'JobID' )),
    COMMETHOD(['propget', helpstring(u'The cadastral job description.')], HRESULT, 'Description',
              ( ['retval', 'out'], POINTER(BSTR), 'Description' )),
    COMMETHOD(['propput', helpstring(u'The cadastral job description.')], HRESULT, 'Description',
              ( ['in'], BSTR, 'Description' )),
    COMMETHOD(['propget', helpstring(u'The cadastral job name.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propput', helpstring(u'The cadastral job name.')], HRESULT, 'Name',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD(['propget', helpstring(u'The cadastral job status.')], HRESULT, 'Status',
              ( ['retval', 'out'], POINTER(c_int), 'Status' )),
    COMMETHOD(['propput', helpstring(u'The cadastral job status.')], HRESULT, 'Status',
              ( ['in'], c_int, 'Status' )),
    COMMETHOD(['propget', helpstring(u'The owner of the cadastral job.')], HRESULT, 'Owner',
              ( ['retval', 'out'], POINTER(BSTR), 'Owner' )),
    COMMETHOD(['propput', helpstring(u'The owner of the cadastral job.')], HRESULT, 'Owner',
              ( ['in'], BSTR, 'Owner' )),
    COMMETHOD(['propget', helpstring(u'The value of an extended attribute.')], HRESULT, 'ExtendedAttribute',
              ( ['in'], c_int, 'fieldPosition' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'Value' )),
    COMMETHOD(['propput', helpstring(u'The value of an extended attribute.')], HRESULT, 'ExtendedAttribute',
              ( ['in'], c_int, 'fieldPosition' ),
              ( ['in'], VARIANT, 'Value' )),
    COMMETHOD(['propget', helpstring(u'The start date for the cadastral job.')], HRESULT, 'StartDate',
              ( ['retval', 'out'], POINTER(BSTR), 'Date' )),
    COMMETHOD(['propget', helpstring(u'The date the cadastral job was last modified.')], HRESULT, 'ModifiedDate',
              ( ['retval', 'out'], POINTER(BSTR), 'Date' )),
    COMMETHOD(['propget', helpstring(u'The date the cadastral job was committed.')], HRESULT, 'CommitDate',
              ( ['retval', 'out'], POINTER(BSTR), 'Date' )),
    COMMETHOD(['propget', helpstring(u'Edit parcels for the cadastral job.')], HRESULT, 'EditParcels',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFIDSet)), 'EditParcelIDs' )),
    COMMETHOD(['propput', helpstring(u'Edit parcels for the cadastral job.')], HRESULT, 'EditParcels',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFIDSet), 'EditParcelIDs' )),
    COMMETHOD(['propget', helpstring(u'All parcels for the complete area of the job.')], HRESULT, 'AdjustmentAreaParcels',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFIDSet)), 'AdjustmentAreaParcelIDs' )),
    COMMETHOD(['propput', helpstring(u'All parcels for the complete area of the job.')], HRESULT, 'AdjustmentAreaParcels',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFIDSet), 'AdjustmentAreaParcelIDs' )),
    COMMETHOD(['propget', helpstring(u'The control points for the cadastral job.')], HRESULT, 'ControlPoints',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFIDSet)), 'ControlPointslIDs' )),
    COMMETHOD(['propput', helpstring(u'The control points for the cadastral job.')], HRESULT, 'ControlPoints',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFIDSet), 'ControlPointslIDs' )),
    COMMETHOD([helpstring(u'Adds an edit parcel to the job.')], HRESULT, 'AddEditParcel',
              ( ['in'], c_int, 'ParcelID' )),
    COMMETHOD([helpstring(u'Removes a parcel from the job.')], HRESULT, 'RemoveEditParcel',
              ( ['in'], c_int, 'ParcelID' )),
    COMMETHOD([helpstring(u'Adds a control point to the job.')], HRESULT, 'AddControlPoint',
              ( ['in'], c_int, 'PointID' )),
    COMMETHOD([helpstring(u'Removes a control point from the job.')], HRESULT, 'RemoveControlPoint',
              ( ['in'], c_int, 'PointID' )),
    COMMETHOD(['propget', helpstring(u'All the parcels participating in the cadastral job.')], HRESULT, 'JobParcels',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFIDSet)), 'ppParcelIDSet' )),
]
################################################################
## code template for ICadastralJob implementation
##class ICadastralJob_Impl(object):
##    def _get(self):
##        u'The cadastral job status.'
##        #return Status
##    def _set(self, Status):
##        u'The cadastral job status.'
##    Status = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def StartDate(self):
##        u'The start date for the cadastral job.'
##        #return Date
##
##    def AddEditParcel(self, ParcelID):
##        u'Adds an edit parcel to the job.'
##        #return 
##
##    def _get(self):
##        u'The cadastral job name.'
##        #return Name
##    def _set(self, Name):
##        u'The cadastral job name.'
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'All parcels for the complete area of the job.'
##        #return AdjustmentAreaParcelIDs
##    def _set(self, AdjustmentAreaParcelIDs):
##        u'All parcels for the complete area of the job.'
##    AdjustmentAreaParcels = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self, fieldPosition):
##        u'The value of an extended attribute.'
##        #return Value
##    def _set(self, fieldPosition, Value):
##        u'The value of an extended attribute.'
##    ExtendedAttribute = property(_get, _set, doc = _set.__doc__)
##
##    def RemoveEditParcel(self, ParcelID):
##        u'Removes a parcel from the job.'
##        #return 
##
##    def AddControlPoint(self, PointID):
##        u'Adds a control point to the job.'
##        #return 
##
##    @property
##    def CommitDate(self):
##        u'The date the cadastral job was committed.'
##        #return Date
##
##    def RemoveControlPoint(self, PointID):
##        u'Removes a control point from the job.'
##        #return 
##
##    @property
##    def ModifiedDate(self):
##        u'The date the cadastral job was last modified.'
##        #return Date
##
##    def _get(self):
##        u'Edit parcels for the cadastral job.'
##        #return EditParcelIDs
##    def _set(self, EditParcelIDs):
##        u'Edit parcels for the cadastral job.'
##    EditParcels = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def JobParcels(self):
##        u'All the parcels participating in the cadastral job.'
##        #return ppParcelIDSet
##
##    def _get(self):
##        u'The owner of the cadastral job.'
##        #return Owner
##    def _set(self, Owner):
##        u'The owner of the cadastral job.'
##    Owner = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The control points for the cadastral job.'
##        #return ControlPointslIDs
##    def _set(self, ControlPointslIDs):
##        u'The control points for the cadastral job.'
##    ControlPoints = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def ID(self):
##        u'The ObjectID of the Cadastral Job.'
##        #return JobID
##
##    def _get(self):
##        u'The cadastral job description.'
##        #return Description
##    def _set(self, Description):
##        u'The cadastral job description.'
##    Description = property(_get, _set, doc = _set.__doc__)
##

class TerrainPyramidLevelWindowSize(CoClass):
    _reg_clsid_ = GUID('{47724AFE-3FB9-4FC3-B96B-55F56EF9DEDE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
TerrainPyramidLevelWindowSize._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ITerrainPyramidLevel]

ICadastralFabricRegeneration._methods_ = [
    COMMETHOD(['propputref', helpstring(u'Store the Cadastral Fabric which is to be regenerated')], HRESULT, 'CadastralFabric',
              ( ['in'], POINTER(ICadastralFabric), 'ppCadastralFabric' )),
    COMMETHOD(['propget', helpstring(u'Store the Cadastral Fabric which is to be regenerated')], HRESULT, 'CadastralFabric',
              ( ['retval', 'out'], POINTER(POINTER(ICadastralFabric)), 'ppCadastralFabric' )),
    COMMETHOD(['propput', helpstring(u'Store the bitmask defining which operations are to be performed by the regenerator')], HRESULT, 'RegeneratorBitmask',
              ( ['in'], c_int, 'pRegeneratorBitmask' )),
    COMMETHOD(['propget', helpstring(u'Store the bitmask defining which operations are to be performed by the regenerator')], HRESULT, 'RegeneratorBitmask',
              ( ['retval', 'out'], POINTER(c_int), 'pRegeneratorBitmask' )),
    COMMETHOD([helpstring(u'Regenerate the geometries of parcels, lines and linepoints associated with the input parcel ID set.')], HRESULT, 'RegenerateParcels',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFIDSet), 'pParcelsToRegenerate' ),
              ( ['in'], VARIANT_BOOL, 'regeneratePoints' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' )),
    COMMETHOD([helpstring(u'Regenerate the geometries of all parcels, lines and linepoints in the fabric.')], HRESULT, 'RegenerateAllParcels',
              ( ['in'], VARIANT_BOOL, 'regeneratePoints' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' )),
    COMMETHOD([helpstring(u'Regenerate the geometries associated with the input control point ID set.')], HRESULT, 'RegenerateControlPoints',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFIDSet), 'pControlPointsToRegenerate' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' )),
    COMMETHOD([helpstring(u'Regenerate the geometries of all control points in the fabric.')], HRESULT, 'RegenerateAllControlPoints',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' )),
    COMMETHOD([helpstring(u'Regenerate the geometries of the entire fabric.')], HRESULT, 'RegenerateEntireFabric',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' )),
    COMMETHOD([helpstring(u'Regenerate point features which have been removed from the database.')], HRESULT, 'RegenerateMissingPoints',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' )),
]
################################################################
## code template for ICadastralFabricRegeneration implementation
##class ICadastralFabricRegeneration_Impl(object):
##    @property
##    def CadastralFabric(self, ppCadastralFabric):
##        u'Store the Cadastral Fabric which is to be regenerated'
##        #return 
##
##    def _get(self):
##        u'Store the bitmask defining which operations are to be performed by the regenerator'
##        #return pRegeneratorBitmask
##    def _set(self, pRegeneratorBitmask):
##        u'Store the bitmask defining which operations are to be performed by the regenerator'
##    RegeneratorBitmask = property(_get, _set, doc = _set.__doc__)
##
##    def RegenerateControlPoints(self, pControlPointsToRegenerate, pTrackCancel):
##        u'Regenerate the geometries associated with the input control point ID set.'
##        #return 
##
##    def RegenerateAllParcels(self, regeneratePoints, pTrackCancel):
##        u'Regenerate the geometries of all parcels, lines and linepoints in the fabric.'
##        #return 
##
##    def RegenerateEntireFabric(self, pTrackCancel):
##        u'Regenerate the geometries of the entire fabric.'
##        #return 
##
##    def RegenerateMissingPoints(self, pTrackCancel):
##        u'Regenerate point features which have been removed from the database.'
##        #return 
##
##    def RegenerateAllControlPoints(self, pTrackCancel):
##        u'Regenerate the geometries of all control points in the fabric.'
##        #return 
##
##    def RegenerateParcels(self, pParcelsToRegenerate, regeneratePoints, pTrackCancel):
##        u'Regenerate the geometries of parcels, lines and linepoints associated with the input parcel ID set.'
##        #return 
##

class Library(object):
    u'Esri GeoDatabaseExtensions Object Library 10.2'
    name = u'esriGeoDatabaseExtensions'
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)

class LasPointInfo(CoClass):
    u'Esri LAS point info object.'
    _reg_clsid_ = GUID('{FD112EB0-4A24-4135-AD29-98EC25E37821}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
LasPointInfo._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ILasPointInfo]

ITerrainEditEvents._methods_ = [
    COMMETHOD([helpstring(u'This event is fired when Build is called on a Terrain.')], HRESULT, 'OnBuild',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'pExtent' )),
    COMMETHOD([helpstring(u'This event is fired when Undo Build is called on a Terrain.')], HRESULT, 'OnUndoBuild',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'pExtent' )),
    COMMETHOD([helpstring(u'This event is fired when Redo Build is called on a Terrain.')], HRESULT, 'OnRedoBuild',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'pExtent' )),
    COMMETHOD([helpstring(u'This event is fired when Reconcile is called on a Terrain.')], HRESULT, 'OnReconcile'),
    COMMETHOD([helpstring(u'This event is fired when Undo Reconcile is called on a Terrain.')], HRESULT, 'OnUndoReconcile'),
    COMMETHOD([helpstring(u'This event is fired when Redo Reconcile is called on a Terrain.')], HRESULT, 'OnRedoReconcile'),
]
################################################################
## code template for ITerrainEditEvents implementation
##class ITerrainEditEvents_Impl(object):
##    def OnRedoReconcile(self):
##        u'This event is fired when Redo Reconcile is called on a Terrain.'
##        #return 
##
##    def OnUndoReconcile(self):
##        u'This event is fired when Undo Reconcile is called on a Terrain.'
##        #return 
##
##    def OnReconcile(self):
##        u'This event is fired when Reconcile is called on a Terrain.'
##        #return 
##
##    def OnUndoBuild(self, pExtent):
##        u'This event is fired when Undo Build is called on a Terrain.'
##        #return 
##
##    def OnBuild(self, pExtent):
##        u'This event is fired when Build is called on a Terrain.'
##        #return 
##
##    def OnRedoBuild(self, pExtent):
##        u'This event is fired when Redo Build is called on a Terrain.'
##        #return 
##

class IConstructionParentParcels(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the parent parcels of a parcel construction.'
    _iid_ = GUID('{B6A52380-87E2-4628-9EBD-771C0BDACF23}')
    _idlflags_ = ['oleautomation']
IConstructionParentParcels._methods_ = [
    COMMETHOD(['propget', helpstring(u'The number of parent parcels.')], HRESULT, 'ParentParcelCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD([helpstring(u'The parent parcelNo at the given index.')], HRESULT, 'GetParentParcel',
              ( ['in'], c_int, 'i' ),
              ( ['in', 'out'], POINTER(c_int), 'ParcelNo' )),
    COMMETHOD([helpstring(u'Add a parent parcelNo for the construction.')], HRESULT, 'AddParentParcel',
              ( ['in'], c_int, 'ParcelNo' )),
    COMMETHOD([helpstring(u'Remove parent parcel from construction data.')], HRESULT, 'RemoveParentParcel',
              ( ['in'], c_int, 'ParcelNo' )),
    COMMETHOD([helpstring(u'Clear the parent parcel numbers.')], HRESULT, 'ClearParentParcels'),
]
################################################################
## code template for IConstructionParentParcels implementation
##class IConstructionParentParcels_Impl(object):
##    def GetParentParcel(self, i):
##        u'The parent parcelNo at the given index.'
##        #return ParcelNo
##
##    @property
##    def ParentParcelCount(self):
##        u'The number of parent parcels.'
##        #return Count
##
##    def ClearParentParcels(self):
##        u'Clear the parent parcel numbers.'
##        #return 
##
##    def AddParentParcel(self, ParcelNo):
##        u'Add a parent parcelNo for the construction.'
##        #return 
##
##    def RemoveParentParcel(self, ParcelNo):
##        u'Remove parent parcel from construction data.'
##        #return 
##

ITerrainEdit._methods_ = [
    COMMETHOD([helpstring(u'Adds a reference to a feature class.')], HRESULT, 'AddDataSource',
              ( ['in'], POINTER(ITerrainDataSource), 'pDataSource' )),
    COMMETHOD([helpstring(u'Removes reference to a participating feature class.')], HRESULT, 'RemoveDataSource',
              ( ['in'], c_int, 'index' )),
    COMMETHOD([helpstring(u'Adds a pyramid level.')], HRESULT, 'AddPyramidLevel',
              ( ['in'], POINTER(ITerrainPyramidLevel), 'pPyramidLevel' )),
    COMMETHOD([helpstring(u'Removes a pyramid level.')], HRESULT, 'RemovePyramidLevel',
              ( ['in'], c_int, 'index' )),
    COMMETHOD([helpstring(u'Modifies the largest display scale used for a particular level of a terrain pyramid.')], HRESULT, 'ChangeMaxScale',
              ( ['in'], c_int, 'index' ),
              ( ['in'], c_int, 'newScale' )),
    COMMETHOD([helpstring(u'Change the resolution bounds of a data source.')], HRESULT, 'ChangeResolutionBounds',
              ( ['in'], c_int, 'index' ),
              ( ['in'], c_double, 'lowerBound' ),
              ( ['in'], c_double, 'upperBound' )),
    COMMETHOD([helpstring(u'Removes measurements from a terrain data source (feature class).')], HRESULT, 'DeleteDataSourceData',
              ( ['in'], c_int, 'index' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'pAOI' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' )),
    COMMETHOD([helpstring(u'Appends measurements to a terrain data source (feature class).')], HRESULT, 'AddDataSourceData',
              ( ['in'], c_int, 'index' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'pAOI' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'pInFC' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' )),
    COMMETHOD([helpstring(u'Replaces measurements from a terrain data source (feature class) with measurements in another feature class.')], HRESULT, 'ReplaceDataSourceData',
              ( ['in'], c_int, 'index' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'pAOI' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'pInFC' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' )),
    COMMETHOD([helpstring(u'Constructs the terrain.')], HRESULT, 'Build',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' )),
]
################################################################
## code template for ITerrainEdit implementation
##class ITerrainEdit_Impl(object):
##    def ChangeMaxScale(self, index, newScale):
##        u'Modifies the largest display scale used for a particular level of a terrain pyramid.'
##        #return 
##
##    def RemoveDataSource(self, index):
##        u'Removes reference to a participating feature class.'
##        #return 
##
##    def AddDataSource(self, pDataSource):
##        u'Adds a reference to a feature class.'
##        #return 
##
##    def RemovePyramidLevel(self, index):
##        u'Removes a pyramid level.'
##        #return 
##
##    def ReplaceDataSourceData(self, index, pAOI, pInFC, pTrackCancel):
##        u'Replaces measurements from a terrain data source (feature class) with measurements in another feature class.'
##        #return 
##
##    def ChangeResolutionBounds(self, index, lowerBound, upperBound):
##        u'Change the resolution bounds of a data source.'
##        #return 
##
##    def AddPyramidLevel(self, pPyramidLevel):
##        u'Adds a pyramid level.'
##        #return 
##
##    def Build(self, pTrackCancel):
##        u'Constructs the terrain.'
##        #return 
##
##    def DeleteDataSourceData(self, index, pAOI, pTrackCancel):
##        u'Removes measurements from a terrain data source (feature class).'
##        #return 
##
##    def AddDataSourceData(self, index, pAOI, pInFC, pTrackCancel):
##        u'Appends measurements to a terrain data source (feature class).'
##        #return 
##

class LasDatasetWorkspaceFactory(CoClass):
    u'Esri LasDataset workspace-factory component.'
    _reg_clsid_ = GUID('{7AB01D9A-FDFE-4DFB-9209-86603EE9AEC6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
LasDatasetWorkspaceFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceFactory, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceFactory2]

ILasSurface._methods_ = [
    COMMETHOD([helpstring(u'Export to TIN.')], HRESULT, 'AsTin',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( ['in'], POINTER(ILasFilter), 'pFilter' ),
              ( ['in'], c_double, 'Resolution' ),
              ( ['in'], esriTinPointSelectionMethod, 'Method' ),
              ( ['in'], c_double, 'ZFactor' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITin)), 'ppTin' )),
    COMMETHOD([helpstring(u'Export to Raster.')], HRESULT, 'AsRaster',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( ['in'], POINTER(ILasFilter), 'pFilter' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRasterDataset), 'pDataset' ),
              ( ['in'], esriPointToRasterMethod, 'Method' ),
              ( ['in'], esriLasZSource, 'zSource' ),
              ( ['in'], esriPointToRasterVoidFillMethod, 'fillMethod' ),
              ( ['in'], comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriSurfaceInterpolationType, 'Type' ),
              ( ['in'], c_double, 'ZFactor' )),
    COMMETHOD([helpstring(u'Export to Raster through triangulation.')], HRESULT, 'InterpolateRaster',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( ['in'], POINTER(ILasFilter), 'pLasFilter' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRasterDataset), 'pDataset' ),
              ( ['in'], c_double, 'Resolution' ),
              ( ['in'], esriTinPointSelectionMethod, 'Method' ),
              ( ['in'], comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriSurfaceInterpolationType, 'Type' ),
              ( ['in'], c_double, 'ZFactor' )),
    COMMETHOD([helpstring(u'Interpolate feature class.')], HRESULT, 'InterpolateFeatureClass',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( ['in'], POINTER(ILasFilter), 'pLasFilter' ),
              ( ['in'], c_double, 'Resolution' ),
              ( ['in'], esriTinPointSelectionMethod, 'Method' ),
              ( ['in'], comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriSurfaceInterpolationType, 'Type' ),
              ( ['in'], c_double, 'ZFactor' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'pInClass' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IQueryFilter), 'pQueryFilter' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'pOutClass' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'pStepSize' )),
    COMMETHOD([helpstring(u'Interpolate feature class (vertices only).')], HRESULT, 'InterpolateFeatureClassVertices',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( ['in'], POINTER(ILasFilter), 'pLasFilter' ),
              ( ['in'], c_double, 'Resolution' ),
              ( ['in'], esriTinPointSelectionMethod, 'Method' ),
              ( ['in'], comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriSurfaceInterpolationType, 'Type' ),
              ( ['in'], c_double, 'ZFactor' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'pInClass' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IQueryFilter), 'pQueryFilter' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'pOutClass' )),
    COMMETHOD(['propget', helpstring(u'Indicates if earth curvature can be applied.')], HRESULT, 'CanDoCurvature',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbCanDo' )),
    COMMETHOD([helpstring(u'Get line-of-sight.')], HRESULT, 'GetLineOfSightFeatureClass',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( ['in'], POINTER(ILasFilter), 'pLasFilter' ),
              ( ['in'], c_double, 'Resolution' ),
              ( ['in'], esriTinPointSelectionMethod, 'Method' ),
              ( ['in'], c_double, 'ZFactor' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'pInputLines' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IQueryFilter), 'pQueryFilter' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'pOutputLines' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'pObstructionPoints' ),
              ( ['in'], VARIANT_BOOL, 'bApplyCurvature' ),
              ( ['in'], VARIANT_BOOL, 'bApplyRefraction' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'pRefractionFactor' )),
]
################################################################
## code template for ILasSurface implementation
##class ILasSurface_Impl(object):
##    def InterpolateFeatureClass(self, pTrackCancel, pLasFilter, Resolution, Method, Type, ZFactor, pInClass, pQueryFilter, pOutClass, pStepSize):
##        u'Interpolate feature class.'
##        #return 
##
##    def AsTin(self, pTrackCancel, pFilter, Resolution, Method, ZFactor):
##        u'Export to TIN.'
##        #return ppTin
##
##    def GetLineOfSightFeatureClass(self, pTrackCancel, pLasFilter, Resolution, Method, ZFactor, pInputLines, pQueryFilter, pOutputLines, pObstructionPoints, bApplyCurvature, bApplyRefraction, pRefractionFactor):
##        u'Get line-of-sight.'
##        #return 
##
##    def InterpolateRaster(self, pTrackCancel, pLasFilter, pDataset, Resolution, Method, Type, ZFactor):
##        u'Export to Raster through triangulation.'
##        #return 
##
##    def InterpolateFeatureClassVertices(self, pTrackCancel, pLasFilter, Resolution, Method, Type, ZFactor, pInClass, pQueryFilter, pOutClass):
##        u'Interpolate feature class (vertices only).'
##        #return 
##
##    @property
##    def CanDoCurvature(self):
##        u'Indicates if earth curvature can be applied.'
##        #return pbCanDo
##
##    def AsRaster(self, pTrackCancel, pFilter, pDataset, Method, zSource, fillMethod, Type, ZFactor):
##        u'Export to Raster.'
##        #return 
##

class IInternalTable(ITemporalTable):
    _case_insensitive_ = True
    _iid_ = GUID('{A677AB63-2FB8-11D5-B7E2-00010265ADC5}')
    _idlflags_ = ['oleautomation']
IInternalTable._methods_ = [
    COMMETHOD([helpstring(u'Adds a row to the temporal table.')], HRESULT, 'AddRow',
              ( ['in'], POINTER(IDataMessage), 'piDataMessage' ),
              ( ['retval', 'out'], POINTER(c_int), 'plRowID' )),
]
################################################################
## code template for IInternalTable implementation
##class IInternalTable_Impl(object):
##    def AddRow(self, piDataMessage):
##        u'Adds a row to the temporal table.'
##        #return plRowID
##

class _ITemporalFeatureClassEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to temporal feature class events.'
    _iid_ = GUID('{CC018A65-24FB-11D4-B34C-00104BA2ABCC}')
    _idlflags_ = []
_ITemporalFeatureClassEvents._methods_ = [
    COMMETHOD([helpstring(u'Event notification that feature class added data to storage and indicates the bounding rectangle of the addition.')], HRESULT, 'OnAddData',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'piEnvelope' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'piFeatureClass' )),
    COMMETHOD([helpstring(u'Event notification that a client feature source removed data from storage and indicates the bounding rectangle of the removal.')], HRESULT, 'OnRemoveData',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'piEnvelope' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'piFeatureClass' )),
]
################################################################
## code template for _ITemporalFeatureClassEvents implementation
##class _ITemporalFeatureClassEvents_Impl(object):
##    def OnAddData(self, piEnvelope, piFeatureClass):
##        u'Event notification that feature class added data to storage and indicates the bounding rectangle of the addition.'
##        #return 
##
##    def OnRemoveData(self, piEnvelope, piFeatureClass):
##        u'Event notification that a client feature source removed data from storage and indicates the bounding rectangle of the removal.'
##        #return 
##

class CadastralFabric(CoClass):
    u'A container for querying information about a cadastral fabric.'
    _reg_clsid_ = GUID('{8081CA69-9711-4CAF-BDD9-45DAAB4A4666}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
CadastralFabric._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IConnectionPointContainer, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataset, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset, ICadastralFabric, ICadastralFabric2, ICadastralFabric3, ICadastralFabricLocks, ICadastralFabricLocks2, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetComponent, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetEdit, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ISchemaLock, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IVersionedObject2, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, ICadastralFabricSchemaEdit, ICadastralFabricSchemaEdit2]

ITerrainPyramidLevel._methods_ = [
    COMMETHOD(['propget', helpstring(u'The pyramid type of this pyramid level associated with.')], HRESULT, 'PyramidType',
              ( ['retval', 'out'], POINTER(esriTerrainPyramidType), 'pType' )),
    COMMETHOD(['propput', helpstring(u'The resolution this pyramid level associated with.')], HRESULT, 'Resolution',
              ( ['in'], c_double, 'pResolution' )),
    COMMETHOD(['propget', helpstring(u'The resolution this pyramid level associated with.')], HRESULT, 'Resolution',
              ( ['retval', 'out'], POINTER(c_double), 'pResolution' )),
    COMMETHOD(['propput', helpstring(u'The maximum scale this pyramid level associated with.')], HRESULT, 'MaxScale',
              ( ['in'], c_int, 'pScale' )),
    COMMETHOD(['propget', helpstring(u'The maximum scale this pyramid level associated with.')], HRESULT, 'MaxScale',
              ( ['retval', 'out'], POINTER(c_int), 'pScale' )),
]
################################################################
## code template for ITerrainPyramidLevel implementation
##class ITerrainPyramidLevel_Impl(object):
##    def _get(self):
##        u'The maximum scale this pyramid level associated with.'
##        #return pScale
##    def _set(self, pScale):
##        u'The maximum scale this pyramid level associated with.'
##    MaxScale = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The resolution this pyramid level associated with.'
##        #return pResolution
##    def _set(self, pResolution):
##        u'The resolution this pyramid level associated with.'
##    Resolution = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def PyramidType(self):
##        u'The pyramid type of this pyramid level associated with.'
##        #return pType
##


# values for enumeration 'enumTemporalCursorType'
enumSelect = 0
enumSelect_OID = 1
enumCount = 2
enumUpdate = 3
enumInsert = 4
enumSearch = 5
enumTemporalCursorType = c_int # enum

# values for enumeration 'esriCadastralLinePointCategory'
esriCadastralLinePointStandard = 0
esriCadastralLinePointBreak = 1
esriCadastralLinePointCategory = c_int # enum
class LasHeaderInfo(CoClass):
    u'Esri LAS header info object.'
    _reg_clsid_ = GUID('{8463E10E-689A-45C1-B468-F660B5EC1DD1}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
LasHeaderInfo._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ILasHeaderInfo]

ITerrainEdit2._methods_ = [
    COMMETHOD([helpstring(u"Refresh terrain's extent.")], HRESULT, 'UpdateExtent',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' )),
]
################################################################
## code template for ITerrainEdit2 implementation
##class ITerrainEdit2_Impl(object):
##    def UpdateExtent(self, pTrackCancel):
##        u"Refresh terrain's extent."
##        #return 
##

ITerrainEdit3._methods_ = [
    COMMETHOD([helpstring(u'Change the ApplyToOverviewTerrain property of the specified data source.')], HRESULT, 'ChangeUsageInOverview',
              ( ['in'], c_int, 'index' ),
              ( ['in'], VARIANT_BOOL, 'bApply' )),
    COMMETHOD([helpstring(u'Removes measurements from a terrain data source (feature class).')], HRESULT, 'DeleteDataSourceDataByFC',
              ( ['in'], c_int, 'index' ),
              ( ['in'], BSTR, 'pointCountFieldName' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'pFC' ),
              ( ['in'], VARIANT_BOOL, 'bSparseData' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' )),
    COMMETHOD([helpstring(u'Removes measurements from a terrain data source (feature class).')], HRESULT, 'DeleteDataSourceData2',
              ( ['in'], c_int, 'index' ),
              ( ['in'], BSTR, 'pointCountFieldName' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'pAOI' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' )),
    COMMETHOD([helpstring(u'Appends measurements to terrain data source (feature class).')], HRESULT, 'AddDataSourceData2',
              ( ['in'], c_int, 'index' ),
              ( ['in'], BSTR, 'pointCountFieldName' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'pAOI' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'pInFC' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' )),
    COMMETHOD([helpstring(u'Replaces measurements from a terrain data source (feature class) with measurements in another feature class.')], HRESULT, 'ReplaceDataSourceData2',
              ( ['in'], c_int, 'index' ),
              ( ['in'], BSTR, 'pointCountFieldName' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'pAOI' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'pInFC' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' )),
    COMMETHOD([helpstring(u'Calculate Terrain blob field statistics of the specified embedded data source.')], HRESULT, 'CalculateFieldStatistics',
              ( ['in'], c_int, 'index' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray), 'pFieldNames' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' )),
]
################################################################
## code template for ITerrainEdit3 implementation
##class ITerrainEdit3_Impl(object):
##    def ReplaceDataSourceData2(self, index, pointCountFieldName, pAOI, pInFC, pTrackCancel):
##        u'Replaces measurements from a terrain data source (feature class) with measurements in another feature class.'
##        #return 
##
##    def DeleteDataSourceData2(self, index, pointCountFieldName, pAOI, pTrackCancel):
##        u'Removes measurements from a terrain data source (feature class).'
##        #return 
##
##    def ChangeUsageInOverview(self, index, bApply):
##        u'Change the ApplyToOverviewTerrain property of the specified data source.'
##        #return 
##
##    def DeleteDataSourceDataByFC(self, index, pointCountFieldName, pFC, bSparseData, pTrackCancel):
##        u'Removes measurements from a terrain data source (feature class).'
##        #return 
##
##    def CalculateFieldStatistics(self, index, pFieldNames, pTrackCancel):
##        u'Calculate Terrain blob field statistics of the specified embedded data source.'
##        #return 
##
##    def AddDataSourceData2(self, index, pointCountFieldName, pAOI, pInFC, pTrackCancel):
##        u'Appends measurements to terrain data source (feature class).'
##        #return 
##

class CadastralFabricFDExtension(CoClass):
    u"A container for describing this cadastral fabric's feature dataset extension properties."
    _reg_clsid_ = GUID('{0822E62D-8C8F-4483-8EB7-96DD0C343343}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
CadastralFabricFDExtension._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureDatasetExtension, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetContainer3, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetEdit]

class TerrainBlobReader(CoClass):
    u'Esri Terrain blob reader.'
    _reg_clsid_ = GUID('{564BBA1A-9F3A-40C5-B4BF-E8E534388944}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
TerrainBlobReader._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ITerrainBlobReader]

class LasDatasetToRasterFunction(CoClass):
    u'The LasDatasetToRasterFunction class.'
    _reg_clsid_ = GUID('{06A78A67-BA8A-4592-83E5-5DD4362F6636}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
LasDatasetToRasterFunction._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._8F0541A3_D5BE_4B3F_A8D9_062D5579E19B_0_10_2.IRasterFunction, comtypes.gen._8F0541A3_D5BE_4B3F_A8D9_062D5579E19B_0_10_2.IRasterFunction2, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLVersionSupport]

ILasReturnStatistics._methods_ = [
    COMMETHOD(['propget', helpstring(u'The return type associated with the statistics.')], HRESULT, 'ReturnType',
              ( ['retval', 'out'], POINTER(esriTerrainLasReturnType), 'pType' )),
    COMMETHOD(['propget', helpstring(u'The number of points associated with this return (excluding withheld points).')], HRESULT, 'PointCount',
              ( ['retval', 'out'], POINTER(c_double), 'pCount' )),
    COMMETHOD(['propget', helpstring(u'The number of Synthetic points associated with this return.')], HRESULT, 'SyntheticPointCount',
              ( ['retval', 'out'], POINTER(c_double), 'pCount' )),
    COMMETHOD(['propget', helpstring(u'The number of Key points associated with this return.')], HRESULT, 'KeyPointCount',
              ( ['retval', 'out'], POINTER(c_double), 'pCount' )),
    COMMETHOD(['propget', helpstring(u'The XYZ extent of points associated with this return (excluding withheld points).')], HRESULT, 'Extent',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'ppExt' )),
]
################################################################
## code template for ILasReturnStatistics implementation
##class ILasReturnStatistics_Impl(object):
##    @property
##    def ReturnType(self):
##        u'The return type associated with the statistics.'
##        #return pType
##
##    @property
##    def KeyPointCount(self):
##        u'The number of Key points associated with this return.'
##        #return pCount
##
##    @property
##    def PointCount(self):
##        u'The number of points associated with this return (excluding withheld points).'
##        #return pCount
##
##    @property
##    def Extent(self):
##        u'The XYZ extent of points associated with this return (excluding withheld points).'
##        #return ppExt
##
##    @property
##    def SyntheticPointCount(self):
##        u'The number of Synthetic points associated with this return.'
##        #return pCount
##

class IConstructionBasisOfBearing(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manipulate the basis of bearing setting for a parcel construction.'
    _iid_ = GUID('{2B82AC6E-AA06-43D8-AE70-7B200E07BE6B}')
    _idlflags_ = ['oleautomation']
IConstructionBasisOfBearing._methods_ = [
    COMMETHOD(['propget', helpstring(u'The basis of bearing offset angle.')], HRESULT, 'BasisOfBearingOffset',
              ( ['retval', 'out'], POINTER(c_double), 'angleOffset' )),
    COMMETHOD(['propput', helpstring(u'The basis of bearing offset angle.')], HRESULT, 'BasisOfBearingOffset',
              ( ['in'], c_double, 'angleOffset' )),
]
################################################################
## code template for IConstructionBasisOfBearing implementation
##class IConstructionBasisOfBearing_Impl(object):
##    def _get(self):
##        u'The basis of bearing offset angle.'
##        #return angleOffset
##    def _set(self, angleOffset):
##        u'The basis of bearing offset angle.'
##    BasisOfBearingOffset = property(_get, _set, doc = _set.__doc__)
##

ILasDatasetEdit._methods_ = [
    COMMETHOD([helpstring(u'Saves the changes.')], HRESULT, 'Save'),
    COMMETHOD(['propput', helpstring(u'Indicates if the dataset is saved with relative path.')], HRESULT, 'UsesRelativePath',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD([helpstring(u'Sets spatial reference.')], HRESULT, 'SetSpatialReference',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference), 'pSpatialReference' )),
    COMMETHOD([helpstring(u'Adds a file to the dataset.')], HRESULT, 'AddFile',
              ( ['in'], BSTR, 'fileName' )),
    COMMETHOD([helpstring(u'Adds all the files in the specified a folder, and potentially subfolders, to the dataset.')], HRESULT, 'AddFolder',
              ( ['in'], BSTR, 'folderName' ),
              ( ['in'], BSTR, 'fileExtension' ),
              ( ['in'], VARIANT_BOOL, 'bRecursive' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'ppBadFiles' )),
    COMMETHOD([helpstring(u'Removes the specified file from the dataset.')], HRESULT, 'RemoveFile',
              ( ['in'], c_int, 'index' )),
    COMMETHOD([helpstring(u'Removes the specified file from the dataset.')], HRESULT, 'RemoveFileByName',
              ( ['in'], BSTR, 'fileName' )),
    COMMETHOD([helpstring(u'Adds surface constraint (e.g., breaklines) to the dataset.')], HRESULT, 'AddSurfaceConstraint',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'pFeatureClass' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IField), 'pHeightField' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IField), 'pTagField' ),
              ( ['in'], comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriTinSurfaceType, 'Type' )),
    COMMETHOD([helpstring(u'Removes the specified surface constraint from the dataset.')], HRESULT, 'RemoveSurfaceConstraint',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'pFeatureClass' )),
    COMMETHOD([helpstring(u'Removes the specified surface constraint from the dataset.')], HRESULT, 'RemoveSurfaceConstraintByID',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID), 'pGuid' )),
    COMMETHOD([helpstring(u'Calculate statistics of the entire dataset.')], HRESULT, 'CalculateStatistics',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( ['in'], VARIANT_BOOL, 'bForce' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray)), 'ppBadFiles' )),
    COMMETHOD([helpstring(u'Calculate statistics of the specified file.')], HRESULT, 'CalculateFileStatistics',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( ['in'], c_int, 'index' )),
]
################################################################
## code template for ILasDatasetEdit implementation
##class ILasDatasetEdit_Impl(object):
##    def CalculateFileStatistics(self, pTrackCancel, index):
##        u'Calculate statistics of the specified file.'
##        #return 
##
##    def AddSurfaceConstraint(self, pFeatureClass, pHeightField, pTagField, Type):
##        u'Adds surface constraint (e.g., breaklines) to the dataset.'
##        #return 
##
##    def AddFolder(self, folderName, fileExtension, bRecursive):
##        u'Adds all the files in the specified a folder, and potentially subfolders, to the dataset.'
##        #return ppBadFiles
##
##    def _set(self, rhs):
##        u'Indicates if the dataset is saved with relative path.'
##    UsesRelativePath = property(fset = _set, doc = _set.__doc__)
##
##    def RemoveSurfaceConstraint(self, pFeatureClass):
##        u'Removes the specified surface constraint from the dataset.'
##        #return 
##
##    def AddFile(self, fileName):
##        u'Adds a file to the dataset.'
##        #return 
##
##    def RemoveFileByName(self, fileName):
##        u'Removes the specified file from the dataset.'
##        #return 
##
##    def SetSpatialReference(self, pSpatialReference):
##        u'Sets spatial reference.'
##        #return 
##
##    def RemoveFile(self, index):
##        u'Removes the specified file from the dataset.'
##        #return 
##
##    def RemoveSurfaceConstraintByID(self, pGuid):
##        u'Removes the specified surface constraint from the dataset.'
##        #return 
##
##    def Save(self):
##        u'Saves the changes.'
##        #return 
##
##    def CalculateStatistics(self, pTrackCancel, bForce):
##        u'Calculate statistics of the entire dataset.'
##        #return ppBadFiles
##

class LasReturnStatistics(CoClass):
    u'Esri LasReturnStatistics object.'
    _reg_clsid_ = GUID('{0135C452-608B-4831-9262-1C6C772F300E}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
LasReturnStatistics._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ILasReturnStatistics]

class ParcelConstructionData(CoClass):
    u'Esri Cadastral Fabric Parcel Construction Data Class.'
    _reg_clsid_ = GUID('{BCB1E8C9-1AA6-4012-AEAA-8FB4F62D85CB}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
ParcelConstructionData._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN, IParcelConstructionData, IConstructionParentParcels, IConstructionBreakPoints, IConstructionBasisOfBearing, IConstructionJoinLinks, IConstructionUnbuildableLines, IConstructionPoints, IConstructionAdjustment]

ICadastralFabricName._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The name of the feature dataset containing the cadastral fabric.')], HRESULT, 'FeatureDatasetName',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetName), 'Name' )),
    COMMETHOD(['propget', helpstring(u'The name of the feature dataset containing the cadastral fabric.')], HRESULT, 'FeatureDatasetName',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetName)), 'Name' )),
]
################################################################
## code template for ICadastralFabricName implementation
##class ICadastralFabricName_Impl(object):
##    @property
##    def FeatureDatasetName(self, Name):
##        u'The name of the feature dataset containing the cadastral fabric.'
##        #return 
##

class LasAttributeStatistics(CoClass):
    u'Esri LasAttributeStatistics object.'
    _reg_clsid_ = GUID('{CBEF81BA-43FD-4AE5-A235-7E69724BEE49}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7BA654FE-F55E-4EE5-8CF2-FAEFFBC04A61}', 10, 2)
LasAttributeStatistics._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ISimpleStatistics]

ICadastralTransformationData._methods_ = [
    COMMETHOD([helpstring(u'Add a featureClassID, adjustmentLevel pair.')], HRESULT, 'AddData',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName), 'Name' ),
              ( ['in'], c_int, 'adjustmentLevel' )),
    COMMETHOD([helpstring(u'Retrieve a featureClassName, adjustmentLevel pair.')], HRESULT, 'GetData',
              ( ['in'], c_int, 'index' ),
              ( ['in', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName)), 'Name' ),
              ( ['in', 'out'], POINTER(c_int), 'adjustmentLevel' )),
    COMMETHOD(['propget', helpstring(u'Retrieve the number of entries.')], HRESULT, 'TransDataCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD([helpstring(u'Clear all the data.')], HRESULT, 'Clear'),
]
################################################################
## code template for ICadastralTransformationData implementation
##class ICadastralTransformationData_Impl(object):
##    def Clear(self):
##        u'Clear all the data.'
##        #return 
##
##    def GetData(self, index):
##        u'Retrieve a featureClassName, adjustmentLevel pair.'
##        #return Name, adjustmentLevel
##
##    @property
##    def TransDataCount(self):
##        u'Retrieve the number of entries.'
##        #return Count
##
##    def AddData(self, Name, adjustmentLevel):
##        u'Add a featureClassID, adjustmentLevel pair.'
##        #return 
##

__all__ = ['ICadastralFabricName', 'TerrainToRasterFunction',
           'esriCadastralLineConnection', 'esriPointToRasterIDW',
           'E_TERRAIN_VALUE_OVERFLOW', 'esriTerrainLasReturnSingle',
           'E_TERRAIN_CANCELLED', 'esriLasGpsTime',
           'esriTerrainFloat', 'ITerrainLasDataImporter',
           'enumShapeSource', 'esriTinPointSelectionZmin',
           'E_TERRAIN_NOT_MATCH', 'enumTemporalRelation',
           'TerrainFieldStatistics', 'esriTerrainLasReturnNumber',
           'E_TERRAIN_NOT_MULTIPOINT', 'ITxEnumTrackId',
           'enumTemporalOperatorHours', 'esriLasClassFlag',
           'E_TERRAIN_VERSION_NOT_SUPPORTED', 'esriTerrainLong',
           'ILasPointInfo', 'ILineResequencer', 'Terrain',
           'esriLasPointStatsPulseCount', 'TerrainWorkspaceExtension',
           'E_TERRAIN_ZTOLERANCE_EXISTS', 'esriLasClassFlagSet',
           'esriCadastralPropSetUserDefined', 'ILasFile',
           'esriTerrainLasNumberOfReturns',
           'enumTemporalOperatorInterval',
           'ICadastralFabricEditControl', 'CadastralDataTools',
           'esriCadastralRegenRemoveOrphanPoints',
           'esriCadastralPropSetEditSettings', 'DETerrainType',
           'IConstructionParentParcels', 'esriCDUFoot',
           'esriPointToRasterNearest', 'E_TERRAIN_BAD_WINDOWSIZE',
           'ITerrain', 'esriCadastralLPAngleAndDistance',
           'esriPointToRasterVoidFillMethod', 'shapefromObject',
           'esriCadastralDensifiedGCS',
           'esriCadastralPointConstruction', 'enumSearch',
           'ICadastralAdjustmentVectors', 'esriLasColorRGB',
           'ITerrainEdit', 'esriCadastralLineRoad',
           'esriLasNumberOfReturns',
           'esriCadastralLPBearingAndDistance',
           'E_TERRAIN_CANNOT_BE_ANCHORED', 'ILasHeaderInfo',
           'E_TERRAIN_CANNOT_PERFORM_SIMPLIFY_OVERVIEW',
           'esriTerrainLasColorRed', 'enumTemporalOperatorUnits',
           'ICadastralFabric2', 'ICadastralFabric3',
           'esriCadastralPacketNoSetting',
           'E_TERRAIN_WRONG_GEOMETRY_TYPE', 'esriCAUSquareUSFoot',
           'esriCAUHectare', 'TerrainBlobWriter',
           'esriTerrainBlobDataType', 'enumSelect_OID',
           'E_LAS_FAILED_TO_OVER_WRITE', 'esriCFTJobs',
           'esriTerrainZThresholdMildThinning',
           'esriCadastralAreaUnits',
           'esriTerrainLasReturnFirstOfMany', 'IDETerrainType',
           'esriCadastralLPChordBearingAndDeltaAndRadius',
           'ITerrainPyramidLevel', 'E_TERRAIN_NOT_MULTIPOINT_Z',
           'esriCFTAdjustments', 'esriCadastralDensifiedNormal',
           'esriTerrainDecimalSeparatorPoint', 'esriLasAttributeType',
           'enumTemporalOperatorWeeks',
           'E_TERRAIN_INVALID_TERRAIN_NAME',
           'esriCadastralLineBoundary', 'esriTerrainLasColorBlue',
           'E_TERRAIN_WRONG_FORMAT', 'DETerrain',
           'esriTerrainLasClassification',
           'esriCadastralLineCategory',
           'esriTerrainPyramidZTolerance',
           'esriCadastralPropSetCoordinateTolerances',
           'ILasDatasetWorkspace', 'E_LAS_INVALID_VERSION',
           'ITerrain2', 'IConstructionAdjustment',
           'esriLasReturnNumber', 'esriLasIntensity',
           'enumKeepLatest', 'CadastralJob',
           'esriCadastralRegenRegenerateMissingRadials',
           'esriCadastralLPChordBearingAndArcLengthAndRadius',
           'ITemporalQueryFilter2', 'esriLasZSource',
           'ISimpleStatistics', 'ILasSurface', 'esriCAUAcre',
           'esriCDUUSSurveyLink', 'TerrainPyramidLevelZTolerance',
           'ILasPointFilter', 'ITemporalFeatureClassStatistics',
           'sourceLocalGeoDatabase', 'esriTinPointSelectionZmax',
           'IConstructionBasisOfBearing', 'esriLasZSourceColorBlue',
           'TerrainBlobReader', 'ITerrainAsciiDataImporter2',
           'ITemporalFeature', 'esriCDUUSSurveyFoot',
           'esriCFTParcels', 'esriTerrainShort',
           'ITemporalQueryFilter', 'GPTerrainMembership',
           'esriCadastralJob', 'sourceShapeFile', 'ILasStatistics',
           'E_TERRAIN_NULL_FIELD_VALUE', 'E_TERRAIN_BOUNDS_OVERLAP',
           'esriCDUChain', 'ITxFeatureClass', 'ITerrainName',
           'E_TERRAIN_UNKNOWN_FIELD', 'LasDatasetToRasterFunction',
           'E_TERRAIN_NOT_EMBEDDED', 'E_TERRAIN_INVALID_FILE',
           'esriTerrainAsciiDataFormatXYZ', 'esriCFJobAll',
           'E_TERRAIN_MUST_BE_ZLESS', 'E_TERRAIN_INCONSIST_LOR',
           'esriCadastralRegenRemoveInvalidLinePoints',
           'esriCFTPoints', 'TerrainDataSource',
           'IParcelConstructionData', 'enumTemporalOperatorType',
           'esriTerrainLasDataPropertyType',
           'esriTerrainLasReturnLast', 'esriTerrainPyramidType',
           'esriCAUMetric', 'ICadastralGroundToGridTools',
           'esriCadastralPacketSetting',
           'esriCadastralLinePointCategory',
           'esriPointToRasterMethod', 'esriTerrainLasScanAngleRank',
           'LasClassCodeStatistics', 'TerrainAsciiDataImporter',
           'esriTerrainLasColorGreen', 'esriTerrainLasUserBitField',
           'esriCadastralLPRadialBearingAndArcLengthAndRadius',
           'ITemporalOperator', 'esriLasScanDirectionFlag',
           'esriCadastralLPChordBearingAndDeltaAndArcLength',
           'ITerrainBlobReader',
           'E_TERRAIN_TOO_MANY_CLIPPING_SOURCES',
           'esriCadastralDistanceUnits', 'ITemporalCursor',
           'esriCadastralPointStandard',
           'esriCadastralDensifiedCurve', 'TerrainBlockCursor',
           'esriCadastralLPDeltaAndRadius',
           'esriCadastralLPChordLengthAndRadius', 'sourceSDE',
           'esriTerrainWindowSizeZmin',
           'esriTerrainAsciiDataFormatType',
           'esriLasClassFlagEditType', 'LasPointInfo',
           'esriLasClassFlagClear', 'LasHeaderInfo',
           'esriTerrainZThresholdStrategy', 'ITerrainDataSource',
           'esriTerrainLasFileMarker', 'E_TERRAIN_NEED_UPDATE',
           'esriLasZSourceZ', 'ILasPointCloud', 'TerrainName',
           'ITrackingServiceDef', 'IInternalTable',
           'ICadastralFabric', 'ITrackingConnectionFolder',
           'esriCAUSquareFoot', 'E_TERRAIN_TERRAIN_NOT_FOUND',
           'E_TERRAIN_INVALID_BOUNDS', 'E_TERRAIN_WRONG_PYRAMID_TYPE',
           '_RGB32', 'ITerrainFieldStatistics',
           'E_TERRAIN_WRONG_TOPOLOGY', 'ILasDatasetEdit',
           'esriCadastralPointStation', 'enumObjectSource', 'RGB32',
           'E_TERRAIN_FILE_WRITE_ERROR', 'E_TERRAIN_FILE_OPEN_ERROR',
           'E_TERRAIN_NO_SPATIALREF_INFO',
           'enumTemporalOperatorMilliseconds',
           'esriTerrainWindowSizeZmax',
           'esriCadastralLPRadialBearingAndDeltaAndArcLength',
           'ICadastralTableFieldEdits', 'esriCadastralLineParameters',
           'msgtypeSTATUS', 'esriTFCMNone', 'LasDatasetName',
           'ICadastralFabricSchemaEdit2', 'ICadastralFabricLocks',
           'ICadastralFabricLocks2', 'E_TERRAIN_INVALID_Z',
           'esriLasColorRed', 'esriCFTControl',
           'esriCadastralLineOriginConnection', 'msgtypeDATA',
           'enumTemporalFeatureType', 'esriCAUSections',
           'LasStatistics', 'IDataMessage',
           'E_TERRAIN_INVALID_DEFINITION',
           'esriCadastralPropSetCatalogDataset',
           'esriTerrainDecimalSeparatorType',
           'ICadastralFabricRegeneration',
           'E_TERRAIN_FILE_NOT_EXISTS', 'IEnumEnvelope',
           'esriCadastralDensifiedLineString',
           'esriTerrainLasReturnAll', 'CadastralFabric',
           'ITemporalRecordSet', 'LasDataset',
           'esriPointToRasterZmin', 'IConstructionBreakPoints',
           'esriCadastralFabricTable', 'ITemporalFeatureClass2',
           'esriCFJobCommitted', 'esriCadastralLineDependent',
           'enumUpdate', 'esriCadastralLineRadial',
           'DECadastralFabric', 'IEnumLasPoint',
           'E_TERRAIN_INCONSIST', 'E_TERRAIN_DATA_TYPE_MISMATCH',
           'esriCadastralLinePointBreak', 'esriTFCMCacheAll',
           'ICadastralFabricSchemaEdit', 'ITerrainBlobWriter',
           'ICadastralUnitTools',
           'esriCadastralLPRadialBearingAndChordLengthAndRadius',
           'esriLasColorBlue', 'ITemporalTable',
           'esriLasZSourceColorGreen',
           'esriTerrainZThresholdStrongThinning',
           'E_TERRAIN_FC_OUTSIDE', 'esriCadastralSurvey',
           'LasSurface', 'ILasPointEdit', 'E_TERRAIN_FILE_READ_ERROR',
           'esriCadastralRegenRegenerateMissingPoints',
           'ILasClassCodeStatistics', 'esriCFTLinePoints',
           'enumTemporalConversionToOLEDate', 'esriCDURod',
           'LasDatasetWorkspaceFactory',
           'esriParcelAdjustmentTransit',
           'esriCadastralLPChordBearingAndChordLengthAndRadius',
           'IConstructionPoints', 'esriTinPointSelectionZaverage',
           'esriCadastralRegenSnapLinePoints',
           'CadastralFabricFDExtension',
           'esriTerrainLasEdgeOfFlightLine', 'E_TERRAIN_FILE_EXISTS',
           'enumTemporalRelationIntersects',
           'esriLasClassFlagNoChange', 'enumTemporalOrder',
           'CadastralTableFieldEdits', 'ILasReturnStatistics',
           'esriCAUPerches', 'E_LAS_BAD_CLASS_CODE',
           'ILasAttributeFilter', 'ITemporalObservationsTable',
           'esriTerrainULong', 'E_TERRAIN_FORMAT_NOT_SUPPORTED',
           'enumTemporalOperatorMonths', 'esriCFTJobObjects',
           'esriCFTLines', 'enumTemporalOperatorYears',
           'esriTerrainLasReturn8', 'esriLasColorGreen',
           'esriTerrainLasReturn5', 'esriTerrainLasReturn4',
           'esriTerrainLasReturn7', 'esriTerrainLasReturn6',
           'esriTerrainLasReturn1', 'esriTerrainLasReturn3',
           'esriTerrainLasReturn2', 'E_TERRAIN_INVALID_TERRAIN',
           'esriCadastralMap', 'esriLasClassFlagKey',
           'esriCadastralRegeneratorSetting',
           'esriPointToRasterVoidFillSimple',
           'esriCAUQuarterSections', 'CadastralTransformationData',
           'enumTemporalOperatorMinutes',
           'E_TERRAIN_CANNOT_CHANGE_SCHEMA',
           'TerrainPyramidLevelWindowSize',
           'CadastralWorkspaceDatasetExtension',
           'E_TERRAIN_TERRAIN_NOT_SUPPORTED_IN_RELEASE',
           'E_TERRAIN_ANCHOR_POINTS_NOT_SUPPORTED',
           'LasReturnStatistics', 'E_TERRAIN_TOO_MANY_BASE',
           'IConstructionJoinLinks', 'DECadastralFabricType',
           'esriCFTAccuracy', 'E_LAS_BAD_Z_SOURCE',
           'esriPointToRasterVoidFillInterpolation', 'enumOldest',
           '_ITemporalFeatureClassEvents', 'esriTerrainChar',
           'E_TERRAIN_FIELD_NULLABLE', 'E_TERRAIN_NO_DATA',
           'IDynamicSurface3', 'IDynamicSurface2',
           'esriPointToRasterVoidFillNoFill',
           'esriTerrainWindowSizeZminZmax', 'esriCFJobActive',
           'E_TERRAIN_INDEX_OUT_OF_RANGE',
           'esriPointToRasterZaverage',
           'IConstructionUnbuildableLines', 'esriTerrainLasGpsTime',
           'TerrainLasDataImporter', 'CadastralFabricName',
           'LasAttributeStatistics', 'E_TERRAIN_FIELD_TYPE_MISMATCH',
           'esriCadastralLPTangentBearingAndDeltaAndArcLength',
           'DESCENDING', 'E_TERRAIN_DIRTY_TERRAIN',
           'esriTinPointSelectionMethod', 'IDECadastralFabric3',
           'IDECadastralFabric2', 'esriTerrainDecimalSeparatorComma',
           'E_LAS_UNABLE_TO_EDIT_ZIP_FILE', 'esriLasUserData',
           'ITerrainEditEvents', 'ILockedFeatureSearch',
           'esriCadastralLinePreciseConnection',
           'E_TERRAIN_CHANGE_CLASS_ID', 'ITerrainLasDataInfo2',
           'E_TERRAIN_WRONG_DATASET_TYPE',
           'esriCadastralPointCategory',
           'E_TERRAIN_WINSIZE_NOT_SUPPORTED',
           'esriCadastralPointInterpolated',
           'esriParcelAdjustmentCompass', 'IGPTerrainMembership',
           'E_TERRAIN_INVALID_EMBEDDED_FC_NAME', 'IDynamicSurface',
           'LasToRasterFunctionArguments',
           'esriCadastralPropertySetType', 'IDECadastralFabricType',
           'esriLasZSourceColorRGB',
           'esriTerrainAsciiDataFormatGenerate', 'enumSelect',
           'DynamicSurface', 'esriLasPointStatsMostFrequent',
           'LasPointEnumerator', 'ICadastralUnitConversion',
           'ITemporalWorkspaceStatistics2', 'enumPurgeRule',
           'CadastralUnitConversion', 'esriCadastralFabricType',
           'E_TERRAIN_EDIT_SESSION_REQUIRED',
           'esriCadastralLPDeltaAndArcLength',
           'esriTxFeatureClassCachingMode', 'IDETerrainWindowSize',
           'esriTerrainDouble',
           'esriCadastralPacketNeighborsInPacket',
           'esriCAUSquareRods', 'esriLasDatasetError',
           'esriTerrainUShort', 'esriTerrainLasReturnType',
           'esriCadastralLinePointStandard', 'esriLasClassCode',
           'esriLasClassFlagSynthetic', 'esriTerrainWindowSizeMethod',
           'esriCadastralPointBenchMark',
           'E_TERRAIN_TERRAIN_ALREADY_EXISTS',
           'esriTerrainLasScanDirectionFlag',
           'esriCadastralLPArcLengthAndRadius',
           'ITemporalObservationsTable2',
           'esriLasPointStatsPointCount', 'E_TERRAIN_NO_RETURN',
           'LasToRasterFunction', 'E_LAS_FAILED_TO_COPY_FILE',
           'esriTerrainUChar', 'esriTerrainPyramidWindowSize',
           'esriLasScanAngleRank', 'E_TERRAIN_IN_EDIT_SESSION',
           'E_TERRAIN_CANNOT_ADD_REGISTERED_CLASS_TO_TERRAIN',
           'esriCadastralPropSetImporterLoading',
           'enumTemporalSource', 'ILasFilter',
           'esriCadastralLPTangentBearingAndArcLengthAndRadius',
           'esriCadastralRegenRegenerateGeometries',
           'esriLasPointStatsType', 'enumTemporalOperatorSeconds',
           'esriPointToRasterZmax', 'esriCadastralDensifiedType',
           'enumTimeStamp', 'esriLasPointSourceID',
           'esriLasClassFlagWithheld', 'ITerrainEmbeddedDataSource2',
           'shapefromObservation', 'IDECadastralFabric',
           'esriCAUSquareMeter', 'esriCadastralPointReferenceMark',
           'E_TERRAIN_INVALID_GEOMETRY_TYPE_FOR_TERRAIN',
           'E_LAS_NO_STATISTICS', 'esriLasZSourceColorRed',
           'ITerrainBlockCursor', 'ITerrainDataImporter',
           'ITxWorkspaceEditor', 'E_LAS_CLASS_FLAG_NOT_SUPPORTED',
           'esriTerrainLasIntensity', 'enumTemporalConversionNone',
           'esriCDUMeter', 'E_TERRAIN_UNKNOWN_BLOB',
           'enumMessageType', 'esriParcelAdjustmentCrandall',
           'E_TERRAIN_BAD_SHAPE_SIZE',
           'TerrainToRasterFunctionArguments',
           'esriCadastralLinePartConnection',
           'LasDatasetToRasterFunctionArguments',
           'esriTerrainLasReturnLastOfMany', 'ParcelConstructionData',
           'IDETerrain', 'IListener', 'msgtypeRESPONSE',
           'msgtypeCOMMAND', 'enumCount',
           'E_TERRAIN_NOT_PROJECTED_SYSTEM', 'enumTemporalConversion',
           'enumTemporalConversionToString', 'esriCFTHistory',
           'LasFilter', 'ITerrainEdit3', 'ITerrainEdit2',
           'enumTemporalOperatorDateTime', 'ITerrainLasDataInfo',
           'enumTemporalCursorType', 'E_TERRAIN_NOT_INITIALIZED',
           'esriLasClassFlagNone', 'ICadastralTransformationData',
           'E_TERRAIN_INVALID_DATA_SOURCE', 'esriCDUUSSurveyRod',
           'esriLasPointStatsRange', 'IAMSDatasetName',
           'esriLasZSourceIntensity', 'ICadastralJob',
           'E_TERRAIN_WRONG_SF_TYPE', 'ASCENDING',
           'esriTerrainWindowSizeZaverage', 'ILasDataset2',
           'TerrainFeatureDatasetExtension', 'esriCAUImperial',
           'E_LAS_IN_MEMORY_DATASET', 'E_LAS_DATASET_EXISTS',
           'E_TERRAIN_WKT_NOT_SUPPORTED',
           'esriTinPointSelectionRandom', 'esriLasNone',
           'esriCadastralRegenRepairLineSequencing', 'esriCFTPlans',
           'esriLasZ', 'ITerrainEmbeddedDataSource',
           'esriCadastralPointControl',
           'E_TERRAIN_DATA_SOURCE_EXISTS', 'enumTemporalOperatorDays',
           'esriCadastralLPTangentBearingAndChordLengthAndRadius',
           'esriCadastralLPRadialBearingAndDeltaAndRadius',
           'ITemporalWorkspaceStatistics', 'esriCDUUSSurveyChain',
           'esriTerrainError',
           'esriTerrainZThresholdModerateThinning', 'esriCFTLevels',
           'LasFile', 'ILasDataset',
           'E_TERRAIN_MUST_APPLY_TO_OVERVIEW',
           'esriLasEdgeOfFlightLine', 'IDatasetNames',
           'esriCFTVectors', 'enumTemporalRelationContains',
           'E_LAS_FAILED_TO_OPEN', 'esriCAURoods',
           'E_TERRAIN_MUST_NOT_BE_GROUPED', 'E_LAS_FAILED_TO_SAVE',
           'E_TERRAIN_EDIT_OPERATION_REQUIRED', 'LineResequencer',
           'esriTerrainAsciiDataFormatXYZI', 'sourceDynamic',
           'enumTemporalSourceField', 'ITerrainAsciiDataImporter',
           'ITemporalObjectTable', 'esriCDULink',
           'esriCadastralLPTangentBearingAndDeltaAndRadius',
           'esriParcelAdjustmentType', 'esriParcelAdjustmentNone',
           'E_TERRAIN_MIXING_2D_AND_3D', 'ITerrainDataSource2',
           'enumInsert', 'IExcludedEventIDs',
           'CadastralFabricRegenerator', 'E_TERRAIN_OLD_VERSION',
           'E_LAS_OPERATION_NOT_SUPPORTED_ON_ZIP_FILE']
from comtypes import _check_version; _check_version('501')

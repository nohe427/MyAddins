# -*- coding: mbcs -*-
typelib_path = u'C:\\Program Files (x86)\\ArcGIS\\Engine10.2\\com\\esriGISClient.olb'
_lcid = 0 # change this if required
from ctypes import *
from comtypes import GUID
from comtypes import CoClass
import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0
import comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2
import comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2
from comtypes import BSTR
from ctypes import HRESULT
from comtypes import helpstring
from comtypes import COMMETHOD
from comtypes import dispid
from comtypes.automation import VARIANT
from ctypes.wintypes import VARIANT_BOOL
from comtypes import IUnknown
import comtypes.gen._18F2FC71_6B30_45B9_B101_037A8B868B66_0_10_2
import comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2
from comtypes.automation import VARIANT


class WMTSConnection(CoClass):
    u'The Connection for WMTS.'
    _reg_clsid_ = GUID('{EBF93DB1-B6F1-4DFE-94E0-A0D9F2898B83}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{746F6817-89BB-4490-9829-83CA25FD505A}', 10, 2)
class IWMTSConnection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that supply WMTS connection information.'
    _iid_ = GUID('{525ADE39-E2E6-418A-BB56-04EAB6FEBBB3}')
    _idlflags_ = ['oleautomation']
class IWMTSServiceDescription(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members give access to WMTSServiceDescription information.'
    _iid_ = GUID('{B5543B2A-65EF-410C-9819-80ED5BD7E669}')
    _idlflags_ = ['oleautomation']
WMTSConnection._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IWMTSConnection, IWMTSServiceDescription, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]


# values for enumeration 'esriAGSServerType'
esriAGSServerTypeUnknown = -1
esriAGSServerTypeClassic = 0
esriAGSServerTypeDiscovery = 1
esriAGSServerTypeSDS = 2
esriAGSServerTypeAGO = 3
esriAGSServerType = c_int # enum
class WMTSConnectionFactory(CoClass):
    u'A factory object for WMTS Connections.'
    _reg_clsid_ = GUID('{5DC87020-5300-4B06-B6FB-915CECF9D893}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{746F6817-89BB-4490-9829-83CA25FD505A}', 10, 2)
class IWMTSConnectionFactory(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members give access to WMTSFactory information.'
    _iid_ = GUID('{8043C9BE-1311-4020-A18F-EC23EFEC6289}')
    _idlflags_ = ['oleautomation']
WMTSConnectionFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IWMTSConnectionFactory]

class IAGSServerObjectName(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that supply server object name information.'
    _iid_ = GUID('{436BD37C-FE61-4A2E-9D74-1AE6FC8D654D}')
    _idlflags_ = ['oleautomation']
class IAGSServerConnectionName(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that supply GIS server connection name information.'
    _iid_ = GUID('{298CCE6A-4D86-40EE-8F4A-BEBC419B9A4D}')
    _idlflags_ = ['oleautomation']
IAGSServerObjectName._methods_ = [
    COMMETHOD(['propput', helpstring(u'Name of the server object.')], HRESULT, 'Name',
              ( ['in'], BSTR, 'objectName' )),
    COMMETHOD(['propget', helpstring(u'Name of the server object.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'objectName' )),
    COMMETHOD(['propput', helpstring(u'Type of the server object (MapServer or GeocodeServer).')], HRESULT, 'Type',
              ( ['in'], BSTR, 'ObjectType' )),
    COMMETHOD(['propget', helpstring(u'Type of the server object (MapServer or GeocodeServer).')], HRESULT, 'Type',
              ( ['retval', 'out'], POINTER(BSTR), 'ObjectType' )),
    COMMETHOD(['propput', helpstring(u'Server object URL (if connection type is internet).')], HRESULT, 'URL',
              ( ['in'], BSTR, 'objectURL' )),
    COMMETHOD(['propget', helpstring(u'Server object URL (if connection type is internet).')], HRESULT, 'URL',
              ( ['retval', 'out'], POINTER(BSTR), 'objectURL' )),
    COMMETHOD(['propget', helpstring(u'The connection name object for this server object.')], HRESULT, 'AGSServerConnectionName',
              ( ['retval', 'out'], POINTER(POINTER(IAGSServerConnectionName)), 'ppServerConnName' )),
    COMMETHOD(['propputref', helpstring(u'The connection name object for this server object.')], HRESULT, 'AGSServerConnectionName',
              ( ['in'], POINTER(IAGSServerConnectionName), 'ppServerConnName' )),
]
################################################################
## code template for IAGSServerObjectName implementation
##class IAGSServerObjectName_Impl(object):
##    def _get(self):
##        u'Server object URL (if connection type is internet).'
##        #return objectURL
##    def _set(self, objectURL):
##        u'Server object URL (if connection type is internet).'
##    URL = property(_get, _set, doc = _set.__doc__)
##
##    def AGSServerConnectionName(self, ppServerConnName):
##        u'The connection name object for this server object.'
##        #return 
##
##    def _get(self):
##        u'Type of the server object (MapServer or GeocodeServer).'
##        #return ObjectType
##    def _set(self, ObjectType):
##        u'Type of the server object (MapServer or GeocodeServer).'
##    Type = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Name of the server object.'
##        #return objectName
##    def _set(self, objectName):
##        u'Name of the server object.'
##    Name = property(_get, _set, doc = _set.__doc__)
##

class IAGSServerConnection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that have information about the GIS server connection..'
    _iid_ = GUID('{657F65FD-9795-40B4-B1CE-E235EF08614C}')
    _idlflags_ = ['oleautomation']
class IAGSEnumServerObjectName(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that hand out enumerated server object names and reset the enumeration.'
    _iid_ = GUID('{E584B406-753E-4E29-B20B-FED66FA3EF3C}')
    _idlflags_ = ['oleautomation']
IAGSServerConnection._methods_ = [
    COMMETHOD(['propput', helpstring(u'The name of the connection.')], HRESULT, 'Name',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD(['propget', helpstring(u'The name of the connection.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'The ServerObjectNames in the GIS server.')], HRESULT, 'ServerObjectNames',
              ( ['retval', 'out'], POINTER(POINTER(IAGSEnumServerObjectName)), 'ppSONames' )),
    COMMETHOD(['propget', helpstring(u'The AGSServerConnectionName object assiated with the GIS server connection.')], HRESULT, 'FullName',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName)), 'ppNameObject' )),
    COMMETHOD(['propputref', helpstring(u'The AGSServerConnectionName object assiated with the GIS server connection.')], HRESULT, 'FullName',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName), 'ppNameObject' )),
]
################################################################
## code template for IAGSServerConnection implementation
##class IAGSServerConnection_Impl(object):
##    @property
##    def ServerObjectNames(self):
##        u'The ServerObjectNames in the GIS server.'
##        #return ppSONames
##
##    def FullName(self, ppNameObject):
##        u'The AGSServerConnectionName object assiated with the GIS server connection.'
##        #return 
##
##    def _get(self):
##        u'The name of the connection.'
##        #return Name
##    def _set(self, Name):
##        u'The name of the connection.'
##    Name = property(_get, _set, doc = _set.__doc__)
##

class IIMSWorkspace(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that provide information on the ArcIMS Workspace.'
    _iid_ = GUID('{5E773EC1-F5E7-11D3-9F48-00C04F79927C}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'acMapUnits'
acDecimalDegrees = 0
acMeters = 1
acFeet = 2
acKilometers = 3
acMiles = 4
acMapUnits = c_int # enum
IIMSWorkspace._methods_ = [
    COMMETHOD(['propget', helpstring(u'The native spatial reference of the data.')], HRESULT, 'SpatialReference',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference)), 'SpatialReference' )),
    COMMETHOD(['propget', helpstring(u'The area of interest.')], HRESULT, 'AreaOfInterest',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'envelope' )),
    COMMETHOD(['propget', helpstring(u'The map units.')], HRESULT, 'MapUnits',
              ( ['retval', 'out'], POINTER(acMapUnits), 'MapUnits' )),
]
################################################################
## code template for IIMSWorkspace implementation
##class IIMSWorkspace_Impl(object):
##    @property
##    def MapUnits(self):
##        u'The map units.'
##        #return MapUnits
##
##    @property
##    def AreaOfInterest(self):
##        u'The area of interest.'
##        #return envelope
##
##    @property
##    def SpatialReference(self):
##        u'The native spatial reference of the data.'
##        #return SpatialReference
##

class IEnumUploadItem(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that enumerate through Discovery uploads items.'
    _iid_ = GUID('{F00D29B6-E9D5-4AC2-A8C7-7C8338CF88C6}')
    _idlflags_ = ['oleautomation']
class IUploadItem(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to upload item objects.'
    _iid_ = GUID('{68BD2CAD-90AF-4BFB-9117-4F28AED6CBE0}')
    _idlflags_ = ['oleautomation']
IEnumUploadItem._methods_ = [
    COMMETHOD([helpstring(u'The next Discovery uploads item.')], HRESULT, 'Next',
              ( ['retval', 'out'], POINTER(POINTER(IUploadItem)), 'ppUploadItemConfig' )),
    COMMETHOD([helpstring(u'Starts the enumeration at the beginning.')], HRESULT, 'Reset'),
]
################################################################
## code template for IEnumUploadItem implementation
##class IEnumUploadItem_Impl(object):
##    def Reset(self):
##        u'Starts the enumeration at the beginning.'
##        #return 
##
##    def Next(self):
##        u'The next Discovery uploads item.'
##        #return ppUploadItemConfig
##

class WMSConnectionName(CoClass):
    u'The WMS Connection name.'
    _reg_clsid_ = GUID('{98B0E997-F21D-4195-8E06-F9CD2AD97165}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{746F6817-89BB-4490-9829-83CA25FD505A}', 10, 2)
class IWMSConnectionName(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that supply WMS server connection name information.'
    _iid_ = GUID('{07C8FD52-5D97-4B1F-A6BF-4973C9BB4117}')
    _idlflags_ = ['oleautomation']
WMSConnectionName._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IWMSConnectionName, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName]

class WMSConnection(CoClass):
    u'The Connection for WMS.'
    _reg_clsid_ = GUID('{FDDB9510-1619-49E9-BAA5-9A6620F315AD}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{746F6817-89BB-4490-9829-83CA25FD505A}', 10, 2)
class IWMSConnection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that supply WMS connection information.'
    _iid_ = GUID('{67BC7DE0-0A6D-4BA6-9D26-437C44DBDDF3}')
    _idlflags_ = ['oleautomation']
class IWMSServiceDescription(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members give access to WMSServiceDescription information.'
    _iid_ = GUID('{DE0E6EBF-8ABF-4700-B9F5-B097E14C0E51}')
    _idlflags_ = ['oleautomation']
class IWMSClientEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to events that occur when a URL request is made to the WMS server.'
    _iid_ = GUID('{4EE28878-3A87-40E5-B25D-6FCC4D683E8C}')
    _idlflags_ = ['oleautomation']
WMSConnection._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IWMSConnection, IWMSServiceDescription, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]
WMSConnection._outgoing_interfaces_ = [IWMSClientEvents]

class WMTSLayerDescription(CoClass):
    u'A factory object for WMTS Layer Description.'
    _reg_clsid_ = GUID('{6FE7AE5F-3097-44CE-AB5C-F35BD568A58A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{746F6817-89BB-4490-9829-83CA25FD505A}', 10, 2)
class IWMTSLayerDescription(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members give access to WMTSLayerDescription information.'
    _iid_ = GUID('{E28B0014-208C-4C9B-8E24-AC882D0B4C36}')
    _idlflags_ = ['oleautomation']
WMTSLayerDescription._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IWMTSLayerDescription]

class WMSServiceExceptionHandler(CoClass):
    u'WMS Service Exception Handler.'
    _reg_clsid_ = GUID('{EB412F19-FB25-44AA-8421-070EDD242F3C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{746F6817-89BB-4490-9829-83CA25FD505A}', 10, 2)
class IWMSServiceExceptionHandler(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that provide WMS error descriptions.'
    _iid_ = GUID('{CFCACA30-440A-488E-815A-86351CD78ECC}')
    _idlflags_ = ['oleautomation']
WMSServiceExceptionHandler._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IWMSServiceExceptionHandler]

class WMSConnectionFactory(CoClass):
    u'A factory object for WMS Connections.'
    _reg_clsid_ = GUID('{F7C34345-87CE-4AB5-9CA8-2012D7241075}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{746F6817-89BB-4490-9829-83CA25FD505A}', 10, 2)
class IWMSConnectionFactory(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members give access to WMSFactory information.'
    _iid_ = GUID('{253C9134-0D0F-45C7-BFDC-D230D0F8CE35}')
    _idlflags_ = ['oleautomation']
WMSConnectionFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IWMSConnectionFactory]

class AGSServerConnectionName(CoClass):
    u'A name object for ArcGIS Server Connections.'
    _reg_clsid_ = GUID('{CBA35C3F-EDEF-408F-8B51-510784C78EB9}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{746F6817-89BB-4490-9829-83CA25FD505A}', 10, 2)
class IAGSServerConnectionName2(IAGSServerConnectionName):
    _case_insensitive_ = True
    u'Provides access to members that supply GIS server connection name information.'
    _iid_ = GUID('{C65DC76B-B454-4B35-83EC-E9082B57A56F}')
    _idlflags_ = ['oleautomation']
AGSServerConnectionName._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IAGSServerConnectionName, IAGSServerConnectionName2, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream]

class IIMSServiceDescription(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members to get IMS connection properties and get the specified service child.'
    _iid_ = GUID('{FE9F959A-06B5-4D52-8148-3BD33C29C0C5}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'acServiceType'
acMapService = 0
acFeatureService = 1
acMetadataService = 2
acGlobeService = 3
acWMSService = 4
acUnknownService = 5
acServiceType = c_int # enum
IIMSServiceDescription._methods_ = [
    COMMETHOD(['propget', helpstring(u'Service Name.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propput', helpstring(u'Service Name.')], HRESULT, 'Name',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD(['propget', helpstring(u'URL to ArcIMS server.')], HRESULT, 'URL',
              ( ['retval', 'out'], POINTER(BSTR), 'URL' )),
    COMMETHOD(['propput', helpstring(u'URL to ArcIMS server.')], HRESULT, 'URL',
              ( ['in'], BSTR, 'URL' )),
    COMMETHOD(['propput', helpstring(u'User name for the specified service.')], HRESULT, 'UserName',
              ( ['in'], BSTR, 'UserName' )),
    COMMETHOD(['propget', helpstring(u'User name for the specified service.')], HRESULT, 'UserName',
              ( ['retval', 'out'], POINTER(BSTR), 'UserName' )),
    COMMETHOD(['propget', helpstring(u'Password for the specified service.')], HRESULT, 'Password',
              ( ['retval', 'out'], POINTER(VARIANT), 'Password' )),
    COMMETHOD(['propput', helpstring(u'Password for the specified service.')], HRESULT, 'Password',
              ( ['in'], BSTR, 'Password' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the password should be saved.')], HRESULT, 'SavePassword',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the password should be saved.')], HRESULT, 'SavePassword',
              ( ['in'], VARIANT_BOOL, 'flag' )),
    COMMETHOD(['propget', helpstring(u'Type of service.')], HRESULT, 'ServiceType',
              ( ['retval', 'out'], POINTER(acServiceType), 'Type' )),
    COMMETHOD(['propput', helpstring(u'Type of service.')], HRESULT, 'ServiceType',
              ( ['in'], acServiceType, 'Type' )),
    COMMETHOD(['propget', helpstring(u'Type of security set on the service.  Use a combination of acSecurityType constants.')], HRESULT, 'Security',
              ( ['retval', 'out'], POINTER(c_int), 'Security' )),
    COMMETHOD(['propput', helpstring(u'Type of security set on the service.  Use a combination of acSecurityType constants.')], HRESULT, 'Security',
              ( ['in'], c_int, 'Security' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the service is private (requires password).')], HRESULT, 'IsPrivate',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsPrivate' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the service is private (requires password).')], HRESULT, 'IsPrivate',
              ( ['in'], VARIANT_BOOL, 'IsPrivate' )),
    COMMETHOD(['propget', helpstring(u'True if the service is free.')], HRESULT, 'ConnectionProperties',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'ConnectionProperties' )),
    COMMETHOD(['propput', helpstring(u'True if the service is free.')], HRESULT, 'ConnectionProperties',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'ConnectionProperties' )),
]
################################################################
## code template for IIMSServiceDescription implementation
##class IIMSServiceDescription_Impl(object):
##    def _get(self):
##        u'User name for the specified service.'
##        #return UserName
##    def _set(self, UserName):
##        u'User name for the specified service.'
##    UserName = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Type of service.'
##        #return Type
##    def _set(self, Type):
##        u'Type of service.'
##    ServiceType = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'True if the service is free.'
##        #return ConnectionProperties
##    def _set(self, ConnectionProperties):
##        u'True if the service is free.'
##    ConnectionProperties = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Service Name.'
##        #return Name
##    def _set(self, Name):
##        u'Service Name.'
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'URL to ArcIMS server.'
##        #return URL
##    def _set(self, URL):
##        u'URL to ArcIMS server.'
##    URL = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the service is private (requires password).'
##        #return IsPrivate
##    def _set(self, IsPrivate):
##        u'Indicates if the service is private (requires password).'
##    IsPrivate = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Type of security set on the service.  Use a combination of acSecurityType constants.'
##        #return Security
##    def _set(self, Security):
##        u'Type of security set on the service.  Use a combination of acSecurityType constants.'
##    Security = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Password for the specified service.'
##        #return Password
##    def _set(self, Password):
##        u'Password for the specified service.'
##    Password = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the password should be saved.'
##        #return flag
##    def _set(self, flag):
##        u'Indicates if the password should be saved.'
##    SavePassword = property(_get, _set, doc = _set.__doc__)
##

class WCSConnectionName(CoClass):
    u'The WCS Connection name.'
    _reg_clsid_ = GUID('{B96CFE9E-44C7-4616-8A2A-F1FBA8642AF6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{746F6817-89BB-4490-9829-83CA25FD505A}', 10, 2)
class IWCSConnectionName(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that supply WCS server connection name information.'
    _iid_ = GUID('{E1A24FDE-E0CB-4C17-BDC0-B5520DF063CB}')
    _idlflags_ = ['oleautomation']
WCSConnectionName._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IWCSConnectionName, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName]

class IWMSLayerDescription2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members give access to WMSLayerDescription information.'
    _iid_ = GUID('{3D35C25C-BBB5-4AAE-B9DA-9EC15756D432}')
    _idlflags_ = ['oleautomation']
class IWMTSDimension(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members give access to WMTSDimension information.'
    _iid_ = GUID('{DBC40029-335F-47C2-8CB0-75473FEF52BF}')
    _idlflags_ = ['oleautomation']
class IWMSLayerDescription(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members give access to WMSLayerDescription information.'
    _iid_ = GUID('{2290F5AC-8561-4B1D-8FDA-482A063F1EF4}')
    _idlflags_ = ['oleautomation']
class IWMSLayerStyleDescription(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members give access to WMSLayerStyleDescription information.'
    _iid_ = GUID('{0E5D8D4C-A8CD-4EB9-A311-AF312DC308BC}')
    _idlflags_ = ['oleautomation']
IWMSLayerDescription2._methods_ = [
    COMMETHOD(['propget', helpstring(u'Number of dimension in the layer.')], HRESULT, 'DimensionCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Dimension of the layer at the given index.')], HRESULT, 'Dimension',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IWMTSDimension)), 'Dimension' )),
    COMMETHOD(['propget', helpstring(u'Name of WMS layer.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'Title of WMS layer.')], HRESULT, 'Title',
              ( ['retval', 'out'], POINTER(BSTR), 'Title' )),
    COMMETHOD(['propget', helpstring(u'Abstract of the WMS layer.')], HRESULT, 'Abstract',
              ( ['retval', 'out'], POINTER(BSTR), 'Abstract' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the layer is queryable.')], HRESULT, 'IsQueryable',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'isQuaryable' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the layer is opaque or transparent in terms of the area that gets drawn.')], HRESULT, 'IsOpaque',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsOpaque' )),
    COMMETHOD(['propget', helpstring(u'Indicates the number of times the layer has been reserved.')], HRESULT, 'IsCascaded',
              ( ['retval', 'out'], POINTER(c_int), 'IsCascaded' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether or not the server will be able to crop the data to a geographic area smaller than its enclosing bounding box.')], HRESULT, 'IsSubsettable',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsSubsettable' )),
    COMMETHOD(['propget', helpstring(u'Fixed width at which server is able to display the layer. If this is zero, server can display the layer at any resolution.')], HRESULT, 'FixedWidth',
              ( ['retval', 'out'], POINTER(c_double), 'Width' )),
    COMMETHOD(['propget', helpstring(u'Fixed height at which server is able to display the layer. If this is zero, server can display the layer at any resolution.')], HRESULT, 'FixedHeight',
              ( ['retval', 'out'], POINTER(c_double), 'Height' )),
    COMMETHOD(['propget', helpstring(u'Number of WMSLayerDescriptions.')], HRESULT, 'LayerDescriptionCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'WMSLayerDescription at a given index.')], HRESULT, 'LayerDescription',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IWMSLayerDescription)), 'ppLayerDescription' )),
    COMMETHOD(['propget', helpstring(u'Suggested minimimum scale for the WMS layer.')], HRESULT, 'ScaleHintMin',
              ( ['retval', 'out'], POINTER(c_double), 'Scale' )),
    COMMETHOD(['propget', helpstring(u'Suggested maximum scale of the WMS layer.')], HRESULT, 'ScaleHintMax',
              ( ['retval', 'out'], POINTER(c_double), 'Scale' )),
    COMMETHOD(['propget', helpstring(u'Minimum bounding extent of the layer data in EPSG:4326.')], HRESULT, 'LatLongBoundingBox',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'envelope' )),
    COMMETHOD(['propget', helpstring(u'Number of bounding extents of the layer.')], HRESULT, 'BoundingBoxCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Minimum bounding extents of the layer data along with the applicable SRS.')], HRESULT, 'BoundingBox',
              ( ['in'], c_int, 'index' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'envelope' ),
              ( ['out'], POINTER(BSTR), 'srsCode' )),
    COMMETHOD(['propget', helpstring(u'Number of styles in the layer.')], HRESULT, 'StyleDescriptionCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Style of the layer at the given index.')], HRESULT, 'StyleDescription',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IWMSLayerStyleDescription)), 'StyleDescription' )),
    COMMETHOD(['propget', helpstring(u'Supported SRS count.')], HRESULT, 'SRSCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Supproted SRS at the given index.')], HRESULT, 'SRS',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'SRS' )),
    COMMETHOD(['propget', helpstring(u'WMS Version.')], HRESULT, 'WMSVersion',
              ( ['retval', 'out'], POINTER(BSTR), 'WMSVersion' )),
    COMMETHOD(['propget', helpstring(u"Supported GetMap's ImageFormat count.")], HRESULT, 'ImageFormatCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u"Supported GetMap's ImageFormat at the given index.")], HRESULT, 'ImageFormat',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ImageFormat' )),
    COMMETHOD(['propget', helpstring(u'Supported FeatureInfoFormat count.')], HRESULT, 'FeatureInfoFormatCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Supported FeatureInfoFormat at the given index.')], HRESULT, 'FeatureInfoFormat',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ImageFormat' )),
    COMMETHOD(['propget', helpstring(u'Supported exception format count.')], HRESULT, 'ExceptionFormatCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Supported exception at the given index.')], HRESULT, 'ExceptionFormat',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ExceptionFormat' )),
]
################################################################
## code template for IWMSLayerDescription2 implementation
##class IWMSLayerDescription2_Impl(object):
##    @property
##    def IsCascaded(self):
##        u'Indicates the number of times the layer has been reserved.'
##        #return IsCascaded
##
##    @property
##    def ExceptionFormat(self, index):
##        u'Supported exception at the given index.'
##        #return ExceptionFormat
##
##    @property
##    def Title(self):
##        u'Title of WMS layer.'
##        #return Title
##
##    @property
##    def ExceptionFormatCount(self):
##        u'Supported exception format count.'
##        #return Count
##
##    @property
##    def DimensionCount(self):
##        u'Number of dimension in the layer.'
##        #return Count
##
##    @property
##    def ImageFormat(self, index):
##        u"Supported GetMap's ImageFormat at the given index."
##        #return ImageFormat
##
##    @property
##    def ScaleHintMax(self):
##        u'Suggested maximum scale of the WMS layer.'
##        #return Scale
##
##    @property
##    def FixedWidth(self):
##        u'Fixed width at which server is able to display the layer. If this is zero, server can display the layer at any resolution.'
##        #return Width
##
##    @property
##    def FeatureInfoFormat(self, index):
##        u'Supported FeatureInfoFormat at the given index.'
##        #return ImageFormat
##
##    @property
##    def IsOpaque(self):
##        u'Indicates whether the layer is opaque or transparent in terms of the area that gets drawn.'
##        #return IsOpaque
##
##    @property
##    def StyleDescription(self, index):
##        u'Style of the layer at the given index.'
##        #return StyleDescription
##
##    @property
##    def LayerDescriptionCount(self):
##        u'Number of WMSLayerDescriptions.'
##        #return Count
##
##    @property
##    def FixedHeight(self):
##        u'Fixed height at which server is able to display the layer. If this is zero, server can display the layer at any resolution.'
##        #return Height
##
##    @property
##    def SRSCount(self):
##        u'Supported SRS count.'
##        #return Count
##
##    @property
##    def Name(self):
##        u'Name of WMS layer.'
##        #return Name
##
##    @property
##    def IsQueryable(self):
##        u'Indicates whether the layer is queryable.'
##        #return isQuaryable
##
##    @property
##    def ImageFormatCount(self):
##        u"Supported GetMap's ImageFormat count."
##        #return Count
##
##    @property
##    def LatLongBoundingBox(self):
##        u'Minimum bounding extent of the layer data in EPSG:4326.'
##        #return envelope
##
##    @property
##    def SRS(self, index):
##        u'Supproted SRS at the given index.'
##        #return SRS
##
##    @property
##    def LayerDescription(self, index):
##        u'WMSLayerDescription at a given index.'
##        #return ppLayerDescription
##
##    @property
##    def StyleDescriptionCount(self):
##        u'Number of styles in the layer.'
##        #return Count
##
##    @property
##    def IsSubsettable(self):
##        u'Indicates whether or not the server will be able to crop the data to a geographic area smaller than its enclosing bounding box.'
##        #return IsSubsettable
##
##    @property
##    def ScaleHintMin(self):
##        u'Suggested minimimum scale for the WMS layer.'
##        #return Scale
##
##    @property
##    def Dimension(self, index):
##        u'Dimension of the layer at the given index.'
##        #return Dimension
##
##    @property
##    def BoundingBoxCount(self):
##        u'Number of bounding extents of the layer.'
##        #return Count
##
##    @property
##    def Abstract(self):
##        u'Abstract of the WMS layer.'
##        #return Abstract
##
##    @property
##    def FeatureInfoFormatCount(self):
##        u'Supported FeatureInfoFormat count.'
##        #return Count
##
##    @property
##    def WMSVersion(self):
##        u'WMS Version.'
##        #return WMSVersion
##
##    @property
##    def BoundingBox(self, index):
##        u'Minimum bounding extents of the layer data along with the applicable SRS.'
##        #return envelope, srsCode
##

class IWMTSTileMatrix(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that describe a particular tile matrix.'
    _iid_ = GUID('{3FC53A77-74D8-4EB5-AA3C-D3797439E2A3}')
    _idlflags_ = ['oleautomation']
IWMTSTileMatrix._methods_ = [
    COMMETHOD(['propget', helpstring(u'Tile matrix set identifier.')], HRESULT, 'Identifier',
              ( ['retval', 'out'], POINTER(BSTR), 'ID' )),
    COMMETHOD(['propget', helpstring(u'Scale denominator level of this tile matrix.')], HRESULT, 'ScaleDenominator',
              ( ['retval', 'out'], POINTER(c_double), 'Scale' )),
    COMMETHOD(['propget', helpstring(u'Position in CRS coordinates of the top-left corner of this tile matrix.')], HRESULT, 'TopLeftCorner',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.WKSPoint), 'position' )),
    COMMETHOD(['propget', helpstring(u'Width of each tile of this tile matrix in pixels.')], HRESULT, 'TileWidth',
              ( ['retval', 'out'], POINTER(c_int), 'Width' )),
    COMMETHOD(['propget', helpstring(u'Height of each tile of this tile matrix in pixels.')], HRESULT, 'TileHeight',
              ( ['retval', 'out'], POINTER(c_int), 'Height' )),
    COMMETHOD(['propget', helpstring(u'Width of each tile of this tile matrix in pixels.')], HRESULT, 'MatrixWidth',
              ( ['retval', 'out'], POINTER(c_int), 'Width' )),
    COMMETHOD(['propget', helpstring(u'Height of each tile of this tile matrix in pixels.')], HRESULT, 'MatrixHeight',
              ( ['retval', 'out'], POINTER(c_int), 'Height' )),
]
################################################################
## code template for IWMTSTileMatrix implementation
##class IWMTSTileMatrix_Impl(object):
##    @property
##    def MatrixHeight(self):
##        u'Height of each tile of this tile matrix in pixels.'
##        #return Height
##
##    @property
##    def TileHeight(self):
##        u'Height of each tile of this tile matrix in pixels.'
##        #return Height
##
##    @property
##    def TileWidth(self):
##        u'Width of each tile of this tile matrix in pixels.'
##        #return Width
##
##    @property
##    def MatrixWidth(self):
##        u'Width of each tile of this tile matrix in pixels.'
##        #return Width
##
##    @property
##    def TopLeftCorner(self):
##        u'Position in CRS coordinates of the top-left corner of this tile matrix.'
##        #return position
##
##    @property
##    def Identifier(self):
##        u'Tile matrix set identifier.'
##        #return ID
##
##    @property
##    def ScaleDenominator(self):
##        u'Scale denominator level of this tile matrix.'
##        #return Scale
##

class WCSConnection(CoClass):
    u'The Connection for WCS.'
    _reg_clsid_ = GUID('{A9F6D7D9-F493-4EAF-B0D2-E8F6A3465667}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{746F6817-89BB-4490-9829-83CA25FD505A}', 10, 2)
class IWCSConnection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that supply WCS connection information.'
    _iid_ = GUID('{2BB26ED5-6774-4FF5-8252-1E973EBD5BDC}')
    _idlflags_ = ['oleautomation']
class IWCSServiceDescription(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members give access to WCSServiceDescription information.'
    _iid_ = GUID('{E19A5310-486C-4D32-8D44-93696D6804D4}')
    _idlflags_ = ['oleautomation']
WCSConnection._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IWCSConnection, IWCSServiceDescription, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

IWMSServiceExceptionHandler._methods_ = [
    COMMETHOD([helpstring(u'Parses the response to the give URL for any WMS error codes and descriptions.')], HRESULT, 'ParseExceptions',
              ( [], BSTR, 'fileOrURL' )),
    COMMETHOD(['propget', helpstring(u'Number of exceptions.')], HRESULT, 'ExceptionCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'WMS service exception code at the given index.')], HRESULT, 'ExceptionCode',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'wmsErrorCode' )),
    COMMETHOD(['propget', helpstring(u'WMS service exception description at the given index.')], HRESULT, 'ExceptionDescription',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'wmsErrorDescription' )),
]
################################################################
## code template for IWMSServiceExceptionHandler implementation
##class IWMSServiceExceptionHandler_Impl(object):
##    @property
##    def ExceptionDescription(self, index):
##        u'WMS service exception description at the given index.'
##        #return wmsErrorDescription
##
##    def ParseExceptions(self, fileOrURL):
##        u'Parses the response to the give URL for any WMS error codes and descriptions.'
##        #return 
##
##    @property
##    def ExceptionCode(self, index):
##        u'WMS service exception code at the given index.'
##        #return wmsErrorCode
##
##    @property
##    def ExceptionCount(self):
##        u'Number of exceptions.'
##        #return Count
##


# values for enumeration 'wcsErrors'
WCSCONN_E_ACCESS_DENIED = -2147220479
WCSCONN_E_PROXY_AUTHENTICATION_FAILED = -2147220478
WCSCONN_E_UNABLE_TO_CONNECT = -2147220477
WCSCONN_E_MISSING_URL = -2147220476
WCSCONN_E_MISSING_SERVICENAME = -2147220475
WCSCONN_E_INCORRECT_URL = -2147220474
WCSCONN_E_SERVER_NOT_AVAILABLE = -2147220473
wcsErrors = c_int # enum
IWMSConnectionName._methods_ = [
    COMMETHOD(['propput', helpstring(u'Connection properties that will be used to connect to the WMS server.')], HRESULT, 'ConnectionProperties',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'ConnectionProperties' )),
    COMMETHOD(['propget', helpstring(u'Connection properties that will be used to connect to the WMS server.')], HRESULT, 'ConnectionProperties',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'ConnectionProperties' )),
    COMMETHOD([helpstring(u'Opens the WMS Connection.')], HRESULT, 'OpenEx',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'ppUnknown' )),
]
################################################################
## code template for IWMSConnectionName implementation
##class IWMSConnectionName_Impl(object):
##    def OpenEx(self, pTrackCancel):
##        u'Opens the WMS Connection.'
##        #return ppUnknown
##
##    def _get(self):
##        u'Connection properties that will be used to connect to the WMS server.'
##        #return ConnectionProperties
##    def _set(self, ConnectionProperties):
##        u'Connection properties that will be used to connect to the WMS server.'
##    ConnectionProperties = property(_get, _set, doc = _set.__doc__)
##

class WCSServiceExceptionHandler(CoClass):
    u'WCS Service Exception Handler.'
    _reg_clsid_ = GUID('{6C1B586B-6D46-4528-BAE6-BF1552817C4A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{746F6817-89BB-4490-9829-83CA25FD505A}', 10, 2)
class IWCSServiceExceptionHandler(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that provide WCS error descriptions.'
    _iid_ = GUID('{AD2E4DE6-CC7E-41E1-911F-5343CD27F227}')
    _idlflags_ = ['oleautomation']
WCSServiceExceptionHandler._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IWCSServiceExceptionHandler]

class WCSConnectionFactory(CoClass):
    u'A factory object for WCS Connections.'
    _reg_clsid_ = GUID('{ED030E3A-BA11-4047-9B36-0FA11E513DCD}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{746F6817-89BB-4490-9829-83CA25FD505A}', 10, 2)
class IWCSConnectionFactory(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members give access to WCSFactory information.'
    _iid_ = GUID('{A73A11E4-AEB0-4917-B36E-A43865CC9B7B}')
    _idlflags_ = ['oleautomation']
WCSConnectionFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IWCSConnectionFactory]

class WMTSTileMatrixSetLink(CoClass):
    u'Object that describes metadata about the TileMatrixSet reference'
    _reg_clsid_ = GUID('{2C10EDFC-4429-44D1-AF58-2D9034571F66}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{746F6817-89BB-4490-9829-83CA25FD505A}', 10, 2)
class IWMTSTileMatrixSetLink(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that describe metadata about the TileMatrixSet reference.'
    _iid_ = GUID('{95AD2016-D7AE-44D4-A121-CB2645F4EA42}')
    _idlflags_ = ['oleautomation']
WMTSTileMatrixSetLink._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IWMTSTileMatrixSetLink]


# values for enumeration 'agsClientError'
AGS_E_CONNECTION_CANCELLED = -2147219199
AGS_E_INSECURE_TOKENSERVICEURL = -2147219198
AGS_E_NO_CONNECT_INSECURE_TOKENSERVICEURL = -2147219197
AGS_E_SERVICE_STARTED_WITH_ERRORS = -2147219196
AGS_E_REDIRECTION = -2147219195
AGS_E_UPLOAD_IS_TOO_LARGE = -2147219194
agsClientError = c_int # enum
class IServiceUploader(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to properties and members of the Uploader object.'
    _iid_ = GUID('{0FB7B5A0-F5C5-412B-AA10-8D34B2D583D9}')
    _idlflags_ = ['oleautomation']
IServiceUploader._methods_ = [
    COMMETHOD([helpstring(u'.')], HRESULT, 'ServiceUploadFile',
              ( ['in'], BSTR, 'file' ),
              ( ['in'], BSTR, 'Description' ),
              ( ['in'], POINTER(IAGSServerObjectName), 'pTargetService' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( ['retval', 'out'], POINTER(POINTER(IUploadItem)), 'ppUploadItem' )),
]
################################################################
## code template for IServiceUploader implementation
##class IServiceUploader_Impl(object):
##    def ServiceUploadFile(self, file, Description, pTargetService, pTrackCancel):
##        u'.'
##        #return ppUploadItem
##

class IIMSUserRole(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members to get the IMS role of the currently logged in user.'
    _iid_ = GUID('{448631A6-2BDA-4F54-A341-76CC7FFD70A7}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'acUserRole'
acLegacyUser = -1
acBrowser = 0
acPublisher = 1
acServiceAuthor = 2
acAdministrator = 3
acUserRole = c_int # enum
IIMSUserRole._methods_ = [
    COMMETHOD(['propget', helpstring(u'User role.')], HRESULT, 'UserRole',
              ( ['retval', 'out'], POINTER(acUserRole), 'role' )),
    COMMETHOD(['propput', helpstring(u'User role.')], HRESULT, 'UserRole',
              ( ['in'], acUserRole, 'role' )),
]
################################################################
## code template for IIMSUserRole implementation
##class IIMSUserRole_Impl(object):
##    def _get(self):
##        u'User role.'
##        #return role
##    def _set(self, role):
##        u'User role.'
##    UserRole = property(_get, _set, doc = _set.__doc__)
##

class IWMTSConnectionName(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that supply WMTS server connection name information.'
    _iid_ = GUID('{0A014545-E32C-43C2-AA97-243F43294492}')
    _idlflags_ = ['oleautomation']
IWMTSConnectionName._methods_ = [
    COMMETHOD(['propput', helpstring(u'Connection properties that will be used to connect to the WMS server.')], HRESULT, 'ConnectionProperties',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'ConnectionProperties' )),
    COMMETHOD(['propget', helpstring(u'Connection properties that will be used to connect to the WMS server.')], HRESULT, 'ConnectionProperties',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'ConnectionProperties' )),
    COMMETHOD([helpstring(u'Opens the WMS Connection.')], HRESULT, 'OpenEx',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'ppUnknown' )),
]
################################################################
## code template for IWMTSConnectionName implementation
##class IWMTSConnectionName_Impl(object):
##    def OpenEx(self, pTrackCancel):
##        u'Opens the WMS Connection.'
##        #return ppUnknown
##
##    def _get(self):
##        u'Connection properties that will be used to connect to the WMS server.'
##        #return ConnectionProperties
##    def _set(self, ConnectionProperties):
##        u'Connection properties that will be used to connect to the WMS server.'
##    ConnectionProperties = property(_get, _set, doc = _set.__doc__)
##

class WMTSTileMatrixSet(CoClass):
    u'Object that describes a particular set of tile matrices'
    _reg_clsid_ = GUID('{120AD27E-B63C-4503-A37A-1624B715C421}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{746F6817-89BB-4490-9829-83CA25FD505A}', 10, 2)
class IWMTSTileMatrixSet(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods that describe a particular set of tile matrices.'
    _iid_ = GUID('{B7D67EDA-DAF2-49B0-8C27-3C4DF14B69B5}')
    _idlflags_ = ['oleautomation']
WMTSTileMatrixSet._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IWMTSTileMatrixSet]

class IIMSAxlRequest(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control AXL requests to IMS server.'
    _iid_ = GUID('{2844F4EF-098F-4858-80A6-B6A29EB5F140}')
    _idlflags_ = ['oleautomation']
IIMSAxlRequest._methods_ = [
    COMMETHOD([helpstring(u'Sends an Axl request.')], HRESULT, 'SendAxlRequest',
              ( ['in'], BSTR, 'Axl' ),
              ( ['in'], VARIANT_BOOL, 'queryRequest' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'trackCancel' ),
              ( ['in'], VARIANT_BOOL, 'showConnectingAVI' ),
              ( ['in'], VARIANT_BOOL, 'processMessages' ),
              ( ['retval', 'out'], POINTER(BSTR), 'response' )),
    COMMETHOD([helpstring(u'Sends an Axl request and returns a stream.')], HRESULT, 'SendAxlRequestStream',
              ( ['in'], BSTR, 'Axl' ),
              ( ['in'], VARIANT_BOOL, 'queryRequest' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'trackCancel' ),
              ( ['in'], VARIANT_BOOL, 'showConnectingAVI' ),
              ( ['in'], VARIANT_BOOL, 'processMessages' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStream)), 'response' )),
    COMMETHOD([helpstring(u'Sends a command request,i.e.: ConnectorPing.')], HRESULT, 'SendCommandRequest',
              ( ['in'], BSTR, 'command' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'trackCancel' ),
              ( ['in'], VARIANT_BOOL, 'showConnectingAVI' ),
              ( ['in'], VARIANT_BOOL, 'processMessages' ),
              ( ['retval', 'out'], POINTER(BSTR), 'response' )),
    COMMETHOD(['propget', helpstring(u'The ArcIMS server version.')], HRESULT, 'ServerVersion',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'trackCancel' ),
              ( ['in'], VARIANT_BOOL, 'showConnectingAVI' ),
              ( ['in'], VARIANT_BOOL, 'processMessages' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ServerVersion' )),
]
################################################################
## code template for IIMSAxlRequest implementation
##class IIMSAxlRequest_Impl(object):
##    def SendCommandRequest(self, command, trackCancel, showConnectingAVI, processMessages):
##        u'Sends a command request,i.e.: ConnectorPing.'
##        #return response
##
##    def SendAxlRequest(self, Axl, queryRequest, trackCancel, showConnectingAVI, processMessages):
##        u'Sends an Axl request.'
##        #return response
##
##    @property
##    def ServerVersion(self, trackCancel, showConnectingAVI, processMessages):
##        u'The ArcIMS server version.'
##        #return ServerVersion
##
##    def SendAxlRequestStream(self, Axl, queryRequest, trackCancel, showConnectingAVI, processMessages):
##        u'Sends an Axl request and returns a stream.'
##        #return response
##

class WMTSDimension(CoClass):
    u'WMTS Dimension.'
    _reg_clsid_ = GUID('{56122069-7970-4F9F-9E5E-434A5942259A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{746F6817-89BB-4490-9829-83CA25FD505A}', 10, 2)
WMTSDimension._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IWMTSDimension]

class IServerObjectDescription(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods describing the type and class id of the server object.'
    _iid_ = GUID('{FBB35630-AF4A-4423-976A-762D53991E5E}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriAGSConnectionType'
esriAGSConnectionTypeLAN = 1
esriAGSConnectionTypeInternet = 2
esriAGSConnectionTypeRESTAdmin = 3
esriAGSConnectionType = c_int # enum
IServerObjectDescription._methods_ = [
    COMMETHOD(['propget', helpstring(u'Defines the type for the server object.')], HRESULT, 'Type',
              ( ['retval', 'out'], POINTER(BSTR), 'Type' )),
    COMMETHOD(['propget', helpstring(u'The clsid for the client proxy.')], HRESULT, 'ClientProxyCLSID',
              ( ['in'], esriAGSConnectionType, 'connType' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID)), 'ppClsid' )),
]
################################################################
## code template for IServerObjectDescription implementation
##class IServerObjectDescription_Impl(object):
##    @property
##    def Type(self):
##        u'Defines the type for the server object.'
##        #return Type
##
##    @property
##    def ClientProxyCLSID(self, connType):
##        u'The clsid for the client proxy.'
##        #return ppClsid
##

class IIMSMetadataAxlRequest(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control AXL requests to IMS metadata servers.'
    _iid_ = GUID('{64C58B58-B932-4F91-8A60-4A85964AF693}')
    _idlflags_ = ['oleautomation']
IIMSMetadataAxlRequest._methods_ = [
    COMMETHOD([helpstring(u'Sends an Axl request.')], HRESULT, 'SendMetadataAxlRequest',
              ( ['in'], BSTR, 'Axl' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( ['retval', 'out'], POINTER(BSTR), 'response' )),
]
################################################################
## code template for IIMSMetadataAxlRequest implementation
##class IIMSMetadataAxlRequest_Impl(object):
##    def SendMetadataAxlRequest(self, Axl, pTrackCancel):
##        u'Sends an Axl request.'
##        #return response
##

IWMSServiceDescription._methods_ = [
    COMMETHOD(['propget', helpstring(u'Name of WMS Service.')], HRESULT, 'WMSName',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'Abstract of WMS Service.')], HRESULT, 'WMSAbstract',
              ( ['retval', 'out'], POINTER(BSTR), 'Abstract' )),
    COMMETHOD(['propget', helpstring(u'Title of WMS Service.')], HRESULT, 'WMSTitle',
              ( ['retval', 'out'], POINTER(BSTR), 'Title' )),
    COMMETHOD(['propget', helpstring(u'Version of WMS Service.')], HRESULT, 'WMSVersion',
              ( ['retval', 'out'], POINTER(BSTR), 'Title' )),
    COMMETHOD(['propget', helpstring(u'WMS layer count.')], HRESULT, 'LayerDescriptionCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'WMS layer information at the given index.')], HRESULT, 'LayerDescription',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IWMSLayerDescription)), 'ppLayerDescription' )),
    COMMETHOD(['propget', helpstring(u'Supported SRS count.')], HRESULT, 'SRSCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Supported SRS at the given index.')], HRESULT, 'SRS',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'SRS' )),
    COMMETHOD(['propget', helpstring(u'The URL to download the map image from.')], HRESULT, 'ImageRequestUrl',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IArray), 'pLayers' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'pBoundingBox' ),
              ( ['in'], c_int, 'imageWidth' ),
              ( ['in'], c_int, 'imageHeight' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_COLOR, 'bgColor' ),
              ( ['in'], BSTR, 'responseFormat' ),
              ( ['in'], VARIANT_BOOL, 'drawTransparent' ),
              ( ['retval', 'out'], POINTER(BSTR), 'URL' )),
    COMMETHOD(['propget', helpstring(u'The url to download the feature info from.')], HRESULT, 'FeatureInfoRequestURL',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IArray), 'pLayers' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'pBoundingBox' ),
              ( ['in'], c_int, 'imageWidth' ),
              ( ['in'], c_int, 'imageHeight' ),
              ( ['in'], c_int, 'positionX' ),
              ( ['in'], c_int, 'positionY' ),
              ( ['in'], c_int, 'featureCount' ),
              ( ['in'], BSTR, 'responseFormat' ),
              ( ['retval', 'out'], POINTER(BSTR), 'URL' )),
    COMMETHOD(['propget', helpstring(u"Supported GetMap's ImageFormat count.")], HRESULT, 'ImageFormatCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u"Supported GetMap's ImageFormat at the given index.")], HRESULT, 'ImageFormat',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ImageFormat' )),
    COMMETHOD(['propget', helpstring(u'Supported FeatureInfoFormat count.')], HRESULT, 'FeatureInfoFormatCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Supported FeatureInfoFormat at the given index.')], HRESULT, 'FeatureInfoFormat',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ImageFormat' )),
    COMMETHOD(['propget', helpstring(u'Supported exception format count.')], HRESULT, 'ExceptionFormatCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Supported exception at the given index.')], HRESULT, 'ExceptionFormat',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ExceptionFormat' )),
    COMMETHOD(['propget', helpstring(u'Base url for given capability and request method.')], HRESULT, 'BaseURL',
              ( ['in'], BSTR, 'capability' ),
              ( ['in'], BSTR, 'requestMethod' ),
              ( ['retval', 'out'], POINTER(BSTR), 'BaseURL' )),
    COMMETHOD([helpstring(u'Notifies listeners about the URL request made to this WMS Service.')], HRESULT, 'FireWMSRequest',
              ( ['in'], BSTR, 'requestType' ),
              ( ['in'], BSTR, 'requestURL' )),
    COMMETHOD([helpstring(u'Notifies listeners about a valid exception from the WMS Service.')], HRESULT, 'FireWMSException',
              ( ['in'], BSTR, 'requestType' ),
              ( ['in'], BSTR, 'requestURL' ),
              ( ['in'], POINTER(IWMSServiceExceptionHandler), 'pException' )),
]
################################################################
## code template for IWMSServiceDescription implementation
##class IWMSServiceDescription_Impl(object):
##    @property
##    def ImageRequestUrl(self, pLayers, pBoundingBox, imageWidth, imageHeight, bgColor, responseFormat, drawTransparent):
##        u'The URL to download the map image from.'
##        #return URL
##
##    @property
##    def ExceptionFormatCount(self):
##        u'Supported exception format count.'
##        #return Count
##
##    @property
##    def ExceptionFormat(self, index):
##        u'Supported exception at the given index.'
##        #return ExceptionFormat
##
##    @property
##    def WMSTitle(self):
##        u'Title of WMS Service.'
##        #return Title
##
##    @property
##    def ImageFormat(self, index):
##        u"Supported GetMap's ImageFormat at the given index."
##        #return ImageFormat
##
##    @property
##    def FeatureInfoRequestURL(self, pLayers, pBoundingBox, imageWidth, imageHeight, positionX, positionY, featureCount, responseFormat):
##        u'The url to download the feature info from.'
##        #return URL
##
##    def FireWMSException(self, requestType, requestURL, pException):
##        u'Notifies listeners about a valid exception from the WMS Service.'
##        #return 
##
##    @property
##    def ImageFormatCount(self):
##        u"Supported GetMap's ImageFormat count."
##        #return Count
##
##    @property
##    def BaseURL(self, capability, requestMethod):
##        u'Base url for given capability and request method.'
##        #return BaseURL
##
##    @property
##    def FeatureInfoFormat(self, index):
##        u'Supported FeatureInfoFormat at the given index.'
##        #return ImageFormat
##
##    def FireWMSRequest(self, requestType, requestURL):
##        u'Notifies listeners about the URL request made to this WMS Service.'
##        #return 
##
##    @property
##    def SRS(self, index):
##        u'Supported SRS at the given index.'
##        #return SRS
##
##    @property
##    def FeatureInfoFormatCount(self):
##        u'Supported FeatureInfoFormat count.'
##        #return Count
##
##    @property
##    def WMSVersion(self):
##        u'Version of WMS Service.'
##        #return Title
##
##    @property
##    def LayerDescriptionCount(self):
##        u'WMS layer count.'
##        #return Count
##
##    @property
##    def LayerDescription(self, index):
##        u'WMS layer information at the given index.'
##        #return ppLayerDescription
##
##    @property
##    def WMSName(self):
##        u'Name of WMS Service.'
##        #return Name
##
##    @property
##    def WMSAbstract(self):
##        u'Abstract of WMS Service.'
##        #return Abstract
##
##    @property
##    def SRSCount(self):
##        u'Supported SRS count.'
##        #return Count
##

class IAdminUploadsClient(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to properties and members the uploads client object.'
    _iid_ = GUID('{2362AD5F-C545-4BD8-B538-557A1C5B89F1}')
    _idlflags_ = ['oleautomation']
IAdminUploadsClient._methods_ = [
    COMMETHOD([helpstring(u'Uploads a file to the server without breaking it into parts.')], HRESULT, 'AdminUploadFile',
              ( ['in'], BSTR, 'file' ),
              ( ['in'], BSTR, 'Description' ),
              ( ['retval', 'out'], POINTER(POINTER(IUploadItem)), 'ppUploadedItem' )),
    COMMETHOD([helpstring(u'Instruct the server to reserve space for a new upload item, to be uploaded in parts.')], HRESULT, 'AdminRegister',
              ( ['in'], BSTR, 'itemName' ),
              ( ['in'], BSTR, 'Description' ),
              ( ['retval', 'out'], POINTER(POINTER(IUploadItem)), 'ppUploadsItem' )),
    COMMETHOD([helpstring(u'Uploads a part for the upload item.')], HRESULT, 'AdminUploadPart',
              ( ['in'], POINTER(IUploadItem), 'pUploadItem' ),
              ( ['in'], BSTR, 'file' ),
              ( ['in'], c_int, 'uploadPartNumber' ),
              ( ['in'], c_ulonglong, 'offset' ),
              ( ['in'], c_int, 'bytesToWrite' )),
    COMMETHOD([helpstring(u'Returns the numbers of the parts that have already been uploaded for the upload item.')], HRESULT, 'AdminGetPartNumbers',
              ( ['in'], POINTER(IUploadItem), 'pUploadItem' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray)), 'ppPartNumbers' )),
    COMMETHOD([helpstring(u'Commits a registered upload item.')], HRESULT, 'AdminCommit',
              ( ['in'], POINTER(IUploadItem), 'pUploadItem' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray), 'pPartNumbers' )),
    COMMETHOD([helpstring(u'Returns all uploaded items.')], HRESULT, 'GetUploadItems',
              ( ['retval', 'out'], POINTER(POINTER(IEnumUploadItem)), 'ppUploadItems' )),
    COMMETHOD([helpstring(u'Returns the upload item with the given itemID.')], HRESULT, 'GetUploadItem',
              ( ['in'], BSTR, 'ItemID' ),
              ( ['retval', 'out'], POINTER(POINTER(IUploadItem)), 'ppUploadsItem' )),
    COMMETHOD([helpstring(u'Deletes the upload item.')], HRESULT, 'AdminDelete',
              ( ['in'], POINTER(IUploadItem), 'pUploadItem' )),
]
################################################################
## code template for IAdminUploadsClient implementation
##class IAdminUploadsClient_Impl(object):
##    def AdminCommit(self, pUploadItem, pPartNumbers):
##        u'Commits a registered upload item.'
##        #return 
##
##    def AdminRegister(self, itemName, Description):
##        u'Instruct the server to reserve space for a new upload item, to be uploaded in parts.'
##        #return ppUploadsItem
##
##    def AdminDelete(self, pUploadItem):
##        u'Deletes the upload item.'
##        #return 
##
##    def GetUploadItems(self):
##        u'Returns all uploaded items.'
##        #return ppUploadItems
##
##    def AdminUploadPart(self, pUploadItem, file, uploadPartNumber, offset, bytesToWrite):
##        u'Uploads a part for the upload item.'
##        #return 
##
##    def GetUploadItem(self, ItemID):
##        u'Returns the upload item with the given itemID.'
##        #return ppUploadsItem
##
##    def AdminGetPartNumbers(self, pUploadItem):
##        u'Returns the numbers of the parts that have already been uploaded for the upload item.'
##        #return ppPartNumbers
##
##    def AdminUploadFile(self, file, Description):
##        u'Uploads a file to the server without breaking it into parts.'
##        #return ppUploadedItem
##

IUploadItem._methods_ = [
    COMMETHOD(['propput', helpstring(u'The name of the uploaded item.')], HRESULT, 'Name',
              ( ['in'], BSTR, 'pName' )),
    COMMETHOD(['propget', helpstring(u'The name of the uploaded item.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pName' )),
    COMMETHOD(['propput', helpstring(u'The ID of the uploaded item.')], HRESULT, 'ID',
              ( ['in'], BSTR, 'pItemID' )),
    COMMETHOD(['propget', helpstring(u'The ID of the uploaded item.')], HRESULT, 'ID',
              ( ['retval', 'out'], POINTER(BSTR), 'pItemID' )),
    COMMETHOD(['propput', helpstring(u'The path of this uploaded item.')], HRESULT, 'FilePath',
              ( ['in'], BSTR, 'pPath' )),
    COMMETHOD(['propget', helpstring(u'The path of this uploaded item.')], HRESULT, 'FilePath',
              ( ['retval', 'out'], POINTER(BSTR), 'pPath' )),
    COMMETHOD(['propput', helpstring(u'The path of this uploaded item on server.')], HRESULT, 'PathOnServer',
              ( ['in'], BSTR, 'pPathOnServer' )),
    COMMETHOD(['propget', helpstring(u'The path of this uploaded item on server.')], HRESULT, 'PathOnServer',
              ( ['retval', 'out'], POINTER(BSTR), 'pPathOnServer' )),
    COMMETHOD(['propput', helpstring(u'The description of the uploaded item.')], HRESULT, 'Description',
              ( ['in'], BSTR, 'pDesc' )),
    COMMETHOD(['propget', helpstring(u'The description of the uploaded item.')], HRESULT, 'Description',
              ( ['retval', 'out'], POINTER(BSTR), 'pDesc' )),
    COMMETHOD(['propput', helpstring(u"The date for the upload (in the server's time zone).")], HRESULT, 'Date',
              ( ['in'], c_double, 'pDate' )),
    COMMETHOD(['propget', helpstring(u"The date for the upload (in the server's time zone).")], HRESULT, 'Date',
              ( ['retval', 'out'], POINTER(c_double), 'pDate' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the upload item has been committed.')], HRESULT, 'Committed',
              ( ['in'], VARIANT_BOOL, 'Committed' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the upload item has been committed.')], HRESULT, 'Committed',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Committed' )),
]
################################################################
## code template for IUploadItem implementation
##class IUploadItem_Impl(object):
##    def _get(self):
##        u'The name of the uploaded item.'
##        #return pName
##    def _set(self, pName):
##        u'The name of the uploaded item.'
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The path of this uploaded item.'
##        #return pPath
##    def _set(self, pPath):
##        u'The path of this uploaded item.'
##    FilePath = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The path of this uploaded item on server.'
##        #return pPathOnServer
##    def _set(self, pPathOnServer):
##        u'The path of this uploaded item on server.'
##    PathOnServer = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the upload item has been committed.'
##        #return Committed
##    def _set(self, Committed):
##        u'Indicates if the upload item has been committed.'
##    Committed = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u"The date for the upload (in the server's time zone)."
##        #return pDate
##    def _set(self, pDate):
##        u"The date for the upload (in the server's time zone)."
##    Date = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The ID of the uploaded item.'
##        #return pItemID
##    def _set(self, pItemID):
##        u'The ID of the uploaded item.'
##    ID = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The description of the uploaded item.'
##        #return pDesc
##    def _set(self, pDesc):
##        u'The description of the uploaded item.'
##    Description = property(_get, _set, doc = _set.__doc__)
##

IWMSConnection._methods_ = [
    COMMETHOD(['propget', helpstring(u'Name of the connection.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propput', helpstring(u'Name of the connection.')], HRESULT, 'Name',
              ( [], BSTR, 'Name' )),
    COMMETHOD(['propget', helpstring(u'Complete information required to connect to a WMS server..')], HRESULT, 'FullName',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName)), 'ppName' )),
    COMMETHOD(['propputref', helpstring(u'Complete information required to connect to a WMS server..')], HRESULT, 'FullName',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName), 'ppName' )),
]
################################################################
## code template for IWMSConnection implementation
##class IWMSConnection_Impl(object):
##    def FullName(self, ppName):
##        u'Complete information required to connect to a WMS server..'
##        #return 
##
##    def _get(self):
##        u'Name of the connection.'
##        #return Name
##    def _set(self, Name):
##        u'Name of the connection.'
##    Name = property(_get, _set, doc = _set.__doc__)
##

class IMSMetadataServiceName(CoClass):
    u'ArIMS Metadata Service Name Object.'
    _reg_clsid_ = GUID('{D2B6FCE3-3F56-478B-8125-177B3373A634}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{746F6817-89BB-4490-9829-83CA25FD505A}', 10, 2)
class IRemoteMetadataName(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members to manipulate information specific to metadata stored in an ArcIMS Metadata Server.'
    _iid_ = GUID('{C7535706-3898-419C-B65B-9FAF0D8BFC83}')
    _idlflags_ = ['oleautomation']
class IRemoteMetadataName2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members to manipulate information specific to metadata stored in an ArcIMS Metadata Server.'
    _iid_ = GUID('{EDC3739D-807F-47EA-978D-E6AE0FC67018}')
    _idlflags_ = ['oleautomation']
IMSMetadataServiceName._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IIMSServiceDescription, IIMSAxlRequest, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, IRemoteMetadataName, IIMSMetadataAxlRequest, IIMSUserRole, IRemoteMetadataName2]

class IWCSClientEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to events that occur when a URL request is made to the WCS server.'
    _iid_ = GUID('{C8CD44B2-4412-4A12-BDED-7225D81056C4}')
    _idlflags_ = ['oleautomation']
IWCSClientEvents._methods_ = [
    COMMETHOD([helpstring(u'Fired when the an URL request is made to WCS server.')], HRESULT, 'WCSRequest',
              ( ['in'], POINTER(IWCSServiceDescription), 'pService' ),
              ( ['in'], BSTR, 'requestType' ),
              ( ['in'], BSTR, 'requestURL' )),
    COMMETHOD([helpstring(u'Fired when the an URL request is made to WCS server and the server fails with a valid exception.')], HRESULT, 'WCSException',
              ( ['in'], POINTER(IWCSServiceDescription), 'pService' ),
              ( ['in'], BSTR, 'requestType' ),
              ( ['in'], BSTR, 'requestURL' ),
              ( ['in'], POINTER(IWCSServiceExceptionHandler), 'pException' )),
]
################################################################
## code template for IWCSClientEvents implementation
##class IWCSClientEvents_Impl(object):
##    def WCSException(self, pService, requestType, requestURL, pException):
##        u'Fired when the an URL request is made to WCS server and the server fails with a valid exception.'
##        #return 
##
##    def WCSRequest(self, pService, requestType, requestURL):
##        u'Fired when the an URL request is made to WCS server.'
##        #return 
##


# values for enumeration 'acIndexStatus'
acNotIndexed = 0
acIndexed = 1
acIndexError = 2
acIndexStatus = c_int # enum
IRemoteMetadataName._methods_ = [
    COMMETHOD(['propput', helpstring(u'Name of metadata document on server.')], HRESULT, 'Dataset',
              ( ['in'], BSTR, 'pDataset' )),
    COMMETHOD(['propget', helpstring(u'Name of metadata document on server.')], HRESULT, 'Dataset',
              ( ['retval', 'out'], POINTER(BSTR), 'pDataset' )),
    COMMETHOD(['propput', helpstring(u'ArcIMS authenticated user owning metadata document.')], HRESULT, 'Owner',
              ( ['in'], BSTR, 'pOwner' )),
    COMMETHOD(['propget', helpstring(u'ArcIMS authenticated user owning metadata document.')], HRESULT, 'Owner',
              ( ['retval', 'out'], POINTER(BSTR), 'pOwner' )),
    COMMETHOD(['propput', helpstring(u'Unique id (UUID) of metadata document.')], HRESULT, 'UserID',
              ( ['in'], BSTR, 'pUserID' )),
    COMMETHOD(['propget', helpstring(u'Unique id (UUID) of metadata document.')], HRESULT, 'UserID',
              ( ['retval', 'out'], POINTER(BSTR), 'pUserID' )),
    COMMETHOD(['propput', helpstring(u'Name of parent of metadata document on server.')], HRESULT, 'ParentDataset',
              ( ['in'], BSTR, 'pDataset' )),
    COMMETHOD(['propget', helpstring(u'Name of parent of metadata document on server.')], HRESULT, 'ParentDataset',
              ( ['retval', 'out'], POINTER(BSTR), 'pDataset' )),
    COMMETHOD(['propput', helpstring(u'ArcIMS authenticated user owning parent of metadata document.')], HRESULT, 'ParentOwner',
              ( ['in'], BSTR, 'pOwner' )),
    COMMETHOD(['propget', helpstring(u'ArcIMS authenticated user owning parent of metadata document.')], HRESULT, 'ParentOwner',
              ( ['retval', 'out'], POINTER(BSTR), 'pOwner' )),
    COMMETHOD(['propput', helpstring(u'Unique id (UUID) of parent of metadata document.')], HRESULT, 'ParentUserID',
              ( ['in'], BSTR, 'pUserID' )),
    COMMETHOD(['propget', helpstring(u'Unique id (UUID) of parent of metadata document.')], HRESULT, 'ParentUserID',
              ( ['retval', 'out'], POINTER(BSTR), 'pUserID' )),
    COMMETHOD(['propput', helpstring(u'URL of metadata document on server.')], HRESULT, 'MetadataURL',
              ( ['in'], BSTR, 'pUrl' )),
    COMMETHOD(['propget', helpstring(u'URL of metadata document on server.')], HRESULT, 'MetadataURL',
              ( ['retval', 'out'], POINTER(BSTR), 'pUrl' )),
    COMMETHOD(['propput', helpstring(u'URL of thumbnail image on server.')], HRESULT, 'ThumbnailURL',
              ( ['in'], BSTR, 'pUrl' )),
    COMMETHOD(['propget', helpstring(u'URL of thumbnail image on server.')], HRESULT, 'ThumbnailURL',
              ( ['retval', 'out'], POINTER(BSTR), 'pUrl' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether this metadata document is a folder.')], HRESULT, 'isFolder',
              ( ['in'], VARIANT_BOOL, 'pIsFolder' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether this metadata document is a folder.')], HRESULT, 'isFolder',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pIsFolder' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether this metadata document is the root document.')], HRESULT, 'IsRoot',
              ( ['in'], VARIANT_BOOL, 'pIsRoot' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether this metadata document is the root document.')], HRESULT, 'IsRoot',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pIsRoot' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether this metadata document is private.')], HRESULT, 'IsPrivateDocument',
              ( ['in'], VARIANT_BOOL, 'pIsPrivate' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether this metadata document is private.')], HRESULT, 'IsPrivateDocument',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pIsPrivate' )),
    COMMETHOD(['propput', helpstring(u'The number of references to this document on the server.')], HRESULT, 'RefCount',
              ( ['in'], c_int, 'pRefCount' )),
    COMMETHOD(['propget', helpstring(u'The number of references to this document on the server.')], HRESULT, 'RefCount',
              ( ['retval', 'out'], POINTER(c_int), 'pRefCount' )),
    COMMETHOD(['propputref', helpstring(u'The extent of the dataset represented by this document.')], HRESULT, 'Extent',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'ppExtent' )),
    COMMETHOD(['propget', helpstring(u'The extent of the dataset represented by this document.')], HRESULT, 'Extent',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'ppExtent' )),
    COMMETHOD(['propput', helpstring(u'The online linkage contained within this document.')], HRESULT, 'Onlink',
              ( ['in'], BSTR, 'Onlink' )),
    COMMETHOD(['propget', helpstring(u'The online linkage contained within this document.')], HRESULT, 'Onlink',
              ( ['retval', 'out'], POINTER(BSTR), 'Onlink' )),
    COMMETHOD(['propput', helpstring(u'The URL of the ArcIMS server running the service represented by this document.')], HRESULT, 'server',
              ( ['in'], BSTR, 'server' )),
    COMMETHOD(['propget', helpstring(u'The URL of the ArcIMS server running the service represented by this document.')], HRESULT, 'server',
              ( ['retval', 'out'], POINTER(BSTR), 'server' )),
    COMMETHOD(['propput', helpstring(u'The name of the ArcIMS service represented by this document.')], HRESULT, 'Service',
              ( ['in'], BSTR, 'Service' )),
    COMMETHOD(['propget', helpstring(u'The name of the ArcIMS service represented by this document.')], HRESULT, 'Service',
              ( ['retval', 'out'], POINTER(BSTR), 'Service' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether this document is indexed on the server.')], HRESULT, 'IndexStatus',
              ( ['retval', 'out'], POINTER(acIndexStatus), 'pIndexStatus' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether this document is indexed on the server.')], HRESULT, 'IndexStatus',
              ( ['in'], acIndexStatus, 'pIndexStatus' )),
]
################################################################
## code template for IRemoteMetadataName implementation
##class IRemoteMetadataName_Impl(object):
##    def _get(self):
##        u'URL of metadata document on server.'
##        #return pUrl
##    def _set(self, pUrl):
##        u'URL of metadata document on server.'
##    MetadataURL = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Extent(self, ppExtent):
##        u'The extent of the dataset represented by this document.'
##        #return 
##
##    def _get(self):
##        u'Indicates whether this metadata document is private.'
##        #return pIsPrivate
##    def _set(self, pIsPrivate):
##        u'Indicates whether this metadata document is private.'
##    IsPrivateDocument = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Name of parent of metadata document on server.'
##        #return pDataset
##    def _set(self, pDataset):
##        u'Name of parent of metadata document on server.'
##    ParentDataset = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Unique id (UUID) of parent of metadata document.'
##        #return pUserID
##    def _set(self, pUserID):
##        u'Unique id (UUID) of parent of metadata document.'
##    ParentUserID = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether this metadata document is a folder.'
##        #return pIsFolder
##    def _set(self, pIsFolder):
##        u'Indicates whether this metadata document is a folder.'
##    isFolder = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The name of the ArcIMS service represented by this document.'
##        #return Service
##    def _set(self, Service):
##        u'The name of the ArcIMS service represented by this document.'
##    Service = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Unique id (UUID) of metadata document.'
##        #return pUserID
##    def _set(self, pUserID):
##        u'Unique id (UUID) of metadata document.'
##    UserID = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The URL of the ArcIMS server running the service represented by this document.'
##        #return server
##    def _set(self, server):
##        u'The URL of the ArcIMS server running the service represented by this document.'
##    server = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Name of metadata document on server.'
##        #return pDataset
##    def _set(self, pDataset):
##        u'Name of metadata document on server.'
##    Dataset = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The number of references to this document on the server.'
##        #return pRefCount
##    def _set(self, pRefCount):
##        u'The number of references to this document on the server.'
##    RefCount = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether this metadata document is the root document.'
##        #return pIsRoot
##    def _set(self, pIsRoot):
##        u'Indicates whether this metadata document is the root document.'
##    IsRoot = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'ArcIMS authenticated user owning parent of metadata document.'
##        #return pOwner
##    def _set(self, pOwner):
##        u'ArcIMS authenticated user owning parent of metadata document.'
##    ParentOwner = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether this document is indexed on the server.'
##        #return pIndexStatus
##    def _set(self, pIndexStatus):
##        u'Indicates whether this document is indexed on the server.'
##    IndexStatus = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'ArcIMS authenticated user owning metadata document.'
##        #return pOwner
##    def _set(self, pOwner):
##        u'ArcIMS authenticated user owning metadata document.'
##    Owner = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The online linkage contained within this document.'
##        #return Onlink
##    def _set(self, Onlink):
##        u'The online linkage contained within this document.'
##    Onlink = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'URL of thumbnail image on server.'
##        #return pUrl
##    def _set(self, pUrl):
##        u'URL of thumbnail image on server.'
##    ThumbnailURL = property(_get, _set, doc = _set.__doc__)
##

IWMSLayerDescription._methods_ = [
    COMMETHOD(['propget', helpstring(u'Name of WMS layer.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'Title of WMS layer.')], HRESULT, 'Title',
              ( ['retval', 'out'], POINTER(BSTR), 'Title' )),
    COMMETHOD(['propget', helpstring(u'Abstract of the WMS layer.')], HRESULT, 'Abstract',
              ( ['retval', 'out'], POINTER(BSTR), 'Abstract' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the layer is queryable.')], HRESULT, 'IsQueryable',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'isQuaryable' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the layer is opaque or transparent in terms of the area that gets drawn.')], HRESULT, 'IsOpaque',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsOpaque' )),
    COMMETHOD(['propget', helpstring(u'Indicates the number of times the layer has been reserved.')], HRESULT, 'IsCascaded',
              ( ['retval', 'out'], POINTER(c_int), 'IsCascaded' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether or not the server will be able to crop the data to a geographic area smaller than its enclosing bounding box.')], HRESULT, 'IsSubsettable',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsSubsettable' )),
    COMMETHOD(['propget', helpstring(u'Fixed width at which server is able to display the layer. If this is zero, server can display the layer at any resolution.')], HRESULT, 'FixedWidth',
              ( ['retval', 'out'], POINTER(c_double), 'Width' )),
    COMMETHOD(['propget', helpstring(u'Fixed height at which server is able to display the layer. If this is zero, server can display the layer at any resolution.')], HRESULT, 'FixedHeight',
              ( ['retval', 'out'], POINTER(c_double), 'Height' )),
    COMMETHOD(['propget', helpstring(u'Number of WMSLayerDescriptions.')], HRESULT, 'LayerDescriptionCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'WMSLayerDescription at a given index.')], HRESULT, 'LayerDescription',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IWMSLayerDescription)), 'ppLayerDescription' )),
    COMMETHOD(['propget', helpstring(u'Suggested minimimum scale for the WMS layer.')], HRESULT, 'ScaleHintMin',
              ( ['retval', 'out'], POINTER(c_double), 'Scale' )),
    COMMETHOD(['propget', helpstring(u'Suggested maximum scale of the WMS layer.')], HRESULT, 'ScaleHintMax',
              ( ['retval', 'out'], POINTER(c_double), 'Scale' )),
    COMMETHOD(['propget', helpstring(u'Minimum bounding extent of the layer data in EPSG:4326.')], HRESULT, 'LatLongBoundingBox',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'envelope' )),
    COMMETHOD(['propget', helpstring(u'Number of bounding extents of the layer.')], HRESULT, 'BoundingBoxCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Minimum bounding extents of the layer data along with the applicable SRS.')], HRESULT, 'BoundingBox',
              ( ['in'], c_int, 'index' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'envelope' ),
              ( ['out'], POINTER(BSTR), 'srsCode' )),
    COMMETHOD(['propget', helpstring(u'Number of styles in the layer.')], HRESULT, 'StyleDescriptionCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Style of the layer at the given index.')], HRESULT, 'StyleDescription',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IWMSLayerStyleDescription)), 'StyleDescription' )),
    COMMETHOD(['propget', helpstring(u'Supported SRS count.')], HRESULT, 'SRSCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Supproted SRS at the given index.')], HRESULT, 'SRS',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'SRS' )),
    COMMETHOD(['propget', helpstring(u'WMS Version.')], HRESULT, 'WMSVersion',
              ( ['retval', 'out'], POINTER(BSTR), 'WMSVersion' )),
    COMMETHOD(['propget', helpstring(u"Supported GetMap's ImageFormat count.")], HRESULT, 'ImageFormatCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u"Supported GetMap's ImageFormat at the given index.")], HRESULT, 'ImageFormat',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ImageFormat' )),
    COMMETHOD(['propget', helpstring(u'Supported FeatureInfoFormat count.')], HRESULT, 'FeatureInfoFormatCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Supported FeatureInfoFormat at the given index.')], HRESULT, 'FeatureInfoFormat',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ImageFormat' )),
    COMMETHOD(['propget', helpstring(u'Supported exception format count.')], HRESULT, 'ExceptionFormatCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Supported exception at the given index.')], HRESULT, 'ExceptionFormat',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ExceptionFormat' )),
]
################################################################
## code template for IWMSLayerDescription implementation
##class IWMSLayerDescription_Impl(object):
##    @property
##    def IsCascaded(self):
##        u'Indicates the number of times the layer has been reserved.'
##        #return IsCascaded
##
##    @property
##    def ExceptionFormat(self, index):
##        u'Supported exception at the given index.'
##        #return ExceptionFormat
##
##    @property
##    def Title(self):
##        u'Title of WMS layer.'
##        #return Title
##
##    @property
##    def ExceptionFormatCount(self):
##        u'Supported exception format count.'
##        #return Count
##
##    @property
##    def ScaleHintMin(self):
##        u'Suggested minimimum scale for the WMS layer.'
##        #return Scale
##
##    @property
##    def ImageFormat(self, index):
##        u"Supported GetMap's ImageFormat at the given index."
##        #return ImageFormat
##
##    @property
##    def ScaleHintMax(self):
##        u'Suggested maximum scale of the WMS layer.'
##        #return Scale
##
##    @property
##    def FixedWidth(self):
##        u'Fixed width at which server is able to display the layer. If this is zero, server can display the layer at any resolution.'
##        #return Width
##
##    @property
##    def FeatureInfoFormat(self, index):
##        u'Supported FeatureInfoFormat at the given index.'
##        #return ImageFormat
##
##    @property
##    def IsOpaque(self):
##        u'Indicates whether the layer is opaque or transparent in terms of the area that gets drawn.'
##        #return IsOpaque
##
##    @property
##    def StyleDescription(self, index):
##        u'Style of the layer at the given index.'
##        #return StyleDescription
##
##    @property
##    def LayerDescriptionCount(self):
##        u'Number of WMSLayerDescriptions.'
##        #return Count
##
##    @property
##    def FixedHeight(self):
##        u'Fixed height at which server is able to display the layer. If this is zero, server can display the layer at any resolution.'
##        #return Height
##
##    @property
##    def SRSCount(self):
##        u'Supported SRS count.'
##        #return Count
##
##    @property
##    def Name(self):
##        u'Name of WMS layer.'
##        #return Name
##
##    @property
##    def IsQueryable(self):
##        u'Indicates whether the layer is queryable.'
##        #return isQuaryable
##
##    @property
##    def ImageFormatCount(self):
##        u"Supported GetMap's ImageFormat count."
##        #return Count
##
##    @property
##    def LatLongBoundingBox(self):
##        u'Minimum bounding extent of the layer data in EPSG:4326.'
##        #return envelope
##
##    @property
##    def SRS(self, index):
##        u'Supproted SRS at the given index.'
##        #return SRS
##
##    @property
##    def WMSVersion(self):
##        u'WMS Version.'
##        #return WMSVersion
##
##    @property
##    def StyleDescriptionCount(self):
##        u'Number of styles in the layer.'
##        #return Count
##
##    @property
##    def IsSubsettable(self):
##        u'Indicates whether or not the server will be able to crop the data to a geographic area smaller than its enclosing bounding box.'
##        #return IsSubsettable
##
##    @property
##    def BoundingBoxCount(self):
##        u'Number of bounding extents of the layer.'
##        #return Count
##
##    @property
##    def Abstract(self):
##        u'Abstract of the WMS layer.'
##        #return Abstract
##
##    @property
##    def FeatureInfoFormatCount(self):
##        u'Supported FeatureInfoFormat count.'
##        #return Count
##
##    @property
##    def LayerDescription(self, index):
##        u'WMSLayerDescription at a given index.'
##        #return ppLayerDescription
##
##    @property
##    def BoundingBox(self, index):
##        u'Minimum bounding extents of the layer data along with the applicable SRS.'
##        #return envelope, srsCode
##

IWMSConnectionFactory._methods_ = [
    COMMETHOD([helpstring(u'Opens a WMS connection for the given properties.')], HRESULT, 'Open',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'pConnectionProperties' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hWnd' ),
              ( [], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( ['retval', 'out'], POINTER(POINTER(IWMSConnection)), 'ppConnection' )),
]
################################################################
## code template for IWMSConnectionFactory implementation
##class IWMSConnectionFactory_Impl(object):
##    def Open(self, pConnectionProperties, hWnd, pTrackCancel):
##        u'Opens a WMS connection for the given properties.'
##        #return ppConnection
##

IWCSConnectionFactory._methods_ = [
    COMMETHOD([helpstring(u'Opens an WCS connection for the given properties.')], HRESULT, 'Open',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'pConnectionProperties' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hWnd' ),
              ( [], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( ['retval', 'out'], POINTER(POINTER(IWCSConnection)), 'ppConnection' )),
]
################################################################
## code template for IWCSConnectionFactory implementation
##class IWCSConnectionFactory_Impl(object):
##    def Open(self, pConnectionProperties, hWnd, pTrackCancel):
##        u'Opens an WCS connection for the given properties.'
##        #return ppConnection
##

class IMSCatalogPathParser(CoClass):
    u'IMSGIS Server Catalog Path Parser.'
    _reg_clsid_ = GUID('{D6BA032F-5391-445A-A012-ABA4A0AD5B4E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{746F6817-89BB-4490-9829-83CA25FD505A}', 10, 2)
IMSCatalogPathParser._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IParseNameString]

IWMTSConnection._methods_ = [
    COMMETHOD(['propget', helpstring(u'Name of the connection.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propput', helpstring(u'Name of the connection.')], HRESULT, 'Name',
              ( [], BSTR, 'Name' )),
    COMMETHOD(['propget', helpstring(u'Complete information required to connect to a WMTS server..')], HRESULT, 'FullName',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName)), 'ppName' )),
    COMMETHOD(['propputref', helpstring(u'Complete information required to connect to a WMTS server..')], HRESULT, 'FullName',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName), 'ppName' )),
]
################################################################
## code template for IWMTSConnection implementation
##class IWMTSConnection_Impl(object):
##    def FullName(self, ppName):
##        u'Complete information required to connect to a WMTS server..'
##        #return 
##
##    def _get(self):
##        u'Name of the connection.'
##        #return Name
##    def _set(self, Name):
##        u'Name of the connection.'
##    Name = property(_get, _set, doc = _set.__doc__)
##

IWMTSConnectionFactory._methods_ = [
    COMMETHOD([helpstring(u'Opens a WMTS connection for the given properties.')], HRESULT, 'Open',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'pConnectionProperties' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hWnd' ),
              ( [], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( ['retval', 'out'], POINTER(POINTER(IWMTSConnection)), 'ppConnection' )),
]
################################################################
## code template for IWMTSConnectionFactory implementation
##class IWMTSConnectionFactory_Impl(object):
##    def Open(self, pConnectionProperties, hWnd, pTrackCancel):
##        u'Opens a WMTS connection for the given properties.'
##        #return ppConnection
##

class IUploadsClient(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to properties and members the uploads client object.'
    _iid_ = GUID('{EDB37AFF-C199-4063-AB1F-FE936D5B5FD0}')
    _idlflags_ = ['oleautomation']
IUploadsClient._methods_ = [
    COMMETHOD([helpstring(u'Initializes the uploads client object.')], HRESULT, 'Init',
              ( ['in'], POINTER(IAGSServerConnection), 'pConn' )),
    COMMETHOD(['propput', helpstring(u'.')], HRESULT, 'TimeoutInSecs',
              ( ['in'], c_int, 'pTimeout' )),
    COMMETHOD(['propget', helpstring(u'.')], HRESULT, 'TimeoutInSecs',
              ( ['retval', 'out'], POINTER(c_int), 'pTimeout' )),
]
################################################################
## code template for IUploadsClient implementation
##class IUploadsClient_Impl(object):
##    def Init(self, pConn):
##        u'Initializes the uploads client object.'
##        #return 
##
##    def _get(self):
##        u'.'
##        #return pTimeout
##    def _set(self, pTimeout):
##        u'.'
##    TimeoutInSecs = property(_get, _set, doc = _set.__doc__)
##

class IMSServiceName(CoClass):
    u'The IMS Service Name.'
    _reg_clsid_ = GUID('{630F3DE8-E213-4A5E-AC01-2BD5BCD646B6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{746F6817-89BB-4490-9829-83CA25FD505A}', 10, 2)
IMSServiceName._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IIMSServiceDescription, IIMSAxlRequest, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, IIMSUserRole, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITestConnection]

IWMTSTileMatrixSetLink._methods_ = [
    COMMETHOD(['propget', helpstring(u'Identifier for the TileMatrix.')], HRESULT, 'TileMatrixSet',
              ( ['retval', 'out'], POINTER(BSTR), 'ID' )),
    COMMETHOD(['propget', helpstring(u'TileMatrixSetLimits count.')], HRESULT, 'TileMatrixSetLimitsCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'TileMatrixLimits that describe the availble tile for this layer.')], HRESULT, 'TileMatrixSetLimits',
              ( ['in'], c_int, 'ix' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'limitsAsProps' )),
]
################################################################
## code template for IWMTSTileMatrixSetLink implementation
##class IWMTSTileMatrixSetLink_Impl(object):
##    @property
##    def TileMatrixSetLimitsCount(self):
##        u'TileMatrixSetLimits count.'
##        #return Count
##
##    @property
##    def TileMatrixSet(self):
##        u'Identifier for the TileMatrix.'
##        #return ID
##
##    @property
##    def TileMatrixSetLimits(self, ix):
##        u'TileMatrixLimits that describe the availble tile for this layer.'
##        #return limitsAsProps
##

class WMTSConnectionName(CoClass):
    u'The WMTS Connection name.'
    _reg_clsid_ = GUID('{93B061BB-DB92-4E90-9927-48C031B33FE8}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{746F6817-89BB-4490-9829-83CA25FD505A}', 10, 2)
WMTSConnectionName._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IWMTSConnectionName, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName]

class IAdminUploader(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to properties and members of the Uploader object.'
    _iid_ = GUID('{657E7708-500D-47EC-8E96-2327083ECDC0}')
    _idlflags_ = ['oleautomation']
IAdminUploader._methods_ = [
    COMMETHOD([helpstring(u'.')], HRESULT, 'AdminUploadFile',
              ( ['in'], BSTR, 'file' ),
              ( ['in'], BSTR, 'Description' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( ['retval', 'out'], POINTER(POINTER(IUploadItem)), 'ppUploadItem' )),
]
################################################################
## code template for IAdminUploader implementation
##class IAdminUploader_Impl(object):
##    def AdminUploadFile(self, file, Description, pTrackCancel):
##        u'.'
##        #return ppUploadItem
##

class IWCSCoverageDescription(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members give access to WCSCoverageDescription information.'
    _iid_ = GUID('{165F657D-6E52-4CE6-984A-7300ACB2E291}')
    _idlflags_ = ['oleautomation']
IWCSServiceDescription._methods_ = [
    COMMETHOD(['propget', helpstring(u'Name of WCS Service.')], HRESULT, 'WCSName',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'Abstract of WCS Service.')], HRESULT, 'Abstract',
              ( ['retval', 'out'], POINTER(BSTR), 'Abstract' )),
    COMMETHOD(['propget', helpstring(u'Title of WCS Service.')], HRESULT, 'Title',
              ( ['retval', 'out'], POINTER(BSTR), 'Title' )),
    COMMETHOD(['propget', helpstring(u'Default version of WCS Service.')], HRESULT, 'Version',
              ( ['retval', 'out'], POINTER(BSTR), 'ver' )),
    COMMETHOD(['propget', helpstring(u'Constrains to access to this WCS Service.')], HRESULT, 'AccessConstrains',
              ( ['retval', 'out'], POINTER(BSTR), 'constrains' )),
    COMMETHOD(['propget', helpstring(u'Base url for given capability and request method.')], HRESULT, 'BaseURL',
              ( ['in'], BSTR, 'capability' ),
              ( ['in'], BSTR, 'requestMethod' ),
              ( ['retval', 'out'], POINTER(BSTR), 'BaseURL' )),
    COMMETHOD(['propget', helpstring(u'Supported exception format count.')], HRESULT, 'ExceptionFormatCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Supported exception at the given index.')], HRESULT, 'ExceptionFormat',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ExceptionFormat' )),
    COMMETHOD(['propget', helpstring(u'Supported versions count.')], HRESULT, 'SupportedVersionsCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Supported version at the given index.')], HRESULT, 'SupportedVersion',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Version' )),
    COMMETHOD(['propget', helpstring(u'Available keyword count.')], HRESULT, 'KeywordCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Available keyword at the given index.')], HRESULT, 'Keyword',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Keyword' )),
    COMMETHOD(['propget', helpstring(u'WCS coverage count.')], HRESULT, 'CoverageDescriptionCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'WCS coverage information at the given index.')], HRESULT, 'CoverageDescriptionByIndex',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IWCSCoverageDescription)), 'ppCoverageDescription' )),
    COMMETHOD(['propget', helpstring(u'CoverageDescription by name.')], HRESULT, 'CoverageDescriptionByName',
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(POINTER(IWCSCoverageDescription)), 'ppCoverageDescription' )),
    COMMETHOD(['propget', helpstring(u'The URL to download the coverage from.')], HRESULT, 'CoverageRequestUrl',
              ( ['in'], BSTR, 'coverageName' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'pBoundingBox' ),
              ( ['in'], BSTR, 'CRS' ),
              ( ['in'], BSTR, 'responseFormat' ),
              ( ['in'], c_int, 'imageWidth' ),
              ( ['in'], c_int, 'imageHeight' ),
              ( ['retval', 'out'], POINTER(BSTR), 'URL' )),
    COMMETHOD([helpstring(u'Notifies listeners about the URL request made to this WCS Service.')], HRESULT, 'FireWCSRequest',
              ( ['in'], BSTR, 'requestType' ),
              ( ['in'], BSTR, 'requestURL' )),
    COMMETHOD([helpstring(u'Notifies listeners about a valid exception from the WCS Service.')], HRESULT, 'FireWCSException',
              ( ['in'], BSTR, 'requestType' ),
              ( ['in'], BSTR, 'requestURL' ),
              ( ['in'], POINTER(IWCSServiceExceptionHandler), 'pException' )),
]
################################################################
## code template for IWCSServiceDescription implementation
##class IWCSServiceDescription_Impl(object):
##    def FireWCSException(self, requestType, requestURL, pException):
##        u'Notifies listeners about a valid exception from the WCS Service.'
##        #return 
##
##    @property
##    def CoverageRequestUrl(self, coverageName, pBoundingBox, CRS, responseFormat, imageWidth, imageHeight):
##        u'The URL to download the coverage from.'
##        #return URL
##
##    @property
##    def ExceptionFormat(self, index):
##        u'Supported exception at the given index.'
##        #return ExceptionFormat
##
##    @property
##    def Keyword(self, index):
##        u'Available keyword at the given index.'
##        #return Keyword
##
##    @property
##    def Title(self):
##        u'Title of WCS Service.'
##        #return Title
##
##    @property
##    def SupportedVersionsCount(self):
##        u'Supported versions count.'
##        #return Count
##
##    @property
##    def Abstract(self):
##        u'Abstract of WCS Service.'
##        #return Abstract
##
##    @property
##    def ExceptionFormatCount(self):
##        u'Supported exception format count.'
##        #return Count
##
##    def FireWCSRequest(self, requestType, requestURL):
##        u'Notifies listeners about the URL request made to this WCS Service.'
##        #return 
##
##    @property
##    def BaseURL(self, capability, requestMethod):
##        u'Base url for given capability and request method.'
##        #return BaseURL
##
##    @property
##    def SupportedVersion(self, index):
##        u'Supported version at the given index.'
##        #return Version
##
##    @property
##    def CoverageDescriptionByIndex(self, index):
##        u'WCS coverage information at the given index.'
##        #return ppCoverageDescription
##
##    @property
##    def Version(self):
##        u'Default version of WCS Service.'
##        #return ver
##
##    @property
##    def CoverageDescriptionCount(self):
##        u'WCS coverage count.'
##        #return Count
##
##    @property
##    def CoverageDescriptionByName(self, Name):
##        u'CoverageDescription by name.'
##        #return ppCoverageDescription
##
##    @property
##    def AccessConstrains(self):
##        u'Constrains to access to this WCS Service.'
##        #return constrains
##
##    @property
##    def KeywordCount(self):
##        u'Available keyword count.'
##        #return Count
##
##    @property
##    def WCSName(self):
##        u'Name of WCS Service.'
##        #return Name
##

IWMTSLayerDescription._methods_ = [
    COMMETHOD(['propget', helpstring(u'Identifier of WMTS layer.')], HRESULT, 'Identifier',
              ( ['retval', 'out'], POINTER(BSTR), 'stringId' )),
    COMMETHOD(['propget', helpstring(u'Title of WMTS layer.')], HRESULT, 'Title',
              ( ['retval', 'out'], POINTER(BSTR), 'Title' )),
    COMMETHOD(['propget', helpstring(u'Abstract of the WMTS layer.')], HRESULT, 'Abstract',
              ( ['retval', 'out'], POINTER(BSTR), 'Abstract' )),
    COMMETHOD(['propget', helpstring(u'Minimum bounding extent of the layer data in EPSG:4326.')], HRESULT, 'WGS84BoundingBox',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'envelope' )),
    COMMETHOD(['propget', helpstring(u'Number of bounding extents of the layer.')], HRESULT, 'BoundingBoxCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Minimum bounding extents of the layer data along with the applicable SRS.')], HRESULT, 'BoundingBox',
              ( ['in'], c_int, 'index' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'envelope' ),
              ( ['out'], POINTER(BSTR), 'srsCode' )),
    COMMETHOD(['propget', helpstring(u'Number of styles in the layer.')], HRESULT, 'StyleDescriptionCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Style of the layer at the given index.')], HRESULT, 'StyleDescription',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IWMSLayerStyleDescription)), 'StyleDescription' )),
    COMMETHOD(['propget', helpstring(u'WMTS Version.')], HRESULT, 'WMTSVersion',
              ( ['retval', 'out'], POINTER(BSTR), 'WMTSVersion' )),
    COMMETHOD(['propget', helpstring(u"Supported GetMap's ImageFormat count.")], HRESULT, 'ImageFormatCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u"Supported GetMap's ImageFormat at the given index.")], HRESULT, 'ImageFormat',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ImageFormat' )),
    COMMETHOD(['propget', helpstring(u'Supported FeatureInfoFormat count.')], HRESULT, 'FeatureInfoFormatCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Supported FeatureInfoFormat at the given index.')], HRESULT, 'FeatureInfoFormat',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ImageFormat' )),
    COMMETHOD(['propget', helpstring(u'Number of dimension in the layer.')], HRESULT, 'DimensionCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Dimension of the layer at the given index.')], HRESULT, 'Dimension',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IWMTSDimension)), 'Dimension' )),
    COMMETHOD(['propget', helpstring(u'Number of TileMatrixSet Links in the layer.')], HRESULT, 'TileMatrixSetLinkCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'TileMatrixSet Link of the layer at the given index.')], HRESULT, 'TileMatrixSetLink',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IWMTSTileMatrixSetLink)), 'matrixSetLink' )),
    COMMETHOD([helpstring(u'Url for the given REST resource.')], HRESULT, 'GetRESTResourceInfo',
              ( ['in'], BSTR, 'resourceType' ),
              ( ['out'], POINTER(BSTR), 'templateUrl' ),
              ( ['out'], POINTER(BSTR), 'format' )),
]
################################################################
## code template for IWMTSLayerDescription implementation
##class IWMTSLayerDescription_Impl(object):
##    @property
##    def BoundingBoxCount(self):
##        u'Number of bounding extents of the layer.'
##        #return Count
##
##    def GetRESTResourceInfo(self, resourceType):
##        u'Url for the given REST resource.'
##        #return templateUrl, format
##
##    @property
##    def Title(self):
##        u'Title of WMTS layer.'
##        #return Title
##
##    @property
##    def Abstract(self):
##        u'Abstract of the WMTS layer.'
##        #return Abstract
##
##    @property
##    def ImageFormatCount(self):
##        u"Supported GetMap's ImageFormat count."
##        #return Count
##
##    @property
##    def FeatureInfoFormat(self, index):
##        u'Supported FeatureInfoFormat at the given index.'
##        #return ImageFormat
##
##    @property
##    def DimensionCount(self):
##        u'Number of dimension in the layer.'
##        #return Count
##
##    @property
##    def BoundingBox(self, index):
##        u'Minimum bounding extents of the layer data along with the applicable SRS.'
##        #return envelope, srsCode
##
##    @property
##    def FeatureInfoFormatCount(self):
##        u'Supported FeatureInfoFormat count.'
##        #return Count
##
##    @property
##    def StyleDescription(self, index):
##        u'Style of the layer at the given index.'
##        #return StyleDescription
##
##    @property
##    def TileMatrixSetLinkCount(self):
##        u'Number of TileMatrixSet Links in the layer.'
##        #return Count
##
##    @property
##    def StyleDescriptionCount(self):
##        u'Number of styles in the layer.'
##        #return Count
##
##    @property
##    def WMTSVersion(self):
##        u'WMTS Version.'
##        #return WMTSVersion
##
##    @property
##    def WGS84BoundingBox(self):
##        u'Minimum bounding extent of the layer data in EPSG:4326.'
##        #return envelope
##
##    @property
##    def TileMatrixSetLink(self, index):
##        u'TileMatrixSet Link of the layer at the given index.'
##        #return matrixSetLink
##
##    @property
##    def Identifier(self):
##        u'Identifier of WMTS layer.'
##        #return stringId
##
##    @property
##    def Dimension(self, index):
##        u'Dimension of the layer at the given index.'
##        #return Dimension
##
##    @property
##    def ImageFormat(self, index):
##        u"Supported GetMap's ImageFormat at the given index."
##        #return ImageFormat
##


# values for enumeration 'acSecurityType'
acSecurityNone = 0
acSecurityGetFeaturesDisabled = 1
acSecurityType = c_int # enum
class WMTSTileMatrix(CoClass):
    u'Object that describes a particular tile matrix'
    _reg_clsid_ = GUID('{65E7E2D0-28BB-4F81-A572-F4D7BD48BF67}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{746F6817-89BB-4490-9829-83CA25FD505A}', 10, 2)
WMTSTileMatrix._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IWMTSTileMatrix]

class IRESTServerObjectAdmin(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods adminstrating AGS rest services.'
    _iid_ = GUID('{F21F82A2-6317-4A00-9877-8431C74A6707}')
    _idlflags_ = ['oleautomation']
IRESTServerObjectAdmin._methods_ = [
    COMMETHOD([helpstring(u'The configuration infos within a folder (use empty string for root).')], HRESULT, 'GetConfigurationInfos',
              ( ['in'], BSTR, 'FolderName' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._18F2FC71_6B30_45B9_B101_037A8B868B66_0_10_2.IEnumServerObjectConfigurationInfo)), 'ppConfigInfos' )),
    COMMETHOD(['propget', helpstring(u"Returns the version of the server's admin API.")], HRESULT, 'AdminVersion',
              ( ['retval', 'out'], POINTER(c_double), 'pAdminVersion' )),
    COMMETHOD([helpstring(u'The ItemInfo of a service.')], HRESULT, 'GetItemInfo',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], BSTR, 'Type' ),
              ( ['in'], BSTR, 'soeType' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IItemInfo)), 'ppItemInfo' )),
    COMMETHOD([helpstring(u'Add or update the ItemInfo of a service.')], HRESULT, 'PutItemInfo',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], BSTR, 'Type' ),
              ( ['in'], BSTR, 'soeType' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IItemInfo), 'pItemInfo' )),
    COMMETHOD([helpstring(u'The metadata of a service.')], HRESULT, 'GetMetadata',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], BSTR, 'Type' ),
              ( ['in'], BSTR, 'soeType' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'ppMetadata' )),
    COMMETHOD([helpstring(u'Add or update the metadata of a service.')], HRESULT, 'PutMetadata',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], BSTR, 'Type' ),
              ( ['in'], BSTR, 'soeType' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'pMetadata' )),
]
################################################################
## code template for IRESTServerObjectAdmin implementation
##class IRESTServerObjectAdmin_Impl(object):
##    def PutMetadata(self, Name, Type, soeType, pMetadata):
##        u'Add or update the metadata of a service.'
##        #return 
##
##    def GetMetadata(self, Name, Type, soeType):
##        u'The metadata of a service.'
##        #return ppMetadata
##
##    def PutItemInfo(self, Name, Type, soeType, pItemInfo):
##        u'Add or update the ItemInfo of a service.'
##        #return 
##
##    @property
##    def AdminVersion(self):
##        u"Returns the version of the server's admin API."
##        #return pAdminVersion
##
##    def GetConfigurationInfos(self, FolderName):
##        u'The configuration infos within a folder (use empty string for root).'
##        #return ppConfigInfos
##
##    def GetItemInfo(self, Name, Type, soeType):
##        u'The ItemInfo of a service.'
##        #return ppItemInfo
##

class UploadItem(CoClass):
    u'The UploadItem object.'
    _reg_clsid_ = GUID('{912E7FC9-1F8D-490C-B7E8-3403C21545FB}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{746F6817-89BB-4490-9829-83CA25FD505A}', 10, 2)
UploadItem._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IUploadItem]

IRemoteMetadataName2._methods_ = [
    COMMETHOD(['propget', helpstring(u'The content type of the metadata document.')], HRESULT, 'ContentType',
              ( ['retval', 'out'], POINTER(BSTR), 'pContentType' )),
    COMMETHOD(['propput', helpstring(u'The content type of the metadata document.')], HRESULT, 'ContentType',
              ( ['in'], BSTR, 'pContentType' )),
    COMMETHOD(['propget', helpstring(u'The modified date and time of the metadata document.')], HRESULT, 'ModifiedTime',
              ( ['retval', 'out'], POINTER(BSTR), 'pModifiedTime' )),
    COMMETHOD(['propput', helpstring(u'The modified date and time of the metadata document.')], HRESULT, 'ModifiedTime',
              ( ['in'], BSTR, 'pModifiedTime' )),
]
################################################################
## code template for IRemoteMetadataName2 implementation
##class IRemoteMetadataName2_Impl(object):
##    def _get(self):
##        u'The content type of the metadata document.'
##        #return pContentType
##    def _set(self, pContentType):
##        u'The content type of the metadata document.'
##    ContentType = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The modified date and time of the metadata document.'
##        #return pModifiedTime
##    def _set(self, pModifiedTime):
##        u'The modified date and time of the metadata document.'
##    ModifiedTime = property(_get, _set, doc = _set.__doc__)
##

IWCSConnection._methods_ = [
    COMMETHOD(['propget', helpstring(u'Name of the connection.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propput', helpstring(u'Name of the connection.')], HRESULT, 'Name',
              ( [], BSTR, 'Name' )),
    COMMETHOD(['propget', helpstring(u'Complete information required to connect to a WCS server..')], HRESULT, 'FullName',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName)), 'ppName' )),
    COMMETHOD(['propputref', helpstring(u'Complete information required to connect to a WCS server..')], HRESULT, 'FullName',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName), 'ppName' )),
]
################################################################
## code template for IWCSConnection implementation
##class IWCSConnection_Impl(object):
##    def FullName(self, ppName):
##        u'Complete information required to connect to a WCS server..'
##        #return 
##
##    def _get(self):
##        u'Name of the connection.'
##        #return Name
##    def _set(self, Name):
##        u'Name of the connection.'
##    Name = property(_get, _set, doc = _set.__doc__)
##

IWCSConnectionName._methods_ = [
    COMMETHOD(['propput', helpstring(u'Connection properties that will be used to connect to the WCS server.')], HRESULT, 'ConnectionProperties',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'ppConnProps' )),
    COMMETHOD(['propget', helpstring(u'Connection properties that will be used to connect to the WCS server.')], HRESULT, 'ConnectionProperties',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'ppConnProps' )),
    COMMETHOD(['propput', helpstring(u'Connection info about this connection.')], HRESULT, 'ConnectionInfo',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'ppConnInfo' )),
    COMMETHOD(['propget', helpstring(u'Connection info about this connection.')], HRESULT, 'ConnectionInfo',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'ppConnInfo' )),
    COMMETHOD([helpstring(u'Opens the WCS Connection.')], HRESULT, 'OpenEx',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'ppUnknown' )),
]
################################################################
## code template for IWCSConnectionName implementation
##class IWCSConnectionName_Impl(object):
##    def OpenEx(self, pTrackCancel):
##        u'Opens the WCS Connection.'
##        #return ppUnknown
##
##    def _get(self):
##        u'Connection info about this connection.'
##        #return ppConnInfo
##    def _set(self, ppConnInfo):
##        u'Connection info about this connection.'
##    ConnectionInfo = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Connection properties that will be used to connect to the WCS server.'
##        #return ppConnProps
##    def _set(self, ppConnProps):
##        u'Connection properties that will be used to connect to the WCS server.'
##    ConnectionProperties = property(_get, _set, doc = _set.__doc__)
##

class UploadsClient(CoClass):
    u'The uploads client object.'
    _reg_clsid_ = GUID('{A6DD18CA-776B-4CBB-B386-F2D5E1E4374D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{746F6817-89BB-4490-9829-83CA25FD505A}', 10, 2)
class IServiceUploadsClient(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to properties and members of the uploads client object.'
    _iid_ = GUID('{DDCBDAAC-B932-4279-A2C1-5A151632B793}')
    _idlflags_ = ['oleautomation']
UploadsClient._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IUploadsClient, IAdminUploadsClient, IServiceUploadsClient]

IServiceUploadsClient._methods_ = [
    COMMETHOD([helpstring(u'Uploads a file to the server without breaking it into parts.')], HRESULT, 'ServiceUploadFile',
              ( ['in'], BSTR, 'file' ),
              ( ['in'], BSTR, 'Description' ),
              ( ['in'], POINTER(IAGSServerObjectName), 'pTargetService' ),
              ( ['retval', 'out'], POINTER(POINTER(IUploadItem)), 'ppUploadedItem' )),
    COMMETHOD([helpstring(u'Instruct the server to reserve space for a new upload item, to be uploaded in parts.')], HRESULT, 'ServiceRegister',
              ( ['in'], BSTR, 'itemName' ),
              ( ['in'], BSTR, 'Description' ),
              ( ['in'], POINTER(IAGSServerObjectName), 'pTargetService' ),
              ( ['retval', 'out'], POINTER(POINTER(IUploadItem)), 'ppUploadsItem' )),
    COMMETHOD([helpstring(u'Uploads a part for the upload item.')], HRESULT, 'ServiceUploadPart',
              ( ['in'], POINTER(IUploadItem), 'pUploadItem' ),
              ( ['in'], BSTR, 'file' ),
              ( ['in'], c_int, 'uploadPartNumber' ),
              ( ['in'], c_ulonglong, 'offset' ),
              ( ['in'], c_int, 'bytesToWrite' ),
              ( ['in'], POINTER(IAGSServerObjectName), 'pTargetService' )),
    COMMETHOD([helpstring(u'Returns the numbers of the parts that have already been uploaded for the upload item.')], HRESULT, 'ServiceGetPartNumbers',
              ( ['in'], POINTER(IUploadItem), 'pUploadItem' ),
              ( ['in'], POINTER(IAGSServerObjectName), 'pTargetService' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray)), 'ppPartNumbers' )),
    COMMETHOD([helpstring(u'Commits a registered upload item.')], HRESULT, 'ServiceCommit',
              ( ['in'], POINTER(IUploadItem), 'pUploadItem' ),
              ( ['in'], POINTER(IAGSServerObjectName), 'pTargetService' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray), 'pPartNumbers' )),
    COMMETHOD([helpstring(u'Deletes the upload item.')], HRESULT, 'ServiceDelete',
              ( ['in'], POINTER(IUploadItem), 'pUploadItem' ),
              ( ['in'], POINTER(IAGSServerObjectName), 'pTargetService' )),
    COMMETHOD([helpstring(u'Returns the maximum upload size for a service.')], HRESULT, 'GetServiceMaxUploadSizeInBytes',
              ( ['in'], POINTER(IAGSServerObjectName), 'pTargetSevice' ),
              ( ['retval', 'out'], POINTER(c_ulonglong), 'pMaxSize' )),
]
################################################################
## code template for IServiceUploadsClient implementation
##class IServiceUploadsClient_Impl(object):
##    def GetServiceMaxUploadSizeInBytes(self, pTargetSevice):
##        u'Returns the maximum upload size for a service.'
##        #return pMaxSize
##
##    def ServiceGetPartNumbers(self, pUploadItem, pTargetService):
##        u'Returns the numbers of the parts that have already been uploaded for the upload item.'
##        #return ppPartNumbers
##
##    def ServiceDelete(self, pUploadItem, pTargetService):
##        u'Deletes the upload item.'
##        #return 
##
##    def ServiceUploadFile(self, file, Description, pTargetService):
##        u'Uploads a file to the server without breaking it into parts.'
##        #return ppUploadedItem
##
##    def ServiceCommit(self, pUploadItem, pTargetService, pPartNumbers):
##        u'Commits a registered upload item.'
##        #return 
##
##    def ServiceUploadPart(self, pUploadItem, file, uploadPartNumber, offset, bytesToWrite, pTargetService):
##        u'Uploads a part for the upload item.'
##        #return 
##
##    def ServiceRegister(self, itemName, Description, pTargetService):
##        u'Instruct the server to reserve space for a new upload item, to be uploaded in parts.'
##        #return ppUploadsItem
##

IAGSServerConnectionName._methods_ = [
    COMMETHOD(['propput', helpstring(u'The connection properties of the AGSServerConnectionName.')], HRESULT, 'ConnectionProperties',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'ppConnProps' )),
    COMMETHOD(['propget', helpstring(u'The connection properties of the AGSServerConnectionName.')], HRESULT, 'ConnectionProperties',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'ppConnProps' )),
    COMMETHOD(['propget', helpstring(u'The type of the associated GIS server connection.')], HRESULT, 'ConnectionType',
              ( ['retval', 'out'], POINTER(esriAGSConnectionType), 'pConnType' )),
]
################################################################
## code template for IAGSServerConnectionName implementation
##class IAGSServerConnectionName_Impl(object):
##    def _get(self):
##        u'The connection properties of the AGSServerConnectionName.'
##        #return ppConnProps
##    def _set(self, ppConnProps):
##        u'The connection properties of the AGSServerConnectionName.'
##    ConnectionProperties = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def ConnectionType(self):
##        u'The type of the associated GIS server connection.'
##        #return pConnType
##

IAGSServerConnectionName2._methods_ = [
    COMMETHOD(['propget', helpstring(u'The connection properties of the GIS server connection.')], HRESULT, 'ConnectionString',
              ( ['retval', 'out'], POINTER(BSTR), 'connString' )),
    COMMETHOD(['propput', helpstring(u'The connection properties of the GIS server connection.')], HRESULT, 'ConnectionString',
              ( ['in'], BSTR, 'connString' )),
    COMMETHOD(['propget', helpstring(u'The programmatic ID of the server connection factory.')], HRESULT, 'ServerConnectionFactoryProgID',
              ( ['retval', 'out'], POINTER(BSTR), 'progID' )),
    COMMETHOD(['propput', helpstring(u'The programmatic ID of the server connection factory.')], HRESULT, 'ServerConnectionFactoryProgID',
              ( ['in'], BSTR, 'progID' )),
]
################################################################
## code template for IAGSServerConnectionName2 implementation
##class IAGSServerConnectionName2_Impl(object):
##    def _get(self):
##        u'The connection properties of the GIS server connection.'
##        #return connString
##    def _set(self, connString):
##        u'The connection properties of the GIS server connection.'
##    ConnectionString = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The programmatic ID of the server connection factory.'
##        #return progID
##    def _set(self, progID):
##        u'The programmatic ID of the server connection factory.'
##    ServerConnectionFactoryProgID = property(_get, _set, doc = _set.__doc__)
##

class IMSWorkspaceFactory(CoClass):
    u'The IMS Workspace Factory.'
    _reg_clsid_ = GUID('{BAC84D58-FA9D-11D3-9F48-00C04F79927C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{746F6817-89BB-4490-9829-83CA25FD505A}', 10, 2)
IMSWorkspaceFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceFactory, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceFactory2]

class AGSServerConnection(CoClass):
    u'The AGSServerConnection object for connecting to the GIS server and getting the ServerObjectManager and ServerObjectAdmin.'
    _reg_clsid_ = GUID('{B49DEFD0-85C0-46F4-918B-1FB7E02A8C70}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{746F6817-89BB-4490-9829-83CA25FD505A}', 10, 2)
class IAGSServerConnection2(IAGSServerConnection):
    _case_insensitive_ = True
    u'Provides access to members that create and open GIS server connections and supply server connection factory information.'
    _iid_ = GUID('{6921C52D-0D14-4D2C-8A80-A7873C1306EA}')
    _idlflags_ = ['oleautomation']
class IAGSServerConnection3(IAGSServerConnection2):
    _case_insensitive_ = True
    u'Provides access to members that have information about the GIS server connection..'
    _iid_ = GUID('{20E6A647-DE9E-4E4C-A301-640B9AB0D143}')
    _idlflags_ = ['oleautomation']
class IAGSServerConnectionAdmin(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the server object manager, server object admin and server object configurations for the GIS server.'
    _iid_ = GUID('{2609D396-4C06-4C35-9AE3-DF690ED88506}')
    _idlflags_ = ['oleautomation']
AGSServerConnection._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IAGSServerConnection, IAGSServerConnection2, IAGSServerConnection3, IAGSServerConnectionAdmin, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

class AGSServerObjectName(CoClass):
    u'A name object for ArcGIS Server Objects.'
    _reg_clsid_ = GUID('{6C22971C-D450-4B4D-9422-EE96A40FACC5}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{746F6817-89BB-4490-9829-83CA25FD505A}', 10, 2)
class IAGSServerObjectName2(IAGSServerObjectName):
    _case_insensitive_ = True
    u'Provides access to members that supply server object name information.'
    _iid_ = GUID('{2F311F9A-50F9-45D4-9553-D781A08445E8}')
    _idlflags_ = ['oleautomation']
class IAGSServerObjectName3(IAGSServerObjectName2):
    _case_insensitive_ = True
    u'Provides access to members that supply server object name information.'
    _iid_ = GUID('{4B815919-7659-4A55-8608-26EB7D6B24F2}')
    _idlflags_ = ['oleautomation']
AGSServerObjectName._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IAGSServerObjectName, IAGSServerObjectName2, IAGSServerObjectName3, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream]

IWMTSDimension._methods_ = [
    COMMETHOD(['propget', helpstring(u'Identifier of WMTS Dimension.')], HRESULT, 'Identifier',
              ( ['retval', 'out'], POINTER(BSTR), 'ID' )),
    COMMETHOD(['propget', helpstring(u'Title of WMTS Dimension.')], HRESULT, 'Title',
              ( ['retval', 'out'], POINTER(BSTR), 'Title' )),
    COMMETHOD(['propget', helpstring(u'Abstract of the WMTS Dimension.')], HRESULT, 'Abstract',
              ( ['retval', 'out'], POINTER(BSTR), 'Abstract' )),
    COMMETHOD(['propget', helpstring(u'Value count in WMTS Dimension.')], HRESULT, 'ValueCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Value at a given index in WMTS Dimension.')], HRESULT, 'Value',
              ( ['in'], c_int, 'ix' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD(['propget', helpstring(u'Default value for WMTS Dimension.')], HRESULT, 'DefaultValue',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the current keyword is supported as a value.')], HRESULT, 'SupportsCurrentValue',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'supports' )),
    COMMETHOD(['propget', helpstring(u'Symbol of the units for value in WMTS Dimension.')], HRESULT, 'UnitsSymbol',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
]
################################################################
## code template for IWMTSDimension implementation
##class IWMTSDimension_Impl(object):
##    @property
##    def Title(self):
##        u'Title of WMTS Dimension.'
##        #return Title
##
##    @property
##    def DefaultValue(self):
##        u'Default value for WMTS Dimension.'
##        #return Value
##
##    @property
##    def Value(self, ix):
##        u'Value at a given index in WMTS Dimension.'
##        #return Value
##
##    @property
##    def ValueCount(self):
##        u'Value count in WMTS Dimension.'
##        #return Count
##
##    @property
##    def SupportsCurrentValue(self):
##        u'Indicates whether the current keyword is supported as a value.'
##        #return supports
##
##    @property
##    def Identifier(self):
##        u'Identifier of WMTS Dimension.'
##        #return ID
##
##    @property
##    def Abstract(self):
##        u'Abstract of the WMTS Dimension.'
##        #return Abstract
##
##    @property
##    def UnitsSymbol(self):
##        u'Symbol of the units for value in WMTS Dimension.'
##        #return Value
##

class Uploader(CoClass):
    u'The uploader object.'
    _reg_clsid_ = GUID('{62CC7834-F2B8-4E4B-93CF-FC2D0571811F}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{746F6817-89BB-4490-9829-83CA25FD505A}', 10, 2)
class IUploader(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to properties and members of the Uploader object.'
    _iid_ = GUID('{0788EAF6-42AC-404A-894E-E0330782912A}')
    _idlflags_ = ['oleautomation']
Uploader._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IUploader, IAdminUploader, IServiceUploader]

IAGSServerConnection2._methods_ = [
    COMMETHOD(['propget', helpstring(u'The ServerObjectNames in the GIS server folder.')], HRESULT, 'ServerObjectNamesEx',
              ( [], BSTR, 'FolderName' ),
              ( ['retval', 'out'], POINTER(POINTER(IAGSEnumServerObjectName)), 'ppSONames' )),
    COMMETHOD([helpstring(u'Returns an enumeration of folder names beneath the specified folder.')], HRESULT, 'GetFolders',
              ( ['in'], BSTR, 'reserved' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IEnumBSTR)), 'ppEnum' )),
]
################################################################
## code template for IAGSServerConnection2 implementation
##class IAGSServerConnection2_Impl(object):
##    def GetFolders(self, reserved):
##        u'Returns an enumeration of folder names beneath the specified folder.'
##        #return ppEnum
##
##    @property
##    def ServerObjectNamesEx(self, FolderName):
##        u'The ServerObjectNames in the GIS server folder.'
##        #return ppSONames
##

IAGSEnumServerObjectName._methods_ = [
    COMMETHOD([helpstring(u'Retrieves the next server object name in the enumeration sequence.')], HRESULT, 'Next',
              ( ['retval', 'out'], POINTER(POINTER(IAGSServerObjectName)), 'ppSOName' )),
    COMMETHOD([helpstring(u'Resets the enumeration sequence to the beginning.')], HRESULT, 'Reset'),
]
################################################################
## code template for IAGSEnumServerObjectName implementation
##class IAGSEnumServerObjectName_Impl(object):
##    def Reset(self):
##        u'Resets the enumeration sequence to the beginning.'
##        #return 
##
##    def Next(self):
##        u'Retrieves the next server object name in the enumeration sequence.'
##        #return ppSOName
##

IAGSServerObjectName2._methods_ = [
    COMMETHOD(['propput', helpstring(u'The name string for the server object name.')], HRESULT, 'NameString2',
              ( ['in'], BSTR, 'ns' )),
    COMMETHOD(['propget', helpstring(u'The name string for the server object name.')], HRESULT, 'NameString2',
              ( ['retval', 'out'], POINTER(BSTR), 'ns' )),
    COMMETHOD(['propput', helpstring(u'The type of server object this server object extension is associated with.')], HRESULT, 'ParentType',
              ( ['in'], BSTR, 'ParentType' )),
    COMMETHOD(['propget', helpstring(u'The type of server object this server object extension is associated with.')], HRESULT, 'ParentType',
              ( ['retval', 'out'], POINTER(BSTR), 'ParentType' )),
    COMMETHOD(['propput', helpstring(u'The web capabilities of the service.')], HRESULT, 'Capabilities',
              ( ['in'], BSTR, 'caps' )),
    COMMETHOD(['propget', helpstring(u'The web capabilities of the service.')], HRESULT, 'Capabilities',
              ( ['retval', 'out'], POINTER(BSTR), 'caps' )),
]
################################################################
## code template for IAGSServerObjectName2 implementation
##class IAGSServerObjectName2_Impl(object):
##    def _get(self):
##        u'The type of server object this server object extension is associated with.'
##        #return ParentType
##    def _set(self, ParentType):
##        u'The type of server object this server object extension is associated with.'
##    ParentType = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The web capabilities of the service.'
##        #return caps
##    def _set(self, caps):
##        u'The web capabilities of the service.'
##    Capabilities = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The name string for the server object name.'
##        #return ns
##    def _set(self, ns):
##        u'The name string for the server object name.'
##    NameString2 = property(_get, _set, doc = _set.__doc__)
##

IAGSServerObjectName3._methods_ = [
    COMMETHOD(['propput', helpstring(u'The name of the service.')], HRESULT, 'Description',
              ( ['in'], BSTR, 'objectURL' )),
    COMMETHOD(['propget', helpstring(u'The name of the service.')], HRESULT, 'Description',
              ( ['retval', 'out'], POINTER(BSTR), 'objectURL' )),
]
################################################################
## code template for IAGSServerObjectName3 implementation
##class IAGSServerObjectName3_Impl(object):
##    def _get(self):
##        u'The name of the service.'
##        #return objectURL
##    def _set(self, objectURL):
##        u'The name of the service.'
##    Description = property(_get, _set, doc = _set.__doc__)
##

class IAGSServerConnectionFactory(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that create and open GIS server connections and supply server connection factory information.'
    _iid_ = GUID('{6047C9FC-2D91-420A-A5A2-EB36B7E2FEA2}')
    _idlflags_ = ['oleautomation']
IAGSServerConnectionFactory._methods_ = [
    COMMETHOD([helpstring(u'Opens the GIS server connection specified by the connection properties.')], HRESULT, 'Open',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'pConnectionProperties' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hWnd' ),
              ( ['retval', 'out'], POINTER(POINTER(IAGSServerConnection)), 'ppConnection' )),
]
################################################################
## code template for IAGSServerConnectionFactory implementation
##class IAGSServerConnectionFactory_Impl(object):
##    def Open(self, pConnectionProperties, hWnd):
##        u'Opens the GIS server connection specified by the connection properties.'
##        #return ppConnection
##

class AGSServerConnectionFactory(CoClass):
    u'A factory object for ArcGIS Server Connections.'
    _reg_clsid_ = GUID('{7932A86E-F371-4C64-AB84-9E83DDA2581B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{746F6817-89BB-4490-9829-83CA25FD505A}', 10, 2)
class IAGSServerConnectionFactory2(IAGSServerConnectionFactory):
    _case_insensitive_ = True
    u'Provides access to members that create and open GIS server connections and supply server connection factory information.'
    _iid_ = GUID('{0264CA94-B0EB-435F-9D3A-5FCC5DA0FBAE}')
    _idlflags_ = ['oleautomation']
class IAGSServerConnectionFactory3(IAGSServerConnectionFactory2):
    _case_insensitive_ = True
    u'Provides access to members that create and open GIS server connections and supply server connection factory information.'
    _iid_ = GUID('{02D56C6D-9134-42C7-B6B0-6804A125B7A9}')
    _idlflags_ = ['oleautomation']
class ISetDefaultAgsConnectionInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to user entered information for an ArcGIS Server Connection.'
    _iid_ = GUID('{DF667332-0E2B-49BF-9DF9-BA8B15A37601}')
    _idlflags_ = ['oleautomation']
AGSServerConnectionFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IAGSServerConnectionFactory, IAGSServerConnectionFactory2, IAGSServerConnectionFactory3, ISetDefaultAgsConnectionInfo]

class IWCSBoundingBoxInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to IWCSBoundingBoxInfo information.'
    _iid_ = GUID('{ED79B15F-9133-4D1C-8BAC-170562B5FF9D}')
    _idlflags_ = []
IWCSBoundingBoxInfo._methods_ = [
    COMMETHOD(['propget', helpstring(u'CRS name of of this bounding box.')], HRESULT, 'CRS',
              ( ['retval', 'out'], POINTER(BSTR), 'CRS' )),
    COMMETHOD(['propget', helpstring(u'The bounding extent of the coverage data.')], HRESULT, 'BoundingBox',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'ppEnvelope' )),
]
################################################################
## code template for IWCSBoundingBoxInfo implementation
##class IWCSBoundingBoxInfo_Impl(object):
##    @property
##    def BoundingBox(self):
##        u'The bounding extent of the coverage data.'
##        #return ppEnvelope
##
##    @property
##    def CRS(self):
##        u'CRS name of of this bounding box.'
##        #return CRS
##

ISetDefaultAgsConnectionInfo._methods_ = [
    COMMETHOD([helpstring(u"Clears an ArcGIS Server connection's user entered parameters.")], HRESULT, 'ClearParameters',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'pConnectionProperties' )),
]
################################################################
## code template for ISetDefaultAgsConnectionInfo implementation
##class ISetDefaultAgsConnectionInfo_Impl(object):
##    def ClearParameters(self, pConnectionProperties):
##        u"Clears an ArcGIS Server connection's user entered parameters."
##        #return 
##

IAGSServerConnectionAdmin._methods_ = [
    COMMETHOD(['propget', helpstring(u'The server object manager for the connected GIS server.')], HRESULT, 'ServerObjectManager',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._18F2FC71_6B30_45B9_B101_037A8B868B66_0_10_2.IServerObjectManager)), 'ppObjectManager' )),
    COMMETHOD(['propget', helpstring(u'The server object admin for the connected GIS server.')], HRESULT, 'ServerObjectAdmin',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._18F2FC71_6B30_45B9_B101_037A8B868B66_0_10_2.IServerObjectAdmin)), 'ppObjectAdmin' )),
    COMMETHOD(['propget', helpstring(u'The server object configuration with the specified Name and TypeName.')], HRESULT, 'ServerObjectConfiguration',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], BSTR, 'Type' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._18F2FC71_6B30_45B9_B101_037A8B868B66_0_10_2.IServerObjectConfiguration)), 'ppObject' )),
]
################################################################
## code template for IAGSServerConnectionAdmin implementation
##class IAGSServerConnectionAdmin_Impl(object):
##    @property
##    def ServerObjectAdmin(self):
##        u'The server object admin for the connected GIS server.'
##        #return ppObjectAdmin
##
##    @property
##    def ServerObjectManager(self):
##        u'The server object manager for the connected GIS server.'
##        #return ppObjectManager
##
##    @property
##    def ServerObjectConfiguration(self, Name, Type):
##        u'The server object configuration with the specified Name and TypeName.'
##        #return ppObject
##

class IWCSSpatialDomain(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to IWCSSpatialDomain information.'
    _iid_ = GUID('{B7EC7893-EFB4-4B61-8FE0-E746CF0422B5}')
    _idlflags_ = []
IWCSSpatialDomain._methods_ = [
    COMMETHOD(['propget', helpstring(u'The boundingboxinfo count of the coverage data.')], HRESULT, 'BoundingBoxInfoCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'BoundingBoxInfo at the given index.')], HRESULT, 'BoundingBoxInfo',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IWCSBoundingBoxInfo)), 'ppWCSBBInfo' )),
    COMMETHOD(['propget', helpstring(u'Base CRS name of grid.')], HRESULT, 'GridBaseCRS',
              ( ['retval', 'out'], POINTER(BSTR), 'CRS' )),
    COMMETHOD(['propget', helpstring(u'X of grid origin.')], HRESULT, 'GridOrigin_X',
              ( ['retval', 'out'], POINTER(c_double), 'x' )),
    COMMETHOD(['propget', helpstring(u'Y of grid origin.')], HRESULT, 'GridOrigin_Y',
              ( ['retval', 'out'], POINTER(c_double), 'y' )),
    COMMETHOD(['propget', helpstring(u'X offset of grid.')], HRESULT, 'GridOffsets_X',
              ( ['retval', 'out'], POINTER(c_double), 'x' )),
    COMMETHOD(['propget', helpstring(u'Y offset of grid.')], HRESULT, 'GridOffsets_Y',
              ( ['retval', 'out'], POINTER(c_double), 'y' )),
    COMMETHOD(['propget', helpstring(u'The bounding box of grid offsets.')], HRESULT, 'GridOffsetsBoundingBox',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'ppEnvelope' )),
]
################################################################
## code template for IWCSSpatialDomain implementation
##class IWCSSpatialDomain_Impl(object):
##    @property
##    def GridOrigin_Y(self):
##        u'Y of grid origin.'
##        #return y
##
##    @property
##    def GridOrigin_X(self):
##        u'X of grid origin.'
##        #return x
##
##    @property
##    def GridBaseCRS(self):
##        u'Base CRS name of grid.'
##        #return CRS
##
##    @property
##    def BoundingBoxInfo(self, index):
##        u'BoundingBoxInfo at the given index.'
##        #return ppWCSBBInfo
##
##    @property
##    def GridOffsetsBoundingBox(self):
##        u'The bounding box of grid offsets.'
##        #return ppEnvelope
##
##    @property
##    def GridOffsets_X(self):
##        u'X offset of grid.'
##        #return x
##
##    @property
##    def GridOffsets_Y(self):
##        u'Y offset of grid.'
##        #return y
##
##    @property
##    def BoundingBoxInfoCount(self):
##        u'The boundingboxinfo count of the coverage data.'
##        #return Count
##

IWMSLayerStyleDescription._methods_ = [
    COMMETHOD(['propget', helpstring(u'Name of the WMS Style.')], HRESULT, 'Name',
              ( [], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'Title of the WMS Style.')], HRESULT, 'Title',
              ( ['out'], POINTER(BSTR), 'Title' )),
    COMMETHOD(['propget', helpstring(u'Abstract of the WMS Style.')], HRESULT, 'Abstract',
              ( ['out'], POINTER(BSTR), 'Abstract' )),
    COMMETHOD(['propget', helpstring(u'Width of the symbol.')], HRESULT, 'Width',
              ( ['retval', 'out'], POINTER(c_double), 'Width' )),
    COMMETHOD(['propget', helpstring(u'Height of the symbol.')], HRESULT, 'Height',
              ( ['retval', 'out'], POINTER(c_double), 'Height' )),
    COMMETHOD(['propget', helpstring(u'URL of the symbol image.')], HRESULT, 'URL',
              ( ['retval', 'out'], POINTER(BSTR), 'URL' )),
    COMMETHOD(['propget', helpstring(u'Supported image format count.')], HRESULT, 'ImageFormatCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Supported image format at the given index.')], HRESULT, 'ImageFormat',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ImageFormat' )),
]
################################################################
## code template for IWMSLayerStyleDescription implementation
##class IWMSLayerStyleDescription_Impl(object):
##    @property
##    def Name(self, Name):
##        u'Name of the WMS Style.'
##        #return 
##
##    @property
##    def Title(self):
##        u'Title of the WMS Style.'
##        #return Title
##
##    @property
##    def URL(self):
##        u'URL of the symbol image.'
##        #return URL
##
##    @property
##    def Abstract(self):
##        u'Abstract of the WMS Style.'
##        #return Abstract
##
##    @property
##    def ImageFormatCount(self):
##        u'Supported image format count.'
##        #return Count
##
##    @property
##    def Height(self):
##        u'Height of the symbol.'
##        #return Height
##
##    @property
##    def Width(self):
##        u'Width of the symbol.'
##        #return Width
##
##    @property
##    def ImageFormat(self, index):
##        u'Supported image format at the given index.'
##        #return ImageFormat
##


# values for enumeration 'esriServiceURLType'
esriServiceURLTypeSoap = 0
esriServiceURLTypeREST = 1
esriServiceURLTypeAdmin = 2
esriServiceURLType = c_int # enum

# values for enumeration 'esriAGSServerVersionType'
esriAGSServerVersionTypeSoap = 0
esriAGSServerVersionTypeREST = 1
esriAGSServerVersionTypeAdmin = 2
esriAGSServerVersionType = c_int # enum
class IEnumAGSServerConnectionName(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that enumerate over a collection of server connection name objects.'
    _iid_ = GUID('{4F11971A-F293-47A4-ACF2-FEF737FB71F4}')
    _idlflags_ = ['oleautomation']
IEnumAGSServerConnectionName._methods_ = [
    COMMETHOD([helpstring(u'Resets the enumerator.')], HRESULT, 'Reset'),
    COMMETHOD([helpstring(u'Returns the next element in the enumerator.')], HRESULT, 'Next',
              ( ['retval', 'out'], POINTER(POINTER(IAGSServerConnectionName)), 'connName' )),
]
################################################################
## code template for IEnumAGSServerConnectionName implementation
##class IEnumAGSServerConnectionName_Impl(object):
##    def Reset(self):
##        u'Resets the enumerator.'
##        #return 
##
##    def Next(self):
##        u'Returns the next element in the enumerator.'
##        #return connName
##

IAGSServerConnection3._methods_ = [
    COMMETHOD([helpstring(u'Retrieves a file from the specified url.')], HRESULT, 'GetFile',
              ( ['in'], BSTR, 'URL' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStream)), 'stream' )),
    COMMETHOD([helpstring(u'Retrieves the stream as variant from the specified url.')], HRESULT, 'GetFileAsVariant',
              ( ['in'], BSTR, 'URL' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'pValue' )),
]
################################################################
## code template for IAGSServerConnection3 implementation
##class IAGSServerConnection3_Impl(object):
##    def GetFile(self, URL):
##        u'Retrieves a file from the specified url.'
##        #return stream
##
##    def GetFileAsVariant(self, URL):
##        u'Retrieves the stream as variant from the specified url.'
##        #return pValue
##

IUploader._methods_ = [
    COMMETHOD(['propput', helpstring(u'.')], HRESULT, 'SingleUploadThresholdInBytes',
              ( ['in'], c_int, 'pThreshold' )),
    COMMETHOD(['propget', helpstring(u'.')], HRESULT, 'SingleUploadThresholdInBytes',
              ( ['retval', 'out'], POINTER(c_int), 'pThreshold' )),
    COMMETHOD(['propput', helpstring(u'.')], HRESULT, 'TimeoutInSecs',
              ( ['in'], c_int, 'pTimeout' )),
    COMMETHOD(['propget', helpstring(u'.')], HRESULT, 'TimeoutInSecs',
              ( ['retval', 'out'], POINTER(c_int), 'pTimeout' )),
    COMMETHOD(['propget', helpstring(u'.')], HRESULT, 'UploadsClient',
              ( ['retval', 'out'], POINTER(POINTER(IUploadsClient)), 'ppUploadsClient' )),
    COMMETHOD([helpstring(u'.')], HRESULT, 'Init',
              ( ['in'], POINTER(IAGSServerConnection), 'pConn' )),
]
################################################################
## code template for IUploader implementation
##class IUploader_Impl(object):
##    def _get(self):
##        u'.'
##        #return pThreshold
##    def _set(self, pThreshold):
##        u'.'
##    SingleUploadThresholdInBytes = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'.'
##        #return pTimeout
##    def _set(self, pTimeout):
##        u'.'
##    TimeoutInSecs = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def UploadsClient(self):
##        u'.'
##        #return ppUploadsClient
##
##    def Init(self, pConn):
##        u'.'
##        #return 
##

IAGSServerConnectionFactory2._methods_ = [
    COMMETHOD([helpstring(u'Opens the server connection specified by the given file name.')], HRESULT, 'OpenFromFile',
              ( ['in'], BSTR, 'fileName' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hWnd' ),
              ( ['retval', 'out'], POINTER(POINTER(IAGSServerConnection)), 'ppConnection' )),
    COMMETHOD([helpstring(u'The connection properties from the specified file.')], HRESULT, 'ReadConnectionPropertiesFromFile',
              ( ['in'], BSTR, 'fileName' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'ConnectionProperties' )),
    COMMETHOD(['propput', helpstring(u'The default timeout for http requests to the server (in seconds).')], HRESULT, 'DefaultHttpTimeout',
              ( ['in'], c_int, 'seconds' )),
    COMMETHOD(['propget', helpstring(u'The default timeout for http requests to the server (in seconds).')], HRESULT, 'DefaultHttpTimeout',
              ( ['retval', 'out'], POINTER(c_int), 'seconds' )),
]
################################################################
## code template for IAGSServerConnectionFactory2 implementation
##class IAGSServerConnectionFactory2_Impl(object):
##    def _get(self):
##        u'The default timeout for http requests to the server (in seconds).'
##        #return seconds
##    def _set(self, seconds):
##        u'The default timeout for http requests to the server (in seconds).'
##    DefaultHttpTimeout = property(_get, _set, doc = _set.__doc__)
##
##    def ReadConnectionPropertiesFromFile(self, fileName):
##        u'The connection properties from the specified file.'
##        #return ConnectionProperties
##
##    def OpenFromFile(self, fileName, hWnd):
##        u'Opens the server connection specified by the given file name.'
##        #return ppConnection
##

IAGSServerConnectionFactory3._methods_ = [
    COMMETHOD([helpstring(u'Returns server object names for the hosted servers accessible to the user.')], HRESULT, 'GetHostedServers',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hWnd' ),
              ( ['retval', 'out'], POINTER(POINTER(IEnumAGSServerConnectionName)), 'connNames' )),
    COMMETHOD([helpstring(u'Returns a server connection name that can be used to connect to the server from within a server process. Fails if run outside a server process.')], HRESULT, 'GetInServerConnectionName',
              ( ['retval', 'out'], POINTER(POINTER(IAGSServerConnectionName)), 'connName' )),
]
################################################################
## code template for IAGSServerConnectionFactory3 implementation
##class IAGSServerConnectionFactory3_Impl(object):
##    def GetInServerConnectionName(self):
##        u'Returns a server connection name that can be used to connect to the server from within a server process. Fails if run outside a server process.'
##        #return connName
##
##    def GetHostedServers(self, hWnd):
##        u'Returns server object names for the hosted servers accessible to the user.'
##        #return connNames
##

IWMSClientEvents._methods_ = [
    COMMETHOD([helpstring(u'Fired when the an URL request is made to WMS server.')], HRESULT, 'WMSRequest',
              ( ['in'], POINTER(IWMSServiceDescription), 'pService' ),
              ( ['in'], BSTR, 'requestType' ),
              ( ['in'], BSTR, 'requestURL' )),
    COMMETHOD([helpstring(u'Fired when the an URL request is made to WMS server and the server fails with a valid exception.')], HRESULT, 'WMSException',
              ( ['in'], POINTER(IWMSServiceDescription), 'pService' ),
              ( ['in'], BSTR, 'requestType' ),
              ( ['in'], BSTR, 'requestURL' ),
              ( ['in'], POINTER(IWMSServiceExceptionHandler), 'pException' )),
]
################################################################
## code template for IWMSClientEvents implementation
##class IWMSClientEvents_Impl(object):
##    def WMSRequest(self, pService, requestType, requestURL):
##        u'Fired when the an URL request is made to WMS server.'
##        #return 
##
##    def WMSException(self, pService, requestType, requestURL, pException):
##        u'Fired when the an URL request is made to WMS server and the server fails with a valid exception.'
##        #return 
##


# values for enumeration 'wmsErrors'
WMSCONN_E_ACCESS_DENIED = -2147220735
WMSCONN_E_PROXY_AUTHENTICATION_FAILED = -2147220734
WMSCONN_E_UNABLE_TO_CONNECT = -2147220733
WMSCONN_E_MISSING_URL = -2147220732
WMSCONN_E_MISSING_SERVICENAME = -2147220731
WMSCONN_E_INCORRECT_URL = -2147220730
WMSCONN_E_SERVER_NOT_AVAILABLE = -2147220729
wmsErrors = c_int # enum

# values for enumeration 'imsErrors'
IMS_E_ACCESS_DENIED = -2147220991
IMS_E_PROXY_AUTHENTICATION_FAILED = -2147220990
IMS_E_UNABLE_TO_CONNECT = -2147220989
IMS_E_MISSING_URL = -2147220988
IMS_E_MISSING_SERVICENAME = -2147220987
imsErrors = c_int # enum
class IIMSFeatureClass(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the ArcIMS Feature Class.'
    _iid_ = GUID('{B6F0197B-EA28-11D3-9F47-00C04F79927C}')
    _idlflags_ = ['oleautomation']
IIMSFeatureClass._methods_ = [
    COMMETHOD(['propget', helpstring(u'The Feature Class AXL.')], HRESULT, 'Axl',
              ( ['retval', 'out'], POINTER(BSTR), 'Axl' )),
    COMMETHOD(['propget', helpstring(u'The Feature Class Layer ID.')], HRESULT, 'LayerID',
              ( ['retval', 'out'], POINTER(BSTR), 'LayerID' )),
    COMMETHOD(['propget', helpstring(u'The map units.')], HRESULT, 'MapUnits',
              ( ['retval', 'out'], POINTER(acMapUnits), 'MapUnits' )),
]
################################################################
## code template for IIMSFeatureClass implementation
##class IIMSFeatureClass_Impl(object):
##    @property
##    def MapUnits(self):
##        u'The map units.'
##        #return MapUnits
##
##    @property
##    def Axl(self):
##        u'The Feature Class AXL.'
##        #return Axl
##
##    @property
##    def LayerID(self):
##        u'The Feature Class Layer ID.'
##        #return LayerID
##

class IWCSCoverageName(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that supply WCS coverage name information.'
    _iid_ = GUID('{CB717BF3-F1EC-4BEB-A6C8-EC80A11E9010}')
    _idlflags_ = ['oleautomation']
class IWCSRange(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to IWCSRange information.'
    _iid_ = GUID('{7F5B3583-A7B7-47A9-B517-6E30AB0C1333}')
    _idlflags_ = []
IWCSCoverageDescription._methods_ = [
    COMMETHOD(['propget', helpstring(u'Name of WCS coverage.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'Title of WCS coverage.')], HRESULT, 'Title',
              ( ['retval', 'out'], POINTER(BSTR), 'Title' )),
    COMMETHOD(['propget', helpstring(u'Abstract of WCS coverage.')], HRESULT, 'Abstract',
              ( ['retval', 'out'], POINTER(BSTR), 'Abstract' )),
    COMMETHOD(['propget', helpstring(u'Identifier of WCS coverage.')], HRESULT, 'Identifier',
              ( ['retval', 'out'], POINTER(BSTR), 'Identifier' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether this coverage has been selected when it is added to the connection.')], HRESULT, 'IsSelected',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pIsSelected' )),
    COMMETHOD(['propget', helpstring(u'WCS coverage name of this description.')], HRESULT, 'WCSCoverageName',
              ( ['retval', 'out'], POINTER(POINTER(IWCSCoverageName)), 'ppName' )),
    COMMETHOD(['propput', helpstring(u'SRS name of longtitude and latitude envelope.')], HRESULT, 'LonLatSRSName',
              ( ['in'], BSTR, 'SRS' )),
    COMMETHOD(['propget', helpstring(u'SRS name of longtitude and latitude envelope.')], HRESULT, 'LonLatSRSName',
              ( ['retval', 'out'], POINTER(BSTR), 'SRS' )),
    COMMETHOD(['propget', helpstring(u'Minimum bounding extent of the coverage data.')], HRESULT, 'LonLatBoundingBox',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'ppEnvelope' )),
    COMMETHOD(['propget', helpstring(u'The default bounding box of this coverage.')], HRESULT, 'DefaultBoundingBox',
              ( ['in'], BSTR, 'CRS' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'ppEnvelope' )),
    COMMETHOD(['propget', helpstring(u'CRS name of default bounding box.')], HRESULT, 'DefaultBoundingCRS',
              ( ['retval', 'out'], POINTER(BSTR), 'CRS' )),
    COMMETHOD(['propget', helpstring(u'Spatial domain of the coverage data.')], HRESULT, 'SpatialDomain',
              ( ['retval', 'out'], POINTER(POINTER(IWCSSpatialDomain)), 'ppSpatailDomain' )),
    COMMETHOD(['propget', helpstring(u'Range of the coverage data.')], HRESULT, 'Range',
              ( ['retval', 'out'], POINTER(POINTER(IWCSRange)), 'ppRange' )),
    COMMETHOD(['propget', helpstring(u'The default interpolation.')], HRESULT, 'DefaultInterpolation',
              ( ['retval', 'out'], POINTER(BSTR), 'Interpolation' )),
    COMMETHOD(['propget', helpstring(u'Supported interpolation count.')], HRESULT, 'InterpolationCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Available interpolation at the given index.')], HRESULT, 'Interpolation',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Interpolation' )),
    COMMETHOD(['propget', helpstring(u'Supported CRS count.')], HRESULT, 'CRSCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Available CRS at the given index.')], HRESULT, 'CRS',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'CRS' )),
    COMMETHOD(['propget', helpstring(u'The native CRS or the first CRS if the native CRS is not given.')], HRESULT, 'NativeCRS',
              ( ['retval', 'out'], POINTER(BSTR), 'CRS' )),
    COMMETHOD(['propget', helpstring(u'Supported formats count.')], HRESULT, 'ImageFormatCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Available format at the given index.')], HRESULT, 'ImageFormat',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'format' )),
    COMMETHOD(['propget', helpstring(u'The native format or the first format if the native format is not given.')], HRESULT, 'NativeImageFormat',
              ( ['retval', 'out'], POINTER(BSTR), 'format' )),
]
################################################################
## code template for IWCSCoverageDescription implementation
##class IWCSCoverageDescription_Impl(object):
##    def _get(self):
##        u'SRS name of longtitude and latitude envelope.'
##        #return SRS
##    def _set(self, SRS):
##        u'SRS name of longtitude and latitude envelope.'
##    LonLatSRSName = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def DefaultBoundingCRS(self):
##        u'CRS name of default bounding box.'
##        #return CRS
##
##    @property
##    def ImageFormatCount(self):
##        u'Supported formats count.'
##        #return Count
##
##    @property
##    def LonLatBoundingBox(self):
##        u'Minimum bounding extent of the coverage data.'
##        #return ppEnvelope
##
##    @property
##    def Name(self):
##        u'Name of WCS coverage.'
##        #return Name
##
##    @property
##    def Title(self):
##        u'Title of WCS coverage.'
##        #return Title
##
##    @property
##    def CRS(self, index):
##        u'Available CRS at the given index.'
##        #return CRS
##
##    @property
##    def NativeImageFormat(self):
##        u'The native format or the first format if the native format is not given.'
##        #return format
##
##    @property
##    def Abstract(self):
##        u'Abstract of WCS coverage.'
##        #return Abstract
##
##    @property
##    def Interpolation(self, index):
##        u'Available interpolation at the given index.'
##        #return Interpolation
##
##    @property
##    def WCSCoverageName(self):
##        u'WCS coverage name of this description.'
##        #return ppName
##
##    @property
##    def CRSCount(self):
##        u'Supported CRS count.'
##        #return Count
##
##    @property
##    def IsSelected(self):
##        u'Indicates whether this coverage has been selected when it is added to the connection.'
##        #return pIsSelected
##
##    @property
##    def Range(self):
##        u'Range of the coverage data.'
##        #return ppRange
##
##    @property
##    def DefaultInterpolation(self):
##        u'The default interpolation.'
##        #return Interpolation
##
##    @property
##    def NativeCRS(self):
##        u'The native CRS or the first CRS if the native CRS is not given.'
##        #return CRS
##
##    @property
##    def SpatialDomain(self):
##        u'Spatial domain of the coverage data.'
##        #return ppSpatailDomain
##
##    @property
##    def DefaultBoundingBox(self, CRS):
##        u'The default bounding box of this coverage.'
##        #return ppEnvelope
##
##    @property
##    def ImageFormat(self, index):
##        u'Available format at the given index.'
##        #return format
##
##    @property
##    def Identifier(self):
##        u'Identifier of WCS coverage.'
##        #return Identifier
##
##    @property
##    def InterpolationCount(self):
##        u'Supported interpolation count.'
##        #return Count
##

IWCSServiceExceptionHandler._methods_ = [
    COMMETHOD([helpstring(u'Parses the response to the give URL for any WCS error codes and descriptions.')], HRESULT, 'ParseExceptions',
              ( [], BSTR, 'fileOrURL' )),
    COMMETHOD(['propget', helpstring(u'Number of exceptions.')], HRESULT, 'ExceptionCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'WCS service exception code at the given index.')], HRESULT, 'ExceptionCode',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'wcsErrorCode' )),
    COMMETHOD(['propget', helpstring(u'WCS service exception description at the given index.')], HRESULT, 'ExceptionDescription',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'wcsErrorDescription' )),
]
################################################################
## code template for IWCSServiceExceptionHandler implementation
##class IWCSServiceExceptionHandler_Impl(object):
##    @property
##    def ExceptionDescription(self, index):
##        u'WCS service exception description at the given index.'
##        #return wcsErrorDescription
##
##    def ParseExceptions(self, fileOrURL):
##        u'Parses the response to the give URL for any WCS error codes and descriptions.'
##        #return 
##
##    @property
##    def ExceptionCode(self, index):
##        u'WCS service exception code at the given index.'
##        #return wcsErrorCode
##
##    @property
##    def ExceptionCount(self):
##        u'Number of exceptions.'
##        #return Count
##

class IAGSServerConnection4(IAGSServerConnection3):
    _case_insensitive_ = True
    u'Provides access to members that have information about the GIS server connection.'
    _iid_ = GUID('{B291FD85-B247-4AB0-85D0-2244688936FD}')
    _idlflags_ = ['oleautomation']
IAGSServerConnection4._methods_ = [
    COMMETHOD([helpstring(u'Returns the server version.')], HRESULT, 'GetServerVersion',
              ( ['in'], esriAGSServerVersionType, 'versionType' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'ServerVersion' )),
    COMMETHOD([helpstring(u'Returns the URL for a service in the server behind this connection.')], HRESULT, 'GetServiceURL',
              ( ['in'], esriServiceURLType, 'urlType' ),
              ( ['in'], POINTER(IAGSServerObjectName), 'Service' ),
              ( ['retval', 'out'], POINTER(BSTR), 'URL' )),
    COMMETHOD([helpstring(u'Returns the Item Info of a service.')], HRESULT, 'GetItemInfo',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], BSTR, 'Type' ),
              ( ['in'], BSTR, 'soeType' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IItemInfo)), 'ppItemInfo' )),
    COMMETHOD([helpstring(u'Returns the metadata of a service.')], HRESULT, 'GetMetadata',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], BSTR, 'Type' ),
              ( ['in'], BSTR, 'soeType' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'ppMetadata' )),
]
################################################################
## code template for IAGSServerConnection4 implementation
##class IAGSServerConnection4_Impl(object):
##    def GetMetadata(self, Name, Type, soeType):
##        u'Returns the metadata of a service.'
##        #return ppMetadata
##
##    def GetServerVersion(self, versionType):
##        u'Returns the server version.'
##        #return ServerVersion
##
##    def GetServiceURL(self, urlType, Service):
##        u'Returns the URL for a service in the server behind this connection.'
##        #return URL
##
##    def GetItemInfo(self, Name, Type, soeType):
##        u'Returns the Item Info of a service.'
##        #return ppItemInfo
##

class IIMSWorkspace2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that provide information on the ArcIMS Workspace.'
    _iid_ = GUID('{E4A0F674-B705-405A-B356-3CC81F283622}')
    _idlflags_ = ['oleautomation']
IIMSWorkspace2._methods_ = [
    COMMETHOD(['propget', helpstring(u'Capabilities of the IMS services.')], HRESULT, 'QueryCapabilities',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'ppCapabilities' )),
    COMMETHOD(['propget', helpstring(u'The native spatial reference of the data.')], HRESULT, 'SpatialReference',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference)), 'SpatialReference' )),
    COMMETHOD(['propget', helpstring(u'The area of interest.')], HRESULT, 'AreaOfInterest',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'envelope' )),
    COMMETHOD(['propget', helpstring(u'The map units.')], HRESULT, 'MapUnits',
              ( ['retval', 'out'], POINTER(acMapUnits), 'MapUnits' )),
]
################################################################
## code template for IIMSWorkspace2 implementation
##class IIMSWorkspace2_Impl(object):
##    @property
##    def SpatialReference(self):
##        u'The native spatial reference of the data.'
##        #return SpatialReference
##
##    @property
##    def AreaOfInterest(self):
##        u'The area of interest.'
##        #return envelope
##
##    @property
##    def MapUnits(self):
##        u'The map units.'
##        #return MapUnits
##
##    @property
##    def QueryCapabilities(self):
##        u'Capabilities of the IMS services.'
##        #return ppCapabilities
##

class IWCSCoverageField(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to IWCSCoverageField information.'
    _iid_ = GUID('{D970569F-8F77-42CB-98BE-B7C0D8B87795}')
    _idlflags_ = []
IWCSRange._methods_ = [
    COMMETHOD(['propget', helpstring(u'The field count of this WCS coverage.')], HRESULT, 'FieldCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'The WCS field at the given index.')], HRESULT, 'Field',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IWCSCoverageField)), 'ppField' )),
]
################################################################
## code template for IWCSRange implementation
##class IWCSRange_Impl(object):
##    @property
##    def Field(self, index):
##        u'The WCS field at the given index.'
##        #return ppField
##
##    @property
##    def FieldCount(self):
##        u'The field count of this WCS coverage.'
##        #return Count
##

IWMTSTileMatrixSet._methods_ = [
    COMMETHOD(['propget', helpstring(u'Tile matrix set identifier.')], HRESULT, 'Identifier',
              ( ['retval', 'out'], POINTER(BSTR), 'Identifier' )),
    COMMETHOD(['propget', helpstring(u'Tile matrix set title.')], HRESULT, 'Title',
              ( ['retval', 'out'], POINTER(BSTR), 'Title' )),
    COMMETHOD(['propget', helpstring(u'Reference to one coordinate reference system (CRS).')], HRESULT, 'SupportedCRS',
              ( ['retval', 'out'], POINTER(BSTR), 'CRS' )),
    COMMETHOD(['propget', helpstring(u'Reference to a well known scale set.')], HRESULT, 'WellKnownScaleSet',
              ( ['retval', 'out'], POINTER(BSTR), 'scaleSetUri' )),
    COMMETHOD(['propget', helpstring(u'CRS for the BoundingBox')], HRESULT, 'BoundingBoxCRS',
              ( ['retval', 'out'], POINTER(BSTR), 'CRS' )),
    COMMETHOD(['propget', helpstring(u'Minimum bounding rectangle surrounding the visible layer presented by this tile matrix set, in the supported CRS.')], HRESULT, 'BoundingBox',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'BoundingBox' )),
    COMMETHOD(['propget', helpstring(u'TileMatrix count.')], HRESULT, 'TileMatrixCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'TileMatrix at the given index.')], HRESULT, 'TileMatrix',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IWMTSTileMatrix)), 'ppTileMatrix' )),
]
################################################################
## code template for IWMTSTileMatrixSet implementation
##class IWMTSTileMatrixSet_Impl(object):
##    @property
##    def WellKnownScaleSet(self):
##        u'Reference to a well known scale set.'
##        #return scaleSetUri
##
##    @property
##    def Title(self):
##        u'Tile matrix set title.'
##        #return Title
##
##    @property
##    def SupportedCRS(self):
##        u'Reference to one coordinate reference system (CRS).'
##        #return CRS
##
##    @property
##    def BoundingBoxCRS(self):
##        u'CRS for the BoundingBox'
##        #return CRS
##
##    @property
##    def TileMatrixCount(self):
##        u'TileMatrix count.'
##        #return Count
##
##    @property
##    def TileMatrix(self, index):
##        u'TileMatrix at the given index.'
##        #return ppTileMatrix
##
##    @property
##    def BoundingBox(self):
##        u'Minimum bounding rectangle surrounding the visible layer presented by this tile matrix set, in the supported CRS.'
##        #return BoundingBox
##
##    @property
##    def Identifier(self):
##        u'Tile matrix set identifier.'
##        #return Identifier
##

class IAGSServerObject(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to properties of a map or geocode server object.'
    _iid_ = GUID('{7C25FB69-EAC4-433C-B08C-7AE39E83FFBD}')
    _idlflags_ = ['oleautomation']
class IAGSServerObject2(IAGSServerObject):
    _case_insensitive_ = True
    u'Provides access to properties of a server object.'
    _iid_ = GUID('{2E07DAA3-6DEC-4DC3-A7ED-2F29E2ECFE4A}')
    _idlflags_ = ['oleautomation']
IAGSServerObject._methods_ = [
]
################################################################
## code template for IAGSServerObject implementation
##class IAGSServerObject_Impl(object):

IAGSServerObject2._methods_ = [
    COMMETHOD(['propget', helpstring(u'The AGSServerConnectionName object associated with the server object.')], HRESULT, 'FullName',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName)), 'ServerObjectName' )),
    COMMETHOD(['propput', helpstring(u'The maximum time in seconds to wait for a response from the server (Internet only).')], HRESULT, 'HttpTimeout',
              ( ['in'], c_int, 'secs' )),
    COMMETHOD(['propget', helpstring(u'The maximum time in seconds to wait for a response from the server (Internet only).')], HRESULT, 'HttpTimeout',
              ( ['retval', 'out'], POINTER(c_int), 'secs' )),
]
################################################################
## code template for IAGSServerObject2 implementation
##class IAGSServerObject2_Impl(object):
##    @property
##    def FullName(self):
##        u'The AGSServerConnectionName object associated with the server object.'
##        #return ServerObjectName
##
##    def _get(self):
##        u'The maximum time in seconds to wait for a response from the server (Internet only).'
##        #return secs
##    def _set(self, secs):
##        u'The maximum time in seconds to wait for a response from the server (Internet only).'
##    HttpTimeout = property(_get, _set, doc = _set.__doc__)
##

class IAGSServerConnectionName3(IAGSServerConnectionName2):
    _case_insensitive_ = True
    u'Provides access to members that supply GIS server connection name information.'
    _iid_ = GUID('{9FE30BFC-AA29-4763-BCC4-D9C1256427EA}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriAGSConnectionMode'
esriAGSConnectionModeConsumer = 0
esriAGSConnectionModeAdmin = 1
esriAGSConnectionModePublisher = 2
esriAGSConnectionMode = c_int # enum
IAGSServerConnectionName3._methods_ = [
    COMMETHOD(['propget', helpstring(u'The connect mode.')], HRESULT, 'ConnectionMode',
              ( ['retval', 'out'], POINTER(esriAGSConnectionMode), 'pConnMode' )),
    COMMETHOD(['propput', helpstring(u'The connect mode.')], HRESULT, 'ConnectionMode',
              ( ['in'], esriAGSConnectionMode, 'pConnMode' )),
    COMMETHOD(['propget', helpstring(u'The ArcGIS server type.')], HRESULT, 'ServerType',
              ( ['retval', 'out'], POINTER(esriAGSServerType), 'pServerType' )),
    COMMETHOD(['propput', helpstring(u'The ArcGIS server type.')], HRESULT, 'ServerType',
              ( ['in'], esriAGSServerType, 'pServerType' )),
]
################################################################
## code template for IAGSServerConnectionName3 implementation
##class IAGSServerConnectionName3_Impl(object):
##    def _get(self):
##        u'The ArcGIS server type.'
##        #return pServerType
##    def _set(self, pServerType):
##        u'The ArcGIS server type.'
##    ServerType = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The connect mode.'
##        #return pConnMode
##    def _set(self, pConnMode):
##        u'The connect mode.'
##    ConnectionMode = property(_get, _set, doc = _set.__doc__)
##

IWCSCoverageField._methods_ = [
    COMMETHOD(['propget', helpstring(u'Title of a WCS coverage field.')], HRESULT, 'Title',
              ( ['retval', 'out'], POINTER(BSTR), 'Title' )),
    COMMETHOD(['propget', helpstring(u'Abstract of a WCS coverage field.')], HRESULT, 'Abstract',
              ( ['retval', 'out'], POINTER(BSTR), 'Abstract' )),
    COMMETHOD(['propget', helpstring(u'Identifier of WCS field.')], HRESULT, 'Identifier',
              ( ['retval', 'out'], POINTER(BSTR), 'Identifier' )),
    COMMETHOD(['propget', helpstring(u'Axis ID of a WCS coverage field.')], HRESULT, 'AxisID',
              ( ['retval', 'out'], POINTER(BSTR), 'AxisID' )),
    COMMETHOD(['propget', helpstring(u'The count of available axis keys.')], HRESULT, 'AxisKeysCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Available axis key at the given index.')], HRESULT, 'AxisKey',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'key' )),
    COMMETHOD(['propget', helpstring(u'The default interpolation.')], HRESULT, 'DefaultInterpolation',
              ( ['retval', 'out'], POINTER(BSTR), 'Interpolation' )),
    COMMETHOD(['propget', helpstring(u'Supported interpolation count.')], HRESULT, 'InterpolationCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Available interpolation at the given index.')], HRESULT, 'Interpolation',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Interpolation' )),
]
################################################################
## code template for IWCSCoverageField implementation
##class IWCSCoverageField_Impl(object):
##    @property
##    def Interpolation(self, index):
##        u'Available interpolation at the given index.'
##        #return Interpolation
##
##    @property
##    def AxisKeysCount(self):
##        u'The count of available axis keys.'
##        #return Count
##
##    @property
##    def Title(self):
##        u'Title of a WCS coverage field.'
##        #return Title
##
##    @property
##    def Abstract(self):
##        u'Abstract of a WCS coverage field.'
##        #return Abstract
##
##    @property
##    def DefaultInterpolation(self):
##        u'The default interpolation.'
##        #return Interpolation
##
##    @property
##    def InterpolationCount(self):
##        u'Supported interpolation count.'
##        #return Count
##
##    @property
##    def Identifier(self):
##        u'Identifier of WCS field.'
##        #return Identifier
##
##    @property
##    def AxisID(self):
##        u'Axis ID of a WCS coverage field.'
##        #return AxisID
##
##    @property
##    def AxisKey(self, index):
##        u'Available axis key at the given index.'
##        #return key
##

class Library(object):
    u'Esri GIS Client Object Library 10.2'
    name = u'esriGISClient'
    _reg_typelib_ = ('{746F6817-89BB-4490-9829-83CA25FD505A}', 10, 2)

IWCSCoverageName._methods_ = [
    COMMETHOD(['propput', helpstring(u'Name of the WCS coverage description.')], HRESULT, 'Name',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD(['propget', helpstring(u'Name of the WCS coverage description.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'The connection name object for this description.')], HRESULT, 'WCSConnectionName',
              ( ['retval', 'out'], POINTER(POINTER(IWCSConnectionName)), 'ppServerConnName' )),
    COMMETHOD(['propputref', helpstring(u'The connection name object for this description.')], HRESULT, 'WCSConnectionName',
              ( ['in'], POINTER(IWCSConnectionName), 'ppServerConnName' )),
]
################################################################
## code template for IWCSCoverageName implementation
##class IWCSCoverageName_Impl(object):
##    def WCSConnectionName(self, ppServerConnName):
##        u'The connection name object for this description.'
##        #return 
##
##    def _get(self):
##        u'Name of the WCS coverage description.'
##        #return Name
##    def _set(self, Name):
##        u'Name of the WCS coverage description.'
##    Name = property(_get, _set, doc = _set.__doc__)
##

IWMTSServiceDescription._methods_ = [
    COMMETHOD(['propget', helpstring(u'Name of WMTS Service.')], HRESULT, 'WMTSName',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'Abstract of WMTS Service.')], HRESULT, 'WMTSAbstract',
              ( ['retval', 'out'], POINTER(BSTR), 'Abstract' )),
    COMMETHOD(['propget', helpstring(u'Title of WMTS Service.')], HRESULT, 'WMTSTitle',
              ( ['retval', 'out'], POINTER(BSTR), 'Title' )),
    COMMETHOD(['propget', helpstring(u'Version of WMTS Service.')], HRESULT, 'WMTSVersion',
              ( ['retval', 'out'], POINTER(BSTR), 'Title' )),
    COMMETHOD(['propget', helpstring(u'WMTS layer count.')], HRESULT, 'LayerDescriptionCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'WMTS layer information at the given index.')], HRESULT, 'LayerDescription',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IWMTSLayerDescription)), 'ppLayerDescription' )),
    COMMETHOD(['propget', helpstring(u'WMTS TileMatrix Set count.')], HRESULT, 'TileMatrixSetCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'WMTS Tile Matrix information at the given index.')], HRESULT, 'TileMatrixSet',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IWMTSTileMatrixSet)), 'TileMatrix' )),
    COMMETHOD(['propget', helpstring(u"Supported GetMap's ImageFormat count.")], HRESULT, 'ImageFormatCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u"Supported GetMap's ImageFormat at the given index.")], HRESULT, 'ImageFormat',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ImageFormat' )),
    COMMETHOD(['propget', helpstring(u'Supported FeatureInfoFormat count.')], HRESULT, 'FeatureInfoFormatCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Supported FeatureInfoFormat at the given index.')], HRESULT, 'FeatureInfoFormat',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ImageFormat' )),
    COMMETHOD([helpstring(u'Base url for given operation.')], HRESULT, 'GetOperationUrl',
              ( ['in'], BSTR, 'operation' ),
              ( ['retval', 'out'], POINTER(BSTR), 'BaseURL' )),
]
################################################################
## code template for IWMTSServiceDescription implementation
##class IWMTSServiceDescription_Impl(object):
##    def GetOperationUrl(self, operation):
##        u'Base url for given operation.'
##        #return BaseURL
##
##    @property
##    def WMTSName(self):
##        u'Name of WMTS Service.'
##        #return Name
##
##    @property
##    def ImageFormatCount(self):
##        u"Supported GetMap's ImageFormat count."
##        #return Count
##
##    @property
##    def WMTSAbstract(self):
##        u'Abstract of WMTS Service.'
##        #return Abstract
##
##    @property
##    def FeatureInfoFormat(self, index):
##        u'Supported FeatureInfoFormat at the given index.'
##        #return ImageFormat
##
##    @property
##    def FeatureInfoFormatCount(self):
##        u'Supported FeatureInfoFormat count.'
##        #return Count
##
##    @property
##    def LayerDescription(self, index):
##        u'WMTS layer information at the given index.'
##        #return ppLayerDescription
##
##    @property
##    def TileMatrixSet(self, index):
##        u'WMTS Tile Matrix information at the given index.'
##        #return TileMatrix
##
##    @property
##    def LayerDescriptionCount(self):
##        u'WMTS layer count.'
##        #return Count
##
##    @property
##    def WMTSVersion(self):
##        u'Version of WMTS Service.'
##        #return Title
##
##    @property
##    def TileMatrixSetCount(self):
##        u'WMTS TileMatrix Set count.'
##        #return Count
##
##    @property
##    def WMTSTitle(self):
##        u'Title of WMTS Service.'
##        #return Title
##
##    @property
##    def ImageFormat(self, index):
##        u"Supported GetMap's ImageFormat at the given index."
##        #return ImageFormat
##

__all__ = ['imsErrors', 'WMSConnectionFactory',
           'WMSCONN_E_INCORRECT_URL', 'esriAGSConnectionModeConsumer',
           'esriAGSServerVersionTypeAdmin', 'IMS_E_UNABLE_TO_CONNECT',
           'WMTSLayerDescription', 'esriAGSServerTypeUnknown',
           'IRemoteMetadataName2', 'ISetDefaultAgsConnectionInfo',
           'IRemoteMetadataName', 'IMS_E_PROXY_AUTHENTICATION_FAILED',
           'IIMSServiceDescription', 'esriAGSServerVersionType',
           'WCSConnectionFactory', 'WCSCONN_E_INCORRECT_URL',
           'WMSServiceExceptionHandler', 'WCSCONN_E_MISSING_URL',
           'IWMSConnectionFactory', 'IWMTSServiceDescription',
           'esriAGSConnectionModePublisher', 'IAGSServerConnection',
           'IIMSAxlRequest', 'acSecurityGetFeaturesDisabled',
           'WMTSConnectionFactory', 'acMiles', 'IMS_E_MISSING_URL',
           'IWCSServiceDescription', 'WCSCONN_E_MISSING_SERVICENAME',
           'IIMSWorkspace2', 'AGS_E_CONNECTION_CANCELLED',
           'IWMTSTileMatrixSetLink',
           'WMSCONN_E_PROXY_AUTHENTICATION_FAILED',
           'AGSServerConnection', 'UploadsClient',
           'IAGSServerConnectionName3', 'esriServiceURLTypeREST',
           'IAGSServerConnectionName', 'esriAGSServerTypeAGO',
           'IWMTSConnection', 'WMSCONN_E_SERVER_NOT_AVAILABLE',
           'esriAGSConnectionTypeInternet', 'acMapService',
           'IWCSConnectionName', 'IWCSBoundingBoxInfo', 'acMapUnits',
           'WCSCONN_E_SERVER_NOT_AVAILABLE', 'IMS_E_ACCESS_DENIED',
           'esriAGSServerTypeDiscovery', 'IWMTSConnectionFactory',
           'WCSServiceExceptionHandler', 'AGSServerConnectionFactory',
           'IEnumUploadItem', 'acAdministrator',
           'IMSWorkspaceFactory', 'IMSMetadataServiceName',
           'IWMSLayerDescription2', 'esriAGSConnectionTypeRESTAdmin',
           'IMSServiceName', 'IWCSSpatialDomain', 'IAdminUploader',
           'IServiceUploadsClient', 'Uploader', 'IAGSServerObject2',
           'agsClientError', 'WMTSConnectionName', 'IIMSUserRole',
           'acNotIndexed', 'acBrowser',
           'WCSCONN_E_PROXY_AUTHENTICATION_FAILED',
           'IWMSServiceDescription', 'esriAGSServerTypeSDS',
           'WMTSTileMatrixSetLink', 'IWCSCoverageName',
           'esriAGSConnectionTypeLAN', 'acSecurityType',
           'IWMSConnection', 'IWMSConnectionName',
           'esriAGSConnectionType', 'AGSServerConnectionName',
           'IWMTSConnectionName', 'esriAGSServerType',
           'IIMSWorkspace', 'IWMTSTileMatrix', 'WCSConnection',
           'IAGSEnumServerObjectName', 'IAGSServerConnection4',
           'IAGSServerConnectionName2', 'IAGSServerConnection2',
           'IAGSServerConnection3', 'IWCSCoverageField',
           'IIMSFeatureClass', 'IAGSServerConnectionFactory2',
           'WMTSConnection', 'IAGSServerConnectionFactory3',
           'acKilometers', 'IWMTSLayerDescription', 'wmsErrors',
           'WCSCONN_E_UNABLE_TO_CONNECT', 'WMSConnection',
           'acPublisher', 'AGS_E_UPLOAD_IS_TOO_LARGE',
           'WMSCONN_E_UNABLE_TO_CONNECT', 'IWMTSDimension',
           'esriAGSConnectionMode', 'IWCSRange',
           'AGSServerObjectName', 'WMTSTileMatrixSet',
           'IAdminUploadsClient', 'IWMSClientEvents', 'acUserRole',
           'IWCSClientEvents', 'IWMSLayerStyleDescription',
           'acMetadataService', 'acIndexError', 'acServiceType',
           'IServerObjectDescription', 'esriAGSConnectionModeAdmin',
           'WMSCONN_E_MISSING_URL', 'AGS_E_REDIRECTION',
           'acUnknownService', 'IWCSServiceExceptionHandler',
           'esriServiceURLTypeAdmin', 'WMSConnectionName',
           'IUploadItem', 'WMSCONN_E_MISSING_SERVICENAME',
           'acFeatureService', 'IWCSConnection', 'IUploader',
           'IWCSConnectionFactory', 'esriAGSServerTypeClassic',
           'IIMSMetadataAxlRequest', 'acIndexed',
           'AGS_E_SERVICE_STARTED_WITH_ERRORS', 'acLegacyUser',
           'esriAGSServerVersionTypeSoap',
           'IEnumAGSServerConnectionName',
           'AGS_E_INSECURE_TOKENSERVICEURL',
           'IWMSServiceExceptionHandler', 'esriServiceURLType',
           'IMS_E_MISSING_SERVICENAME', 'WMTSTileMatrix', 'wcsErrors',
           'IWCSCoverageDescription', 'IMSCatalogPathParser',
           'esriServiceURLTypeSoap', 'IAGSServerObject',
           'IUploadsClient', 'WMSCONN_E_ACCESS_DENIED',
           'WCSConnectionName', 'acGlobeService', 'IServiceUploader',
           'IWMTSTileMatrixSet', 'UploadItem', 'acSecurityNone',
           'acServiceAuthor', 'IAGSServerObjectName2',
           'IAGSServerObjectName3', 'acDecimalDegrees',
           'WMTSDimension', 'esriAGSServerVersionTypeREST',
           'AGS_E_NO_CONNECT_INSECURE_TOKENSERVICEURL',
           'IAGSServerConnectionFactory', 'acIndexStatus',
           'WCSCONN_E_ACCESS_DENIED', 'acFeet',
           'IRESTServerObjectAdmin', 'acMeters',
           'IAGSServerConnectionAdmin', 'acWMSService',
           'IAGSServerObjectName', 'IWMSLayerDescription']
from comtypes import _check_version; _check_version('501')

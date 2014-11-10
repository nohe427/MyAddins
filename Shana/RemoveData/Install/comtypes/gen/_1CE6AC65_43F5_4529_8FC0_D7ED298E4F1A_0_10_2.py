# -*- coding: mbcs -*-
typelib_path = u'C:\\Program Files (x86)\\ArcGIS\\Engine10.2\\com\\esriDataSourcesFile.olb'
_lcid = 0 # change this if required
from ctypes import *
import comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2
from comtypes import GUID
from comtypes import CoClass
import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0
from comtypes import helpstring
from comtypes import COMMETHOD
from comtypes import dispid
from comtypes import BSTR
from ctypes import HRESULT
from comtypes.automation import VARIANT
import comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2
from ctypes.wintypes import VARIANT_BOOL
import comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2
from comtypes.automation import VARIANT


class ShapefileWorkspaceFactory(CoClass):
    u'Esri Shapefile Workspace Factory.'
    _reg_clsid_ = GUID('{A06ADB96-D95C-11D1-AA81-00C04FA33A15}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
ShapefileWorkspaceFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceFactory, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceFactory2]

class IDECatalogRoot(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the Catalog Root Data Element.'
    _iid_ = GUID('{49B7BB60-02C3-49DE-9642-A0B07215DA63}')
    _idlflags_ = ['oleautomation']
IDECatalogRoot._methods_ = [
]
################################################################
## code template for IDECatalogRoot implementation
##class IDECatalogRoot_Impl(object):

class IDataLicenseInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to data license information.'
    _iid_ = GUID('{37474491-1C04-4669-99B5-825CF67294C5}')
    _idlflags_ = []
class IMetaInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to meta information.'
    _iid_ = GUID('{0DB7A450-5FED-441B-BB3A-DB6E24D6CDA3}')
    _idlflags_ = []

# values for enumeration 'esriDataLicenseType'
esriDataLicSeatType = 1
esriDataLicFloatType = 2
esriDataLicenseType = c_int # enum
class IUsageModeInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to user mode information.'
    _iid_ = GUID('{07713846-9DA7-45F8-886F-3EB2F0A30187}')
    _idlflags_ = []
IDataLicenseInfo._methods_ = [
    COMMETHOD(['propget', helpstring(u'Name of data product.')], HRESULT, 'DataProductName',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Number of licensed applications.')], HRESULT, 'ApplicationsCount',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Name of licensed applications.')], HRESULT, 'ApplicationName',
              ( ['in'], c_int, 'nIdx' ),
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Number of attribute groups.')], HRESULT, 'AttrCroupsCount',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Name of attribute group.')], HRESULT, 'AttrGroupName',
              ( ['in'], c_int, 'nIdx' ),
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Number of geographies divisions')], HRESULT, 'GeographiesCount',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Name of geographies divisions.')], HRESULT, 'GeographyName',
              ( ['in'], c_int, 'nIdx' ),
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Number of meta information strings.')], HRESULT, 'MetaCount',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Meta information pair.')], HRESULT, 'MetaInfo',
              ( ['in'], c_int, 'nIdx' ),
              ( ['retval', 'out'], POINTER(POINTER(IMetaInfo)), 'ppMeta' )),
    COMMETHOD(['propget', helpstring(u'Number of layer groups.')], HRESULT, 'LayerCroupsCount',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Name of layer groups.')], HRESULT, 'LayerGroupName',
              ( ['in'], c_int, 'nIdx' ),
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propget', helpstring(u'License ID.')], HRESULT, 'LicenseID',
              ( ['retval', 'out'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Expiration date.')], HRESULT, 'Expiration',
              ( ['retval', 'out'], POINTER(VARIANT), 'pvtDate' )),
    COMMETHOD(['propget', helpstring(u'License type.')], HRESULT, 'LicenseType',
              ( ['retval', 'out'], POINTER(esriDataLicenseType), 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Maximum connections allowed.')], HRESULT, 'MaxConnections',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Available connections.')], HRESULT, 'AvailableConnections',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Number of usage modes.')], HRESULT, 'UsageModeCount',
              ( ['retval', 'out'], POINTER(c_int), 'pnCount' )),
    COMMETHOD(['propget', helpstring(u'Usage mode by its number.')], HRESULT, 'UsageMode',
              ( ['in'], c_int, 'nIndex' ),
              ( ['retval', 'out'], POINTER(POINTER(IUsageModeInfo)), 'pInfo' )),
]
################################################################
## code template for IDataLicenseInfo implementation
##class IDataLicenseInfo_Impl(object):
##    @property
##    def ApplicationName(self, nIdx):
##        u'Name of licensed applications.'
##        #return pVal
##
##    @property
##    def LicenseType(self):
##        u'License type.'
##        #return pVal
##
##    @property
##    def LayerGroupName(self, nIdx):
##        u'Name of layer groups.'
##        #return pVal
##
##    @property
##    def MetaCount(self):
##        u'Number of meta information strings.'
##        #return pVal
##
##    @property
##    def LayerCroupsCount(self):
##        u'Number of layer groups.'
##        #return pVal
##
##    @property
##    def LicenseID(self):
##        u'License ID.'
##        #return pVal
##
##    @property
##    def GeographyName(self, nIdx):
##        u'Name of geographies divisions.'
##        #return pVal
##
##    @property
##    def MetaInfo(self, nIdx):
##        u'Meta information pair.'
##        #return ppMeta
##
##    @property
##    def GeographiesCount(self):
##        u'Number of geographies divisions'
##        #return pVal
##
##    @property
##    def DataProductName(self):
##        u'Name of data product.'
##        #return pVal
##
##    @property
##    def AttrGroupName(self, nIdx):
##        u'Name of attribute group.'
##        #return pVal
##
##    @property
##    def MaxConnections(self):
##        u'Maximum connections allowed.'
##        #return pVal
##
##    @property
##    def UsageMode(self, nIndex):
##        u'Usage mode by its number.'
##        #return pInfo
##
##    @property
##    def Expiration(self):
##        u'Expiration date.'
##        #return pvtDate
##
##    @property
##    def ApplicationsCount(self):
##        u'Number of licensed applications.'
##        #return pVal
##
##    @property
##    def AvailableConnections(self):
##        u'Available connections.'
##        #return pVal
##
##    @property
##    def UsageModeCount(self):
##        u'Number of usage modes.'
##        #return pnCount
##
##    @property
##    def AttrCroupsCount(self):
##        u'Number of attribute groups.'
##        #return pVal
##

class DECadDrawingDatasetType(CoClass):
    u'CadDrawing Dataset Data Element object Type.'
    _reg_clsid_ = GUID('{43A72293-AAC8-4F0C-B8F8-8B2CDB298F85}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
class IDECadDrawingDatasetType(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the CadDrawing Dataset Data Element Type.'
    _iid_ = GUID('{6850E61D-EDA7-45FF-9291-25AF6C10C556}')
    _idlflags_ = ['oleautomation']
DECadDrawingDatasetType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDECadDrawingDatasetType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEFeatureDatasetType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEGeoDatasetType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEDatasetType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElementType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGxFilterInfo, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDataType, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone]

class IDataLicenseManager(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to data license manager.'
    _iid_ = GUID('{2D5B7A40-F25B-4490-B36C-EDD367DF33D0}')
    _idlflags_ = []
IDataLicenseManager._methods_ = [
    COMMETHOD(['propget', helpstring(u'Number of license information.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD([helpstring(u'Returns license information by index.')], HRESULT, 'GetLicenseInfo',
              ( ['in'], c_int, 'nIdx' ),
              ( ['retval', 'out'], POINTER(POINTER(IDataLicenseInfo)), 'pLicInfo' )),
    COMMETHOD([helpstring(u'Adds license information.')], HRESULT, 'AddLicenseFromFile',
              ( ['in'], BSTR, 'bstrLicenseFileName' )),
    COMMETHOD([helpstring(u'Removes license information.')], HRESULT, 'RemoveLicense',
              ( ['in'], c_int, 'nIdx' )),
    COMMETHOD([helpstring(u'Returns license information by file name.')], HRESULT, 'GetLicenseInfoFromFile',
              ( ['in'], BSTR, 'bstrLicenseFileName' ),
              ( ['retval', 'out'], POINTER(POINTER(IDataLicenseInfo)), 'pLicInfo' )),
]
################################################################
## code template for IDataLicenseManager implementation
##class IDataLicenseManager_Impl(object):
##    @property
##    def Count(self):
##        u'Number of license information.'
##        #return pVal
##
##    def AddLicenseFromFile(self, bstrLicenseFileName):
##        u'Adds license information.'
##        #return 
##
##    def RemoveLicense(self, nIdx):
##        u'Removes license information.'
##        #return 
##
##    def GetLicenseInfoFromFile(self, bstrLicenseFileName):
##        u'Returns license information by file name.'
##        #return pLicInfo
##
##    def GetLicenseInfo(self, nIdx):
##        u'Returns license information by index.'
##        #return pLicInfo
##


# values for enumeration 'esriSMRestrictionType'
esriSMRTStrict = 1
esriSMRTRelaxed = 2
esriSMRestrictionType = c_int # enum
class IArcInfoItem(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that retrieve ArcInfo Item information.'
    _iid_ = GUID('{B5E470D2-CEAB-11D2-B0DC-0000F8780820}')
    _idlflags_ = ['oleautomation']
class IArcInfoItemEdit(IArcInfoItem):
    _case_insensitive_ = True
    u'Provides access to members that control ArcInfo Item Editing.'
    _iid_ = GUID('{B5E470D3-CEAB-11D2-B0DC-0000F8780820}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriArcInfoItemType'
esriItemTypeDate = 1
esriItemTypeCharacter = 2
esriItemTypeInteger = 3
esriItemTypeNumber = 4
esriItemTypeBinary = 5
esriItemTypeFloat = 6
esriItemTypeLeadFill = 7
esriItemTypePacked = 8
esriItemTypeZeroFill = 9
esriItemTypeOverpunch = 10
esriItemTypeTrailingSign = 11
esriItemTypeOID = 12
esriItemTypeGeometry = 13
esriItemTypeBlob = 14
esriArcInfoItemType = c_int # enum
IArcInfoItem._methods_ = [
    COMMETHOD(['propget', helpstring(u'Start Position of the Item.')], HRESULT, 'StartPosition',
              ( ['retval', 'out'], POINTER(c_int), 'StartPosition' )),
    COMMETHOD(['propget', helpstring(u'Name of the Item.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'Storage Width, in Bytes, for values stored in the Item.')], HRESULT, 'Width',
              ( ['retval', 'out'], POINTER(c_int), 'Width' )),
    COMMETHOD(['propget', helpstring(u'Output Width, in Bytes, for values stored in the Item.')], HRESULT, 'OutputWidth',
              ( ['retval', 'out'], POINTER(c_int), 'OutputWidth' )),
    COMMETHOD(['propget', helpstring(u'Type of the Item, as an enumeration.')], HRESULT, 'Type',
              ( ['retval', 'out'], POINTER(esriArcInfoItemType), 'Type' )),
    COMMETHOD(['propget', helpstring(u'Number of Decimals for Item values.')], HRESULT, 'NumberDecimals',
              ( ['retval', 'out'], POINTER(c_int), 'NumberDecimals' )),
    COMMETHOD(['propget', helpstring(u'Alternate Name of the Item.')], HRESULT, 'AlternateName',
              ( ['retval', 'out'], POINTER(BSTR), 'AlternateName' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the Item is a Redefined Item.')], HRESULT, 'IsRedefined',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsRedefined' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the Item is a Pseudo Item.')], HRESULT, 'IsPseudo',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsPseudo' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the Item is Indexed.')], HRESULT, 'IsIndexed',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsIndexed' )),
]
################################################################
## code template for IArcInfoItem implementation
##class IArcInfoItem_Impl(object):
##    @property
##    def Name(self):
##        u'Name of the Item.'
##        #return Name
##
##    @property
##    def OutputWidth(self):
##        u'Output Width, in Bytes, for values stored in the Item.'
##        #return OutputWidth
##
##    @property
##    def StartPosition(self):
##        u'Start Position of the Item.'
##        #return StartPosition
##
##    @property
##    def IsPseudo(self):
##        u'Indicates if the Item is a Pseudo Item.'
##        #return IsPseudo
##
##    @property
##    def IsIndexed(self):
##        u'Indicates if the Item is Indexed.'
##        #return IsIndexed
##
##    @property
##    def Width(self):
##        u'Storage Width, in Bytes, for values stored in the Item.'
##        #return Width
##
##    @property
##    def IsRedefined(self):
##        u'Indicates if the Item is a Redefined Item.'
##        #return IsRedefined
##
##    @property
##    def AlternateName(self):
##        u'Alternate Name of the Item.'
##        #return AlternateName
##
##    @property
##    def Type(self):
##        u'Type of the Item, as an enumeration.'
##        #return Type
##
##    @property
##    def NumberDecimals(self):
##        u'Number of Decimals for Item values.'
##        #return NumberDecimals
##

IArcInfoItemEdit._methods_ = [
    COMMETHOD(['propput', helpstring(u'Start Position of the Item.')], HRESULT, 'StartPosition',
              ( ['in'], c_int, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Name of the Item.')], HRESULT, 'Name',
              ( ['in'], BSTR, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Storage Width, in Bytes, for values stored in the Item.')], HRESULT, 'Width',
              ( ['in'], c_int, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Output Width, in Bytes, for values stored in the Item.')], HRESULT, 'OutputWidth',
              ( ['in'], c_int, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Type of the Item, as an enumeration.')], HRESULT, 'Type',
              ( ['in'], esriArcInfoItemType, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Number of Decimals for Item values.')], HRESULT, 'NumberDecimals',
              ( ['in'], c_int, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Alternate Name of the Item.')], HRESULT, 'AlternateName',
              ( ['in'], BSTR, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the Item is Redefined.')], HRESULT, 'IsRedefined',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the Item is a Pseudo Item.')], HRESULT, 'IsPseudo',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the Item is Indexed.')], HRESULT, 'IsIndexed',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
]
################################################################
## code template for IArcInfoItemEdit implementation
##class IArcInfoItemEdit_Impl(object):
##    def _set(self, rhs):
##        u'Name of the Item.'
##    Name = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Output Width, in Bytes, for values stored in the Item.'
##    OutputWidth = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Start Position of the Item.'
##    StartPosition = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Indicates if the Item is a Pseudo Item.'
##    IsPseudo = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Indicates if the Item is Indexed.'
##    IsIndexed = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Storage Width, in Bytes, for values stored in the Item.'
##    Width = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Indicates if the Item is Redefined.'
##    IsRedefined = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Alternate Name of the Item.'
##    AlternateName = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Type of the Item, as an enumeration.'
##    Type = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Number of Decimals for Item values.'
##    NumberDecimals = property(fset = _set, doc = _set.__doc__)
##

class DECoverageType(CoClass):
    u'Coverage Data Element object Type.'
    _reg_clsid_ = GUID('{80172DB6-5715-4157-B253-6150EA74203E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
class IDECoverageType(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Indicator interface for the Coverage Data Element Type.'
    _iid_ = GUID('{AB6143ED-A1EA-4193-B97C-F8BE9A6C4C83}')
    _idlflags_ = ['oleautomation']
DECoverageType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDECoverageType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEFeatureDatasetType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEGeoDatasetType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEDatasetType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElementType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGxFilterInfo, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDataType, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone]

class DEPrjFileType(CoClass):
    u'Projection File Data Element object Type.'
    _reg_clsid_ = GUID('{EBFEBC90-CFBF-11D5-933D-0080C71A3226}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
class IDEPrjFileType(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the Projection File Data Element Type.'
    _iid_ = GUID('{AE8C96F0-CFBE-11D5-933D-0080C71A3226}')
    _idlflags_ = ['oleautomation']
class IDEFileType(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the File Data Element Type.'
    _iid_ = GUID('{5CEA7586-5550-418A-A6CB-9B8E67133C43}')
    _idlflags_ = ['oleautomation']
DEPrjFileType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDEPrjFileType, IDEFileType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElementType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDataType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGxFilterInfo, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone]

class IGPLayer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the GP Layer Type.'
    _iid_ = GUID('{EA30B18D-2D75-4593-BF44-B3620F41D8DB}')
    _idlflags_ = ['oleautomation']
IGPLayer._methods_ = [
    COMMETHOD(['propget', helpstring(u'The name string.')], HRESULT, 'NameString',
              ( ['retval', 'out'], POINTER(BSTR), 'pNamestring' )),
    COMMETHOD(['propput', helpstring(u'The name string.')], HRESULT, 'NameString',
              ( ['in'], BSTR, 'pNamestring' )),
    COMMETHOD(['propget', helpstring(u'The default area of interest for the layer.')], HRESULT, 'AreaOfInterest',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'ppExtent' )),
    COMMETHOD(['propputref', helpstring(u'The default area of interest for the layer.')], HRESULT, 'AreaOfInterest',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'ppExtent' )),
    COMMETHOD([helpstring(u'The set Extent of the feature layer.')], HRESULT, 'SetAOICoords',
              ( ['in'], c_double, 'xMin' ),
              ( ['in'], c_double, 'yMin' ),
              ( ['in'], c_double, 'xMax' ),
              ( ['in'], c_double, 'yMax' )),
    COMMETHOD(['propget', helpstring(u'The data element of the layer.')], HRESULT, 'DataElement',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElement)), 'ppDataElement' )),
    COMMETHOD(['propputref', helpstring(u'The data element of the layer.')], HRESULT, 'DataElement',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElement), 'ppDataElement' )),
]
################################################################
## code template for IGPLayer implementation
##class IGPLayer_Impl(object):
##    def _get(self):
##        u'The name string.'
##        #return pNamestring
##    def _set(self, pNamestring):
##        u'The name string.'
##    NameString = property(_get, _set, doc = _set.__doc__)
##
##    def SetAOICoords(self, xMin, yMin, xMax, yMax):
##        u'The set Extent of the feature layer.'
##        #return 
##
##    def AreaOfInterest(self, ppExtent):
##        u'The default area of interest for the layer.'
##        #return 
##
##    def DataElement(self, ppDataElement):
##        u'The data element of the layer.'
##        #return 
##

class IGPLayerType(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Indicator interface for a GPLayer Type.'
    _iid_ = GUID('{8547FF12-E020-4C17-893B-BDA0176F0C3B}')
    _idlflags_ = ['oleautomation']
IGPLayerType._methods_ = [
]
################################################################
## code template for IGPLayerType implementation
##class IGPLayerType_Impl(object):

class IUsageModeOption(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to user mode options.'
    _iid_ = GUID('{C1D85FC8-F132-4187-B897-623C647C9213}')
    _idlflags_ = []
IUsageModeInfo._methods_ = [
    COMMETHOD(['propget', helpstring(u'Usage mode name.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'psName' )),
    COMMETHOD(['propget', helpstring(u'Usage mode options count.')], HRESULT, 'OptionCount',
              ( ['retval', 'out'], POINTER(c_int), 'pnCount' )),
    COMMETHOD(['propget', helpstring(u'Usage mode option.')], HRESULT, 'Option',
              ( ['in'], c_int, 'nIndex' ),
              ( ['retval', 'out'], POINTER(POINTER(IUsageModeOption)), 'pOption' )),
]
################################################################
## code template for IUsageModeInfo implementation
##class IUsageModeInfo_Impl(object):
##    @property
##    def OptionCount(self):
##        u'Usage mode options count.'
##        #return pnCount
##
##    @property
##    def Name(self):
##        u'Usage mode name.'
##        #return psName
##
##    @property
##    def Option(self, nIndex):
##        u'Usage mode option.'
##        #return pOption
##

class DEArcInfoTableType(CoClass):
    u'ArcInfo Table Data Element object Type.'
    _reg_clsid_ = GUID('{0E3F5CB0-2445-4ABB-BE9A-FCF0492E180A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
class IDEArcInfoTableType(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Indicator interface for the ArcInfo Table Data Element Type.'
    _iid_ = GUID('{2864D010-402B-4B4E-B27C-DB2CB238FFE4}')
    _idlflags_ = ['oleautomation']
DEArcInfoTableType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDEArcInfoTableType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDETableType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEDatasetType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElementType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGxFilterInfo, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDataType, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone]

IMetaInfo._methods_ = [
    COMMETHOD(['propget', helpstring(u'Meta information parameter name.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'psName' )),
    COMMETHOD(['propget', helpstring(u'Mata information parameter value.')], HRESULT, 'Value',
              ( ['retval', 'out'], POINTER(BSTR), 'psValue' )),
]
################################################################
## code template for IMetaInfo implementation
##class IMetaInfo_Impl(object):
##    @property
##    def Name(self):
##        u'Meta information parameter name.'
##        #return psName
##
##    @property
##    def Value(self):
##        u'Mata information parameter value.'
##        #return psValue
##

class DECatalogRoot(CoClass):
    u'Catalog Root Data Element object.'
    _reg_clsid_ = GUID('{01D6EBDD-DE9A-4217-8BFE-327265855FA2}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
DECatalogRoot._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDECatalogRoot, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElement, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPValue, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDescribe]

class IArcInfoTable(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that modify ArcInfo Tables.'
    _iid_ = GUID('{D3EC3D31-CFFE-11D2-B0DC-0000F8780820}')
    _idlflags_ = ['oleautomation']
class IArcInfoItems(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that retrieve ArcInfo Items Collection information.'
    _iid_ = GUID('{B5E470D4-CEAB-11D2-B0DC-0000F8780820}')
    _idlflags_ = ['oleautomation']
IArcInfoTable._methods_ = [
    COMMETHOD([helpstring(u'Index of the Item with the specified name.')], HRESULT, 'FindItem',
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(c_int), 'itemIndex' )),
    COMMETHOD(['propget', helpstring(u'Item Collection for this Feature Class or Info Table.')], HRESULT, 'ItemSet',
              ( ['retval', 'out'], POINTER(POINTER(IArcInfoItems)), 'ItemSet' )),
    COMMETHOD([helpstring(u'Adds an Item to this Table.')], HRESULT, 'AddItem',
              ( ['in'], POINTER(IArcInfoItem), 'Item' ),
              ( ['in'], BSTR, 'startItem' )),
    COMMETHOD([helpstring(u'Deletes an Item from this Table.')], HRESULT, 'DeleteItem',
              ( ['in'], BSTR, 'itemName' )),
    COMMETHOD([helpstring(u'Adds an Index for the specified Item.')], HRESULT, 'AddIndex',
              ( ['in'], BSTR, 'itemName' )),
    COMMETHOD([helpstring(u'Deletes an Index from the specified Item.')], HRESULT, 'DeleteIndex',
              ( ['in'], BSTR, 'itemName' )),
    COMMETHOD([helpstring(u'Changes the properties of the specified Item.')], HRESULT, 'AlterItem',
              ( ['in'], BSTR, 'itemName' ),
              ( ['in'], POINTER(IArcInfoItem), 'Item' )),
]
################################################################
## code template for IArcInfoTable implementation
##class IArcInfoTable_Impl(object):
##    def DeleteIndex(self, itemName):
##        u'Deletes an Index from the specified Item.'
##        #return 
##
##    def AddIndex(self, itemName):
##        u'Adds an Index for the specified Item.'
##        #return 
##
##    def AlterItem(self, itemName, Item):
##        u'Changes the properties of the specified Item.'
##        #return 
##
##    def AddItem(self, Item, startItem):
##        u'Adds an Item to this Table.'
##        #return 
##
##    @property
##    def ItemSet(self):
##        u'Item Collection for this Feature Class or Info Table.'
##        #return ItemSet
##
##    def FindItem(self, Name):
##        u'Index of the Item with the specified name.'
##        #return itemIndex
##
##    def DeleteItem(self, itemName):
##        u'Deletes an Item from this Table.'
##        #return 
##

class DERemoteDatabaseFolderType(CoClass):
    u'Remote Database Folder Data Element object Type.'
    _reg_clsid_ = GUID('{2919C9EF-DC76-4C52-9539-F357A4F68925}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
class IDERemoteDatabaseFolderType(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the Remote Database Folder Data Element Type.'
    _iid_ = GUID('{EF94D455-32D3-4D10-B080-FE7508C05DC9}')
    _idlflags_ = ['oleautomation']
DERemoteDatabaseFolderType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDERemoteDatabaseFolderType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElementType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDataType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGxFilterInfo, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone]

class ICoverageName(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that maintains ArcInfo Coverage Feature Dataset Information.'
    _iid_ = GUID('{DE61A108-0E08-11D3-9F31-00C04F79927C}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriCoverageType'
esriEmptyCoverage = 0
esriAnnotationCoverage = 1
esriPointCoverage = 2
esriLineCoverage = 3
esriPolygonCoverage = 4
esriPreliminaryPolygonCoverage = 5
esriCoverageType = c_int # enum
ICoverageName._methods_ = [
    COMMETHOD(['propget', helpstring(u'Type of the Coverage.')], HRESULT, 'CoverageType',
              ( ['retval', 'out'], POINTER(esriCoverageType), 'CoverageType' )),
    COMMETHOD(['propput', helpstring(u'Type of the Coverage.')], HRESULT, 'CoverageType',
              ( ['in'], esriCoverageType, 'CoverageType' )),
]
################################################################
## code template for ICoverageName implementation
##class ICoverageName_Impl(object):
##    def _get(self):
##        u'Type of the Coverage.'
##        #return CoverageType
##    def _set(self, CoverageType):
##        u'Type of the Coverage.'
##    CoverageType = property(_get, _set, doc = _set.__doc__)
##

class IDEPrjFile(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the Projection File Data Element.'
    _iid_ = GUID('{F69CA920-CFBB-11D5-933D-0080C71A3226}')
    _idlflags_ = ['oleautomation']
IDEPrjFile._methods_ = [
    COMMETHOD(['propget', helpstring(u'SpatialReference.')], HRESULT, 'SpatialReference',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference)), 'ppSpatialReference' )),
    COMMETHOD(['propputref', helpstring(u'SpatialReference.')], HRESULT, 'SpatialReference',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference), 'ppSpatialReference' )),
]
################################################################
## code template for IDEPrjFile implementation
##class IDEPrjFile_Impl(object):
##    def SpatialReference(self, ppSpatialReference):
##        u'SpatialReference.'
##        #return 
##

class DEFolderType(CoClass):
    u'Folder Data Element object Type.'
    _reg_clsid_ = GUID('{FE29B0ED-DECF-4A61-8ED0-BE233BFE376B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
class IDEFolderType(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the Folder Data Element Type.'
    _iid_ = GUID('{B2DFE80E-7EE0-4AAA-BEE0-498593374743}')
    _idlflags_ = ['oleautomation']
DEFolderType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDEFolderType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEWorkspaceType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElementType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDataType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGxFilterInfo, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone]

class DECadDrawingDataset(CoClass):
    u'Cad Drawing Dataset Data Element object.'
    _reg_clsid_ = GUID('{F786332D-20B2-4607-BF34-0A53E4D0B413}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
class IDECadDrawingDataset(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the CadDrawingDataset Data Element.'
    _iid_ = GUID('{6EC9D0C5-C3C5-4A2C-B9B3-5959209F427C}')
    _idlflags_ = ['oleautomation']
DECadDrawingDataset._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDECadDrawingDataset, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEFeatureDataset, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEGeoDataset, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEDataset, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElement, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPValue, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDescribe]

class IInfoTableOnlyWorkspaceEdit(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that limit internal editing to standalone tables only.'
    _iid_ = GUID('{215B5973-795C-499F-B3FF-798C1CD4DBE6}')
    _idlflags_ = ['oleautomation']
IInfoTableOnlyWorkspaceEdit._methods_ = [
    COMMETHOD([helpstring(u'Start editing standalone Info Tables only.')], HRESULT, 'StartEditingTablesOnly',
              ( ['in'], VARIANT_BOOL, 'withUndoRedo' )),
]
################################################################
## code template for IInfoTableOnlyWorkspaceEdit implementation
##class IInfoTableOnlyWorkspaceEdit_Impl(object):
##    def StartEditingTablesOnly(self, withUndoRedo):
##        u'Start editing standalone Info Tables only.'
##        #return 
##

class DETin(CoClass):
    u'Tin Data Element object.'
    _reg_clsid_ = GUID('{5EDC32F1-C1B2-4808-88E0-2ED68E77269D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
class IDETin(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the TIN Data Element.'
    _iid_ = GUID('{B0B62284-0080-4EA3-9716-DE5293A73F6E}')
    _idlflags_ = ['oleautomation']
DETin._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDETin, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEGeoDataset, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEDataset, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElement, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPValue, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDescribe]


# values for enumeration 'esriCadTransform'
esriCadTransformByWorldFile = 0
esriCadTransformByPoints = 1
esriCadTransformByRst = 2
esriCadTransform = c_int # enum
class SMRouterPoint(CoClass):
    u'Deprecated as of 10.1. The geographic location of the point.'
    _reg_clsid_ = GUID('{F8B65FEE-5850-11D7-B321-008048DB11DE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
class ISMRouterPoint(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Deprecated as of 10.1. Provides access to the location of single geographic point.'
    _iid_ = GUID('{F8B65FED-5850-11D7-B321-008048DB11DE}')
    _idlflags_ = ['dual', 'oleautomation']
SMRouterPoint._com_interfaces_ = [ISMRouterPoint]

class ICadSettings(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the use of Dgn files with any file extension.'
    _iid_ = GUID('{628022FD-E7DF-11D4-A2A8-444553547777}')
    _idlflags_ = ['oleautomation']
ICadSettings._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates whether the use of Dgn files with any file extension is enabled.')], HRESULT, 'EnableAllDgnFileExtensions',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pEnabled' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether the use of Dgn files with any file extension is enabled.')], HRESULT, 'EnableAllDgnFileExtensions',
              ( ['in'], VARIANT_BOOL, 'pEnabled' )),
]
################################################################
## code template for ICadSettings implementation
##class ICadSettings_Impl(object):
##    def _get(self):
##        u'Indicates whether the use of Dgn files with any file extension is enabled.'
##        #return pEnabled
##    def _set(self, pEnabled):
##        u'Indicates whether the use of Dgn files with any file extension is enabled.'
##    EnableAllDgnFileExtensions = property(_get, _set, doc = _set.__doc__)
##


# values for enumeration 'esriSMBacktrackPolicy'
esriSMBTPDisable = 1
esriSMBTPAllow = 2
esriSMBTPDeadend = 3
esriSMBacktrackPolicy = c_int # enum

# values for enumeration 'esriSMStreetSideType'
esriSMStreetSideLeft = 1
esriSMStreetSideRight = 2
esriSMStreetSideUndefined = 3
esriSMStreetSideType = c_int # enum
class ISMRouterSetup(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Deprecated as of 10.1. Provides access to router settings, such as restrictions, backtrack policy, length units.'
    _iid_ = GUID('{A386707F-FB42-4D0E-AF12-3C1FEB26F771}')
    _idlflags_ = ['dual', 'oleautomation']
class ISMRouterSetup2(ISMRouterSetup):
    _case_insensitive_ = True
    u'Deprecated as of 10.1. Provides access to router restrictions settings.'
    _iid_ = GUID('{06EFA9D2-490C-4325-BF15-3F73F4492F34}')
    _idlflags_ = ['dual', 'oleautomation']
class ISMRestriction(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Deprecated as of 10.1. Provides access to the routing restriction properties.'
    _iid_ = GUID('{3DF8D708-18E9-4D3C-BC69-54190A3577D8}')
    _idlflags_ = ['dual', 'oleautomation']

# values for enumeration 'esriSMDirectionsLengthUnits'
esriSMDLUMiles = 1
esriSMDLUKilometers = 2
esriSMDLUMeters = 3
esriSMDLUFeet = 4
esriSMDLUYards = 5
esriSMDirectionsLengthUnits = c_int # enum
ISMRouterSetup._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Sets a restriction to be used by the route solver.')], HRESULT, 'SetRestriction',
              ( ['in'], POINTER(ISMRestriction), 'pRestriction' )),
    COMMETHOD([dispid(2), helpstring(u'Removes all restrictions set on the route solver.')], HRESULT, 'ClearAllRestrictions'),
    COMMETHOD([dispid(3), helpstring(u'Controls the backtrack policy of the route solver.'), 'propget'], HRESULT, 'BacktrackPolicy',
              ( ['retval', 'out'], POINTER(esriSMBacktrackPolicy), 'pVal' )),
    COMMETHOD([dispid(3), helpstring(u'Controls the backtrack policy of the route solver.'), 'propput'], HRESULT, 'BacktrackPolicy',
              ( ['in'], esriSMBacktrackPolicy, 'pVal' )),
    COMMETHOD([dispid(4), helpstring(u'The output length units used in driving directions.'), 'propget'], HRESULT, 'DirectionsLengthUnits',
              ( ['retval', 'out'], POINTER(esriSMDirectionsLengthUnits), 'pVal' )),
    COMMETHOD([dispid(4), helpstring(u'The output length units used in driving directions.'), 'propput'], HRESULT, 'DirectionsLengthUnits',
              ( ['in'], esriSMDirectionsLengthUnits, 'pVal' )),
]
################################################################
## code template for ISMRouterSetup implementation
##class ISMRouterSetup_Impl(object):
##    def _get(self):
##        u'The output length units used in driving directions.'
##        #return pVal
##    def _set(self, pVal):
##        u'The output length units used in driving directions.'
##    DirectionsLengthUnits = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Controls the backtrack policy of the route solver.'
##        #return pVal
##    def _set(self, pVal):
##        u'Controls the backtrack policy of the route solver.'
##    BacktrackPolicy = property(_get, _set, doc = _set.__doc__)
##
##    def SetRestriction(self, pRestriction):
##        u'Sets a restriction to be used by the route solver.'
##        #return 
##
##    def ClearAllRestrictions(self):
##        u'Removes all restrictions set on the route solver.'
##        #return 
##

ISMRouterSetup2._methods_ = [
    COMMETHOD([dispid(5), helpstring(u'Number of restrictions in the list, which will be applied when finding route.'), 'propget'], HRESULT, 'RestrictionCount',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(6), helpstring(u'Restriction at the position, specified by index.'), 'propget'], HRESULT, 'Restriction',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(ISMRestriction)), 'pVal' )),
    COMMETHOD([dispid(7), helpstring(u'The method removes restriction at specified position from the list.')], HRESULT, 'ClearRestriction',
              ( ['in'], c_int, 'index' )),
]
################################################################
## code template for ISMRouterSetup2 implementation
##class ISMRouterSetup2_Impl(object):
##    @property
##    def Restriction(self, index):
##        u'Restriction at the position, specified by index.'
##        #return pVal
##
##    def ClearRestriction(self, index):
##        u'The method removes restriction at specified position from the list.'
##        #return 
##
##    @property
##    def RestrictionCount(self):
##        u'Number of restrictions in the list, which will be applied when finding route.'
##        #return pVal
##

class IArcInfoWorkspace(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that create ArcInfo Coverages and Tables.'
    _iid_ = GUID('{730E2FF7-E3B4-11D2-9F30-00C04F79927C}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriCoveragePrecisionType'
esriCoveragePrecisionSingle = 1
esriCoveragePrecisionDouble = 2
esriCoveragePrecisionType = c_int # enum
IArcInfoWorkspace._methods_ = [
    COMMETHOD([helpstring(u'Creates a new Coverage.')], HRESULT, 'CreateCoverage',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], BSTR, 'templateCoverage' ),
              ( ['in'], esriCoveragePrecisionType, 'precision' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureDataset)), 'featureDataset' )),
    COMMETHOD([helpstring(u'Creates a new Info Table.')], HRESULT, 'CreateInfoTable',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], POINTER(IArcInfoItems), 'ItemSet' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable)), 'Table' )),
]
################################################################
## code template for IArcInfoWorkspace implementation
##class IArcInfoWorkspace_Impl(object):
##    def CreateInfoTable(self, Name, ItemSet):
##        u'Creates a new Info Table.'
##        #return Table
##
##    def CreateCoverage(self, Name, templateCoverage, precision):
##        u'Creates a new Coverage.'
##        #return featureDataset
##

class IDETextFileType(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the TextFile Data Element Type.'
    _iid_ = GUID('{72835EFA-D940-430F-87E3-6E9B3D121023}')
    _idlflags_ = ['oleautomation']
IDETextFileType._methods_ = [
]
################################################################
## code template for IDETextFileType implementation
##class IDETextFileType_Impl(object):

class DEMapDocument(CoClass):
    u'Map Document Data Element object.'
    _reg_clsid_ = GUID('{C0BED5D9-13E2-469B-A7D8-22704B0C8630}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
class IDEMapDocument(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the MapDocument Data Element.'
    _iid_ = GUID('{81DAEED8-EF11-40EB-A617-60E4D4654FD8}')
    _idlflags_ = ['oleautomation']
DEMapDocument._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDEMapDocument, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElement, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPValue, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDescribe]

class ISMRouter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Deprecated as of 10.1. Provides access to the main functionality for route finding.'
    _iid_ = GUID('{F8B66020-5850-11D7-B321-008048DB11DE}')
    _idlflags_ = ['dual', 'oleautomation']
class ISMNetBarriersCollection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Deprecated as of 10.1. Provides access to the collection of network barriers.'
    _iid_ = GUID('{F8B65FFF-5850-11D7-B321-008048DB11DE}')
    _idlflags_ = ['dual', 'oleautomation']
class ISMNetAttributesCollection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Deprecated as of 10.1. Provides access to the collection of network attributes.'
    _iid_ = GUID('{F8B65FF9-5850-11D7-B321-008048DB11DE}')
    _idlflags_ = ['dual', 'oleautomation']
class ISMRoadPreferences(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Deprecated as of 10.1. Provides access to preferences for different road types that the router supports.'
    _iid_ = GUID('{F8B66002-5850-11D7-B321-008048DB11DE}')
    _idlflags_ = ['dual', 'oleautomation']
class ISMSpeedGroups(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Deprecated as of 10.1. Provides access to the collection of speed groups.'
    _iid_ = GUID('{F8B66008-5850-11D7-B321-008048DB11DE}')
    _idlflags_ = ['dual', 'oleautomation']
class ISMTripPlanSettings(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Deprecated as of 10.1. Provides access to the trip planning settings.'
    _iid_ = GUID('{F8B6600B-5850-11D7-B321-008048DB11DE}')
    _idlflags_ = ['dual', 'oleautomation']
class ISMStopsCollection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Deprecated as of 10.1. Provides access to the collection of route stops.'
    _iid_ = GUID('{F8B66017-5850-11D7-B321-008048DB11DE}')
    _idlflags_ = ['dual', 'oleautomation']
class ISMBreakTracker(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Deprecated as of 10.1. Provides access to members that control the long operation cancellation.'
    _iid_ = GUID('{122FC3AE-A421-4922-9459-DFF9D3631333}')
    _idlflags_ = ['dual', 'oleautomation']
class ISMDirections(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Deprecated as of 10.1. Provides access to the driving directions information (path geometry and description of each path segment).'
    _iid_ = GUID('{F8B6601D-5850-11D7-B321-008048DB11DE}')
    _idlflags_ = ['dual', 'oleautomation']
class ISMNetAttributesAccess(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Deprecated as of 10.1. Provides access to the network attribute value.'
    _iid_ = GUID('{198DC955-519B-41EC-AF33-1090D356C674}')
    _idlflags_ = ['dual', 'oleautomation']
class ISMFlagCreator(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Deprecated as of 10.1. Provides access to members for creating SMFlag objects.'
    _iid_ = GUID('{8A4BB863-0C3F-4897-AA09-1479A4B76A6F}')
    _idlflags_ = ['dual', 'oleautomation']
ISMRouter._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'The network barriers collection of the router object.'), 'propget'], HRESULT, 'Barriers',
              ( ['retval', 'out'], POINTER(POINTER(ISMNetBarriersCollection)), 'pVal' )),
    COMMETHOD([dispid(2), helpstring(u'The network attributes collection of the router object.'), 'propget'], HRESULT, 'NetAttributes',
              ( ['retval', 'out'], POINTER(POINTER(ISMNetAttributesCollection)), 'pVal' )),
    COMMETHOD([dispid(3), helpstring(u'The road preferences used by the router object.'), 'propget'], HRESULT, 'Preferences',
              ( ['retval', 'out'], POINTER(POINTER(ISMRoadPreferences)), 'pVal' )),
    COMMETHOD([dispid(4), helpstring(u'The speed groups used by the router object.'), 'propget'], HRESULT, 'SpeedGroups',
              ( ['retval', 'out'], POINTER(POINTER(ISMSpeedGroups)), 'pVal' )),
    COMMETHOD([dispid(5), helpstring(u'The trip planning settings used by the router object.'), 'propget'], HRESULT, 'TripPlanSettings',
              ( ['retval', 'out'], POINTER(POINTER(ISMTripPlanSettings)), 'pVal' )),
    COMMETHOD([dispid(6), helpstring(u'The network attribute that the router object currently uses.'), 'propget'], HRESULT, 'NetAttributeName',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(6), helpstring(u'The network attribute that the router object currently uses.'), 'propput'], HRESULT, 'NetAttributeName',
              ( ['in'], BSTR, 'pVal' )),
    COMMETHOD([dispid(8), helpstring(u'Reorders the stops collection to minimize total driving time or distance.')], HRESULT, 'ReorderStops',
              ( ['in'], POINTER(ISMStopsCollection), 'pISrcStops' ),
              ( ['retval', 'out'], POINTER(POINTER(ISMStopsCollection)), 'pIResStops' )),
    COMMETHOD([dispid(9), helpstring(u'Calculates the route using the current settings of the router object.')], HRESULT, 'Solve',
              ( ['in'], POINTER(ISMStopsCollection), 'pIStops' ),
              ( ['in'], POINTER(ISMBreakTracker), 'pITracker' ),
              ( ['retval', 'out'], POINTER(POINTER(ISMDirections)), 'pIDirections' )),
    COMMETHOD([dispid(12), helpstring(u'The network attributes access of the router object.'), 'propget'], HRESULT, 'NetAttributesAccess',
              ( ['retval', 'out'], POINTER(POINTER(ISMNetAttributesAccess)), 'ppNetAttrAccess' )),
    COMMETHOD([dispid(13), helpstring(u'The spatial reference of the source data used by the router object.'), 'propget'], HRESULT, 'ProjectionString',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(14), helpstring(u'The flag creator used by the router object.'), 'propget'], HRESULT, 'FlagCreator',
              ( ['retval', 'out'], POINTER(POINTER(ISMFlagCreator)), 'pVal' )),
]
################################################################
## code template for ISMRouter implementation
##class ISMRouter_Impl(object):
##    @property
##    def Preferences(self):
##        u'The road preferences used by the router object.'
##        #return pVal
##
##    @property
##    def SpeedGroups(self):
##        u'The speed groups used by the router object.'
##        #return pVal
##
##    def _get(self):
##        u'The network attribute that the router object currently uses.'
##        #return pVal
##    def _set(self, pVal):
##        u'The network attribute that the router object currently uses.'
##    NetAttributeName = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def ProjectionString(self):
##        u'The spatial reference of the source data used by the router object.'
##        #return pVal
##
##    @property
##    def FlagCreator(self):
##        u'The flag creator used by the router object.'
##        #return pVal
##
##    @property
##    def TripPlanSettings(self):
##        u'The trip planning settings used by the router object.'
##        #return pVal
##
##    def Solve(self, pIStops, pITracker):
##        u'Calculates the route using the current settings of the router object.'
##        #return pIDirections
##
##    @property
##    def Barriers(self):
##        u'The network barriers collection of the router object.'
##        #return pVal
##
##    def ReorderStops(self, pISrcStops):
##        u'Reorders the stops collection to minimize total driving time or distance.'
##        #return pIResStops
##
##    @property
##    def NetAttributesAccess(self):
##        u'The network attributes access of the router object.'
##        #return ppNetAttrAccess
##
##    @property
##    def NetAttributes(self):
##        u'The network attributes collection of the router object.'
##        #return pVal
##

class IDEFolder(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the Folder Data Element.'
    _iid_ = GUID('{4368E06B-E887-43B6-AB24-1FF4FED5837B}')
    _idlflags_ = ['oleautomation']
IDEFolder._methods_ = [
]
################################################################
## code template for IDEFolder implementation
##class IDEFolder_Impl(object):

class IDECatalogRootType(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the CatalogRoot Data Element Type.'
    _iid_ = GUID('{4BA00494-AB4C-45B5-B7FF-7E3B9E595BF1}')
    _idlflags_ = ['oleautomation']
IDECatalogRootType._methods_ = [
]
################################################################
## code template for IDECatalogRootType implementation
##class IDECatalogRootType_Impl(object):

class ISMNetAttribute(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Deprecated as of 10.1. Provides access to the network attribute properties.'
    _iid_ = GUID('{F8B65FF6-5850-11D7-B321-008048DB11DE}')
    _idlflags_ = ['dual', 'oleautomation']

# values for enumeration 'esriSMNetAttributeType'
esriSMNetAttrInteger = 1
esriSMNetAttrFloat = 2
esriSMNetAttrDouble = 3
esriSMNetAttrBoolean = 4
esriSMNetAttrString = 5
esriSMNetAttrShape = 6
esriSMNetAttributeType = c_int # enum
ISMNetAttribute._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'The network attribute name.'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(2), helpstring(u'The network attribute type. Returns an esriSMNetAttributeType constant.'), 'propget'], HRESULT, 'Type',
              ( ['retval', 'out'], POINTER(esriSMNetAttributeType), 'pVal' )),
]
################################################################
## code template for ISMNetAttribute implementation
##class ISMNetAttribute_Impl(object):
##    @property
##    def Type(self):
##        u'The network attribute type. Returns an esriSMNetAttributeType constant.'
##        #return pVal
##
##    @property
##    def Name(self):
##        u'The network attribute name.'
##        #return pVal
##

class SMNetAttributesAccess(CoClass):
    u'Deprecated as of 10.1. The object to access the value of network attributes.'
    _reg_clsid_ = GUID('{2041D5A1-C9B6-4C74-8954-033AF25557B8}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
SMNetAttributesAccess._com_interfaces_ = [ISMNetAttributesAccess]


# values for enumeration 'esriCoverageFeatureClassType'
esriCFCTPoint = 1
esriCFCTArc = 2
esriCFCTPolygon = 3
esriCFCTNode = 4
esriCFCTTic = 5
esriCFCTAnnotation = 6
esriCFCTSection = 7
esriCFCTRoute = 8
esriCFCTLink = 9
esriCFCTRegion = 11
esriCFCTLabel = 51
esriCFCTFile = 666
esriCoverageFeatureClassType = c_int # enum
class IDEDiskConnectionType(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the Disk Connection Data Element Type.'
    _iid_ = GUID('{BD15433A-67D7-4FDB-B0CA-42EF470F704E}')
    _idlflags_ = ['oleautomation']
IDEDiskConnectionType._methods_ = [
]
################################################################
## code template for IDEDiskConnectionType implementation
##class IDEDiskConnectionType_Impl(object):

class IArcInfoItemsEdit(IArcInfoItems):
    _case_insensitive_ = True
    u'Provides access to members that create the ArcInfo Items Collection.'
    _iid_ = GUID('{B5E470D5-CEAB-11D2-B0DC-0000F8780820}')
    _idlflags_ = ['oleautomation']
IArcInfoItems._methods_ = [
    COMMETHOD(['propget', helpstring(u'Number of Items in the Items Collection.')], HRESULT, 'ItemCount',
              ( ['retval', 'out'], POINTER(c_int), 'numItems' )),
    COMMETHOD(['propget', helpstring(u'Item at the specified index in the Items Collection.')], HRESULT, 'Item',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IArcInfoItem)), 'Item' )),
    COMMETHOD([helpstring(u'Finds the index of the specified Item in the Items Collection.')], HRESULT, 'FindItem',
              ( ['in'], BSTR, 'Name' ),
              ( ['out'], POINTER(c_int), 'index' )),
]
################################################################
## code template for IArcInfoItems implementation
##class IArcInfoItems_Impl(object):
##    @property
##    def Item(self, index):
##        u'Item at the specified index in the Items Collection.'
##        #return Item
##
##    @property
##    def ItemCount(self):
##        u'Number of Items in the Items Collection.'
##        #return numItems
##
##    def FindItem(self, Name):
##        u'Finds the index of the specified Item in the Items Collection.'
##        #return index
##

IArcInfoItemsEdit._methods_ = [
    COMMETHOD(['propput', helpstring(u'Number of Items in this Item Collection.')], HRESULT, 'ItemCount',
              ( ['in'], c_int, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Item at the specified position.')], HRESULT, 'Item',
              ( ['in'], c_int, 'index' ),
              ( ['in'], POINTER(IArcInfoItem), 'rhs' )),
    COMMETHOD(['hidden', helpstring(u'Adds an Item to the Items Collection.')], HRESULT, 'AddItem',
              ( ['in'], POINTER(IArcInfoItem), 'Item' )),
    COMMETHOD(['hidden', helpstring(u'Deletes an Item from the Items Collection.')], HRESULT, 'DeleteItem',
              ( ['in'], POINTER(IArcInfoItem), 'Item' )),
    COMMETHOD(['hidden', helpstring(u'Deletes all the Items from the Items Collection.')], HRESULT, 'DeleteAllItems'),
]
################################################################
## code template for IArcInfoItemsEdit implementation
##class IArcInfoItemsEdit_Impl(object):
##    def DeleteAllItems(self):
##        u'Deletes all the Items from the Items Collection.'
##        #return 
##
##    def _set(self, index, rhs):
##        u'Item at the specified position.'
##    Item = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Number of Items in this Item Collection.'
##    ItemCount = property(fset = _set, doc = _set.__doc__)
##
##    def DeleteItem(self, Item):
##        u'Deletes an Item from the Items Collection.'
##        #return 
##
##    def AddItem(self, Item):
##        u'Adds an Item to the Items Collection.'
##        #return 
##

class ICadTransformations(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control Cad Transformations.'
    _iid_ = GUID('{E37F71AB-BFB1-11D2-9B20-00C04FA33299}')
    _idlflags_ = ['oleautomation']
ICadTransformations._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if global transformations are enabled.')], HRESULT, 'EnableTransformations',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'enabled' )),
    COMMETHOD(['propput', helpstring(u'Indicates if global transformations are enabled.')], HRESULT, 'EnableTransformations',
              ( ['in'], VARIANT_BOOL, 'enabled' )),
    COMMETHOD(['propget', helpstring(u'The pathname of the world file.')], HRESULT, 'WorldFileName',
              ( ['retval', 'out'], POINTER(BSTR), 'FilePath' )),
    COMMETHOD(['propput', helpstring(u'The pathname of the world file.')], HRESULT, 'WorldFileName',
              ( ['in'], BSTR, 'FilePath' )),
    COMMETHOD(['propget', helpstring(u'The transformation type.')], HRESULT, 'TransformMode',
              ( ['retval', 'out'], POINTER(esriCadTransform), 'mode' )),
    COMMETHOD(['propput', helpstring(u'The transformation type.')], HRESULT, 'TransformMode',
              ( ['in'], esriCadTransform, 'mode' )),
    COMMETHOD([helpstring(u'Returns the points of a two point transformation.')], HRESULT, 'GetFromToTransform',
              ( ['out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.WKSPoint), 'fromPoint1' ),
              ( ['out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.WKSPoint), 'fromPoint2' ),
              ( ['out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.WKSPoint), 'toPoint1' ),
              ( ['out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.WKSPoint), 'toPoint2' )),
    COMMETHOD([helpstring(u'Sets the points of a two point transformation.')], HRESULT, 'SetFromToTransform',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.WKSPoint), 'fromPoint1' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.WKSPoint), 'fromPoint2' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.WKSPoint), 'toPoint1' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.WKSPoint), 'toPoint2' )),
    COMMETHOD([helpstring(u'Returns the rotation, scale, and translation of a transformation.')], HRESULT, 'GetTransformation',
              ( ['out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.WKSPoint), 'from' ),
              ( ['out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.WKSPoint), 'to' ),
              ( ['out'], POINTER(c_double), 'angle' ),
              ( ['out'], POINTER(c_double), 'scale' )),
    COMMETHOD([helpstring(u'Sets the rotation, scale, and translation of a transformation.')], HRESULT, 'SetTransformation',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.WKSPoint), 'from' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.WKSPoint), 'to' ),
              ( ['in'], c_double, 'angle' ),
              ( ['in'], c_double, 'scale' )),
]
################################################################
## code template for ICadTransformations implementation
##class ICadTransformations_Impl(object):
##    def SetTransformation(self, from, to, angle, scale):
##        u'Sets the rotation, scale, and translation of a transformation.'
##        #return 
##
##    def GetTransformation(self):
##        u'Returns the rotation, scale, and translation of a transformation.'
##        #return from, to, angle, scale
##
##    def _get(self):
##        u'The transformation type.'
##        #return mode
##    def _set(self, mode):
##        u'The transformation type.'
##    TransformMode = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The pathname of the world file.'
##        #return FilePath
##    def _set(self, FilePath):
##        u'The pathname of the world file.'
##    WorldFileName = property(_get, _set, doc = _set.__doc__)
##
##    def GetFromToTransform(self):
##        u'Returns the points of a two point transformation.'
##        #return fromPoint1, fromPoint2, toPoint1, toPoint2
##
##    def SetFromToTransform(self, fromPoint1, fromPoint2, toPoint1, toPoint2):
##        u'Sets the points of a two point transformation.'
##        #return 
##
##    def _get(self):
##        u'Indicates if global transformations are enabled.'
##        #return enabled
##    def _set(self, enabled):
##        u'Indicates if global transformations are enabled.'
##    EnableTransformations = property(_get, _set, doc = _set.__doc__)
##

IDECoverageType._methods_ = [
]
################################################################
## code template for IDECoverageType implementation
##class IDECoverageType_Impl(object):

class SMRouterEnvelope(CoClass):
    u'Deprecated as of 10.1. The bounding envelope of the route path.'
    _reg_clsid_ = GUID('{F8B65FF1-5850-11D7-B321-008048DB11DE}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
class ISMRouterEnvelope(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Deprecated as of 10.1. Provides access to the bounding envelope of the route path.'
    _iid_ = GUID('{F8B65FF0-5850-11D7-B321-008048DB11DE}')
    _idlflags_ = ['dual', 'oleautomation']
SMRouterEnvelope._com_interfaces_ = [ISMRouterEnvelope]

class SMPointsCollection(CoClass):
    u'Deprecated as of 10.1. The collection of geographic points.'
    _reg_clsid_ = GUID('{F8B65FF4-5850-11D7-B321-008048DB11DE}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
class ISMPointsCollection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Deprecated as of 10.1. Provides access to the collection of geographic points.'
    _iid_ = GUID('{F8B65FF3-5850-11D7-B321-008048DB11DE}')
    _idlflags_ = ['dual', 'oleautomation']
SMPointsCollection._com_interfaces_ = [ISMPointsCollection]

class Library(object):
    u'Esri DataSourcesFile Object Library 10.2'
    name = u'esriDataSourcesFile'
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)

ISMBreakTracker._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Called frequently while associated operation is progressing. A return value of false indicates that the operation should stop.')], HRESULT, 'Continue',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bKeepGoing' )),
]
################################################################
## code template for ISMBreakTracker implementation
##class ISMBreakTracker_Impl(object):
##    def Continue(self):
##        u'Called frequently while associated operation is progressing. A return value of false indicates that the operation should stop.'
##        #return bKeepGoing
##

class ICoverageFeatureClassName(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that maintains ArcInfo Coverage Feature Class information.'
    _iid_ = GUID('{DE61A107-0E08-11D3-9F31-00C04F79927C}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriFeatureClassTopology'
esriFCTNotApplicable = 0
esriFCTPreliminary = 1
esriFCTExists = 2
esriFCTUnknown = 3
esriFeatureClassTopology = c_int # enum
ICoverageFeatureClassName._methods_ = [
    COMMETHOD(['propget', helpstring(u'Type of the Feature Class.')], HRESULT, 'FeatureClassType',
              ( ['retval', 'out'], POINTER(esriCoverageFeatureClassType), 'FeatureClassType' )),
    COMMETHOD(['propput', helpstring(u'Type of the Feature Class.')], HRESULT, 'FeatureClassType',
              ( ['in'], esriCoverageFeatureClassType, 'FeatureClassType' )),
    COMMETHOD(['propget', helpstring(u'Topology of the Feature Class.')], HRESULT, 'Topology',
              ( ['retval', 'out'], POINTER(esriFeatureClassTopology), 'Topology' )),
    COMMETHOD(['propput', helpstring(u'Topology of the Feature Class.')], HRESULT, 'Topology',
              ( ['in'], esriFeatureClassTopology, 'Topology' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the Feature Class has a Feature Attribute Table.')], HRESULT, 'HasFAT',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'HasFAT' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the Feature Class has a Feature Attribute Table.')], HRESULT, 'HasFAT',
              ( ['in'], VARIANT_BOOL, 'HasFAT' )),
]
################################################################
## code template for ICoverageFeatureClassName implementation
##class ICoverageFeatureClassName_Impl(object):
##    def _get(self):
##        u'Type of the Feature Class.'
##        #return FeatureClassType
##    def _set(self, FeatureClassType):
##        u'Type of the Feature Class.'
##    FeatureClassType = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the Feature Class has a Feature Attribute Table.'
##        #return HasFAT
##    def _set(self, HasFAT):
##        u'Indicates if the Feature Class has a Feature Attribute Table.'
##    HasFAT = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Topology of the Feature Class.'
##        #return Topology
##    def _set(self, Topology):
##        u'Topology of the Feature Class.'
##    Topology = property(_get, _set, doc = _set.__doc__)
##

class SMNetBarrier(CoClass):
    u'Deprecated as of 10.1. The network barrier object.'
    _reg_clsid_ = GUID('{F8B65FFD-5850-11D7-B321-008048DB11DE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
class ISMNetBarrier(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Deprecated as of 10.1. Provides access to the network barrier properties.'
    _iid_ = GUID('{F8B65FFC-5850-11D7-B321-008048DB11DE}')
    _idlflags_ = ['dual', 'oleautomation']
SMNetBarrier._com_interfaces_ = [ISMNetBarrier]

IDEArcInfoTableType._methods_ = [
]
################################################################
## code template for IDEArcInfoTableType implementation
##class IDEArcInfoTableType_Impl(object):

ISMNetBarrier._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'The network barrier ID.'), 'propget'], HRESULT, 'BarrierID',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(1), helpstring(u'The network barrier ID.'), 'propput'], HRESULT, 'BarrierID',
              ( ['in'], c_int, 'pVal' )),
    COMMETHOD([dispid(2), helpstring(u'Geographic location of the barrier.'), 'propget'], HRESULT, 'Point',
              ( ['retval', 'out'], POINTER(POINTER(ISMRouterPoint)), 'pVal' )),
    COMMETHOD([dispid(2), helpstring(u'Geographic location of the barrier.'), 'propput'], HRESULT, 'Point',
              ( ['in'], POINTER(ISMRouterPoint), 'pVal' )),
]
################################################################
## code template for ISMNetBarrier implementation
##class ISMNetBarrier_Impl(object):
##    def _get(self):
##        u'The network barrier ID.'
##        #return pVal
##    def _set(self, pVal):
##        u'The network barrier ID.'
##    BarrierID = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Geographic location of the barrier.'
##        #return pVal
##    def _set(self, pVal):
##        u'Geographic location of the barrier.'
##    Point = property(_get, _set, doc = _set.__doc__)
##

class ISMFlag(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u"Deprecated as of 10.1. Provides access to the information about a stop's geographic location."
    _iid_ = GUID('{F8B66011-5850-11D7-B321-008048DB11DE}')
    _idlflags_ = ['dual', 'oleautomation']
ISMFlagCreator._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Creates the route flag using its geographic location.')], HRESULT, 'CreateFlag',
              ( ['in'], POINTER(ISMRouterPoint), 'pPoint' ),
              ( ['retval', 'out'], POINTER(POINTER(ISMFlag)), 'pIFlag' )),
    COMMETHOD([dispid(2), helpstring(u'Creates the route flag using its geographic location and required direction.')], HRESULT, 'CreateFlagDirection',
              ( ['in'], POINTER(ISMRouterPoint), 'pPoint' ),
              ( ['in'], c_double, 'dOrientation' ),
              ( ['in'], c_double, 'dTolerance' ),
              ( ['out'], POINTER(c_double), 'pdAdjustedOrientation' ),
              ( ['retval', 'out'], POINTER(POINTER(ISMFlag)), 'ppFlag' )),
    COMMETHOD([dispid(3), helpstring(u'Creates the route flag using its geographic location, required direction and latency.')], HRESULT, 'CreateFlagDirectionAdv',
              ( ['in'], POINTER(ISMRouterPoint), 'pPoint' ),
              ( ['in'], c_double, 'dOrientation' ),
              ( ['in'], c_double, 'dTolerance' ),
              ( ['in'], c_double, 'dSpeed' ),
              ( ['in'], c_double, 'dLatency' ),
              ( ['out'], POINTER(c_double), 'pdAdjustedOrientation' ),
              ( ['retval', 'out'], POINTER(POINTER(ISMFlag)), 'ppFlag' )),
]
################################################################
## code template for ISMFlagCreator implementation
##class ISMFlagCreator_Impl(object):
##    def CreateFlag(self, pPoint):
##        u'Creates the route flag using its geographic location.'
##        #return pIFlag
##
##    def CreateFlagDirection(self, pPoint, dOrientation, dTolerance):
##        u'Creates the route flag using its geographic location and required direction.'
##        #return pdAdjustedOrientation, ppFlag
##
##    def CreateFlagDirectionAdv(self, pPoint, dOrientation, dTolerance, dSpeed, dLatency):
##        u'Creates the route flag using its geographic location, required direction and latency.'
##        #return pdAdjustedOrientation, ppFlag
##

class SMNetBarriersCollection(CoClass):
    u'Deprecated as of 10.1. The collection of network barriers.'
    _reg_clsid_ = GUID('{F8B66000-5850-11D7-B321-008048DB11DE}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
SMNetBarriersCollection._com_interfaces_ = [ISMNetBarriersCollection]

class IDEDiskConnection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the Disk Connection Data Element.'
    _iid_ = GUID('{AE51F9D8-5864-4CF2-8186-736AF8C4022C}')
    _idlflags_ = ['oleautomation']
IDEDiskConnection._methods_ = [
]
################################################################
## code template for IDEDiskConnection implementation
##class IDEDiskConnection_Impl(object):

class SMTripPlanSettings(CoClass):
    u'Deprecated as of 10.1. The object that controls trip plan settings.'
    _reg_clsid_ = GUID('{F8B6600C-5850-11D7-B321-008048DB11DE}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
SMTripPlanSettings._com_interfaces_ = [ISMTripPlanSettings]

class IDELayer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the Layer Data Element.'
    _iid_ = GUID('{991993E4-7DFD-4E23-BCA0-689B174E3030}')
    _idlflags_ = ['oleautomation']
IDELayer._methods_ = [
    COMMETHOD(['propget', helpstring(u'The data element layer.')], HRESULT, 'GPLayer',
              ( ['retval', 'out'], POINTER(POINTER(IGPLayer)), 'ppLayer' )),
    COMMETHOD(['propputref', helpstring(u'The data element layer.')], HRESULT, 'GPLayer',
              ( ['in'], POINTER(IGPLayer), 'ppLayer' )),
]
################################################################
## code template for IDELayer implementation
##class IDELayer_Impl(object):
##    def GPLayer(self, ppLayer):
##        u'The data element layer.'
##        #return 
##

IDEFolderType._methods_ = [
]
################################################################
## code template for IDEFolderType implementation
##class IDEFolderType_Impl(object):

class SMRoadPreferences(CoClass):
    u'Deprecated as of 10.1. The object for retrieving and modifying road preferences.'
    _reg_clsid_ = GUID('{F8B66003-5850-11D7-B321-008048DB11DE}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
SMRoadPreferences._com_interfaces_ = [ISMRoadPreferences]

ISMNetAttributesAccess._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the network attribute value by object ID.')], HRESULT, 'GetNetAttributeValue',
              ( ['in'], BSTR, 'bstrAttrName' ),
              ( ['in'], c_int, 'lObjectID' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'pvtVal' )),
]
################################################################
## code template for ISMNetAttributesAccess implementation
##class ISMNetAttributesAccess_Impl(object):
##    def GetNetAttributeValue(self, bstrAttrName, lObjectID):
##        u'Returns the network attribute value by object ID.'
##        #return pvtVal
##

class SMSpeedGroup(CoClass):
    u'Deprecated as of 10.1. Information about the speed group.'
    _reg_clsid_ = GUID('{F8B66006-5850-11D7-B321-008048DB11DE}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
class ISMSpeedGroup(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Deprecated as of 10.1. Provides access to the speed group properties.'
    _iid_ = GUID('{F8B66005-5850-11D7-B321-008048DB11DE}')
    _idlflags_ = ['dual', 'oleautomation']
class ISMSpeedGroup2(ISMSpeedGroup):
    _case_insensitive_ = True
    u'Deprecated as of 10.1. Provides access to speed group query string.'
    _iid_ = GUID('{1E436C24-CF57-4ACA-BBD3-FFDDB1151FA7}')
    _idlflags_ = ['dual', 'oleautomation']
SMSpeedGroup._com_interfaces_ = [ISMSpeedGroup, ISMSpeedGroup2]

class DERemoteDatabaseFolder(CoClass):
    u'Remote Database Folder Data Element object.'
    _reg_clsid_ = GUID('{DB3E6FDF-D5F8-4C94-B743-47AB4DE79A05}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
class IDERemoteDatabaseFolder(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the Remote Database Folder Data Element.'
    _iid_ = GUID('{3DD1A87B-30B2-4A02-ABD2-205C5363AE4B}')
    _idlflags_ = ['oleautomation']
DERemoteDatabaseFolder._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDERemoteDatabaseFolder, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElement, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPValue, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDescribe]

IDEPrjFileType._methods_ = [
]
################################################################
## code template for IDEPrjFileType implementation
##class IDEPrjFileType_Impl(object):

class SMStopsCollection(CoClass):
    u'Deprecated as of 10.1. The collection of route stops.'
    _reg_clsid_ = GUID('{F8B66018-5850-11D7-B321-008048DB11DE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
SMStopsCollection._com_interfaces_ = [ISMStopsCollection]

class IArcInfoTable2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that modify ArcInfo Tables.'
    _iid_ = GUID('{99D56004-BB97-4606-A141-6BB061F87940}')
    _idlflags_ = ['oleautomation']
IArcInfoTable2._methods_ = [
    COMMETHOD([helpstring(u'Assigns external name to an ArcInfo table.')], HRESULT, 'External',
              ( ['in'], BSTR, 'externalname' )),
]
################################################################
## code template for IArcInfoTable2 implementation
##class IArcInfoTable2_Impl(object):
##    def External(self, externalname):
##        u'Assigns external name to an ArcInfo table.'
##        #return 
##


# values for enumeration 'esriCoverageToleranceType'
esriCTTFuzzy = 1
esriCTTGeneralize = 2
esriCTTNodeMatch = 3
esriCTTDangle = 4
esriCTTTicMatch = 5
esriCTTEdit = 6
esriCTTNodeSnap = 7
esriCTTWeed = 8
esriCTTGrain = 9
esriCTTSnap = 10
esriCoverageToleranceType = c_int # enum
ISMSpeedGroups._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'The number of speed groups in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(2), helpstring(u'The speed group at the specified position in the collection.'), 'propget'], HRESULT, 'Item',
              ( ['in'], c_int, 'Position' ),
              ( ['retval', 'out'], POINTER(POINTER(ISMSpeedGroup)), 'pVal' )),
]
################################################################
## code template for ISMSpeedGroups implementation
##class ISMSpeedGroups_Impl(object):
##    @property
##    def Count(self):
##        u'The number of speed groups in the collection.'
##        #return pVal
##
##    @property
##    def Item(self, Position):
##        u'The speed group at the specified position in the collection.'
##        #return pVal
##

class IDEMapDocumentType(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the MapDocument Data Element Type.'
    _iid_ = GUID('{5826A85F-D7CD-4B32-A2D9-0ECCFDE297A2}')
    _idlflags_ = ['oleautomation']
IDEMapDocumentType._methods_ = [
]
################################################################
## code template for IDEMapDocumentType implementation
##class IDEMapDocumentType_Impl(object):

class IDEArcInfoTable(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the ArcInfo Table Data Element.'
    _iid_ = GUID('{DC3B7FDB-CE0F-4AEE-945C-0755F89109E4}')
    _idlflags_ = ['oleautomation']
IDEArcInfoTable._methods_ = [
    COMMETHOD(['propget', helpstring(u'The list of items.')], HRESULT, 'ItemSet',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IArray)), 'ppItems' )),
    COMMETHOD(['propputref', helpstring(u'The list of items.')], HRESULT, 'ItemSet',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IArray), 'ppItems' )),
]
################################################################
## code template for IDEArcInfoTable implementation
##class IDEArcInfoTable_Impl(object):
##    def ItemSet(self, ppItems):
##        u'The list of items.'
##        #return 
##

class SMFlag(CoClass):
    u'Deprecated as of 10.1. The object that represents flag properties.'
    _reg_clsid_ = GUID('{F8B66012-5850-11D7-B321-008048DB11DE}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
SMFlag._com_interfaces_ = [ISMFlag]

class ArcInfoWorkspaceFactory(CoClass):
    u'Workspace factory used to create workspace objects for ArcInfo coverages and Info tables.'
    _reg_clsid_ = GUID('{1D887452-D9F2-11D1-AA81-00C04FA33A15}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
ArcInfoWorkspaceFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceFactory, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceFactory2, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IParseNameString]

class SMStop(CoClass):
    u'Deprecated as of 10.1. The information about route stop.'
    _reg_clsid_ = GUID('{F8B66015-5850-11D7-B321-008048DB11DE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
class ISMStop(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Deprecated as of 10.1. Provides access to the route stop properties.'
    _iid_ = GUID('{F8B66014-5850-11D7-B321-008048DB11DE}')
    _idlflags_ = ['dual', 'oleautomation']
SMStop._com_interfaces_ = [ISMStop]

IDECadDrawingDatasetType._methods_ = [
]
################################################################
## code template for IDECadDrawingDatasetType implementation
##class IDECadDrawingDatasetType_Impl(object):

class IArcInfoWorkspaceUtil(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that retreives ArcInfo Info Table information.'
    _iid_ = GUID('{A476810A-0C8D-469A-8332-7B3C1CFB8923}')
    _idlflags_ = ['oleautomation']
IArcInfoWorkspaceUtil._methods_ = [
    COMMETHOD([helpstring(u'Maps a prefix to a table name.')], HRESULT, 'GetInfoTableName',
              ( ['in'], BSTR, 'prefix' ),
              ( ['retval', 'out'], POINTER(BSTR), 'pTableName' )),
]
################################################################
## code template for IArcInfoWorkspaceUtil implementation
##class IArcInfoWorkspaceUtil_Impl(object):
##    def GetInfoTableName(self, prefix):
##        u'Maps a prefix to a table name.'
##        #return pTableName
##

class SdcExporter(CoClass):
    u'Helper object for exporting data to SDC.'
    _reg_clsid_ = GUID('{3C8B1A03-64B8-4E29-86AD-D4C4CB371EC1}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
class ISdcExporter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Provides access to members for compressing data to SDC.'
    _iid_ = GUID('{989B9737-FECF-467D-8544-D3B3EE30E60C}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation']
SdcExporter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ISdcExporter, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

class IDESpatialReferencesFolderType(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the Spatial References Folder Data Element Type.'
    _iid_ = GUID('{E2B9400D-655C-4976-B3DD-04F31C48BB81}')
    _idlflags_ = ['oleautomation']
IDESpatialReferencesFolderType._methods_ = [
]
################################################################
## code template for IDESpatialReferencesFolderType implementation
##class IDESpatialReferencesFolderType_Impl(object):

class ArcInfoItems(CoClass):
    u'Collection used for creating ArcInfo Items.'
    _reg_clsid_ = GUID('{5BB90FA2-D013-11D2-B0DC-0000F8780820}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
ArcInfoItems._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IArcInfoItems, IArcInfoItemsEdit, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

class ArcInfoItem(CoClass):
    u'ArcInfo Item Object used to create items.'
    _reg_clsid_ = GUID('{5BB90FA1-D013-11D2-B0DC-0000F8780820}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
ArcInfoItem._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IArcInfoItem, IArcInfoItemEdit, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

class SMDirItem(CoClass):
    u'Deprecated as of 10.1. A description and geography of one item of driving directions.'
    _reg_clsid_ = GUID('{F8B6601B-5850-11D7-B321-008048DB11DE}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
class ISMDirItem(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Deprecated as of 10.1. Provides access to the description and geography of one item of driving directions.'
    _iid_ = GUID('{F8B6601A-5850-11D7-B321-008048DB11DE}')
    _idlflags_ = ['dual', 'oleautomation']
SMDirItem._com_interfaces_ = [ISMDirItem]

class ICoverageFeatureClass(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that retrieve ArcInfo Coverage Feature Class information.'
    _iid_ = GUID('{4E471BB1-06FA-11D3-9F31-00C04F79927C}')
    _idlflags_ = ['oleautomation']
ICoverageFeatureClass._methods_ = [
    COMMETHOD(['propget', helpstring(u'Type of the Feature Class.')], HRESULT, 'FeatureClassType',
              ( ['retval', 'out'], POINTER(esriCoverageFeatureClassType), 'FeatureClassType' )),
    COMMETHOD(['propget', helpstring(u'Topology of the Feature Class.')], HRESULT, 'Topology',
              ( ['retval', 'out'], POINTER(esriFeatureClassTopology), 'Topology' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the Feature Class has a Feature Attribute Table.')], HRESULT, 'HasFAT',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'HasFAT' )),
]
################################################################
## code template for ICoverageFeatureClass implementation
##class ICoverageFeatureClass_Impl(object):
##    @property
##    def FeatureClassType(self):
##        u'Type of the Feature Class.'
##        #return FeatureClassType
##
##    @property
##    def HasFAT(self):
##        u'Indicates if the Feature Class has a Feature Attribute Table.'
##        #return HasFAT
##
##    @property
##    def Topology(self):
##        u'Topology of the Feature Class.'
##        #return Topology
##

class SMDirections(CoClass):
    u'Deprecated as of 10.1. Driving directions information including path geometry and description of each path segment.'
    _reg_clsid_ = GUID('{F8B6601E-5850-11D7-B321-008048DB11DE}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
SMDirections._com_interfaces_ = [ISMDirections]

class DECatalogRootType(CoClass):
    u'CatalogRootType Data Element object Type.'
    _reg_clsid_ = GUID('{07359AEA-34BA-4B5A-AB2C-0B43C7E8E9FB}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
DECatalogRootType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDECatalogRootType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElementType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDataType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGxFilterInfo, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone]

class SMRouter(CoClass):
    u'Deprecated as of 10.1. The object for calculating routes and defining route settings.'
    _reg_clsid_ = GUID('{F8B66021-5850-11D7-B321-008048DB11DE}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
class ISMRoutingMetaData(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Deprecated as of 10.1. Provides access to the meta data of the routing service.'
    _iid_ = GUID('{C8128B1A-23C3-4E21-93EB-50739B68F17A}')
    _idlflags_ = ['dual', 'oleautomation']
SMRouter._com_interfaces_ = [ISMRouter, ISMRoutingMetaData, ISMRouterSetup, ISMRouterSetup2]

class IDETextFile(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the TextFile Data Element.'
    _iid_ = GUID('{5348D943-C798-434A-9E72-AC97CA802A71}')
    _idlflags_ = ['oleautomation']
IDETextFile._methods_ = [
]
################################################################
## code template for IDETextFile implementation
##class IDETextFile_Impl(object):

class SMRouterFactory(CoClass):
    u'Deprecated as of 10.1. The object for creating router objects.'
    _reg_clsid_ = GUID('{F8B66024-5850-11D7-B321-008048DB11DE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
class ISMRouterFactory(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Deprecated as of 10.1. Provides access to members for creating SMRouter objects.'
    _iid_ = GUID('{F8B66023-5850-11D7-B321-008048DB11DE}')
    _idlflags_ = ['dual', 'oleautomation']
SMRouterFactory._com_interfaces_ = [ISMRouterFactory]

class DESpatialReferencesFolderType(CoClass):
    u'Spatial References Folder Data Element object Type.'
    _reg_clsid_ = GUID('{9FD4B414-498A-48B8-BF2F-82302524D513}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
DESpatialReferencesFolderType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDESpatialReferencesFolderType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElementType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDataType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGxFilterInfo, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone]

ISMRestriction._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'The network attribute used as a restriction.'), 'propget'], HRESULT, 'Attribute',
              ( ['retval', 'out'], POINTER(POINTER(ISMNetAttribute)), 'pAttr' )),
    COMMETHOD([dispid(1), helpstring(u'The network attribute used as a restriction.'), 'propputref'], HRESULT, 'Attribute',
              ( ['in'], POINTER(ISMNetAttribute), 'pAttr' )),
    COMMETHOD([dispid(2), helpstring(u'Restriction type.'), 'propget'], HRESULT, 'Type',
              ( ['retval', 'out'], POINTER(esriSMRestrictionType), 'pVal' )),
    COMMETHOD([dispid(2), helpstring(u'Restriction type.'), 'propput'], HRESULT, 'Type',
              ( ['in'], esriSMRestrictionType, 'pVal' )),
    COMMETHOD([dispid(3), helpstring(u'The restriction parameter value.'), 'propget'], HRESULT, 'Param',
              ( ['retval', 'out'], POINTER(VARIANT), 'pvParam' )),
    COMMETHOD([dispid(3), helpstring(u'The restriction parameter value.'), 'propput'], HRESULT, 'Param',
              ( ['in'], VARIANT, 'pvParam' )),
]
################################################################
## code template for ISMRestriction implementation
##class ISMRestriction_Impl(object):
##    def Attribute(self, pAttr):
##        u'The network attribute used as a restriction.'
##        #return 
##
##    def _get(self):
##        u'Restriction type.'
##        #return pVal
##    def _set(self, pVal):
##        u'Restriction type.'
##    Type = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The restriction parameter value.'
##        #return pvParam
##    def _set(self, pvParam):
##        u'The restriction parameter value.'
##    Param = property(_get, _set, doc = _set.__doc__)
##

ISdcExporter._methods_ = [
    COMMETHOD([dispid(1610743808), helpstring(u'Creates a SDC dataset from the input cursor.')], HRESULT, 'Export',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ICursor), 'cursor' ),
              ( ['in'], BSTR, 'outputRootname' ),
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'Key' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'trackCancel' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataset)), 'sdcDataset' )),
]
################################################################
## code template for ISdcExporter implementation
##class ISdcExporter_Impl(object):
##    def Export(self, cursor, outputRootname, Key, trackCancel):
##        u'Creates a SDC dataset from the input cursor.'
##        #return sdcDataset
##

class SMFlagCreator(CoClass):
    u'Deprecated as of 10.1. The object for route flag creation.'
    _reg_clsid_ = GUID('{38A979E8-086F-4CA8-AC30-890F22E65EBC}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
class ISMFlagCreator2(ISMFlagCreator):
    _case_insensitive_ = True
    u'Deprecated as of 10.1. Provides access to SMFlag search tolerance.'
    _iid_ = GUID('{0E8F6257-745F-4DE3-B651-6ECF14728C5C}')
    _idlflags_ = ['dual', 'oleautomation']
SMFlagCreator._com_interfaces_ = [ISMFlagCreator, ISMFlagCreator2]

class IGPArcInfoItemType(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Indicator interface for the ArcInfoItem Data Element Type.'
    _iid_ = GUID('{82C365F0-7956-47EC-86F3-B8D628837712}')
    _idlflags_ = ['oleautomation']
IGPArcInfoItemType._methods_ = [
]
################################################################
## code template for IGPArcInfoItemType implementation
##class IGPArcInfoItemType_Impl(object):

class SMRestriction(CoClass):
    u'Deprecated as of 10.1. The object for defining route restrictions.'
    _reg_clsid_ = GUID('{71A8E2B4-5A6C-4BDD-B005-A0FB02414197}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
SMRestriction._com_interfaces_ = [ISMRestriction]

class ICoverage(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that modifies ArcInfo Coverages.'
    _iid_ = GUID('{D42131E1-D187-11D2-B0DC-0000F8780820}')
    _idlflags_ = ['oleautomation']
ICoverage._methods_ = [
    COMMETHOD(['propget', helpstring(u'Value of the specified Tolerance.')], HRESULT, 'Tolerance',
              ( ['in'], esriCoverageToleranceType, 'toleranceType' ),
              ( ['retval', 'out'], POINTER(c_double), 'toleranceValue' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the specified Tolerance has been verified.')], HRESULT, 'ToleranceStatus',
              ( ['in'], esriCoverageToleranceType, 'toleranceType' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'isVerified' )),
    COMMETHOD(['propput', helpstring(u'Value of the specified Tolerance.')], HRESULT, 'Tolerance',
              ( ['in'], esriCoverageToleranceType, 'toleranceType' ),
              ( ['in'], c_double, 'toleranceValue' )),
    COMMETHOD([helpstring(u'Performs a BUILD operation.')], HRESULT, 'Build',
              ( ['in'], esriCoverageFeatureClassType, 'FeatureClassType' ),
              ( ['in', 'optional'], BSTR, 'subclassName' )),
    COMMETHOD([helpstring(u'Performs a CLEAN operation.')], HRESULT, 'Clean',
              ( ['in'], c_double, 'dangleTolerance' ),
              ( ['in'], c_double, 'fuzzyTolerance' ),
              ( ['in'], esriCoverageFeatureClassType, 'FeatureClassType' )),
    COMMETHOD([helpstring(u'Creates an empty Feature Class in the Coverage.')], HRESULT, 'CreateFeatureClass',
              ( ['in'], esriCoverageFeatureClassType, 'FeatureClassType' ),
              ( ['in', 'optional'], BSTR, 'subclassName' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass)), 'featureClass' )),
]
################################################################
## code template for ICoverage implementation
##class ICoverage_Impl(object):
##    def CreateFeatureClass(self, FeatureClassType, subclassName):
##        u'Creates an empty Feature Class in the Coverage.'
##        #return featureClass
##
##    @property
##    def ToleranceStatus(self, toleranceType):
##        u'Indicates if the specified Tolerance has been verified.'
##        #return isVerified
##
##    def _get(self, toleranceType):
##        u'Value of the specified Tolerance.'
##        #return toleranceValue
##    def _set(self, toleranceType, toleranceValue):
##        u'Value of the specified Tolerance.'
##    Tolerance = property(_get, _set, doc = _set.__doc__)
##
##    def Build(self, FeatureClassType, subclassName):
##        u'Performs a BUILD operation.'
##        #return 
##
##    def Clean(self, dangleTolerance, fuzzyTolerance, FeatureClassType):
##        u'Performs a CLEAN operation.'
##        #return 
##

class IDEShapeFile(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the ShapeFile Data Element.'
    _iid_ = GUID('{4E458CD7-D677-4E02-A827-2C5F1874FF88}')
    _idlflags_ = ['oleautomation']
IDEShapeFile._methods_ = [
]
################################################################
## code template for IDEShapeFile implementation
##class IDEShapeFile_Impl(object):

class CadWorkspaceFactory(CoClass):
    u'Esri Cad Workspace Factory.'
    _reg_clsid_ = GUID('{9E2C27CE-62C6-11D2-9AED-00C04FA33299}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
CadWorkspaceFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceFactory, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceFactory2, ICadSettings]

ISMFlagCreator2._methods_ = [
    COMMETHOD([dispid(4), helpstring(u'Defines maximum allowed distance in miles from stop location to closest street segment when creating a flag.'), 'propget'], HRESULT, 'SearchTolerance',
              ( ['retval', 'out'], POINTER(c_double), 'pVal' )),
    COMMETHOD([dispid(4), helpstring(u'Defines maximum allowed distance in miles from stop location to closest street segment when creating a flag.'), 'propput'], HRESULT, 'SearchTolerance',
              ( ['in'], c_double, 'pVal' )),
]
################################################################
## code template for ISMFlagCreator2 implementation
##class ISMFlagCreator2_Impl(object):
##    def _get(self):
##        u'Defines maximum allowed distance in miles from stop location to closest street segment when creating a flag.'
##        #return pVal
##    def _set(self, pVal):
##        u'Defines maximum allowed distance in miles from stop location to closest street segment when creating a flag.'
##    SearchTolerance = property(_get, _set, doc = _set.__doc__)
##

class DELayerType(CoClass):
    u'Layer Data Element object Type.'
    _reg_clsid_ = GUID('{775700AF-8577-442D-ADC9-74D7A9AA3C41}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
class IDELayerType(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the Layer Data Element Type.'
    _iid_ = GUID('{2A3E65FD-9D5B-4BAA-8A3B-39824FC8C587}')
    _idlflags_ = ['oleautomation']
DELayerType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDELayerType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGxFilterInfo, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElementType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEGeoDatasetType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDataType, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, IDEFileType]

ISMRoutingMetaData._methods_ = [
    COMMETHOD([dispid(1610678272), helpstring(u'Name of data vendor.'), 'propget'], HRESULT, 'Vendor',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(1610678273), helpstring(u'Name of data product.'), 'propget'], HRESULT, 'ProductName',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(1610678274), helpstring(u'Version of data product.'), 'propget'], HRESULT, 'ProductVersion',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(1610678275), helpstring(u'The name of the geographic region covered by the routing service.'), 'propget'], HRESULT, 'Geography',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(1610678276), helpstring(u'Descriptive text of the data product used in the routing service.'), 'propget'], HRESULT, 'Description',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(1610678277), helpstring(u'Date and time of data creation in ISO 8601 format.'), 'propget'], HRESULT, 'Time',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
]
################################################################
## code template for ISMRoutingMetaData implementation
##class ISMRoutingMetaData_Impl(object):
##    @property
##    def Vendor(self):
##        u'Name of data vendor.'
##        #return pVal
##
##    @property
##    def Description(self):
##        u'Descriptive text of the data product used in the routing service.'
##        #return pVal
##
##    @property
##    def ProductName(self):
##        u'Name of data product.'
##        #return pVal
##
##    @property
##    def ProductVersion(self):
##        u'Version of data product.'
##        #return pVal
##
##    @property
##    def Time(self):
##        u'Date and time of data creation in ISO 8601 format.'
##        #return pVal
##
##    @property
##    def Geography(self):
##        u'The name of the geographic region covered by the routing service.'
##        #return pVal
##

class IDECoverageFeatureClassType(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Indicator interface for the CoverageFeatureClass Data Element Type.'
    _iid_ = GUID('{943DB542-3A26-40E3-9A26-3342655BD3A2}')
    _idlflags_ = ['oleautomation']
IDECoverageFeatureClassType._methods_ = [
]
################################################################
## code template for IDECoverageFeatureClassType implementation
##class IDECoverageFeatureClassType_Impl(object):

class ICadDrawingLayers(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to properties that give information on the layers in the CAD drawing.'
    _iid_ = GUID('{E37F71AA-BFB1-11D2-9B20-00C04FA33299}')
    _idlflags_ = ['oleautomation']
ICadDrawingLayers._methods_ = [
    COMMETHOD(['propget', helpstring(u'The number of layers in the CAD drawing.')], HRESULT, 'DrawingLayerCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'The name of the CAD drawing layer at the specified index.')], HRESULT, 'DrawingLayerName',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'FilePath' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the specified CAD drawing layer visible in the CAD layer in ArcMap.')], HRESULT, 'DrawingLayerVisible',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'visible' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the specified CAD drawing layer visible in the CAD layer in ArcMap.')], HRESULT, 'DrawingLayerVisible',
              ( ['in'], c_int, 'index' ),
              ( ['in'], VARIANT_BOOL, 'visible' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the specified CAD drawing layer visible in the CAD drawing itself.')], HRESULT, 'OriginalDrawingLayerVisible',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'visible' )),
]
################################################################
## code template for ICadDrawingLayers implementation
##class ICadDrawingLayers_Impl(object):
##    @property
##    def DrawingLayerName(self, index):
##        u'The name of the CAD drawing layer at the specified index.'
##        #return FilePath
##
##    @property
##    def OriginalDrawingLayerVisible(self, index):
##        u'Indicates if the specified CAD drawing layer visible in the CAD drawing itself.'
##        #return visible
##
##    def _get(self, index):
##        u'Indicates if the specified CAD drawing layer visible in the CAD layer in ArcMap.'
##        #return visible
##    def _set(self, index, visible):
##        u'Indicates if the specified CAD drawing layer visible in the CAD layer in ArcMap.'
##    DrawingLayerVisible = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def DrawingLayerCount(self):
##        u'The number of layers in the CAD drawing.'
##        #return Count
##

class CoverageFeatureClassName(CoClass):
    u'Maintains ArcInfo Coverage Feature Class information.'
    _reg_clsid_ = GUID('{72F77DE8-122A-11D3-9F31-00C04F79927C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
CoverageFeatureClassName._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName, ICoverageFeatureClassName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetName2, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetNameFileStat, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClassName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITableName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IModelInfo, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IObjectClassName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITopologyClassName]

class IDEFile(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the File Data Element.'
    _iid_ = GUID('{DF006D6F-661E-46CA-A591-D3C6CB5D94D3}')
    _idlflags_ = ['oleautomation']
IDEFile._methods_ = [
]
################################################################
## code template for IDEFile implementation
##class IDEFile_Impl(object):

class CoverageName(CoClass):
    u'Maintains ArcInfo Coverage information.'
    _reg_clsid_ = GUID('{1E921C72-122F-11D3-9F31-00C04F79927C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
CoverageName._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName, ICoverageName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetNameFileStat, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureDatasetName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureDatasetName2, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetContainerName]

class IDEVPFCoverageType(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the DEVPFCoverage Data Element Type.'
    _iid_ = GUID('{BA80D3FD-B1C8-4111-B3DB-037D6EA3D9EB}')
    _idlflags_ = ['oleautomation']
IDEVPFCoverageType._methods_ = [
]
################################################################
## code template for IDEVPFCoverageType implementation
##class IDEVPFCoverageType_Impl(object):

class DEFileType(CoClass):
    u'File Data Element object Type.'
    _reg_clsid_ = GUID('{C486AA07-9027-4D78-88FC-4A7A940BB367}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
DEFileType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDEFileType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElementType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDataType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGxFilterInfo, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone]

class DELayer(CoClass):
    u'Layer Data Element object.'
    _reg_clsid_ = GUID('{BDD71708-3463-4787-A491-B9363B937DBE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
DELayer._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDELayer, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElement, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEGeoDataset, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPValue, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDescribe, IDEFile]

class DEMapDocumentType(CoClass):
    u'MapDocument Data Element object Type.'
    _reg_clsid_ = GUID('{EC42CEB1-8029-4F90-A18C-5790AE1FAD01}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
DEMapDocumentType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDEMapDocumentType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElementType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDataType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGxFilterInfo, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone]

class IDEDbaseTableType(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the Dbase Table Data Element Type.'
    _iid_ = GUID('{5B5C7610-A953-11D5-9321-0080C71A3226}')
    _idlflags_ = ['oleautomation']
IDEDbaseTableType._methods_ = [
]
################################################################
## code template for IDEDbaseTableType implementation
##class IDEDbaseTableType_Impl(object):

class DEVPFCoverage(CoClass):
    u'DEVPFCoverage Dataset Data Element object.'
    _reg_clsid_ = GUID('{CA4FF80D-85A9-445C-ADB2-A5C7811B3C36}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
class IDEVPFCoverage(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the DEVPFCoverage Data Element.'
    _iid_ = GUID('{26785829-6D41-457C-B953-08FED1E16EDA}')
    _idlflags_ = ['oleautomation']
DEVPFCoverage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEFeatureDataset, IDEVPFCoverage, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEGeoDataset, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEDataset, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElement, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPValue, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDescribe]

class GPArcInfoItem(CoClass):
    u'ArcInfo Item Data Element object.'
    _reg_clsid_ = GUID('{6DDDBBB2-41DC-4F12-913E-803196EB33FA}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
class IGPArcInfoItem(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the ArcInfo Item Data Element.'
    _iid_ = GUID('{C95B22E0-A3C3-11D5-931C-0080C71A3226}')
    _idlflags_ = ['oleautomation']
GPArcInfoItem._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGPArcInfoItem, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPValue, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDescribe]

class StreetMapWorkspaceFactory(CoClass):
    u'Esri StreetMap workspace factory.'
    _reg_clsid_ = GUID('{AE2469E8-E110-4CD6-B3F4-A756CBF921CA}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
StreetMapWorkspaceFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IPlugInWorkspaceFactoryHelper, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceFactory, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceFactory2]

class DELasDataset(CoClass):
    u'LAS Dataset Data Element object.'
    _reg_clsid_ = GUID('{EA006709-CD03-439D-80A1-9254E25412E3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
class IDELasDataset(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the LAS Dataset Data Element.'
    _iid_ = GUID('{1508D058-F970-487C-AFBE-31DB1C3ED594}')
    _idlflags_ = ['oleautomation']
DELasDataset._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDELasDataset, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEGeoDataset, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEDataset, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElement, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPValue, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDescribe, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

ISMRouterEnvelope._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'The position of the top.'), 'propget'], HRESULT, 'Top',
              ( ['retval', 'out'], POINTER(c_double), 'pVal' )),
    COMMETHOD([dispid(1), helpstring(u'The position of the top.'), 'propput'], HRESULT, 'Top',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD([dispid(2), helpstring(u'The position of the bottom.'), 'propget'], HRESULT, 'Bottom',
              ( ['retval', 'out'], POINTER(c_double), 'pVal' )),
    COMMETHOD([dispid(2), helpstring(u'The position of the bottom.'), 'propput'], HRESULT, 'Bottom',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD([dispid(3), helpstring(u'The position of the left side.'), 'propget'], HRESULT, 'Left',
              ( ['retval', 'out'], POINTER(c_double), 'pVal' )),
    COMMETHOD([dispid(3), helpstring(u'The position of the left side.'), 'propput'], HRESULT, 'Left',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD([dispid(4), helpstring(u'The position of the right side.'), 'propget'], HRESULT, 'Right',
              ( ['retval', 'out'], POINTER(c_double), 'pVal' )),
    COMMETHOD([dispid(4), helpstring(u'The position of the right side.'), 'propput'], HRESULT, 'Right',
              ( ['in'], c_double, 'pVal' )),
]
################################################################
## code template for ISMRouterEnvelope implementation
##class ISMRouterEnvelope_Impl(object):
##    def _get(self):
##        u'The position of the right side.'
##        #return pVal
##    def _set(self, pVal):
##        u'The position of the right side.'
##    Right = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The position of the top.'
##        #return pVal
##    def _set(self, pVal):
##        u'The position of the top.'
##    Top = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The position of the left side.'
##        #return pVal
##    def _set(self, pVal):
##        u'The position of the left side.'
##    Left = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The position of the bottom.'
##        #return pVal
##    def _set(self, pVal):
##        u'The position of the bottom.'
##    Bottom = property(_get, _set, doc = _set.__doc__)
##

class SMNetAttribute(CoClass):
    u'Deprecated as of 10.1. Information about network attribute properties.'
    _reg_clsid_ = GUID('{F8B65FF7-5850-11D7-B321-008048DB11DE}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
class ISMNetAttribute2(ISMNetAttribute):
    _case_insensitive_ = True
    u'Deprecated as of 10.1. Provides access to network attribute usage type.'
    _iid_ = GUID('{B1A5376C-DFDF-48DD-A472-076808C0C73E}')
    _idlflags_ = ['dual', 'oleautomation']
SMNetAttribute._com_interfaces_ = [ISMNetAttribute, ISMNetAttribute2]

class DEVPFTableType(CoClass):
    u'VPFTable Data Element object Type.'
    _reg_clsid_ = GUID('{3F3C713F-CC15-4EA7-A780-193E021D4251}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
class IDEVPFTableType(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the VPFTable Data Element Type.'
    _iid_ = GUID('{DBB10AC8-BBBD-44AF-AAD6-A689AF24DBFB}')
    _idlflags_ = ['oleautomation']
DEVPFTableType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDEVPFTableType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDETableType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEDatasetType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGxFilterInfo, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElementType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDataType, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone]

class DEDiskConnectionType(CoClass):
    u'Disk Connection Data Element object Type.'
    _reg_clsid_ = GUID('{36AFBB31-CDBE-41CB-BB11-58484C2ACF45}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
DEDiskConnectionType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDEDiskConnectionType, IDEFolderType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEWorkspaceType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElementType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDataType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGxFilterInfo, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone]

IDEFileType._methods_ = [
]
################################################################
## code template for IDEFileType implementation
##class IDEFileType_Impl(object):

class DECoverageFeatureClassType(CoClass):
    u'CoverageFeatureClass Data Element object Type.'
    _reg_clsid_ = GUID('{874E63D8-B362-457B-A3C8-AA0F3F443E0B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
DECoverageFeatureClassType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDECoverageFeatureClassType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEFeatureClassType, IDEArcInfoTableType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDETableType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEGeoDatasetType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEDatasetType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElementType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGxFilterInfo, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDataType, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone]

class DEArcInfoTable(CoClass):
    u'ArcInfo Table Data Element object.'
    _reg_clsid_ = GUID('{1CC786EC-5EFE-493C-8A25-B546844665D7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
DEArcInfoTable._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDEArcInfoTable, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDETable, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEDataset, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElement, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPValue, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDescribe]

class DEFile(CoClass):
    u'File Data Element object.'
    _reg_clsid_ = GUID('{175CF2C5-12BF-413A-8FDF-3DA30CC09BEE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
DEFile._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDEFile, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElement, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPValue, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDescribe]

class DEArcInfoUtilities(CoClass):
    u'ArcInfo Data Element utilities object.'
    _reg_clsid_ = GUID('{95D74728-CADD-41C2-AF2B-7E816364D905}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
class IDEArcInfoUtilities(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the ArcInfo Data Element Utilities.'
    _iid_ = GUID('{1C1D3491-9E02-4283-BE2F-B8177CC8F01F}')
    _idlflags_ = ['oleautomation']
DEArcInfoUtilities._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDEArcInfoUtilities]

IDELayerType._methods_ = [
]
################################################################
## code template for IDELayerType implementation
##class IDELayerType_Impl(object):

class IDESpatialReferencesFolder(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the Spatial References Folder Data Element.'
    _iid_ = GUID('{BC5EDBFD-375C-40A2-B9C2-EA8DFE2DE1E0}')
    _idlflags_ = ['oleautomation']
IDESpatialReferencesFolder._methods_ = [
]
################################################################
## code template for IDESpatialReferencesFolder implementation
##class IDESpatialReferencesFolder_Impl(object):

ISMSpeedGroup._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'The speed value of the group.'), 'propget'], HRESULT, 'Speed',
              ( ['retval', 'out'], POINTER(c_float), 'pVal' )),
    COMMETHOD([dispid(1), helpstring(u'The speed value of the group.'), 'propput'], HRESULT, 'Speed',
              ( ['in'], c_float, 'pVal' )),
    COMMETHOD([dispid(2), helpstring(u'Speed group description.'), 'propget'], HRESULT, 'Description',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
]
################################################################
## code template for ISMSpeedGroup implementation
##class ISMSpeedGroup_Impl(object):
##    def _get(self):
##        u'The speed value of the group.'
##        #return pVal
##    def _set(self, pVal):
##        u'The speed value of the group.'
##    Speed = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Description(self):
##        u'Speed group description.'
##        #return pVal
##

ISMSpeedGroup2._methods_ = [
    COMMETHOD([dispid(3), helpstring(u'A SQL-like query string for determining records that belong to the speed group.'), 'propget'], HRESULT, 'QueryString',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
]
################################################################
## code template for ISMSpeedGroup2 implementation
##class ISMSpeedGroup2_Impl(object):
##    @property
##    def QueryString(self):
##        u'A SQL-like query string for determining records that belong to the speed group.'
##        #return pVal
##

class IDEVPFTable(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the VPFTable Data Element.'
    _iid_ = GUID('{A30B5D18-63ED-493A-90E5-75DC2D55D79C}')
    _idlflags_ = ['oleautomation']
IDEVPFTable._methods_ = [
]
################################################################
## code template for IDEVPFTable implementation
##class IDEVPFTable_Impl(object):

IDEVPFTableType._methods_ = [
]
################################################################
## code template for IDEVPFTableType implementation
##class IDEVPFTableType_Impl(object):

class DETextFileType(CoClass):
    u'Text File Data Element object Type.'
    _reg_clsid_ = GUID('{9A4700E6-C10C-4ECB-AAE6-90D382AE22C4}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
DETextFileType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDETextFileType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDETableType, IDEFileType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEDatasetType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElementType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDataType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGxFilterInfo, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone]


# values for enumeration 'esriSMRoadType'
esriSMRoadTypeHighways = 1
esriSMRoadTypeFerries = 2
esriSMRoadType = c_int # enum
class DEDbaseTableType(CoClass):
    u'Dbase Table Data Element object Type.'
    _reg_clsid_ = GUID('{11E37CD0-A664-11D5-931D-0080C71A3226}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
DEDbaseTableType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDEDbaseTableType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDETableType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEDatasetType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGxFilterInfo, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElementType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDataType, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone]

class DEDiskConnection(CoClass):
    u'Disk Connection Data Element object.'
    _reg_clsid_ = GUID('{8E5E855A-7D60-4CE1-AFD0-45929C9F492C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
DEDiskConnection._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDEDiskConnection, IDEFolder, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEWorkspace, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElement, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPValue, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDescribe]

ISMRouterPoint._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'The X coordinate of the point.'), 'propget'], HRESULT, 'X',
              ( ['retval', 'out'], POINTER(c_double), 'pVal' )),
    COMMETHOD([dispid(1), helpstring(u'The X coordinate of the point.'), 'propput'], HRESULT, 'X',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD([dispid(2), helpstring(u'The Y coordinate of the point.'), 'propget'], HRESULT, 'Y',
              ( ['retval', 'out'], POINTER(c_double), 'pVal' )),
    COMMETHOD([dispid(2), helpstring(u'The Y coordinate of the point.'), 'propput'], HRESULT, 'Y',
              ( ['in'], c_double, 'pVal' )),
]
################################################################
## code template for ISMRouterPoint implementation
##class ISMRouterPoint_Impl(object):
##    def _get(self):
##        u'The Y coordinate of the point.'
##        #return pVal
##    def _set(self, pVal):
##        u'The Y coordinate of the point.'
##    Y = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The X coordinate of the point.'
##        #return pVal
##    def _set(self, pVal):
##        u'The X coordinate of the point.'
##    X = property(_get, _set, doc = _set.__doc__)
##

ISMStopsCollection._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'The number of stops in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(2), helpstring(u'The stop at the specified position in the collection.'), 'propget'], HRESULT, 'Item',
              ( ['in'], c_int, 'Position' ),
              ( ['retval', 'out'], POINTER(POINTER(ISMStop)), 'pVal' )),
    COMMETHOD([dispid(3), helpstring(u'Adds a stop to the end of collection.')], HRESULT, 'Add',
              ( ['in'], POINTER(ISMStop), 'pItem' )),
    COMMETHOD([dispid(4), helpstring(u'Inserts a stop at the specified position in the collection.')], HRESULT, 'Insert',
              ( ['in'], c_int, 'Position' ),
              ( ['in'], POINTER(ISMStop), 'pItem' )),
    COMMETHOD([dispid(5), helpstring(u'Removes the stop at the specified position in the collection.')], HRESULT, 'Remove',
              ( ['in'], c_int, 'Position' )),
    COMMETHOD([dispid(6), helpstring(u'Removes all stops from the collection.')], HRESULT, 'Clear'),
]
################################################################
## code template for ISMStopsCollection implementation
##class ISMStopsCollection_Impl(object):
##    @property
##    def Count(self):
##        u'The number of stops in the collection.'
##        #return pVal
##
##    def Insert(self, Position, pItem):
##        u'Inserts a stop at the specified position in the collection.'
##        #return 
##
##    def Clear(self):
##        u'Removes all stops from the collection.'
##        #return 
##
##    def Remove(self, Position):
##        u'Removes the stop at the specified position in the collection.'
##        #return 
##
##    @property
##    def Item(self, Position):
##        u'The stop at the specified position in the collection.'
##        #return pVal
##
##    def Add(self, pItem):
##        u'Adds a stop to the end of collection.'
##        #return 
##

IDECadDrawingDataset._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates whether Cad Dataset is 2d.')], HRESULT, 'Is2d',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Is2d' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether Cad Dataset is 2d.')], HRESULT, 'Is2d',
              ( ['in'], VARIANT_BOOL, 'Is2d' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether Cad Dataset is 3d.')], HRESULT, 'Is3d',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Is3d' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether Cad Dataset is 3d.')], HRESULT, 'Is3d',
              ( ['in'], VARIANT_BOOL, 'Is3d' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether Cad Dataset is an AutoCad file.')], HRESULT, 'IsAutoCad',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsAutoCad' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether Cad Dataset is an AutoCad file.')], HRESULT, 'IsAutoCad',
              ( ['in'], VARIANT_BOOL, 'IsAutoCad' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether Cad Dataset is an Microstation file.')], HRESULT, 'IsDgn',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsDgn' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether Cad Dataset is an Microstation file.')], HRESULT, 'IsDgn',
              ( ['in'], VARIANT_BOOL, 'IsDgn' )),
]
################################################################
## code template for IDECadDrawingDataset implementation
##class IDECadDrawingDataset_Impl(object):
##    def _get(self):
##        u'Indicates whether Cad Dataset is 3d.'
##        #return Is3d
##    def _set(self, Is3d):
##        u'Indicates whether Cad Dataset is 3d.'
##    Is3d = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether Cad Dataset is an AutoCad file.'
##        #return IsAutoCad
##    def _set(self, IsAutoCad):
##        u'Indicates whether Cad Dataset is an AutoCad file.'
##    IsAutoCad = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether Cad Dataset is an Microstation file.'
##        #return IsDgn
##    def _set(self, IsDgn):
##        u'Indicates whether Cad Dataset is an Microstation file.'
##    IsDgn = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether Cad Dataset is 2d.'
##        #return Is2d
##    def _set(self, Is2d):
##        u'Indicates whether Cad Dataset is 2d.'
##    Is2d = property(_get, _set, doc = _set.__doc__)
##

class SDCNetworkAttribute(CoClass):
    u'A container for describing a SDC network dataset attribute.'
    _reg_clsid_ = GUID('{A2AB1FBA-AA5F-485E-97FE-79D0F5FF9984}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
SDCNetworkAttribute._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INetworkAttribute, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDescribe]

class PCCoverageWorkspaceFactory(CoClass):
    u'Esri PC ARC/INFO Workspace Factory.'
    _reg_clsid_ = GUID('{6DE812D2-9AB6-11D2-B0D7-0000F8780820}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
PCCoverageWorkspaceFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceFactory, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceFactory2]

ISMRouterFactory._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Creates a SMRouter object based on information in the input routing initialization file.')], HRESULT, 'CreateRouter',
              ( ['in'], BSTR, 'RoutingFilePath' ),
              ( ['retval', 'out'], POINTER(POINTER(ISMRouter)), 'pIRouter' )),
    COMMETHOD([dispid(2), helpstring(u'Creates a SMRouter object based on additional information in the alternate routing configuration file.')], HRESULT, 'CreateRouterCfg',
              ( ['in'], BSTR, 'RoutingFilePath' ),
              ( ['in'], BSTR, 'ConfigPath' ),
              ( ['retval', 'out'], POINTER(POINTER(ISMRouter)), 'pIRouter' )),
]
################################################################
## code template for ISMRouterFactory implementation
##class ISMRouterFactory_Impl(object):
##    def CreateRouterCfg(self, RoutingFilePath, ConfigPath):
##        u'Creates a SMRouter object based on additional information in the alternate routing configuration file.'
##        #return pIRouter
##
##    def CreateRouter(self, RoutingFilePath):
##        u'Creates a SMRouter object based on information in the input routing initialization file.'
##        #return pIRouter
##

class DEVPFTable(CoClass):
    u'VPFTable Data Element object.'
    _reg_clsid_ = GUID('{48AAB232-6F1F-4261-9DAC-CBA55D183649}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
DEVPFTable._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDEVPFTable, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDETable, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEDataset, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElement, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPValue, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDescribe]

class DECoverageFeatureClass(CoClass):
    u'Coverage Feature Class Data Element object.'
    _reg_clsid_ = GUID('{B7EC3865-805B-41A4-804C-8B4A30AA4128}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
class IDECoverageFeatureClass(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the Coverage Feature Class Data Element.'
    _iid_ = GUID('{25EA15B1-7425-452B-8FB6-CA3F8D088129}')
    _idlflags_ = ['oleautomation']
DECoverageFeatureClass._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDECoverageFeatureClass, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEFeatureClass, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDETable, IDEArcInfoTable, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEGeoDataset, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEDataset, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElement, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPValue, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDescribe]

class SDCWorkspaceFactory(CoClass):
    u'Esri SDC workspace factory.'
    _reg_clsid_ = GUID('{34DAE34F-DBE2-409C-8F85-DDBB46138011}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
SDCWorkspaceFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceFactory, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceFactory2, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IPlugInWorkspaceFactoryHelper, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IPlugInCreateWorkspace, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IParseNameString]

ISMPointsCollection._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Number of points in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(2), helpstring(u'Represents the point in the collection at the specified position.'), 'propget'], HRESULT, 'Item',
              ( ['in'], c_int, 'Position' ),
              ( ['retval', 'out'], POINTER(POINTER(ISMRouterPoint)), 'pVal' )),
    COMMETHOD([dispid(3), helpstring(u'Adds a point to the end of the collection.')], HRESULT, 'Add',
              ( ['in'], POINTER(ISMRouterPoint), 'pItem' )),
    COMMETHOD([dispid(4), helpstring(u'Inserts a point in the collection at the specified position.')], HRESULT, 'Insert',
              ( ['in'], c_int, 'Position' ),
              ( ['in'], POINTER(ISMRouterPoint), 'pItem' )),
    COMMETHOD([dispid(5), helpstring(u'Removes a point from the collection at the specified position.')], HRESULT, 'Remove',
              ( ['in'], c_int, 'Position' )),
    COMMETHOD([dispid(6), helpstring(u'Removes all points from the collection.')], HRESULT, 'Clear'),
]
################################################################
## code template for ISMPointsCollection implementation
##class ISMPointsCollection_Impl(object):
##    @property
##    def Count(self):
##        u'Number of points in the collection.'
##        #return pVal
##
##    def Insert(self, Position, pItem):
##        u'Inserts a point in the collection at the specified position.'
##        #return 
##
##    def Clear(self):
##        u'Removes all points from the collection.'
##        #return 
##
##    def Remove(self, Position):
##        u'Removes a point from the collection at the specified position.'
##        #return 
##
##    @property
##    def Item(self, Position):
##        u'Represents the point in the collection at the specified position.'
##        #return pVal
##
##    def Add(self, pItem):
##        u'Adds a point to the end of the collection.'
##        #return 
##

ISMDirections._methods_ = [
    COMMETHOD([dispid(3), helpstring(u'The total length of the route (in miles by default).'), 'propget'], HRESULT, 'TotalLength',
              ( ['retval', 'out'], POINTER(c_double), 'pVal' )),
    COMMETHOD([dispid(4), helpstring(u'The total time of the entire trip.'), 'propget'], HRESULT, 'TotalTime',
              ( ['retval', 'out'], POINTER(c_double), 'pVal' )),
    COMMETHOD([dispid(5), helpstring(u'The total driving time for the route.'), 'propget'], HRESULT, 'TotalDrivingTime',
              ( ['retval', 'out'], POINTER(c_double), 'pVal' )),
    COMMETHOD([dispid(6), helpstring(u'A string containing the total time and length of the route.'), 'propget'], HRESULT, 'TotalsText',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(7), helpstring(u'The geographic extent of the entire route.'), 'propget'], HRESULT, 'BoundBox',
              ( ['retval', 'out'], POINTER(POINTER(ISMRouterEnvelope)), 'pVal' )),
    COMMETHOD([dispid(8), helpstring(u'The total number of items in the driving directions object.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(9), helpstring(u'A reference to a direction item by its position.'), 'propget'], HRESULT, 'Item',
              ( ['in'], c_int, 'Position' ),
              ( ['retval', 'out'], POINTER(POINTER(ISMDirItem)), 'pVal' )),
]
################################################################
## code template for ISMDirections implementation
##class ISMDirections_Impl(object):
##    @property
##    def TotalTime(self):
##        u'The total time of the entire trip.'
##        #return pVal
##
##    @property
##    def TotalLength(self):
##        u'The total length of the route (in miles by default).'
##        #return pVal
##
##    @property
##    def Count(self):
##        u'The total number of items in the driving directions object.'
##        #return pVal
##
##    @property
##    def Item(self, Position):
##        u'A reference to a direction item by its position.'
##        #return pVal
##
##    @property
##    def BoundBox(self):
##        u'The geographic extent of the entire route.'
##        #return pVal
##
##    @property
##    def TotalDrivingTime(self):
##        u'The total driving time for the route.'
##        #return pVal
##
##    @property
##    def TotalsText(self):
##        u'A string containing the total time and length of the route.'
##        #return pVal
##

class ICadDrawingDataset(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Cad Drawing Dataset.'
    _iid_ = GUID('{6C1D6540-4930-11D3-9B39-00C04FA33299}')
    _idlflags_ = ['oleautomation']
ICadDrawingDataset._methods_ = [
    COMMETHOD(['propget', helpstring(u'The Full PathName of the Cad File.')], HRESULT, 'FilePath',
              ( ['retval', 'out'], POINTER(BSTR), 'FilePath' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether Cad Dataset is 2d.')], HRESULT, 'Is2d',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Is2d' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether Cad Dataset is 3d.')], HRESULT, 'Is3d',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Is3d' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether Cad Dataset is an AutoCad file.')], HRESULT, 'IsAutoCad',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsAutoCad' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether Cad Dataset is an Microstation file.')], HRESULT, 'IsDgn',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsDgn' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether Cad Dataset exists.')], HRESULT, 'Exists',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Exists' )),
]
################################################################
## code template for ICadDrawingDataset implementation
##class ICadDrawingDataset_Impl(object):
##    @property
##    def Is3d(self):
##        u'Indicates whether Cad Dataset is 3d.'
##        #return Is3d
##
##    @property
##    def IsAutoCad(self):
##        u'Indicates whether Cad Dataset is an AutoCad file.'
##        #return IsAutoCad
##
##    @property
##    def Exists(self):
##        u'Indicates whether Cad Dataset exists.'
##        #return Exists
##
##    @property
##    def FilePath(self):
##        u'The Full PathName of the Cad File.'
##        #return FilePath
##
##    @property
##    def IsDgn(self):
##        u'Indicates whether Cad Dataset is an Microstation file.'
##        #return IsDgn
##
##    @property
##    def Is2d(self):
##        u'Indicates whether Cad Dataset is 2d.'
##        #return Is2d
##

class DEShapeFileType(CoClass):
    u'ShapeFile Data Element object Type.'
    _reg_clsid_ = GUID('{44A51F3F-EF06-4FD9-BC52-010E6CA0E84B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
class IDEShapeFileType(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the ShapeFile Data Element Type.'
    _iid_ = GUID('{C7D6C9E2-278E-4F86-A349-F80BAAC7A733}')
    _idlflags_ = ['oleautomation']
DEShapeFileType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDEShapeFileType, IDEDbaseTableType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEFeatureClassType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDETableType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEGeoDatasetType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEDatasetType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGxFilterInfo, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElementType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDataType, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone]

class DECoverage(CoClass):
    u'Coverage Data Element object.'
    _reg_clsid_ = GUID('{96B70C47-2C7F-405F-B9FD-DEAA3CDC084C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
class IDECoverage(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the Coverage Data Element.'
    _iid_ = GUID('{BDE67D8B-BF5E-45EC-A3FD-09AC77EFE850}')
    _idlflags_ = ['oleautomation']
DECoverage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDECoverage, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEFeatureDataset, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEGeoDataset, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEDataset, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElement, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPValue, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDescribe]

IDERemoteDatabaseFolderType._methods_ = [
]
################################################################
## code template for IDERemoteDatabaseFolderType implementation
##class IDERemoteDatabaseFolderType_Impl(object):

class CadDrawingName(CoClass):
    u'Cad Drawing Name object'
    _reg_clsid_ = GUID('{D4224309-A5CB-11D2-9B10-00C04FA33299}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
CadDrawingName._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetName, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo]

IUsageModeOption._methods_ = [
    COMMETHOD(['propget', helpstring(u'Usage mode option name.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'psName' )),
    COMMETHOD(['propget', helpstring(u'Usage mode option value.')], HRESULT, 'Value',
              ( ['retval', 'out'], POINTER(BSTR), 'psValue' )),
]
################################################################
## code template for IUsageModeOption implementation
##class IUsageModeOption_Impl(object):
##    @property
##    def Name(self):
##        u'Usage mode option name.'
##        #return psName
##
##    @property
##    def Value(self):
##        u'Usage mode option value.'
##        #return psValue
##

IDECoverage._methods_ = [
    COMMETHOD(['propget', helpstring(u'The tolerances of the coverage.')], HRESULT, 'Tolerances',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'propertySet' )),
    COMMETHOD(['propputref', helpstring(u'The tolerances of the coverage.')], HRESULT, 'Tolerances',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'propertySet' )),
]
################################################################
## code template for IDECoverage implementation
##class IDECoverage_Impl(object):
##    def Tolerances(self, propertySet):
##        u'The tolerances of the coverage.'
##        #return 
##

class DETinType(CoClass):
    u'Tin Data Element object Type.'
    _reg_clsid_ = GUID('{F0B41A32-EE77-4B16-A5EE-16BCE3D8F3CC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
class IDETinType(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the Tin Data Element Type.'
    _iid_ = GUID('{0853EB47-69E4-4309-A8BA-5D14B356362B}')
    _idlflags_ = ['oleautomation']
DETinType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDETinType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEGeoDatasetType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEDatasetType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElementType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGxFilterInfo, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDataType, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone]

class VpfWorkspaceFactory(CoClass):
    u'Esri VPF Workspace Factory'
    _reg_clsid_ = GUID('{397847F9-C865-11D3-9B56-00C04FA33299}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
VpfWorkspaceFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceFactory, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceFactory2, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IParseNameString]

IDEShapeFileType._methods_ = [
]
################################################################
## code template for IDEShapeFileType implementation
##class IDEShapeFileType_Impl(object):

class DEFolder(CoClass):
    u'Folder Data Element object.'
    _reg_clsid_ = GUID('{273CCEBC-1AA2-4429-BBD5-4CB7C6E20465}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
DEFolder._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDEFolder, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEWorkspace, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElement, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPValue, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDescribe]

IDETinType._methods_ = [
]
################################################################
## code template for IDETinType implementation
##class IDETinType_Impl(object):

class DEShapeFile(CoClass):
    u'ShapeFile Data Element object.'
    _reg_clsid_ = GUID('{03E6FB47-AA38-476C-934B-1DF5765C76EB}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
class IDEDbaseTable(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the Dbase Table Data Element.'
    _iid_ = GUID('{CBA6712B-E7C5-4013-9BC7-9656BFB0DE41}')
    _idlflags_ = ['oleautomation']
DEShapeFile._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDEShapeFile, IDEDbaseTable, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEDataset, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEGeoDataset, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEFeatureClass, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDETable, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElement, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPValue, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDescribe]

class DESpatialReferencesFolder(CoClass):
    u'Spatial References Folder Data Element object.'
    _reg_clsid_ = GUID('{3189F8FC-A9C8-4B8E-8C47-43C758A7A8BD}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
DESpatialReferencesFolder._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDESpatialReferencesFolder, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElement, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPValue, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDescribe]

IDEVPFCoverage._methods_ = [
]
################################################################
## code template for IDEVPFCoverage implementation
##class IDEVPFCoverage_Impl(object):

class IDELasDatasetType(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the LAS Dataset Data Element Type.'
    _iid_ = GUID('{E4C66C0C-69EA-466B-84C7-EB6ACAB69490}')
    _idlflags_ = ['oleautomation']
IDELasDatasetType._methods_ = [
]
################################################################
## code template for IDELasDatasetType implementation
##class IDELasDatasetType_Impl(object):

class SMSpeedGroups(CoClass):
    u'Deprecated as of 10.1. The collection of speed groups.'
    _reg_clsid_ = GUID('{F8B66009-5850-11D7-B321-008048DB11DE}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
SMSpeedGroups._com_interfaces_ = [ISMSpeedGroups]

class SMNetAttributesCollection(CoClass):
    u'Deprecated as of 10.1. The collection of network attributes.'
    _reg_clsid_ = GUID('{F8B65FFA-5850-11D7-B321-008048DB11DE}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
SMNetAttributesCollection._com_interfaces_ = [ISMNetAttributesCollection]

ISMTripPlanSettings._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Indicates whether trip planning is enabled.'), 'propget'], HRESULT, 'TripPlanningEnable',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD([dispid(1), helpstring(u'Indicates whether trip planning is enabled.'), 'propput'], HRESULT, 'TripPlanningEnable',
              ( ['in'], VARIANT_BOOL, 'pVal' )),
    COMMETHOD([dispid(2), helpstring(u'The start date of the trip.'), 'propget'], HRESULT, 'TripStart',
              ( ['retval', 'out'], POINTER(c_double), 'pVal' )),
    COMMETHOD([dispid(2), helpstring(u'The start date of the trip.'), 'propput'], HRESULT, 'TripStart',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD([dispid(3), helpstring(u'Time from midnight when driving must start every day.'), 'propget'], HRESULT, 'DayDriveStart',
              ( ['retval', 'out'], POINTER(c_double), 'pVal' )),
    COMMETHOD([dispid(3), helpstring(u'Time from midnight when driving must start every day.'), 'propput'], HRESULT, 'DayDriveStart',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD([dispid(4), helpstring(u'Time from midnight when driving must stop every day.'), 'propget'], HRESULT, 'DayDriveEnd',
              ( ['retval', 'out'], POINTER(c_double), 'pVal' )),
    COMMETHOD([dispid(4), helpstring(u'Time from midnight when driving must stop every day.'), 'propput'], HRESULT, 'DayDriveEnd',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD([dispid(5), helpstring(u'Amount of driving time allowed after the DayDriveEnd time is reached.'), 'propget'], HRESULT, 'DriveFlexibility',
              ( ['retval', 'out'], POINTER(c_short), 'pVal' )),
    COMMETHOD([dispid(5), helpstring(u'Amount of driving time allowed after the DayDriveEnd time is reached.'), 'propput'], HRESULT, 'DriveFlexibility',
              ( ['in'], c_short, 'pVal' )),
    COMMETHOD([dispid(6), helpstring(u'Indicates whether periodic rest breaks are enabled.'), 'propget'], HRESULT, 'RestBreaksEnable',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD([dispid(6), helpstring(u'Indicates whether periodic rest breaks are enabled.'), 'propput'], HRESULT, 'RestBreaksEnable',
              ( ['in'], VARIANT_BOOL, 'pVal' )),
    COMMETHOD([dispid(7), helpstring(u'The duration of rest breaks in minutes.'), 'propget'], HRESULT, 'RestDuration',
              ( ['retval', 'out'], POINTER(c_short), 'pVal' )),
    COMMETHOD([dispid(7), helpstring(u'The duration of rest breaks in minutes.'), 'propput'], HRESULT, 'RestDuration',
              ( ['in'], c_short, 'pVal' )),
    COMMETHOD([dispid(8), helpstring(u'Driving time between rest breaks in minutes.'), 'propget'], HRESULT, 'DriveBetweenRest',
              ( ['retval', 'out'], POINTER(c_short), 'pVal' )),
    COMMETHOD([dispid(8), helpstring(u'Driving time between rest breaks in minutes.'), 'propput'], HRESULT, 'DriveBetweenRest',
              ( ['in'], c_short, 'pVal' )),
]
################################################################
## code template for ISMTripPlanSettings implementation
##class ISMTripPlanSettings_Impl(object):
##    def _get(self):
##        u'Indicates whether trip planning is enabled.'
##        #return pVal
##    def _set(self, pVal):
##        u'Indicates whether trip planning is enabled.'
##    TripPlanningEnable = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether periodic rest breaks are enabled.'
##        #return pVal
##    def _set(self, pVal):
##        u'Indicates whether periodic rest breaks are enabled.'
##    RestBreaksEnable = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Driving time between rest breaks in minutes.'
##        #return pVal
##    def _set(self, pVal):
##        u'Driving time between rest breaks in minutes.'
##    DriveBetweenRest = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Amount of driving time allowed after the DayDriveEnd time is reached.'
##        #return pVal
##    def _set(self, pVal):
##        u'Amount of driving time allowed after the DayDriveEnd time is reached.'
##    DriveFlexibility = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Time from midnight when driving must stop every day.'
##        #return pVal
##    def _set(self, pVal):
##        u'Time from midnight when driving must stop every day.'
##    DayDriveEnd = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Time from midnight when driving must start every day.'
##        #return pVal
##    def _set(self, pVal):
##        u'Time from midnight when driving must start every day.'
##    DayDriveStart = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The start date of the trip.'
##        #return pVal
##    def _set(self, pVal):
##        u'The start date of the trip.'
##    TripStart = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The duration of rest breaks in minutes.'
##        #return pVal
##    def _set(self, pVal):
##        u'The duration of rest breaks in minutes.'
##    RestDuration = property(_get, _set, doc = _set.__doc__)
##

IDECoverageFeatureClass._methods_ = [
    COMMETHOD(['propget', helpstring(u'The coverage feature class type.')], HRESULT, 'FeatureClassType',
              ( ['retval', 'out'], POINTER(esriCoverageFeatureClassType), 'FeatureClassType' )),
    COMMETHOD(['propput', helpstring(u'The coverage feature class type.')], HRESULT, 'FeatureClassType',
              ( ['in'], esriCoverageFeatureClassType, 'FeatureClassType' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the coverage feature class have attributes.')], HRESULT, 'HasFAT',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'HasFAT' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the coverage feature class have attributes.')], HRESULT, 'HasFAT',
              ( ['in'], VARIANT_BOOL, 'HasFAT' )),
    COMMETHOD(['propget', helpstring(u'Coverage feature class topology status.')], HRESULT, 'Topology',
              ( ['retval', 'out'], POINTER(esriFeatureClassTopology), 'pTopology' )),
    COMMETHOD(['propput', helpstring(u'Coverage feature class topology status.')], HRESULT, 'Topology',
              ( ['in'], esriFeatureClassTopology, 'pTopology' )),
]
################################################################
## code template for IDECoverageFeatureClass implementation
##class IDECoverageFeatureClass_Impl(object):
##    def _get(self):
##        u'The coverage feature class type.'
##        #return FeatureClassType
##    def _set(self, FeatureClassType):
##        u'The coverage feature class type.'
##    FeatureClassType = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the coverage feature class have attributes.'
##        #return HasFAT
##    def _set(self, HasFAT):
##        u'Indicates if the coverage feature class have attributes.'
##    HasFAT = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Coverage feature class topology status.'
##        #return pTopology
##    def _set(self, pTopology):
##        u'Coverage feature class topology status.'
##    Topology = property(_get, _set, doc = _set.__doc__)
##


# values for enumeration 'esriSMAzimuthType'
esriSMAzimuthN = 1
esriSMAzimuthNE = 2
esriSMAzimuthE = 3
esriSMAzimuthSE = 4
esriSMAzimuthS = 5
esriSMAzimuthSW = 6
esriSMAzimuthW = 7
esriSMAzimuthNW = 8
esriSMAzimuthUnknown = 9
esriSMAzimuthType = c_int # enum
class DETextFile(CoClass):
    u'Text File Data Element object.'
    _reg_clsid_ = GUID('{E98D0766-C13E-45CA-BA78-1DEF8B60CAB2}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
DETextFile._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDETextFile, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDETable, IDEFile, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEDataset, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElement, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPValue, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDescribe]

IDEDbaseTable._methods_ = [
]
################################################################
## code template for IDEDbaseTable implementation
##class IDEDbaseTable_Impl(object):

IGPArcInfoItem._methods_ = [
    COMMETHOD(['propget', helpstring(u'The name of the info item.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propput', helpstring(u'The name of the info item.')], HRESULT, 'Name',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD(['propget', helpstring(u'The start position of the info item.')], HRESULT, 'StartPosition',
              ( ['retval', 'out'], POINTER(c_int), 'Position' )),
    COMMETHOD(['propput', helpstring(u'The start position of the info item.')], HRESULT, 'StartPosition',
              ( ['in'], c_int, 'Position' )),
    COMMETHOD(['propget', helpstring(u'The width of the info item.')], HRESULT, 'Width',
              ( ['retval', 'out'], POINTER(c_int), 'Width' )),
    COMMETHOD(['propput', helpstring(u'The width of the info item.')], HRESULT, 'Width',
              ( ['in'], c_int, 'Width' )),
    COMMETHOD(['propget', helpstring(u'The output width of the info item.')], HRESULT, 'OutputWidth',
              ( ['retval', 'out'], POINTER(c_int), 'Width' )),
    COMMETHOD(['propput', helpstring(u'The output width of the info item.')], HRESULT, 'OutputWidth',
              ( ['in'], c_int, 'Width' )),
    COMMETHOD(['propget', helpstring(u'The type of the info item.')], HRESULT, 'Type',
              ( ['retval', 'out'], POINTER(esriArcInfoItemType), 'Type' )),
    COMMETHOD(['propput', helpstring(u'The type of the info item.')], HRESULT, 'Type',
              ( ['in'], esriArcInfoItemType, 'Type' )),
    COMMETHOD(['propget', helpstring(u'The number of decimal places of the info item.')], HRESULT, 'NumberDecimals',
              ( ['retval', 'out'], POINTER(c_int), 'number' )),
    COMMETHOD(['propput', helpstring(u'The number of decimal places of the info item.')], HRESULT, 'NumberDecimals',
              ( ['in'], c_int, 'number' )),
    COMMETHOD(['propget', helpstring(u'The alternate name of the info item.')], HRESULT, 'AlternateName',
              ( ['retval', 'out'], POINTER(BSTR), 'AlternateName' )),
    COMMETHOD(['propput', helpstring(u'The alternate name of the info item.')], HRESULT, 'AlternateName',
              ( ['in'], BSTR, 'AlternateName' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the info item redefined.')], HRESULT, 'IsRedefined',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'redefined' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the info item redefined.')], HRESULT, 'IsRedefined',
              ( ['in'], VARIANT_BOOL, 'redefined' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the info item has an index.')], HRESULT, 'IsIndexed',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsIndexed' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the info item has an index.')], HRESULT, 'IsIndexed',
              ( ['in'], VARIANT_BOOL, 'IsIndexed' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the item a psuedo item.')], HRESULT, 'IsPseudo',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'isPsuedo' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the item a psuedo item.')], HRESULT, 'IsPseudo',
              ( ['in'], VARIANT_BOOL, 'isPsuedo' )),
]
################################################################
## code template for IGPArcInfoItem implementation
##class IGPArcInfoItem_Impl(object):
##    def _get(self):
##        u'The name of the info item.'
##        #return Name
##    def _set(self, Name):
##        u'The name of the info item.'
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The output width of the info item.'
##        #return Width
##    def _set(self, Width):
##        u'The output width of the info item.'
##    OutputWidth = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The start position of the info item.'
##        #return Position
##    def _set(self, Position):
##        u'The start position of the info item.'
##    StartPosition = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the item a psuedo item.'
##        #return isPsuedo
##    def _set(self, isPsuedo):
##        u'Indicates if the item a psuedo item.'
##    IsPseudo = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the info item has an index.'
##        #return IsIndexed
##    def _set(self, IsIndexed):
##        u'Indicates if the info item has an index.'
##    IsIndexed = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The width of the info item.'
##        #return Width
##    def _set(self, Width):
##        u'The width of the info item.'
##    Width = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the info item redefined.'
##        #return redefined
##    def _set(self, redefined):
##        u'Indicates if the info item redefined.'
##    IsRedefined = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The alternate name of the info item.'
##        #return AlternateName
##    def _set(self, AlternateName):
##        u'The alternate name of the info item.'
##    AlternateName = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The type of the info item.'
##        #return Type
##    def _set(self, Type):
##        u'The type of the info item.'
##    Type = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The number of decimal places of the info item.'
##        #return number
##    def _set(self, number):
##        u'The number of decimal places of the info item.'
##    NumberDecimals = property(_get, _set, doc = _set.__doc__)
##

ISMNetBarriersCollection._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Adds a barrier to the collection.')], HRESULT, 'Add',
              ( ['in'], POINTER(ISMNetBarrier), 'pItem' )),
    COMMETHOD([dispid(2), helpstring(u'Removes a barrier with a specified ID from the collection.')], HRESULT, 'Remove',
              ( ['in'], c_int, 'lID' )),
    COMMETHOD([dispid(3), helpstring(u'Removes all barriers from the collection.')], HRESULT, 'Clear'),
]
################################################################
## code template for ISMNetBarriersCollection implementation
##class ISMNetBarriersCollection_Impl(object):
##    def Add(self, pItem):
##        u'Adds a barrier to the collection.'
##        #return 
##
##    def Clear(self):
##        u'Removes all barriers from the collection.'
##        #return 
##
##    def Remove(self, lID):
##        u'Removes a barrier with a specified ID from the collection.'
##        #return 
##


# values for enumeration 'esriSMDirItemType'
esriSMDirItemNewRoad = 1
esriSMDirItemBypass = 2
esriSMDirItemBorder = 3
esriSMDirItemEndOfDay = 4
esriSMDirItemDayNumber = 5
esriSMDirItemRestBreak = 6
esriSMDirItemDepart = 7
esriSMDirItemArrive = 8
esriSMDirItemType = c_int # enum

# values for enumeration 'esriSMNetAttributeUsageType'
esriSMNAUTCost = 1
esriSMNAUTDescription = 2
esriSMNAUTRestrictionBoolean = 3
esriSMNAUTRestrictionMinAllowed = 4
esriSMNAUTRestrictionMaxAllowed = 5
esriSMNetAttributeUsageType = c_int # enum
ISMNetAttribute2._methods_ = [
    COMMETHOD([dispid(3), helpstring(u'The network attribute usage type. Returns an esriSMNetAttributeUsageType constant.'), 'propget'], HRESULT, 'UsageType',
              ( ['retval', 'out'], POINTER(esriSMNetAttributeUsageType), 'pVal' )),
]
################################################################
## code template for ISMNetAttribute2 implementation
##class ISMNetAttribute2_Impl(object):
##    @property
##    def UsageType(self):
##        u'The network attribute usage type. Returns an esriSMNetAttributeUsageType constant.'
##        #return pVal
##

ISMFlag._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Flag ID.'), 'propget'], HRESULT, 'ObjectID',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(1), helpstring(u'Flag ID.'), 'propput'], HRESULT, 'ObjectID',
              ( ['in'], c_int, 'pVal' )),
    COMMETHOD([dispid(2), helpstring(u'Flag position along the street segment as a percent of the segment length.'), 'propget'], HRESULT, 'PercentAlong',
              ( ['retval', 'out'], POINTER(c_float), 'pVal' )),
    COMMETHOD([dispid(2), helpstring(u'Flag position along the street segment as a percent of the segment length.'), 'propput'], HRESULT, 'PercentAlong',
              ( ['in'], c_float, 'pVal' )),
    COMMETHOD([dispid(3), helpstring(u'The side of the street that the flag is on. Returns an esriSMStreetSideType constant.'), 'propget'], HRESULT, 'Side',
              ( ['retval', 'out'], POINTER(esriSMStreetSideType), 'pVal' )),
    COMMETHOD([dispid(3), helpstring(u'The side of the street that the flag is on. Returns an esriSMStreetSideType constant.'), 'propput'], HRESULT, 'Side',
              ( ['in'], esriSMStreetSideType, 'pVal' )),
    COMMETHOD([dispid(4), helpstring(u'The geographic location of the flag.'), 'propget'], HRESULT, 'StreetPoint',
              ( ['retval', 'out'], POINTER(POINTER(ISMRouterPoint)), 'pVal' )),
    COMMETHOD([dispid(4), helpstring(u'The geographic location of the flag.'), 'propput'], HRESULT, 'StreetPoint',
              ( ['in'], POINTER(ISMRouterPoint), 'pVal' )),
]
################################################################
## code template for ISMFlag implementation
##class ISMFlag_Impl(object):
##    def _get(self):
##        u'The geographic location of the flag.'
##        #return pVal
##    def _set(self, pVal):
##        u'The geographic location of the flag.'
##    StreetPoint = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Flag position along the street segment as a percent of the segment length.'
##        #return pVal
##    def _set(self, pVal):
##        u'Flag position along the street segment as a percent of the segment length.'
##    PercentAlong = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Flag ID.'
##        #return pVal
##    def _set(self, pVal):
##        u'Flag ID.'
##    ObjectID = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The side of the street that the flag is on. Returns an esriSMStreetSideType constant.'
##        #return pVal
##    def _set(self, pVal):
##        u'The side of the street that the flag is on. Returns an esriSMStreetSideType constant.'
##    Side = property(_get, _set, doc = _set.__doc__)
##

IDELasDataset._methods_ = [
    COMMETHOD(['propget', helpstring(u'The number of files in the LAS dataset.')], HRESULT, 'FileCount',
              ( ['retval', 'out'], POINTER(c_int), 'pFileCount' )),
    COMMETHOD(['propput', helpstring(u'The number of files in the LAS dataset.')], HRESULT, 'FileCount',
              ( ['in'], c_int, 'pFileCount' )),
    COMMETHOD(['propget', helpstring(u'The number of points in the LAS dataset.')], HRESULT, 'PointCount',
              ( ['retval', 'out'], POINTER(c_int), 'pPointCount' )),
    COMMETHOD(['propput', helpstring(u'The number of points in the LAS dataset.')], HRESULT, 'PointCount',
              ( ['in'], c_int, 'pPointCount' )),
    COMMETHOD(['propget', helpstring(u'The number of surface constraint feature classes in the LAS dataset.')], HRESULT, 'SurfaceConstraintCount',
              ( ['retval', 'out'], POINTER(c_int), 'pSurfaceConstraintCount' )),
    COMMETHOD(['propput', helpstring(u'The number of surface constraint feature classes in the LAS dataset.')], HRESULT, 'SurfaceConstraintCount',
              ( ['in'], c_int, 'pSurfaceConstraintCount' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether there are statistics.')], HRESULT, 'HasStatistics',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbHasStatistics' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether there are statistics.')], HRESULT, 'HasStatistics',
              ( ['in'], VARIANT_BOOL, 'pbHasStatistics' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the statistics are up to date.')], HRESULT, 'NeedsUpdateStatistics',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbNeedsUpdateStatistics' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether the statistics are up to date.')], HRESULT, 'NeedsUpdateStatistics',
              ( ['in'], VARIANT_BOOL, 'pbNeedsUpdateStatistics' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the LAS dataset uses a relative path to its files.')], HRESULT, 'UsesRelativePath',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbUsesRelativePath' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether the LAS dataset uses a relative path to its files.')], HRESULT, 'UsesRelativePath',
              ( ['in'], VARIANT_BOOL, 'pbUsesRelativePath' )),
]
################################################################
## code template for IDELasDataset implementation
##class IDELasDataset_Impl(object):
##    def _get(self):
##        u'Indicates whether the LAS dataset uses a relative path to its files.'
##        #return pbUsesRelativePath
##    def _set(self, pbUsesRelativePath):
##        u'Indicates whether the LAS dataset uses a relative path to its files.'
##    UsesRelativePath = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether there are statistics.'
##        #return pbHasStatistics
##    def _set(self, pbHasStatistics):
##        u'Indicates whether there are statistics.'
##    HasStatistics = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The number of points in the LAS dataset.'
##        #return pPointCount
##    def _set(self, pPointCount):
##        u'The number of points in the LAS dataset.'
##    PointCount = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether the statistics are up to date.'
##        #return pbNeedsUpdateStatistics
##    def _set(self, pbNeedsUpdateStatistics):
##        u'Indicates whether the statistics are up to date.'
##    NeedsUpdateStatistics = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The number of surface constraint feature classes in the LAS dataset.'
##        #return pSurfaceConstraintCount
##    def _set(self, pSurfaceConstraintCount):
##        u'The number of surface constraint feature classes in the LAS dataset.'
##    SurfaceConstraintCount = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The number of files in the LAS dataset.'
##        #return pFileCount
##    def _set(self, pFileCount):
##        u'The number of files in the LAS dataset.'
##    FileCount = property(_get, _set, doc = _set.__doc__)
##

class LicensedDataExtension(CoClass):
    u'The Licensed Data Extension.'
    _reg_clsid_ = GUID('{39BC41A4-B140-4F7B-B1C9-ACCD507EE339}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
LicensedDataExtension._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IAutoExtension, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IExtension, IDataLicenseManager]

class DEVPFCoverageType(CoClass):
    u'DEVPFCoverage Dataset Data Element object Type.'
    _reg_clsid_ = GUID('{728BBF56-85FA-4598-9CE8-77FC8BA73127}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
DEVPFCoverageType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEFeatureDatasetType, IDEVPFCoverageType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEGeoDatasetType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEDatasetType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGxFilterInfo, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElementType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDataType, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone]

class ICadDrawingWorkspace(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Cad Drawing Workspace.'
    _iid_ = GUID('{76B47B11-AC32-11D4-A226-444553547777}')
    _idlflags_ = ['oleautomation']
ICadDrawingWorkspace._methods_ = [
    COMMETHOD([helpstring(u'Open a Cad Drawing Dataset.')], HRESULT, 'OpenCadDrawingDataset',
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(POINTER(ICadDrawingDataset)), 'dataset' )),
]
################################################################
## code template for ICadDrawingWorkspace implementation
##class ICadDrawingWorkspace_Impl(object):
##    def OpenCadDrawingDataset(self, Name):
##        u'Open a Cad Drawing Dataset.'
##        #return dataset
##

ISMNetAttributesCollection._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'The number of attributes in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(2), helpstring(u'The network attribute at a specified index in the collection.'), 'propget'], HRESULT, 'Item',
              ( ['in'], c_int, 'Position' ),
              ( ['retval', 'out'], POINTER(POINTER(ISMNetAttribute)), 'pVal' )),
]
################################################################
## code template for ISMNetAttributesCollection implementation
##class ISMNetAttributesCollection_Impl(object):
##    @property
##    def Count(self):
##        u'The number of attributes in the collection.'
##        #return pVal
##
##    @property
##    def Item(self, Position):
##        u'The network attribute at a specified index in the collection.'
##        #return pVal
##

IDEMapDocument._methods_ = [
]
################################################################
## code template for IDEMapDocument implementation
##class IDEMapDocument_Impl(object):

ISMRoadPreferences._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'The preference value for the specified road type.'), 'propget'], HRESULT, 'Item',
              ( ['in'], esriSMRoadType, 'RoadType' ),
              ( ['retval', 'out'], POINTER(c_short), 'pVal' )),
    COMMETHOD([dispid(1), helpstring(u'The preference value for the specified road type.'), 'propput'], HRESULT, 'Item',
              ( ['in'], esriSMRoadType, 'RoadType' ),
              ( ['in'], c_short, 'pVal' )),
]
################################################################
## code template for ISMRoadPreferences implementation
##class ISMRoadPreferences_Impl(object):
##    def _get(self, RoadType):
##        u'The preference value for the specified road type.'
##        #return pVal
##    def _set(self, RoadType, pVal):
##        u'The preference value for the specified road type.'
##    Item = property(_get, _set, doc = _set.__doc__)
##

class DELasDatasetType(CoClass):
    u'LAS Dataset Data Element object Type.'
    _reg_clsid_ = GUID('{160BC182-CE75-4DAB-8ABF-8E6DC866C73B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
DELasDatasetType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDELasDatasetType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEGeoDatasetType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEDatasetType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElementType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGxFilterInfo, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDataType, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone]

class GeoRSSWorkspaceFactory(CoClass):
    u'GeoRSS workspace factory.'
    _reg_clsid_ = GUID('{894AF6A1-157A-47BA-BDEC-3CF98D4CCE74}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
GeoRSSWorkspaceFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IPlugInWorkspaceFactoryHelper, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceFactory, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceFactory2]

class TinWorkspaceFactory(CoClass):
    u'Esri TIN workspace factory is used to access TINs on disk.'
    _reg_clsid_ = GUID('{AD4E89D9-00A5-11D2-B1CA-00C04F8EDEFF}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
TinWorkspaceFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceFactory, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceFactory2]

class DEDbaseTable(CoClass):
    u'Dbase Table Data Element object.'
    _reg_clsid_ = GUID('{69E84176-FB98-4036-A8FF-E69C8E82F013}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
DEDbaseTable._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDEDbaseTable, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDETable, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEDataset, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElement, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPValue, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDescribe]

IDETin._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if TIN was constructed using Delaunay triangulation.')], HRESULT, 'IsDelaunay',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbIsDelaunay' )),
    COMMETHOD(['propput', helpstring(u'Indicates if TIN was constructed using Delaunay triangulation.')], HRESULT, 'IsDelaunay',
              ( ['in'], VARIANT_BOOL, 'pbIsDelaunay' )),
    COMMETHOD(['propget', helpstring(u'Multiplication factor applied to all z values in a TIN to provide unit-congruency between coordinate components.')], HRESULT, 'ZFactor',
              ( ['retval', 'out'], POINTER(c_double), 'pFactor' )),
    COMMETHOD(['propput', helpstring(u'Multiplication factor applied to all z values in a TIN to provide unit-congruency between coordinate components.')], HRESULT, 'ZFactor',
              ( ['in'], c_double, 'pFactor' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the TIN dataset has node tag values.')], HRESULT, 'HasNodeTagValues',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbHasNodeValues' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the TIN dataset has node tag values.')], HRESULT, 'HasNodeTagValues',
              ( ['in'], VARIANT_BOOL, 'pbHasNodeValues' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the TIN dataset has edge tag values.')], HRESULT, 'HasEdgeTagValues',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbHasEdgeValues' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the TIN dataset has edge tag values.')], HRESULT, 'HasEdgeTagValues',
              ( ['in'], VARIANT_BOOL, 'pbHasEdgeValues' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the TIN dataset has triangle tag values.')], HRESULT, 'HasTriangleTagValues',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbHasTriangleValues' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the TIN dataset has triangle tag values.')], HRESULT, 'HasTriangleTagValues',
              ( ['in'], VARIANT_BOOL, 'pbHasTriangleValues' )),
    COMMETHOD(['propget', helpstring(u'The list of Fields.')], HRESULT, 'Fields',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFields)), 'ppFields' )),
    COMMETHOD(['propputref', helpstring(u'The list of Fields.')], HRESULT, 'Fields',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFields), 'ppFields' )),
]
################################################################
## code template for IDETin implementation
##class IDETin_Impl(object):
##    def _get(self):
##        u'Indicates if TIN was constructed using Delaunay triangulation.'
##        #return pbIsDelaunay
##    def _set(self, pbIsDelaunay):
##        u'Indicates if TIN was constructed using Delaunay triangulation.'
##    IsDelaunay = property(_get, _set, doc = _set.__doc__)
##
##    def Fields(self, ppFields):
##        u'The list of Fields.'
##        #return 
##
##    def _get(self):
##        u'Indicates if the TIN dataset has triangle tag values.'
##        #return pbHasTriangleValues
##    def _set(self, pbHasTriangleValues):
##        u'Indicates if the TIN dataset has triangle tag values.'
##    HasTriangleTagValues = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the TIN dataset has edge tag values.'
##        #return pbHasEdgeValues
##    def _set(self, pbHasEdgeValues):
##        u'Indicates if the TIN dataset has edge tag values.'
##    HasEdgeTagValues = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Multiplication factor applied to all z values in a TIN to provide unit-congruency between coordinate components.'
##        #return pFactor
##    def _set(self, pFactor):
##        u'Multiplication factor applied to all z values in a TIN to provide unit-congruency between coordinate components.'
##    ZFactor = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the TIN dataset has node tag values.'
##        #return pbHasNodeValues
##    def _set(self, pbHasNodeValues):
##        u'Indicates if the TIN dataset has node tag values.'
##    HasNodeTagValues = property(_get, _set, doc = _set.__doc__)
##

class DEPrjFile(CoClass):
    u'Projection File Data Element object.'
    _reg_clsid_ = GUID('{7E704BB0-CFBE-11D5-933D-0080C71A3226}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
DEPrjFile._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDEPrjFile, IDEFile, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElement, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPValue, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDescribe]

ISMStop._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Numeric identifier of the user defined route stop.'), 'propget'], HRESULT, 'StopID',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(1), helpstring(u'Numeric identifier of the user defined route stop.'), 'propput'], HRESULT, 'StopID',
              ( ['in'], c_int, 'pVal' )),
    COMMETHOD([dispid(2), helpstring(u'Descriptive text of the route stop used in driving directions.'), 'propget'], HRESULT, 'Description',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(2), helpstring(u'Descriptive text of the route stop used in driving directions.'), 'propput'], HRESULT, 'Description',
              ( ['in'], BSTR, 'pVal' )),
    COMMETHOD([dispid(3), helpstring(u'The SMFlag object of the stop that describes its geographic location.'), 'propget'], HRESULT, 'Flag',
              ( ['retval', 'out'], POINTER(POINTER(ISMFlag)), 'pVal' )),
    COMMETHOD([dispid(3), helpstring(u'The SMFlag object of the stop that describes its geographic location.'), 'propput'], HRESULT, 'Flag',
              ( ['in'], POINTER(ISMFlag), 'pVal' )),
    COMMETHOD([dispid(4), helpstring(u'Stop duration in minutes.'), 'propget'], HRESULT, 'Duration',
              ( ['retval', 'out'], POINTER(c_short), 'pVal' )),
    COMMETHOD([dispid(4), helpstring(u'Stop duration in minutes.'), 'propput'], HRESULT, 'Duration',
              ( ['in'], c_short, 'pVal' )),
    COMMETHOD([dispid(5), helpstring(u'Minimal allowed distance to turn.'), 'propget'], HRESULT, 'MinDistanceToTurn',
              ( ['retval', 'out'], POINTER(c_double), 'pdDist' )),
    COMMETHOD([dispid(5), helpstring(u'Minimal allowed distance to turn.'), 'propput'], HRESULT, 'MinDistanceToTurn',
              ( ['in'], c_double, 'pdDist' )),
    COMMETHOD([dispid(6), helpstring(u'Indicates whether shortest path is restricted when traveling to and from the given stop.'), 'propget'], HRESULT, 'EnforceSideOfStreet',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbESS' )),
    COMMETHOD([dispid(6), helpstring(u'Indicates whether shortest path is restricted when traveling to and from the given stop.'), 'propput'], HRESULT, 'EnforceSideOfStreet',
              ( ['in'], VARIANT_BOOL, 'pbESS' )),
]
################################################################
## code template for ISMStop implementation
##class ISMStop_Impl(object):
##    def _get(self):
##        u'Descriptive text of the route stop used in driving directions.'
##        #return pVal
##    def _set(self, pVal):
##        u'Descriptive text of the route stop used in driving directions.'
##    Description = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Minimal allowed distance to turn.'
##        #return pdDist
##    def _set(self, pdDist):
##        u'Minimal allowed distance to turn.'
##    MinDistanceToTurn = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Numeric identifier of the user defined route stop.'
##        #return pVal
##    def _set(self, pVal):
##        u'Numeric identifier of the user defined route stop.'
##    StopID = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The SMFlag object of the stop that describes its geographic location.'
##        #return pVal
##    def _set(self, pVal):
##        u'The SMFlag object of the stop that describes its geographic location.'
##    Flag = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether shortest path is restricted when traveling to and from the given stop.'
##        #return pbESS
##    def _set(self, pbESS):
##        u'Indicates whether shortest path is restricted when traveling to and from the given stop.'
##    EnforceSideOfStreet = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Stop duration in minutes.'
##        #return pVal
##    def _set(self, pVal):
##        u'Stop duration in minutes.'
##    Duration = property(_get, _set, doc = _set.__doc__)
##

class ICoverageFeatureClass2(ICoverageFeatureClass):
    _case_insensitive_ = True
    u'Provides access to members that retrieve ArcInfo Coverage Feature Class information.'
    _iid_ = GUID('{2DA3B82A-B02A-11D4-9F5A-00C04F79927C}')
    _idlflags_ = ['oleautomation']
ICoverageFeatureClass2._methods_ = [
    COMMETHOD([helpstring(u'Copies this Feature Class to another coverage using the specified name.')], HRESULT, 'Copy',
              ( ['in'], BSTR, 'copyName' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureDataset), 'copyFeatureDataset' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass)), 'copyFeatureClass' )),
]
################################################################
## code template for ICoverageFeatureClass2 implementation
##class ICoverageFeatureClass2_Impl(object):
##    def Copy(self, copyName, copyFeatureDataset):
##        u'Copies this Feature Class to another coverage using the specified name.'
##        #return copyFeatureClass
##

class ICoverage2(ICoverage):
    _case_insensitive_ = True
    u'Provides access to members that modifies ArcInfo Coverages.'
    _iid_ = GUID('{D1E706BC-6EEE-11D4-9F55-00C04F79927C}')
    _idlflags_ = ['oleautomation']
ICoverage2._methods_ = [
    COMMETHOD(['propput', helpstring(u'The BND file of the Coverage.')], HRESULT, 'Extent',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'rhs' )),
    COMMETHOD([helpstring(u'Refreshes the Extent and Spatial Reference properties.')], HRESULT, 'RefreshSpatialProperties'),
]
################################################################
## code template for ICoverage2 implementation
##class ICoverage2_Impl(object):
##    def RefreshSpatialProperties(self):
##        u'Refreshes the Extent and Spatial Reference properties.'
##        #return 
##
##    def _set(self, rhs):
##        u'The BND file of the Coverage.'
##    Extent = property(fset = _set, doc = _set.__doc__)
##

class SDCNetworkSource(CoClass):
    u'A container for describing a SDC network dataset source.'
    _reg_clsid_ = GUID('{5BE00C09-A03F-4A69-B678-985108A500D3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
SDCNetworkSource._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INetworkSource, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDescribe]

IDERemoteDatabaseFolder._methods_ = [
]
################################################################
## code template for IDERemoteDatabaseFolder implementation
##class IDERemoteDatabaseFolder_Impl(object):

ISMDirItem._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'A string describing the direction item.'), 'propget'], HRESULT, 'Text',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(2), helpstring(u'The length of the route part, in miles by default, corresponding to the direction item.'), 'propget'], HRESULT, 'Length',
              ( ['retval', 'out'], POINTER(c_double), 'pVal' )),
    COMMETHOD([dispid(3), helpstring(u'The driving time of the route part corresponding to the direction item.'), 'propget'], HRESULT, 'Time',
              ( ['retval', 'out'], POINTER(c_double), 'pVal' )),
    COMMETHOD([dispid(4), helpstring(u'Formatted text descrbing the length and time of the direction item.'), 'propget'], HRESULT, 'DriveText',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(5), helpstring(u'The type of direction item. Returns an esriSMDirItemType constant.'), 'propget'], HRESULT, 'ItemType',
              ( ['retval', 'out'], POINTER(esriSMDirItemType), 'pVal' )),
    COMMETHOD([dispid(6), helpstring(u'The route part number associated with a direction item.'), 'propget'], HRESULT, 'RoutePart',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(7), helpstring(u'A collection of points representing the shape of the direction item.'), 'propget'], HRESULT, 'Shape',
              ( ['retval', 'out'], POINTER(POINTER(ISMPointsCollection)), 'pVal' )),
    COMMETHOD([dispid(8), helpstring(u'The geographic extent of the direction item.'), 'propget'], HRESULT, 'BoundBox',
              ( ['retval', 'out'], POINTER(POINTER(ISMRouterEnvelope)), 'pVal' )),
    COMMETHOD([dispid(9), helpstring(u'The street name of the direction item.'), 'propget'], HRESULT, 'StreetName',
              ( ['retval', 'out'], POINTER(BSTR), 'pbstrStreetName' )),
    COMMETHOD([dispid(10), helpstring(u'The turn angle of the direction item.'), 'propget'], HRESULT, 'TurnAngle',
              ( ['retval', 'out'], POINTER(c_double), 'pdAngle' )),
    COMMETHOD([dispid(11), helpstring(u'The azimuth of the direction item. Returns an esriSMAzimuthType constant.'), 'propget'], HRESULT, 'Azimuth',
              ( ['retval', 'out'], POINTER(esriSMAzimuthType), 'pAzimuth' )),
]
################################################################
## code template for ISMDirItem implementation
##class ISMDirItem_Impl(object):
##    @property
##    def ItemType(self):
##        u'The type of direction item. Returns an esriSMDirItemType constant.'
##        #return pVal
##
##    @property
##    def Text(self):
##        u'A string describing the direction item.'
##        #return pVal
##
##    @property
##    def Azimuth(self):
##        u'The azimuth of the direction item. Returns an esriSMAzimuthType constant.'
##        #return pAzimuth
##
##    @property
##    def DriveText(self):
##        u'Formatted text descrbing the length and time of the direction item.'
##        #return pVal
##
##    @property
##    def RoutePart(self):
##        u'The route part number associated with a direction item.'
##        #return pVal
##
##    @property
##    def Length(self):
##        u'The length of the route part, in miles by default, corresponding to the direction item.'
##        #return pVal
##
##    @property
##    def BoundBox(self):
##        u'The geographic extent of the direction item.'
##        #return pVal
##
##    @property
##    def Time(self):
##        u'The driving time of the route part corresponding to the direction item.'
##        #return pVal
##
##    @property
##    def Shape(self):
##        u'A collection of points representing the shape of the direction item.'
##        #return pVal
##
##    @property
##    def TurnAngle(self):
##        u'The turn angle of the direction item.'
##        #return pdAngle
##
##    @property
##    def StreetName(self):
##        u'The street name of the direction item.'
##        #return pbstrStreetName
##

IDEArcInfoUtilities._methods_ = [
    COMMETHOD([helpstring(u'Assign coverage properties.')], HRESULT, 'AssignCoverageProperties',
              ( ['in'], POINTER(ICoverage), 'pCoverage' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElement), 'pDataElement' )),
    COMMETHOD([helpstring(u'Assign ArcInfo table properties.')], HRESULT, 'AssignArcInfoTableProperties',
              ( ['in'], POINTER(IArcInfoTable), 'pArcInfoTable' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElement), 'pDataElement' )),
    COMMETHOD([helpstring(u'Assign coverage feature class properties.')], HRESULT, 'AssignCoverageFeatureClassProperties',
              ( ['in'], POINTER(ICoverageFeatureClass), 'pCoverageFeatureClass' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElement), 'pDataElement' )),
    COMMETHOD([helpstring(u'Assign coverage feature class name properties.')], HRESULT, 'AssignCoverageFeatureClassNameProperties',
              ( ['in'], POINTER(ICoverageFeatureClassName), 'pCoverageFeatureClassName' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElement), 'pDataElement' )),
    COMMETHOD([helpstring(u'Make tolerances.')], HRESULT, 'MakeDETolerances',
              ( ['in'], POINTER(ICoverage), 'pCoverage' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'ppTolerances' )),
    COMMETHOD([helpstring(u'Make Items.')], HRESULT, 'MakeGPItems',
              ( ['in'], POINTER(IArcInfoItems), 'pItems' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IArray)), 'ppGPItems' )),
    COMMETHOD([helpstring(u'Make item.')], HRESULT, 'MakeGPItem',
              ( ['in'], POINTER(IArcInfoItem), 'pItem' ),
              ( ['retval', 'out'], POINTER(POINTER(IGPArcInfoItem)), 'ppGPItem' )),
    COMMETHOD([helpstring(u'Get coverage feature class type from string.')], HRESULT, 'GetCoverageFeatureClassTypeFromString',
              ( ['in'], BSTR, 'desc' ),
              ( ['retval', 'out'], POINTER(esriCoverageFeatureClassType), 'Type' )),
    COMMETHOD([helpstring(u'Get coverage feature class type description.')], HRESULT, 'GetCoverageFeatureClassTypeDescription',
              ( ['in'], esriCoverageFeatureClassType, 'Type' ),
              ( ['retval', 'out'], POINTER(BSTR), 'desc' )),
    COMMETHOD([helpstring(u'Get feature class topology from string.')], HRESULT, 'GetFeatureClassTopologyFromString',
              ( ['in'], BSTR, 'desc' ),
              ( ['retval', 'out'], POINTER(esriFeatureClassTopology), 'Type' )),
    COMMETHOD([helpstring(u'Get feature class topology description.')], HRESULT, 'GetFeatureClassTopologyDescription',
              ( ['in'], esriFeatureClassTopology, 'Type' ),
              ( ['retval', 'out'], POINTER(BSTR), 'desc' )),
    COMMETHOD([helpstring(u'Get item type from string.')], HRESULT, 'GetItemTypeFromString',
              ( ['in'], BSTR, 'desc' ),
              ( ['retval', 'out'], POINTER(esriArcInfoItemType), 'Type' )),
    COMMETHOD([helpstring(u'Get item type description.')], HRESULT, 'GetItemTypeDescription',
              ( ['in'], esriArcInfoItemType, 'Type' ),
              ( ['retval', 'out'], POINTER(BSTR), 'desc' )),
    COMMETHOD([helpstring(u'Item exists.')], HRESULT, 'ItemExists',
              ( ['in'], POINTER(IDEArcInfoTable), 'pDEArcInfoTable' ),
              ( ['in'], POINTER(IGPArcInfoItem), 'pGPItem' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pExists' )),
    COMMETHOD([helpstring(u'FindItem.')], HRESULT, 'FindItem',
              ( ['in'], POINTER(IDEArcInfoTable), 'pDEArcInfoTable' ),
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(POINTER(IGPArcInfoItem)), 'ppGPItem' )),
]
################################################################
## code template for IDEArcInfoUtilities implementation
##class IDEArcInfoUtilities_Impl(object):
##    def AssignCoverageFeatureClassProperties(self, pCoverageFeatureClass, pDataElement):
##        u'Assign coverage feature class properties.'
##        #return 
##
##    def GetItemTypeDescription(self, Type):
##        u'Get item type description.'
##        #return desc
##
##    def GetItemTypeFromString(self, desc):
##        u'Get item type from string.'
##        #return Type
##
##    def GetCoverageFeatureClassTypeFromString(self, desc):
##        u'Get coverage feature class type from string.'
##        #return Type
##
##    def GetCoverageFeatureClassTypeDescription(self, Type):
##        u'Get coverage feature class type description.'
##        #return desc
##
##    def MakeGPItems(self, pItems):
##        u'Make Items.'
##        #return ppGPItems
##
##    def AssignArcInfoTableProperties(self, pArcInfoTable, pDataElement):
##        u'Assign ArcInfo table properties.'
##        #return 
##
##    def GetFeatureClassTopologyFromString(self, desc):
##        u'Get feature class topology from string.'
##        #return Type
##
##    def MakeDETolerances(self, pCoverage):
##        u'Make tolerances.'
##        #return ppTolerances
##
##    def GetFeatureClassTopologyDescription(self, Type):
##        u'Get feature class topology description.'
##        #return desc
##
##    def MakeGPItem(self, pItem):
##        u'Make item.'
##        #return ppGPItem
##
##    def AssignCoverageFeatureClassNameProperties(self, pCoverageFeatureClassName, pDataElement):
##        u'Assign coverage feature class name properties.'
##        #return 
##
##    def AssignCoverageProperties(self, pCoverage, pDataElement):
##        u'Assign coverage properties.'
##        #return 
##
##    def FindItem(self, pDEArcInfoTable, Name):
##        u'FindItem.'
##        #return ppGPItem
##
##    def ItemExists(self, pDEArcInfoTable, pGPItem):
##        u'Item exists.'
##        #return pExists
##

class GPArcInfoItemType(CoClass):
    u'ArcInfo Item Data Element object Type.'
    _reg_clsid_ = GUID('{5356DADD-53E4-4E70-99C9-996CDD224E25}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{1CE6AC65-43F5-4529-8FC0-D7ED298E4F1A}', 10, 2)
GPArcInfoItemType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGPArcInfoItemType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDataType, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPChoiceList]

__all__ = ['esriCTTNodeMatch', 'esriSMNAUTRestrictionMaxAllowed',
           'DELasDatasetType', 'esriSMRoadType', 'esriItemTypeOID',
           'ISMNetBarriersCollection', 'DEArcInfoTable',
           'IDECoverage', 'esriItemTypeGeometry', 'IDELasDatasetType',
           'DEVPFCoverage', 'DEFolderType', 'ISMSpeedGroup',
           'ISMDirItem', 'IDEArcInfoTable', 'IArcInfoItems',
           'DEArcInfoTableType', 'esriAnnotationCoverage',
           'esriCTTFuzzy', 'esriCFCTFile', 'esriFCTPreliminary',
           'DEFile', 'ISMStopsCollection', 'IArcInfoWorkspace',
           'SMRouter', 'CoverageName', 'DEDiskConnection',
           'ArcInfoItem', 'ISMRouterSetup', 'ISMNetAttribute2',
           'DEFolder', 'IDESpatialReferencesFolderType',
           'esriItemTypeNumber', 'esriCFCTPolygon',
           'esriSMNetAttrBoolean', 'PCCoverageWorkspaceFactory',
           'CadDrawingName', 'IGPArcInfoItemType', 'IDECoverageType',
           'ISMSpeedGroups', 'ISMRoutingMetaData',
           'esriItemTypeInteger', 'esriPointCoverage',
           'IDataLicenseManager', 'DEVPFTable', 'esriCTTEdit',
           'DEDiskConnectionType', 'esriSMNAUTRestrictionBoolean',
           'IArcInfoTable', 'IDEDbaseTableType', 'esriSMDLUFeet',
           'SMRestriction', 'IArcInfoWorkspaceUtil',
           'esriItemTypeFloat', 'esriItemTypeDate',
           'esriItemTypeBlob', 'esriSMDirItemType', 'esriCTTGrain',
           'DEPrjFileType', 'ISMBreakTracker',
           'esriCoverageToleranceType', 'IDEVPFCoverageType',
           'SMTripPlanSettings', 'IDEArcInfoTableType', 'DETin',
           'SMStopsCollection', 'IDELayer', 'esriSMDLUMiles',
           'ISMRouterPoint', 'esriSMRestrictionType',
           'esriArcInfoItemType', 'DEArcInfoUtilities', 'SMStop',
           'IDEShapeFile', 'esriCTTTicMatch', 'DECatalogRoot',
           'esriCTTSnap', 'IUsageModeOption', 'esriSMDirItemEndOfDay',
           'esriCFCTArc', 'ISdcExporter', 'ISMStop',
           'esriSMAzimuthNE', 'esriSMDLUYards',
           'esriItemTypeZeroFill', 'DECoverageType',
           'esriCTTNodeSnap', 'esriSMAzimuthNW', 'SMPointsCollection',
           'SMDirItem', 'esriSMNAUTCost', 'IArcInfoItem',
           'esriSMNetAttributeType', 'esriItemTypePacked',
           'DECadDrawingDatasetType', 'SDCWorkspaceFactory',
           'IDESpatialReferencesFolder', 'DERemoteDatabaseFolderType',
           'IGPLayer', 'IDETextFileType', 'IUsageModeInfo',
           'IDEVPFTable', 'DETextFileType', 'SMNetAttribute',
           'SdcExporter', 'esriCFCTLink',
           'DECoverageFeatureClassType', 'SMRoadPreferences',
           'esriCoveragePrecisionSingle', 'IDETinType',
           'ISMRestriction', 'esriPolygonCoverage',
           'ISMNetAttributesAccess', 'IDEVPFTableType',
           'DEDbaseTableType', 'ISMFlagCreator2',
           'ICadDrawingDataset', 'DECatalogRootType',
           'SMRouterEnvelope', 'ArcInfoItems', 'esriSMDirItemBypass',
           'IDataLicenseInfo', 'DECoverage',
           'esriCadTransformByPoints', 'IDECadDrawingDataset',
           'IDECatalogRootType', 'esriSMDirectionsLengthUnits',
           'DEMapDocumentType', 'esriEmptyCoverage',
           'esriSMDirItemRestBreak', 'DEShapeFileType',
           'ISMNetAttributesCollection', 'esriSMDirItemBorder',
           'SMNetAttributesAccess', 'esriSMNetAttrShape',
           'DECoverageFeatureClass', 'esriSMNAUTDescription',
           'esriItemTypeLeadFill', 'esriCFCTPoint',
           'SDCNetworkAttribute', 'IDEMapDocumentType',
           'esriSMNetAttributeUsageType', 'esriFCTNotApplicable',
           'DEFileType', 'IArcInfoItemsEdit', 'esriItemTypeBinary',
           'ISMRouterEnvelope', 'ICadDrawingWorkspace',
           'IDECatalogRoot', 'ICoverageFeatureClass2', 'IDEFile',
           'IArcInfoItemEdit', 'esriSMRoadTypeHighways',
           'IDEFolderType', 'SMNetBarriersCollection',
           'DEVPFCoverageType', 'ISMNetBarrier', 'esriSMAzimuthType',
           'esriCFCTRoute', 'esriSMStreetSideType',
           'GeoRSSWorkspaceFactory', 'SDCNetworkSource',
           'esriSMDirItemNewRoad', 'esriCoveragePrecisionDouble',
           'ICoverageFeatureClass', 'esriSMAzimuthN',
           'VpfWorkspaceFactory', 'IDEArcInfoUtilities',
           'esriSMBTPAllow', 'esriCoveragePrecisionType',
           'GPArcInfoItemType', 'esriSMBTPDeadend', 'esriSMRTRelaxed',
           'esriFCTUnknown', 'ISMRouter', 'IDETextFile', 'IDETin',
           'esriCadTransformByRst', 'IArcInfoTable2', 'DETextFile',
           'esriSMAzimuthUnknown', 'IDECoverageFeatureClassType',
           'esriSMAzimuthW', 'esriSMAzimuthS', 'ICoverage2',
           'esriCFCTNode', 'esriDataLicenseType',
           'TinWorkspaceFactory', 'IDEVPFCoverage',
           'LicensedDataExtension', 'esriFeatureClassTopology',
           'ISMDirections', 'SMFlag', 'IDEDbaseTable', 'DELasDataset',
           'esriSMStreetSideUndefined', 'esriSMNetAttrDouble',
           'IDECadDrawingDatasetType', 'esriCTTWeed', 'GPArcInfoItem',
           'DESpatialReferencesFolderType', 'esriSMNetAttrString',
           'esriSMDLUMeters', 'SMRouterPoint', 'ICadDrawingLayers',
           'esriCoverageType', 'SMNetBarrier', 'esriSMDirItemDepart',
           'esriSMBTPDisable', 'esriCoverageFeatureClassType',
           'IDEPrjFile', 'esriItemTypeOverpunch',
           'StreetMapWorkspaceFactory', 'esriSMDirItemDayNumber',
           'esriCFCTSection', 'DECadDrawingDataset',
           'ArcInfoWorkspaceFactory', 'ICoverageFeatureClassName',
           'esriSMStreetSideRight', 'DEDbaseTable', 'ISMSpeedGroup2',
           'DELayer', 'esriCadTransform', 'ICadTransformations',
           'esriSMDirItemArrive', 'IDEMapDocument', 'IDEPrjFileType',
           'esriCFCTTic', 'ISMRouterSetup2', 'esriFCTExists',
           'esriDataLicSeatType', 'esriSMRoadTypeFerries',
           'IGPLayerType', 'esriSMBacktrackPolicy',
           'esriCadTransformByWorldFile', 'DETinType', 'DEPrjFile',
           'ISMRoadPreferences', 'IDEDiskConnectionType',
           'ISMFlagCreator', 'CadWorkspaceFactory',
           'ShapefileWorkspaceFactory', 'IDELasDataset',
           'SMNetAttributesCollection', 'esriCFCTLabel',
           'esriDataLicFloatType', 'esriItemTypeCharacter',
           'esriCFCTRegion', 'ISMRouterFactory', 'DEShapeFile',
           'IDERemoteDatabaseFolderType', 'esriLineCoverage',
           'DEVPFTableType', 'SMSpeedGroup', 'esriSMStreetSideLeft',
           'esriSMNetAttrInteger', 'IDERemoteDatabaseFolder',
           'SMDirections', 'DESpatialReferencesFolder',
           'IDEShapeFileType', 'esriSMNetAttrFloat', 'SMFlagCreator',
           'IInfoTableOnlyWorkspaceEdit', 'esriSMAzimuthSW',
           'IMetaInfo', 'ICadSettings', 'esriItemTypeTrailingSign',
           'esriPreliminaryPolygonCoverage', 'SMSpeedGroups',
           'IDEDiskConnection', 'ISMPointsCollection',
           'ISMNetAttribute', 'ICoverageName', 'esriCFCTAnnotation',
           'esriCTTGeneralize', 'esriSMAzimuthSE', 'IDELayerType',
           'ICoverage', 'CoverageFeatureClassName', 'DELayerType',
           'IDEFileType', 'SMRouterFactory', 'IGPArcInfoItem',
           'DEMapDocument', 'esriSMRTStrict', 'ISMFlag',
           'esriSMNAUTRestrictionMinAllowed',
           'DERemoteDatabaseFolder', 'esriSMAzimuthE',
           'esriCTTDangle', 'IDECoverageFeatureClass',
           'ISMTripPlanSettings', 'esriSMDLUKilometers', 'IDEFolder']
from comtypes import _check_version; _check_version('501')

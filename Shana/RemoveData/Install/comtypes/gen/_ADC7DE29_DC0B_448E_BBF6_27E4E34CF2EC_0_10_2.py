# -*- coding: mbcs -*-
typelib_path = u'C:\\Program Files (x86)\\ArcGIS\\Desktop10.2\\com\\esriCatalog.olb'
_lcid = 0 # change this if required
from ctypes import *
from comtypes import GUID
from comtypes import CoClass
import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0
import comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2
from comtypes import BSTR
from ctypes import HRESULT
from comtypes import helpstring
from comtypes import COMMETHOD
from comtypes import dispid
import comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2
from comtypes.automation import VARIANT
from comtypes.automation import VARIANT
from ctypes.wintypes import VARIANT_BOOL
import comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2
import comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2
import comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2
import comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2
from comtypes import IUnknown
import comtypes.gen._18F2FC71_6B30_45B9_B101_037A8B868B66_0_10_2
import comtypes.gen._C031A050_82C6_4F8F_8836_5692631CFFE6_0_10_2
import comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2


class GxFilterNetworkDatasets(CoClass):
    u'A filter for displaying/choosing network datasets.'
    _reg_clsid_ = GUID('{2A663A7F-A5D5-4FBF-9D0F-A7494793EDFC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxObjectFilter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that defines a GxObject filter.'
    _iid_ = GUID('{9E14BC46-19F4-11D3-9F55-00C04F6BC69E}')
    _idlflags_ = ['oleautomation']
GxFilterNetworkDatasets._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class IGxFolderAdmin(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that help find child GX folder.'
    _iid_ = GUID('{C3670290-3CEB-4438-8D81-644BE88E9249}')
    _idlflags_ = ['oleautomation']
class IGxObject(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that are common to all GxObjects.'
    _iid_ = GUID('{BDBBB3EB-D0B2-11D1-AED9-080009EC734B}')
    _idlflags_ = ['oleautomation']
IGxFolderAdmin._methods_ = [
    COMMETHOD([helpstring(u'Find a child folder.')], HRESULT, 'FindChildFolder',
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(POINTER(IGxObject)), 'child' )),
]
################################################################
## code template for IGxFolderAdmin implementation
##class IGxFolderAdmin_Impl(object):
##    def FindChildFolder(self, Name):
##        u'Find a child folder.'
##        #return child
##

class GxFilterTopologies(CoClass):
    u'A filter for displaying/choosing topologies.'
    _reg_clsid_ = GUID('{E9F5D571-12DC-47AE-9048-6666D8C95014}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterTopologies._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class IGxAGSFolder(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{7274CD39-52AD-4256-B799-4FA053361684}')
    _idlflags_ = ['oleautomation']
IGxAGSFolder._methods_ = [
    COMMETHOD(['propput', helpstring(u'The AGS folder name.')], HRESULT, 'Name',
              ( ['in'], BSTR, 'rhs' )),
    COMMETHOD(['propputref', helpstring(u'The AGS server connection.')], HRESULT, 'AGSServerConnection',
              ( ['in'], POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IAGSServerConnection), 'conn' )),
    COMMETHOD(['propget', helpstring(u'The AGS server connection.')], HRESULT, 'AGSServerConnection',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IAGSServerConnection)), 'conn' )),
    COMMETHOD(['propget', helpstring(u'The AGS server connection name.')], HRESULT, 'AGSServerConnectionName',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IAGSServerConnectionName)), 'connName' )),
    COMMETHOD(['propputref', helpstring(u'The AGS server connection name.')], HRESULT, 'AGSServerConnectionName',
              ( ['in'], POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IAGSServerConnectionName), 'connName' )),
    COMMETHOD([helpstring(u'Edit the folder properties.')], HRESULT, 'EditFolderProperties',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hParent' )),
    COMMETHOD(['propget', helpstring(u'The selected server objects.')], HRESULT, 'SelectedServerObjects',
              ( ['retval', 'out'], POINTER(VARIANT), 'SelectedObjects' )),
    COMMETHOD(['propput', helpstring(u'The selected server objects.')], HRESULT, 'SelectedServerObjects',
              ( ['in'], VARIANT, 'SelectedObjects' )),
]
################################################################
## code template for IGxAGSFolder implementation
##class IGxAGSFolder_Impl(object):
##    def AGSServerConnectionName(self, connName):
##        u'The AGS server connection name.'
##        #return 
##
##    @property
##    def AGSServerConnection(self, conn):
##        u'The AGS server connection.'
##        #return 
##
##    def EditFolderProperties(self, hParent):
##        u'Edit the folder properties.'
##        #return 
##
##    def _set(self, rhs):
##        u'The AGS folder name.'
##    Name = property(fset = _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The selected server objects.'
##        #return SelectedObjects
##    def _set(self, SelectedObjects):
##        u'The selected server objects.'
##    SelectedServerObjects = property(_get, _set, doc = _set.__doc__)
##


# values for enumeration 'esriGxPackageType'
esriGxPackageTypeMap = 0
esriGxPackageTypeLayer = 1
esriGxPackageTypeGeoprocessing = 2
esriGxPackageTypeLocator = 3
esriGxPackageTypeTile = 4
esriGxPackageType = c_int # enum

# values for enumeration 'esriDoubleClickResult'
esriDCRDefault = 0
esriDCRChooseAndDismiss = 1
esriDCRShowChildren = 2
esriDCRNothing = 100
esriDoubleClickResult = c_int # enum
IGxObjectFilter._methods_ = [
    COMMETHOD(['propget', helpstring(u'A user-friendly name identifying this filter.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'A string that describes what this filter does.')], HRESULT, 'Description',
              ( ['retval', 'out'], POINTER(BSTR), 'Description' )),
    COMMETHOD([helpstring(u'Indicates if the given object can be displayed.')], HRESULT, 'CanDisplayObject',
              ( ['in'], POINTER(IGxObject), 'object' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'canDisplay' )),
    COMMETHOD([helpstring(u'Indicates if the given object can be chosen.')], HRESULT, 'CanChooseObject',
              ( ['in'], POINTER(IGxObject), 'object' ),
              ( ['in', 'out'], POINTER(esriDoubleClickResult), 'result' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'canChoose' )),
    COMMETHOD([helpstring(u'Indicates if a new object named newObjectName could be saved in the specified location.  If objectAlreadyExists is set to True, a confirmation dialog will appear asking if the existing object should be replaced.')], HRESULT, 'CanSaveObject',
              ( ['in'], POINTER(IGxObject), 'Location' ),
              ( ['in'], BSTR, 'newObjectName' ),
              ( ['in', 'out'], POINTER(VARIANT_BOOL), 'objectAlreadyExists' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'canSave' )),
]
################################################################
## code template for IGxObjectFilter implementation
##class IGxObjectFilter_Impl(object):
##    def CanSaveObject(self, Location, newObjectName):
##        u'Indicates if a new object named newObjectName could be saved in the specified location.  If objectAlreadyExists is set to True, a confirmation dialog will appear asking if the existing object should be replaced.'
##        #return objectAlreadyExists, canSave
##
##    def CanChooseObject(self, object):
##        u'Indicates if the given object can be chosen.'
##        #return result, canChoose
##
##    def CanDisplayObject(self, object):
##        u'Indicates if the given object can be displayed.'
##        #return canDisplay
##
##    @property
##    def Name(self):
##        u'A user-friendly name identifying this filter.'
##        #return Name
##
##    @property
##    def Description(self):
##        u'A string that describes what this filter does.'
##        #return Description
##

class GxFilterTablesAndFeatureClasses(CoClass):
    u'A filter for displaying/choosing tables and feature classes.'
    _reg_clsid_ = GUID('{9E14BC45-19F4-11D3-9F55-00C04F6BC69E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterTablesAndFeatureClasses._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxFilterRelationshipClasses(CoClass):
    u'A filter for displaying/choosing relationship classes.'
    _reg_clsid_ = GUID('{B3A06038-A008-4F16-B3BC-1B1B78DB68F1}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterRelationshipClasses._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class IGxTextFile(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Indicator interface that identifies a GxObject that corresponds to a text file.'
    _iid_ = GUID('{07D8C093-A491-4C72-9E9B-728D61999B9D}')
    _idlflags_ = ['oleautomation']
IGxTextFile._methods_ = [
]
################################################################
## code template for IGxTextFile implementation
##class IGxTextFile_Impl(object):

class GxFilterTables(CoClass):
    u'A filter for displaying/choosing tables.'
    _reg_clsid_ = GUID('{9E14BC35-19F4-11D3-9F55-00C04F6BC69E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterTables._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxMap(CoClass):
    u'GxObject that represents a map.'
    _reg_clsid_ = GUID('{BDBBB40E-D0B2-11D1-AED9-080009EC734B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxMap(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Indicator interface that identifies a GxObject that corresponds to an ArcMap document.'
    _iid_ = GUID('{BDBBB3F0-D0B2-11D1-AED9-080009EC734B}')
    _idlflags_ = ['oleautomation']
class IGxMapPageLayout(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that returns the page layer for a map document.'
    _iid_ = GUID('{252C4A5D-F6D7-11D3-A68C-0008C7D3AE8D}')
    _idlflags_ = ['oleautomation']
class IGxObjectUI(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that represent the icons and menus for a GxObject.'
    _iid_ = GUID('{7273AA57-E6F9-11D2-9F30-00C04F6BC69E}')
    _idlflags_ = ['oleautomation']
class IGxObjectEdit(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that edit/modify a GxObject.'
    _iid_ = GUID('{BDBBB3FC-D0B2-11D1-AED9-080009EC734B}')
    _idlflags_ = ['oleautomation']
class IGxFile(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manages a file object.'
    _iid_ = GUID('{BDBBB3F2-D0B2-11D1-AED9-080009EC734B}')
    _idlflags_ = ['oleautomation']
class IGxThumbnail(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manages the thumbnail of a GxObject.'
    _iid_ = GUID('{DA1862ED-95F8-11D2-AF67-080009EC734B}')
    _idlflags_ = ['oleautomation']
class IGxObjectInternalName(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manage the name object that the GxObject represents.'
    _iid_ = GUID('{D3CC0862-A328-4B51-A05A-540BF20CEF25}')
    _idlflags_ = ['oleautomation']
class IGxObjectProperties(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that return properties of the GxObject.'
    _iid_ = GUID('{D342626E-F9DA-11D3-A68D-0008C7D3AE8D}')
    _idlflags_ = ['oleautomation']
class IGxDataElement(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to all GxObjects to get their associated data elements.'
    _iid_ = GUID('{611C22E5-DAB3-4AC6-9C98-665D0F89AACD}')
    _idlflags_ = ['oleautomation']
class IGxDataElementHelper(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to interface which allows GxObject implementers to partially or completely fill the properties of the peer data element.'
    _iid_ = GUID('{880AF9DA-A704-4546-9FF3-BD2FA8AB9E82}')
    _idlflags_ = ['oleautomation']
GxMap._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxMap, IGxMapPageLayout, IGxObject, IGxObjectUI, IGxObjectEdit, IGxFile, IGxThumbnail, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, IGxObjectInternalName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, IGxObjectProperties, IGxDataElement, IGxDataElementHelper]

class GxFolder(CoClass):
    u'GxObject that represents a folder.'
    _reg_clsid_ = GUID('{BDBBB40D-D0B2-11D1-AED9-080009EC734B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxFolder(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that return file system workspaces represented by this folder.'
    _iid_ = GUID('{BDBBB3EF-D0B2-11D1-AED9-080009EC734B}')
    _idlflags_ = ['oleautomation']
class IGxObjectContainer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manage child GxObjects.'
    _iid_ = GUID('{7273AA58-E6F9-11D2-9F30-00C04F6BC69E}')
    _idlflags_ = ['oleautomation']
class IGxPasteTarget(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members for pasting objects.'
    _iid_ = GUID('{BDBBB403-D0B2-11D1-AED9-080009EC734B}')
    _idlflags_ = ['oleautomation']
class IGxCachedObjects(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that load/release objects being cached for efficiency.'
    _iid_ = GUID('{BDBBB404-D0B2-11D1-AED9-080009EC734B}')
    _idlflags_ = ['oleautomation']
GxFolder._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxFolder, IGxFolderAdmin, IGxObject, IGxObjectUI, IGxObjectContainer, IGxObjectEdit, IGxPasteTarget, IGxCachedObjects, IGxFile, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, IGxObjectInternalName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, IGxObjectProperties, IGxDataElement, IGxDataElementHelper]

class IGxServiceDefinition(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manage a GxServiceDefinition object.'
    _iid_ = GUID('{970FBDD1-1292-4E83-9571-BB707C87C65E}')
    _idlflags_ = ['oleautomation']
IGxServiceDefinition._methods_ = [
    COMMETHOD(['propget', helpstring(u'Name of draft Type.')], HRESULT, 'TypeName',
              ( ['retval', 'out'], POINTER(BSTR), 'pType' )),
    COMMETHOD(['propget', helpstring(u'The cooresponding file path of a draft service.')], HRESULT, 'FilePath',
              ( ['retval', 'out'], POINTER(BSTR), 'pFilePath' )),
    COMMETHOD(['propput', helpstring(u'The cooresponding file path of a draft service.')], HRESULT, 'FilePath',
              ( ['in'], BSTR, 'pFilePath' )),
]
################################################################
## code template for IGxServiceDefinition implementation
##class IGxServiceDefinition_Impl(object):
##    @property
##    def TypeName(self):
##        u'Name of draft Type.'
##        #return pType
##
##    def _get(self):
##        u'The cooresponding file path of a draft service.'
##        #return pFilePath
##    def _set(self, pFilePath):
##        u'The cooresponding file path of a draft service.'
##    FilePath = property(_get, _set, doc = _set.__doc__)
##

class IGxFolderConnections(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Indicator interface that identifies an object that contains folder connections.'
    _iid_ = GUID('{10A14ACD-18AE-4EC3-8239-A7CE54B5FD2B}')
    _idlflags_ = ['oleautomation']
IGxFolderConnections._methods_ = [
]
################################################################
## code template for IGxFolderConnections implementation
##class IGxFolderConnections_Impl(object):

class GxFilterPolygonFeatureClasses(CoClass):
    u'A filter for displaying/choosing polygon feature classes.'
    _reg_clsid_ = GUID('{9E14BC41-19F4-11D3-9F55-00C04F6BC69E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterPolygonFeatureClasses._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

IGxPasteTarget._methods_ = [
    COMMETHOD([helpstring(u'Indicates if the specified names may be pasted into this object.  On output, moveOperation indicates if a subsequent paste operation would represent a move, or merely a copy, operation.')], HRESULT, 'CanPaste',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IEnumName), 'names' ),
              ( ['in', 'out'], POINTER(VARIANT_BOOL), 'moveOperation' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'CanPaste' )),
    COMMETHOD([helpstring(u'Pastes the specified names into this object.  On input, moveOperation indicates if this is a move operation.  On output, it indicates if the objects have been moved, or merely copied.')], HRESULT, 'Paste',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IEnumName), 'names' ),
              ( ['in', 'out'], POINTER(VARIANT_BOOL), 'moveOperation' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'successfulPaste' )),
]
################################################################
## code template for IGxPasteTarget implementation
##class IGxPasteTarget_Impl(object):
##    def Paste(self, names):
##        u'Pastes the specified names into this object.  On input, moveOperation indicates if this is a move operation.  On output, it indicates if the objects have been moved, or merely copied.'
##        #return moveOperation, successfulPaste
##
##    def CanPaste(self, names):
##        u'Indicates if the specified names may be pasted into this object.  On output, moveOperation indicates if a subsequent paste operation would represent a move, or merely a copy, operation.'
##        #return moveOperation, CanPaste
##

class IEnumGxObjectFactory(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that enumerate through GxObject factories.'
    _iid_ = GUID('{3E72EA9A-5DF0-4462-AC0B-DCD13F3C409D}')
    _idlflags_ = ['oleautomation']
class IGxObjectFactory(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that define a GxObject factory.'
    _iid_ = GUID('{65D77502-895C-11D2-AF5D-080009EC734B}')
    _idlflags_ = ['oleautomation']
IEnumGxObjectFactory._methods_ = [
    COMMETHOD([helpstring(u'The next factory.')], HRESULT, 'Next',
              ( ['retval', 'out'], POINTER(POINTER(IGxObjectFactory)), 'factory' )),
    COMMETHOD([helpstring(u'Starts the enumeration at the beginning.')], HRESULT, 'Reset'),
]
################################################################
## code template for IEnumGxObjectFactory implementation
##class IEnumGxObjectFactory_Impl(object):
##    def Reset(self):
##        u'Starts the enumeration at the beginning.'
##        #return 
##
##    def Next(self):
##        u'The next factory.'
##        #return factory
##

class RasterFormatFGDBFilter(CoClass):
    u'The format filter for File Geodatabase Raster.'
    _reg_clsid_ = GUID('{3D25E36D-7A80-4903-AF8A-8010E3C19085}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IRasterFormatFilter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that provide information about raster formats.'
    _iid_ = GUID('{59CBD1F2-2AB6-11D4-ABDD-0008C73FCA1C}')
    _idlflags_ = ['oleautomation']
RasterFormatFGDBFilter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter, IRasterFormatFilter]

class GxFilterPointFeatureClasses(CoClass):
    u'A filter for displaying/choosing point feature classes.'
    _reg_clsid_ = GUID('{9E14BC3F-19F4-11D3-9F55-00C04F6BC69E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterPointFeatureClasses._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxCatalog(CoClass):
    u'GxObject that represents the catalog.'
    _reg_clsid_ = GUID('{BDBBB40C-D0B2-11D1-AED9-080009EC734B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxCatalog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manages a GX catalog.'
    _iid_ = GUID('{BDBBB3EE-D0B2-11D1-AED9-080009EC734B}')
    _idlflags_ = ['oleautomation']
class IGxCatalogWorkspace(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manages a GX catalog workspace.'
    _iid_ = GUID('{9585BC1B-3477-48F7-9F28-C1ED484AD498}')
    _idlflags_ = ['oleautomation']
class IGxCatalogDefaultDatabase(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manages a GX catalog default geodatabase.'
    _iid_ = GUID('{F154FD7B-C485-47D2-810A-2792E41F225D}')
    _idlflags_ = ['oleautomation']
class IGxObjectFactories(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manage a collection of GxObject factories.'
    _iid_ = GUID('{6EEC9A26-E824-45D7-9536-FE28393BA9C1}')
    _idlflags_ = ['oleautomation']
class IGxPasteTargetHelper(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that help pasting GxObjects.'
    _iid_ = GUID('{C8B779C7-9CE0-45F9-BB53-C09898688C25}')
    _idlflags_ = ['oleautomation']
class IGxCatalogEventsDisp(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Provides access to events that the catalog can fire.'
    _iid_ = GUID('{BDBBB401-D0B2-11D1-AED9-080009EC734B}')
    _idlflags_ = ['oleautomation']
class IGxCatalogEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to events that the catalog can fire.'
    _iid_ = GUID('{BDBBB3F8-D0B2-11D1-AED9-080009EC734B}')
    _idlflags_ = ['oleautomation']
class IGxObjectSort(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manages the properties determining whether an object should be sorted or not.'
    _iid_ = GUID('{4B7EB42E-D500-11D3-A6F3-0008C7D3AE50}')
    _idlflags_ = ['oleautomation']
GxCatalog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxCatalog, IGxCatalogWorkspace, IGxCatalogDefaultDatabase, IGxObject, IGxObjectUI, IGxObjectContainer, IGxObjectEdit, IGxPasteTarget, IGxFile, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IComPropertySheetEvents, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IConnectionPointContainer, IGxObjectFactories, IGxPasteTargetHelper, IGxDataElement, IGxDataElementHelper, IGxObjectSort]
GxCatalog._outgoing_interfaces_ = [IGxCatalogEventsDisp, IGxCatalogEvents]

class IGxCatalogAdmin(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manage the behavior of the GX catalog object.'
    _iid_ = GUID('{9598FB2F-22BA-11D3-9F58-00C04F6BC69E}')
    _idlflags_ = ['oleautomation', 'hidden']
IGxCatalogAdmin._methods_ = [
    COMMETHOD(['propput', helpstring(u'The cached locations.')], HRESULT, 'CachedLocations',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IEnumBSTR), 'locations' )),
    COMMETHOD(['propget', helpstring(u'The cached locations.')], HRESULT, 'CachedLocations',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IEnumBSTR)), 'locations' )),
    COMMETHOD(['propget', helpstring(u'The number of root-level objects in the catalog.')], HRESULT, 'RootObjectCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'The specified root-level object.')], HRESULT, 'RootObject',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IGxObject)), 'gxObject' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the specified root-level object is enabled within the catalog.')], HRESULT, 'IsRootObjectEnabled',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsEnabled' )),
    COMMETHOD([helpstring(u'Enables or disables the specified root-level object within the catalog.')], HRESULT, 'EnableRootObject',
              ( ['in'], c_int, 'index' ),
              ( ['in'], VARIANT_BOOL, 'IsEnabled' )),
    COMMETHOD([helpstring(u"Refreshes the catalog's root objects without refreshing disk connections.")], HRESULT, 'RefreshRootObjects'),
    COMMETHOD(['propput', helpstring(u'Indicates if file extensions are hidden.')], HRESULT, 'HideExtensions',
              ( ['in'], VARIANT_BOOL, 'isHidden' )),
    COMMETHOD(['propget', helpstring(u'Indicates if file extensions are hidden.')], HRESULT, 'HideExtensions',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'isHidden' )),
    COMMETHOD(['propput', helpstring(u'Indicates if ArcCatalog should return to last location on startup.')], HRESULT, 'ReturnToLastLocation',
              ( ['in'], VARIANT_BOOL, 'isSet' )),
    COMMETHOD(['propget', helpstring(u'Indicates if ArcCatalog should return to last location on startup.')], HRESULT, 'ReturnToLastLocation',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'isSet' )),
    COMMETHOD(['propput', helpstring(u'Indicates if ArcCatalog should prescan folders and display them with a special icon if they contain GIS data.')], HRESULT, 'PrescanFolders',
              ( ['in'], VARIANT_BOOL, 'PrescanFolders' )),
    COMMETHOD(['propget', helpstring(u'Indicates if ArcCatalog should prescan folders and display them with a special icon if they contain GIS data.')], HRESULT, 'PrescanFolders',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'PrescanFolders' )),
]
################################################################
## code template for IGxCatalogAdmin implementation
##class IGxCatalogAdmin_Impl(object):
##    def _get(self):
##        u'Indicates if ArcCatalog should return to last location on startup.'
##        #return isSet
##    def _set(self, isSet):
##        u'Indicates if ArcCatalog should return to last location on startup.'
##    ReturnToLastLocation = property(_get, _set, doc = _set.__doc__)
##
##    def EnableRootObject(self, index, IsEnabled):
##        u'Enables or disables the specified root-level object within the catalog.'
##        #return 
##
##    @property
##    def RootObjectCount(self):
##        u'The number of root-level objects in the catalog.'
##        #return Count
##
##    @property
##    def RootObject(self, index):
##        u'The specified root-level object.'
##        #return gxObject
##
##    def _get(self):
##        u'Indicates if file extensions are hidden.'
##        #return isHidden
##    def _set(self, isHidden):
##        u'Indicates if file extensions are hidden.'
##    HideExtensions = property(_get, _set, doc = _set.__doc__)
##
##    def RefreshRootObjects(self):
##        u"Refreshes the catalog's root objects without refreshing disk connections."
##        #return 
##
##    @property
##    def IsRootObjectEnabled(self, index):
##        u'Indicates if the specified root-level object is enabled within the catalog.'
##        #return IsEnabled
##
##    def _get(self):
##        u'Indicates if ArcCatalog should prescan folders and display them with a special icon if they contain GIS data.'
##        #return PrescanFolders
##    def _set(self, PrescanFolders):
##        u'Indicates if ArcCatalog should prescan folders and display them with a special icon if they contain GIS data.'
##    PrescanFolders = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The cached locations.'
##        #return locations
##    def _set(self, locations):
##        u'The cached locations.'
##    CachedLocations = property(_get, _set, doc = _set.__doc__)
##

class GxFilterFeatureClasses(CoClass):
    u'A filter for displaying/choosing feature classes.'
    _reg_clsid_ = GUID('{9E14BC34-19F4-11D3-9F55-00C04F6BC69E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterFeatureClasses._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxFilterCoverageAnnotationClasses(CoClass):
    u'A filter for displaying/choosing coverage annotation classes.'
    _reg_clsid_ = GUID('{CAE94A9F-5FBA-11D3-9FBD-00C04F6BC78E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterCoverageAnnotationClasses._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]


# values for enumeration 'esriGxDeleteOption'
esriGxDeleteSingle = 0
esriGxDeleteYesToAll = 1
esriGxDeleteCancel = 2
esriGxDeleteOption = c_int # enum
IGxDataElementHelper._methods_ = [
    COMMETHOD([helpstring(u"Retrieve the GxObject's heavy-weight properties.")], HRESULT, 'RetrieveDEFullProperties',
              ( ['in', 'out'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElement), 'dataElement' )),
    COMMETHOD([helpstring(u"Retrieve the GxObject's light-weight properties.")], HRESULT, 'RetrieveDEBaseProperties',
              ( ['in', 'out'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElement), 'dataElement' )),
]
################################################################
## code template for IGxDataElementHelper implementation
##class IGxDataElementHelper_Impl(object):
##    def RetrieveDEFullProperties(self):
##        u"Retrieve the GxObject's heavy-weight properties."
##        #return dataElement
##
##    def RetrieveDEBaseProperties(self):
##        u"Retrieve the GxObject's light-weight properties."
##        #return dataElement
##

class GxFilterDimensionFeatureClasses(CoClass):
    u'A filter for displaying/choosing dimension feature classes.'
    _reg_clsid_ = GUID('{32648160-958A-11D4-80ED-00C04F601565}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterDimensionFeatureClasses._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class IGxObjectFilterCollectionAdmin(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that returns the first passed GxObject filter in a collection.'
    _iid_ = GUID('{FD7AD57B-DA73-11D3-A67D-0008C7D3AE8D}')
    _idlflags_ = ['oleautomation']
IGxObjectFilterCollectionAdmin._methods_ = [
    COMMETHOD(['propget', helpstring(u'The first passed object filter in filter collection.')], HRESULT, 'FirstPassedFilter',
              ( ['retval', 'out'], POINTER(POINTER(IGxObjectFilter)), 'Filter' )),
]
################################################################
## code template for IGxObjectFilterCollectionAdmin implementation
##class IGxObjectFilterCollectionAdmin_Impl(object):
##    @property
##    def FirstPassedFilter(self):
##        u'The first passed object filter in filter collection.'
##        #return Filter
##

class IGxWorkspaceFolder(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Indicator interface for GxWorkspaceFolder objects.'
    _iid_ = GUID('{576B2BD6-F1F0-40F8-8FC8-2EE0929CC9F6}')
    _idlflags_ = ['oleautomation']
IGxWorkspaceFolder._methods_ = [
]
################################################################
## code template for IGxWorkspaceFolder implementation
##class IGxWorkspaceFolder_Impl(object):

class GxLayer(CoClass):
    u'GxObject that represents a layer.'
    _reg_clsid_ = GUID('{BDBBB40F-D0B2-11D1-AED9-080009EC734B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxLayer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manage a GX layer object.'
    _iid_ = GUID('{BDBBB3F1-D0B2-11D1-AED9-080009EC734B}')
    _idlflags_ = ['oleautomation']
GxLayer._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxLayer, IGxObject, IGxObjectUI, IGxObjectEdit, IGxFile, IGxThumbnail, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, IGxObjectInternalName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, IGxObjectProperties, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IComPropertySheetEvents, IGxCachedObjects, IGxDataElement, IGxDataElementHelper, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersion]

IGxMap._methods_ = [
]
################################################################
## code template for IGxMap implementation
##class IGxMap_Impl(object):

IGxCatalogEventsDisp._methods_ = [
    COMMETHOD([helpstring(u'Called when the whole catalog has changed.')], HRESULT, 'OnRefreshAll'),
    COMMETHOD([helpstring(u'Called when an object has been added to some part of the catalog.')], HRESULT, 'OnObjectAdded',
              ( [], POINTER(IGxObject), 'gxObject' )),
    COMMETHOD([helpstring(u'Called when an object has been deleted from some part of the catalog.')], HRESULT, 'OnObjectDeleted',
              ( [], POINTER(IGxObject), 'gxObject' )),
    COMMETHOD([helpstring(u'Called when an object in some part of the catalog has been changed.')], HRESULT, 'OnObjectChanged',
              ( [], POINTER(IGxObject), 'gxObject' )),
    COMMETHOD([helpstring(u'Called when an object in some part of the catalog has been refreshed.')], HRESULT, 'OnObjectRefreshed',
              ( [], POINTER(IGxObject), 'gxObject' )),
]
################################################################
## code template for IGxCatalogEventsDisp implementation
##class IGxCatalogEventsDisp_Impl(object):
##    def OnObjectAdded(self, gxObject):
##        u'Called when an object has been added to some part of the catalog.'
##        #return 
##
##    def OnObjectDeleted(self, gxObject):
##        u'Called when an object has been deleted from some part of the catalog.'
##        #return 
##
##    def OnObjectRefreshed(self, gxObject):
##        u'Called when an object in some part of the catalog has been refreshed.'
##        #return 
##
##    def OnRefreshAll(self):
##        u'Called when the whole catalog has changed.'
##        #return 
##
##    def OnObjectChanged(self, gxObject):
##        u'Called when an object in some part of the catalog has been changed.'
##        #return 
##

class GxFilterAnnotationFeatureClasses(CoClass):
    u'A filter for displaying/choosing annotation feature classes.'
    _reg_clsid_ = GUID('{02B8C7CB-2D83-11D3-9F9F-00C04F6BC6A5}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterAnnotationFeatureClasses._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

IGxLayer._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The associated layer.')], HRESULT, 'Layer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer), 'Layer' )),
    COMMETHOD(['propget', helpstring(u'The associated layer.')], HRESULT, 'Layer',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer)), 'Layer' )),
]
################################################################
## code template for IGxLayer implementation
##class IGxLayer_Impl(object):
##    @property
##    def Layer(self, Layer):
##        u'The associated layer.'
##        #return 
##

class IGxDisplayName(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the display name of GxObjects.'
    _iid_ = GUID('{CCB73C73-EB3F-46D8-AF8B-EAA8B450205F}')
    _idlflags_ = ['oleautomation']
IGxDisplayName._methods_ = [
    COMMETHOD(['propget', helpstring(u'The display name of the object.')], HRESULT, 'DisplayName',
              ( ['retval', 'out'], POINTER(BSTR), 'DisplayName' )),
    COMMETHOD(['propput', helpstring(u'The display name of the object.')], HRESULT, 'DisplayName',
              ( ['in'], BSTR, 'DisplayName' )),
]
################################################################
## code template for IGxDisplayName implementation
##class IGxDisplayName_Impl(object):
##    def _get(self):
##        u'The display name of the object.'
##        #return DisplayName
##    def _set(self, DisplayName):
##        u'The display name of the object.'
##    DisplayName = property(_get, _set, doc = _set.__doc__)
##

class IGxObjectArray(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manage an array of GxObjects.'
    _iid_ = GUID('{B330F487-DE4D-11D2-9F2F-00C04F6BC69E}')
    _idlflags_ = ['oleautomation']
IGxObjectArray._methods_ = [
    COMMETHOD(['propget', helpstring(u'The number of objects in the array.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD([helpstring(u'Inserts an object into the array before the specified index.  If index is -1, the object is inserted at the end.')], HRESULT, 'Insert',
              ( ['in'], c_int, 'index' ),
              ( ['in'], POINTER(IGxObject), 'gxObject' )),
    COMMETHOD([helpstring(u'Removes the object at the specified index in the array.')], HRESULT, 'Remove',
              ( ['in'], c_int, 'index' )),
    COMMETHOD([helpstring(u'The object at the given index in the array.')], HRESULT, 'Item',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IGxObject)), 'gxObject' )),
    COMMETHOD([helpstring(u'Removes all objects from the array.')], HRESULT, 'Empty'),
]
################################################################
## code template for IGxObjectArray implementation
##class IGxObjectArray_Impl(object):
##    @property
##    def Count(self):
##        u'The number of objects in the array.'
##        #return Count
##
##    def Insert(self, index, gxObject):
##        u'Inserts an object into the array before the specified index.  If index is -1, the object is inserted at the end.'
##        #return 
##
##    def Empty(self):
##        u'Removes all objects from the array.'
##        #return 
##
##    def Remove(self, index):
##        u'Removes the object at the specified index in the array.'
##        #return 
##
##    def Item(self, index):
##        u'The object at the given index in the array.'
##        #return gxObject
##

class GxFeatureDefinitionPackage(CoClass):
    u'GxObject that represents a feature definition package.'
    _reg_clsid_ = GUID('{D20E4F17-352D-4FD3-B154-0E0EF254251F}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxFileSetup(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that sets up the properties of a file object.'
    _iid_ = GUID('{B330F48A-DE4D-11D2-9F2F-00C04F6BC69E}')
    _idlflags_ = ['oleautomation']
class IGxFeatureDefinitionPackage(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manage a GX feature definition package object.'
    _iid_ = GUID('{3F91D150-E86C-4FB5-ACB6-02FE036C30C9}')
    _idlflags_ = ['oleautomation']
GxFeatureDefinitionPackage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxFile, IGxFileSetup, IGxObject, IGxObjectUI, IGxObjectEdit, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, IGxObjectInternalName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, IGxObjectProperties, IGxDataElement, IGxDataElementHelper, IGxFeatureDefinitionPackage]

class GxFilterDatasetsAndLayers(CoClass):
    u'A filter for displaying/choosing a dataset or layer.'
    _reg_clsid_ = GUID('{701C66DB-1DD1-11D3-9F56-00C04F6BC69E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterDatasetsAndLayers._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

IGxFile._methods_ = [
    COMMETHOD(['propput', helpstring(u'The full path for the file.')], HRESULT, 'Path',
              ( ['in'], BSTR, 'Path' )),
    COMMETHOD(['propget', helpstring(u'The full path for the file.')], HRESULT, 'Path',
              ( ['retval', 'out'], POINTER(BSTR), 'Path' )),
    COMMETHOD([helpstring(u'Creates a new file.')], HRESULT, 'New'),
    COMMETHOD([helpstring(u'Opens the file.')], HRESULT, 'Open'),
    COMMETHOD([helpstring(u'Closes the file, optionally saving changes.')], HRESULT, 'Close',
              ( ['in'], VARIANT_BOOL, 'saveChanges' )),
    COMMETHOD([helpstring(u'Opens an editor to modify the file.')], HRESULT, 'Edit'),
    COMMETHOD([helpstring(u'Saves changes without closing the file.')], HRESULT, 'Save'),
]
################################################################
## code template for IGxFile implementation
##class IGxFile_Impl(object):
##    def Edit(self):
##        u'Opens an editor to modify the file.'
##        #return 
##
##    def Close(self, saveChanges):
##        u'Closes the file, optionally saving changes.'
##        #return 
##
##    def _get(self):
##        u'The full path for the file.'
##        #return Path
##    def _set(self, Path):
##        u'The full path for the file.'
##    Path = property(_get, _set, doc = _set.__doc__)
##
##    def Save(self):
##        u'Saves changes without closing the file.'
##        #return 
##
##    def Open(self):
##        u'Opens the file.'
##        #return 
##
##    def New(self):
##        u'Creates a new file.'
##        #return 
##

class GxFilterSceneDatasetsAndLayers(CoClass):
    u'A filter for displaying/choosing a dataset or layer in ArcScene.'
    _reg_clsid_ = GUID('{C7F5FD23-9B6B-4777-A4A8-5C5326C39861}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterSceneDatasetsAndLayers._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxFilterDatasets(CoClass):
    u'A filter for displaying/choosing a dataset.'
    _reg_clsid_ = GUID('{B9EA9FD9-1AB7-11D3-9F55-00C04F6BC69E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterDatasets._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

IGxFeatureDefinitionPackage._methods_ = [
]
################################################################
## code template for IGxFeatureDefinitionPackage implementation
##class IGxFeatureDefinitionPackage_Impl(object):

class GxPackage(CoClass):
    u'GxObject that represents a layer or map package.'
    _reg_clsid_ = GUID('{11A537DF-362C-4453-87C1-C65FAB2F59D7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxPackage(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manage a GxPackage object.'
    _iid_ = GUID('{6A25E02B-6565-467F-A09C-8015AC9362C2}')
    _idlflags_ = ['oleautomation']
GxPackage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxPackage, IGxObject, IGxObjectUI, IGxObjectEdit, IGxFile, IGxThumbnail, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, IGxObjectInternalName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, IGxObjectProperties, IGxDataElement, IGxDataElementHelper]

class GxFilterMapDatasetsLayersAndResults(CoClass):
    u'A filter for displaying/choosing a dataset, layer or geoprocessing result in ArcMap.'
    _reg_clsid_ = GUID('{BE5DE34D-D8B3-40EE-A82D-7F23FA957CF7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterMapDatasetsLayersAndResults._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxFile(CoClass):
    u'GxObject that represents a file.'
    _reg_clsid_ = GUID('{BDBBB410-D0B2-11D1-AED9-080009EC734B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFile._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxFile, IGxFileSetup, IGxObject, IGxObjectUI, IGxObjectEdit, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, IGxObjectInternalName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, IGxObjectProperties, IGxDataElement, IGxDataElementHelper]

class ShortcutNativeType(CoClass):
    u'Native type for a shortcut.'
    _reg_clsid_ = GUID('{29CFF5A5-6675-4F16-BD5A-F682EC45E426}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
ShortcutNativeType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeType]

class IGxRemoteDatabaseFolder(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that defines the remote databases folder.'
    _iid_ = GUID('{BDBBB3FE-D0B2-11D1-AED9-080009EC734B}')
    _idlflags_ = ['oleautomation']
IGxRemoteDatabaseFolder._methods_ = [
    COMMETHOD(['propget', helpstring(u'The value of the Path property.')], HRESULT, 'Path',
              ( ['retval', 'out'], POINTER(BSTR), 'Path' )),
    COMMETHOD(['propput', helpstring(u'The value of the Path property.')], HRESULT, 'Path',
              ( ['in'], BSTR, 'Path' )),
]
################################################################
## code template for IGxRemoteDatabaseFolder implementation
##class IGxRemoteDatabaseFolder_Impl(object):
##    def _get(self):
##        u'The value of the Path property.'
##        #return Path
##    def _set(self, Path):
##        u'The value of the Path property.'
##    Path = property(_get, _set, doc = _set.__doc__)
##

class GxFilterFeatureDatasets(CoClass):
    u'A filter for displaying/choosing feature datasets.'
    _reg_clsid_ = GUID('{9E14BC33-19F4-11D3-9F55-00C04F6BC69E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterFeatureDatasets._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxFilterDefaultDatabaseWorkspaces(CoClass):
    u'A filter for displaying/choosing workspaces use as the default database.'
    _reg_clsid_ = GUID('{D2DC4AC2-A5AD-42BE-AEE7-93D94DDE9DCA}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterDefaultDatabaseWorkspaces._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxFilterFeatureDatasetsAndFeatureClasses(CoClass):
    u'A filter for displaying/choosing feature datasets or feature classes.'
    _reg_clsid_ = GUID('{BBE5A114-1D2C-11D3-9F55-00C04F6BC69E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterFeatureDatasetsAndFeatureClasses._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxFilterGeometricNetworks(CoClass):
    u'A filter for displaying/choosing geometric networks.'
    _reg_clsid_ = GUID('{A0D451BB-CC31-4C9E-BF07-2AAFFFC50512}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterGeometricNetworks._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxFilterMaps(CoClass):
    u'A filter for displaying/choosing maps.'
    _reg_clsid_ = GUID('{9E14BC37-19F4-11D3-9F55-00C04F6BC69E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterMaps._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxFilterMapDatasetsAndLayers(CoClass):
    u'A filter for displaying/choosing a dataset or layer in ArcMap.'
    _reg_clsid_ = GUID('{6FB420CA-A3AC-4185-ADCA-61742FAC65FB}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterMapDatasetsAndLayers._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxToolboxExtension(CoClass):
    u'GX Toolbox object factory.'
    _reg_clsid_ = GUID('{F13B82DC-C395-43E3-8AC0-E13F3FA22F53}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxDatabaseExtension(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manage a GX database extension.'
    _iid_ = GUID('{CDB0CC46-4E87-11D3-9F52-00C04F6BDF06}')
    _idlflags_ = ['oleautomation']
GxToolboxExtension._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxDatabaseExtension, IGxPasteTargetHelper]

class GxVpfDataset(CoClass):
    u'A VPF Feature Class.'
    _reg_clsid_ = GUID('{397847FB-C865-11D3-9B56-00C04FA33299}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxDataset(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manages the properties of a GX dataset object.'
    _iid_ = GUID('{BDBBB3F4-D0B2-11D1-AED9-080009EC734B}')
    _idlflags_ = ['oleautomation']
GxVpfDataset._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxDataset, IGxObject, IGxObjectUI, IGxPasteTarget, IGxCachedObjects, IGxObjectEdit, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, IGxThumbnail, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, IGxObjectContainer, IGxObjectProperties, IGxObjectInternalName, IGxDataElement, IGxDataElementHelper]

class GxSpatialWeightsMatrixFile(CoClass):
    u'GxObject that represents a spatial weights matrix file.'
    _reg_clsid_ = GUID('{ED3FC5EB-FC13-4EE3-8B9B-41331F787AA9}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxSpatialWeightsMatrixFile._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectUI, IGxObjectEdit, IGxFile, IGxThumbnail, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, IGxObjectInternalName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, IGxObjectProperties, IGxDataElement, IGxDataElementHelper]

class GxDatabaseServerFolder(CoClass):
    u'Container for Database Servers.'
    _reg_clsid_ = GUID('{89648B3E-8469-489F-9745-D7A1D365E082}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxRootObjectSortPriority(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the sort priority for Gx Root Objects.'
    _iid_ = GUID('{E393F857-2ED2-468E-9539-E6355E53027E}')
    _idlflags_ = ['oleautomation']
GxDatabaseServerFolder._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectUI, IGxObjectContainer, IGxObjectEdit, IGxObjectProperties, IGxCachedObjects, IGxRootObjectSortPriority]

class IGxAGSImage(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of GxObject that represents a ArcGIS Image Server Service object.'
    _iid_ = GUID('{0CBBD747-7A18-47A8-AEE4-108A1625094E}')
    _idlflags_ = ['oleautomation']
class IGxAGSImage2(IGxAGSImage):
    _case_insensitive_ = True
    u'Provides access to members of GxObject that represents a ArcGIS Image Server Service object.'
    _iid_ = GUID('{BBBA462F-3701-4D7F-B1CC-962ADB4685CC}')
    _idlflags_ = ['oleautomation']
IGxAGSImage._methods_ = [
]
################################################################
## code template for IGxAGSImage implementation
##class IGxAGSImage_Impl(object):

IGxAGSImage2._methods_ = [
    COMMETHOD(['propget', helpstring(u'The attribute table of the Image Service.')], HRESULT, 'Table',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable)), 'Table' )),
]
################################################################
## code template for IGxAGSImage2 implementation
##class IGxAGSImage2_Impl(object):
##    @property
##    def Table(self):
##        u'The attribute table of the Image Service.'
##        #return Table
##

class IMSImageMap(CoClass):
    u'GxObject that represents ArcIMS Image Map.'
    _reg_clsid_ = GUID('{66B9113D-7129-4AD4-BC47-A9CE904337EB}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxLayerSource(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Indicator interface that identifies that the given GxObject can generate a layer for the underlying data source.'
    _iid_ = GUID('{FBBBDFA1-59C3-42C9-B63F-1CE5D8FCB7C5}')
    _idlflags_ = ['oleautomation']
IMSImageMap._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectUI, IGxLayerSource, comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IIMSServiceDescription, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, IGxObjectProperties, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, IGxObjectEdit, IGxObjectInternalName, IGxThumbnail, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IIMSUserRole]

class IGxContentViewControlCustom(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that controls GxContentViewControlCustom.'
    _iid_ = GUID('{13D440F2-8703-40EB-BF6F-0668444065DE}')
    _idlflags_ = ['oleautomation']
IGxContentViewControlCustom._methods_ = [
    COMMETHOD(['propget', helpstring(u'The class ID of the custom content view control.')], HRESULT, 'ViewClassID',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID)), 'ppUID' )),
]
################################################################
## code template for IGxContentViewControlCustom implementation
##class IGxContentViewControlCustom_Impl(object):
##    @property
##    def ViewClassID(self):
##        u'The class ID of the custom content view control.'
##        #return ppUID
##

class IGxGDSConnection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of GxObject that connects to a GeoData Server.'
    _iid_ = GUID('{E10B6C94-58ED-4E45-84B2-285559BFA11E}')
    _idlflags_ = ['oleautomation']
IGxGDSConnection._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates whether the GIS Data server connection has been made.')], HRESULT, 'IsConnected',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsConnected' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the connected user is an administrator or not.')], HRESULT, 'IsAdministrator',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsAdministrator' )),
    COMMETHOD([helpstring(u'Connects to a GIS Data server.')], HRESULT, 'Connect'),
    COMMETHOD([helpstring(u'Disconnects from a GIS Data server.')], HRESULT, 'Disconnect'),
    COMMETHOD(['propget', helpstring(u'The server name.')], HRESULT, 'ServerName',
              ( ['retval', 'out'], POINTER(BSTR), 'ServerName' )),
    COMMETHOD(['propget', helpstring(u'The Data Server Manager object.')], HRESULT, 'DataServerManager',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'DataServerManager' )),
    COMMETHOD([helpstring(u'Creates a new Geodatabase.')], HRESULT, 'CreateGeoDatabase',
              ( ['in'], BSTR, 'gdbName' ),
              ( ['in'], BSTR, 'gdbFileName' ),
              ( ['in'], c_int, 'gdbFileSize' )),
    COMMETHOD([helpstring(u'Attaches a Geodatabase.')], HRESULT, 'AttachGeoDatabase',
              ( ['in'], BSTR, 'gdbName' ),
              ( ['in'], BSTR, 'gdbFileName' )),
    COMMETHOD([helpstring(u'Restores a backup to the specified Geodatabase.')], HRESULT, 'RestoreGeodatabase',
              ( ['in'], BSTR, 'gdbName' ),
              ( ['in'], BSTR, 'backupFileName' ),
              ( ['in'], BSTR, 'dbFileName' )),
    COMMETHOD([helpstring(u'Starts a Database server.')], HRESULT, 'Start'),
    COMMETHOD([helpstring(u'Stops a Database server.')], HRESULT, 'Stop'),
    COMMETHOD([helpstring(u'Resumes a Database server.')], HRESULT, 'Resume'),
    COMMETHOD([helpstring(u'Pauses a Database server.')], HRESULT, 'Pause'),
]
################################################################
## code template for IGxGDSConnection implementation
##class IGxGDSConnection_Impl(object):
##    def RestoreGeodatabase(self, gdbName, backupFileName, dbFileName):
##        u'Restores a backup to the specified Geodatabase.'
##        #return 
##
##    def Pause(self):
##        u'Pauses a Database server.'
##        #return 
##
##    def Disconnect(self):
##        u'Disconnects from a GIS Data server.'
##        #return 
##
##    def CreateGeoDatabase(self, gdbName, gdbFileName, gdbFileSize):
##        u'Creates a new Geodatabase.'
##        #return 
##
##    @property
##    def DataServerManager(self):
##        u'The Data Server Manager object.'
##        #return DataServerManager
##
##    @property
##    def ServerName(self):
##        u'The server name.'
##        #return ServerName
##
##    def Resume(self):
##        u'Resumes a Database server.'
##        #return 
##
##    def Stop(self):
##        u'Stops a Database server.'
##        #return 
##
##    @property
##    def IsConnected(self):
##        u'Indicates whether the GIS Data server connection has been made.'
##        #return IsConnected
##
##    def Start(self):
##        u'Starts a Database server.'
##        #return 
##
##    def Connect(self):
##        u'Connects to a GIS Data server.'
##        #return 
##
##    @property
##    def IsAdministrator(self):
##        u'Indicates whether the connected user is an administrator or not.'
##        #return IsAdministrator
##
##    def AttachGeoDatabase(self, gdbName, gdbFileName):
##        u'Attaches a Geodatabase.'
##        #return 
##

class IMSMetadataService(CoClass):
    u'GxObject that represents ArcIMS Metadata Service.'
    _reg_clsid_ = GUID('{E2D5C938-C9CC-471A-A3FF-049618618959}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxObjectDeleteOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that specify behavior when deleting multiple objects.'
    _iid_ = GUID('{C78D055B-23AE-4874-8C12-B280FAD9B8B8}')
    _idlflags_ = ['oleautomation']
class IRemoteMetadata(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members to manipulate information specific to metadata stored in an ArcIMS Metadata Server.'
    _iid_ = GUID('{9DF1041E-2F52-405E-B7B9-B736BA74340B}')
    _idlflags_ = ['oleautomation']
class IRemoteMetadata2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to allow user to decide whether to show dialog and to manipulate specific information on ArcIMS Server.'
    _iid_ = GUID('{F5FFCB33-CFD6-4A01-B777-A11724C56A35}')
    _idlflags_ = ['oleautomation']
IMSMetadataService._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectEdit, IGxObjectUI, IGxLayerSource, IGxObjectContainer, IGxObjectDeleteOptions, IGxThumbnail, comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IIMSServiceDescription, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, IGxObjectProperties, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, IGxObjectInternalName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, IRemoteMetadata, IGxPasteTarget, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, IGxObjectSort, comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IIMSUserRole, IRemoteMetadata2]

class GxSpatialReferencesFolder(CoClass):
    u'Container of spatial references (PRJ files).'
    _reg_clsid_ = GUID('{F7BF067C-969E-11D2-AD2C-00C04FA33A15}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxSpatialReferencesFolder(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manages the properties of a spatial reference folder.'
    _iid_ = GUID('{F7BF067B-969E-11D2-AD2C-00C04FA33A15}')
    _idlflags_ = ['oleautomation']
class IGxRootObjectStartupProperties(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the startup properties for Gx Root Objects.'
    _iid_ = GUID('{B1C5DD7C-DB4E-485A-8BEB-6C656B15A294}')
    _idlflags_ = ['oleautomation']
GxSpatialReferencesFolder._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectContainer, IGxObjectEdit, IGxObjectProperties, IGxObjectUI, IGxPasteTarget, IGxCachedObjects, IGxSpatialReferencesFolder, IGxDataElement, IGxDataElementHelper, IGxRootObjectStartupProperties, IGxRootObjectSortPriority]

class GxDatabase(CoClass):
    u'GxObject that represents a database.'
    _reg_clsid_ = GUID('{BDBBB411-D0B2-11D1-AED9-080009EC734B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxDatabase(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manage the properties of a GX database object.'
    _iid_ = GUID('{BDBBB3F3-D0B2-11D1-AED9-080009EC734B}')
    _idlflags_ = ['oleautomation']
class IGxDatabase2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manage the properties of a GX database object.'
    _iid_ = GUID('{C34479BA-1D3C-11D4-A0DB-00C04F6BC626}')
    _idlflags_ = ['oleautomation']
class IGxObjectWizard(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that invokes a wizard associated with the GxObject.'
    _iid_ = GUID('{C6DF682D-A28C-476A-924C-44D1194CF78D}')
    _idlflags_ = ['oleautomation']
class IGxRemoteConnection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members pertaining to remote connections.'
    _iid_ = GUID('{3F5C143C-8E15-40C7-8CE8-F67289C6842A}')
    _idlflags_ = ['oleautomation']
GxDatabase._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxDatabase, IGxDatabase2, IGxObject, IGxObjectUI, IGxObjectContainer, IGxObjectProperties, IGxObjectWizard, IGxPasteTarget, IGxCachedObjects, IGxObjectEdit, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, IGxObjectInternalName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceEvents, IGxRemoteConnection, IGxDataElement, IGxDataElementHelper]

class IGxAGSGeometry(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of GxObject that represents a ArcGIS Server geometry object.'
    _iid_ = GUID('{88193A73-B588-41B4-895D-4BA8BAD5ACC8}')
    _idlflags_ = ['oleautomation']
IGxAGSGeometry._methods_ = [
]
################################################################
## code template for IGxAGSGeometry implementation
##class IGxAGSGeometry_Impl(object):

class GxFilterRemoteMetadata(CoClass):
    u'A filter for displaying ArcIMS Metadata Documents.'
    _reg_clsid_ = GUID('{81D3B308-862A-4872-ACAD-4F45B17259D7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterRemoteMetadata._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxExcelFile(CoClass):
    u'GxObject that represents a excel file.'
    _reg_clsid_ = GUID('{FC91C8D2-4F05-4E45-ABC3-0454FBD5F9C5}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxExcelFile(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manage the properties of a GxExcelFile object.'
    _iid_ = GUID('{E1C64112-201D-4B1F-9CFD-28C77E63C798}')
    _idlflags_ = ['oleautomation']
GxExcelFile._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxExcelFile, IGxObject, IGxObjectContainer, IGxObjectWizard, IGxCachedObjects, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, IGxObjectInternalName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceEvents]

class IGxGeoprocessingResult(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to properties/methods of a catalog geoprocessing result object.'
    _iid_ = GUID('{A03DF6C7-763C-4039-AE16-0858BF4D406C}')
    _idlflags_ = ['oleautomation']
IGxGeoprocessingResult._methods_ = [
]
################################################################
## code template for IGxGeoprocessingResult implementation
##class IGxGeoprocessingResult_Impl(object):

class IGxAGSLocator(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of GxObject that represents a ArcGIS Server locator object.'
    _iid_ = GUID('{CD840193-D8E3-4A7F-B216-BE919BE275C0}')
    _idlflags_ = ['oleautomation']
IGxAGSLocator._methods_ = [
]
################################################################
## code template for IGxAGSLocator implementation
##class IGxAGSLocator_Impl(object):

class GxToolboxesRoot(CoClass):
    u'Catalog object corresponding to root-level Toolboxes node.'
    _reg_clsid_ = GUID('{42E1CD15-8557-4152-A4F9-26ABE862C47F}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxToolboxesRoot(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to properties/methods of the root-level catalog Toolboxes object.'
    _iid_ = GUID('{5BC85E0E-5C73-4B4B-B987-43EDE7779517}')
    _idlflags_ = ['oleautomation']
GxToolboxesRoot._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectUI, IGxObjectEdit, IGxObjectProperties, IGxObjectContainer, IGxPasteTarget, IGxCachedObjects, IGxRootObjectStartupProperties, IGxRootObjectSortPriority, IGxToolboxesRoot]

class GxAddGDSConnection(CoClass):
    u'The one and only GxAddGDSConnection object.'
    _reg_clsid_ = GUID('{A4AF6DE7-7255-497F-A506-D06DAE2B6253}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxBasicObject(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Indicator interface that identifies an object that is considered a basic object type (for example, a folder).'
    _iid_ = GUID('{74F0D7F1-C7F5-4116-A9F5-5B51C9312D95}')
    _idlflags_ = ['oleautomation']
class IGxGISDataServers(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the list of GIS Data Servers registered on the system.'
    _iid_ = GUID('{8C946413-8DCE-4AED-84A0-4CE453702E33}')
    _idlflags_ = ['oleautomation']
GxAddGDSConnection._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectUI, IGxBasicObject, IGxObjectProperties, IGxObjectWizard, IGxGISDataServers]

class IEnumGxObject(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that enumerate through GxObjects.'
    _iid_ = GUID('{BDBBB3EC-D0B2-11D1-AED9-080009EC734B}')
    _idlflags_ = ['oleautomation']
IGxGISDataServers._methods_ = [
    COMMETHOD([helpstring(u'Gets the servers registered on the computer.')], HRESULT, 'GetRegisteredServers',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IFileNames), 'fileNames' ),
              ( ['retval', 'out'], POINTER(POINTER(IEnumGxObject)), 'Children' )),
]
################################################################
## code template for IGxGISDataServers implementation
##class IGxGISDataServers_Impl(object):
##    def GetRegisteredServers(self, fileNames):
##        u'Gets the servers registered on the computer.'
##        #return Children
##

class GxGDSGeodatabase(CoClass):
    u'GxObject that represents an ArcGIS Geodatabase connection.'
    _reg_clsid_ = GUID('{10696E09-13A8-4CD9-B7DA-84891B5E9179}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxGeodatabase(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of GxObject that connect to an Geodatabase object.'
    _iid_ = GUID('{E0FF3A92-9800-4BBD-807F-5168B89390A0}')
    _idlflags_ = ['oleautomation']
GxGDSGeodatabase._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectContainer, IGxDatabase, IGxDatabase2, IGxObjectWizard, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, IGxObjectInternalName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, IGxPasteTarget, IGxCachedObjects, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceEvents, IGxRemoteConnection, IGxDataElement, IGxDataElementHelper, IGxGeodatabase]

class GxShortcut(CoClass):
    u'GxObject that represents a shortcut to a GxObject.  This object is not supported on ArcGIS version 10.1. or later.'
    _reg_clsid_ = GUID('{896EF5A3-AE8C-11D3-A6D5-0008C7D3AE50}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxShortcut(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manages the target of a shortcut object.'
    _iid_ = GUID('{82289F34-2C34-40D2-A2CF-5BBCB19CB21F}')
    _idlflags_ = ['oleautomation']
GxShortcut._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxFile, IGxObject, IGxObjectEdit, IGxObjectProperties, IGxObjectUI, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, IGxShortcut, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, IGxDataElement, IGxDataElementHelper]

class IMSGlobeServiceDescription(CoClass):
    u'GxObject that represents ArcIMS Globe File.'
    _reg_clsid_ = GUID('{52900577-5366-464F-BF79-18034F9B9687}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
IMSGlobeServiceDescription._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectUI, comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IIMSServiceDescription, comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IIMSUserRole, IGxObjectContainer, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName]

class IAGSObjectCreationProperties(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that define creation properties of an ArcGIS Server object.'
    _iid_ = GUID('{AD1C813F-0C3D-4D1F-AF54-9ADEB22E67F1}')
    _idlflags_ = ['oleautomation']
IAGSObjectCreationProperties._methods_ = [
    COMMETHOD(['propget', helpstring(u'The associated server object configuration during object creation time.')], HRESULT, 'ObjectConfiguration',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._18F2FC71_6B30_45B9_B101_037A8B868B66_0_10_2.IServerObjectConfiguration)), 'config' )),
    COMMETHOD(['propputref', helpstring(u'The associated server object configuration during object creation time.')], HRESULT, 'ObjectConfiguration',
              ( ['in'], POINTER(comtypes.gen._18F2FC71_6B30_45B9_B101_037A8B868B66_0_10_2.IServerObjectConfiguration), 'config' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the server object has been started.')], HRESULT, 'DoStartEnable',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'doEnable' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether the server object has been started.')], HRESULT, 'DoStartEnable',
              ( ['in'], VARIANT_BOOL, 'doEnable' )),
]
################################################################
## code template for IAGSObjectCreationProperties implementation
##class IAGSObjectCreationProperties_Impl(object):
##    def _get(self):
##        u'Indicates whether the server object has been started.'
##        #return doEnable
##    def _set(self, doEnable):
##        u'Indicates whether the server object has been started.'
##    DoStartEnable = property(_get, _set, doc = _set.__doc__)
##
##    def ObjectConfiguration(self, config):
##        u'The associated server object configuration during object creation time.'
##        #return 
##

IGxGeodatabase._methods_ = [
    COMMETHOD(['propget', helpstring(u'The Geodatabase name.')], HRESULT, 'GeodatabaseName',
              ( ['in'], POINTER(BSTR), 'Name' )),
    COMMETHOD([helpstring(u'Detach a Geodatabase from a Data server.')], HRESULT, 'DetachGeodatabase'),
    COMMETHOD([helpstring(u'Backs up a Geodatabase from a Data server.')], HRESULT, 'Backup',
              ( ['in'], BSTR, 'backupName' ),
              ( ['in'], BSTR, 'backupFileName' ),
              ( ['in'], BSTR, 'Description' ),
              ( ['out'], POINTER(VARIANT_BOOL), 'isSimpleRecoveryModel' )),
    COMMETHOD([helpstring(u'Backup information.')], HRESULT, 'GetProperties',
              ( ['out'], POINTER(BSTR), 'Owner' ),
              ( ['out'], POINTER(VARIANT), 'creationDate' ),
              ( ['out'], POINTER(c_int), 'size' ),
              ( ['out'], POINTER(BSTR), 'fileLocation' ),
              ( ['out'], POINTER(VARIANT), 'lastBackup' )),
    COMMETHOD([helpstring(u'Upgrades Geodatabase.')], HRESULT, 'Upgrade'),
    COMMETHOD(['propget', helpstring(u'The Data Server Manager object.')], HRESULT, 'DataServerManager',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'DataServerManager' )),
]
################################################################
## code template for IGxGeodatabase implementation
##class IGxGeodatabase_Impl(object):
##    def Upgrade(self):
##        u'Upgrades Geodatabase.'
##        #return 
##
##    @property
##    def DataServerManager(self):
##        u'The Data Server Manager object.'
##        #return DataServerManager
##
##    def DetachGeodatabase(self):
##        u'Detach a Geodatabase from a Data server.'
##        #return 
##
##    def GetProperties(self):
##        u'Backup information.'
##        #return Owner, creationDate, size, fileLocation, lastBackup
##
##    def Backup(self, backupName, backupFileName, Description):
##        u'Backs up a Geodatabase from a Data server.'
##        #return isSimpleRecoveryModel
##
##    @property
##    def GeodatabaseName(self, Name):
##        u'The Geodatabase name.'
##        #return 
##

class GxNewDatabase(CoClass):
    u'Shortcut to create new databases.'
    _reg_clsid_ = GUID('{BDBBB418-D0B2-11D1-AED9-080009EC734B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxNewDatabase(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that defines a new database shortcut.'
    _iid_ = GUID('{BDBBB3FF-D0B2-11D1-AED9-080009EC734B}')
    _idlflags_ = ['oleautomation']
GxNewDatabase._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxBasicObject, IGxNewDatabase, IGxObject, IGxObjectEdit, IGxObjectProperties, IGxObjectUI, IGxObjectWizard]

class GxDataset(CoClass):
    u'GxObject that represents a dataset.'
    _reg_clsid_ = GUID('{BDBBB412-D0B2-11D1-AED9-080009EC734B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxDataset._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxDataset, IGxObject, IGxObjectUI, IGxObjectContainer, IGxObjectProperties, IGxPasteTarget, IGxCachedObjects, IGxObjectEdit, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, IGxThumbnail, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IObjectClassSchemaEvents, IGxObjectInternalName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, IGxDataElement, IGxDataElementHelper]

class GxFilterRemoteMetadataContainer(CoClass):
    u'A filter for displaying containers of ArcIMS Metadata documents.'
    _reg_clsid_ = GUID('{A1C7449C-CEAB-427B-A10D-E92618E4F634}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterRemoteMetadataContainer._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxDatabaseFactory(CoClass):
    u'Esri GxDatabase object factory.'
    _reg_clsid_ = GUID('{65D77506-895C-11D2-AF5D-080009EC734B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxObjectFactoryMetadata(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that returns a GxObject from some metadata.'
    _iid_ = GUID('{5F31857E-62C8-415B-A126-F8EAE2F26F55}')
    _idlflags_ = ['oleautomation']
class IGxObjectFactoryFileExtensions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to a set of extensions handled by the factory.'
    _iid_ = GUID('{F61DC478-8F2E-43FA-9090-7FCCB8450E18}')
    _idlflags_ = ['oleautomation']
GxDatabaseFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFactory, IGxObjectFactoryMetadata, IGxObjectFactoryFileExtensions]

class GxSelection(CoClass):
    u"GxObject that represents the catalog's selection."
    _reg_clsid_ = GUID('{BDBBB414-D0B2-11D1-AED9-080009EC734B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxSelection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manages the selection within the catalog.'
    _iid_ = GUID('{BDBBB3ED-D0B2-11D1-AED9-080009EC734B}')
    _idlflags_ = ['oleautomation']
class IGxSelectionEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to events that the ArcCatalog selection can fire.'
    _iid_ = GUID('{BDBBB3F9-D0B2-11D1-AED9-080009EC734B}')
    _idlflags_ = ['oleautomation']
GxSelection._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxSelection, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IConnectionPointContainer]
GxSelection._outgoing_interfaces_ = [IGxSelectionEvents]

class IGxAGSCatalog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of GxObject that represents a ArcGIS Server data sharing object.'
    _iid_ = GUID('{DC95F566-575D-43C4-B0B3-0267CC7CC9DF}')
    _idlflags_ = ['oleautomation']
IGxAGSCatalog._methods_ = [
]
################################################################
## code template for IGxAGSCatalog implementation
##class IGxAGSCatalog_Impl(object):

class GxShortcutFactory(CoClass):
    u'Esri GxShortcut object factory.  This object is not supported on ArcGIS version 10.1. or later.'
    _reg_clsid_ = GUID('{287C39E0-6F68-4D11-9831-5A948FF96070}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxShortcutFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFactory, IGxObjectFactoryFileExtensions]

class GxFilterBasicTypes(CoClass):
    u'A filter for displaying basic types, like the catalog, disk connections, folders, etc.  Typically, other filters use this object internally.'
    _reg_clsid_ = GUID('{52F78821-299B-11D3-9F5B-00C04F6BC69E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterBasicTypes._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class IGxAGSDraftFolder(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of GxObject that represents a draft service folder object.'
    _iid_ = GUID('{D62FFFBE-FF58-40B3-BE97-275357E25D30}')
    _idlflags_ = ['oleautomation']
IGxAGSDraftFolder._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The AGS server connection.')], HRESULT, 'AGSServerConnectionName',
              ( ['in'], POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IAGSServerConnectionName), 'rhs' )),
    COMMETHOD(['propget', helpstring(u'The staging folder of this connection.')], HRESULT, 'StagingFolder',
              ( ['retval', 'out'], POINTER(BSTR), 'pFolderPath' )),
]
################################################################
## code template for IGxAGSDraftFolder implementation
##class IGxAGSDraftFolder_Impl(object):
##    def AGSServerConnectionName(self, rhs):
##        u'The AGS server connection.'
##        #return 
##
##    @property
##    def StagingFolder(self):
##        u'The staging folder of this connection.'
##        #return pFolderPath
##

class GxFilterCadFeatureClasses(CoClass):
    u'A filter for displaying/choosing Cad Feature Classes.'
    _reg_clsid_ = GUID('{71048673-CACF-11D4-A25E-444553547777}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterCadFeatureClasses._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class IMSGlobeSubServiceDescription(CoClass):
    u'ArcIMS Globe Sub Service.'
    _reg_clsid_ = GUID('{BC9381F5-DF2C-4739-ABEB-F4745AD92F47}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
IMSGlobeSubServiceDescription._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectUI, comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IIMSServiceDescription, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IIMSGlobeSubServiceDescription, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName]

class GxFolderConnections(CoClass):
    u'Container of folder connections.'
    _reg_clsid_ = GUID('{A213E820-71FD-4E21-851C-18FC7BE82268}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxRemoteContainer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Indicator interface that identifies an object that contains objects from a remote source.'
    _iid_ = GUID('{B0277E3E-917D-44F3-8860-D2C5E01AD215}')
    _idlflags_ = ['oleautomation']
GxFolderConnections._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectUI, IGxObjectContainer, IGxObjectEdit, IGxObjectProperties, IGxPasteTarget, IGxCachedObjects, IGxFolderConnections, IGxRemoteContainer, IGxDataElement, IGxDataElementHelper, IGxRootObjectStartupProperties, IGxRootObjectSortPriority]

class IGxWMTSConnection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members to connect to an WMTS server.'
    _iid_ = GUID('{617B2704-1614-40EF-84C5-668800065FBE}')
    _idlflags_ = []
IGxWMTSConnection._methods_ = [
    COMMETHOD(['propget', helpstring(u'Assosicated name object used to connect to a WMTS service.')], HRESULT, 'WMTSConnectionName',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IWMTSConnectionName)), 'connectionName' )),
    COMMETHOD(['propputref', helpstring(u'Assosicated name object used to connect to a WMTS service.')], HRESULT, 'WMTSConnectionName',
              ( ['in'], POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IWMTSConnectionName), 'connectionName' )),
    COMMETHOD([helpstring(u'Loads a WMTS connection file.')], HRESULT, 'LoadFromFile',
              ( ['in'], BSTR, 'Path' )),
    COMMETHOD([helpstring(u'Writes a WMTS connection file.')], HRESULT, 'SaveToFile',
              ( ['in'], BSTR, 'Path' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the server is connected to or not.')], HRESULT, 'IsConnected',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsConnected' )),
    COMMETHOD([helpstring(u'Connects to the WMTS service.')], HRESULT, 'Connect'),
    COMMETHOD([helpstring(u'Disconnects from the WMTS service.')], HRESULT, 'Disconnect'),
    COMMETHOD(['propget', helpstring(u'The description of WMTS service.')], HRESULT, 'WMTSServiceDescription',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IWMTSServiceDescription)), 'ppWMTSLayerDescription' )),
]
################################################################
## code template for IGxWMTSConnection implementation
##class IGxWMTSConnection_Impl(object):
##    def Disconnect(self):
##        u'Disconnects from the WMTS service.'
##        #return 
##
##    def SaveToFile(self, Path):
##        u'Writes a WMTS connection file.'
##        #return 
##
##    def LoadFromFile(self, Path):
##        u'Loads a WMTS connection file.'
##        #return 
##
##    @property
##    def WMTSServiceDescription(self):
##        u'The description of WMTS service.'
##        #return ppWMTSLayerDescription
##
##    @property
##    def IsConnected(self):
##        u'Indicates whether the server is connected to or not.'
##        #return IsConnected
##
##    def Connect(self):
##        u'Connects to the WMTS service.'
##        #return 
##
##    def WMTSConnectionName(self, connectionName):
##        u'Assosicated name object used to connect to a WMTS service.'
##        #return 
##

class IGxObjectFilterCollection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manages a collection of GxObject filters.'
    _iid_ = GUID('{41F5C02D-D9C8-11D3-A67D-0008C7D3AE8D}')
    _idlflags_ = ['oleautomation']
IGxObjectFilterCollection._methods_ = [
    COMMETHOD([helpstring(u'Add a filter to the filter collection, and specify if it is to selected by default.')], HRESULT, 'AddFilter',
              ( ['in'], POINTER(IGxObjectFilter), 'Filter' ),
              ( ['in'], VARIANT_BOOL, 'defaultFilter' )),
    COMMETHOD([helpstring(u'Remove all filters from the filter collection.')], HRESULT, 'RemoveAllFilters'),
]
################################################################
## code template for IGxObjectFilterCollection implementation
##class IGxObjectFilterCollection_Impl(object):
##    def RemoveAllFilters(self):
##        u'Remove all filters from the filter collection.'
##        #return 
##
##    def AddFilter(self, Filter, defaultFilter):
##        u'Add a filter to the filter collection, and specify if it is to selected by default.'
##        #return 
##

class GxObjectArray(CoClass):
    u'GxObject that represents an array of GxObjects.'
    _reg_clsid_ = GUID('{B330F488-DE4D-11D2-9F2F-00C04F6BC69E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxObjectArray._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectArray, IEnumGxObject]

class GxTextFileFactory(CoClass):
    u'Esri GxTextFile object factory.'
    _reg_clsid_ = GUID('{01FDEF6D-0D73-11D4-AE04-00C04FA33A15}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxObjectFactoryEdit(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u"Provides access to members that modify the object factory's properties."
    _iid_ = GUID('{527E3BAD-D8DF-11D3-A67D-0008C7D3AE8D}')
    _idlflags_ = ['oleautomation']
GxTextFileFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFactory, IGxObjectFactoryMetadata, IGxObjectFactoryEdit, IGxObjectFactoryFileExtensions]

class GxLayerFactory(CoClass):
    u'Esri GxLayer object factory.'
    _reg_clsid_ = GUID('{65D77508-895C-11D2-AF5D-080009EC734B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxLayerFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFactory, IGxObjectFactoryMetadata, IGxObjectFactoryFileExtensions]

class IMSConnectionNativeType(CoClass):
    u'Native type for an ArcIMS Connection.'
    _reg_clsid_ = GUID('{1C56F53D-EC49-4B5B-A990-BE113AF2303E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
IMSConnectionNativeType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeType]

class GxPackageFactory(CoClass):
    u'Layer or Map Package object factory.'
    _reg_clsid_ = GUID('{DF61D9CF-E5EE-4D5A-8454-CBE5402984FA}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxPackageFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFactory, IGxObjectFactoryMetadata, IGxObjectFactoryFileExtensions]

class IMSFeatureServiceNativeType(CoClass):
    u'Native type for a ArcIMS Feature Service.'
    _reg_clsid_ = GUID('{43AE6140-AC20-497F-91B5-8BE40FA486EA}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
IMSFeatureServiceNativeType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeSearch]

class IGxAGSWMServer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of GxObject that represents a ArcGIS Server Workflow Manager object.'
    _iid_ = GUID('{79CAECB0-C6D0-48FF-97F3-D94BF82A924D}')
    _idlflags_ = ['oleautomation']
IGxAGSWMServer._methods_ = [
]
################################################################
## code template for IGxAGSWMServer implementation
##class IGxAGSWMServer_Impl(object):

class GxDataServer(CoClass):
    u'The one and only Data Server object.'
    _reg_clsid_ = GUID('{9DA704AF-A694-4CB3-8E4B-F63E0BD9A241}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxDataServer._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectUI, IGxObjectProperties, IGxObjectWizard, IGxObjectContainer, IGxGDSConnection]

class GxFilterSDCNetworkDatasets(CoClass):
    u'A filter for displaying and choosing SDC network datasets.'
    _reg_clsid_ = GUID('{57C32778-72E7-4EC2-A873-B52DB887317C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterSDCNetworkDatasets._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class IMSMetadataServiceNativeType(CoClass):
    u'Native type for a ArcIMS Metadata Service.'
    _reg_clsid_ = GUID('{CADBA869-A488-4858-8431-B48A7A3371D8}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
IMSMetadataServiceNativeType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeType]

class GxSpatialWeightsMatrixFileFactory(CoClass):
    u'Spatial weights matrix file object factory.'
    _reg_clsid_ = GUID('{DE5DACF0-8341-4C14-9C62-CDFBD568116A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxSpatialWeightsMatrixFileFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFactory, IGxObjectFactoryMetadata, IGxObjectFactoryFileExtensions]

class GxTextFile(CoClass):
    u'GxObject that represents the text file.'
    _reg_clsid_ = GUID('{01FDEF6C-0D73-11D4-AE04-00C04FA33A15}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxTextFile._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxCachedObjects, IGxDataset, IGxFile, IGxFileSetup, IGxObject, IGxObjectEdit, IGxObjectInternalName, IGxObjectProperties, IGxObjectUI, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IObjectClassSchemaEvents, IGxTextFile, IGxDataElement, IGxDataElementHelper]

class IMSImageMapNativeType(CoClass):
    u'Native type for a ArcIMS ImageMap.'
    _reg_clsid_ = GUID('{D0032BA5-8CDA-490F-9E12-B662AACAFA39}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
IMSImageMapNativeType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeType]

class IGxAGSGlobeLayer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of GxObject that represents a layer in an ArcGIS Server globe object.'
    _iid_ = GUID('{186AECE5-9C47-44C9-B767-C468CE9C4ECC}')
    _idlflags_ = ['oleautomation']
IGxAGSGlobeLayer._methods_ = [
    COMMETHOD(['propget', helpstring(u'The associated AGS server object name.')], HRESULT, 'AGSServerObjectName',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IAGSServerObjectName)), 'agsObjectName' )),
    COMMETHOD(['propputref', helpstring(u'The associated AGS server object name.')], HRESULT, 'AGSServerObjectName',
              ( ['in'], POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IAGSServerObjectName), 'agsObjectName' )),
    COMMETHOD(['propget', helpstring(u'The information provided by the server.')], HRESULT, 'GlobeLayerInfo',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'layerInfo' )),
    COMMETHOD(['propputref', helpstring(u'The information provided by the server.')], HRESULT, 'GlobeLayerInfo',
              ( ['in'], POINTER(IUnknown), 'layerInfo' )),
]
################################################################
## code template for IGxAGSGlobeLayer implementation
##class IGxAGSGlobeLayer_Impl(object):
##    def GlobeLayerInfo(self, layerInfo):
##        u'The information provided by the server.'
##        #return 
##
##    def AGSServerObjectName(self, agsObjectName):
##        u'The associated AGS server object name.'
##        #return 
##

class GxRemoteDatabaseFolder(CoClass):
    u'Container of remote database workspaces.'
    _reg_clsid_ = GUID('{BDBBB417-D0B2-11D1-AED9-080009EC734B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxRemoteDatabaseFolder._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectUI, IGxObjectContainer, IGxObjectEdit, IGxObjectProperties, IGxPasteTarget, IGxCachedObjects, IGxRemoteDatabaseFolder, IGxRemoteContainer, IGxDataElement, IGxDataElementHelper, IGxRootObjectSortPriority]

class GxFileFactory(CoClass):
    u'Esri GxFile object factory.'
    _reg_clsid_ = GUID('{6E7C9CFF-944D-11D2-AF62-080009EC734B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFileFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFactory, IGxObjectFactoryMetadata, IGxObjectFactoryFileExtensions]

class GxToolboxesFolder(CoClass):
    u'Catalog object corresponding to the System Toolboxes and My Toolboxes nodes.'
    _reg_clsid_ = GUID('{0897C602-1625-46A4-B619-63D896C9D309}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxToolboxesFolder(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to properties/methods of a catalog toolboxes folder object.'
    _iid_ = GUID('{9F8371BE-98E8-4A07-A83A-CFC8331FE926}')
    _idlflags_ = ['oleautomation']
GxToolboxesFolder._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectUI, IGxObjectEdit, IGxObjectProperties, IGxObjectContainer, IGxPasteTarget, IGxCachedObjects, IGxToolboxesFolder]

class IGxWMSConnection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members to connect to an WMS server.'
    _iid_ = GUID('{924E350D-E6B5-4457-AE3C-70C6A598C07B}')
    _idlflags_ = []
IGxWMSConnection._methods_ = [
    COMMETHOD(['propget', helpstring(u'Assosicated name object used to connect to a WMS service.')], HRESULT, 'WMSConnectionName',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IWMSConnectionName)), 'connectionName' )),
    COMMETHOD(['propputref', helpstring(u'Assosicated name object used to connect to a WMS service.')], HRESULT, 'WMSConnectionName',
              ( ['in'], POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IWMSConnectionName), 'connectionName' )),
    COMMETHOD([helpstring(u'Loads a WMS connection file.')], HRESULT, 'LoadFromFile',
              ( ['in'], BSTR, 'Path' )),
    COMMETHOD([helpstring(u'Writes a WMS connection file.')], HRESULT, 'SaveToFile',
              ( ['in'], BSTR, 'Path' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the server is connected to or not.')], HRESULT, 'IsConnected',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsConnected' )),
    COMMETHOD([helpstring(u'Connects to the WMS service.')], HRESULT, 'Connect'),
    COMMETHOD([helpstring(u'Disconnects from the WMS service.')], HRESULT, 'Disconnect'),
]
################################################################
## code template for IGxWMSConnection implementation
##class IGxWMSConnection_Impl(object):
##    def Disconnect(self):
##        u'Disconnects from the WMS service.'
##        #return 
##
##    def LoadFromFile(self, Path):
##        u'Loads a WMS connection file.'
##        #return 
##
##    def WMSConnectionName(self, connectionName):
##        u'Assosicated name object used to connect to a WMS service.'
##        #return 
##
##    @property
##    def IsConnected(self):
##        u'Indicates whether the server is connected to or not.'
##        #return IsConnected
##
##    def Connect(self):
##        u'Connects to the WMS service.'
##        #return 
##
##    def SaveToFile(self, Path):
##        u'Writes a WMS connection file.'
##        #return 
##

class IGxAGSGeoprocessing(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of GxObject that represents a ArcGIS Server geoprocessing object.'
    _iid_ = GUID('{22610358-89BE-4677-9F63-E24F3061444F}')
    _idlflags_ = ['oleautomation']
IGxAGSGeoprocessing._methods_ = [
]
################################################################
## code template for IGxAGSGeoprocessing implementation
##class IGxAGSGeoprocessing_Impl(object):

class GxFilterSDCTables(CoClass):
    u'A filter for displaying and choosing SDC tables.'
    _reg_clsid_ = GUID('{0AC47545-F1AC-4BE0-A3DB-8038A075C5FF}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterSDCTables._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

IGxDataElement._methods_ = [
    COMMETHOD([helpstring(u"Get the GxObject's data element.")], HRESULT, 'GetDataElement',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEBrowseOptions), 'browseOptions' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElement)), 'dataElement' )),
]
################################################################
## code template for IGxDataElement implementation
##class IGxDataElement_Impl(object):
##    def GetDataElement(self, browseOptions):
##        u"Get the GxObject's data element."
##        #return dataElement
##

class GxGISServersFolder(CoClass):
    u'Container of GIS servers.'
    _reg_clsid_ = GUID('{DB6890D0-F90E-424A-A41C-486FB7E0F0F1}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxGISServersFolder(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manages the properties of a GISServers root folder.'
    _iid_ = GUID('{CC37FE42-5DAD-4567-9C76-B41B29C58468}')
    _idlflags_ = ['oleautomation']
GxGISServersFolder._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectUI, IGxObjectContainer, IGxGISServersFolder, IGxRemoteContainer, IGxRootObjectSortPriority]

class IMSMetadataDocumentNativeType(CoClass):
    u'Native type for a ArcIMS Metadata Document.'
    _reg_clsid_ = GUID('{3B4A9F32-D220-4D75-8127-12F2E8C14445}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
IMSMetadataDocumentNativeType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeType]

class IGxAGSGlobe(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of GxObject that represents a ArcGIS Server globe object.'
    _iid_ = GUID('{E9E6F5D8-3120-4E2E-8239-7AACEEE42CB6}')
    _idlflags_ = ['oleautomation']
IGxAGSGlobe._methods_ = [
]
################################################################
## code template for IGxAGSGlobe implementation
##class IGxAGSGlobe_Impl(object):

class GxWorkspaceFolder(CoClass):
    u'GxObject that represents a workspace folder.'
    _reg_clsid_ = GUID('{A58934AD-0EC4-4B18-9AE3-DE3A7221302B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxWorkspaceFolder._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxWorkspaceFolder, IGxFolder, IGxFolderAdmin, IGxObject, IGxObjectUI, IGxObjectContainer, IGxObjectEdit, IGxPasteTarget, IGxCachedObjects, IGxFile, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, IGxObjectInternalName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, IGxObjectProperties, IGxDataElement, IGxDataElementHelper, IGxDisplayName]

class GxExcelFactory(CoClass):
    u'Esri GxExcel object factory.'
    _reg_clsid_ = GUID('{AFC83112-936C-4213-B10D-88BF185936FE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxExcelFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFactory, IGxObjectFactoryMetadata, IGxObjectFactoryFileExtensions]

class WMSConnectionNativeType(CoClass):
    u'The native type of WMS connection.'
    _reg_clsid_ = GUID('{AE2865F2-DEFD-4465-A2FA-ACA33378ABD7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
WMSConnectionNativeType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeType]

class GxDiskConnection(CoClass):
    u'GxObject that represents a disk connection.'
    _reg_clsid_ = GUID('{BDBBB41A-D0B2-11D1-AED9-080009EC734B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxDiskConnection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Indicator interface that identifies an object that represents a connection to disk.'
    _iid_ = GUID('{BDBBB402-D0B2-11D1-AED9-080009EC734B}')
    _idlflags_ = ['oleautomation']
class IGxDiskConnection2(IGxDiskConnection):
    _case_insensitive_ = True
    u'Provides access to members that manage properties of GX disk connection.'
    _iid_ = GUID('{C9BB82E5-1801-4EE9-9DFF-0EFF01A7B016}')
    _idlflags_ = ['oleautomation']
GxDiskConnection._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxDiskConnection, IGxDiskConnection2, IGxObject, IGxObjectEdit, IGxObjectContainer, IGxObjectInternalName, IGxObjectProperties, IGxObjectUI, IGxPasteTarget, IGxCachedObjects, IGxFile, IGxFolder, IGxFolderAdmin, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, IGxDataElement, IGxDataElementHelper, IGxDisplayName]


# values for enumeration 'esriSynchronizationOption'
esriSyncNever = 0
esriSyncCreated = 1
esriSyncAccessed = 2
esriSyncNotCreated = 3
esriSynchronizationOption = c_int # enum
class MetadataNativeType(CoClass):
    u'Native type for standalone metadata.'
    _reg_clsid_ = GUID('{02C7EA2C-356A-4BFB-B559-883E1B1D0D59}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
MetadataNativeType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeType]

class GxGeoprocessingFileFactory(CoClass):
    u'GX Geoprocessing File object factory.'
    _reg_clsid_ = GUID('{01F055EF-E421-419B-A047-F645D96D7084}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxGeoprocessingFileFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFactory, IGxObjectFactoryFileExtensions]

class GxMetadata(CoClass):
    u'GxObject that represents an XML file.'
    _reg_clsid_ = GUID('{159AA449-DBF4-11D2-9F92-00C04F8ED211}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxMetadata._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxFile, IGxObject, IGxObjectEdit, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, IGxObjectInternalName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, IGxObjectProperties, IGxObjectUI]

class GxCadDataset(CoClass):
    u'A Cad Feature Class or Drawing dataset.'
    _reg_clsid_ = GUID('{83EEE9B8-0CB1-11D3-9B35-00C04FA33299}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxCadDataset._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxDataset, IGxObject, IGxObjectUI, IGxPasteTarget, IGxCachedObjects, IGxObjectEdit, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, IGxThumbnail, IGxObjectContainer, IGxObjectProperties, IGxObjectInternalName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, IGxDataElement, IGxDataElementHelper]

class IGxAGSConnection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of GxObject that connects to an ArcGIS server (AGS).'
    _iid_ = GUID('{85E89175-26EF-490B-8FCC-9363399275BB}')
    _idlflags_ = ['oleautomation']
IGxAGSConnection._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates whether the AGS connection has been made.')], HRESULT, 'IsConnected',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsConnected' )),
    COMMETHOD([helpstring(u'Connects to an ArcGIS server.')], HRESULT, 'Connect'),
    COMMETHOD([helpstring(u'Disconnects from an ArcGIS server.')], HRESULT, 'Disconnect'),
    COMMETHOD([helpstring(u'Loads an AGS connection file.')], HRESULT, 'LoadFromFile',
              ( ['in'], BSTR, 'Path' )),
    COMMETHOD([helpstring(u'Writes an AGS connection file.')], HRESULT, 'SaveToFile',
              ( ['in'], BSTR, 'Path' )),
    COMMETHOD(['propget', helpstring(u'Path to the AGS connection file.')], HRESULT, 'FileName',
              ( ['retval', 'out'], POINTER(BSTR), 'FileName' )),
    COMMETHOD(['propget', helpstring(u'The associated AGS server connection name object.')], HRESULT, 'AGSServerConnectionName',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IAGSServerConnectionName)), 'serverConnName' )),
    COMMETHOD(['propputref', helpstring(u'The associated AGS server connection name object.')], HRESULT, 'AGSServerConnectionName',
              ( ['in'], POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IAGSServerConnectionName), 'serverConnName' )),
    COMMETHOD(['propget', helpstring(u'The selected server objects.')], HRESULT, 'SelectedServerObjects',
              ( ['retval', 'out'], POINTER(VARIANT), 'SelectedObjects' )),
    COMMETHOD(['propput', helpstring(u'The selected server objects.')], HRESULT, 'SelectedServerObjects',
              ( ['in'], VARIANT, 'SelectedObjects' )),
    COMMETHOD([helpstring(u'Presents a modal dialog to allow editing the default properties of the server.')], HRESULT, 'EditServerProperties',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hParent' ),
              ( ['in'], c_short, 'activePage' )),
]
################################################################
## code template for IGxAGSConnection implementation
##class IGxAGSConnection_Impl(object):
##    def SaveToFile(self, Path):
##        u'Writes an AGS connection file.'
##        #return 
##
##    def LoadFromFile(self, Path):
##        u'Loads an AGS connection file.'
##        #return 
##
##    def _get(self):
##        u'The selected server objects.'
##        #return SelectedObjects
##    def _set(self, SelectedObjects):
##        u'The selected server objects.'
##    SelectedServerObjects = property(_get, _set, doc = _set.__doc__)
##
##    def EditServerProperties(self, hParent, activePage):
##        u'Presents a modal dialog to allow editing the default properties of the server.'
##        #return 
##
##    @property
##    def IsConnected(self):
##        u'Indicates whether the AGS connection has been made.'
##        #return IsConnected
##
##    @property
##    def FileName(self):
##        u'Path to the AGS connection file.'
##        #return FileName
##
##    def Connect(self):
##        u'Connects to an ArcGIS server.'
##        #return 
##
##    def AGSServerConnectionName(self, serverConnName):
##        u'The associated AGS server connection name object.'
##        #return 
##
##    def Disconnect(self):
##        u'Disconnects from an ArcGIS server.'
##        #return 
##

class IGxWMSLayer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members GxWMSLayer object.'
    _iid_ = GUID('{A257840D-7628-498C-B3CA-CC9584B3B47A}')
    _idlflags_ = []
IGxWMSLayer._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The description of WMS service.')], HRESULT, 'WMSServiceDescription',
              ( ['in'], POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IWMSServiceDescription), 'ppWMSServiceDescription' )),
    COMMETHOD(['propget', helpstring(u'The description of WMS service.')], HRESULT, 'WMSServiceDescription',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IWMSServiceDescription)), 'ppWMSServiceDescription' )),
    COMMETHOD(['propputref', helpstring(u'The description of WMS layer.')], HRESULT, 'WMSLayerDescription',
              ( ['in'], POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IWMSLayerDescription), 'ppWMSLayerDescription' )),
    COMMETHOD(['propget', helpstring(u'The description of WMS layer.')], HRESULT, 'WMSLayerDescription',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IWMSLayerDescription)), 'ppWMSLayerDescription' )),
]
################################################################
## code template for IGxWMSLayer implementation
##class IGxWMSLayer_Impl(object):
##    @property
##    def WMSServiceDescription(self, ppWMSServiceDescription):
##        u'The description of WMS service.'
##        #return 
##
##    @property
##    def WMSLayerDescription(self, ppWMSLayerDescription):
##        u'The description of WMS layer.'
##        #return 
##

class GxCadFactory(CoClass):
    u'Gx Cad Feature Class and Drawing object factory.'
    _reg_clsid_ = GUID('{83EEE9B7-0CB1-11D3-9B35-00C04FA33299}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxCadFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFactory, IGxObjectFactoryMetadata, IGxObjectFactoryFileExtensions]

IGxDatabase._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The workspace name.')], HRESULT, 'WorkspaceName',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceName), 'WorkspaceName' )),
    COMMETHOD(['propget', helpstring(u'The workspace name.')], HRESULT, 'WorkspaceName',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceName)), 'WorkspaceName' )),
    COMMETHOD(['propget', helpstring(u'The associated workspace.')], HRESULT, 'Workspace',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspace)), 'Workspace' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the database is remote.')], HRESULT, 'IsRemoteDatabase',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsRemoteDatabase' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the database is connected.')], HRESULT, 'IsConnected',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsConnected' )),
    COMMETHOD([helpstring(u'Disconnects or releases the connection to the underlying database.')], HRESULT, 'Disconnect'),
]
################################################################
## code template for IGxDatabase implementation
##class IGxDatabase_Impl(object):
##    @property
##    def IsRemoteDatabase(self):
##        u'Indicates if the database is remote.'
##        #return IsRemoteDatabase
##
##    def Disconnect(self):
##        u'Disconnects or releases the connection to the underlying database.'
##        #return 
##
##    @property
##    def IsConnected(self):
##        u'Indicates if the database is connected.'
##        #return IsConnected
##
##    @property
##    def Workspace(self):
##        u'The associated workspace.'
##        #return Workspace
##
##    @property
##    def WorkspaceName(self, WorkspaceName):
##        u'The workspace name.'
##        #return 
##

class GxStreetMapDataset(CoClass):
    u'A StreetMap feature class.'
    _reg_clsid_ = GUID('{D9EA7450-C103-434A-962D-CFE7036E2CCC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxStreetMapDataset._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxDataset, IGxObject, IGxObjectUI, IGxCachedObjects, IGxObjectEdit, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, IGxThumbnail, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, IGxObjectInternalName, IGxObjectProperties, IGxDataElement, IGxDataElementHelper]

class GxPCCoverage(CoClass):
    u'GxObject that represents PC Coverage.'
    _reg_clsid_ = GUID('{C65A2BBC-32ED-11D3-9F33-00C04F79927C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxPCCoverage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxCachedObjects, IGxDataset, IGxObject, IGxObjectContainer, IGxObjectEdit, IGxObjectProperties, IGxObjectUI, IGxPasteTarget, IGxThumbnail, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, IGxObjectInternalName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo]

class GxFilterInfoTables(CoClass):
    u'A filter for displaying/choosing info tables.'
    _reg_clsid_ = GUID('{29652E4E-E65E-11D3-A682-0008C7D3AE8D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterInfoTables._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeType]

class IGxWCSConnection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members to connect to an WCS server.'
    _iid_ = GUID('{A722FD16-1D3B-4365-A656-7FEC86379D19}')
    _idlflags_ = []
IGxWCSConnection._methods_ = [
    COMMETHOD(['propget', helpstring(u'Assosicated name object used to connect to a WCS service.')], HRESULT, 'WCSConnectionName',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IWCSConnectionName)), 'connectionName' )),
    COMMETHOD(['propputref', helpstring(u'Assosicated name object used to connect to a WCS service.')], HRESULT, 'WCSConnectionName',
              ( ['in'], POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IWCSConnectionName), 'connectionName' )),
    COMMETHOD([helpstring(u'Loads a WCS connection file.')], HRESULT, 'LoadFromFile',
              ( ['in'], BSTR, 'Path' )),
    COMMETHOD([helpstring(u'Writes a WCS connection file.')], HRESULT, 'SaveToFile',
              ( ['in'], BSTR, 'Path' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the server is connected to or not.')], HRESULT, 'IsConnected',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsConnected' )),
    COMMETHOD([helpstring(u'Connects to the WCS service.')], HRESULT, 'Connect'),
    COMMETHOD([helpstring(u'Disconnects from the WCS service.')], HRESULT, 'Disconnect'),
]
################################################################
## code template for IGxWCSConnection implementation
##class IGxWCSConnection_Impl(object):
##    def SaveToFile(self, Path):
##        u'Writes a WCS connection file.'
##        #return 
##
##    def WCSConnectionName(self, connectionName):
##        u'Assosicated name object used to connect to a WCS service.'
##        #return 
##
##    def LoadFromFile(self, Path):
##        u'Loads a WCS connection file.'
##        #return 
##
##    @property
##    def IsConnected(self):
##        u'Indicates whether the server is connected to or not.'
##        #return IsConnected
##
##    def Connect(self):
##        u'Connects to the WCS service.'
##        #return 
##
##    def Disconnect(self):
##        u'Disconnects from the WCS service.'
##        #return 
##

class GxPre70Coverage(CoClass):
    u'GxObject that represents Pre-7.0 Coverage.'
    _reg_clsid_ = GUID('{06D6440A-2F3C-11D3-9F33-00C04F79927C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxPre70Coverage(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Gx Pre-7.0 Coverage.'
    _iid_ = GUID('{C65A2BB9-32ED-11D3-9F33-00C04F79927C}')
    _idlflags_ = ['oleautomation']
GxPre70Coverage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxPre70Coverage, IGxObject, IGxObjectEdit, IGxObjectProperties, IGxObjectUI, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo]

class IMetadataImport(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that define a metadata importer.'
    _iid_ = GUID('{E5FB4CEF-660C-11D3-A68B-0008C7D3AE50}')
    _idlflags_ = ['oleautomation']
IMetadataImport._methods_ = [
    COMMETHOD(['propget', helpstring(u'Name of the metadata importer.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'Default filename (including the file extension) from which to import.')], HRESULT, 'DefaultFilename',
              ( ['retval', 'out'], POINTER(BSTR), 'FileName' )),
    COMMETHOD([helpstring(u'Imports metadata from the specified location.')], HRESULT, 'Import',
              ( ['in'], BSTR, 'source' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata), 'destination' )),
]
################################################################
## code template for IMetadataImport implementation
##class IMetadataImport_Impl(object):
##    def Import(self, source, destination):
##        u'Imports metadata from the specified location.'
##        #return 
##
##    @property
##    def Name(self):
##        u'Name of the metadata importer.'
##        #return Name
##
##    @property
##    def DefaultFilename(self):
##        u'Default filename (including the file extension) from which to import.'
##        #return FileName
##

class IGxDataGraph2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control data graph GxObject.'
    _iid_ = GUID('{ED598D6E-0A34-442B-8250-E3B0C53DF0FD}')
    _idlflags_ = ['oleautomation']
IGxDataGraph2._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The data graph associated with GXObject.')], HRESULT, 'DataGraphBase',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDataGraphBase), 'dataGraph' )),
    COMMETHOD(['propget', helpstring(u'The data graph associated with GXObject.')], HRESULT, 'DataGraphBase',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDataGraphBase)), 'dataGraph' )),
]
################################################################
## code template for IGxDataGraph2 implementation
##class IGxDataGraph2_Impl(object):
##    @property
##    def DataGraphBase(self, dataGraph):
##        u'The data graph associated with GXObject.'
##        #return 
##

class DataGraphNativeType(CoClass):
    u'Native type for a data graph.'
    _reg_clsid_ = GUID('{B1431594-098A-11D4-A676-0008C7DF88DB}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
DataGraphNativeType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeType]

class GxReportFactory(CoClass):
    u'Report object factory.'
    _reg_clsid_ = GUID('{24F2B6FE-6A51-4A5A-83B1-9FF2496ABB62}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxReportFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFactory, IGxObjectFactoryMetadata, IGxObjectFactoryFileExtensions]

class GxFileFilter(CoClass):
    u"The catalog's file filter."
    _reg_clsid_ = GUID('{BDBBB415-D0B2-11D1-AED9-080009EC734B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxFileFilter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manage a file filter for various file types.'
    _iid_ = GUID('{BDBBB3F7-D0B2-11D1-AED9-080009EC734B}')
    _idlflags_ = ['oleautomation']
class IGxFileFilterEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to events that the ArcCatalog file filter can fire.'
    _iid_ = GUID('{BDBBB3FA-D0B2-11D1-AED9-080009EC734B}')
    _idlflags_ = ['oleautomation']
GxFileFilter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxFileFilter, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream]
GxFileFilter._outgoing_interfaces_ = [IGxFileFilterEvents]

class IGxWCSCoverage(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members GxWCSCoverage object.'
    _iid_ = GUID('{75EA50E7-10A2-4F9E-BF24-A8CFD72BF6E0}')
    _idlflags_ = []
IGxWCSCoverage._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The description of WCS coverage.')], HRESULT, 'WCSCoverageDescription',
              ( ['in'], POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IWCSCoverageDescription), 'ppWCSCoverageDescription' )),
    COMMETHOD(['propget', helpstring(u'The description of WCS coverage.')], HRESULT, 'WCSCoverageDescription',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IWCSCoverageDescription)), 'ppWCSCoverageDescription' )),
]
################################################################
## code template for IGxWCSCoverage implementation
##class IGxWCSCoverage_Impl(object):
##    @property
##    def WCSCoverageDescription(self, ppWCSCoverageDescription):
##        u'The description of WCS coverage.'
##        #return 
##

IGxSelection._methods_ = [
    COMMETHOD(['propget', helpstring(u'The location of the selection.')], HRESULT, 'Location',
              ( ['retval', 'out'], POINTER(POINTER(IGxObject)), 'Location' )),
    COMMETHOD([helpstring(u'Clears the selection and sets a new location.')], HRESULT, 'SetLocation',
              ( ['in'], POINTER(IGxObject), 'Location' ),
              ( [], POINTER(IUnknown), 'pInitiator' )),
    COMMETHOD(['propget', helpstring(u'The number of selected objects.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'The first object in the selection.')], HRESULT, 'FirstObject',
              ( ['retval', 'out'], POINTER(POINTER(IGxObject)), 'firstSelectedObject' )),
    COMMETHOD(['propput', helpstring(u'Delays or resumes selection event firing.  If the selection changed while events were being delayed, a single event is fired when events are resumed.')], HRESULT, 'DelayEvents',
              ( ['in'], VARIANT_BOOL, 'DelayEvents' )),
    COMMETHOD(['propget', helpstring(u'Delays or resumes selection event firing.  If the selection changed while events were being delayed, a single event is fired when events are resumed.')], HRESULT, 'DelayEvents',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'DelayEvents' )),
    COMMETHOD([helpstring(u'Selects an object, optionally appending it to the existing selection.')], HRESULT, 'Select',
              ( ['in'], POINTER(IGxObject), 'object' ),
              ( ['in'], VARIANT_BOOL, 'appendToExistingSelection' ),
              ( ['in'], POINTER(IUnknown), 'initiator' )),
    COMMETHOD([helpstring(u'Unselects an object.')], HRESULT, 'Unselect',
              ( ['in'], POINTER(IGxObject), 'object' ),
              ( ['in'], POINTER(IUnknown), 'initiator' )),
    COMMETHOD([helpstring(u'Checks if an object is selected.')], HRESULT, 'IsSelected',
              ( ['in'], POINTER(IGxObject), 'object' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsSelected' )),
    COMMETHOD([helpstring(u'Unselects all objects.')], HRESULT, 'Clear',
              ( ['in'], POINTER(IUnknown), 'initiator' )),
    COMMETHOD(['propget', helpstring(u'The objects in the selection.')], HRESULT, 'SelectedObjects',
              ( ['retval', 'out'], POINTER(POINTER(IEnumGxObject)), 'SelectedObjects' )),
]
################################################################
## code template for IGxSelection implementation
##class IGxSelection_Impl(object):
##    @property
##    def Count(self):
##        u'The number of selected objects.'
##        #return Count
##
##    def Unselect(self, object, initiator):
##        u'Unselects an object.'
##        #return 
##
##    def Clear(self, initiator):
##        u'Unselects all objects.'
##        #return 
##
##    def IsSelected(self, object):
##        u'Checks if an object is selected.'
##        #return IsSelected
##
##    @property
##    def FirstObject(self):
##        u'The first object in the selection.'
##        #return firstSelectedObject
##
##    @property
##    def Location(self):
##        u'The location of the selection.'
##        #return Location
##
##    def SetLocation(self, Location, pInitiator):
##        u'Clears the selection and sets a new location.'
##        #return 
##
##    @property
##    def SelectedObjects(self):
##        u'The objects in the selection.'
##        #return SelectedObjects
##
##    def Select(self, object, appendToExistingSelection, initiator):
##        u'Selects an object, optionally appending it to the existing selection.'
##        #return 
##
##    def _get(self):
##        u'Delays or resumes selection event firing.  If the selection changed while events were being delayed, a single event is fired when events are resumed.'
##        #return DelayEvents
##    def _set(self, DelayEvents):
##        u'Delays or resumes selection event firing.  If the selection changed while events were being delayed, a single event is fired when events are resumed.'
##    DelayEvents = property(_get, _set, doc = _set.__doc__)
##

class GxFilterWorkspaces(CoClass):
    u'A filter for displaying/choosing workspaces.'
    _reg_clsid_ = GUID('{9E14BC32-19F4-11D3-9F55-00C04F6BC69E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterWorkspaces._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

IGxExcelFile._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The workspace name.')], HRESULT, 'WorkspaceName',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceName), 'WorkspaceName' )),
    COMMETHOD(['propget', helpstring(u'The workspace name.')], HRESULT, 'WorkspaceName',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceName)), 'WorkspaceName' )),
    COMMETHOD(['propget', helpstring(u'The associated workspace.')], HRESULT, 'Workspace',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspace)), 'Workspace' )),
]
################################################################
## code template for IGxExcelFile implementation
##class IGxExcelFile_Impl(object):
##    @property
##    def Workspace(self):
##        u'The associated workspace.'
##        #return Workspace
##
##    @property
##    def WorkspaceName(self, WorkspaceName):
##        u'The workspace name.'
##        #return 
##

class Pre70CoverageNativeType(CoClass):
    u'Native type for pre-7.0 coverages.'
    _reg_clsid_ = GUID('{A8E6EDE6-B96D-4498-BCA6-BE3F4C03999E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
Pre70CoverageNativeType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeType]

class GxPCCoverageFactory(CoClass):
    u'Esri GxPCCoverage object factory.'
    _reg_clsid_ = GUID('{C65A2BBA-32ED-11D3-9F33-00C04F79927C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxPCCoverageFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFactory, IGxObjectFactoryMetadata, IGxObjectFactoryFileExtensions]

class GxFilterCoverages(CoClass):
    u'A filter for displaying/choosing coverages.'
    _reg_clsid_ = GUID('{31EFC1A3-E655-11D3-A682-0008C7D3AE8D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterCoverages._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeType]

class IMetadataExport(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that define a metadata exporter.'
    _iid_ = GUID('{E5FB4CF0-660C-11D3-A68B-0008C7D3AE50}')
    _idlflags_ = ['oleautomation']
IMetadataExport._methods_ = [
    COMMETHOD(['propget', helpstring(u'Name of the metadata exporter.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'Default filename (including the file extension) to create on export.')], HRESULT, 'DefaultFilename',
              ( ['retval', 'out'], POINTER(BSTR), 'FileName' )),
    COMMETHOD([helpstring(u'Exports metadata to the specified location.')], HRESULT, 'Export',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata), 'source' ),
              ( ['in'], BSTR, 'destination' )),
]
################################################################
## code template for IMetadataExport implementation
##class IMetadataExport_Impl(object):
##    def Export(self, source, destination):
##        u'Exports metadata to the specified location.'
##        #return 
##
##    @property
##    def Name(self):
##        u'Name of the metadata exporter.'
##        #return Name
##
##    @property
##    def DefaultFilename(self):
##        u'Default filename (including the file extension) to create on export.'
##        #return FileName
##

class IGxWMTSLayer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members GxWMTSLayer object.'
    _iid_ = GUID('{44ACB999-3E3F-43EB-865F-A9959B5B4F3A}')
    _idlflags_ = []
IGxWMTSLayer._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The description of WMTS service.')], HRESULT, 'WMTSServiceDescription',
              ( ['in'], POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IWMTSServiceDescription), 'ppWMTSServiceDescription' )),
    COMMETHOD(['propget', helpstring(u'The description of WMTS service.')], HRESULT, 'WMTSServiceDescription',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IWMTSServiceDescription)), 'ppWMTSServiceDescription' )),
    COMMETHOD(['propputref', helpstring(u'The description of WMTS layer.')], HRESULT, 'WMTSLayerDescription',
              ( ['in'], POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IWMTSLayerDescription), 'ppWMTSLayerDescription' )),
    COMMETHOD(['propget', helpstring(u'The description of WMTS layer.')], HRESULT, 'WMTSLayerDescription',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IWMTSLayerDescription)), 'ppWMTSLayerDescription' )),
]
################################################################
## code template for IGxWMTSLayer implementation
##class IGxWMTSLayer_Impl(object):
##    @property
##    def WMTSLayerDescription(self, ppWMTSLayerDescription):
##        u'The description of WMTS layer.'
##        #return 
##
##    @property
##    def WMTSServiceDescription(self, ppWMTSServiceDescription):
##        u'The description of WMTS service.'
##        #return 
##

class GxDataGraph(CoClass):
    u'GxObject that represents data graph.'
    _reg_clsid_ = GUID('{B143158F-098A-11D4-A676-0008C7DF88DB}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxDataGraph._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxDataGraph2, IGxObject, IGxObjectUI, IGxObjectEdit, IGxFile, IGxThumbnail, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, IGxObjectInternalName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, IGxObjectProperties, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IComPropertySheetEvents]


# values for enumeration 'esriFindFieldType'
esriFindFieldTypeFullText = 0
esriFindFieldTypeTitle = 1
esriFindFieldTypeEdition = 2
esriFindFieldTypeOriginator = 3
esriFindFieldTypeSourceAgency = 4
esriFindFieldTypeAbstract = 5
esriFindFieldTypePurpose = 6
esriFindFieldTypeGeoForm = 7
esriFindFieldTypeTheme = 8
esriFindFieldTypePlace = 9
esriFindFieldTypeStratum = 10
esriFindFieldTypeTemporal = 11
esriFindFieldTypeEntity = 12
esriFindFieldTypeAttribute = 13
esriFindFieldTypeLineage = 14
esriFindFieldTypeSourceScale = 15
esriFindFieldTypeCloudCover = 16
esriFindFieldTypeProgress = 17
esriFindFieldTypeUserDefined = 18
esriFindFieldTypeDataTheme = 19
esriFindFieldType = c_int # enum
class GxCoverageDataset(CoClass):
    u'A Coverage, Feature Class or Info Table dataset.'
    _reg_clsid_ = GUID('{7D80306C-E319-11D2-9F30-00C04F79927C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxCoverageDataset._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxCachedObjects, IGxDataset, IGxObject, IGxObjectContainer, IGxObjectEdit, IGxObjectInternalName, IGxObjectProperties, IGxObjectUI, IGxPasteTarget, IGxThumbnail, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IObjectClassSchemaEvents, IGxDataElement, IGxDataElementHelper]

class GxDataGraphFactory(CoClass):
    u'Data graph GxObject factory.'
    _reg_clsid_ = GUID('{048DBEB5-0988-11D4-A676-0008C7DF88DB}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxDataGraphFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFactory, IGxObjectFactoryFileExtensions]

class GxCoverageFactory(CoClass):
    u'Gx Coverage, Feature Class and INFO Table object factory.'
    _reg_clsid_ = GUID('{9C9641D1-DD54-11D2-9F30-00C04F79927C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxObjectFactoryPriority(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manages the priority of a GxObject factory.'
    _iid_ = GUID('{36F2BA2C-D538-4652-A089-82BE069EAB65}')
    _idlflags_ = ['oleautomation']
GxCoverageFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFactory, IGxObjectFactoryEdit, IGxObjectFactoryMetadata, IGxObjectFactoryFileExtensions, IGxObjectFactoryPriority]

class GxPre70CoverageFactory(CoClass):
    u'Esri GxPre70Coverage object factory.'
    _reg_clsid_ = GUID('{06D64408-2F3C-11D3-9F33-00C04F79927C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxPre70CoverageFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFactory, IGxObjectFactoryFileExtensions]

class IGxAGSGeoDataServer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of GxObject that represents a ArcGIS Server geodataserver object.'
    _iid_ = GUID('{9CD68F19-59BD-4985-8E10-D4B4A62779A3}')
    _idlflags_ = ['oleautomation']
IGxAGSGeoDataServer._methods_ = [
]
################################################################
## code template for IGxAGSGeoDataServer implementation
##class IGxAGSGeoDataServer_Impl(object):

class GxMetadataFactory(CoClass):
    u'A factory for creating GxMetadata objects to show XML files in the Catalog.'
    _reg_clsid_ = GUID('{FA57CC27-DC0F-11D2-9F92-00C04F8ED211}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxMetadataFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFactory, IGxObjectFactoryMetadata, IGxObjectFactoryPriority, IGxObjectFactoryFileExtensions]

class GxStreetMapFactory(CoClass):
    u'Gx StreetMap object factory.'
    _reg_clsid_ = GUID('{7EEFACAA-0108-41C6-A502-D9E924624166}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxStreetMapFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFactory, IGxObjectFactoryMetadata, IGxObjectFactoryFileExtensions]

class GxFilterTerrains(CoClass):
    u'A filter for displaying/choosing Terrains datasets.'
    _reg_clsid_ = GUID('{6E51AF1C-C8AD-4A63-A24F-0E3480AFDED5}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterTerrains._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxFilterStreetMapFeatureClasses(CoClass):
    u'A filter for displaying and choosing StreetMap feature classes.'
    _reg_clsid_ = GUID('{00F1A235-5AC3-4DB8-930F-70353DCC4988}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterStreetMapFeatureClasses._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxFilterPolylineFeatureClasses(CoClass):
    u'A filter for displaying/choosing polyline feature classes.'
    _reg_clsid_ = GUID('{9E14BC40-19F4-11D3-9F55-00C04F6BC69E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterPolylineFeatureClasses._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxVpfFactory(CoClass):
    u'Gx VPF Feature Datasets and Table object factory.'
    _reg_clsid_ = GUID('{397847FA-C865-11D3-9B56-00C04FA33299}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxVpfFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFactory, IGxObjectFactoryMetadata, IGxObjectFactoryFileExtensions]

class GxFilterLayers(CoClass):
    u'A filter for displaying/choosing layers.'
    _reg_clsid_ = GUID('{9E14BC38-19F4-11D3-9F55-00C04F6BC69E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterLayers._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersion]

class IMSFeatureClass(CoClass):
    u'GxObject that represents ArcIMS Feature Class.'
    _reg_clsid_ = GUID('{7CC18907-AA8E-4E9B-A01D-A7B6AE3038DA}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
IMSFeatureClass._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectUI, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, IGxCachedObjects, IGxDataset, IGxObject, IGxObjectContainer, IGxObjectEdit, IGxObjectInternalName, IGxObjectProperties, IGxPasteTarget, IGxThumbnail, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IObjectClassSchemaEvents]

class GxFilterTINDatasets(CoClass):
    u'A filter for displaying/choosing TIN datasets.'
    _reg_clsid_ = GUID('{B9EA9FDC-1AB7-11D3-9F55-00C04F6BC69E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterTINDatasets._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxFilterRasterDatasets(CoClass):
    u'A filter for displaying/choosing raster datasets.'
    _reg_clsid_ = GUID('{B9EA9FDB-1AB7-11D3-9F55-00C04F6BC69E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterRasterDatasets._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

IGxObjectFactories._methods_ = [
    COMMETHOD(['propget', helpstring(u'The number of registered GxObject factories.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Indicates if a specific GxObject factory is enabled.')], HRESULT, 'IsEnabled',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsEnabled' )),
    COMMETHOD([helpstring(u'Enables or disables a GxObject factory.')], HRESULT, 'EnableGxObjectFactory',
              ( [], c_int, 'index' ),
              ( [], VARIANT_BOOL, 'Enabled' )),
    COMMETHOD(['propget', helpstring(u'The class ID of the specified GxObject factory.')], HRESULT, 'GxObjectFactoryCLSID',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID)), 'ClassID' )),
    COMMETHOD(['propget', helpstring(u'The specified GxObject factory.')], HRESULT, 'GxObjectFactory',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IGxObjectFactory)), 'objFactory' )),
    COMMETHOD(['propget', helpstring(u'The enabled GxObject factories (sorted by priority).')], HRESULT, 'EnabledGxObjectFactories',
              ( ['retval', 'out'], POINTER(POINTER(IEnumGxObjectFactory)), 'objFactories' )),
]
################################################################
## code template for IGxObjectFactories implementation
##class IGxObjectFactories_Impl(object):
##    @property
##    def Count(self):
##        u'The number of registered GxObject factories.'
##        #return Count
##
##    @property
##    def GxObjectFactoryCLSID(self, index):
##        u'The class ID of the specified GxObject factory.'
##        #return ClassID
##
##    @property
##    def IsEnabled(self, index):
##        u'Indicates if a specific GxObject factory is enabled.'
##        #return IsEnabled
##
##    def EnableGxObjectFactory(self, index, Enabled):
##        u'Enables or disables a GxObject factory.'
##        #return 
##
##    @property
##    def GxObjectFactory(self, index):
##        u'The specified GxObject factory.'
##        #return objFactory
##
##    @property
##    def EnabledGxObjectFactories(self):
##        u'The enabled GxObject factories (sorted by priority).'
##        #return objFactories
##

class GxSDCDataset(CoClass):
    u'A SDC feature dataset, feature class or table.'
    _reg_clsid_ = GUID('{EBB6D1E5-F977-4921-83D0-9EE9C2B24ACF}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxSDCDataset._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxDataset, IGxObject, IGxObjectUI, IGxCachedObjects, IGxObjectEdit, IGxObjectContainer, IGxPasteTarget, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, IGxThumbnail, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, IGxObjectInternalName, IGxObjectProperties, IGxDataElement, IGxDataElementHelper]

class GxFilterSDCFeatureClasses(CoClass):
    u'A filter for displaying and choosing SDC feature classes.'
    _reg_clsid_ = GUID('{9E43FCDB-1C2E-44BB-8543-305A06546D69}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterSDCFeatureClasses._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

IGxRootObjectStartupProperties._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates whether the Root level Object will be visible during startup.')], HRESULT, 'Enabled',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsEnabled' )),
]
################################################################
## code template for IGxRootObjectStartupProperties implementation
##class IGxRootObjectStartupProperties_Impl(object):
##    @property
##    def Enabled(self):
##        u'Indicates whether the Root level Object will be visible during startup.'
##        #return IsEnabled
##

class GNValidator(CoClass):
    u'Esri Geography Network Metadata Validator.'
    _reg_clsid_ = GUID('{8DC9C31A-4323-408E-91A4-B2C6F12275B8}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IMetadataValidator(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods to validate metadata.'
    _iid_ = GUID('{C9575F93-39E5-4CBA-BEF6-50E598CF058D}')
    _idlflags_ = ['oleautomation']
GNValidator._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMetadataValidator]

IGxToolboxesRoot._methods_ = [
]
################################################################
## code template for IGxToolboxesRoot implementation
##class IGxToolboxesRoot_Impl(object):

class GxSDCFactory(CoClass):
    u'Gx SDC object factory.'
    _reg_clsid_ = GUID('{CE8C6AF8-F111-47D8-9B20-AE8C52B96CEF}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxSDCFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFactory, IGxObjectFactoryMetadata, IGxObjectFactoryFileExtensions]

IGxToolboxesFolder._methods_ = [
    COMMETHOD(['propget', helpstring(u'The value of the Path property.')], HRESULT, 'Path',
              ( ['retval', 'out'], POINTER(BSTR), 'Path' )),
]
################################################################
## code template for IGxToolboxesFolder implementation
##class IGxToolboxesFolder_Impl(object):
##    @property
##    def Path(self):
##        u'The value of the Path property.'
##        #return Path
##

class IGxAddGISServerCommand(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manages Add GIS Server command.'
    _iid_ = GUID('{CCDCCE1B-D6D4-4E54-B01B-375F2AA53AE9}')
    _idlflags_ = ['oleautomation']
IGxAddGISServerCommand._methods_ = [
    COMMETHOD([helpstring(u'An enumeration of the child objects.')], HRESULT, 'GetChildren',
              ( ['retval', 'out'], POINTER(POINTER(IEnumGxObject)), 'Children' )),
]
################################################################
## code template for IGxAddGISServerCommand implementation
##class IGxAddGISServerCommand_Impl(object):
##    def GetChildren(self):
##        u'An enumeration of the child objects.'
##        #return Children
##


# values for enumeration 'esriContentType'
esriContentTypeNone = 0
esriContentTypeData = 1
esriContentTypeLiveData = 2
esriContentTypeDownloadableData = 3
esriContentTypeOfflineData = 4
esriContentTypeDocuments = 5
esriContentTypeStaticMapImages = 6
esriContentTypeOtherDocuments = 7
esriContentTypeResources = 8
esriContentTypeApplications = 9
esriContentTypeGeographicServices = 10
esriContentTypeClearinghouses = 11
esriContentTypeMapFiles = 12
esriContentTypeGeographicActivities = 13
esriContentType = c_int # enum

# values for enumeration 'esriFindDateOperator'
esriFindDateOperatorPrevious = 0
esriFindDateOperatorBefore = 1
esriFindDateOperatorDuring = 2
esriFindDateOperatorEqual = 3
esriFindDateOperatorAfter = 4
esriFindDateOperator = c_int # enum

# values for enumeration 'esriFindEnvelopeOperator'
esriFindEnvelopeOperatorWithin = 0
esriFindEnvelopeOperatorOverlaps = 1
esriFindEnvelopeOperator = c_int # enum
class IGxMetadataSupport(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to information for metadata toolbar.'
    _iid_ = GUID('{ECDD192B-F45C-4159-8725-D7658BCE0C57}')
    _idlflags_ = ['oleautomation']
IGxMetadataSupport._methods_ = [
    COMMETHOD(['propget', helpstring(u'Retrive metadata editor.')], HRESULT, 'Editor',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID)), 'Editor' )),
    COMMETHOD(['propget', helpstring(u'Retrieve stylesheet path.')], HRESULT, 'StylesheetPath',
              ( ['retval', 'out'], POINTER(BSTR), 'Path' )),
]
################################################################
## code template for IGxMetadataSupport implementation
##class IGxMetadataSupport_Impl(object):
##    @property
##    def StylesheetPath(self):
##        u'Retrieve stylesheet path.'
##        #return Path
##
##    @property
##    def Editor(self):
##        u'Retrive metadata editor.'
##        #return Editor
##

class GxFilterFileGeodatabases(CoClass):
    u'A filter for displaying/choosing file geodatabases.'
    _reg_clsid_ = GUID('{2A76401E-E2FB-4732-A7F1-AC8216383315}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterFileGeodatabases._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxGeoprocessingResultNativeType(CoClass):
    u'Geoprocessing Result Native Type.'
    _reg_clsid_ = GUID('{01AB1F19-9DBF-48B7-A3D9-D9566562E0ED}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxGeoprocessingResultNativeType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeType]

class GxFilterDataGraphs(CoClass):
    u'A filter for displaying or choosing data graphs.'
    _reg_clsid_ = GUID('{B143159F-098A-11D4-A676-0008C7DF88DB}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterDataGraphs._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]


# values for enumeration 'esriFindDateType'
esriFindDateTypeNone = 0
esriFindDateTypeContent = 1
esriFindDateTypePublication = 2
esriFindDateTypeMetadata = 3
esriFindDateType = c_int # enum
class IQuery(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that let you modify a query.'
    _iid_ = GUID('{4EA3E4EB-9DFA-11D3-A6CB-0008C7D3AE50}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriFindFieldOperator'
esriFindFieldOperatorIncludes = 0
esriFindFieldOperatorEquals = 1
esriFindFieldOperatorExists = 2
esriFindFieldOperatorEqualTo = 3
esriFindFieldOperatorGreaterThan = 4
esriFindFieldOperatorGreaterThanOrEqualTo = 5
esriFindFieldOperatorLessThan = 6
esriFindFieldOperatorLessThanOrEqualTo = 7
esriFindFieldOperatorNotEqualTo = 8
esriFindFieldOperator = c_int # enum
IQuery._methods_ = [
    COMMETHOD(['propget', helpstring(u'Name of the query.')], HRESULT, 'NameOfQuery',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propput', helpstring(u'Name of the query.')], HRESULT, 'NameOfQuery',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD(['propget', helpstring(u'Name of the dataset for which to search.')], HRESULT, 'DatasetName',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propput', helpstring(u'Name of the dataset for which to search.')], HRESULT, 'DatasetName',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD(['propget', helpstring(u'Indicates if field query comparisons will be case sensitive.')], HRESULT, 'IsCaseSensitive',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsCaseSensitive' )),
    COMMETHOD(['propput', helpstring(u'Indicates if field query comparisons will be case sensitive.')], HRESULT, 'IsCaseSensitive',
              ( ['in'], VARIANT_BOOL, 'IsCaseSensitive' )),
    COMMETHOD(['propget', helpstring(u'Type of object for which to search.')], HRESULT, 'DatasetType',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeType)), 'ppNativeType' )),
    COMMETHOD(['propputref', helpstring(u'Type of object for which to search.')], HRESULT, 'DatasetType',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeType), 'ppNativeType' )),
    COMMETHOD(['propget', helpstring(u'Search extent in decimal degrees.')], HRESULT, 'Envelope',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'ppEnvelope' )),
    COMMETHOD(['propputref', helpstring(u'Search extent in decimal degrees.')], HRESULT, 'Envelope',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'ppEnvelope' )),
    COMMETHOD(['propget', helpstring(u"Search extent in the dataset's coordinate system.")], HRESULT, 'NativeEnvelope',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'ppEnvelope' )),
    COMMETHOD(['propputref', helpstring(u"Search extent in the dataset's coordinate system.")], HRESULT, 'NativeEnvelope',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'ppEnvelope' )),
    COMMETHOD(['propget', helpstring(u"Operator for comparing the dataset's extent to the search extent.")], HRESULT, 'EnvelopeOperator',
              ( ['retval', 'out'], POINTER(esriFindEnvelopeOperator), 'pOp' )),
    COMMETHOD(['propput', helpstring(u"Operator for comparing the dataset's extent to the search extent.")], HRESULT, 'EnvelopeOperator',
              ( ['in'], esriFindEnvelopeOperator, 'pOp' )),
    COMMETHOD(['propget', helpstring(u'Date that will be tested.')], HRESULT, 'DateType',
              ( ['retval', 'out'], POINTER(esriFindDateType), 'Type' )),
    COMMETHOD(['propput', helpstring(u'Date that will be tested.')], HRESULT, 'DateType',
              ( ['in'], esriFindDateType, 'Type' )),
    COMMETHOD(['propget', helpstring(u'Operator for comparing dates.')], HRESULT, 'DateOperator',
              ( ['retval', 'out'], POINTER(esriFindDateOperator), 'op' )),
    COMMETHOD(['propput', helpstring(u'Operator for comparing dates.')], HRESULT, 'DateOperator',
              ( ['in'], esriFindDateOperator, 'op' )),
    COMMETHOD(['propget', helpstring(u'Start date, or first date.')], HRESULT, 'Date1',
              ( ['retval', 'out'], POINTER(BSTR), 'date' )),
    COMMETHOD(['propput', helpstring(u'Start date, or first date.')], HRESULT, 'Date1',
              ( ['in'], BSTR, 'date' )),
    COMMETHOD(['propget', helpstring(u'End date, or second date.')], HRESULT, 'Date2',
              ( ['retval', 'out'], POINTER(BSTR), 'date' )),
    COMMETHOD(['propput', helpstring(u'End date, or second date.')], HRESULT, 'Date2',
              ( ['in'], BSTR, 'date' )),
    COMMETHOD(['propget', helpstring(u'Number of field queries.')], HRESULT, 'NumFieldQueries',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD([helpstring(u'Returns the nth field query.')], HRESULT, 'GetFieldQuery',
              ( ['in'], c_int, 'index' ),
              ( ['out'], POINTER(esriFindFieldType), 'Type' ),
              ( ['out'], POINTER(esriFindFieldOperator), 'op' ),
              ( ['out'], POINTER(BSTR), 'value' ),
              ( ['out'], POINTER(BSTR), 'tag' )),
    COMMETHOD([helpstring(u'Adds a field query.')], HRESULT, 'AddFieldQuery',
              ( ['in'], esriFindFieldType, 'Type' ),
              ( ['in'], esriFindFieldOperator, 'op' ),
              ( ['in'], BSTR, 'value' ),
              ( ['in'], BSTR, 'tag' )),
    COMMETHOD(['propget', helpstring(u'Class ID indicating the type of query object that has been defined.')], HRESULT, 'ClassID',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID)), 'ClassID' )),
    COMMETHOD([helpstring(u"Loads the query's parameters from the given XML property set.")], HRESULT, 'Load',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'pPropertySet' )),
    COMMETHOD([helpstring(u"Saves the query's parameters to the given XML property set.")], HRESULT, 'Save',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'pPropertySet' )),
    COMMETHOD(['propget', helpstring(u'Property set containing properties of the search engine that will be used to execute the query.')], HRESULT, 'EngineProperties',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'ppPropertySet' )),
]
################################################################
## code template for IQuery implementation
##class IQuery_Impl(object):
##    def _get(self):
##        u'Operator for comparing dates.'
##        #return op
##    def _set(self, op):
##        u'Operator for comparing dates.'
##    DateOperator = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Start date, or first date.'
##        #return date
##    def _set(self, date):
##        u'Start date, or first date.'
##    Date1 = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Name of the dataset for which to search.'
##        #return Name
##    def _set(self, Name):
##        u'Name of the dataset for which to search.'
##    DatasetName = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'End date, or second date.'
##        #return date
##    def _set(self, date):
##        u'End date, or second date.'
##    Date2 = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u"Operator for comparing the dataset's extent to the search extent."
##        #return pOp
##    def _set(self, pOp):
##        u"Operator for comparing the dataset's extent to the search extent."
##    EnvelopeOperator = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def EngineProperties(self):
##        u'Property set containing properties of the search engine that will be used to execute the query.'
##        #return ppPropertySet
##
##    def Save(self, pPropertySet):
##        u"Saves the query's parameters to the given XML property set."
##        #return 
##
##    def _get(self):
##        u'Indicates if field query comparisons will be case sensitive.'
##        #return IsCaseSensitive
##    def _set(self, IsCaseSensitive):
##        u'Indicates if field query comparisons will be case sensitive.'
##    IsCaseSensitive = property(_get, _set, doc = _set.__doc__)
##
##    def Envelope(self, ppEnvelope):
##        u'Search extent in decimal degrees.'
##        #return 
##
##    @property
##    def ClassID(self):
##        u'Class ID indicating the type of query object that has been defined.'
##        #return ClassID
##
##    def GetFieldQuery(self, index):
##        u'Returns the nth field query.'
##        #return Type, op, value, tag
##
##    def NativeEnvelope(self, ppEnvelope):
##        u"Search extent in the dataset's coordinate system."
##        #return 
##
##    def AddFieldQuery(self, Type, op, value, tag):
##        u'Adds a field query.'
##        #return 
##
##    def _get(self):
##        u'Name of the query.'
##        #return Name
##    def _set(self, Name):
##        u'Name of the query.'
##    NameOfQuery = property(_get, _set, doc = _set.__doc__)
##
##    def Load(self, pPropertySet):
##        u"Loads the query's parameters from the given XML property set."
##        #return 
##
##    def DatasetType(self, ppNativeType):
##        u'Type of object for which to search.'
##        #return 
##
##    def _get(self):
##        u'Date that will be tested.'
##        #return Type
##    def _set(self, Type):
##        u'Date that will be tested.'
##    DateType = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def NumFieldQueries(self):
##        u'Number of field queries.'
##        #return Count
##

class GxFilterSDCFeatureDatasets(CoClass):
    u'A filter for displaying and choosing SDC feature datasets.'
    _reg_clsid_ = GUID('{56A3FEB8-8EF6-4EF6-8053-96A0B36A9CE6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterSDCFeatureDatasets._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxFilterTools(CoClass):
    u'Object used to filter for geoprocessing Tools.'
    _reg_clsid_ = GUID('{AB8B13B2-0CC4-43A6-8F15-D669A1B4007B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterTools._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxFilterCadDrawingDatasets(CoClass):
    u'A filter for displaying/choosing Cad Drawing datasets.'
    _reg_clsid_ = GUID('{B4EAA08B-2B4F-11D3-9B38-00C04FA33299}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterCadDrawingDatasets._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class IGxAGSFeatureServer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of GxObject that represents a ArcGIS Server feature server object.'
    _iid_ = GUID('{0BEA8F63-2B61-47D0-91C1-BEF76FC71193}')
    _idlflags_ = ['oleautomation']
IGxAGSFeatureServer._methods_ = [
]
################################################################
## code template for IGxAGSFeatureServer implementation
##class IGxAGSFeatureServer_Impl(object):

class GxFilterGeoDatasets(CoClass):
    u'A filter for displaying/choosing geographic datasets.'
    _reg_clsid_ = GUID('{2C16657F-6572-11D3-9FBE-00C04F6BC78E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterGeoDatasets._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class IGxWorkspaceDatabase(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Indicator interface for GxWorkspaceDatabase objects.'
    _iid_ = GUID('{06F48F3E-5028-4C19-B2D7-189F5560ACEA}')
    _idlflags_ = ['oleautomation']
IGxWorkspaceDatabase._methods_ = [
]
################################################################
## code template for IGxWorkspaceDatabase implementation
##class IGxWorkspaceDatabase_Impl(object):

class IGxDocument(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that returns the open status of a document.'
    _iid_ = GUID('{67E567D1-F2BB-4193-AA3F-54A6B53454C9}')
    _idlflags_ = ['oleautomation']
IGxDocument._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if this document is the current open document.')], HRESULT, 'IsOpen',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsOpen' )),
]
################################################################
## code template for IGxDocument implementation
##class IGxDocument_Impl(object):
##    @property
##    def IsOpen(self):
##        u'Indicates if this document is the current open document.'
##        #return IsOpen
##

class GxFilterFGDBFeatureClasses(CoClass):
    u'A filter for displaying/choosing file geodatabase feature classes.'
    _reg_clsid_ = GUID('{29C0E38D-06DB-4F58-B1AE-FCF63907E3E0}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterFGDBFeatureClasses._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GPToolNativeType(CoClass):
    u'Geoprocessing Tool Native Type.'
    _reg_clsid_ = GUID('{4F4AE537-051A-4A54-B82C-A38F3278DDB2}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GPToolNativeType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeType]

class GxGeoprocessingResultFactory(CoClass):
    u'Esri GxGeoprocessingResult object factory.'
    _reg_clsid_ = GUID('{30AAAF00-3551-4D75-84A3-CF909DC563F8}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxGeoprocessingResultFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFactory, IGxObjectFactoryMetadata, IGxObjectFactoryFileExtensions]

class IGxDefaultDatabase(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that returns default state of a database.'
    _iid_ = GUID('{79CC0043-A0FE-4447-BB08-48663ECCF74D}')
    _idlflags_ = ['oleautomation']
IGxDefaultDatabase._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if this database is the current default database.')], HRESULT, 'IsDefault',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsDefault' )),
]
################################################################
## code template for IGxDefaultDatabase implementation
##class IGxDefaultDatabase_Impl(object):
##    @property
##    def IsDefault(self):
##        u'Indicates if this database is the current default database.'
##        #return IsDefault
##

IGxMapPageLayout._methods_ = [
    COMMETHOD(['propget', helpstring(u'The page layout object in the map document.')], HRESULT, 'PageLayout',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IPageLayout)), 'PageLayout' )),
]
################################################################
## code template for IGxMapPageLayout implementation
##class IGxMapPageLayout_Impl(object):
##    @property
##    def PageLayout(self):
##        u'The page layout object in the map document.'
##        #return PageLayout
##

class GxFilterRunningCachedService(CoClass):
    u'A filter for displaying / choosing cached running service.'
    _reg_clsid_ = GUID('{8D26A3F8-CA7F-433D-9BEE-A20A5234B497}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterRunningCachedService._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxGeoprocessingResult(CoClass):
    u'GxObject that represents a Geoprocessing Result.'
    _reg_clsid_ = GUID('{5C1D8167-6A7B-4618-898A-3E2BA09604BA}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxGeoprocessingResult._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxGeoprocessingResult, IGxObject, IGxObjectUI, IGxObjectEdit, IGxFile, IGxThumbnail, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, IGxObjectInternalName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, IGxObjectProperties]

class GxFilterMapServersTilingScheme(CoClass):
    u'A filter for displaying/choosing map service tiling scheme.'
    _reg_clsid_ = GUID('{6FFCED7C-7A5F-4663-A628-B3D4EB683A7E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterMapServersTilingScheme._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

IGxFileSetup._methods_ = [
    COMMETHOD(['propput', helpstring(u'The category of the object.')], HRESULT, 'Category',
              ( ['in'], BSTR, 'rhs' )),
    COMMETHOD([helpstring(u'The images used to represent the object.')], HRESULT, 'SetImages',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hSmallImageBitmap' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hSmallImageSelectedBitmap' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hLargeImageBitmap' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hLargeImageSelectedBitmap' )),
]
################################################################
## code template for IGxFileSetup implementation
##class IGxFileSetup_Impl(object):
##    def _set(self, rhs):
##        u'The category of the object.'
##    Category = property(fset = _set, doc = _set.__doc__)
##
##    def SetImages(self, hSmallImageBitmap, hSmallImageSelectedBitmap, hLargeImageBitmap, hLargeImageSelectedBitmap):
##        u'The images used to represent the object.'
##        #return 
##

class GxFilterFiles(CoClass):
    u'A filter for displaying/choosing files.'
    _reg_clsid_ = GUID('{BEA72057-1D22-11D3-9F55-00C04F6BC69E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterFiles._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

IGxLayerSource._methods_ = [
]
################################################################
## code template for IGxLayerSource implementation
##class IGxLayerSource_Impl(object):

class GxFilterFGDBFeatureDatasets(CoClass):
    u'A filter for displaying/choosing file geodatabase feature datasets.'
    _reg_clsid_ = GUID('{84CC333F-C1CD-457A-BD0B-1E457058887F}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterFGDBFeatureDatasets._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

IGxRootObjectSortPriority._methods_ = [
    COMMETHOD(['propget', helpstring(u'Returns the sort priority for the Root level Object.')], HRESULT, 'SortPriority',
              ( ['retval', 'out'], POINTER(c_int), 'Priority' )),
]
################################################################
## code template for IGxRootObjectSortPriority implementation
##class IGxRootObjectSortPriority_Impl(object):
##    @property
##    def SortPriority(self):
##        u'Returns the sort priority for the Root level Object.'
##        #return Priority
##

IGxRemoteConnection._methods_ = [
    COMMETHOD([helpstring(u'Connects to a remote data source.')], HRESULT, 'Connect'),
    COMMETHOD([helpstring(u'Disconnects to a remote data source.')], HRESULT, 'Disconnect'),
]
################################################################
## code template for IGxRemoteConnection implementation
##class IGxRemoteConnection_Impl(object):
##    def Disconnect(self):
##        u'Disconnects to a remote data source.'
##        #return 
##
##    def Connect(self):
##        u'Connects to a remote data source.'
##        #return 
##

class GxFilterFGDBTables(CoClass):
    u'A filter for displaying/choosing file geodatabase tables.'
    _reg_clsid_ = GUID('{CA2B8CFA-4119-4C43-B55D-61B62420ACDE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterFGDBTables._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxTool(CoClass):
    u'Catalog object corresponding to geoprocessing tools.'
    _reg_clsid_ = GUID('{4796F40C-DE5D-4397-A5F7-91E8E755A552}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxGPTool(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to properties/methods of a catalog geoprocessing tool object.'
    _iid_ = GUID('{68C7A493-B394-479F-82BB-1C317DADB734}')
    _idlflags_ = ['oleautomation']
GxTool._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectUI, IGxObjectProperties, IGxCachedObjects, IGxObjectEdit, IGxObjectInternalName, IGxMetadataSupport, IGxGPTool, IGxObjectWizard, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, IGxDataset]

class GxFilterSpatialReferences(CoClass):
    u'A filter for displaying/choosing spatial references.'
    _reg_clsid_ = GUID('{9E14BC39-19F4-11D3-9F55-00C04F6BC69E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterSpatialReferences._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

IGxDatabase2._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The workspace name.')], HRESULT, 'WorkspaceName',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceName), 'WorkspaceName' )),
    COMMETHOD(['propget', helpstring(u'The workspace name.')], HRESULT, 'WorkspaceName',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceName)), 'WorkspaceName' )),
    COMMETHOD(['propget', helpstring(u'The associated workspace.')], HRESULT, 'Workspace',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspace)), 'Workspace' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the database is remote.')], HRESULT, 'IsRemoteDatabase',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsRemoteDatabase' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the database is connected.')], HRESULT, 'IsConnected',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsConnected' )),
    COMMETHOD([helpstring(u'Disconnects or releases the connection to the underlying database.')], HRESULT, 'Disconnect'),
    COMMETHOD(['propget', helpstring(u'Indicates if the database is an enterprise geodatabase.')], HRESULT, 'IsEnterpriseGeodatabase',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsEnterpriseGeodatabase' )),
    COMMETHOD([helpstring(u'Connectsto the underlying database.')], HRESULT, 'Connect'),
]
################################################################
## code template for IGxDatabase2 implementation
##class IGxDatabase2_Impl(object):
##    def Disconnect(self):
##        u'Disconnects or releases the connection to the underlying database.'
##        #return 
##
##    @property
##    def WorkspaceName(self, WorkspaceName):
##        u'The workspace name.'
##        #return 
##
##    @property
##    def IsConnected(self):
##        u'Indicates if the database is connected.'
##        #return IsConnected
##
##    @property
##    def IsEnterpriseGeodatabase(self):
##        u'Indicates if the database is an enterprise geodatabase.'
##        #return IsEnterpriseGeodatabase
##
##    @property
##    def IsRemoteDatabase(self):
##        u'Indicates if the database is remote.'
##        #return IsRemoteDatabase
##
##    def Connect(self):
##        u'Connectsto the underlying database.'
##        #return 
##
##    @property
##    def Workspace(self):
##        u'The associated workspace.'
##        #return Workspace
##

class SearchResultsIdentifyObj(CoClass):
    u'An object for identifying the contents of a search results layer.  This object is not supported on ArcGIS version 10.1. or later.'
    _reg_clsid_ = GUID('{39169D70-931F-45F4-9A0A-0DB897CB1F80}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class ISearchResultsIdentifyObject(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that identify an object in the search results layer.'
    _iid_ = GUID('{6ECFBC99-B4EE-4471-A81D-BAB3FEA34E3A}')
    _idlflags_ = ['oleautomation']
SearchResultsIdentifyObj._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IIdentifyObj, ISearchResultsIdentifyObject]

class GxFilterPGDBFeatureClasses(CoClass):
    u'A filter for displaying/choosing personal geodatabase feature classes.'
    _reg_clsid_ = GUID('{402A9394-E951-11D3-A682-0008C7D3AE8D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterPGDBFeatureClasses._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxFilterPGDBFeatureDatasets(CoClass):
    u'A filter for displaying/choosing personal geodatabase feature datasets.'
    _reg_clsid_ = GUID('{402A9395-E951-11D3-A682-0008C7D3AE8D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterPGDBFeatureDatasets._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

IGxPackage._methods_ = [
    COMMETHOD(['propget', helpstring(u'GxPackage type.')], HRESULT, 'PackageType',
              ( ['retval', 'out'], POINTER(esriGxPackageType), 'Type' )),
]
################################################################
## code template for IGxPackage implementation
##class IGxPackage_Impl(object):
##    @property
##    def PackageType(self):
##        u'GxPackage type.'
##        #return Type
##

class GxFilterFileToolboxes(CoClass):
    u'Object used to filter for file-based Toolboxes.'
    _reg_clsid_ = GUID('{ED934B15-8E0C-48D5-96BA-EE0803192DE5}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterFileToolboxes._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class IGxFilterSearchServers(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manage the properties of a GxFilterSearchServer object.'
    _iid_ = GUID('{CD161E5D-F30E-4CA0-B8B5-DFEDD52FC68B}')
    _idlflags_ = ['oleautomation']
IGxFilterSearchServers._methods_ = [
    COMMETHOD(['propput', helpstring(u'The connection type.')], HRESULT, 'ConnectionType',
              ( ['in'], comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.esriAGSConnectionType, 'rhs' )),
]
################################################################
## code template for IGxFilterSearchServers implementation
##class IGxFilterSearchServers_Impl(object):
##    def _set(self, rhs):
##        u'The connection type.'
##    ConnectionType = property(fset = _set, doc = _set.__doc__)
##

class IGxDatabaseExtensionCompare(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that defines whether something is a database extension.'
    _iid_ = GUID('{B526F7BE-4EB3-11D3-9F52-00C04F6BDF06}')
    _idlflags_ = ['oleautomation']
IGxDatabaseExtensionCompare._methods_ = [
    COMMETHOD(['propget', helpstring(u'The extension manager.')], HRESULT, 'ExtensionManager',
              ( ['retval', 'out'], POINTER(POINTER(IGxDatabaseExtension)), 'ExtensionManager' )),
    COMMETHOD(['propputref', helpstring(u'The extension manager.')], HRESULT, 'ExtensionManager',
              ( ['in'], POINTER(IGxDatabaseExtension), 'ExtensionManager' )),
]
################################################################
## code template for IGxDatabaseExtensionCompare implementation
##class IGxDatabaseExtensionCompare_Impl(object):
##    def ExtensionManager(self, ExtensionManager):
##        u'The extension manager.'
##        #return 
##

class GxToolboxFactory(CoClass):
    u'GX Toolbox object factory.'
    _reg_clsid_ = GUID('{0308EB86-6E11-4AF8-B819-7B0A11B85E9A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxToolboxFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFactory, IGxObjectFactoryFileExtensions]

class GxMapFactory(CoClass):
    u'Esri GxMap object factory.'
    _reg_clsid_ = GUID('{65D77507-895C-11D2-AF5D-080009EC734B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxMapFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFactory, IGxObjectFactoryMetadata, IGxObjectFactoryFileExtensions]

class GxFilterCadAnnotationClasses(CoClass):
    u'A filter for displaying/choosing Cad Annotation Classes.'
    _reg_clsid_ = GUID('{059C25ED-C7DD-11D4-9BCE-00C04FA33299}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterCadAnnotationClasses._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxToolset(CoClass):
    u'Catalog object corresponding to toolsets.'
    _reg_clsid_ = GUID('{4A7874DE-0020-4F35-8955-CB414813FE78}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxGPToolbox(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to properties/methods of a catalog toolbox object.'
    _iid_ = GUID('{0A51D075-7EF9-447B-A78F-96449FF6DFA8}')
    _idlflags_ = ['oleautomation']
GxToolset._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectUI, IGxObjectEdit, IGxObjectProperties, IGxObjectContainer, IGxCachedObjects, IGxGPToolbox]

class GxFilterVerticalCoordinateSystems(CoClass):
    u'A filter for displaying/choosing vertical coordinate systems.'
    _reg_clsid_ = GUID('{BBA46C4C-47B8-4931-8F8A-EB59ECEC90B4}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterVerticalCoordinateSystems._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxFilterFileFolder(CoClass):
    u'A filter for displaying/choosing file system folder.'
    _reg_clsid_ = GUID('{6BD87813-FF82-414C-BD3D-2E396EF35C21}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterFileFolder._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxAGSGlobeLayer(CoClass):
    u'GxObject that represents a layer in an ArcGIS Server globe object.'
    _reg_clsid_ = GUID('{F37B65E1-C26C-4429-9EE5-F410EAA363C3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxAGSGlobeLayer._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectEdit, IGxObjectUI, IGxAGSGlobeLayer, IGxLayerSource, IGxObjectContainer]

class GxAddAGSObject(CoClass):
    u'The one and only GxAddAGSObject object.'
    _reg_clsid_ = GUID('{0E3941FA-02EB-44C7-BCAB-7824C92FD8EC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxAddAGSObject._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectUI, IGxBasicObject, IGxObjectProperties, IGxObjectWizard]

class GxAGSConnectionFactory(CoClass):
    u'Esri GxAGSConnection object factory.'
    _reg_clsid_ = GUID('{9B922A82-6E91-41B0-B294-312244B698B4}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxAGSConnectionFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFactory, IGxObjectFactoryFileExtensions]

IGxObjectProperties._methods_ = [
    COMMETHOD(['propget', helpstring(u'The number of properties in the GxObject.')], HRESULT, 'PropertyCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD([helpstring(u'The name and value of the indexed property in the GxObject.')], HRESULT, 'GetPropByIndex',
              ( ['in'], c_int, 'index' ),
              ( ['in', 'out'], POINTER(BSTR), 'Name' ),
              ( ['in', 'out'], POINTER(VARIANT), 'value' )),
    COMMETHOD([helpstring(u'The value of the named property in the GxObject.')], HRESULT, 'GetProperty',
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'value' )),
    COMMETHOD([helpstring(u'Set the value of the named property in the GxObject.')], HRESULT, 'SetProperty',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], VARIANT, 'value' )),
]
################################################################
## code template for IGxObjectProperties implementation
##class IGxObjectProperties_Impl(object):
##    def SetProperty(self, Name, value):
##        u'Set the value of the named property in the GxObject.'
##        #return 
##
##    def GetProperty(self, Name):
##        u'The value of the named property in the GxObject.'
##        #return value
##
##    @property
##    def PropertyCount(self):
##        u'The number of properties in the GxObject.'
##        #return Count
##
##    def GetPropByIndex(self, index):
##        u'The name and value of the indexed property in the GxObject.'
##        #return Name, value
##

class GxAddAGSConnection(CoClass):
    u'The one and only GxAddAGSConnection object.'
    _reg_clsid_ = GUID('{11B2AC99-C0D3-4571-95DF-ED41FB4D7BCF}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxAddAGSConnection._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectUI, IGxBasicObject, IGxObjectProperties, IGxObjectWizard]

class GxAGSFeatureServer(CoClass):
    u'GxObject that represents an ArcGIS Server feature server object.'
    _reg_clsid_ = GUID('{1E7BE363-2806-4CDF-AD56-83E48B1F656A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxAGSObject(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of GxObject that represents a ArcGIS Server (AGS) object.'
    _iid_ = GUID('{04429BE9-3A92-4327-9F49-9EE30B95FB3C}')
    _idlflags_ = ['oleautomation']
class IGxAGSObject2(IGxAGSObject):
    _case_insensitive_ = True
    u'Provides access to members of GxObject that represents a ArcGIS Server (AGS) object.'
    _iid_ = GUID('{D4887D25-38E9-461E-9E37-731CC4934D1A}')
    _idlflags_ = ['oleautomation']
class IGxAGSObject3(IGxAGSObject2):
    _case_insensitive_ = True
    u'Provides access to members of GxObject that represents a ArcGIS Server (AGS) object.'
    _iid_ = GUID('{D7C32B7F-28A8-4A7C-8C8A-333DFA49696A}')
    _idlflags_ = ['oleautomation']
class IGxItemInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to ItemInfo of GxObjects.'
    _iid_ = GUID('{5EBC0F34-E575-4F40-A36B-F7E3896AC9A2}')
    _idlflags_ = ['oleautomation']
GxAGSFeatureServer._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectEdit, IGxObjectUI, IGxObjectProperties, IGxAGSObject, IGxAGSObject2, IGxAGSObject3, IGxItemInfo, IGxAGSFeatureServer, IGxLayerSource]

class IGxObjectContainer2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manage child GxObjects.'
    _iid_ = GUID('{3802CC51-6523-497A-9663-9CBB66B0DAC5}')
    _idlflags_ = ['oleautomation']
IGxObjectContainer2._methods_ = [
    COMMETHOD([helpstring(u'An search of the child objects.')], HRESULT, 'SearchChildren',
              ( ['in'], BSTR, 'Name' ),
              ( ['in', 'out'], POINTER(IGxObjectArray), 'objectArray' )),
]
################################################################
## code template for IGxObjectContainer2 implementation
##class IGxObjectContainer2_Impl(object):
##    def SearchChildren(self, Name):
##        u'An search of the child objects.'
##        #return objectArray
##

class GxAGSDraftFolder(CoClass):
    u'The Esri GxAGSDraftFolder object.'
    _reg_clsid_ = GUID('{85925188-BAA7-463A-95EF-979FA40A3518}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxAGSDraftFolder._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectContainer, IGxAGSDraftFolder, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, IGxObjectEdit, IGxObjectProperties, IGxObjectUI, IGxPasteTarget]

IMetadataValidator._methods_ = [
    COMMETHOD([helpstring(u'Validates metadata.')], HRESULT, 'Validate',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'pPropertySet' ),
              ( ['in'], VARIANT_BOOL, 'silent' ),
              ( ['out'], POINTER(BSTR), 'failureReasons' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'isOk' )),
]
################################################################
## code template for IMetadataValidator implementation
##class IMetadataValidator_Impl(object):
##    def Validate(self, pPropertySet, silent):
##        u'Validates metadata.'
##        #return failureReasons, isOk
##

IGxObjectFactory._methods_ = [
    COMMETHOD(['propputref', helpstring(u'Attach the catalog to the object factory.')], HRESULT, 'Catalog',
              ( [], POINTER(IGxCatalog), 'rhs' )),
    COMMETHOD(['propget', helpstring(u'The name of the object factory.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'factoryName' )),
    COMMETHOD([helpstring(u'Indicates if any of the specified files are supported by the object factory.')], HRESULT, 'HasChildren',
              ( ['in'], BSTR, 'parentDir' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IFileNames), 'fileNames' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'HasChildren' )),
    COMMETHOD([helpstring(u'Returns an enumeration of objects corresponding to one or more of the given file names supported by the object factory.')], HRESULT, 'GetChildren',
              ( ['in'], BSTR, 'parentDir' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IFileNames), 'fileNames' ),
              ( ['retval', 'out'], POINTER(POINTER(IEnumGxObject)), 'Children' )),
]
################################################################
## code template for IGxObjectFactory implementation
##class IGxObjectFactory_Impl(object):
##    def Catalog(self, rhs):
##        u'Attach the catalog to the object factory.'
##        #return 
##
##    def GetChildren(self, parentDir, fileNames):
##        u'Returns an enumeration of objects corresponding to one or more of the given file names supported by the object factory.'
##        #return Children
##
##    @property
##    def Name(self):
##        u'The name of the object factory.'
##        #return factoryName
##
##    def HasChildren(self, parentDir, fileNames):
##        u'Indicates if any of the specified files are supported by the object factory.'
##        #return HasChildren
##

IGxObjectFactoryEdit._methods_ = [
    COMMETHOD([helpstring(u"Presents a modal dialog to allow editing the object factory's properties.")], HRESULT, 'EditProperties',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hParent' )),
]
################################################################
## code template for IGxObjectFactoryEdit implementation
##class IGxObjectFactoryEdit_Impl(object):
##    def EditProperties(self, hParent):
##        u"Presents a modal dialog to allow editing the object factory's properties."
##        #return 
##

IGxObjectEdit._methods_ = [
    COMMETHOD([helpstring(u'Indicates if the object can be renamed.')], HRESULT, 'CanRename',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'CanRename' )),
    COMMETHOD([helpstring(u'Renames the object.')], HRESULT, 'Rename',
              ( ['in'], BSTR, 'newShortName' )),
    COMMETHOD([helpstring(u'Indicates if the object can be deleted.')], HRESULT, 'CanDelete',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'CanDelete' )),
    COMMETHOD([helpstring(u'Deletes the object.')], HRESULT, 'Delete'),
    COMMETHOD([helpstring(u"Presents a modal dialog to allow editing the object's properties.")], HRESULT, 'EditProperties',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hParent' )),
    COMMETHOD([helpstring(u'Indicates if the object can be copied.')], HRESULT, 'CanCopy',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'CanCopy' )),
]
################################################################
## code template for IGxObjectEdit implementation
##class IGxObjectEdit_Impl(object):
##    def Rename(self, newShortName):
##        u'Renames the object.'
##        #return 
##
##    def CanCopy(self):
##        u'Indicates if the object can be copied.'
##        #return CanCopy
##
##    def CanDelete(self):
##        u'Indicates if the object can be deleted.'
##        #return CanDelete
##
##    def EditProperties(self, hParent):
##        u"Presents a modal dialog to allow editing the object's properties."
##        #return 
##
##    def CanRename(self):
##        u'Indicates if the object can be renamed.'
##        #return CanRename
##
##    def Delete(self):
##        u'Deletes the object.'
##        #return 
##

class GxTaskServicesRootFolder(CoClass):
    u'Root container of ready-to-use Task Services.'
    _reg_clsid_ = GUID('{1B93D9F9-F46F-464C-89A7-67F6FE7A028F}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxTaskServicesRootFolder(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manages the properties of a GxTaskServices root folder.'
    _iid_ = GUID('{950EDD81-A0B8-4C38-BCE9-2743D24F6314}')
    _idlflags_ = ['oleautomation']
GxTaskServicesRootFolder._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectUI, IGxObjectContainer, IGxTaskServicesRootFolder, IGxRemoteContainer, IGxRootObjectSortPriority]

IGxCachedObjects._methods_ = [
    COMMETHOD([helpstring(u'Loads any objects that should be cached for efficiency.')], HRESULT, 'LoadCachedObjects'),
    COMMETHOD([helpstring(u'Releases any objects that have been cached for efficiency.')], HRESULT, 'ReleaseCachedObjects'),
]
################################################################
## code template for IGxCachedObjects implementation
##class IGxCachedObjects_Impl(object):
##    def ReleaseCachedObjects(self):
##        u'Releases any objects that have been cached for efficiency.'
##        #return 
##
##    def LoadCachedObjects(self):
##        u'Loads any objects that should be cached for efficiency.'
##        #return 
##

IGxFileFilterEvents._methods_ = [
    COMMETHOD([helpstring(u'Called when the file filter definition has changed.')], HRESULT, 'OnDefinitionChanged'),
]
################################################################
## code template for IGxFileFilterEvents implementation
##class IGxFileFilterEvents_Impl(object):
##    def OnDefinitionChanged(self):
##        u'Called when the file filter definition has changed.'
##        #return 
##

IGxNewDatabase._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The value of the workspace factory property.')], HRESULT, 'WorkspaceFactory',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceFactory), 'rhs' )),
]
################################################################
## code template for IGxNewDatabase implementation
##class IGxNewDatabase_Impl(object):
##    def WorkspaceFactory(self, rhs):
##        u'The value of the workspace factory property.'
##        #return 
##

IGxObjectFactoryMetadata._methods_ = [
    COMMETHOD([helpstring(u'Given a path to some metadata, constructs the corresponding GxObject.')], HRESULT, 'GetGxObjectFromMetadata',
              ( ['in'], BSTR, 'metadataPath' ),
              ( ['retval', 'out'], POINTER(POINTER(IGxObject)), 'gxObject' )),
]
################################################################
## code template for IGxObjectFactoryMetadata implementation
##class IGxObjectFactoryMetadata_Impl(object):
##    def GetGxObjectFromMetadata(self, metadataPath):
##        u'Given a path to some metadata, constructs the corresponding GxObject.'
##        #return gxObject
##

IGxDiskConnection._methods_ = [
]
################################################################
## code template for IGxDiskConnection implementation
##class IGxDiskConnection_Impl(object):

ISearchResultsIdentifyObject._methods_ = [
    COMMETHOD(['propputref', helpstring(u'Extent of a shortcut.')], HRESULT, 'Extent',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'rhs' )),
    COMMETHOD(['propputref', helpstring(u'Shortcut to identify.')], HRESULT, 'Shortcut',
              ( ['in'], POINTER(IGxShortcut), 'rhs' )),
    COMMETHOD([helpstring(u'Selects a shortcut in the Catalog tree.')], HRESULT, 'Select'),
]
################################################################
## code template for ISearchResultsIdentifyObject implementation
##class ISearchResultsIdentifyObject_Impl(object):
##    def Select(self):
##        u'Selects a shortcut in the Catalog tree.'
##        #return 
##
##    def Shortcut(self, rhs):
##        u'Shortcut to identify.'
##        #return 
##
##    def Extent(self, rhs):
##        u'Extent of a shortcut.'
##        #return 
##

class GxTaskServicesFolder(CoClass):
    u'GxTaskServicesFolder of ready-to-use Task Services.'
    _reg_clsid_ = GUID('{0B08A499-5DA7-42DA-9A7F-5E24177682E1}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxTaskServicesFolder(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manages the properties of a GxTaskServicesFolder.'
    _iid_ = GUID('{CBE68E51-D134-4715-AD3F-C94C80B9FF30}')
    _idlflags_ = ['oleautomation']
GxTaskServicesFolder._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectUI, IGxObjectContainer, IGxTaskServicesFolder, IGxRemoteContainer]

class ISearchResults(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manage the search result.'
    _iid_ = GUID('{64AB252E-1CCA-4C79-A929-1CE0AC219724}')
    _idlflags_ = ['oleautomation']
ISearchResults._methods_ = [
    COMMETHOD(['propputref', helpstring(u'Query defining the search parameters.')], HRESULT, 'Query',
              ( ['in'], POINTER(IQuery), 'ppQuery' )),
    COMMETHOD(['propget', helpstring(u'Query defining the search parameters.')], HRESULT, 'Query',
              ( ['retval', 'out'], POINTER(POINTER(IQuery)), 'ppQuery' )),
]
################################################################
## code template for ISearchResults implementation
##class ISearchResults_Impl(object):
##    @property
##    def Query(self, ppQuery):
##        u'Query defining the search parameters.'
##        #return 
##

class IGxPrjFile(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that returns the properties of a PRJ file.'
    _iid_ = GUID('{A38CB584-95CE-11D2-AD2A-00C04FA33A15}')
    _idlflags_ = ['oleautomation']
IGxPrjFile._methods_ = [
    COMMETHOD(['propget', helpstring(u'The geographic or projected coordinate system contained in the PRJ file.')], HRESULT, 'SpatialReference',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference)), 'SpatialReference' )),
]
################################################################
## code template for IGxPrjFile implementation
##class IGxPrjFile_Impl(object):
##    @property
##    def SpatialReference(self):
##        u'The geographic or projected coordinate system contained in the PRJ file.'
##        #return SpatialReference
##

IGxObjectFactoryFileExtensions._methods_ = [
    COMMETHOD(['propget', helpstring(u'The complete set of file extensions relevant to the factory.')], HRESULT, 'RelevantExtensions',
              ( ['retval', 'out'], POINTER(BSTR), 'extSet' )),
    COMMETHOD(['propget', helpstring(u'The minimal set of file extensions which should cause the factory to be activated.')], HRESULT, 'ActivationExtensions',
              ( ['retval', 'out'], POINTER(BSTR), 'extSet' )),
]
################################################################
## code template for IGxObjectFactoryFileExtensions implementation
##class IGxObjectFactoryFileExtensions_Impl(object):
##    @property
##    def ActivationExtensions(self):
##        u'The minimal set of file extensions which should cause the factory to be activated.'
##        #return extSet
##
##    @property
##    def RelevantExtensions(self):
##        u'The complete set of file extensions relevant to the factory.'
##        #return extSet
##

class GxAGSConnection(CoClass):
    u'GxObject that represents an ArcGIS Server connection.'
    _reg_clsid_ = GUID('{F3DFB191-97FD-45C4-97D1-941A147046F3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxAGSConnection._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectContainer, IGxAGSConnection, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, IGxObjectEdit, IGxObjectProperties, IGxObjectUI, IGxObjectWizard, IGxPasteTarget, IGxRemoteConnection]

class GxTaskServicesConnection(CoClass):
    u'GxTaskServicesConnection of ready-to-use Task Services.'
    _reg_clsid_ = GUID('{E26683CA-CCBC-4495-8A8F-F77F6F9A3B6F}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxTaskServicesConnection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manages the properties of a GxTaskServicesConnection.'
    _iid_ = GUID('{FC3FC389-BDF8-47D1-B8AE-82BB557F7174}')
    _idlflags_ = ['oleautomation']
GxTaskServicesConnection._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectUI, IGxObjectContainer, IGxTaskServicesConnection, IGxRemoteContainer]

IGxDatabaseExtension._methods_ = [
    COMMETHOD(['propputref', helpstring(u'Attach the catalog to the database extension.')], HRESULT, 'Catalog',
              ( [], POINTER(IGxCatalog), 'rhs' )),
    COMMETHOD(['propget', helpstring(u'The name of the extension.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'extensionName' )),
    COMMETHOD([helpstring(u'Verify if this extension has children.')], HRESULT, 'HasChildren',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspace), 'Workspace' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'HasChildren' )),
    COMMETHOD([helpstring(u'Get children.')], HRESULT, 'GetChildren',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspace), 'Workspace' ),
              ( ['retval', 'out'], POINTER(POINTER(IEnumGxObject)), 'Children' )),
    COMMETHOD([helpstring(u'Check if the objects are children and if yes compare them.')], HRESULT, 'Compare',
              ( ['in'], POINTER(IGxObject), 'gxObject1' ),
              ( ['in'], POINTER(IGxObject), 'gxObject2' ),
              ( ['in'], VARIANT_BOOL, 'ascending' ),
              ( ['retval', 'out'], POINTER(c_int), 'result' )),
]
################################################################
## code template for IGxDatabaseExtension implementation
##class IGxDatabaseExtension_Impl(object):
##    def Compare(self, gxObject1, gxObject2, ascending):
##        u'Check if the objects are children and if yes compare them.'
##        #return result
##
##    def Catalog(self, rhs):
##        u'Attach the catalog to the database extension.'
##        #return 
##
##    def GetChildren(self, Workspace):
##        u'Get children.'
##        #return Children
##
##    @property
##    def Name(self):
##        u'The name of the extension.'
##        #return extensionName
##
##    def HasChildren(self, Workspace):
##        u'Verify if this extension has children.'
##        #return HasChildren
##

IGxObjectFactoryPriority._methods_ = [
    COMMETHOD(['propget', helpstring(u'The priority of the object factory.  The higher the priority, the sooner the object factory is used to discover GxObjects.')], HRESULT, 'Priority',
              ( ['retval', 'out'], POINTER(c_int), 'Priority' )),
    COMMETHOD(['propput', helpstring(u'The priority of the object factory.  The higher the priority, the sooner the object factory is used to discover GxObjects.')], HRESULT, 'Priority',
              ( ['in'], c_int, 'Priority' )),
]
################################################################
## code template for IGxObjectFactoryPriority implementation
##class IGxObjectFactoryPriority_Impl(object):
##    def _get(self):
##        u'The priority of the object factory.  The higher the priority, the sooner the object factory is used to discover GxObjects.'
##        #return Priority
##    def _set(self, Priority):
##        u'The priority of the object factory.  The higher the priority, the sooner the object factory is used to discover GxObjects.'
##    Priority = property(_get, _set, doc = _set.__doc__)
##

class SearchResultsLayerFactory(CoClass):
    u'A factory for creating search result layers.  This object is not supported on ArcGIS version 10.1. or later.'
    _reg_clsid_ = GUID('{E641BA7A-68D6-4594-A0D7-3D5DCE2DCD30}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
SearchResultsLayerFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayerFactory]

IGxSpatialReferencesFolder._methods_ = [
    COMMETHOD(['propput', helpstring(u'The full path for the spatial references folder.')], HRESULT, 'Path',
              ( ['in'], BSTR, 'Path' )),
    COMMETHOD(['propget', helpstring(u'The full path for the spatial references folder.')], HRESULT, 'Path',
              ( ['retval', 'out'], POINTER(BSTR), 'Path' )),
]
################################################################
## code template for IGxSpatialReferencesFolder implementation
##class IGxSpatialReferencesFolder_Impl(object):
##    def _get(self):
##        u'The full path for the spatial references folder.'
##        #return Path
##    def _set(self, Path):
##        u'The full path for the spatial references folder.'
##    Path = property(_get, _set, doc = _set.__doc__)
##

class IGxRasterDataset(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that provide information about Gx raster dataset.'
    _iid_ = GUID('{925E49AD-A84B-47CE-893C-255C9A9ADD95}')
    _idlflags_ = ['oleautomation']
IGxRasterDataset._methods_ = [
]
################################################################
## code template for IGxRasterDataset implementation
##class IGxRasterDataset_Impl(object):

class SearchResultsLayer(CoClass):
    u'A layer that lets you preview a search result in the Geography tab.  This object is not supported on ArcGIS version 10.1. or later.'
    _reg_clsid_ = GUID('{5A4E2E23-4426-4708-97F3-A925FE980A48}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class ISearchResultsLayer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the search results layer.'
    _iid_ = GUID('{F4273DCC-B220-4B1F-A177-11C4A1F6F5A6}')
    _idlflags_ = ['oleautomation']
SearchResultsLayer._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ISearchResultsLayer, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeoDataset, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IIdentify, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IPublishLayer]

class GxAGSDraft(CoClass):
    u'GxObject that represents an ArcGIS AGS draft service object.'
    _reg_clsid_ = GUID('{2B349339-BF63-4F17-9969-1D915331FD43}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxAGSDraft(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of GxObject that represents a ArcGIS Server (AGS) draft object.'
    _iid_ = GUID('{80C5231D-B8FE-42A7-B965-FEB6DE6D7432}')
    _idlflags_ = ['oleautomation']
GxAGSDraft._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectEdit, IGxObjectUI, IGxObjectProperties, IGxAGSDraft, IGxItemInfo]

class GxMyHostedMapsFolder(CoClass):
    u'Container of My Hosted Services.'
    _reg_clsid_ = GUID('{AF9E0528-EC0D-43B1-8B98-9B88AABC6696}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxMyHostedMapsFolder(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manages the properties of a GxMyHostedMapsFolder root folder.'
    _iid_ = GUID('{865A8CCD-9E6B-4099-A187-3CF57B4DF50F}')
    _idlflags_ = ['oleautomation']
GxMyHostedMapsFolder._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectUI, IGxObjectContainer, IGxMyHostedMapsFolder, IGxRemoteContainer, IGxRootObjectSortPriority]

IGxPasteTargetHelper._methods_ = [
    COMMETHOD([helpstring(u'Indicates if the specified name object may be pasted into the given target.  On output, moveOperation indicates if a subsequent paste operation would represent a move, or merely a copy, operation.')], HRESULT, 'CanPaste',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName), 'Name' ),
              ( ['in'], POINTER(IGxObject), 'Target' ),
              ( ['out'], POINTER(VARIANT_BOOL), 'moveOperation' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'CanPaste' )),
    COMMETHOD([helpstring(u'Pastes the specified name object into the given target.  On input, moveOperation indicates if this is a move operation.  On output, it indicates if the objects have been moved, or merely copied.')], HRESULT, 'Paste',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName), 'Name' ),
              ( ['in'], POINTER(IGxObject), 'Target' ),
              ( ['in', 'out'], POINTER(VARIANT_BOOL), 'moveOperation' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'successfulPaste' )),
]
################################################################
## code template for IGxPasteTargetHelper implementation
##class IGxPasteTargetHelper_Impl(object):
##    def Paste(self, Name, Target):
##        u'Pastes the specified name object into the given target.  On input, moveOperation indicates if this is a move operation.  On output, it indicates if the objects have been moved, or merely copied.'
##        #return moveOperation, successfulPaste
##
##    def CanPaste(self, Name, Target):
##        u'Indicates if the specified name object may be pasted into the given target.  On output, moveOperation indicates if a subsequent paste operation would represent a move, or merely a copy, operation.'
##        #return moveOperation, CanPaste
##

IGxSelectionEvents._methods_ = [
    COMMETHOD([helpstring(u'Called when the selection contents have changed.')], HRESULT, 'OnSelectionChanged',
              ( ['in'], POINTER(IGxSelection), 'Selection' ),
              ( ['in'], POINTER(VARIANT), 'initiator' )),
]
################################################################
## code template for IGxSelectionEvents implementation
##class IGxSelectionEvents_Impl(object):
##    def OnSelectionChanged(self, Selection, initiator):
##        u'Called when the selection contents have changed.'
##        #return 
##

IGxCatalogEvents._methods_ = [
    COMMETHOD([helpstring(u'Called when the whole catalog has changed.')], HRESULT, 'OnRefreshAll'),
    COMMETHOD([helpstring(u'Called when an object has been added to some part of the catalog.')], HRESULT, 'OnObjectAdded',
              ( [], POINTER(IGxObject), 'gxObject' )),
    COMMETHOD([helpstring(u'Called when an object has been deleted from some part of the catalog.')], HRESULT, 'OnObjectDeleted',
              ( [], POINTER(IGxObject), 'gxObject' )),
    COMMETHOD([helpstring(u'Called when an object in some part of the catalog has been changed.')], HRESULT, 'OnObjectChanged',
              ( [], POINTER(IGxObject), 'gxObject' )),
    COMMETHOD([helpstring(u'Called when an object in some part of the catalog has been refreshed.')], HRESULT, 'OnObjectRefreshed',
              ( [], POINTER(IGxObject), 'gxObject' )),
]
################################################################
## code template for IGxCatalogEvents implementation
##class IGxCatalogEvents_Impl(object):
##    def OnObjectAdded(self, gxObject):
##        u'Called when an object has been added to some part of the catalog.'
##        #return 
##
##    def OnObjectDeleted(self, gxObject):
##        u'Called when an object has been deleted from some part of the catalog.'
##        #return 
##
##    def OnObjectRefreshed(self, gxObject):
##        u'Called when an object in some part of the catalog has been refreshed.'
##        #return 
##
##    def OnRefreshAll(self):
##        u'Called when the whole catalog has changed.'
##        #return 
##
##    def OnObjectChanged(self, gxObject):
##        u'Called when an object in some part of the catalog has been changed.'
##        #return 
##

class SearchResultsRoot(CoClass):
    u'A container for search results.  This object is not supported on ArcGIS version 10.1. or later.'
    _reg_clsid_ = GUID('{3B11C773-9EE7-11D3-A6CB-0008C7D3AE50}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
SearchResultsRoot._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectUI, IGxObjectContainer, IGxObjectEdit, IGxPasteTarget, IGxFile, IGxCachedObjects, IGxObjectProperties, IGxRootObjectStartupProperties]

class GxServiceDefinition(CoClass):
    u'GxObject that represents a service definition.'
    _reg_clsid_ = GUID('{054442DE-E17F-4BDA-96ED-A58C2DC006E4}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxServiceDefinition._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectEdit, IGxObjectUI, IGxObjectProperties, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, IGxServiceDefinition, IGxItemInfo, IGxThumbnail, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit]

class GxServiceDefinitionFactory(CoClass):
    u'Service definition object factory.'
    _reg_clsid_ = GUID('{E2E693CC-340C-4205-8D80-D0B1FB6DD5A7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxServiceDefinitionFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFactory]

class SearchResults(CoClass):
    u'GxObject that represents the search result.  This object is not supported on ArcGIS version 10.1. or later.'
    _reg_clsid_ = GUID('{974730C1-AE9D-11D3-A6D5-0008C7D3AE50}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
SearchResults._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectUI, IGxObjectContainer, IGxObjectEdit, IGxPasteTarget, IGxObjectSort, IGxFile, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, ISearchResults, IGxCachedObjects, IGxObjectProperties]

class GxAGSFolder(CoClass):
    u'The Esri GxAGSFolder object.'
    _reg_clsid_ = GUID('{5D5C554D-5DE2-4EC3-A291-13DE76D5B958}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxAGSFolder._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectContainer, IGxAGSFolder, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, IGxObjectEdit, IGxObjectProperties, IGxObjectUI, IGxObjectWizard, IGxPasteTarget, IGxRemoteConnection]

IRasterFormatFilter._methods_ = [
    COMMETHOD(['propget', helpstring(u'The extension string for a raster format.')], HRESULT, 'Extension',
              ( ['retval', 'out'], POINTER(BSTR), 'Extension' )),
]
################################################################
## code template for IRasterFormatFilter implementation
##class IRasterFormatFilter_Impl(object):
##    @property
##    def Extension(self):
##        u'The extension string for a raster format.'
##        #return Extension
##

class IGxDatabaseExtensions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that return GX database extensions.'
    _iid_ = GUID('{0CAD4508-4F3E-11D3-9F52-00C04F6BDF06}')
    _idlflags_ = ['oleautomation']
IGxDatabaseExtensions._methods_ = [
    COMMETHOD(['propget', helpstring(u'The number of database extensions.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD([helpstring(u'Get an extension.')], HRESULT, 'GetExtension',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IGxDatabaseExtension)), 'Extension' )),
]
################################################################
## code template for IGxDatabaseExtensions implementation
##class IGxDatabaseExtensions_Impl(object):
##    @property
##    def Count(self):
##        u'The number of database extensions.'
##        #return Count
##
##    def GetExtension(self, index):
##        u'Get an extension.'
##        #return Extension
##

IGxGPTool._methods_ = [
    COMMETHOD(['propget', helpstring(u'The geoprocessing tool object associated with this catalog geoprocessing tool object.')], HRESULT, 'Tool',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C031A050_82C6_4F8F_8836_5692631CFFE6_0_10_2.IGPTool)), 'Tool' )),
    COMMETHOD(['propputref', helpstring(u'The geoprocessing tool object associated with this catalog geoprocessing tool object.')], HRESULT, 'Tool',
              ( ['in'], POINTER(comtypes.gen._C031A050_82C6_4F8F_8836_5692631CFFE6_0_10_2.IGPTool), 'Tool' )),
    COMMETHOD([helpstring(u'Updates the icon of the geoprocessing tool displayed in ArcCatalog.')], HRESULT, 'UpdateToolState'),
]
################################################################
## code template for IGxGPTool implementation
##class IGxGPTool_Impl(object):
##    def Tool(self, Tool):
##        u'The geoprocessing tool object associated with this catalog geoprocessing tool object.'
##        #return 
##
##    def UpdateToolState(self):
##        u'Updates the icon of the geoprocessing tool displayed in ArcCatalog.'
##        #return 
##

class IGxWMSMap(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members GxWMSMap object.'
    _iid_ = GUID('{170CFE7F-664D-4D87-907B-0F744BDBB194}')
    _idlflags_ = []
IGxWMSMap._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The description of WMS service.')], HRESULT, 'WMSServiceDescription',
              ( ['in'], POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IWMSServiceDescription), 'ppWMSLayerDescription' )),
    COMMETHOD(['propget', helpstring(u'The description of WMS service.')], HRESULT, 'WMSServiceDescription',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IWMSServiceDescription)), 'ppWMSLayerDescription' )),
]
################################################################
## code template for IGxWMSMap implementation
##class IGxWMSMap_Impl(object):
##    @property
##    def WMSServiceDescription(self, ppWMSLayerDescription):
##        u'The description of WMS service.'
##        #return 
##

class GxRasterFileSystemFactory(CoClass):
    u'Gx Raster File System object factory.'
    _reg_clsid_ = GUID('{3FA63EB5-9471-4EFF-A03E-AE729C9CF8D5}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxRasterFileSystemFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFactory, IGxObjectFactoryMetadata, IGxObjectFactoryEdit, IGxObjectFactoryFileExtensions]

class GxRasterDataset(CoClass):
    u'A Gx Raster dataset.'
    _reg_clsid_ = GUID('{942F6AB0-9025-4DBC-A70F-74C33B437C08}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxRasterDataset._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxDataset, IGxObject, IGxObjectUI, IGxPasteTarget, IGxCachedObjects, IGxObjectEdit, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, IGxThumbnail, IGxObjectContainer, IGxObjectProperties, IGxObjectInternalName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, IGxContentViewControlCustom, IGxDataElement, IGxDataElementHelper, IGxObjectContainer2]

class GxFilterAGSConnection(CoClass):
    u'A filter for displaying/choosing AGS Server Connection objects.'
    _reg_clsid_ = GUID('{E0BBF5D7-5C0F-4EEB-B29D-0E84B32AC1BB}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterAGSConnection._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxGDBRasterExtension(CoClass):
    u'A Gx GDB Raster dataset Extension.'
    _reg_clsid_ = GUID('{D307857C-5DD8-4292-BEC0-0BDC7522A3BE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxGDBRasterExtension._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxDatabaseExtension]

class GxFilterRasterCatalogDatasets(CoClass):
    u'A filter for displaying/choosing raster catalog datasets.'
    _reg_clsid_ = GUID('{5517B69B-6714-4DF3-AA43-4283382DA5C3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterRasterCatalogDatasets._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxFilterMapServers(CoClass):
    u'A filter for displaying/choosing map server object.'
    _reg_clsid_ = GUID('{D5222D62-3809-4863-8E81-FDB2C9047EB8}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterMapServers._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxFilterSearchServers(CoClass):
    u'A filter for displaying/choosing Enterprise Catalog Server objects.'
    _reg_clsid_ = GUID('{B1C01561-BA53-4E44-AAFC-DF93BCF3FC8F}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterSearchServers._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxFilterSearchServers, IGxObjectFilter]

class RasterFormatGridFilter(CoClass):
    u'The format filter for Grid.'
    _reg_clsid_ = GUID('{7F3AE05F-63D6-495A-A8C2-C102C4D7FDF2}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
RasterFormatGridFilter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter, IRasterFormatFilter]

class GxFilterMosaicDatasets(CoClass):
    u'A filter for displaying/choosing mosaic datasets.'
    _reg_clsid_ = GUID('{55FE6609-1C3E-4837-B1DE-7871E3A9D2B1}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterMosaicDatasets._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

IGxObjectUI._methods_ = [
    COMMETHOD(['propget', helpstring(u'The small image that represents the object.')], HRESULT, 'SmallImage',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'hBitmap' )),
    COMMETHOD(['propget', helpstring(u'The small image that represents the object when it is selected.')], HRESULT, 'SmallSelectedImage',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'hBitmap' )),
    COMMETHOD(['propget', helpstring(u'The large image that represents the object.')], HRESULT, 'LargeImage',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'hBitmap' )),
    COMMETHOD(['propget', helpstring(u'The large image that represents the object when it is selected.')], HRESULT, 'LargeSelectedImage',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'hBitmap' )),
    COMMETHOD(['propget', helpstring(u'The class ID of the context menu for this object.')], HRESULT, 'ContextMenu',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID)), 'ClassID' )),
    COMMETHOD(['propget', helpstring(u'The class ID of the New menu for this object.')], HRESULT, 'NewMenu',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID)), 'ClassID' )),
]
################################################################
## code template for IGxObjectUI implementation
##class IGxObjectUI_Impl(object):
##    @property
##    def LargeSelectedImage(self):
##        u'The large image that represents the object when it is selected.'
##        #return hBitmap
##
##    @property
##    def LargeImage(self):
##        u'The large image that represents the object.'
##        #return hBitmap
##
##    @property
##    def ContextMenu(self):
##        u'The class ID of the context menu for this object.'
##        #return ClassID
##
##    @property
##    def SmallSelectedImage(self):
##        u'The small image that represents the object when it is selected.'
##        #return hBitmap
##
##    @property
##    def NewMenu(self):
##        u'The class ID of the New menu for this object.'
##        #return ClassID
##
##    @property
##    def SmallImage(self):
##        u'The small image that represents the object.'
##        #return hBitmap
##

class GxFilterdBASEFiles(CoClass):
    u'A filter for displaying/choosing dBASE files.'
    _reg_clsid_ = GUID('{1EB22543-E960-11D3-A682-0008C7D3AE8D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterdBASEFiles._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeType]

class GxFilterShapefiles(CoClass):
    u'A filter for displaying/choosing shapefiles.'
    _reg_clsid_ = GUID('{90E9D96D-E647-11D3-A682-0008C7D3AE8D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterShapefiles._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeType]

class GxShapefileDataset(CoClass):
    u'A Shapefile Feature Class or DBase Table.'
    _reg_clsid_ = GUID('{4CA28C82-06E5-11D3-9F87-00C04F6BC626}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxShapefileDataset._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectUI, IGxObjectEdit, IGxObjectProperties, IGxDataset, IGxCachedObjects, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, IGxThumbnail, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IObjectClassSchemaEvents, IGxObjectInternalName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, IGxDataElement, IGxDataElementHelper]

class GxFilterRunningMapServers(CoClass):
    u'A filter for displaying/choosing running map server object.'
    _reg_clsid_ = GUID('{48AF8B11-64F8-47B4-B9B6-8826F5EFE4B0}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterRunningMapServers._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

IGxPre70Coverage._methods_ = [
    COMMETHOD(['propput', helpstring(u'The full path of the Coverage.')], HRESULT, 'Path',
              ( ['in'], BSTR, 'Path' )),
    COMMETHOD(['propget', helpstring(u'The full path of the Coverage.')], HRESULT, 'Path',
              ( ['retval', 'out'], POINTER(BSTR), 'Path' )),
]
################################################################
## code template for IGxPre70Coverage implementation
##class IGxPre70Coverage_Impl(object):
##    def _get(self):
##        u'The full path of the Coverage.'
##        #return Path
##    def _set(self, Path):
##        u'The full path of the Coverage.'
##    Path = property(_get, _set, doc = _set.__doc__)
##

class GxFilterImageServers(CoClass):
    u'A filter for displaying/choosing Image Server Object.'
    _reg_clsid_ = GUID('{9ADBEEFA-CF26-432F-B87F-33BD5261663E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterImageServers._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class ComplexNativeType(CoClass):
    u'Native type for built up of other native types.'
    _reg_clsid_ = GUID('{3037BECC-165C-48C8-868B-0E7CDCD342D5}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
ComplexNativeType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeType, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IComplexNativeType]

class RasterFormatImgFilter(CoClass):
    u'The format filter for IMG.'
    _reg_clsid_ = GUID('{A2534692-E4DA-4DC1-B23B-E04F75AC1398}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
RasterFormatImgFilter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter, IRasterFormatFilter]

class RasterFormatSDEFilter(CoClass):
    u'The format filter for SDE Raster.'
    _reg_clsid_ = GUID('{2FD91000-7F9B-11D4-B284-00508BCDC7C8}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
RasterFormatSDEFilter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter, IRasterFormatFilter]

class GxShapefileFactory(CoClass):
    u'Gx Object Factory for Shapefile Feature Classes and DBase Tables.'
    _reg_clsid_ = GUID('{4CA28C81-06E5-11D3-9F87-00C04F6BC626}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxShapefileFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFactory, IGxObjectFactoryMetadata, IGxObjectFactoryFileExtensions]

class MapNativeType(CoClass):
    u'Native type for a map.'
    _reg_clsid_ = GUID('{3627F039-8599-42CC-A15E-3248B82BFE82}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
MapNativeType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeType]

class GxFilterWCSCoverage(CoClass):
    u'A filter for displaying/choosing WCS Coverage.'
    _reg_clsid_ = GUID('{C5240D58-2127-4E54-8299-903BC71FE33C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterWCSCoverage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxAGSMap(CoClass):
    u'GxObject that represents an ArcGIS Server map object.'
    _reg_clsid_ = GUID('{DD9C51A7-1740-4651-9C83-2D9ECCD53975}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxAGSMap(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of GxObject that represents a ArcGIS Server map object.'
    _iid_ = GUID('{46E2C9BF-E363-498C-B200-43A8F773E485}')
    _idlflags_ = ['oleautomation']
GxAGSMap._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectEdit, IGxObjectUI, IGxObjectProperties, IGxAGSObject, IGxAGSObject2, IGxAGSObject3, IGxItemInfo, IGxAGSMap, IGxLayerSource, IGxThumbnail, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit]

class GxFilterGeoDataServersAndWorkspaces(CoClass):
    u'A filter for displaying/choosing geodataserver/workspaces objects.'
    _reg_clsid_ = GUID('{87DA5CFE-4F48-4059-A504-90658B4D9920}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterGeoDataServersAndWorkspaces._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxFilterLasDatasets(CoClass):
    u'A filter for displaying/choosing LAS datasets.'
    _reg_clsid_ = GUID('{083BEBBA-49A6-4AC8-BC60-2DCD9C75B5A3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterLasDatasets._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxFilterImageServerDataSource(CoClass):
    u'A filter for displaying/choosing image service data sources.'
    _reg_clsid_ = GUID('{14153E17-1729-43D9-9FC5-9E71BBFAA3D6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterImageServerDataSource._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class LayerNativeType(CoClass):
    u'Native type for a layer.'
    _reg_clsid_ = GUID('{8F0231EC-2C81-4E2B-871A-09C864B58DCE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
LayerNativeType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeType]

class GxFilterWMTSConnection(CoClass):
    u'A filter for displaying/choosing WMTS Server Connection objects.'
    _reg_clsid_ = GUID('{E923A09B-10A1-4E45-ADAA-89C30D058C60}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterWMTSConnection._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class FdpFileNativeType(CoClass):
    u'Native type for a fdp file.'
    _reg_clsid_ = GUID('{952DAF6E-4A64-4E29-9818-064EE899B13E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
FdpFileNativeType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeType]

class RasterFormatBMPFilter(CoClass):
    u'The format filter for BMP.'
    _reg_clsid_ = GUID('{1B2730E3-36A8-45F0-BD5F-17E3BBF93EB8}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
RasterFormatBMPFilter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter, IRasterFormatFilter]

class GxAGSImage(CoClass):
    u'GxObject that represents an ArcGIS Image Server Service object.'
    _reg_clsid_ = GUID('{AE4A081A-8A1B-4F18-A190-CEFF6C47F590}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxAGSImage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectEdit, IGxObjectUI, IGxObjectProperties, IGxAGSObject, IGxAGSObject2, IGxAGSObject3, IGxItemInfo, IGxAGSImage, IGxAGSImage2, IGxLayerSource, IGxThumbnail, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit]

class RasterFormatGIFFilter(CoClass):
    u'The format filter for GIF.'
    _reg_clsid_ = GUID('{6808039B-678D-400D-B084-1D04CB8FA96D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
RasterFormatGIFFilter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter, IRasterFormatFilter]

class GxFilterCadastralFabrics(CoClass):
    u'A filter for displaying/choosing Cadastral Fabric datasets.'
    _reg_clsid_ = GUID('{D028106A-20F4-4776-9644-BC5BA1E716D8}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterCadastralFabrics._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class RasterFormatJPGFilter(CoClass):
    u'The format filter for JPG.'
    _reg_clsid_ = GUID('{CCDA21FF-634D-47B7-8F66-51EBE7EA2416}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
RasterFormatJPGFilter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter, IRasterFormatFilter]

IGxCatalogWorkspace._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if the catalog uses a workspace folder as a home folder.')], HRESULT, 'UseWorkspaceFolder',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bUseWorkspaceFolder' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the catalog uses a workspace folder as a home folder.')], HRESULT, 'UseWorkspaceFolder',
              ( ['in'], VARIANT_BOOL, 'bUseWorkspaceFolder' )),
    COMMETHOD(['propget', helpstring(u'The workspace path.')], HRESULT, 'WorkspaceFolderPath',
              ( ['retval', 'out'], POINTER(BSTR), 'WorkspaceFolderPath' )),
    COMMETHOD([helpstring(u'Opens the document catalog.')], HRESULT, 'OpenWorkspaceFolder',
              ( ['in'], BSTR, 'WorkspaceFolderPath' )),
]
################################################################
## code template for IGxCatalogWorkspace implementation
##class IGxCatalogWorkspace_Impl(object):
##    @property
##    def WorkspaceFolderPath(self):
##        u'The workspace path.'
##        #return WorkspaceFolderPath
##
##    def OpenWorkspaceFolder(self, WorkspaceFolderPath):
##        u'Opens the document catalog.'
##        #return 
##
##    def _get(self):
##        u'Indicates if the catalog uses a workspace folder as a home folder.'
##        #return bUseWorkspaceFolder
##    def _set(self, bUseWorkspaceFolder):
##        u'Indicates if the catalog uses a workspace folder as a home folder.'
##    UseWorkspaceFolder = property(_get, _set, doc = _set.__doc__)
##

class RasterFormatJP2Filter(CoClass):
    u'The format filter for JP2.'
    _reg_clsid_ = GUID('{B590E4C6-75F5-4901-8006-EEFFC23DDC8D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
RasterFormatJP2Filter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter, IRasterFormatFilter]

class GxFilterRoute(CoClass):
    u'GxFilterRoute for selecting only polyline-m feature classes.'
    _reg_clsid_ = GUID('{ABD56605-A1E3-4784-99B9-FA8B442A2691}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterRoute._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxFilterSDETables(CoClass):
    u'A filter for displaying/choosing SDE tables.'
    _reg_clsid_ = GUID('{D2724373-EA1D-11D3-A682-0008C7D3AE8D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterSDETables._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class RasterFormatPNGFilter(CoClass):
    u'The format filter for png.'
    _reg_clsid_ = GUID('{DED25A12-B66B-4D81-B016-F98772520B52}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
RasterFormatPNGFilter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter, IRasterFormatFilter]

class RasterFormatBILFilter(CoClass):
    u'The format filter for Esri bil.'
    _reg_clsid_ = GUID('{3D4B7090-19D3-4A43-A062-B2DE7E80F5D8}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
RasterFormatBILFilter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter, IRasterFormatFilter]

class EnumGxObject(CoClass):
    u'Provides access to a set of GxObjects.'
    _reg_clsid_ = GUID('{D8B883F2-D005-4EC4-9A95-B9735660B78D}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
EnumGxObject._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IEnumGxObject]

class GxFilterGeometryServers(CoClass):
    u'A filter for displaying/choosing geometry server objects.'
    _reg_clsid_ = GUID('{1294ECD7-3612-4CF3-94F4-5AE21163DF74}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterGeometryServers._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class RasterFormatBSQFilter(CoClass):
    u'The format filter for Esri bsq.'
    _reg_clsid_ = GUID('{566B1F4A-55A0-4FBD-A202-A398C6F8BE31}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
RasterFormatBSQFilter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter, IRasterFormatFilter]

class WorkspaceFolderNativeType(CoClass):
    u'Native type for a workspace folder.'
    _reg_clsid_ = GUID('{AD327B2A-8197-4CF9-AF48-00B9431507FB}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
WorkspaceFolderNativeType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeType]

class FolderNativeType(CoClass):
    u'Native type for a folder.'
    _reg_clsid_ = GUID('{983B714E-116F-4249-8062-4B940ED1D215}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
FolderNativeType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeType]

class RasterFormatBIPFilter(CoClass):
    u'The format filter for Esri bip.'
    _reg_clsid_ = GUID('{49F96CE1-1585-4B88-8E5F-8FD1200E5A3C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
RasterFormatBIPFilter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter, IRasterFormatFilter]

class FileNativeType(CoClass):
    u'Native type for a filtered file.'
    _reg_clsid_ = GUID('{9AC4E0EB-90FE-42A3-A688-AFFFE16F1D52}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
FileNativeType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeType]

class GxFilterDataElements(CoClass):
    u'A filter for displaying/choosing data elements.'
    _reg_clsid_ = GUID('{6EFE3D6B-4623-4487-A84B-E2861AEC6A55}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxFilterDataElements(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to GxFilter data elements.'
    _iid_ = GUID('{CD492CC1-D71C-4B7A-BEC9-B43E7374D9E1}')
    _idlflags_ = ['oleautomation']
GxFilterDataElements._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxFilterDataElements, IGxObjectFilter]

class RasterFormatENVIFilter(CoClass):
    u'The format filter for ENVI.'
    _reg_clsid_ = GUID('{2B1ED0A2-F201-4419-9D9D-5C4DCAD84F97}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
RasterFormatENVIFilter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter, IRasterFormatFilter]

class GxDatabaseExtensions(CoClass):
    u'GxObject that represents the database extensions.'
    _reg_clsid_ = GUID('{27E179F2-4F3E-11D3-9F52-00C04F6BDF06}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxDatabaseExtensions._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxDatabaseExtensions]

class GxFilterSDEFeatureDatasets(CoClass):
    u'A filter for displaying/choosing SDE feature datasets.'
    _reg_clsid_ = GUID('{D2724375-EA1D-11D3-A682-0008C7D3AE8D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterSDEFeatureDatasets._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class PrjFileNativeType(CoClass):
    u'Native type for a prj file.'
    _reg_clsid_ = GUID('{476B1B32-766A-4293-AF8B-2B4A35539652}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
PrjFileNativeType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeType]

class GxFilterTextFiles(CoClass):
    u'A filter for displaying/choosing delimited text files.'
    _reg_clsid_ = GUID('{A3D02AF4-10A6-11D4-AE05-00C04FA33A15}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterTextFiles._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeType]

class IIMSConnection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members to connect to an ArcIMS server (IMS).'
    _iid_ = GUID('{A98227BF-D1CD-402E-B5EA-D05F77513755}')
    _idlflags_ = ['oleautomation']
IIMSConnection._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates whether the IMS connection has been made.')], HRESULT, 'IsConnected',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsConnected' )),
    COMMETHOD([helpstring(u'Connects to an ArcIMS server.')], HRESULT, 'Connect'),
    COMMETHOD([helpstring(u'Disconnects from an ArcIMS server.')], HRESULT, 'Disconnect'),
    COMMETHOD([helpstring(u'Loads an IMS connection file containing the URL.')], HRESULT, 'LoadFromFile',
              ( ['in'], BSTR, 'Path' )),
    COMMETHOD([helpstring(u'Writes an IMS connection file containing the URL.')], HRESULT, 'SaveToFile',
              ( ['in'], BSTR, 'Path' )),
    COMMETHOD(['propget', helpstring(u'Path to the IMS connection file.')], HRESULT, 'FileName',
              ( ['retval', 'out'], POINTER(BSTR), 'FileName' )),
    COMMETHOD(['propget', helpstring(u'URL to ArcIMS server.')], HRESULT, 'URL',
              ( ['retval', 'out'], POINTER(BSTR), 'URL' )),
    COMMETHOD(['propput', helpstring(u'URL to ArcIMS server.')], HRESULT, 'URL',
              ( ['in'], BSTR, 'URL' )),
    COMMETHOD(['propput', helpstring(u'User name.')], HRESULT, 'UserName',
              ( ['in'], BSTR, 'UserName' )),
    COMMETHOD(['propget', helpstring(u'User name.')], HRESULT, 'UserName',
              ( ['retval', 'out'], POINTER(BSTR), 'UserName' )),
    COMMETHOD(['propput', helpstring(u'Password.')], HRESULT, 'Password',
              ( ['in'], BSTR, 'rhs' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the password should be saved.')], HRESULT, 'SavePassword',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the password should be saved.')], HRESULT, 'SavePassword',
              ( ['in'], VARIANT_BOOL, 'flag' )),
    COMMETHOD(['propget', helpstring(u'Filters out only the specified services. Array of strings.')], HRESULT, 'FilterServices',
              ( ['retval', 'out'], POINTER(VARIANT), 'names' )),
    COMMETHOD(['propput', helpstring(u'Filters out only the specified services. Array of strings.')], HRESULT, 'FilterServices',
              ( ['in'], VARIANT, 'names' )),
]
################################################################
## code template for IIMSConnection implementation
##class IIMSConnection_Impl(object):
##    def _get(self):
##        u'User name.'
##        #return UserName
##    def _set(self, UserName):
##        u'User name.'
##    UserName = property(_get, _set, doc = _set.__doc__)
##
##    def SaveToFile(self, Path):
##        u'Writes an IMS connection file containing the URL.'
##        #return 
##
##    def _get(self):
##        u'URL to ArcIMS server.'
##        #return URL
##    def _set(self, URL):
##        u'URL to ArcIMS server.'
##    URL = property(_get, _set, doc = _set.__doc__)
##
##    def LoadFromFile(self, Path):
##        u'Loads an IMS connection file containing the URL.'
##        #return 
##
##    @property
##    def IsConnected(self):
##        u'Indicates whether the IMS connection has been made.'
##        #return IsConnected
##
##    @property
##    def FileName(self):
##        u'Path to the IMS connection file.'
##        #return FileName
##
##    def Connect(self):
##        u'Connects to an ArcIMS server.'
##        #return 
##
##    def _get(self):
##        u'Filters out only the specified services. Array of strings.'
##        #return names
##    def _set(self, names):
##        u'Filters out only the specified services. Array of strings.'
##    FilterServices = property(_get, _set, doc = _set.__doc__)
##
##    def Disconnect(self):
##        u'Disconnects from an ArcIMS server.'
##        #return 
##
##    def _set(self, rhs):
##        u'Password.'
##    Password = property(fset = _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the password should be saved.'
##        #return flag
##    def _set(self, flag):
##        u'Indicates if the password should be saved.'
##    SavePassword = property(_get, _set, doc = _set.__doc__)
##

class GxFilterSDEFeatureClasses(CoClass):
    u'A filter for displaying/choosing SDE feature classes.'
    _reg_clsid_ = GUID('{D2724374-EA1D-11D3-A682-0008C7D3AE8D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterSDEFeatureClasses._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxFilterGlobeServers(CoClass):
    u'A filter for displaying/choosing globe service objects.'
    _reg_clsid_ = GUID('{214F0F87-F421-4CFC-BE6F-3DE1EB4C6C98}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterGlobeServers._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxFilterWMS(CoClass):
    u'A filter for displaying/choosing WMS service object.'
    _reg_clsid_ = GUID('{DE622381-4F00-4555-8200-01D886697C67}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterWMS._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxFilterContainers(CoClass):
    u'A filter for displaying/choosing containers (for example, folders and databases).'
    _reg_clsid_ = GUID('{7EB9E472-3A09-489E-9AFB-93AFB1B17881}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterContainers._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxFilterCoverageFeatureClasses(CoClass):
    u'A filter for displaying/choosing coverage feature classes.'
    _reg_clsid_ = GUID('{29652E4D-E65E-11D3-A682-0008C7D3AE8D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterCoverageFeatureClasses._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeType]

class GxFilterGPServers(CoClass):
    u'A filter for displaying/choosing gp server objects.'
    _reg_clsid_ = GUID('{AB49479B-2F39-44F8-89F8-246DFF78D276}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterGPServers._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class ServiceDefinitionFileNativeType(CoClass):
    u'Native type for a service definition file.'
    _reg_clsid_ = GUID('{284F18EC-41FD-48B5-BC1C-F49CE483C449}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
ServiceDefinitionFileNativeType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeType]

class GxFilterGeoDataServers(CoClass):
    u'A filter for displaying/choosing geodataserver objects.'
    _reg_clsid_ = GUID('{1208F728-F2D1-4AF1-97C7-6E8FCEC94DD1}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterGeoDataServers._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GPToolboxNativeType(CoClass):
    u'Geoprocessing Toolbox Native Type.'
    _reg_clsid_ = GUID('{B2B01BAC-9FB7-4F5A-971A-7CA3A58279E0}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GPToolboxNativeType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeType]

IGxFolder._methods_ = [
    COMMETHOD(['propget', helpstring(u'The Name objects for all file system workspaces represented by this folder.')], HRESULT, 'FileSystemWorkspaceNames',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IEnumName)), 'workspaceNames' )),
]
################################################################
## code template for IGxFolder implementation
##class IGxFolder_Impl(object):
##    @property
##    def FileSystemWorkspaceNames(self):
##        u'The Name objects for all file system workspaces represented by this folder.'
##        #return workspaceNames
##

class Library(object):
    u'Esri Catalog Object Library 10.2'
    name = u'esriCatalog'
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)

IGxTaskServicesFolder._methods_ = [
    COMMETHOD(['propput', helpstring(u'The folder name.')], HRESULT, 'Name',
              ( ['in'], BSTR, 'rhs' )),
]
################################################################
## code template for IGxTaskServicesFolder implementation
##class IGxTaskServicesFolder_Impl(object):
##    def _set(self, rhs):
##        u'The folder name.'
##    Name = property(fset = _set, doc = _set.__doc__)
##

class GxFilterGlobeCaches(CoClass):
    u'A filter for displaying/choosing Globe Layer Caches.'
    _reg_clsid_ = GUID('{E4A322D0-D2B2-40C1-86FA-AE4D0EA7929F}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterGlobeCaches._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

IGxThumbnail._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The Thumbnail.')], HRESULT, 'Thumbnail',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IPicture), 'picture' )),
    COMMETHOD(['propget', helpstring(u'The Thumbnail.')], HRESULT, 'Thumbnail',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IPicture)), 'picture' )),
]
################################################################
## code template for IGxThumbnail implementation
##class IGxThumbnail_Impl(object):
##    @property
##    def Thumbnail(self, picture):
##        u'The Thumbnail.'
##        #return 
##

class GxFilterGeoDatasetsAndCoordinateSystems(CoClass):
    u'A filter for displaying/choosing datasets or coordinate systems.'
    _reg_clsid_ = GUID('{74EA2CC4-0E97-4EFF-9B36-16AB6E6822C6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterGeoDatasetsAndCoordinateSystems._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

IGxTaskServicesRootFolder._methods_ = [
    COMMETHOD(['propget', helpstring(u'The fully qualified name.')], HRESULT, 'DisplayName',
              ( ['retval', 'out'], POINTER(BSTR), 'pDisplayName' )),
]
################################################################
## code template for IGxTaskServicesRootFolder implementation
##class IGxTaskServicesRootFolder_Impl(object):
##    @property
##    def DisplayName(self):
##        u'The fully qualified name.'
##        #return pDisplayName
##

IGxTaskServicesConnection._methods_ = [
]
################################################################
## code template for IGxTaskServicesConnection implementation
##class IGxTaskServicesConnection_Impl(object):

class GxIMSConnectionFactory(CoClass):
    u'Esri GxIMSConnection object factory.'
    _reg_clsid_ = GUID('{FEA91207-522C-48C5-AE64-6E6C9825F8CA}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxIMSConnectionFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFactory, IGxObjectFactoryFileExtensions]

IGxFilterDataElements._methods_ = [
    COMMETHOD(['propget', helpstring(u'Data element domain.')], HRESULT, 'ChooseDomain',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDomain)), 'domain' )),
    COMMETHOD(['propputref', helpstring(u'Data element domain.')], HRESULT, 'ChooseDomain',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDomain), 'domain' )),
    COMMETHOD(['propget', helpstring(u'Data element domain.')], HRESULT, 'DisplayDomain',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDomain)), 'domain' )),
    COMMETHOD(['propputref', helpstring(u'Data element domain.')], HRESULT, 'DisplayDomain',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDomain), 'domain' )),
    COMMETHOD(['propput', helpstring(u'Filter name.')], HRESULT, 'Name',
              ( ['in'], BSTR, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Filter description.')], HRESULT, 'Description',
              ( ['in'], BSTR, 'rhs' )),
]
################################################################
## code template for IGxFilterDataElements implementation
##class IGxFilterDataElements_Impl(object):
##    def DisplayDomain(self, domain):
##        u'Data element domain.'
##        #return 
##
##    def ChooseDomain(self, domain):
##        u'Data element domain.'
##        #return 
##
##    def _set(self, rhs):
##        u'Filter name.'
##    Name = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Filter description.'
##    Description = property(fset = _set, doc = _set.__doc__)
##

IGxObject._methods_ = [
    COMMETHOD(['propget', helpstring(u'The short name of the object.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'The full name of the object.')], HRESULT, 'FullName',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'The base name of the object (i.e. no extension).')], HRESULT, 'BaseName',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'The category of the object.')], HRESULT, 'Category',
              ( ['retval', 'out'], POINTER(BSTR), 'Category' )),
    COMMETHOD(['propget', helpstring(u'The parent of the object.')], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(IGxObject)), 'Parent' )),
    COMMETHOD(['propget', helpstring(u'The class ID of this object.')], HRESULT, 'ClassID',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID)), 'ClassID' )),
    COMMETHOD(['propget', helpstring(u'The Name for the internal object that this GxObject represents.')], HRESULT, 'InternalObjectName',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName)), 'InternalObjectName' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the object is still valid.')], HRESULT, 'IsValid',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsValid' )),
    COMMETHOD([helpstring(u'Attaches the object to its parent and the catalog.')], HRESULT, 'Attach',
              ( ['in'], POINTER(IGxObject), 'Parent' ),
              ( ['in'], POINTER(IGxCatalog), 'pCatalog' )),
    COMMETHOD([helpstring(u'Instructs the object to detach itself from its parent and the catalog.')], HRESULT, 'Detach'),
    COMMETHOD([helpstring(u'Updates the object and any children of the object.')], HRESULT, 'Refresh'),
]
################################################################
## code template for IGxObject implementation
##class IGxObject_Impl(object):
##    @property
##    def Category(self):
##        u'The category of the object.'
##        #return Category
##
##    @property
##    def ClassID(self):
##        u'The class ID of this object.'
##        #return ClassID
##
##    @property
##    def Name(self):
##        u'The short name of the object.'
##        #return Name
##
##    @property
##    def Parent(self):
##        u'The parent of the object.'
##        #return Parent
##
##    @property
##    def IsValid(self):
##        u'Indicates if the object is still valid.'
##        #return IsValid
##
##    @property
##    def BaseName(self):
##        u'The base name of the object (i.e. no extension).'
##        #return Name
##
##    @property
##    def InternalObjectName(self):
##        u'The Name for the internal object that this GxObject represents.'
##        #return InternalObjectName
##
##    def Refresh(self):
##        u'Updates the object and any children of the object.'
##        #return 
##
##    def Attach(self, Parent, pCatalog):
##        u'Attaches the object to its parent and the catalog.'
##        #return 
##
##    @property
##    def FullName(self):
##        u'The full name of the object.'
##        #return Name
##
##    def Detach(self):
##        u'Instructs the object to detach itself from its parent and the catalog.'
##        #return 
##

IGxObjectDeleteOptions._methods_ = [
    COMMETHOD(['propput', helpstring(u'Behavior when deleting multiple objects.')], HRESULT, 'DeleteOption',
              ( ['in'], esriGxDeleteOption, 'option' )),
    COMMETHOD(['propget', helpstring(u'Behavior when deleting multiple objects.')], HRESULT, 'DeleteOption',
              ( ['retval', 'out'], POINTER(esriGxDeleteOption), 'option' )),
]
################################################################
## code template for IGxObjectDeleteOptions implementation
##class IGxObjectDeleteOptions_Impl(object):
##    def _get(self):
##        u'Behavior when deleting multiple objects.'
##        #return option
##    def _set(self, option):
##        u'Behavior when deleting multiple objects.'
##    DeleteOption = property(_get, _set, doc = _set.__doc__)
##

class GxPrjFile(CoClass):
    u'GxObject that represents GxPrjFile.'
    _reg_clsid_ = GUID('{A38CB585-95CE-11D2-AD2A-00C04FA33A15}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
class IGxPrjFile2(IGxPrjFile):
    _case_insensitive_ = True
    u'Provides access to members that returns the properties of a PRJ file.'
    _iid_ = GUID('{4C8FCEF2-199C-4A31-B06B-440F34CC60F9}')
    _idlflags_ = ['oleautomation']
GxPrjFile._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxFile, IGxFileSetup, IGxObject, IGxObjectEdit, IGxObjectInternalName, IGxObjectProperties, IGxObjectUI, IGxPrjFile, IGxPrjFile2, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, IGxDataElement, IGxDataElementHelper]

class GxAGSWMServer(CoClass):
    u'GxObject that represents an ArcGIS Server Workflow Manager object.'
    _reg_clsid_ = GUID('{CE01F6B9-DEDA-410F-B896-A675B34D2BD1}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxAGSWMServer._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectEdit, IGxObjectUI, IGxObjectProperties, IGxAGSObject, IGxAGSObject2, IGxAGSObject3, IGxItemInfo, IGxAGSWMServer, IGxThumbnail, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit]

IGxRemoteContainer._methods_ = [
]
################################################################
## code template for IGxRemoteContainer implementation
##class IGxRemoteContainer_Impl(object):

IGxBasicObject._methods_ = [
]
################################################################
## code template for IGxBasicObject implementation
##class IGxBasicObject_Impl(object):

IGxDataset._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The associated dataset name.')], HRESULT, 'DatasetName',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetName), 'DatasetName' )),
    COMMETHOD(['propget', helpstring(u'The associated dataset name.')], HRESULT, 'DatasetName',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetName)), 'DatasetName' )),
    COMMETHOD(['propget', helpstring(u'The associated dataset.')], HRESULT, 'Dataset',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataset)), 'Dataset' )),
    COMMETHOD(['propget', helpstring(u'The type of the associated dataset.')], HRESULT, 'Type',
              ( ['retval', 'out'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriDatasetType), 'Type' )),
]
################################################################
## code template for IGxDataset implementation
##class IGxDataset_Impl(object):
##    @property
##    def DatasetName(self, DatasetName):
##        u'The associated dataset name.'
##        #return 
##
##    @property
##    def Type(self):
##        u'The type of the associated dataset.'
##        #return Type
##
##    @property
##    def Dataset(self):
##        u'The associated dataset.'
##        #return Dataset
##

class GxFilterPersonalGeodatabases(CoClass):
    u'A filter for displaying/choosing personal geodatabases.'
    _reg_clsid_ = GUID('{402A9393-E951-11D3-A682-0008C7D3AE8D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterPersonalGeodatabases._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

IGxObjectWizard._methods_ = [
    COMMETHOD([helpstring(u'Called when the object is double-clicked.')], HRESULT, 'Invoke',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hParentWnd' )),
]
################################################################
## code template for IGxObjectWizard implementation
##class IGxObjectWizard_Impl(object):
##    def Invoke(self, hParentWnd):
##        u'Called when the object is double-clicked.'
##        #return 
##

class GxReport(CoClass):
    u'GxObject that represents a report.'
    _reg_clsid_ = GUID('{1949E623-0051-4D24-8348-58677E812670}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxReport._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectUI, IGxObjectEdit, IGxFile, IGxThumbnail, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, IGxObjectInternalName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, IGxObjectProperties, IGxDataElement, IGxDataElementHelper]

IGxDiskConnection2._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates whether the disk connection has children cached.')], HRESULT, 'HasCachedChildren',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'HasCachedChildren' )),
    COMMETHOD([helpstring(u"Refresh the disk connection's status (i.e availability).")], HRESULT, 'RefreshStatus'),
]
################################################################
## code template for IGxDiskConnection2 implementation
##class IGxDiskConnection2_Impl(object):
##    def RefreshStatus(self):
##        u"Refresh the disk connection's status (i.e availability)."
##        #return 
##
##    @property
##    def HasCachedChildren(self):
##        u'Indicates whether the disk connection has children cached.'
##        #return HasCachedChildren
##

IGxCatalogDefaultDatabase._methods_ = [
    COMMETHOD(['propget', helpstring(u'The default geodatabase.')], HRESULT, 'DefaultDatabaseName',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceName)), 'ppWorkspaceName' )),
    COMMETHOD(['propput', helpstring(u'The default geodatabase.')], HRESULT, 'DefaultDatabaseName',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceName), 'ppWorkspaceName' )),
    COMMETHOD(['propget', helpstring(u'The default geodatabase.  Does not perform validation on the geodatabase.')], HRESULT, 'DefaultDatabaseNameNoValidate',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceName)), 'ppWorkspaceName' )),
    COMMETHOD(['propput', helpstring(u'The default geodatabase.  Does not perform validation on the geodatabase.')], HRESULT, 'DefaultDatabaseNameNoValidate',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceName), 'ppWorkspaceName' )),
]
################################################################
## code template for IGxCatalogDefaultDatabase implementation
##class IGxCatalogDefaultDatabase_Impl(object):
##    def _get(self):
##        u'The default geodatabase.'
##        #return ppWorkspaceName
##    def _set(self, ppWorkspaceName):
##        u'The default geodatabase.'
##    DefaultDatabaseName = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The default geodatabase.  Does not perform validation on the geodatabase.'
##        #return ppWorkspaceName
##    def _set(self, ppWorkspaceName):
##        u'The default geodatabase.  Does not perform validation on the geodatabase.'
##    DefaultDatabaseNameNoValidate = property(_get, _set, doc = _set.__doc__)
##

IGxObjectContainer._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if the object has any children.')], HRESULT, 'HasChildren',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'HasChildren' )),
    COMMETHOD(['propget', helpstring(u'An enumeration of the child objects.')], HRESULT, 'Children',
              ( ['retval', 'out'], POINTER(POINTER(IEnumGxObject)), 'Children' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the objects children are available for viewing in the tree-view.')], HRESULT, 'AreChildrenViewable',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'areViewable' )),
    COMMETHOD([helpstring(u'Adds a new child and returns a reference to it.  However, if a duplicate already exists, the function returns the existing child instead.')], HRESULT, 'AddChild',
              ( ['in'], POINTER(IGxObject), 'child' ),
              ( ['retval', 'out'], POINTER(POINTER(IGxObject)), 'resultingChild' )),
    COMMETHOD([helpstring(u'Deletes the specified child object.')], HRESULT, 'DeleteChild',
              ( ['in'], POINTER(IGxObject), 'child' )),
]
################################################################
## code template for IGxObjectContainer implementation
##class IGxObjectContainer_Impl(object):
##    def AddChild(self, child):
##        u'Adds a new child and returns a reference to it.  However, if a duplicate already exists, the function returns the existing child instead.'
##        #return resultingChild
##
##    def DeleteChild(self, child):
##        u'Deletes the specified child object.'
##        #return 
##
##    @property
##    def AreChildrenViewable(self):
##        u'Indicates if the objects children are available for viewing in the tree-view.'
##        #return areViewable
##
##    @property
##    def Children(self):
##        u'An enumeration of the child objects.'
##        #return Children
##
##    @property
##    def HasChildren(self):
##        u'Indicates if the object has any children.'
##        #return HasChildren
##

class IGxToolbox(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manage tools for the current selection.'
    _iid_ = GUID('{1B6629EF-A67D-11D2-AF6C-080009EC734B}')
    _idlflags_ = ['oleautomation']
IGxToolbox._methods_ = [
    COMMETHOD([helpstring(u'Returns an array of names of tools that apply to the selection.')], HRESULT, 'GetApplicableTools',
              ( ['in'], POINTER(IEnumGxObject), 'Selection' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'toolNames' )),
    COMMETHOD([helpstring(u'Executes a named tool with the specified selection.')], HRESULT, 'Execute',
              ( ['in'], BSTR, 'toolName' ),
              ( ['in'], POINTER(IEnumGxObject), 'Selection' )),
]
################################################################
## code template for IGxToolbox implementation
##class IGxToolbox_Impl(object):
##    def GetApplicableTools(self, Selection):
##        u'Returns an array of names of tools that apply to the selection.'
##        #return toolNames
##
##    def Execute(self, toolName, Selection):
##        u'Executes a named tool with the specified selection.'
##        #return 
##

class GxAGSGeometry(CoClass):
    u'GxObject that represents an ArcGIS Geometry Server Service object.'
    _reg_clsid_ = GUID('{E86C46FD-284E-4357-A711-80D800A66A20}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxAGSGeometry._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectEdit, IGxObjectUI, IGxObjectProperties, IGxAGSObject, IGxAGSObject2, IGxAGSObject3, IGxItemInfo, IGxAGSGeometry, IGxThumbnail, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit]

class IGxObjectSortAlwaysOnTop(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the interface which makes the GxObject ALWAYS stay at the top of sort list (regardless of sorting order). eg. GxAddAGSConnection.'
    _iid_ = GUID('{5BE00D0D-D750-433C-979E-8D872CBDD6FC}')
    _idlflags_ = ['oleautomation']
IGxObjectSortAlwaysOnTop._methods_ = [
]
################################################################
## code template for IGxObjectSortAlwaysOnTop implementation
##class IGxObjectSortAlwaysOnTop_Impl(object):

class GxPrjFileFactory(CoClass):
    u'Esri GxPrjFile object factory.'
    _reg_clsid_ = GUID('{A38CB586-95CE-11D2-AD2A-00C04FA33A15}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxPrjFileFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFactory, IGxObjectFactoryMetadata, IGxObjectFactoryPriority, IGxObjectFactoryFileExtensions]

class GxAGSGeoDataServer(CoClass):
    u'GxObject that represents an ArcGIS Server geodataserver object.'
    _reg_clsid_ = GUID('{B96CF02A-B113-40DA-9D01-DCA908B72ED6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxAGSGeoDataServer._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectEdit, IGxObjectUI, IGxObjectProperties, IGxAGSObject, IGxAGSObject2, IGxAGSObject3, IGxItemInfo, IGxAGSGeoDataServer, IGxThumbnail, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit]

IGxFileFilter._methods_ = [
    COMMETHOD([helpstring(u'Checks to see if the indicated file passes the filter.')], HRESULT, 'Filter',
              ( ['in'], BSTR, 'FilePath' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'passesFilter' )),
    COMMETHOD([helpstring(u'The index of the file type in the filter or -1.')], HRESULT, 'FindFileType',
              ( ['in'], BSTR, 'Extension' ),
              ( ['retval', 'out'], POINTER(c_int), 'index' )),
    COMMETHOD(['propget', helpstring(u'The number of file types for the filter.')], HRESULT, 'FileTypeCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD([helpstring(u'Returns information on the file type at the specified index in the file filter.')], HRESULT, 'GetFileType',
              ( ['in'], c_int, 'index' ),
              ( ['out'], POINTER(BSTR), 'Extension' ),
              ( ['out'], POINTER(BSTR), 'Description' ),
              ( ['out'], POINTER(BSTR), 'imageFile' ),
              ( ['out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'smallBitmap' ),
              ( ['out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'largeBitmap' )),
    COMMETHOD([helpstring(u'Add the file type to the collection.')], HRESULT, 'AddFileType',
              ( ['in'], BSTR, 'Extension' ),
              ( ['in'], BSTR, 'Description' ),
              ( ['in'], BSTR, 'filePathImage' )),
    COMMETHOD([helpstring(u'Remove the file type.')], HRESULT, 'DeleteFileType',
              ( ['in'], c_int, 'index' )),
]
################################################################
## code template for IGxFileFilter implementation
##class IGxFileFilter_Impl(object):
##    def DeleteFileType(self, index):
##        u'Remove the file type.'
##        #return 
##
##    def FindFileType(self, Extension):
##        u'The index of the file type in the filter or -1.'
##        #return index
##
##    @property
##    def FileTypeCount(self):
##        u'The number of file types for the filter.'
##        #return Count
##
##    def Filter(self, FilePath):
##        u'Checks to see if the indicated file passes the filter.'
##        #return passesFilter
##
##    def GetFileType(self, index):
##        u'Returns information on the file type at the specified index in the file filter.'
##        #return Extension, Description, imageFile, smallBitmap, largeBitmap
##
##    def AddFileType(self, Extension, Description, filePathImage):
##        u'Add the file type to the collection.'
##        #return 
##

class IGxLocator(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members for retrieving the locator.'
    _iid_ = GUID('{5F01E7B0-49F2-11D3-9F51-00C04F6BDF06}')
    _idlflags_ = ['oleautomation']
IGxLocator._methods_ = [
    COMMETHOD(['propputref', helpstring(u'Name object for the locator.')], HRESULT, 'LocatorName',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ILocatorName), 'Name' )),
    COMMETHOD(['propget', helpstring(u'Name object for the locator.')], HRESULT, 'LocatorName',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ILocatorName)), 'Name' )),
    COMMETHOD(['propget', helpstring(u'Locator represented by the GxLocator.')], HRESULT, 'Locator',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ILocator)), 'Locator' )),
]
################################################################
## code template for IGxLocator implementation
##class IGxLocator_Impl(object):
##    @property
##    def LocatorName(self, Name):
##        u'Name object for the locator.'
##        #return 
##
##    @property
##    def Locator(self):
##        u'Locator represented by the GxLocator.'
##        #return Locator
##

IGxPrjFile2._methods_ = [
    COMMETHOD(['propget', helpstring(u'The vertical or horizontal coordinate system contained in the PRJ file.')], HRESULT, 'SpatialReferenceInfo',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReferenceInfo)), 'SpatialReferenceInfo' )),
]
################################################################
## code template for IGxPrjFile2 implementation
##class IGxPrjFile2_Impl(object):
##    @property
##    def SpatialReferenceInfo(self):
##        u'The vertical or horizontal coordinate system contained in the PRJ file.'
##        #return SpatialReferenceInfo
##

IGxObjectSort._methods_ = [
    COMMETHOD(['propput', helpstring(u'Indicates if sorting is enabled for this GxObject.')], HRESULT, 'SortEnabled',
              ( ['in'], VARIANT_BOOL, 'Path' )),
    COMMETHOD(['propget', helpstring(u'Indicates if sorting is enabled for this GxObject.')], HRESULT, 'SortEnabled',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Path' )),
]
################################################################
## code template for IGxObjectSort implementation
##class IGxObjectSort_Impl(object):
##    def _get(self):
##        u'Indicates if sorting is enabled for this GxObject.'
##        #return Path
##    def _set(self, Path):
##        u'Indicates if sorting is enabled for this GxObject.'
##    SortEnabled = property(_get, _set, doc = _set.__doc__)
##

class IMSFeatureService(CoClass):
    u'GxObject that represents ArcIMS Feature Service.'
    _reg_clsid_ = GUID('{344EAFF1-6A1A-4AEC-BB17-3BBEBB26C699}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
IMSFeatureService._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectUI, comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IIMSServiceDescription, IGxLayerSource, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, IGxObjectProperties, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, IGxObjectContainer, IGxObjectEdit, IGxObjectInternalName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IIMSUserRole, IGxThumbnail]

class GxAGSGlobe(CoClass):
    u'GxObject that represents an ArcGIS Server globe object.'
    _reg_clsid_ = GUID('{27441B4C-79D8-42E0-9867-DCC06531EB47}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxAGSGlobe._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectEdit, IGxObjectUI, IGxObjectProperties, IGxAGSObject, IGxAGSObject2, IGxAGSObject3, IGxItemInfo, IGxAGSGlobe, IGxLayerSource, IGxObjectContainer, IGxThumbnail, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit]

class IGxObjectSortAlwaysOnBottom(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the interface which makes the GxObject ALWAYS stay at the botton of sort list (regardless of sorting order). eg. GxAGSDatabaseFolder.'
    _iid_ = GUID('{B90717C2-9124-4CAC-A52B-F160CDF03D4B}')
    _idlflags_ = ['oleautomation']
IGxObjectSortAlwaysOnBottom._methods_ = [
]
################################################################
## code template for IGxObjectSortAlwaysOnBottom implementation
##class IGxObjectSortAlwaysOnBottom_Impl(object):

IGxCatalog._methods_ = [
    COMMETHOD([helpstring(u'Closes the catalog object.  Clients that create a catalog object must call this method when they are finished using it.')], HRESULT, 'Close'),
    COMMETHOD(['propget', helpstring(u'The selection.')], HRESULT, 'Selection',
              ( ['retval', 'out'], POINTER(POINTER(IGxSelection)), 'Selection' )),
    COMMETHOD(['propget', helpstring(u'The first selected object, or the location if no objects are selected.')], HRESULT, 'SelectedObject',
              ( ['retval', 'out'], POINTER(POINTER(IGxObject)), 'SelectedObject' )),
    COMMETHOD(['propput', helpstring(u"The location to the specified path.  If the path isn't yet part of the catalog, it is added as a folder connection.")], HRESULT, 'Location',
              ( ['in'], BSTR, 'rhs' )),
    COMMETHOD(['propget', helpstring(u'The file filter.')], HRESULT, 'FileFilter',
              ( ['retval', 'out'], POINTER(POINTER(IGxFileFilter)), 'Filter' )),
    COMMETHOD([helpstring(u'Adds a folder connection to the catalog and returns the folder object.')], HRESULT, 'ConnectFolder',
              ( ['in'], BSTR, 'folderPath' ),
              ( ['retval', 'out'], POINTER(POINTER(IGxFolder)), 'folder' )),
    COMMETHOD([helpstring(u'Removes a folder connection from the catalog.')], HRESULT, 'DisconnectFolder',
              ( ['in'], BSTR, 'folderPath' )),
    COMMETHOD([helpstring(u'Called when a new object has been added to part of the catalog.')], HRESULT, 'ObjectAdded',
              ( ['in'], POINTER(IGxObject), 'gxObject' )),
    COMMETHOD([helpstring(u'Called when an existing object has been deleted from part of the catalog.')], HRESULT, 'ObjectDeleted',
              ( ['in'], POINTER(IGxObject), 'gxObject' )),
    COMMETHOD([helpstring(u'Called when an existing object from part of the catalog has been changed.')], HRESULT, 'ObjectChanged',
              ( ['in'], POINTER(IGxObject), 'gxObject' )),
    COMMETHOD([helpstring(u'Called when an existing object has been refreshed.')], HRESULT, 'ObjectRefreshed',
              ( ['in'], POINTER(IGxObject), 'gxObject' )),
    COMMETHOD([helpstring(u'Constructs the full name for an object.')], HRESULT, 'ConstructFullName',
              ( ['in'], POINTER(IGxObject), 'gxObject' ),
              ( ['retval', 'out'], POINTER(BSTR), 'FullName' )),
    COMMETHOD([helpstring(u'Finds an object in the catalog tree given its full name.  Returns a Variant containing an IGxObject or IEnumGxObject (if duplicate names were encountered), along with the number of objects found.')], HRESULT, 'GetObjectFromFullName',
              ( ['in'], BSTR, 'FullName' ),
              ( ['out'], POINTER(c_int), 'numFound' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'result' )),
]
################################################################
## code template for IGxCatalog implementation
##class IGxCatalog_Impl(object):
##    @property
##    def Selection(self):
##        u'The selection.'
##        #return Selection
##
##    def ObjectRefreshed(self, gxObject):
##        u'Called when an existing object has been refreshed.'
##        #return 
##
##    def DisconnectFolder(self, folderPath):
##        u'Removes a folder connection from the catalog.'
##        #return 
##
##    @property
##    def FileFilter(self):
##        u'The file filter.'
##        #return Filter
##
##    def ConstructFullName(self, gxObject):
##        u'Constructs the full name for an object.'
##        #return FullName
##
##    def ObjectDeleted(self, gxObject):
##        u'Called when an existing object has been deleted from part of the catalog.'
##        #return 
##
##    def _set(self, rhs):
##        u"The location to the specified path.  If the path isn't yet part of the catalog, it is added as a folder connection."
##    Location = property(fset = _set, doc = _set.__doc__)
##
##    def GetObjectFromFullName(self, FullName):
##        u'Finds an object in the catalog tree given its full name.  Returns a Variant containing an IGxObject or IEnumGxObject (if duplicate names were encountered), along with the number of objects found.'
##        #return numFound, result
##
##    def Close(self):
##        u'Closes the catalog object.  Clients that create a catalog object must call this method when they are finished using it.'
##        #return 
##
##    def ObjectChanged(self, gxObject):
##        u'Called when an existing object from part of the catalog has been changed.'
##        #return 
##
##    @property
##    def SelectedObject(self):
##        u'The first selected object, or the location if no objects are selected.'
##        #return SelectedObject
##
##    def ObjectAdded(self, gxObject):
##        u'Called when a new object has been added to part of the catalog.'
##        #return 
##
##    def ConnectFolder(self, folderPath):
##        u'Adds a folder connection to the catalog and returns the folder object.'
##        #return folder
##

IGxObjectInternalName._methods_ = [
    COMMETHOD(['propget', helpstring(u'The Name for the internal object that this GxObject represents.')], HRESULT, 'InternalObjectName',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName)), 'InternalObjectName' )),
    COMMETHOD(['propputref', helpstring(u'The Name for the internal object that this GxObject represents.')], HRESULT, 'InternalObjectName',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName), 'InternalObjectName' )),
]
################################################################
## code template for IGxObjectInternalName implementation
##class IGxObjectInternalName_Impl(object):
##    def InternalObjectName(self, InternalObjectName):
##        u'The Name for the internal object that this GxObject represents.'
##        #return 
##

class GxAGSCatalog(CoClass):
    u'GxObject that represents an ArcGIS Server data sharing object.'
    _reg_clsid_ = GUID('{82FACE5C-9833-485D-9E1A-D7206C54F6CD}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxAGSCatalog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectEdit, IGxObjectUI, IGxObjectProperties, IGxAGSObject, IGxAGSObject2, IGxAGSObject3, IGxItemInfo, IGxAGSCatalog, IGxThumbnail, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit]

IEnumGxObject._methods_ = [
    COMMETHOD([helpstring(u'The next object.')], HRESULT, 'Next',
              ( ['retval', 'out'], POINTER(POINTER(IGxObject)), 'object' )),
    COMMETHOD([helpstring(u'Starts the enumeration at the beginning.')], HRESULT, 'Reset'),
]
################################################################
## code template for IEnumGxObject implementation
##class IEnumGxObject_Impl(object):
##    def Reset(self):
##        u'Starts the enumeration at the beginning.'
##        #return 
##
##    def Next(self):
##        u'The next object.'
##        #return object
##

class GxAGSGeoprocessing(CoClass):
    u'GxObject that represents an ArcGIS Server geoprocessing object.'
    _reg_clsid_ = GUID('{EB40C04E-EC0F-49AD-88A4-05CC8F4A0B85}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxAGSGeoprocessing._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectEdit, IGxObjectUI, IGxObjectProperties, IGxAGSObject, IGxAGSObject2, IGxAGSObject3, IGxItemInfo, IGxAGSGeoprocessing, IGxThumbnail, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit]

IGxGISServersFolder._methods_ = [
    COMMETHOD(['propput', helpstring(u'The full path for the GIS servers folder.')], HRESULT, 'Path',
              ( ['in'], BSTR, 'Path' )),
    COMMETHOD(['propget', helpstring(u'The full path for the GIS servers folder.')], HRESULT, 'Path',
              ( ['retval', 'out'], POINTER(BSTR), 'Path' )),
]
################################################################
## code template for IGxGISServersFolder implementation
##class IGxGISServersFolder_Impl(object):
##    def _get(self):
##        u'The full path for the GIS servers folder.'
##        #return Path
##    def _set(self, Path):
##        u'The full path for the GIS servers folder.'
##    Path = property(_get, _set, doc = _set.__doc__)
##

class GxFeatureDefinitionPackageFactory(CoClass):
    u'Esri GxFeatureDefinitionPackage object factory.'
    _reg_clsid_ = GUID('{BFAAF64C-A3CC-442B-8DA8-E27DDF9DA7F7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFeatureDefinitionPackageFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFactory, IGxObjectFactoryMetadata, IGxObjectFactoryFileExtensions]

class GxAGSLocator(CoClass):
    u'GxObject that represents an ArcGIS Server locator object.'
    _reg_clsid_ = GUID('{239AFF32-67CA-4403-8B93-149E7F2E94CD}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxAGSLocator._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectEdit, IGxObjectUI, IGxObjectProperties, IGxAGSObject, IGxAGSObject2, IGxAGSObject3, IGxItemInfo, IGxAGSLocator, IGxThumbnail, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit]

IGxShortcut._methods_ = [
    COMMETHOD(['propget', helpstring(u'The value of the Target property.')], HRESULT, 'Target',
              ( ['retval', 'out'], POINTER(POINTER(IGxObject)), 'Target' )),
    COMMETHOD(['propputref', helpstring(u'The value of the Target property.')], HRESULT, 'Target',
              ( ['in'], POINTER(IGxObject), 'Target' )),
    COMMETHOD(['propput', helpstring(u'The location of the target.')], HRESULT, 'TargetLocation',
              ( ['in'], BSTR, 'Location' )),
    COMMETHOD(['propget', helpstring(u'The location of the target.')], HRESULT, 'TargetLocation',
              ( ['retval', 'out'], POINTER(BSTR), 'Location' )),
]
################################################################
## code template for IGxShortcut implementation
##class IGxShortcut_Impl(object):
##    def _get(self):
##        u'The location of the target.'
##        #return Location
##    def _set(self, Location):
##        u'The location of the target.'
##    TargetLocation = property(_get, _set, doc = _set.__doc__)
##
##    def Target(self, Target):
##        u'The value of the Target property.'
##        #return 
##

class GxWMSMap(CoClass):
    u'GxWMSMap object for the ArcCatalog.'
    _reg_clsid_ = GUID('{C5F5CAC6-F07F-482D-9B29-3DCD206B942A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxWMSMap._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectEdit, IGxObjectUI, IGxObjectContainer, IGxObjectProperties, IGxThumbnail, IGxWMSMap, IGxLayerSource]

class GxAddWMSConnection(CoClass):
    u'The object of Add WMS connection.'
    _reg_clsid_ = GUID('{8E49FDED-581E-47FD-93B2-8778DD0A15D3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxAddWMSConnection._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectUI, IGxBasicObject, IGxObjectProperties, IGxObjectWizard]

class IIMSConnection2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members to connect to an ArcIMS server (IMS).'
    _iid_ = GUID('{2F81075F-0ADF-4DEA-9C0C-38F7E032705F}')
    _idlflags_ = ['oleautomation']
IIMSConnection2._methods_ = [
    COMMETHOD(['propget', helpstring(u'ArcIMS server version.')], HRESULT, 'Version',
              ( ['retval', 'out'], POINTER(BSTR), 'Version' )),
]
################################################################
## code template for IIMSConnection2 implementation
##class IIMSConnection2_Impl(object):
##    @property
##    def Version(self):
##        u'ArcIMS server version.'
##        #return Version
##

class GxWMSConnection(CoClass):
    u'The connection of WMS service.'
    _reg_clsid_ = GUID('{23C0B7A0-224C-4DC1-BF09-AAB72F18FAF2}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxWMSConnection._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectUI, IGxObjectContainer, IGxObjectEdit, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, IGxObjectWizard, IGxObjectProperties, IGxWMSConnection, IGxRemoteConnection]

class GxWMSConnectionFactory(CoClass):
    u'Gx Object Factory for GxWMSConnections.'
    _reg_clsid_ = GUID('{C2FE1CF6-4F7B-4116-806D-DB2E12E4A032}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxWMSConnectionFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFactory]

class RasterFormatPGDBFilter(CoClass):
    u'The format filter for Personal Geodatabase Raster.'
    _reg_clsid_ = GUID('{7B9EC1C3-F41B-4867-B4C3-1C8800AE3A9C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
RasterFormatPGDBFilter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter, IRasterFormatFilter]

IRemoteMetadata._methods_ = [
    COMMETHOD(['propput', helpstring(u'Name of metadata document on server.')], HRESULT, 'Dataset',
              ( ['in'], BSTR, 'Dataset' )),
    COMMETHOD(['propget', helpstring(u'Name of metadata document on server.')], HRESULT, 'Dataset',
              ( ['retval', 'out'], POINTER(BSTR), 'Dataset' )),
    COMMETHOD(['propput', helpstring(u'ArcIMS authenticated user owning metadata document.')], HRESULT, 'Owner',
              ( ['in'], BSTR, 'Owner' )),
    COMMETHOD(['propget', helpstring(u'ArcIMS authenticated user owning metadata document.')], HRESULT, 'Owner',
              ( ['retval', 'out'], POINTER(BSTR), 'Owner' )),
    COMMETHOD(['propput', helpstring(u'Unique id (UUID) of metadata document.')], HRESULT, 'UserID',
              ( ['in'], BSTR, 'UserID' )),
    COMMETHOD(['propget', helpstring(u'Unique id (UUID) of metadata document.')], HRESULT, 'UserID',
              ( ['retval', 'out'], POINTER(BSTR), 'UserID' )),
    COMMETHOD(['propput', helpstring(u'URL of metadata document on server.')], HRESULT, 'MetadataURL',
              ( ['in'], BSTR, 'URL' )),
    COMMETHOD(['propget', helpstring(u'URL of metadata document on server.')], HRESULT, 'MetadataURL',
              ( ['retval', 'out'], POINTER(BSTR), 'URL' )),
    COMMETHOD(['propput', helpstring(u'URL of thumbnail image on server.')], HRESULT, 'ThumbnailURL',
              ( ['in'], BSTR, 'URL' )),
    COMMETHOD(['propget', helpstring(u'URL of thumbnail image on server.')], HRESULT, 'ThumbnailURL',
              ( ['retval', 'out'], POINTER(BSTR), 'URL' )),
    COMMETHOD([helpstring(u'Creates a new folder as a child of this folder.')], HRESULT, 'CreateChild',
              ( ['in'], BSTR, 'server' ),
              ( ['in'], BSTR, 'Service' ),
              ( ['in'], BSTR, 'UserName' ),
              ( ['in'], BSTR, 'Password' ),
              ( ['in'], VARIANT_BOOL, 'isFolder' ),
              ( ['retval', 'out'], POINTER(POINTER(IGxObject)), 'child' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether this folder has children.')], HRESULT, 'HasChildren',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether this metadata document is a folder.')], HRESULT, 'isFolder',
              ( ['in'], VARIANT_BOOL, 'isFolder' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether this metadata document is a folder.')], HRESULT, 'isFolder',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'isFolder' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether this metadata document is the root document.')], HRESULT, 'IsRoot',
              ( ['in'], VARIANT_BOOL, 'IsRoot' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether this metadata document is the root document.')], HRESULT, 'IsRoot',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsRoot' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether this metadata document is private.')], HRESULT, 'IsPrivateDocument',
              ( ['in'], VARIANT_BOOL, 'isPrivate' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether this metadata document is private.')], HRESULT, 'IsPrivateDocument',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'isPrivate' )),
    COMMETHOD([helpstring(u'Publish the metadata of a set of datasets to an ArcIMS Metadata Server.')], HRESULT, 'PublishDatasets',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IEnumName), 'names' )),
    COMMETHOD(['propput', helpstring(u'The number of references to this document on the server.')], HRESULT, 'RefCount',
              ( ['in'], c_int, 'RefCount' )),
    COMMETHOD(['propget', helpstring(u'The number of references to this document on the server.')], HRESULT, 'RefCount',
              ( ['retval', 'out'], POINTER(c_int), 'RefCount' )),
    COMMETHOD(['propputref', helpstring(u'The extent of the dataset represented by this document.')], HRESULT, 'Extent',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'Extent' )),
    COMMETHOD(['propget', helpstring(u'The extent of the dataset represented by this document.')], HRESULT, 'Extent',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'Extent' )),
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
              ( ['retval', 'out'], POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.acIndexStatus), 'IndexStatus' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether this document is indexed on the server.')], HRESULT, 'IndexStatus',
              ( ['in'], comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.acIndexStatus, 'IndexStatus' )),
]
################################################################
## code template for IRemoteMetadata implementation
##class IRemoteMetadata_Impl(object):
##    def _get(self):
##        u'URL of metadata document on server.'
##        #return URL
##    def _set(self, URL):
##        u'URL of metadata document on server.'
##    MetadataURL = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether this metadata document is private.'
##        #return isPrivate
##    def _set(self, isPrivate):
##        u'Indicates whether this metadata document is private.'
##    IsPrivateDocument = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether this metadata document is the root document.'
##        #return IsRoot
##    def _set(self, IsRoot):
##        u'Indicates whether this metadata document is the root document.'
##    IsRoot = property(_get, _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Indicates whether this folder has children.'
##    HasChildren = property(fset = _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether this metadata document is a folder.'
##        #return isFolder
##    def _set(self, isFolder):
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
##        #return UserID
##    def _set(self, UserID):
##        u'Unique id (UUID) of metadata document.'
##    UserID = property(_get, _set, doc = _set.__doc__)
##
##    def CreateChild(self, server, Service, UserName, Password, isFolder):
##        u'Creates a new folder as a child of this folder.'
##        #return child
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
##        #return Dataset
##    def _set(self, Dataset):
##        u'Name of metadata document on server.'
##    Dataset = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The number of references to this document on the server.'
##        #return RefCount
##    def _set(self, RefCount):
##        u'The number of references to this document on the server.'
##    RefCount = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Extent(self, Extent):
##        u'The extent of the dataset represented by this document.'
##        #return 
##
##    def _get(self):
##        u'Indicates whether this document is indexed on the server.'
##        #return IndexStatus
##    def _set(self, IndexStatus):
##        u'Indicates whether this document is indexed on the server.'
##    IndexStatus = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'ArcIMS authenticated user owning metadata document.'
##        #return Owner
##    def _set(self, Owner):
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
##        #return URL
##    def _set(self, URL):
##        u'URL of thumbnail image on server.'
##    ThumbnailURL = property(_get, _set, doc = _set.__doc__)
##
##    def PublishDatasets(self, names):
##        u'Publish the metadata of a set of datasets to an ArcIMS Metadata Server.'
##        #return 
##

class GxWMSLayer(CoClass):
    u'GxWMSLayer object for the ArcCatalog.'
    _reg_clsid_ = GUID('{C5750B6A-D90F-4DEC-BD25-8222ED3A9133}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxWMSLayer._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectEdit, IGxObjectUI, IGxObjectProperties, IGxThumbnail, IGxWMSLayer, IGxLayerSource]

class RasterFormatTifFilter(CoClass):
    u'The format filter for TIFF.'
    _reg_clsid_ = GUID('{09D710F9-E104-4E91-B431-C1C269C9D762}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
RasterFormatTifFilter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter, IRasterFormatFilter]

class GxWCSCoverage(CoClass):
    u'GxWCSCoverage object for the ArcCatalog.'
    _reg_clsid_ = GUID('{99BAEC02-E7C6-4C9E-B2DA-B2C735EC03F4}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxWCSCoverage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectEdit, IGxObjectUI, IGxObjectProperties, IGxObjectInternalName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, IGxThumbnail, IGxWCSCoverage, IGxLayerSource]

class WCSConnectionNativeType(CoClass):
    u'The native type of WCS connection.'
    _reg_clsid_ = GUID('{BDA6C124-A6E2-47C4-9A22-0ED83827C959}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
WCSConnectionNativeType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeType]

IGxAGSMap._methods_ = [
]
################################################################
## code template for IGxAGSMap implementation
##class IGxAGSMap_Impl(object):

class GxToolbox(CoClass):
    u'Catalog object corresponding to toolboxes.'
    _reg_clsid_ = GUID('{6D540878-0233-47E4-A044-030A712B8CE7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxToolbox._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectUI, IGxObjectContainer, IGxObjectProperties, IGxPasteTarget, IGxCachedObjects, IGxObjectEdit, IGxMetadataSupport, IGxDataset, IGxGPToolbox, IGxFile, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, comtypes.gen._C031A050_82C6_4F8F_8836_5692631CFFE6_0_10_2.IGPToolboxEvents]

class GxAddWCSConnection(CoClass):
    u'The object of Add WCS connection.'
    _reg_clsid_ = GUID('{122B2BC2-256B-4701-B06B-C0CD1D5B498D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxAddWCSConnection._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectUI, IGxBasicObject, IGxObjectProperties, IGxObjectWizard]

class IGxAGSMobile(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of GxObject that represents a ArcGIS Server mobile object.'
    _iid_ = GUID('{6CC1AFBB-29A5-42AF-8A8C-06C233233266}')
    _idlflags_ = ['oleautomation']
IGxAGSMobile._methods_ = [
]
################################################################
## code template for IGxAGSMobile implementation
##class IGxAGSMobile_Impl(object):

class GxWCSConnection(CoClass):
    u'The connection of WCS service.'
    _reg_clsid_ = GUID('{CF7F898B-C996-46B7-AD3B-01737800CF93}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxWCSConnection._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectUI, IGxObjectContainer, IGxObjectEdit, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, IGxObjectWizard, IGxObjectProperties, IGxWCSConnection, IGxRemoteConnection]

class GxWCSConnectionFactory(CoClass):
    u'Gx Object Factory for GxWCSConnections.'
    _reg_clsid_ = GUID('{244928BD-DC5A-402F-ADE6-412C755C4D05}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxWCSConnectionFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFactory]

ISearchResultsLayer._methods_ = [
    COMMETHOD(['propput', helpstring(u'Full path to the search results layer file.')], HRESULT, 'Path',
              ( ['in'], BSTR, 'Path' )),
    COMMETHOD(['propget', helpstring(u'Full path to the search results layer file.')], HRESULT, 'Path',
              ( ['retval', 'out'], POINTER(BSTR), 'Path' )),
]
################################################################
## code template for ISearchResultsLayer implementation
##class ISearchResultsLayer_Impl(object):
##    def _get(self):
##        u'Full path to the search results layer file.'
##        #return Path
##    def _set(self, Path):
##        u'Full path to the search results layer file.'
##    Path = property(_get, _set, doc = _set.__doc__)
##

IGxAGSObject._methods_ = [
    COMMETHOD(['propget', helpstring(u'The associated AGS server object name.')], HRESULT, 'AGSServerObjectName',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IAGSServerObjectName)), 'agsObjectName' )),
    COMMETHOD(['propputref', helpstring(u'The associated AGS server object name.')], HRESULT, 'AGSServerObjectName',
              ( ['in'], POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IAGSServerObjectName), 'agsObjectName' )),
    COMMETHOD([helpstring(u'Presents a modal dialog to allow editing the properties of the server object.')], HRESULT, 'EditServerObjectProperties',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hParent' )),
    COMMETHOD(['propget', helpstring(u'The status of the server object.')], HRESULT, 'Status',
              ( ['retval', 'out'], POINTER(BSTR), 'Status' )),
    COMMETHOD(['propget', helpstring(u'The number of instances running.')], HRESULT, 'NumInstancesRunning',
              ( ['retval', 'out'], POINTER(c_int), 'number' )),
    COMMETHOD(['propget', helpstring(u'The number of instances in use.')], HRESULT, 'NumInstancesInUse',
              ( ['retval', 'out'], POINTER(c_int), 'number' )),
]
################################################################
## code template for IGxAGSObject implementation
##class IGxAGSObject_Impl(object):
##    @property
##    def Status(self):
##        u'The status of the server object.'
##        #return Status
##
##    def EditServerObjectProperties(self, hParent):
##        u'Presents a modal dialog to allow editing the properties of the server object.'
##        #return 
##
##    @property
##    def NumInstancesInUse(self):
##        u'The number of instances in use.'
##        #return number
##
##    def AGSServerObjectName(self, agsObjectName):
##        u'The associated AGS server object name.'
##        #return 
##
##    @property
##    def NumInstancesRunning(self):
##        u'The number of instances running.'
##        #return number
##

IGxAGSObject2._methods_ = [
    COMMETHOD(['propget', helpstring(u'Name of Server Object Type.')], HRESULT, 'ServerObjectType',
              ( ['retval', 'out'], POINTER(BSTR), 'ServerObjectType' )),
]
################################################################
## code template for IGxAGSObject2 implementation
##class IGxAGSObject2_Impl(object):
##    @property
##    def ServerObjectType(self):
##        u'Name of Server Object Type.'
##        #return ServerObjectType
##

IGxAGSObject3._methods_ = [
    COMMETHOD(['propget', helpstring(u'Server Object Configuration.')], HRESULT, 'ServerObjectConfiguration',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._18F2FC71_6B30_45B9_B101_037A8B868B66_0_10_2.IServerObjectConfiguration)), 'soc' )),
]
################################################################
## code template for IGxAGSObject3 implementation
##class IGxAGSObject3_Impl(object):
##    @property
##    def ServerObjectConfiguration(self):
##        u'Server Object Configuration.'
##        #return soc
##

class WMTSConnectionNativeType(CoClass):
    u'The native type of WMTS connection.'
    _reg_clsid_ = GUID('{7A3BF5FC-9A81-4C0F-AEED-D4FECF1FB45F}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
WMTSConnectionNativeType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeType]

class GxAddWMTSConnection(CoClass):
    u'The object of Add WMTS connection.'
    _reg_clsid_ = GUID('{4592334B-35EC-4A61-89AD-E1F1D8AAE744}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxAddWMTSConnection._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectUI, IGxBasicObject, IGxObjectProperties, IGxObjectWizard]

IGxItemInfo._methods_ = [
    COMMETHOD(['propget', helpstring(u'The ItemInfo of the service.')], HRESULT, 'ItemInfo',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IItemInfo)), 'ppItemInfo' )),
    COMMETHOD(['propput', helpstring(u'The ItemInfo of the service.')], HRESULT, 'ItemInfo',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IItemInfo), 'ppItemInfo' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the ItemInfo is editable.')], HRESULT, 'CanEditItemInfo',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pEditable' )),
]
################################################################
## code template for IGxItemInfo implementation
##class IGxItemInfo_Impl(object):
##    @property
##    def CanEditItemInfo(self):
##        u'Indicates whether the ItemInfo is editable.'
##        #return pEditable
##
##    def _get(self):
##        u'The ItemInfo of the service.'
##        #return ppItemInfo
##    def _set(self, ppItemInfo):
##        u'The ItemInfo of the service.'
##    ItemInfo = property(_get, _set, doc = _set.__doc__)
##

class GxFilterToolboxes(CoClass):
    u'Object used to filter for Toolboxes.'
    _reg_clsid_ = GUID('{8D9B3E90-A075-473B-B617-BC19076AA8E3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterToolboxes._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class GxWMTSConnection(CoClass):
    u'The connection of WMTS service.'
    _reg_clsid_ = GUID('{038DD7B7-A2B5-4AF9-8FAF-56B0E674F557}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxWMTSConnection._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectUI, IGxObjectContainer, IGxObjectEdit, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, IGxObjectWizard, IGxObjectProperties, IGxWMTSConnection, IGxRemoteConnection]

class GxWMTSConnectionFactory(CoClass):
    u'Gx Object Factory for GxWMTSConnections.'
    _reg_clsid_ = GUID('{E7FD59EB-F335-4EBE-AA55-734BADFFD0DD}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxWMTSConnectionFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFactory]

IGxMyHostedMapsFolder._methods_ = [
    COMMETHOD(['propget', helpstring(u'Gets the fully qualified name of the My Hosted Services Catalog Item.')], HRESULT, 'DisplayName',
              ( ['retval', 'out'], POINTER(BSTR), 'pDisplayName' )),
]
################################################################
## code template for IGxMyHostedMapsFolder implementation
##class IGxMyHostedMapsFolder_Impl(object):
##    @property
##    def DisplayName(self):
##        u'Gets the fully qualified name of the My Hosted Services Catalog Item.'
##        #return pDisplayName
##

IGxAGSDraft._methods_ = [
    COMMETHOD(['propget', helpstring(u'Name of draft Type.')], HRESULT, 'TypeName',
              ( ['retval', 'out'], POINTER(BSTR), 'pType' )),
    COMMETHOD(['propget', helpstring(u'The cooresponding file path of a draft service.')], HRESULT, 'FilePath',
              ( ['retval', 'out'], POINTER(BSTR), 'pFilePath' )),
    COMMETHOD(['propput', helpstring(u'The cooresponding file path of a draft service.')], HRESULT, 'FilePath',
              ( ['in'], BSTR, 'pFilePath' )),
]
################################################################
## code template for IGxAGSDraft implementation
##class IGxAGSDraft_Impl(object):
##    @property
##    def TypeName(self):
##        u'Name of draft Type.'
##        #return pType
##
##    def _get(self):
##        u'The cooresponding file path of a draft service.'
##        #return pFilePath
##    def _set(self, pFilePath):
##        u'The cooresponding file path of a draft service.'
##    FilePath = property(_get, _set, doc = _set.__doc__)
##

class GxWMTSLayer(CoClass):
    u'GxWMTSLayer object for the ArcCatalog.'
    _reg_clsid_ = GUID('{B4BF3D0C-5A63-43C3-A7B4-6BD029389410}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxWMTSLayer._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectEdit, IGxObjectUI, IGxObjectProperties, IGxThumbnail, IGxWMTSLayer, IGxLayerSource]

class GxFilterPGDBTables(CoClass):
    u'A filter for displaying/choosing personal geodatabase tables.'
    _reg_clsid_ = GUID('{1EB22542-E960-11D3-A682-0008C7D3AE8D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterPGDBTables._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

IGxGPToolbox._methods_ = [
    COMMETHOD(['propget', helpstring(u'The toolbox name object associated with this GxGPToolbox object.')], HRESULT, 'ToolboxName',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C031A050_82C6_4F8F_8836_5692631CFFE6_0_10_2.IGPToolboxName)), 'ToolboxName' )),
    COMMETHOD(['propputref', helpstring(u'The toolbox name object associated with this GxGPToolbox object.')], HRESULT, 'ToolboxName',
              ( ['in'], POINTER(comtypes.gen._C031A050_82C6_4F8F_8836_5692631CFFE6_0_10_2.IGPToolboxName), 'ToolboxName' )),
    COMMETHOD(['propget', helpstring(u'The toolbox object associated with this GxGPToolbox object.')], HRESULT, 'Toolbox',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C031A050_82C6_4F8F_8836_5692631CFFE6_0_10_2.IGPToolbox)), 'Toolbox' )),
]
################################################################
## code template for IGxGPToolbox implementation
##class IGxGPToolbox_Impl(object):
##    @property
##    def Toolbox(self):
##        u'The toolbox object associated with this GxGPToolbox object.'
##        #return Toolbox
##
##    def ToolboxName(self, ToolboxName):
##        u'The toolbox name object associated with this GxGPToolbox object.'
##        #return 
##

IRemoteMetadata2._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates whether publishing status dialogs are shown.')], HRESULT, 'ShowDialogs',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'show' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether publishing status dialogs are shown.')], HRESULT, 'ShowDialogs',
              ( ['in'], VARIANT_BOOL, 'show' )),
    COMMETHOD(['propget', helpstring(u'The content type of the metadata document.')], HRESULT, 'ContentType',
              ( ['retval', 'out'], POINTER(BSTR), 'ContentType' )),
    COMMETHOD(['propput', helpstring(u'The content type of the metadata document.')], HRESULT, 'ContentType',
              ( ['in'], BSTR, 'ContentType' )),
    COMMETHOD(['propget', helpstring(u'The modified date and time of the metadata document.')], HRESULT, 'ModifiedTime',
              ( ['retval', 'out'], POINTER(BSTR), 'ModifiedTime' )),
    COMMETHOD(['propput', helpstring(u'The modified date and time of the metadata document.')], HRESULT, 'ModifiedTime',
              ( ['in'], BSTR, 'ModifiedTime' )),
]
################################################################
## code template for IRemoteMetadata2 implementation
##class IRemoteMetadata2_Impl(object):
##    def _get(self):
##        u'The content type of the metadata document.'
##        #return ContentType
##    def _set(self, ContentType):
##        u'The content type of the metadata document.'
##    ContentType = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether publishing status dialogs are shown.'
##        #return show
##    def _set(self, show):
##        u'Indicates whether publishing status dialogs are shown.'
##    ShowDialogs = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The modified date and time of the metadata document.'
##        #return ModifiedTime
##    def _set(self, ModifiedTime):
##        u'The modified date and time of the metadata document.'
##    ModifiedTime = property(_get, _set, doc = _set.__doc__)
##

class IGxGPToolset(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to properties/methods of a catalog toolset object.'
    _iid_ = GUID('{330B7862-7F2E-4B29-A989-1B44A37C421D}')
    _idlflags_ = ['oleautomation']
IGxGPToolset._methods_ = [
]
################################################################
## code template for IGxGPToolset implementation
##class IGxGPToolset_Impl(object):

class GxFilterWMSConnection(CoClass):
    u'A filter for displaying/choosing WMS Server Connection objects.'
    _reg_clsid_ = GUID('{F69A88E9-DB20-4F90-BB61-A361BDEB4858}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GxFilterWMSConnection._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObjectFilter]

class NewIMSConnection(CoClass):
    u'GxObject that represents new ArcIMS Connection.'
    _reg_clsid_ = GUID('{85946D27-CF79-4088-8236-EA7B15038CA4}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
NewIMSConnection._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectUI, IGxBasicObject, IGxObjectProperties, IGxObjectWizard]

class GNSynchronizer(CoClass):
    u'Esri Geography Network Synchronizer object.'
    _reg_clsid_ = GUID('{270C5887-97AF-4C2A-9AFF-C9E893BFF73A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
GNSynchronizer._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataSynchronizer]

class IMSConnection(CoClass):
    u'GxObject that represents ArcIMS Connection.'
    _reg_clsid_ = GUID('{519DBF3E-67BD-4243-8EF5-F98DF19862A2}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{ADC7DE29-DC0B-448E-BBF6-27E4E34CF2EC}', 10, 2)
IMSConnection._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxObject, IGxObjectContainer, IIMSConnection, IIMSConnection2, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, IGxObjectEdit, IGxObjectProperties, IGxObjectUI, IGxObjectWizard, IGxRemoteConnection]

__all__ = ['IGxLocator', 'GxFilterRelationshipClasses',
           'IGxDatabase2', 'GxGeoprocessingResultFactory',
           'GxFilterRemoteMetadataContainer', 'GxFilterWCSCoverage',
           'GxFilterSpatialReferences', 'GxFilterPointFeatureClasses',
           'IMSFeatureServiceNativeType', 'IGxNewDatabase',
           'IGxCatalogAdmin', 'GxFilterFeatureClasses', 'GxFolder',
           'GPToolNativeType', 'GxFilterCoverageAnnotationClasses',
           'GxDatabaseFactory', 'IGxCatalogWorkspace',
           'IGxObjectFactoryEdit', 'GxPackageFactory',
           'RasterFormatJPGFilter', 'GxFolderConnections',
           'GxFilterStreetMapFeatureClasses', 'GxShapefileFactory',
           'esriFindDateTypePublication', 'IGxAGSImage',
           'IGxTaskServicesConnection', 'GxFilterFGDBFeatureDatasets',
           'GNValidator', 'GxCadDataset', 'esriSynchronizationOption',
           'IGxAGSMobile', 'IGxAGSLocator', 'IGxFilterDataElements',
           'IGxObjectContainer2', 'IEnumGxObject',
           'GxFilterFGDBFeatureClasses', 'GxGDSGeodatabase',
           'GxAGSConnectionFactory', 'IMSImageMap', 'IGxSelection',
           'GxAGSMap', 'IGxExcelFile', 'RasterFormatBMPFilter',
           'IMSGlobeSubServiceDescription', 'IGxItemInfo',
           'esriFindFieldTypePurpose', 'GxToolset',
           'RasterFormatFGDBFilter', 'esriFindFieldTypeProgress',
           'GxSDCDataset', 'GxFilterLayers', 'GxAGSLocator',
           'GxPrjFile', 'SearchResultsLayer', 'IGxMap', 'IGxShortcut',
           'esriFindFieldTypeStratum',
           'GxFilterMapDatasetsLayersAndResults',
           'IGxWorkspaceDatabase', 'GxRasterFileSystemFactory',
           'esriContentTypeClearinghouses', 'EnumGxObject', 'IGxFile',
           'GxWMSConnection', 'esriContentTypeNone',
           'esriFindFieldTypeTitle',
           'esriFindFieldOperatorLessThanOrEqualTo',
           'esriContentType', 'IGxAGSDraftFolder', 'GxWCSCoverage',
           'IGxToolboxesFolder', 'esriGxPackageTypeGeoprocessing',
           'GxFilterMapServers', 'GxFilterCadFeatureClasses',
           'GxFilterImageServers', 'GxSpatialReferencesFolder',
           'GxSDCFactory', 'GxStreetMapFactory', 'IGxAGSImage2',
           'IGxToolbox', 'IMSFeatureClass', 'GxPrjFileFactory',
           'IGxObjectFactoryPriority', 'IGxFeatureDefinitionPackage',
           'IRemoteMetadata2', 'ISearchResults', 'IGxAGSDraft',
           'IGxObjectEdit', 'RasterFormatBIPFilter',
           'esriFindDateOperatorDuring', 'GxShortcutFactory',
           'esriFindFieldOperatorLessThan', 'IGxRasterDataset',
           'IGxObjectFilterCollectionAdmin', 'GxFilterFileToolboxes',
           'esriFindDateOperatorPrevious',
           'GxFilterRasterCatalogDatasets', 'IGxDatabaseExtensions',
           'IGxCatalogDefaultDatabase', 'SearchResultsRoot',
           'GxFilterDimensionFeatureClasses', 'GxPre70Coverage',
           'IGxAGSWMServer', 'IGxObject', 'GxWorkspaceFolder',
           'esriFindFieldOperatorNotEqualTo', 'IGxPackage',
           'GxMyHostedMapsFolder', 'esriFindEnvelopeOperatorWithin',
           'esriFindDateOperatorEqual', 'RasterFormatENVIFilter',
           'GxFilterTables', 'esriFindDateTypeNone',
           'GxAGSFeatureServer',
           'esriContentTypeGeographicActivities',
           'GxFilterdBASEFiles', 'esriFindFieldTypeCloudCover',
           'RasterFormatPGDBFilter', 'GxObjectArray', 'IGxDatabase',
           'GxFilterTopologies', 'IGxWCSCoverage', 'IMSConnection',
           'GxFilterFeatureDatasetsAndFeatureClasses',
           'GxWMTSConnection', 'IMSFeatureService',
           'IGxDataElementHelper', 'IIMSConnection',
           'IGxObjectDeleteOptions', 'GxFilterTools',
           'GxFilterSDETables', 'GxFilterPersonalGeodatabases',
           'IAGSObjectCreationProperties', 'GxFileFactory',
           'GxFilterFeatureDatasets', 'ISearchResultsLayer',
           'GxAGSGeoDataServer', 'GxRemoteDatabaseFolder',
           'GxFilterMapDatasetsAndLayers', 'IGxWMTSConnection',
           'IQuery', 'esriContentTypeOfflineData',
           'GxFilterTablesAndFeatureClasses', 'GxFilterGlobeServers',
           'IGxCatalogEvents', 'IGxThumbnail',
           'GxFilterSDCFeatureDatasets', 'GxFilterWMS', 'GxAGSGlobe',
           'GxFilterCoverageFeatureClasses', 'GxWMSLayer',
           'IGxGeodatabase', 'GxFilterMapServersTilingScheme',
           'IGxDiskConnection2', 'GxWCSConnection',
           'GxFilterWorkspaces', 'IGxAGSGeoprocessing',
           'IGxSpatialReferencesFolder', 'GxDatabaseServerFolder',
           'IGxObjectFilterCollection', 'esriGxDeleteSingle',
           'GxFilterSDEFeatureClasses', 'IMSMetadataService',
           'GxFilterSceneDatasetsAndLayers', 'esriDoubleClickResult',
           'GxLayerFactory', 'esriFindFieldTypeSourceAgency',
           'MapNativeType', 'IGxObjectSortAlwaysOnBottom',
           'esriContentTypeApplications', 'esriDCRChooseAndDismiss',
           'esriGxPackageTypeMap', 'esriFindFieldOperatorExists',
           'IGxPasteTargetHelper', 'IGxObjectFactory',
           'GxToolboxesRoot', 'GxTaskServicesConnection',
           'GxSpatialWeightsMatrixFile', 'IGxGeoprocessingResult',
           'esriDCRShowChildren', 'GxFilterDataElements',
           'GxVpfDataset', 'GxAddWMTSConnection', 'GxCoverageFactory',
           'GxFilterImageServerDataSource', 'GxGeoprocessingResult',
           'IGxMyHostedMapsFolder', 'IGxDiskConnection',
           'GxFilterAGSConnection', 'esriContentTypeResources',
           'IGxDataGraph2', 'GxFilterDatasets',
           'GxFilterMosaicDatasets', 'IGxAGSGlobeLayer',
           'SearchResultsLayerFactory', 'GxFilterMaps',
           'IGxDatabaseExtensionCompare',
           'IMSMetadataDocumentNativeType', 'GxTaskServicesFolder',
           'GxAddAGSConnection', 'GPToolboxNativeType',
           'IGxObjectSortAlwaysOnTop', 'esriContentTypeDocuments',
           'GxFilterGeometricNetworks', 'IGxObjectWizard',
           'IGxTaskServicesFolder', 'esriDCRNothing',
           'esriFindEnvelopeOperatorOverlaps', 'IGxRemoteConnection',
           'WMTSConnectionNativeType', 'IGxGPToolset',
           'IGxRemoteDatabaseFolder', 'esriContentTypeOtherDocuments',
           'IGxWCSConnection', 'IGxDocument', 'GxDataset',
           'IMSConnectionNativeType', 'IGxDisplayName',
           'IGxObjectContainer', 'IGxAGSGlobe',
           'esriFindFieldTypeEdition', 'esriSyncAccessed',
           'GxPCCoverage', 'GxAddAGSObject', 'GxFilterInfoTables',
           'GxAGSDraft', 'GxVpfFactory', 'IGxGISServersFolder',
           'IGxAGSFeatureServer', 'GxNewDatabase',
           'IGxAGSGeoDataServer', 'GxPackage',
           'IGxRootObjectSortPriority', 'GxWMTSLayer', 'GxAGSImage',
           'GxReport', 'GxDatabaseExtensions',
           'esriFindFieldOperatorEquals', 'esriFindFieldTypePlace',
           'GxAddGDSConnection', 'esriGxPackageTypeLayer',
           'GxPCCoverageFactory', 'GxCoverageDataset',
           'IEnumGxObjectFactory', 'GxWCSConnectionFactory',
           'GxFilterContainers', 'GxCatalog',
           'esriFindDateOperatorBefore', 'IGxGPTool',
           'esriFindFieldOperatorIncludes', 'FolderNativeType',
           'IGxAGSConnection', 'esriGxDeleteYesToAll',
           'esriFindFieldTypeUserDefined', 'RasterFormatTifFilter',
           'SearchResultsIdentifyObj', 'GxMapFactory',
           'GxFilterRunningMapServers', 'IGxObjectFactoryMetadata',
           'GxStreetMapDataset', 'IGxContentViewControlCustom',
           'IGxObjectProperties', 'GxFilterRunningCachedService',
           'esriContentTypeLiveData', 'GxFilterFileFolder',
           'GxDataGraph', 'GxAGSCatalog', 'PrjFileNativeType',
           'GxFilterAnnotationFeatureClasses', 'GxFilterGlobeCaches',
           'esriFindDateOperatorAfter', 'IGxBasicObject',
           'RasterFormatBSQFilter', 'GxShapefileDataset',
           'GxFilterSDCFeatureClasses', 'esriGxPackageTypeTile',
           'esriFindDateType', 'GxFilterFGDBTables',
           'IGxObjectFactoryFileExtensions', 'GxFilterWMSConnection',
           'GxFilterShapefiles', 'esriFindFieldTypeLineage',
           'GxAddWCSConnection', 'GxFilterPGDBTables', 'IGxWMSMap',
           'esriGxPackageType', 'GxFile',
           'esriFindFieldTypeSourceScale', 'ComplexNativeType',
           'esriFindDateTypeContent', 'GxFilterPolygonFeatureClasses',
           'GxTaskServicesRootFolder', 'IGxWMSConnection',
           'IGxFolderConnections', 'GxFilterPolylineFeatureClasses',
           'RasterFormatGIFFilter', 'GxPre70CoverageFactory',
           'WCSConnectionNativeType',
           'esriFindFieldOperatorGreaterThanOrEqualTo', 'GxSelection',
           'GxDatabase', 'IGxWMTSLayer', 'IGxMetadataSupport',
           'IGxDataset', 'IGxLayerSource', 'GxFilterSDCTables',
           'esriFindFieldTypeEntity', 'GxFilterCadastralFabrics',
           'GxFilterPGDBFeatureClasses',
           'GxFilterPGDBFeatureDatasets', 'GxFilterGPServers',
           'IGxCatalogEventsDisp', 'IGxRootObjectStartupProperties',
           'GxLayer', 'GxToolboxFactory',
           'esriFindFieldOperatorGreaterThan', 'MetadataNativeType',
           'esriGxPackageTypeLocator',
           'ServiceDefinitionFileNativeType',
           'esriFindFieldTypeDataTheme', 'IGxObjectInternalName',
           'GxFeatureDefinitionPackageFactory',
           'ISearchResultsIdentifyObject', 'FileNativeType',
           'IGxCachedObjects', 'NewIMSConnection',
           'FdpFileNativeType', 'IGxFilterSearchServers',
           'esriSyncNever', 'IMetadataImport', 'IMetadataExport',
           'esriFindFieldOperatorEqualTo', 'GxToolboxExtension',
           'esriSyncCreated', 'GxFilterRoute',
           'esriContentTypeGeographicServices',
           'Pre70CoverageNativeType', 'IMSImageMapNativeType',
           'GxAGSGeometry', 'IGxObjectArray', 'LayerNativeType',
           'GxToolbox', 'GxFilterTerrains', 'GxTool', 'GxDataServer',
           'GxFilterToolboxes', 'IRasterFormatFilter',
           'GxMetadataFactory', 'IGxSelectionEvents',
           'esriContentTypeDownloadableData',
           'RasterFormatGridFilter', 'GxAGSDraftFolder',
           'GxReportFactory', 'GxMap', 'GxToolboxesFolder',
           'IGxObjectSort', 'GxFilterBasicTypes',
           'GxWMTSConnectionFactory', 'IMSGlobeServiceDescription',
           'GxFilterLasDatasets', 'IGxServiceDefinition',
           'IGxDatabaseExtension',
           'GxFilterGeoDataServersAndWorkspaces', 'esriDCRDefault',
           'IGxToolboxesRoot', 'IGxAGSObject3', 'IGxAGSObject2',
           'IGxRemoteContainer', 'GxFilterCadAnnotationClasses',
           'IGxPre70Coverage', 'esriContentTypeData',
           'IGxTaskServicesRootFolder', 'GxFilterTextFiles',
           'esriFindFieldTypeAbstract', 'esriFindFieldType',
           'GxAGSConnection', 'ShortcutNativeType', 'GxFilterFiles',
           'IGxObjectFactories', 'RasterFormatBILFilter',
           'IGxCatalog', 'IGxAddGISServerCommand', 'IGxFileSetup',
           'esriGxDeleteOption', 'GxExcelFile',
           'RasterFormatImgFilter', 'IIMSConnection2',
           'GxWMSConnectionFactory', 'IGxWorkspaceFolder',
           'GxFilterGeoDataServers', 'GNSynchronizer',
           'GxFilterGeometryServers', 'esriFindFieldTypeAttribute',
           'GxFilterDataGraphs', 'IGxAGSObject', 'IGxFileFilter',
           'GxWMSMap', 'GxSpatialWeightsMatrixFileFactory',
           'IGxLayer', 'GxServiceDefinitionFactory',
           'GxTextFileFactory', 'IMSMetadataServiceNativeType',
           'IGxAGSFolder', 'esriGxDeleteCancel', 'GxAGSFolder',
           'RasterFormatJP2Filter', 'GxGeoprocessingFileFactory',
           'GxFilterNetworkDatasets', 'esriFindFieldTypeOriginator',
           'IGxAGSGeometry', 'RasterFormatSDEFilter',
           'GxAGSGlobeLayer', 'GxFilterSDEFeatureDatasets',
           'IGxFileFilterEvents', 'IGxAGSMap', 'GxCadFactory',
           'GxFilterRemoteMetadata',
           'GxFilterVerticalCoordinateSystems',
           'GxFilterCadDrawingDatasets', 'IGxFolder',
           'esriFindFieldOperator', 'GxFilterSDCNetworkDatasets',
           'GxFilterCoverages', 'IGxPrjFile2',
           'esriFindFieldTypeGeoForm', 'IGxGISDataServers',
           'IGxGPToolbox', 'IGxPasteTarget',
           'GxFilterDatasetsAndLayers', 'GxFileFilter',
           'GxFilterGeoDatasets', 'GxIMSConnectionFactory',
           'GxFilterWMTSConnection', 'GxFilterSearchServers',
           'GxShortcut', 'IGxDefaultDatabase', 'GxAddWMSConnection',
           'GxDataGraphFactory', 'IMetadataValidator',
           'GxGeoprocessingResultNativeType',
           'esriContentTypeMapFiles', 'DataGraphNativeType',
           'GxGDBRasterExtension', 'GxServiceDefinition',
           'WorkspaceFolderNativeType', 'esriFindEnvelopeOperator',
           'IGxObjectFilter', 'GxFilterFileGeodatabases',
           'GxFeatureDefinitionPackage', 'IGxAGSCatalog',
           'IRemoteMetadata', 'GxRasterDataset', 'IGxPrjFile',
           'esriFindDateOperator', 'esriFindFieldTypeTemporal',
           'IGxDataElement', 'IGxGDSConnection', 'GxAGSWMServer',
           'GxExcelFactory', 'esriFindFieldTypeTheme',
           'RasterFormatPNGFilter', 'WMSConnectionNativeType',
           'IGxMapPageLayout', 'IGxObjectUI', 'GxDiskConnection',
           'IGxWMSLayer', 'GxMetadata', 'GxFilterTINDatasets',
           'SearchResults', 'esriSyncNotCreated', 'IGxTextFile',
           'GxFilterDefaultDatabaseWorkspaces', 'GxAGSGeoprocessing',
           'GxFilterRasterDatasets', 'IGxFolderAdmin', 'GxTextFile',
           'GxFilterGeoDatasetsAndCoordinateSystems',
           'esriFindDateTypeMetadata', 'GxGISServersFolder',
           'esriContentTypeStaticMapImages',
           'esriFindFieldTypeFullText']
from comtypes import _check_version; _check_version('501')

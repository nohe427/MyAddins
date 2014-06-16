# -*- coding: mbcs -*-
typelib_path = u'C:\\Program Files (x86)\\ArcGIS\\Desktop10.2\\com\\esriCatalogUI.olb'
_lcid = 0 # change this if required
from ctypes import *
import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0
from comtypes import GUID
from ctypes.wintypes import VARIANT_BOOL
from ctypes import HRESULT
import comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2
from comtypes import helpstring
from comtypes import COMMETHOD
from comtypes import dispid
from comtypes import CoClass
import comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2
import comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2
import comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2
import comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2
from comtypes import BSTR
import comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2
import comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2
import comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2
import comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2
import comtypes.gen._8F0541A3_D5BE_4B3F_A8D9_062D5579E19B_0_10_2
from comtypes import IUnknown
import comtypes.gen._C031A050_82C6_4F8F_8836_5692631CFFE6_0_10_2
from comtypes.automation import VARIANT
import comtypes.gen._18F2FC71_6B30_45B9_B101_037A8B868B66_0_10_2
import comtypes.gen._E418C392_C3A6_4EB2_8870_001ABAE6B5B4_0_10_2


class IFindDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the operation of the Search dialog box.'
    _iid_ = GUID('{70E62545-D396-11D3-A6F3-0008C7D3AE50}')
    _idlflags_ = ['oleautomation']
class ISearchEngine(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the operation of the search engine.'
    _iid_ = GUID('{D18306A2-9D3C-11D3-A6CB-0008C7D3AE50}')
    _idlflags_ = ['oleautomation']
IFindDialog._methods_ = [
    COMMETHOD([helpstring(u'Initializes the dialog box and opens it if indicated.')], HRESULT, 'Show',
              ( ['in'], VARIANT_BOOL, 'bShow' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the dialog box is visible.')], HRESULT, 'IsVisible',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVisible' )),
    COMMETHOD([helpstring(u'Starts executing the search defined by the query.')], HRESULT, 'DoSearch',
              ( ['in'], POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IQuery), 'pQuery' )),
    COMMETHOD([helpstring(u'Cancels an ongoing search.')], HRESULT, 'StopSearch'),
    COMMETHOD([helpstring(u"Initializes the dialog box based on a query's parameters and then opens it.")], HRESULT, 'Initialize',
              ( ['in'], POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IQuery), 'pQuery' )),
    COMMETHOD([helpstring(u'Number of available search engines.')], HRESULT, 'GetNumSearchEngines',
              ( ['retval', 'out'], POINTER(c_int), 'num' )),
    COMMETHOD([helpstring(u'The nth search engine.')], HRESULT, 'GetSearchEngine',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(ISearchEngine)), 'ppSearchEngine' )),
]
################################################################
## code template for IFindDialog implementation
##class IFindDialog_Impl(object):
##    def GetNumSearchEngines(self):
##        u'Number of available search engines.'
##        #return num
##
##    def Show(self, bShow):
##        u'Initializes the dialog box and opens it if indicated.'
##        #return 
##
##    def GetSearchEngine(self, index):
##        u'The nth search engine.'
##        #return ppSearchEngine
##
##    def StopSearch(self):
##        u'Cancels an ongoing search.'
##        #return 
##
##    @property
##    def IsVisible(self):
##        u'Indicates if the dialog box is visible.'
##        #return pVisible
##
##    def Initialize(self, pQuery):
##        u"Initializes the dialog box based on a query's parameters and then opens it."
##        #return 
##
##    def DoSearch(self, pQuery):
##        u'Starts executing the search defined by the query.'
##        #return 
##

class GeographicCoordinateSystemDialog(CoClass):
    u'Geographic Coordinate System Dialog.'
    _reg_clsid_ = GUID('{A38CB582-95CE-11D2-AD2A-00C04FA33A15}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
class IGeographicCoordinateSystemDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Geographic Coordinate System Dialog.'
    _iid_ = GUID('{A38CB580-95CE-11D2-AD2A-00C04FA33A15}')
    _idlflags_ = ['oleautomation']
GeographicCoordinateSystemDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGeographicCoordinateSystemDialog]

class GxDocumentationView(CoClass):
    u'GxView that represents the metadata view.'
    _reg_clsid_ = GUID('{B1DE27B1-D892-11D1-AA81-064342000000}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
class IGxView(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the GxView.'
    _iid_ = GUID('{B1DE27AB-D892-11D1-AA81-064342000000}')
    _idlflags_ = ['oleautomation']
class IGxDocumentationView(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that edit metadata.'
    _iid_ = GUID('{DA1862EB-95F8-11D2-AF67-080009EC734B}')
    _idlflags_ = ['oleautomation']
class IGxViewPrint(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the printing of a GxView object.'
    _iid_ = GUID('{A6164232-9140-41AD-B3F3-1DA263C80D56}')
    _idlflags_ = ['oleautomation']
GxDocumentationView._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxView, IGxDocumentationView, comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxCatalogEvents, comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxSelectionEvents, IGxViewPrint]

class MetadataExtension(CoClass):
    u'Provides access to metadata extension.'
    _reg_clsid_ = GUID('{055B2B99-F2C9-11D2-9FC1-00C04F8ED211}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
class IMetadataHelper(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u"Provides access to members that change the Catalog's metadata settings."
    _iid_ = GUID('{055B2B9A-F2C9-11D2-9FC1-00C04F8ED211}')
    _idlflags_ = ['oleautomation']
class IMetadataEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to events that occur when the state of the Documentation View changes.'
    _iid_ = GUID('{43390CCD-5906-4C57-81FD-7A2F95A7A84E}')
    _idlflags_ = ['oleautomation']
MetadataExtension._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IExtension, IMetadataHelper, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IConnectionPointContainer]
MetadataExtension._outgoing_interfaces_ = [IMetadataEvents]

class GxFilterMSDFiles(CoClass):
    u'A filter for displaying/choosing MSDFiles.'
    _reg_clsid_ = GUID('{D8030A15-980F-45DA-BFF7-AE14D1479BD0}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GxFilterMSDFiles._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxObjectFilter, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeType]

class IGxGeographicView(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the GxGeographicView.'
    _iid_ = GUID('{19BD00A9-E455-11D1-AEE4-080009EC734B}')
    _idlflags_ = ['oleautomation']
IGxGeographicView._methods_ = [
    COMMETHOD(['propget', helpstring(u'The layer object currently being displayed.')], HRESULT, 'DisplayedLayer',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer)), 'layer' )),
    COMMETHOD(['propget', helpstring(u'The display object that is used to draw the layer.')], HRESULT, 'MapDisplay',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IScreenDisplay)), 'screenDisplay' )),
    COMMETHOD(['propget', helpstring(u'The map object that is used to draw the layer.')], HRESULT, 'Map',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMap)), 'Map' )),
]
################################################################
## code template for IGxGeographicView implementation
##class IGxGeographicView_Impl(object):
##    @property
##    def Map(self):
##        u'The map object that is used to draw the layer.'
##        #return Map
##
##    @property
##    def MapDisplay(self):
##        u'The display object that is used to draw the layer.'
##        #return screenDisplay
##
##    @property
##    def DisplayedLayer(self):
##        u'The layer object currently being displayed.'
##        #return layer
##

class IGxDocumentationViewWindow(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of IGxDocumentationViewWindow interface.'
    _iid_ = GUID('{5626C4A7-9000-49D3-B0E4-83B8CD3F15EC}')
    _idlflags_ = ['oleautomation']
IGxDocumentationViewWindow._methods_ = [
    COMMETHOD(['propget', helpstring(u'HWND of the child window.')], HRESULT, 'hWnd',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'hWnd' )),
    COMMETHOD([helpstring(u'The selected object is changed.')], HRESULT, 'OnObjectChanged',
              ( ['in'], POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxObject), 'pGxObject' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'pMetadata' )),
    COMMETHOD([helpstring(u'The metadata of the selected object is changed.')], HRESULT, 'OnMetadataChanged',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata), 'pMetadata' )),
    COMMETHOD([helpstring(u'The metadata of the selected object is changed.')], HRESULT, 'OnMetadataChanged2',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'pMetadata' )),
    COMMETHOD([helpstring(u'The selected ItemInfo is changed.')], HRESULT, 'OnItemInfoChanged',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IItemInfo), 'pItemInfo' )),
    COMMETHOD([helpstring(u'Close the embeded window.')], HRESULT, 'Close'),
    COMMETHOD([helpstring(u'Print selected content.')], HRESULT, 'Print'),
    COMMETHOD([helpstring(u'Force UI to repaint.')], HRESULT, 'Invalidate'),
]
################################################################
## code template for IGxDocumentationViewWindow implementation
##class IGxDocumentationViewWindow_Impl(object):
##    def Invalidate(self):
##        u'Force UI to repaint.'
##        #return 
##
##    @property
##    def hWnd(self):
##        u'HWND of the child window.'
##        #return hWnd
##
##    def Print(self):
##        u'Print selected content.'
##        #return 
##
##    def OnItemInfoChanged(self, pItemInfo):
##        u'The selected ItemInfo is changed.'
##        #return 
##
##    def OnObjectChanged(self, pGxObject, pMetadata):
##        u'The selected object is changed.'
##        #return 
##
##    def Close(self):
##        u'Close the embeded window.'
##        #return 
##
##    def OnMetadataChanged2(self, pMetadata):
##        u'The metadata of the selected object is changed.'
##        #return 
##
##    def OnMetadataChanged(self, pMetadata):
##        u'The metadata of the selected object is changed.'
##        #return 
##

IMetadataEvents._methods_ = [
    COMMETHOD([helpstring(u'Occurs when the current stylesheet changes.')], HRESULT, 'OnStylesheetChanged',
              ( ['in'], BSTR, 'Stylesheet' )),
]
################################################################
## code template for IMetadataEvents implementation
##class IMetadataEvents_Impl(object):
##    def OnStylesheetChanged(self, Stylesheet):
##        u'Occurs when the current stylesheet changes.'
##        #return 
##

class IGxItemIndexer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to functions of GxIndexer coclass.  Also see the GPItemIndexer coclass.'
    _iid_ = GUID('{76994811-3B0C-4CD0-977E-2E599FC98690}')
    _idlflags_ = ['oleautomation']
IGxItemIndexer._methods_ = [
    COMMETHOD(['propget', helpstring(u'Total indexed items count.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'pCount' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the ancestor of this GxObject has been registered to be indexed.')], HRESULT, 'IsAncestorRegistered',
              ( ['in'], POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxObject), 'pGxObject' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pRegistered' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the current object has been indexed.')], HRESULT, 'HasBeenIndexed',
              ( ['in'], POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxObject), 'pGxObject' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pIndexed' )),
    COMMETHOD([helpstring(u'Update the index.')], HRESULT, 'UpdateIndex',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IItemInfo), 'pItemInfo' )),
    COMMETHOD([helpstring(u'Index the current object.')], HRESULT, 'IndexObject',
              ( ['in'], POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxObject), 'pObject' )),
    COMMETHOD([helpstring(u'Index the children of the current object.')], HRESULT, 'IndexChildren',
              ( ['in'], POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxObject), 'pObject' )),
    COMMETHOD([helpstring(u"Update current object's thumbnail in index.")], HRESULT, 'UpdateThumbnailInIndex',
              ( ['in'], POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxObject), 'pObject' )),
]
################################################################
## code template for IGxItemIndexer implementation
##class IGxItemIndexer_Impl(object):
##    @property
##    def Count(self):
##        u'Total indexed items count.'
##        #return pCount
##
##    @property
##    def HasBeenIndexed(self, pGxObject):
##        u'Indicates whether the current object has been indexed.'
##        #return pIndexed
##
##    def UpdateThumbnailInIndex(self, pObject):
##        u"Update current object's thumbnail in index."
##        #return 
##
##    def IndexObject(self, pObject):
##        u'Index the current object.'
##        #return 
##
##    def IndexChildren(self, pObject):
##        u'Index the children of the current object.'
##        #return 
##
##    def UpdateIndex(self, pItemInfo):
##        u'Update the index.'
##        #return 
##
##    @property
##    def IsAncestorRegistered(self, pGxObject):
##        u'Indicates whether the ancestor of this GxObject has been registered to be indexed.'
##        #return pRegistered
##

class AGSDiscoveryArcGISOnlinePage(CoClass):
    u'Esri AGS Service ArcGISOnline property page.'
    _reg_clsid_ = GUID('{B6F23369-B484-480E-9FF7-D5477B15AA7D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSDiscoveryArcGISOnlinePage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class GeneralDatabaseServerPropertyPage(CoClass):
    u'The general geodatabase property page.'
    _reg_clsid_ = GUID('{096A8D7E-5CF9-40D0-BA0F-864799E40515}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GeneralDatabaseServerPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class GxContentsViewPage(CoClass):
    u'Esri GxContentsView property page.'
    _reg_clsid_ = GUID('{D342626B-F9DA-11D3-A68D-0008C7D3AE8D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GxContentsViewPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class IAGSObjectAdminDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Server Object Admin Dialog.'
    _iid_ = GUID('{CAC7E0E9-BDE5-4A18-A18F-92B6B0BF86F4}')
    _idlflags_ = ['oleautomation']
IAGSObjectAdminDialog._methods_ = [
    COMMETHOD([helpstring(u'Displays the dialog to create a new server object.')], HRESULT, 'DoModalCreateServerObject',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hParent' ),
              ( ['in'], POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IAGSServerConnectionName), 'pServerConnName' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IAGSObjectCreationProperties)), 'ppProps' )),
]
################################################################
## code template for IAGSObjectAdminDialog implementation
##class IAGSObjectAdminDialog_Impl(object):
##    def DoModalCreateServerObject(self, hParent, pServerConnName):
##        u'Displays the dialog to create a new server object.'
##        #return ppProps
##

class IGxTreeView(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the GxTreeView.'
    _iid_ = GUID('{2EF87699-EC64-11D1-AA96-00C04FA375E3}')
    _idlflags_ = ['oleautomation']
IGxTreeView._methods_ = [
    COMMETHOD([helpstring(u'Instructs the tree view to expand the current selection.')], HRESULT, 'ExpandSelection',
              ( ['in'], POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxSelection), 'Selection' )),
    COMMETHOD([helpstring(u'Starts a rename operation on the current selection.')], HRESULT, 'BeginRename'),
    COMMETHOD([helpstring(u'Ensures that the current selection is visible, scrolling/expanding if necessary.')], HRESULT, 'EnsureVisible',
              ( ['in'], POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxObject), 'object' )),
]
################################################################
## code template for IGxTreeView implementation
##class IGxTreeView_Impl(object):
##    def BeginRename(self):
##        u'Starts a rename operation on the current selection.'
##        #return 
##
##    def ExpandSelection(self, Selection):
##        u'Instructs the tree view to expand the current selection.'
##        #return 
##
##    def EnsureVisible(self, object):
##        u'Ensures that the current selection is visible, scrolling/expanding if necessary.'
##        #return 
##

class IGxTableView(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Indicator interface that identifies the GX Table preview.'
    _iid_ = GUID('{8ED63615-DA21-4807-A4CE-97EFCFB8FDDB}')
    _idlflags_ = ['oleautomation']
IGxTableView._methods_ = [
]
################################################################
## code template for IGxTableView implementation
##class IGxTableView_Impl(object):

class IEnumGxView(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the EnumGxView.'
    _iid_ = GUID('{D342626C-F9DA-11D3-A68D-0008C7D3AE8D}')
    _idlflags_ = ['oleautomation']
IEnumGxView._methods_ = [
    COMMETHOD([helpstring(u'The next GxView.')], HRESULT, 'Next',
              ( ['retval', 'out'], POINTER(POINTER(IGxView)), 'ppView' )),
    COMMETHOD([helpstring(u'Resets the enumerator.')], HRESULT, 'Reset'),
]
################################################################
## code template for IEnumGxView implementation
##class IEnumGxView_Impl(object):
##    def Reset(self):
##        u'Resets the enumerator.'
##        #return 
##
##    def Next(self):
##        u'The next GxView.'
##        #return ppView
##

class IGxTableView2(IGxTableView):
    _case_insensitive_ = True
    u'Provides access to members that control the IGxTableView.'
    _iid_ = GUID('{82A28CF6-5F38-40D4-80A8-CFC644A2EC3A}')
    _idlflags_ = ['oleautomation']
IGxTableView2._methods_ = [
    COMMETHOD([helpstring(u'The object for table view.')], HRESULT, 'SetObject',
              ( ['in'], POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxObject), 'pObject' )),
    COMMETHOD([helpstring(u'The RasterCatalogFilter for table view.')], HRESULT, 'FilterRasterCatalog',
              ( ['in'], VARIANT_BOOL, 'filter' )),
]
################################################################
## code template for IGxTableView2 implementation
##class IGxTableView2_Impl(object):
##    def FilterRasterCatalog(self, filter):
##        u'The RasterCatalogFilter for table view.'
##        #return 
##
##    def SetObject(self, pObject):
##        u'The object for table view.'
##        #return 
##

class IGxViewContainer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the GxViewContainer.'
    _iid_ = GUID('{E7E3DA73-F904-11D3-A68C-0008C7D3AE8D}')
    _idlflags_ = ['oleautomation']
IGxViewContainer._methods_ = [
    COMMETHOD([helpstring(u'Finds a view by CLSID. If recursive is true, it will return views in a container view.')], HRESULT, 'FindView',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID), 'pUID' ),
              ( ['in', 'optional'], VARIANT_BOOL, 'bRecursive', False ),
              ( ['retval', 'out'], POINTER(POINTER(IGxView)), 'ppView' )),
    COMMETHOD(['propget', helpstring(u'All Gxviews in the application.')], HRESULT, 'Views',
              ( ['retval', 'out'], POINTER(POINTER(IEnumGxView)), 'ppGxViews' )),
]
################################################################
## code template for IGxViewContainer implementation
##class IGxViewContainer_Impl(object):
##    def FindView(self, pUID, bRecursive):
##        u'Finds a view by CLSID. If recursive is true, it will return views in a container view.'
##        #return ppView
##
##    @property
##    def Views(self):
##        u'All Gxviews in the application.'
##        #return ppGxViews
##

class IGxContentsViewColumn(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the GxContentsViewColumn.'
    _iid_ = GUID('{22E48EC9-F92D-11D3-A68D-0008C7D3AE8D}')
    _idlflags_ = ['oleautomation']
IGxContentsViewColumn._methods_ = [
    COMMETHOD(['propget', helpstring(u'The caption of the column.')], HRESULT, 'Caption',
              ( ['retval', 'out'], POINTER(BSTR), 'pCaption' )),
    COMMETHOD(['propput', helpstring(u'The caption of the column.')], HRESULT, 'Caption',
              ( ['in'], BSTR, 'pCaption' )),
    COMMETHOD(['propget', helpstring(u'The property name.')], HRESULT, 'PropertyName',
              ( ['retval', 'out'], POINTER(BSTR), 'pPropName' )),
    COMMETHOD(['propput', helpstring(u'The property name.')], HRESULT, 'PropertyName',
              ( ['in'], BSTR, 'pPropName' )),
    COMMETHOD(['propget', helpstring(u'The width of the column.')], HRESULT, 'Width',
              ( ['retval', 'out'], POINTER(c_int), 'pWidth' )),
    COMMETHOD(['propput', helpstring(u'The width of the column.')], HRESULT, 'Width',
              ( ['in'], c_int, 'pWidth' )),
    COMMETHOD(['propget', helpstring(u'Indicates if visible.')], HRESULT, 'Visible',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVisible' )),
    COMMETHOD(['propput', helpstring(u'Indicates if visible.')], HRESULT, 'Visible',
              ( ['in'], VARIANT_BOOL, 'pVisible' )),
    COMMETHOD(['propget', helpstring(u'Indicates if intrinsic.')], HRESULT, 'Intrinsic',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pIntrinsic' )),
    COMMETHOD(['propput', helpstring(u'Indicates if intrinsic.')], HRESULT, 'Intrinsic',
              ( ['in'], VARIANT_BOOL, 'pIntrinsic' )),
]
################################################################
## code template for IGxContentsViewColumn implementation
##class IGxContentsViewColumn_Impl(object):
##    def _get(self):
##        u'The caption of the column.'
##        #return pCaption
##    def _set(self, pCaption):
##        u'The caption of the column.'
##    Caption = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The property name.'
##        #return pPropName
##    def _set(self, pPropName):
##        u'The property name.'
##    PropertyName = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if visible.'
##        #return pVisible
##    def _set(self, pVisible):
##        u'Indicates if visible.'
##    Visible = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if intrinsic.'
##        #return pIntrinsic
##    def _set(self, pIntrinsic):
##        u'Indicates if intrinsic.'
##    Intrinsic = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The width of the column.'
##        #return pWidth
##    def _set(self, pWidth):
##        u'The width of the column.'
##    Width = property(_get, _set, doc = _set.__doc__)
##

class AGSDiscoveryImageTilingSchemePage(CoClass):
    u'Esri AGS Image Service Cache Tiling Scheme property page.'
    _reg_clsid_ = GUID('{0B906F72-DED9-45B8-B4D4-2C66BDF93E17}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSDiscoveryImageTilingSchemePage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class GxWCSSOEPage(CoClass):
    u'WCS SOE properties page.'
    _reg_clsid_ = GUID('{301C07DB-E5FC-4020-8CD8-6FDCF1D86D13}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
class IAGSSOEParameterPage(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control ArcGIS server object extension parameter pages.'
    _iid_ = GUID('{2CC34141-016D-4EC0-913E-4D803EE43B8F}')
    _idlflags_ = ['oleautomation']
class IAGSSOEParameterPage2(IAGSSOEParameterPage):
    _case_insensitive_ = True
    u'Provides access to members that control ArcGIS server object extension parameter pages.'
    _iid_ = GUID('{A81C1560-C5ED-43BC-B921-B328A9C652E2}')
    _idlflags_ = ['oleautomation']
GxWCSSOEPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, IAGSSOEParameterPage, IAGSSOEParameterPage2]

class FeatureDatasetDefDialog(CoClass):
    u'Dialog to create a new Feature Dataset.'
    _reg_clsid_ = GUID('{B4F57D5E-001F-4760-92AD-71F9D8C6626D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
class IFeatureDatasetDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the dialog that creates a new feature dataset.'
    _iid_ = GUID('{6EDC31DD-E3AD-11D2-99C1-0000F80372B4}')
    _idlflags_ = ['oleautomation']
FeatureDatasetDefDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IFeatureDatasetDialog]

class CreateManageRoleMenuItem(CoClass):
    u'Context menu command to create and manage roles.'
    _reg_clsid_ = GUID('{39B594AC-4065-4363-8777-4940F46E7F64}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
CreateManageRoleMenuItem._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.ICommand]

class GxWPSSOEPage(CoClass):
    u'WPS SOE properties page.'
    _reg_clsid_ = GUID('{BD84C8F9-DEBC-4C64-BBDE-ED38481828D8}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GxWPSSOEPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, IAGSSOEParameterPage, IAGSSOEParameterPage2]

class EnumGxView(CoClass):
    u'Provides access to a set of GxView object.'
    _reg_clsid_ = GUID('{0ED03264-CFED-4BCE-9F7F-30830A020394}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
EnumGxView._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IEnumGxView]

class IAttributesEditContext(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to attributes edit context.'
    _iid_ = GUID('{F54484AF-D0BF-4407-8A52-342212299D0F}')
    _idlflags_ = ['oleautomation']
class IEditEvaluatorContext(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the edit evaluator context.'
    _iid_ = GUID('{01EFC9B9-2277-4F01-9B24-1AF85B678BC2}')
    _idlflags_ = ['oleautomation']
class INetworkAttributeConfiguration(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the network attribute configuration.'
    _iid_ = GUID('{2B089C6B-7A8E-4410-9594-1EF8771CCA68}')
    _idlflags_ = ['oleautomation']
IAttributesEditContext._methods_ = [
    COMMETHOD(['propget', helpstring(u'The network dataset container.')], HRESULT, 'Container',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetContainer2)), 'Container' )),
    COMMETHOD(['propget', helpstring(u'The network dataset data element.')], HRESULT, 'DENetwork',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDENetworkDataset)), 'dataElement' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the attribute edit context is read only.')], HRESULT, 'ReadOnly',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ReadOnly' )),
    COMMETHOD(['propget', helpstring(u'The number of edit evaluator contexts.')], HRESULT, 'EditEvaluatorContextCount',
              ( ['in'], VARIANT_BOOL, 'defaultMode' ),
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'The edit evaluator context.')], HRESULT, 'EditEvaluatorContext',
              ( ['in'], VARIANT_BOOL, 'defaultMode' ),
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IEditEvaluatorContext)), 'context' )),
    COMMETHOD(['propget', helpstring(u'The network attribute templates.')], HRESULT, 'AttributeTemplates',
              ( ['retval', 'out'], POINTER(POINTER(INetworkAttributeConfiguration)), 'templates' )),
]
################################################################
## code template for IAttributesEditContext implementation
##class IAttributesEditContext_Impl(object):
##    @property
##    def EditEvaluatorContext(self, defaultMode, index):
##        u'The edit evaluator context.'
##        #return context
##
##    @property
##    def Container(self):
##        u'The network dataset container.'
##        #return Container
##
##    @property
##    def EditEvaluatorContextCount(self, defaultMode):
##        u'The number of edit evaluator contexts.'
##        #return Count
##
##    @property
##    def ReadOnly(self):
##        u'Indicates whether the attribute edit context is read only.'
##        #return ReadOnly
##
##    @property
##    def DENetwork(self):
##        u'The network dataset data element.'
##        #return dataElement
##
##    @property
##    def AttributeTemplates(self):
##        u'The network attribute templates.'
##        #return templates
##

class AGSDiscoveryProcessPage(CoClass):
    u'Esri AGS Service Processing property page.'
    _reg_clsid_ = GUID('{EDD45734-A36F-4C31-AEB7-77B9D368DD86}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSDiscoveryProcessPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class IGxApplication(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Gx Application object.'
    _iid_ = GUID('{D1BF6A01-7A1C-11D0-B77D-00805F7CED21}')
    _idlflags_ = ['oleautomation']
IGxView._methods_ = [
    COMMETHOD(['propget', helpstring(u'The name of the view.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'The class ID of the view.')], HRESULT, 'ClassID',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID)), 'ClassID' )),
    COMMETHOD(['propget', helpstring(u"The view's window handle.")], HRESULT, 'hWnd',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'window' )),
    COMMETHOD(['propget', helpstring(u"The class ID of the view's default toolbar.  Not currently used.")], HRESULT, 'DefaultToolbarCLSID',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID)), 'toolbarCLSID' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the view supports tools.')], HRESULT, 'SupportsTools',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'SupportsTools' )),
    COMMETHOD([helpstring(u'Indicates if the view can display the given object.')], HRESULT, 'Applies',
              ( ['in'], POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxObject), 'Selection' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Applies' )),
    COMMETHOD([helpstring(u'Activates the view.')], HRESULT, 'Activate',
              ( ['in'], POINTER(IGxApplication), 'Application' ),
              ( ['in'], POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxCatalog), 'Catalog' )),
    COMMETHOD([helpstring(u'Deactivates the view.')], HRESULT, 'Deactivate'),
    COMMETHOD([helpstring(u'Refreshes the view.')], HRESULT, 'Refresh'),
    COMMETHOD([helpstring(u'Informs the view that a system setting has changed.')], HRESULT, 'SystemSettingChanged',
              ( ['in'], c_int, 'flag' ),
              ( ['in'], BSTR, 'section' )),
]
################################################################
## code template for IGxView implementation
##class IGxView_Impl(object):
##    @property
##    def ClassID(self):
##        u'The class ID of the view.'
##        #return ClassID
##
##    @property
##    def DefaultToolbarCLSID(self):
##        u"The class ID of the view's default toolbar.  Not currently used."
##        #return toolbarCLSID
##
##    def Activate(self, Application, Catalog):
##        u'Activates the view.'
##        #return 
##
##    @property
##    def Name(self):
##        u'The name of the view.'
##        #return Name
##
##    @property
##    def SupportsTools(self):
##        u'Indicates if the view supports tools.'
##        #return SupportsTools
##
##    @property
##    def hWnd(self):
##        u"The view's window handle."
##        #return window
##
##    def Refresh(self):
##        u'Refreshes the view.'
##        #return 
##
##    def Deactivate(self):
##        u'Deactivates the view.'
##        #return 
##
##    def SystemSettingChanged(self, flag, section):
##        u'Informs the view that a system setting has changed.'
##        #return 
##
##    def Applies(self, Selection):
##        u'Indicates if the view can display the given object.'
##        #return Applies
##

IGxApplication._methods_ = [
    COMMETHOD(['propget', helpstring(u'The current catalog.')], HRESULT, 'Catalog',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxCatalog)), 'Catalog' )),
    COMMETHOD(['propget', helpstring(u'The current view.')], HRESULT, 'View',
              ( ['retval', 'out'], POINTER(POINTER(IGxView)), 'View' )),
    COMMETHOD(['propget', helpstring(u"The current view's class ID.")], HRESULT, 'ViewClassID',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID)), 'ViewClassID' )),
    COMMETHOD(['propput', helpstring(u"The current view's class ID.")], HRESULT, 'ViewClassID',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID), 'ViewClassID' )),
    COMMETHOD(['propget', helpstring(u'The tree view.')], HRESULT, 'TreeView',
              ( ['retval', 'out'], POINTER(POINTER(IGxTreeView)), 'TreeView' )),
    COMMETHOD(['propget', helpstring(u'The selection of application.')], HRESULT, 'Selection',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxSelection)), 'Selection' )),
    COMMETHOD(['propget', helpstring(u'The first selected object, or the location if no objects are selected.')], HRESULT, 'SelectedObject',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxObject)), 'SelectedObject' )),
    COMMETHOD(['propput', helpstring(u"The location to the specified path.  If the path isn't yet part of the catalog, it is added as a folder connection.")], HRESULT, 'Location',
              ( ['in'], BSTR, 'rhs' )),
    COMMETHOD([helpstring(u'Refreshes the catalog tree starting at the specified path.  If startingPath is 0 or the empty string, the entire catalog is refreshed.')], HRESULT, 'Refresh',
              ( ['in'], BSTR, 'startingPath' )),
    COMMETHOD([helpstring(u'Displays a context menu for the current selection.')], HRESULT, 'ShowContextMenu',
              ( ['in'], c_int, 'x' ),
              ( ['in'], c_int, 'y' )),
    COMMETHOD([helpstring(u'Expands the current selection.')], HRESULT, 'ExpandSelection'),
    COMMETHOD(['propget', helpstring(u'Indicates if the current selection can be deleted.')], HRESULT, 'CanDeleteSelection',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pEnabled' )),
    COMMETHOD([helpstring(u'Deletes the current selection.')], HRESULT, 'DeleteSelection'),
    COMMETHOD(['propget', helpstring(u'Indicates if the current selection can be renamed.')], HRESULT, 'CanRenameSelection',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pEnabled' )),
    COMMETHOD([helpstring(u'Renames the current selection.')], HRESULT, 'RenameSelection'),
    COMMETHOD(['propget', helpstring(u'The default area of interest for the application.')], HRESULT, 'AreaOfInterest',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'aoi' )),
    COMMETHOD(['propput', helpstring(u'The default area of interest for the application.')], HRESULT, 'AreaOfInterest',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'aoi' )),
]
################################################################
## code template for IGxApplication implementation
##class IGxApplication_Impl(object):
##    def ShowContextMenu(self, x, y):
##        u'Displays a context menu for the current selection.'
##        #return 
##
##    @property
##    def Selection(self):
##        u'The selection of application.'
##        #return Selection
##
##    @property
##    def CanRenameSelection(self):
##        u'Indicates if the current selection can be renamed.'
##        #return pEnabled
##
##    def Refresh(self, startingPath):
##        u'Refreshes the catalog tree starting at the specified path.  If startingPath is 0 or the empty string, the entire catalog is refreshed.'
##        #return 
##
##    @property
##    def CanDeleteSelection(self):
##        u'Indicates if the current selection can be deleted.'
##        #return pEnabled
##
##    @property
##    def Catalog(self):
##        u'The current catalog.'
##        #return Catalog
##
##    def RenameSelection(self):
##        u'Renames the current selection.'
##        #return 
##
##    def _get(self):
##        u'The default area of interest for the application.'
##        #return aoi
##    def _set(self, aoi):
##        u'The default area of interest for the application.'
##    AreaOfInterest = property(_get, _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u"The location to the specified path.  If the path isn't yet part of the catalog, it is added as a folder connection."
##    Location = property(fset = _set, doc = _set.__doc__)
##
##    def _get(self):
##        u"The current view's class ID."
##        #return ViewClassID
##    def _set(self, ViewClassID):
##        u"The current view's class ID."
##    ViewClassID = property(_get, _set, doc = _set.__doc__)
##
##    def DeleteSelection(self):
##        u'Deletes the current selection.'
##        #return 
##
##    @property
##    def TreeView(self):
##        u'The tree view.'
##        #return TreeView
##
##    @property
##    def SelectedObject(self):
##        u'The first selected object, or the location if no objects are selected.'
##        #return SelectedObject
##
##    def ExpandSelection(self):
##        u'Expands the current selection.'
##        #return 
##
##    @property
##    def View(self):
##        u'The current view.'
##        #return View
##


# values for enumeration 'esriContentsViewStyle'
esriCVSLargeIcons = 0
esriCVSList = 1
esriCVSDetails = 2
esriCVSThumbnails = 3
esriContentsViewStyle = c_int # enum
class GxContentsViewColumn(CoClass):
    u'Provides access to contents view column.'
    _reg_clsid_ = GUID('{22E48ECB-F92D-11D3-A68D-0008C7D3AE8D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GxContentsViewColumn._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxContentsViewColumn, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone]

class Library(object):
    u'Esri CatalogUI Object Library 10.2'
    name = u'esriCatalogUI'
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)

class GxGeographicView(CoClass):
    u'GxView that represents the geographic view.'
    _reg_clsid_ = GUID('{B1DE27B0-D892-11D1-AA81-064342000000}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
class IGxGeographicView2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to more members that control the GxGeographicView.'
    _iid_ = GUID('{20F44EEB-F618-11D3-A68B-0008C7D3AE8D}')
    _idlflags_ = ['oleautomation']
GxGeographicView._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxView, IGxGeographicView, IGxGeographicView2, comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxSelectionEvents, comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxCatalogEvents, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.ITransformEvents]

class IRepairMosaicDatasetDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods that control the dialog for repairing a mosaic dataset.'
    _iid_ = GUID('{2FF6AF43-4334-4D3E-9798-D0E3A8585275}')
    _idlflags_ = ['oleautomation']
IRepairMosaicDatasetDialog._methods_ = [
    COMMETHOD([helpstring(u'Open dialog in modal.')], HRESULT, 'DoModal',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hParent' )),
    COMMETHOD(['propputref', helpstring(u'The Mosaic Dataset.')], HRESULT, 'MosaicDataset',
              ( ['in'], POINTER(comtypes.gen._8F0541A3_D5BE_4B3F_A8D9_062D5579E19B_0_10_2.IMosaicDataset), 'ppMosaicDataset' )),
    COMMETHOD(['propget', helpstring(u'The Mosaic Dataset.')], HRESULT, 'MosaicDataset',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._8F0541A3_D5BE_4B3F_A8D9_062D5579E19B_0_10_2.IMosaicDataset)), 'ppMosaicDataset' )),
    COMMETHOD(['propputref', helpstring(u'The Selection Set.')], HRESULT, 'SelectionSet',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ISelectionSet), 'ppSelectionSet' )),
    COMMETHOD(['propget', helpstring(u'The Selection Set.')], HRESULT, 'SelectionSet',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ISelectionSet)), 'ppSelectionSet' )),
]
################################################################
## code template for IRepairMosaicDatasetDialog implementation
##class IRepairMosaicDatasetDialog_Impl(object):
##    def DoModal(self, hParent):
##        u'Open dialog in modal.'
##        #return 
##
##    @property
##    def MosaicDataset(self, ppMosaicDataset):
##        u'The Mosaic Dataset.'
##        #return 
##
##    @property
##    def SelectionSet(self, ppSelectionSet):
##        u'The Selection Set.'
##        #return 
##

class GxTableView(CoClass):
    u'GxView that represents the table contents view.'
    _reg_clsid_ = GUID('{9C34344D-99DC-11D2-AF6A-080009EC734B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GxTableView._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxView, comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxSelectionEvents, comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxCatalogEvents, IGxTableView2, IGxViewPrint]

class AGSDiscoveryGeoDataParametersPage(CoClass):
    u'Esri AGS GeoData Service Parameters Property Page.'
    _reg_clsid_ = GUID('{B442DE39-9293-42E4-9919-B1BA7FFB5215}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSDiscoveryGeoDataParametersPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class GxRasterCatalogSubPropertyView(CoClass):
    u'The property sub-view of RasterCatalog.'
    _reg_clsid_ = GUID('{643F3BA9-0352-4F05-9393-1F403E6CBB29}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
class IGxRasterCatalogSubView(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods that control RasterCatalog sub view.'
    _iid_ = GUID('{0EDA5F3D-FE01-40D1-9018-1B2E4A01FD2E}')
    _idlflags_ = ['oleautomation']
GxRasterCatalogSubPropertyView._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxView, IGxRasterCatalogSubView]

class QueryTableDialog(CoClass):
    u'Dialog to create query layer.'
    _reg_clsid_ = GUID('{A26D3415-734C-4986-9FF7-D5B3A17399FC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
class IQueryTableDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to member that display Query Table dialog.'
    _iid_ = GUID('{4FF00DC6-47CC-489D-9D0A-100083C27C9D}')
    _idlflags_ = ['oleautomation']
QueryTableDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IQueryTableDialog]

class AGSDiscoveryGeocodeParametersPage(CoClass):
    u'Esri AGS Geocode Service Parameters Property Page.'
    _reg_clsid_ = GUID('{359AEFBD-CFE3-4F56-8DE7-E2959C2ECBBD}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSDiscoveryGeocodeParametersPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class AGSDiscoveryImageParametersPage(CoClass):
    u'Esri AGS Image Service Parameters Property Page.'
    _reg_clsid_ = GUID('{ED16CAB5-EEE2-4515-B3EA-88E31EC9A604}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSDiscoveryImageParametersPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class IGxPreview(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the GxPreview.'
    _iid_ = GUID('{DA1862EC-95F8-11D2-AF67-080009EC734B}')
    _idlflags_ = ['oleautomation']
IGxPreview._methods_ = [
    COMMETHOD(['propget', helpstring(u'The current view.')], HRESULT, 'View',
              ( ['retval', 'out'], POINTER(POINTER(IGxView)), 'currentView' )),
    COMMETHOD(['propget', helpstring(u'The class ID of the current view.')], HRESULT, 'ViewClassID',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID)), 'ViewClassID' )),
    COMMETHOD(['propput', helpstring(u'The class ID of the current view.')], HRESULT, 'ViewClassID',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID), 'ViewClassID' )),
    COMMETHOD(['propget', helpstring(u'A list of the class IDs for the views that are supported given the current selection.')], HRESULT, 'SupportedViewClassIDs',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISet)), 'viewClassIDs' )),
]
################################################################
## code template for IGxPreview implementation
##class IGxPreview_Impl(object):
##    def _get(self):
##        u'The class ID of the current view.'
##        #return ViewClassID
##    def _set(self, ViewClassID):
##        u'The class ID of the current view.'
##    ViewClassID = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def SupportedViewClassIDs(self):
##        u'A list of the class IDs for the views that are supported given the current selection.'
##        #return viewClassIDs
##
##    @property
##    def View(self):
##        u'The current view.'
##        #return currentView
##

class GxHomeFolderOptionsPage(CoClass):
    u'GX Home Folder Options Property Page.'
    _reg_clsid_ = GUID('{CD84E143-732C-491D-8B18-6AB567FE4FA1}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GxHomeFolderOptionsPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class AGSMapParameterPage(CoClass):
    u'Esri AGS Map Parameters property page.'
    _reg_clsid_ = GUID('{6CF43581-586C-4DA6-ACA3-3A24766D69DA}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
class IAGSParameterPage(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control ArcGIS server parameter pages.'
    _iid_ = GUID('{674787AC-FEF9-4932-B03C-BCBB1576A7EF}')
    _idlflags_ = ['oleautomation']
AGSMapParameterPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, IAGSParameterPage]

class ISpatialReferenceDialog2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Spatial Reference Dialog.'
    _iid_ = GUID('{B088F162-CDD1-11D3-A097-00C04F6BDF0E}')
    _idlflags_ = ['oleautomation']
ISpatialReferenceDialog2._methods_ = [
    COMMETHOD([helpstring(u'Prompts the user to define a new spatial reference.')], HRESULT, 'DoModalCreate',
              ( ['in'], VARIANT_BOOL, 'hasXY' ),
              ( ['in'], VARIANT_BOOL, 'hasZ' ),
              ( ['in'], VARIANT_BOOL, 'hasM' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hParent' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference)), 'SpatialReference' )),
    COMMETHOD([helpstring(u'Displays/edits the properties of the given spatial reference.')], HRESULT, 'DoModalEdit',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference), 'inputSpatialReference' ),
              ( ['in'], VARIANT_BOOL, 'hasXY' ),
              ( ['in'], VARIANT_BOOL, 'hasZ' ),
              ( ['in'], VARIANT_BOOL, 'hasM' ),
              ( ['in'], VARIANT_BOOL, 'coordPageReadOnly' ),
              ( ['in'], VARIANT_BOOL, 'xyDomainPageReadOnly' ),
              ( ['in'], VARIANT_BOOL, 'mDomainPageReadOnly' ),
              ( ['in'], VARIANT_BOOL, 'zDomainPageReadOnly' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hParent' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference)), 'outputSpatialReference' )),
]
################################################################
## code template for ISpatialReferenceDialog2 implementation
##class ISpatialReferenceDialog2_Impl(object):
##    def DoModalEdit(self, inputSpatialReference, hasXY, hasZ, hasM, coordPageReadOnly, xyDomainPageReadOnly, mDomainPageReadOnly, zDomainPageReadOnly, hParent):
##        u'Displays/edits the properties of the given spatial reference.'
##        #return outputSpatialReference
##
##    def DoModalCreate(self, hasXY, hasZ, hasM, hParent):
##        u'Prompts the user to define a new spatial reference.'
##        #return SpatialReference
##


# values for enumeration 'esriSpatialReferenceXYFilter'
esriShowOnlyGeographic = 1
esriShowOnlyProjected = 2
esriShowBoth = 3
esriSpatialReferenceXYFilter = c_int # enum
class GeneralRelationshipClassPropertyPage(CoClass):
    u'General Relationship Class Property Page.'
    _reg_clsid_ = GUID('{38B5EAFB-DE47-11D2-9F54-00C04F6BC626}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GeneralRelationshipClassPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class FeatureExtentPage(CoClass):
    u'Esri feature class extent page.'
    _reg_clsid_ = GUID('{3B2BE6CA-7140-4C79-AE24-B312BFE29F98}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
FeatureExtentPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class IRelationshipClassDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Relationship Class Dialog.'
    _iid_ = GUID('{2A4E2F8C-DAF1-11D2-9F52-00C04F6BC626}')
    _idlflags_ = ['oleautomation']
IRelationshipClassDialog._methods_ = [
    COMMETHOD([helpstring(u'Prompts the user to define a new relationship class.')], HRESULT, 'DoModalCreate',
              ( ['in'], POINTER(IUnknown), 'pUnk' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hParent' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRelationshipClass)), 'relationshipClass' )),
]
################################################################
## code template for IRelationshipClassDialog implementation
##class IRelationshipClassDialog_Impl(object):
##    def DoModalCreate(self, pUnk, hParent):
##        u'Prompts the user to define a new relationship class.'
##        #return relationshipClass
##

class INetworkTrafficConfiguration(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the network traffic configuration.'
    _iid_ = GUID('{251ABD7F-250C-42C1-A147-A9B84ED35BDA}')
    _idlflags_ = ['oleautomation']
class INetworkTrafficConfiguration2(INetworkTrafficConfiguration):
    _case_insensitive_ = True
    u'Provides access to the network traffic configuration.'
    _iid_ = GUID('{E89EFA12-134F-4FC1-B3EE-3278A4768FCC}')
    _idlflags_ = ['oleautomation']
INetworkTrafficConfiguration._methods_ = [
    COMMETHOD(['propget', helpstring(u'The candidate base names for the travel time factor field names in the profiles table.')], HRESULT, 'TimeSliceBaseNames',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'BaseNames' )),
    COMMETHOD(['propget', helpstring(u'The default start time of the first time slice.')], HRESULT, 'DefaultFirstTimeSliceStartTime',
              ( ['retval', 'out'], POINTER(c_double), 'StartTime' )),
    COMMETHOD(['propget', helpstring(u'The default finish time of the last time slice.')], HRESULT, 'DefaultLastTimeSliceFinishTime',
              ( ['retval', 'out'], POINTER(c_double), 'finishTime' )),
    COMMETHOD(['propget', helpstring(u'The candidate base names for the base travel time field name in the Streets-Profiles table.')], HRESULT, 'TrafficBaseTravelTimeBaseNames',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'BaseNames' )),
    COMMETHOD(['propget', helpstring(u'The candidate time unit names for the time unit of the base travel time field in the Streets-Profiles table.')], HRESULT, 'TrafficTimeUnitNames',
              ( ['in'], comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriNetworkAttributeUnits, 'timeUnit' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'timeUnitNames' )),
    COMMETHOD(['propget', helpstring(u'The candidate base names forming part of each Streets-Profiles table daily profile ID field name.')], HRESULT, 'JoinTableProfileIDFieldBaseNames',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'BaseNames' )),
    COMMETHOD(['propget', helpstring(u'The weekday names for each day (in groups of 7) used for part of the Streets-Profiles table daily profile ID field names.')], HRESULT, 'DayOfWeekNameGroups',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IArray)), 'DayOfWeekNameGroups' )),
    COMMETHOD(['propget', helpstring(u'The preferred weekday fallback template travel time attribute names used by the network edge traffic evaluator.')], HRESULT, 'WeekdayFallbackTemplateAttributeNames',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'WeekdayFallbackTemplateAttributeNames' )),
    COMMETHOD(['propget', helpstring(u'The preferred weekend fallback template travel time attribute names used by the network edge traffic evaluator.')], HRESULT, 'WeekendFallbackTemplateAttributeNames',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'WeekdayFallbackTemplateAttributeNames' )),
]
################################################################
## code template for INetworkTrafficConfiguration implementation
##class INetworkTrafficConfiguration_Impl(object):
##    @property
##    def WeekendFallbackTemplateAttributeNames(self):
##        u'The preferred weekend fallback template travel time attribute names used by the network edge traffic evaluator.'
##        #return WeekdayFallbackTemplateAttributeNames
##
##    @property
##    def DayOfWeekNameGroups(self):
##        u'The weekday names for each day (in groups of 7) used for part of the Streets-Profiles table daily profile ID field names.'
##        #return DayOfWeekNameGroups
##
##    @property
##    def DefaultLastTimeSliceFinishTime(self):
##        u'The default finish time of the last time slice.'
##        #return finishTime
##
##    @property
##    def JoinTableProfileIDFieldBaseNames(self):
##        u'The candidate base names forming part of each Streets-Profiles table daily profile ID field name.'
##        #return BaseNames
##
##    @property
##    def TimeSliceBaseNames(self):
##        u'The candidate base names for the travel time factor field names in the profiles table.'
##        #return BaseNames
##
##    @property
##    def DefaultFirstTimeSliceStartTime(self):
##        u'The default start time of the first time slice.'
##        #return StartTime
##
##    @property
##    def TrafficTimeUnitNames(self, timeUnit):
##        u'The candidate time unit names for the time unit of the base travel time field in the Streets-Profiles table.'
##        #return timeUnitNames
##
##    @property
##    def TrafficBaseTravelTimeBaseNames(self):
##        u'The candidate base names for the base travel time field name in the Streets-Profiles table.'
##        #return BaseNames
##
##    @property
##    def WeekdayFallbackTemplateAttributeNames(self):
##        u'The preferred weekday fallback template travel time attribute names used by the network edge traffic evaluator.'
##        #return WeekdayFallbackTemplateAttributeNames
##

INetworkTrafficConfiguration2._methods_ = [
    COMMETHOD(['propget', helpstring(u'The candidate base names for the speed factor field names in the profiles table.')], HRESULT, 'TimeSliceBaseSpeedFactorNames',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'BaseNames' )),
    COMMETHOD(['propget', helpstring(u'The candidate full names in the specified unit for the base field name in the Streets-Profiles table.')], HRESULT, 'TrafficBaseFullNames',
              ( ['in'], comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriNetworkAttributeUnits, 'unit' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'FullNames' )),
    COMMETHOD(['propget', helpstring(u'The candidate base names for the base speed field name in the Streets-Profiles table.')], HRESULT, 'TrafficBaseSpeedBaseNames',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'BaseNames' )),
    COMMETHOD(['propget', helpstring(u'The candidate speed unit names for the speed unit of the base speed field in the Streets-Profiles table.')], HRESULT, 'TrafficSpeedUnitNames',
              ( ['in'], comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriNetworkAttributeUnits, 'timeUnit' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'timeUnitNames' )),
    COMMETHOD(['propget', helpstring(u'The candidate TMC field names in the Streets-TMC table.')], HRESULT, 'DynamicTrafficTMCFullNames',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'FullNames' )),
]
################################################################
## code template for INetworkTrafficConfiguration2 implementation
##class INetworkTrafficConfiguration2_Impl(object):
##    @property
##    def DynamicTrafficTMCFullNames(self):
##        u'The candidate TMC field names in the Streets-TMC table.'
##        #return FullNames
##
##    @property
##    def TimeSliceBaseSpeedFactorNames(self):
##        u'The candidate base names for the speed factor field names in the profiles table.'
##        #return BaseNames
##
##    @property
##    def TrafficBaseSpeedBaseNames(self):
##        u'The candidate base names for the base speed field name in the Streets-Profiles table.'
##        #return BaseNames
##
##    @property
##    def TrafficBaseFullNames(self, unit):
##        u'The candidate full names in the specified unit for the base field name in the Streets-Profiles table.'
##        #return FullNames
##
##    @property
##    def TrafficSpeedUnitNames(self, timeUnit):
##        u'The candidate speed unit names for the speed unit of the base speed field in the Streets-Profiles table.'
##        #return timeUnitNames
##

class TableDefEditorTrackingPage(CoClass):
    u'Esri feature class Editor Tracking page.'
    _reg_clsid_ = GUID('{5D330FC1-55E5-4636-A3E1-F768B4B69D21}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
TableDefEditorTrackingPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class WorkspaceEditorTrackingPropertyPage(CoClass):
    u'The Workspace editor tracking property page.'
    _reg_clsid_ = GUID('{5E444088-EFF6-47B9-8FA6-3A088C413441}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
WorkspaceEditorTrackingPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class CoordSysDetailsPage(CoClass):
    u'Esri Coordinate System Details Page.'
    _reg_clsid_ = GUID('{61182707-6C5D-4C07-BB26-C786FDD6BE1E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
class ICoordSysDetailsPage(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Coordinate System Details Page.'
    _iid_ = GUID('{2A426347-8AA3-4846-920D-9F1F32C09B6C}')
    _idlflags_ = ['oleautomation']
CoordSysDetailsPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, ICoordSysDetailsPage]

class TableDefCoordPage(CoClass):
    u'Esri feature class coordinate system page.'
    _reg_clsid_ = GUID('{B78BAF9A-ABA9-4003-A645-989944C3C5B3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
TableDefCoordPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class XYCoordSysPage(CoClass):
    u'Esri XY Coordinate System Page.'
    _reg_clsid_ = GUID('{F86DB1EC-E376-49D9-8A61-E4A984B33620}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
XYCoordSysPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class FeatureDatasetDialog(CoClass):
    u'Dialog to create a new Feature Dataset.'
    _reg_clsid_ = GUID('{6EDC31DE-E3AD-11D2-99C1-0000F80372B4}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
FeatureDatasetDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IFeatureDatasetDialog]

class IGxObjectEnumerator(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods that control the object enumerator.'
    _iid_ = GUID('{9C204F5E-59B2-475A-A52B-37B0F750F0F6}')
    _idlflags_ = ['oleautomation']
IGxObjectEnumerator._methods_ = [
    COMMETHOD(['propget', helpstring(u'The current GxObject in the enumerator.')], HRESULT, 'Current',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxObject)), 'ppSelected' )),
    COMMETHOD(['propget', helpstring(u'The current position of the GxObject in the enumerator.')], HRESULT, 'CurrentPos',
              ( ['retval', 'out'], POINTER(c_int), 'pIdx' )),
    COMMETHOD(['propput', helpstring(u'The current position of the GxObject in the enumerator.')], HRESULT, 'CurrentPos',
              ( ['in'], c_int, 'pIdx' )),
    COMMETHOD(['propget', helpstring(u'The number of GxObjects in the enumerator.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'pCount' )),
]
################################################################
## code template for IGxObjectEnumerator implementation
##class IGxObjectEnumerator_Impl(object):
##    @property
##    def Current(self):
##        u'The current GxObject in the enumerator.'
##        #return ppSelected
##
##    def _get(self):
##        u'The current position of the GxObject in the enumerator.'
##        #return pIdx
##    def _set(self, pIdx):
##        u'The current position of the GxObject in the enumerator.'
##    CurrentPos = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Count(self):
##        u'The number of GxObjects in the enumerator.'
##        #return pCount
##

class ResolutionPage(CoClass):
    u'Esri coordinate system resolution page.'
    _reg_clsid_ = GUID('{45B40860-6E1C-430C-B6DE-7B326D4A02FD}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
ResolutionPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class FeatDSSpaRefPage(CoClass):
    u'Feature Dataset Spatial Reference Property Page.'
    _reg_clsid_ = GUID('{E813F832-2B3E-11D3-9C25-00C04F5AA6DF}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
FeatDSSpaRefPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class INetworkAttributeConfiguration2(INetworkAttributeConfiguration):
    _case_insensitive_ = True
    u'Provides access to the network attribute configuration.'
    _iid_ = GUID('{8834A016-8E30-4101-8D1B-46DF8DDF0AA9}')
    _idlflags_ = ['oleautomation']
INetworkAttributeConfiguration._methods_ = [
    COMMETHOD(['propget', helpstring(u'The directional prefixes along the digitized direction.')], HRESULT, 'AlongPrefixes',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'prefixes' )),
    COMMETHOD(['propget', helpstring(u'The directional prefixes against the digitized direction.')], HRESULT, 'AgainstPrefixes',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'prefixes' )),
    COMMETHOD(['propget', helpstring(u'The number of template attributes in the network configuration.')], HRESULT, 'TemplateAttributeCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'The ith template attribute.')], HRESULT, 'TemplateAttribute',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IEvaluatedNetworkAttribute)), 'attribute' )),
    COMMETHOD([helpstring(u'Find the index of a template attribute by name.')], HRESULT, 'FindTemplateAttributeByName',
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(c_int), 'index' )),
    COMMETHOD([helpstring(u'Find the index of a matching template attribute.')], HRESULT, 'FindMatchingTemplateAttribute',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INetworkAttribute), 'attribute' ),
              ( ['retval', 'out'], POINTER(c_int), 'index' )),
    COMMETHOD([helpstring(u'Query for the best evaluator match if any.')], HRESULT, 'QueryEvaluator',
              ( ['in'], c_int, 'index' ),
              ( ['in'], POINTER(IEditEvaluatorContext), 'context' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INetworkEvaluator), 'evaluator' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'matched' )),
]
################################################################
## code template for INetworkAttributeConfiguration implementation
##class INetworkAttributeConfiguration_Impl(object):
##    @property
##    def AgainstPrefixes(self):
##        u'The directional prefixes against the digitized direction.'
##        #return prefixes
##
##    def FindTemplateAttributeByName(self, Name):
##        u'Find the index of a template attribute by name.'
##        #return index
##
##    @property
##    def TemplateAttributeCount(self):
##        u'The number of template attributes in the network configuration.'
##        #return Count
##
##    @property
##    def AlongPrefixes(self):
##        u'The directional prefixes along the digitized direction.'
##        #return prefixes
##
##    @property
##    def TemplateAttribute(self, index):
##        u'The ith template attribute.'
##        #return attribute
##
##    def QueryEvaluator(self, index, context, evaluator):
##        u'Query for the best evaluator match if any.'
##        #return matched
##
##    def FindMatchingTemplateAttribute(self, attribute):
##        u'Find the index of a matching template attribute.'
##        #return index
##

INetworkAttributeConfiguration2._methods_ = [
    COMMETHOD(['propget', helpstring(u'The directional suffixes along the digitized direction.')], HRESULT, 'AlongSuffixes',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'suffixes' )),
    COMMETHOD(['propget', helpstring(u'The directional suffixes against the digitized direction.')], HRESULT, 'AgainstSuffixes',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'suffixes' )),
    COMMETHOD(['propget', helpstring(u'The preferred candidate time zone attribute names.')], HRESULT, 'TimeZoneTemplateAttributeNames',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'TimeZoneTemplateAttributeNames' )),
    COMMETHOD(['propget', helpstring(u'The default hierarchy range max values for the specified attribute name.')], HRESULT, 'HierachyRangeMaxValuesByName',
              ( ['in'], BSTR, 'attributeName' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray)), 'ppHierachyRangeMaxValues' )),
]
################################################################
## code template for INetworkAttributeConfiguration2 implementation
##class INetworkAttributeConfiguration2_Impl(object):
##    @property
##    def TimeZoneTemplateAttributeNames(self):
##        u'The preferred candidate time zone attribute names.'
##        #return TimeZoneTemplateAttributeNames
##
##    @property
##    def AlongSuffixes(self):
##        u'The directional suffixes along the digitized direction.'
##        #return suffixes
##
##    @property
##    def HierachyRangeMaxValuesByName(self, attributeName):
##        u'The default hierarchy range max values for the specified attribute name.'
##        #return ppHierachyRangeMaxValues
##
##    @property
##    def AgainstSuffixes(self):
##        u'The directional suffixes against the digitized direction.'
##        #return suffixes
##

class GxItemInfoHelper(CoClass):
    u'Provides access to members of GxItemInfoHelper.'
    _reg_clsid_ = GUID('{B6F2F15F-F98D-43ED-922D-AB8E9BF93ADA}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
class IGxItemInfoHelper(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to helper functions for item info.'
    _iid_ = GUID('{A33CA783-6EC8-4868-9B81-1B5DE34A8FB9}')
    _idlflags_ = ['oleautomation']
GxItemInfoHelper._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxItemInfoHelper]

IFeatureDatasetDialog._methods_ = [
    COMMETHOD([helpstring(u'Prompts the user to define a new feature dataset.')], HRESULT, 'DoModalCreate',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureWorkspace), 'pFeatWS' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentWindow' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureDataset)), 'ppFeatDS' )),
]
################################################################
## code template for IFeatureDatasetDialog implementation
##class IFeatureDatasetDialog_Impl(object):
##    def DoModalCreate(self, pFeatWS, parentWindow):
##        u'Prompts the user to define a new feature dataset.'
##        #return ppFeatDS
##

class IVerticalCoordinateSystemDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Vertical Coordinate System Dialog.'
    _iid_ = GUID('{55415584-F24F-4CCB-A754-77FC3D827361}')
    _idlflags_ = ['oleautomation']
IVerticalCoordinateSystemDialog._methods_ = [
    COMMETHOD([helpstring(u'Prompts the user to define a new vertical coordinate system.')], HRESULT, 'DoModalCreate',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hParent' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IVerticalCoordinateSystem)), 'pcs' )),
]
################################################################
## code template for IVerticalCoordinateSystemDialog implementation
##class IVerticalCoordinateSystemDialog_Impl(object):
##    def DoModalCreate(self, hParent):
##        u'Prompts the user to define a new vertical coordinate system.'
##        #return pcs
##

class GxSqlDatabaseAdminMenu(CoClass):
    u'Sql database administration context menu.'
    _reg_clsid_ = GUID('{80A5A67A-8D1D-4C6E-BED0-D3180CEED8CE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GxSqlDatabaseAdminMenu._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IShortcutMenu]

class FeatDSNamePage(CoClass):
    u'Esri Feature Dataset Name Page.'
    _reg_clsid_ = GUID('{65D96C66-8F7B-4B79-8358-1779A79EB080}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
FeatDSNamePage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class EnableGeodatabaseMenuItem(CoClass):
    u'The context menu command to enable Geodatabase.'
    _reg_clsid_ = GUID('{C4BA9107-3D9F-424E-9C48-8D91D32B4F4E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
EnableGeodatabaseMenuItem._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.ICommand]

class GxPreview(CoClass):
    u'GxView that represents the preview.'
    _reg_clsid_ = GUID('{B1DE27AF-D892-11D1-AA81-064342000000}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GxPreview._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxView, IGxPreview, comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxSelectionEvents, IGxViewContainer]

class GxObjectVisibilityPage(CoClass):
    u'GX Object Visibility Property Page.'
    _reg_clsid_ = GUID('{C26879A1-28BD-11D3-9C1B-00C04F5AA6DF}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GxObjectVisibilityPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class AddUserMenuItem(CoClass):
    u'Context menu command to create database users.'
    _reg_clsid_ = GUID('{FB6C3E18-748A-430F-8F01-F8EF4A98C287}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AddUserMenuItem._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.ICommand]

class GxPackagePropPage(CoClass):
    u'Provides access to GxPackage property page.'
    _reg_clsid_ = GUID('{FEE49CE5-4CDD-4762-9E80-EEEE74E1C22F}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GxPackagePropPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

IAGSSOEParameterPage._methods_ = [
    COMMETHOD(['propget', helpstring(u'Server object type.')], HRESULT, 'ServerObjectType',
              ( ['retval', 'out'], POINTER(BSTR), 'serverObjType' )),
    COMMETHOD(['propget', helpstring(u'Server object extension type.')], HRESULT, 'ServerObjectExtensionType',
              ( ['retval', 'out'], POINTER(BSTR), 'serverObjExtType' )),
    COMMETHOD(['propget', helpstring(u'The extension properties.')], HRESULT, 'ExtensionProperties',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'extProps' )),
    COMMETHOD(['propputref', helpstring(u'The extension properties.')], HRESULT, 'ExtensionProperties',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'extProps' )),
    COMMETHOD(['propget', helpstring(u'The server object properties.')], HRESULT, 'ServerObjectProperties',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'extProps' )),
    COMMETHOD(['propputref', helpstring(u'The server object properties.')], HRESULT, 'ServerObjectProperties',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'extProps' )),
]
################################################################
## code template for IAGSSOEParameterPage implementation
##class IAGSSOEParameterPage_Impl(object):
##    @property
##    def ServerObjectType(self):
##        u'Server object type.'
##        #return serverObjType
##
##    def ServerObjectProperties(self, extProps):
##        u'The server object properties.'
##        #return 
##
##    @property
##    def ServerObjectExtensionType(self):
##        u'Server object extension type.'
##        #return serverObjExtType
##
##    def ExtensionProperties(self, extProps):
##        u'The extension properties.'
##        #return 
##

class GxAddOleDBConnectionCommand(CoClass):
    u'Add OleDB Connection command.'
    _reg_clsid_ = GUID('{D2514FC7-075A-4545-8419-25906757EBB9}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GxAddOleDBConnectionCommand._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.ICommand]

class FeatureClassRepresentationsPage(CoClass):
    u'Esri feature class representations page.'
    _reg_clsid_ = GUID('{94D9C1E3-51B9-4D14-8BD2-45F8F35511C6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
FeatureClassRepresentationsPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class RelationshipClassDialog(CoClass):
    u'Provides access to the relationship class dialog.'
    _reg_clsid_ = GUID('{2A4E2F8D-DAF1-11D2-9F52-00C04F6BC626}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
RelationshipClassDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRelationshipClassDialog]

class GxFileFilterDefinitionPage(CoClass):
    u'GX File Filter Definition Property Page.'
    _reg_clsid_ = GUID('{2D6E3E08-E6C4-11D2-99C1-0000F80372B4}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GxFileFilterDefinitionPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

IGxGeographicView2._methods_ = [
    COMMETHOD(['propget', helpstring(u'The layer object currently being displayed.')], HRESULT, 'DisplayedLayer',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer)), 'layer' )),
    COMMETHOD(['propget', helpstring(u'The display object that is used to draw the layer.')], HRESULT, 'MapDisplay',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IScreenDisplay)), 'screenDisplay' )),
    COMMETHOD(['propget', helpstring(u'The map object that is used to draw the layer.')], HRESULT, 'Map',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMap)), 'Map' )),
    COMMETHOD(['propget', helpstring(u'The active view object(either map or page layout).')], HRESULT, 'ActiveView',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IActiveView)), 'ppActiveView' )),
]
################################################################
## code template for IGxGeographicView2 implementation
##class IGxGeographicView2_Impl(object):
##    @property
##    def Map(self):
##        u'The map object that is used to draw the layer.'
##        #return Map
##
##    @property
##    def ActiveView(self):
##        u'The active view object(either map or page layout).'
##        #return ppActiveView
##
##    @property
##    def MapDisplay(self):
##        u'The display object that is used to draw the layer.'
##        #return screenDisplay
##
##    @property
##    def DisplayedLayer(self):
##        u'The layer object currently being displayed.'
##        #return layer
##

class IDataAdder(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the data adder.'
    _iid_ = GUID('{2FFA788F-808A-49FB-AD5F-451A2F77B281}')
    _idlflags_ = ['oleautomation']
IDataAdder._methods_ = [
    COMMETHOD([helpstring(u'Adds data to the current running application.')], HRESULT, 'AddDataToCurrentApplication',
              ( ['in'], POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IEnumGxObject), 'Datasets' )),
    COMMETHOD([helpstring(u'Adds a dataset to the current running application.')], HRESULT, 'AddDatasetToCurrentApplication',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName), 'datasetName' )),
]
################################################################
## code template for IDataAdder implementation
##class IDataAdder_Impl(object):
##    def AddDatasetToCurrentApplication(self, datasetName):
##        u'Adds a dataset to the current running application.'
##        #return 
##
##    def AddDataToCurrentApplication(self, Datasets):
##        u'Adds data to the current running application.'
##        #return 
##

class NetworkDirectionsLandmarksPage(CoClass):
    u'Esri network directions landmarks page.'
    _reg_clsid_ = GUID('{31D8E13B-E072-4750-8C67-FCC686A3D39A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
NetworkDirectionsLandmarksPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class VerticalCoordSysPropPage(CoClass):
    u'Vertical Coordinate System Property Page.'
    _reg_clsid_ = GUID('{A849A059-D6BB-49A2-B38A-8EB1A475E70D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
VerticalCoordSysPropPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class FeatureServerObjectPropPage(CoClass):
    u'Esri ArcGIS Server Feature Service property page.'
    _reg_clsid_ = GUID('{F57464AD-E531-451B-94B7-77DBE9224E6C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
FeatureServerObjectPropPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class IDescriptionWindow(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of Item Descrition Window.'
    _iid_ = GUID('{65F86C2E-40E4-4135-8EBC-364A0EF7E9AE}')
    _idlflags_ = ['oleautomation']
IDescriptionWindow._methods_ = [
    COMMETHOD(['propputref', helpstring(u'Provides the window with a reference to the application.')], HRESULT, 'Application',
              ( ['in'], POINTER(comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IApplication), 'rhs' )),
    COMMETHOD(['propputref', helpstring(u'Pass the editing target object to item description window.')], HRESULT, 'TargetObject',
              ( ['in'], POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxObject), 'ppGxObject' )),
    COMMETHOD(['propget', helpstring(u'Pass the editing target object to item description window.')], HRESULT, 'TargetObject',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxObject)), 'ppGxObject' )),
    COMMETHOD(['propput', helpstring(u'Pass the editing target path to item description window.')], HRESULT, 'TargetPath',
              ( ['in'], BSTR, 'path' )),
    COMMETHOD(['propget', helpstring(u'Pass the editing target path to item description window.')], HRESULT, 'TargetPath',
              ( ['retval', 'out'], POINTER(BSTR), 'path' )),
    COMMETHOD(['propputref', helpstring(u'Pass the target ItemInfo to item description window.')], HRESULT, 'TargetItemInfo',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IItemInfo), 'ppItemInfo' )),
    COMMETHOD(['propget', helpstring(u'Pass the target ItemInfo to item description window.')], HRESULT, 'TargetItemInfo',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IItemInfo)), 'ppItemInfo' )),
    COMMETHOD([helpstring(u'Indicates whether the Item Description Window is already being displayed for the selected ItemInfo.')], HRESULT, 'FindViaItemInfo',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IItemInfo), 'pItemInfo' ),
              ( ['retval', 'out'], POINTER(POINTER(IDescriptionWindow)), 'ppDescWindow' )),
    COMMETHOD([helpstring(u'Indicates whether the Item Description Window is already being displayed for the selected path.')], HRESULT, 'FindViaPath',
              ( ['in'], BSTR, 'path' ),
              ( ['retval', 'out'], POINTER(POINTER(IDescriptionWindow)), 'ppDescWindow' )),
    COMMETHOD([helpstring(u'Indicates whether the Item Description Window is already being displayed for the selected GxObject.')], HRESULT, 'FindViaObject',
              ( ['in'], POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxObject), 'pGxObject' ),
              ( ['retval', 'out'], POINTER(POINTER(IDescriptionWindow)), 'ppDescWindow' )),
    COMMETHOD(['propget', helpstring(u'HWND of the Item Description Window.')], HRESULT, 'hWnd',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'hWnd' )),
    COMMETHOD([helpstring(u'Show tem Description Window of select object.')], HRESULT, 'Show',
              ( ['in'], VARIANT_BOOL, 'rePosition' )),
    COMMETHOD([helpstring(u'Refresh the Item Description Window.')], HRESULT, 'Refresh'),
    COMMETHOD(['propget', helpstring(u'The documentation view in item description window.')], HRESULT, 'DocumentationView',
              ( ['retval', 'out'], POINTER(POINTER(IGxDocumentationView)), 'ppGxDocView' )),
]
################################################################
## code template for IDescriptionWindow implementation
##class IDescriptionWindow_Impl(object):
##    def FindViaObject(self, pGxObject):
##        u'Indicates whether the Item Description Window is already being displayed for the selected GxObject.'
##        #return ppDescWindow
##
##    def FindViaItemInfo(self, pItemInfo):
##        u'Indicates whether the Item Description Window is already being displayed for the selected ItemInfo.'
##        #return ppDescWindow
##
##    def Show(self, rePosition):
##        u'Show tem Description Window of select object.'
##        #return 
##
##    def Refresh(self):
##        u'Refresh the Item Description Window.'
##        #return 
##
##    @property
##    def TargetItemInfo(self, ppItemInfo):
##        u'Pass the target ItemInfo to item description window.'
##        #return 
##
##    def Application(self, rhs):
##        u'Provides the window with a reference to the application.'
##        #return 
##
##    def FindViaPath(self, path):
##        u'Indicates whether the Item Description Window is already being displayed for the selected path.'
##        #return ppDescWindow
##
##    @property
##    def hWnd(self):
##        u'HWND of the Item Description Window.'
##        #return hWnd
##
##    @property
##    def DocumentationView(self):
##        u'The documentation view in item description window.'
##        #return ppGxDocView
##
##    def _get(self):
##        u'Pass the editing target path to item description window.'
##        #return path
##    def _set(self, path):
##        u'Pass the editing target path to item description window.'
##    TargetPath = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def TargetObject(self, ppGxObject):
##        u'Pass the editing target object to item description window.'
##        #return 
##

class IDocumentDatasets(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the document datasets.'
    _iid_ = GUID('{7BFCE4B1-1228-11D4-9FEC-00C04F6BC78E}')
    _idlflags_ = ['oleautomation']
IDocumentDatasets._methods_ = [
    COMMETHOD(['propget', helpstring(u'The datasets in the document.')], HRESULT, 'Datasets',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IEnumDataset)), 'Datasets' )),
]
################################################################
## code template for IDocumentDatasets implementation
##class IDocumentDatasets_Impl(object):
##    @property
##    def Datasets(self):
##        u'The datasets in the document.'
##        #return Datasets
##

class InfoItemsPage(CoClass):
    u'INFO Table Items Property Page.'
    _reg_clsid_ = GUID('{16D5E96A-33D4-4290-B28D-3C9DDC93C84F}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
InfoItemsPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class GeoDBAdminPropertyPage(CoClass):
    u'The Geodatabase Administration property page.'
    _reg_clsid_ = GUID('{451900E3-B8BD-4E06-A959-365343230DDB}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GeoDBAdminPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class IGxApplicationEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to events fired by the ArcCatalog application.'
    _iid_ = GUID('{979FEA13-D5AE-11D2-9F28-00C04F6BC69E}')
    _idlflags_ = ['oleautomation']
IGxApplicationEvents._methods_ = [
    COMMETHOD([helpstring(u'Called when the clipboard contents have changed.')], HRESULT, 'OnClipboardChanged'),
    COMMETHOD([helpstring(u'Called when the view changes.')], HRESULT, 'OnViewChanged'),
]
################################################################
## code template for IGxApplicationEvents implementation
##class IGxApplicationEvents_Impl(object):
##    def OnClipboardChanged(self):
##        u'Called when the clipboard contents have changed.'
##        #return 
##
##    def OnViewChanged(self):
##        u'Called when the view changes.'
##        #return 
##

class GeoDataServerObjectPropPage(CoClass):
    u'Esri ArcGIS Server GeoData Server Object property page.'
    _reg_clsid_ = GUID('{2F82F2AD-3501-462A-97CF-105D20305ED4}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GeoDataServerObjectPropPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class DataAdder(CoClass):
    u'Provides access to the data adder utility class.'
    _reg_clsid_ = GUID('{57F18814-AF09-43A2-8DFB-0BB8337C7FF5}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
DataAdder._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDataAdder]

class GeometryServerObjectPropPage(CoClass):
    u'Esri ArcGIS Server Geometry Server Object property page.'
    _reg_clsid_ = GUID('{CA503F96-7932-4A44-B3CC-623F78D2A212}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GeometryServerObjectPropPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class InfoTableGeneralPage(CoClass):
    u'INFO Table General Property Page.'
    _reg_clsid_ = GUID('{B9CB3D70-4C2B-4992-B230-6362E633F642}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
InfoTableGeneralPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class Pre70CoveragePropertyPage(CoClass):
    u'Pre 7.0 Coverage Property Page.'
    _reg_clsid_ = GUID('{C65A2BB6-32ED-11D3-9F33-00C04F79927C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
Pre70CoveragePropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class GlobeServerObjectPropPage(CoClass):
    u'Esri ArcGIS Server Globe Server Object property page.'
    _reg_clsid_ = GUID('{AA404CFF-3FBE-4361-87F9-F86E4EC29BA4}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GlobeServerObjectPropPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class AGSDiscoveryPoolingPage(CoClass):
    u'Esri AGS Service Pooling property page.'
    _reg_clsid_ = GUID('{2D03568E-19AC-4D31-BB1C-F9272F95B1EF}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSDiscoveryPoolingPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

IGxItemInfoHelper._methods_ = [
    COMMETHOD(['propget', helpstring(u'Item info of the selected object.')], HRESULT, 'ItemInfo',
              ( ['in'], POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxObject), 'pGxObject' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IItemInfo)), 'ppItemInfo' )),
    COMMETHOD([helpstring(u'Update the item info of the specified object.')], HRESULT, 'UpdateItemInfo',
              ( ['in'], POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxObject), 'pObject' ),
              ( ['in', 'out'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IItemInfo), 'pItemInfo' )),
]
################################################################
## code template for IGxItemInfoHelper implementation
##class IGxItemInfoHelper_Impl(object):
##    def UpdateItemInfo(self, pObject):
##        u'Update the item info of the specified object.'
##        #return pItemInfo
##
##    @property
##    def ItemInfo(self, pGxObject):
##        u'Item info of the selected object.'
##        #return ppItemInfo
##

class AGSDiscoveryAdvancedCacheSettingsPage(CoClass):
    u'Esri AGS Service Advanced Cache Settings property page.'
    _reg_clsid_ = GUID('{E9720218-923E-43F6-9108-1DAA146B3334}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSDiscoveryAdvancedCacheSettingsPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class NetworkConstantEvaluatorEditor(CoClass):
    u'The constant evaluator editor.'
    _reg_clsid_ = GUID('{38D87FAA-D4E3-484C-BCD7-BF71ABFAE5ED}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
class IEvaluatorEditor(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to an evaluator editor.'
    _iid_ = GUID('{23B61A91-0F9E-46A7-B3C5-FE5484F323B8}')
    _idlflags_ = ['oleautomation']
NetworkConstantEvaluatorEditor._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IEvaluatorEditor]

class AGSDiscoveryCapabilityGeneralPage(CoClass):
    u'Esri AGS Service Capability General property page.'
    _reg_clsid_ = GUID('{610280B0-0219-4317-B9DC-E57CF8392D16}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSDiscoveryCapabilityGeneralPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class NetworkFieldEvaluatorEditor(CoClass):
    u'The field evaluator editor.'
    _reg_clsid_ = GUID('{8F201C9F-0C2B-4200-9CAD-E111D7B3F4AF}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
NetworkFieldEvaluatorEditor._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IEvaluatorEditor]

class GxShapefileIndexPage(CoClass):
    u'Shapefile Index Property Page.'
    _reg_clsid_ = GUID('{65EBBA7E-7816-11D3-A662-0008C7D3AE8D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GxShapefileIndexPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class NetworkScriptEvaluatorEditor(CoClass):
    u'The script evaluator editor.'
    _reg_clsid_ = GUID('{8402D5EB-4003-4052-AEC0-C9D945880CD7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
NetworkScriptEvaluatorEditor._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IEvaluatorEditor]

class CreateRasterCatalogWizard(CoClass):
    u'A Dialog Wizard to help creating a raster catalog.'
    _reg_clsid_ = GUID('{9FBEA74E-9BAC-4C3E-9588-24DA5EEB327C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
class ICreateRasterCatalogWizard(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods that control the raster catalog creation wizard.'
    _iid_ = GUID('{D0579FFE-5918-4C35-9F03-D9833F728DF1}')
    _idlflags_ = ['oleautomation']
CreateRasterCatalogWizard._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ICreateRasterCatalogWizard]

class NetworkFunctionEvaluatorEditor(CoClass):
    u'The function evaluator editor.'
    _reg_clsid_ = GUID('{C355D217-6C81-4102-BB76-598BFC1E2625}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
NetworkFunctionEvaluatorEditor._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IEvaluatorEditor]

class NetworkGlobalTurnDelayEvaluatorEditor(CoClass):
    u'The global turn delay evaluator editor.'
    _reg_clsid_ = GUID('{8A22ADE5-5F91-4B0A-8849-7E133A1F5290}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
NetworkGlobalTurnDelayEvaluatorEditor._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IEvaluatorEditor]

class AGSDiscoveryCapabilityDetailsPage(CoClass):
    u'Esri AGS Service Capability Details property page.'
    _reg_clsid_ = GUID('{0B642C07-A835-4D30-96B5-AD395F82970B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSDiscoveryCapabilityDetailsPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class AttributesEditContext(CoClass):
    u'Provides Attributes Editing Contextual Information.'
    _reg_clsid_ = GUID('{AFBF52E1-A729-4929-BAEB-DB455448D2AF}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AttributesEditContext._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IAttributesEditContext]

IGxDocumentationView._methods_ = [
    COMMETHOD([helpstring(u'Opens the current metadata editor.')], HRESULT, 'Edit'),
    COMMETHOD([helpstring(u'Opens the Metadata Properties dialog box.')], HRESULT, 'EditProperties'),
    COMMETHOD([helpstring(u'Writes the current property values to the metadata.')], HRESULT, 'Synchronize'),
]
################################################################
## code template for IGxDocumentationView implementation
##class IGxDocumentationView_Impl(object):
##    def Edit(self):
##        u'Opens the current metadata editor.'
##        #return 
##
##    def Synchronize(self):
##        u'Writes the current property values to the metadata.'
##        #return 
##
##    def EditProperties(self):
##        u'Opens the Metadata Properties dialog box.'
##        #return 
##

class NetworkEdgeTrafficEvaluatorEditor(CoClass):
    u'The edge traffic evaluator editor.'
    _reg_clsid_ = GUID('{161932A8-9A46-45E9-BC45-204079D0AC54}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
NetworkEdgeTrafficEvaluatorEditor._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IEvaluatorEditor]

class SearchServerObjectPropPage(CoClass):
    u'Esri ArcGIS Server Catalog Server Object property page.'
    _reg_clsid_ = GUID('{8866AFA5-6C8F-4615-9E80-D02A2DB833E9}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
SearchServerObjectPropPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class NetworkConfiguration(CoClass):
    u'Provides Network Configuration Information.'
    _reg_clsid_ = GUID('{DCB115F6-77BE-4404-8410-2BAE6C2052F3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
class INetworkConfiguration(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the network configuration.'
    _iid_ = GUID('{6B564787-0986-4656-BFEB-EAFFB5970200}')
    _idlflags_ = ['oleautomation']
class INetworkAttributeConfiguration3(INetworkAttributeConfiguration2):
    _case_insensitive_ = True
    u'Provides access to the network attribute configuration.'
    _iid_ = GUID('{477E4214-65BF-4180-8934-2CAEBAA08BF3}')
    _idlflags_ = ['oleautomation']
class INetworkElevationConfiguration(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the network elevation configuration.'
    _iid_ = GUID('{6DC46E9D-90EC-4F58-8655-44709BA94C54}')
    _idlflags_ = ['oleautomation']
class INetworkElevationConfiguration2(INetworkElevationConfiguration):
    _case_insensitive_ = True
    u'Provides access to the network elevation configuration.'
    _iid_ = GUID('{7C9594A1-E722-45EC-ADD2-D6035BA0C914}')
    _idlflags_ = ['oleautomation']
class INetworkDirectionConfiguration(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the network direction configuration.'
    _iid_ = GUID('{FC9638F4-3E99-4B39-A2D4-8603A712564A}')
    _idlflags_ = ['oleautomation']
class INetworkDirectionConfiguration2(INetworkDirectionConfiguration):
    _case_insensitive_ = True
    u'Provides access to the network direction configuration.'
    _iid_ = GUID('{8455E852-6433-4B4F-B607-19DB93EA6B2B}')
    _idlflags_ = ['oleautomation']
class INetworkDirectionConfiguration3(INetworkDirectionConfiguration2):
    _case_insensitive_ = True
    u'Provides access to the network direction configuration.'
    _iid_ = GUID('{435CFD2D-7C2C-4A2B-BDFA-C4DB9C2377DA}')
    _idlflags_ = ['oleautomation']
NetworkConfiguration._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, INetworkConfiguration, INetworkTrafficConfiguration, INetworkTrafficConfiguration2, INetworkAttributeConfiguration, INetworkAttributeConfiguration2, INetworkAttributeConfiguration3, INetworkElevationConfiguration, INetworkElevationConfiguration2, INetworkDirectionConfiguration, INetworkDirectionConfiguration2, INetworkDirectionConfiguration3]

class RasterCoordSysPage(CoClass):
    u'Esri Raster Coordinate System Page.'
    _reg_clsid_ = GUID('{1D61AF6C-664E-4EE3-8B59-3874F0D303E6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
RasterCoordSysPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class AGSDiscoveryCachingGeneralPage(CoClass):
    u'Esri AGS Service Caching General property page.'
    _reg_clsid_ = GUID('{0871613E-41A9-470A-8D71-55650DEF5E01}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
class ISDEditorPropertyPage(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Optional Method called by the framework to allow the property page to validate itself at the very just before saving.'
    _iid_ = GUID('{6CC28B3A-1E8A-4932-88E4-B8080F76AC36}')
    _idlflags_ = ['oleautomation']
AGSDiscoveryCachingGeneralPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, ISDEditorPropertyPage]

ICreateRasterCatalogWizard._methods_ = [
    COMMETHOD([helpstring(u'Shows modal Dialog of the wizard.')], HRESULT, 'DoModal',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureWorkspace), 'pWorkspace' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'Parent' )),
]
################################################################
## code template for ICreateRasterCatalogWizard implementation
##class ICreateRasterCatalogWizard_Impl(object):
##    def DoModal(self, pWorkspace, Parent):
##        u'Shows modal Dialog of the wizard.'
##        #return 
##

IMetadataHelper._methods_ = [
    COMMETHOD([helpstring(u'Refreshes the currently selected object in the Catalog.')], HRESULT, 'Refresh',
              ( ['in'], POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxObject), 'ipObject' )),
    COMMETHOD(['propput', helpstring(u'CLSID of the currently selected editor.')], HRESULT, 'Editor',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID), 'Editor' )),
    COMMETHOD(['propget', helpstring(u'CLSID of the currently selected editor.')], HRESULT, 'Editor',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID)), 'Editor' )),
    COMMETHOD(['propput', helpstring(u'Name of the currently selected stylesheet.')], HRESULT, 'Stylesheet',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD(['propget', helpstring(u'Name of the currently selected stylesheet.')], HRESULT, 'Stylesheet',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propput', helpstring(u'Name of the default stylesheet.')], HRESULT, 'DefaultStylesheet',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD(['propget', helpstring(u'Name of the default stylesheet.')], HRESULT, 'DefaultStylesheet',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'Path to the Stylesheets directory.')], HRESULT, 'StylesheetPath',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'Path to the HTML directory.')], HRESULT, 'WebPagePath',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propput', helpstring(u'When the Catalog creates and updates metadata automatically.')], HRESULT, 'SynchronizationOption',
              ( ['in'], comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.esriSynchronizationOption, 'option' )),
    COMMETHOD(['propget', helpstring(u'When the Catalog creates and updates metadata automatically.')], HRESULT, 'SynchronizationOption',
              ( ['retval', 'out'], POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.esriSynchronizationOption), 'option' )),
    COMMETHOD(['propput', helpstring(u'The interval in seconds from the last update which must elapse before the Catalog will again update the metadata.')], HRESULT, 'SynchronizationInterval',
              ( ['in'], c_int, 'interval' )),
    COMMETHOD(['propget', helpstring(u'The interval in seconds from the last update which must elapse before the Catalog will again update the metadata.')], HRESULT, 'SynchronizationInterval',
              ( ['retval', 'out'], POINTER(c_int), 'interval' )),
]
################################################################
## code template for IMetadataHelper implementation
##class IMetadataHelper_Impl(object):
##    def _get(self):
##        u'The interval in seconds from the last update which must elapse before the Catalog will again update the metadata.'
##        #return interval
##    def _set(self, interval):
##        u'The interval in seconds from the last update which must elapse before the Catalog will again update the metadata.'
##    SynchronizationInterval = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def WebPagePath(self):
##        u'Path to the HTML directory.'
##        #return Name
##
##    def _get(self):
##        u'Name of the default stylesheet.'
##        #return Name
##    def _set(self, Name):
##        u'Name of the default stylesheet.'
##    DefaultStylesheet = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def StylesheetPath(self):
##        u'Path to the Stylesheets directory.'
##        #return Name
##
##    def Refresh(self, ipObject):
##        u'Refreshes the currently selected object in the Catalog.'
##        #return 
##
##    def _get(self):
##        u'Name of the currently selected stylesheet.'
##        #return Name
##    def _set(self, Name):
##        u'Name of the currently selected stylesheet.'
##    Stylesheet = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'CLSID of the currently selected editor.'
##        #return Editor
##    def _set(self, Editor):
##        u'CLSID of the currently selected editor.'
##    Editor = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'When the Catalog creates and updates metadata automatically.'
##        #return option
##    def _set(self, option):
##        u'When the Catalog creates and updates metadata automatically.'
##    SynchronizationOption = property(_get, _set, doc = _set.__doc__)
##

class TableDefWeightsPage(CoClass):
    u'Esri feature class weights association page.'
    _reg_clsid_ = GUID('{F64D9CE1-1F15-11D3-9C05-00C04F5B951E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
TableDefWeightsPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class CovFCGeneralPage(CoClass):
    u'Coverage Featureclass General Property Page.'
    _reg_clsid_ = GUID('{1BDB58E0-B802-42AD-A7EC-E71DE7A91909}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
CovFCGeneralPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class IGxContentsViewColumns(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the columns of GxContentsView.'
    _iid_ = GUID('{26212055-EF93-11D3-A685-0008C7D3AE8D}')
    _idlflags_ = ['oleautomation']
IGxContentsViewColumns._methods_ = [
    COMMETHOD([helpstring(u'Inserts a GxContentsViewColumn before the specified index.  If index is -1, the column is inserted at the end.')], HRESULT, 'InsertColumn',
              ( ['in'], c_int, 'index' ),
              ( ['in'], POINTER(IGxContentsViewColumn), 'pColumn' )),
    COMMETHOD([helpstring(u'Removes a GxContentsViewColumn.')], HRESULT, 'RemoveColumn',
              ( ['in'], POINTER(IGxContentsViewColumn), 'pColumn' )),
    COMMETHOD([helpstring(u'Removes all columns except Name and Type column (they are always shown).')], HRESULT, 'RemoveAllColumns'),
    COMMETHOD([helpstring(u'Refresh columns in contents view after insert or remove columns.')], HRESULT, 'UpdateColumns'),
    COMMETHOD(['propget', helpstring(u'The total number of columns (include both visible and invisible columns).')], HRESULT, 'ColumnCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'A column by its index.')], HRESULT, 'ColumnByIndex',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IGxContentsViewColumn)), 'ppColumn' )),
    COMMETHOD(['propget', helpstring(u'A column by its property.')], HRESULT, 'ColumnByProperty',
              ( ['in'], BSTR, 'property' ),
              ( ['retval', 'out'], POINTER(POINTER(IGxContentsViewColumn)), 'ppColumn' )),
]
################################################################
## code template for IGxContentsViewColumns implementation
##class IGxContentsViewColumns_Impl(object):
##    @property
##    def ColumnCount(self):
##        u'The total number of columns (include both visible and invisible columns).'
##        #return Count
##
##    @property
##    def ColumnByProperty(self, property):
##        u'A column by its property.'
##        #return ppColumn
##
##    def InsertColumn(self, index, pColumn):
##        u'Inserts a GxContentsViewColumn before the specified index.  If index is -1, the column is inserted at the end.'
##        #return 
##
##    def RemoveAllColumns(self):
##        u'Removes all columns except Name and Type column (they are always shown).'
##        #return 
##
##    def UpdateColumns(self):
##        u'Refresh columns in contents view after insert or remove columns.'
##        #return 
##
##    def RemoveColumn(self, pColumn):
##        u'Removes a GxContentsViewColumn.'
##        #return 
##
##    @property
##    def ColumnByIndex(self, index):
##        u'A column by its index.'
##        #return ppColumn
##

class CovProjectPage(CoClass):
    u'Coverage Projection and Extent Property Page.'
    _reg_clsid_ = GUID('{A5B088D1-D10C-4397-BFA3-215D224851FF}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
CovProjectPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class GeoprocessingServerObjectPropPage(CoClass):
    u'Esri ArcGIS Server Geoprocessing Server Object property page.'
    _reg_clsid_ = GUID('{17886CC0-BFF3-4D36-ACC3-DDDCF6FEAB9D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GeoprocessingServerObjectPropPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class NetworkDirectionsShieldsPage(CoClass):
    u'Esri network directions shields page.'
    _reg_clsid_ = GUID('{D7894778-4843-4141-A988-D74FDB49193D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
NetworkDirectionsShieldsPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class AGSDiscoverySearchParametersPage(CoClass):
    u'Esri AGS Search Service Parameters Property Page.'
    _reg_clsid_ = GUID('{F2923271-3025-4AC8-A608-49F2F5CF2126}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSDiscoverySearchParametersPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class EditEvaluators(CoClass):
    u'Helper for editing evaluated attributes.'
    _reg_clsid_ = GUID('{09C9AF26-F99D-4966-A660-D0C7DB5E3936}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
class IEditEvaluators(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the edit evaluators.'
    _iid_ = GUID('{C6DA44EA-100A-4912-8445-67FE8B586ADA}')
    _idlflags_ = ['oleautomation']
EditEvaluators._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IEditEvaluators]

class RelationshipRulesPage(CoClass):
    u'Relationship Class Rules Property Page.'
    _reg_clsid_ = GUID('{21F4070D-E167-11D2-9F59-00C04F6BC626}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
RelationshipRulesPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class CovGeneralPage(CoClass):
    u'Coverage General Property Page.'
    _reg_clsid_ = GUID('{E9275247-0D16-4606-8182-0B9653C24E7D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
CovGeneralPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class AGSDiscoveryGlobeCachingPage(CoClass):
    u'Esri AGS Discovery Globe Caching property page.'
    _reg_clsid_ = GUID('{C2FCD5F2-45C6-4FE8-BE18-65763F0019A6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSDiscoveryGlobeCachingPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class AGSParameterPagesContainer(CoClass):
    u'Esri AGS Server Parameter Pages Container.'
    _reg_clsid_ = GUID('{07528A12-B4D7-4048-BA37-6B0F7FA1B8F7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSParameterPagesContainer._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class IGxContentsView(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the GxContentsView.'
    _iid_ = GUID('{DA1862EA-95F8-11D2-AF67-080009EC734B}')
    _idlflags_ = ['oleautomation']
IGxContentsView._methods_ = [
    COMMETHOD(['propget', helpstring(u'The current display style.')], HRESULT, 'DisplayStyle',
              ( ['retval', 'out'], POINTER(esriContentsViewStyle), 'contentsStyle' )),
    COMMETHOD(['propput', helpstring(u'The current display style.')], HRESULT, 'DisplayStyle',
              ( ['in'], esriContentsViewStyle, 'contentsStyle' )),
    COMMETHOD(['propget', helpstring(u'Indicates if multiple objects can be selected.')], HRESULT, 'AllowMultiSelect',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'multiSelect' )),
    COMMETHOD(['propput', helpstring(u'Indicates if multiple objects can be selected.')], HRESULT, 'AllowMultiSelect',
              ( ['in'], VARIANT_BOOL, 'multiSelect' )),
    COMMETHOD(['propputref', helpstring(u'The object filter used for controlling what objects are displayed.')], HRESULT, 'ObjectFilter',
              ( ['in'], POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxObjectFilter), 'rhs' )),
    COMMETHOD([helpstring(u'Starts a rename operation on the current selection.')], HRESULT, 'BeginRename'),
]
################################################################
## code template for IGxContentsView implementation
##class IGxContentsView_Impl(object):
##    def BeginRename(self):
##        u'Starts a rename operation on the current selection.'
##        #return 
##
##    def _get(self):
##        u'Indicates if multiple objects can be selected.'
##        #return multiSelect
##    def _set(self, multiSelect):
##        u'Indicates if multiple objects can be selected.'
##    AllowMultiSelect = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The current display style.'
##        #return contentsStyle
##    def _set(self, contentsStyle):
##        u'The current display style.'
##    DisplayStyle = property(_get, _set, doc = _set.__doc__)
##
##    def ObjectFilter(self, rhs):
##        u'The object filter used for controlling what objects are displayed.'
##        #return 
##

class TableDefViewDescPage(CoClass):
    u'ESRI table view description page.'
    _reg_clsid_ = GUID('{C29DB756-509F-4704-AD45-7D0A6C526952}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
TableDefViewDescPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class AGSServerDirsPage(CoClass):
    u'Esri AGS Server Directories property page.'
    _reg_clsid_ = GUID('{E432528B-C2CA-4955-B9AF-5B2426FCC525}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSServerDirsPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class AGSServerClustersPage(CoClass):
    u'Esri AGS Server Config Store property page.'
    _reg_clsid_ = GUID('{A7C79BB8-18D9-4779-B762-767C10FB868A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSServerClustersPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class LocalCachePage(CoClass):
    u'Esri GIS Server Map Service Local Cache property page.'
    _reg_clsid_ = GUID('{56292C46-9F24-456B-A63D-8F1EF2E83909}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
LocalCachePage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

IGxViewPrint._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if the view can be printed.')], HRESULT, 'IsPrintable',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsPrintable' )),
    COMMETHOD([helpstring(u'Prints the view.')], HRESULT, 'Print'),
]
################################################################
## code template for IGxViewPrint implementation
##class IGxViewPrint_Impl(object):
##    def Print(self):
##        u'Prints the view.'
##        #return 
##
##    @property
##    def IsPrintable(self):
##        u'Indicates if the view can be printed.'
##        #return IsPrintable
##

class GxBrowserDockWindow(CoClass):
    u'The Catalog window dockable window.'
    _reg_clsid_ = GUID('{7F09BEFF-4F85-48A2-A3DC-39430262799E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GxBrowserDockWindow._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IDockableWindowDef, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IDockableWindowInitialPlacement, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IDockableWindowImageDef]

class EditEvaluatorContext(CoClass):
    u'The edit evaluator context.'
    _reg_clsid_ = GUID('{F0CC23FE-2DE9-4312-B8DE-D46EB55DC8AB}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
EditEvaluatorContext._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IEditEvaluatorContext]

class ProxyServerPage(CoClass):
    u'Esri Proxy Server property page.'
    _reg_clsid_ = GUID('{F66C99F8-D7C0-43C6-88C7-DC15435C5321}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
ProxyServerPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class AGSServerLogSettingsPage(CoClass):
    u'Esri AGS Server Log Settings property page.'
    _reg_clsid_ = GUID('{B239C44A-C406-4E45-A527-60D7EA309C92}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSServerLogSettingsPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class AGSImageParameterPage(CoClass):
    u'Esri AGS Image Service Parameter property page.'
    _reg_clsid_ = GUID('{653B8E23-753F-4D9D-9FE0-4A0313D1F753}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSImageParameterPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, IAGSParameterPage]

class GxTreeView(CoClass):
    u'GxView that represents the tree view.'
    _reg_clsid_ = GUID('{B1DE27AD-D892-11D1-AA81-064342000000}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GxTreeView._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxCatalogEvents, comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxSelectionEvents, IGxTreeView, IGxView]

class MapServerObjectPropPage(CoClass):
    u'Esri ArcGIS Server Map Server Object property page.'
    _reg_clsid_ = GUID('{0D0281C4-CB32-432E-ADB1-58978969B1FC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
MapServerObjectPropPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class GxContentsView(CoClass):
    u'GxView that represents the contents view.'
    _reg_clsid_ = GUID('{B1DE27AE-D892-11D1-AA81-064342000000}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GxContentsView._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxCatalogEvents, IGxContentsView, IGxContentsViewColumns, comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxSelectionEvents, IGxView, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream]

class INetworkDatasetDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that show dialogs for creating and editing network datasets.'
    _iid_ = GUID('{9D465195-F9BB-4D61-B4EA-B3F867F6CA03}')
    _idlflags_ = ['oleautomation']
INetworkDatasetDialog._methods_ = [
    COMMETHOD([helpstring(u'Prompts the user to define a new network dataset.')], HRESULT, 'DoModalCreateNetwork',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClassName), 'lineClassName' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentWindow' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INetworkDataset)), 'network' )),
    COMMETHOD([helpstring(u'Prompts the user to define a new network dataset.')], HRESULT, 'DoModalAdvancedCreateNetwork',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureDatasetName), 'fdsName' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentWindow' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INetworkDataset)), 'network' )),
    COMMETHOD([helpstring(u'Prompts the user to define a new network dataset.')], HRESULT, 'DoModalDataElementCreateNetwork',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetContainer2), 'datasetContainer' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDENetworkDataset), 'netDataElement' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentWindow' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INetworkDataset)), 'network' )),
    COMMETHOD([helpstring(u'Shows the properties of a network dataset.')], HRESULT, 'DoModalEdit',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INetworkDataset), 'network' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentWindow' )),
]
################################################################
## code template for INetworkDatasetDialog implementation
##class INetworkDatasetDialog_Impl(object):
##    def DoModalCreateNetwork(self, lineClassName, parentWindow):
##        u'Prompts the user to define a new network dataset.'
##        #return network
##
##    def DoModalEdit(self, network, parentWindow):
##        u'Shows the properties of a network dataset.'
##        #return 
##
##    def DoModalAdvancedCreateNetwork(self, fdsName, parentWindow):
##        u'Prompts the user to define a new network dataset.'
##        #return network
##
##    def DoModalDataElementCreateNetwork(self, datasetContainer, netDataElement, parentWindow):
##        u'Prompts the user to define a new network dataset.'
##        #return network
##

class AGSSearchServerParameterPage(CoClass):
    u'Esri AGS Catalog Server Parameter property page.'
    _reg_clsid_ = GUID('{E25C1FB8-6836-4828-A8C1-E2F8F9025F2B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSSearchServerParameterPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, IAGSParameterPage]

class AGSSOEPage(CoClass):
    u'Esri AGS Server Object Extensions property page.'
    _reg_clsid_ = GUID('{4D25B14E-5951-4460-B03B-53AB7EBD6FFB}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSSOEPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class AGSServerHostsPage(CoClass):
    u'Esri AGS Server Hosts property page.'
    _reg_clsid_ = GUID('{7F97972E-A634-4DEF-AD97-4B6C23A9EC25}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSServerHostsPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class TableDefRelationshipsPage(CoClass):
    u'Esri table definition relationships page.'
    _reg_clsid_ = GUID('{4D4B95A5-E153-11D2-99C0-0000F80372B4}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
TableDefRelationshipsPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class IDataFrameShapeDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Allows for the selection of a shape that is derived from a data frame.'
    _iid_ = GUID('{335EF59C-229F-4825-86C5-E7F943D46D2A}')
    _idlflags_ = ['oleautomation']
IDataFrameShapeDialog._methods_ = [
    COMMETHOD(['propput', helpstring(u'Provides access to the shape.')], HRESULT, 'Geometry',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'Geometry' )),
    COMMETHOD(['propget', helpstring(u'Provides access to the shape.')], HRESULT, 'Geometry',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry)), 'Geometry' )),
    COMMETHOD([helpstring(u'Opens and shows the dialog.')], HRESULT, 'DoModal',
              ( ['in'], BSTR, 'Title' ),
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMapFrame), 'pMapFrame' ),
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IGraphicsContainer), 'pContainer' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hParentWnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ok' )),
]
################################################################
## code template for IDataFrameShapeDialog implementation
##class IDataFrameShapeDialog_Impl(object):
##    def _get(self):
##        u'Provides access to the shape.'
##        #return Geometry
##    def _set(self, Geometry):
##        u'Provides access to the shape.'
##    Geometry = property(_get, _set, doc = _set.__doc__)
##
##    def DoModal(self, Title, pMapFrame, pContainer, hParentWnd):
##        u'Opens and shows the dialog.'
##        #return ok
##

class AGSServerTypesPage(CoClass):
    u'Esri AGS Server Types property page.'
    _reg_clsid_ = GUID('{8CB4298C-5E83-4DF6-9AD8-A5788A3A7448}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSServerTypesPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class AGSGeoDataServerParameterPage(CoClass):
    u'Esri AGS GeoDataServer Parameter property page.'
    _reg_clsid_ = GUID('{C816DBA7-E455-4F47-B6E6-ED10F202ECCA}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSGeoDataServerParameterPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, IAGSParameterPage]

class IProjectedCoordinateSystemDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Projected Coordinate System Dialog.'
    _iid_ = GUID('{A38CB581-95CE-11D2-AD2A-00C04FA33A15}')
    _idlflags_ = ['oleautomation']
IProjectedCoordinateSystemDialog._methods_ = [
    COMMETHOD([helpstring(u'Prompts the user to define a new projected coordinate system.')], HRESULT, 'DoModalCreate',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hParent' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IProjectedCoordinateSystem)), 'pcs' )),
]
################################################################
## code template for IProjectedCoordinateSystemDialog implementation
##class IProjectedCoordinateSystemDialog_Impl(object):
##    def DoModalCreate(self, hParent):
##        u'Prompts the user to define a new projected coordinate system.'
##        #return pcs
##

class AGSServerConfigStorePage(CoClass):
    u'Esri AGS Server Config Store property page.'
    _reg_clsid_ = GUID('{690FC9A6-F217-4F4F-9006-9A1B982C72E9}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSServerConfigStorePage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class AGSNewCachingPage(CoClass):
    u'Esri AGS Caching property page.'
    _reg_clsid_ = GUID('{79A2823B-ABFC-49A3-B52B-1A5FD76223B2}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSNewCachingPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class ISpatialReferenceDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Spatial Reference Dialog.'
    _iid_ = GUID('{16688540-54C4-11D2-AAD3-00C04FA33A15}')
    _idlflags_ = ['oleautomation']
ISpatialReferenceDialog._methods_ = [
    COMMETHOD([helpstring(u'Prompts the user to define a new spatial reference.')], HRESULT, 'DoModalCreate',
              ( ['in'], VARIANT_BOOL, 'hasXY' ),
              ( ['in'], VARIANT_BOOL, 'hasZ' ),
              ( ['in'], VARIANT_BOOL, 'hasM' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hParent' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference)), 'SpatialReference' )),
    COMMETHOD([helpstring(u'Displays/edits the properties of the given spatial reference.')], HRESULT, 'DoModalEdit',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference), 'inputSpatialReference' ),
              ( ['in'], VARIANT_BOOL, 'hasXY' ),
              ( ['in'], VARIANT_BOOL, 'hasZ' ),
              ( ['in'], VARIANT_BOOL, 'hasM' ),
              ( ['in'], VARIANT_BOOL, 'coordPageReadOnly' ),
              ( ['in'], VARIANT_BOOL, 'domainPageReadOnly' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hParent' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference)), 'outputSpatialReference' )),
]
################################################################
## code template for ISpatialReferenceDialog implementation
##class ISpatialReferenceDialog_Impl(object):
##    def DoModalEdit(self, inputSpatialReference, hasXY, hasZ, hasM, coordPageReadOnly, domainPageReadOnly, hParent):
##        u'Displays/edits the properties of the given spatial reference.'
##        #return outputSpatialReference
##
##    def DoModalCreate(self, hasXY, hasZ, hasM, hParent):
##        u'Prompts the user to define a new spatial reference.'
##        #return SpatialReference
##

class TableIndexPage(CoClass):
    u'Esri table index page.'
    _reg_clsid_ = GUID('{4D4B95A4-E153-11D2-99C0-0000F80372B4}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
TableIndexPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class AGSGeoprocessingParameterPage(CoClass):
    u'Esri AGS Geoprocessing Parameter property page.'
    _reg_clsid_ = GUID('{535765F5-28C1-47B3-B63C-F9A81934EEAA}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSGeoprocessingParameterPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, IAGSParameterPage]

class ZCoordSysPage(CoClass):
    u'Esri Z Coordinate System Page.'
    _reg_clsid_ = GUID('{577FA5D9-B888-428B-89F3-B078EE2DCE51}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
ZCoordSysPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class AGSGeometryParameterPage(CoClass):
    u'Esri AGS Geometry Parameter property page.'
    _reg_clsid_ = GUID('{55550C54-9486-4347-AEEA-991FA7703CFF}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSGeometryParameterPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, IAGSParameterPage]

IQueryTableDialog._methods_ = [
    COMMETHOD([helpstring(u'Displays the  dialog to define a query layer.')], HRESULT, 'DoModalQueryTable',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IQueryTableName), 'pName' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hParent' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IQueryTableName)), 'ppName' )),
]
################################################################
## code template for IQueryTableDialog implementation
##class IQueryTableDialog_Impl(object):
##    def DoModalQueryTable(self, pName, hParent):
##        u'Displays the  dialog to define a query layer.'
##        #return ppName
##

IEditEvaluators._methods_ = [
    COMMETHOD([helpstring(u'Intitialize the network attribute edit context.')], HRESULT, 'Initialize',
              ( ['in'], POINTER(IAttributesEditContext), 'context' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IEvaluatedNetworkAttribute), 'attribute' ),
              ( ['in'], VARIANT_BOOL, 'defaultMode' )),
    COMMETHOD(['propget', helpstring(u'The network dataset context.')], HRESULT, 'AttributesEditContext',
              ( ['retval', 'out'], POINTER(POINTER(IAttributesEditContext)), 'context' )),
    COMMETHOD(['propget', helpstring(u'The evaluated network attribute.')], HRESULT, 'EvaluatedAttribute',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IEvaluatedNetworkAttribute)), 'netAttribute' )),
    COMMETHOD(['propget', helpstring(u'Indicates if is default evaluators mode.')], HRESULT, 'IsDefault',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'defaultMode' )),
    COMMETHOD(['propget', helpstring(u'The total number of evaluators.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'The ith edit evaluator.')], HRESULT, 'EditEvaluator',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INetworkEvaluator)), 'evaluator' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the evaluator is selected.')], HRESULT, 'IsSelected',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'selected' )),
    COMMETHOD(['propget', helpstring(u'The number of selected evaluators.')], HRESULT, 'SelectedCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'The index of the selPostion selected evaluator.')], HRESULT, 'SelectedIndex',
              ( ['in'], c_int, 'selPosition' ),
              ( ['retval', 'out'], POINTER(c_int), 'index' )),
]
################################################################
## code template for IEditEvaluators implementation
##class IEditEvaluators_Impl(object):
##    @property
##    def Count(self):
##        u'The total number of evaluators.'
##        #return Count
##
##    @property
##    def EditEvaluator(self, index):
##        u'The ith edit evaluator.'
##        #return evaluator
##
##    @property
##    def SelectedCount(self):
##        u'The number of selected evaluators.'
##        #return Count
##
##    @property
##    def SelectedIndex(self, selPosition):
##        u'The index of the selPostion selected evaluator.'
##        #return index
##
##    @property
##    def IsSelected(self, index):
##        u'Indicates if the evaluator is selected.'
##        #return selected
##
##    @property
##    def EvaluatedAttribute(self):
##        u'The evaluated network attribute.'
##        #return netAttribute
##
##    def Initialize(self, context, attribute, defaultMode):
##        u'Intitialize the network attribute edit context.'
##        #return 
##
##    @property
##    def AttributesEditContext(self):
##        u'The network dataset context.'
##        #return context
##
##    @property
##    def IsDefault(self):
##        u'Indicates if is default evaluators mode.'
##        #return defaultMode
##

class ISearchEngineProperties(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u"Provides access to members that modify the search engine's property set."
    _iid_ = GUID('{B46F085C-DB78-4862-A391-FCFDC92C62CB}')
    _idlflags_ = ['oleautomation']
ISearchEngineProperties._methods_ = [
    COMMETHOD([helpstring(u"Opens a dialog box that lets a user set the search engine's properties.")], HRESULT, 'Edit',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentHWnd' )),
    COMMETHOD([helpstring(u'Loads the search engine properties from the given property set.')], HRESULT, 'Load',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'pPropertySet' )),
    COMMETHOD([helpstring(u'Saves the search engine properties to the given property set.')], HRESULT, 'Save',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'pPropertySet' )),
    COMMETHOD(['propget', helpstring(u'Starting location of a search.')], HRESULT, 'LocationString',
              ( ['retval', 'out'], POINTER(BSTR), 'pLocation' )),
    COMMETHOD(['propput', helpstring(u'Starting location of a search.')], HRESULT, 'LocationString',
              ( ['in'], BSTR, 'pLocation' )),
]
################################################################
## code template for ISearchEngineProperties implementation
##class ISearchEngineProperties_Impl(object):
##    def Edit(self, parentHWnd):
##        u"Opens a dialog box that lets a user set the search engine's properties."
##        #return 
##
##    def Load(self, pPropertySet):
##        u'Loads the search engine properties from the given property set.'
##        #return 
##
##    def Save(self, pPropertySet):
##        u'Saves the search engine properties to the given property set.'
##        #return 
##
##    def _get(self):
##        u'Starting location of a search.'
##        #return pLocation
##    def _set(self, pLocation):
##        u'Starting location of a search.'
##    LocationString = property(_get, _set, doc = _set.__doc__)
##

INetworkConfiguration._methods_ = [
    COMMETHOD(['propget', helpstring(u'The template configuration path.')], HRESULT, 'XMLPath',
              ( ['retval', 'out'], POINTER(BSTR), 'path' )),
    COMMETHOD(['propget', helpstring(u'The schema definition path.')], HRESULT, 'XSDPath',
              ( ['retval', 'out'], POINTER(BSTR), 'path' )),
    COMMETHOD(['propget', helpstring(u'The template configuration target namespace.')], HRESULT, 'TargetNamespace',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the templates are valid.')], HRESULT, 'TemplatesValid',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'valid' )),
    COMMETHOD(['propget', helpstring(u'The template configuration status description.')], HRESULT, 'StatusDescription',
              ( ['retval', 'out'], POINTER(BSTR), 'Description' )),
]
################################################################
## code template for INetworkConfiguration implementation
##class INetworkConfiguration_Impl(object):
##    @property
##    def XMLPath(self):
##        u'The template configuration path.'
##        #return path
##
##    @property
##    def TargetNamespace(self):
##        u'The template configuration target namespace.'
##        #return Name
##
##    @property
##    def StatusDescription(self):
##        u'The template configuration status description.'
##        #return Description
##
##    @property
##    def TemplatesValid(self):
##        u'Indicates if the templates are valid.'
##        #return valid
##
##    @property
##    def XSDPath(self):
##        u'The schema definition path.'
##        #return path
##

INetworkDirectionConfiguration._methods_ = [
    COMMETHOD(['propget', helpstring(u'The default output linear units.')], HRESULT, 'OutputLinearUnits',
              ( ['retval', 'out'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriNetworkAttributeUnits), 'outputUnits' )),
    COMMETHOD(['propget', helpstring(u'The road class attribute names.')], HRESULT, 'RoadClassAttributeNames',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'names' )),
    COMMETHOD(['propget', helpstring(u'The prefix direction field names.')], HRESULT, 'PreDirNames',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'names' )),
    COMMETHOD(['propget', helpstring(u'The prefix type direction field names.')], HRESULT, 'PreTypeNames',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'names' )),
    COMMETHOD(['propget', helpstring(u'The street name direction field names.')], HRESULT, 'StreetNames',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'names' )),
    COMMETHOD(['propget', helpstring(u'The suffix type direction field names.')], HRESULT, 'SuffixTypeNames',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'names' )),
    COMMETHOD(['propget', helpstring(u'The suffix direction field names.')], HRESULT, 'SuffixNames',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'names' )),
]
################################################################
## code template for INetworkDirectionConfiguration implementation
##class INetworkDirectionConfiguration_Impl(object):
##    @property
##    def StreetNames(self):
##        u'The street name direction field names.'
##        #return names
##
##    @property
##    def PreTypeNames(self):
##        u'The prefix type direction field names.'
##        #return names
##
##    @property
##    def SuffixTypeNames(self):
##        u'The suffix type direction field names.'
##        #return names
##
##    @property
##    def PreDirNames(self):
##        u'The prefix direction field names.'
##        #return names
##
##    @property
##    def OutputLinearUnits(self):
##        u'The default output linear units.'
##        #return outputUnits
##
##    @property
##    def RoadClassAttributeNames(self):
##        u'The road class attribute names.'
##        #return names
##
##    @property
##    def SuffixNames(self):
##        u'The suffix direction field names.'
##        #return names
##

INetworkDirectionConfiguration2._methods_ = [
    COMMETHOD(['propget', helpstring(u'The full name direction field names.')], HRESULT, 'FullNames',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'names' )),
    COMMETHOD(['propget', helpstring(u'The highway direction field names.')], HRESULT, 'HighwayDirectionNames',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'names' )),
    COMMETHOD(['propget', helpstring(u'The language direction field names.')], HRESULT, 'LanguageNames',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'names' )),
    COMMETHOD(['propget', helpstring(u'The PropertySet containing a PropertySet of attribute mapping constraints for each attribute mapping key.')], HRESULT, 'DirectionsAttributeMappingConstraintsPropertySets',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'propSets' )),
    COMMETHOD(['propget', helpstring(u'The PropertySet containing a PropertySet of field mapping constraints for each field mapping key.')], HRESULT, 'DirectionsFieldMappingConstraintsPropertySets',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'propSets' )),
]
################################################################
## code template for INetworkDirectionConfiguration2 implementation
##class INetworkDirectionConfiguration2_Impl(object):
##    @property
##    def DirectionsFieldMappingConstraintsPropertySets(self):
##        u'The PropertySet containing a PropertySet of field mapping constraints for each field mapping key.'
##        #return propSets
##
##    @property
##    def HighwayDirectionNames(self):
##        u'The highway direction field names.'
##        #return names
##
##    @property
##    def FullNames(self):
##        u'The full name direction field names.'
##        #return names
##
##    @property
##    def DirectionsAttributeMappingConstraintsPropertySets(self):
##        u'The PropertySet containing a PropertySet of attribute mapping constraints for each attribute mapping key.'
##        #return propSets
##
##    @property
##    def LanguageNames(self):
##        u'The language direction field names.'
##        #return names
##

INetworkDirectionConfiguration3._methods_ = [
    COMMETHOD(['propget', helpstring(u'The landmark label field names.')], HRESULT, 'LandmarkLabelFieldNames',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'names' )),
]
################################################################
## code template for INetworkDirectionConfiguration3 implementation
##class INetworkDirectionConfiguration3_Impl(object):
##    @property
##    def LandmarkLabelFieldNames(self):
##        u'The landmark label field names.'
##        #return names
##

class AGSGeneralPage(CoClass):
    u'Esri AGS Object Configuration general property page.'
    _reg_clsid_ = GUID('{DFB425AB-5EBB-4A99-A215-B1BBFEB5F96A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSGeneralPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

ISDEditorPropertyPage._methods_ = [
    COMMETHOD([helpstring(u'Optional Method called by the framework to allow the property page to validate itself at the very just before saving.')], HRESULT, 'ValidateData',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' ),
              ( ['in'], VARIANT, 'vParameters' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage)), 'ppPropertyPageWithError' )),
]
################################################################
## code template for ISDEditorPropertyPage implementation
##class ISDEditorPropertyPage_Impl(object):
##    def ValidateData(self, pTrackCancel, vParameters):
##        u'Optional Method called by the framework to allow the property page to validate itself at the very just before saving.'
##        #return ppPropertyPageWithError
##

class AGSDiscoveryGeneralPage(CoClass):
    u'Esri AGS General Service Property Page.'
    _reg_clsid_ = GUID('{F6D3EB58-69BA-45EA-A22C-D44331350014}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSDiscoveryGeneralPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]


# values for enumeration 'esriCoordSysContext'
esriCoordSystemNone = 0
esriCoordSystemXY = 1
esriCoordSystemZ = 2
esriCoordSystemRaster = 3
esriCoordSysContext = c_int # enum
class AGSDiscoveryItemDescriptionPage(CoClass):
    u'Esri AGS Service Item Description property page.'
    _reg_clsid_ = GUID('{65B205C0-4D30-476B-BA3A-3A20320968DA}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSDiscoveryItemDescriptionPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class AGSServerStatisticsPage(CoClass):
    u'Esri AGS Server Statistics property page.'
    _reg_clsid_ = GUID('{20B0DE7D-1084-447C-8E17-1D1058C05B39}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSServerStatisticsPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class GxComBrowser(CoClass):
    u'Provides access to GX browser dialog.'
    _reg_clsid_ = GUID('{6AA37E56-2D92-42E6-B74B-8F19C268F8F6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
class IGxBrowser(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the GxBrowser.'
    _iid_ = GUID('{86057A65-426A-4C04-BA66-CF73EBB70A9F}')
    _idlflags_ = ['oleautomation']
GxComBrowser._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxBrowser, comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxSelectionEvents, comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxCatalogEvents, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IComPropertySheetEvents]

INetworkAttributeConfiguration3._methods_ = [
    COMMETHOD(['propget', helpstring(u'The default script parser language supported at arcgisVersion.')], HRESULT, 'DefaultSupportedScriptParserLanguage',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.esriArcGISVersion, 'arcgisVersion' ),
              ( ['retval', 'out'], POINTER(BSTR), 'language' )),
]
################################################################
## code template for INetworkAttributeConfiguration3 implementation
##class INetworkAttributeConfiguration3_Impl(object):
##    @property
##    def DefaultSupportedScriptParserLanguage(self, arcgisVersion):
##        u'The default script parser language supported at arcgisVersion.'
##        #return language
##

class GxMSDFileFactory(CoClass):
    u'Gx Object Factory for MapServerDefinitionFile Datasets.'
    _reg_clsid_ = GUID('{89792E96-BC13-4E41-9974-C9B7713DA226}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GxMSDFileFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxObjectFactory, comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxObjectFactoryMetadata, comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxObjectFactoryFileExtensions]

class AddAGSDiscoveryUserConnectionPage(CoClass):
    u'Esri AGS Discovery Server user connection general property page.'
    _reg_clsid_ = GUID('{1B48D172-ADC3-4D6E-903D-DB8A96862BDF}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AddAGSDiscoveryUserConnectionPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

INetworkElevationConfiguration._methods_ = [
    COMMETHOD(['propget', helpstring(u'The elevation prefixes for the from end.')], HRESULT, 'FromEndPrefixes',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'prefixes' )),
    COMMETHOD(['propget', helpstring(u'The elevation prefixes for the to end.')], HRESULT, 'ToEndPrefixes',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'prefixes' )),
    COMMETHOD(['propget', helpstring(u'The root names of the elevation fields.')], HRESULT, 'BaseNames',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'names' )),
]
################################################################
## code template for INetworkElevationConfiguration implementation
##class INetworkElevationConfiguration_Impl(object):
##    @property
##    def FromEndPrefixes(self):
##        u'The elevation prefixes for the from end.'
##        #return prefixes
##
##    @property
##    def ToEndPrefixes(self):
##        u'The elevation prefixes for the to end.'
##        #return prefixes
##
##    @property
##    def BaseNames(self):
##        u'The root names of the elevation fields.'
##        #return names
##

IAGSSOEParameterPage2._methods_ = [
    COMMETHOD(['propput', helpstring(u'Name of the service.')], HRESULT, 'ServiceName',
              ( ['in'], BSTR, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Qualified name  of the service.')], HRESULT, 'QualifiedDefaultName',
              ( ['in'], BSTR, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'URL of the service.')], HRESULT, 'ServiceURL',
              ( ['in'], BSTR, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Read-only state of the SOE parameter page.')], HRESULT, 'PageReadOnly',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
]
################################################################
## code template for IAGSSOEParameterPage2 implementation
##class IAGSSOEParameterPage2_Impl(object):
##    def _set(self, rhs):
##        u'Name of the service.'
##    ServiceName = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Qualified name  of the service.'
##    QualifiedDefaultName = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'URL of the service.'
##    ServiceURL = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Read-only state of the SOE parameter page.'
##    PageReadOnly = property(fset = _set, doc = _set.__doc__)
##

class IAGSSOEParameterPage3(IAGSSOEParameterPage2):
    _case_insensitive_ = True
    u'Provides access to members that control ArcGIS server object extension parameter pages.'
    _iid_ = GUID('{A81C1561-C5ED-43BC-B921-B328A9C652E2}')
    _idlflags_ = ['oleautomation']
IAGSSOEParameterPage3._methods_ = [
    COMMETHOD(['propput', helpstring(u'The enum of server directories.')], HRESULT, 'ServerDirectories',
              ( ['in'], POINTER(comtypes.gen._18F2FC71_6B30_45B9_B101_037A8B868B66_0_10_2.IEnumServerDirectory), 'rhs' )),
]
################################################################
## code template for IAGSSOEParameterPage3 implementation
##class IAGSSOEParameterPage3_Impl(object):
##    def _set(self, rhs):
##        u'The enum of server directories.'
##    ServerDirectories = property(fset = _set, doc = _set.__doc__)
##

IEvaluatorEditor._methods_ = [
    COMMETHOD(['propget', helpstring(u'The evaluator CLSID associated with this editor.')], HRESULT, 'EvaluatorCLSID',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID)), 'clsid' )),
    COMMETHOD(['propputref', helpstring(u'The available set of edit evaluators.')], HRESULT, 'EditEvaluators',
              ( ['in'], POINTER(IEditEvaluators), 'rhs' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the editor supports textbox editing of the descriptor value for the current attribute edit context.')], HRESULT, 'ContextSupportsEditDescriptors',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'supports' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the editor supports a dialog for the current attribute edit context.')], HRESULT, 'ContextSupportsEditProperties',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'supports' )),
    COMMETHOD([helpstring(u'The default properties for the edit evaluator based on the current context.')], HRESULT, 'SetDefaultProperties',
              ( ['in'], c_int, 'index' )),
    COMMETHOD(['propget', helpstring(u'The ith full description value.')], HRESULT, 'FullDescription',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'value' )),
    COMMETHOD(['propget', helpstring(u'The ith descriptor value.')], HRESULT, 'Descriptor',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'value' )),
    COMMETHOD([helpstring(u'Change the descriptor for all selected evaluators.')], HRESULT, 'EditDescriptors',
              ( ['in'], BSTR, 'value' )),
    COMMETHOD(['propget', helpstring(u'The number of value choices.')], HRESULT, 'ValueChoiceCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'The value choice description.')], HRESULT, 'ValueChoiceDescriptor',
              ( ['in'], c_int, 'choice' ),
              ( ['retval', 'out'], POINTER(BSTR), 'value' )),
    COMMETHOD(['propput', helpstring(u'The index of the selected value choice.')], HRESULT, 'ValueChoice',
              ( ['in'], c_int, 'rhs' )),
    COMMETHOD([helpstring(u'Prompts the user to edit the evaluator.')], HRESULT, 'EditProperties',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentWindow' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'applyEdits' )),
]
################################################################
## code template for IEvaluatorEditor implementation
##class IEvaluatorEditor_Impl(object):
##    @property
##    def ValueChoiceDescriptor(self, choice):
##        u'The value choice description.'
##        #return value
##
##    @property
##    def ContextSupportsEditDescriptors(self):
##        u'Indicates if the editor supports textbox editing of the descriptor value for the current attribute edit context.'
##        #return supports
##
##    @property
##    def EvaluatorCLSID(self):
##        u'The evaluator CLSID associated with this editor.'
##        #return clsid
##
##    @property
##    def Descriptor(self, index):
##        u'The ith descriptor value.'
##        #return value
##
##    @property
##    def FullDescription(self, index):
##        u'The ith full description value.'
##        #return value
##
##    def EditProperties(self, parentWindow):
##        u'Prompts the user to edit the evaluator.'
##        #return applyEdits
##
##    def EditEvaluators(self, rhs):
##        u'The available set of edit evaluators.'
##        #return 
##
##    @property
##    def ValueChoiceCount(self):
##        u'The number of value choices.'
##        #return Count
##
##    def SetDefaultProperties(self, index):
##        u'The default properties for the edit evaluator based on the current context.'
##        #return 
##
##    def EditDescriptors(self, value):
##        u'Change the descriptor for all selected evaluators.'
##        #return 
##
##    @property
##    def ContextSupportsEditProperties(self):
##        u'Indicates if the editor supports a dialog for the current attribute edit context.'
##        #return supports
##
##    def _set(self, rhs):
##        u'The index of the selected value choice.'
##    ValueChoice = property(fset = _set, doc = _set.__doc__)
##

class AGSGeocodeParameterPage(CoClass):
    u'Esri AGS Geocode Parameter property page.'
    _reg_clsid_ = GUID('{00150F78-FF50-4BD4-AEFB-7E85E63DD317}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSGeocodeParameterPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, IAGSParameterPage]

INetworkElevationConfiguration2._methods_ = [
    COMMETHOD(['propget', helpstring(u'The elevation suffixes for the from end.')], HRESULT, 'FromEndSuffixes',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'suffixes' )),
    COMMETHOD(['propget', helpstring(u'The elevation suffixes for the to end.')], HRESULT, 'ToEndSuffixes',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'suffixes' )),
]
################################################################
## code template for INetworkElevationConfiguration2 implementation
##class INetworkElevationConfiguration2_Impl(object):
##    @property
##    def ToEndSuffixes(self):
##        u'The elevation suffixes for the to end.'
##        #return suffixes
##
##    @property
##    def FromEndSuffixes(self):
##        u'The elevation suffixes for the from end.'
##        #return suffixes
##

class AGSDiscoveryGlobeParametersPage(CoClass):
    u'Esri AGS Globe Service Parameters Property Page.'
    _reg_clsid_ = GUID('{BEE59311-BF36-4257-A782-3201D7DA818A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSDiscoveryGlobeParametersPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class SubtypesPropertyPage(CoClass):
    u'Esri table subtypes page.'
    _reg_clsid_ = GUID('{4D4B95A3-E153-11D2-99C0-0000F80372B4}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
SubtypesPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class ISpatialReferenceDialogContext(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that change the calling context of the Spatial Reference Dialog.'
    _iid_ = GUID('{8163A6FF-0ED6-4141-BC5D-FEB844C1B30F}')
    _idlflags_ = ['oleautomation']
ISpatialReferenceDialogContext._methods_ = [
    COMMETHOD(['propget', helpstring(u'The basic map that provides the layer list and spatial filtering extent.')], HRESULT, 'BasicMap',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IBasicMap)), 'BasicMap' )),
    COMMETHOD(['propputref', helpstring(u'The basic map that provides the layer list and spatial filtering extent.')], HRESULT, 'BasicMap',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IBasicMap), 'BasicMap' )),
    COMMETHOD(['propget', helpstring(u'Restriction on the type of coordinate system to show.')], HRESULT, 'XYFilter',
              ( ['retval', 'out'], POINTER(esriSpatialReferenceXYFilter), 'filter' )),
    COMMETHOD(['propput', helpstring(u'Restriction on the type of coordinate system to show.')], HRESULT, 'XYFilter',
              ( ['in'], esriSpatialReferenceXYFilter, 'filter' )),
]
################################################################
## code template for ISpatialReferenceDialogContext implementation
##class ISpatialReferenceDialogContext_Impl(object):
##    def BasicMap(self, BasicMap):
##        u'The basic map that provides the layer list and spatial filtering extent.'
##        #return 
##
##    def _get(self):
##        u'Restriction on the type of coordinate system to show.'
##        #return filter
##    def _set(self, filter):
##        u'Restriction on the type of coordinate system to show.'
##    XYFilter = property(_get, _set, doc = _set.__doc__)
##

class GxMapSOPage(CoClass):
    u'Map service properties page.'
    _reg_clsid_ = GUID('{B91D62FF-4669-4120-9E44-A601A955F6D6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GxMapSOPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, IAGSSOEParameterPage, IAGSSOEParameterPage2]

class AGSObjectAdminDialog(CoClass):
    u'Server Object Admin Dialog.'
    _reg_clsid_ = GUID('{216DA6F2-116E-4AE7-9634-C6986654B46E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
class IAGSObjectAdminDialog2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Server Object Admin Dialog.'
    _iid_ = GUID('{2024BC01-B2D4-4ADC-B25C-B623E1ABE338}')
    _idlflags_ = ['oleautomation']
AGSObjectAdminDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IAGSObjectAdminDialog, IAGSObjectAdminDialog2]

class AGSDiscoveryImageCachingGeneralPage(CoClass):
    u'Esri AGS Discovery Image Caching property page.'
    _reg_clsid_ = GUID('{AD3E80AE-A08D-4B2A-9F6D-DE35179E37AA}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSDiscoveryImageCachingGeneralPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class AGSConnectionAdminDialog(CoClass):
    u'ArcGIS Server Connection Admin tools.'
    _reg_clsid_ = GUID('{D7DA5943-3246-493E-B561-8BC9CED4C1C4}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
class IAGSConnectionAdminDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Connection Admin Dialog.'
    _iid_ = GUID('{B2772436-4029-4B58-ABD2-8E4AD62EA569}')
    _idlflags_ = ['oleautomation']
AGSConnectionAdminDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IAGSConnectionAdminDialog]

class IGxMSDFileView(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to more members that control the GxMSDFileView.'
    _iid_ = GUID('{D09F7AB7-773D-47CE-8BA4-89980C37B3B1}')
    _idlflags_ = ['oleautomation']
IGxMSDFileView._methods_ = [
    COMMETHOD(['propget', helpstring(u'The active view object(either map or page layout).')], HRESULT, 'ActiveView',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IActiveView)), 'ppActiveView' )),
]
################################################################
## code template for IGxMSDFileView implementation
##class IGxMSDFileView_Impl(object):
##    @property
##    def ActiveView(self):
##        u'The active view object(either map or page layout).'
##        #return ppActiveView
##

class GxMSDFilePropPage(CoClass):
    u'Provides access to GxMSDFile property page.'
    _reg_clsid_ = GUID('{7964E45B-1A20-4B58-9DA9-2E4B5801237E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GxMSDFilePropPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class DomainResolutionTolerancePage(CoClass):
    u'Esri feature class domain, resolution and tolerance page.'
    _reg_clsid_ = GUID('{87E5A161-7D68-4FF6-B6C2-265E462D1E6E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
DomainResolutionTolerancePage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class AddAGSFolderPage(CoClass):
    u'Esri AGS Server user connection folders property page.'
    _reg_clsid_ = GUID('{2CABDDF1-0B1A-4E81-80DE-305C3D528398}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AddAGSFolderPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class GxMSDFileView(CoClass):
    u'GxView that represents the MSDFile view.'
    _reg_clsid_ = GUID('{F1111ED3-4C31-465B-B065-91F7148DBDEB}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GxMSDFileView._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxView, IGxGeographicView, IGxGeographicView2, comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxSelectionEvents, comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxCatalogEvents, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.ITransformEvents]

class AddAGSDiscoveryDialog(CoClass):
    u'Add ArcGIS Discovery Server Dialog.'
    _reg_clsid_ = GUID('{E898645E-D138-4224-8FEF-32404BD3FE99}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AddAGSDiscoveryDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IAGSConnectionAdminDialog]

class GxNASOEPage(CoClass):
    u'NA SOE properties page.'
    _reg_clsid_ = GUID('{C91B9AF1-B6D8-40A0-A888-B41AF04D0A61}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GxNASOEPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, IAGSSOEParameterPage, IAGSSOEParameterPage2, IAGSSOEParameterPage3]

class AGSServerDataStoresPage(CoClass):
    u'Esri AGS Server Data Stores property page.'
    _reg_clsid_ = GUID('{91F76A3F-4CCE-4E78-B052-CBFAC470EE05}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSServerDataStoresPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class GxWMSSOEPage(CoClass):
    u'WMS SOE properties page.'
    _reg_clsid_ = GUID('{A070B4F3-8E64-43D4-87B0-8440FAB321AD}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GxWMSSOEPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, IAGSSOEParameterPage, IAGSSOEParameterPage2]

class SpatialReferenceDialog(CoClass):
    u'Provides access to the spatial reference dialog.'
    _reg_clsid_ = GUID('{16688541-54C4-11D2-AAD3-00C04FA33A15}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
class ISpatialReferenceDialog3(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Spatial Reference Dialog 3.'
    _iid_ = GUID('{7D6C0E92-CB16-48B3-9BF5-6B051045840C}')
    _idlflags_ = ['oleautomation']
SpatialReferenceDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ISpatialReferenceDialog, ISpatialReferenceDialog2, ISpatialReferenceDialog3, ISpatialReferenceDialogContext]

class AddAGSDiscoveryConnectionPage(CoClass):
    u'Esri AGS Discovery Server admin / publisher connection general property page.'
    _reg_clsid_ = GUID('{35172EF0-781F-49BF-9FF0-F67D9C65F0BD}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AddAGSDiscoveryConnectionPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class AGSPublishToolboxDialog(CoClass):
    u'ArcGIS Server Toolbox Publish Dialog.'
    _reg_clsid_ = GUID('{2273E4CA-FF53-469E-A48B-3041C6EA5A35}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
class IAGSPublishToolboxAdminDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Publisher Admin Dialog.'
    _iid_ = GUID('{F0912A16-B68E-4CFD-83CB-857A317B0CC8}')
    _idlflags_ = ['oleautomation']
AGSPublishToolboxDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IAGSPublishToolboxAdminDialog]

class GxServiceWorkspacesMenuItem(CoClass):
    u'GxServiceWorkspaces Menu Item.'
    _reg_clsid_ = GUID('{53135627-1589-4843-8EDE-3046A35075FC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GxServiceWorkspacesMenuItem._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.ICommand]

class GeocodeServerObjectPropPage(CoClass):
    u'Esri ArcGIS Server Geocode Server Object property page.'
    _reg_clsid_ = GUID('{1B5FF4B1-37CE-4A72-A2AE-B9D09B25CA26}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GeocodeServerObjectPropPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class ISearchEngineEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to events that are fired by an ongoing search.'
    _iid_ = GUID('{D18306A3-9D3C-11D3-A6CB-0008C7D3AE50}')
    _idlflags_ = ['oleautomation']
ISearchEngineEvents._methods_ = [
    COMMETHOD([helpstring(u'Fired when an object is found that satisfies the search criteria.')], HRESULT, 'ObjectFound',
              ( ['in'], POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxObject), 'anObject' ),
              ( ['in'], BSTR, 'Location' )),
    COMMETHOD([helpstring(u'Fired when the search is complete.')], HRESULT, 'SearchFinished'),
    COMMETHOD([helpstring(u'Fired when the search terminates prematurely.')], HRESULT, 'SearchFailed'),
    COMMETHOD([helpstring(u'Fired when the search is explicitly canceled.')], HRESULT, 'SearchCanceled'),
    COMMETHOD([helpstring(u'Fired when the search begins looking inside a new folder or other container.')], HRESULT, 'SearchLocationChanged',
              ( ['in'], BSTR, 'Location' )),
]
################################################################
## code template for ISearchEngineEvents implementation
##class ISearchEngineEvents_Impl(object):
##    def ObjectFound(self, anObject, Location):
##        u'Fired when an object is found that satisfies the search criteria.'
##        #return 
##
##    def SearchFinished(self):
##        u'Fired when the search is complete.'
##        #return 
##
##    def SearchCanceled(self):
##        u'Fired when the search is explicitly canceled.'
##        #return 
##
##    def SearchLocationChanged(self, Location):
##        u'Fired when the search begins looking inside a new folder or other container.'
##        #return 
##
##    def SearchFailed(self):
##        u'Fired when the search terminates prematurely.'
##        #return 
##

class GxAGSFolderPropertyPage(CoClass):
    u'Esri AGS Server folder property page.'
    _reg_clsid_ = GUID('{2C5CE907-9195-4E35-BB97-BEA51C1714F2}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GxAGSFolderPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class IDataFrameShapeDialog2(IDataFrameShapeDialog):
    _case_insensitive_ = True
    u'Allows for the selection of a shape that is derived from a data frame.'
    _iid_ = GUID('{34559545-E034-40D6-84AB-E67290D73DA2}')
    _idlflags_ = ['oleautomation']
IDataFrameShapeDialog2._methods_ = [
    COMMETHOD([helpstring(u'Show the dialog using only a map.')], HRESULT, 'DoModal2',
              ( ['in'], BSTR, 'Title' ),
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMap), 'pMap' ),
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IGraphicsContainer), 'pContainer' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hParentWnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ok' )),
]
################################################################
## code template for IDataFrameShapeDialog2 implementation
##class IDataFrameShapeDialog2_Impl(object):
##    def DoModal2(self, Title, pMap, pContainer, hParentWnd):
##        u'Show the dialog using only a map.'
##        #return ok
##

class IXmlQuery(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that generate XSL Pattern expressions from a query.'
    _iid_ = GUID('{B1C0A748-D6C7-4477-9C84-E83DA6F60617}')
    _idlflags_ = ['oleautomation']
IXmlQuery._methods_ = [
    COMMETHOD([helpstring(u'Creates a set of XSL Pattern expressions from a query.')], HRESULT, 'BuildExpressions'),
    COMMETHOD(['propget', helpstring(u'Number of expressions that were generated.')], HRESULT, 'NumExpressions',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD([helpstring(u'The nth expression.')], HRESULT, 'GetExpression',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the expressions are ANDed together (as opposed to ORed).')], HRESULT, 'IsAnd',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsAnd' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the expressions are ANDed together (as opposed to ORed).')], HRESULT, 'IsAnd',
              ( ['in'], VARIANT_BOOL, 'IsAnd' )),
]
################################################################
## code template for IXmlQuery implementation
##class IXmlQuery_Impl(object):
##    def BuildExpressions(self):
##        u'Creates a set of XSL Pattern expressions from a query.'
##        #return 
##
##    def GetExpression(self, index):
##        u'The nth expression.'
##        #return Name
##
##    def _get(self):
##        u'Indicates if the expressions are ANDed together (as opposed to ORed).'
##        #return IsAnd
##    def _set(self, IsAnd):
##        u'Indicates if the expressions are ANDed together (as opposed to ORed).'
##    IsAnd = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def NumExpressions(self):
##        u'Number of expressions that were generated.'
##        #return Count
##

class IGxDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the GxDialog.'
    _iid_ = GUID('{EAB9CE29-E777-11D1-AEE7-080009EC734B}')
    _idlflags_ = ['oleautomation']
IGxDialog._methods_ = [
    COMMETHOD(['propput', helpstring(u'Indicates if multiple items may be selected.  False, by default.')], HRESULT, 'AllowMultiSelect',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD(['propput', helpstring(u"The dialog's title.")], HRESULT, 'Title',
              ( ['in'], BSTR, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'The caption to use for the Open or Save button.')], HRESULT, 'ButtonCaption',
              ( ['in'], BSTR, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'The text in the Name text box (only for DoModalSave).')], HRESULT, 'Name',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD(['propget', helpstring(u'The text in the Name text box (only for DoModalSave).')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'Indicates if an object already exists with the name supplied by the user, and is being replaced.')], HRESULT, 'ReplacingObject',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ReplacingObject' )),
    COMMETHOD(['propput', helpstring(u"The dialog's starting location. This can be an IGxObject or a text-string containing the full name of an object.")], HRESULT, 'StartingLocation',
              ( ['in'], POINTER(VARIANT), 'rhs' )),
    COMMETHOD(['propget', helpstring(u"The dialog's final location.")], HRESULT, 'FinalLocation',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxObject)), 'FinalLocation' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the dialog should use the final location as the next starting location. True, by default.')], HRESULT, 'RememberLocation',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD(['propputref', helpstring(u'The object filter.')], HRESULT, 'ObjectFilter',
              ( ['in'], POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxObjectFilter), 'filter' )),
    COMMETHOD(['propget', helpstring(u'The object filter.')], HRESULT, 'ObjectFilter',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxObjectFilter)), 'filter' )),
    COMMETHOD(['propget', helpstring(u'The catalog object used internally by the GxDialog.')], HRESULT, 'InternalCatalog',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxCatalog)), 'Catalog' )),
    COMMETHOD([helpstring(u'Opens the dialog to choose data.')], HRESULT, 'DoModalOpen',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentWindow' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IEnumGxObject)), 'Selection' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'result' )),
    COMMETHOD([helpstring(u'Opens the dialog to save data.')], HRESULT, 'DoModalSave',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentWindow' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'result' )),
]
################################################################
## code template for IGxDialog implementation
##class IGxDialog_Impl(object):
##    def _set(self, rhs):
##        u'Indicates if multiple items may be selected.  False, by default.'
##    AllowMultiSelect = property(fset = _set, doc = _set.__doc__)
##
##    @property
##    def InternalCatalog(self):
##        u'The catalog object used internally by the GxDialog.'
##        #return Catalog
##
##    def _get(self):
##        u'The text in the Name text box (only for DoModalSave).'
##        #return Name
##    def _set(self, Name):
##        u'The text in the Name text box (only for DoModalSave).'
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    def DoModalSave(self, parentWindow):
##        u'Opens the dialog to save data.'
##        #return result
##
##    def _set(self, rhs):
##        u"The dialog's title."
##    Title = property(fset = _set, doc = _set.__doc__)
##
##    @property
##    def FinalLocation(self):
##        u"The dialog's final location."
##        #return FinalLocation
##
##    def _set(self, rhs):
##        u"The dialog's starting location. This can be an IGxObject or a text-string containing the full name of an object."
##    StartingLocation = property(fset = _set, doc = _set.__doc__)
##
##    @property
##    def ObjectFilter(self, filter):
##        u'The object filter.'
##        #return 
##
##    def _set(self, rhs):
##        u'The caption to use for the Open or Save button.'
##    ButtonCaption = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Indicates if the dialog should use the final location as the next starting location. True, by default.'
##    RememberLocation = property(fset = _set, doc = _set.__doc__)
##
##    @property
##    def ReplacingObject(self):
##        u'Indicates if an object already exists with the name supplied by the user, and is being replaced.'
##        #return ReplacingObject
##
##    def DoModalOpen(self, parentWindow):
##        u'Opens the dialog to choose data.'
##        #return Selection, result
##

class AddAGSServerPage(CoClass):
    u'Esri AGS Server admin connection general property page.'
    _reg_clsid_ = GUID('{A9216048-57A3-4A7C-A951-002F6AB77F39}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AddAGSServerPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class AGSDiscoveryImageMensurationPage(CoClass):
    u'Esri AGS Image Mensuration Parameters Property Page.'
    _reg_clsid_ = GUID('{AF657D8F-9380-442D-9F58-24A77BF261DE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSDiscoveryImageMensurationPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class IMetadataEditor(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that define a metadata editor.'
    _iid_ = GUID('{7AD0DA09-0D4A-11D3-A626-0008C7D3AE50}')
    _idlflags_ = ['oleautomation']
IMetadataEditor._methods_ = [
    COMMETHOD(['propget', helpstring(u'Name of the metadata editor.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD([helpstring(u'Shows the metadata editor and indicates if the metadata property set was modified.')], HRESULT, 'Edit',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'props' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hWnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pOk' )),
]
################################################################
## code template for IMetadataEditor implementation
##class IMetadataEditor_Impl(object):
##    def Edit(self, props, hWnd):
##        u'Shows the metadata editor and indicates if the metadata property set was modified.'
##        #return pOk
##
##    @property
##    def Name(self):
##        u'Name of the metadata editor.'
##        #return Name
##

class AGSDiscoveryImageCatalogEditingPage(CoClass):
    u'Esri AGS Image Catalog Editing Parameters Property Page.'
    _reg_clsid_ = GUID('{EF30C8CC-5807-47A8-9653-103344F2468C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSDiscoveryImageCatalogEditingPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class IArcIMSQuery(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that let you modify a query.'
    _iid_ = GUID('{3155EEF7-8734-43A5-87E7-62BD658363AF}')
    _idlflags_ = ['oleautomation']
IArcIMSQuery._methods_ = [
    COMMETHOD(['propget', helpstring(u'The Content type.')], HRESULT, 'ContentType',
              ( ['retval', 'out'], POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.esriContentType), 'type' )),
    COMMETHOD(['propput', helpstring(u'The Content type.')], HRESULT, 'ContentType',
              ( ['in'], comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.esriContentType, 'type' )),
]
################################################################
## code template for IArcIMSQuery implementation
##class IArcIMSQuery_Impl(object):
##    def _get(self):
##        u'The Content type.'
##        #return type
##    def _set(self, type):
##        u'The Content type.'
##    ContentType = property(_get, _set, doc = _set.__doc__)
##

class DescriptionWindow(CoClass):
    u'Provides access to memebers of DescriptionWindow.'
    _reg_clsid_ = GUID('{DAD5408A-CE79-4C22-9225-185C0F1D2F7B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
DescriptionWindow._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDescriptionWindow]

class AddAGSConnectionPage(CoClass):
    u'Esri AGS Server user connection general property page.'
    _reg_clsid_ = GUID('{DC50E01F-38A1-42BF-AFFA-CF7BF5A39B7F}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AddAGSConnectionPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class GxFeatureAccessSOEPage(CoClass):
    u'Feature Access SOE properties page.'
    _reg_clsid_ = GUID('{ED17281E-85A0-453B-BB85-DDD1B7BEE3B6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GxFeatureAccessSOEPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, IAGSSOEParameterPage, IAGSSOEParameterPage2]

class GxDocumentationViewWindow(CoClass):
    u'Provides access to memebers of DescriptionWindow.'
    _reg_clsid_ = GUID('{9C070434-1932-4135-A01A-20B1D1C78EF4}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GxDocumentationViewWindow._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxDocumentationViewWindow]

class AddAGSDialog(CoClass):
    u'Add ArcGIS Server Dialog.'
    _reg_clsid_ = GUID('{5933C3D6-36B8-4B0C-9A88-2CC3AD7C964C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AddAGSDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IAGSConnectionAdminDialog]

ISearchEngine._methods_ = [
    COMMETHOD(['propget', helpstring(u'Name of the search engine.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pName' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the search engine is enabled.')], HRESULT, 'Enabled',
              ( ['in'], VARIANT_BOOL, 'isEnabled' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the search engine is enabled.')], HRESULT, 'Enabled',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'isEnabled' )),
    COMMETHOD(['propputref', helpstring(u'Query that will be executed.')], HRESULT, 'Query',
              ( ['in'], POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IQuery), 'rhs' )),
    COMMETHOD([helpstring(u'Executes the query asynchronously.')], HRESULT, 'ExecuteAsynchronous'),
    COMMETHOD([helpstring(u'Cancels an ongoing search (if it is currently executing).')], HRESULT, 'Stop'),
    COMMETHOD(['propget', helpstring(u'Indicates if the search is currently executing.')], HRESULT, 'IsExecuting',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsExecuting' )),
]
################################################################
## code template for ISearchEngine implementation
##class ISearchEngine_Impl(object):
##    @property
##    def Name(self):
##        u'Name of the search engine.'
##        #return pName
##
##    def _get(self):
##        u'Indicates if the search engine is enabled.'
##        #return isEnabled
##    def _set(self, isEnabled):
##        u'Indicates if the search engine is enabled.'
##    Enabled = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def IsExecuting(self):
##        u'Indicates if the search is currently executing.'
##        #return IsExecuting
##
##    def Stop(self):
##        u'Cancels an ongoing search (if it is currently executing).'
##        #return 
##
##    def Query(self, rhs):
##        u'Query that will be executed.'
##        #return 
##
##    def ExecuteAsynchronous(self):
##        u'Executes the query asynchronously.'
##        #return 
##

IGxBrowser._methods_ = [
    COMMETHOD(['propget', helpstring(u'The Catalog object used internally by the Catalog window.')], HRESULT, 'InternalCatalog',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxCatalog)), 'Catalog' )),
    COMMETHOD(['propget', helpstring(u"The Catalog window's current view.")], HRESULT, 'View',
              ( ['retval', 'out'], POINTER(POINTER(IGxView)), 'View' )),
    COMMETHOD(['propget', helpstring(u"The Catalog window's current view's class ID.")], HRESULT, 'ViewClassID',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID)), 'ViewClassID' )),
    COMMETHOD(['propput', helpstring(u"The Catalog window's current view's class ID.")], HRESULT, 'ViewClassID',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID), 'ViewClassID' )),
    COMMETHOD(['propget', helpstring(u"The Catalog window's tree view.")], HRESULT, 'TreeView',
              ( ['retval', 'out'], POINTER(POINTER(IGxTreeView)), 'TreeView' )),
    COMMETHOD([helpstring(u'Shows or hides the Catalog window.')], HRESULT, 'Show',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentWindow' ),
              ( ['in'], VARIANT_BOOL, 'Show' )),
    COMMETHOD([helpstring(u'Instruct the Catalog window to destroy itself.')], HRESULT, 'Terminate'),
    COMMETHOD(['propget', helpstring(u'The HWND of the Catalog window.')], HRESULT, 'hWnd',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'pHwnd' )),
    COMMETHOD([helpstring(u'Refresh the Catalog window.')], HRESULT, 'Refresh'),
]
################################################################
## code template for IGxBrowser implementation
##class IGxBrowser_Impl(object):
##    def Show(self, parentWindow, Show):
##        u'Shows or hides the Catalog window.'
##        #return 
##
##    @property
##    def hWnd(self):
##        u'The HWND of the Catalog window.'
##        #return pHwnd
##
##    @property
##    def InternalCatalog(self):
##        u'The Catalog object used internally by the Catalog window.'
##        #return Catalog
##
##    def Terminate(self):
##        u'Instruct the Catalog window to destroy itself.'
##        #return 
##
##    def Refresh(self):
##        u'Refresh the Catalog window.'
##        #return 
##
##    def _get(self):
##        u"The Catalog window's current view's class ID."
##        #return ViewClassID
##    def _set(self, ViewClassID):
##        u"The Catalog window's current view's class ID."
##    ViewClassID = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def TreeView(self):
##        u"The Catalog window's tree view."
##        #return TreeView
##
##    @property
##    def View(self):
##        u"The Catalog window's current view."
##        #return View
##

class SDSServerDataSourcesPage(CoClass):
    u'Esri SDS Server Property Page.'
    _reg_clsid_ = GUID('{2942F53B-ACAB-4687-A515-331F0BA6D1F6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
SDSServerDataSourcesPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class GxKMLSOEPage(CoClass):
    u'KML SOE properties page.'
    _reg_clsid_ = GUID('{F2F7A0A5-EBAA-440D-972A-AA0BF7E821BB}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GxKMLSOEPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, IAGSSOEParameterPage, IAGSSOEParameterPage2]

class GxDialog(CoClass):
    u'Provides access to GX browser dialog.'
    _reg_clsid_ = GUID('{EAB9CE2A-E777-11D1-AEE7-080009EC734B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GxDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxDialog, comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxObjectFilterCollection, comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxSelectionEvents]

IGeographicCoordinateSystemDialog._methods_ = [
    COMMETHOD([helpstring(u'Prompts the user to define a new geographic coordinate system.')], HRESULT, 'DoModalCreate',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hParent' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeographicCoordinateSystem)), 'gcs' )),
]
################################################################
## code template for IGeographicCoordinateSystemDialog implementation
##class IGeographicCoordinateSystemDialog_Impl(object):
##    def DoModalCreate(self, hParent):
##        u'Prompts the user to define a new geographic coordinate system.'
##        #return gcs
##

class GxWFSSOEPage(CoClass):
    u'WFS SOE properties page.'
    _reg_clsid_ = GUID('{1BE48754-C1AB-4AE3-9532-65D6E28800E0}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GxWFSSOEPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, IAGSSOEParameterPage, IAGSSOEParameterPage2]

class IFileSystemQuery(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u"Provides access to members that manage the file system XML search engine's properties."
    _iid_ = GUID('{4EA3E4EC-9DFA-11D3-A6CB-0008C7D3AE50}')
    _idlflags_ = ['oleautomation']
IFileSystemQuery._methods_ = [
    COMMETHOD(['propget', helpstring(u'Starting location of a search.')], HRESULT, 'Location',
              ( ['retval', 'out'], POINTER(BSTR), 'Location' )),
    COMMETHOD(['propput', helpstring(u'Starting location of a search.')], HRESULT, 'Location',
              ( ['in'], BSTR, 'Location' )),
    COMMETHOD(['propget', helpstring(u'Indicates if subfolders will be searched.')], HRESULT, 'IncludeSubFolders',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IncludeSubFolders' )),
    COMMETHOD(['propput', helpstring(u'Indicates if subfolders will be searched.')], HRESULT, 'IncludeSubFolders',
              ( ['in'], VARIANT_BOOL, 'IncludeSubFolders' )),
]
################################################################
## code template for IFileSystemQuery implementation
##class IFileSystemQuery_Impl(object):
##    def _get(self):
##        u'Indicates if subfolders will be searched.'
##        #return IncludeSubFolders
##    def _set(self, IncludeSubFolders):
##        u'Indicates if subfolders will be searched.'
##    IncludeSubFolders = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Starting location of a search.'
##        #return Location
##    def _set(self, Location):
##        u'Starting location of a search.'
##    Location = property(_get, _set, doc = _set.__doc__)
##

ISpatialReferenceDialog3._methods_ = [
    COMMETHOD([helpstring(u'Prompts the user to define a new spatial reference.')], HRESULT, 'DoModalCreate3',
              ( ['in'], VARIANT_BOOL, 'hasZ' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hParent' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference)), 'SpatialReference' )),
    COMMETHOD([helpstring(u'Displays/edits the properties of the given spatial reference.')], HRESULT, 'DoModalEdit3',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference), 'inputSpatialReference' ),
              ( ['in'], VARIANT_BOOL, 'hasZ' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hParent' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference)), 'outputSpatialReference' )),
]
################################################################
## code template for ISpatialReferenceDialog3 implementation
##class ISpatialReferenceDialog3_Impl(object):
##    def DoModalEdit3(self, inputSpatialReference, hasZ, hParent):
##        u'Displays/edits the properties of the given spatial reference.'
##        #return outputSpatialReference
##
##    def DoModalCreate3(self, hasZ, hParent):
##        u'Prompts the user to define a new spatial reference.'
##        #return SpatialReference
##

class IFindDialogSettings(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control how the query appears in the Search dialog box.'
    _iid_ = GUID('{52E909BA-552E-4AE2-87E7-9ED84C703D1E}')
    _idlflags_ = ['oleautomation']
IFindDialogSettings._methods_ = [
    COMMETHOD(['propget', helpstring(u'Full name of the dataset to be used as the background map in the Geography tab.')], HRESULT, 'BackgroundMap',
              ( ['retval', 'out'], POINTER(BSTR), 'pBackgroundMap' )),
    COMMETHOD(['propput', helpstring(u'Full name of the dataset to be used as the background map in the Geography tab.')], HRESULT, 'BackgroundMap',
              ( ['in'], BSTR, 'pBackgroundMap' )),
]
################################################################
## code template for IFindDialogSettings implementation
##class IFindDialogSettings_Impl(object):
##    def _get(self):
##        u'Full name of the dataset to be used as the background map in the Geography tab.'
##        #return pBackgroundMap
##    def _set(self, pBackgroundMap):
##        u'Full name of the dataset to be used as the background map in the Geography tab.'
##    BackgroundMap = property(_get, _set, doc = _set.__doc__)
##

class AGSDiscoveryImageServerRFxPage(CoClass):
    u'Esri AGS Image Server Raster Functions Parameters Property Page.'
    _reg_clsid_ = GUID('{F8ADCAD3-B1EF-492E-8C57-A8A386A4B1F4}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSDiscoveryImageServerRFxPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class AGSDiscoveryMapParametersPage(CoClass):
    u'Esri AGS Map Service Parameters Property Page.'
    _reg_clsid_ = GUID('{0D095AF6-CB48-4CB8-BA7E-E6CA26ADE352}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSDiscoveryMapParametersPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class NetworkDirectionsGeneralPage(CoClass):
    u'Esri network directions general page.'
    _reg_clsid_ = GUID('{8F8BA427-4E0C-4275-A12C-81792246839A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
NetworkDirectionsGeneralPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class ProjectedCoordinateSystemDialog(CoClass):
    u'Projected Coordinate System Dialog.'
    _reg_clsid_ = GUID('{A38CB583-95CE-11D2-AD2A-00C04FA33A15}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
ProjectedCoordinateSystemDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IProjectedCoordinateSystemDialog]

class MetadataServiceEngine(CoClass):
    u'Metadata Service Search Engine.'
    _reg_clsid_ = GUID('{D40F0567-7ADE-480B-B77B-87DB16CB3D78}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
MetadataServiceEngine._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IConnectionPointContainer, ISearchEngine, ISearchEngineProperties]
MetadataServiceEngine._outgoing_interfaces_ = [ISearchEngineEvents]

class TableDefTolerancePage(CoClass):
    u'Esri feature class tolerance page.'
    _reg_clsid_ = GUID('{C77C9E17-9BAE-42BB-850C-7CBA31DBA9C3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
TableDefTolerancePage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class TableDefVerticalPage(CoClass):
    u'Esri feature class vertical page.'
    _reg_clsid_ = GUID('{46C0585D-26EF-48B5-AA32-56A76DD44039}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
TableDefVerticalPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, ICoordSysDetailsPage]

class ProjectedCoordSysPropPage(CoClass):
    u'Projected Coordinate System Property Page.'
    _reg_clsid_ = GUID('{92F6F58E-E21F-11D2-99C0-0000F80372B4}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
ProjectedCoordSysPropPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class TableDefDomainPage(CoClass):
    u'Esri feature class domain page.'
    _reg_clsid_ = GUID('{0BD4185C-18CF-4E8F-82BA-C77EE1038902}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
TableDefDomainPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class TableDefFieldsPage(CoClass):
    u'Esri table definition fields page.'
    _reg_clsid_ = GUID('{4D4B95A1-E153-11D2-99C0-0000F80372B4}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
class ITableDefFieldsPage(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Table Definition Fields Page.'
    _iid_ = GUID('{B8EB61D1-6223-11D3-9FF0-00C04F6BC626}')
    _idlflags_ = ['oleautomation']
TableDefFieldsPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, ITableDefFieldsPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

IEditEvaluatorContext._methods_ = [
    COMMETHOD(['propget', helpstring(u'The evaluator element type.')], HRESULT, 'ElementType',
              ( ['retval', 'out'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriNetworkElementType), 'ElementType' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether it is the default evaluator context.')], HRESULT, 'IsDefault',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'defaultMode' )),
    COMMETHOD(['propget', helpstring(u'The edge direction type.')], HRESULT, 'DirectionType',
              ( ['retval', 'out'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriNetworkEdgeDirection), 'DirectionType' )),
    COMMETHOD(['propget', helpstring(u'The evaluator network source.')], HRESULT, 'Source',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INetworkSource)), 'netSource' )),
    COMMETHOD(['propget', helpstring(u'The evaluator network source table.')], HRESULT, 'Table',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable)), 'Table' )),
]
################################################################
## code template for IEditEvaluatorContext implementation
##class IEditEvaluatorContext_Impl(object):
##    @property
##    def Source(self):
##        u'The evaluator network source.'
##        #return netSource
##
##    @property
##    def ElementType(self):
##        u'The evaluator element type.'
##        #return ElementType
##
##    @property
##    def DirectionType(self):
##        u'The edge direction type.'
##        #return DirectionType
##
##    @property
##    def IsDefault(self):
##        u'Indicates whether it is the default evaluator context.'
##        #return defaultMode
##
##    @property
##    def Table(self):
##        u'The evaluator network source table.'
##        #return Table
##

class GeographicCoordSysPropPage(CoClass):
    u'Geographic Coordinate System Property Page.'
    _reg_clsid_ = GUID('{92F6F58D-E21F-11D2-99C0-0000F80372B4}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GeographicCoordSysPropPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class ICreateRasterDatasetDlg(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods that control the dialog for creating a Raster dataset.'
    _iid_ = GUID('{40F59116-40C0-4CF1-830B-DCA136CC1C8F}')
    _idlflags_ = ['oleautomation']
ICreateRasterDatasetDlg._methods_ = [
    COMMETHOD([helpstring(u'Shows the raster dataset creation dialog.')], HRESULT, 'DoModal',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hParent' )),
    COMMETHOD(['propget', helpstring(u'The definition of the raster dataset.')], HRESULT, 'RasterDef',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRasterDef)), 'ppRasterDef' )),
    COMMETHOD(['propputref', helpstring(u'The definition of the raster dataset.')], HRESULT, 'RasterDef',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRasterDef), 'ppRasterDef' )),
    COMMETHOD(['propget', helpstring(u'The definition of the raster dataset storage.')], HRESULT, 'RasterStorageDef',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRasterStorageDef)), 'ppRasterStorageDef' )),
    COMMETHOD(['propputref', helpstring(u'The definition of the raster dataset storage.')], HRESULT, 'RasterStorageDef',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRasterStorageDef), 'ppRasterStorageDef' )),
    COMMETHOD(['propget', helpstring(u'The name of the raster dataset.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'ppName' )),
    COMMETHOD(['propput', helpstring(u'The name of the raster dataset.')], HRESULT, 'Name',
              ( ['in'], BSTR, 'ppName' )),
    COMMETHOD(['propget', helpstring(u'Number of bands of the raster dataset.')], HRESULT, 'Bands',
              ( ['retval', 'out'], POINTER(c_int), 'pBamds' )),
    COMMETHOD(['propput', helpstring(u'Number of bands of the raster dataset.')], HRESULT, 'Bands',
              ( ['in'], c_int, 'pBamds' )),
    COMMETHOD(['propget', helpstring(u'The pixel type of the raster dataset.')], HRESULT, 'PixelType',
              ( ['retval', 'out'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.rstPixelType), 'pPixelType' )),
    COMMETHOD(['propput', helpstring(u'The pixel type of the raster dataset.')], HRESULT, 'PixelType',
              ( ['in'], comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.rstPixelType, 'pPixelType' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether the enterprise Geodatabase is supported.')], HRESULT, 'SupportEnterprise',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
]
################################################################
## code template for ICreateRasterDatasetDlg implementation
##class ICreateRasterDatasetDlg_Impl(object):
##    def _set(self, rhs):
##        u'Indicates whether the enterprise Geodatabase is supported.'
##    SupportEnterprise = property(fset = _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The name of the raster dataset.'
##        #return ppName
##    def _set(self, ppName):
##        u'The name of the raster dataset.'
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The pixel type of the raster dataset.'
##        #return pPixelType
##    def _set(self, pPixelType):
##        u'The pixel type of the raster dataset.'
##    PixelType = property(_get, _set, doc = _set.__doc__)
##
##    def RasterDef(self, ppRasterDef):
##        u'The definition of the raster dataset.'
##        #return 
##
##    def _get(self):
##        u'Number of bands of the raster dataset.'
##        #return pBamds
##    def _set(self, pBamds):
##        u'Number of bands of the raster dataset.'
##    Bands = property(_get, _set, doc = _set.__doc__)
##
##    def DoModal(self, hParent):
##        u'Shows the raster dataset creation dialog.'
##        #return 
##
##    def RasterStorageDef(self, ppRasterStorageDef):
##        u'The definition of the raster dataset storage.'
##        #return 
##

class VerticalCoordinateSystemDialog(CoClass):
    u'Vertical Coordinate System Dialog.'
    _reg_clsid_ = GUID('{CD87BB70-AAFC-4ABE-89DE-EAEFD9EDA715}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
VerticalCoordinateSystemDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IVerticalCoordinateSystemDialog]

class ITableDefinitionDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Table Definition Dialog.'
    _iid_ = GUID('{5DBEDE6B-4CDE-11D2-AAD2-00C04FA33A15}')
    _idlflags_ = ['oleautomation']
ITableDefinitionDialog._methods_ = [
    COMMETHOD([helpstring(u'Displays the dialog to define a new table.')], HRESULT, 'DoModalCreateTable',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureWorkspace), 'workspace' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hParent' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable)), 'Table' )),
    COMMETHOD([helpstring(u'Displays the dialog to define a new feature class.')], HRESULT, 'DoModalCreateFeatureClass',
              ( ['in'], POINTER(IUnknown), 'Parent' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hParent' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass)), 'featureClass' )),
]
################################################################
## code template for ITableDefinitionDialog implementation
##class ITableDefinitionDialog_Impl(object):
##    def DoModalCreateFeatureClass(self, Parent, hParent):
##        u'Displays the dialog to define a new feature class.'
##        #return featureClass
##
##    def DoModalCreateTable(self, workspace, hParent):
##        u'Displays the dialog to define a new table.'
##        #return Table
##


# values for enumeration 'esriTableDefFieldsPageContext'
esriFieldsPageTable = 0
esriFieldsPageFeatureClass = 1
esriFieldsPageRelationshipClass = 2
esriTableDefFieldsPageContext = c_int # enum
ITableDefFieldsPage._methods_ = [
    COMMETHOD(['propput', helpstring(u'The context of the property page.')], HRESULT, 'PageContext',
              ( ['in'], esriTableDefFieldsPageContext, 'rhs' )),
    COMMETHOD(['propputref', helpstring(u'The workspace domains property.')], HRESULT, 'WorkspaceDomains',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceDomains), 'rhs' )),
    COMMETHOD(['propget', helpstring(u'The fields specified in the property page.')], HRESULT, 'Fields',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFields)), 'Fields' )),
    COMMETHOD([helpstring(u'Notifies the property page that the Next button on the wizard has been selected.')], HRESULT, 'WizardNext'),
    COMMETHOD([helpstring(u'Notifies the property page when it becomes active.')], HRESULT, 'OnSetActive'),
]
################################################################
## code template for ITableDefFieldsPage implementation
##class ITableDefFieldsPage_Impl(object):
##    def WizardNext(self):
##        u'Notifies the property page that the Next button on the wizard has been selected.'
##        #return 
##
##    @property
##    def Fields(self):
##        u'The fields specified in the property page.'
##        #return Fields
##
##    def WorkspaceDomains(self, rhs):
##        u'The workspace domains property.'
##        #return 
##
##    def OnSetActive(self):
##        u'Notifies the property page when it becomes active.'
##        #return 
##
##    def _set(self, rhs):
##        u'The context of the property page.'
##    PageContext = property(fset = _set, doc = _set.__doc__)
##

IAGSPublishToolboxAdminDialog._methods_ = [
    COMMETHOD([helpstring(u'Displays the dialog to publish a toolbox.')], HRESULT, 'DoModalPublish',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hParent' ),
              ( ['in'], POINTER(comtypes.gen._C031A050_82C6_4F8F_8836_5692631CFFE6_0_10_2.IGPToolbox), 'pGpToolbox' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pSuccess' )),
]
################################################################
## code template for IAGSPublishToolboxAdminDialog implementation
##class IAGSPublishToolboxAdminDialog_Impl(object):
##    def DoModalPublish(self, hParent, pGpToolbox):
##        u'Displays the dialog to publish a toolbox.'
##        #return pSuccess
##

class GxDataGraphView(CoClass):
    u'GxView that represents the data graph contents view.'
    _reg_clsid_ = GUID('{B14315A8-098A-11D4-A676-0008C7DF88DB}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GxDataGraphView._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxView, comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxSelectionEvents, comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxCatalogEvents]

IAGSObjectAdminDialog2._methods_ = [
    COMMETHOD([helpstring(u'Displays the dialog to create a new service object.')], HRESULT, 'DoModalCreateService',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hParent' ),
              ( ['in'], POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IAGSServerConnectionName), 'pServerConnName' ),
              ( ['in'], BSTR, 'folderName' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IAGSObjectCreationProperties)), 'ppProps' )),
]
################################################################
## code template for IAGSObjectAdminDialog2 implementation
##class IAGSObjectAdminDialog2_Impl(object):
##    def DoModalCreateService(self, hParent, pServerConnName, folderName):
##        u'Displays the dialog to create a new service object.'
##        #return ppProps
##

class NetworkDirectionsRoadDetailPage(CoClass):
    u'Esri network directions road detail page.'
    _reg_clsid_ = GUID('{8247138A-D1A2-42F4-B0F5-929292110696}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
NetworkDirectionsRoadDetailPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

IAGSParameterPage._methods_ = [
    COMMETHOD(['propget', helpstring(u'The Server Object Type.')], HRESULT, 'ServerObjectType',
              ( ['retval', 'out'], POINTER(BSTR), 'ServerObjectType' )),
    COMMETHOD(['propget', helpstring(u'The parameter page description.')], HRESULT, 'Description',
              ( ['retval', 'out'], POINTER(BSTR), 'desc' )),
    COMMETHOD(['propput', helpstring(u'Initialize the wizard mode the selected parameter page.')], HRESULT, 'IsWizard',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Initialize the server object configuration of the selected parameter page.')], HRESULT, 'ServerObjectConfiguration',
              ( ['in'], POINTER(comtypes.gen._18F2FC71_6B30_45B9_B101_037A8B868B66_0_10_2.IServerObjectConfiguration), 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Initialize the server directories the selected parameter page.')], HRESULT, 'ServerDirectories',
              ( ['in'], POINTER(comtypes.gen._18F2FC71_6B30_45B9_B101_037A8B868B66_0_10_2.IEnumServerDirectory), 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Initialize the server object name the selected parameter page.')], HRESULT, 'ServerObjectName',
              ( ['in'], POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IAGSServerObjectName), 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Initialize the SOM of the parameter page.')], HRESULT, 'SOM',
              ( ['in'], POINTER(comtypes.gen._18F2FC71_6B30_45B9_B101_037A8B868B66_0_10_2.IServerObjectAdmin), 'rhs' )),
    COMMETHOD([helpstring(u'Initialize the selected parameter page.')], HRESULT, 'UpdatePage'),
    COMMETHOD([helpstring(u'Upate this page before go next.')], HRESULT, 'QueryPage',
              ( ['in'], VARIANT_BOOL, 'commitApply' )),
    COMMETHOD([helpstring(u'Refresh the read/page status of controls.')], HRESULT, 'RefreshPage'),
    COMMETHOD([helpstring(u'Close the selected parameter page.')], HRESULT, 'ClosePage'),
]
################################################################
## code template for IAGSParameterPage implementation
##class IAGSParameterPage_Impl(object):
##    def RefreshPage(self):
##        u'Refresh the read/page status of controls.'
##        #return 
##
##    @property
##    def Description(self):
##        u'The parameter page description.'
##        #return desc
##
##    @property
##    def ServerObjectType(self):
##        u'The Server Object Type.'
##        #return ServerObjectType
##
##    def QueryPage(self, commitApply):
##        u'Upate this page before go next.'
##        #return 
##
##    def ClosePage(self):
##        u'Close the selected parameter page.'
##        #return 
##
##    def _set(self, rhs):
##        u'Initialize the SOM of the parameter page.'
##    SOM = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Initialize the server object configuration of the selected parameter page.'
##    ServerObjectConfiguration = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Initialize the server object name the selected parameter page.'
##    ServerObjectName = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Initialize the server directories the selected parameter page.'
##    ServerDirectories = property(fset = _set, doc = _set.__doc__)
##
##    def UpdatePage(self):
##        u'Initialize the selected parameter page.'
##        #return 
##
##    def _set(self, rhs):
##        u'Initialize the wizard mode the selected parameter page.'
##    IsWizard = property(fset = _set, doc = _set.__doc__)
##

class AGSDiscoveryImageCatalogPage(CoClass):
    u'Esri AGS Image Catalog Parameters Property Page.'
    _reg_clsid_ = GUID('{A3D46959-CF28-47FA-BCB8-BA69D1DFA56A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
AGSDiscoveryImageCatalogPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class TableDefinitionDialog(CoClass):
    u'Dialog to define/edit table/feature class definitions.'
    _reg_clsid_ = GUID('{5DBEDE6C-4CDE-11D2-AAD2-00C04FA33A15}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
TableDefinitionDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ITableDefinitionDialog]

class GxRasterCatalogContentView(CoClass):
    u'The RasterCatalog content view.'
    _reg_clsid_ = GUID('{0B0BA0E2-C445-4E2D-B57B-D3431AFE015D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GxRasterCatalogContentView._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxView, IGxPreview, comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxSelectionEvents, comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxCatalogEvents, IGxContentsView, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IObjectClassEvents, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IObjectClassSchemaEvents]

class NetworkDatasetDialog(CoClass):
    u'Dialogs for creating and editing network datasets.'
    _reg_clsid_ = GUID('{1DC92901-ED5B-41BC-ACCA-B5E1B6DFC0F9}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
NetworkDatasetDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, INetworkDatasetDialog]

class TableDefNamePage(CoClass):
    u'Esri table definition name page.'
    _reg_clsid_ = GUID('{4D4B95A2-E153-11D2-99C0-0000F80372B4}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
TableDefNamePage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class GxMSDFile(CoClass):
    u'A MapServerDefinitionFile Dataset.'
    _reg_clsid_ = GUID('{D7AFA39D-4A05-4055-89F0-AB3DECF6E79B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
class IGxMSDFile(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Indicator interface that identifies a GxObject that corresponds to an MSDFile document.'
    _iid_ = GUID('{C5472018-4A88-4331-9C2D-CE5CF3E805A5}')
    _idlflags_ = ['oleautomation']
GxMSDFile._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGxMSDFile, comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxObject, comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxObjectUI, comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxObjectEdit, comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxObjectProperties, comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxFile, comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxCachedObjects, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxThumbnail, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IObjectClassSchemaEvents, comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxObjectInternalName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxDataElement, comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxDataElementHelper]

class GxItemIndexer(CoClass):
    u'Provides access to members of GxIndexer.'
    _reg_clsid_ = GUID('{6305F6DF-0CC5-43C7-A8DD-49FF080D00A1}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GxItemIndexer._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._E418C392_C3A6_4EB2_8870_001ABAE6B5B4_0_10_2.IItemIndexer, IGxItemIndexer]

class IGxAddOGCConnectionDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Add OGC Connection Dialog.'
    _iid_ = GUID('{7AF6CFB5-CC47-4EC0-9DB2-0671CC2C9B08}')
    _idlflags_ = ['oleautomation']
IGxAddOGCConnectionDialog._methods_ = [
    COMMETHOD([helpstring(u'Displays the dialog to create a new WMS server connection.')], HRESULT, 'DoModalCreateWMSConnection',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hParent' ),
              ( ['in', 'out'], POINTER(VARIANT), 'selectedResources' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IWMSConnection)), 'ppWMSConnection' )),
    COMMETHOD([helpstring(u'Displays the dialog to create a new WCS server connection.')], HRESULT, 'DoModalCreateWCSConnection',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hParent' ),
              ( ['in', 'out'], POINTER(VARIANT), 'selectedResources' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IWCSConnection)), 'ppWCSConnection' )),
]
################################################################
## code template for IGxAddOGCConnectionDialog implementation
##class IGxAddOGCConnectionDialog_Impl(object):
##    def DoModalCreateWMSConnection(self, hParent):
##        u'Displays the dialog to create a new WMS server connection.'
##        #return selectedResources, ppWMSConnection
##
##    def DoModalCreateWCSConnection(self, hParent):
##        u'Displays the dialog to create a new WCS server connection.'
##        #return selectedResources, ppWCSConnection
##

IAGSConnectionAdminDialog._methods_ = [
    COMMETHOD([helpstring(u'Displays the dialog to create a new server connection.')], HRESULT, 'DoModalCreateServerConnection',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hParent' ),
              ( ['in', 'out'], POINTER(VARIANT), 'selectedResources' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IAGSServerConnection)), 'ppServerConnection' )),
    COMMETHOD([helpstring(u'Displays the dialog to update an existing server connection.')], HRESULT, 'DoModalUpdateServerConnection',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hParent' ),
              ( ['in', 'out'], POINTER(VARIANT), 'selectedResources' ),
              ( ['in', 'out'], POINTER(POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxAGSConnection)), 'ppGxAGSConn' )),
]
################################################################
## code template for IAGSConnectionAdminDialog implementation
##class IAGSConnectionAdminDialog_Impl(object):
##    def DoModalCreateServerConnection(self, hParent):
##        u'Displays the dialog to create a new server connection.'
##        #return selectedResources, ppServerConnection
##
##    def DoModalUpdateServerConnection(self, hParent):
##        u'Displays the dialog to update an existing server connection.'
##        #return selectedResources, ppGxAGSConn
##

IGxMSDFile._methods_ = [
]
################################################################
## code template for IGxMSDFile implementation
##class IGxMSDFile_Impl(object):

class FindDialog(CoClass):
    u'The Search dialog box.'
    _reg_clsid_ = GUID('{AD0B37A9-D396-11D3-A6F3-0008C7D3AE50}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
FindDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IFindDialog, ISearchEngineEvents, comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxSelectionEvents, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IDllThreadManager]

class DomainsPropertyPage(CoClass):
    u'Esri workspace domains property page.'
    _reg_clsid_ = GUID('{C255D345-CB5C-11D2-9F3C-00C04F6BC626}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
DomainsPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class GxMSDFileContextMenu(CoClass):
    u' Context Menu.'
    _reg_clsid_ = GUID('{C61FE9E2-28E1-4FFC-B84C-3021E4E03317}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
GxMSDFileContextMenu._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IMenuDef, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IShortcutMenu]


# values for enumeration 'esriAGSServiceWebAccessStatus'
esriCSWAEnabled = 0
esriCSWADisabled = 1
esriAGSServiceWebAccessStatus = c_int # enum
ICoordSysDetailsPage._methods_ = [
    COMMETHOD(['propget', helpstring(u'The related spatial refrence.')], HRESULT, 'SpatialReference',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference)), 'ppStpaialReference' )),
    COMMETHOD(['propget', helpstring(u'The coordinate system context.')], HRESULT, 'CoordSysContext',
              ( ['retval', 'out'], POINTER(esriCoordSysContext), 'CoordSysContext' )),
    COMMETHOD(['propput', helpstring(u'The coordinate system context.')], HRESULT, 'CoordSysContext',
              ( ['in'], esriCoordSysContext, 'CoordSysContext' )),
    COMMETHOD(['propget', helpstring(u'The vertical coordinate system.')], HRESULT, 'VerticalCoordinateSystem',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IVerticalCoordinateSystem)), 'ppVCS' )),
]
################################################################
## code template for ICoordSysDetailsPage implementation
##class ICoordSysDetailsPage_Impl(object):
##    def _get(self):
##        u'The coordinate system context.'
##        #return CoordSysContext
##    def _set(self, CoordSysContext):
##        u'The coordinate system context.'
##    CoordSysContext = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def VerticalCoordinateSystem(self):
##        u'The vertical coordinate system.'
##        #return ppVCS
##
##    @property
##    def SpatialReference(self):
##        u'The related spatial refrence.'
##        #return ppStpaialReference
##

class FileSystemQuery(CoClass):
    u'A query that can be used to search XML documents.'
    _reg_clsid_ = GUID('{4EA3E4EA-9DFA-11D3-A6CB-0008C7D3AE50}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
FileSystemQuery._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IQuery, IXmlQuery, IArcIMSQuery, IFindDialogSettings]

IGxRasterCatalogSubView._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates whether the multiple selection is supported.')], HRESULT, 'SupportMultiSelection',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
]
################################################################
## code template for IGxRasterCatalogSubView implementation
##class IGxRasterCatalogSubView_Impl(object):
##    @property
##    def SupportMultiSelection(self):
##        u'Indicates whether the multiple selection is supported.'
##        #return pVal
##

class FileSystemXmlSearchEngine(CoClass):
    u'A search engine that looks on the file system for XML files that match the search criteria.'
    _reg_clsid_ = GUID('{D18306A4-9D3C-11D3-A6CB-0008C7D3AE50}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
FileSystemXmlSearchEngine._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ISearchEngine, ISearchEngineProperties, IFileSystemQuery, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IConnectionPointContainer]
FileSystemXmlSearchEngine._outgoing_interfaces_ = [ISearchEngineEvents]

class CatalogSearchEngine(CoClass):
    u'A search engine that looks in the Catalog for objects that match the search criteria.'
    _reg_clsid_ = GUID('{2D9E0A39-9BCD-4313-9452-4C5E35318E7A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C0FC1503-7E6F-11D2-AABF-00C04FA375F1}', 10, 2)
CatalogSearchEngine._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ISearchEngine, ISearchEngineProperties, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IConnectionPointContainer]
CatalogSearchEngine._outgoing_interfaces_ = [ISearchEngineEvents]

__all__ = ['EditEvaluatorContext', 'GeographicCoordinateSystemDialog',
           'FindDialog', 'VerticalCoordSysPropPage',
           'GeneralRelationshipClassPropertyPage',
           'AGSDiscoveryGeocodeParametersPage', 'IMetadataEvents',
           'GxComBrowser', 'IGxDocumentationView',
           'ProjectedCoordinateSystemDialog', 'esriCoordSystemNone',
           'AGSGeneralPage', 'IGxMSDFileView', 'QueryTableDialog',
           'AGSDiscoveryProcessPage', 'IGxPreview',
           'ITableDefinitionDialog', 'AGSServerClustersPage',
           'IGxViewContainer', 'IAttributesEditContext', 'AGSSOEPage',
           'FeatureClassRepresentationsPage',
           'INetworkElevationConfiguration', 'GxTableView',
           'IMetadataHelper', 'INetworkDatasetDialog',
           'IGxAddOGCConnectionDialog', 'IGxObjectEnumerator',
           'GxMSDFilePropPage', 'GxFeatureAccessSOEPage',
           'GxWPSSOEPage', 'esriContentsViewStyle', 'IDataAdder',
           'AddAGSFolderPage', 'IEditEvaluatorContext',
           'IGxRasterCatalogSubView', 'ISearchEngineProperties',
           'GxItemInfoHelper', 'CovGeneralPage',
           'AddAGSDiscoveryUserConnectionPage',
           'NetworkGlobalTurnDelayEvaluatorEditor',
           'AGSDiscoveryMapParametersPage',
           'AGSGeoDataServerParameterPage', 'IAGSObjectAdminDialog2',
           'GxMSDFileFactory', 'IRelationshipClassDialog',
           'AGSDiscoveryGeneralPage', 'IRepairMosaicDatasetDialog',
           'TableDefViewDescPage', 'FeatureExtentPage',
           'AGSDiscoveryGlobeParametersPage', 'IFileSystemQuery',
           'INetworkAttributeConfiguration', 'TableDefDomainPage',
           'EnableGeodatabaseMenuItem', 'AGSConnectionAdminDialog',
           'IAGSParameterPage', 'IGxGeographicView',
           'FileSystemQuery', 'GxRasterCatalogSubPropertyView',
           'FeatureServerObjectPropPage',
           'IAGSPublishToolboxAdminDialog', 'IGxTreeView',
           'IAGSSOEParameterPage', 'CovProjectPage', 'IGxDialog',
           'INetworkDirectionConfiguration3',
           'INetworkDirectionConfiguration2', 'IGxMSDFile',
           'ISpatialReferenceDialog', 'GxMSDFileView',
           'esriTableDefFieldsPageContext', 'esriCoordSysContext',
           'esriAGSServiceWebAccessStatus',
           'INetworkElevationConfiguration2',
           'AGSPublishToolboxDialog', 'GxContentsViewPage',
           'Pre70CoveragePropertyPage', 'DataAdder',
           'IGxGeographicView2', 'IGxBrowser',
           'GxHomeFolderOptionsPage', 'GxKMLSOEPage',
           'SDSServerDataSourcesPage', 'IGxTableView2',
           'GxBrowserDockWindow', 'AGSGeocodeParameterPage',
           'IEvaluatorEditor', 'AGSDiscoveryImageParametersPage',
           'INetworkTrafficConfiguration', 'IMetadataEditor',
           'IEnumGxView', 'FileSystemXmlSearchEngine',
           'IGxContentsViewColumns', 'GeocodeServerObjectPropPage',
           'AGSDiscoverySearchParametersPage', 'IGxTableView',
           'CreateRasterCatalogWizard', 'IGxItemInfoHelper',
           'NetworkDatasetDialog', 'AGSParameterPagesContainer',
           'INetworkAttributeConfiguration2',
           'INetworkAttributeConfiguration3',
           'AGSDiscoveryGeoDataParametersPage', 'GxDataGraphView',
           'AGSServerStatisticsPage', 'TableDefVerticalPage',
           'AGSDiscoveryImageCachingGeneralPage', 'AddAGSServerPage',
           'TableDefEditorTrackingPage', 'EnumGxView',
           'InfoTableGeneralPage', 'AGSDiscoveryImageServerRFxPage',
           'GxDocumentationViewWindow',
           'AGSDiscoveryCachingGeneralPage',
           'MapServerObjectPropPage',
           'AGSDiscoveryImageTilingSchemePage', 'RasterCoordSysPage',
           'AGSObjectAdminDialog', 'GxFilterMSDFiles',
           'GeoDBAdminPropertyPage', 'AGSDiscoveryImageCatalogPage',
           'IDataFrameShapeDialog',
           'GeneralDatabaseServerPropertyPage', 'IGxApplication',
           'ProjectedCoordSysPropPage',
           'GeoprocessingServerObjectPropPage', 'IGxItemIndexer',
           'AGSServerLogSettingsPage',
           'DomainResolutionTolerancePage', 'IQueryTableDialog',
           'esriCVSDetails', 'ISearchEngineEvents',
           'NetworkDirectionsLandmarksPage',
           'NetworkDirectionsGeneralPage', 'AddAGSDialog',
           'SpatialReferenceDialog',
           'WorkspaceEditorTrackingPropertyPage',
           'AGSGeometryParameterPage', 'IDocumentDatasets',
           'IDataFrameShapeDialog2', 'GxContentsViewColumn',
           'TableDefCoordPage', 'esriCVSList', 'IDescriptionWindow',
           'AGSServerDirsPage', 'GxWFSSOEPage', 'GxDocumentationView',
           'InfoItemsPage', 'SearchServerObjectPropPage',
           'AttributesEditContext', 'GxMSDFile',
           'AGSDiscoveryPoolingPage', 'AddAGSConnectionPage',
           'esriCoordSystemZ', 'TableDefFieldsPage',
           'AddAGSDiscoveryConnectionPage',
           'NetworkScriptEvaluatorEditor',
           'GeoDataServerObjectPropPage',
           'GeometryServerObjectPropPage',
           'esriSpatialReferenceXYFilter', 'INetworkConfiguration',
           'IGeographicCoordinateSystemDialog',
           'AGSDiscoveryImageCatalogEditingPage', 'ISearchEngine',
           'GxGeographicView', 'GxWCSSOEPage',
           'GxSqlDatabaseAdminMenu', 'esriCSWAEnabled',
           'CreateManageRoleMenuItem', 'IGxApplicationEvents',
           'CoordSysDetailsPage', 'IAGSSOEParameterPage2',
           'IAGSSOEParameterPage3', 'AGSGeoprocessingParameterPage',
           'ISDEditorPropertyPage', 'ResolutionPage',
           'SubtypesPropertyPage', 'AGSDiscoveryArcGISOnlinePage',
           'CatalogSearchEngine', 'IFindDialog',
           'AGSDiscoveryGlobeCachingPage', 'IGxView',
           'AGSNewCachingPage', 'FeatureDatasetDefDialog',
           'AGSServerConfigStorePage', 'AGSMapParameterPage',
           'GxShapefileIndexPage', 'NetworkConfiguration',
           'IVerticalCoordinateSystemDialog', 'LocalCachePage',
           'AddAGSDiscoveryDialog', 'FeatureDatasetDialog',
           'esriShowBoth', 'VerticalCoordinateSystemDialog',
           'GxNASOEPage', 'GxContentsView', 'GxPreview',
           'AGSDiscoveryCapabilityDetailsPage', 'AGSServerHostsPage',
           'TableDefNamePage', 'ISpatialReferenceDialogContext',
           'GxRasterCatalogContentView', 'DescriptionWindow',
           'GeographicCoordSysPropPage', 'IGxContentsViewColumn',
           'GxFileFilterDefinitionPage', 'GxMSDFileContextMenu',
           'esriCVSThumbnails', 'CovFCGeneralPage', 'GxTreeView',
           'TableDefRelationshipsPage',
           'NetworkEdgeTrafficEvaluatorEditor',
           'RelationshipRulesPage', 'ISpatialReferenceDialog2',
           'ISpatialReferenceDialog3',
           'AGSDiscoveryItemDescriptionPage', 'TableIndexPage',
           'ICreateRasterCatalogWizard',
           'NetworkFieldEvaluatorEditor', 'DomainsPropertyPage',
           'ProxyServerPage', 'NetworkConstantEvaluatorEditor',
           'GxAddOleDBConnectionCommand', 'esriCoordSystemRaster',
           'XYCoordSysPage', 'NetworkDirectionsRoadDetailPage',
           'ICreateRasterDatasetDlg', 'NetworkDirectionsShieldsPage',
           'GlobeServerObjectPropPage', 'IXmlQuery',
           'esriFieldsPageRelationshipClass', 'IArcIMSQuery',
           'esriFieldsPageFeatureClass',
           'INetworkTrafficConfiguration2',
           'AGSDiscoveryAdvancedCacheSettingsPage',
           'MetadataExtension', 'ITableDefFieldsPage',
           'ICoordSysDetailsPage', 'GxServiceWorkspacesMenuItem',
           'esriFieldsPageTable', 'GxPackagePropPage', 'GxDialog',
           'AGSSearchServerParameterPage', 'esriCVSLargeIcons',
           'ZCoordSysPage', 'IFeatureDatasetDialog',
           'IAGSConnectionAdminDialog',
           'IProjectedCoordinateSystemDialog', 'GxMapSOPage',
           'AGSServerDataStoresPage', 'GxObjectVisibilityPage',
           'AGSServerTypesPage', 'esriCoordSystemXY',
           'MetadataServiceEngine', 'RelationshipClassDialog',
           'TableDefinitionDialog', 'IGxDocumentationViewWindow',
           'FeatDSNamePage', 'FeatDSSpaRefPage',
           'NetworkFunctionEvaluatorEditor', 'esriShowOnlyGeographic',
           'AGSImageParameterPage', 'GxAGSFolderPropertyPage',
           'AGSDiscoveryImageMensurationPage',
           'esriShowOnlyProjected', 'INetworkDirectionConfiguration',
           'GxWMSSOEPage', 'TableDefWeightsPage',
           'IAGSObjectAdminDialog', 'IEditEvaluators',
           'EditEvaluators', 'IGxContentsView',
           'AGSDiscoveryCapabilityGeneralPage', 'GxItemIndexer',
           'TableDefTolerancePage', 'esriCSWADisabled',
           'IFindDialogSettings', 'IGxViewPrint', 'AddUserMenuItem']
from comtypes import _check_version; _check_version('501')

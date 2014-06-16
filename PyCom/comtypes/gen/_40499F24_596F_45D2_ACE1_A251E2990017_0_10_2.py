# -*- coding: mbcs -*-
typelib_path = 'C:\\Program Files (x86)\\ArcGIS\\Desktop10.2\\com\\esriArcMapUI.olb'
_lcid = 0 # change this if required
from ctypes import *
from comtypes import GUID
from comtypes import CoClass
import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0
import comtypes.gen._D92377DC_FAB1_4DFB_A4C1_61BD8C40DBEB_0_10_2
import comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2
from comtypes.automation import IDispatch
from ctypes import HRESULT
from ctypes.wintypes import VARIANT_BOOL
from comtypes import helpstring
from comtypes import COMMETHOD
from comtypes import dispid
import comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2
import comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2
import comtypes.gen._4A9C9ED7_F7DB_4614_B480_A5D265C961FC_0_10_2
import comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2
from comtypes.automation import VARIANT
from comtypes import BSTR
import comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2
import comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2
from comtypes import IUnknown
import comtypes.gen._7DB92CEC_CB65_420A_8737_FCD0722FD436_0_10_2
import comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2
import comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2
import comtypes.gen._C0FC1503_7E6F_11D2_AABF_00C04FA375F1_0_10_2
import comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2


class AVImageThemeImporter(CoClass):
    u'A mechanism for importing image themes from Arc View 3.x into ArcGIS.'
    _reg_clsid_ = GUID('{B7DD8329-E649-11D3-9FD8-00C04F6BC78E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
AVImageThemeImporter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._D92377DC_FAB1_4DFB_A4C1_61BD8C40DBEB_0_10_2.IAVThemeImporter]

class IDataWindow(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control popup windows that show map data.'
    _iid_ = GUID('{04DBD416-AEE2-11D1-8750-0000F8751720}')
    _idlflags_ = ['oleautomation']
class ITableWindow(IDataWindow):
    _case_insensitive_ = True
    u"Provides access to members that display table window in ArcMap. This interface intergrates ITableView with ArcMap's events and selections."
    _iid_ = GUID('{4519EAF6-1A9C-11D2-A06C-0000F8775BF9}')
    _idlflags_ = ['oleautomation']
IDataWindow._methods_ = [
    COMMETHOD(['propputref', helpstring(u'Provides the window with a reference to the application.')], HRESULT, 'Application',
              ( ['in'], POINTER(IDispatch), 'rhs' )),
    COMMETHOD(['propget', helpstring(u"The window's handle.")], HRESULT, 'hWnd',
              ( ['retval', 'out'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.OLE_HANDLE), 'hWnd' )),
    COMMETHOD([helpstring(u"The window's position in screen pixels.")], HRESULT, 'QueryPosition',
              ( ['out'], POINTER(c_int), 'left' ),
              ( ['out'], POINTER(c_int), 'top' ),
              ( ['out'], POINTER(c_int), 'right' ),
              ( ['out'], POINTER(c_int), 'bottom' )),
    COMMETHOD([helpstring(u"The window's position in screen pixels.")], HRESULT, 'PutPosition',
              ( ['in'], c_int, 'left' ),
              ( ['in'], c_int, 'top' ),
              ( ['in'], c_int, 'right' ),
              ( ['in'], c_int, 'bottom' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the window is visible.')], HRESULT, 'IsVisible',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsVisible' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the window is dockable.')], HRESULT, 'IsDockable',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsVisible' )),
    COMMETHOD([helpstring(u'Indicates if the window is shown.')], HRESULT, 'Show',
              ( ['in'], VARIANT_BOOL, 'Show' )),
    COMMETHOD([helpstring(u'Cause the window to redraw.')], HRESULT, 'Refresh'),
]
################################################################
## code template for IDataWindow implementation
##class IDataWindow_Impl(object):
##    @property
##    def hWnd(self):
##        u"The window's handle."
##        #return hWnd
##
##    def Show(self, Show):
##        u'Indicates if the window is shown.'
##        #return 
##
##    def PutPosition(self, left, top, right, bottom):
##        u"The window's position in screen pixels."
##        #return 
##
##    @property
##    def IsDockable(self):
##        u'Indicates if the window is dockable.'
##        #return IsVisible
##
##    def Refresh(self):
##        u'Cause the window to redraw.'
##        #return 
##
##    def QueryPosition(self):
##        u"The window's position in screen pixels."
##        #return left, top, right, bottom
##
##    def Application(self, rhs):
##        u'Provides the window with a reference to the application.'
##        #return 
##
##    @property
##    def IsVisible(self):
##        u'Indicates if the window is visible.'
##        #return IsVisible
##

ITableWindow._methods_ = [
    COMMETHOD(['propputref', helpstring(u'Setup table to view/edit.')], HRESULT, 'Table',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable), 'ppTable' )),
    COMMETHOD(['propget', helpstring(u'Setup table to view/edit.')], HRESULT, 'Table',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable)), 'ppTable' )),
    COMMETHOD(['propputref', helpstring(u'Setup feature class to view/edit.')], HRESULT, 'FeatureLayer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IFeatureLayer), 'ppFeatureLayer' )),
    COMMETHOD(['propget', helpstring(u'Setup feature class to view/edit.')], HRESULT, 'FeatureLayer',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IFeatureLayer)), 'ppFeatureLayer' )),
    COMMETHOD(['propput', helpstring(u'Action to perform when table selections are made.')], HRESULT, 'TableSelectionAction',
              ( ['in'], comtypes.gen._4A9C9ED7_F7DB_4614_B480_A5D265C961FC_0_10_2.esriTableSelectionActions, 'pAction' )),
    COMMETHOD(['propget', helpstring(u'Action to perform when table selections are made.')], HRESULT, 'TableSelectionAction',
              ( ['retval', 'out'], POINTER(comtypes.gen._4A9C9ED7_F7DB_4614_B480_A5D265C961FC_0_10_2.esriTableSelectionActions), 'pAction' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether to show only features that are selected.')], HRESULT, 'ShowSelected',
              ( ['in'], VARIANT_BOOL, 'pShowSelected' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether to show only features that are selected.')], HRESULT, 'ShowSelected',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pShowSelected' )),
    COMMETHOD([helpstring(u'Is table (of a featurelayer) already being displayed.')], HRESULT, 'FindViaFeatureLayer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IFeatureLayer), 'pFeatureLayer' ),
              ( ['in'], VARIANT_BOOL, 'ShowSelected' ),
              ( ['retval', 'out'], POINTER(POINTER(ITableWindow)), 'ppTableWindow' )),
    COMMETHOD([helpstring(u'Is table already being displayed.')], HRESULT, 'FindViaTable',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable), 'pTable' ),
              ( ['in'], VARIANT_BOOL, 'ShowSelected' ),
              ( ['retval', 'out'], POINTER(POINTER(ITableWindow)), 'ppTableWindow' )),
    COMMETHOD(['propget', helpstring(u'Current s1election set of the table. Only valid for tables showing all rows.')], HRESULT, 'SelectionSet',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ISelectionSet)), 'ppSelectionSet' )),
    COMMETHOD([helpstring(u'Updates current table selection. Does not update Mx feature layer selection.')], HRESULT, 'UpdateSelection',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ISelectionSet), 'pSelection' )),
    COMMETHOD(['propput', helpstring(u'Show alias names or the real field name in column headings. Default False.')], HRESULT, 'ShowAliasNamesInColumnHeadings',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD(['propget', helpstring(u'The table control. Table needs to be showing before you can get a valid pointer.')], HRESULT, 'TableControl',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._4A9C9ED7_F7DB_4614_B480_A5D265C961FC_0_10_2.ITableControl)), 'ppTableControl' )),
]
################################################################
## code template for ITableWindow implementation
##class ITableWindow_Impl(object):
##    def _get(self):
##        u'Action to perform when table selections are made.'
##        #return pAction
##    def _set(self, pAction):
##        u'Action to perform when table selections are made.'
##    TableSelectionAction = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def FeatureLayer(self, ppFeatureLayer):
##        u'Setup feature class to view/edit.'
##        #return 
##
##    @property
##    def TableControl(self):
##        u'The table control. Table needs to be showing before you can get a valid pointer.'
##        #return ppTableControl
##
##    def _get(self):
##        u'Indicates whether to show only features that are selected.'
##        #return pShowSelected
##    def _set(self, pShowSelected):
##        u'Indicates whether to show only features that are selected.'
##    ShowSelected = property(_get, _set, doc = _set.__doc__)
##
##    def FindViaFeatureLayer(self, pFeatureLayer, ShowSelected):
##        u'Is table (of a featurelayer) already being displayed.'
##        #return ppTableWindow
##
##    @property
##    def Table(self, ppTable):
##        u'Setup table to view/edit.'
##        #return 
##
##    def _set(self, rhs):
##        u'Show alias names or the real field name in column headings. Default False.'
##    ShowAliasNamesInColumnHeadings = property(fset = _set, doc = _set.__doc__)
##
##    def UpdateSelection(self, pSelection):
##        u'Updates current table selection. Does not update Mx feature layer selection.'
##        #return 
##
##    @property
##    def SelectionSet(self):
##        u'Current s1election set of the table. Only valid for tables showing all rows.'
##        #return ppSelectionSet
##
##    def FindViaTable(self, pTable, ShowSelected):
##        u'Is table already being displayed.'
##        #return ppTableWindow
##

class RasterGxBrowserFactory(CoClass):
    u'The Raster GX Browser Factory is used to help look for rasters on disk.'
    _reg_clsid_ = GUID('{AAE25030-35FB-11D2-B1F2-00C04F8EDEFF}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
RasterGxBrowserFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayerFactory]

class IFindCallBack(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the results in a custom find dialog page.'
    _iid_ = GUID('{9F573561-56F3-11D2-A07B-0000F8775BF9}')
    _idlflags_ = ['oleautomation']
IFindCallBack._methods_ = [
    COMMETHOD(['propget', helpstring(u'The application that this dialog belongs to.')], HRESULT, 'Application',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IApplication)), 'pApplication' )),
    COMMETHOD(['propputref', helpstring(u'The object value of the new row. This object is passed to the popup menu in an ISet.')], HRESULT, 'Object',
              ( ['in'], VARIANT, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Rows column value in listbox.')], HRESULT, 'ColumnValue',
              ( ['in'], c_int, 'column' ),
              ( ['in'], BSTR, 'rhs' )),
    COMMETHOD(['propget', helpstring(u'Number of columns to display in list box.')], HRESULT, 'ColumnCount',
              ( ['retval', 'out'], POINTER(c_int), 'ColumnCount' )),
    COMMETHOD([helpstring(u'Adds a new row to the listbox, using values set with ColumnValue.')], HRESULT, 'AddNewRow'),
    COMMETHOD([helpstring(u'Processes messages. Run this method often.')], HRESULT, 'ProcessMessages',
              ( ['out'], POINTER(VARIANT_BOOL), 'quitProcessing' )),
    COMMETHOD([helpstring(u'Generic method to flash a point on the display n times.')], HRESULT, 'FlashGeometry',
              ( [], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'pGeometry' ),
              ( [], c_int, 'nTimes' ),
              ( [], VARIANT_BOOL, 'bCoolFlash' )),
]
################################################################
## code template for IFindCallBack implementation
##class IFindCallBack_Impl(object):
##    @property
##    def ColumnCount(self):
##        u'Number of columns to display in list box.'
##        #return ColumnCount
##
##    def ProcessMessages(self):
##        u'Processes messages. Run this method often.'
##        #return quitProcessing
##
##    def FlashGeometry(self, pGeometry, nTimes, bCoolFlash):
##        u'Generic method to flash a point on the display n times.'
##        #return 
##
##    def _set(self, column, rhs):
##        u'Rows column value in listbox.'
##    ColumnValue = property(fset = _set, doc = _set.__doc__)
##
##    def Object(self, rhs):
##        u'The object value of the new row. This object is passed to the popup menu in an ISet.'
##        #return 
##
##    @property
##    def Application(self):
##        u'The application that this dialog belongs to.'
##        #return pApplication
##
##    def AddNewRow(self):
##        u'Adds a new row to the listbox, using values set with ColumnValue.'
##        #return 
##

class AddDataDialog(CoClass):
    u'Add Data Dialog.'
    _reg_clsid_ = GUID('{B16C802C-4CBC-11D2-AE2A-080009EC732A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
class IAddDataDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Add Data Dialog.'
    _iid_ = GUID('{B16C802B-4CBC-11D2-AE2A-080009EC732A}')
    _idlflags_ = ['oleautomation']
class IAddDataDialog2(IAddDataDialog):
    _case_insensitive_ = True
    u'Provides access to members that control the Add Data Dialog.'
    _iid_ = GUID('{D03D289F-8F4B-4205-8062-544F5A35BC49}')
    _idlflags_ = ['oleautomation']
AddDataDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IAddDataDialog, IAddDataDialog2]

class ITableWindow2(IDataWindow):
    _case_insensitive_ = True
    u'Provides access to members that extend ITableWindow functionality to work with ILayers.'
    _iid_ = GUID('{911D4652-AED0-41DF-B528-81DAC35D0B5E}')
    _idlflags_ = ['oleautomation']
ITableWindow2._methods_ = [
    COMMETHOD(['propput', helpstring(u'Action to perform when table selections are made.')], HRESULT, 'TableSelectionAction',
              ( ['in'], comtypes.gen._4A9C9ED7_F7DB_4614_B480_A5D265C961FC_0_10_2.esriTableSelectionActions, 'pAction' )),
    COMMETHOD(['propget', helpstring(u'Action to perform when table selections are made.')], HRESULT, 'TableSelectionAction',
              ( ['retval', 'out'], POINTER(comtypes.gen._4A9C9ED7_F7DB_4614_B480_A5D265C961FC_0_10_2.esriTableSelectionActions), 'pAction' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether to show only features that are selected.')], HRESULT, 'ShowSelected',
              ( ['in'], VARIANT_BOOL, 'pShowSelected' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether to show only features that are selected.')], HRESULT, 'ShowSelected',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pShowSelected' )),
    COMMETHOD(['propget', helpstring(u'Current selection set of the table. Only valid for tables showing all rows.')], HRESULT, 'SelectionSet',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ISelectionSet)), 'ppSelectionSet' )),
    COMMETHOD([helpstring(u'Updates current table selection. Does not update Mx feature layer selection.')], HRESULT, 'UpdateSelection',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ISelectionSet), 'pSelection' )),
    COMMETHOD(['propput', helpstring(u'Show alias names or the real field name in column headings. Default False.')], HRESULT, 'ShowAliasNamesInColumnHeadings',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD(['propget', helpstring(u'The table control. Table needs to be showing before you can get a valid pointer.')], HRESULT, 'TableControl',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._4A9C9ED7_F7DB_4614_B480_A5D265C961FC_0_10_2.ITableControl)), 'ppTableControl' )),
    COMMETHOD(['propputref', helpstring(u'Setup layer attributes to view.')], HRESULT, 'Layer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer), 'ppLayer' )),
    COMMETHOD(['propget', helpstring(u'Setup layer attributes to view.')], HRESULT, 'Layer',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer)), 'ppLayer' )),
    COMMETHOD(['propputref', helpstring(u'The standalone table to view/edit.')], HRESULT, 'StandaloneTable',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IStandaloneTable), 'Table' )),
    COMMETHOD(['propget', helpstring(u'The standalone table to view/edit.')], HRESULT, 'StandaloneTable',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IStandaloneTable)), 'Table' )),
    COMMETHOD([helpstring(u'Is table (of a layer) already being displayed.')], HRESULT, 'FindViaLayer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer), 'pLayer' ),
              ( ['retval', 'out'], POINTER(POINTER(ITableWindow)), 'ppTableWindow' )),
    COMMETHOD([helpstring(u'Is table (of a standalonetable) already being displayed.')], HRESULT, 'FindViaStandaloneTable',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IStandaloneTable), 'pStandaloneTable' ),
              ( ['retval', 'out'], POINTER(POINTER(ITableWindow)), 'ppTableWindow' )),
]
################################################################
## code template for ITableWindow2 implementation
##class ITableWindow2_Impl(object):
##    @property
##    def Layer(self, ppLayer):
##        u'Setup layer attributes to view.'
##        #return 
##
##    def FindViaStandaloneTable(self, pStandaloneTable):
##        u'Is table (of a standalonetable) already being displayed.'
##        #return ppTableWindow
##
##    @property
##    def StandaloneTable(self, Table):
##        u'The standalone table to view/edit.'
##        #return 
##
##    def _get(self):
##        u'Action to perform when table selections are made.'
##        #return pAction
##    def _set(self, pAction):
##        u'Action to perform when table selections are made.'
##    TableSelectionAction = property(_get, _set, doc = _set.__doc__)
##
##    def FindViaLayer(self, pLayer):
##        u'Is table (of a layer) already being displayed.'
##        #return ppTableWindow
##
##    def _get(self):
##        u'Indicates whether to show only features that are selected.'
##        #return pShowSelected
##    def _set(self, pShowSelected):
##        u'Indicates whether to show only features that are selected.'
##    ShowSelected = property(_get, _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Show alias names or the real field name in column headings. Default False.'
##    ShowAliasNamesInColumnHeadings = property(fset = _set, doc = _set.__doc__)
##
##    def UpdateSelection(self, pSelection):
##        u'Updates current table selection. Does not update Mx feature layer selection.'
##        #return 
##
##    @property
##    def SelectionSet(self):
##        u'Current selection set of the table. Only valid for tables showing all rows.'
##        #return ppSelectionSet
##
##    @property
##    def TableControl(self):
##        u'The table control. Table needs to be showing before you can get a valid pointer.'
##        #return ppTableControl
##

class RasterLayerContextAnalyzer(CoClass):
    u'A coclass for RasterLayer context analyzer.'
    _reg_clsid_ = GUID('{6D572FA6-9155-11D2-AAD7-00C04FA375FB}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
RasterLayerContextAnalyzer._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IContextAnalyzer]

class IRelateData(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that relate a class or a table to a layer.'
    _iid_ = GUID('{2CBD0A81-FE89-11D3-ADF8-00C04FA33A15}')
    _idlflags_ = ['oleautomation']
IRelateData._methods_ = [
    COMMETHOD(['propputref', helpstring(u'Primary layer to join from.')], HRESULT, 'RelateOrigin',
              ( ['in'], POINTER(IUnknown), 'rhs' )),
    COMMETHOD([helpstring(u'Shows modal window.')], HRESULT, 'DoModal',
              ( ['in'], comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.OLE_HANDLE, 'parentWindow' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRelationshipClass)), 'relationshipClass' )),
]
################################################################
## code template for IRelateData implementation
##class IRelateData_Impl(object):
##    def RelateOrigin(self, rhs):
##        u'Primary layer to join from.'
##        #return 
##
##    def DoModal(self, parentWindow):
##        u'Shows modal window.'
##        #return relationshipClass
##

class IDataWindow2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control popup windows that show map data.'
    _iid_ = GUID('{04DBD418-AEE2-11D1-8750-0000F8751720}')
    _idlflags_ = ['oleautomation']
IDataWindow2._methods_ = [
    COMMETHOD(['propputref', helpstring(u'Provides the window with a reference to the application.')], HRESULT, 'Application',
              ( ['in'], POINTER(IDispatch), 'rhs' )),
    COMMETHOD(['propget', helpstring(u"The window's handle.")], HRESULT, 'hWnd',
              ( ['retval', 'out'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.OLE_HANDLE), 'hWnd' )),
    COMMETHOD([helpstring(u"The window's position in screen pixels.")], HRESULT, 'QueryPosition',
              ( ['out'], POINTER(c_int), 'left' ),
              ( ['out'], POINTER(c_int), 'top' ),
              ( ['out'], POINTER(c_int), 'right' ),
              ( ['out'], POINTER(c_int), 'bottom' )),
    COMMETHOD([helpstring(u"The window's position in screen pixels.")], HRESULT, 'PutPosition',
              ( ['in'], c_int, 'left' ),
              ( ['in'], c_int, 'top' ),
              ( ['in'], c_int, 'right' ),
              ( ['in'], c_int, 'bottom' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the window is visible.')], HRESULT, 'IsVisible',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsVisible' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the window is dockable.')], HRESULT, 'IsDockable',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsVisible' )),
    COMMETHOD([helpstring(u'Indicates if the window is shown.')], HRESULT, 'Show',
              ( ['in'], VARIANT_BOOL, 'Show' )),
    COMMETHOD([helpstring(u'Cause the window to redraw.')], HRESULT, 'Refresh'),
    COMMETHOD(['propget', helpstring(u'For developer use.')], HRESULT, 'Tag',
              ( ['retval', 'out'], POINTER(BSTR), 'Tag' )),
    COMMETHOD(['propput', helpstring(u'For developer use.')], HRESULT, 'Tag',
              ( ['in'], BSTR, 'Tag' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the context menu should be enabled.')], HRESULT, 'EnableContextMenu',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'enable' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the context menu should be enabled.')], HRESULT, 'EnableContextMenu',
              ( ['in'], VARIANT_BOOL, 'enable' )),
    COMMETHOD([helpstring(u'Close and destroy the window.')], HRESULT, 'Destroy'),
]
################################################################
## code template for IDataWindow2 implementation
##class IDataWindow2_Impl(object):
##    @property
##    def hWnd(self):
##        u"The window's handle."
##        #return hWnd
##
##    def Show(self, Show):
##        u'Indicates if the window is shown.'
##        #return 
##
##    def PutPosition(self, left, top, right, bottom):
##        u"The window's position in screen pixels."
##        #return 
##
##    @property
##    def IsDockable(self):
##        u'Indicates if the window is dockable.'
##        #return IsVisible
##
##    def _get(self):
##        u'Indicates if the context menu should be enabled.'
##        #return enable
##    def _set(self, enable):
##        u'Indicates if the context menu should be enabled.'
##    EnableContextMenu = property(_get, _set, doc = _set.__doc__)
##
##    def Refresh(self):
##        u'Cause the window to redraw.'
##        #return 
##
##    def QueryPosition(self):
##        u"The window's position in screen pixels."
##        #return left, top, right, bottom
##
##    def Application(self, rhs):
##        u'Provides the window with a reference to the application.'
##        #return 
##
##    def _get(self):
##        u'For developer use.'
##        #return Tag
##    def _set(self, Tag):
##        u'For developer use.'
##    Tag = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def IsVisible(self):
##        u'Indicates if the window is visible.'
##        #return IsVisible
##
##    def Destroy(self):
##        u'Close and destroy the window.'
##        #return 
##

class BasemapSubLayerRasterLayerContextAnalyzer(CoClass):
    u'A coclass for Basemap Sub Layer which is a RasterLayer context analyzer.'
    _reg_clsid_ = GUID('{F69C4523-6D83-4308-A89E-2AC1997787AC}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
BasemapSubLayerRasterLayerContextAnalyzer._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IContextAnalyzer]

class RasterBasemapLayerContextAnalyzer(CoClass):
    u'A coclass for Raster Basemap Layer context analyzer.'
    _reg_clsid_ = GUID('{E637FBCB-3F57-4CA2-B089-B1F58680D453}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
RasterBasemapLayerContextAnalyzer._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IContextAnalyzer]

class ILayerEffectsEnvironment2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Layer Effects Environment.'
    _iid_ = GUID('{5AFA7340-1EEC-4EB8-9E15-B414DF0FF8E9}')
    _idlflags_ = ['oleautomation']
ILayerEffectsEnvironment2._methods_ = [
    COMMETHOD(['propget', helpstring(u'The ILayerEffects interface of the current effects layer.')], HRESULT, 'EffectsLayer',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayerEffects)), 'effects' )),
    COMMETHOD(['propputref', helpstring(u'The ILayerEffects interface of the current effects layer.')], HRESULT, 'EffectsLayer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayerEffects), 'effects' )),
    COMMETHOD(['propget', helpstring(u'The IActiveView interface of the view to be refreshed.')], HRESULT, 'ActiveView',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IActiveView)), 'ActiveView' )),
    COMMETHOD(['propputref', helpstring(u'The IActiveView interface of the view to be refreshed.')], HRESULT, 'ActiveView',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IActiveView), 'ActiveView' )),
    COMMETHOD(['propget', helpstring(u'Currenttly selected layer.')], HRESULT, 'SelectedLayer',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer)), 'Layer' )),
    COMMETHOD(['propputref', helpstring(u'Currenttly selected layer.')], HRESULT, 'SelectedLayer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer), 'Layer' )),
]
################################################################
## code template for ILayerEffectsEnvironment2 implementation
##class ILayerEffectsEnvironment2_Impl(object):
##    def ActiveView(self, ActiveView):
##        u'The IActiveView interface of the view to be refreshed.'
##        #return 
##
##    def SelectedLayer(self, Layer):
##        u'Currenttly selected layer.'
##        #return 
##
##    def EffectsLayer(self, effects):
##        u'The ILayerEffects interface of the current effects layer.'
##        #return 
##

class RasterCatalogGxBrowserFactory(CoClass):
    u'The Raster Catalog GX Browser Factory.'
    _reg_clsid_ = GUID('{C66BCB39-FEA7-47B0-9CCC-5FA02D59B542}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
RasterCatalogGxBrowserFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayerFactory]

class ILayerEffectsEnvironment(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Layer Effects Environment.'
    _iid_ = GUID('{377ABA23-2019-11D3-9F97-00C04F6BC78E}')
    _idlflags_ = ['oleautomation']
ILayerEffectsEnvironment._methods_ = [
    COMMETHOD(['propget', helpstring(u'The ILayerEffects interface of the current effects layer.')], HRESULT, 'EffectsLayer',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayerEffects)), 'effects' )),
    COMMETHOD(['propputref', helpstring(u'The ILayerEffects interface of the current effects layer.')], HRESULT, 'EffectsLayer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayerEffects), 'effects' )),
    COMMETHOD(['propget', helpstring(u'The IActiveView interface of the view to be refreshed.')], HRESULT, 'ActiveView',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IActiveView)), 'ActiveView' )),
    COMMETHOD(['propputref', helpstring(u'The IActiveView interface of the view to be refreshed.')], HRESULT, 'ActiveView',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IActiveView), 'ActiveView' )),
]
################################################################
## code template for ILayerEffectsEnvironment implementation
##class ILayerEffectsEnvironment_Impl(object):
##    def ActiveView(self, ActiveView):
##        u'The IActiveView interface of the view to be refreshed.'
##        #return 
##
##    def EffectsLayer(self, effects):
##        u'The ILayerEffects interface of the current effects layer.'
##        #return 
##

class PixelInspectionDockWin(CoClass):
    u'The Pixel Inspection Dockable Window.'
    _reg_clsid_ = GUID('{9EDB656A-3FE6-4D2A-BBF7-A408298ADF61}')
    _idlflags_ = ['restricted']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
class IPixelInspectionWindow(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the PixelInspection Window.'
    _iid_ = GUID('{0E7E386A-8BCE-4A95-B74E-2839414412EC}')
    _idlflags_ = ['oleautomation', 'restricted']
class IDocumentEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to events that occur in ArcMap.'
    _iid_ = GUID('{6DB7C4BD-0A7C-11D1-86AA-0000F8751720}')
    _idlflags_ = ['oleautomation']
PixelInspectionDockWin._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IDockableWindowDef, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IDockableWindowImageDef, IPixelInspectionWindow, IDocumentEvents, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IActiveViewEvents, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IConnectionPointContainer]

IPixelInspectionWindow._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The raster layer to be inspected.')], HRESULT, 'Layer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer), 'ppLayer' )),
    COMMETHOD(['propget', helpstring(u'The raster layer to be inspected.')], HRESULT, 'Layer',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer)), 'ppLayer' )),
    COMMETHOD(['propput', helpstring(u'The raster band index to be inspected.')], HRESULT, 'BandIndex',
              ( ['in'], c_int, 'BandIndex' )),
    COMMETHOD(['propget', helpstring(u'The raster band index to be inspected.')], HRESULT, 'BandIndex',
              ( ['retval', 'out'], POINTER(c_int), 'BandIndex' )),
    COMMETHOD([helpstring(u'Map location to inspect the pixels.')], HRESULT, 'DisplayPixels',
              ( ['in'], c_int, 'action' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'point' ),
              ( ['in'], POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IDisplay), 'pDisplay' )),
    COMMETHOD(['propput', helpstring(u'The name of the layer.')], HRESULT, 'LayerName',
              ( ['in'], BSTR, 'rhs' )),
]
################################################################
## code template for IPixelInspectionWindow implementation
##class IPixelInspectionWindow_Impl(object):
##    @property
##    def Layer(self, ppLayer):
##        u'The raster layer to be inspected.'
##        #return 
##
##    def _set(self, rhs):
##        u'The name of the layer.'
##    LayerName = property(fset = _set, doc = _set.__doc__)
##
##    def DisplayPixels(self, action, point, pDisplay):
##        u'Map location to inspect the pixels.'
##        #return 
##
##    def _get(self):
##        u'The raster band index to be inspected.'
##        #return BandIndex
##    def _set(self, BandIndex):
##        u'The raster band index to be inspected.'
##    BandIndex = property(_get, _set, doc = _set.__doc__)
##

class ILensWindow(IDataWindow):
    _case_insensitive_ = True
    u'Provides access to members that control the Lens Window.'
    _iid_ = GUID('{279C3487-36AA-11D1-8809-080009EC732A}')
    _idlflags_ = ['oleautomation']
ILensWindow._methods_ = [
    COMMETHOD(['propget', helpstring(u'The screen display used by this window.')], HRESULT, 'ScreenDisplay',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IScreenDisplay)), 'screen' )),
    COMMETHOD(['propget', helpstring(u"Indicates if the window is redrawn as it's moved or not.")], HRESULT, 'UpdateWhileDragging',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'UpdateWhileDragging' )),
    COMMETHOD(['propput', helpstring(u"Indicates if the window is redrawn as it's moved or not.")], HRESULT, 'UpdateWhileDragging',
              ( ['in'], VARIANT_BOOL, 'UpdateWhileDragging' )),
    COMMETHOD(['propget', helpstring(u"Indicates if the window shows a live view of what's under it or a snapshot.")], HRESULT, 'IsLive',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsLive' )),
    COMMETHOD(['propput', helpstring(u"Indicates if the window shows a live view of what's under it or a snapshot.")], HRESULT, 'IsLive',
              ( ['in'], VARIANT_BOOL, 'IsLive' )),
]
################################################################
## code template for ILensWindow implementation
##class ILensWindow_Impl(object):
##    def _get(self):
##        u"Indicates if the window shows a live view of what's under it or a snapshot."
##        #return IsLive
##    def _set(self, IsLive):
##        u"Indicates if the window shows a live view of what's under it or a snapshot."
##    IsLive = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def ScreenDisplay(self):
##        u'The screen display used by this window.'
##        #return screen
##
##    def _get(self):
##        u"Indicates if the window is redrawn as it's moved or not."
##        #return UpdateWhileDragging
##    def _set(self, UpdateWhileDragging):
##        u"Indicates if the window is redrawn as it's moved or not."
##    UpdateWhileDragging = property(_get, _set, doc = _set.__doc__)
##

class LayerSelectionContextMenu(CoClass):
    u'Layer Selection Context Menu.'
    _reg_clsid_ = GUID('{DC37DB9E-D40D-43BB-9757-7E59B557F101}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
LayerSelectionContextMenu._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IMenuDef]

class IMoveMapsOperation(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Move maps operation.'
    _iid_ = GUID('{82D7A63E-6223-410B-AC81-0F15B8F57EE4}')
    _idlflags_ = ['oleautomation']
IMoveMapsOperation._methods_ = [
    COMMETHOD([helpstring(u'Information of the map to be moved.')], HRESULT, 'Add',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMap), 'pMap' )),
    COMMETHOD(['propput', helpstring(u'Information regarding where the the layer needs to be moved. Destination group is NULL if the layer is bing moved to into a map.')], HRESULT, 'NewIndex',
              ( ['in'], c_int, 'rhs' )),
]
################################################################
## code template for IMoveMapsOperation implementation
##class IMoveMapsOperation_Impl(object):
##    def Add(self, pMap):
##        u'Information of the map to be moved.'
##        #return 
##
##    def _set(self, rhs):
##        u'Information regarding where the the layer needs to be moved. Destination group is NULL if the layer is bing moved to into a map.'
##    NewIndex = property(fset = _set, doc = _set.__doc__)
##

class JoinRelatePage(CoClass):
    u'Join and Relate property page.'
    _reg_clsid_ = GUID('{4C839CB3-01C3-11D4-A0B7-00C04F6BC626}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
JoinRelatePage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class ReferenceScaleOperation(CoClass):
    u'Reference Scale Operation.'
    _reg_clsid_ = GUID('{65749418-48DA-11D2-AE28-080009EC732A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
class IReferenceScaleOperation(comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IOperation):
    _case_insensitive_ = True
    u'Provides access to members that control the Reference Scale Operation.'
    _iid_ = GUID('{65749419-48DA-11D2-AE28-080009EC732A}')
    _idlflags_ = ['oleautomation']
ReferenceScaleOperation._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IOperation, IReferenceScaleOperation]

class RasterToolExtension(CoClass):
    u'The extension of raster tool.'
    _reg_clsid_ = GUID('{60817537-E48F-476A-A112-1C9222AAA549}')
    _idlflags_ = ['restricted']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
RasterToolExtension._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IExtension]

class IMapInsetWindow(ILensWindow):
    _case_insensitive_ = True
    u'Provides access to members that control the Map Inset Window.'
    _iid_ = GUID('{279C3488-36AA-11D1-8809-080009EC732A}')
    _idlflags_ = ['oleautomation']
IMapInsetWindow._methods_ = [
    COMMETHOD(['propget', helpstring(u'The MapInset used by this window.')], HRESULT, 'MapInset',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMapInset)), 'MapInset' )),
    COMMETHOD(['propputref', helpstring(u'The MapInset used by this window.')], HRESULT, 'MapInset',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMapInset), 'MapInset' )),
    COMMETHOD([helpstring(u'Draw leader lines from the inset to the location on the map shown by the inset.')], HRESULT, 'FlashLocation'),
]
################################################################
## code template for IMapInsetWindow implementation
##class IMapInsetWindow_Impl(object):
##    def MapInset(self, MapInset):
##        u'The MapInset used by this window.'
##        #return 
##
##    def FlashLocation(self):
##        u'Draw leader lines from the inset to the location on the map shown by the inset.'
##        #return 
##

class IJoinPages(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control which pages are shown.'
    _iid_ = GUID('{062453B6-4896-4CB6-8D90-13BE49779810}')
    _idlflags_ = ['oleautomation']
IJoinPages._methods_ = [
    COMMETHOD(['propput', helpstring(u'Indicates if attribute page is shown. Default: True.')], HRESULT, 'ShowJoinAttributePage',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Indicates if relationship page is shown. Default: True. If no relationships are present for layer, page will not be shown.')], HRESULT, 'ShowJoinRelationshipPage',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Indicates if location page is shown. Default: True.')], HRESULT, 'ShowJoinLocationPage',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
]
################################################################
## code template for IJoinPages implementation
##class IJoinPages_Impl(object):
##    def _set(self, rhs):
##        u'Indicates if relationship page is shown. Default: True. If no relationships are present for layer, page will not be shown.'
##    ShowJoinRelationshipPage = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Indicates if attribute page is shown. Default: True.'
##    ShowJoinAttributePage = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Indicates if location page is shown. Default: True.'
##    ShowJoinLocationPage = property(fset = _set, doc = _set.__doc__)
##

class IOverviewWindow(IDataWindow):
    _case_insensitive_ = True
    u'Provides access to members that control the Overview Window.'
    _iid_ = GUID('{263F34B3-0A12-11D2-ADFB-080009EC732A}')
    _idlflags_ = ['oleautomation']
IOverviewWindow._methods_ = [
    COMMETHOD(['propget', helpstring(u'The Overview used by this window.')], HRESULT, 'Overview',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IOverview)), 'Overview' )),
    COMMETHOD(['propputref', helpstring(u'The Overview used by this window.')], HRESULT, 'Overview',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IOverview), 'Overview' )),
]
################################################################
## code template for IOverviewWindow implementation
##class IOverviewWindow_Impl(object):
##    def Overview(self, Overview):
##        u'The Overview used by this window.'
##        #return 
##

class MapServerIdentifyObject(CoClass):
    u'Provides programmatic access to a map server identify object.'
    _reg_clsid_ = GUID('{12917439-AE70-432A-A461-500B2B86BC1A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
MapServerIdentifyObject._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IIdentifyObj, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IIdentifyObject, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMapServerIdentifyObject, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMapIdentifyObject, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IBasicMapIdentifyObject]

class IMetadataViewWindow(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members setting the Metadata View Window.'
    _iid_ = GUID('{3D477E2F-B719-4FF0-9C48-8C4A01EF1F00}')
    _idlflags_ = ['oleautomation']
class IMetadataViewWindow2(IMetadataViewWindow):
    _case_insensitive_ = True
    u'Provides access to members setting the Metadata View Window.'
    _iid_ = GUID('{CC40A88D-28C9-46FC-88CF-F487E81EAD99}')
    _idlflags_ = ['oleautomation']
IMetadataViewWindow._methods_ = [
    COMMETHOD(['propputref', helpstring(u'Provides the window with a reference to the application.')], HRESULT, 'Application',
              ( ['in'], POINTER(IDispatch), 'rhs' )),
    COMMETHOD(['propget', helpstring(u'The stored layer.')], HRESULT, 'Layer',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer)), 'pLayer' )),
    COMMETHOD(['propputref', helpstring(u'The stored layer.')], HRESULT, 'Layer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer), 'pLayer' )),
    COMMETHOD(['propputref', helpstring(u'The standalone table to view/edit.')], HRESULT, 'StandaloneTable',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IStandaloneTable), 'Table' )),
    COMMETHOD(['propget', helpstring(u'The standalone table to view/edit.')], HRESULT, 'StandaloneTable',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IStandaloneTable)), 'Table' )),
    COMMETHOD(['propputref', helpstring(u'Pass the data source name of the selected layer to Metadata View window.')], HRESULT, 'DataSource',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetName), 'rhs' )),
    COMMETHOD([helpstring(u"Is Metadata (of a layer's data source) already being displayed.")], HRESULT, 'FindViaLayer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer), 'pLayer' ),
              ( ['retval', 'out'], POINTER(POINTER(IMetadataViewWindow)), 'ppMetadataViewWindow' )),
    COMMETHOD([helpstring(u'Is Metadata (of a standalone table) already being displayed.')], HRESULT, 'FindViaStandaloneTable',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IStandaloneTable), 'pStandaloneTable' ),
              ( ['retval', 'out'], POINTER(POINTER(IMetadataViewWindow)), 'ppMetadataViewWindow' )),
    COMMETHOD(['propget', helpstring(u'HWND of the Metadata View Window.')], HRESULT, 'hWnd',
              ( ['retval', 'out'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.OLE_HANDLE), 'hWnd' )),
    COMMETHOD(['propget', helpstring(u'Stylesheet path from Metadata helper.')], HRESULT, 'StylesheetPath',
              ( ['retval', 'out'], POINTER(BSTR), 'pStylesheetPath' )),
    COMMETHOD(['propget', helpstring(u'Selected Stylesheet from Metadata helper.')], HRESULT, 'SelectedStylesheet',
              ( ['retval', 'out'], POINTER(BSTR), 'pSelectedStylesheet' )),
    COMMETHOD(['propget', helpstring(u"The Metadata of the selected layer's data source.")], HRESULT, 'Metadata',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'pPropertySet' )),
    COMMETHOD(['propget', helpstring(u'The Metadata helper to get stylesheet path and metadata.')], HRESULT, 'MetadataHelper',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C0FC1503_7E6F_11D2_AABF_00C04FA375F1_0_10_2.IMetadataHelper)), 'pMetadataHelper' )),
    COMMETHOD([helpstring(u"Show MetadataViewWindow of the selected layer's data source.")], HRESULT, 'Show',
              ( ['in'], VARIANT_BOOL, 'Show' )),
    COMMETHOD([helpstring(u'Refresh the metadata view.')], HRESULT, 'Refresh'),
]
################################################################
## code template for IMetadataViewWindow implementation
##class IMetadataViewWindow_Impl(object):
##    def Layer(self, pLayer):
##        u'The stored layer.'
##        #return 
##
##    def Show(self, Show):
##        u"Show MetadataViewWindow of the selected layer's data source."
##        #return 
##
##    @property
##    def MetadataHelper(self):
##        u'The Metadata helper to get stylesheet path and metadata.'
##        #return pMetadataHelper
##
##    @property
##    def hWnd(self):
##        u'HWND of the Metadata View Window.'
##        #return hWnd
##
##    @property
##    def StylesheetPath(self):
##        u'Stylesheet path from Metadata helper.'
##        #return pStylesheetPath
##
##    def FindViaStandaloneTable(self, pStandaloneTable):
##        u'Is Metadata (of a standalone table) already being displayed.'
##        #return ppMetadataViewWindow
##
##    def FindViaLayer(self, pLayer):
##        u"Is Metadata (of a layer's data source) already being displayed."
##        #return ppMetadataViewWindow
##
##    def Refresh(self):
##        u'Refresh the metadata view.'
##        #return 
##
##    def Application(self, rhs):
##        u'Provides the window with a reference to the application.'
##        #return 
##
##    def DataSource(self, rhs):
##        u'Pass the data source name of the selected layer to Metadata View window.'
##        #return 
##
##    @property
##    def Metadata(self):
##        u"The Metadata of the selected layer's data source."
##        #return pPropertySet
##
##    @property
##    def StandaloneTable(self, Table):
##        u'The standalone table to view/edit.'
##        #return 
##
##    @property
##    def SelectedStylesheet(self):
##        u'Selected Stylesheet from Metadata helper.'
##        #return pSelectedStylesheet
##

IMetadataViewWindow2._methods_ = [
    COMMETHOD(['propputref', helpstring(u'Pass the metadata directly to Metadata View window.')], HRESULT, 'Metadata',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'rhs' )),
]
################################################################
## code template for IMetadataViewWindow2 implementation
##class IMetadataViewWindow2_Impl(object):
##    def Metadata(self, rhs):
##        u'Pass the metadata directly to Metadata View window.'
##        #return 
##

class IReportUnitFormat2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to report unit formatting.'
    _iid_ = GUID('{5FC55A42-B276-4E9C-9DCE-C54F61419DFE}')
    _idlflags_ = ['oleautomation']
IReportUnitFormat2._methods_ = [
    COMMETHOD(['propget', helpstring(u"When a map's display units are set to esriDecimalDegrees, tools use this format to report coordinates.")], HRESULT, 'LatLonFormat',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILatLonFormat)), 'Format' )),
    COMMETHOD(['propputref', helpstring(u"When a map's display units are set to esriDecimalDegrees, tools use this format to report coordinates.")], HRESULT, 'LatLonFormat',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILatLonFormat), 'Format' )),
    COMMETHOD(['propget', helpstring(u'The number format used to report coordinate values.')], HRESULT, 'NumericFormat',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.INumberFormat)), 'Format' )),
    COMMETHOD(['propputref', helpstring(u'The number format used to report coordinate values.')], HRESULT, 'NumericFormat',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.INumberFormat), 'Format' )),
    COMMETHOD(['propget', helpstring(u'The format used for the coordinate readout on the status bar.')], HRESULT, 'CoordinateReadoutLatLonFormat',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILatLonFormat)), 'Format' )),
    COMMETHOD(['propputref', helpstring(u'The format used for the coordinate readout on the status bar.')], HRESULT, 'CoordinateReadoutLatLonFormat',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILatLonFormat), 'Format' )),
    COMMETHOD(['propget', helpstring(u'The units used for the coordinate readout on the status bar. If set to esriUnknown,  map display units are used.')], HRESULT, 'CoordinateReadoutUnits',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.esriUnits), 'units' )),
    COMMETHOD(['propput', helpstring(u'The units used for the coordinate readout on the status bar. If set to esriUnknown,  map display units are used.')], HRESULT, 'CoordinateReadoutUnits',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.esriUnits, 'units' )),
]
################################################################
## code template for IReportUnitFormat2 implementation
##class IReportUnitFormat2_Impl(object):
##    def CoordinateReadoutLatLonFormat(self, Format):
##        u'The format used for the coordinate readout on the status bar.'
##        #return 
##
##    def NumericFormat(self, Format):
##        u'The number format used to report coordinate values.'
##        #return 
##
##    def _get(self):
##        u'The units used for the coordinate readout on the status bar. If set to esriUnknown,  map display units are used.'
##        #return units
##    def _set(self, units):
##        u'The units used for the coordinate readout on the status bar. If set to esriUnknown,  map display units are used.'
##    CoordinateReadoutUnits = property(_get, _set, doc = _set.__doc__)
##
##    def LatLonFormat(self, Format):
##        u"When a map's display units are set to esriDecimalDegrees, tools use this format to report coordinates."
##        #return 
##

class OverviewWindowFactory(CoClass):
    u'Factory to generate an Overview window.'
    _reg_clsid_ = GUID('{263F34B5-0A12-11D2-ADFB-080009EC732A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
class IDataWindowFactory(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Factory for creating floating windows.'
    _iid_ = GUID('{04DBD417-AEE2-11D1-8750-0000F8751720}')
    _idlflags_ = ['oleautomation']
OverviewWindowFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDataWindowFactory]

class OverviewPropertyPage(CoClass):
    u'Property page for Overview window properties.'
    _reg_clsid_ = GUID('{7A4FB39F-0BA5-11D2-ADFD-080009EC732A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
OverviewPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class TableDockWindow(CoClass):
    u'Table dock window'
    _reg_clsid_ = GUID('{2B740D8F-442C-4975-BCE7-59D9949DAD9E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
class ITableDockWindowAdmin(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the table docking window.'
    _iid_ = GUID('{9060EAA6-7A2E-452C-8224-6B89E015B89D}')
    _idlflags_ = ['oleautomation']
TableDockWindow._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IDockableWindowDef, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IDockableWindowImageDef, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IDockableWindowInitialPlacement, ITableDockWindowAdmin]

class TableContextMenuArrangeItems(CoClass):
    u'Arrange table windows context menu items.'
    _reg_clsid_ = GUID('{EA0A5880-D696-4FDE-AAE3-A0B76B186598}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
TableContextMenuArrangeItems._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.ICommand]

class TinHistogram(CoClass):
    u'TIN histogram of data values.'
    _reg_clsid_ = GUID('{62503EF2-6AD9-11D3-9F59-00C04F6BC619}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
class ITinHistogram(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that create a Histogram from TIN data values.'
    _iid_ = GUID('{62503EF1-6AD9-11D3-9F59-00C04F6BC619}')
    _idlflags_ = ['oleautomation']
TinHistogram._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._D92377DC_FAB1_4DFB_A4C1_61BD8C40DBEB_0_10_2.IHistogram, ITinHistogram, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStatisticsResults]

class MapInsetPropertyPage(CoClass):
    u'Property page for magnifier window.'
    _reg_clsid_ = GUID('{19EB659B-F2B1-11D2-B870-00600802E603}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
MapInsetPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class MapPropertyPage(CoClass):
    u'Property page for Map general properties.'
    _reg_clsid_ = GUID('{E8458D0C-EA9C-11D1-8782-0000F8751720}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
MapPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class TableContextMenuArrange(CoClass):
    u'Arrange table windows context menu.'
    _reg_clsid_ = GUID('{4214670A-582A-4843-8594-A1D20A7F7198}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
TableContextMenuArrange._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IMenuDef]

class MapIlluminationPropertyPage(CoClass):
    u'Property page for Map illumination properties.'
    _reg_clsid_ = GUID('{D77ED1C7-B0AF-11D2-81FC-00104BC4CD03}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
MapIlluminationPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]


# values for enumeration 'esriMxCustomizationEvent'
esriCEShowDataFrameProperties = 100
esriCEShowAddDataDialog = 101
esriCEShowLayersProperties = 102
esriMxCustomizationEvent = c_int # enum

# values for enumeration 'esriTinHistogramType'
esriTinElevationHisto = 0
esriTinAspectHisto = 1
esriTinSlopeHisto = 2
esriTinNodeElevationHisto = 3
esriTerrainPointElevationHisto = 4
esriTerrainPointAttributeHisto = 5
esriLasPointElevationHisto = 6
esriTinHistogramType = c_int # enum
class ISpatialJoin(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that join the attributes of feature classes based on the spatial relationships of the features.'
    _iid_ = GUID('{12B35C8F-010F-11D4-A692-0008C7D3AE8D}')
    _idlflags_ = ['oleautomation']
ISpatialJoin._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The spatial table to append fields to.')], HRESULT, 'SourceTable',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable), 'rhs' )),
    COMMETHOD(['propputref', helpstring(u'The spatial table to append fields from.')], HRESULT, 'JoinTable',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable), 'rhs' )),
    COMMETHOD([helpstring(u'Join using aggregate. Only features within a distance of maxMapDist will be joined. A maxMapDist of -1 means infinity.')], HRESULT, 'JoinAggregate',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName), 'pOutputName' ),
              ( ['in'], c_double, 'maxMapDist' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass)), 'ppJoinedFeatureClass' )),
    COMMETHOD([helpstring(u'Joins with the nearest feature in the join feature class. Only features within a distance of maxMapDist will be joined. A maxMapDist of -1 means infinity.')], HRESULT, 'JoinNearest',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName), 'pOutputName' ),
              ( ['in'], c_double, 'maxMapDist' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass)), 'ppJoinedFeatureClass' )),
    COMMETHOD([helpstring(u'Joins a feature in the source feature class with the feature if it falls within in the join feature class.')], HRESULT, 'JoinWithin',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName), 'pOutputName' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass)), 'ppJoinedFeatureClass' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether to show update messages while processing join.')], HRESULT, 'ShowProcess',
              ( ['in'], VARIANT_BOOL, 'bShowMessage' ),
              ( ['in'], comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.OLE_HANDLE, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether a match is required before adding a record from the source feature class to the result. If TRUE, all records in the source feature class are added regardless of whether there is a match.')], HRESULT, 'LeftOuterJoin',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
]
################################################################
## code template for ISpatialJoin implementation
##class ISpatialJoin_Impl(object):
##    def JoinWithin(self, pOutputName):
##        u'Joins a feature in the source feature class with the feature if it falls within in the join feature class.'
##        #return ppJoinedFeatureClass
##
##    def JoinNearest(self, pOutputName, maxMapDist):
##        u'Joins with the nearest feature in the join feature class. Only features within a distance of maxMapDist will be joined. A maxMapDist of -1 means infinity.'
##        #return ppJoinedFeatureClass
##
##    def JoinTable(self, rhs):
##        u'The spatial table to append fields from.'
##        #return 
##
##    def _set(self, bShowMessage, rhs):
##        u'Indicates whether to show update messages while processing join.'
##    ShowProcess = property(fset = _set, doc = _set.__doc__)
##
##    def JoinAggregate(self, pOutputName, maxMapDist):
##        u'Join using aggregate. Only features within a distance of maxMapDist will be joined. A maxMapDist of -1 means infinity.'
##        #return ppJoinedFeatureClass
##
##    def SourceTable(self, rhs):
##        u'The spatial table to append fields to.'
##        #return 
##
##    def _set(self, rhs):
##        u'Indicates whether a match is required before adding a record from the source feature class to the result. If TRUE, all records in the source feature class are added regardless of whether there is a match.'
##    LeftOuterJoin = property(fset = _set, doc = _set.__doc__)
##

class MapGridsPropertyPage(CoClass):
    u'Property page for Map grid properties.'
    _reg_clsid_ = GUID('{D5549ADB-3845-11D2-AE12-080009EC732A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
MapGridsPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class IMxApplication(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Mx Application.'
    _iid_ = GUID('{0522A5F2-487C-11D0-98BD-00805F7CED21}')
    _idlflags_ = ['oleautomation']
IMxApplication._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The current printer settings.')], HRESULT, 'Printer',
              ( ['in'], POINTER(comtypes.gen._7DB92CEC_CB65_420A_8737_FCD0722FD436_0_10_2.IPrinter), 'Printer' )),
    COMMETHOD(['propget', helpstring(u'The current printer settings.')], HRESULT, 'Printer',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._7DB92CEC_CB65_420A_8737_FCD0722FD436_0_10_2.IPrinter)), 'Printer' )),
    COMMETHOD(['propget', helpstring(u'The current paper settings.')], HRESULT, 'Paper',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._7DB92CEC_CB65_420A_8737_FCD0722FD436_0_10_2.IPaper)), 'Paper' )),
    COMMETHOD(['propget', helpstring(u'The application display.')], HRESULT, 'Display',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IAppDisplay)), 'Display' )),
    COMMETHOD(['propget', helpstring(u'The selection environment.')], HRESULT, 'SelectionEnvironment',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ISelectionEnvironment)), 'env' )),
    COMMETHOD([helpstring(u'Exports the current document.')], HRESULT, 'Export'),
    COMMETHOD([helpstring(u'Copies the current view to the clipboard.')], HRESULT, 'CopyToClipboard'),
]
################################################################
## code template for IMxApplication implementation
##class IMxApplication_Impl(object):
##    def CopyToClipboard(self):
##        u'Copies the current view to the clipboard.'
##        #return 
##
##    @property
##    def Printer(self, Printer):
##        u'The current printer settings.'
##        #return 
##
##    @property
##    def SelectionEnvironment(self):
##        u'The selection environment.'
##        #return env
##
##    @property
##    def Paper(self):
##        u'The current paper settings.'
##        #return Paper
##
##    def Export(self):
##        u'Exports the current document.'
##        #return 
##
##    @property
##    def Display(self):
##        u'The application display.'
##        #return Display
##

class IMxApplication2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Mx Application.'
    _iid_ = GUID('{0522A5F3-487C-11D0-98BD-00805F7CED21}')
    _idlflags_ = ['oleautomation']
IMxApplication2._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The current printer settings.')], HRESULT, 'Printer',
              ( ['in'], POINTER(comtypes.gen._7DB92CEC_CB65_420A_8737_FCD0722FD436_0_10_2.IPrinter), 'Printer' )),
    COMMETHOD(['propget', helpstring(u'The current printer settings.')], HRESULT, 'Printer',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._7DB92CEC_CB65_420A_8737_FCD0722FD436_0_10_2.IPrinter)), 'Printer' )),
    COMMETHOD(['propget', helpstring(u'The current paper settings.')], HRESULT, 'Paper',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._7DB92CEC_CB65_420A_8737_FCD0722FD436_0_10_2.IPaper)), 'Paper' )),
    COMMETHOD(['propget', helpstring(u'The application display.')], HRESULT, 'Display',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IAppDisplay)), 'Display' )),
    COMMETHOD(['propget', helpstring(u'The selection environment.')], HRESULT, 'SelectionEnvironment',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ISelectionEnvironment)), 'env' )),
    COMMETHOD([helpstring(u'Exports the current document.')], HRESULT, 'Export'),
    COMMETHOD([helpstring(u'Copies the current view to the clipboard.')], HRESULT, 'CopyToClipboard'),
    COMMETHOD(['propput', helpstring(u'Pause display updates.')], HRESULT, 'PauseDrawing',
              ( ['in'], VARIANT_BOOL, 'flag' )),
    COMMETHOD(['propget', helpstring(u'Pause display updates.')], HRESULT, 'PauseDrawing',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
]
################################################################
## code template for IMxApplication2 implementation
##class IMxApplication2_Impl(object):
##    def CopyToClipboard(self):
##        u'Copies the current view to the clipboard.'
##        #return 
##
##    @property
##    def Printer(self, Printer):
##        u'The current printer settings.'
##        #return 
##
##    def _get(self):
##        u'Pause display updates.'
##        #return flag
##    def _set(self, flag):
##        u'Pause display updates.'
##    PauseDrawing = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def SelectionEnvironment(self):
##        u'The selection environment.'
##        #return env
##
##    @property
##    def Paper(self):
##        u'The current paper settings.'
##        #return Paper
##
##    def Export(self):
##        u'Exports the current document.'
##        #return 
##
##    @property
##    def Display(self):
##        u'The application display.'
##        #return Display
##

class IGroupLayersOperation(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Group layers operation.'
    _iid_ = GUID('{195A29FB-4845-4E73-B4D7-1264456F082D}')
    _idlflags_ = ['oleautomation']
IGroupLayersOperation._methods_ = [
    COMMETHOD([helpstring(u'Adds layer to be added to the group.')], HRESULT, 'AddLayer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer), 'pLayer' )),
    COMMETHOD(['propput', helpstring(u'Parent group if the layers belongs to a group layer.')], HRESULT, 'SourceGroupLayer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IGroupLayer), 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Parent map of the layers being added.')], HRESULT, 'SourceMap',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMap), 'rhs' )),
]
################################################################
## code template for IGroupLayersOperation implementation
##class IGroupLayersOperation_Impl(object):
##    def _set(self, rhs):
##        u'Parent map of the layers being added.'
##    SourceMap = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Parent group if the layers belongs to a group layer.'
##    SourceGroupLayer = property(fset = _set, doc = _set.__doc__)
##
##    def AddLayer(self, pLayer):
##        u'Adds layer to be added to the group.'
##        #return 
##

class IJoinData2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that join a feature class or a table to a layer/standalone table in ArcMap.'
    _iid_ = GUID('{C0310BF4-067F-4631-BCC4-637A5C7A5BA6}')
    _idlflags_ = ['oleautomation']
IJoinData2._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The application to which this window belongs (Optional).')], HRESULT, 'Application',
              ( ['in'], POINTER(IDispatch), 'rhs' )),
    COMMETHOD(['propputref', helpstring(u'Primary layer to join from (removes standalone table setting).')], HRESULT, 'Layer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer), 'rhs' )),
    COMMETHOD([helpstring(u'Shows modal window.')], HRESULT, 'DoModal',
              ( ['in'], comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.OLE_HANDLE, 'parentWindow' )),
    COMMETHOD(['hidden', helpstring(u'Updates all UI controls (used internally only).')], HRESULT, 'UpdateUIControls'),
    COMMETHOD(['propputref', helpstring(u'Primary table to join from (removes layer setting).')], HRESULT, 'StandaloneTable',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IStandaloneTable), 'rhs' )),
]
################################################################
## code template for IJoinData2 implementation
##class IJoinData2_Impl(object):
##    def Application(self, rhs):
##        u'The application to which this window belongs (Optional).'
##        #return 
##
##    def Layer(self, rhs):
##        u'Primary layer to join from (removes standalone table setting).'
##        #return 
##
##    def UpdateUIControls(self):
##        u'Updates all UI controls (used internally only).'
##        #return 
##
##    def StandaloneTable(self, rhs):
##        u'Primary table to join from (removes layer setting).'
##        #return 
##
##    def DoModal(self, parentWindow):
##        u'Shows modal window.'
##        #return 
##

class LasDatasetIdentifyObject(CoClass):
    u'Provides programmatic access to LasDataset layer identify object.'
    _reg_clsid_ = GUID('{C63C2295-6033-42FF-A47B-40B26E1B3D73}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
LasDatasetIdentifyObject._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IIdentifyObj, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IIdentifyObject]

class IDatasetFilter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Filter for dataset inclusion.'
    _iid_ = GUID('{A21772E4-575C-4F74-A5AD-2FCE96597BDA}')
    _idlflags_ = ['oleautomation']
IDatasetFilter._methods_ = [
    COMMETHOD([helpstring(u'Indicates if the dataset should be included.')], HRESULT, 'ApplyFilter',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataset), 'Dataset' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'includeDataset' )),
]
################################################################
## code template for IDatasetFilter implementation
##class IDatasetFilter_Impl(object):
##    def ApplyFilter(self, Dataset):
##        u'Indicates if the dataset should be included.'
##        #return includeDataset
##

class TinGxBrowserFactory(CoClass):
    u'The TIN GX Browser Factory is used to help look for TINs on disk.'
    _reg_clsid_ = GUID('{60236540-0003-11D2-B1CA-00C04F8EDEFF}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
TinGxBrowserFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayerFactory]

class DataViewPropertyPage(CoClass):
    u'Property page for Data view properties.'
    _reg_clsid_ = GUID('{421F13D2-007F-11D2-A253-080009B6F22B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
DataViewPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class LasDatasetGxBrowserFactory(CoClass):
    u'The LasDataset GX Browser Factory is used to help look for LasDatasets.'
    _reg_clsid_ = GUID('{A7ECF5F5-BDDE-4487-A8DD-C604A2DB5960}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
LasDatasetGxBrowserFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayerFactory]

class IMSLayersPropertyPage(CoClass):
    u'IMS Map Layers property page.'
    _reg_clsid_ = GUID('{1C22EB67-DA97-11D3-9FF6-00C04F6BC6A5}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
IMSLayersPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class IMxApplication3(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Mx Application.'
    _iid_ = GUID('{0522A5F4-487C-11D0-98BD-00805F7CED21}')
    _idlflags_ = ['oleautomation']
IMxApplication3._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The current printer settings.')], HRESULT, 'Printer',
              ( ['in'], POINTER(comtypes.gen._7DB92CEC_CB65_420A_8737_FCD0722FD436_0_10_2.IPrinter), 'Printer' )),
    COMMETHOD(['propget', helpstring(u'The current printer settings.')], HRESULT, 'Printer',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._7DB92CEC_CB65_420A_8737_FCD0722FD436_0_10_2.IPrinter)), 'Printer' )),
    COMMETHOD(['propget', helpstring(u'The current paper settings.')], HRESULT, 'Paper',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._7DB92CEC_CB65_420A_8737_FCD0722FD436_0_10_2.IPaper)), 'Paper' )),
    COMMETHOD(['propget', helpstring(u'The application display.')], HRESULT, 'Display',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IAppDisplay)), 'Display' )),
    COMMETHOD(['propget', helpstring(u'The selection environment.')], HRESULT, 'SelectionEnvironment',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ISelectionEnvironment)), 'env' )),
    COMMETHOD([helpstring(u'Exports the current document.')], HRESULT, 'Export'),
    COMMETHOD([helpstring(u'Copies the current view to the clipboard.')], HRESULT, 'CopyToClipboard'),
    COMMETHOD(['propput', helpstring(u'Pause display updates.')], HRESULT, 'PauseDrawing',
              ( ['in'], VARIANT_BOOL, 'flag' )),
    COMMETHOD(['propget', helpstring(u'Pause display updates.')], HRESULT, 'PauseDrawing',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD(['propput', helpstring(u'Show or hide the status bar.')], HRESULT, 'ShowStatusBar',
              ( ['in'], VARIANT_BOOL, 'flag' )),
    COMMETHOD(['propget', helpstring(u'Show or hide the status bar.')], HRESULT, 'ShowStatusBar',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
]
################################################################
## code template for IMxApplication3 implementation
##class IMxApplication3_Impl(object):
##    def CopyToClipboard(self):
##        u'Copies the current view to the clipboard.'
##        #return 
##
##    @property
##    def Printer(self, Printer):
##        u'The current printer settings.'
##        #return 
##
##    def _get(self):
##        u'Show or hide the status bar.'
##        #return flag
##    def _set(self, flag):
##        u'Show or hide the status bar.'
##    ShowStatusBar = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Pause display updates.'
##        #return flag
##    def _set(self, flag):
##        u'Pause display updates.'
##    PauseDrawing = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def SelectionEnvironment(self):
##        u'The selection environment.'
##        #return env
##
##    @property
##    def Paper(self):
##        u'The current paper settings.'
##        #return Paper
##
##    def Export(self):
##        u'Exports the current document.'
##        #return 
##
##    @property
##    def Display(self):
##        u'The application display.'
##        #return Display
##

class IContentsViewSelection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control table of contents views.'
    _iid_ = GUID('{30BE80A5-6158-4B49-9077-61024CE6F746}')
    _idlflags_ = ['oleautomation']
IContentsViewSelection._methods_ = [
    COMMETHOD(['propget', helpstring(u'Selection set containing the highlighted items in contents view.')], HRESULT, 'SelectedItems',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISet)), 'Selection' )),
    COMMETHOD(['propput', helpstring(u'Selection set containing the highlighted items in contents view.')], HRESULT, 'SelectedItems',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISet), 'Selection' )),
]
################################################################
## code template for IContentsViewSelection implementation
##class IContentsViewSelection_Impl(object):
##    def _get(self):
##        u'Selection set containing the highlighted items in contents view.'
##        #return Selection
##    def _set(self, Selection):
##        u'Selection set containing the highlighted items in contents view.'
##    SelectedItems = property(_get, _set, doc = _set.__doc__)
##

class TOCGeneralPropertyPage(CoClass):
    u'Property page for Table Of Contents window general properties.'
    _reg_clsid_ = GUID('{4AE14F92-28A7-4E4B-84D5-CA723C6D1B6B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
TOCGeneralPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class IMSSubLayerContextAnalyzer(CoClass):
    u'IMS SubLayer Context Analyzer.'
    _reg_clsid_ = GUID('{1ABF8E95-A0A8-4DAC-A6BD-5172AC35BAE1}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
IMSSubLayerContextAnalyzer._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IContextAnalyzer]

class IAggregateOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that allows you to specify the types of aggregation that will be applied to all numeric fields during an aggregate spatial join.'
    _iid_ = GUID('{12B35C90-010F-11D4-A692-0008C7D3AE8D}')
    _idlflags_ = ['oleautomation']
IAggregateOptions._methods_ = [
    COMMETHOD(['propput', helpstring(u'Indicates if the sum of all numeric fields in the join feature class is appended to the result.')], HRESULT, 'IsSum',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the average of all numeric fields in the join feature class is appended to the result.')], HRESULT, 'IsAverage',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the count of all numeric fields in the join feature class is appended to the result.')], HRESULT, 'IsCount',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the maximum of all numeric fields in the join feature class is appended to the result.')], HRESULT, 'IsMax',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the minimum of all numeric fields in the join feature class is appended to the result.')], HRESULT, 'IsMin',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the standard deviation of all numeric fields in the join feature class is appended to the result.')], HRESULT, 'IsStdDev',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the variance of all numeric fields in the join feature class is appended to the result.')], HRESULT, 'IsVar',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
]
################################################################
## code template for IAggregateOptions implementation
##class IAggregateOptions_Impl(object):
##    def _set(self, rhs):
##        u'Indicates if the maximum of all numeric fields in the join feature class is appended to the result.'
##    IsMax = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Indicates if the minimum of all numeric fields in the join feature class is appended to the result.'
##    IsMin = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Indicates if the average of all numeric fields in the join feature class is appended to the result.'
##    IsAverage = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Indicates if the standard deviation of all numeric fields in the join feature class is appended to the result.'
##    IsStdDev = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Indicates if the sum of all numeric fields in the join feature class is appended to the result.'
##    IsSum = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Indicates if the variance of all numeric fields in the join feature class is appended to the result.'
##    IsVar = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Indicates if the count of all numeric fields in the join feature class is appended to the result.'
##    IsCount = property(fset = _set, doc = _set.__doc__)
##

class IFindWindow(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Find Window. Allows you to search for features/addresses/etc. Deprecated. Please consider using the IFind interface in the Carto library instead.'
    _iid_ = GUID('{212A710B-4C00-11D2-A079-0000F8775BF9}')
    _idlflags_ = ['oleautomation']
IFindWindow._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The application to which the window belongs.')], HRESULT, 'Application',
              ( ['in'], POINTER(IDispatch), 'pApplication' )),
    COMMETHOD(['hidden', helpstring(u'The application to which the window belongs.'), 'propget'], HRESULT, 'Application',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IApplication)), 'pApplication' )),
    COMMETHOD([helpstring(u'Shows or hides the window.')], HRESULT, 'Show',
              ( ['in'], VARIANT_BOOL, 'Show' )),
]
################################################################
## code template for IFindWindow implementation
##class IFindWindow_Impl(object):
##    @property
##    def Application(self, pApplication):
##        u'The application to which the window belongs.'
##        #return 
##
##    def Show(self, Show):
##        u'Shows or hides the window.'
##        #return 
##

class IGNetExtension(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Geography Network Extension.'
    _iid_ = GUID('{9CDBD931-2ADE-4DED-938E-0E7E73588F4D}')
    _idlflags_ = ['oleautomation']
IGNetExtension._methods_ = [
    COMMETHOD([helpstring(u'Shows/hides the GNet dialog.')], HRESULT, 'ShowWindow',
              ( ['in'], VARIANT_BOOL, 'Show' )),
]
################################################################
## code template for IGNetExtension implementation
##class IGNetExtension_Impl(object):
##    def ShowWindow(self, Show):
##        u'Shows/hides the GNet dialog.'
##        #return 
##

class GNetExtension(CoClass):
    u'GNet Extension.'
    _reg_clsid_ = GUID('{03FB6AFF-E277-40A6-8824-A670EE542718}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
GNetExtension._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IExtension, IGNetExtension]

class LayerEffectsEnvironment(CoClass):
    u'Singleton instance of the Layer Effects Environment.'
    _reg_clsid_ = GUID('{377ABA22-2019-11D3-9F97-00C04F6BC78E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
class ILayerEffectsEnvironment3(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Layer Effects Environment.'
    _iid_ = GUID('{5AFA7340-1EEC-4EB8-9E15-B414DF0FF8EA}')
    _idlflags_ = ['oleautomation']
LayerEffectsEnvironment._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ILayerEffectsEnvironment, ILayerEffectsEnvironment2, ILayerEffectsEnvironment3]

class LayoutViewPropertyPage(CoClass):
    u'Property page for Layout view properties.'
    _reg_clsid_ = GUID('{421F13D3-007F-11D2-A253-080009B6F22B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
LayoutViewPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class IMSMapLayerSourcePropertyPage(CoClass):
    u'IMS Map Layer source property page.'
    _reg_clsid_ = GUID('{429ED6FF-DB20-11D3-9FF6-00C04F6BC6A5}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
IMSMapLayerSourcePropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class GNetCommandHandler(CoClass):
    u'GNet Command Handler.'
    _reg_clsid_ = GUID('{A13A8F40-912B-4161-99D4-1AE05A7B1394}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
GNetCommandHandler._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IDDECommandHandler]

class DataGraphMxDocumentDropTarget(CoClass):
    u'Supports data graph drag-and-drop functionality in ArcMap.'
    _reg_clsid_ = GUID('{9168AC01-5DBE-11D4-A689-0008C7DF88DB}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
class IMxDocumentDropTarget(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the MxDocument Drop Target.'
    _iid_ = GUID('{9168ABFE-5DBE-11D4-A689-0008C7DF88DB}')
    _idlflags_ = ['oleautomation']
DataGraphMxDocumentDropTarget._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMxDocumentDropTarget]

class IDataGraphWindow2(IDataWindow):
    _case_insensitive_ = True
    u'Provides access to members that control the DataGraph Window.'
    _iid_ = GUID('{875AE97A-A973-4102-B4DD-6E8FE8ACA893}')
    _idlflags_ = ['oleautomation']
IDataGraphWindow2._methods_ = [
    COMMETHOD(['propget', helpstring(u'The window that uses data graph.')], HRESULT, 'DataGraphBase',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDataGraphBase)), 'ppDataGraphBase' )),
    COMMETHOD(['propputref', helpstring(u'The window that uses data graph.')], HRESULT, 'DataGraphBase',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDataGraphBase), 'ppDataGraphBase' )),
]
################################################################
## code template for IDataGraphWindow2 implementation
##class IDataGraphWindow2_Impl(object):
##    def DataGraphBase(self, ppDataGraphBase):
##        u'The window that uses data graph.'
##        #return 
##

class TableWindow(CoClass):
    u'Window to display Tables in ArcMap.'
    _reg_clsid_ = GUID('{C671B641-83B9-11D2-850C-0000F875B9C6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
class IDataWindowEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to events that occur in a data window.'
    _iid_ = GUID('{FA277DC5-6059-41CF-A86F-69FE3881544D}')
    _idlflags_ = ['oleautomation']
class ITableWindow3(ITableWindow2):
    _case_insensitive_ = True
    u'Provides access to members that extend ITableWindow functionality to work with dockable tables.'
    _iid_ = GUID('{195E57B7-CB45-47DC-853F-2B4E8D9B4BD6}')
    _idlflags_ = ['oleautomation']
TableWindow._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ITableWindow, IDataWindow, IDataWindow2, ITableWindow2, ITableWindow3, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.ITimeDisplayEvents]
TableWindow._outgoing_interfaces_ = [IDataWindowEvents]

ITableDockWindowAdmin._methods_ = [
    COMMETHOD([helpstring(u'Show Table pane.')], HRESULT, 'Show',
              ( ['in'], POINTER(ITableWindow), 'pTableWindow' ),
              ( ['in'], VARIANT_BOOL, 'Show' )),
    COMMETHOD([helpstring(u'Close table pane.')], HRESULT, 'Close',
              ( ['in'], POINTER(ITableWindow), 'pTableWindow' )),
    COMMETHOD([helpstring(u'Close all table panes.')], HRESULT, 'CloseAllTables'),
    COMMETHOD([helpstring(u'Is Table window open.')], HRESULT, 'IsOpen',
              ( ['in'], POINTER(ITableWindow), 'pTableWindow' ),
              ( ['out'], POINTER(VARIANT_BOOL), 'pIsOpen' )),
    COMMETHOD([helpstring(u'Is table already being displayed.')], HRESULT, 'FindViaTable',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable), 'pTable' ),
              ( ['in'], VARIANT_BOOL, 'ShowSelected' ),
              ( ['retval', 'out'], POINTER(POINTER(ITableWindow)), 'ppTableWindow' )),
    COMMETHOD([helpstring(u'Is table (of a layer) already being displayed.')], HRESULT, 'FindViaLayer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer), 'pLayer' ),
              ( ['retval', 'out'], POINTER(POINTER(ITableWindow)), 'ppTableWindow' )),
    COMMETHOD([helpstring(u'Is table (of a featurelayer) already being displayed.')], HRESULT, 'FindViaFeatureLayer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IFeatureLayer), 'pFeatureLayer' ),
              ( ['in'], VARIANT_BOOL, 'ShowSelected' ),
              ( ['retval', 'out'], POINTER(POINTER(ITableWindow)), 'ppTableWindow' )),
    COMMETHOD([helpstring(u'Is table (of a standalonetable) already being displayed.')], HRESULT, 'FindViaStandaloneTable',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IStandaloneTable), 'pStandaloneTable' ),
              ( ['retval', 'out'], POINTER(POINTER(ITableWindow)), 'ppTableWindow' )),
    COMMETHOD([helpstring(u'Is table already being displayed.')], HRESULT, 'FindViaUnknown',
              ( ['in'], POINTER(IUnknown), 'pUnknown' ),
              ( ['retval', 'out'], POINTER(POINTER(ITableWindow)), 'ppTableWindow' )),
    COMMETHOD([helpstring(u'Gets all the open table windows.')], HRESULT, 'FindOpenTableWindows',
              ( ['out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISet)), 'pTableWindows' )),
    COMMETHOD([helpstring(u'Update the pane title.')], HRESULT, 'UpdateTitle',
              ( ['in'], POINTER(ITableWindow), 'pTableWindow' )),
    COMMETHOD([helpstring(u'Set the active window.')], HRESULT, 'SetActiveWindow',
              ( ['in'], POINTER(ITableWindow), 'pTableWindow' )),
    COMMETHOD([helpstring(u'Show next table pane.')], HRESULT, 'ShowNextTable',
              ( ['in'], VARIANT_BOOL, 'forward' )),
    COMMETHOD(['propget', helpstring(u'Gets the active table window.')], HRESULT, 'ActiveTableWindow',
              ( ['retval', 'out'], POINTER(POINTER(ITableWindow)), 'ppTableWindow' )),
]
################################################################
## code template for ITableDockWindowAdmin implementation
##class ITableDockWindowAdmin_Impl(object):
##    def FindViaUnknown(self, pUnknown):
##        u'Is table already being displayed.'
##        #return ppTableWindow
##
##    def FindViaLayer(self, pLayer):
##        u'Is table (of a layer) already being displayed.'
##        #return ppTableWindow
##
##    def UpdateTitle(self, pTableWindow):
##        u'Update the pane title.'
##        #return 
##
##    def IsOpen(self, pTableWindow):
##        u'Is Table window open.'
##        #return pIsOpen
##
##    def Show(self, pTableWindow, Show):
##        u'Show Table pane.'
##        #return 
##
##    def FindViaStandaloneTable(self, pStandaloneTable):
##        u'Is table (of a standalonetable) already being displayed.'
##        #return ppTableWindow
##
##    @property
##    def ActiveTableWindow(self):
##        u'Gets the active table window.'
##        #return ppTableWindow
##
##    def CloseAllTables(self):
##        u'Close all table panes.'
##        #return 
##
##    def ShowNextTable(self, forward):
##        u'Show next table pane.'
##        #return 
##
##    def FindViaTable(self, pTable, ShowSelected):
##        u'Is table already being displayed.'
##        #return ppTableWindow
##
##    def Close(self, pTableWindow):
##        u'Close table pane.'
##        #return 
##
##    def SetActiveWindow(self, pTableWindow):
##        u'Set the active window.'
##        #return 
##
##    def FindOpenTableWindows(self):
##        u'Gets all the open table windows.'
##        #return pTableWindows
##
##    def FindViaFeatureLayer(self, pFeatureLayer, ShowSelected):
##        u'Is table (of a featurelayer) already being displayed.'
##        #return ppTableWindow
##

class TemplateStartupDialog(CoClass):
    u'Startup dialog that lets you choose a template.'
    _reg_clsid_ = GUID('{CA691DD3-8A14-11D2-AE6C-080009EC732A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
class IStartupDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Startup Dialog.'
    _iid_ = GUID('{CF008475-88BC-11D2-AE6A-080009EC732A}')
    _idlflags_ = ['oleautomation']
class IStartupDialog3(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to more members that control the Startup Dialog.'
    _iid_ = GUID('{CE7CBE9A-7996-476A-80DD-06AD2B404D4C}')
    _idlflags_ = ['oleautomation']
TemplateStartupDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IStartupDialog, IStartupDialog3]

class TOCPatchesPropertyPage(CoClass):
    u'Property page for Table Of Contents window patch properties.'
    _reg_clsid_ = GUID('{C432BA87-E1C0-469B-BE8E-68CE9A56AAD9}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
TOCPatchesPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class IMSLayerFactory(CoClass):
    u'IMS Layer Factory.'
    _reg_clsid_ = GUID('{8313C3DE-5874-4AAA-9F5D-BF195E5C547C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
IMSLayerFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayerFactory]

class IMSPropsPropertyPage(CoClass):
    u'IMS properties property page.'
    _reg_clsid_ = GUID('{411DFB51-64C3-4314-A34A-B9744CB2CA7C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
IMSPropsPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class RemoveLayersOperation(CoClass):
    u'Remove Layers Operation.'
    _reg_clsid_ = GUID('{1A216B2F-1B8C-4E41-B6C0-4541D1E696E7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
class IRemoveLayersOperation(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Remove layers operation.'
    _iid_ = GUID('{EFAA43D7-78C4-4990-B829-B2D288A17DA3}')
    _idlflags_ = ['oleautomation']
RemoveLayersOperation._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IOperation, IRemoveLayersOperation]

class AddLayersOperation(CoClass):
    u'Add Layers Operation.'
    _reg_clsid_ = GUID('{85B6B052-EA58-4E12-9C70-E2F9CC835EED}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
class IAddLayersOperation(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Add layers operation.'
    _iid_ = GUID('{1AC6F042-C7C8-464B-BB0F-6FC5A7F7C12E}')
    _idlflags_ = ['oleautomation']
AddLayersOperation._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IOperation, IAddLayersOperation]

class TOCDisplayView(CoClass):
    u'Esri TOC Display View.'
    _reg_clsid_ = GUID('{FDDB19F0-CB6F-11D2-9F38-00C04F6BC78E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
class IContentsView(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control table of contents views.'
    _iid_ = GUID('{FDDB19EF-CB6F-11D2-9F38-00C04F6BC78E}')
    _idlflags_ = ['oleautomation']
TOCDisplayView._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IContentsView, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IComPropertySheetEvents, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IActiveViewEvents, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, IContentsViewSelection]

class TOCDockableWindow(CoClass):
    u'Esri TOC Dockable Window.'
    _reg_clsid_ = GUID('{368131A0-F15F-11D3-A67E-0008C7DF97B9}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
TOCDockableWindow._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IDockableWindowDef, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IDockableWindowImageDef, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IDockableWindowInitialPlacement]

class GroupLayersOperation(CoClass):
    u'Group Layer Operation.'
    _reg_clsid_ = GUID('{1AFA5EAD-29C4-4BAB-B310-6B56200BEA56}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
GroupLayersOperation._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IOperation, IGroupLayersOperation]

class UngroupLayerOperation(CoClass):
    u'Ungroup Layer Operation.'
    _reg_clsid_ = GUID('{DC0FE382-2B7F-4209-B6A9-3CED06F850FC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
class IUngroupLayerOperation(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Ungroup layers operation.'
    _iid_ = GUID('{0C33B683-C94B-401F-927C-A3F8FBA76683}')
    _idlflags_ = ['oleautomation']
UngroupLayerOperation._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IOperation, IUngroupLayerOperation]

class MapServerLayerCachePropertyPage(CoClass):
    u"Property page for showing a map server layer's local cache properties."
    _reg_clsid_ = GUID('{E65B0AD9-E470-421B-B4D0-1BD8231D4F83}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
MapServerLayerCachePropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class GpsExtension(CoClass):
    u'The GPS extension object.'
    _reg_clsid_ = GUID('{C994BFE6-47F1-4BAC-8F35-0743C7576673}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
class IGpsExtension(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to GPS Extension properties.'
    _iid_ = GUID('{533F9D03-740C-4D63-BB43-641336DD3302}')
    _idlflags_ = ['oleautomation']
GpsExtension._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IExtension, IGpsExtension, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, IDocumentEvents]

class IBasicDocumentDefaultSymbols(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control Default basic symbols for the document.'
    _iid_ = GUID('{BAF98C1C-6E13-11D4-AB81-0008C73FD50C}')
    _idlflags_ = ['oleautomation']
IBasicDocumentDefaultSymbols._methods_ = [
    COMMETHOD(['propput', helpstring(u'Default Fill Symbol.')], HRESULT, 'FillSymbol',
              ( ['in'], POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IFillSymbol), 'lSymbol' )),
    COMMETHOD(['propget', helpstring(u'Default Fill Symbol.')], HRESULT, 'FillSymbol',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IFillSymbol)), 'lSymbol' )),
    COMMETHOD(['propput', helpstring(u'Default Line Symbol.')], HRESULT, 'LineSymbol',
              ( ['in'], POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.ILineSymbol), 'LineSymbol' )),
    COMMETHOD(['propget', helpstring(u'Default Line Symbol.')], HRESULT, 'LineSymbol',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.ILineSymbol)), 'LineSymbol' )),
    COMMETHOD(['propput', helpstring(u'Default Marker Symbol.')], HRESULT, 'MarkerSymbol',
              ( ['in'], POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IMarkerSymbol), 'MarkerSymbol' )),
    COMMETHOD(['propget', helpstring(u'Default Marker Symbol.')], HRESULT, 'MarkerSymbol',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IMarkerSymbol)), 'MarkerSymbol' )),
    COMMETHOD(['propput', helpstring(u'Default Area Patch.')], HRESULT, 'AreaPatch',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IAreaPatch), 'patch' )),
    COMMETHOD(['propget', helpstring(u'Default Area Patch.')], HRESULT, 'AreaPatch',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IAreaPatch)), 'patch' )),
    COMMETHOD(['propput', helpstring(u'Default Line Patch.')], HRESULT, 'LinePatch',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILinePatch), 'patch' )),
    COMMETHOD(['propget', helpstring(u'Default Line Patch.')], HRESULT, 'LinePatch',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILinePatch)), 'patch' )),
    COMMETHOD(['propput', helpstring(u'Default Patch Width in Points.')], HRESULT, 'PatchWidth',
              ( ['in'], c_double, 'widthPts' )),
    COMMETHOD(['propget', helpstring(u'Default Patch Width in Points.')], HRESULT, 'PatchWidth',
              ( ['retval', 'out'], POINTER(c_double), 'widthPts' )),
    COMMETHOD(['propput', helpstring(u'Default Patch Height in Points.')], HRESULT, 'PatchHeight',
              ( ['in'], c_double, 'heightPts' )),
    COMMETHOD(['propget', helpstring(u'Default Patch Height in Points.')], HRESULT, 'PatchHeight',
              ( ['retval', 'out'], POINTER(c_double), 'heightPts' )),
    COMMETHOD(['propput', helpstring(u'Custom TOC Font.')], HRESULT, 'CustomTOCFont',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IFontDisp), 'font' )),
    COMMETHOD(['propget', helpstring(u'Custom TOC Font.')], HRESULT, 'CustomTOCFont',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IFontDisp)), 'font' )),
    COMMETHOD(['propput', helpstring(u'Custom TOC Font Size in Points.')], HRESULT, 'CustomTOCFontSize',
              ( ['in'], c_double, 'fontSizePts' )),
    COMMETHOD(['propget', helpstring(u'Custom TOC Font Size in Points.')], HRESULT, 'CustomTOCFontSize',
              ( ['retval', 'out'], POINTER(c_double), 'fontSizePts' )),
]
################################################################
## code template for IBasicDocumentDefaultSymbols implementation
##class IBasicDocumentDefaultSymbols_Impl(object):
##    def _get(self):
##        u'Default Patch Width in Points.'
##        #return widthPts
##    def _set(self, widthPts):
##        u'Default Patch Width in Points.'
##    PatchWidth = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Default Line Patch.'
##        #return patch
##    def _set(self, patch):
##        u'Default Line Patch.'
##    LinePatch = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Default Patch Height in Points.'
##        #return heightPts
##    def _set(self, heightPts):
##        u'Default Patch Height in Points.'
##    PatchHeight = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Default Fill Symbol.'
##        #return lSymbol
##    def _set(self, lSymbol):
##        u'Default Fill Symbol.'
##    FillSymbol = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Custom TOC Font.'
##        #return font
##    def _set(self, font):
##        u'Custom TOC Font.'
##    CustomTOCFont = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Default Marker Symbol.'
##        #return MarkerSymbol
##    def _set(self, MarkerSymbol):
##        u'Default Marker Symbol.'
##    MarkerSymbol = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Default Line Symbol.'
##        #return LineSymbol
##    def _set(self, LineSymbol):
##        u'Default Line Symbol.'
##    LineSymbol = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Default Area Patch.'
##        #return patch
##    def _set(self, patch):
##        u'Default Area Patch.'
##    AreaPatch = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Custom TOC Font Size in Points.'
##        #return fontSizePts
##    def _set(self, fontSizePts):
##        u'Custom TOC Font Size in Points.'
##    CustomTOCFontSize = property(_get, _set, doc = _set.__doc__)
##

class LayersClipboardFormat(CoClass):
    u'Esri Layers Clipboard format.'
    _reg_clsid_ = GUID('{62A370EF-59E9-41E3-85F1-D4B5074AACDD}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
class IClipboardFormat(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the ClipBoard Format.'
    _iid_ = GUID('{52BB5361-947E-11D2-ACFF-0000F87808EE}')
    _idlflags_ = ['oleautomation']
LayersClipboardFormat._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IClipboardFormat]

IGpsExtension._methods_ = [
    COMMETHOD(['propget', helpstring(u'The RealTimeFeedManager object associated with the extension.')], HRESULT, 'RealTimeFeedManager',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IRealTimeFeedManager)), 'ppRTFManager' )),
]
################################################################
## code template for IGpsExtension implementation
##class IGpsExtension_Impl(object):
##    @property
##    def RealTimeFeedManager(self):
##        u'The RealTimeFeedManager object associated with the extension.'
##        #return ppRTFManager
##

class ProgressBar(CoClass):
    u'ProgressBar object.'
    _reg_clsid_ = GUID('{9ACE6D77-D641-4A81-940B-E31C2E8BBCD2}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
ProgressBar._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStepProgressor, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IProgressor]

class ProgressDialog(CoClass):
    u'Progress dialog object.'
    _reg_clsid_ = GUID('{F5140146-D2E5-4F7D-8E81-843308BD60C4}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
ProgressDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IProgressor, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IProgressDialog, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IProgressDialog2, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStepProgressor]

class TOCLegendSelectionView(CoClass):
    _reg_clsid_ = GUID('{AF395E08-A159-4472-8164-7E6B284ADF8A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
TOCLegendSelectionView._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IContentsView]

class TOCLegendDisplayView(CoClass):
    _reg_clsid_ = GUID('{74429E76-DC73-4C84-A6EE-50F9643A19EB}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
TOCLegendDisplayView._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IContentsView]

class GpsPositionDialog(CoClass):
    u'Display GPS Position information.'
    _reg_clsid_ = GUID('{F56723F3-063D-4B4A-89B9-F03AFADF2078}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
class IGpsPositionDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control GPS position dialog.'
    _iid_ = GUID('{62BD896A-A9FD-489D-87BC-9086CAB22930}')
    _idlflags_ = ['oleautomation']
GpsPositionDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGpsPositionDialog, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IRealTimeFeedEvents]

class TOCCatalogView(CoClass):
    u'Esri TOC Catalog View.'
    _reg_clsid_ = GUID('{089874FB-CC18-11D2-9F39-00C04F6BC78E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
TOCCatalogView._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IContentsView, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IComPropertySheetEvents, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IActiveViewEvents, IDocumentEvents, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, IContentsViewSelection]

class MxStatusBar(CoClass):
    u'MxStatusBar object.'
    _reg_clsid_ = GUID('{2FDE4861-D8FE-48CD-B526-A5E565771B06}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
MxStatusBar._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStatusBar]

IGpsPositionDialog._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The RealTimeFeed which is used to display the GPS position information.')], HRESULT, 'RealTimeFeed',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IRealTimeFeed), 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the GPS position dialog is displayed.')], HRESULT, 'Visible',
              ( ['in'], VARIANT_BOOL, 'pShow' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the GPS position dialog is displayed.')], HRESULT, 'Visible',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pShow' )),
]
################################################################
## code template for IGpsPositionDialog implementation
##class IGpsPositionDialog_Impl(object):
##    def _get(self):
##        u'Indicates if the GPS position dialog is displayed.'
##        #return pShow
##    def _set(self, pShow):
##        u'Indicates if the GPS position dialog is displayed.'
##    Visible = property(_get, _set, doc = _set.__doc__)
##
##    def RealTimeFeed(self, rhs):
##        u'The RealTimeFeed which is used to display the GPS position information.'
##        #return 
##

class GpsLogFilter(CoClass):
    u'The GPS Log Filter.'
    _reg_clsid_ = GUID('{768D0AA1-B5A9-41DF-A425-A1D2D6F95BB3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
GpsLogFilter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxObjectFilter]

class ReportSelection(CoClass):
    u'Captures selection change, and reports this on the status bar.'
    _reg_clsid_ = GUID('{69DE6E2E-F9A2-11D2-9F4C-00C04F6BC886}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
ReportSelection._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDocumentEvents, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IActiveViewEvents]

class TOCSelectionView(CoClass):
    u'Esri TOC Selection View.'
    _reg_clsid_ = GUID('{42559942-8575-4083-B76B-DFBED25B0143}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
TOCSelectionView._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IContentsView, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IActiveViewEvents, IDocumentEvents]

class WMSLayerSourcePropertyPage(CoClass):
    u"Property page for showing a map server layer's source information."
    _reg_clsid_ = GUID('{26D10423-B5C2-47D9-91EB-006A720B809C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
WMSLayerSourcePropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class MapViewCommandsMenuItems(CoClass):
    u'Map View Commands Menu Items.'
    _reg_clsid_ = GUID('{8D0CFE2D-9972-4E46-A404-4EC9EF81A472}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
MapViewCommandsMenuItems._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.ICommand]

class WMSLayerStylePropertyPage(CoClass):
    u"Property page for showing wms sub layer's properties."
    _reg_clsid_ = GUID('{CB9FEE4C-DD93-4E1C-90E7-4618709F6453}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
WMSLayerStylePropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class GroupLayerContextAnalyzer(CoClass):
    u'Group Layer Context Analyzer.'
    _reg_clsid_ = GUID('{FB113BE7-69F5-4F14-AFDE-77B8081D4D7A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
GroupLayerContextAnalyzer._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IContextAnalyzer]

class MapViewCommandsContextAnalyzer(CoClass):
    u'Map View Commands Context Analyzer.'
    _reg_clsid_ = GUID('{A28E3E4A-46F7-4AEC-B95D-60AB00F9A130}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
MapViewCommandsContextAnalyzer._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IContextAnalyzer]

class MapViewCommandsContextMenu(CoClass):
    u'Map View Commands Context Menu.'
    _reg_clsid_ = GUID('{3846A5B5-D3F8-44CB-BFA3-A5C30F4E535F}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
MapViewCommandsContextMenu._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IMenuDef]

class WMSLayerAdvancedPropertyPage(CoClass):
    u"Property page for showing a map server layer's advanced properties."
    _reg_clsid_ = GUID('{39B5C9FF-DD32-446B-8BE8-70FD420B876C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
WMSLayerAdvancedPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class WMSSublayersPropertyPage(CoClass):
    u"Property page for showing a map server layer's sublayer information."
    _reg_clsid_ = GUID('{063BA6AC-3510-4125-977F-C43BF0578DE0}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
WMSSublayersPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class TableProperty(CoClass):
    u'Table window property.'
    _reg_clsid_ = GUID('{4657D952-5FFB-11D3-9F6C-00C04F6BC886}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
class ITableProperty(comtypes.gen._4A9C9ED7_F7DB_4614_B480_A5D265C961FC_0_10_2.ITableViewInfo):
    _case_insensitive_ = True
    u'Provides access to members that control Table window properties.'
    _iid_ = GUID('{4657D951-5FFB-11D3-9F6C-00C04F6BC886}')
    _idlflags_ = ['oleautomation']
class ITableProperty2(comtypes.gen._4A9C9ED7_F7DB_4614_B480_A5D265C961FC_0_10_2.ITableViewInfo):
    _case_insensitive_ = True
    u'Provides access to members that control Linked table window properties.'
    _iid_ = GUID('{1CF1C3E1-6C5F-4E61-A802-FA00A9E33A9F}')
    _idlflags_ = ['oleautomation']
class ITableProperty3(comtypes.gen._4A9C9ED7_F7DB_4614_B480_A5D265C961FC_0_10_2.ITableViewInfo):
    _case_insensitive_ = True
    u'Provides access to members that control Linked table window properties.'
    _iid_ = GUID('{890F9558-6292-4903-9C4D-4F033CAB5994}')
    _idlflags_ = ['oleautomation']
TableProperty._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ITableProperty, ITableProperty2, ITableProperty3, comtypes.gen._4A9C9ED7_F7DB_4614_B480_A5D265C961FC_0_10_2.ITableSelectionColor, comtypes.gen._4A9C9ED7_F7DB_4614_B480_A5D265C961FC_0_10_2.ITableCharacteristics, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream]

class MetadataViewWindow(CoClass):
    u"MetadataViewWindow class used to display the metadata of selected layer's data source."
    _reg_clsid_ = GUID('{513FB19D-AC27-4AD0-9101-1C3DC4ADD609}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
class IMetadataViewWindow3(IMetadataViewWindow2):
    _case_insensitive_ = True
    u'Provides access to members setting the Metadata View Window.'
    _iid_ = GUID('{83DAC7BA-9F42-465A-8530-BE77710E8F0B}')
    _idlflags_ = ['oleautomation']
MetadataViewWindow._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMetadataViewWindow, IMetadataViewWindow2, IMetadataViewWindow3, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IActiveViewEvents, IDocumentEvents]

class Maps(CoClass):
    u'Helper for working with the IMaps interface.'
    _reg_clsid_ = GUID('{81883183-A851-4AA8-97D4-BED00CF50503}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
Maps._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMaps]

class OleFrame(CoClass):
    u'The OLE frame.'
    _reg_clsid_ = GUID('{F6705E85-523B-11D1-86E7-0000F8751720}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
OleFrame._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IElement, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IElementProperties, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IElementProperties2, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IOleFrame, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IGraphicElement, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IBoundsProperties, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IFrameElement, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IFrameDraw, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IFrameProperties, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySupport, comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ITransform2D, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IElementShutdown]

class IContentsViewEdit(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control Contents View Edit.'
    _iid_ = GUID('{B0F32EAF-EBDB-11D3-9FDB-00C04F6BC78E}')
    _idlflags_ = ['oleautomation']
IContentsViewEdit._methods_ = [
    COMMETHOD([helpstring(u'Removes all current contents views.')], HRESULT, 'ClearContentsViews'),
    COMMETHOD([helpstring(u'Adds a contents view object to the TOC.')], HRESULT, 'AddContentsView',
              ( ['in'], POINTER(IContentsView), 'ContentsView' )),
]
################################################################
## code template for IContentsViewEdit implementation
##class IContentsViewEdit_Impl(object):
##    def AddContentsView(self, ContentsView):
##        u'Adds a contents view object to the TOC.'
##        #return 
##
##    def ClearContentsViews(self):
##        u'Removes all current contents views.'
##        #return 
##

IDataWindowFactory._methods_ = [
    COMMETHOD(['propget', helpstring(u'The name of objects created by this factory.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD([helpstring(u'Indicates if the window is available given the current application state.')], HRESULT, 'CanCreate',
              ( ['in'], POINTER(IDispatch), 'app' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'CanCreate' )),
    COMMETHOD([helpstring(u'Create a new floating window.')], HRESULT, 'Create',
              ( ['in'], POINTER(IDispatch), 'app' ),
              ( ['retval', 'out'], POINTER(POINTER(IDataWindow)), 'dataWindow' )),
]
################################################################
## code template for IDataWindowFactory implementation
##class IDataWindowFactory_Impl(object):
##    def Create(self, app):
##        u'Create a new floating window.'
##        #return dataWindow
##
##    def CanCreate(self, app):
##        u'Indicates if the window is available given the current application state.'
##        #return CanCreate
##
##    @property
##    def Name(self):
##        u'The name of objects created by this factory.'
##        #return Name
##

class Library(object):
    u'Esri ArcMapUI Object Library 10.2'
    name = u'esriArcMapUI'
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)

class OpenTableCommand(CoClass):
    u'Global Command that opens the table(s) associated to the current selection in the TOC.'
    _reg_clsid_ = GUID('{D75069B8-7534-4953-83AE-03E3EBFBD7F8}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
OpenTableCommand._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.ICommand]

class IStartupDialogSettings(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that contorl the behavior of the Getting Started window.'
    _iid_ = GUID('{7A2E7EB0-45AE-451B-8D5F-99BEF3DDFE32}')
    _idlflags_ = ['oleautomation']
IStartupDialogSettings._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if the startup window should be displayed.')], HRESULT, 'ShowStartup',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pShowStartup' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the last document should be opened.')], HRESULT, 'OpenLastDocument',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pOpenLast' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the Add Data dialog should be displayed.')], HRESULT, 'AddData',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pAddData' )),
    COMMETHOD(['propget', helpstring(u'The startup window prog id.')], HRESULT, 'ProgId',
              ( ['retval', 'out'], POINTER(BSTR), 'pProgID' )),
    COMMETHOD([helpstring(u'Loads the current values from the registry.')], HRESULT, 'Load'),
]
################################################################
## code template for IStartupDialogSettings implementation
##class IStartupDialogSettings_Impl(object):
##    def Load(self):
##        u'Loads the current values from the registry.'
##        #return 
##
##    @property
##    def ShowStartup(self):
##        u'Indicates if the startup window should be displayed.'
##        #return pShowStartup
##
##    @property
##    def OpenLastDocument(self):
##        u'Indicates if the last document should be opened.'
##        #return pOpenLast
##
##    @property
##    def ProgId(self):
##        u'The startup window prog id.'
##        #return pProgID
##
##    @property
##    def AddData(self):
##        u'Indicates if the Add Data dialog should be displayed.'
##        #return pAddData
##


# values for enumeration 'esriMxDefaultColorTypes'
esriMxTextColor = 0
esriMxFillColor = 1
esriMxLineColor = 2
esriMxMarkerColor = 3
esriMxDefaultColorTypes = c_int # enum

# values for enumeration 'esriMxDlgIDs'
esriMxDlgCustomize = 0
esriMxDlgStyleGallery = 1
esriMxDlgOverflowLabels = 2
esriMxDlgMacros = 3
esriMxDlgVBA = 4
esriMxDlgOptions = 5
esriMxDlgContents = 6
esriMxDlgZoom = 7
esriMxDlgPageSetup = 8
esriMxDlgPrintSetup = 9
esriMxDlgProperties = 10
esriMxDlgUnlockCustomization = 11
esriMxDlgLockCustomization = 12
esriMxDlgIDs = c_int # enum
class ImageAnalysisWindowCommand(CoClass):
    u'Command to open the Image Analysis Window.'
    _reg_clsid_ = GUID('{2106ABBA-A7C1-4CB9-8B10-097A647E7595}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
ImageAnalysisWindowCommand._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.ICommand]

class WMSIdentifyObject(CoClass):
    u'Provides programmatic access to a WMS map layer factory.'
    _reg_clsid_ = GUID('{78812421-9DBC-403C-9E4A-7E43AC8C8F0B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
WMSIdentifyObject._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IIdentifyObj, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IIdentifyObject, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IWMSIdentifyObject]

class WMSMapLayerFactory(CoClass):
    u'Provides programmatic access to a WMS map layer factory.'
    _reg_clsid_ = GUID('{23F7321F-0B67-4CE8-9743-3DDF25DFE331}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
WMSMapLayerFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayerFactory, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

class IMxDocument(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Mx Document.'
    _iid_ = GUID('{0522A5F1-487C-11D0-98BD-00805F7CED21}')
    _idlflags_ = ['oleautomation']
IContentsView._methods_ = [
    COMMETHOD(['propget', helpstring(u'The name of the contents view.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'The HWND of the contents view.')], HRESULT, 'hWnd',
              ( ['retval', 'out'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.OLE_HANDLE), 'hWnd' )),
    COMMETHOD([helpstring(u'Activates the contents view.')], HRESULT, 'Activate',
              ( ['in'], comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.OLE_HANDLE, 'parentHWnd' ),
              ( ['in'], POINTER(IMxDocument), 'Document' )),
    COMMETHOD([helpstring(u'Deactivates the contents view.')], HRESULT, 'Deactivate'),
    COMMETHOD([helpstring(u'Refreshes the contents view.  If a non-null item is specified, it refreshes only that item and its children.')], HRESULT, 'Refresh',
              ( ['in'], VARIANT, 'item' )),
    COMMETHOD(['propget', helpstring(u'The selected item (could be an enumerator).')], HRESULT, 'SelectedItem',
              ( ['retval', 'out'], POINTER(VARIANT), 'item' )),
    COMMETHOD(['propput', helpstring(u'The selected item (could be an enumerator).')], HRESULT, 'SelectedItem',
              ( ['in'], VARIANT, 'item' )),
    COMMETHOD([helpstring(u'Adds to the selected items.')], HRESULT, 'AddToSelectedItems',
              ( ['in'], VARIANT, 'item' )),
    COMMETHOD([helpstring(u'Removes an item from the selected items.')], HRESULT, 'RemoveFromSelectedItems',
              ( ['in'], VARIANT, 'item' )),
    COMMETHOD(['propget', helpstring(u'The context item (could be an enumerator).')], HRESULT, 'ContextItem',
              ( ['retval', 'out'], POINTER(VARIANT), 'item' )),
    COMMETHOD(['propput', helpstring(u'The context item (could be an enumerator).')], HRESULT, 'ContextItem',
              ( ['in'], VARIANT, 'item' )),
    COMMETHOD(['propget', helpstring(u'Indicates if lines are shown in the TOC tree.')], HRESULT, 'ShowLines',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Show' )),
    COMMETHOD(['propput', helpstring(u'Indicates if lines are shown in the TOC tree.')], HRESULT, 'ShowLines',
              ( ['in'], VARIANT_BOOL, 'Show' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the view is visible.')], HRESULT, 'Visible',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'vis' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the view is visible.')], HRESULT, 'Visible',
              ( ['in'], VARIANT_BOOL, 'vis' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the view is currently responding to events.')], HRESULT, 'ProcessEvents',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
]
################################################################
## code template for IContentsView implementation
##class IContentsView_Impl(object):
##    def AddToSelectedItems(self, item):
##        u'Adds to the selected items.'
##        #return 
##
##    def Activate(self, parentHWnd, Document):
##        u'Activates the contents view.'
##        #return 
##
##    @property
##    def Name(self):
##        u'The name of the contents view.'
##        #return Name
##
##    def _get(self):
##        u'The context item (could be an enumerator).'
##        #return item
##    def _set(self, item):
##        u'The context item (could be an enumerator).'
##    ContextItem = property(_get, _set, doc = _set.__doc__)
##
##    def Deactivate(self):
##        u'Deactivates the contents view.'
##        #return 
##
##    @property
##    def hWnd(self):
##        u'The HWND of the contents view.'
##        #return hWnd
##
##    def _get(self):
##        u'The selected item (could be an enumerator).'
##        #return item
##    def _set(self, item):
##        u'The selected item (could be an enumerator).'
##    SelectedItem = property(_get, _set, doc = _set.__doc__)
##
##    def Refresh(self, item):
##        u'Refreshes the contents view.  If a non-null item is specified, it refreshes only that item and its children.'
##        #return 
##
##    def _get(self):
##        u'Indicates if the view is visible.'
##        #return vis
##    def _set(self, vis):
##        u'Indicates if the view is visible.'
##    Visible = property(_get, _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Indicates if the view is currently responding to events.'
##    ProcessEvents = property(fset = _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if lines are shown in the TOC tree.'
##        #return Show
##    def _set(self, Show):
##        u'Indicates if lines are shown in the TOC tree.'
##    ShowLines = property(_get, _set, doc = _set.__doc__)
##
##    def RemoveFromSelectedItems(self, item):
##        u'Removes an item from the selected items.'
##        #return 
##

ITableWindow3._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if the window is open in the table window docking pane.')], HRESULT, 'IsOpen',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pIsOpen' )),
    COMMETHOD([helpstring(u'Gets all the open table windows.')], HRESULT, 'FindOpenTableWindows',
              ( ['out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISet)), 'pTableWindows' )),
    COMMETHOD(['propget', helpstring(u'Gets the active table window.')], HRESULT, 'ActiveTableWindow',
              ( ['retval', 'out'], POINTER(POINTER(ITableWindow)), 'ppTableWindow' )),
]
################################################################
## code template for ITableWindow3 implementation
##class ITableWindow3_Impl(object):
##    def FindOpenTableWindows(self):
##        u'Gets all the open table windows.'
##        #return pTableWindows
##
##    @property
##    def IsOpen(self):
##        u'Indicates if the window is open in the table window docking pane.'
##        #return pIsOpen
##
##    @property
##    def ActiveTableWindow(self):
##        u'Gets the active table window.'
##        #return ppTableWindow
##

class ImageInsetWindow(CoClass):
    u'Window to display ImageInsets.'
    _reg_clsid_ = GUID('{471A5627-C3B3-4116-94E0-BBE1CF95A017}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
ImageInsetWindow._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMapInsetWindow, ILensWindow, IDataWindow, IDataWindow2, IDocumentEvents, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IActiveViewEvents, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMapSurroundEvents, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream]
ImageInsetWindow._outgoing_interfaces_ = [IDataWindowEvents]

class NetworkLayerFactory(CoClass):
    _reg_clsid_ = GUID('{F3A7B339-70DA-4E8A-8DD3-83498A0FCF59}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
NetworkLayerFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayerFactory]

class NetCDFFeaturePropertyPage(CoClass):
    u'The NetCDF Feature Property Page.'
    _reg_clsid_ = GUID('{29B86626-324B-42CA-9BD0-2D424D8C4CF6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
NetCDFFeaturePropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

IClipboardFormat._methods_ = [
    COMMETHOD(['propget', helpstring(u'The Clipboard Format.')], HRESULT, 'Format',
              ( ['out'], POINTER(c_int), 'Format' )),
    COMMETHOD(['propget', helpstring(u'Priority of the Clipboard format for Paste (1 to 100, 100 highest priority).')], HRESULT, 'Priority',
              ( ['out'], POINTER(c_short), 'Priority' )),
    COMMETHOD(['propget', helpstring(u'Description of the Clipboard format.')], HRESULT, 'Description',
              ( ['out'], POINTER(BSTR), 'Description' )),
    COMMETHOD(['propget', helpstring(u'StorageMedium for Paste.  (Look up the C++ TYMED enumeration on MSDN for details).')], HRESULT, 'StorageMedium',
              ( ['out'], POINTER(c_int), 'tymed' )),
    COMMETHOD([helpstring(u'Copy selection to the Clipboard.')], HRESULT, 'Copy',
              ( ['in'], POINTER(IMxDocument), 'MxDocument' )),
    COMMETHOD([helpstring(u'Paste the Element in the GraphicsContainer to the Clipboard.')], HRESULT, 'Paste',
              ( ['in'], POINTER(IMxDocument), 'MxDocument' )),
]
################################################################
## code template for IClipboardFormat implementation
##class IClipboardFormat_Impl(object):
##    @property
##    def StorageMedium(self):
##        u'StorageMedium for Paste.  (Look up the C++ TYMED enumeration on MSDN for details).'
##        #return tymed
##
##    @property
##    def Description(self):
##        u'Description of the Clipboard format.'
##        #return Description
##
##    @property
##    def Format(self):
##        u'The Clipboard Format.'
##        #return Format
##
##    @property
##    def Priority(self):
##        u'Priority of the Clipboard format for Paste (1 to 100, 100 highest priority).'
##        #return Priority
##
##    def Copy(self, MxDocument):
##        u'Copy selection to the Clipboard.'
##        #return 
##
##    def Paste(self, MxDocument):
##        u'Paste the Element in the GraphicsContainer to the Clipboard.'
##        #return 
##

class HistoryViewerWindow(CoClass):
    u'History Viewer Window'
    _reg_clsid_ = GUID('{91496775-5D9E-4F01-B1EF-C6B33C34FAA5}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
class IHistoryViewerWindow(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of HistoryViewerWindow.'
    _iid_ = GUID('{462E59C1-2FA3-4D36-98F0-22E134D9BCE3}')
    _idlflags_ = ['oleautomation']
HistoryViewerWindow._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IDockableWindowDef, IHistoryViewerWindow, IDocumentEvents, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IActiveViewEvents, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMapEvents]

IHistoryViewerWindow._methods_ = [
    COMMETHOD([helpstring(u'Show the HistoryViewerWindow.')], HRESULT, 'Show',
              ( ['in'], comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.OLE_HANDLE, 'parentWindow' )),
]
################################################################
## code template for IHistoryViewerWindow implementation
##class IHistoryViewerWindow_Impl(object):
##    def Show(self, parentWindow):
##        u'Show the HistoryViewerWindow.'
##        #return 
##

class TerrainGxBrowserFactory(CoClass):
    u'The Terrain GX Browser Factory is used to help look for Terrains.'
    _reg_clsid_ = GUID('{C5E605A1-C840-47AA-9BC5-E09C94B7953F}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
TerrainGxBrowserFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayerFactory]

class IClipboardFormat2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the ClipBoard Format.'
    _iid_ = GUID('{9D584D2E-BBCA-423B-A94C-A4D25A4D52E5}')
    _idlflags_ = ['oleautomation']
IClipboardFormat2._methods_ = [
    COMMETHOD(['propget', helpstring(u'The Clipboard Format.')], HRESULT, 'Format',
              ( ['out'], POINTER(c_int), 'Format' )),
    COMMETHOD(['propget', helpstring(u'Priority of the Clipboard format for Paste (1 to 100, 100 highest priority).')], HRESULT, 'Priority',
              ( ['out'], POINTER(c_short), 'Priority' )),
    COMMETHOD(['propget', helpstring(u'Description of the Clipboard format.')], HRESULT, 'Description',
              ( ['out'], POINTER(BSTR), 'Description' )),
    COMMETHOD(['propget', helpstring(u'StorageMedium for Paste.  (Look up the C++ TYMED enumeration on MSDN for details).')], HRESULT, 'StorageMedium',
              ( ['out'], POINTER(c_int), 'tymed' )),
    COMMETHOD([helpstring(u'Copy selection to the Clipboard.')], HRESULT, 'Copy',
              ( ['in'], POINTER(IMxDocument), 'MxDocument' )),
    COMMETHOD([helpstring(u'Paste the Element in the GraphicsContainer to the Clipboard.')], HRESULT, 'Paste',
              ( ['in'], POINTER(IMxDocument), 'MxDocument' )),
    COMMETHOD([helpstring(u'Copy the entire view to the Clipboard.')], HRESULT, 'CopyMap',
              ( ['in'], POINTER(IMxDocument), 'MxDocument' )),
]
################################################################
## code template for IClipboardFormat2 implementation
##class IClipboardFormat2_Impl(object):
##    @property
##    def StorageMedium(self):
##        u'StorageMedium for Paste.  (Look up the C++ TYMED enumeration on MSDN for details).'
##        #return tymed
##
##    def CopyMap(self, MxDocument):
##        u'Copy the entire view to the Clipboard.'
##        #return 
##
##    @property
##    def Description(self):
##        u'Description of the Clipboard format.'
##        #return Description
##
##    @property
##    def Format(self):
##        u'The Clipboard Format.'
##        #return Format
##
##    @property
##    def Priority(self):
##        u'Priority of the Clipboard format for Paste (1 to 100, 100 highest priority).'
##        #return Priority
##
##    def Copy(self, MxDocument):
##        u'Copy selection to the Clipboard.'
##        #return 
##
##    def Paste(self, MxDocument):
##        u'Paste the Element in the GraphicsContainer to the Clipboard.'
##        #return 
##

class ITableProperties(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control Table properties, for Layers and Tables in ArcMap.'
    _iid_ = GUID('{4657D94E-5FFB-11D3-9F6C-00C04F6BC886}')
    _idlflags_ = ['oleautomation']
IMxDocument._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The page layout.')], HRESULT, 'PageLayout',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IPageLayout), 'PageLayout' )),
    COMMETHOD(['propget', helpstring(u'The page layout.')], HRESULT, 'PageLayout',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IPageLayout)), 'PageLayout' )),
    COMMETHOD(['propget', helpstring(u'The active view.')], HRESULT, 'ActiveView',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IActiveView)), 'ActiveView' )),
    COMMETHOD(['propputref', helpstring(u'The active view.')], HRESULT, 'ActiveView',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IActiveView), 'ActiveView' )),
    COMMETHOD(['propget', helpstring(u'The activated view.  This is the same as the active view unless a data frame is activated within a layout.')], HRESULT, 'ActivatedView',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IActiveView)), 'mainView' )),
    COMMETHOD(['propget', helpstring(u'The command associated with the active view.')], HRESULT, 'ActiveViewCommand',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.ICommand)), 'command' )),
    COMMETHOD(['propget', helpstring(u'The current focus map.')], HRESULT, 'FocusMap',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMap)), 'FocusMap' )),
    COMMETHOD(['propget', helpstring(u'The selected layer in the layer control.')], HRESULT, 'SelectedLayer',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer)), 'Layer' )),
    COMMETHOD(['propget', helpstring(u'The selected item in the layer control.')], HRESULT, 'SelectedItem',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'item' )),
    COMMETHOD(['propget', helpstring(u'The last item that was right-clicked.')], HRESULT, 'ContextItem',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'item' )),
    COMMETHOD(['propput', helpstring(u'The last item that was right-clicked.')], HRESULT, 'ContextItem',
              ( ['in'], POINTER(IUnknown), 'item' )),
    COMMETHOD(['propget', helpstring(u"Reference to the document's Style Gallery.")], HRESULT, 'StyleGallery',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IStyleGallery)), 'gallery' )),
    COMMETHOD([helpstring(u'Adds a layer to the current focus map.')], HRESULT, 'AddLayer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer), 'Layer' )),
    COMMETHOD([helpstring(u'Notifies the document that the contents have been updated.')], HRESULT, 'UpdateContents'),
    COMMETHOD(['propget', helpstring(u'The global search tolerance in geographic units for selection.')], HRESULT, 'SearchTolerance',
              ( ['retval', 'out'], POINTER(c_double), 'tol' )),
    COMMETHOD(['propget', helpstring(u'The global search tolerance in pixels for selection.')], HRESULT, 'SearchTolerancePixels',
              ( ['retval', 'out'], POINTER(c_int), 'tol' )),
    COMMETHOD(['propput', helpstring(u'The global search tolerance in pixels for selection.')], HRESULT, 'SearchTolerancePixels',
              ( ['in'], c_int, 'tol' )),
    COMMETHOD([helpstring(u'Inserts an object into the document.  Displays the insert object dialog.')], HRESULT, 'InsertObject'),
    COMMETHOD([helpstring(u'Indicates if the document allows objects to be inserted.')], HRESULT, 'CanInsertObject',
              ( [], POINTER(VARIANT_BOOL), 'pEnabled' )),
    COMMETHOD(['propget', helpstring(u'The collection of maps in the document.')], HRESULT, 'Maps',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMaps)), 'Maps' )),
    COMMETHOD(['propget', helpstring(u'The operation stack.')], HRESULT, 'OperationStack',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IOperationStack)), 'OperationStack' )),
    COMMETHOD(['propget', helpstring(u'The default font for text.')], HRESULT, 'DefaultTextFont',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IFontDisp)), 'fontDisp' )),
    COMMETHOD(['propput', helpstring(u'The default font size for text.')], HRESULT, 'DefaultTextFontSize',
              ( ['in'], POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IFontSize), 'fontSize' )),
    COMMETHOD(['propget', helpstring(u'The default font size for text.')], HRESULT, 'DefaultTextFontSize',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IFontSize)), 'fontSize' )),
    COMMETHOD(['propput', helpstring(u'The default font for text.')], HRESULT, 'DefaultTextFont',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IFontDisp), 'fontDisp' )),
    COMMETHOD(['propget', helpstring(u'The default color for the given type.')], HRESULT, 'DefaultColor',
              ( ['in'], esriMxDefaultColorTypes, 'Type' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IColor)), 'color' )),
    COMMETHOD(['propput', helpstring(u'The default color for the given type.')], HRESULT, 'DefaultColor',
              ( ['in'], esriMxDefaultColorTypes, 'Type' ),
              ( ['in'], POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IColor), 'color' )),
    COMMETHOD(['propget', helpstring(u'The current mouse location in map units.')], HRESULT, 'CurrentLocation',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint)), 'mouseLoc' )),
    COMMETHOD(['propput', helpstring(u'The current mouse location in map units.')], HRESULT, 'CurrentLocation',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'mouseLoc' )),
    COMMETHOD(['propput', helpstring(u'Indicates document update notifications should be ignored.')], HRESULT, 'DelayUpdateContents',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD(['propget', helpstring(u'Indicates if path names are stored relative to the document.')], HRESULT, 'RelativePaths',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'relPaths' )),
    COMMETHOD(['propput', helpstring(u'Indicates if path names are stored relative to the document.')], HRESULT, 'RelativePaths',
              ( ['in'], VARIANT_BOOL, 'relPaths' )),
    COMMETHOD(['propget', helpstring(u'The current contents view of the document.')], HRESULT, 'CurrentContentsView',
              ( ['retval', 'out'], POINTER(POINTER(IContentsView)), 'view' )),
    COMMETHOD(['propputref', helpstring(u'The current contents view of the document.')], HRESULT, 'CurrentContentsView',
              ( ['in'], POINTER(IContentsView), 'view' )),
    COMMETHOD(['propget', helpstring(u'The number of contents views in the document.')], HRESULT, 'ContentsViewCount',
              ( ['retval', 'out'], POINTER(c_int), 'count' )),
    COMMETHOD(['propget', helpstring(u'The contents view at the specified index.')], HRESULT, 'ContentsView',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IContentsView)), 'view' )),
    COMMETHOD(['propget', helpstring(u'Table properties, for Layers and Tables in ArcMap.')], HRESULT, 'TableProperties',
              ( ['retval', 'out'], POINTER(POINTER(ITableProperties)), 'pTableProperties' )),
]
################################################################
## code template for IMxDocument implementation
##class IMxDocument_Impl(object):
##    @property
##    def FocusMap(self):
##        u'The current focus map.'
##        #return FocusMap
##
##    def _get(self):
##        u'The global search tolerance in pixels for selection.'
##        #return tol
##    def _set(self, tol):
##        u'The global search tolerance in pixels for selection.'
##    SearchTolerancePixels = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def SelectedItem(self):
##        u'The selected item in the layer control.'
##        #return item
##
##    @property
##    def SelectedLayer(self):
##        u'The selected layer in the layer control.'
##        #return Layer
##
##    @property
##    def Maps(self):
##        u'The collection of maps in the document.'
##        #return Maps
##
##    def _get(self):
##        u'The default font for text.'
##        #return fontDisp
##    def _set(self, fontDisp):
##        u'The default font for text.'
##    DefaultTextFont = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def ActivatedView(self):
##        u'The activated view.  This is the same as the active view unless a data frame is activated within a layout.'
##        #return mainView
##
##    @property
##    def ContentsView(self, index):
##        u'The contents view at the specified index.'
##        #return view
##
##    def ActiveView(self, ActiveView):
##        u'The active view.'
##        #return 
##
##    def AddLayer(self, Layer):
##        u'Adds a layer to the current focus map.'
##        #return 
##
##    @property
##    def OperationStack(self):
##        u'The operation stack.'
##        #return OperationStack
##
##    def _get(self):
##        u'The last item that was right-clicked.'
##        #return item
##    def _set(self, item):
##        u'The last item that was right-clicked.'
##    ContextItem = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def TableProperties(self):
##        u'Table properties, for Layers and Tables in ArcMap.'
##        #return pTableProperties
##
##    def CurrentContentsView(self, view):
##        u'The current contents view of the document.'
##        #return 
##
##    def InsertObject(self):
##        u'Inserts an object into the document.  Displays the insert object dialog.'
##        #return 
##
##    @property
##    def StyleGallery(self):
##        u"Reference to the document's Style Gallery."
##        #return gallery
##
##    def _get(self):
##        u'The default font size for text.'
##        #return fontSize
##    def _set(self, fontSize):
##        u'The default font size for text.'
##    DefaultTextFontSize = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self, Type):
##        u'The default color for the given type.'
##        #return color
##    def _set(self, Type, color):
##        u'The default color for the given type.'
##    DefaultColor = property(_get, _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Indicates document update notifications should be ignored.'
##    DelayUpdateContents = property(fset = _set, doc = _set.__doc__)
##
##    @property
##    def ActiveViewCommand(self):
##        u'The command associated with the active view.'
##        #return command
##
##    @property
##    def SearchTolerance(self):
##        u'The global search tolerance in geographic units for selection.'
##        #return tol
##
##    @property
##    def PageLayout(self, PageLayout):
##        u'The page layout.'
##        #return 
##
##    def _get(self):
##        u'Indicates if path names are stored relative to the document.'
##        #return relPaths
##    def _set(self, relPaths):
##        u'Indicates if path names are stored relative to the document.'
##    RelativePaths = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def ContentsViewCount(self):
##        u'The number of contents views in the document.'
##        #return count
##
##    def UpdateContents(self):
##        u'Notifies the document that the contents have been updated.'
##        #return 
##
##    def _get(self):
##        u'The current mouse location in map units.'
##        #return mouseLoc
##    def _set(self, mouseLoc):
##        u'The current mouse location in map units.'
##    CurrentLocation = property(_get, _set, doc = _set.__doc__)
##
##    def CanInsertObject(self, pEnabled):
##        u'Indicates if the document allows objects to be inserted.'
##        #return 
##

class NetCDFRasterPropertyPage(CoClass):
    u'The NetCDF Raster Property Page.'
    _reg_clsid_ = GUID('{0301A37D-476F-4FD7-AF25-DE99F119FB65}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
NetCDFRasterPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class NetCDFTablePropertyPage(CoClass):
    u'The NetCDF Table Property Page.'
    _reg_clsid_ = GUID('{00726D99-B3F7-4BCA-9BDD-1C8A0CB41139}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
NetCDFTablePropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class ImageServerLayerContextAnalyzer(CoClass):
    u'A coclass for ImageServerLayer context analyzer.'
    _reg_clsid_ = GUID('{A0710BCC-B508-4CB0-8751-A6694D05F1D0}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
ImageServerLayerContextAnalyzer._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IContextAnalyzer]

class IPageIndexControl(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Data Driven Page Control interface.'
    _iid_ = GUID('{36F0873A-4237-4535-A486-F3CB8AE91130}')
    _idlflags_ = ['oleautomation']
IPageIndexControl._methods_ = [
    COMMETHOD(['propget', helpstring(u'Is the current data driven page the first?')], HRESULT, 'IsFirstPageShown',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD(['propget', helpstring(u'Is the current data driven page the last?')], HRESULT, 'IsLastPageShown',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD([helpstring(u'Show the first data driven page.')], HRESULT, 'ShowFirstPage'),
    COMMETHOD([helpstring(u'Show the next data driven page.')], HRESULT, 'ShowNextPage'),
    COMMETHOD([helpstring(u'Show the previous data driven page.')], HRESULT, 'ShowPreviousPage'),
    COMMETHOD([helpstring(u'Show the last data driven page.')], HRESULT, 'ShowLastPage'),
]
################################################################
## code template for IPageIndexControl implementation
##class IPageIndexControl_Impl(object):
##    def ShowFirstPage(self):
##        u'Show the first data driven page.'
##        #return 
##
##    @property
##    def IsFirstPageShown(self):
##        u'Is the current data driven page the first?'
##        #return flag
##
##    def ShowLastPage(self):
##        u'Show the last data driven page.'
##        #return 
##
##    @property
##    def IsLastPageShown(self):
##        u'Is the current data driven page the last?'
##        #return flag
##
##    def ShowNextPage(self):
##        u'Show the next data driven page.'
##        #return 
##
##    def ShowPreviousPage(self):
##        u'Show the previous data driven page.'
##        #return 
##

class MosaicDatasetExtension(CoClass):
    u'The extension of the mosaic layer.'
    _reg_clsid_ = GUID('{55A00062-4728-4807-BBF4-4A082B288FA5}')
    _idlflags_ = ['restricted']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
MosaicDatasetExtension._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IExtension]

class ElementEditVerticesOperation(CoClass):
    u'Command for editing an elements vertices.'
    _reg_clsid_ = GUID('{BF4FAD51-798A-11D2-A2D4-080009B6F22B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
ElementEditVerticesOperation._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IElementEditVerticesOperation, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IOperation]

class IDocumentDefaultSymbols(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control Default Symbols for the document.'
    _iid_ = GUID('{85961926-D8E9-11D3-9FF5-00C04F6BC8DD}')
    _idlflags_ = ['oleautomation']
IDocumentDefaultSymbols._methods_ = [
    COMMETHOD(['propput', helpstring(u'Default Fill Symbol.')], HRESULT, 'FillSymbol',
              ( ['in'], POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IFillSymbol), 'lSymbol' )),
    COMMETHOD(['propget', helpstring(u'Default Fill Symbol.')], HRESULT, 'FillSymbol',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IFillSymbol)), 'lSymbol' )),
    COMMETHOD(['propput', helpstring(u'Default Line Symbol.')], HRESULT, 'LineSymbol',
              ( ['in'], POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.ILineSymbol), 'LineSymbol' )),
    COMMETHOD(['propget', helpstring(u'Default Line Symbol.')], HRESULT, 'LineSymbol',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.ILineSymbol)), 'LineSymbol' )),
    COMMETHOD(['propput', helpstring(u'Default Marker Symbol.')], HRESULT, 'MarkerSymbol',
              ( ['in'], POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IMarkerSymbol), 'MarkerSymbol' )),
    COMMETHOD(['propget', helpstring(u'Default Marker Symbol.')], HRESULT, 'MarkerSymbol',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IMarkerSymbol)), 'MarkerSymbol' )),
    COMMETHOD(['propput', helpstring(u'Default Text Symbol.')], HRESULT, 'TextSymbol',
              ( ['in'], POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.ITextSymbol), 'TextSymbol' )),
    COMMETHOD(['propget', helpstring(u'Default Text Symbol.')], HRESULT, 'TextSymbol',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.ITextSymbol)), 'TextSymbol' )),
    COMMETHOD(['propput', helpstring(u'Default Callout.')], HRESULT, 'Callout',
              ( ['in'], POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IFormattedTextSymbol), 'Callout' )),
    COMMETHOD(['propget', helpstring(u'Default Callout.')], HRESULT, 'Callout',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IFormattedTextSymbol)), 'Callout' )),
    COMMETHOD(['propput', helpstring(u'Default Area Patch.')], HRESULT, 'AreaPatch',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IAreaPatch), 'patch' )),
    COMMETHOD(['propget', helpstring(u'Default Area Patch.')], HRESULT, 'AreaPatch',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IAreaPatch)), 'patch' )),
    COMMETHOD(['propput', helpstring(u'Default Line Patch.')], HRESULT, 'LinePatch',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILinePatch), 'patch' )),
    COMMETHOD(['propget', helpstring(u'Default Line Patch.')], HRESULT, 'LinePatch',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILinePatch)), 'patch' )),
    COMMETHOD(['propput', helpstring(u'Default Patch Width in Points.')], HRESULT, 'PatchWidth',
              ( ['in'], c_double, 'widthPts' )),
    COMMETHOD(['propget', helpstring(u'Default Patch Width in Points.')], HRESULT, 'PatchWidth',
              ( ['retval', 'out'], POINTER(c_double), 'widthPts' )),
    COMMETHOD(['propput', helpstring(u'Default Patch Height in Points.')], HRESULT, 'PatchHeight',
              ( ['in'], c_double, 'heightPts' )),
    COMMETHOD(['propget', helpstring(u'Default Patch Height in Points.')], HRESULT, 'PatchHeight',
              ( ['retval', 'out'], POINTER(c_double), 'heightPts' )),
    COMMETHOD(['propput', helpstring(u'Custom TOC Font.')], HRESULT, 'CustomTOCFont',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IFontDisp), 'font' )),
    COMMETHOD(['propget', helpstring(u'Custom TOC Font.')], HRESULT, 'CustomTOCFont',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IFontDisp)), 'font' )),
    COMMETHOD(['propput', helpstring(u'Custom TOC Font Size in Points.')], HRESULT, 'CustomTOCFontSize',
              ( ['in'], c_double, 'fontSizePts' )),
    COMMETHOD(['propget', helpstring(u'Custom TOC Font Size in Points.')], HRESULT, 'CustomTOCFontSize',
              ( ['retval', 'out'], POINTER(c_double), 'fontSizePts' )),
]
################################################################
## code template for IDocumentDefaultSymbols implementation
##class IDocumentDefaultSymbols_Impl(object):
##    def _get(self):
##        u'Default Patch Width in Points.'
##        #return widthPts
##    def _set(self, widthPts):
##        u'Default Patch Width in Points.'
##    PatchWidth = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Default Line Patch.'
##        #return patch
##    def _set(self, patch):
##        u'Default Line Patch.'
##    LinePatch = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Default Callout.'
##        #return Callout
##    def _set(self, Callout):
##        u'Default Callout.'
##    Callout = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Default Patch Height in Points.'
##        #return heightPts
##    def _set(self, heightPts):
##        u'Default Patch Height in Points.'
##    PatchHeight = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Default Fill Symbol.'
##        #return lSymbol
##    def _set(self, lSymbol):
##        u'Default Fill Symbol.'
##    FillSymbol = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Default Text Symbol.'
##        #return TextSymbol
##    def _set(self, TextSymbol):
##        u'Default Text Symbol.'
##    TextSymbol = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Default Marker Symbol.'
##        #return MarkerSymbol
##    def _set(self, MarkerSymbol):
##        u'Default Marker Symbol.'
##    MarkerSymbol = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Default Line Symbol.'
##        #return LineSymbol
##    def _set(self, LineSymbol):
##        u'Default Line Symbol.'
##    LineSymbol = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Default Area Patch.'
##        #return patch
##    def _set(self, patch):
##        u'Default Area Patch.'
##    AreaPatch = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Custom TOC Font.'
##        #return font
##    def _set(self, font):
##        u'Custom TOC Font.'
##    CustomTOCFont = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Custom TOC Font Size in Points.'
##        #return fontSizePts
##    def _set(self, fontSizePts):
##        u'Custom TOC Font Size in Points.'
##    CustomTOCFontSize = property(_get, _set, doc = _set.__doc__)
##

IDataWindowEvents._methods_ = [
    COMMETHOD([helpstring(u'Fired when window is shown.')], HRESULT, 'ShowWindow',
              ( [], POINTER(IDataWindow), 'window' )),
    COMMETHOD([helpstring(u'Fired when window is hidden.')], HRESULT, 'HideWindow',
              ( [], POINTER(IDataWindow), 'window' )),
    COMMETHOD([helpstring(u'Fired when window is destroyed.')], HRESULT, 'DestroyWindow',
              ( [], POINTER(IDataWindow), 'window' )),
]
################################################################
## code template for IDataWindowEvents implementation
##class IDataWindowEvents_Impl(object):
##    def ShowWindow(self, window):
##        u'Fired when window is shown.'
##        #return 
##
##    def HideWindow(self, window):
##        u'Fired when window is hidden.'
##        #return 
##
##    def DestroyWindow(self, window):
##        u'Fired when window is destroyed.'
##        #return 
##

class IEnumPrinterNames(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to an enumeration of all the Printers.'
    _iid_ = GUID('{1C79DAED-C3DA-4954-A7D2-330CEF0BD4B1}')
    _idlflags_ = ['oleautomation']
IEnumPrinterNames._methods_ = [
    COMMETHOD([helpstring(u'Reset the Enumeration to the beginning.')], HRESULT, 'Reset'),
    COMMETHOD([helpstring(u'The next Printer Name.')], HRESULT, 'Next',
              ( ['retval', 'out'], POINTER(BSTR), 'printerName' )),
]
################################################################
## code template for IEnumPrinterNames implementation
##class IEnumPrinterNames_Impl(object):
##    def Reset(self):
##        u'Reset the Enumeration to the beginning.'
##        #return 
##
##    def Next(self):
##        u'The next Printer Name.'
##        #return printerName
##

class MetaFileClipboardFormat(CoClass):
    u'Windows Metafile Clipboard Format (WMF).'
    _reg_clsid_ = GUID('{A584BEB7-F834-11D2-9F5B-00C04F6BC8DD}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
MetaFileClipboardFormat._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IClipboardFormat, IClipboardFormat2]

class DocumentPropertyPage(CoClass):
    u'Property page for Document general properties.'
    _reg_clsid_ = GUID('{421F13D1-007F-11D2-A253-080009B6F22B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
DocumentPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

ILayerEffectsEnvironment3._methods_ = [
    COMMETHOD(['propget', helpstring(u'The ILayerEffects interface of the current effects layer.')], HRESULT, 'EffectsLayer',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayerEffects)), 'effects' )),
    COMMETHOD(['propputref', helpstring(u'The ILayerEffects interface of the current effects layer.')], HRESULT, 'EffectsLayer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayerEffects), 'effects' )),
    COMMETHOD(['propget', helpstring(u'The IActiveView interface of the view to be refreshed.')], HRESULT, 'ActiveView',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IActiveView)), 'ActiveView' )),
    COMMETHOD(['propputref', helpstring(u'The IActiveView interface of the view to be refreshed.')], HRESULT, 'ActiveView',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IActiveView), 'ActiveView' )),
    COMMETHOD(['propget', helpstring(u'Currenttly selected layer.')], HRESULT, 'SelectedLayer',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer)), 'Layer' )),
    COMMETHOD(['propputref', helpstring(u'Currenttly selected layer.')], HRESULT, 'SelectedLayer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer), 'Layer' )),
    COMMETHOD(['propget', helpstring(u'Current document.')], HRESULT, 'Document',
              ( ['retval', 'out'], POINTER(POINTER(IMxDocument)), 'doc' )),
    COMMETHOD(['propputref', helpstring(u'Current document.')], HRESULT, 'Document',
              ( ['in'], POINTER(IMxDocument), 'doc' )),
]
################################################################
## code template for ILayerEffectsEnvironment3 implementation
##class ILayerEffectsEnvironment3_Impl(object):
##    def Document(self, doc):
##        u'Current document.'
##        #return 
##
##    def ActiveView(self, ActiveView):
##        u'The IActiveView interface of the view to be refreshed.'
##        #return 
##
##    def SelectedLayer(self, Layer):
##        u'Currenttly selected layer.'
##        #return 
##
##    def EffectsLayer(self, effects):
##        u'The ILayerEffects interface of the current effects layer.'
##        #return 
##

class BmpClipboardFormat(CoClass):
    u'BMP Clipboard Format.'
    _reg_clsid_ = GUID('{A5D5245F-F841-11D2-9F5B-00C04F6BC8DD}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
BmpClipboardFormat._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IClipboardFormat, IClipboardFormat2]

class INewDocumentDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the new document dialog.'
    _iid_ = GUID('{3A124166-E8B0-44EF-BA25-B8D90A7C061B}')
    _idlflags_ = ['oleautomation']
INewDocumentDialog._methods_ = [
    COMMETHOD([helpstring(u'Shows the new document dialog.')], HRESULT, 'DoModal',
              ( ['in'], comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.OLE_HANDLE, 'parentHWnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pOk' )),
    COMMETHOD(['propget', helpstring(u'The selected document.')], HRESULT, 'FilePath',
              ( ['retval', 'out'], POINTER(BSTR), 'fileName' )),
    COMMETHOD(['propget', helpstring(u'The database for the document.')], HRESULT, 'Database',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceName)), 'ppWorkspaceName' )),
]
################################################################
## code template for INewDocumentDialog implementation
##class INewDocumentDialog_Impl(object):
##    def DoModal(self, parentHWnd):
##        u'Shows the new document dialog.'
##        #return pOk
##
##    @property
##    def Database(self):
##        u'The database for the document.'
##        #return ppWorkspaceName
##
##    @property
##    def FilePath(self):
##        u'The selected document.'
##        #return fileName
##

class PageIndexGeneralPropPage(CoClass):
    u'General property page for data driven pages.'
    _reg_clsid_ = GUID('{05597F66-26ED-4BE2-869A-60B247E49F84}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
PageIndexGeneralPropPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class PageIndexExtentPropPage(CoClass):
    u'Extent property page for data driven pages.'
    _reg_clsid_ = GUID('{05597F67-26ED-4BE2-869A-60B247E49F84}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
PageIndexExtentPropPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class IModelessQueryAttributes(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Modeless Attribute query window.'
    _iid_ = GUID('{4393F3FD-1AFC-11D4-9FEE-00C04F6BC78E}')
    _idlflags_ = ['oleautomation']
IModelessQueryAttributes._methods_ = [
    COMMETHOD([helpstring(u'Shows attribute query window in a modeless state.')], HRESULT, 'Show',
              ( ['in'], comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.OLE_HANDLE, 'parentHWnd' )),
    COMMETHOD([helpstring(u"Refreshes the attribute query window when it's in a modeless state.")], HRESULT, 'Refresh'),
]
################################################################
## code template for IModelessQueryAttributes implementation
##class IModelessQueryAttributes_Impl(object):
##    def Refresh(self):
##        u"Refreshes the attribute query window when it's in a modeless state."
##        #return 
##
##    def Show(self, parentHWnd):
##        u'Shows attribute query window in a modeless state.'
##        #return 
##

class JoinData(CoClass):
    u'Join Data dialog.'
    _reg_clsid_ = GUID('{F45ABEFC-9A92-11D2-A089-0000F8775BF9}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
class IJoinData(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that join a feature class or a table to a layer/standalone table in ArcMap.'
    _iid_ = GUID('{F45ABEFB-9A92-11D2-A089-0000F8775BF9}')
    _idlflags_ = ['oleautomation']
JoinData._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IJoinData, IJoinData2, IJoinPages]

class IStartupDialog2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to more members that control the Startup Dialog.'
    _iid_ = GUID('{35E1EA98-16D0-11D4-9FED-00C04F6BC78E}')
    _idlflags_ = ['oleautomation']
IStartupDialog2._methods_ = [
    COMMETHOD(['propget', helpstring(u'An initial command to run (may be nothing).')], HRESULT, 'InitialCommand',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID)), 'commandID' )),
]
################################################################
## code template for IStartupDialog2 implementation
##class IStartupDialog2_Impl(object):
##    @property
##    def InitialCommand(self):
##        u'An initial command to run (may be nothing).'
##        #return commandID
##

class IBasicDocument(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Basic Document.'
    _iid_ = GUID('{A58923BC-14D4-11D4-A0FF-00C04F8ECE27}')
    _idlflags_ = ['oleautomation']
IBasicDocument._methods_ = [
    COMMETHOD(['restricted', helpstring(u'The active view.'), 'propget'], HRESULT, 'ActiveView',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IActiveView)), 'ppActiveView' )),
    COMMETHOD(['restricted', helpstring(u'The active view.'), 'propputref'], HRESULT, 'ActiveView',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IActiveView), 'ppActiveView' )),
    COMMETHOD(['propget', helpstring(u'The selected layer in the layer control.')], HRESULT, 'SelectedLayer',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer)), 'ppLayer' )),
    COMMETHOD(['propget', helpstring(u'The selected item in the layer control.')], HRESULT, 'SelectedItem',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'ppItem' )),
    COMMETHOD(['propget', helpstring(u'The last item that was right-clicked.')], HRESULT, 'ContextItem',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'ppItem' )),
    COMMETHOD(['propput', helpstring(u'The last item that was right-clicked.')], HRESULT, 'ContextItem',
              ( ['in'], POINTER(IUnknown), 'ppItem' )),
    COMMETHOD([helpstring(u'Adds a layer to the current focus map or scene.')], HRESULT, 'AddLayer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer), 'pLayer' )),
    COMMETHOD([helpstring(u'Notifies the document that the contents have been updated.')], HRESULT, 'UpdateContents'),
    COMMETHOD(['propget', helpstring(u'Table properties, for Layers and Tables.')], HRESULT, 'TableProperties',
              ( ['retval', 'out'], POINTER(POINTER(ITableProperties)), 'pTableProperties' )),
]
################################################################
## code template for IBasicDocument implementation
##class IBasicDocument_Impl(object):
##    def UpdateContents(self):
##        u'Notifies the document that the contents have been updated.'
##        #return 
##
##    def _get(self):
##        u'The last item that was right-clicked.'
##        #return ppItem
##    def _set(self, ppItem):
##        u'The last item that was right-clicked.'
##    ContextItem = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def TableProperties(self):
##        u'Table properties, for Layers and Tables.'
##        #return pTableProperties
##
##    @property
##    def SelectedItem(self):
##        u'The selected item in the layer control.'
##        #return ppItem
##
##    @property
##    def SelectedLayer(self):
##        u'The selected layer in the layer control.'
##        #return ppLayer
##
##    def ActiveView(self, ppActiveView):
##        u'The active view.'
##        #return 
##
##    def AddLayer(self, pLayer):
##        u'Adds a layer to the current focus map or scene.'
##        #return 
##

IAddLayersOperation._methods_ = [
    COMMETHOD([helpstring(u'Layer to be added.')], HRESULT, 'AddLayer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer), 'Layer' )),
    COMMETHOD([helpstring(u'Information regarding where the the layer needs to be added. pDestination can be a Map or a GroupLayer.')], HRESULT, 'SetDestinationInfo',
              ( [], c_int, 'atIndex' ),
              ( [], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMap), 'pDestinationMap' ),
              ( [], POINTER(IUnknown), 'pDestinationGroup' )),
    COMMETHOD(['propput', helpstring(u'A Boolean expression that represents whether the layers need to arranged as per their shape.')], HRESULT, 'ArrangeLayers',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Name of the the operation.')], HRESULT, 'Name',
              ( ['in'], BSTR, 'rhs' )),
]
################################################################
## code template for IAddLayersOperation implementation
##class IAddLayersOperation_Impl(object):
##    def _set(self, rhs):
##        u'A Boolean expression that represents whether the layers need to arranged as per their shape.'
##    ArrangeLayers = property(fset = _set, doc = _set.__doc__)
##
##    def AddLayer(self, Layer):
##        u'Layer to be added.'
##        #return 
##
##    def _set(self, rhs):
##        u'Name of the the operation.'
##    Name = property(fset = _set, doc = _set.__doc__)
##
##    def SetDestinationInfo(self, atIndex, pDestinationMap, pDestinationGroup):
##        u'Information regarding where the the layer needs to be added. pDestination can be a Map or a GroupLayer.'
##        #return 
##

IStartupDialog._methods_ = [
    COMMETHOD([helpstring(u'Shows the startup dialog.')], HRESULT, 'DoModal',
              ( ['in'], comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.OLE_HANDLE, 'parentHWnd' )),
    COMMETHOD(['propget', helpstring(u'An initial file name (may be blank).')], HRESULT, 'FilePath',
              ( ['retval', 'out'], POINTER(BSTR), 'fileName' )),
]
################################################################
## code template for IStartupDialog implementation
##class IStartupDialog_Impl(object):
##    def DoModal(self, parentHWnd):
##        u'Shows the startup dialog.'
##        #return 
##
##    @property
##    def FilePath(self):
##        u'An initial file name (may be blank).'
##        #return fileName
##

class MoveLayersOperation(CoClass):
    u'Move Layers Operation.'
    _reg_clsid_ = GUID('{F8A674C6-5F60-4B4A-86FF-EE1A1A9AD81E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
class IMoveLayersOperation(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Move layer operation.'
    _iid_ = GUID('{2DE06476-BFCB-4628-9A6E-9CC0F0A7DB54}')
    _idlflags_ = ['oleautomation']
MoveLayersOperation._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IOperation, IMoveLayersOperation]

class IRelateData2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that join a feature class or a table to a layer/standalone table in ArcMap.'
    _iid_ = GUID('{8AA8974B-A74F-48F4-8308-42F799080238}')
    _idlflags_ = ['oleautomation']
IRelateData2._methods_ = [
    COMMETHOD(['propputref', helpstring(u'Primary layer to join from.')], HRESULT, 'RelateOrigin',
              ( ['in'], POINTER(IUnknown), 'rhs' )),
    COMMETHOD([helpstring(u'Shows modal window.')], HRESULT, 'DoModal',
              ( ['in'], comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.OLE_HANDLE, 'parentWindow' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRelationshipClass)), 'relationshipClass' )),
    COMMETHOD(['propputref', helpstring(u'The application to which this window belongs (Optional).')], HRESULT, 'Application',
              ( ['in'], POINTER(IDispatch), 'rhs' )),
    COMMETHOD(['propputref', helpstring(u'Primary layer to relate from (removes standalone table setting).')], HRESULT, 'Layer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer), 'rhs' )),
    COMMETHOD(['propputref', helpstring(u'Primary table to relate from (removes layer setting).')], HRESULT, 'StandaloneTable',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IStandaloneTable), 'rhs' )),
]
################################################################
## code template for IRelateData2 implementation
##class IRelateData2_Impl(object):
##    def Application(self, rhs):
##        u'The application to which this window belongs (Optional).'
##        #return 
##
##    def RelateOrigin(self, rhs):
##        u'Primary layer to join from.'
##        #return 
##
##    def Layer(self, rhs):
##        u'Primary layer to relate from (removes standalone table setting).'
##        #return 
##
##    def StandaloneTable(self, rhs):
##        u'Primary table to relate from (removes layer setting).'
##        #return 
##
##    def DoModal(self, parentWindow):
##        u'Shows modal window.'
##        #return relationshipClass
##

class MapDocumentPropPage(CoClass):
    u'Property page for Document properties.'
    _reg_clsid_ = GUID('{C7D8A74A-17C3-4EBB-90B9-02F23B3FD919}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
MapDocumentPropPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

IStartupDialog3._methods_ = [
    COMMETHOD(['propget', helpstring(u'The database for the document.')], HRESULT, 'Database',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceName)), 'ppWorkspaceName' )),
    COMMETHOD(['propget', helpstring(u'Gets the value determining if file path is a template.')], HRESULT, 'IsTemplate',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pIsTemplate' )),
]
################################################################
## code template for IStartupDialog3 implementation
##class IStartupDialog3_Impl(object):
##    @property
##    def IsTemplate(self):
##        u'Gets the value determining if file path is a template.'
##        #return pIsTemplate
##
##    @property
##    def Database(self):
##        u'The database for the document.'
##        #return ppWorkspaceName
##

class SpatialJoin(CoClass):
    u'Spatial Join two feature classes.'
    _reg_clsid_ = GUID('{12B35C91-010F-11D4-A692-0008C7D3AE8D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
SpatialJoin._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ISpatialJoin, IAggregateOptions]

class IBasicDocument2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides additional access to members that control the Basic Document.'
    _iid_ = GUID('{EF2EC034-C197-48A0-90EE-C6B7DB797EB8}')
    _idlflags_ = ['oleautomation']
IBasicDocument2._methods_ = [
    COMMETHOD(['restricted', helpstring(u'The active view.'), 'propget'], HRESULT, 'ActiveView',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IActiveView)), 'ppActiveView' )),
    COMMETHOD(['restricted', helpstring(u'The active view.'), 'propputref'], HRESULT, 'ActiveView',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IActiveView), 'ppActiveView' )),
    COMMETHOD(['propget', helpstring(u'The selected layer in the layer control.')], HRESULT, 'SelectedLayer',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer)), 'ppLayer' )),
    COMMETHOD(['propget', helpstring(u'The selected item in the layer control.')], HRESULT, 'SelectedItem',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'ppItem' )),
    COMMETHOD(['propget', helpstring(u'The last item that was right-clicked.')], HRESULT, 'ContextItem',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'ppItem' )),
    COMMETHOD(['propput', helpstring(u'The last item that was right-clicked.')], HRESULT, 'ContextItem',
              ( ['in'], POINTER(IUnknown), 'ppItem' )),
    COMMETHOD([helpstring(u'Adds a layer to the current focus map or scene.')], HRESULT, 'AddLayer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer), 'pLayer' )),
    COMMETHOD([helpstring(u'Notifies the document that the contents have been updated.')], HRESULT, 'UpdateContents'),
    COMMETHOD(['propget', helpstring(u'Table properties, for Layers and Tables.')], HRESULT, 'TableProperties',
              ( ['retval', 'out'], POINTER(POINTER(ITableProperties)), 'pTableProperties' )),
    COMMETHOD(['propputref', helpstring(u'The page layout.')], HRESULT, 'PageLayout',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IPageLayout), 'PageLayout' )),
    COMMETHOD(['propget', helpstring(u'The page layout.')], HRESULT, 'PageLayout',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IPageLayout)), 'PageLayout' )),
    COMMETHOD(['propget', helpstring(u'The activated view.  This is the same as the active view unless a data frame is activated within a layout.')], HRESULT, 'ActivatedView',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IActiveView)), 'mainView' )),
    COMMETHOD(['propget', helpstring(u'The current focus map.')], HRESULT, 'FocusMap',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMap)), 'FocusMap' )),
    COMMETHOD(['propget', helpstring(u"Reference to the document's Style Gallery.")], HRESULT, 'StyleGallery',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IStyleGallery)), 'gallery' )),
    COMMETHOD(['propget', helpstring(u'The global search tolerance in geographic units for selection.')], HRESULT, 'SearchTolerance',
              ( ['retval', 'out'], POINTER(c_double), 'tol' )),
    COMMETHOD(['propget', helpstring(u'The global search tolerance in pixels for selection.')], HRESULT, 'SearchTolerancePixels',
              ( ['retval', 'out'], POINTER(c_int), 'tol' )),
    COMMETHOD(['propput', helpstring(u'The global search tolerance in pixels for selection.')], HRESULT, 'SearchTolerancePixels',
              ( ['in'], c_int, 'tol' )),
    COMMETHOD(['propget', helpstring(u'The collection of maps in the document.')], HRESULT, 'Maps',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMaps)), 'Maps' )),
    COMMETHOD(['propget', helpstring(u'The operation stack.')], HRESULT, 'OperationStack',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IOperationStack)), 'OperationStack' )),
    COMMETHOD(['propget', helpstring(u'The current mouse location in map units.')], HRESULT, 'CurrentLocation',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint)), 'mouseLoc' )),
    COMMETHOD(['propput', helpstring(u'The current mouse location in map units.')], HRESULT, 'CurrentLocation',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'mouseLoc' )),
]
################################################################
## code template for IBasicDocument2 implementation
##class IBasicDocument2_Impl(object):
##    @property
##    def PageLayout(self, PageLayout):
##        u'The page layout.'
##        #return 
##
##    @property
##    def FocusMap(self):
##        u'The current focus map.'
##        #return FocusMap
##
##    def UpdateContents(self):
##        u'Notifies the document that the contents have been updated.'
##        #return 
##
##    def _get(self):
##        u'The global search tolerance in pixels for selection.'
##        #return tol
##    def _set(self, tol):
##        u'The global search tolerance in pixels for selection.'
##    SearchTolerancePixels = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The last item that was right-clicked.'
##        #return ppItem
##    def _set(self, ppItem):
##        u'The last item that was right-clicked.'
##    ContextItem = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def TableProperties(self):
##        u'Table properties, for Layers and Tables.'
##        #return pTableProperties
##
##    @property
##    def SelectedItem(self):
##        u'The selected item in the layer control.'
##        #return ppItem
##
##    @property
##    def SelectedLayer(self):
##        u'The selected layer in the layer control.'
##        #return ppLayer
##
##    @property
##    def Maps(self):
##        u'The collection of maps in the document.'
##        #return Maps
##
##    @property
##    def ActivatedView(self):
##        u'The activated view.  This is the same as the active view unless a data frame is activated within a layout.'
##        #return mainView
##
##    @property
##    def StyleGallery(self):
##        u"Reference to the document's Style Gallery."
##        #return gallery
##
##    def ActiveView(self, ppActiveView):
##        u'The active view.'
##        #return 
##
##    def AddLayer(self, pLayer):
##        u'Adds a layer to the current focus map or scene.'
##        #return 
##
##    def _get(self):
##        u'The current mouse location in map units.'
##        #return mouseLoc
##    def _set(self, mouseLoc):
##        u'The current mouse location in map units.'
##    CurrentLocation = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def SearchTolerance(self):
##        u'The global search tolerance in geographic units for selection.'
##        #return tol
##
##    @property
##    def OperationStack(self):
##        u'The operation stack.'
##        #return OperationStack
##

class IGenericWindow(IDataWindow):
    _case_insensitive_ = True
    u'Provides access to members that control a data window with a particular hWnd.'
    _iid_ = GUID('{4B043FA0-7906-11D2-A084-0000F8775BF9}')
    _idlflags_ = ['oleautomation']
IGenericWindow._methods_ = [
    COMMETHOD(['propput', helpstring(u'Name displayed on form.')], HRESULT, 'Title',
              ( ['in'], BSTR, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Name of data window.')], HRESULT, 'Name',
              ( ['in'], BSTR, 'pWindowName' )),
    COMMETHOD(['propget', helpstring(u'Name of data window.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pWindowName' )),
    COMMETHOD(['propput', helpstring(u'UID of ActiveX component to place in data window.')], HRESULT, 'ActiveXUID',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID), 'rhs' )),
    COMMETHOD(['propget', helpstring(u'Find an already displayed window.')], HRESULT, 'FindWindow',
              ( ['in'], BSTR, 'windowName' ),
              ( ['retval', 'out'], POINTER(POINTER(IGenericWindow)), 'pGenericWindow' )),
]
################################################################
## code template for IGenericWindow implementation
##class IGenericWindow_Impl(object):
##    @property
##    def FindWindow(self, windowName):
##        u'Find an already displayed window.'
##        #return pGenericWindow
##
##    def _get(self):
##        u'Name of data window.'
##        #return pWindowName
##    def _set(self, pWindowName):
##        u'Name of data window.'
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'UID of ActiveX component to place in data window.'
##    ActiveXUID = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Name displayed on form.'
##    Title = property(fset = _set, doc = _set.__doc__)
##

class IChangeLayout(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u"Provides access to members that control changing the document's layout."
    _iid_ = GUID('{1A8D7EAD-DF05-11D3-9309-00600802E603}')
    _idlflags_ = ['oleautomation']
IChangeLayout._methods_ = [
    COMMETHOD([helpstring(u'Indicates if the wizard used to select a new layout is shown.')], HRESULT, 'ChangeLayout',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'changed' )),
]
################################################################
## code template for IChangeLayout implementation
##class IChangeLayout_Impl(object):
##    def ChangeLayout(self):
##        u'Indicates if the wizard used to select a new layout is shown.'
##        #return changed
##

IDocumentEvents._methods_ = [
    COMMETHOD([helpstring(u'Fired when the active view changes.')], HRESULT, 'ActiveViewChanged'),
    COMMETHOD([helpstring(u'Fired when a change is made to the map collection.')], HRESULT, 'MapsChanged'),
    COMMETHOD([helpstring(u'Indicates if a context menu should be displayed at the given xy location. Return true if handled.')], HRESULT, 'OnContextMenu',
              ( ['in'], c_int, 'x' ),
              ( ['in'], c_int, 'y' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'handled' )),
    COMMETHOD([helpstring(u'Fired when a new document is created.')], HRESULT, 'NewDocument'),
    COMMETHOD([helpstring(u'Fired when a document is opened.')], HRESULT, 'OpenDocument'),
    COMMETHOD([helpstring(u'Fired before a document is closed. Return True to abort the close process.')], HRESULT, 'BeforeCloseDocument',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'abortClose' )),
    COMMETHOD([helpstring(u'Fired when a document is closed.')], HRESULT, 'CloseDocument'),
]
################################################################
## code template for IDocumentEvents implementation
##class IDocumentEvents_Impl(object):
##    def OnContextMenu(self, x, y):
##        u'Indicates if a context menu should be displayed at the given xy location. Return true if handled.'
##        #return handled
##
##    def MapsChanged(self):
##        u'Fired when a change is made to the map collection.'
##        #return 
##
##    def NewDocument(self):
##        u'Fired when a new document is created.'
##        #return 
##
##    def ActiveViewChanged(self):
##        u'Fired when the active view changes.'
##        #return 
##
##    def OpenDocument(self):
##        u'Fired when a document is opened.'
##        #return 
##
##    def CloseDocument(self):
##        u'Fired when a document is closed.'
##        #return 
##
##    def BeforeCloseDocument(self):
##        u'Fired before a document is closed. Return True to abort the close process.'
##        #return abortClose
##

class RelateData(CoClass):
    u'Relate Data dialog.'
    _reg_clsid_ = GUID('{B5856942-FE6C-11D3-ADF8-00C04FA33A15}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
RelateData._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRelateData, IRelateData2]

IUngroupLayerOperation._methods_ = [
    COMMETHOD(['propput', helpstring(u'Parent group layer, if any to which the layer that needs to be ungrouped belongs to.')], HRESULT, 'ParentGroupLayer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IGroupLayer), 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Parent map to which the group layer or parent group layer belongs to.')], HRESULT, 'ParentMap',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMap), 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Group layer that needs to be ungrouped.')], HRESULT, 'GroupLayer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IGroupLayer), 'rhs' )),
]
################################################################
## code template for IUngroupLayerOperation implementation
##class IUngroupLayerOperation_Impl(object):
##    def _set(self, rhs):
##        u'Parent map to which the group layer or parent group layer belongs to.'
##    ParentMap = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Parent group layer, if any to which the layer that needs to be ungrouped belongs to.'
##    ParentGroupLayer = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Group layer that needs to be ungrouped.'
##    GroupLayer = property(fset = _set, doc = _set.__doc__)
##

ITableProperty2._methods_ = [
    COMMETHOD(['propput', helpstring(u'Indicates if the Selected table is shown.')], HRESULT, 'SelectedTable',
              ( ['in'], VARIANT_BOOL, 'pShowSelectedTable' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the Selected table is shown.')], HRESULT, 'SelectedTable',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pShowSelectedTable' )),
    COMMETHOD(['propputref', helpstring(u'Table of table window (Overrides feature class setting).')], HRESULT, 'Table',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable), 'ppTable' )),
    COMMETHOD(['propget', helpstring(u'Table of table window (Overrides feature class setting).')], HRESULT, 'Table',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable)), 'ppTable' )),
    COMMETHOD(['propputref', helpstring(u'Feature class of table window (Overrides table setting).')], HRESULT, 'FeatureLayer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IFeatureLayer), 'ppFeatureLayer' )),
    COMMETHOD(['propget', helpstring(u'Feature class of table window (Overrides table setting).')], HRESULT, 'FeatureLayer',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IFeatureLayer)), 'ppFeatureLayer' )),
    COMMETHOD(['propputref', helpstring(u'Layer for table window (Overrides table and featurelayer setting).')], HRESULT, 'Layer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer), 'ppLayer' )),
    COMMETHOD(['propget', helpstring(u'Layer for table window (Overrides table and featurelayer setting).')], HRESULT, 'Layer',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer)), 'ppLayer' )),
]
################################################################
## code template for ITableProperty2 implementation
##class ITableProperty2_Impl(object):
##    @property
##    def Table(self, ppTable):
##        u'Table of table window (Overrides feature class setting).'
##        #return 
##
##    @property
##    def Layer(self, ppLayer):
##        u'Layer for table window (Overrides table and featurelayer setting).'
##        #return 
##
##    def _get(self):
##        u'Indicates if the Selected table is shown.'
##        #return pShowSelectedTable
##    def _set(self, pShowSelectedTable):
##        u'Indicates if the Selected table is shown.'
##    SelectedTable = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def FeatureLayer(self, ppFeatureLayer):
##        u'Feature class of table window (Overrides table setting).'
##        #return 
##

class IDocumentEventsDisp(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Provides access to events that occur in ArcMap.'
    _iid_ = GUID('{91E55EF5-FBC5-11D1-94A2-080009EEBECB}')
    _idlflags_ = ['oleautomation']
IDocumentEventsDisp._methods_ = [
    COMMETHOD([helpstring(u'Fired when the active view has changed.')], HRESULT, 'ActiveViewChanged',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bStop' )),
    COMMETHOD([helpstring(u'Fired when a change is made to the map collection.')], HRESULT, 'MapsChanged',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bStop' )),
    COMMETHOD([helpstring(u'Indicates if a context menu should be displayed at the given xy location. Return true if handled.')], HRESULT, 'OnContextMenu',
              ( ['in'], c_int, 'x' ),
              ( ['in'], c_int, 'y' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'handled' )),
    COMMETHOD([helpstring(u'Fired when a new document is created.')], HRESULT, 'NewDocument',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bStop' )),
    COMMETHOD([helpstring(u'Fired when a document is opened.')], HRESULT, 'OpenDocument',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bStop' )),
    COMMETHOD([helpstring(u'Fired when a document is closed.')], HRESULT, 'CloseDocument',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bStop' )),
    COMMETHOD([helpstring(u'Fired before a document is closed. Return True to abort the close process.')], HRESULT, 'BeforeCloseDocument',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'abortClose' )),
    COMMETHOD([helpstring(u'Fired when VBA is reset.')], HRESULT, 'VBAReset',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bStop' )),
]
################################################################
## code template for IDocumentEventsDisp implementation
##class IDocumentEventsDisp_Impl(object):
##    def OnContextMenu(self, x, y):
##        u'Indicates if a context menu should be displayed at the given xy location. Return true if handled.'
##        #return handled
##
##    def MapsChanged(self):
##        u'Fired when a change is made to the map collection.'
##        #return bStop
##
##    def NewDocument(self):
##        u'Fired when a new document is created.'
##        #return bStop
##
##    def ActiveViewChanged(self):
##        u'Fired when the active view has changed.'
##        #return bStop
##
##    def OpenDocument(self):
##        u'Fired when a document is opened.'
##        #return bStop
##
##    def CloseDocument(self):
##        u'Fired when a document is closed.'
##        #return bStop
##
##    def BeforeCloseDocument(self):
##        u'Fired before a document is closed. Return True to abort the close process.'
##        #return abortClose
##
##    def VBAReset(self):
##        u'Fired when VBA is reset.'
##        #return bStop
##

class IDataGraphTWizard(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the data graph wizard.'
    _iid_ = GUID('{92518444-EAD5-4DE2-A050-A9428A1025F3}')
    _idlflags_ = ['oleautomation']
IDataGraphTWizard._methods_ = [
    COMMETHOD(['propget', helpstring(u'The data graph created by this new wizard.')], HRESULT, 'DataGraphT',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDataGraphT)), 'graph' )),
    COMMETHOD(['propputref', helpstring(u'The application to which the wizard dialog belongs.')], HRESULT, 'Application',
              ( ['in'], POINTER(IDispatch), 'rhs' )),
    COMMETHOD([helpstring(u'Default data source to select in the wizard.')], HRESULT, 'SelectDataSource',
              ( [], POINTER(IUnknown), 'pDataSource' )),
    COMMETHOD([helpstring(u'Starts the wizard dialog.')], HRESULT, 'DoModal',
              ( ['in'], comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.OLE_HANDLE, 'parentWindow' )),
]
################################################################
## code template for IDataGraphTWizard implementation
##class IDataGraphTWizard_Impl(object):
##    def Application(self, rhs):
##        u'The application to which the wizard dialog belongs.'
##        #return 
##
##    @property
##    def DataGraphT(self):
##        u'The data graph created by this new wizard.'
##        #return graph
##
##    def DoModal(self, parentWindow):
##        u'Starts the wizard dialog.'
##        #return 
##
##    def SelectDataSource(self, pDataSource):
##        u'Default data source to select in the wizard.'
##        #return 
##

class IContentsView2(IContentsView):
    _case_insensitive_ = True
    u'Provides access to members that control the table of contents views of GMx.'
    _iid_ = GUID('{B461CDE5-216D-11D6-B2B3-00508BCDDE28}')
    _idlflags_ = ['oleautomation']
IContentsView2._methods_ = [
    COMMETHOD([helpstring(u'Activates the contents view.')], HRESULT, 'BasicActivate',
              ( ['in'], comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.OLE_HANDLE, 'parentHWnd' ),
              ( ['in'], POINTER(comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IDocument), 'Document' )),
]
################################################################
## code template for IContentsView2 implementation
##class IContentsView2_Impl(object):
##    def BasicActivate(self, parentHWnd, Document):
##        u'Activates the contents view.'
##        #return 
##

class IRemoveLayerOperation(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Remove layer operation.'
    _iid_ = GUID('{A231C0E2-0BDB-11D4-9FEA-00C04F6BC78E}')
    _idlflags_ = ['oleautomation']
IRemoveLayerOperation._methods_ = [
    COMMETHOD(['propput', helpstring(u'The layer to remove.')], HRESULT, 'Layer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer), 'rhs' )),
    COMMETHOD(['propput', helpstring(u'The map.')], HRESULT, 'Map',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMap), 'rhs' )),
]
################################################################
## code template for IRemoveLayerOperation implementation
##class IRemoveLayerOperation_Impl(object):
##    def _set(self, rhs):
##        u'The map.'
##    Map = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'The layer to remove.'
##    Layer = property(fset = _set, doc = _set.__doc__)
##

class IContentsView3(IContentsView2):
    _case_insensitive_ = True
    _iid_ = GUID('{E4D75693-5FC8-4311-B990-B3D53138DEE3}')
    _idlflags_ = ['oleautomation']
IContentsView3._methods_ = [
    COMMETHOD(['propget', helpstring(u'Bitmap shown in Table Of Contents window toolbar.')], HRESULT, 'Bitmap',
              ( ['retval', 'out'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.OLE_HANDLE), 'Bitmap' )),
    COMMETHOD(['propget'], HRESULT, 'Tooltip',
              ( ['retval', 'out'], POINTER(BSTR), 'Tooltip' )),
]
################################################################
## code template for IContentsView3 implementation
##class IContentsView3_Impl(object):
##    @property
##    def Tooltip(self):
##        '-no docstring-'
##        #return Tooltip
##
##    @property
##    def Bitmap(self):
##        u'Bitmap shown in Table Of Contents window toolbar.'
##        #return Bitmap
##

class ISummarizeUI(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that summarize a table by an attribute.'
    _iid_ = GUID('{6EA934A3-1F85-11D4-A69E-0008C7D3AE8D}')
    _idlflags_ = ['oleautomation']
ISummarizeUI._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The summarize table.')], HRESULT, 'SummarizeTable',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable), 'rhs' )),
    COMMETHOD(['propputref', helpstring(u'The summarize field.')], HRESULT, 'SummarizeField',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IField), 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether to summarize only on selected records.')], HRESULT, 'SummarizeOnSelectedOnly',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD(['propputref', helpstring(u'The reference to the application to which this window belongs.')], HRESULT, 'Application',
              ( ['in'], POINTER(IDispatch), 'rhs' )),
    COMMETHOD([helpstring(u'Shows or hides the window.')], HRESULT, 'DoModal',
              ( ['in'], comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.OLE_HANDLE, 'parentWindow' )),
]
################################################################
## code template for ISummarizeUI implementation
##class ISummarizeUI_Impl(object):
##    def Application(self, rhs):
##        u'The reference to the application to which this window belongs.'
##        #return 
##
##    def _set(self, rhs):
##        u'Indicates whether to summarize only on selected records.'
##    SummarizeOnSelectedOnly = property(fset = _set, doc = _set.__doc__)
##
##    def SummarizeField(self, rhs):
##        u'The summarize field.'
##        #return 
##
##    def DoModal(self, parentWindow):
##        u'Shows or hides the window.'
##        #return 
##
##    def SummarizeTable(self, rhs):
##        u'The summarize table.'
##        #return 
##

class IRemoveLayerOperation2(IRemoveLayerOperation):
    _case_insensitive_ = True
    u'Provides access to members that control the Remove layer operation.'
    _iid_ = GUID('{628428DA-4DE3-46A1-AAD4-BAA1D293B2E9}')
    _idlflags_ = ['oleautomation']
IRemoveLayerOperation2._methods_ = [
    COMMETHOD(['propput', helpstring(u'The group layer from which the layer needs to be removed.')], HRESULT, 'GroupLayer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IGroupLayer), 'rhs' )),
]
################################################################
## code template for IRemoveLayerOperation2 implementation
##class IRemoveLayerOperation2_Impl(object):
##    def _set(self, rhs):
##        u'The group layer from which the layer needs to be removed.'
##    GroupLayer = property(fset = _set, doc = _set.__doc__)
##

class IDissolveUI(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that dissolve features by a common attribute value.'
    _iid_ = GUID('{21A43A5F-DB29-11D2-9F29-00C04F6BC886}')
    _idlflags_ = ['oleautomation']
IDissolveUI._methods_ = [
    COMMETHOD(['propputref', helpstring(u'A reference to the application to which this window belongs.')], HRESULT, 'Application',
              ( ['in'], POINTER(IDispatch), 'rhs' )),
    COMMETHOD([helpstring(u'Shows or hides the window.')], HRESULT, 'DoModal',
              ( ['in'], comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.OLE_HANDLE, 'parentWindow' )),
]
################################################################
## code template for IDissolveUI implementation
##class IDissolveUI_Impl(object):
##    def Application(self, rhs):
##        u'A reference to the application to which this window belongs.'
##        #return 
##
##    def DoModal(self, parentWindow):
##        u'Shows or hides the window.'
##        #return 
##

class ISelectFeaturesOperation(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Select Features operation.'
    _iid_ = GUID('{347CB77F-0F2A-11D4-9FEC-00C04F6BC78E}')
    _idlflags_ = ['oleautomation']
ISelectFeaturesOperation._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The layer from which to select features.')], HRESULT, 'Layer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer), 'rhs' )),
    COMMETHOD(['propputref', helpstring(u'The selection set.')], HRESULT, 'SelectionSet',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ISelectionSet), 'rhs' )),
    COMMETHOD(['propputref', helpstring(u'The active view (for refresh).')], HRESULT, 'ActiveView',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IActiveView), 'rhs' )),
]
################################################################
## code template for ISelectFeaturesOperation implementation
##class ISelectFeaturesOperation_Impl(object):
##    def Layer(self, rhs):
##        u'The layer from which to select features.'
##        #return 
##
##    def ActiveView(self, rhs):
##        u'The active view (for refresh).'
##        #return 
##
##    def SelectionSet(self, rhs):
##        u'The selection set.'
##        #return 
##

class IApplicationWindows(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the DataWindow Container.'
    _iid_ = GUID('{01030199-17AC-11D4-9FED-00C04F6BC78E}')
    _idlflags_ = ['oleautomation']
IApplicationWindows._methods_ = [
    COMMETHOD(['propget', helpstring(u'The data windows in the application.')], HRESULT, 'DataWindows',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISet)), 'DataWindows' )),
]
################################################################
## code template for IApplicationWindows implementation
##class IApplicationWindows_Impl(object):
##    @property
##    def DataWindows(self):
##        u'The data windows in the application.'
##        #return DataWindows
##

ITableProperty3._methods_ = [
    COMMETHOD(['propput', helpstring(u'Indicates if the Selected table is shown.')], HRESULT, 'SelectedTable',
              ( ['in'], VARIANT_BOOL, 'pShowSelectedTable' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the Selected table is shown.')], HRESULT, 'SelectedTable',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pShowSelectedTable' )),
    COMMETHOD(['propputref', helpstring(u'Layer for table window (Overrides table and featurelayer setting).')], HRESULT, 'Layer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer), 'ppLayer' )),
    COMMETHOD(['propget', helpstring(u'Layer for table window (Overrides table and featurelayer setting).')], HRESULT, 'Layer',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer)), 'ppLayer' )),
    COMMETHOD(['propputref', helpstring(u'StandaloneTable for table window (Overrides table and layer setting).')], HRESULT, 'StandaloneTable',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IStandaloneTable), 'ppStandaloneTable' )),
    COMMETHOD(['propget', helpstring(u'StandaloneTable for table window (Overrides table and layer setting).')], HRESULT, 'StandaloneTable',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IStandaloneTable)), 'ppStandaloneTable' )),
]
################################################################
## code template for ITableProperty3 implementation
##class ITableProperty3_Impl(object):
##    @property
##    def StandaloneTable(self, ppStandaloneTable):
##        u'StandaloneTable for table window (Overrides table and layer setting).'
##        #return 
##
##    @property
##    def Layer(self, ppLayer):
##        u'Layer for table window (Overrides table and featurelayer setting).'
##        #return 
##
##    def _get(self):
##        u'Indicates if the Selected table is shown.'
##        #return pShowSelectedTable
##    def _set(self, pShowSelectedTable):
##        u'Indicates if the Selected table is shown.'
##    SelectedTable = property(_get, _set, doc = _set.__doc__)
##

class IDissolveUIAdmin(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to alternative members that dissolve features by a common attribute value.'
    _iid_ = GUID('{413F8CF3-F38C-11D3-A689-0008C7D3AE8D}')
    _idlflags_ = ['oleautomation']
IDissolveUIAdmin._methods_ = [
    COMMETHOD(['propget', helpstring(u'The dissolve table.')], HRESULT, 'DissolveTable',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable)), 'ppTable' )),
    COMMETHOD(['propputref', helpstring(u'The dissolve table.')], HRESULT, 'DissolveTable',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable), 'ppTable' )),
]
################################################################
## code template for IDissolveUIAdmin implementation
##class IDissolveUIAdmin_Impl(object):
##    def DissolveTable(self, ppTable):
##        u'The dissolve table.'
##        #return 
##

IMxDocumentDropTarget._methods_ = [
    COMMETHOD([helpstring(u'Indicates if targetName can be added to the Document.')], HRESULT, 'CanCreate',
              ( ['in'], POINTER(IMxDocument), 'Document' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName), 'targetName' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'CanCreate' )),
    COMMETHOD([helpstring(u'Adds targetName to the current Document.')], HRESULT, 'Create',
              ( ['in'], POINTER(IMxDocument), 'Document' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName), 'targetName' )),
]
################################################################
## code template for IMxDocumentDropTarget implementation
##class IMxDocumentDropTarget_Impl(object):
##    def Create(self, Document, targetName):
##        u'Adds targetName to the current Document.'
##        #return 
##
##    def CanCreate(self, Document, targetName):
##        u'Indicates if targetName can be added to the Document.'
##        #return CanCreate
##

class SummarizeUI(CoClass):
    u'Window to display the summarize dialog in ArcMap.'
    _reg_clsid_ = GUID('{6EA934A4-1F85-11D4-A69E-0008C7D3AE8D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
SummarizeUI._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ISummarizeUI]

class IReportUnitFormat(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to report unit formatting.'
    _iid_ = GUID('{5FC55A41-B276-4E9C-9DCE-C54F61419DFE}')
    _idlflags_ = ['oleautomation']
IReportUnitFormat._methods_ = [
    COMMETHOD(['propget', helpstring(u'The format object used for reporting lat-lon values.')], HRESULT, 'LatLonFormat',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILatLonFormat)), 'Format' )),
    COMMETHOD(['propputref', helpstring(u'The format object used for reporting lat-lon values.')], HRESULT, 'LatLonFormat',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILatLonFormat), 'Format' )),
    COMMETHOD(['propget', helpstring(u'The format object used for reporting numeric values.')], HRESULT, 'NumericFormat',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.INumberFormat)), 'Format' )),
    COMMETHOD(['propputref', helpstring(u'The format object used for reporting numeric values.')], HRESULT, 'NumericFormat',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.INumberFormat), 'Format' )),
]
################################################################
## code template for IReportUnitFormat implementation
##class IReportUnitFormat_Impl(object):
##    def NumericFormat(self, Format):
##        u'The format object used for reporting numeric values.'
##        #return 
##
##    def LatLonFormat(self, Format):
##        u'The format object used for reporting lat-lon values.'
##        #return 
##

class ColorCorrectionDockWin(CoClass):
    u'The Color Correction Tools Dockable Window.'
    _reg_clsid_ = GUID('{508F6853-2721-4BD7-B23E-560C0E87108E}')
    _idlflags_ = ['restricted']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
ColorCorrectionDockWin._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IDockableWindowDef, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IDockableWindowInitialPlacement, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IDockableWindowImageDef, IDocumentEvents, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IActiveViewEvents, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IConnectionPointContainer]

class TimeSliderWindowCommand(CoClass):
    u'Command to open the Time Slider Window.'
    _reg_clsid_ = GUID('{4E41FC2B-1114-40D3-8326-68EAAB68D2E1}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
TimeSliderWindowCommand._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.ICommand]

class PublishOptionsPage(CoClass):
    u'Global Publishing UI Option Property Page.'
    _reg_clsid_ = GUID('{EABF531D-DF0D-433B-B729-61F93D59BDBE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
PublishOptionsPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class ColorCorrectionWindowCommand(CoClass):
    u'Opens Color Correction Window'
    _reg_clsid_ = GUID('{55A96418-18FC-486B-8C4D-F17D4320A215}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
ColorCorrectionWindowCommand._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.ICommand]

class IdentifyWindowCommand(CoClass):
    u'Command to open the Identify Window.'
    _reg_clsid_ = GUID('{20C52011-97C1-43BB-988D-7DD5E0096A62}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
IdentifyWindowCommand._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.ICommand]

class IDataConnectionPropertyPage2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Data connection property page.'
    _iid_ = GUID('{B12C31FE-4CD4-4341-A95C-72A0CFD2E83A}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriDCType'
esriDCFeatureClass = 0
esriDCTable = 1
esriDCDataFile = 2
esriDCRasterCatalog = 3
esriDCType = c_int # enum
class IDataConnectionCallback(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control Callback from data connection property page.'
    _iid_ = GUID('{206B036D-A419-11D2-A08A-0000F8775BF9}')
    _idlflags_ = ['oleautomation']
IDataConnectionPropertyPage2._methods_ = [
    COMMETHOD(['propput', helpstring(u'Indicates if all the window controls in the property page are enabled.')], HRESULT, 'Enabled',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the dialog is for new data.')], HRESULT, 'NewDataFile',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Default name when NewDataFile is true.')], HRESULT, 'DefaultName',
              ( ['in'], BSTR, 'rhs' )),
    COMMETHOD(['propput', helpstring(u"Prompt name. Default is to use 'Save As:' for saving and 'Choose:' for loading.")], HRESULT, 'PromptName',
              ( ['in'], BSTR, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Type of data we are getting or putting.')], HRESULT, 'Type',
              ( ['in'], esriDCType, 'rhs' )),
    COMMETHOD(['propget', helpstring(u'User selected Name (ie, FeatureClassName, TableName).')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName)), 'ppName' )),
    COMMETHOD(['propputref', helpstring(u'When NewDataFile is false, skip this table/featureclass in the ComboBox.')], HRESULT, 'Skip',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable), 'rhs' )),
    COMMETHOD([helpstring(u'For save dialogs, attempt to delete the table/feature class. Returns successfully if the object is delete, S_FALSE if the user requested no, or the delete error.')], HRESULT, 'AttemptToDeleteExistingName'),
    COMMETHOD(['propput', helpstring(u'Callback implementation (not mandatory).')], HRESULT, 'Callback',
              ( ['in'], POINTER(IDataConnectionCallback), 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Last location of the GxDialog.')], HRESULT, 'BrowseLocation',
              ( ['in'], BSTR, 'filter' )),
    COMMETHOD(['propget', helpstring(u'Last location of the GxDialog.')], HRESULT, 'BrowseLocation',
              ( ['retval', 'out'], POINTER(BSTR), 'filter' )),
    COMMETHOD([helpstring(u'Selects the name from the list.')], HRESULT, 'SelectName',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName), 'Name' )),
    COMMETHOD([helpstring(u'Sets the focus to the file name window.')], HRESULT, 'SetFocus'),
    COMMETHOD(['propputref', helpstring(u'Filter (optional) for the page. Determines what datasets are visible.')], HRESULT, 'DatasetFilter',
              ( ['in'], POINTER(IDatasetFilter), 'filter' )),
    COMMETHOD(['propget', helpstring(u'Filter (optional) for the page. Determines what datasets are visible.')], HRESULT, 'DatasetFilter',
              ( ['retval', 'out'], POINTER(POINTER(IDatasetFilter)), 'filter' )),
    COMMETHOD(['propputref', helpstring(u'Filter (optional) for the GxDialog.')], HRESULT, 'DialogFilter',
              ( ['in'], POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxObjectFilter), 'filter' )),
    COMMETHOD(['propget', helpstring(u'Filter (optional) for the GxDialog.')], HRESULT, 'DialogFilter',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._ADC7DE29_DC0B_448E_BBF6_27E4E34CF2EC_0_10_2.IGxObjectFilter)), 'filter' )),
    COMMETHOD([helpstring(u'A Unique Default name when NewDataFile is true.')], HRESULT, 'SetUniqueDefaultName',
              ( ['in'], BSTR, 'baseName' )),
    COMMETHOD(['propput', helpstring(u'Indicates if existing data is shown in a dropdown.')], HRESULT, 'ShowDropdown',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the option <None> is shown in a dropdown.')], HRESULT, 'ShowNone',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Indicates if a raw FDO or a display table name is returned when get_Name method is called.')], HRESULT, 'ReturnDisplayTableName',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
]
################################################################
## code template for IDataConnectionPropertyPage2 implementation
##class IDataConnectionPropertyPage2_Impl(object):
##    def SetFocus(self):
##        u'Sets the focus to the file name window.'
##        #return 
##
##    @property
##    def DatasetFilter(self, filter):
##        u'Filter (optional) for the page. Determines what datasets are visible.'
##        #return 
##
##    def AttemptToDeleteExistingName(self):
##        u'For save dialogs, attempt to delete the table/feature class. Returns successfully if the object is delete, S_FALSE if the user requested no, or the delete error.'
##        #return 
##
##    @property
##    def Name(self):
##        u'User selected Name (ie, FeatureClassName, TableName).'
##        #return ppName
##
##    def _set(self, rhs):
##        u'Callback implementation (not mandatory).'
##    Callback = property(fset = _set, doc = _set.__doc__)
##
##    def Skip(self, rhs):
##        u'When NewDataFile is false, skip this table/featureclass in the ComboBox.'
##        #return 
##
##    @property
##    def DialogFilter(self, filter):
##        u'Filter (optional) for the GxDialog.'
##        #return 
##
##    def _set(self, rhs):
##        u'Indicates if all the window controls in the property page are enabled.'
##    Enabled = property(fset = _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Last location of the GxDialog.'
##        #return filter
##    def _set(self, filter):
##        u'Last location of the GxDialog.'
##    BrowseLocation = property(_get, _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Indicates if the option <None> is shown in a dropdown.'
##    ShowNone = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Default name when NewDataFile is true.'
##    DefaultName = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Indicates if the dialog is for new data.'
##    NewDataFile = property(fset = _set, doc = _set.__doc__)
##
##    def SetUniqueDefaultName(self, baseName):
##        u'A Unique Default name when NewDataFile is true.'
##        #return 
##
##    def _set(self, rhs):
##        u'Indicates if existing data is shown in a dropdown.'
##    ShowDropdown = property(fset = _set, doc = _set.__doc__)
##
##    def SelectName(self, Name):
##        u'Selects the name from the list.'
##        #return 
##
##    def _set(self, rhs):
##        u'Type of data we are getting or putting.'
##    Type = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u"Prompt name. Default is to use 'Save As:' for saving and 'Choose:' for loading."
##    PromptName = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Indicates if a raw FDO or a display table name is returned when get_Name method is called.'
##    ReturnDisplayTableName = property(fset = _set, doc = _set.__doc__)
##

class DataGraphTWizard(CoClass):
    u'Wizard in creating data graph.'
    _reg_clsid_ = GUID('{3CBB80FC-7BAE-4897-BAA3-1CEA6B48854E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
DataGraphTWizard._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDataGraphTWizard, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDataGraphTEvents]

class GettingStartedWindow(CoClass):
    u'Getting Started Window'
    _reg_clsid_ = GUID('{853A87BE-D3A5-4160-9F92-40486091CB11}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
GettingStartedWindow._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IStartupDialog, IStartupDialog2, IStartupDialog3]

class PublishAntiAliasingPage(CoClass):
    u'Publishing UI - Anti Aliasing Property Page.'
    _reg_clsid_ = GUID('{6902497D-7647-494F-B28F-CDDA3F076E35}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
PublishAntiAliasingPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class GettingStartedSettings(CoClass):
    u'Getting Started Settings'
    _reg_clsid_ = GUID('{24F4E14A-FB6F-4B5A-8A98-8F894DAAD469}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
GettingStartedSettings._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IStartupDialogSettings]

class MapServerLayerSourcePropertyPage(CoClass):
    u"Property page for showing a map server layer's source information."
    _reg_clsid_ = GUID('{EA8C9303-60FD-45F9-A4D2-05DD2E9639C8}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
MapServerLayerSourcePropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class IDataConnectionCallback2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides more access to members that control Callback from data connection property page.'
    _iid_ = GUID('{6E76303E-8491-4F29-B5C0-2C964B4F5852}')
    _idlflags_ = ['oleautomation']
IDataConnectionCallback2._methods_ = [
    COMMETHOD([helpstring(u'The user finished an action that modified the name of the Table or Feature Class.')], HRESULT, 'NameChangeFinished'),
]
################################################################
## code template for IDataConnectionCallback2 implementation
##class IDataConnectionCallback2_Impl(object):
##    def NameChangeFinished(self):
##        u'The user finished an action that modified the name of the Table or Feature Class.'
##        #return 
##

class IFindWindow2(IFindWindow):
    _case_insensitive_ = True
    u'Provides access to additional control of the Find Window. Deprecated. Please consider using the IFind interface in the Carto library instead.'
    _iid_ = GUID('{F609E798-026D-435A-8627-039275ECF606}')
    _idlflags_ = ['oleautomation']
IFindWindow2._methods_ = [
    COMMETHOD(['propput', helpstring(u'The component category to use in the Find Window.')], HRESULT, 'CategoryID',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID), 'rhs' )),
]
################################################################
## code template for IFindWindow2 implementation
##class IFindWindow2_Impl(object):
##    def _set(self, rhs):
##        u'The component category to use in the Find Window.'
##    CategoryID = property(fset = _set, doc = _set.__doc__)
##

class AddQueryTableDialog(CoClass):
    u'Add Query table dialog.'
    _reg_clsid_ = GUID('{2E475C22-41BD-4CDA-BE0D-AF2D5AC69D7C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
AddQueryTableDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IAddDataDialog, IAddDataDialog2]

class IAIAProperties(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control AIA window properties.'
    _iid_ = GUID('{F0269AE8-86FD-442A-B746-BF10219F9099}')
    _idlflags_ = ['oleautomation', 'restricted']
IAIAProperties._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The active layer.')], HRESULT, 'Layer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer), 'ppLayer' )),
    COMMETHOD(['propget', helpstring(u'The active layer.')], HRESULT, 'Layer',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer)), 'ppLayer' )),
]
################################################################
## code template for IAIAProperties implementation
##class IAIAProperties_Impl(object):
##    @property
##    def Layer(self, ppLayer):
##        u'The active layer.'
##        #return 
##

IMetadataViewWindow3._methods_ = [
    COMMETHOD(['propputref', helpstring(u'Pass the server object name to Metadata View window.')], HRESULT, 'AGSServerObjectName',
              ( ['in'], POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IAGSServerObjectName), 'rhs' )),
]
################################################################
## code template for IMetadataViewWindow3 implementation
##class IMetadataViewWindow3_Impl(object):
##    def AGSServerObjectName(self, rhs):
##        u'Pass the server object name to Metadata View window.'
##        #return 
##

class IDataConnectionPropertyPage(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Data connection property page.'
    _iid_ = GUID('{26056537-9EBC-11D2-A089-0000F8775BF9}')
    _idlflags_ = ['oleautomation']
IDataConnectionPropertyPage._methods_ = [
    COMMETHOD(['propput', helpstring(u'Indicates if all the window controls in the property page are enabled.')], HRESULT, 'Enabled',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the dialog is for new data.')], HRESULT, 'NewDataFile',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Default name when NewDataFile is true.')], HRESULT, 'DefaultName',
              ( ['in'], BSTR, 'rhs' )),
    COMMETHOD(['propput', helpstring(u"Prompt name. Default is to use 'Save As:' for saving and 'Choose:' for loading.")], HRESULT, 'PromptName',
              ( ['in'], BSTR, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Type of data we are getting or putting.')], HRESULT, 'Type',
              ( ['in'], esriDCType, 'rhs' )),
    COMMETHOD(['propget', helpstring(u'User selected Name (ie, FeatureClassName, TableName).')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName)), 'ppName' )),
    COMMETHOD(['propputref', helpstring(u'When NewDataFile is false, skip this table/featureclass in the ComboBox.')], HRESULT, 'Skip',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable), 'rhs' )),
    COMMETHOD([helpstring(u'For save dialogs, attempt to delete the table/feature class. Returns successfully if the object is delete, S_FALSE if the user requested no, or the delete error.')], HRESULT, 'AttemptToDeleteExistingName'),
    COMMETHOD(['propput', helpstring(u'Callback implementation (not mandatory).')], HRESULT, 'Callback',
              ( ['in'], POINTER(IDataConnectionCallback), 'rhs' )),
]
################################################################
## code template for IDataConnectionPropertyPage implementation
##class IDataConnectionPropertyPage_Impl(object):
##    def AttemptToDeleteExistingName(self):
##        u'For save dialogs, attempt to delete the table/feature class. Returns successfully if the object is delete, S_FALSE if the user requested no, or the delete error.'
##        #return 
##
##    @property
##    def Name(self):
##        u'User selected Name (ie, FeatureClassName, TableName).'
##        #return ppName
##
##    def _set(self, rhs):
##        u'Callback implementation (not mandatory).'
##    Callback = property(fset = _set, doc = _set.__doc__)
##
##    def Skip(self, rhs):
##        u'When NewDataFile is false, skip this table/featureclass in the ComboBox.'
##        #return 
##
##    def _set(self, rhs):
##        u'Indicates if all the window controls in the property page are enabled.'
##    Enabled = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Default name when NewDataFile is true.'
##    DefaultName = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Indicates if the dialog is for new data.'
##    NewDataFile = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Type of data we are getting or putting.'
##    Type = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u"Prompt name. Default is to use 'Save As:' for saving and 'Choose:' for loading."
##    PromptName = property(fset = _set, doc = _set.__doc__)
##

class SelectByCommonValueTool(CoClass):
    u'Tool for selecting features by a common attribute value.'
    _reg_clsid_ = GUID('{7C53CA18-42C5-499E-AE78-4FDAF1183BC9}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
SelectByCommonValueTool._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.ICommand, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.ITool]

class RotateOperation(CoClass):
    u'Operation for handling rotation.'
    _reg_clsid_ = GUID('{D27E809F-806E-11D1-8723-0000F8751720}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
RotateOperation._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IRotateOperation, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IOperation]

class QueryAttributes(CoClass):
    u'Display query attribute dialog in Mx.'
    _reg_clsid_ = GUID('{9E138103-6DCC-11D2-A07E-0000F8775BF9}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
class IQueryAttributes(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Attribute query window.'
    _iid_ = GUID('{9E138101-6DCC-11D2-A07E-0000F8775BF9}')
    _idlflags_ = ['oleautomation']
QueryAttributes._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IQueryAttributes, IModelessQueryAttributes, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IObjectClassSchemaEvents]

class ExcludeUnselectedFeaturesCommand(CoClass):
    u"Adds all unselected features in all layers to the layer's exclusion set, so those feature will not draw."
    _reg_clsid_ = GUID('{DDF3DCEB-CB04-49BE-B61A-BB7D30E2D1F8}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
ExcludeUnselectedFeaturesCommand._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.ICommand]

class IFindPanelEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to events that control communication from find pages to the main find form.'
    _iid_ = GUID('{8F8DE9D8-3A48-11D3-9F58-00C04F8ED1C4}')
    _idlflags_ = ['oleautomation']
IFindPanelEvents._methods_ = [
    COMMETHOD([helpstring(u'Notifies Find Dialog that the outputs of the find panel have changed.')], HRESULT, 'OutputsChanged'),
    COMMETHOD([helpstring(u'Tells Find Dialog to execute a find.  If the parameter passed is true, the dialog will only find if there are already results showing.')], HRESULT, 'ExecuteFind',
              ( [], VARIANT_BOOL, 'refreshResultsOnly' )),
]
################################################################
## code template for IFindPanelEvents implementation
##class IFindPanelEvents_Impl(object):
##    def OutputsChanged(self):
##        u'Notifies Find Dialog that the outputs of the find panel have changed.'
##        #return 
##
##    def ExecuteFind(self, refreshResultsOnly):
##        u'Tells Find Dialog to execute a find.  If the parameter passed is true, the dialog will only find if there are already results showing.'
##        #return 
##

class DataConnectionCallback(CoClass):
    u'DataConnectionCallback.'
    _reg_clsid_ = GUID('{206B036E-A419-11D2-A08A-0000F8775BF9}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
DataConnectionCallback._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDataConnectionCallback]

IMoveLayersOperation._methods_ = [
    COMMETHOD([helpstring(u'Information of the layer to be moved. Source group is NULL if the layer belongs to a map. This method can be called repeatedly until all the layers are added.')], HRESULT, 'AddLayerInfo',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer), 'Layer' ),
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMap), 'pSourceMap' ),
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IGroupLayer), 'pSourceGroup' )),
    COMMETHOD([helpstring(u'Information regarding where the the layer needs to be moved. Destination group is NULL if the layer is bing moved to into a map.')], HRESULT, 'SetDestinationInfo',
              ( ['in'], c_int, 'toIndex' ),
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMap), 'pDestinationMap' ),
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IGroupLayer), 'pDestinationGroup' )),
]
################################################################
## code template for IMoveLayersOperation implementation
##class IMoveLayersOperation_Impl(object):
##    def AddLayerInfo(self, Layer, pSourceMap, pSourceGroup):
##        u'Information of the layer to be moved. Source group is NULL if the layer belongs to a map. This method can be called repeatedly until all the layers are added.'
##        #return 
##
##    def SetDestinationInfo(self, toIndex, pDestinationMap, pDestinationGroup):
##        u'Information regarding where the the layer needs to be moved. Destination group is NULL if the layer is bing moved to into a map.'
##        #return 
##

class AnnotateSelectedFeatures(CoClass):
    u'Display annotate selected features dialog.'
    _reg_clsid_ = GUID('{9CCB85EB-9EA0-46F7-BC34-E06A0E764420}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
class IAnnotateSelectedFeatures(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the annotate selected features.'
    _iid_ = GUID('{F23F890A-CF0F-4249-8501-69F41FA25943}')
    _idlflags_ = ['oleautomation']
AnnotateSelectedFeatures._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IAnnotateSelectedFeatures]

class FindWindowUI(CoClass):
    u'Window to display Find dialog in. Deprecated. Please consider using the IFind interface in the Carto library instead.'
    _reg_clsid_ = GUID('{212A710D-4C00-11D2-A079-0000F8775BF9}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
FindWindowUI._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IFindWindow, IFindWindow2, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IActiveViewEvents, IDocumentEvents, IFindPanelEvents]

class DataConnectionPropertyPage(CoClass):
    u'Data Connection Property Page.'
    _reg_clsid_ = GUID('{26056536-9EBC-11D2-A089-0000F8775BF9}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
DataConnectionPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDataConnectionPropertyPage, IDataConnectionPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class RestoreExcludedFeaturesCommand(CoClass):
    u"Removes features from all layers' exclusion sets."
    _reg_clsid_ = GUID('{57972E1E-4A2A-44EE-AA63-3180AC5D4542}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
RestoreExcludedFeaturesCommand._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.ICommand]

class MapServerSublayersPropertyPage(CoClass):
    u"Property page for showing a map server layer's sublayer information."
    _reg_clsid_ = GUID('{4D6CAB29-5A91-4AD0-A636-CCA3D56BDED3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
MapServerSublayersPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class FindFeatures(CoClass):
    u'Provides access to FindFeatures. Create a class with this interface (and add to category) for custom find dialog page.'
    _reg_clsid_ = GUID('{8803C8F0-75FE-11D3-A6A6-0008C7D3AE50}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
class IFinder(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to IFinder interface for the MxFind routine. Implement this interface to create a custom find dialog page.'
    _iid_ = GUID('{D7410CC7-5239-11D2-A079-0000F8775BF9}')
    _idlflags_ = ['oleautomation']
FindFeatures._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IFinder]

class MapServerLayerAdvancedPropertyPage(CoClass):
    u"Property page for showing a map server layer's advanced properties."
    _reg_clsid_ = GUID('{876547E2-F826-4BE9-BE79-059DDD5016D4}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
MapServerLayerAdvancedPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class RasterTableShowMultiItem(CoClass):
    u'A coclass shows multi-item menu of a RasterTable.'
    _reg_clsid_ = GUID('{CE0B7870-9556-11D2-AAD7-00C04FA375FB}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
RasterTableShowMultiItem._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IMultiItem]

class IRasterDockWin(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{743CBF92-694D-41EA-8FF8-E245431F3AC3}')
    _idlflags_ = []
IRasterDockWin._methods_ = [
    COMMETHOD([helpstring(u'Updates child windows')], HRESULT, 'Update'),
    COMMETHOD([helpstring(u'Updates child windows')], HRESULT, 'UpdateResult',
              ( [], BSTR, 'measure' )),
]
################################################################
## code template for IRasterDockWin implementation
##class IRasterDockWin_Impl(object):
##    def UpdateResult(self, measure):
##        u'Updates child windows'
##        #return 
##
##    def Update(self):
##        u'Updates child windows'
##        #return 
##

class RemoveLayerOperation(CoClass):
    u'Remove Layer Operation.'
    _reg_clsid_ = GUID('{A231C0E3-0BDB-11D4-9FEA-00C04F6BC78E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
RemoveLayerOperation._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IOperation, IRemoveLayerOperation, IRemoveLayerOperation2]

IFinder._methods_ = [
    COMMETHOD([helpstring(u'Called to initialize control.')], HRESULT, 'InitializeControl',
              ( ['in'], POINTER(comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IApplication), 'pApplication' ),
              ( ['in'], POINTER(IFindPanelEvents), 'pFindEventsCallBack' )),
    COMMETHOD([helpstring(u'Called whenever ArcMap status changes.')], HRESULT, 'UpdateControl'),
    COMMETHOD(['propget', helpstring(u'The control name. Used for the FindUI tab.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'Number of columns to display in list box.')], HRESULT, 'ColumnCount',
              ( ['retval', 'out'], POINTER(c_int), 'ColumnCount' )),
    COMMETHOD(['propget', helpstring(u'The column name.')], HRESULT, 'ColumnName',
              ( ['in'], c_int, 'column' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ColumnName' )),
    COMMETHOD(['propget', helpstring(u'The column width in Dialog Units (1/4 of avg. char width).')], HRESULT, 'ColumnWidth',
              ( ['in'], c_int, 'column' ),
              ( ['retval', 'out'], POINTER(c_int), 'width' )),
    COMMETHOD(['propget', helpstring(u'UID of menu to popup in list box.')], HRESULT, 'MenuUID',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID)), 'pNameOrID' )),
    COMMETHOD([helpstring(u'Perform find functionality.')], HRESULT, 'Find',
              ( ['in'], POINTER(IFindCallBack), 'pFindCallBack' )),
    COMMETHOD([helpstring(u'User requested find to stop.')], HRESULT, 'Stop'),
    COMMETHOD([helpstring(u'New search. Clear control input boxes.')], HRESULT, 'NewSearch'),
    COMMETHOD(['propget', helpstring(u'The window handle for the finder.')], HRESULT, 'hWnd',
              ( ['retval', 'out'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.OLE_HANDLE), 'hWnd' )),
]
################################################################
## code template for IFinder implementation
##class IFinder_Impl(object):
##    @property
##    def ColumnCount(self):
##        u'Number of columns to display in list box.'
##        #return ColumnCount
##
##    def UpdateControl(self):
##        u'Called whenever ArcMap status changes.'
##        #return 
##
##    @property
##    def Name(self):
##        u'The control name. Used for the FindUI tab.'
##        #return Name
##
##    def InitializeControl(self, pApplication, pFindEventsCallBack):
##        u'Called to initialize control.'
##        #return 
##
##    @property
##    def ColumnWidth(self, column):
##        u'The column width in Dialog Units (1/4 of avg. char width).'
##        #return width
##
##    def Stop(self):
##        u'User requested find to stop.'
##        #return 
##
##    @property
##    def ColumnName(self, column):
##        u'The column name.'
##        #return ColumnName
##
##    def NewSearch(self):
##        u'New search. Clear control input boxes.'
##        #return 
##
##    @property
##    def hWnd(self):
##        u'The window handle for the finder.'
##        #return hWnd
##
##    def Find(self, pFindCallBack):
##        u'Perform find functionality.'
##        #return 
##
##    @property
##    def MenuUID(self):
##        u'UID of menu to popup in list box.'
##        #return pNameOrID
##

class ITableFrame(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control table frames.'
    _iid_ = GUID('{23514918-7189-44FD-B7F1-71CB973ACA26}')
    _idlflags_ = ['oleautomation']
ITableFrame._methods_ = [
    COMMETHOD(['propput', helpstring(u'The table view to show.')], HRESULT, 'TableView',
              ( ['in'], POINTER(comtypes.gen._4A9C9ED7_F7DB_4614_B480_A5D265C961FC_0_10_2.ITableView), 'TableView' )),
    COMMETHOD(['propget', helpstring(u'The table view to show.')], HRESULT, 'TableView',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._4A9C9ED7_F7DB_4614_B480_A5D265C961FC_0_10_2.ITableView)), 'TableView' )),
    COMMETHOD(['propputref', helpstring(u'The table (either standalone table or feature layer).')], HRESULT, 'Table',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable), 'ppTable' )),
    COMMETHOD(['propget', helpstring(u'The table (either standalone table or feature layer).')], HRESULT, 'Table',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable)), 'ppTable' )),
    COMMETHOD(['propput', helpstring(u'The table property.')], HRESULT, 'TableProperty',
              ( ['in'], POINTER(ITableProperty), 'TableProperty' )),
    COMMETHOD(['propget', helpstring(u'The table property.')], HRESULT, 'TableProperty',
              ( ['retval', 'out'], POINTER(POINTER(ITableProperty)), 'TableProperty' )),
    COMMETHOD(['propput', helpstring(u'The first row to display.')], HRESULT, 'StartRow',
              ( ['in'], c_int, 'StartRow' )),
    COMMETHOD(['propget', helpstring(u'The first row to display.')], HRESULT, 'StartRow',
              ( ['retval', 'out'], POINTER(c_int), 'StartRow' )),
    COMMETHOD(['propput', helpstring(u'The first column to display.')], HRESULT, 'StartCol',
              ( ['in'], c_int, 'StartCol' )),
    COMMETHOD(['propget', helpstring(u'The first column to display.')], HRESULT, 'StartCol',
              ( ['retval', 'out'], POINTER(c_int), 'StartCol' )),
]
################################################################
## code template for ITableFrame implementation
##class ITableFrame_Impl(object):
##    def _get(self):
##        u'The first row to display.'
##        #return StartRow
##    def _set(self, StartRow):
##        u'The first row to display.'
##    StartRow = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Table(self, ppTable):
##        u'The table (either standalone table or feature layer).'
##        #return 
##
##    def _get(self):
##        u'The table property.'
##        #return TableProperty
##    def _set(self, TableProperty):
##        u'The table property.'
##    TableProperty = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The first column to display.'
##        #return StartCol
##    def _set(self, StartCol):
##        u'The first column to display.'
##    StartCol = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The table view to show.'
##        #return TableView
##    def _set(self, TableView):
##        u'The table view to show.'
##    TableView = property(_get, _set, doc = _set.__doc__)
##

class MoveMapsOperation(CoClass):
    u'Move Maps Operation.'
    _reg_clsid_ = GUID('{AF28C650-46DB-4B07-8D46-84F6B965DD2B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
MoveMapsOperation._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IOperation, IMoveMapsOperation]

class SelectFeaturesOperation(CoClass):
    u'Select Features Operation.'
    _reg_clsid_ = GUID('{347CB780-0F2A-11D4-9FEC-00C04F6BC78E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
SelectFeaturesOperation._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IOperation, ISelectFeaturesOperation]

class IMensurationResult(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control mensuration result.'
    _iid_ = GUID('{210ED094-AE87-44DE-B676-2F01C9958A8E}')
    _idlflags_ = []
IMensurationResult._methods_ = [
    COMMETHOD([helpstring(u'Update measurement result')], HRESULT, 'UpdateMessage',
              ( ['in'], BSTR, 'Type' ),
              ( ['in'], BSTR, 'comment' ),
              ( ['in'], BSTR, 'id' ),
              ( ['in'], BSTR, 'result' ),
              ( ['in'], BSTR, 'headline' )),
    COMMETHOD([helpstring(u'Update result lists')], HRESULT, 'UpdateResultList',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray), 'pComments' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray), 'pIDs' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray), 'pTypes' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray), 'pSelections' )),
]
################################################################
## code template for IMensurationResult implementation
##class IMensurationResult_Impl(object):
##    def UpdateResultList(self, pComments, pIDs, pTypes, pSelections):
##        u'Update result lists'
##        #return 
##
##    def UpdateMessage(self, Type, comment, id, result, headline):
##        u'Update measurement result'
##        #return 
##

IRemoveLayersOperation._methods_ = [
    COMMETHOD([helpstring(u'Adds the information of the layer that needs to be removed.')], HRESULT, 'AddLayerInfo',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer), 'pLayer' ),
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMap), 'pSourceMap' ),
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IGroupLayer), 'pSourceGroup' )),
]
################################################################
## code template for IRemoveLayersOperation implementation
##class IRemoveLayersOperation_Impl(object):
##    def AddLayerInfo(self, pLayer, pSourceMap, pSourceGroup):
##        u'Adds the information of the layer that needs to be removed.'
##        #return 
##

class IMSFeatureLayerSymbology(CoClass):
    u'Defines the symbology for an IMS feature layer.'
    _reg_clsid_ = GUID('{5F3364FF-599B-4AFD-83C2-EDD36EE74C23}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
IMSFeatureLayerSymbology._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IFeatureLayerSymbology]

class ElementNewOperation(CoClass):
    u'Command for adding new maps to a layout.'
    _reg_clsid_ = GUID('{C22579D6-BC17-11D0-8667-0000F8751720}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
ElementNewOperation._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IElementOperation, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IOperation]

class ElementSelection(CoClass):
    u'Maintains the the graphic element selection.'
    _reg_clsid_ = GUID('{85DCFD04-8E4F-11D4-A697-00508B4A4114}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
ElementSelection._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ISelection, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IEnumElement, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IConnectionPointContainer]
ElementSelection._outgoing_interfaces_ = [comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ISelectionEvents]

class EnhMetaFileClipboardFormat(CoClass):
    u'Enhanced Metafile Clipboard Format(EMF).'
    _reg_clsid_ = GUID('{52BB5362-947E-11D2-ACFF-0000F87808EE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
EnhMetaFileClipboardFormat._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IClipboardFormat, IClipboardFormat2]

IDataConnectionCallback._methods_ = [
    COMMETHOD([helpstring(u'Table or FeatureClass changed.')], HRESULT, 'NameChanged'),
]
################################################################
## code template for IDataConnectionCallback implementation
##class IDataConnectionCallback_Impl(object):
##    def NameChanged(self):
##        u'Table or FeatureClass changed.'
##        #return 
##

class IViewCommand(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control view commands.'
    _iid_ = GUID('{565FAF4D-5961-11D3-B8C5-00600802E603}')
    _idlflags_ = ['oleautomation']
IViewCommand._methods_ = [
    COMMETHOD(['propget', helpstring(u'The selection object used by the associated view.')], HRESULT, 'Selection',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ISelection)), 'Selection' )),
    COMMETHOD([helpstring(u'Indicates if command works with the specified view.')], HRESULT, 'Applies',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IActiveView), 'view' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Applies' )),
]
################################################################
## code template for IViewCommand implementation
##class IViewCommand_Impl(object):
##    @property
##    def Selection(self):
##        u'The selection object used by the associated view.'
##        #return Selection
##
##    def Applies(self, view):
##        u'Indicates if command works with the specified view.'
##        #return Applies
##

class ProgressAnimation(CoClass):
    u'ProgressAnimation object.'
    _reg_clsid_ = GUID('{4E46AF53-9741-462D-AE1A-8DDAF6E1AF7C}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
ProgressAnimation._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IProgressor, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IAnimationProgressor]

ITinHistogram._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The TIN used to define the histogram.')], HRESULT, 'Tin',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITin), 'Tin' )),
    COMMETHOD(['propget', helpstring(u'The TIN used to define the histogram.')], HRESULT, 'Tin',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITin)), 'Tin' )),
    COMMETHOD(['propputref', helpstring(u'The TIN histogram data sampling.')], HRESULT, 'Sampling',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDataSampling), 'dataSampling' )),
    COMMETHOD(['propget', helpstring(u'The TIN histogram data sampling.')], HRESULT, 'Sampling',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDataSampling)), 'dataSampling' )),
    COMMETHOD(['propput', helpstring(u'The TIN histogram type.')], HRESULT, 'HistogramType',
              ( ['in'], esriTinHistogramType, 'pType' )),
    COMMETHOD(['propget', helpstring(u'The TIN histogram type.')], HRESULT, 'HistogramType',
              ( ['retval', 'out'], POINTER(esriTinHistogramType), 'pType' )),
]
################################################################
## code template for ITinHistogram implementation
##class ITinHistogram_Impl(object):
##    @property
##    def Tin(self, Tin):
##        u'The TIN used to define the histogram.'
##        #return 
##
##    def _get(self):
##        u'The TIN histogram type.'
##        #return pType
##    def _set(self, pType):
##        u'The TIN histogram type.'
##    HistogramType = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Sampling(self, dataSampling):
##        u'The TIN histogram data sampling.'
##        #return 
##

IAddDataDialog._methods_ = [
    COMMETHOD(['propput', helpstring(u'The document.')], HRESULT, 'Document',
              ( [], POINTER(IMxDocument), 'rhs' )),
    COMMETHOD(['propput', helpstring(u'The map.')], HRESULT, 'Map',
              ( [], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMap), 'rhs' )),
    COMMETHOD([helpstring(u'Indicates if the dialog is shown and adds the data.')], HRESULT, 'Show',
              ( ['in'], comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.OLE_HANDLE, 'parentHWnd' ),
              ( [], POINTER(VARIANT_BOOL), 'ok' )),
]
################################################################
## code template for IAddDataDialog implementation
##class IAddDataDialog_Impl(object):
##    def _set(self, rhs):
##        u'The map.'
##    Map = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'The document.'
##    Document = property(fset = _set, doc = _set.__doc__)
##
##    def Show(self, parentHWnd, ok):
##        u'Indicates if the dialog is shown and adds the data.'
##        #return 
##

IAddDataDialog2._methods_ = [
    COMMETHOD(['propput', helpstring(u'The group layer to which data needs to be added.')], HRESULT, 'GroupLayer',
              ( [], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IGroupLayer), 'rhs' )),
]
################################################################
## code template for IAddDataDialog2 implementation
##class IAddDataDialog2_Impl(object):
##    def _set(self, rhs):
##        u'The group layer to which data needs to be added.'
##    GroupLayer = property(fset = _set, doc = _set.__doc__)
##

class IViewCommandToolbars(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control view commands which have toolbars associated with them.'
    _iid_ = GUID('{7BA357DF-3D21-4A17-B027-B1A515CCDFFC}')
    _idlflags_ = ['oleautomation']
IViewCommandToolbars._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if toolbars associated with the view should be shown automatically.')], HRESULT, 'AutoShowToolbars',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'autoShow' )),
    COMMETHOD(['propput', helpstring(u'Indicates if toolbars associated with the view should be shown automatically.')], HRESULT, 'AutoShowToolbars',
              ( ['in'], VARIANT_BOOL, 'autoShow' )),
    COMMETHOD([helpstring(u'Shows or hides the toolbars associated with a view.')], HRESULT, 'ShowToolbars',
              ( ['in'], VARIANT_BOOL, 'Show' )),
]
################################################################
## code template for IViewCommandToolbars implementation
##class IViewCommandToolbars_Impl(object):
##    def _get(self):
##        u'Indicates if toolbars associated with the view should be shown automatically.'
##        #return autoShow
##    def _set(self, autoShow):
##        u'Indicates if toolbars associated with the view should be shown automatically.'
##    AutoShowToolbars = property(_get, _set, doc = _set.__doc__)
##
##    def ShowToolbars(self, Show):
##        u'Shows or hides the toolbars associated with a view.'
##        #return 
##

IReferenceScaleOperation._methods_ = [
    COMMETHOD(['propput', helpstring(u'The name of this operation.')], HRESULT, 'Name',
              ( [], BSTR, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'The map that the Reference Scale operates on.')], HRESULT, 'Map',
              ( [], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMap), 'rhs' )),
    COMMETHOD(['propput', helpstring(u'The previous Reference Scale.')], HRESULT, 'PreviousScale',
              ( [], c_double, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'The new Reference Scale.')], HRESULT, 'ReferenceScale',
              ( [], c_double, 'rhs' )),
]
################################################################
## code template for IReferenceScaleOperation implementation
##class IReferenceScaleOperation_Impl(object):
##    def _set(self, rhs):
##        u'The map that the Reference Scale operates on.'
##    Map = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'The name of this operation.'
##    Name = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'The previous Reference Scale.'
##    PreviousScale = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'The new Reference Scale.'
##    ReferenceScale = property(fset = _set, doc = _set.__doc__)
##

class IdentifyWindow(CoClass):
    u'Esri map identify window.'
    _reg_clsid_ = GUID('{4A2EE508-46EB-4AC8-AE21-D17A11DCCA4E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
IdentifyWindow._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IDockableWindowDef, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IDockableWindowImageDef, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IDockableWindowInitialPlacement]

class NewDocumentDialog(CoClass):
    u'New Document Dialog'
    _reg_clsid_ = GUID('{48CCE6A1-E50B-462C-B122-40789D5E243A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
NewDocumentDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, INewDocumentDialog]

class IAnnotateFeaturesCallback(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members for the annotate selected features callback.'
    _iid_ = GUID('{16383483-A0DA-4ADC-B51D-9BFFED43DE59}')
    _idlflags_ = ['oleautomation']
IAnnotateFeaturesCallback._methods_ = [
    COMMETHOD([helpstring(u'Called before anno is added.')], HRESULT, 'BeforeAnnotate',
              ( [], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IEnumLayer), 'AnnotatingLayers' )),
    COMMETHOD([helpstring(u'Called after anno is added.')], HRESULT, 'AfterAnnotate',
              ( [], VARIANT_BOOL, 'ok' )),
]
################################################################
## code template for IAnnotateFeaturesCallback implementation
##class IAnnotateFeaturesCallback_Impl(object):
##    def AfterAnnotate(self, ok):
##        u'Called after anno is added.'
##        #return 
##
##    def BeforeAnnotate(self, AnnotatingLayers):
##        u'Called before anno is added.'
##        #return 
##

IAnnotateSelectedFeatures._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The map to check for existing annotation classes.')], HRESULT, 'Map',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMap), 'rhs' )),
    COMMETHOD(['propputref', helpstring(u'The layer to annotate.')], HRESULT, 'Layer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer), 'rhs' )),
    COMMETHOD(['propputref', helpstring(u'Provides a hook before and after annotation is created.')], HRESULT, 'Callback',
              ( ['in'], POINTER(IAnnotateFeaturesCallback), 'rhs' )),
    COMMETHOD([helpstring(u'Shows annotate selected features window in a modal state.')], HRESULT, 'DoModal',
              ( ['in'], comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.OLE_HANDLE, 'parentHWnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'okPressed' )),
]
################################################################
## code template for IAnnotateSelectedFeatures implementation
##class IAnnotateSelectedFeatures_Impl(object):
##    def Map(self, rhs):
##        u'The map to check for existing annotation classes.'
##        #return 
##
##    def Layer(self, rhs):
##        u'The layer to annotate.'
##        #return 
##
##    def DoModal(self, parentHWnd):
##        u'Shows annotate selected features window in a modal state.'
##        #return okPressed
##
##    def Callback(self, rhs):
##        u'Provides a hook before and after annotation is created.'
##        #return 
##

IQueryAttributes._methods_ = [
    COMMETHOD(['propputref', helpstring(u'Provides the window with a reference to the application.')], HRESULT, 'Application',
              ( ['in'], POINTER(IDispatch), 'rhs' )),
    COMMETHOD([helpstring(u'Shows attribute query window in a modal state.')], HRESULT, 'DoModal',
              ( ['in'], comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.OLE_HANDLE, 'parentHWnd' )),
    COMMETHOD(['propput', helpstring(u'CombinationMethod on form.')], HRESULT, 'CombinationMethod',
              ( ['in'], comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.esriSelectionResultEnum, 'pMethod' )),
    COMMETHOD(['propget', helpstring(u'CombinationMethod on form.')], HRESULT, 'CombinationMethod',
              ( ['retval', 'out'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.esriSelectionResultEnum), 'pMethod' )),
    COMMETHOD(['propget', helpstring(u'Layer selected by the user.')], HRESULT, 'Layer',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer)), 'ppLayer' )),
    COMMETHOD(['propputref', helpstring(u'Layer selected by the user.')], HRESULT, 'Layer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer), 'ppLayer' )),
    COMMETHOD(['propput', helpstring(u"When the user presses OK, select features. If there is an error, don't return. Default: FALSE.")], HRESULT, 'SelectFeaturesInLayerOnOK',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Default expression.')], HRESULT, 'Expression',
              ( ['in'], BSTR, 'rhs' )),
    COMMETHOD(['propget', helpstring(u'Provide a QueryFilter after form has been executed.')], HRESULT, 'QueryFilter',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IQueryFilter)), 'ppQueryFilter' )),
]
################################################################
## code template for IQueryAttributes implementation
##class IQueryAttributes_Impl(object):
##    def Layer(self, ppLayer):
##        u'Layer selected by the user.'
##        #return 
##
##    @property
##    def QueryFilter(self):
##        u'Provide a QueryFilter after form has been executed.'
##        #return ppQueryFilter
##
##    def _set(self, rhs):
##        u"When the user presses OK, select features. If there is an error, don't return. Default: FALSE."
##    SelectFeaturesInLayerOnOK = property(fset = _set, doc = _set.__doc__)
##
##    def Application(self, rhs):
##        u'Provides the window with a reference to the application.'
##        #return 
##
##    def DoModal(self, parentHWnd):
##        u'Shows attribute query window in a modal state.'
##        #return 
##
##    def _get(self):
##        u'CombinationMethod on form.'
##        #return pMethod
##    def _set(self, pMethod):
##        u'CombinationMethod on form.'
##    CombinationMethod = property(_get, _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Default expression.'
##    Expression = property(fset = _set, doc = _set.__doc__)
##

class RasterToolsDockWin(CoClass):
    u'The Raster Tools Dockable Window.'
    _reg_clsid_ = GUID('{5F3D3254-67F5-4664-A8A2-742F884F7704}')
    _idlflags_ = ['restricted']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
RasterToolsDockWin._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IDockableWindowDef, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IDockableWindowInitialPlacement, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IDockableWindowImageDef, IDocumentEvents, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IActiveViewEvents, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IConnectionPointContainer, IRasterDockWin]

class TableProperties(CoClass):
    u'Table window properties.'
    _reg_clsid_ = GUID('{4657D950-5FFB-11D3-9F6C-00C04F6BC886}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
class IEnumTableProperties(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to an enumeration of table properties.'
    _iid_ = GUID('{4657D953-5FFB-11D3-9F6C-00C04F6BC886}')
    _idlflags_ = ['oleautomation']
TableProperties._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ITableProperties, comtypes.gen._4A9C9ED7_F7DB_4614_B480_A5D265C961FC_0_10_2.IDefaultTableProperty, comtypes.gen._4A9C9ED7_F7DB_4614_B480_A5D265C961FC_0_10_2.ITableCharacteristics, comtypes.gen._4A9C9ED7_F7DB_4614_B480_A5D265C961FC_0_10_2.ITableCalculator, IEnumTableProperties, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, IDocumentEvents, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IActiveViewEvents]

class OverviewWindow(CoClass):
    u'Window to display Overviews.'
    _reg_clsid_ = GUID('{263F34B4-0A12-11D2-ADFB-080009EC732A}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
OverviewWindow._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IOverviewWindow, IDataWindow, IDataWindow2, IDocumentEvents, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IActiveViewEvents, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMapSurroundEvents, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream]
OverviewWindow._outgoing_interfaces_ = [IDataWindowEvents]

class TextClipboardFormat(CoClass):
    u'Text Clipboard Format.'
    _reg_clsid_ = GUID('{52BB5363-947E-11D2-ACFF-0000F87808EE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
TextClipboardFormat._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IClipboardFormat, IClipboardFormat2]

class DataGraphTCreateScatterplotMatrix(CoClass):
    u'Dialog in creating data scatterplot matrix graph.'
    _reg_clsid_ = GUID('{7AD0842E-ACAF-4647-91B5-9C97D6AEDF57}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
DataGraphTCreateScatterplotMatrix._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDataGraphTWizard, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDataGraphTEvents]

class AppDisplay(CoClass):
    u'Esri Display.'
    _reg_clsid_ = GUID('{72A6358D-E806-11D0-8681-0000F8751720}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
AppDisplay._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IAppDisplay, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IScreenDisplay, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IScreenDisplay2, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IDisplay, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IDraw]

class DataGraphWindow(CoClass):
    u'Window in hosting and displaying data graph.'
    _reg_clsid_ = GUID('{8945AC7E-D51E-11D3-A65E-0008C7DF88DB}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
DataGraphWindow._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDataGraphWindow2, IDataWindow, IDocumentEvents, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IActiveViewEvents, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDataGraphCollectionEvents, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDataGraphTEvents, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.ITimeDisplayEvents]
DataGraphWindow._outgoing_interfaces_ = [IDataWindowEvents]

class MxDocument(CoClass):
    u'Esri Mx Document.'
    _reg_clsid_ = GUID('{006B1AFE-C66C-11D0-B94C-080009EE4E51}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
MxDocument._com_interfaces_ = [comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IDocument, IMxDocument, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IDocumentDirty, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IDocumentDirty2, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySupport, IChangeLayout, IDocumentDefaultSymbols, IContentsViewEdit, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDataGraphCollection, comtypes.gen._C0FC1503_7E6F_11D2_AABF_00C04FA375F1_0_10_2.IDocumentDatasets, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDocumentInfo, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDocumentInfo2, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDocumentPreview, IReportUnitFormat, IReportUnitFormat2, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersion, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, IBasicDocument, IBasicDocument2, IBasicDocumentDefaultSymbols, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMapDocument, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IConnectionPointContainer]
MxDocument._outgoing_interfaces_ = [IDocumentEventsDisp, IDocumentEvents, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDataGraphCollectionEvents]

class GenericWindow(CoClass):
    u'User data windows.'
    _reg_clsid_ = GUID('{4B043FA1-7906-11D2-A084-0000F8775BF9}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
GenericWindow._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGenericWindow]

class MapInsetWindow(CoClass):
    u'Window to display MapInsets.'
    _reg_clsid_ = GUID('{3141F2EA-38E2-11D1-8809-080009EC732A}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
MapInsetWindow._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMapInsetWindow, ILensWindow, IDataWindow, IDataWindow2, IDocumentEvents, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IActiveViewEvents, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMapSurroundEvents, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream]
MapInsetWindow._outgoing_interfaces_ = [IDataWindowEvents]

IJoinData._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The application to which this window belongs (Optional).')], HRESULT, 'Application',
              ( ['in'], POINTER(IDispatch), 'rhs' )),
    COMMETHOD(['propputref', helpstring(u'Primary layer to join from (removes standalone table setting).')], HRESULT, 'Layer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer), 'rhs' )),
    COMMETHOD([helpstring(u'Shows modal window.')], HRESULT, 'DoModal',
              ( ['in'], comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.OLE_HANDLE, 'parentWindow' )),
    COMMETHOD(['hidden', helpstring(u'Updates all UI controls (used internally only).')], HRESULT, 'UpdateUIControls'),
]
################################################################
## code template for IJoinData implementation
##class IJoinData_Impl(object):
##    def Application(self, rhs):
##        u'The application to which this window belongs (Optional).'
##        #return 
##
##    def Layer(self, rhs):
##        u'Primary layer to join from (removes standalone table setting).'
##        #return 
##
##    def UpdateUIControls(self):
##        u'Updates all UI controls (used internally only).'
##        #return 
##
##    def DoModal(self, parentWindow):
##        u'Shows modal window.'
##        #return 
##

ITableProperties._methods_ = [
    COMMETHOD(['propget', helpstring(u'Table Property Enum.')], HRESULT, 'IEnumTableProperties',
              ( ['retval', 'out'], POINTER(POINTER(IEnumTableProperties)), 'ppEnumTableProperty' )),
    COMMETHOD([helpstring(u'Add a table property.')], HRESULT, 'Add',
              ( ['in'], POINTER(ITableProperty), 'pTableProperty' )),
    COMMETHOD([helpstring(u'Remove a table property.')], HRESULT, 'Remove',
              ( ['in'], POINTER(ITableProperty), 'pTableProperty' )),
    COMMETHOD([helpstring(u'Remove all table properties.')], HRESULT, 'RemoveAll'),
]
################################################################
## code template for ITableProperties implementation
##class ITableProperties_Impl(object):
##    def RemoveAll(self):
##        u'Remove all table properties.'
##        #return 
##
##    def Add(self, pTableProperty):
##        u'Add a table property.'
##        #return 
##
##    @property
##    def IEnumTableProperties(self):
##        u'Table Property Enum.'
##        #return ppEnumTableProperty
##
##    def Remove(self, pTableProperty):
##        u'Remove a table property.'
##        #return 
##

IEnumTableProperties._methods_ = [
    COMMETHOD([helpstring(u'Get the next table property.')], HRESULT, 'Next',
              ( ['retval', 'out'], POINTER(POINTER(ITableProperty)), 'ppTableProperty' )),
    COMMETHOD([helpstring(u'Reset.')], HRESULT, 'Reset'),
]
################################################################
## code template for IEnumTableProperties implementation
##class IEnumTableProperties_Impl(object):
##    def Reset(self):
##        u'Reset.'
##        #return 
##
##    def Next(self):
##        u'Get the next table property.'
##        #return ppTableProperty
##

class DocumentEvents(CoClass):
    u'Helper coclass for working with the nondefault outbound IDocumentEvents interface in VB.'
    _reg_clsid_ = GUID('{F138ADA0-9210-4DEA-A246-2772E27CE08A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
DocumentEvents._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown]
DocumentEvents._outgoing_interfaces_ = [IDocumentEvents]

class PublishDestinationPage(CoClass):
    u'Publishing UI - Destination Property Page.'
    _reg_clsid_ = GUID('{79E55837-CB41-47C0-8C27-804565675B64}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
PublishDestinationPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

ITableProperty._methods_ = [
    COMMETHOD(['propput', helpstring(u'Indicates if the Selected table is shown.')], HRESULT, 'SelectedTable',
              ( ['in'], VARIANT_BOOL, 'pShowSelectedTable' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the Selected table is shown.')], HRESULT, 'SelectedTable',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pShowSelectedTable' )),
    COMMETHOD(['propputref', helpstring(u'Table of table window (Overrides feature class setting).')], HRESULT, 'Table',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable), 'ppTable' )),
    COMMETHOD(['propget', helpstring(u'Table of table window (Overrides feature class setting).')], HRESULT, 'Table',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable)), 'ppTable' )),
    COMMETHOD(['propputref', helpstring(u'Feature class of table window (Overrides table setting).')], HRESULT, 'FeatureLayer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IFeatureLayer), 'ppFeatureLayer' )),
    COMMETHOD(['propget', helpstring(u'Feature class of table window (Overrides table setting).')], HRESULT, 'FeatureLayer',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IFeatureLayer)), 'ppFeatureLayer' )),
]
################################################################
## code template for ITableProperty implementation
##class ITableProperty_Impl(object):
##    @property
##    def Table(self, ppTable):
##        u'Table of table window (Overrides feature class setting).'
##        #return 
##
##    def _get(self):
##        u'Indicates if the Selected table is shown.'
##        #return pShowSelectedTable
##    def _set(self, pShowSelectedTable):
##        u'Indicates if the Selected table is shown.'
##    SelectedTable = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def FeatureLayer(self, ppFeatureLayer):
##        u'Feature class of table window (Overrides table setting).'
##        #return 
##

class MapViewerWindowFactory(CoClass):
    u'Factory to generate a Viewer Window.'
    _reg_clsid_ = GUID('{B03C71E7-58F1-46F0-BF4D-F40FEB792D64}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
MapViewerWindowFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDataWindowFactory]

class MapInsetWindowFactory(CoClass):
    u'Factory to generate a MapInset window.'
    _reg_clsid_ = GUID('{2BF3A4DF-AFB7-11D1-8750-0000F8751720}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
MapInsetWindowFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDataWindowFactory]

class MensurationDockWin(CoClass):
    u'The Mensuration Result Dockable Window.'
    _reg_clsid_ = GUID('{910103AF-8D36-4B11-829D-D1A00F5C6A2D}')
    _idlflags_ = ['restricted']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{40499F24-596F-45D2-ACE1-A251E2990017}', 10, 2)
MensurationDockWin._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IDockableWindowDef, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IDockableWindowInitialPlacement, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IDockableWindowImageDef, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IConnectionPointContainer, IMensurationResult]

__all__ = ['TableContextMenuArrangeItems', 'IMxApplication',
           'IDocumentDefaultSymbols', 'OverviewWindowFactory',
           'GenericWindow', 'ILayerEffectsEnvironment2',
           'IDataGraphWindow2', 'esriMxFillColor', 'AddDataDialog',
           'RasterCatalogGxBrowserFactory', 'IDissolveUIAdmin',
           'IBasicDocument', 'IFindWindow', 'IJoinData',
           'esriDCFeatureClass', 'TOCDockableWindow', 'ITableWindow',
           'ElementNewOperation', 'MetadataViewWindow', 'IDissolveUI',
           'IStartupDialog2', 'IDataConnectionPropertyPage',
           'AppDisplay', 'esriMxDlgCustomize',
           'esriTerrainPointAttributeHisto',
           'esriCEShowDataFrameProperties', 'IChangeLayout',
           'MetaFileClipboardFormat', 'AnnotateSelectedFeatures',
           'PageIndexGeneralPropPage', 'NewDocumentDialog',
           'IDataConnectionCallback', 'esriLasPointElevationHisto',
           'ITableWindow2', 'IMSPropsPropertyPage',
           'ColorCorrectionDockWin', 'esriTinElevationHisto',
           'esriCEShowLayersProperties', 'RemoveLayersOperation',
           'LasDatasetGxBrowserFactory',
           'ImageServerLayerContextAnalyzer', 'IDataWindow2',
           'GettingStartedSettings', 'MapPropertyPage',
           'IMSLayersPropertyPage', 'IJoinData2',
           'MapServerLayerAdvancedPropertyPage',
           'IStartupDialogSettings', 'IFindPanelEvents',
           'SelectByCommonValueTool', 'esriMxDlgIDs',
           'ISelectFeaturesOperation', 'ILayerEffectsEnvironment',
           'FindWindowUI', 'TimeSliderWindowCommand',
           'TOCDisplayView', 'ILensWindow', 'IContentsViewEdit',
           'IDocumentEventsDisp', 'IRemoveLayerOperation2',
           'AVImageThemeImporter', 'ITableProperty3',
           'LasDatasetIdentifyObject', 'IMoveLayersOperation',
           'GpsLogFilter', 'MxStatusBar', 'ILayerEffectsEnvironment3',
           'DataGraphMxDocumentDropTarget', 'esriDCRasterCatalog',
           'IFindWindow2', 'OverviewPropertyPage', 'IMSLayerFactory',
           'IMetadataViewWindow2', 'IAddDataDialog2',
           'TinGxBrowserFactory', 'ReferenceScaleOperation',
           'IMxDocument', 'ElementSelection',
           'PublishAntiAliasingPage', 'MoveLayersOperation',
           'IMxApplication3', 'ImageInsetWindow',
           'PublishOptionsPage', 'IModelessQueryAttributes',
           'IGpsExtension', 'TinHistogram', 'esriMxDlgVBA',
           'WMSMapLayerFactory', 'NetCDFTablePropertyPage',
           'IGpsPositionDialog', 'IEnumTableProperties',
           'IDocumentEvents', 'TableProperties', 'esriMxDlgOptions',
           'MxDocument', 'esriMxDlgPageSetup', 'IStartupDialog3',
           'DataViewPropertyPage', 'IApplicationWindows',
           'RotateOperation', 'RasterLayerContextAnalyzer',
           'GroupLayerContextAnalyzer', 'IAnnotateFeaturesCallback',
           'IRasterDockWin', 'ProgressAnimation',
           'esriMxDefaultColorTypes', 'esriMxDlgMacros',
           'RasterToolsDockWin', 'IDataConnectionCallback2',
           'MapServerLayerSourcePropertyPage', 'IDataWindowFactory',
           'IReportUnitFormat2', 'ITinHistogram', 'IRelateData',
           'DataGraphTCreateScatterplotMatrix',
           'esriMxDlgLockCustomization', 'esriCEShowAddDataDialog',
           'GroupLayersOperation', 'RelateData', 'FindFeatures',
           'ITableProperty', 'ProgressDialog', 'IGenericWindow',
           'TableContextMenuArrange', 'IRelateData2',
           'ReportSelection', 'IBasicDocumentDefaultSymbols',
           'ProgressBar', 'JoinData', 'TOCSelectionView',
           'RasterTableShowMultiItem', 'MapIlluminationPropertyPage',
           'LayerSelectionContextMenu', 'IMapInsetWindow',
           'TextClipboardFormat', 'MapDocumentPropPage',
           'esriTinHistogramType', 'esriDCDataFile',
           'IMetadataViewWindow3', 'WMSLayerAdvancedPropertyPage',
           'esriMxTextColor', 'MapInsetWindow', 'TOCCatalogView',
           'IViewCommandToolbars', 'GettingStartedWindow',
           'LayoutViewPropertyPage', 'EnhMetaFileClipboardFormat',
           'IFindCallBack', 'IContentsView',
           'WMSLayerStylePropertyPage', 'GNetCommandHandler', 'Maps',
           'MapServerLayerCachePropertyPage',
           'ExcludeUnselectedFeaturesCommand', 'IEnumPrinterNames',
           'TOCPatchesPropertyPage', 'IMxApplication2',
           'MapGridsPropertyPage', 'ITableProperty2',
           'IRemoveLayersOperation', 'MoveMapsOperation',
           'esriMxLineColor', 'JoinRelatePage',
           'IReferenceScaleOperation', 'esriMxDlgZoom',
           'IViewCommand', 'TOCLegendDisplayView', 'IDatasetFilter',
           'ITableFrame', 'BasemapSubLayerRasterLayerContextAnalyzer',
           'IPixelInspectionWindow', 'TOCLegendSelectionView',
           'esriDCType', 'TableDockWindow',
           'RasterBasemapLayerContextAnalyzer',
           'MapViewCommandsContextMenu', 'IContentsView2',
           'IPageIndexControl', 'IRemoveLayerOperation',
           'IDataWindowEvents', 'SelectFeaturesOperation',
           'MensurationDockWin', 'esriTinAspectHisto',
           'DataConnectionPropertyPage', 'LayerEffectsEnvironment',
           'ITableDockWindowAdmin', 'WMSSublayersPropertyPage',
           'PageIndexExtentPropPage', 'IHistoryViewerWindow',
           'TableWindow', 'IUngroupLayerOperation',
           'esriMxDlgContents', 'IDataWindow', 'ITableWindow3',
           'IAddDataDialog', 'IGNetExtension', 'AddLayersOperation',
           'HistoryViewerWindow', 'MapViewCommandsMenuItems',
           'MapViewerWindowFactory', 'TOCGeneralPropertyPage',
           'IContentsView3', 'LayersClipboardFormat',
           'QueryAttributes', 'IMensurationResult',
           'RemoveLayerOperation', 'MapServerSublayersPropertyPage',
           'IJoinPages', 'GNetExtension', 'ISpatialJoin',
           'IContentsViewSelection', 'PixelInspectionDockWin',
           'MapInsetWindowFactory', 'DataGraphTWizard',
           'ColorCorrectionWindowCommand', 'esriMxDlgProperties',
           'IReportUnitFormat', 'OpenTableCommand',
           'IMoveMapsOperation', 'MosaicDatasetExtension',
           'IGroupLayersOperation', 'WMSIdentifyObject',
           'TemplateStartupDialog', 'esriMxDlgUnlockCustomization',
           'esriDCTable', 'IdentifyWindowCommand',
           'IDataConnectionPropertyPage2',
           'IMSSubLayerContextAnalyzer', 'DocumentEvents',
           'IMSFeatureLayerSymbology', 'DocumentPropertyPage',
           'SpatialJoin', 'IAnnotateSelectedFeatures',
           'OverviewWindow', 'INewDocumentDialog', 'OleFrame',
           'ITableProperties', 'IClipboardFormat2',
           'RestoreExcludedFeaturesCommand', 'NetworkLayerFactory',
           'IFinder', 'IBasicDocument2', 'IAggregateOptions',
           'esriMxDlgStyleGallery', 'esriMxDlgPrintSetup',
           'GpsExtension', 'ImageAnalysisWindowCommand',
           'MapServerIdentifyObject', 'BmpClipboardFormat',
           'NetCDFRasterPropertyPage', 'IAddLayersOperation',
           'PublishDestinationPage', 'ISummarizeUI',
           'TerrainGxBrowserFactory', 'IAIAProperties',
           'IDataGraphTWizard', 'IMSMapLayerSourcePropertyPage',
           'TableProperty', 'esriMxCustomizationEvent',
           'AddQueryTableDialog', 'NetCDFFeaturePropertyPage',
           'RasterToolExtension', 'IClipboardFormat',
           'IdentifyWindow', 'IOverviewWindow', 'esriMxMarkerColor',
           'IStartupDialog', 'IMetadataViewWindow',
           'GpsPositionDialog', 'MapInsetPropertyPage', 'SummarizeUI',
           'IMxDocumentDropTarget', 'esriMxDlgOverflowLabels',
           'IQueryAttributes', 'esriTinSlopeHisto',
           'ElementEditVerticesOperation',
           'WMSLayerSourcePropertyPage', 'RasterGxBrowserFactory',
           'DataGraphWindow', 'UngroupLayerOperation',
           'MapViewCommandsContextAnalyzer',
           'esriTinNodeElevationHisto',
           'esriTerrainPointElevationHisto', 'DataConnectionCallback']
from comtypes import _check_version; _check_version('501')

# -*- coding: mbcs -*-
typelib_path = u'C:\\Program Files (x86)\\ArcGIS\\Desktop10.2\\com\\esriGeoDatabaseUI.olb'
_lcid = 0 # change this if required
from ctypes import *
import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0
import comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2
import comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2
from comtypes import GUID
from comtypes import CoClass
import comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2
from ctypes import HRESULT
from comtypes import helpstring
from comtypes import COMMETHOD
from comtypes import dispid
import comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2
from ctypes.wintypes import VARIANT_BOOL
from comtypes import BSTR
import comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2


class QueryPropertyPage(CoClass):
    u'Property page for setting up the query.'
    _reg_clsid_ = GUID('{7FF5459F-6F59-11D2-A07E-0000F8775BF9}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{4A9C9ED7-F7DB-4614-B480-A5D265C961FC}', 10, 2)
class IQueryPropertyPage(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Query property page.'
    _iid_ = GUID('{C315FC73-705A-11D2-A07E-0000F8775BF9}')
    _idlflags_ = ['oleautomation']
class IQueryPropertyPage2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Query property page.'
    _iid_ = GUID('{813C9EEC-5D9D-40C8-918C-6725A73EEF10}')
    _idlflags_ = ['oleautomation']
class IQueryPropertyPageFieldInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Query property page field info.'
    _iid_ = GUID('{9D3D2768-7760-43F3-B200-69BB4D852180}')
    _idlflags_ = ['oleautomation']
QueryPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IQueryPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, IQueryPropertyPage2, IQueryPropertyPageFieldInfo, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext]

class ITableViewTableFields(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that associate additional field properties with the table being displayed.'
    _iid_ = GUID('{EDD9326B-E6DF-11D3-ADEC-00C04FA33A15}')
    _idlflags_ = ['oleautomation']
ITableViewTableFields._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The collection of field information for the table being viewed/edited.')], HRESULT, 'TableFields',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITableFields), 'TableFields' )),
    COMMETHOD(['propget', helpstring(u'The collection of field information for the table being viewed/edited.')], HRESULT, 'TableFields',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITableFields)), 'TableFields' )),
]
################################################################
## code template for ITableViewTableFields implementation
##class ITableViewTableFields_Impl(object):
##    @property
##    def TableFields(self, TableFields):
##        u'The collection of field information for the table being viewed/edited.'
##        #return 
##

class VersionManager(CoClass):
    u'A dialog for managing versions in a versioned geodatabase.'
    _reg_clsid_ = GUID('{FB895240-121E-11D3-80BA-0080C7625171}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{4A9C9ED7-F7DB-4614-B480-A5D265C961FC}', 10, 2)
class IVersionManager(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the version management dialog for a versioned geodatabase.'
    _iid_ = GUID('{FB895241-121E-11D3-80BA-0080C7625171}')
    _idlflags_ = ['oleautomation']
class IVersionManagerEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to events fired by the Version Manager dialog.'
    _iid_ = GUID('{2F6252B5-9401-492E-81F8-47B795A3F5CF}')
    _idlflags_ = ['oleautomation']
VersionManager._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IVersionManager, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IConnectionPointContainer]
VersionManager._outgoing_interfaces_ = [IVersionManagerEvents]

class ITableControl3(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the table once it has been shown.'
    _iid_ = GUID('{1E5471D9-7F04-4479-97AB-576A12A7CB9C}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriTVRowInsertPlacement'
esriTVRowInsBeginningOfWin = 0
esriTVRowInsBeforeGivenOID = 1
esriTVRowInsAfterGivenOID = 2
esriTVRowInsAfterGivenOIDAutoAdv = 3
esriTVRowInsEndOfWin = 4
esriTVRowInsertPlacement = c_int # enum

# values for enumeration 'esriTableViewOptions'
esriTVOptionNoOptionSelected = -1
esriTVOptionShowSQLWindow = 0
esriTVOptionShowFindReplaceWindow = 1
esriTVOptionSelectAll = 2
esriTVOptionUnselectAll = 3
esriTVOptionSwitchSelection = 4
esriTVOptionShowAppearanceWindow = 5
esriTVOptionShowAddFieldWindow = 6
esriTVOptionShowMakeGraphWindow = 7
esriTVOptionAddTableToLayout = 8
esriTVOptionShowExportTableWindow = 9
esriTVOptionReloadCache = 10
esriTVOptionPrintTable = 11
esriTVOptionCreateReport = 12
esriTVOptionCreateCrystalReport = 13
esriTVOptionTableProperties = 14
esriTVOptionAutoResizeColumns = 15
esriTVOptionUnHideAllColumns = 16
esriTVOptionAliasNameToggle = 17
esriTVOptionResetFieldOrder = 18
esriTableViewOptions = c_int # enum
ITableControl3._methods_ = [
    COMMETHOD([helpstring(u'Call after start or stop editing, to update table grid.')], HRESULT, 'EditChanged'),
    COMMETHOD([helpstring(u'Lose cache, so the table window is current with the underlying database.')], HRESULT, 'RemoveAndReloadCache'),
    COMMETHOD([helpstring(u'Updates the current selection, that the current selection is currently pointing to.')], HRESULT, 'UpdateSelection',
              ( [], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ISelectionSet), 'pSelection' )),
    COMMETHOD([helpstring(u'Draws selected features on display.')], HRESULT, 'DrawSelectedShapes',
              ( ['in'], POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IDisplay), 'pDisplay' )),
    COMMETHOD([helpstring(u'Rereads rows. Called when viewing selected records and the selection changes.')], HRESULT, 'RereadFIDs',
              ( [], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ISelectionSet), 'pSelection' )),
    COMMETHOD([helpstring(u'The current row the user is on. If isOid = TRUE, then rowNumber is an OID, else it is an offset.')], HRESULT, 'SetCurrentRow',
              ( ['in'], VARIANT_BOOL, 'isOid' ),
              ( ['in'], c_int, 'rowNumber' )),
    COMMETHOD([helpstring(u'The current row the user is on. If isOid = TRUE, then rowNumber is an OID, else it is an offset.')], HRESULT, 'GetCurrentRow',
              ( ['in'], VARIANT_BOOL, 'isOid' ),
              ( ['retval', 'out'], POINTER(c_int), 'pRowNumber' )),
    COMMETHOD([helpstring(u'Redraws the grid.')], HRESULT, 'Redraw'),
    COMMETHOD([helpstring(u'Read all the OIDs/Rows in the table.')], HRESULT, 'ReadToEndOfTable'),
    COMMETHOD([helpstring(u'Overrides the font setting for table cells. At least the oid or fieldName must be specified. Enter null fonts to erase.')], HRESULT, 'SetCellFont',
              ( ['in'], c_int, 'oid' ),
              ( ['in'], BSTR, 'fieldName' ),
              ( ['in'], POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IColor), 'pCellColor' ),
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IFont), 'pTextFont' ),
              ( ['in'], POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IColor), 'pTextColor' )),
    COMMETHOD([helpstring(u'Determines where the next insert record is inserted when OnCreate is fired. Adding records manually via the table window allways adds records to the end of the table.')], HRESULT, 'InsertNextRowAt',
              ( ['in'], esriTVRowInsertPlacement, 'placement' ),
              ( ['in'], c_int, 'oid' )),
    COMMETHOD([helpstring(u'Executes a command in the option menu.')], HRESULT, 'ExecuteOptionCommand',
              ( ['in'], esriTableViewOptions, 'option' )),
    COMMETHOD(['propput', helpstring(u'Hides the options button. Default is False.')], HRESULT, 'HideOptionsButton',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Ensures that the Select button is always active of the view toggle buttons. Default is False.')], HRESULT, 'SelectToggleAlwaysEnabled',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Hides the view toggle buttons. Default is False.')], HRESULT, 'HideViewToggleButtons',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
]
################################################################
## code template for ITableControl3 implementation
##class ITableControl3_Impl(object):
##    def GetCurrentRow(self, isOid):
##        u'The current row the user is on. If isOid = TRUE, then rowNumber is an OID, else it is an offset.'
##        #return pRowNumber
##
##    def RereadFIDs(self, pSelection):
##        u'Rereads rows. Called when viewing selected records and the selection changes.'
##        #return 
##
##    def _set(self, rhs):
##        u'Hides the options button. Default is False.'
##    HideOptionsButton = property(fset = _set, doc = _set.__doc__)
##
##    def SetCurrentRow(self, isOid, rowNumber):
##        u'The current row the user is on. If isOid = TRUE, then rowNumber is an OID, else it is an offset.'
##        #return 
##
##    def DrawSelectedShapes(self, pDisplay):
##        u'Draws selected features on display.'
##        #return 
##
##    def ReadToEndOfTable(self):
##        u'Read all the OIDs/Rows in the table.'
##        #return 
##
##    def EditChanged(self):
##        u'Call after start or stop editing, to update table grid.'
##        #return 
##
##    def InsertNextRowAt(self, placement, oid):
##        u'Determines where the next insert record is inserted when OnCreate is fired. Adding records manually via the table window allways adds records to the end of the table.'
##        #return 
##
##    def ExecuteOptionCommand(self, option):
##        u'Executes a command in the option menu.'
##        #return 
##
##    def RemoveAndReloadCache(self):
##        u'Lose cache, so the table window is current with the underlying database.'
##        #return 
##
##    def _set(self, rhs):
##        u'Hides the view toggle buttons. Default is False.'
##    HideViewToggleButtons = property(fset = _set, doc = _set.__doc__)
##
##    def SetCellFont(self, oid, fieldName, pCellColor, pTextFont, pTextColor):
##        u'Overrides the font setting for table cells. At least the oid or fieldName must be specified. Enter null fonts to erase.'
##        #return 
##
##    def Redraw(self):
##        u'Redraws the grid.'
##        #return 
##
##    def UpdateSelection(self, pSelection):
##        u'Updates the current selection, that the current selection is currently pointing to.'
##        #return 
##
##    def _set(self, rhs):
##        u'Ensures that the Select button is always active of the view toggle buttons. Default is False.'
##    SelectToggleAlwaysEnabled = property(fset = _set, doc = _set.__doc__)
##

class ITableControlInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that inform you about the table window.'
    _iid_ = GUID('{071B47F3-293E-4868-BAC9-986B55F4C0D8}')
    _idlflags_ = ['oleautomation']
ITableControlInfo._methods_ = [
    COMMETHOD([helpstring(u'The current row the user is on. If isOid = TRUE, then rowNumber is an OID, else it is an offset.')], HRESULT, 'GetCurrentRow',
              ( ['in'], VARIANT_BOOL, 'isOid' ),
              ( ['retval', 'out'], POINTER(c_int), 'pRowNumber' )),
    COMMETHOD([helpstring(u'Gets the top visible row of the view window.')], HRESULT, 'GetTopRow',
              ( ['retval', 'out'], POINTER(c_int), 'topRow' )),
    COMMETHOD([helpstring(u'Gets the left visible column of the view window.')], HRESULT, 'GetLeftCol',
              ( ['retval', 'out'], POINTER(c_int), 'leftCol' )),
    COMMETHOD(['propget', helpstring(u'Number of records read.')], HRESULT, 'RecordCount',
              ( ['retval', 'out'], POINTER(c_int), 'pRecCount' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether all records have been read by the table window.')], HRESULT, 'AreAllRecordsRead',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'allRecordsRead' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the table window is in an editing session.')], HRESULT, 'IsEditing',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsEditing' )),
    COMMETHOD([helpstring(u'The current col (FDO field index) the user is on.')], HRESULT, 'GetCurrentCol',
              ( ['retval', 'out'], POINTER(c_int), 'pFDOFieldIndex' )),
]
################################################################
## code template for ITableControlInfo implementation
##class ITableControlInfo_Impl(object):
##    def GetCurrentRow(self, isOid):
##        u'The current row the user is on. If isOid = TRUE, then rowNumber is an OID, else it is an offset.'
##        #return pRowNumber
##
##    @property
##    def RecordCount(self):
##        u'Number of records read.'
##        #return pRecCount
##
##    def GetLeftCol(self):
##        u'Gets the left visible column of the view window.'
##        #return leftCol
##
##    @property
##    def AreAllRecordsRead(self):
##        u'Indicates whether all records have been read by the table window.'
##        #return allRecordsRead
##
##    @property
##    def IsEditing(self):
##        u'Indicates whether the table window is in an editing session.'
##        #return IsEditing
##
##    def GetCurrentCol(self):
##        u'The current col (FDO field index) the user is on.'
##        #return pFDOFieldIndex
##
##    def GetTopRow(self):
##        u'Gets the top visible row of the view window.'
##        #return topRow
##

class IGPCalculatorUI(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the field calculator.'
    _iid_ = GUID('{2F6E5F8B-B8B1-44BB-B55B-DBAA0321B9C2}')
    _idlflags_ = ['oleautomation', 'hidden']
IGPCalculatorUI._methods_ = [
    COMMETHOD(['propputref', helpstring(u'DETable to perform calculation on.')], HRESULT, 'DETable',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDETable), 'rhs' )),
]
################################################################
## code template for IGPCalculatorUI implementation
##class IGPCalculatorUI_Impl(object):
##    def DETable(self, rhs):
##        u'DETable to perform calculation on.'
##        #return 
##

class CalculatorUI(CoClass):
    u'Window to display calculator dialog.'
    _reg_clsid_ = GUID('{309194D7-CCEB-11D2-9F24-00C04F6BC886}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{4A9C9ED7-F7DB-4614-B480-A5D265C961FC}', 10, 2)
class ICalculatorUI(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the field calculator.'
    _iid_ = GUID('{309194D6-CCEB-11D2-9F24-00C04F6BC886}')
    _idlflags_ = ['oleautomation']
class ICalculatorUI2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the field calculator.'
    _iid_ = GUID('{504996E3-9ABE-4A42-847D-39D641B7FD41}')
    _idlflags_ = ['oleautomation']
class ICalculatorUIJoinSettings(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the field calculator join settings.'
    _iid_ = GUID('{8F3E794A-EF0B-43CA-9DE4-34DEC440AAA5}')
    _idlflags_ = ['oleautomation']
CalculatorUI._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ICalculatorUI, ICalculatorUI2, ICalculatorUIJoinSettings]

class ITableCalculator(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the characteristics the calculator form the table.'
    _iid_ = GUID('{1C1B8CE1-D23B-4EDE-9A0E-2F65AF61F1D1}')
    _idlflags_ = ['oleautomation']
ITableCalculator._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if row changed events should be fires for join tables.')], HRESULT, 'FireRowChangedEventsForJoins',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pFireRowEvents' )),
    COMMETHOD(['propput', helpstring(u'Indicates if row changed events should be fires for join tables.')], HRESULT, 'FireRowChangedEventsForJoins',
              ( ['in'], VARIANT_BOOL, 'pFireRowEvents' )),
]
################################################################
## code template for ITableCalculator implementation
##class ITableCalculator_Impl(object):
##    def _get(self):
##        u'Indicates if row changed events should be fires for join tables.'
##        #return pFireRowEvents
##    def _set(self, pFireRowEvents):
##        u'Indicates if row changed events should be fires for join tables.'
##    FireRowChangedEventsForJoins = property(_get, _set, doc = _set.__doc__)
##

class HistoricalMarkerManager(CoClass):
    u'A dialog for managing historical markers.'
    _reg_clsid_ = GUID('{281507BA-493D-4DEF-94A7-B0B5550D06FD}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{4A9C9ED7-F7DB-4614-B480-A5D265C961FC}', 10, 2)
class IHistoricalMarkerManager(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the historical marker management dialog.'
    _iid_ = GUID('{F5E4DF8B-6CE9-449A-B1CF-B94ACFA41646}')
    _idlflags_ = ['oleautomation']
HistoricalMarkerManager._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IHistoricalMarkerManager]

class VersioningGeneralPropertyPage(CoClass):
    u'A dialog for setting the properties of a versions in a versioned geodatabase.'
    _reg_clsid_ = GUID('{0224F7BD-F736-11D2-9F2E-00C04F6BC979}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{4A9C9ED7-F7DB-4614-B480-A5D265C961FC}', 10, 2)
VersioningGeneralPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class ITableControl2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the table once it has been shown.'
    _iid_ = GUID('{6831ECBD-4264-4BEF-82E6-A6311A0B4FA0}')
    _idlflags_ = ['oleautomation']
ITableControl2._methods_ = [
    COMMETHOD([helpstring(u'Call after start or stop editing, to update table grid.')], HRESULT, 'EditChanged'),
    COMMETHOD([helpstring(u'Lose cache, so the table window is current with the underlying database.')], HRESULT, 'RemoveAndReloadCache'),
    COMMETHOD([helpstring(u'Updates the current selection, that the current selection is currently pointing to.')], HRESULT, 'UpdateSelection',
              ( [], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ISelectionSet), 'pSelection' )),
    COMMETHOD([helpstring(u'Draws selected features on display.')], HRESULT, 'DrawSelectedShapes',
              ( ['in'], POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IDisplay), 'pDisplay' )),
    COMMETHOD([helpstring(u'Rereads rows. Called when viewing selected records and the selection changes.')], HRESULT, 'RereadFIDs',
              ( [], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ISelectionSet), 'pSelection' )),
    COMMETHOD([helpstring(u'The current row the user is on. If isOid = TRUE, then rowNumber is an OID, else it is an offset.')], HRESULT, 'SetCurrentRow',
              ( ['in'], VARIANT_BOOL, 'isOid' ),
              ( ['in'], c_int, 'rowNumber' )),
    COMMETHOD([helpstring(u'The current row the user is on. If isOid = TRUE, then rowNumber is an OID, else it is an offset.')], HRESULT, 'GetCurrentRow',
              ( ['in'], VARIANT_BOOL, 'isOid' ),
              ( ['retval', 'out'], POINTER(c_int), 'pRowNumber' )),
    COMMETHOD([helpstring(u'Redraws the grid.')], HRESULT, 'Redraw'),
    COMMETHOD([helpstring(u'Read all the OIDs/Rows in the table.')], HRESULT, 'ReadToEndOfTable'),
]
################################################################
## code template for ITableControl2 implementation
##class ITableControl2_Impl(object):
##    def GetCurrentRow(self, isOid):
##        u'The current row the user is on. If isOid = TRUE, then rowNumber is an OID, else it is an offset.'
##        #return pRowNumber
##
##    def RereadFIDs(self, pSelection):
##        u'Rereads rows. Called when viewing selected records and the selection changes.'
##        #return 
##
##    def SetCurrentRow(self, isOid, rowNumber):
##        u'The current row the user is on. If isOid = TRUE, then rowNumber is an OID, else it is an offset.'
##        #return 
##
##    def DrawSelectedShapes(self, pDisplay):
##        u'Draws selected features on display.'
##        #return 
##
##    def ReadToEndOfTable(self):
##        u'Read all the OIDs/Rows in the table.'
##        #return 
##
##    def EditChanged(self):
##        u'Call after start or stop editing, to update table grid.'
##        #return 
##
##    def RemoveAndReloadCache(self):
##        u'Lose cache, so the table window is current with the underlying database.'
##        #return 
##
##    def Redraw(self):
##        u'Redraws the grid.'
##        #return 
##
##    def UpdateSelection(self, pSelection):
##        u'Updates the current selection, that the current selection is currently pointing to.'
##        #return 
##

class Calculator(CoClass):
    u'Calculator engine which is used by the UI and can be used independently.'
    _reg_clsid_ = GUID('{D676066E-38CA-429A-B846-DA7A8446C52D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{4A9C9ED7-F7DB-4614-B480-A5D265C961FC}', 10, 2)
class ICalculator(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that calculate field values in a table.'
    _iid_ = GUID('{28232C3A-D7D8-450C-A1DA-9C1EF5A5A175}')
    _idlflags_ = ['oleautomation']
Calculator._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ICalculator]

class ITableSelectionColor(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to events that occur for which a client can store and load info about the selection color.'
    _iid_ = GUID('{B1D2FCEC-F7B9-4B77-B8FD-3425772F6AD8}')
    _idlflags_ = ['oleautomation']
ITableSelectionColor._methods_ = [
    COMMETHOD(['propget', helpstring(u'Selection color use to highlight rows in the the selected tables and graphics.')], HRESULT, 'SelectedTableSelectionColor',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IColor)), 'ppSelectionColor' )),
    COMMETHOD(['propputref', helpstring(u'Selection color use to highlight rows in the the selected tables and graphics.')], HRESULT, 'SelectedTableSelectionColor',
              ( ['in'], POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IColor), 'ppSelectionColor' )),
    COMMETHOD(['propget', helpstring(u'Selection color use to highlight rows and graphics.')], HRESULT, 'SelectionColor',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IColor)), 'ppSelectionColor' )),
    COMMETHOD(['propputref', helpstring(u'Selection color use to highlight rows and graphics.')], HRESULT, 'SelectionColor',
              ( ['in'], POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IColor), 'ppSelectionColor' )),
]
################################################################
## code template for ITableSelectionColor implementation
##class ITableSelectionColor_Impl(object):
##    def SelectedTableSelectionColor(self, ppSelectionColor):
##        u'Selection color use to highlight rows in the the selected tables and graphics.'
##        #return 
##
##    def SelectionColor(self, ppSelectionColor):
##        u'Selection color use to highlight rows and graphics.'
##        #return 
##


# values for enumeration 'esriTableSelectionActions'
esriNoAction = 0
esriSelectCurrentRow = 1
esriSelectFeatures = 2
esriDrawFeatures = 3
esriTableSelectionActions = c_int # enum
class ITableViewInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to events that occur for which a client can store and load info about the look of the table.'
    _iid_ = GUID('{0F25F47C-657A-11D3-9F6C-00C04F6BC886}')
    _idlflags_ = ['oleautomation']
ITableViewInfo._methods_ = [
    COMMETHOD([helpstring(u'Table window position.')], HRESULT, 'PutPosition',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' )),
    COMMETHOD([helpstring(u'Query table window position.')], HRESULT, 'QueryPosition',
              ( ['out'], POINTER(c_int), 'pX1' ),
              ( ['out'], POINTER(c_int), 'pY1' ),
              ( ['out'], POINTER(c_int), 'pX2' ),
              ( ['out'], POINTER(c_int), 'pY2' )),
    COMMETHOD(['propget', helpstring(u'Selection color used to highlight rows and graphics.')], HRESULT, 'SelectionColor',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IColor)), 'ppSelectionColor' )),
    COMMETHOD(['propputref', helpstring(u'Selection color used to highlight rows and graphics.')], HRESULT, 'SelectionColor',
              ( ['in'], POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IColor), 'ppSelectionColor' )),
    COMMETHOD(['propput', helpstring(u'Order of fields.')], HRESULT, 'FieldOrder',
              ( ['in'], BSTR, 'pFieldList' )),
    COMMETHOD(['propget', helpstring(u'Order of fields.')], HRESULT, 'FieldOrder',
              ( ['retval', 'out'], POINTER(BSTR), 'pFieldList' )),
    COMMETHOD(['propput', helpstring(u'Field Width.')], HRESULT, 'FieldWidth',
              ( ['in'], BSTR, 'fieldName' ),
              ( ['in'], c_int, 'pFieldWidth' )),
    COMMETHOD(['propget', helpstring(u'Field Width.')], HRESULT, 'FieldWidth',
              ( ['in'], BSTR, 'fieldName' ),
              ( ['retval', 'out'], POINTER(c_int), 'pFieldWidth' )),
    COMMETHOD(['propput', helpstring(u'Number of frozen fields.')], HRESULT, 'FrozenFields',
              ( ['in'], c_int, 'pNumberOfFields' )),
    COMMETHOD(['propget', helpstring(u'Number of frozen fields.')], HRESULT, 'FrozenFields',
              ( ['retval', 'out'], POINTER(c_int), 'pNumberOfFields' )),
]
################################################################
## code template for ITableViewInfo implementation
##class ITableViewInfo_Impl(object):
##    def _get(self, fieldName):
##        u'Field Width.'
##        #return pFieldWidth
##    def _set(self, fieldName, pFieldWidth):
##        u'Field Width.'
##    FieldWidth = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Order of fields.'
##        #return pFieldList
##    def _set(self, pFieldList):
##        u'Order of fields.'
##    FieldOrder = property(_get, _set, doc = _set.__doc__)
##
##    def PutPosition(self, x1, y1, x2, y2):
##        u'Table window position.'
##        #return 
##
##    def QueryPosition(self):
##        u'Query table window position.'
##        #return pX1, pY1, pX2, pY2
##
##    def _get(self):
##        u'Number of frozen fields.'
##        #return pNumberOfFields
##    def _set(self, pNumberOfFields):
##        u'Number of frozen fields.'
##    FrozenFields = property(_get, _set, doc = _set.__doc__)
##
##    def SelectionColor(self, ppSelectionColor):
##        u'Selection color used to highlight rows and graphics.'
##        #return 
##

class CalculatorCallback(CoClass):
    u'If the calculation engine has a class of CalculatorCallback, then it can interact with the client on the current progress.'
    _reg_clsid_ = GUID('{0A8C43B8-79EC-40E2-915A-D01050AFF244}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{4A9C9ED7-F7DB-4614-B480-A5D265C961FC}', 10, 2)
class ICalculatorCallback(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to events that occur when the state of the calculator changes.'
    _iid_ = GUID('{4FFEA595-65D7-431A-A102-F8377402DC88}')
    _idlflags_ = ['oleautomation']
CalculatorCallback._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ICalculatorCallback]

class GDBConnectionsPropertyPage(CoClass):
    u'A property page for controlling connections to an enterprise Geodatabase'
    _reg_clsid_ = GUID('{F9B62235-AE10-42FC-B48F-F401A5636899}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{4A9C9ED7-F7DB-4614-B480-A5D265C961FC}', 10, 2)
GDBConnectionsPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class ITableView4(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that interact with table.'
    _iid_ = GUID('{DFBD1276-D664-4FFE-A7F5-8B0B8130A683}')
    _idlflags_ = ['oleautomation']
ITableView4._methods_ = [
    COMMETHOD(['propput', helpstring(u'Allow delete row during editing. Default: True.')], HRESULT, 'AllowDeleteRow',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD(['propget', helpstring(u'Editing allowed on the table.')], HRESULT, 'AllowEditing',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pAllowEditing' )),
]
################################################################
## code template for ITableView4 implementation
##class ITableView4_Impl(object):
##    def _set(self, rhs):
##        u'Allow delete row during editing. Default: True.'
##    AllowDeleteRow = property(fset = _set, doc = _set.__doc__)
##
##    @property
##    def AllowEditing(self):
##        u'Editing allowed on the table.'
##        #return pAllowEditing
##

class ITableView2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that interact with table.'
    _iid_ = GUID('{B68CFFCB-A325-4BD0-BA35-33A51012B025}')
    _idlflags_ = ['oleautomation']
class ITableViewCallback(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to events that occur for which a client of the table can act upon and provide information.'
    _iid_ = GUID('{22488807-BC7B-11D2-9F23-00C04F6BC886}')
    _idlflags_ = ['oleautomation']
ITableView2._methods_ = [
    COMMETHOD(['propputref', helpstring(u'Table to view/edit.')], HRESULT, 'Table',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable), 'ppTable' )),
    COMMETHOD(['propputref', helpstring(u'QueryFilter of records to show.')], HRESULT, 'QueryFilter',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IQueryFilter), 'rhs' )),
    COMMETHOD(['propputref', helpstring(u'Selection set of records to show/select.')], HRESULT, 'SelectionSet',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ISelectionSet), 'ppSelection' )),
    COMMETHOD(['propget', helpstring(u'Selection set of records to show/select.')], HRESULT, 'SelectionSet',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ISelectionSet)), 'ppSelection' )),
    COMMETHOD(['propput', helpstring(u'Action to perform when table selections are made.')], HRESULT, 'TableSelectionAction',
              ( ['in'], esriTableSelectionActions, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Show only features that are selected.')], HRESULT, 'ShowSelected',
              ( ['in'], VARIANT_BOOL, 'pShowSelected' )),
    COMMETHOD(['propput', helpstring(u'Show alias names or the real field name in column headings. Default False.')], HRESULT, 'ShowAliasNamesInColumnHeadings',
              ( ['in'], VARIANT_BOOL, 'pShowAliases' )),
    COMMETHOD(['propputref', helpstring(u'The call back routine.')], HRESULT, 'Callback',
              ( ['in'], POINTER(ITableViewCallback), 'rhs' )),
    COMMETHOD([helpstring(u'Show table.')], HRESULT, 'Show',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentHWnd' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.tagRECT), 'initialExtent' ),
              ( ['in'], VARIANT_BOOL, 'initiallyVisible' )),
    COMMETHOD(['propget', helpstring(u'Table to view/edit.')], HRESULT, 'Table',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable)), 'ppTable' )),
    COMMETHOD(['propget', helpstring(u'Show only features that are selected.')], HRESULT, 'ShowSelected',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pShowSelected' )),
    COMMETHOD(['propget', helpstring(u'Show alias names or the real field name in column headings. Default False.')], HRESULT, 'ShowAliasNamesInColumnHeadings',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pShowAliases' )),
    COMMETHOD(['propput', helpstring(u'Allow editing. Default: True.')], HRESULT, 'AllowEditing',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
]
################################################################
## code template for ITableView2 implementation
##class ITableView2_Impl(object):
##    def Show(self, parentHWnd, initialExtent, initiallyVisible):
##        u'Show table.'
##        #return 
##
##    def QueryFilter(self, rhs):
##        u'QueryFilter of records to show.'
##        #return 
##
##    def _set(self, rhs):
##        u'Action to perform when table selections are made.'
##    TableSelectionAction = property(fset = _set, doc = _set.__doc__)
##
##    def Callback(self, rhs):
##        u'The call back routine.'
##        #return 
##
##    def _get(self):
##        u'Show only features that are selected.'
##        #return pShowSelected
##    def _set(self, pShowSelected):
##        u'Show only features that are selected.'
##    ShowSelected = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Table(self, ppTable):
##        u'Table to view/edit.'
##        #return 
##
##    def _get(self):
##        u'Show alias names or the real field name in column headings. Default False.'
##        #return pShowAliases
##    def _set(self, pShowAliases):
##        u'Show alias names or the real field name in column headings. Default False.'
##    ShowAliasNamesInColumnHeadings = property(_get, _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Allow editing. Default: True.'
##    AllowEditing = property(fset = _set, doc = _set.__doc__)
##
##    @property
##    def SelectionSet(self, ppSelection):
##        u'Selection set of records to show/select.'
##        #return 
##

class PrivilegesDialog(CoClass):
    u'A dialog for viewing and editing dataset privileges'
    _reg_clsid_ = GUID('{E87A524C-7EFC-4EF5-A93A-99718260A955}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{4A9C9ED7-F7DB-4614-B480-A5D265C961FC}', 10, 2)
class IPrivilegesDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Geodatabase privileges dialog.'
    _iid_ = GUID('{097EE20C-4DA2-40C0-B43A-D2B5F37B1774}')
    _idlflags_ = ['oleautomation']
PrivilegesDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IPrivilegesDialog]

class ITableViewOutput(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that allow you to output the table to a hDC.'
    _iid_ = GUID('{2DAF7BFC-0D1F-47CD-B9D5-D334D300CCA6}')
    _idlflags_ = ['oleautomation']
ITableViewOutput._methods_ = [
    COMMETHOD([helpstring(u'Sets the position of the view window.')], HRESULT, 'SetPosition',
              ( ['in'], c_int, 'left' ),
              ( ['in'], c_int, 'top' ),
              ( ['in'], c_int, 'width' ),
              ( ['in'], c_int, 'height' )),
    COMMETHOD([helpstring(u'Draw the table to the specified device context, and return windows enhanced metafile.')], HRESULT, 'Output',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDC' ),
              ( ['in'], c_int, 'dpi' ),
              ( ['in'], c_int, 'left' ),
              ( ['in'], c_int, 'top' ),
              ( ['in'], c_int, 'width' ),
              ( ['in'], c_int, 'height' ),
              ( ['in'], c_int, 'startRow' ),
              ( ['in'], c_int, 'startCol' ),
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'pHEMF' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether the metafile needs to be re-generated next time when Output is called.')], HRESULT, 'IsMetafileDirty',
              ( ['in'], VARIANT_BOOL, 'pIsDirty' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the metafile needs to be re-generated next time when Output is called.')], HRESULT, 'IsMetafileDirty',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pIsDirty' )),
]
################################################################
## code template for ITableViewOutput implementation
##class ITableViewOutput_Impl(object):
##    def Output(self, hDC, dpi, left, top, width, height, startRow, startCol):
##        u'Draw the table to the specified device context, and return windows enhanced metafile.'
##        #return pHEMF
##
##    def SetPosition(self, left, top, width, height):
##        u'Sets the position of the view window.'
##        #return 
##
##    def _get(self):
##        u'Indicates whether the metafile needs to be re-generated next time when Output is called.'
##        #return pIsDirty
##    def _set(self, pIsDirty):
##        u'Indicates whether the metafile needs to be re-generated next time when Output is called.'
##    IsMetafileDirty = property(_get, _set, doc = _set.__doc__)
##

class IExportOperation(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members used for exporting tables and feature classes.'
    _iid_ = GUID('{4147A361-EFC4-11D3-A0A4-00C04F6BC626}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriExportTableOptions'
esriExportAllRecords = 0
esriExportSelectedRecords = 1
esriExportFeaturesWithinExtent = 2
esriExportTableOptions = c_int # enum
IExportOperation._methods_ = [
    COMMETHOD([helpstring(u'Provides a dialog that prompts for export options. These include including the output table/feature class.')], HRESULT, 'GetOptions',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'featureClass' ),
              ( ['in'], BSTR, 'layerName' ),
              ( ['in'], VARIANT_BOOL, 'hasSelection' ),
              ( ['in'], VARIANT_BOOL, 'supportMapProjection' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentHWnd' ),
              ( ['out'], POINTER(VARIANT_BOOL), 'saveProjection' ),
              ( ['out'], POINTER(esriExportTableOptions), 'option' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetName)), 'outputDataset' )),
    COMMETHOD([helpstring(u'Exports the given table to a new table.')], HRESULT, 'ExportTable',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetName), 'inputDatasetName' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IQueryFilter), 'inputQueryFilter' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ISelectionSet), 'inputSelectionSet' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetName), 'outputDatasetName' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentHWnd' )),
    COMMETHOD([helpstring(u'Exports the given feature class to a new feature class.')], HRESULT, 'ExportFeatureClass',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetName), 'inputDatasetName' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IQueryFilter), 'inputQueryFilter' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ISelectionSet), 'inputSelectionSet' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGeometryDef), 'inputGeometryDef' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClassName), 'outputFClassName' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parantHWnd' )),
]
################################################################
## code template for IExportOperation implementation
##class IExportOperation_Impl(object):
##    def ExportFeatureClass(self, inputDatasetName, inputQueryFilter, inputSelectionSet, inputGeometryDef, outputFClassName, parantHWnd):
##        u'Exports the given feature class to a new feature class.'
##        #return 
##
##    def GetOptions(self, featureClass, layerName, hasSelection, supportMapProjection, parentHWnd):
##        u'Provides a dialog that prompts for export options. These include including the output table/feature class.'
##        #return saveProjection, option, outputDataset
##
##    def ExportTable(self, inputDatasetName, inputQueryFilter, inputSelectionSet, outputDatasetName, parentHWnd):
##        u'Exports the given table to a new table.'
##        #return 
##

class ITableDataCallback2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u"Provides access to member using which a client provide information that the object can't fully known about itself.  A callback interface."
    _iid_ = GUID('{F3001283-847B-44F4-A14A-22CD0017D79A}')
    _idlflags_ = ['oleautomation']
ITableDataCallback2._methods_ = [
    COMMETHOD([helpstring(u'Returns a search cursor on the table.')], HRESULT, 'TableSearch',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IQueryFilter), 'pQueryFilter' ),
              ( ['in'], VARIANT_BOOL, 'recycling' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ICursor)), 'ppCursor' )),
    COMMETHOD([helpstring(u'Returns a update cursor on the table.')], HRESULT, 'TableUpdate',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IQueryFilter), 'pQueryFilter' ),
              ( ['in'], VARIANT_BOOL, 'recycling' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ICursor)), 'ppCursor' )),
]
################################################################
## code template for ITableDataCallback2 implementation
##class ITableDataCallback2_Impl(object):
##    def TableSearch(self, pQueryFilter, recycling):
##        u'Returns a search cursor on the table.'
##        #return ppCursor
##
##    def TableUpdate(self, pQueryFilter, recycling):
##        u'Returns a update cursor on the table.'
##        #return ppCursor
##

class INewVersionDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the new version dialog for a versioned geodatabase.'
    _iid_ = GUID('{FB895243-121E-11D3-80BA-0080C7625171}')
    _idlflags_ = ['oleautomation']
INewVersionDialog._methods_ = [
    COMMETHOD([helpstring(u'Displays the dialog used to create new versions in a versioned geodatabase.')], HRESULT, 'DoModal',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'okPressed' )),
    COMMETHOD(['propget', helpstring(u'The name of the version.')], HRESULT, 'VersionName',
              ( ['retval', 'out'], POINTER(BSTR), 'VersionName' )),
    COMMETHOD(['propget', helpstring(u'The description of the version.')], HRESULT, 'VersionDescription',
              ( ['retval', 'out'], POINTER(BSTR), 'VersionDescription' )),
    COMMETHOD(['propget', helpstring(u'The level of access provided for the version.')], HRESULT, 'VersionAccess',
              ( ['retval', 'out'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriVersionAccess), 'VersionAccess' )),
]
################################################################
## code template for INewVersionDialog implementation
##class INewVersionDialog_Impl(object):
##    @property
##    def VersionDescription(self):
##        u'The description of the version.'
##        #return VersionDescription
##
##    def DoModal(self):
##        u'Displays the dialog used to create new versions in a versioned geodatabase.'
##        #return okPressed
##
##    @property
##    def VersionName(self):
##        u'The name of the version.'
##        #return VersionName
##
##    @property
##    def VersionAccess(self):
##        u'The level of access provided for the version.'
##        #return VersionAccess
##

class GdbAdminWindowFactory(CoClass):
    u'A window for administering enterprise Geodatabases.'
    _reg_clsid_ = GUID('{D94954D3-FD95-4D12-9AAB-B6C08C433439}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{4A9C9ED7-F7DB-4614-B480-A5D265C961FC}', 10, 2)
class IGdbAdminWindowFactory(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members for working with Geodatabase administration windows.'
    _iid_ = GUID('{31047739-1FD4-4732-9A27-D327252C340D}')
    _idlflags_ = []
GdbAdminWindowFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGdbAdminWindowFactory]

class ITableControlWidth(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the table once it has been shown.'
    _iid_ = GUID('{B74C691E-C7AF-11D3-9F80-00C04F6BC886}')
    _idlflags_ = ['oleautomation']
ITableControlWidth._methods_ = [
    COMMETHOD(['propget', helpstring(u'Table width of all columns, and scroll bars.')], HRESULT, 'FullTableWidth',
              ( ['retval', 'out'], POINTER(c_int), 'pMaxPixels' )),
    COMMETHOD(['propget', helpstring(u'Recommend minimum table width, that will ensure all controls can be seen.')], HRESULT, 'RecommendMinimumTableWidth',
              ( ['retval', 'out'], POINTER(c_int), 'pMinPixels' )),
]
################################################################
## code template for ITableControlWidth implementation
##class ITableControlWidth_Impl(object):
##    @property
##    def RecommendMinimumTableWidth(self):
##        u'Recommend minimum table width, that will ensure all controls can be seen.'
##        #return pMinPixels
##
##    @property
##    def FullTableWidth(self):
##        u'Table width of all columns, and scroll bars.'
##        #return pMaxPixels
##

class ITableView3(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that interact with table.'
    _iid_ = GUID('{EEDBF036-7E29-4C42-881E-B8E7ADDC727A}')
    _idlflags_ = ['oleautomation']
ITableView3._methods_ = [
    COMMETHOD(['propputref', helpstring(u'Table to view/edit.')], HRESULT, 'Table',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable), 'ppTable' )),
    COMMETHOD(['propputref', helpstring(u'QueryFilter of records to show.')], HRESULT, 'QueryFilter',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IQueryFilter), 'rhs' )),
    COMMETHOD(['propputref', helpstring(u'Selection set of records to show/select.')], HRESULT, 'SelectionSet',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ISelectionSet), 'ppSelection' )),
    COMMETHOD(['propget', helpstring(u'Selection set of records to show/select.')], HRESULT, 'SelectionSet',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ISelectionSet)), 'ppSelection' )),
    COMMETHOD(['propput', helpstring(u'Action to perform when table selections are made.')], HRESULT, 'TableSelectionAction',
              ( ['in'], esriTableSelectionActions, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Show only features that are selected.')], HRESULT, 'ShowSelected',
              ( ['in'], VARIANT_BOOL, 'pShowSelected' )),
    COMMETHOD(['propput', helpstring(u'Show alias names or the real field name in column headings. Default False.')], HRESULT, 'ShowAliasNamesInColumnHeadings',
              ( ['in'], VARIANT_BOOL, 'pShowAliases' )),
    COMMETHOD(['propputref', helpstring(u'The call back routine.')], HRESULT, 'Callback',
              ( ['in'], POINTER(ITableViewCallback), 'rhs' )),
    COMMETHOD([helpstring(u'Show table.')], HRESULT, 'Show',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentHWnd' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.tagRECT), 'initialExtent' ),
              ( ['in'], VARIANT_BOOL, 'initiallyVisible' )),
    COMMETHOD(['propget', helpstring(u'Table to view/edit.')], HRESULT, 'Table',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable)), 'ppTable' )),
    COMMETHOD(['propget', helpstring(u'Show only features that are selected.')], HRESULT, 'ShowSelected',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pShowSelected' )),
    COMMETHOD(['propget', helpstring(u'Show alias names or the real field name in column headings. Default False.')], HRESULT, 'ShowAliasNamesInColumnHeadings',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pShowAliases' )),
    COMMETHOD(['propput', helpstring(u'Allow editing. Default: True.')], HRESULT, 'AllowEditing',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Allow add row to be displayed during editing. Default: True.')], HRESULT, 'AllowAddRow',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
]
################################################################
## code template for ITableView3 implementation
##class ITableView3_Impl(object):
##    def Show(self, parentHWnd, initialExtent, initiallyVisible):
##        u'Show table.'
##        #return 
##
##    def QueryFilter(self, rhs):
##        u'QueryFilter of records to show.'
##        #return 
##
##    def _set(self, rhs):
##        u'Action to perform when table selections are made.'
##    TableSelectionAction = property(fset = _set, doc = _set.__doc__)
##
##    def Callback(self, rhs):
##        u'The call back routine.'
##        #return 
##
##    def _get(self):
##        u'Show only features that are selected.'
##        #return pShowSelected
##    def _set(self, pShowSelected):
##        u'Show only features that are selected.'
##    ShowSelected = property(_get, _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Allow add row to be displayed during editing. Default: True.'
##    AllowAddRow = property(fset = _set, doc = _set.__doc__)
##
##    @property
##    def Table(self, ppTable):
##        u'Table to view/edit.'
##        #return 
##
##    def _get(self):
##        u'Show alias names or the real field name in column headings. Default False.'
##        #return pShowAliases
##    def _set(self, pShowAliases):
##        u'Show alias names or the real field name in column headings. Default False.'
##    ShowAliasNamesInColumnHeadings = property(_get, _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Allow editing. Default: True.'
##    AllowEditing = property(fset = _set, doc = _set.__doc__)
##
##    @property
##    def SelectionSet(self, ppSelection):
##        u'Selection set of records to show/select.'
##        #return 
##

class ITableControl(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the table once it has been shown.'
    _iid_ = GUID('{38CDB63F-BFAD-11D2-9F23-00C04F6BC886}')
    _idlflags_ = ['oleautomation']
ITableControl._methods_ = [
    COMMETHOD([helpstring(u'Call after start or stop editing, to update table grid.')], HRESULT, 'EditChanged'),
    COMMETHOD([helpstring(u'Lose cache, so the table window is current with the underlying database.')], HRESULT, 'RemoveAndReloadCache'),
    COMMETHOD([helpstring(u'Updates the current selection, that the current selection is currently pointing to.')], HRESULT, 'UpdateSelection',
              ( [], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ISelectionSet), 'pSelection' )),
    COMMETHOD([helpstring(u'Draws selected features on display.')], HRESULT, 'DrawSelectedShapes',
              ( ['in'], POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IDisplay), 'pDisplay' )),
    COMMETHOD([helpstring(u'ReReads rows. Called when viewing selected records and the selection changes.')], HRESULT, 'RereadFIDs',
              ( [], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ISelectionSet), 'pSelection' )),
    COMMETHOD([helpstring(u'The current row the user is on. If isOid = TRUE, then rowNumber is an OID, else it is an offset.')], HRESULT, 'SetCurrentRow',
              ( ['in'], VARIANT_BOOL, 'isOid' ),
              ( ['in'], c_int, 'rowNumber' )),
    COMMETHOD([helpstring(u'The current row the user is on. If isOid = TRUE, then rowNumber is an OID, else it is an offset.')], HRESULT, 'GetCurrentRow',
              ( ['in'], VARIANT_BOOL, 'isOid' ),
              ( ['retval', 'out'], POINTER(c_int), 'pRowNumber' )),
    COMMETHOD([helpstring(u'Redraws the grid.')], HRESULT, 'Redraw'),
]
################################################################
## code template for ITableControl implementation
##class ITableControl_Impl(object):
##    def GetCurrentRow(self, isOid):
##        u'The current row the user is on. If isOid = TRUE, then rowNumber is an OID, else it is an offset.'
##        #return pRowNumber
##
##    def RereadFIDs(self, pSelection):
##        u'ReReads rows. Called when viewing selected records and the selection changes.'
##        #return 
##
##    def SetCurrentRow(self, isOid, rowNumber):
##        u'The current row the user is on. If isOid = TRUE, then rowNumber is an OID, else it is an offset.'
##        #return 
##
##    def DrawSelectedShapes(self, pDisplay):
##        u'Draws selected features on display.'
##        #return 
##
##    def EditChanged(self):
##        u'Call after start or stop editing, to update table grid.'
##        #return 
##
##    def RemoveAndReloadCache(self):
##        u'Lose cache, so the table window is current with the underlying database.'
##        #return 
##
##    def Redraw(self):
##        u'Redraws the grid.'
##        #return 
##
##    def UpdateSelection(self, pSelection):
##        u'Updates the current selection, that the current selection is currently pointing to.'
##        #return 
##

class IChangeVersionDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the change version dialog for a versioned geodatabase.'
    _iid_ = GUID('{B647D0BC-6221-4497-80DC-C12A7068C728}')
    _idlflags_ = []
IChangeVersionDialog._methods_ = [
    COMMETHOD([helpstring(u'Displays the dialog used to create new versions in a versioned geodatabase.')], HRESULT, 'DoModal',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspace), 'workspace' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'okPressed' )),
    COMMETHOD(['propget', helpstring(u'The selected version.')], HRESULT, 'SelectedVersion',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IVersion)), 'vers' )),
]
################################################################
## code template for IChangeVersionDialog implementation
##class IChangeVersionDialog_Impl(object):
##    def DoModal(self, workspace):
##        u'Displays the dialog used to create new versions in a versioned geodatabase.'
##        #return okPressed
##
##    @property
##    def SelectedVersion(self):
##        u'The selected version.'
##        #return vers
##

class ITableViewContextMenus(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u"Provides access to menu requests that occur with the TableView. This interface must the QI'able from the callback interface."
    _iid_ = GUID('{488B6554-E351-4648-A8F4-2BDEFF20CD99}')
    _idlflags_ = ['oleautomation']
ITableViewContextMenus._methods_ = [
    COMMETHOD([helpstring(u'This method is called if the user requests a Column menu.')], HRESULT, 'ColumnMenu',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Handled' )),
    COMMETHOD([helpstring(u'This method is called if the user requests a Row menu.')], HRESULT, 'RowMenu',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Handled' )),
    COMMETHOD([helpstring(u'This method is called if the user requests a Cell menu.')], HRESULT, 'CellMenu',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Handled' )),
    COMMETHOD([helpstring(u'This method is called if the user requests a Option menu.')], HRESULT, 'OptionMenu',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Handled' )),
]
################################################################
## code template for ITableViewContextMenus implementation
##class ITableViewContextMenus_Impl(object):
##    def OptionMenu(self):
##        u'This method is called if the user requests a Option menu.'
##        #return Handled
##
##    def CellMenu(self):
##        u'This method is called if the user requests a Cell menu.'
##        #return Handled
##
##    def ColumnMenu(self):
##        u'This method is called if the user requests a Column menu.'
##        #return Handled
##
##    def RowMenu(self):
##        u'This method is called if the user requests a Row menu.'
##        #return Handled
##

class TableView(CoClass):
    u'Window to display Tables.'
    _reg_clsid_ = GUID('{11B27697-AC0E-11D2-A08C-0000F8775BF9}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{4A9C9ED7-F7DB-4614-B480-A5D265C961FC}', 10, 2)
class ITableView(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that set up the table and initially show it.'
    _iid_ = GUID('{11B27696-AC0E-11D2-A08C-0000F8775BF9}')
    _idlflags_ = ['oleautomation']
class ITableViewEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to events that occur with the TableView.'
    _iid_ = GUID('{EAFDE0DF-251D-4936-AAA7-0AF6D4DBD685}')
    _idlflags_ = ['oleautomation']
TableView._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ITableView, ITableView2, ITableView3, ITableView4, ITableViewOutput, ITableControl, ITableControl2, ITableControl3, ITableControlWidth, ITableControlInfo, ITableViewTableFields, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone]
TableView._outgoing_interfaces_ = [ITableViewEvents]


# values for enumeration 'esriCalculatorErrorType'
esriCalculatorErrorNoScript = 0
esriCalculatorErrorParse = 1
esriCalculatorErrorCode = 2
esriCalculatorErrorEmptyVal = 3
esriCalculatorErrorPutValue = 4
esriCalculatorErrorStore = 5
esriCalculatorErrorAllEmptyVal = 6
esriCalculatorErrorType = c_int # enum
class ITableDataCallback(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u"Provides access to member using which a client provide information that the object can't fully known about itself.  A callback interface."
    _iid_ = GUID('{DF4FB24A-FD07-11D2-9F4C-00C04F6BC886}')
    _idlflags_ = ['oleautomation']
ICalculatorUI._methods_ = [
    COMMETHOD(['propputref', helpstring(u'Table to perform calculation on.')], HRESULT, 'Table',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable), 'rhs' )),
    COMMETHOD(['propputref', helpstring(u'SelectionSet to perform calculation on (optional).')], HRESULT, 'SelectionSet',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ISelectionSet), 'rhs' )),
    COMMETHOD(['propputref', helpstring(u'QueryFilter used for reading and writing data (optional).')], HRESULT, 'QueryFilter',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IQueryFilter), 'rhs' )),
    COMMETHOD(['propputref', helpstring(u'The call back routine.')], HRESULT, 'Callback',
              ( ['in'], POINTER(ITableDataCallback), 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Field to perform calculation on.')], HRESULT, 'Field',
              ( ['in'], BSTR, 'rhs' )),
    COMMETHOD([helpstring(u'Displays the dialog used to perform calculations.')], HRESULT, 'DoModal',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentWindow' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'ppStoredExtent' )),
]
################################################################
## code template for ICalculatorUI implementation
##class ICalculatorUI_Impl(object):
##    def Callback(self, rhs):
##        u'The call back routine.'
##        #return 
##
##    def QueryFilter(self, rhs):
##        u'QueryFilter used for reading and writing data (optional).'
##        #return 
##
##    def _set(self, rhs):
##        u'Field to perform calculation on.'
##    Field = property(fset = _set, doc = _set.__doc__)
##
##    def DoModal(self, parentWindow):
##        u'Displays the dialog used to perform calculations.'
##        #return ppStoredExtent
##
##    def Table(self, rhs):
##        u'Table to perform calculation on.'
##        #return 
##
##    def SelectionSet(self, rhs):
##        u'SelectionSet to perform calculation on (optional).'
##        #return 
##

ITableViewEvents._methods_ = [
    COMMETHOD([helpstring(u'This event is fired when the user changes cell location.')], HRESULT, 'OnCellMove',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRow), 'pRow' ),
              ( ['in'], c_int, 'fieldPos' )),
    COMMETHOD([helpstring(u'This event is fired when the user presses the select toggle.')], HRESULT, 'OnSelectToggle'),
]
################################################################
## code template for ITableViewEvents implementation
##class ITableViewEvents_Impl(object):
##    def OnCellMove(self, pRow, fieldPos):
##        u'This event is fired when the user changes cell location.'
##        #return 
##
##    def OnSelectToggle(self):
##        u'This event is fired when the user presses the select toggle.'
##        #return 
##

class IGPQueryPropertyPage(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Query property page.'
    _iid_ = GUID('{331DC86B-6C88-4A46-A025-9A13BFFF5374}')
    _idlflags_ = ['oleautomation', 'hidden']
IGPQueryPropertyPage._methods_ = [
    COMMETHOD([helpstring(u'The insert DETable and its corresponding table.')], HRESULT, 'AddDETable',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDETable), 'pDETable' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable), 'pTable' )),
]
################################################################
## code template for IGPQueryPropertyPage implementation
##class IGPQueryPropertyPage_Impl(object):
##    def AddDETable(self, pDETable, pTable):
##        u'The insert DETable and its corresponding table.'
##        #return 
##

IGdbAdminWindowFactory._methods_ = [
    COMMETHOD([helpstring(u'Opens the Geodatabase administration window.')], HRESULT, 'Open',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspace), 'workspace' )),
    COMMETHOD([helpstring(u'Opens the Geodatabase administration window to show user connected to the database.')], HRESULT, 'ShowConnectedUsers',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspace), 'workspace' )),
    COMMETHOD([helpstring(u'Opens the Geodatabase adminstration window to show locks on the dataset.')], HRESULT, 'ShowDatasetLocks',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetName), 'dataset' )),
]
################################################################
## code template for IGdbAdminWindowFactory implementation
##class IGdbAdminWindowFactory_Impl(object):
##    def ShowDatasetLocks(self, dataset):
##        u'Opens the Geodatabase adminstration window to show locks on the dataset.'
##        #return 
##
##    def Open(self, workspace):
##        u'Opens the Geodatabase administration window.'
##        #return 
##
##    def ShowConnectedUsers(self, workspace):
##        u'Opens the Geodatabase administration window to show user connected to the database.'
##        #return 
##

ITableDataCallback._methods_ = [
    COMMETHOD([helpstring(u'Returns a search cursor on the table.')], HRESULT, 'TableSearch',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IQueryFilter), 'pQueryFilter' ),
              ( ['in'], VARIANT_BOOL, 'recycling' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ICursor)), 'ppCursor' )),
]
################################################################
## code template for ITableDataCallback implementation
##class ITableDataCallback_Impl(object):
##    def TableSearch(self, pQueryFilter, recycling):
##        u'Returns a search cursor on the table.'
##        #return ppCursor
##

class ExportOperation(CoClass):
    u'ExportOperation class used to export a table or feature class.'
    _reg_clsid_ = GUID('{4147A362-EFC4-11D3-A0A4-00C04F6BC626}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{4A9C9ED7-F7DB-4614-B480-A5D265C961FC}', 10, 2)
ExportOperation._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IExportOperation, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureProgress]

class TableViewEventsHelper(CoClass):
    _reg_clsid_ = GUID('{1093852B-08FC-4729-99E7-A28BFEC32D5C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{4A9C9ED7-F7DB-4614-B480-A5D265C961FC}', 10, 2)
TableViewEventsHelper._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown]
TableViewEventsHelper._outgoing_interfaces_ = [ITableViewEvents]

ICalculator._methods_ = [
    COMMETHOD(['propputref', helpstring(u'Cursor used to access the rows on which the calculation will be performed.')], HRESULT, 'Cursor',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ICursor), 'rhs' )),
    COMMETHOD(['propputref', helpstring(u'The call back routine.')], HRESULT, 'Callback',
              ( ['in'], POINTER(ICalculatorCallback), 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Field to perform the calculation on.')], HRESULT, 'Field',
              ( ['in'], BSTR, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'A pre-calculation determination of a value or variable that may be used as the expression (or value) of the calculation.')], HRESULT, 'PreExpression',
              ( ['in'], BSTR, 'pPreExpression' )),
    COMMETHOD(['propget', helpstring(u'A pre-calculation determination of a value or variable that may be used as the expression (or value) of the calculation.')], HRESULT, 'PreExpression',
              ( ['retval', 'out'], POINTER(BSTR), 'pPreExpression' )),
    COMMETHOD(['propput', helpstring(u'Expression or value applied to a field in each row of the cursor.')], HRESULT, 'Expression',
              ( ['in'], BSTR, 'pExpression' )),
    COMMETHOD(['propget', helpstring(u'Expression or value applied to a field in each row of the cursor.')], HRESULT, 'Expression',
              ( ['retval', 'out'], POINTER(BSTR), 'pExpression' )),
    COMMETHOD([helpstring(u'Performs the calculation by executing the pre-expression and expression.')], HRESULT, 'Calculate',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'ppStoredExtent' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether to show a message prompt when an error occurs during calculation.')], HRESULT, 'ShowErrorPrompt',
              ( ['in'], VARIANT_BOOL, 'pShowPrompt' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether to show a message prompt when an error occurs during calculation.')], HRESULT, 'ShowErrorPrompt',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pShowPrompt' )),
]
################################################################
## code template for ICalculator implementation
##class ICalculator_Impl(object):
##    def Calculate(self):
##        u'Performs the calculation by executing the pre-expression and expression.'
##        #return ppStoredExtent
##
##    def _set(self, rhs):
##        u'Field to perform the calculation on.'
##    Field = property(fset = _set, doc = _set.__doc__)
##
##    def Cursor(self, rhs):
##        u'Cursor used to access the rows on which the calculation will be performed.'
##        #return 
##
##    def Callback(self, rhs):
##        u'The call back routine.'
##        #return 
##
##    def _get(self):
##        u'A pre-calculation determination of a value or variable that may be used as the expression (or value) of the calculation.'
##        #return pPreExpression
##    def _set(self, pPreExpression):
##        u'A pre-calculation determination of a value or variable that may be used as the expression (or value) of the calculation.'
##    PreExpression = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Expression or value applied to a field in each row of the cursor.'
##        #return pExpression
##    def _set(self, pExpression):
##        u'Expression or value applied to a field in each row of the cursor.'
##    Expression = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether to show a message prompt when an error occurs during calculation.'
##        #return pShowPrompt
##    def _set(self, pShowPrompt):
##        u'Indicates whether to show a message prompt when an error occurs during calculation.'
##    ShowErrorPrompt = property(_get, _set, doc = _set.__doc__)
##

ICalculatorUIJoinSettings._methods_ = [
    COMMETHOD(['propput', helpstring(u'Should row events be fired during calculation (default false).')], HRESULT, 'FireRowEventsForJoins',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
]
################################################################
## code template for ICalculatorUIJoinSettings implementation
##class ICalculatorUIJoinSettings_Impl(object):
##    def _set(self, rhs):
##        u'Should row events be fired during calculation (default false).'
##    FireRowEventsForJoins = property(fset = _set, doc = _set.__doc__)
##

IQueryPropertyPageFieldInfo._methods_ = [
    COMMETHOD([helpstring(u'Sets the field info for a perticular string.')], HRESULT, 'SetFieldInfo',
              ( ['in'], BSTR, 'fieldName' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFieldInfo), 'pFieldInfo' )),
    COMMETHOD([helpstring(u'Removes all the field infos set using the SetFieldInfo method.')], HRESULT, 'RemoveAllFieldInfos'),
    COMMETHOD([helpstring(u'Refreshes the fields list.')], HRESULT, 'RefreshFields'),
]
################################################################
## code template for IQueryPropertyPageFieldInfo implementation
##class IQueryPropertyPageFieldInfo_Impl(object):
##    def RefreshFields(self):
##        u'Refreshes the fields list.'
##        #return 
##
##    def SetFieldInfo(self, fieldName, pFieldInfo):
##        u'Sets the field info for a perticular string.'
##        #return 
##
##    def RemoveAllFieldInfos(self):
##        u'Removes all the field infos set using the SetFieldInfo method.'
##        #return 
##

IQueryPropertyPage2._methods_ = [
    COMMETHOD(['propput', helpstring(u'The query name (optional).')], HRESULT, 'ExpressionLabel',
              ( ['in'], BSTR, 'rhs' )),
    COMMETHOD(['propputref', helpstring(u'The query table. A null value resets this option.')], HRESULT, 'Table',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable), 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Default expression.')], HRESULT, 'Expression',
              ( ['in'], BSTR, 'rhs' )),
    COMMETHOD(['propget', helpstring(u'Provide a QueryFilter after form has been executed.')], HRESULT, 'QueryFilter',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IQueryFilter)), 'ppQueryFilter' )),
    COMMETHOD(['propputref', helpstring(u'The call back routine.')], HRESULT, 'Callback',
              ( ['in'], POINTER(ITableDataCallback), 'rhs' )),
    COMMETHOD([helpstring(u'Clears all internals cursors.')], HRESULT, 'FreeCursors'),
]
################################################################
## code template for IQueryPropertyPage2 implementation
##class IQueryPropertyPage2_Impl(object):
##    def FreeCursors(self):
##        u'Clears all internals cursors.'
##        #return 
##
##    def _set(self, rhs):
##        u'The query name (optional).'
##    ExpressionLabel = property(fset = _set, doc = _set.__doc__)
##
##    @property
##    def QueryFilter(self):
##        u'Provide a QueryFilter after form has been executed.'
##        #return ppQueryFilter
##
##    def Callback(self, rhs):
##        u'The call back routine.'
##        #return 
##
##    def Table(self, rhs):
##        u'The query table. A null value resets this option.'
##        #return 
##
##    def _set(self, rhs):
##        u'Default expression.'
##    Expression = property(fset = _set, doc = _set.__doc__)
##

ITableView._methods_ = [
    COMMETHOD(['propputref', helpstring(u'Table to view/edit.')], HRESULT, 'Table',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable), 'rhs' )),
    COMMETHOD(['propputref', helpstring(u'QueryFilter of records to show.')], HRESULT, 'QueryFilter',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IQueryFilter), 'rhs' )),
    COMMETHOD(['propputref', helpstring(u'Selection set of records to show/select.')], HRESULT, 'SelectionSet',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ISelectionSet), 'ppSelection' )),
    COMMETHOD(['propget', helpstring(u'Selection set of records to show/select.')], HRESULT, 'SelectionSet',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ISelectionSet)), 'ppSelection' )),
    COMMETHOD(['propput', helpstring(u'Action to perform when table selections are made.')], HRESULT, 'TableSelectionAction',
              ( ['in'], esriTableSelectionActions, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Show only features that are selected.')], HRESULT, 'ShowSelected',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Show alias names or the real field name in column headings. Default False.')], HRESULT, 'ShowAliasNamesInColumnHeadings',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD(['propputref', helpstring(u'The call back routine.')], HRESULT, 'Callback',
              ( ['in'], POINTER(ITableViewCallback), 'rhs' )),
    COMMETHOD([helpstring(u'Show table.')], HRESULT, 'Show',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentHWnd' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.tagRECT), 'initialExtent' ),
              ( ['in'], VARIANT_BOOL, 'initiallyVisible' )),
]
################################################################
## code template for ITableView implementation
##class ITableView_Impl(object):
##    def Show(self, parentHWnd, initialExtent, initiallyVisible):
##        u'Show table.'
##        #return 
##
##    def QueryFilter(self, rhs):
##        u'QueryFilter of records to show.'
##        #return 
##
##    def _set(self, rhs):
##        u'Action to perform when table selections are made.'
##    TableSelectionAction = property(fset = _set, doc = _set.__doc__)
##
##    def Callback(self, rhs):
##        u'The call back routine.'
##        #return 
##
##    def _set(self, rhs):
##        u'Show only features that are selected.'
##    ShowSelected = property(fset = _set, doc = _set.__doc__)
##
##    def Table(self, rhs):
##        u'Table to view/edit.'
##        #return 
##
##    def _set(self, rhs):
##        u'Show alias names or the real field name in column headings. Default False.'
##    ShowAliasNamesInColumnHeadings = property(fset = _set, doc = _set.__doc__)
##
##    @property
##    def SelectionSet(self, ppSelection):
##        u'Selection set of records to show/select.'
##        #return 
##

class GNWeightsPropPage(CoClass):
    u'Esri GeometricNetwork Weights property page.'
    _reg_clsid_ = GUID('{750D8191-E0B5-11D2-99BF-0000F80372B4}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{4A9C9ED7-F7DB-4614-B480-A5D265C961FC}', 10, 2)
GNWeightsPropPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

ITableViewCallback._methods_ = [
    COMMETHOD(['propget', helpstring(u'Current Spatial Reference.')], HRESULT, 'SpatialReference',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference)), 'ppSpatialReference' )),
    COMMETHOD([helpstring(u'Selection has been changed.')], HRESULT, 'SelectionChange',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ISelectionSet), 'pSelection' ),
              ( ['in'], VARIANT_BOOL, 'newSelectionSet' )),
    COMMETHOD([helpstring(u'Refresh graphics for selected table or selection when viewing the full table.')], HRESULT, 'RefreshSelection',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'pRedrawArea' )),
    COMMETHOD([helpstring(u'Refresh all screen caches.')], HRESULT, 'RefreshDisplay',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'pRedrawArea' )),
    COMMETHOD([helpstring(u'Redraw feature layer (ie, when features are deleted, etc).')], HRESULT, 'RedrawFeatureLayer',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'pRedrawArea' )),
    COMMETHOD([helpstring(u'Start an edit operation.')], HRESULT, 'StartEditOperation'),
    COMMETHOD([helpstring(u'Stop an edit operation.')], HRESULT, 'StopEditOperation',
              ( [], BSTR, 'operationName' )),
    COMMETHOD([helpstring(u'Enable/Disable Undo/Redo.')], HRESULT, 'EnableEditUndoRedo',
              ( [], VARIANT_BOOL, 'Enable' )),
    COMMETHOD([helpstring(u'Abort an edit operation.')], HRESULT, 'AbortEditOperation'),
    COMMETHOD([helpstring(u'Show the destination relationship table with origin table selection.')], HRESULT, 'ShowRelationshipTable',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRelationshipClass), 'pRelationshipClass' ),
              ( ['in'], VARIANT_BOOL, 'showSource' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ISelectionSet), 'pOriginSelectionSet' )),
    COMMETHOD([helpstring(u'Returns a cursor on the FeatureLayer or Table.')], HRESULT, 'Search',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IQueryFilter), 'pQueryFilter' ),
              ( ['in'], VARIANT_BOOL, 'recycling' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ICursor)), 'ppCursor' )),
]
################################################################
## code template for ITableViewCallback implementation
##class ITableViewCallback_Impl(object):
##    def Search(self, pQueryFilter, recycling):
##        u'Returns a cursor on the FeatureLayer or Table.'
##        #return ppCursor
##
##    def ShowRelationshipTable(self, pRelationshipClass, showSource, pOriginSelectionSet):
##        u'Show the destination relationship table with origin table selection.'
##        #return 
##
##    def RefreshDisplay(self, pRedrawArea):
##        u'Refresh all screen caches.'
##        #return 
##
##    def StartEditOperation(self):
##        u'Start an edit operation.'
##        #return 
##
##    @property
##    def SpatialReference(self):
##        u'Current Spatial Reference.'
##        #return ppSpatialReference
##
##    def SelectionChange(self, pSelection, newSelectionSet):
##        u'Selection has been changed.'
##        #return 
##
##    def AbortEditOperation(self):
##        u'Abort an edit operation.'
##        #return 
##
##    def RefreshSelection(self, pRedrawArea):
##        u'Refresh graphics for selected table or selection when viewing the full table.'
##        #return 
##
##    def StopEditOperation(self, operationName):
##        u'Stop an edit operation.'
##        #return 
##
##    def EnableEditUndoRedo(self, Enable):
##        u'Enable/Disable Undo/Redo.'
##        #return 
##
##    def RedrawFeatureLayer(self, pRedrawArea):
##        u'Redraw feature layer (ie, when features are deleted, etc).'
##        #return 
##

class NewVersionDialog(CoClass):
    u'A dialog for creating new versions in a versioned geodatabase.'
    _reg_clsid_ = GUID('{FB895242-121E-11D3-80BA-0080C7625171}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{4A9C9ED7-F7DB-4614-B480-A5D265C961FC}', 10, 2)
NewVersionDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, INewVersionDialog]

IVersionManager._methods_ = [
    COMMETHOD([helpstring(u'Displays the dialog used to manage versions for a versioned geodatabase.')], HRESULT, 'DoModal',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IVersionedWorkspace), 'vw' )),
]
################################################################
## code template for IVersionManager implementation
##class IVersionManager_Impl(object):
##    def DoModal(self, vw):
##        u'Displays the dialog used to manage versions for a versioned geodatabase.'
##        #return 
##

class IProtectNameGeoDatabaseUI(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to dummy methods protecting name correctness.'
    _iid_ = GUID('{3F562D92-BB1C-4D4F-A1E3-998A1793C384}')
    _idlflags_ = []
IProtectNameGeoDatabaseUI._methods_ = [
    COMMETHOD([], HRESULT, 'ProtectOLE_HANDLE',
              ( [], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'aHandle' )),
    COMMETHOD([], HRESULT, 'ProtectOLE_COLOR',
              ( [], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_COLOR, 'aColor' )),
]
################################################################
## code template for IProtectNameGeoDatabaseUI implementation
##class IProtectNameGeoDatabaseUI_Impl(object):
##    def ProtectOLE_COLOR(self, aColor):
##        '-no docstring-'
##        #return 
##
##    def ProtectOLE_HANDLE(self, aHandle):
##        '-no docstring-'
##        #return 
##

ICalculatorUI2._methods_ = [
    COMMETHOD(['propputref', helpstring(u'Table to perform calculation on.')], HRESULT, 'Table',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable), 'rhs' )),
    COMMETHOD(['propputref', helpstring(u'SelectionSet to perform calculation on (optional).')], HRESULT, 'SelectionSet',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ISelectionSet), 'rhs' )),
    COMMETHOD(['propputref', helpstring(u'QueryFilter used for reading and writing data (optional).')], HRESULT, 'QueryFilter',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IQueryFilter), 'rhs' )),
    COMMETHOD(['propputref', helpstring(u'The call back routine.')], HRESULT, 'Callback',
              ( ['in'], POINTER(ITableDataCallback), 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Field to perform calculation on.')], HRESULT, 'Field',
              ( ['in'], BSTR, 'rhs' )),
    COMMETHOD([helpstring(u'Displays the dialog used to perform calculations.')], HRESULT, 'DoModal',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentWindow' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'ppStoredExtent' )),
    COMMETHOD(['propput', helpstring(u'A pre-calculation code determination of a value or variable that may be passed to the expression, or value, of the calculation.')], HRESULT, 'PreExpression',
              ( ['in'], BSTR, 'pPreExpression' )),
    COMMETHOD(['propget', helpstring(u'A pre-calculation code determination of a value or variable that may be passed to the expression, or value, of the calculation.')], HRESULT, 'PreExpression',
              ( ['retval', 'out'], POINTER(BSTR), 'pPreExpression' )),
    COMMETHOD(['propput', helpstring(u'Expression or value applied to a field in each row of the cursor.')], HRESULT, 'Expression',
              ( ['in'], BSTR, 'pExpression' )),
    COMMETHOD(['propget', helpstring(u'Expression or value applied to a field in each row of the cursor.')], HRESULT, 'Expression',
              ( ['retval', 'out'], POINTER(BSTR), 'pExpression' )),
]
################################################################
## code template for ICalculatorUI2 implementation
##class ICalculatorUI2_Impl(object):
##    def Callback(self, rhs):
##        u'The call back routine.'
##        #return 
##
##    def QueryFilter(self, rhs):
##        u'QueryFilter used for reading and writing data (optional).'
##        #return 
##
##    def _set(self, rhs):
##        u'Field to perform calculation on.'
##    Field = property(fset = _set, doc = _set.__doc__)
##
##    def DoModal(self, parentWindow):
##        u'Displays the dialog used to perform calculations.'
##        #return ppStoredExtent
##
##    def _get(self):
##        u'A pre-calculation code determination of a value or variable that may be passed to the expression, or value, of the calculation.'
##        #return pPreExpression
##    def _set(self, pPreExpression):
##        u'A pre-calculation code determination of a value or variable that may be passed to the expression, or value, of the calculation.'
##    PreExpression = property(_get, _set, doc = _set.__doc__)
##
##    def Table(self, rhs):
##        u'Table to perform calculation on.'
##        #return 
##
##    def _get(self):
##        u'Expression or value applied to a field in each row of the cursor.'
##        #return pExpression
##    def _set(self, pExpression):
##        u'Expression or value applied to a field in each row of the cursor.'
##    Expression = property(_get, _set, doc = _set.__doc__)
##
##    def SelectionSet(self, rhs):
##        u'SelectionSet to perform calculation on (optional).'
##        #return 
##

IHistoricalMarkerManager._methods_ = [
    COMMETHOD([helpstring(u'Displays the dialog used to manage historical markers.')], HRESULT, 'DoModal',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IHistoricalWorkspace), 'historicalWorkspace' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hParentWnd' )),
]
################################################################
## code template for IHistoricalMarkerManager implementation
##class IHistoricalMarkerManager_Impl(object):
##    def DoModal(self, historicalWorkspace, hParentWnd):
##        u'Displays the dialog used to manage historical markers.'
##        #return 
##

ICalculatorCallback._methods_ = [
    COMMETHOD([helpstring(u'Current Status of the calculator.')], HRESULT, 'Status',
              ( ['in'], c_int, 'rowsWritten' ),
              ( ['in'], VARIANT_BOOL, 'lastStatus' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pAbort' )),
    COMMETHOD([helpstring(u'Error message provided by the calculator.')], HRESULT, 'CalculatorError',
              ( ['in'], c_int, 'rowID' ),
              ( ['in'], VARIANT_BOOL, 'bHasOID' ),
              ( ['in'], esriCalculatorErrorType, 'errorType' ),
              ( ['in'], VARIANT_BOOL, 'bShowPrompt' ),
              ( ['in'], BSTR, 'errorMsg' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pAbort' )),
    COMMETHOD([helpstring(u'Warning message provided by the calculator.')], HRESULT, 'CalculatorWarning',
              ( ['in'], c_int, 'rowID' ),
              ( ['in'], VARIANT_BOOL, 'bHasOID' ),
              ( ['in'], esriCalculatorErrorType, 'errorType' ),
              ( ['in'], BSTR, 'errorMsg' )),
]
################################################################
## code template for ICalculatorCallback implementation
##class ICalculatorCallback_Impl(object):
##    def Status(self, rowsWritten, lastStatus):
##        u'Current Status of the calculator.'
##        #return pAbort
##
##    def CalculatorError(self, rowID, bHasOID, errorType, bShowPrompt, errorMsg):
##        u'Error message provided by the calculator.'
##        #return pAbort
##
##    def CalculatorWarning(self, rowID, bHasOID, errorType, errorMsg):
##        u'Warning message provided by the calculator.'
##        #return 
##

IPrivilegesDialog._methods_ = [
    COMMETHOD([helpstring(u'Show the privileges dialog based on the provided dataset.')], HRESULT, 'DoModal',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetName), 'dataset' )),
]
################################################################
## code template for IPrivilegesDialog implementation
##class IPrivilegesDialog_Impl(object):
##    def DoModal(self, dataset):
##        u'Show the privileges dialog based on the provided dataset.'
##        #return 
##

class IDefaultTableProperty(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Default table properties.'
    _iid_ = GUID('{4657D94F-5FFB-11D3-9F6C-00C04F6BC886}')
    _idlflags_ = ['oleautomation', 'hidden']
IDefaultTableProperty._methods_ = [
    COMMETHOD(['propget', helpstring(u'Selection color use to highlight rows.')], HRESULT, 'SelectionColor',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IColor)), 'ppSelectionColor' )),
    COMMETHOD(['propputref', helpstring(u'Selection color use to highlight rows.')], HRESULT, 'SelectionColor',
              ( ['in'], POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IColor), 'ppSelectionColor' )),
]
################################################################
## code template for IDefaultTableProperty implementation
##class IDefaultTableProperty_Impl(object):
##    def SelectionColor(self, ppSelectionColor):
##        u'Selection color use to highlight rows.'
##        #return 
##

class Library(object):
    u'Esri GeoDatabaseUI Object Library 10.2'
    name = u'esriGeoDatabaseUI'
    _reg_typelib_ = ('{4A9C9ED7-F7DB-4614-B480-A5D265C961FC}', 10, 2)

class ITableCharacteristics(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the characteristics of a Table.'
    _iid_ = GUID('{BB16FF23-F083-4191-B921-6291CA3B512F}')
    _idlflags_ = ['oleautomation']
ITableCharacteristics._methods_ = [
    COMMETHOD(['propget', helpstring(u'Table font.')], HRESULT, 'HeadingFont',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IFontDisp)), 'ppFont' )),
    COMMETHOD(['propget', helpstring(u'Table font.')], HRESULT, 'CellFont',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IFontDisp)), 'ppFont' )),
    COMMETHOD(['propget', helpstring(u'Text color use in table window.')], HRESULT, 'HeadingTextColor',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IColor)), 'ppTextColor' )),
    COMMETHOD(['propget', helpstring(u'Text color use in table window.')], HRESULT, 'CellTextColor',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IColor)), 'ppTextColor' )),
    COMMETHOD(['propget', helpstring(u'Character placed to the right of the field name when a field is indexed.')], HRESULT, 'IndexFieldCharacter',
              ( ['retval', 'out'], POINTER(BSTR), 'pIndexChar' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether table window should show field index character.')], HRESULT, 'ShowIndexFieldCharacter',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pShowIndexCharacter' )),
    COMMETHOD(['propputref', helpstring(u'Table font.')], HRESULT, 'HeadingFont',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IFontDisp), 'ppFont' )),
    COMMETHOD(['propputref', helpstring(u'Table font.')], HRESULT, 'CellFont',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IFontDisp), 'ppFont' )),
    COMMETHOD(['propputref', helpstring(u'Text color use in table window.')], HRESULT, 'HeadingTextColor',
              ( ['in'], POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IColor), 'ppTextColor' )),
    COMMETHOD(['propputref', helpstring(u'Text color use in table window.')], HRESULT, 'CellTextColor',
              ( ['in'], POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IColor), 'ppTextColor' )),
    COMMETHOD(['propput', helpstring(u'Character placed to the right of the field name when a field is indexed.')], HRESULT, 'IndexFieldCharacter',
              ( ['in'], BSTR, 'pIndexChar' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether table window should show field index character.')], HRESULT, 'ShowIndexFieldCharacter',
              ( ['in'], VARIANT_BOOL, 'pShowIndexCharacter' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the table window should validate any changes to the data during editing.')], HRESULT, 'AutoValidateEdits',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'AutoValidateEdits' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the table window should validate any changes to the data during editing.')], HRESULT, 'AutoValidateEdits',
              ( ['in'], VARIANT_BOOL, 'AutoValidateEdits' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the table window shows coded value domain descriptions or values.')], HRESULT, 'ShowCodedValueDomainDescriptions',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ShowCodedValueDomainDescriptions' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the table window shows coded value domain descriptions or values.')], HRESULT, 'ShowCodedValueDomainDescriptions',
              ( ['in'], VARIANT_BOOL, 'ShowCodedValueDomainDescriptions' )),
]
################################################################
## code template for ITableCharacteristics implementation
##class ITableCharacteristics_Impl(object):
##    def HeadingTextColor(self, ppTextColor):
##        u'Text color use in table window.'
##        #return 
##
##    def CellTextColor(self, ppTextColor):
##        u'Text color use in table window.'
##        #return 
##
##    def _get(self):
##        u'Indicates if the table window shows coded value domain descriptions or values.'
##        #return ShowCodedValueDomainDescriptions
##    def _set(self, ShowCodedValueDomainDescriptions):
##        u'Indicates if the table window shows coded value domain descriptions or values.'
##    ShowCodedValueDomainDescriptions = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether table window should show field index character.'
##        #return pShowIndexCharacter
##    def _set(self, pShowIndexCharacter):
##        u'Indicates whether table window should show field index character.'
##    ShowIndexFieldCharacter = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the table window should validate any changes to the data during editing.'
##        #return AutoValidateEdits
##    def _set(self, AutoValidateEdits):
##        u'Indicates if the table window should validate any changes to the data during editing.'
##    AutoValidateEdits = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Character placed to the right of the field name when a field is indexed.'
##        #return pIndexChar
##    def _set(self, pIndexChar):
##        u'Character placed to the right of the field name when a field is indexed.'
##    IndexFieldCharacter = property(_get, _set, doc = _set.__doc__)
##
##    def CellFont(self, ppFont):
##        u'Table font.'
##        #return 
##
##    def HeadingFont(self, ppFont):
##        u'Table font.'
##        #return 
##

IQueryPropertyPage._methods_ = [
    COMMETHOD(['propput', helpstring(u'The query name (optional).')], HRESULT, 'ExpressionLabel',
              ( ['in'], BSTR, 'rhs' )),
    COMMETHOD(['propputref', helpstring(u'The query table. A null value resets this option.')], HRESULT, 'Table',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable), 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Default expression.')], HRESULT, 'Expression',
              ( ['in'], BSTR, 'rhs' )),
    COMMETHOD(['propget', helpstring(u'Provide a QueryFilter after form has been executed.')], HRESULT, 'QueryFilter',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IQueryFilter)), 'ppQueryFilter' )),
    COMMETHOD(['propputref', helpstring(u'The call back routine.')], HRESULT, 'Callback',
              ( ['in'], POINTER(ITableDataCallback), 'rhs' )),
]
################################################################
## code template for IQueryPropertyPage implementation
##class IQueryPropertyPage_Impl(object):
##    def Table(self, rhs):
##        u'The query table. A null value resets this option.'
##        #return 
##
##    def _set(self, rhs):
##        u'Default expression.'
##    Expression = property(fset = _set, doc = _set.__doc__)
##
##    @property
##    def QueryFilter(self):
##        u'Provide a QueryFilter after form has been executed.'
##        #return ppQueryFilter
##
##    def Callback(self, rhs):
##        u'The call back routine.'
##        #return 
##
##    def _set(self, rhs):
##        u'The query name (optional).'
##    ExpressionLabel = property(fset = _set, doc = _set.__doc__)
##

class GNConnectivityRulesPropPage(CoClass):
    u'Esri GeometricNetwork ConnectivityRules property page.'
    _reg_clsid_ = GUID('{750D8193-E0B5-11D2-99BF-0000F80372B4}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{4A9C9ED7-F7DB-4614-B480-A5D265C961FC}', 10, 2)
GNConnectivityRulesPropPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

IVersionManagerEvents._methods_ = [
    COMMETHOD([helpstring(u'Called when a version is renamed.')], HRESULT, 'OnVersionRenamed',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IVersion), 'vers' )),
    COMMETHOD([helpstring(u'Called when a version is deleted.')], HRESULT, 'OnVersionDeleted',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IVersion), 'vers' )),
    COMMETHOD([helpstring(u'Called when a version is created.')], HRESULT, 'OnVersionCreated',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IVersion), 'vers' )),
]
################################################################
## code template for IVersionManagerEvents implementation
##class IVersionManagerEvents_Impl(object):
##    def OnVersionDeleted(self, vers):
##        u'Called when a version is deleted.'
##        #return 
##
##    def OnVersionRenamed(self, vers):
##        u'Called when a version is renamed.'
##        #return 
##
##    def OnVersionCreated(self, vers):
##        u'Called when a version is created.'
##        #return 
##

class GNNamePropPage(CoClass):
    u'Esri GeometricNetwork Name property page.'
    _reg_clsid_ = GUID('{750D8192-E0B5-11D2-99BF-0000F80372B4}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{4A9C9ED7-F7DB-4614-B480-A5D265C961FC}', 10, 2)
GNNamePropPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

__all__ = ['esriTVRowInsAfterGivenOIDAutoAdv',
           'esriTVOptionCreateReport', 'esriCalculatorErrorType',
           'esriTVOptionShowAddFieldWindow', 'ITableView',
           'esriExportTableOptions',
           'esriTVOptionShowMakeGraphWindow', 'esriTableViewOptions',
           'esriTVOptionCreateCrystalReport',
           'esriTVOptionAliasNameToggle', 'GNWeightsPropPage',
           'esriTVOptionShowAppearanceWindow', 'ITableView3',
           'ITableView2', 'esriTVRowInsBeginningOfWin', 'ITableView4',
           'PrivilegesDialog', 'esriTVOptionSwitchSelection',
           'ITableViewInfo', 'esriTableSelectionActions',
           'esriTVOptionShowExportTableWindow',
           'esriCalculatorErrorPutValue', 'ITableDataCallback',
           'esriTVOptionAutoResizeColumns', 'CalculatorUI',
           'esriTVOptionReloadCache', 'ITableSelectionColor',
           'ExportOperation', 'VersioningGeneralPropertyPage',
           'ITableControl2', 'esriCalculatorErrorCode',
           'ITableViewEvents', 'IQueryPropertyPage2',
           'esriTVOptionUnHideAllColumns',
           'esriTVRowInsBeforeGivenOID', 'IHistoricalMarkerManager',
           'esriTVOptionResetFieldOrder', 'esriSelectFeatures',
           'ITableViewCallback', 'NewVersionDialog',
           'IQueryPropertyPageFieldInfo', 'ICalculatorUIJoinSettings',
           'ITableControlInfo', 'esriTVOptionPrintTable',
           'ITableControl3', 'ITableControlWidth', 'TableView',
           'TableViewEventsHelper', 'Calculator', 'esriDrawFeatures',
           'IExportOperation', 'esriNoAction',
           'GNConnectivityRulesPropPage', 'IGdbAdminWindowFactory',
           'esriTVOptionNoOptionSelected',
           'GDBConnectionsPropertyPage', 'ICalculatorUI',
           'esriCalculatorErrorParse', 'VersionManager',
           'IGPQueryPropertyPage', 'ITableCalculator',
           'esriExportSelectedRecords',
           'esriTVOptionShowFindReplaceWindow', 'QueryPropertyPage',
           'IQueryPropertyPage', 'esriTVOptionSelectAll',
           'ITableViewTableFields', 'INewVersionDialog',
           'esriTVRowInsAfterGivenOID', 'esriTVRowInsEndOfWin',
           'esriCalculatorErrorEmptyVal', 'ITableControl',
           'esriExportAllRecords', 'esriTVOptionUnselectAll',
           'esriTVOptionTableProperties', 'ICalculatorCallback',
           'IPrivilegesDialog', 'esriTVRowInsertPlacement',
           'esriCalculatorErrorStore', 'esriSelectCurrentRow',
           'ITableDataCallback2', 'GNNamePropPage',
           'GdbAdminWindowFactory', 'ICalculator',
           'IVersionManagerEvents', 'esriTVOptionAddTableToLayout',
           'esriCalculatorErrorNoScript', 'ITableViewContextMenus',
           'ITableCharacteristics', 'IVersionManager',
           'HistoricalMarkerManager', 'IDefaultTableProperty',
           'esriCalculatorErrorAllEmptyVal',
           'esriExportFeaturesWithinExtent', 'ITableViewOutput',
           'ICalculatorUI2', 'IProtectNameGeoDatabaseUI',
           'CalculatorCallback', 'IChangeVersionDialog',
           'IGPCalculatorUI', 'esriTVOptionShowSQLWindow']
from comtypes import _check_version; _check_version('501')

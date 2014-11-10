# -*- coding: mbcs -*-
typelib_path = u'C:\\Program Files (x86)\\ArcGIS\\Engine10.2\\com\\esriSystemUI.olb'
_lcid = 0 # change this if required
from ctypes import *
import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0
from comtypes import GUID
from comtypes import BSTR
from ctypes import HRESULT
from comtypes.automation import IDispatch
import comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2
from ctypes.wintypes import VARIANT_BOOL
from comtypes import helpstring
from comtypes import COMMETHOD
from comtypes import dispid
from comtypes import CoClass
from comtypes.automation import VARIANT
from comtypes import IUnknown
from comtypes.automation import VARIANT


class IMultiItem(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that define a multiItem.'
    _iid_ = GUID('{AF948931-11D1-11D2-94B4-080009EEBECB}')
    _idlflags_ = ['oleautomation']
IMultiItem._methods_ = [
    COMMETHOD(['propget', helpstring(u'The name of the multiItem.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'The caption of the multiItem.')], HRESULT, 'Caption',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'The status bar message for all items on the multiItem.')], HRESULT, 'Message',
              ( ['retval', 'out'], POINTER(BSTR), 'Message' )),
    COMMETHOD(['propget', helpstring(u'The name of the help file associated with this multiItem.')], HRESULT, 'HelpFile',
              ( ['retval', 'out'], POINTER(BSTR), 'HelpFile' )),
    COMMETHOD(['propget', helpstring(u'The help context ID associated with this multiItem.')], HRESULT, 'HelpContextID',
              ( ['retval', 'out'], POINTER(c_int), 'ID' )),
    COMMETHOD([helpstring(u'Occurs when the menu that contains the multiItem is about to be displayed.')], HRESULT, 'OnPopup',
              ( ['in'], POINTER(IDispatch), 'Hook' ),
              ( ['retval', 'out'], POINTER(c_int), 'ItemCount' )),
    COMMETHOD(['propget', helpstring(u'The caption of the item at the specified index.')], HRESULT, 'ItemCaption',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'itemName' )),
    COMMETHOD(['propget', helpstring(u'The bitmap for the item at the specified index.')], HRESULT, 'ItemBitmap',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'Bitmap' )),
    COMMETHOD([helpstring(u'Occurs when the item at the specified index is clicked.')], HRESULT, 'OnItemClick',
              ( ['in'], c_int, 'index' )),
    COMMETHOD(['propget', helpstring(u'Indicates if item at the specified index is checked.')], HRESULT, 'ItemChecked',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bChecked' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the item at the specified index is enabled.')], HRESULT, 'ItemEnabled',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bEnabled' )),
]
################################################################
## code template for IMultiItem implementation
##class IMultiItem_Impl(object):
##    @property
##    def Name(self):
##        u'The name of the multiItem.'
##        #return Name
##
##    @property
##    def ItemBitmap(self, index):
##        u'The bitmap for the item at the specified index.'
##        #return Bitmap
##
##    @property
##    def ItemEnabled(self, index):
##        u'Indicates if the item at the specified index is enabled.'
##        #return bEnabled
##
##    @property
##    def HelpContextID(self):
##        u'The help context ID associated with this multiItem.'
##        #return ID
##
##    @property
##    def Caption(self):
##        u'The caption of the multiItem.'
##        #return Name
##
##    @property
##    def ItemChecked(self, index):
##        u'Indicates if item at the specified index is checked.'
##        #return bChecked
##
##    def OnPopup(self, Hook):
##        u'Occurs when the menu that contains the multiItem is about to be displayed.'
##        #return ItemCount
##
##    @property
##    def HelpFile(self):
##        u'The name of the help file associated with this multiItem.'
##        #return HelpFile
##
##    @property
##    def Message(self):
##        u'The status bar message for all items on the multiItem.'
##        #return Message
##
##    def OnItemClick(self, index):
##        u'Occurs when the item at the specified index is clicked.'
##        #return 
##
##    @property
##    def ItemCaption(self, index):
##        u'The caption of the item at the specified index.'
##        #return itemName
##

class ICommandSubType(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that define a subtyped command.'
    _iid_ = GUID('{5A141A5B-D096-11D1-B9A9-080009EE4E51}')
    _idlflags_ = ['oleautomation']
ICommandSubType._methods_ = [
    COMMETHOD([helpstring(u'The subtype of the command.')], HRESULT, 'SetSubType',
              ( ['in'], c_int, 'SubType' )),
    COMMETHOD([helpstring(u'The number of commands defined with this CLSID.')], HRESULT, 'GetCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
]
################################################################
## code template for ICommandSubType implementation
##class ICommandSubType_Impl(object):
##    def GetCount(self):
##        u'The number of commands defined with this CLSID.'
##        #return Count
##
##    def SetSubType(self, SubType):
##        u'The subtype of the command.'
##        #return 
##

class IComponentTip(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u"Provides a tip for a component that is displayed by the What's This Help tool."
    _iid_ = GUID('{FD86ED38-01C7-4A41-A72C-5502031AA216}')
    _idlflags_ = ['oleautomation']
IComponentTip._methods_ = [
    COMMETHOD(['propget', helpstring(u'The heading for the tip.')], HRESULT, 'Heading',
              ( ['retval', 'out'], POINTER(BSTR), 'Heading' )),
    COMMETHOD(['propget', helpstring(u'The main body of the tip.')], HRESULT, 'Tip',
              ( ['retval', 'out'], POINTER(BSTR), 'Tip' )),
    COMMETHOD(['propget', helpstring(u'The image for the tip.')], HRESULT, 'Image',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'Image' )),
]
################################################################
## code template for IComponentTip implementation
##class IComponentTip_Impl(object):
##    @property
##    def Image(self):
##        u'The image for the tip.'
##        #return Image
##
##    @property
##    def Tip(self):
##        u'The main body of the tip.'
##        #return Tip
##
##    @property
##    def Heading(self):
##        u'The heading for the tip.'
##        #return Heading
##

class IOperationStack(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Operation Stack.'
    _iid_ = GUID('{303EE675-3087-11D2-94C9-080009EEBECB}')
    _idlflags_ = ['oleautomation']
class IOperation(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control Operations.'
    _iid_ = GUID('{80A807AB-7BB9-11D0-87EC-080009EC732A}')
    _idlflags_ = ['oleautomation']
IOperationStack._methods_ = [
    COMMETHOD(['propget', helpstring(u'The number of operations on the stack.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'The operation at the specified index.')], HRESULT, 'Item',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IOperation)), 'operation' )),
    COMMETHOD([helpstring(u'Removes all operations from the stack.')], HRESULT, 'Reset'),
    COMMETHOD([helpstring(u'Performs the given operation and places it on the stack.')], HRESULT, 'Do',
              ( ['in'], POINTER(IOperation), 'operation' )),
    COMMETHOD([helpstring(u'Undoes the previous operation on the stack.')], HRESULT, 'Undo'),
    COMMETHOD([helpstring(u'Redoes the next operation on the stack.')], HRESULT, 'Redo'),
    COMMETHOD(['hidden', helpstring(u'Undoes a specified operation.'), 'propget'], HRESULT, 'UndoOperation',
              ( ['retval', 'out'], POINTER(POINTER(IOperation)), 'operation' )),
    COMMETHOD(['hidden', helpstring(u'Redoes a specified operation.'), 'propget'], HRESULT, 'RedoOperation',
              ( ['retval', 'out'], POINTER(POINTER(IOperation)), 'operation' )),
    COMMETHOD([helpstring(u'Removes an operation from the stack.')], HRESULT, 'Remove',
              ( ['in'], c_int, 'index' )),
]
################################################################
## code template for IOperationStack implementation
##class IOperationStack_Impl(object):
##    @property
##    def Count(self):
##        u'The number of operations on the stack.'
##        #return Count
##
##    def Reset(self):
##        u'Removes all operations from the stack.'
##        #return 
##
##    def Do(self, operation):
##        u'Performs the given operation and places it on the stack.'
##        #return 
##
##    @property
##    def UndoOperation(self):
##        u'Undoes a specified operation.'
##        #return operation
##
##    def Undo(self):
##        u'Undoes the previous operation on the stack.'
##        #return 
##
##    @property
##    def Item(self, index):
##        u'The operation at the specified index.'
##        #return operation
##
##    def Remove(self, index):
##        u'Removes an operation from the stack.'
##        #return 
##
##    @property
##    def RedoOperation(self):
##        u'Redoes a specified operation.'
##        #return operation
##
##    def Redo(self):
##        u'Redoes the next operation on the stack.'
##        #return 
##

class ControlsOperationStack(CoClass):
    u'Use this class to provide operation support to the ToolbarControl.'
    _reg_clsid_ = GUID('{05E57ADB-7785-4D48-B982-8255730A41E3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{4ECCA6E2-B16B-4ACA-BD17-E74CAE4C150A}', 10, 2)
ControlsOperationStack._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IOperationStack, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

class IToolControl(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that define a toolcontrol.'
    _iid_ = GUID('{E2287753-940F-11D0-835B-080009B996CC}')
    _idlflags_ = ['oleautomation']
class ICompletionNotify(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to a method that advises the framework that the control user has indicated completion.'
    _iid_ = GUID('{12F412E9-2CBC-11D2-94C8-080009EEBECB}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriCmdBarType'
esriCmdBarTypeToolbar = 0
esriCmdBarTypeMenu = 1
esriCmdBarTypeShortcutMenu = 2
esriCmdBarType = c_int # enum
IToolControl._methods_ = [
    COMMETHOD(['propget', helpstring(u'The handle of the control.')], HRESULT, 'hWnd',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'hWnd' )),
    COMMETHOD([helpstring(u'Occurs when the control gains focus.')], HRESULT, 'OnFocus',
              ( ['in'], POINTER(ICompletionNotify), 'complete' )),
    COMMETHOD([helpstring(u'Indicates if the drag-drop operation is valid.')], HRESULT, 'OnDrop',
              ( ['in'], esriCmdBarType, 'barType' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bValid' )),
]
################################################################
## code template for IToolControl implementation
##class IToolControl_Impl(object):
##    @property
##    def hWnd(self):
##        u'The handle of the control.'
##        #return hWnd
##
##    def OnFocus(self, complete):
##        u'Occurs when the control gains focus.'
##        #return 
##
##    def OnDrop(self, barType):
##        u'Indicates if the drag-drop operation is valid.'
##        #return bValid
##

class DataObjectHelper(CoClass):
    u'Helper class for OLE drag and drop.'
    _reg_clsid_ = GUID('{E0CCBCB1-CD47-11D5-A9E6-00104BB6FC1C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{4ECCA6E2-B16B-4ACA-BD17-E74CAE4C150A}', 10, 2)
class IDataObjectHelper(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members for OLE drag and drop.'
    _iid_ = GUID('{E0CCBCB0-CD47-11D5-A9E6-00104BB6FC1C}')
    _idlflags_ = ['oleautomation']
DataObjectHelper._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDataObjectHelper, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

class ICommandHost(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the ICommandHost Interface.'
    _iid_ = GUID('{14CB3146-6FDD-4B45-8759-0A297A4DAD10}')
    _idlflags_ = ['oleautomation']
ICommandHost._methods_ = [
    COMMETHOD([helpstring(u'The SetCommand method is used to bind a command instance to its host.')], HRESULT, 'SetCommand',
              ( ['in'], POINTER(VARIANT), 'commandInstance' )),
]
################################################################
## code template for ICommandHost implementation
##class ICommandHost_Impl(object):
##    def SetCommand(self, commandInstance):
##        u'The SetCommand method is used to bind a command instance to its host.'
##        #return 
##

class IToolPalette(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Tool palette.'
    _iid_ = GUID('{5678B14A-102B-493F-BADB-1A83AE8A3830}')
    _idlflags_ = ['oleautomation']
IToolPalette._methods_ = [
    COMMETHOD(['propget', helpstring(u'The number of items in this menu.')], HRESULT, 'PaletteItemCount',
              ( ['retval', 'out'], POINTER(c_int), 'numItems' )),
    COMMETHOD(['propget', helpstring(u'The CLSID for the item on this menu at the specified index.')], HRESULT, 'PaletteItem',
              ( ['in'], c_int, 'pos' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ID' )),
    COMMETHOD(['propget', helpstring(u'The Number of Columns to display')], HRESULT, 'PaletteColumns',
              ( ['retval', 'out'], POINTER(c_int), 'columns' )),
    COMMETHOD(['propget', helpstring(u'The menu style')], HRESULT, 'MenuStyle',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'menu' )),
    COMMETHOD(['propget', helpstring(u'The tearoff style')], HRESULT, 'TearOff',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'TearOff' )),
]
################################################################
## code template for IToolPalette implementation
##class IToolPalette_Impl(object):
##    @property
##    def PaletteColumns(self):
##        u'The Number of Columns to display'
##        #return columns
##
##    @property
##    def MenuStyle(self):
##        u'The menu style'
##        #return menu
##
##    @property
##    def PaletteItem(self, pos):
##        u'The CLSID for the item on this menu at the specified index.'
##        #return ID
##
##    @property
##    def TearOff(self):
##        u'The tearoff style'
##        #return TearOff
##
##    @property
##    def PaletteItemCount(self):
##        u'The number of items in this menu.'
##        #return numItems
##

class ISystemMouseCursor(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that load and get mouse cursor.'
    _iid_ = GUID('{623BF41C-3E34-4586-A729-C2E34CBE8FA9}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriSystemMouseCursor'
esriSystemMouseCursorDefault = 0
esriSystemMouseCursorArrow = 1
esriSystemMouseCursorCrosshair = 2
esriSystemMouseCursorIBeam = 3
esriSystemMouseCursorIcon = 4
esriSystemMouseCursorSize = 5
esriSystemMouseCursorSizeNESW = 6
esriSystemMouseCursorSizeNS = 7
esriSystemMouseCursorSizeNWSE = 8
esriSystemMouseCursorSizeWE = 9
esriSystemMouseCursorUpArrow = 10
esriSystemMouseCursorHourglass = 11
esriSystemMouseCursorNoDrop = 12
esriSystemMouseCursorArrowHourglass = 13
esriSystemMouseCursorArrowQuestion = 14
esriSystemMouseCursorSizeAll = 15
esriSystemMouseCursorZoom = 50
esriSystemMouseCursorZoomIn = 51
esriSystemMouseCursorZoomOut = 52
esriSystemMouseCursorPan = 53
esriSystemMouseCursorPanning = 54
esriSystemMouseCursorIdentify = 55
esriSystemMouseCursorLabel = 56
esriSystemMouseCursorHotLink = 57
esriSystemMouseCursorPencil = 58
esriSystemMouseCursorHand = 59
esriSystemMouseCursorPageZoomIn = 60
esriSystemMouseCursorPageZoomOut = 61
esriSystemMouseCursorPagePan = 62
esriSystemMouseCursorPagePanning = 63
esriSystemMouseCursor = c_int # enum
ISystemMouseCursor._methods_ = [
    COMMETHOD([helpstring(u'Loads system provided mouse cursor.')], HRESULT, 'Load',
              ( ['in'], esriSystemMouseCursor, 'mouseCursorType' )),
    COMMETHOD([helpstring(u'Loads mouse cursor from file. If file name uses relative path, the path must be relative to current application executable.')], HRESULT, 'LoadFromFile',
              ( ['in'], BSTR, 'fileName' )),
    COMMETHOD(['propget', helpstring(u'Currently loaded mouse cursor.')], HRESULT, 'Cursor',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'mouseCursor' )),
    COMMETHOD(['propput', helpstring(u'Currently loaded mouse cursor.')], HRESULT, 'Cursor',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'mouseCursor' )),
]
################################################################
## code template for ISystemMouseCursor implementation
##class ISystemMouseCursor_Impl(object):
##    def Load(self, mouseCursorType):
##        u'Loads system provided mouse cursor.'
##        #return 
##
##    def _get(self):
##        u'Currently loaded mouse cursor.'
##        #return mouseCursor
##    def _set(self, mouseCursor):
##        u'Currently loaded mouse cursor.'
##    Cursor = property(_get, _set, doc = _set.__doc__)
##
##    def LoadFromFile(self, fileName):
##        u'Loads mouse cursor from file. If file name uses relative path, the path must be relative to current application executable.'
##        #return 
##

class IComboBoxHook(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Provides methods to program system provided combo boxes.'
    _iid_ = GUID('{457FA6E9-2B50-4335-9990-B321FF228DAF}')
    _idlflags_ = ['dual', 'oleautomation', 'hidden']
IComboBoxHook._methods_ = [
    COMMETHOD([dispid(1610743808), helpstring(u'Get Application hook.'), 'propget'], HRESULT, 'Hook',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'app' )),
    COMMETHOD([dispid(1610743809), helpstring(u'Add an element to the combo box.')], HRESULT, 'Add',
              ( ['in'], BSTR, 'str' ),
              ( ['retval', 'out'], POINTER(c_int), 'cookie' )),
    COMMETHOD([dispid(1610743810), helpstring(u'Remove an element from the combo box.')], HRESULT, 'Remove',
              ( ['in'], c_int, 'cookie' )),
    COMMETHOD([dispid(1610743811), helpstring(u'Set the value for the edit control.'), 'propput'], HRESULT, 'Value',
              ( ['in'], BSTR, 'Value' )),
    COMMETHOD([dispid(1610743811), helpstring(u'Set the value for the edit control.'), 'propget'], HRESULT, 'Value',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(1610743813), helpstring(u'Clear the combo box of all items.')], HRESULT, 'Clear'),
    COMMETHOD([dispid(1610743814), helpstring(u'Select an Item in the combo box.')], HRESULT, 'Select',
              ( ['in'], c_int, 'cookie' )),
    COMMETHOD([dispid(1610743815), helpstring(u'GetThe currently selected item in the combo box.'), 'propget'], HRESULT, 'Selected',
              ( ['retval', 'out'], POINTER(c_int), 'cookie' )),
]
################################################################
## code template for IComboBoxHook implementation
##class IComboBoxHook_Impl(object):
##    def Clear(self):
##        u'Clear the combo box of all items.'
##        #return 
##
##    @property
##    def Selected(self):
##        u'GetThe currently selected item in the combo box.'
##        #return cookie
##
##    def _get(self):
##        u'Set the value for the edit control.'
##        #return Value
##    def _set(self, Value):
##        u'Set the value for the edit control.'
##    Value = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Hook(self):
##        u'Get Application hook.'
##        #return app
##
##    def Add(self, str):
##        u'Add an element to the combo box.'
##        #return cookie
##
##    def Remove(self, cookie):
##        u'Remove an element from the combo box.'
##        #return 
##
##    def Select(self, cookie):
##        u'Select an Item in the combo box.'
##        #return 
##

class CommandHost(CoClass):
    u'Use this class to host C++ command implementations in a Toolbar.'
    _reg_clsid_ = GUID('{A318A696-3ED1-4775-A922-147E8C36D79D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{4ECCA6E2-B16B-4ACA-BD17-E74CAE4C150A}', 10, 2)
class ICommand(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that define a COM command.'
    _iid_ = GUID('{36B06538-4437-11D1-B970-080009EE4E51}')
    _idlflags_ = ['oleautomation']
CommandHost._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ICommandHost, ICommand]

class IProgressDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that work with a progress dialog.'
    _iid_ = GUID('{923A1B5A-90E5-4D23-ADD8-ECA3D7D6B1C8}')
    _idlflags_ = ['oleautomation']
IProgressDialog._methods_ = [
    COMMETHOD([helpstring(u'Shows the progress dialog.')], HRESULT, 'ShowDialog'),
    COMMETHOD([helpstring(u'Hides the progress dialog.')], HRESULT, 'HideDialog'),
    COMMETHOD(['propget', helpstring(u'Indicates if the cancel button is enabled.')], HRESULT, 'CancelEnabled',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bVal' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the cancel button is enabled.')], HRESULT, 'CancelEnabled',
              ( ['in'], VARIANT_BOOL, 'bVal' )),
]
################################################################
## code template for IProgressDialog implementation
##class IProgressDialog_Impl(object):
##    def _get(self):
##        u'Indicates if the cancel button is enabled.'
##        #return bVal
##    def _set(self, bVal):
##        u'Indicates if the cancel button is enabled.'
##    CancelEnabled = property(_get, _set, doc = _set.__doc__)
##
##    def HideDialog(self):
##        u'Hides the progress dialog.'
##        #return 
##
##    def ShowDialog(self):
##        u'Shows the progress dialog.'
##        #return 
##

class ITool(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that define a tool.'
    _iid_ = GUID('{2A6B0172-4ED2-11D0-98BE-00805F7CED21}')
    _idlflags_ = ['oleautomation']
ITool._methods_ = [
    COMMETHOD(['propget', helpstring(u'The mouse pointer for this tool.')], HRESULT, 'Cursor',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'Cursor' )),
    COMMETHOD([helpstring(u'Occurs when a mouse button is pressed when this tool is active.')], HRESULT, 'OnMouseDown',
              ( ['in'], c_int, 'button' ),
              ( ['in'], c_int, 'shift' ),
              ( ['in'], c_int, 'x' ),
              ( ['in'], c_int, 'y' )),
    COMMETHOD([helpstring(u'Occurs when the mouse is moved when this tool is active.')], HRESULT, 'OnMouseMove',
              ( ['in'], c_int, 'button' ),
              ( ['in'], c_int, 'shift' ),
              ( ['in'], c_int, 'x' ),
              ( ['in'], c_int, 'y' )),
    COMMETHOD([helpstring(u'Occurs when a mouse button is released when this tool is active.')], HRESULT, 'OnMouseUp',
              ( ['in'], c_int, 'button' ),
              ( ['in'], c_int, 'shift' ),
              ( ['in'], c_int, 'x' ),
              ( ['in'], c_int, 'y' )),
    COMMETHOD([helpstring(u'Occurs when a mouse button is double clicked when this tool is active.')], HRESULT, 'OnDblClick'),
    COMMETHOD([helpstring(u'Occurs when a key on the keyboard is pressed when this tool is active.')], HRESULT, 'OnKeyDown',
              ( ['in'], c_int, 'keyCode' ),
              ( ['in'], c_int, 'shift' )),
    COMMETHOD([helpstring(u'Occurs when a key on the keyboard is released when this tool is active.')], HRESULT, 'OnKeyUp',
              ( ['in'], c_int, 'keyCode' ),
              ( ['in'], c_int, 'shift' )),
    COMMETHOD([helpstring(u'Context menu event occured at the given xy location.')], HRESULT, 'OnContextMenu',
              ( ['in'], c_int, 'x' ),
              ( ['in'], c_int, 'y' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'handled' )),
    COMMETHOD([helpstring(u'Occurs when a screen display in the application is refreshed.')], HRESULT, 'Refresh',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hdc' )),
    COMMETHOD([helpstring(u'Causes the tool to no longer be the active tool.')], HRESULT, 'Deactivate',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'complete' )),
]
################################################################
## code template for ITool implementation
##class ITool_Impl(object):
##    def OnContextMenu(self, x, y):
##        u'Context menu event occured at the given xy location.'
##        #return handled
##
##    def Deactivate(self):
##        u'Causes the tool to no longer be the active tool.'
##        #return complete
##
##    def OnKeyDown(self, keyCode, shift):
##        u'Occurs when a key on the keyboard is pressed when this tool is active.'
##        #return 
##
##    def Refresh(self, hdc):
##        u'Occurs when a screen display in the application is refreshed.'
##        #return 
##
##    def OnMouseDown(self, button, shift, x, y):
##        u'Occurs when a mouse button is pressed when this tool is active.'
##        #return 
##
##    @property
##    def Cursor(self):
##        u'The mouse pointer for this tool.'
##        #return Cursor
##
##    def OnMouseMove(self, button, shift, x, y):
##        u'Occurs when the mouse is moved when this tool is active.'
##        #return 
##
##    def OnMouseUp(self, button, shift, x, y):
##        u'Occurs when a mouse button is released when this tool is active.'
##        #return 
##
##    def OnKeyUp(self, keyCode, shift):
##        u'Occurs when a key on the keyboard is released when this tool is active.'
##        #return 
##
##    def OnDblClick(self):
##        u'Occurs when a mouse button is double clicked when this tool is active.'
##        #return 
##

class IToolBarDef(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that define a toolbar.'
    _iid_ = GUID('{61B318F0-CDA0-11D1-B9A8-080009EE4E51}')
    _idlflags_ = ['oleautomation']
class IItemDef(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that define an item on a commandbar.'
    _iid_ = GUID('{857336BF-E12B-11D1-9495-080009EEBECB}')
    _idlflags_ = ['oleautomation']
IToolBarDef._methods_ = [
    COMMETHOD(['propget', helpstring(u'The number of items in this toolbar.')], HRESULT, 'ItemCount',
              ( ['retval', 'out'], POINTER(c_int), 'numItems' )),
    COMMETHOD([helpstring(u'The CLSID for the item on this toolbar at the specified index.')], HRESULT, 'GetItemInfo',
              ( ['in'], c_int, 'pos' ),
              ( ['in'], POINTER(IItemDef), 'itemDef' )),
    COMMETHOD(['propget', helpstring(u'The name of this toolbar.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'The caption of this toolbar.')], HRESULT, 'Caption',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
]
################################################################
## code template for IToolBarDef implementation
##class IToolBarDef_Impl(object):
##    @property
##    def Caption(self):
##        u'The caption of this toolbar.'
##        #return Name
##
##    @property
##    def ItemCount(self):
##        u'The number of items in this toolbar.'
##        #return numItems
##
##    @property
##    def Name(self):
##        u'The name of this toolbar.'
##        #return Name
##
##    def GetItemInfo(self, pos, itemDef):
##        u'The CLSID for the item on this toolbar at the specified index.'
##        #return 
##

class IMultiItemEx(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that define a multiItem with extended features.'
    _iid_ = GUID('{1E29F387-F77A-42CC-AD58-5FB1F5F8E11D}')
    _idlflags_ = ['oleautomation']
IMultiItemEx._methods_ = [
    COMMETHOD(['propget', helpstring(u'The status bar message for the item specified by the index.')], HRESULT, 'ItemMessage',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Message' )),
    COMMETHOD(['propget', helpstring(u'The name of the help file associated with the item specified by the index.')], HRESULT, 'ItemHelpFile',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'HelpFile' )),
    COMMETHOD(['propget', helpstring(u'The help context ID associated with the item specified by the index.')], HRESULT, 'ItemHelpContextID',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(c_int), 'ID' )),
]
################################################################
## code template for IMultiItemEx implementation
##class IMultiItemEx_Impl(object):
##    @property
##    def ItemMessage(self, index):
##        u'The status bar message for the item specified by the index.'
##        #return Message
##
##    @property
##    def ItemHelpFile(self, index):
##        u'The name of the help file associated with the item specified by the index.'
##        #return HelpFile
##
##    @property
##    def ItemHelpContextID(self, index):
##        u'The help context ID associated with the item specified by the index.'
##        #return ID
##


# values for enumeration 'esriTipStyle'
esriTipStyleSolid = 0
esriTipStyleTransparent = 1
esriTipStyle = c_int # enum
ICommand._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if this command is enabled.')], HRESULT, 'Enabled',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Enabled' )),
    COMMETHOD(['propget', helpstring(u'Indicates if this command is checked.')], HRESULT, 'Checked',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Checked' )),
    COMMETHOD(['propget', helpstring(u'The name of this commmand.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'The caption of this command.')], HRESULT, 'Caption',
              ( ['retval', 'out'], POINTER(BSTR), 'Caption' )),
    COMMETHOD(['propget', helpstring(u'The tooltip for this command.')], HRESULT, 'Tooltip',
              ( ['retval', 'out'], POINTER(BSTR), 'Tooltip' )),
    COMMETHOD(['propget', helpstring(u'The statusbar message for this command.')], HRESULT, 'Message',
              ( ['retval', 'out'], POINTER(BSTR), 'Message' )),
    COMMETHOD(['propget', helpstring(u'The name of the help file associated with this command.')], HRESULT, 'HelpFile',
              ( ['retval', 'out'], POINTER(BSTR), 'HelpFile' )),
    COMMETHOD(['propget', helpstring(u'The help context ID associated with this command.')], HRESULT, 'HelpContextID',
              ( ['retval', 'out'], POINTER(c_int), 'helpID' )),
    COMMETHOD(['propget', helpstring(u'The bitmap that is used as the icon on this command.')], HRESULT, 'Bitmap',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'Bitmap' )),
    COMMETHOD(['propget', helpstring(u'The name of the category with which this command is associated.')], HRESULT, 'Category',
              ( ['retval', 'out'], POINTER(BSTR), 'categoryName' )),
    COMMETHOD([helpstring(u'Occurs when this command is created.')], HRESULT, 'OnCreate',
              ( ['in'], POINTER(IDispatch), 'Hook' )),
    COMMETHOD([helpstring(u'Occurs when this command is clicked.')], HRESULT, 'OnClick'),
]
################################################################
## code template for ICommand implementation
##class ICommand_Impl(object):
##    @property
##    def Category(self):
##        u'The name of the category with which this command is associated.'
##        #return categoryName
##
##    @property
##    def Checked(self):
##        u'Indicates if this command is checked.'
##        #return Checked
##
##    @property
##    def Name(self):
##        u'The name of this commmand.'
##        #return Name
##
##    @property
##    def Enabled(self):
##        u'Indicates if this command is enabled.'
##        #return Enabled
##
##    @property
##    def Tooltip(self):
##        u'The tooltip for this command.'
##        #return Tooltip
##
##    @property
##    def Bitmap(self):
##        u'The bitmap that is used as the icon on this command.'
##        #return Bitmap
##
##    @property
##    def HelpContextID(self):
##        u'The help context ID associated with this command.'
##        #return helpID
##
##    @property
##    def Caption(self):
##        u'The caption of this command.'
##        #return Caption
##
##    def OnClick(self):
##        u'Occurs when this command is clicked.'
##        #return 
##
##    @property
##    def HelpFile(self):
##        u'The name of the help file associated with this command.'
##        #return HelpFile
##
##    @property
##    def Message(self):
##        u'The statusbar message for this command.'
##        #return Message
##
##    def OnCreate(self, Hook):
##        u'Occurs when this command is created.'
##        #return 
##

class ToolHost(CoClass):
    u'Use this class to host pure C++ tool implementations in a Toolbar.'
    _reg_clsid_ = GUID('{60598C68-56CA-4A38-A2D4-328CB74DC665}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{4ECCA6E2-B16B-4ACA-BD17-E74CAE4C150A}', 10, 2)
ToolHost._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ICommandHost, ICommand, ITool]

class IComboBox(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that define a COM combo box.'
    _iid_ = GUID('{B3CF6F42-40B5-42C4-8714-0B6FD2DE8C85}')
    _idlflags_ = ['oleautomation']
IComboBox._methods_ = [
    COMMETHOD(['propget', helpstring(u'Is the combo box editable?')], HRESULT, 'Editable',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Editable' )),
    COMMETHOD(['propget', helpstring(u"The Combo box's width")], HRESULT, 'Width',
              ( ['retval', 'out'], POINTER(BSTR), 'stringForWidth' )),
    COMMETHOD(['propget', helpstring(u"The Combo box's drop down width")], HRESULT, 'DropDownWidth',
              ( ['retval', 'out'], POINTER(BSTR), 'stringForWidth' )),
    COMMETHOD(['propget', helpstring(u"The Combo box's drop down height")], HRESULT, 'DropDownHeight',
              ( ['retval', 'out'], POINTER(c_int), 'rowsHigh' )),
    COMMETHOD(['propget', helpstring(u'Set the hint displayed in the editbox.')], HRESULT, 'HintText',
              ( ['retval', 'out'], POINTER(BSTR), 'HintText' )),
    COMMETHOD([helpstring(u'Called by system when a selection changes')], HRESULT, 'OnSelChange',
              ( ['in'], c_int, 'cookie' )),
    COMMETHOD([helpstring(u'Called by system when the edit box is typed into (if editable)')], HRESULT, 'OnEditChange',
              ( ['in'], BSTR, 'editString' )),
    COMMETHOD([helpstring(u'Called by system when the gets or loses focus')], HRESULT, 'OnFocus',
              ( [], VARIANT_BOOL, 'set' )),
    COMMETHOD([helpstring(u'Called by system when an <enter> key is pressed in the edit box (if editable)')], HRESULT, 'OnEnter'),
    COMMETHOD(['propget', helpstring(u'Indicates if the caption is shown when this combo box is placed on toolbar.')], HRESULT, 'ShowCaption',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ShowCaption' )),
]
################################################################
## code template for IComboBox implementation
##class IComboBox_Impl(object):
##    @property
##    def DropDownHeight(self):
##        u"The Combo box's drop down height"
##        #return rowsHigh
##
##    def OnEnter(self):
##        u'Called by system when an <enter> key is pressed in the edit box (if editable)'
##        #return 
##
##    def OnEditChange(self, editString):
##        u'Called by system when the edit box is typed into (if editable)'
##        #return 
##
##    @property
##    def Editable(self):
##        u'Is the combo box editable?'
##        #return Editable
##
##    @property
##    def DropDownWidth(self):
##        u"The Combo box's drop down width"
##        #return stringForWidth
##
##    @property
##    def Width(self):
##        u"The Combo box's width"
##        #return stringForWidth
##
##    @property
##    def HintText(self):
##        u'Set the hint displayed in the editbox.'
##        #return HintText
##
##    @property
##    def ShowCaption(self):
##        u'Indicates if the caption is shown when this combo box is placed on toolbar.'
##        #return ShowCaption
##
##    def OnSelChange(self, cookie):
##        u'Called by system when a selection changes'
##        #return 
##
##    def OnFocus(self, set):
##        u'Called by system when the gets or loses focus'
##        #return 
##

IItemDef._methods_ = [
    COMMETHOD(['propput', helpstring(u'The CLSID or PROGID of the item being defined.')], HRESULT, 'ID',
              ( ['in'], BSTR, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the defined item should start a group on the menu or toolbar.')], HRESULT, 'Group',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'The subtype of the item being defined.')], HRESULT, 'SubType',
              ( ['in'], c_int, 'rhs' )),
]
################################################################
## code template for IItemDef implementation
##class IItemDef_Impl(object):
##    def _set(self, rhs):
##        u'The subtype of the item being defined.'
##    SubType = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Indicates if the defined item should start a group on the menu or toolbar.'
##    Group = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'The CLSID or PROGID of the item being defined.'
##    ID = property(fset = _set, doc = _set.__doc__)
##

IOperation._methods_ = [
    COMMETHOD(['propget', helpstring(u'The menu string.')], HRESULT, 'MenuString',
              ( ['retval', 'out'], POINTER(BSTR), 'text' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the operation can be undone.')], HRESULT, 'CanUndo',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'result' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the operation can be redone.')], HRESULT, 'CanRedo',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'result' )),
    COMMETHOD([helpstring(u'Performs the operation.')], HRESULT, 'Do'),
    COMMETHOD([helpstring(u'Undoes the operation.')], HRESULT, 'Undo'),
    COMMETHOD([helpstring(u'Redoes the operation.')], HRESULT, 'Redo'),
]
################################################################
## code template for IOperation implementation
##class IOperation_Impl(object):
##    def Do(self):
##        u'Performs the operation.'
##        #return 
##
##    @property
##    def CanUndo(self):
##        u'Indicates if the operation can be undone.'
##        #return result
##
##    @property
##    def MenuString(self):
##        u'The menu string.'
##        #return text
##
##    def Undo(self):
##        u'Undoes the operation.'
##        #return 
##
##    @property
##    def CanRedo(self):
##        u'Indicates if the operation can be redone.'
##        #return result
##
##    def Redo(self):
##        u'Redoes the operation.'
##        #return 
##


# values for enumeration 'esriArcGISUri'
esriArcGISUriBase = 0
esriArcGISUriSecure = 1
esriArcGISUriUpdate = 2
esriArcGISUriPing = 3
esriArcGISUriSpeed = 4
esriArcGISBasemapQuery = 5
esriArcGISGlobeBasemapQuery = 6
esriArcGISUriForgottenPassword = 7
esriArcGISUriNewAccount = 8
esriArcGISSiteName = 9
esriArcGISUri = c_int # enum
class IMenuDef(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that define a menu.'
    _iid_ = GUID('{58E2C6A1-CD8D-11D1-91A7-0080C718DF97}')
    _idlflags_ = ['oleautomation']
IMenuDef._methods_ = [
    COMMETHOD(['propget', helpstring(u'The number of items in this menu.')], HRESULT, 'ItemCount',
              ( ['retval', 'out'], POINTER(c_int), 'numItems' )),
    COMMETHOD([helpstring(u'The CLSID for the item on this menu at the specified index.')], HRESULT, 'GetItemInfo',
              ( ['in'], c_int, 'pos' ),
              ( ['in'], POINTER(IItemDef), 'itemDef' )),
    COMMETHOD(['propget', helpstring(u'The name of this menu.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'The caption of this menu.')], HRESULT, 'Caption',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
]
################################################################
## code template for IMenuDef implementation
##class IMenuDef_Impl(object):
##    @property
##    def Caption(self):
##        u'The caption of this menu.'
##        #return Name
##
##    @property
##    def ItemCount(self):
##        u'The number of items in this menu.'
##        #return numItems
##
##    @property
##    def Name(self):
##        u'The name of this menu.'
##        #return Name
##
##    def GetItemInfo(self, pos, itemDef):
##        u'The CLSID for the item on this menu at the specified index.'
##        #return 
##

class Library(object):
    u'Esri SystemUI Object Library 10.2'
    name = u'esriSystemUI'
    _reg_typelib_ = ('{4ECCA6E2-B16B-4ACA-BD17-E74CAE4C150A}', 10, 2)


# values for enumeration 'esriKeyIntercept'
esriKeyInterceptNone = 0
esriKeyInterceptArrowKeys = 1
esriKeyInterceptAlt = 2
esriKeyInterceptTab = 4
esriKeyInterceptEnter = 8
esriKeyIntercept = c_int # enum
class ArcGISSingleSignon(CoClass):
    u'An object for working with the ArcGIS Single Sign on system.'
    _reg_clsid_ = GUID('{DAE2351B-241B-426D-A3DA-056839A54743}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{4ECCA6E2-B16B-4ACA-BD17-E74CAE4C150A}', 10, 2)
class IArcGISSingleSignon(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the IArcGISSingleSignon Interface.'
    _iid_ = GUID('{E36DC321-5C5B-4D6B-884E-19FF4B5BBCAC}')
    _idlflags_ = ['oleautomation']
class IArcGISPortal(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the IArcGISPortal Interface.'
    _iid_ = GUID('{A128A18C-6769-4E4F-90A9-DF413D139192}')
    _idlflags_ = ['oleautomation']
ArcGISSingleSignon._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IArcGISSingleSignon, IArcGISPortal]

class IMultiItemSeparator(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Extends multiItem capabalities to support separators.'
    _iid_ = GUID('{5398CEE2-0A8E-4BDF-AF26-77C9AF2EBC63}')
    _idlflags_ = ['oleautomation']
IMultiItemSeparator._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if item has a separator.')], HRESULT, 'Separator',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bSeparator' )),
]
################################################################
## code template for IMultiItemSeparator implementation
##class IMultiItemSeparator_Impl(object):
##    @property
##    def Separator(self, index):
##        u'Indicates if item has a separator.'
##        #return bSeparator
##

class SystemFont(CoClass):
    u'A font object encapsulating Windows font object.'
    _reg_clsid_ = GUID('{F130210C-5478-43DE-8012-1C02DDD97BA1}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{4ECCA6E2-B16B-4ACA-BD17-E74CAE4C150A}', 10, 2)
SystemFont._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.Font, comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IFont]

class IComPropertySheetEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to events that occur on a COM property sheet.'
    _iid_ = GUID('{6B7B57F8-5765-11D0-92D9-00805F7C28B0}')
    _idlflags_ = ['oleautomation']
IComPropertySheetEvents._methods_ = [
    COMMETHOD([helpstring(u'Occurs when changes are applied.')], HRESULT, 'OnApply'),
]
################################################################
## code template for IComPropertySheetEvents implementation
##class IComPropertySheetEvents_Impl(object):
##    def OnApply(self):
##        u'Occurs when changes are applied.'
##        #return 
##

class SystemMouseCursor(CoClass):
    u'A helper object working with mouse cursor.'
    _reg_clsid_ = GUID('{CF0C4485-2091-4E5A-A64C-69E4B802F444}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{4ECCA6E2-B16B-4ACA-BD17-E74CAE4C150A}', 10, 2)
SystemMouseCursor._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ISystemMouseCursor]

IDataObjectHelper._methods_ = [
    COMMETHOD(['propputref', helpstring(u'Provides access to the internal IDataObject pointer.')], HRESULT, 'InternalObject',
              ( ['in'], POINTER(IUnknown), 'ppObject' )),
    COMMETHOD(['propget', helpstring(u'Provides access to the internal IDataObject pointer.')], HRESULT, 'InternalObject',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'ppObject' )),
    COMMETHOD([helpstring(u'If specified DataObject format can be retrieved, returns the data as safe array of bytes.')], HRESULT, 'GetData',
              ( ['in'], c_int, 'format' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'pvData' )),
    COMMETHOD([helpstring(u'Indicates if the DataObject supports the specified format.')], HRESULT, 'GetFormat',
              ( ['in'], c_int, 'format' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbFormatSupported' )),
    COMMETHOD([helpstring(u'Indicates if files are available in the DataObject.')], HRESULT, 'CanGetFiles',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'CanGetFiles' )),
    COMMETHOD([helpstring(u'If the DataObject format supports files, returns a safe array of strings representing filenames.')], HRESULT, 'GetFiles',
              ( ['retval', 'out'], POINTER(VARIANT), 'pvData' )),
    COMMETHOD([helpstring(u'Indicates if Esri names are available in the DataObject.')], HRESULT, 'CanGetNames',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'CanGetNames' )),
    COMMETHOD([helpstring(u'If the DataObject format supports Esri names, returns an enumerator of names.')], HRESULT, 'GetNames',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IEnumName)), 'ppNames' )),
]
################################################################
## code template for IDataObjectHelper implementation
##class IDataObjectHelper_Impl(object):
##    def CanGetFiles(self):
##        u'Indicates if files are available in the DataObject.'
##        #return CanGetFiles
##
##    def GetFiles(self):
##        u'If the DataObject format supports files, returns a safe array of strings representing filenames.'
##        #return pvData
##
##    @property
##    def InternalObject(self, ppObject):
##        u'Provides access to the internal IDataObject pointer.'
##        #return 
##
##    def CanGetNames(self):
##        u'Indicates if Esri names are available in the DataObject.'
##        #return CanGetNames
##
##    def GetNames(self):
##        u'If the DataObject format supports Esri names, returns an enumerator of names.'
##        #return ppNames
##
##    def GetData(self, format):
##        u'If specified DataObject format can be retrieved, returns the data as safe array of bytes.'
##        #return pvData
##
##    def GetFormat(self, format):
##        u'Indicates if the DataObject supports the specified format.'
##        #return pbFormatSupported
##

IArcGISSingleSignon._methods_ = [
    COMMETHOD([helpstring(u'Signs the user in to ArcGIS Online if required, and returns the current token and matching referer.')], HRESULT, 'GetToken',
              ( ['in'], c_int, 'hParentHWND' ),
              ( ['in', 'out'], POINTER(BSTR), 'bsToken' ),
              ( ['in', 'out'], POINTER(BSTR), 'bsReferer' ),
              ( ['in', 'out'], POINTER(c_int), 'lExpiration' ),
              ( ['in', 'out'], POINTER(BSTR), 'bsUser' )),
    COMMETHOD([helpstring(u'Signs the user out of ArcGIS Online.')], HRESULT, 'SignOut'),
    COMMETHOD([helpstring(u'Returns the current token and matching referer.')], HRESULT, 'GetCurrentToken',
              ( ['in', 'out'], POINTER(BSTR), 'bsToken' ),
              ( ['in', 'out'], POINTER(BSTR), 'bsReferer' ),
              ( ['in', 'out'], POINTER(c_int), 'lExpiration' ),
              ( ['in', 'out'], POINTER(BSTR), 'bsUser' )),
    COMMETHOD([helpstring(u'Returns the requested ArcGIS online URI')], HRESULT, 'GetURI',
              ( ['in'], esriArcGISUri, 'eType' ),
              ( ['in', 'out'], POINTER(BSTR), 'bsURI' )),
]
################################################################
## code template for IArcGISSingleSignon implementation
##class IArcGISSingleSignon_Impl(object):
##    def GetToken(self, hParentHWND):
##        u'Signs the user in to ArcGIS Online if required, and returns the current token and matching referer.'
##        #return bsToken, bsReferer, lExpiration, bsUser
##
##    def GetURI(self, eType):
##        u'Returns the requested ArcGIS online URI'
##        #return bsURI
##
##    def GetCurrentToken(self):
##        u'Returns the current token and matching referer.'
##        #return bsToken, bsReferer, lExpiration, bsUser
##
##    def SignOut(self):
##        u'Signs the user out of ArcGIS Online.'
##        #return 
##

class IArcGISSingleSignon2(IArcGISSingleSignon):
    _case_insensitive_ = True
    u'Provides access to the IArcGISSingleSignon2 Interface.'
    _iid_ = GUID('{10EF05C7-241F-4DA0-A623-23EF607E0CAB}')
    _idlflags_ = ['oleautomation']
IArcGISSingleSignon2._methods_ = [
    COMMETHOD([helpstring(u'Returns the Bing token and matching referer.')], HRESULT, 'GetBingToken',
              ( ['in', 'out'], POINTER(BSTR), 'bsToken' ),
              ( ['in', 'out'], POINTER(BSTR), 'bsReferer' ),
              ( ['in', 'out'], POINTER(c_int), 'lExpiration' )),
]
################################################################
## code template for IArcGISSingleSignon2 implementation
##class IArcGISSingleSignon2_Impl(object):
##    def GetBingToken(self):
##        u'Returns the Bing token and matching referer.'
##        #return bsToken, bsReferer, lExpiration
##

class IToolSelectedLayer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that set and get the current selected layer, which selection commands and tools works on.'
    _iid_ = GUID('{FC6732DB-6295-4B39-B257-8C799AE20567}')
    _idlflags_ = ['oleautomation']
IToolSelectedLayer._methods_ = [
    COMMETHOD(['propput', helpstring(u'The index of selected layer.')], HRESULT, 'LayerIndex',
              ( ['in'], c_int, 'LayerIndex' )),
    COMMETHOD(['propget', helpstring(u'The index of selected layer.')], HRESULT, 'LayerIndex',
              ( ['retval', 'out'], POINTER(c_int), 'LayerIndex' )),
]
################################################################
## code template for IToolSelectedLayer implementation
##class IToolSelectedLayer_Impl(object):
##    def _get(self):
##        u'The index of selected layer.'
##        #return LayerIndex
##    def _set(self, LayerIndex):
##        u'The index of selected layer.'
##    LayerIndex = property(_get, _set, doc = _set.__doc__)
##

class IPaletteDef(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that define a ToolbarPalette.'
    _iid_ = GUID('{1DB60DBD-AB2B-4D46-A2EE-F2FA3C5B55FB}')
    _idlflags_ = ['oleautomation']
IPaletteDef._methods_ = [
    COMMETHOD(['propget', helpstring(u'The caption of this palette.')], HRESULT, 'Caption',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propget', helpstring(u'The name of this palette.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propget', helpstring(u'The number of items on this palette.')], HRESULT, 'ItemCount',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD([helpstring(u'The CLSID for the item on this palette at the specified index.')], HRESULT, 'GetItemInfo',
              ( ['in'], c_int, 'pos' ),
              ( ['in'], POINTER(IItemDef), 'itemDef' )),
]
################################################################
## code template for IPaletteDef implementation
##class IPaletteDef_Impl(object):
##    @property
##    def Caption(self):
##        u'The caption of this palette.'
##        #return pVal
##
##    @property
##    def ItemCount(self):
##        u'The number of items on this palette.'
##        #return pVal
##
##    @property
##    def Name(self):
##        u'The name of this palette.'
##        #return pVal
##
##    def GetItemInfo(self, pos, itemDef):
##        u'The CLSID for the item on this palette at the specified index.'
##        #return 
##


# values for enumeration 'esriCommandStyles'
esriCommandStyleTextOnly = 0
esriCommandStyleIconOnly = 1
esriCommandStyleIconAndText = 2
esriCommandStyleMenuBar = 4
esriCommandStyles = c_int # enum
ICompletionNotify._methods_ = [
    COMMETHOD([helpstring(u'Advises the framework that the control user has indicated completion.')], HRESULT, 'SetComplete'),
]
################################################################
## code template for ICompletionNotify implementation
##class ICompletionNotify_Impl(object):
##    def SetComplete(self):
##        u'Advises the framework that the control user has indicated completion.'
##        #return 
##

IArcGISPortal._methods_ = [
    COMMETHOD(['propget', helpstring(u'method Portal')], HRESULT, 'Portal',
              ( ['retval', 'out'], POINTER(BSTR), 'bsPortal' )),
    COMMETHOD(['propget', helpstring(u'method SignonImage')], HRESULT, 'SignonImage',
              ( ['retval', 'out'], POINTER(c_int), 'hBitmap' )),
    COMMETHOD(['propget', helpstring(u'method BannerImage')], HRESULT, 'BannerImage',
              ( ['retval', 'out'], POINTER(c_int), 'hBitmap' )),
    COMMETHOD(['propget', helpstring(u'method BannerImageUrl')], HRESULT, 'BannerImageUrl',
              ( ['retval', 'out'], POINTER(BSTR), 'bsUrl' )),
    COMMETHOD(['propget', helpstring(u'method Name')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'bsName' )),
    COMMETHOD(['propget', helpstring(u'method Name')], HRESULT, 'IsMultiTenant',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'isMulti' )),
]
################################################################
## code template for IArcGISPortal implementation
##class IArcGISPortal_Impl(object):
##    @property
##    def IsMultiTenant(self):
##        u'method Name'
##        #return isMulti
##
##    @property
##    def Name(self):
##        u'method Name'
##        #return bsName
##
##    @property
##    def BannerImageUrl(self):
##        u'method BannerImageUrl'
##        #return bsUrl
##
##    @property
##    def Portal(self):
##        u'method Portal'
##        #return bsPortal
##
##    @property
##    def SignonImage(self):
##        u'method SignonImage'
##        #return hBitmap
##
##    @property
##    def BannerImage(self):
##        u'method BannerImage'
##        #return hBitmap
##

class IToolKeys(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Allows a tool to override system shortcut keys.'
    _iid_ = GUID('{10107F77-6A0F-413F-8E88-EDE3B6DEDF66}')
    _idlflags_ = ['oleautomation']
IToolKeys._methods_ = [
    COMMETHOD([helpstring(u'Indicate whether the specified key is handled by the tool.')], HRESULT, 'OverrideKey',
              ( ['in'], c_int, 'keyCode' ),
              ( ['in'], c_int, 'shift' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'override' )),
]
################################################################
## code template for IToolKeys implementation
##class IToolKeys_Impl(object):
##    def OverrideKey(self, keyCode, shift):
##        u'Indicate whether the specified key is handled by the tool.'
##        #return override
##

class ComPropertySheetEventsProxyHelper(CoClass):
    u'ComPropertySheetEvents proxy source helper object.'
    _reg_clsid_ = GUID('{EF32CD1C-E37D-4524-B8D5-6D89D1E85BED}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{4ECCA6E2-B16B-4ACA-BD17-E74CAE4C150A}', 10, 2)
ComPropertySheetEventsProxyHelper._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown]
ComPropertySheetEventsProxyHelper._outgoing_interfaces_ = [IComPropertySheetEvents]

__all__ = ['esriSystemMouseCursorDefault',
           'esriSystemMouseCursorPagePanning',
           'esriSystemMouseCursorSizeNWSE', 'esriCommandStyles',
           'ICompletionNotify', 'esriCommandStyleIconAndText',
           'CommandHost', 'IArcGISSingleSignon2', 'esriKeyIntercept',
           'IMultiItemEx', 'esriSystemMouseCursorHotLink',
           'IArcGISSingleSignon', 'esriArcGISUriNewAccount',
           'esriSystemMouseCursorPagePan', 'esriArcGISUriPing',
           'esriTipStyleTransparent', 'esriSystemMouseCursorZoomIn',
           'esriArcGISUriUpdate', 'esriCommandStyleIconOnly',
           'esriSystemMouseCursorZoomOut', 'ISystemMouseCursor',
           'esriSystemMouseCursorPanning', 'IToolPalette',
           'IOperationStack', 'esriSystemMouseCursorSizeWE',
           'esriCmdBarTypeShortcutMenu',
           'ComPropertySheetEventsProxyHelper', 'IToolKeys',
           'esriSystemMouseCursorPan', 'ControlsOperationStack',
           'esriSystemMouseCursorSizeAll', 'esriTipStyleSolid',
           'esriSystemMouseCursorIcon', 'esriArcGISUriBase',
           'IArcGISPortal', 'ArcGISSingleSignon',
           'esriArcGISGlobeBasemapQuery', 'ITool',
           'esriKeyInterceptTab', 'esriSystemMouseCursor',
           'IMultiItemSeparator', 'IToolSelectedLayer',
           'esriCommandStyleTextOnly', 'esriSystemMouseCursorZoom',
           'esriKeyInterceptEnter', 'DataObjectHelper',
           'SystemMouseCursor', 'esriTipStyle', 'IComboBoxHook',
           'esriSystemMouseCursorPageZoomIn', 'IComponentTip',
           'esriSystemMouseCursorHand', 'esriArcGISUriSecure',
           'esriSystemMouseCursorPageZoomOut', 'IMultiItem',
           'esriCmdBarTypeMenu', 'IDataObjectHelper',
           'esriSystemMouseCursorNoDrop', 'ICommandHost',
           'esriSystemMouseCursorLabel',
           'esriSystemMouseCursorPencil', 'IToolControl',
           'IComPropertySheetEvents', 'esriCommandStyleMenuBar',
           'esriCmdBarTypeToolbar', 'esriSystemMouseCursorHourglass',
           'esriCmdBarType', 'esriArcGISUriForgottenPassword',
           'esriSystemMouseCursorSize',
           'esriSystemMouseCursorSizeNESW', 'IItemDef',
           'esriArcGISUriSpeed', 'ToolHost', 'esriKeyInterceptAlt',
           'esriArcGISSiteName', 'esriSystemMouseCursorCrosshair',
           'IMenuDef', 'esriArcGISBasemapQuery',
           'esriSystemMouseCursorSizeNS',
           'esriSystemMouseCursorIdentify', 'IToolBarDef',
           'esriArcGISUri', 'IComboBox', 'esriKeyInterceptArrowKeys',
           'esriSystemMouseCursorArrow', 'ICommandSubType',
           'esriSystemMouseCursorUpArrow', 'SystemFont', 'ICommand',
           'IOperation', 'IProgressDialog', 'IPaletteDef',
           'esriSystemMouseCursorArrowQuestion',
           'esriSystemMouseCursorIBeam', 'esriKeyInterceptNone',
           'esriSystemMouseCursorArrowHourglass']
from comtypes import _check_version; _check_version('501')

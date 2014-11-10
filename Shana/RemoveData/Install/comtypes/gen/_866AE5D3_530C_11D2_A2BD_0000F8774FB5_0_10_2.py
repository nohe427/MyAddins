# -*- coding: mbcs -*-
typelib_path = u'C:\\Program Files (x86)\\ArcGIS\\Desktop10.2\\com\\esriFramework.olb'
_lcid = 0 # change this if required
from ctypes import *
import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0
from comtypes import GUID
from ctypes import HRESULT
from comtypes import helpstring
from comtypes import COMMETHOD
from comtypes import dispid
from comtypes import CoClass
import comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2
from comtypes.automation import VARIANT
from comtypes import IUnknown
import comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2
from ctypes.wintypes import tagMSG
from comtypes import BSTR
from ctypes.wintypes import VARIANT_BOOL
UINT_PTR = c_ulong
LONG_PTR = c_int
import comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2
from ctypes.wintypes import tagSIZE
WSTRING = c_wchar_p
from comtypes.automation import IDispatch
from comtypes import wireHWND


class IComPropertyPageSite(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the callback mechanism of a COM property sheet.'
    _iid_ = GUID('{3B81F6F1-54A0-11D3-B8C3-00600802E603}')
    _idlflags_ = ['oleautomation']
IComPropertyPageSite._methods_ = [
    COMMETHOD([helpstring(u'Called by the property page to let the property sheet know that something changed.')], HRESULT, 'PageChanged'),
]
################################################################
## code template for IComPropertyPageSite implementation
##class IComPropertyPageSite_Impl(object):
##    def PageChanged(self):
##        u'Called by the property page to let the property sheet know that something changed.'
##        #return 
##

class ColorNamePropertyPage(CoClass):
    u'Esri custom color dialog ColorName page.'
    _reg_clsid_ = GUID('{20CD4007-8F3D-11D0-8590-0800091A2A72}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
class IPropertyPage(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{B196B28D-BAB4-101A-B69C-00AA00341D07}')
    _idlflags_ = []
class IComPropertyPage(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control a COM property page.'
    _iid_ = GUID('{76951CC6-DBB1-11D2-B868-00600802E603}')
    _idlflags_ = ['oleautomation']
class IComPropertyPage2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control a COM property page.'
    _iid_ = GUID('{97AFB06F-5C30-4EB3-A4C9-0327A64246C0}')
    _idlflags_ = ['oleautomation']
class IPropertyPageContext(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that helps you find out if property page applies to a set of objects.'
    _iid_ = GUID('{F87FA8A3-E51A-11D1-877C-0000F8751720}')
    _idlflags_ = ['oleautomation']
ColorNamePropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IPropertyPage, IComPropertyPage, IComPropertyPage2, IPropertyPageContext]

class CmykPropertyPage(CoClass):
    u'Esri custom color dialog CMYK page.'
    _reg_clsid_ = GUID('{20CD4004-8F3D-11D0-8590-0800091A2A72}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
CmykPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IPropertyPage, IComPropertyPage, IComPropertyPage2, IPropertyPageContext]

class RgbPropertyPage(CoClass):
    u'Esri custom color dialog RGB page.'
    _reg_clsid_ = GUID('{20CD4003-8F3D-11D0-8590-0800091A2A72}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
RgbPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IPropertyPage, IComPropertyPage, IComPropertyPage2, IPropertyPageContext]

class ICustomColorPalette(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Setting or Creating of a Custom Color Palette.'
    _iid_ = GUID('{7F579088-5407-42F1-BD80-548E7F3C1E6E}')
    _idlflags_ = ['oleautomation']
ICustomColorPalette._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The Color Objects.')], HRESULT, 'ColorSet',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISet), 'rhs' )),
]
################################################################
## code template for ICustomColorPalette implementation
##class ICustomColorPalette_Impl(object):
##    def ColorSet(self, rhs):
##        u'The Color Objects.'
##        #return 
##

class IObjectFactory(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u"Provides access to members that allow automation clients to create arbitrary objects within the application's process space."
    _iid_ = GUID('{60A1409B-9B67-431B-B428-E2C17BE36E9A}')
    _idlflags_ = ['oleautomation']
IObjectFactory._methods_ = [
    COMMETHOD([helpstring(u'Creates an instance of an object identified by objectID.')], HRESULT, 'Create',
              ( ['in'], VARIANT, 'objectID' ),
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'ppObj' )),
]
################################################################
## code template for IObjectFactory implementation
##class IObjectFactory_Impl(object):
##    def Create(self, objectID):
##        u'Creates an instance of an object identified by objectID.'
##        #return ppObj
##

class StyleGallery(CoClass):
    u'The Style Gallery object.'
    _reg_clsid_ = GUID('{AC0E9827-91CB-11D1-8813-080009EC732A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
StyleGallery._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IStyleGallery, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IStyleGalleryStorage, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream]

class IDocumentDirty(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the dirty flag of the Document.'
    _iid_ = GUID('{B26DE0CF-5C0A-433D-9082-097004E13A0A}')
    _idlflags_ = ['oleautomation']
IDocumentDirty._methods_ = [
    COMMETHOD([helpstring(u'Sets the dirty flag on the document.')], HRESULT, 'SetDirty'),
]
################################################################
## code template for IDocumentDirty implementation
##class IDocumentDirty_Impl(object):
##    def SetDirty(self):
##        u'Sets the dirty flag on the document.'
##        #return 
##

class IApplicationRefreshBitmap(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Triggers the application to call get_Bitmap on the control specified.'
    _iid_ = GUID('{EAC93DBF-9E0F-4AD0-8106-3E32141C15AB}')
    _idlflags_ = ['oleautomation']
IApplicationRefreshBitmap._methods_ = [
    COMMETHOD([helpstring(u'Triggers the application to call get_Bitmap on the control specified.')], HRESULT, 'RefreshBitmap',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID), 'ID' )),
]
################################################################
## code template for IApplicationRefreshBitmap implementation
##class IApplicationRefreshBitmap_Impl(object):
##    def RefreshBitmap(self, ID):
##        u'Triggers the application to call get_Bitmap on the control specified.'
##        #return 
##

class IVbaApplication(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that modify the VBA projects in this application.'
    _iid_ = GUID('{D7EE3483-004D-11D4-9FE7-00C04F6BC78E}')
    _idlflags_ = ['oleautomation']
IVbaApplication._methods_ = [
    COMMETHOD([helpstring(u'Runs the specified VBA macro.')], HRESULT, 'RunVBAMacro',
              ( ['in'], BSTR, 'docName' ),
              ( ['in'], BSTR, 'moduleName' ),
              ( ['in'], BSTR, 'macroName' ),
              ( ['in'], POINTER(VARIANT), 'arguments' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'returnValue' )),
    COMMETHOD([helpstring(u'Creates a code module in the specified VBA project.')], HRESULT, 'CreateCodeModule',
              ( ['in'], BSTR, 'docName' ),
              ( ['in'], BSTR, 'moduleName' )),
    COMMETHOD([helpstring(u'Removes a code module from the specified VBA project.')], HRESULT, 'RemoveCodeModule',
              ( ['in'], BSTR, 'docName' ),
              ( ['in'], BSTR, 'moduleName' )),
    COMMETHOD([helpstring(u'Inserts code into the specified module.')], HRESULT, 'InsertCode',
              ( ['in'], BSTR, 'docName' ),
              ( ['in'], BSTR, 'moduleName' ),
              ( ['in'], BSTR, 'codeText' )),
]
################################################################
## code template for IVbaApplication implementation
##class IVbaApplication_Impl(object):
##    def CreateCodeModule(self, docName, moduleName):
##        u'Creates a code module in the specified VBA project.'
##        #return 
##
##    def RemoveCodeModule(self, docName, moduleName):
##        u'Removes a code module from the specified VBA project.'
##        #return 
##
##    def InsertCode(self, docName, moduleName, codeText):
##        u'Inserts code into the specified module.'
##        #return 
##
##    def RunVBAMacro(self, docName, moduleName, macroName, arguments):
##        u'Runs the specified VBA macro.'
##        #return returnValue
##

class MessageDialog(CoClass):
    u'A dialog used for displaying a message.'
    _reg_clsid_ = GUID('{48F2C007-25C4-11D3-9FBA-00C04F6BC8DD}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
class IMessageDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to a method that works with a dialog for displaying a message.'
    _iid_ = GUID('{48F2C005-25C4-11D3-9FBA-00C04F6BC8DD}')
    _idlflags_ = ['oleautomation']
MessageDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMessageDialog]

class IDDECommandHandler(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that handle DDE commands.'
    _iid_ = GUID('{B8352370-23E6-42FC-9B43-5E7536C13AF9}')
    _idlflags_ = ['oleautomation']
IDDECommandHandler._methods_ = [
    COMMETHOD([helpstring(u'Indicates if the DDE command can be executed.')], HRESULT, 'CanExecute',
              ( ['in'], BSTR, 'Command' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'CanExecute' )),
    COMMETHOD([helpstring(u'Executes the DDE command.')], HRESULT, 'Execute',
              ( ['in'], BSTR, 'Command' )),
]
################################################################
## code template for IDDECommandHandler implementation
##class IDDECommandHandler_Impl(object):
##    def CanExecute(self, Command):
##        u'Indicates if the DDE command can be executed.'
##        #return CanExecute
##
##    def Execute(self, Command):
##        u'Executes the DDE command.'
##        #return 
##

class IDocumentDirty2(IDocumentDirty):
    _case_insensitive_ = True
    u'Provides access to the dirty flag of the Document.'
    _iid_ = GUID('{A684089C-CDE0-407C-92D8-811A3F8E850C}')
    _idlflags_ = ['oleautomation']
IDocumentDirty2._methods_ = [
    COMMETHOD([helpstring(u'Resets the dirty flag on the document.')], HRESULT, 'SetClean'),
]
################################################################
## code template for IDocumentDirty2 implementation
##class IDocumentDirty2_Impl(object):
##    def SetClean(self):
##        u'Resets the dirty flag on the document.'
##        #return 
##

class _RemotableHandle(Structure):
    pass
class __MIDL_IWinTypes_0009(Union):
    pass
__MIDL_IWinTypes_0009._fields_ = [
    ('hInproc', c_int),
    ('hRemote', c_int),
]
assert sizeof(__MIDL_IWinTypes_0009) == 4, sizeof(__MIDL_IWinTypes_0009)
assert alignment(__MIDL_IWinTypes_0009) == 4, alignment(__MIDL_IWinTypes_0009)
_RemotableHandle._fields_ = [
    ('fContext', c_int),
    ('u', __MIDL_IWinTypes_0009),
]
assert sizeof(_RemotableHandle) == 8, sizeof(_RemotableHandle)
assert alignment(_RemotableHandle) == 4, alignment(_RemotableHandle)
class IAppROT(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manipulate the Esri application running object table, AppROT.'
    _iid_ = GUID('{FABC30F9-D273-11D2-9F36-00C04F6BC61A}')
    _idlflags_ = ['oleautomation']
class IApplication(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Provides access to members that query or modify the application.'
    _iid_ = GUID('{8E52B9A5-307B-11D2-94C9-080009EEBECB}')
    _idlflags_ = ['dual', 'oleautomation']
IAppROT._methods_ = [
    COMMETHOD([helpstring(u'Adds an application reference to the running object table.')], HRESULT, 'Add',
              ( ['in'], POINTER(IApplication), 'pApp' ),
              ( ['retval', 'out'], POINTER(c_int), 'cookie' )),
    COMMETHOD([helpstring(u'Removes an application reference from the running object table.')], HRESULT, 'Remove',
              ( ['in'], c_int, 'cookie' )),
    COMMETHOD(['propget', helpstring(u'The count of application references within the running object table.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'The application reference at the specified index in the running object table.')], HRESULT, 'Item',
              ( ['in'], c_int, 'Index' ),
              ( ['retval', 'out'], POINTER(POINTER(IApplication)), 'pApp' )),
]
################################################################
## code template for IAppROT implementation
##class IAppROT_Impl(object):
##    @property
##    def Count(self):
##        u'The count of application references within the running object table.'
##        #return Count
##
##    @property
##    def Item(self, Index):
##        u'The application reference at the specified index in the running object table.'
##        #return pApp
##
##    def Add(self, pApp):
##        u'Adds an application reference to the running object table.'
##        #return cookie
##
##    def Remove(self, cookie):
##        u'Removes an application reference from the running object table.'
##        #return 
##

class IWindowPosition(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u"Provides access to members that query or modify a window's position, size and state."
    _iid_ = GUID('{88C995AE-64A7-43F5-BF12-88AC179B25A6}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriWindowState'
esriWSNormal = 0
esriWSMinimize = 1
esriWSMaximize = 2
esriWSFloating = 4
esriWindowState = c_int # enum
IWindowPosition._methods_ = [
    COMMETHOD(['propput', helpstring(u'The distance between the internal left edge of the window and screen.')], HRESULT, 'Left',
              ( ['in'], c_int, 'Left' )),
    COMMETHOD(['propget', helpstring(u'The distance between the internal left edge of the window and screen.')], HRESULT, 'Left',
              ( ['retval', 'out'], POINTER(c_int), 'Left' )),
    COMMETHOD(['propput', helpstring(u'The distance between the internal top edge of the window and screen.')], HRESULT, 'Top',
              ( ['in'], c_int, 'Top' )),
    COMMETHOD(['propget', helpstring(u'The distance between the internal top edge of the window and screen.')], HRESULT, 'Top',
              ( ['retval', 'out'], POINTER(c_int), 'Top' )),
    COMMETHOD(['propput', helpstring(u'The width of the window.')], HRESULT, 'Width',
              ( ['in'], c_int, 'Width' )),
    COMMETHOD(['propget', helpstring(u'The width of the window.')], HRESULT, 'Width',
              ( ['retval', 'out'], POINTER(c_int), 'Width' )),
    COMMETHOD(['propput', helpstring(u'The height of the window.')], HRESULT, 'Height',
              ( ['in'], c_int, 'Height' )),
    COMMETHOD(['propget', helpstring(u'The height of the window.')], HRESULT, 'Height',
              ( ['retval', 'out'], POINTER(c_int), 'Height' )),
    COMMETHOD([helpstring(u'Moves and optionally resizes the windows in a single function.')], HRESULT, 'Move',
              ( ['in'], c_int, 'Left' ),
              ( ['in'], c_int, 'Top' ),
              ( ['in', 'optional'], c_int, 'Width', 0 ),
              ( ['in', 'optional'], c_int, 'Height', 0 )),
    COMMETHOD(['propput', helpstring(u'The state of the window.')], HRESULT, 'State',
              ( ['in'], esriWindowState, 'windowState' )),
    COMMETHOD(['propget', helpstring(u'The state of the window.')], HRESULT, 'State',
              ( ['retval', 'out'], POINTER(esriWindowState), 'windowState' )),
]
################################################################
## code template for IWindowPosition implementation
##class IWindowPosition_Impl(object):
##    def _get(self):
##        u'The distance between the internal top edge of the window and screen.'
##        #return Top
##    def _set(self, Top):
##        u'The distance between the internal top edge of the window and screen.'
##    Top = property(_get, _set, doc = _set.__doc__)
##
##    def Move(self, Left, Top, Width, Height):
##        u'Moves and optionally resizes the windows in a single function.'
##        #return 
##
##    def _get(self):
##        u'The height of the window.'
##        #return Height
##    def _set(self, Height):
##        u'The height of the window.'
##    Height = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The width of the window.'
##        #return Width
##    def _set(self, Width):
##        u'The width of the window.'
##    Width = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The state of the window.'
##        #return windowState
##    def _set(self, windowState):
##        u'The state of the window.'
##    State = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The distance between the internal left edge of the window and screen.'
##        #return Left
##    def _set(self, Left):
##        u'The distance between the internal left edge of the window and screen.'
##    Left = property(_get, _set, doc = _set.__doc__)
##

class ComPropertySheet(CoClass):
    u'COM Property Sheet Object.'
    _reg_clsid_ = GUID('{01964AF3-7F1A-11D2-A2DE-080009B6F22B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
class IComPropertySheet(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that work with a COM property sheet.'
    _iid_ = GUID('{76951CC7-DBB1-11D2-B868-00600802E603}')
    _idlflags_ = ['oleautomation']
class IPropertyPageSite(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{B196B28C-BAB4-101A-B69C-00AA00341D07}')
    _idlflags_ = []
class IComPropertySheetID(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Properties to identify sheet.'
    _iid_ = GUID('{C7FB79B8-41A6-4F58-B58B-C39FB83AAA0A}')
    _idlflags_ = ['oleautomation']
ComPropertySheet._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IComPropertySheet, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IConnectionPointContainer, IComPropertyPageSite, IPropertyPageSite, IComPropertySheetID]
ComPropertySheet._outgoing_interfaces_ = [comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IComPropertySheetEvents]

class IDockableWindowHelpNotify(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that define and control a dockable window.'
    _iid_ = GUID('{15379638-9153-4002-9B0D-7E8C4E8F1797}')
    _idlflags_ = ['oleautomation']
IDockableWindowHelpNotify._methods_ = [
    COMMETHOD([], HRESULT, 'OnHelpClick',
              ( ['in'], c_int, 'X' ),
              ( ['in'], c_int, 'Y' )),
]
################################################################
## code template for IDockableWindowHelpNotify implementation
##class IDockableWindowHelpNotify_Impl(object):
##    def OnHelpClick(self, X, Y):
##        '-no docstring-'
##        #return 
##

class HsvPropertyPage(CoClass):
    u'Esri custom color dialog HSV page.'
    _reg_clsid_ = GUID('{20CD4005-8F3D-11D0-8590-0800091A2A72}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
HsvPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IPropertyPage, IComPropertyPage, IComPropertyPage2, IPropertyPageContext]

class IDockableWindow(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that define and control a dockable window.'
    _iid_ = GUID('{3EE6D0C3-E3F2-11D3-A679-0008C7DF97B9}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriDockFlags'
esriDockHide = 0
esriDockShow = 1
esriDockLeft = 2
esriDockRight = 4
esriDockTop = 8
esriDockBottom = 16
esriDockFloat = 32
esriDockToggle = 64
esriDockTabbed = 128
esriDockUnPinned = 256
esriDockFlags = c_int # enum
IDockableWindow._methods_ = [
    COMMETHOD(['propget', helpstring(u'The name of the dockable window.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'The caption of the dockable window.')], HRESULT, 'Caption',
              ( ['retval', 'out'], POINTER(BSTR), 'Caption' )),
    COMMETHOD(['propput', helpstring(u'The caption of the dockable window.')], HRESULT, 'Caption',
              ( ['in'], BSTR, 'Caption' )),
    COMMETHOD(['propget', helpstring(u'The unique id for this dockable window.')], HRESULT, 'ID',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID)), 'ID' )),
    COMMETHOD([helpstring(u'Hides or shows the dockable window.')], HRESULT, 'Show',
              ( ['in'], VARIANT_BOOL, 'Show' )),
    COMMETHOD([helpstring(u'Indicates if this docking window is visible.')], HRESULT, 'IsVisible',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bVisible' )),
    COMMETHOD([helpstring(u'Docks or undocks this docking window.')], HRESULT, 'Dock',
              ( ['in'], esriDockFlags, 'dockFlags' )),
    COMMETHOD(['propget', helpstring(u'User defined data.')], HRESULT, 'UserData',
              ( ['retval', 'out'], POINTER(VARIANT), 'data' )),
]
################################################################
## code template for IDockableWindow implementation
##class IDockableWindow_Impl(object):
##    def Dock(self, dockFlags):
##        u'Docks or undocks this docking window.'
##        #return 
##
##    @property
##    def UserData(self):
##        u'User defined data.'
##        #return data
##
##    @property
##    def Name(self):
##        u'The name of the dockable window.'
##        #return Name
##
##    def Show(self, Show):
##        u'Hides or shows the dockable window.'
##        #return 
##
##    def _get(self):
##        u'The caption of the dockable window.'
##        #return Caption
##    def _set(self, Caption):
##        u'The caption of the dockable window.'
##    Caption = property(_get, _set, doc = _set.__doc__)
##
##    def IsVisible(self):
##        u'Indicates if this docking window is visible.'
##        #return bVisible
##
##    @property
##    def ID(self):
##        u'The unique id for this dockable window.'
##        #return ID
##

class IApplicationStatusEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to events fired by application.'
    _iid_ = GUID('{B93E627D-8506-4915-887D-B306B0482BA4}')
    _idlflags_ = ['oleautomation']
IApplicationStatusEvents._methods_ = [
    COMMETHOD([helpstring(u'Fired when the application UI is initialized.')], HRESULT, 'Initialized'),
]
################################################################
## code template for IApplicationStatusEvents implementation
##class IApplicationStatusEvents_Impl(object):
##    def Initialized(self):
##        u'Fired when the application UI is initialized.'
##        #return 
##

class IColorPalette(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Color Palette.'
    _iid_ = GUID('{14746473-1534-11D3-9F49-00C04F6BC709}')
    _idlflags_ = ['oleautomation']
IColorPalette._methods_ = [
    COMMETHOD([helpstring(u'Show Color Palette.')], HRESULT, 'TrackPopupMenu',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.tagRECT), 'rect' ),
              ( ['in'], POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IColor), 'currentColor' ),
              ( ['in'], VARIANT_BOOL, 'orientation' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hParentWnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ok' )),
    COMMETHOD(['propget', helpstring(u'The Selected Color.')], HRESULT, 'Color',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IColor)), 'newColor' )),
]
################################################################
## code template for IColorPalette implementation
##class IColorPalette_Impl(object):
##    @property
##    def Color(self):
##        u'The Selected Color.'
##        #return newColor
##
##    def TrackPopupMenu(self, rect, currentColor, orientation, hParentWnd):
##        u'Show Color Palette.'
##        #return ok
##

class IProgressDialog2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that work with a progress dialog.'
    _iid_ = GUID('{0E21FD01-1DC9-4230-95CD-64EE2C4266A1}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriProgressAnimationTypes'
esriProgressGlobe = 0
esriDownloadFile = 1
esriNoAnimation = 2
esriProgressSpiral = 3
esriProgressAnimationTypes = c_int # enum
IProgressDialog2._methods_ = [
    COMMETHOD([helpstring(u'Shows the progress dialog.')], HRESULT, 'ShowDialog'),
    COMMETHOD([helpstring(u'Hides the progress dialog.')], HRESULT, 'HideDialog'),
    COMMETHOD(['propget', helpstring(u'Indicates if the Cancel button is enabled.')], HRESULT, 'CancelEnabled',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bVal' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the Cancel button is enabled.')], HRESULT, 'CancelEnabled',
              ( ['in'], VARIANT_BOOL, 'bVal' )),
    COMMETHOD(['propput', helpstring(u'The description displayed in the dialog.')], HRESULT, 'Description',
              ( ['in'], BSTR, 'status' )),
    COMMETHOD(['propget', helpstring(u'The description displayed in the dialog.')], HRESULT, 'Description',
              ( ['retval', 'out'], POINTER(BSTR), 'status' )),
    COMMETHOD(['propput', helpstring(u'The caption displayed in the dialog.')], HRESULT, 'Title',
              ( ['in'], BSTR, 'Title' )),
    COMMETHOD(['propget', helpstring(u'The caption displayed in the dialog.')], HRESULT, 'Title',
              ( ['retval', 'out'], POINTER(BSTR), 'Title' )),
    COMMETHOD(['propput', helpstring(u'The animation type displayed in the dialog.')], HRESULT, 'Animation',
              ( ['in'], esriProgressAnimationTypes, 'Type' )),
    COMMETHOD(['propget', helpstring(u'The animation type displayed in the dialog.')], HRESULT, 'Animation',
              ( ['retval', 'out'], POINTER(esriProgressAnimationTypes), 'Type' )),
]
################################################################
## code template for IProgressDialog2 implementation
##class IProgressDialog2_Impl(object):
##    def _get(self):
##        u'The description displayed in the dialog.'
##        #return status
##    def _set(self, status):
##        u'The description displayed in the dialog.'
##    Description = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The caption displayed in the dialog.'
##        #return Title
##    def _set(self, Title):
##        u'The caption displayed in the dialog.'
##    Title = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the Cancel button is enabled.'
##        #return bVal
##    def _set(self, bVal):
##        u'Indicates if the Cancel button is enabled.'
##    CancelEnabled = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The animation type displayed in the dialog.'
##        #return Type
##    def _set(self, Type):
##        u'The animation type displayed in the dialog.'
##    Animation = property(_get, _set, doc = _set.__doc__)
##
##    def ShowDialog(self):
##        u'Shows the progress dialog.'
##        #return 
##
##    def HideDialog(self):
##        u'Hides the progress dialog.'
##        #return 
##

class IDockableWindowImageDef(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u"Provides access to members that define a dockable window's image."
    _iid_ = GUID('{08F4FC5D-C23F-4210-B289-1350ED5632ED}')
    _idlflags_ = ['oleautomation']
IDockableWindowImageDef._methods_ = [
    COMMETHOD(['propget', helpstring(u'The bitmap for the dockable window.')], HRESULT, 'Bitmap',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'Bitmap' )),
]
################################################################
## code template for IDockableWindowImageDef implementation
##class IDockableWindowImageDef_Impl(object):
##    @property
##    def Bitmap(self):
##        u'The bitmap for the dockable window.'
##        #return Bitmap
##


# values for enumeration 'esriDocumentType'
esriDocumentTypeNormal = 0
esriDocumentTypeTemplate = 1
esriDocumentTypeDocument = 2
esriDocumentType = c_int # enum
class EnumStyleGalleryItem(CoClass):
    u'An enumerator of Style Gallery items.'
    _reg_clsid_ = GUID('{AC0E982A-91CB-11D1-8813-080009EC732A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
EnumStyleGalleryItem._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IEnumStyleGalleryItem]

class INumberDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that work with a dialog for getting a number.'
    _iid_ = GUID('{759F7B98-E07D-11D1-AA87-00C04FA374BD}')
    _idlflags_ = ['oleautomation']
INumberDialog._methods_ = [
    COMMETHOD(['propget', helpstring(u'The number value entered in the dialog.')], HRESULT, 'Value',
              ( ['retval', 'out'], POINTER(c_double), 'val' )),
    COMMETHOD([helpstring(u'Shows the dialog.')], HRESULT, 'DoModal',
              ( ['in'], BSTR, 'Title' ),
              ( ['in'], c_double, 'initialValue' ),
              ( ['in'], c_int, 'numDecs' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hWnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'okPressed' )),
]
################################################################
## code template for INumberDialog implementation
##class INumberDialog_Impl(object):
##    def DoModal(self, Title, initialValue, numDecs, hWnd):
##        u'Shows the dialog.'
##        #return okPressed
##
##    @property
##    def Value(self):
##        u'The number value entered in the dialog.'
##        #return val
##

class GrayPropertyPage(CoClass):
    u'Esri custom color dialog Gray page.'
    _reg_clsid_ = GUID('{20CD4006-8F3D-11D0-8590-0800091A2A72}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
GrayPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IPropertyPage, IComPropertyPage, IComPropertyPage2, IPropertyPageContext]

class DllThreadManager(CoClass):
    u'DllThreadManager CoType.'
    _reg_clsid_ = GUID('{057C74E0-FAF0-45CB-89E3-AF132BE1A2A7}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
class IDllThreadManager(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to an event that DLL thread managers listen for.'
    _iid_ = GUID('{52BCFF1B-6A36-49DF-B14F-BE227D8543EF}')
    _idlflags_ = ['oleautomation']
DllThreadManager._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDllThreadManager]

class IGetStringDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that work with a dialog for getting a string.'
    _iid_ = GUID('{A7B8EC8F-AC12-11D2-AB27-00C04FA334B3}')
    _idlflags_ = ['oleautomation']
IGetStringDialog._methods_ = [
    COMMETHOD(['propget', helpstring(u'The value of the string.')], HRESULT, 'Value',
              ( ['retval', 'out'], POINTER(BSTR), 'val' )),
    COMMETHOD([helpstring(u'Shows the dialog.')], HRESULT, 'DoModal',
              ( ['in'], BSTR, 'dialogTitle' ),
              ( ['in'], BSTR, 'getStringLabel' ),
              ( ['in'], BSTR, 'initialValue' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hWnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'okPressed' )),
]
################################################################
## code template for IGetStringDialog implementation
##class IGetStringDialog_Impl(object):
##    def DoModal(self, dialogTitle, getStringLabel, initialValue, hWnd):
##        u'Shows the dialog.'
##        #return okPressed
##
##    @property
##    def Value(self):
##        u'The value of the string.'
##        #return val
##

IComPropertyPage2._methods_ = [
    COMMETHOD(['propput', helpstring(u'The title of the property page.')], HRESULT, 'Title',
              ( ['in'], BSTR, 'Title' )),
    COMMETHOD(['propget', helpstring(u'The title of the property page.')], HRESULT, 'Title',
              ( ['retval', 'out'], POINTER(BSTR), 'Title' )),
    COMMETHOD(['propput', helpstring(u'The page priority. The higher the priority, the sooner the page appears in the containing property sheet.')], HRESULT, 'Priority',
              ( ['in'], c_int, 'Priority' )),
    COMMETHOD(['propget', helpstring(u'The page priority. The higher the priority, the sooner the page appears in the containing property sheet.')], HRESULT, 'Priority',
              ( ['retval', 'out'], POINTER(c_int), 'Priority' )),
    COMMETHOD(['propget', helpstring(u'The width of the page in pixels.')], HRESULT, 'Width',
              ( ['retval', 'out'], POINTER(c_int), 'Width' )),
    COMMETHOD(['propget', helpstring(u'The height of the page in pixels.')], HRESULT, 'Height',
              ( ['retval', 'out'], POINTER(c_int), 'Height' )),
    COMMETHOD(['propputref', helpstring(u'The sheet that contains the page.')], HRESULT, 'PageSite',
              ( ['in'], POINTER(IComPropertyPageSite), 'rhs' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the page made any changes to the object(s).')], HRESULT, 'IsPageDirty',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'isDirty' )),
    COMMETHOD(['propget', helpstring(u'The help file name for the page.')], HRESULT, 'HelpFile',
              ( ['retval', 'out'], POINTER(BSTR), 'HelpFile' )),
    COMMETHOD(['propget', helpstring(u'The help context ID for the specified control on the page.')], HRESULT, 'HelpContextID',
              ( ['in'], c_int, 'controlID' ),
              ( ['retval', 'out'], POINTER(c_int), 'helpID' )),
    COMMETHOD([helpstring(u'Occurs on page creation. Return the hWnd of the page here.')], HRESULT, 'Activate',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'hWnd' )),
    COMMETHOD([helpstring(u'Destroys the page.')], HRESULT, 'Deactivate'),
    COMMETHOD([helpstring(u'Indicates if the page applies to the specified objects.')], HRESULT, 'Applies',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISet), 'objects' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pApplies' )),
    COMMETHOD([helpstring(u'Supplies the page with the object(s) to be edited.')], HRESULT, 'SetObjects',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISet), 'objects' )),
    COMMETHOD([helpstring(u'Shows the page.')], HRESULT, 'Show'),
    COMMETHOD([helpstring(u'Hides the page.')], HRESULT, 'Hide'),
    COMMETHOD([helpstring(u'Applies any changes to the object(s).')], HRESULT, 'Apply'),
    COMMETHOD([helpstring(u'Cancels the changes to the object(s).')], HRESULT, 'Cancel'),
    COMMETHOD([helpstring(u'Returns VARIANT_FALSE to prevent the cancel operation or VARIANT_TRUE to allow it.')], HRESULT, 'QueryCancel',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'QueryCancel' )),
]
################################################################
## code template for IComPropertyPage2 implementation
##class IComPropertyPage2_Impl(object):
##    @property
##    def IsPageDirty(self):
##        u'Indicates if the page made any changes to the object(s).'
##        #return isDirty
##
##    @property
##    def HelpContextID(self, controlID):
##        u'The help context ID for the specified control on the page.'
##        #return helpID
##
##    def Activate(self):
##        u'Occurs on page creation. Return the hWnd of the page here.'
##        #return hWnd
##
##    def Hide(self):
##        u'Hides the page.'
##        #return 
##
##    def _get(self):
##        u'The title of the property page.'
##        #return Title
##    def _set(self, Title):
##        u'The title of the property page.'
##    Title = property(_get, _set, doc = _set.__doc__)
##
##    def PageSite(self, rhs):
##        u'The sheet that contains the page.'
##        #return 
##
##    def Applies(self, objects):
##        u'Indicates if the page applies to the specified objects.'
##        #return pApplies
##
##    @property
##    def Height(self):
##        u'The height of the page in pixels.'
##        #return Height
##
##    def _get(self):
##        u'The page priority. The higher the priority, the sooner the page appears in the containing property sheet.'
##        #return Priority
##    def _set(self, Priority):
##        u'The page priority. The higher the priority, the sooner the page appears in the containing property sheet.'
##    Priority = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Width(self):
##        u'The width of the page in pixels.'
##        #return Width
##
##    def SetObjects(self, objects):
##        u'Supplies the page with the object(s) to be edited.'
##        #return 
##
##    @property
##    def HelpFile(self):
##        u'The help file name for the page.'
##        #return HelpFile
##
##    def Cancel(self):
##        u'Cancels the changes to the object(s).'
##        #return 
##
##    def Apply(self):
##        u'Applies any changes to the object(s).'
##        #return 
##
##    def QueryCancel(self):
##        u'Returns VARIANT_FALSE to prevent the cancel operation or VARIANT_TRUE to allow it.'
##        #return QueryCancel
##
##    def Show(self):
##        u'Shows the page.'
##        #return 
##
##    def Deactivate(self):
##        u'Destroys the page.'
##        #return 
##

IComPropertyPage._methods_ = [
    COMMETHOD(['propput', helpstring(u'The title of the property page.')], HRESULT, 'Title',
              ( ['in'], BSTR, 'Title' )),
    COMMETHOD(['propget', helpstring(u'The title of the property page.')], HRESULT, 'Title',
              ( ['retval', 'out'], POINTER(BSTR), 'Title' )),
    COMMETHOD(['propput', helpstring(u'The page priority. The higher the priority, the sooner the page appears in the containing property sheet.')], HRESULT, 'Priority',
              ( ['in'], c_int, 'Priority' )),
    COMMETHOD(['propget', helpstring(u'The page priority. The higher the priority, the sooner the page appears in the containing property sheet.')], HRESULT, 'Priority',
              ( ['retval', 'out'], POINTER(c_int), 'Priority' )),
    COMMETHOD(['propget', helpstring(u'The width of the page in pixels.')], HRESULT, 'Width',
              ( ['retval', 'out'], POINTER(c_int), 'Width' )),
    COMMETHOD(['propget', helpstring(u'The height of the page in pixels.')], HRESULT, 'Height',
              ( ['retval', 'out'], POINTER(c_int), 'Height' )),
    COMMETHOD(['propputref', helpstring(u'The sheet that contains the page.')], HRESULT, 'PageSite',
              ( ['in'], POINTER(IComPropertyPageSite), 'rhs' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the page made any changes to the object(s).')], HRESULT, 'IsPageDirty',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'isDirty' )),
    COMMETHOD(['propget', helpstring(u'The help file name for the page.')], HRESULT, 'HelpFile',
              ( ['retval', 'out'], POINTER(BSTR), 'HelpFile' )),
    COMMETHOD(['propget', helpstring(u'The help context ID for the specified control on the page.')], HRESULT, 'HelpContextID',
              ( ['in'], c_int, 'controlID' ),
              ( ['retval', 'out'], POINTER(c_int), 'helpID' )),
    COMMETHOD([helpstring(u'Occurs on page creation. Return the hWnd of the page here.')], HRESULT, 'Activate',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'hWnd' )),
    COMMETHOD([helpstring(u'Destroys the page.')], HRESULT, 'Deactivate'),
    COMMETHOD([helpstring(u'Indicates if the page applies to the specified objects.')], HRESULT, 'Applies',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISet), 'objects' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pApplies' )),
    COMMETHOD([helpstring(u'Supplies the page with the object(s) to be edited.')], HRESULT, 'SetObjects',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISet), 'objects' )),
    COMMETHOD([helpstring(u'Shows the page.')], HRESULT, 'Show'),
    COMMETHOD([helpstring(u'Hides the page.')], HRESULT, 'Hide'),
    COMMETHOD([helpstring(u'Applies any changes to the object(s).')], HRESULT, 'Apply'),
    COMMETHOD([helpstring(u'Cancels the changes to the object(s).')], HRESULT, 'Cancel'),
]
################################################################
## code template for IComPropertyPage implementation
##class IComPropertyPage_Impl(object):
##    @property
##    def IsPageDirty(self):
##        u'Indicates if the page made any changes to the object(s).'
##        #return isDirty
##
##    @property
##    def HelpContextID(self, controlID):
##        u'The help context ID for the specified control on the page.'
##        #return helpID
##
##    def Activate(self):
##        u'Occurs on page creation. Return the hWnd of the page here.'
##        #return hWnd
##
##    def Hide(self):
##        u'Hides the page.'
##        #return 
##
##    def _get(self):
##        u'The title of the property page.'
##        #return Title
##    def _set(self, Title):
##        u'The title of the property page.'
##    Title = property(_get, _set, doc = _set.__doc__)
##
##    def PageSite(self, rhs):
##        u'The sheet that contains the page.'
##        #return 
##
##    def Applies(self, objects):
##        u'Indicates if the page applies to the specified objects.'
##        #return pApplies
##
##    @property
##    def Height(self):
##        u'The height of the page in pixels.'
##        #return Height
##
##    def _get(self):
##        u'The page priority. The higher the priority, the sooner the page appears in the containing property sheet.'
##        #return Priority
##    def _set(self, Priority):
##        u'The page priority. The higher the priority, the sooner the page appears in the containing property sheet.'
##    Priority = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Width(self):
##        u'The width of the page in pixels.'
##        #return Width
##
##    def SetObjects(self, objects):
##        u'Supplies the page with the object(s) to be edited.'
##        #return 
##
##    @property
##    def HelpFile(self):
##        u'The help file name for the page.'
##        #return HelpFile
##
##    def Cancel(self):
##        u'Cancels the changes to the object(s).'
##        #return 
##
##    def Apply(self):
##        u'Applies any changes to the object(s).'
##        #return 
##
##    def Show(self):
##        u'Shows the page.'
##        #return 
##
##    def Deactivate(self):
##        u'Destroys the page.'
##        #return 
##

class IRootLevelMenu(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Indicator interface that identifies a root level menu.'
    _iid_ = GUID('{66767665-D576-11D2-9F57-00C04F6BC61A}')
    _idlflags_ = ['oleautomation']
IRootLevelMenu._methods_ = [
]
################################################################
## code template for IRootLevelMenu implementation
##class IRootLevelMenu_Impl(object):

class IAccelerator(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that define an accelerator.'
    _iid_ = GUID('{08300DE1-27FD-11D2-AA2F-000000000000}')
    _idlflags_ = ['oleautomation']
IAccelerator._methods_ = [
    COMMETHOD(['propput', helpstring(u'Indicates if the Shift key is pressed for this accelerator.')], HRESULT, 'Shift',
              ( ['in'], VARIANT_BOOL, 'bShift' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the Shift key is pressed for this accelerator.')], HRESULT, 'Shift',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bShift' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the Alt key is pressed for this accelerator.')], HRESULT, 'Alt',
              ( ['in'], VARIANT_BOOL, 'bAlt' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the Alt key is pressed for this accelerator.')], HRESULT, 'Alt',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bAlt' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the Ctrl key is pressed for this accelerator.')], HRESULT, 'Ctrl',
              ( ['in'], VARIANT_BOOL, 'bCtrl' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the Ctrl key is pressed for this accelerator.')], HRESULT, 'Ctrl',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bCtrl' )),
    COMMETHOD(['propput', helpstring(u'The keycode for this accelerator.')], HRESULT, 'Key',
              ( ['in'], c_int, 'keyCode' )),
    COMMETHOD(['propget', helpstring(u'The keycode for this accelerator.')], HRESULT, 'Key',
              ( ['retval', 'out'], POINTER(c_int), 'keyCode' )),
    COMMETHOD(['propput', helpstring(u'The identifier of the command that this accelerator activates.')], HRESULT, 'CommandID',
              ( ['in'], VARIANT, 'cmdID' )),
    COMMETHOD(['propget', helpstring(u'The identifier of the command that this accelerator activates.')], HRESULT, 'CommandID',
              ( ['retval', 'out'], POINTER(VARIANT), 'cmdID' )),
    COMMETHOD([helpstring(u'Removes this accelerator from the accelerator table.')], HRESULT, 'Delete'),
]
################################################################
## code template for IAccelerator implementation
##class IAccelerator_Impl(object):
##    def _get(self):
##        u'Indicates if the Ctrl key is pressed for this accelerator.'
##        #return bCtrl
##    def _set(self, bCtrl):
##        u'Indicates if the Ctrl key is pressed for this accelerator.'
##    Ctrl = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the Shift key is pressed for this accelerator.'
##        #return bShift
##    def _set(self, bShift):
##        u'Indicates if the Shift key is pressed for this accelerator.'
##    Shift = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The keycode for this accelerator.'
##        #return keyCode
##    def _set(self, keyCode):
##        u'The keycode for this accelerator.'
##    Key = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the Alt key is pressed for this accelerator.'
##        #return bAlt
##    def _set(self, bAlt):
##        u'Indicates if the Alt key is pressed for this accelerator.'
##    Alt = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The identifier of the command that this accelerator activates.'
##        #return cmdID
##    def _set(self, cmdID):
##        u'The identifier of the command that this accelerator activates.'
##    CommandID = property(_get, _set, doc = _set.__doc__)
##
##    def Delete(self):
##        u'Removes this accelerator from the accelerator table.'
##        #return 
##

class tagPROPPAGEINFO(Structure):
    pass
tagPROPPAGEINFO._fields_ = [
    ('cb', c_ulong),
    ('pszTitle', WSTRING),
    ('size', tagSIZE),
    ('pszDocString', WSTRING),
    ('pszHelpFile', WSTRING),
    ('dwHelpContext', c_ulong),
]
assert sizeof(tagPROPPAGEINFO) == 28, sizeof(tagPROPPAGEINFO)
assert alignment(tagPROPPAGEINFO) == 4, alignment(tagPROPPAGEINFO)
class Library(object):
    u'Esri Framework Object Library 10.2'
    name = u'esriFramework'
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)

IDllThreadManager._methods_ = [
    COMMETHOD([helpstring(u'Occurs when the application is shutting down. DLL threads should be terminated upon receiving this message.')], HRESULT, 'OnShutdown'),
]
################################################################
## code template for IDllThreadManager implementation
##class IDllThreadManager_Impl(object):
##    def OnShutdown(self):
##        u'Occurs when the application is shutting down. DLL threads should be terminated upon receiving this message.'
##        #return 
##

class IArcToolboxTool(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Toolbox tools.'
    _iid_ = GUID('{0ACDFE44-F5E2-11D3-A623-0008C711C8C1}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriATModality'
esriATModeless = 0
esriATModal = 1
esriATModality = c_int # enum
IArcToolboxTool._methods_ = [
    COMMETHOD(['propput', helpstring(u'The modality for the tool.')], HRESULT, 'Modality',
              ( ['in'], esriATModality, 'dialogModality' )),
    COMMETHOD(['propget', helpstring(u'The modality for the tool.')], HRESULT, 'Modality',
              ( ['retval', 'out'], POINTER(esriATModality), 'dialogModality' )),
    COMMETHOD(['propget', helpstring(u'The name of this tool.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'The description for this tool.')], HRESULT, 'Message',
              ( ['retval', 'out'], POINTER(BSTR), 'Message' )),
    COMMETHOD(['propget', helpstring(u'The name of the help file associated with this tool.')], HRESULT, 'HelpFile',
              ( ['retval', 'out'], POINTER(BSTR), 'HelpFile' )),
    COMMETHOD(['propget', helpstring(u'The help context ID associated with this tool.')], HRESULT, 'HelpContextID',
              ( ['retval', 'out'], POINTER(c_int), 'helpID' )),
    COMMETHOD(['propget', helpstring(u'The bitmap that is used as the icon for this tool.')], HRESULT, 'Bitmap',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IPictureDisp)), 'Bitmap' )),
    COMMETHOD(['propget', helpstring(u'The location of the tool in the treeview.')], HRESULT, 'TreeviewLocation',
              ( ['retval', 'out'], POINTER(BSTR), 'TreeviewLocation' )),
    COMMETHOD([helpstring(u'Occurs when this tool is created.')], HRESULT, 'OnCreate',
              ( ['in'], POINTER(IDispatch), 'hook' )),
    COMMETHOD([helpstring(u'Run the tool.')], HRESULT, 'Execute',
              ( ['in', 'optional'], POINTER(VARIANT), 'InputData' )),
]
################################################################
## code template for IArcToolboxTool implementation
##class IArcToolboxTool_Impl(object):
##    def Execute(self, InputData):
##        u'Run the tool.'
##        #return 
##
##    @property
##    def Name(self):
##        u'The name of this tool.'
##        #return Name
##
##    @property
##    def Bitmap(self):
##        u'The bitmap that is used as the icon for this tool.'
##        #return Bitmap
##
##    @property
##    def HelpContextID(self):
##        u'The help context ID associated with this tool.'
##        #return helpID
##
##    @property
##    def TreeviewLocation(self):
##        u'The location of the tool in the treeview.'
##        #return TreeviewLocation
##
##    @property
##    def HelpFile(self):
##        u'The name of the help file associated with this tool.'
##        #return HelpFile
##
##    @property
##    def Message(self):
##        u'The description for this tool.'
##        #return Message
##
##    def OnCreate(self, hook):
##        u'Occurs when this tool is created.'
##        #return 
##
##    def _get(self):
##        u'The modality for the tool.'
##        #return dialogModality
##    def _set(self, dialogModality):
##        u'The modality for the tool.'
##    Modality = property(_get, _set, doc = _set.__doc__)
##

class IDockableWindowDef(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that define a dockable window.'
    _iid_ = GUID('{3D1FA10A-F154-11D3-A67E-0008C7DF97B9}')
    _idlflags_ = ['oleautomation']
IDockableWindowDef._methods_ = [
    COMMETHOD([helpstring(u'Occurs when this dockable window is created and provides access to the application.')], HRESULT, 'OnCreate',
              ( ['in'], POINTER(IDispatch), 'hook' )),
    COMMETHOD(['propget', helpstring(u'The hWnd of the window to be embedded in a dockable window.')], HRESULT, 'ChildHWND',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'hWnd' )),
    COMMETHOD(['propget', helpstring(u'The name of the dockable window.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'The caption of the dockable window.')], HRESULT, 'Caption',
              ( ['retval', 'out'], POINTER(BSTR), 'Caption' )),
    COMMETHOD([helpstring(u'Occurs when the docking window is about to be destroyed.')], HRESULT, 'OnDestroy'),
    COMMETHOD(['propget', helpstring(u'User defined data.')], HRESULT, 'UserData',
              ( ['retval', 'out'], POINTER(VARIANT), 'data' )),
]
################################################################
## code template for IDockableWindowDef implementation
##class IDockableWindowDef_Impl(object):
##    @property
##    def UserData(self):
##        u'User defined data.'
##        #return data
##
##    @property
##    def Name(self):
##        u'The name of the dockable window.'
##        #return Name
##
##    @property
##    def Caption(self):
##        u'The caption of the dockable window.'
##        #return Caption
##
##    def OnDestroy(self):
##        u'Occurs when the docking window is about to be destroyed.'
##        #return 
##
##    @property
##    def ChildHWND(self):
##        u'The hWnd of the window to be embedded in a dockable window.'
##        #return hWnd
##
##    def OnCreate(self, hook):
##        u'Occurs when this dockable window is created and provides access to the application.'
##        #return 
##

class ICoordinateDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that work with a dialog for getting coordinates.'
    _iid_ = GUID('{759F7B9B-E07D-11D1-AA87-00C04FA374BD}')
    _idlflags_ = ['oleautomation']
ICoordinateDialog._methods_ = [
    COMMETHOD(['propget', helpstring(u'The X value entered in the dialog.')], HRESULT, 'X',
              ( ['retval', 'out'], POINTER(c_double), 'val' )),
    COMMETHOD(['propget', helpstring(u'The Y value entered in the dialog.')], HRESULT, 'Y',
              ( ['retval', 'out'], POINTER(c_double), 'val' )),
    COMMETHOD([helpstring(u'Shows the dialog.')], HRESULT, 'DoModal',
              ( ['in'], BSTR, 'Title' ),
              ( ['in'], c_double, 'initialX' ),
              ( ['in'], c_double, 'initialY' ),
              ( ['in'], c_int, 'numDecs' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hWnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'okPressed' )),
]
################################################################
## code template for ICoordinateDialog implementation
##class ICoordinateDialog_Impl(object):
##    @property
##    def Y(self):
##        u'The Y value entered in the dialog.'
##        #return val
##
##    @property
##    def X(self):
##        u'The X value entered in the dialog.'
##        #return val
##
##    def DoModal(self, Title, initialX, initialY, numDecs, hWnd):
##        u'Shows the dialog.'
##        #return okPressed
##

class MouseCursor(CoClass):
    u'The the system mouse cursor.'
    _reg_clsid_ = GUID('{DCAB4344-69D0-492A-9468-9A89A8E9B571}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
class IMouseCursor(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that set the system cursor.'
    _iid_ = GUID('{F91752EF-3339-482F-AD92-4B752C98E744}')
    _idlflags_ = ['oleautomation']
MouseCursor._com_interfaces_ = [IMouseCursor]

IPropertyPageContext._methods_ = [
    COMMETHOD(['propget', helpstring(u"The page's priority relative to other pages that interact with the same object.  The higher the value, the higher the priority.")], HRESULT, 'Priority',
              ( ['retval', 'out'], POINTER(c_int), 'Priority' )),
    COMMETHOD([helpstring(u'Check if property page applies to the specified set of objects.  Signature corresponds to IPropertyPage::SetObjects.')], HRESULT, 'Applies',
              ( ['in'], VARIANT, 'unkArray' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Applies' )),
    COMMETHOD([helpstring(u'Create a new object using the specified object as a template.  The kind argument may be NULL if the page interacts with only a single object.')], HRESULT, 'CreateCompatibleObject',
              ( ['in'], VARIANT, 'kind' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'pNewObject' )),
    COMMETHOD([helpstring(u'Apply the property page settings to the specified object.')], HRESULT, 'QueryObject',
              ( ['in'], VARIANT, 'theObject' )),
    COMMETHOD([helpstring(u'Returns the help file name for the specified control.')], HRESULT, 'GetHelpFile',
              ( ['in'], c_int, 'controlID' ),
              ( ['retval', 'out'], POINTER(BSTR), 'HelpFile' )),
    COMMETHOD([helpstring(u'Returns the help ID for the specified control.')], HRESULT, 'GetHelpId',
              ( ['in'], c_int, 'controlID' ),
              ( ['retval', 'out'], POINTER(c_int), 'helpID' )),
    COMMETHOD([helpstring(u'Property sheet calls this when cancel button is pressed.')], HRESULT, 'Cancel'),
]
################################################################
## code template for IPropertyPageContext implementation
##class IPropertyPageContext_Impl(object):
##    def GetHelpFile(self, controlID):
##        u'Returns the help file name for the specified control.'
##        #return HelpFile
##
##    def CreateCompatibleObject(self, kind):
##        u'Create a new object using the specified object as a template.  The kind argument may be NULL if the page interacts with only a single object.'
##        #return pNewObject
##
##    def GetHelpId(self, controlID):
##        u'Returns the help ID for the specified control.'
##        #return helpID
##
##    @property
##    def Priority(self):
##        u"The page's priority relative to other pages that interact with the same object.  The higher the value, the higher the priority."
##        #return Priority
##
##    def Applies(self, unkArray):
##        u'Check if property page applies to the specified set of objects.  Signature corresponds to IPropertyPage::SetObjects.'
##        #return Applies
##
##    def Cancel(self):
##        u'Property sheet calls this when cancel button is pressed.'
##        #return 
##
##    def QueryObject(self, theObject):
##        u'Apply the property page settings to the specified object.'
##        #return 
##

class IAppROTEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to events that occur on the Esri application running object table.'
    _iid_ = GUID('{FABC30FA-D273-11D2-9F36-00C04F6BC61A}')
    _idlflags_ = ['oleautomation']
IAppROTEvents._methods_ = [
    COMMETHOD([helpstring(u'Occurs when an application reference is added to the table.')], HRESULT, 'AppAdded',
              ( ['in'], POINTER(IApplication), 'pApp' )),
    COMMETHOD([helpstring(u'Occurs when an application reference is removed from the table.')], HRESULT, 'AppRemoved',
              ( ['in'], POINTER(IApplication), 'pApp' )),
]
################################################################
## code template for IAppROTEvents implementation
##class IAppROTEvents_Impl(object):
##    def AppRemoved(self, pApp):
##        u'Occurs when an application reference is removed from the table.'
##        #return 
##
##    def AppAdded(self, pApp):
##        u'Occurs when an application reference is added to the table.'
##        #return 
##

class IDockableWindowInitialPlacement(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides initial placement for dockable windows.'
    _iid_ = GUID('{1EC80980-7A02-426D-BD2B-C6D3BEB2ED54}')
    _idlflags_ = ['oleautomation']
IDockableWindowInitialPlacement._methods_ = [
    COMMETHOD(['propget', helpstring(u'The default height of the dockable window in pixels.')], HRESULT, 'Height',
              ( ['retval', 'out'], POINTER(c_int), 'Height' )),
    COMMETHOD(['propget', helpstring(u'The default width of the dockable window in pixels.')], HRESULT, 'Width',
              ( ['retval', 'out'], POINTER(c_int), 'Width' )),
    COMMETHOD(['propget', helpstring(u'The location where this dockable window should dock by default.')], HRESULT, 'DockPosition',
              ( ['retval', 'out'], POINTER(esriDockFlags), 'dockFlags' )),
    COMMETHOD(['propget', helpstring(u'An alternate dockable window this dockable window should dock relative to.')], HRESULT, 'Neighbor',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID)), 'uid' )),
]
################################################################
## code template for IDockableWindowInitialPlacement implementation
##class IDockableWindowInitialPlacement_Impl(object):
##    @property
##    def DockPosition(self):
##        u'The location where this dockable window should dock by default.'
##        #return dockFlags
##
##    @property
##    def Width(self):
##        u'The default width of the dockable window in pixels.'
##        #return Width
##
##    @property
##    def Neighbor(self):
##        u'An alternate dockable window this dockable window should dock relative to.'
##        #return uid
##
##    @property
##    def Height(self):
##        u'The default height of the dockable window in pixels.'
##        #return Height
##

class ITemplates(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that query the templates collection.'
    _iid_ = GUID('{CE7C5749-3921-11D2-94CF-080009EEBECB}')
    _idlflags_ = ['oleautomation']
ITemplates._methods_ = [
    COMMETHOD(['propget', helpstring(u'The number of templates associated with the current document.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'The pathname to the template at the given index.')], HRESULT, 'Item',
              ( ['in'], c_int, 'Index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'pathName' )),
]
################################################################
## code template for ITemplates implementation
##class ITemplates_Impl(object):
##    @property
##    def Count(self):
##        u'The number of templates associated with the current document.'
##        #return Count
##
##    @property
##    def Item(self, Index):
##        u'The pathname to the template at the given index.'
##        #return pathName
##

IMessageDialog._methods_ = [
    COMMETHOD([helpstring(u'Shows the dialog with a message.')], HRESULT, 'DoModal',
              ( ['in'], BSTR, 'Title' ),
              ( ['in'], BSTR, 'Message' ),
              ( ['in'], BSTR, 'OKButtonMessage' ),
              ( ['in'], BSTR, 'CANCELButtonMessage' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hWnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'okPressed' )),
]
################################################################
## code template for IMessageDialog implementation
##class IMessageDialog_Impl(object):
##    def DoModal(self, Title, Message, OKButtonMessage, CANCELButtonMessage, hWnd):
##        u'Shows the dialog with a message.'
##        #return okPressed
##

class IListDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that work with a dialog for displaying a list.'
    _iid_ = GUID('{5F399A16-0B7D-11D2-8C1E-0000F8774F55}')
    _idlflags_ = ['oleautomation']
IListDialog._methods_ = [
    COMMETHOD([helpstring(u'Adds a string to the list that the dialog will show. These strings will be sorted in alphabetical order.')], HRESULT, 'AddString',
              ( [], BSTR, 'Choice' )),
    COMMETHOD(['propget', helpstring(u'The index of the string chosen (use after calling DoModal). Strings are numbered starting at 0 in the order that they were added, not the order that they appear in the dialog.')], HRESULT, 'Choice',
              ( ['retval', 'out'], POINTER(c_int), 'Index' )),
    COMMETHOD([helpstring(u'Displays the list dialog and lets the user select a choice. Returns false if the user hits the cancel button.')], HRESULT, 'DoModal',
              ( ['in'], BSTR, 'Title' ),
              ( ['in'], c_int, 'initialChoice' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hWnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pOK' )),
]
################################################################
## code template for IListDialog implementation
##class IListDialog_Impl(object):
##    def DoModal(self, Title, initialChoice, hWnd):
##        u'Displays the list dialog and lets the user select a choice. Returns false if the user hits the cancel button.'
##        #return pOK
##
##    def AddString(self, Choice):
##        u'Adds a string to the list that the dialog will show. These strings will be sorted in alphabetical order.'
##        #return 
##
##    @property
##    def Choice(self):
##        u'The index of the string chosen (use after calling DoModal). Strings are numbered starting at 0 in the order that they were added, not the order that they appear in the dialog.'
##        #return Index
##

class IGetUserAndPasswordDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that work with a dialog for getting user and password information.'
    _iid_ = GUID('{B7F5DDFF-1301-47A2-901A-D38F364544D2}')
    _idlflags_ = ['oleautomation']
IGetUserAndPasswordDialog._methods_ = [
    COMMETHOD(['propget', helpstring(u'The user name entered in the dialog.')], HRESULT, 'UserName',
              ( ['retval', 'out'], POINTER(BSTR), 'UserName' )),
    COMMETHOD(['propget', helpstring(u'The password entered in the dialog.')], HRESULT, 'Password',
              ( ['retval', 'out'], POINTER(BSTR), 'Password' )),
    COMMETHOD([helpstring(u'Shows the dialog.')], HRESULT, 'DoModal',
              ( ['in'], BSTR, 'dialogTitle' ),
              ( ['in'], BSTR, 'stringLabel' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hWnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'okPressed' )),
]
################################################################
## code template for IGetUserAndPasswordDialog implementation
##class IGetUserAndPasswordDialog_Impl(object):
##    @property
##    def UserName(self):
##        u'The user name entered in the dialog.'
##        #return UserName
##
##    def DoModal(self, dialogTitle, stringLabel, hWnd):
##        u'Shows the dialog.'
##        #return okPressed
##
##    @property
##    def Password(self):
##        u'The password entered in the dialog.'
##        #return Password
##


# values for enumeration 'esriCustomizationEvent'
esriCEAddCategory = 0
esriCEAddCommand = 1
esriCEShowCustDlg = 2
esriCEShowVBAIDE = 3
esriCEInvokeCommand = 4
esriCEShowCustCtxMenu = 5
esriCERunVBACode = 6
esriCEEditVBACode = 7
esriCustomizationEvent = c_int # enum
class Tool(CoClass):
    u'Tool CoType.'
    _reg_clsid_ = GUID('{DA53DC37-E97C-4997-BBDE-93F2BE061EC0}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
Tool._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.ICommand, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.ITool]

class PercentagePropertyPage(CoClass):
    u'Percentage Format Property Page.'
    _reg_clsid_ = GUID('{FCF40D6D-C91F-11D2-AAF8-000000000000}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
PercentagePropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IPropertyPage, IPropertyPageContext, IComPropertyPage, IComPropertyPage2]

class IColorBrowser(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Color Browser Dialog.'
    _iid_ = GUID('{E82A1A9B-7B12-11D1-946C-080009EEBECB}')
    _idlflags_ = ['oleautomation']
class IColorSelector(IColorBrowser):
    _case_insensitive_ = True
    u'Provides access to members that control the Color Selector Dialog.'
    _iid_ = GUID('{569C3921-01BA-11D3-9F38-00C04F6BC709}')
    _idlflags_ = ['oleautomation']
IColorBrowser._methods_ = [
    COMMETHOD(['propput', helpstring(u'Color edited by the browser.')], HRESULT, 'Color',
              ( ['in'], POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IColor), 'Color' )),
    COMMETHOD(['propget', helpstring(u'Color edited by the browser.')], HRESULT, 'Color',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IColor)), 'Color' )),
    COMMETHOD([helpstring(u'Show the browser.')], HRESULT, 'DoModal',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hWnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ok' )),
]
################################################################
## code template for IColorBrowser implementation
##class IColorBrowser_Impl(object):
##    def _get(self):
##        u'Color edited by the browser.'
##        #return Color
##    def _set(self, Color):
##        u'Color edited by the browser.'
##    Color = property(_get, _set, doc = _set.__doc__)
##
##    def DoModal(self, hWnd):
##        u'Show the browser.'
##        #return ok
##

IColorSelector._methods_ = [
    COMMETHOD([helpstring(u'Initialize Popup Position.')], HRESULT, 'InitPopupPosition',
              ( ['in'], c_int, 'parentLeft' ),
              ( [], c_int, 'parentTop' ),
              ( [], c_int, 'parentRight' ),
              ( [], c_int, 'parentBottom' ),
              ( [], VARIANT_BOOL, 'aboveParent' )),
]
################################################################
## code template for IColorSelector implementation
##class IColorSelector_Impl(object):
##    def InitPopupPosition(self, parentLeft, parentTop, parentRight, parentBottom, aboveParent):
##        u'Initialize Popup Position.'
##        #return 
##

class IDockableWindowInitialPlacementNeighbors(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides initial placement for dockable windows.'
    _iid_ = GUID('{BBF9E75E-3675-45C9-A6A6-0A3C6D0AD1B9}')
    _idlflags_ = ['oleautomation']
IDockableWindowInitialPlacementNeighbors._methods_ = [
    COMMETHOD(['propget', helpstring(u'Number of neighbors.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Get Neighbors')], HRESULT, 'NeighborAt',
              ( ['in'], c_int, 'Index' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID)), 'uid' )),
]
################################################################
## code template for IDockableWindowInitialPlacementNeighbors implementation
##class IDockableWindowInitialPlacementNeighbors_Impl(object):
##    @property
##    def Count(self):
##        u'Number of neighbors.'
##        #return Count
##
##    @property
##    def NeighborAt(self, Index):
##        u'Get Neighbors'
##        #return uid
##

class IFileOpenHandler(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that handle the opening of files.'
    _iid_ = GUID('{316F1E91-30B6-43FE-9FD8-9C08C5394EB8}')
    _idlflags_ = ['oleautomation']
IFileOpenHandler._methods_ = [
    COMMETHOD([helpstring(u'Indicates if the specified filename can be opened.')], HRESULT, 'CanOpen',
              ( ['in'], BSTR, 'filename' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'CanOpen' )),
    COMMETHOD([helpstring(u'Opens the filename.')], HRESULT, 'Open',
              ( ['in'], BSTR, 'filename' )),
]
################################################################
## code template for IFileOpenHandler implementation
##class IFileOpenHandler_Impl(object):
##    def CanOpen(self, filename):
##        u'Indicates if the specified filename can be opened.'
##        #return CanOpen
##
##    def Open(self, filename):
##        u'Opens the filename.'
##        #return 
##

class CustomPropertyPage(CoClass):
    u'Custom Number Format Property Page.'
    _reg_clsid_ = GUID('{FCF40D6E-C91F-11D2-AAF8-000000000000}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
CustomPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IPropertyPage, IPropertyPageContext, IComPropertyPage, IComPropertyPage2]

class ListDialog(CoClass):
    u'List Dialog object.'
    _reg_clsid_ = GUID('{5F399A17-0B7D-11D2-8C1E-0000F8774F55}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
ListDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IListDialog]

class IComPropertySheet2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that extend the IComPropertySheet interface with methods for setting the active page.'
    _iid_ = GUID('{C7FB79B7-41A6-4F58-B58B-C39FB83AAA0A}')
    _idlflags_ = []
IComPropertySheet2._methods_ = [
    COMMETHOD(['propput', helpstring(u'The UID of the page to set active.')], HRESULT, 'ActivePageUID',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID), 'rhs' )),
    COMMETHOD([helpstring(u'The UID of the active page.')], HRESULT, 'GetActivePage',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISet), 'pObjects' ),
              ( ['retval', 'out'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pGUID' )),
]
################################################################
## code template for IComPropertySheet2 implementation
##class IComPropertySheet2_Impl(object):
##    def GetActivePage(self, pObjects):
##        u'The UID of the active page.'
##        #return pGUID
##
##    def _set(self, rhs):
##        u'The UID of the page to set active.'
##    ActivePageUID = property(fset = _set, doc = _set.__doc__)
##

class IMenuItem(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to extended notifications for commands on menus.'
    _iid_ = GUID('{2B718169-1B85-11D2-94B6-080009EEBECB}')
    _idlflags_ = ['oleautomation']
class ICommandBar(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that modify a commandbar.'
    _iid_ = GUID('{32E9D003-B867-11D1-947B-080009EEBECB}')
    _idlflags_ = ['oleautomation']
IMenuItem._methods_ = [
    COMMETHOD([helpstring(u'Called on commands just before their parent menu is displayed.')], HRESULT, 'OnPopup',
              ( ['in'], POINTER(ICommandBar), 'pParentMenu' )),
    COMMETHOD([helpstring(u'Called on commands after their parent menu is closed.')], HRESULT, 'OnClose'),
]
################################################################
## code template for IMenuItem implementation
##class IMenuItem_Impl(object):
##    def OnClose(self):
##        u'Called on commands after their parent menu is closed.'
##        #return 
##
##    def OnPopup(self, pParentMenu):
##        u'Called on commands just before their parent menu is displayed.'
##        #return 
##

class IDockableWindowManager(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to a method that finds a dockable window in the application.'
    _iid_ = GUID('{3EE6D0C2-E3F2-11D3-A679-0008C7DF97B9}')
    _idlflags_ = ['oleautomation']
IDockableWindowManager._methods_ = [
    COMMETHOD([helpstring(u'Finds a dockable window looking first in the collection and then in the category.')], HRESULT, 'GetDockableWindow',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID), 'dockWnd' ),
              ( ['retval', 'out'], POINTER(POINTER(IDockableWindow)), 'Item' )),
]
################################################################
## code template for IDockableWindowManager implementation
##class IDockableWindowManager_Impl(object):
##    def GetDockableWindow(self, dockWnd):
##        u'Finds a dockable window looking first in the collection and then in the category.'
##        #return Item
##

class ScientificPropertyPage(CoClass):
    u'Scientific Format Property Page.'
    _reg_clsid_ = GUID('{FECB8199-C694-11D2-9F34-00C04F6BC78E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
ScientificPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IPropertyPage, IPropertyPageContext, IComPropertyPage, IComPropertyPage2]

class IModelessFrame(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to a means of displaying modeless dialogs implemented with VisualBasic.'
    _iid_ = GUID('{06861E43-9020-49EB-B949-824552EE2DE0}')
    _idlflags_ = ['oleautomation']
IModelessFrame._methods_ = [
    COMMETHOD([helpstring(u'Creates the modeless frame around the specified VisualBasic form object.')], HRESULT, 'Create',
              ( ['in'], POINTER(IDispatch), 'vbForm' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the modeless frame is visible.')], HRESULT, 'Visible',
              ( ['in'], VARIANT_BOOL, 'bVisible' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the modeless frame is visible.')], HRESULT, 'Visible',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bVisible' )),
    COMMETHOD(['propput', helpstring(u'The caption of the modeless frame.')], HRESULT, 'Caption',
              ( ['in'], BSTR, 'pCaption' )),
    COMMETHOD(['propget', helpstring(u'The caption of the modeless frame.')], HRESULT, 'Caption',
              ( ['retval', 'out'], POINTER(BSTR), 'pCaption' )),
]
################################################################
## code template for IModelessFrame implementation
##class IModelessFrame_Impl(object):
##    def _get(self):
##        u'Indicates if the modeless frame is visible.'
##        #return bVisible
##    def _set(self, bVisible):
##        u'Indicates if the modeless frame is visible.'
##    Visible = property(_get, _set, doc = _set.__doc__)
##
##    def Create(self, vbForm):
##        u'Creates the modeless frame around the specified VisualBasic form object.'
##        #return 
##
##    def _get(self):
##        u'The caption of the modeless frame.'
##        #return pCaption
##    def _set(self, pCaption):
##        u'The caption of the modeless frame.'
##    Caption = property(_get, _set, doc = _set.__doc__)
##

class ISmallBitmapProvider(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control objects that provide a small 8x8 pixel bitmap.'
    _iid_ = GUID('{92C77DB5-C995-11D1-876B-0000F8751720}')
    _idlflags_ = ['oleautomation']
ISmallBitmapProvider._methods_ = [
    COMMETHOD(['propget', helpstring(u'Handle to bitmap.')], HRESULT, 'SmallBitmap',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'Bitmap' )),
]
################################################################
## code template for ISmallBitmapProvider implementation
##class ISmallBitmapProvider_Impl(object):
##    @property
##    def SmallBitmap(self):
##        u'Handle to bitmap.'
##        #return Bitmap
##

class IArcToolboxFind(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u"Provides access to this tool's properties for the ArcToolbox Find tool."
    _iid_ = GUID('{CA787E4D-17A0-11D4-A629-0008C711C8C1}')
    _idlflags_ = ['oleautomation']
IArcToolboxFind._methods_ = [
    COMMETHOD(['propget', helpstring(u'The ArcCommands used by this tool.')], HRESULT, 'ArcCommands',
              ( ['retval', 'out'], POINTER(BSTR), 'commands' )),
    COMMETHOD(['propget', helpstring(u'Keywords used to find this tool with the ArcToolbox Find tool.')], HRESULT, 'Keywords',
              ( ['retval', 'out'], POINTER(BSTR), 'Keywords' )),
]
################################################################
## code template for IArcToolboxFind implementation
##class IArcToolboxFind_Impl(object):
##    @property
##    def Keywords(self):
##        u'Keywords used to find this tool with the ArcToolbox Find tool.'
##        #return Keywords
##
##    @property
##    def ArcCommands(self):
##        u'The ArcCommands used by this tool.'
##        #return commands
##

class AnglePropertyPage(CoClass):
    u'Angle Format Property Page.'
    _reg_clsid_ = GUID('{FECB819A-C694-11D2-9F34-00C04F6BC78E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
AnglePropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IPropertyPage, IPropertyPageContext, IComPropertyPage, IComPropertyPage2]

IComPropertySheetID._methods_ = [
    COMMETHOD(['propput', helpstring(u'Registry key for sheet settings.')], HRESULT, 'RegistryKey',
              ( ['in'], BSTR, 'idStr' )),
    COMMETHOD(['propget', helpstring(u'Registry key for sheet settings.')], HRESULT, 'RegistryKey',
              ( ['retval', 'out'], POINTER(BSTR), 'idStr' )),
]
################################################################
## code template for IComPropertySheetID implementation
##class IComPropertySheetID_Impl(object):
##    def _get(self):
##        u'Registry key for sheet settings.'
##        #return idStr
##    def _set(self, idStr):
##        u'Registry key for sheet settings.'
##    RegistryKey = property(_get, _set, doc = _set.__doc__)
##

class IMenuItem2(IMenuItem):
    _case_insensitive_ = True
    u'Provides access to extended notifications for commands on menus.'
    _iid_ = GUID('{AD688106-2D34-4CBC-8A3D-60155C837F6E}')
    _idlflags_ = ['oleautomation']
IMenuItem2._methods_ = [
]
################################################################
## code template for IMenuItem2 implementation
##class IMenuItem2_Impl(object):

class DirectionPropertyPage(CoClass):
    u'Direction Format Property Page.'
    _reg_clsid_ = GUID('{ECB196FE-47DC-4F3A-AE2A-1CE2EBFB6DC2}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
DirectionPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IPropertyPage, IPropertyPageContext, IComPropertyPage, IComPropertyPage2]

class IPropertyPageSiteConfig(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that configure a property page site.'
    _iid_ = GUID('{2645F960-B557-4B7B-B017-10F10159B78B}')
    _idlflags_ = ['oleautomation']
IPropertyPageSiteConfig._methods_ = [
    COMMETHOD(['propput', helpstring(u'The window handle of the site.')], HRESULT, 'hWnd',
              ( ['in'], c_int, 'hWnd' )),
    COMMETHOD(['propget', helpstring(u'The window handle of the site.')], HRESULT, 'hWnd',
              ( ['retval', 'out'], POINTER(c_int), 'hWnd' )),
    COMMETHOD(['propputref', helpstring(u'The page contained by the site.')], HRESULT, 'Page',
              ( ['in'], POINTER(IPropertyPage), 'Page' )),
    COMMETHOD(['propget', helpstring(u'The page contained by the site.')], HRESULT, 'Page',
              ( ['retval', 'out'], POINTER(POINTER(IPropertyPage)), 'Page' )),
]
################################################################
## code template for IPropertyPageSiteConfig implementation
##class IPropertyPageSiteConfig_Impl(object):
##    def _get(self):
##        u'The window handle of the site.'
##        #return hWnd
##    def _set(self, hWnd):
##        u'The window handle of the site.'
##    hWnd = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Page(self, Page):
##        u'The page contained by the site.'
##        #return 
##

class ColorPageSite(CoClass):
    u'Esri custom color dialog pagesite.'
    _reg_clsid_ = GUID('{20CD4002-8F3D-11D0-8590-0800091A2A72}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
ColorPageSite._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IPropertyPageSite, IComPropertyPageSite]

class IShortcutMenu(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Indicator interface that identifies a context menu.'
    _iid_ = GUID('{68E13AF7-F1BF-11D1-949F-080009EEBECB}')
    _idlflags_ = ['oleautomation']
IShortcutMenu._methods_ = [
]
################################################################
## code template for IShortcutMenu implementation
##class IShortcutMenu_Impl(object):

class ISymbolPickerDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the SymbolPicker dialog.'
    _iid_ = GUID('{5C8DF895-D553-41F2-B5D3-2703EFE0B07A}')
    _idlflags_ = ['oleautomation']
ISymbolPickerDialog._methods_ = [
    COMMETHOD(['propget', helpstring(u'The name of the Selected Font.')], HRESULT, 'SelectedFontName',
              ( ['retval', 'out'], POINTER(BSTR), 'FontFaceName' )),
    COMMETHOD(['propput', helpstring(u'The name of the Selected Font.')], HRESULT, 'SelectedFontName',
              ( ['in'], BSTR, 'FontFaceName' )),
    COMMETHOD(['propget', helpstring(u'The Selected unicode Character.')], HRESULT, 'SelectedChar',
              ( ['retval', 'out'], POINTER(c_int), 'iCharUnicode' )),
    COMMETHOD(['propput', helpstring(u'The Selected unicode Character.')], HRESULT, 'SelectedChar',
              ( ['in'], c_int, 'iCharUnicode' )),
    COMMETHOD([helpstring(u'Shows modal version of dialog.')], HRESULT, 'DoModal',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hWndParent' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pOK' )),
]
################################################################
## code template for ISymbolPickerDialog implementation
##class ISymbolPickerDialog_Impl(object):
##    def DoModal(self, hWndParent):
##        u'Shows modal version of dialog.'
##        #return pOK
##
##    def _get(self):
##        u'The name of the Selected Font.'
##        #return FontFaceName
##    def _set(self, FontFaceName):
##        u'The name of the Selected Font.'
##    SelectedFontName = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The Selected unicode Character.'
##        #return iCharUnicode
##    def _set(self, iCharUnicode):
##        u'The Selected unicode Character.'
##    SelectedChar = property(_get, _set, doc = _set.__doc__)
##


# values for enumeration 'CustomizationErrors'
cust_err_builtin_only = -2147221404
cust_err_invalid_on_builtin = -2147221403
cust_err_invalid_on_commandbar = -2147221402
cust_err_invalid_type = -2147221401
cust_err_cmdNotAvail = -2147221400
cust_err_invalid = -2147221399
cust_err_alreadyLocked = -2147221392
cust_err_badPasswordLen = -2147221391
cust_err_no_template_lock = -2147221390
CustomizationErrors = c_int # enum
class StyleGalleryItem(CoClass):
    u'An item in the Style Gallery.'
    _reg_clsid_ = GUID('{AC0E9829-91CB-11D1-8813-080009EC732A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
StyleGalleryItem._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IStyleGalleryItem, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IStyleGalleryItem2, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IStyleGalleryItem3, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone]

class INumberFormatDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that work with the number format dialog.'
    _iid_ = GUID('{88002C09-939A-11D2-AE73-080009EC732A}')
    _idlflags_ = ['oleautomation']
INumberFormatDialog._methods_ = [
    COMMETHOD(['propget', helpstring(u'The current number format object.')], HRESULT, 'NumberFormat',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.INumberFormat)), 'format' )),
    COMMETHOD(['propput', helpstring(u'The current number format object.')], HRESULT, 'NumberFormat',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.INumberFormat), 'format' )),
    COMMETHOD([helpstring(u'Displays the number format dialog.')], HRESULT, 'DoModal',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hWnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'okPressed' )),
]
################################################################
## code template for INumberFormatDialog implementation
##class INumberFormatDialog_Impl(object):
##    def DoModal(self, hWnd):
##        u'Displays the number format dialog.'
##        #return okPressed
##
##    def _get(self):
##        u'The current number format object.'
##        #return format
##    def _set(self, format):
##        u'The current number format object.'
##    NumberFormat = property(_get, _set, doc = _set.__doc__)
##

class IApplicationIdentifyDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u"Provides access to class ID of application's identify dialog."
    _iid_ = GUID('{B6165DDF-808E-11D4-80F3-00C04FA0ADF8}')
    _idlflags_ = []
IApplicationIdentifyDialog._methods_ = [
    COMMETHOD([helpstring(u'Returns the identify dialog ID.')], HRESULT, 'GetClassID',
              ( ['out'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'classID' )),
]
################################################################
## code template for IApplicationIdentifyDialog implementation
##class IApplicationIdentifyDialog_Impl(object):
##    def GetClassID(self):
##        u'Returns the identify dialog ID.'
##        #return classID
##

class RatePropertyPage(CoClass):
    u'Rate Format Property Page.'
    _reg_clsid_ = GUID('{FCF40D6F-C91F-11D2-AAF8-000000000000}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
RatePropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IPropertyPage, IPropertyPageContext, IComPropertyPage, IComPropertyPage2]

IPropertyPage._methods_ = [
    COMMETHOD([], HRESULT, 'SetPageSite',
              ( ['in'], POINTER(IPropertyPageSite), 'pPageSite' )),
    COMMETHOD([], HRESULT, 'Activate',
              ( ['in'], wireHWND, 'hWndParent' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.tagRECT), 'pRect' ),
              ( ['in'], c_int, 'bModal' )),
    COMMETHOD([], HRESULT, 'Deactivate'),
    COMMETHOD([], HRESULT, 'GetPageInfo',
              ( ['out'], POINTER(tagPROPPAGEINFO), 'pPageInfo' )),
    COMMETHOD([], HRESULT, 'SetObjects',
              ( ['in'], c_ulong, 'cObjects' ),
              ( ['in'], POINTER(POINTER(IUnknown)), 'ppUnk' )),
    COMMETHOD([], HRESULT, 'Show',
              ( ['in'], c_uint, 'nCmdShow' )),
    COMMETHOD([], HRESULT, 'Move',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.tagRECT), 'pRect' )),
    COMMETHOD([], HRESULT, 'IsPageDirty'),
    COMMETHOD([], HRESULT, 'Apply'),
    COMMETHOD([], HRESULT, 'Help',
              ( ['in'], WSTRING, 'pszHelpDir' )),
    COMMETHOD([], HRESULT, 'TranslateAccelerator',
              ( ['in'], POINTER(tagMSG), 'pMsg' )),
]
################################################################
## code template for IPropertyPage implementation
##class IPropertyPage_Impl(object):
##    def IsPageDirty(self):
##        '-no docstring-'
##        #return 
##
##    def Activate(self, hWndParent, pRect, bModal):
##        '-no docstring-'
##        #return 
##
##    def Help(self, pszHelpDir):
##        '-no docstring-'
##        #return 
##
##    def Show(self, nCmdShow):
##        '-no docstring-'
##        #return 
##
##    def Deactivate(self):
##        '-no docstring-'
##        #return 
##
##    def SetPageSite(self, pPageSite):
##        '-no docstring-'
##        #return 
##
##    def TranslateAccelerator(self, pMsg):
##        '-no docstring-'
##        #return 
##
##    def Move(self, pRect):
##        '-no docstring-'
##        #return 
##
##    def Apply(self):
##        '-no docstring-'
##        #return 
##
##    def GetPageInfo(self):
##        '-no docstring-'
##        #return pPageInfo
##
##    def SetObjects(self, cObjects, ppUnk):
##        '-no docstring-'
##        #return 
##

class IAcceleratorHook(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to a means to decide if a virtual key should act as an accelerator.'
    _iid_ = GUID('{D4511A0E-1D47-461E-BC44-2475545EE2D9}')
    _idlflags_ = ['oleautomation']
IAcceleratorHook._methods_ = [
    COMMETHOD([helpstring(u'Return true if the framework should carry out the action associated with this virtual key.')], HRESULT, 'CheckAccelerator',
              ( ['in'], c_int, 'vkey' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'check' )),
]
################################################################
## code template for IAcceleratorHook implementation
##class IAcceleratorHook_Impl(object):
##    def CheckAccelerator(self, vkey):
##        u'Return true if the framework should carry out the action associated with this virtual key.'
##        #return check
##

class IDocument(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Provides access to other objects in the document.'
    _iid_ = GUID('{3E927177-307A-11D2-94C9-080009EEBECB}')
    _idlflags_ = ['dual', 'oleautomation']
class ICommandItem(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that define a command item.'
    _iid_ = GUID('{423B7723-B858-11D1-947B-080009EEBECB}')
    _idlflags_ = ['oleautomation']
class ICustomizationFilter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that define a customization filter.'
    _iid_ = GUID('{792D7E87-7993-11D2-A2D1-0000F8774FB5}')
    _idlflags_ = ['oleautomation']
IApplication._methods_ = [
    COMMETHOD([dispid(1610743808), helpstring(u'The name of this application.'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD([dispid(1610743809), helpstring(u'The document that is currently loaded in the application.'), 'propget'], HRESULT, 'Document',
              ( ['retval', 'out'], POINTER(POINTER(IDocument)), 'doc' )),
    COMMETHOD([dispid(1610743810), helpstring(u'The statusbar of this application.'), 'propget'], HRESULT, 'StatusBar',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStatusBar)), 'StatusBar' )),
    COMMETHOD([dispid(1610743811), helpstring(u'Displays the specified dialog in the application.')], HRESULT, 'ShowDialog',
              ( ['in'], c_int, 'dialogID' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'bShow' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'result' )),
    COMMETHOD([dispid(1610743812), helpstring(u'Indicates if the specified dialog is visible in the application.')], HRESULT, 'IsDialogVisible',
              ( ['in'], c_int, 'dialogID' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bVisible' )),
    COMMETHOD([dispid(1610743813), helpstring(u'The currently selected tool.'), 'propget'], HRESULT, 'CurrentTool',
              ( ['retval', 'out'], POINTER(POINTER(ICommandItem)), 'Tool' )),
    COMMETHOD([dispid(1610743813), helpstring(u'The currently selected tool.'), 'propputref'], HRESULT, 'CurrentTool',
              ( ['in'], POINTER(ICommandItem), 'Tool' )),
    COMMETHOD([dispid(1610743815), helpstring(u'The Visual Basic Environment.'), 'propget'], HRESULT, 'VBE',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ppVBE' )),
    COMMETHOD([dispid(1610743816), helpstring(u'Creates a new document in this application.')], HRESULT, 'NewDocument',
              ( ['in', 'optional'], VARIANT_BOOL, 'selectTemplate', False ),
              ( ['in', 'optional'], BSTR, 'templatePath' )),
    COMMETHOD([dispid(1610743817), helpstring(u'Opens a document in this application.')], HRESULT, 'OpenDocument',
              ( ['in', 'optional'], BSTR, 'path' )),
    COMMETHOD([dispid(1610743818), helpstring(u'Saves the document that is currently open in this application.')], HRESULT, 'SaveDocument',
              ( ['in', 'optional'], BSTR, 'saveAsPath' )),
    COMMETHOD([dispid(1610743819), helpstring(u'Saves the document that is currently open in this application to a different file.')], HRESULT, 'SaveAsDocument',
              ( ['in', 'optional'], BSTR, 'saveAsPath' ),
              ( ['in', 'optional'], VARIANT_BOOL, 'saveAsCopy', False )),
    COMMETHOD([dispid(1610743820), helpstring(u'Displays how the document will look like when it is printed.')], HRESULT, 'PrintPreview'),
    COMMETHOD([dispid(1610743821), helpstring(u'Displays the Print dialog.')], HRESULT, 'PrintDocument'),
    COMMETHOD([dispid(1610743822), helpstring(u"Locks the application's user interface against any customizations.")], HRESULT, 'LockCustomization',
              ( ['in'], BSTR, 'Password' ),
              ( ['in', 'optional'], POINTER(ICustomizationFilter), 'custFilter' )),
    COMMETHOD([dispid(1610743823), helpstring(u'Unlocks previous user interface customization lock.')], HRESULT, 'UnlockCustomization',
              ( ['in'], BSTR, 'Password' )),
    COMMETHOD([dispid(1610743824), helpstring(u'Redraws the application window.')], HRESULT, 'RefreshWindow'),
    COMMETHOD([dispid(1610743825), helpstring(u'The templates collection.'), 'propget'], HRESULT, 'Templates',
              ( ['retval', 'out'], POINTER(POINTER(ITemplates)), 'Templates' )),
    COMMETHOD([dispid(1610743826), helpstring(u"The handle of the application's window."), 'propget'], HRESULT, 'hWnd',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'hWnd' )),
    COMMETHOD([dispid(1610743827), helpstring(u'Finds an extension by its name.')], HRESULT, 'FindExtensionByName',
              ( ['in'], BSTR, 'extensionName' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IExtension)), 'extension' )),
    COMMETHOD([dispid(1610743828), helpstring(u'Finds an extension by its CLSID.')], HRESULT, 'FindExtensionByCLSID',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID), 'extensionCLSID' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IExtension)), 'extension' )),
    COMMETHOD([dispid(1610743829), helpstring(u'Terminates the application.')], HRESULT, 'Shutdown'),
    COMMETHOD([dispid(1610743830), helpstring(u'Indicates if the application window is visible.'), 'propget'], HRESULT, 'Visible',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Visible' )),
    COMMETHOD([dispid(1610743830), helpstring(u'Indicates if the application window is visible.'), 'propput'], HRESULT, 'Visible',
              ( ['in'], VARIANT_BOOL, 'Visible' )),
    COMMETHOD([dispid(1610743832), helpstring(u'The caption of this application.'), 'propput'], HRESULT, 'Caption',
              ( ['in'], BSTR, 'Caption' )),
    COMMETHOD([dispid(1610743832), helpstring(u'The caption of this application.'), 'propget'], HRESULT, 'Caption',
              ( ['retval', 'out'], POINTER(BSTR), 'Caption' )),
]
################################################################
## code template for IApplication implementation
##class IApplication_Impl(object):
##    @property
##    def StatusBar(self):
##        u'The statusbar of this application.'
##        #return StatusBar
##
##    @property
##    def VBE(self):
##        u'The Visual Basic Environment.'
##        #return ppVBE
##
##    @property
##    def hWnd(self):
##        u"The handle of the application's window."
##        #return hWnd
##
##    def IsDialogVisible(self, dialogID):
##        u'Indicates if the specified dialog is visible in the application.'
##        #return bVisible
##
##    def OpenDocument(self, path):
##        u'Opens a document in this application.'
##        #return 
##
##    @property
##    def Document(self):
##        u'The document that is currently loaded in the application.'
##        #return doc
##
##    @property
##    def Name(self):
##        u'The name of this application.'
##        #return Name
##
##    @property
##    def Templates(self):
##        u'The templates collection.'
##        #return Templates
##
##    def SaveAsDocument(self, saveAsPath, saveAsCopy):
##        u'Saves the document that is currently open in this application to a different file.'
##        #return 
##
##    def PrintDocument(self):
##        u'Displays the Print dialog.'
##        #return 
##
##    def UnlockCustomization(self, Password):
##        u'Unlocks previous user interface customization lock.'
##        #return 
##
##    def FindExtensionByCLSID(self, extensionCLSID):
##        u'Finds an extension by its CLSID.'
##        #return extension
##
##    def FindExtensionByName(self, extensionName):
##        u'Finds an extension by its name.'
##        #return extension
##
##    def PrintPreview(self):
##        u'Displays how the document will look like when it is printed.'
##        #return 
##
##    def RefreshWindow(self):
##        u'Redraws the application window.'
##        #return 
##
##    def _get(self):
##        u'The caption of this application.'
##        #return Caption
##    def _set(self, Caption):
##        u'The caption of this application.'
##    Caption = property(_get, _set, doc = _set.__doc__)
##
##    def ShowDialog(self, dialogID, bShow):
##        u'Displays the specified dialog in the application.'
##        #return result
##
##    def CurrentTool(self, Tool):
##        u'The currently selected tool.'
##        #return 
##
##    def LockCustomization(self, Password, custFilter):
##        u"Locks the application's user interface against any customizations."
##        #return 
##
##    def SaveDocument(self, saveAsPath):
##        u'Saves the document that is currently open in this application.'
##        #return 
##
##    def NewDocument(self, selectTemplate, templatePath):
##        u'Creates a new document in this application.'
##        #return 
##
##    def _get(self):
##        u'Indicates if the application window is visible.'
##        #return Visible
##    def _set(self, Visible):
##        u'Indicates if the application window is visible.'
##    Visible = property(_get, _set, doc = _set.__doc__)
##
##    def Shutdown(self):
##        u'Terminates the application.'
##        #return 
##

class AppRef(CoClass):
    u'A reference to the currently running application.'
    _reg_clsid_ = GUID('{E1740EC5-9513-11D2-A2DF-0000F8774FB5}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
AppRef._com_interfaces_ = [IApplication]

class IProtectNameFramework(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to dummy methods protecting name correctness.'
    _iid_ = GUID('{454CEA50-BDA0-443F-B55F-0297C8712E72}')
    _idlflags_ = []
IProtectNameFramework._methods_ = [
    COMMETHOD([], HRESULT, 'ProtectOLE_HANDLE',
              ( [], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'aHandle' )),
    COMMETHOD([], HRESULT, 'ProtectOLE_COLOR',
              ( [], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_COLOR, 'aColor' )),
]
################################################################
## code template for IProtectNameFramework implementation
##class IProtectNameFramework_Impl(object):
##    def ProtectOLE_COLOR(self, aColor):
##        '-no docstring-'
##        #return 
##
##    def ProtectOLE_HANDLE(self, aHandle):
##        '-no docstring-'
##        #return 
##

class GetStringDialog(CoClass):
    u'A dialog used for getting a string.'
    _reg_clsid_ = GUID('{A7B8EC90-AC12-11D2-AB27-00C04FA334B3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
GetStringDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGetStringDialog]

class IProgressDialogFactory(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to a method that creates a progress dialog.'
    _iid_ = GUID('{31A6AEB1-F644-11D1-A248-080009B6F22B}')
    _idlflags_ = ['oleautomation']
IProgressDialogFactory._methods_ = [
    COMMETHOD([helpstring(u'Creates a progress dialog.')], HRESULT, 'Create',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'trackCancel' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hWnd' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStepProgressor)), 'stepProgressor' )),
]
################################################################
## code template for IProgressDialogFactory implementation
##class IProgressDialogFactory_Impl(object):
##    def Create(self, trackCancel, hWnd):
##        u'Creates a progress dialog.'
##        #return stepProgressor
##

class GetUserAndPasswordDialog(CoClass):
    u'A dialog used for getting user and password information.'
    _reg_clsid_ = GUID('{F4DEB91A-378F-4ACA-9971-12C494D94E58}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
GetUserAndPasswordDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGetUserAndPasswordDialog]

class ApplicationStatusEvents(CoClass):
    u'Helper coclass for working with the nondefault outbound IApplicationStatusEvents interface in VB.'
    _reg_clsid_ = GUID('{ABC37653-E992-48E1-A35B-C2F3E1BCDB45}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
ApplicationStatusEvents._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown]
ApplicationStatusEvents._outgoing_interfaces_ = [IApplicationStatusEvents]

class SymbolPickerDialog(CoClass):
    u'The SymbolPicker Dialog Object.'
    _reg_clsid_ = GUID('{14B6E652-3962-4A79-A8B2-F7D7F8B00B59}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
SymbolPickerDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ISymbolPickerDialog]


# values for enumeration 'esriCommandTypes'
esriCmdTypeCommand = 0
esriCmdTypeMenu = 1
esriCmdTypeToolbar = 2
esriCmdTypeMacro = 3
esriCmdTypeUIButtonCtrl = 4
esriCmdTypeUIToolCtrl = 5
esriCmdTypeUIComboBoxCtrl = 6
esriCmdTypeUIEditBoxCtrl = 7
esriCmdTypeGPTool = 8
esriCommandTypes = c_int # enum
class AppROT(CoClass):
    u'Esri application running object table.'
    _reg_clsid_ = GUID('{FABC30FB-D273-11D2-9F36-00C04F6BC61A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
AppROT._com_interfaces_ = [IAppROT, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IConnectionPointContainer]
AppROT._outgoing_interfaces_ = [IAppROTEvents]

class ICommandBars(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that work on the collection of commandbars.'
    _iid_ = GUID('{289FC451-D249-11D1-91AD-0080C718DF97}')
    _idlflags_ = ['oleautomation']
class IAcceleratorTable(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that modify the accelerator table.'
    _iid_ = GUID('{08300DE2-27FD-11D2-AA2F-000000000000}')
    _idlflags_ = ['oleautomation']
IDocument._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'The application in which this document is open.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(IApplication)), 'app' )),
    COMMETHOD([dispid(0), helpstring(u'The title of this document.'), 'propget'], HRESULT, 'Title',
              ( ['retval', 'out'], POINTER(BSTR), 'Title' )),
    COMMETHOD([dispid(2), helpstring(u'The commandbars collection in this document.'), 'propget'], HRESULT, 'CommandBars',
              ( ['retval', 'out'], POINTER(POINTER(ICommandBars)), 'cmdBars' )),
    COMMETHOD([dispid(4), helpstring(u'The accelerator table for this document.'), 'propget'], HRESULT, 'Accelerators',
              ( ['retval', 'out'], POINTER(POINTER(IAcceleratorTable)), 'accelTable' )),
    COMMETHOD([dispid(5), helpstring(u'The unique id for this document.'), 'propget'], HRESULT, 'ID',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID)), 'ID' )),
    COMMETHOD([dispid(6), helpstring(u'The type of this document.'), 'propget'], HRESULT, 'Type',
              ( ['retval', 'out'], POINTER(esriDocumentType), 'Type' )),
    COMMETHOD([dispid(7), helpstring(u'The VBProject for this document.'), 'propget'], HRESULT, 'VBProject',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'VBProject' )),
]
################################################################
## code template for IDocument implementation
##class IDocument_Impl(object):
##    @property
##    def Parent(self):
##        u'The application in which this document is open.'
##        #return app
##
##    @property
##    def Title(self):
##        u'The title of this document.'
##        #return Title
##
##    @property
##    def VBProject(self):
##        u'The VBProject for this document.'
##        #return VBProject
##
##    @property
##    def Accelerators(self):
##        u'The accelerator table for this document.'
##        #return accelTable
##
##    @property
##    def Type(self):
##        u'The type of this document.'
##        #return Type
##
##    @property
##    def ID(self):
##        u'The unique id for this document.'
##        #return ID
##
##    @property
##    def CommandBars(self):
##        u'The commandbars collection in this document.'
##        #return cmdBars
##

ICommandItem._methods_ = [
    COMMETHOD(['propget', helpstring(u'The name of the VBA macro this command should run when pressed.')], HRESULT, 'Action',
              ( ['retval', 'out'], POINTER(BSTR), 'macro' )),
    COMMETHOD(['propput', helpstring(u'The name of the VBA macro this command should run when pressed.')], HRESULT, 'Action',
              ( ['in'], BSTR, 'macro' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether this command item is built-in or if it was implemented through VBA.')], HRESULT, 'BuiltIn',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'BuiltIn' )),
    COMMETHOD(['propget', helpstring(u'The name of the category with which this command item is associated.')], HRESULT, 'Category',
              ( ['retval', 'out'], POINTER(BSTR), 'Category' )),
    COMMETHOD(['hidden', helpstring(u'A reference to the internal command object.'), 'propget'], HRESULT, 'Command',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.ICommand)), 'Command' )),
    COMMETHOD([helpstring(u'Removes this object from the commandbar.')], HRESULT, 'Delete'),
    COMMETHOD(['propput', helpstring(u'The bitmap that is used as the icon on this command item.')], HRESULT, 'FaceID',
              ( ['in'], VARIANT, 'FaceID' )),
    COMMETHOD(['propget', helpstring(u'The bitmap that is used as the icon on this command item.')], HRESULT, 'FaceID',
              ( ['retval', 'out'], POINTER(VARIANT), 'FaceID' )),
    COMMETHOD(['propput', helpstring(u'Indicates if this command item begins a menu or toolbar group.')], HRESULT, 'Group',
              ( ['in'], VARIANT_BOOL, 'Group' )),
    COMMETHOD(['propget', helpstring(u'Indicates if this command item begins a menu or toolbar group.')], HRESULT, 'Group',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Group' )),
    COMMETHOD(['propget', helpstring(u'The help file associated with this command item.')], HRESULT, 'HelpFile',
              ( ['retval', 'out'], POINTER(BSTR), 'HelpFile' )),
    COMMETHOD(['propput', helpstring(u'The help file associated with this command item.')], HRESULT, 'HelpFile',
              ( ['in'], BSTR, 'HelpFile' )),
    COMMETHOD(['propget', helpstring(u'The help context ID associated with this command item.')], HRESULT, 'HelpContextID',
              ( ['retval', 'out'], POINTER(c_int), 'contextID' )),
    COMMETHOD(['propput', helpstring(u'The help context ID associated with this command item.')], HRESULT, 'HelpContextID',
              ( ['in'], c_int, 'contextID' )),
    COMMETHOD(['propget', helpstring(u'The unique integer ID associated with this command item.')], HRESULT, 'ID',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID)), 'identity' )),
    COMMETHOD(['propget', helpstring(u'The positional index of this command item within its menu or toolbar.')], HRESULT, 'Index',
              ( ['retval', 'out'], POINTER(c_int), 'Index' )),
    COMMETHOD(['propget', helpstring(u'The name of this command item.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propput', helpstring(u'The name of this command item.')], HRESULT, 'Name',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD(['propput', helpstring(u'The caption of this command item.')], HRESULT, 'Caption',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD(['propget', helpstring(u'The caption of this command item.')], HRESULT, 'Caption',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'The menu or toolbar that this command item currently resides on.')], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(ICommandBar)), 'bar' )),
    COMMETHOD([helpstring(u"Restores this command item's properties to that of the original.")], HRESULT, 'Reset'),
    COMMETHOD(['propget', helpstring(u'The display style of this command item.')], HRESULT, 'Style',
              ( ['retval', 'out'], POINTER(comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.esriCommandStyles), 'Style' )),
    COMMETHOD(['propput', helpstring(u'The display style of this command item.')], HRESULT, 'Style',
              ( ['in'], comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.esriCommandStyles, 'Style' )),
    COMMETHOD(['propget', helpstring(u'The tag for this command item.')], HRESULT, 'Tag',
              ( ['retval', 'out'], POINTER(BSTR), 'Tag' )),
    COMMETHOD(['propput', helpstring(u'The tag for this command item.')], HRESULT, 'Tag',
              ( ['in'], BSTR, 'Tag' )),
    COMMETHOD(['propget', helpstring(u'The tooltip for this command item.')], HRESULT, 'Tooltip',
              ( ['retval', 'out'], POINTER(BSTR), 'Tooltip' )),
    COMMETHOD(['propput', helpstring(u'The tooltip for this command item.')], HRESULT, 'Tooltip',
              ( ['in'], BSTR, 'Tooltip' )),
    COMMETHOD(['propget', helpstring(u'The type of this command item.')], HRESULT, 'Type',
              ( ['retval', 'out'], POINTER(esriCommandTypes), 'Type' )),
    COMMETHOD(['propget', helpstring(u'The status bar message for this command item.')], HRESULT, 'Message',
              ( ['retval', 'out'], POINTER(BSTR), 'Message' )),
    COMMETHOD(['propput', helpstring(u'The status bar message for this command item.')], HRESULT, 'Message',
              ( ['in'], BSTR, 'Message' )),
    COMMETHOD([helpstring(u'Causes the command to execute.')], HRESULT, 'Execute'),
    COMMETHOD([helpstring(u'Causes the command to be redrawn.')], HRESULT, 'Refresh'),
]
################################################################
## code template for ICommandItem implementation
##class ICommandItem_Impl(object):
##    @property
##    def Category(self):
##        u'The name of the category with which this command item is associated.'
##        #return Category
##
##    @property
##    def Index(self):
##        u'The positional index of this command item within its menu or toolbar.'
##        #return Index
##
##    def _get(self):
##        u'The display style of this command item.'
##        #return Style
##    def _set(self, Style):
##        u'The display style of this command item.'
##    Style = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if this command item begins a menu or toolbar group.'
##        #return Group
##    def _set(self, Group):
##        u'Indicates if this command item begins a menu or toolbar group.'
##    Group = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The tooltip for this command item.'
##        #return Tooltip
##    def _set(self, Tooltip):
##        u'The tooltip for this command item.'
##    Tooltip = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Type(self):
##        u'The type of this command item.'
##        #return Type
##
##    @property
##    def Parent(self):
##        u'The menu or toolbar that this command item currently resides on.'
##        #return bar
##
##    @property
##    def ID(self):
##        u'The unique integer ID associated with this command item.'
##        #return identity
##
##    def _get(self):
##        u'The help context ID associated with this command item.'
##        #return contextID
##    def _set(self, contextID):
##        u'The help context ID associated with this command item.'
##    HelpContextID = property(_get, _set, doc = _set.__doc__)
##
##    def Reset(self):
##        u"Restores this command item's properties to that of the original."
##        #return 
##
##    def Execute(self):
##        u'Causes the command to execute.'
##        #return 
##
##    def _get(self):
##        u'The name of this command item.'
##        #return Name
##    def _set(self, Name):
##        u'The name of this command item.'
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    def Refresh(self):
##        u'Causes the command to be redrawn.'
##        #return 
##
##    def _get(self):
##        u'The caption of this command item.'
##        #return Name
##    def _set(self, Name):
##        u'The caption of this command item.'
##    Caption = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Command(self):
##        u'A reference to the internal command object.'
##        #return Command
##
##    def _get(self):
##        u'The help file associated with this command item.'
##        #return HelpFile
##    def _set(self, HelpFile):
##        u'The help file associated with this command item.'
##    HelpFile = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The name of the VBA macro this command should run when pressed.'
##        #return macro
##    def _set(self, macro):
##        u'The name of the VBA macro this command should run when pressed.'
##    Action = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The bitmap that is used as the icon on this command item.'
##        #return FaceID
##    def _set(self, FaceID):
##        u'The bitmap that is used as the icon on this command item.'
##    FaceID = property(_get, _set, doc = _set.__doc__)
##
##    def Delete(self):
##        u'Removes this object from the commandbar.'
##        #return 
##
##    @property
##    def BuiltIn(self):
##        u'Indicates whether this command item is built-in or if it was implemented through VBA.'
##        #return BuiltIn
##
##    def _get(self):
##        u'The tag for this command item.'
##        #return Tag
##    def _set(self, Tag):
##        u'The tag for this command item.'
##    Tag = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The status bar message for this command item.'
##        #return Message
##    def _set(self, Message):
##        u'The status bar message for this command item.'
##    Message = property(_get, _set, doc = _set.__doc__)
##

class IPaletteEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to events that occur when the palette changes.'
    _iid_ = GUID('{CEB59B81-D86D-11D1-A21C-080009B6F22B}')
    _idlflags_ = ['oleautomation']
IPaletteEvents._methods_ = [
    COMMETHOD([helpstring(u'Occurs when the contents of the palette change.')], HRESULT, 'ContentsChanged'),
]
################################################################
## code template for IPaletteEvents implementation
##class IPaletteEvents_Impl(object):
##    def ContentsChanged(self):
##        u'Occurs when the contents of the palette change.'
##        #return 
##

class Accelerator(CoClass):
    u'Accelerator object.'
    _reg_clsid_ = GUID('{8A85D730-2949-49DA-8995-CEC77F68BDFA}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
Accelerator._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IAccelerator]

class CommandBars(CoClass):
    u'CommandBars collection object.'
    _reg_clsid_ = GUID('{5C396018-9B88-493C-B47D-8C6332AEDBDD}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
CommandBars._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ICommandBars]

class Templates(CoClass):
    u'Templates collection object.'
    _reg_clsid_ = GUID('{C32FF69D-CF6A-4FE5-B62F-A38FEAEAD0D8}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
Templates._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ITemplates]

class ISelectionPalette(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that define a palette of selection choices.'
    _iid_ = GUID('{5FDD7101-8E9F-11D1-A1B2-080009B6F22B}')
    _idlflags_ = ['oleautomation']
ISelectionPalette._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if the palette is enabled.')], HRESULT, 'Enabled',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Enabled' )),
    COMMETHOD(['propget', helpstring(u'The name of the palette. This will show in the title bar.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'The number of items in the palette.')], HRESULT, 'ItemCount',
              ( ['retval', 'out'], POINTER(c_int), 'ItemCount' )),
    COMMETHOD([helpstring(u'The bitmap and tooltip for the given item.')], HRESULT, 'QueryItem',
              ( ['in'], c_int, 'Index' ),
              ( ['out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'Bitmap' ),
              ( ['out'], POINTER(BSTR), 'Tooltip' )),
    COMMETHOD(['propget', helpstring(u'The number of more buttons in the palette.')], HRESULT, 'MoreButtonCount',
              ( ['retval', 'out'], POINTER(c_int), 'MoreButtonCount' )),
    COMMETHOD([helpstring(u'The tooltip and text for the given more button.')], HRESULT, 'QueryMoreButton',
              ( ['in'], c_int, 'Index' ),
              ( ['out'], POINTER(BSTR), 'Tooltip' ),
              ( ['out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'The category the palette belongs to.')], HRESULT, 'Category',
              ( ['retval', 'out'], POINTER(BSTR), 'Category' )),
    COMMETHOD(['propget', helpstring(u'The shortcut key to show this palette.')], HRESULT, 'ShortCutKey',
              ( ['retval', 'out'], POINTER(BSTR), 'shortCutText' )),
    COMMETHOD(['propget', helpstring(u'The number of columns in this palette.')], HRESULT, 'NumColumns',
              ( ['retval', 'out'], POINTER(c_int), 'NumColumns' )),
    COMMETHOD(['propput', helpstring(u'The number of columns in this palette.')], HRESULT, 'NumColumns',
              ( ['in'], c_int, 'NumColumns' )),
    COMMETHOD(['propget', helpstring(u'The number of rows in this palette.')], HRESULT, 'NumRows',
              ( ['retval', 'out'], POINTER(c_int), 'NumRows' )),
    COMMETHOD(['propput', helpstring(u'The number of rows in this palette.')], HRESULT, 'NumRows',
              ( ['in'], c_int, 'NumRows' )),
    COMMETHOD(['propget', helpstring(u'The index of the item in the palette that was last selected.')], HRESULT, 'LastSelected',
              ( ['retval', 'out'], POINTER(c_int), 'Index' )),
    COMMETHOD(['propput', helpstring(u'The index of the item in the palette that was last selected.')], HRESULT, 'LastSelected',
              ( ['in'], c_int, 'Index' )),
    COMMETHOD([helpstring(u'Gives the palette a hook into the application.')], HRESULT, 'OnCreate',
              ( ['in'], POINTER(IDispatch), 'hook' )),
    COMMETHOD([helpstring(u'Occurs when the user selects an item the palette.')], HRESULT, 'OnClick',
              ( ['in'], c_int, 'Index' )),
]
################################################################
## code template for ISelectionPalette implementation
##class ISelectionPalette_Impl(object):
##    def QueryItem(self, Index):
##        u'The bitmap and tooltip for the given item.'
##        #return Bitmap, Tooltip
##
##    @property
##    def Category(self):
##        u'The category the palette belongs to.'
##        #return Category
##
##    def _get(self):
##        u'The number of columns in this palette.'
##        #return NumColumns
##    def _set(self, NumColumns):
##        u'The number of columns in this palette.'
##    NumColumns = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Name(self):
##        u'The name of the palette. This will show in the title bar.'
##        #return Name
##
##    @property
##    def Enabled(self):
##        u'Indicates if the palette is enabled.'
##        #return Enabled
##
##    def _get(self):
##        u'The index of the item in the palette that was last selected.'
##        #return Index
##    def _set(self, Index):
##        u'The index of the item in the palette that was last selected.'
##    LastSelected = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The number of rows in this palette.'
##        #return NumRows
##    def _set(self, NumRows):
##        u'The number of rows in this palette.'
##    NumRows = property(_get, _set, doc = _set.__doc__)
##
##    def OnCreate(self, hook):
##        u'Gives the palette a hook into the application.'
##        #return 
##
##    @property
##    def MoreButtonCount(self):
##        u'The number of more buttons in the palette.'
##        #return MoreButtonCount
##
##    def OnClick(self, Index):
##        u'Occurs when the user selects an item the palette.'
##        #return 
##
##    @property
##    def ShortCutKey(self):
##        u'The shortcut key to show this palette.'
##        #return shortCutText
##
##    @property
##    def ItemCount(self):
##        u'The number of items in the palette.'
##        #return ItemCount
##
##    def QueryMoreButton(self, Index):
##        u'The tooltip and text for the given more button.'
##        #return Tooltip, Name
##

class CommandBar(CoClass):
    u'CommandBar object.'
    _reg_clsid_ = GUID('{A37EF60A-59B9-4599-8621-AC81112DF947}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
CommandBar._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ICommandItem, ICommandBar, IWindowPosition]

ICommandBars._methods_ = [
    COMMETHOD(['propput', helpstring(u'Indicates if tooltips should be shown.')], HRESULT, 'ShowToolTips',
              ( ['in'], VARIANT_BOOL, 'bShow' )),
    COMMETHOD(['propget', helpstring(u'Indicates if tooltips should be shown.')], HRESULT, 'ShowToolTips',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bShow' )),
    COMMETHOD(['propput', helpstring(u'Indicates if large icons should be shown.')], HRESULT, 'LargeIcons',
              ( ['in'], VARIANT_BOOL, 'bLarge' )),
    COMMETHOD(['propget', helpstring(u'Indicates if large icons should be shown.')], HRESULT, 'LargeIcons',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bLarge' )),
    COMMETHOD([helpstring(u'Creates a new blank toolbar or shortcut menu.')], HRESULT, 'Create',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.esriCmdBarType, 'barType' ),
              ( ['retval', 'out'], POINTER(POINTER(ICommandBar)), 'newBar' )),
    COMMETHOD([helpstring(u'Searches for the item specified by identifier.')], HRESULT, 'Find',
              ( ['in'], VARIANT, 'identifier' ),
              ( ['in', 'optional'], VARIANT_BOOL, 'noRecurse', False ),
              ( ['in', 'optional'], VARIANT_BOOL, 'noCreate', False ),
              ( ['retval', 'out'], POINTER(POINTER(ICommandItem)), 'Item' )),
    COMMETHOD([helpstring(u'Hides all visible bars.')], HRESULT, 'HideAllToolbars'),
]
################################################################
## code template for ICommandBars implementation
##class ICommandBars_Impl(object):
##    def Create(self, Name, barType):
##        u'Creates a new blank toolbar or shortcut menu.'
##        #return newBar
##
##    def _get(self):
##        u'Indicates if tooltips should be shown.'
##        #return bShow
##    def _set(self, bShow):
##        u'Indicates if tooltips should be shown.'
##    ShowToolTips = property(_get, _set, doc = _set.__doc__)
##
##    def Find(self, identifier, noRecurse, noCreate):
##        u'Searches for the item specified by identifier.'
##        #return Item
##
##    def HideAllToolbars(self):
##        u'Hides all visible bars.'
##        #return 
##
##    def _get(self):
##        u'Indicates if large icons should be shown.'
##        #return bLarge
##    def _set(self, bLarge):
##        u'Indicates if large icons should be shown.'
##    LargeIcons = property(_get, _set, doc = _set.__doc__)
##

class ModelessFrame(CoClass):
    u'Object that implements a ModelessFrame.'
    _reg_clsid_ = GUID('{9F79BAAE-E23A-4E3E-83F9-6D85B3D1094F}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
ModelessFrame._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IModelessFrame, IWindowPosition]

class IAtbApplication(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the window handle of the ArcToolbox application.'
    _iid_ = GUID('{EA936DFE-2AA1-11D4-A632-0008C711C8C1}')
    _idlflags_ = ['oleautomation']
IAtbApplication._methods_ = [
    COMMETHOD(['propget', helpstring(u'The window handle of the ArcToolbox application.')], HRESULT, 'hWnd',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'hWnd' )),
]
################################################################
## code template for IAtbApplication implementation
##class IAtbApplication_Impl(object):
##    @property
##    def hWnd(self):
##        u'The window handle of the ArcToolbox application.'
##        #return hWnd
##

class AcceleratorTable(CoClass):
    u'Accelerator Table Object.'
    _reg_clsid_ = GUID('{CE259B71-280C-11D2-AA2F-000000000000}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
AcceleratorTable._com_interfaces_ = [IAcceleratorTable, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream]

class ComPropertyPageSite(CoClass):
    u'COM Property Page Site.'
    _reg_clsid_ = GUID('{DE803DB1-BC9A-44B2-B735-3C0912239587}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
ComPropertyPageSite._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IPropertyPageSite, IPropertyPageSiteConfig, IComPropertyPageSite]

class IStyleSelector(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that work with the style selector dialog.'
    _iid_ = GUID('{C98E418D-78E7-11D2-87D4-0000F8751720}')
    _idlflags_ = ['oleautomation']
IStyleSelector._methods_ = [
    COMMETHOD([helpstring(u'Specifies the original style. May specify more than one.')], HRESULT, 'AddStyle',
              ( ['in'], POINTER(IUnknown), 'Style' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'result' )),
    COMMETHOD([helpstring(u'Returns the updated style. Index is required when more than one style was originally added.')], HRESULT, 'GetStyle',
              ( ['in'], c_int, 'Index' ),
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'Style' )),
    COMMETHOD([helpstring(u'Shows the style selector dialog.')], HRESULT, 'DoModal',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentHWnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ok' )),
]
################################################################
## code template for IStyleSelector implementation
##class IStyleSelector_Impl(object):
##    def DoModal(self, parentHWnd):
##        u'Shows the style selector dialog.'
##        #return ok
##
##    def GetStyle(self, Index):
##        u'Returns the updated style. Index is required when more than one style was originally added.'
##        #return Style
##
##    def AddStyle(self, Style):
##        u'Specifies the original style. May specify more than one.'
##        #return result
##

class FractionPropertyPage(CoClass):
    u'Fraction Format Property Page.'
    _reg_clsid_ = GUID('{FCF40D70-C91F-11D2-AAF8-000000000000}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
FractionPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IPropertyPage, IPropertyPageContext, IComPropertyPage, IComPropertyPage2]

class IComPropertyPageObjectFactory(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the COM Property Page Object Factory.'
    _iid_ = GUID('{76951CC8-DBB1-11D2-B868-00600802E603}')
    _idlflags_ = ['oleautomation']
IComPropertyPageObjectFactory._methods_ = [
    COMMETHOD([helpstring(u'Creates a new object using a template as a model.')], HRESULT, 'CreateCompatibleObject',
              ( ['in'], POINTER(IUnknown), 'objTemplate' ),
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'ppObject' )),
    COMMETHOD([helpstring(u'Returns the new object created by the page.')], HRESULT, 'QueryObject',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'ppObject' )),
]
################################################################
## code template for IComPropertyPageObjectFactory implementation
##class IComPropertyPageObjectFactory_Impl(object):
##    def QueryObject(self):
##        u'Returns the new object created by the page.'
##        #return ppObject
##
##    def CreateCompatibleObject(self, objTemplate):
##        u'Creates a new object using a template as a model.'
##        #return ppObject
##

class ColorSelector(CoClass):
    u'Esri Color Selector object.'
    _reg_clsid_ = GUID('{93051635-F841-11D2-9F36-00C04F6BC709}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
ColorSelector._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IColorBrowser, IColorSelector]

class IComEmbeddedPropertyPage(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods needed for embedded property pages.'
    _iid_ = GUID('{063304C3-7B90-48E9-B2D3-E795A8BA926B}')
    _idlflags_ = ['oleautomation']
IComEmbeddedPropertyPage._methods_ = [
    COMMETHOD([helpstring(u'Create a new object using the specified object as a template.  The kind argument may be NULL if the page interacts with only a single object.')], HRESULT, 'CreateCompatibleObject',
              ( ['in'], VARIANT, 'kind' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'pNewObject' )),
    COMMETHOD([helpstring(u'Apply the property page settings to the specified object.')], HRESULT, 'QueryObject',
              ( ['in'], VARIANT, 'theObject' )),
]
################################################################
## code template for IComEmbeddedPropertyPage implementation
##class IComEmbeddedPropertyPage_Impl(object):
##    def QueryObject(self, theObject):
##        u'Apply the property page settings to the specified object.'
##        #return 
##
##    def CreateCompatibleObject(self, kind):
##        u'Create a new object using the specified object as a template.  The kind argument may be NULL if the page interacts with only a single object.'
##        #return pNewObject
##

class CurrencyPropertyPage(CoClass):
    u'Currency Format Property Page.'
    _reg_clsid_ = GUID('{6F560571-960F-11D2-AE77-080009EC732A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
CurrencyPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IPropertyPage, IPropertyPageContext, IComPropertyPage, IComPropertyPage2]

class NumberDialog(CoClass):
    u'A dialog used for getting a number.'
    _reg_clsid_ = GUID('{759F7B99-E07D-11D1-AA87-00C04FA374BD}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
NumberDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, INumberDialog]

ICustomizationFilter._methods_ = [
    COMMETHOD([helpstring(u'Occurs when certain types of customization occur.')], HRESULT, 'OnCustomizationEvent',
              ( ['in'], esriCustomizationEvent, 'custEventType' ),
              ( ['in'], VARIANT, 'eventCtx' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bDeny' )),
]
################################################################
## code template for ICustomizationFilter implementation
##class ICustomizationFilter_Impl(object):
##    def OnCustomizationEvent(self, custEventType, eventCtx):
##        u'Occurs when certain types of customization occur.'
##        #return bDeny
##

class Button(CoClass):
    u'Button CoType.'
    _reg_clsid_ = GUID('{D13CBE84-71B0-4EEF-8BD6-60D358B431F6}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
Button._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.ICommand]

class ProgressDialogFactory(CoClass):
    u'Progress Dialog Factory object.'
    _reg_clsid_ = GUID('{31A6AEB2-F644-11D1-A248-080009B6F22B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
ProgressDialogFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IProgressDialogFactory]

class ColorPalette(CoClass):
    u'Esri Color Palette object.'
    _reg_clsid_ = GUID('{14746474-1534-11D3-9F49-00C04F6BC709}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
ColorPalette._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IColorPalette, ICustomColorPalette]

class DockableWindow(CoClass):
    u'DockableWindow object.'
    _reg_clsid_ = GUID('{D91ED352-E414-11D3-A679-0008C7DF97B9}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
DockableWindow._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDockableWindow, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo, IWindowPosition]

ICommandBar._methods_ = [
    COMMETHOD([helpstring(u'Adds a new command to this commandbar.')], HRESULT, 'Add',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID), 'cmdID' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'Index' ),
              ( ['retval', 'out'], POINTER(POINTER(ICommandItem)), 'Item' )),
    COMMETHOD([helpstring(u'Creates a new blank menu on this commandbar at the specified position.')], HRESULT, 'CreateMenu',
              ( ['in'], BSTR, 'Name' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'Index' ),
              ( ['retval', 'out'], POINTER(POINTER(ICommandBar)), 'menu' )),
    COMMETHOD([helpstring(u'Creates a new macro item on this commandbar at the specified position.')], HRESULT, 'CreateMacroItem',
              ( ['in'], BSTR, 'Name' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'FaceID' ),
              ( ['in', 'optional'], BSTR, 'Action' ),
              ( ['in', 'optional'], POINTER(VARIANT), 'Index' ),
              ( ['retval', 'out'], POINTER(POINTER(ICommandItem)), 'macro' )),
    COMMETHOD(['propget', helpstring(u'The number of items contained within this commandbar.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD([helpstring(u'Finds a command on this commandbar.')], HRESULT, 'Find',
              ( ['in'], VARIANT, 'identifier' ),
              ( ['in', 'optional'], VARIANT_BOOL, 'noRecurse', False ),
              ( ['retval', 'out'], POINTER(POINTER(ICommandItem)), 'Item' )),
    COMMETHOD(['propget', helpstring(u'The command item on this commandbar at the specified index.')], HRESULT, 'Item',
              ( ['in'], c_int, 'Index' ),
              ( ['retval', 'out'], POINTER(POINTER(ICommandItem)), 'Item' )),
    COMMETHOD([helpstring(u'Displays this commandbar as a popup menu at the specified location.')], HRESULT, 'Popup',
              ( ['in', 'optional'], c_int, 'X', 0 ),
              ( ['in', 'optional'], c_int, 'Y', 0 ),
              ( ['retval', 'out'], POINTER(POINTER(ICommandItem)), 'Choice' )),
    COMMETHOD([helpstring(u'Docks or undocks this commandbar.')], HRESULT, 'Dock',
              ( ['in'], esriDockFlags, 'dockFlags' ),
              ( ['in', 'optional'], POINTER(ICommandBar), 'referenceBar' )),
    COMMETHOD([helpstring(u'Indicates if this commandbar is visible.')], HRESULT, 'IsVisible',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bVisible' )),
]
################################################################
## code template for ICommandBar implementation
##class ICommandBar_Impl(object):
##    @property
##    def Count(self):
##        u'The number of items contained within this commandbar.'
##        #return Count
##
##    def CreateMenu(self, Name, Index):
##        u'Creates a new blank menu on this commandbar at the specified position.'
##        #return menu
##
##    def Dock(self, dockFlags, referenceBar):
##        u'Docks or undocks this commandbar.'
##        #return 
##
##    def CreateMacroItem(self, Name, FaceID, Action, Index):
##        u'Creates a new macro item on this commandbar at the specified position.'
##        #return macro
##
##    @property
##    def Item(self, Index):
##        u'The command item on this commandbar at the specified index.'
##        #return Item
##
##    def Add(self, cmdID, Index):
##        u'Adds a new command to this commandbar.'
##        #return Item
##
##    def Popup(self, X, Y):
##        u'Displays this commandbar as a popup menu at the specified location.'
##        #return Choice
##
##    def IsVisible(self):
##        u'Indicates if this commandbar is visible.'
##        #return bVisible
##
##    def Find(self, identifier, noRecurse):
##        u'Finds a command on this commandbar.'
##        #return Item
##

class CoordinateDialog(CoClass):
    u'A dialog used for getting coordinates.'
    _reg_clsid_ = GUID('{759F7B9C-E07D-11D1-AA87-00C04FA374BD}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
CoordinateDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ICoordinateDialog]

IComPropertySheet._methods_ = [
    COMMETHOD(['propput', helpstring(u'The title of the property sheet.')], HRESULT, 'Title',
              ( ['in'], BSTR, 'Title' )),
    COMMETHOD(['propget', helpstring(u'The title of the property sheet.')], HRESULT, 'Title',
              ( ['retval', 'out'], POINTER(BSTR), 'Title' )),
    COMMETHOD(['propput', helpstring(u'The zero-based index of the page that is active.')], HRESULT, 'ActivePage',
              ( ['in'], c_short, 'Index' )),
    COMMETHOD(['propget', helpstring(u'The zero-based index of the page that is active.')], HRESULT, 'ActivePage',
              ( ['retval', 'out'], POINTER(c_short), 'Index' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the Cancel button is disabled on the property sheet.')], HRESULT, 'DisableCancelButton',
              ( ['in'], VARIANT_BOOL, 'disableButton' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the Cancel button is disabled on the property sheet.')], HRESULT, 'DisableCancelButton',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'disableButton' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the Apply button is visible on the property sheet.')], HRESULT, 'HideApplyButton',
              ( ['in'], VARIANT_BOOL, 'HideApplyButton' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the Apply button is visible on the property sheet.')], HRESULT, 'HideApplyButton',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'HideApplyButton' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the Help button is visible on the property sheet.')], HRESULT, 'HideHelpButton',
              ( ['in'], VARIANT_BOOL, 'HideHelpButton' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the Help button is visible on the property sheet.')], HRESULT, 'HideHelpButton',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'HideHelpButton' )),
    COMMETHOD([helpstring(u'Adds a new Category ID used to look up COM property pages.')], HRESULT, 'AddCategoryID',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID), 'Category' )),
    COMMETHOD([helpstring(u'Clears the category IDs used to look up COM property pages.')], HRESULT, 'ClearCategoryIDs'),
    COMMETHOD([helpstring(u'Manually adds a page to the property sheet. Page must implement IComPropertyPage or IPropertyPage.')], HRESULT, 'AddPage',
              ( [], VARIANT, 'Page' )),
    COMMETHOD([helpstring(u'Indicates if this object can edit the given set of objects.')], HRESULT, 'CanEdit',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISet), 'objects' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'result' )),
    COMMETHOD([helpstring(u'Displays a property sheet for the given set of objects and returns a flag indicating if the objects changed.')], HRESULT, 'EditProperties',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISet), 'objects' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hWnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ok' )),
]
################################################################
## code template for IComPropertySheet implementation
##class IComPropertySheet_Impl(object):
##    def _get(self):
##        u'The zero-based index of the page that is active.'
##        #return Index
##    def _set(self, Index):
##        u'The zero-based index of the page that is active.'
##    ActivePage = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the Help button is visible on the property sheet.'
##        #return HideHelpButton
##    def _set(self, HideHelpButton):
##        u'Indicates if the Help button is visible on the property sheet.'
##    HideHelpButton = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the Cancel button is disabled on the property sheet.'
##        #return disableButton
##    def _set(self, disableButton):
##        u'Indicates if the Cancel button is disabled on the property sheet.'
##    DisableCancelButton = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The title of the property sheet.'
##        #return Title
##    def _set(self, Title):
##        u'The title of the property sheet.'
##    Title = property(_get, _set, doc = _set.__doc__)
##
##    def EditProperties(self, objects, hWnd):
##        u'Displays a property sheet for the given set of objects and returns a flag indicating if the objects changed.'
##        #return ok
##
##    def _get(self):
##        u'Indicates if the Apply button is visible on the property sheet.'
##        #return HideApplyButton
##    def _set(self, HideApplyButton):
##        u'Indicates if the Apply button is visible on the property sheet.'
##    HideApplyButton = property(_get, _set, doc = _set.__doc__)
##
##    def AddCategoryID(self, Category):
##        u'Adds a new Category ID used to look up COM property pages.'
##        #return 
##
##    def AddPage(self, Page):
##        u'Manually adds a page to the property sheet. Page must implement IComPropertyPage or IPropertyPage.'
##        #return 
##
##    def CanEdit(self, objects):
##        u'Indicates if this object can edit the given set of objects.'
##        #return result
##
##    def ClearCategoryIDs(self):
##        u'Clears the category IDs used to look up COM property pages.'
##        #return 
##

class ToolControl(CoClass):
    u'ToolControl CoType.'
    _reg_clsid_ = GUID('{B6BFF46F-6DCF-4DB7-9985-5F41A41F17FC}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
ToolControl._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.ICommand, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IToolControl]

class ColorBrowser(CoClass):
    u'Esri Custom Color Dialog.'
    _reg_clsid_ = GUID('{20CD4001-8F3D-11D0-8590-0800091A2A72}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
ColorBrowser._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IColorBrowser]

class IMultiThreadedApplication(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control DLL thread managers.'
    _iid_ = GUID('{34709A45-8E39-4397-A0CF-63963E5F52E4}')
    _idlflags_ = ['oleautomation']
IMultiThreadedApplication._methods_ = [
    COMMETHOD([helpstring(u'The process ID for the application.')], HRESULT, 'GetProcessID',
              ( ['retval', 'out'], POINTER(c_int), 'pid' )),
    COMMETHOD([helpstring(u'Registers a DLL thread manager with the application.')], HRESULT, 'RegisterThreadManager',
              ( ['in'], POINTER(IDllThreadManager), 'pThreadMgr' ),
              ( ['retval', 'out'], POINTER(c_int), 'mgrCookie' )),
    COMMETHOD([helpstring(u'Unregisters a DLL thread manager with the application.')], HRESULT, 'UnregisterThreadManager',
              ( ['in'], c_int, 'mgrCookie' )),
]
################################################################
## code template for IMultiThreadedApplication implementation
##class IMultiThreadedApplication_Impl(object):
##    def GetProcessID(self):
##        u'The process ID for the application.'
##        #return pid
##
##    def RegisterThreadManager(self, pThreadMgr):
##        u'Registers a DLL thread manager with the application.'
##        #return mgrCookie
##
##    def UnregisterThreadManager(self, mgrCookie):
##        u'Unregisters a DLL thread manager with the application.'
##        #return 
##

IMouseCursor._methods_ = [
    COMMETHOD([helpstring(u"Sets the application's cursor to cursor id or picture object specified by cursorID. The cursor is automatically reset when the MouseCursor instance is released.")], HRESULT, 'SetCursor',
              ( ['in'], VARIANT, 'cursorID' )),
]
################################################################
## code template for IMouseCursor implementation
##class IMouseCursor_Impl(object):
##    def SetCursor(self, cursorID):
##        u"Sets the application's cursor to cursor id or picture object specified by cursorID. The cursor is automatically reset when the MouseCursor instance is released."
##        #return 
##


# values for enumeration 'esriStatusBarPanes'
esriStatusMain = 0
esriStatusAnimation = 1
esriStatusPosition = 2
esriStatusPagePosition = 4
esriStatusSize = 8
esriStatusCapsLock = 16
esriStatusNumLock = 32
esriStatusScrollLock = 64
esriStatusClock = 128
esriStatusSwitchButtons = 256
esriStatusBarPanes = c_int # enum
class NumberFormatDialog(CoClass):
    u'Number Format Dialog object.'
    _reg_clsid_ = GUID('{88002C0A-939A-11D2-AE73-080009EC732A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
NumberFormatDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, INumberFormatDialog]

class NumericPropertyPage(CoClass):
    u'Numeric Format Property Page.'
    _reg_clsid_ = GUID('{9388D95B-9460-11D2-AE74-080009EC732A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
NumericPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IPropertyPage, IPropertyPageContext, IComPropertyPage, IComPropertyPage2]

class CommandItem(CoClass):
    u'Command Item.'
    _reg_clsid_ = GUID('{FA73EF95-B87C-11D1-947B-080009EEBECB}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
CommandItem._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ICommandItem, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

IPropertyPageSite._methods_ = [
    COMMETHOD([], HRESULT, 'OnStatusChange',
              ( ['in'], c_ulong, 'dwFlags' )),
    COMMETHOD([], HRESULT, 'GetLocaleID',
              ( ['out'], POINTER(c_ulong), 'pLocaleID' )),
    COMMETHOD([], HRESULT, 'GetPageContainer',
              ( ['out'], POINTER(POINTER(IUnknown)), 'ppUnk' )),
    COMMETHOD([], HRESULT, 'TranslateAccelerator',
              ( ['in'], POINTER(tagMSG), 'pMsg' )),
]
################################################################
## code template for IPropertyPageSite implementation
##class IPropertyPageSite_Impl(object):
##    def GetLocaleID(self):
##        '-no docstring-'
##        #return pLocaleID
##
##    def OnStatusChange(self, dwFlags):
##        '-no docstring-'
##        #return 
##
##    def GetPageContainer(self):
##        '-no docstring-'
##        #return ppUnk
##
##    def TranslateAccelerator(self, pMsg):
##        '-no docstring-'
##        #return 
##

class MultiItem(CoClass):
    u'MultiItem CoType.'
    _reg_clsid_ = GUID('{BF3DD473-A408-4014-B913-69A31AF6115D}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{866AE5D3-530C-11D2-A2BD-0000F8774FB5}', 10, 2)
MultiItem._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IMultiItem]

IAcceleratorTable._methods_ = [
    COMMETHOD(['propget', helpstring(u'The count of accelerator items in the table.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'The accelerator object at the specified index.')], HRESULT, 'Item',
              ( ['in'], c_int, 'Index' ),
              ( ['retval', 'out'], POINTER(POINTER(IAccelerator)), 'Accelerator' )),
    COMMETHOD([helpstring(u'Adds a new accelerator to the accelerator table.')], HRESULT, 'Add',
              ( ['in'], VARIANT, 'ID' ),
              ( ['in'], c_int, 'Key' ),
              ( ['in', 'optional'], VARIANT_BOOL, 'bCtrl', False ),
              ( ['in', 'optional'], VARIANT_BOOL, 'bAlt', False ),
              ( ['in', 'optional'], VARIANT_BOOL, 'bShift', False ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bSucceeded' )),
    COMMETHOD([helpstring(u'Finds the accelerator object/s currently associated with the specified command ID.')], HRESULT, 'Find',
              ( ['in'], VARIANT, 'ID' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IArray)), 'accelArray' )),
    COMMETHOD([helpstring(u'Finds the accelerator object associated with the specified key combination.')], HRESULT, 'FindByKey',
              ( ['in'], c_int, 'Key' ),
              ( ['in', 'optional'], VARIANT_BOOL, 'bCtrl', False ),
              ( ['in', 'optional'], VARIANT_BOOL, 'bAlt', False ),
              ( ['in', 'optional'], VARIANT_BOOL, 'bShift', False ),
              ( ['retval', 'out'], POINTER(POINTER(IAccelerator)), 'Accelerator' )),
]
################################################################
## code template for IAcceleratorTable implementation
##class IAcceleratorTable_Impl(object):
##    @property
##    def Count(self):
##        u'The count of accelerator items in the table.'
##        #return Count
##
##    @property
##    def Item(self, Index):
##        u'The accelerator object at the specified index.'
##        #return Accelerator
##
##    def Add(self, ID, Key, bCtrl, bAlt, bShift):
##        u'Adds a new accelerator to the accelerator table.'
##        #return bSucceeded
##
##    def Find(self, ID):
##        u'Finds the accelerator object/s currently associated with the specified command ID.'
##        #return accelArray
##
##    def FindByKey(self, Key, bCtrl, bAlt, bShift):
##        u'Finds the accelerator object associated with the specified key combination.'
##        #return Accelerator
##

class IApplicationStatus(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the applications status.'
    _iid_ = GUID('{0573D2F5-A2A0-4EF6-BDF7-416097472C8D}')
    _idlflags_ = ['oleautomation']
IApplicationStatus._methods_ = [
    COMMETHOD(['propget', helpstring(u'Is the application initialized.')], HRESULT, 'Initialized',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pOut' )),
]
################################################################
## code template for IApplicationStatus implementation
##class IApplicationStatus_Impl(object):
##    @property
##    def Initialized(self):
##        u'Is the application initialized.'
##        #return pOut
##

__all__ = ['IComPropertySheetID', 'ListDialog', 'IObjectFactory',
           'IComPropertyPageObjectFactory', 'NumberFormatDialog',
           'esriDockRight', 'AppROT', 'esriCEEditVBACode',
           'ICustomColorPalette', 'GetStringDialog', 'esriStatusSize',
           'ScientificPropertyPage', 'ToolControl',
           'ColorNamePropertyPage', 'esriDockLeft',
           'esriCmdTypeGPTool', 'EnumStyleGalleryItem',
           'INumberDialog', 'IComPropertySheet2', 'GrayPropertyPage',
           'esriWindowState', 'esriDockTabbed', '_RemotableHandle',
           'IAtbApplication', 'IRootLevelMenu', 'IColorBrowser',
           'IComPropertySheet', 'ColorPageSite', 'tagPROPPAGEINFO',
           'IDockableWindowInitialPlacementNeighbors',
           'CurrencyPropertyPage', '__MIDL_IWinTypes_0009',
           'MessageDialog', 'cust_err_no_template_lock',
           'esriStatusSwitchButtons', 'esriDockTop',
           'IPropertyPageContext', 'GetUserAndPasswordDialog',
           'esriWSNormal', 'esriDockFloat', 'IAccelerator',
           'IMenuItem2', 'ApplicationStatusEvents',
           'esriCmdTypeCommand', 'esriCmdTypeUIButtonCtrl',
           'IDocument', 'esriDockFlags', 'IArcToolboxTool',
           'StyleGalleryItem', 'esriDocumentTypeDocument',
           'IApplicationStatusEvents', 'LONG_PTR', 'esriCEShowVBAIDE',
           'esriATModal', 'ColorPalette', 'IPropertyPageSite',
           'IMessageDialog', 'esriStatusAnimation', 'HsvPropertyPage',
           'esriCmdTypeUIToolCtrl', 'ModelessFrame',
           'esriStatusPosition', 'esriDockToggle', 'MouseCursor',
           'esriDownloadFile', 'ICoordinateDialog', 'NumberDialog',
           'IApplicationRefreshBitmap', 'CustomPropertyPage',
           'CoordinateDialog', 'ColorSelector', 'Tool',
           'INumberFormatDialog', 'IGetUserAndPasswordDialog',
           'cust_err_invalid_on_builtin', 'CustomizationErrors',
           'IMenuItem', 'IComEmbeddedPropertyPage',
           'esriCmdTypeUIEditBoxCtrl', 'esriWSFloating',
           'esriCmdTypeMenu', 'ProgressDialogFactory',
           'esriCustomizationEvent', 'esriWSMaximize', 'IMouseCursor',
           'esriStatusScrollLock', 'IModelessFrame',
           'esriDockUnPinned', 'esriATModeless',
           'cust_err_cmdNotAvail', 'esriStatusPagePosition',
           'ICommandBars', 'esriCEAddCommand', 'IProgressDialog2',
           'esriNoAnimation', 'CommandBars', 'IShortcutMenu',
           'AppRef', 'ISymbolPickerDialog', 'IDDECommandHandler',
           'IAcceleratorHook', 'IComPropertyPage2',
           'esriCEShowCustCtxMenu', 'esriCmdTypeToolbar',
           'IApplicationStatus', 'cust_err_invalid',
           'IPropertyPageSiteConfig', 'esriStatusMain',
           'IColorSelector', 'esriATModality', 'IDocumentDirty',
           'IComPropertyPage', 'IVbaApplication',
           'DirectionPropertyPage', 'esriCEShowCustDlg',
           'IMultiThreadedApplication', 'ComPropertyPageSite',
           'RatePropertyPage', 'esriStatusNumLock',
           'esriCERunVBACode', 'CommandItem', 'IListDialog',
           'esriDocumentType', 'esriDockBottom', 'StyleGallery',
           'ColorBrowser', 'CmykPropertyPage', 'esriProgressGlobe',
           'DockableWindow', 'IProtectNameFramework', 'UINT_PTR',
           'esriDockShow', 'esriStatusCapsLock', 'esriStatusClock',
           'Accelerator', 'esriCmdTypeMacro', 'IColorPalette',
           'IDockableWindowHelpNotify', 'IArcToolboxFind',
           'IApplicationIdentifyDialog', 'ISelectionPalette',
           'IApplication', 'SymbolPickerDialog',
           'esriCmdTypeUIComboBoxCtrl', 'IStyleSelector',
           'esriDockHide', 'NumericPropertyPage', 'IAcceleratorTable',
           'esriDocumentTypeNormal', 'CommandBar',
           'ISmallBitmapProvider', 'IAppROT', 'IAppROTEvents',
           'ICommandBar', 'esriDocumentTypeTemplate',
           'AnglePropertyPage', 'esriWSMinimize', 'Templates',
           'ComPropertySheet', 'IDockableWindowImageDef',
           'IDockableWindowManager', 'ICustomizationFilter',
           'esriProgressSpiral', 'cust_err_alreadyLocked',
           'IDockableWindow', 'FractionPropertyPage',
           'esriCEAddCategory', 'IComPropertyPageSite',
           'IDocumentDirty2', 'AcceleratorTable', 'DllThreadManager',
           'Button', 'cust_err_builtin_only',
           'cust_err_badPasswordLen', 'ICommandItem',
           'cust_err_invalid_on_commandbar', 'IDockableWindowDef',
           'PercentagePropertyPage', 'IDllThreadManager',
           'ITemplates', 'IProgressDialogFactory', 'IPaletteEvents',
           'esriProgressAnimationTypes', 'cust_err_invalid_type',
           'IGetStringDialog', 'MultiItem', 'IWindowPosition',
           'esriStatusBarPanes', 'RgbPropertyPage',
           'IDockableWindowInitialPlacement', 'esriCEInvokeCommand',
           'esriCommandTypes', 'IPropertyPage', 'IFileOpenHandler']
from comtypes import _check_version; _check_version('501')

# -*- coding: mbcs -*-
typelib_path = u'C:\\Program Files (x86)\\ArcGIS\\Engine10.2\\com\\esriDisplay.olb'
_lcid = 0 # change this if required
from ctypes import *
import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0
from comtypes import GUID
import comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2
from ctypes import HRESULT
from ctypes.wintypes import VARIANT_BOOL
from comtypes import helpstring
from comtypes import COMMETHOD
from comtypes import dispid
from comtypes import CoClass
import comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2
from comtypes import BSTR
from comtypes import IUnknown
from ctypes.wintypes import tagPOINT
from ctypes.wintypes import tagPOINT
from comtypes.automation import VARIANT
from comtypes.automation import VARIANT
import comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2
from comtypes.automation import _midlSAFEARRAY


class IRubberBand2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control simple rubberbanding.'
    _iid_ = GUID('{E6BDB006-4D35-11D0-98BE-00805F7CED21}')
    _idlflags_ = ['oleautomation']
class IDisplay(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Display.'
    _iid_ = GUID('{E6BDB002-4D35-11D0-98BE-00805F7CED21}')
    _idlflags_ = ['oleautomation']
class IScreenDisplay(IDisplay):
    _case_insensitive_ = True
    u'Provides access to members that control Screen Display.'
    _iid_ = GUID('{E6BDB004-4D35-11D0-98BE-00805F7CED21}')
    _idlflags_ = ['oleautomation']
class ISymbol(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control symbols.'
    _iid_ = GUID('{F3435802-5779-11D0-98BF-00805F7CED21}')
    _idlflags_ = ['oleautomation']
IRubberBand2._methods_ = [
    COMMETHOD([helpstring(u'Call in response to mouse down event to rubberband a new shape on the specified screen.')], HRESULT, 'TrackNew',
              ( ['in'], POINTER(IScreenDisplay), 'ScreenDisplay' ),
              ( ['in'], POINTER(ISymbol), 'Symbol' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry)), 'Geometry' )),
    COMMETHOD([helpstring(u'Indicates if to move or reshape an existing shape on the specified screen in response to a mouse down event.')], HRESULT, 'TrackExisting',
              ( ['in'], POINTER(IScreenDisplay), 'ScreenDisplay' ),
              ( ['in'], POINTER(ISymbol), 'Symbol' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'Geometry' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'completed' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the shift key constrain the shape.')], HRESULT, 'ShiftToConstrain',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether the shift key constrain the shape.')], HRESULT, 'ShiftToConstrain',
              ( ['in'], VARIANT_BOOL, 'flag' )),
]
################################################################
## code template for IRubberBand2 implementation
##class IRubberBand2_Impl(object):
##    def TrackExisting(self, ScreenDisplay, Symbol, Geometry):
##        u'Indicates if to move or reshape an existing shape on the specified screen in response to a mouse down event.'
##        #return completed
##
##    def TrackNew(self, ScreenDisplay, Symbol):
##        u'Call in response to mouse down event to rubberband a new shape on the specified screen.'
##        #return Geometry
##
##    def _get(self):
##        u'Indicates whether the shift key constrain the shape.'
##        #return flag
##    def _set(self, flag):
##        u'Indicates whether the shift key constrain the shape.'
##    ShiftToConstrain = property(_get, _set, doc = _set.__doc__)
##


# values for enumeration 'esriMoveTextConstraints'
esriMoveTextConstraintsLeft = 0
esriMoveTextConstraintsRight = 1
esriMoveTextConstraintsOnTop = 2
esriMoveTextConstraintsCursor = 3
esriMoveTextConstraints = c_int # enum
class LinePattern(CoClass):
    u'A line fill pattern object.'
    _reg_clsid_ = GUID('{444F0F52-DABF-4639-B239-9A88B3C3F830}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IFillPattern(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods that control the fill pattern.'
    _iid_ = GUID('{A8C6CF51-202C-46C7-9DBB-9900C9CD9C2E}')
    _idlflags_ = ['oleautomation']
class IGraphicAttributes(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the graphic attributes.'
    _iid_ = GUID('{7200F877-D9F9-4B54-940E-1E3A68363E2D}')
    _idlflags_ = ['oleautomation']
class IGraphicAttributes2(IGraphicAttributes):
    _case_insensitive_ = True
    u'Provides access to members that control the graphic attributes.'
    _iid_ = GUID('{7C843A64-DBFA-4DE9-9CC9-0414CB2C68BA}')
    _idlflags_ = ['oleautomation']
class IDrawingOutline(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods dealing with the outline of a drawing rule.'
    _iid_ = GUID('{5B50CF13-4F70-4BED-B1B7-55F3AA8D26F8}')
    _idlflags_ = ['oleautomation']
LinePattern._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IFillPattern, IGraphicAttributes, IGraphicAttributes2, IDrawingOutline, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

class IColor(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the basic color interface.'
    _iid_ = GUID('{20CD40B0-8F3D-11D0-8590-0800091A2A72}')
    _idlflags_ = ['oleautomation']
class IGrayColor(IColor):
    _case_insensitive_ = True
    u'Provides access to members that control the gray color.'
    _iid_ = GUID('{20CD40B4-8F3D-11D0-8590-0800091A2A72}')
    _idlflags_ = ['oleautomation']
IColor._methods_ = [
    COMMETHOD(['propput', helpstring(u'The RGB value of color.')], HRESULT, 'RGB',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_COLOR, 'RGB' )),
    COMMETHOD(['propget', helpstring(u'The RGB value of color.')], HRESULT, 'RGB',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_COLOR), 'RGB' )),
    COMMETHOD(['propput', helpstring(u'The CMYK value of color.')], HRESULT, 'CMYK',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_COLOR, 'CMYK' )),
    COMMETHOD(['propget', helpstring(u'The CMYK value of color.')], HRESULT, 'CMYK',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_COLOR), 'CMYK' )),
    COMMETHOD(['propput', helpstring(u"Indicates if colors should be dithered to simulate colors that aren't supported by the display.  This only applies on displays that have 256 or fewer colors.")], HRESULT, 'UseWindowsDithering',
              ( ['in'], VARIANT_BOOL, 'useDithering' )),
    COMMETHOD(['propget', helpstring(u"Indicates if colors should be dithered to simulate colors that aren't supported by the display.  This only applies on displays that have 256 or fewer colors.")], HRESULT, 'UseWindowsDithering',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'useDithering' )),
    COMMETHOD([helpstring(u'The CIELAB value of color.')], HRESULT, 'SetCIELAB',
              ( ['in'], c_double, 'l' ),
              ( ['in'], c_double, 'a' ),
              ( ['in'], c_double, 'b' )),
    COMMETHOD([helpstring(u'The CIELAB value of color.')], HRESULT, 'GetCIELAB',
              ( ['out'], POINTER(c_double), 'l' ),
              ( ['out'], POINTER(c_double), 'a' ),
              ( ['out'], POINTER(c_double), 'b' )),
    COMMETHOD(['propput', helpstring(u'The Alpha Blending value. (0 for transparent, 255 for opaque).')], HRESULT, 'Transparency',
              ( ['in'], c_ubyte, 'alphaValue' )),
    COMMETHOD(['propget', helpstring(u'The Alpha Blending value. (0 for transparent, 255 for opaque).')], HRESULT, 'Transparency',
              ( ['retval', 'out'], POINTER(c_ubyte), 'alphaValue' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether this color is null.')], HRESULT, 'NullColor',
              ( ['in'], VARIANT_BOOL, 'flag' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether this color is null.')], HRESULT, 'NullColor',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
]
################################################################
## code template for IColor implementation
##class IColor_Impl(object):
##    def GetCIELAB(self):
##        u'The CIELAB value of color.'
##        #return l, a, b
##
##    def _get(self):
##        u"Indicates if colors should be dithered to simulate colors that aren't supported by the display.  This only applies on displays that have 256 or fewer colors."
##        #return useDithering
##    def _set(self, useDithering):
##        u"Indicates if colors should be dithered to simulate colors that aren't supported by the display.  This only applies on displays that have 256 or fewer colors."
##    UseWindowsDithering = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The CMYK value of color.'
##        #return CMYK
##    def _set(self, CMYK):
##        u'The CMYK value of color.'
##    CMYK = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The RGB value of color.'
##        #return RGB
##    def _set(self, RGB):
##        u'The RGB value of color.'
##    RGB = property(_get, _set, doc = _set.__doc__)
##
##    def SetCIELAB(self, l, a, b):
##        u'The CIELAB value of color.'
##        #return 
##
##    def _get(self):
##        u'The Alpha Blending value. (0 for transparent, 255 for opaque).'
##        #return alphaValue
##    def _set(self, alphaValue):
##        u'The Alpha Blending value. (0 for transparent, 255 for opaque).'
##    Transparency = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether this color is null.'
##        #return flag
##    def _set(self, flag):
##        u'Indicates whether this color is null.'
##    NullColor = property(_get, _set, doc = _set.__doc__)
##

IGrayColor._methods_ = [
    COMMETHOD(['propput', helpstring(u'The level of grayness of an IGrayColor (0 = White - 255 = Black).')], HRESULT, 'Level',
              ( ['in'], c_int, 'outLevel' )),
    COMMETHOD(['propget', helpstring(u'The level of grayness of an IGrayColor (0 = White - 255 = Black).')], HRESULT, 'Level',
              ( ['retval', 'out'], POINTER(c_int), 'outLevel' )),
]
################################################################
## code template for IGrayColor implementation
##class IGrayColor_Impl(object):
##    def _get(self):
##        u'The level of grayness of an IGrayColor (0 = White - 255 = Black).'
##        #return outLevel
##    def _set(self, outLevel):
##        u'The level of grayness of an IGrayColor (0 = White - 255 = Black).'
##    Level = property(_get, _set, doc = _set.__doc__)
##

class CancelTracker(CoClass):
    u'Cancel tracker class for interrupting drawing.'
    _reg_clsid_ = GUID('{EB16E597-B4F7-11D0-865F-0000F8751720}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
CancelTracker._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel2]

class IMarkerSymbol(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control marker symbols.'
    _iid_ = GUID('{E6BDAA7C-4D35-11D0-98BE-00805F7CED21}')
    _idlflags_ = ['oleautomation']
class IReferenceMarkerSymbol(IMarkerSymbol):
    _case_insensitive_ = True
    u'Provides access to members that control the reference marker symbol.'
    _iid_ = GUID('{7914E5E2-C892-11D0-8BB6-080009EE4E41}')
    _idlflags_ = ['oleautomation']
IMarkerSymbol._methods_ = [
    COMMETHOD(['propget', helpstring(u'Marker symbol size.')], HRESULT, 'Size',
              ( ['retval', 'out'], POINTER(c_double), 'Size' )),
    COMMETHOD(['propput', helpstring(u'Marker symbol size.')], HRESULT, 'Size',
              ( ['in'], c_double, 'Size' )),
    COMMETHOD(['propget', helpstring(u'Marker symbol color.')], HRESULT, 'Color',
              ( ['retval', 'out'], POINTER(POINTER(IColor)), 'Color' )),
    COMMETHOD(['propput', helpstring(u'Marker symbol color.')], HRESULT, 'Color',
              ( ['in'], POINTER(IColor), 'Color' )),
    COMMETHOD(['propget', helpstring(u'Marker symbol angle.')], HRESULT, 'Angle',
              ( ['retval', 'out'], POINTER(c_double), 'Angle' )),
    COMMETHOD(['propput', helpstring(u'Marker symbol angle.')], HRESULT, 'Angle',
              ( ['in'], c_double, 'Angle' )),
    COMMETHOD(['propget', helpstring(u'Symbol X-axis offset from point location.')], HRESULT, 'XOffset',
              ( ['retval', 'out'], POINTER(c_double), 'XOffset' )),
    COMMETHOD(['propput', helpstring(u'Symbol X-axis offset from point location.')], HRESULT, 'XOffset',
              ( ['in'], c_double, 'XOffset' )),
    COMMETHOD(['propget', helpstring(u'Symbol Y-axis offset from point location.')], HRESULT, 'YOffset',
              ( ['retval', 'out'], POINTER(c_double), 'YOffset' )),
    COMMETHOD(['propput', helpstring(u'Symbol Y-axis offset from point location.')], HRESULT, 'YOffset',
              ( ['in'], c_double, 'YOffset' )),
]
################################################################
## code template for IMarkerSymbol implementation
##class IMarkerSymbol_Impl(object):
##    def _get(self):
##        u'Marker symbol color.'
##        #return Color
##    def _set(self, Color):
##        u'Marker symbol color.'
##    Color = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Symbol Y-axis offset from point location.'
##        #return YOffset
##    def _set(self, YOffset):
##        u'Symbol Y-axis offset from point location.'
##    YOffset = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Marker symbol angle.'
##        #return Angle
##    def _set(self, Angle):
##        u'Marker symbol angle.'
##    Angle = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Symbol X-axis offset from point location.'
##        #return XOffset
##    def _set(self, XOffset):
##        u'Symbol X-axis offset from point location.'
##    XOffset = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Marker symbol size.'
##        #return Size
##    def _set(self, Size):
##        u'Marker symbol size.'
##    Size = property(_get, _set, doc = _set.__doc__)
##

IReferenceMarkerSymbol._methods_ = [
    COMMETHOD(['propget', helpstring(u'Symbol set name.')], HRESULT, 'SymbolSetName',
              ( ['retval', 'out'], POINTER(BSTR), 'setName' )),
    COMMETHOD(['propput', helpstring(u'Symbol set name.')], HRESULT, 'SymbolSetName',
              ( ['in'], BSTR, 'setName' )),
    COMMETHOD(['propget', helpstring(u'Symbol name.')], HRESULT, 'SymbolName',
              ( ['retval', 'out'], POINTER(BSTR), 'symName' )),
    COMMETHOD(['propput', helpstring(u'Symbol name.')], HRESULT, 'SymbolName',
              ( ['in'], BSTR, 'symName' )),
]
################################################################
## code template for IReferenceMarkerSymbol implementation
##class IReferenceMarkerSymbol_Impl(object):
##    def _get(self):
##        u'Symbol set name.'
##        #return setName
##    def _set(self, setName):
##        u'Symbol set name.'
##    SymbolSetName = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Symbol name.'
##        #return symName
##    def _set(self, symName):
##        u'Symbol name.'
##    SymbolName = property(_get, _set, doc = _set.__doc__)
##

class AlgorithmicColorRamp(CoClass):
    u'Defines an algorithmic color ramp, where ramp is defined by two colors and the algorithm used to traverse the intervening color space between them.'
    _reg_clsid_ = GUID('{BEB8709B-C0B4-11D0-8379-080009B996CC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IColorRamp(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the methods and properties common to all color ramp objects.'
    _iid_ = GUID('{BEB87091-C0B4-11D0-8379-080009B996CC}')
    _idlflags_ = ['oleautomation']
class IAlgorithmicColorRamp(IColorRamp):
    _case_insensitive_ = True
    u'Provides access to members that control the AlgorithmicColorRamp. A color ramp defined by two colors and the algorithm used to traverse the intervening color space between them.'
    _iid_ = GUID('{BEB87096-C0B4-11D0-8379-080009B996CC}')
    _idlflags_ = ['oleautomation']
AlgorithmicColorRamp._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IAlgorithmicColorRamp, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize]

class RubberPolygon(CoClass):
    u'Rubberbanding class for polygons.'
    _reg_clsid_ = GUID('{E6BDB105-4D35-11D0-98BE-00805F7CED21}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IRubberBand(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control simple rubberbanding.'
    _iid_ = GUID('{E6BDB005-4D35-11D0-98BE-00805F7CED21}')
    _idlflags_ = ['oleautomation']
RubberPolygon._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRubberBand, IRubberBand2]

class GradientPattern(CoClass):
    u'A gradient fill pattern object.'
    _reg_clsid_ = GUID('{00F11C2D-FCBB-4B7F-8135-E7AF481CE592}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
GradientPattern._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IFillPattern, IGraphicAttributes, IGraphicAttributes2, IDrawingOutline, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]


# values for enumeration 'esriOrientMode'
esriOMParallel = 1
esriOMPerpendicular = 2
esriOrientMode = c_int # enum
class BasicLineSymbol(CoClass):
    u'Basic line symbol object.'
    _reg_clsid_ = GUID('{ED8FB823-10FA-468B-8DCD-4327C0DF0B22}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IBasicSymbol(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods that control the basic symbol.'
    _iid_ = GUID('{0E4428D1-2E96-4BDD-B253-06B4C9A75C7A}')
    _idlflags_ = ['oleautomation']
class IBasicLineSymbol(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to properties of the basic line symbol.'
    _iid_ = GUID('{6E353AF0-24EC-4000-A9FE-8E58B16E12CD}')
    _idlflags_ = ['oleautomation']
class IMapLevel(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the map level.'
    _iid_ = GUID('{CEF72580-C1D9-11D2-9888-0080C7E04196}')
    _idlflags_ = ['oleautomation']
class IGeometricEffects(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the geometric effect list.'
    _iid_ = GUID('{6F68089C-1026-4BA3-8930-A52D62EEC539}')
    _idlflags_ = ['oleautomation']
class IGeometricEffect(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the Geometric Effect Interface.'
    _iid_ = GUID('{A5A4CA1C-1164-4DC4-AE82-5611A8F807E5}')
    _idlflags_ = ['oleautomation']
BasicLineSymbol._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IBasicSymbol, IBasicLineSymbol, IMapLevel, IGeometricEffects, IGeometricEffect, IDrawingOutline, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLVersionSupport]

class RepresentationRule(CoClass):
    u'An object defining a representation rule.'
    _reg_clsid_ = GUID('{1079E40A-83C1-467B-B828-E5C06EF5F6B7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IRepresentationRule(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control a representation rule.'
    _iid_ = GUID('{2B7BE3AB-BB72-49D0-A6EE-63ACD1F9068C}')
    _idlflags_ = ['oleautomation']
class IRepresentationRule2(IRepresentationRule):
    _case_insensitive_ = True
    u'Provides access to members that control a representation rule.'
    _iid_ = GUID('{BC4B25E7-E952-4B66-8606-0B5A315AB42B}')
    _idlflags_ = ['oleautomation']
class IRepresentationRuleInit(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that initialize a representation rule.'
    _iid_ = GUID('{7FE42275-2A90-4A53-AF60-71453BC5E6CD}')
    _idlflags_ = ['oleautomation']
class IFieldOverrides(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to a collection of field overrides.'
    _iid_ = GUID('{DC3E1EBA-3DE0-4DEB-B063-218A3E381EFE}')
    _idlflags_ = ['oleautomation']
RepresentationRule._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRepresentationRule, IRepresentationRule2, IRepresentationRuleInit, IMapLevel, IGeometricEffect, IGeometricEffects, IDrawingOutline, IFieldOverrides, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLVersionSupport]

class IDisplayFeedback(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the base display feedback.'
    _iid_ = GUID('{D2C13E55-4BEA-11D1-B6CC-080009B996CC}')
    _idlflags_ = ['oleautomation']
class IRotateTextFeedback(IDisplayFeedback):
    _case_insensitive_ = True
    u'Provides access to members that control the rotate text feedback.'
    _iid_ = GUID('{AE629199-B816-45B9-B20B-D84D919FE0C4}')
    _idlflags_ = ['oleautomation']
IDisplayFeedback._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The symbol the feedback object will use.')], HRESULT, 'Symbol',
              ( ['in'], POINTER(ISymbol), 'Symbol' )),
    COMMETHOD(['propget', helpstring(u'The symbol the feedback object will use.')], HRESULT, 'Symbol',
              ( ['retval', 'out'], POINTER(POINTER(ISymbol)), 'Symbol' )),
    COMMETHOD(['propputref', helpstring(u'The display the feedback object will use.')], HRESULT, 'Display',
              ( ['in'], POINTER(IScreenDisplay), 'rhs' )),
    COMMETHOD([helpstring(u'Call this after a refresh to show feedback again.')], HRESULT, 'Refresh',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDC' )),
    COMMETHOD([helpstring(u'Move to the new point.')], HRESULT, 'MoveTo',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
]
################################################################
## code template for IDisplayFeedback implementation
##class IDisplayFeedback_Impl(object):
##    @property
##    def Symbol(self, Symbol):
##        u'The symbol the feedback object will use.'
##        #return 
##
##    def MoveTo(self, Point):
##        u'Move to the new point.'
##        #return 
##
##    def Display(self, rhs):
##        u'The display the feedback object will use.'
##        #return 
##
##    def Refresh(self, hDC):
##        u'Call this after a refresh to show feedback again.'
##        #return 
##

IRotateTextFeedback._methods_ = [
    COMMETHOD([helpstring(u'Begins a new feedback.')], HRESULT, 'Start',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'cursorPosition' ),
              ( ['in'], c_double, 'ReferenceScale' )),
    COMMETHOD([helpstring(u'Stops the feedback.')], HRESULT, 'Stop',
              ( ['retval', 'out'], POINTER(c_double), 'Angle' )),
    COMMETHOD(['propget', helpstring(u'The anchor point of the feedback.')], HRESULT, 'Anchor',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint)), 'Anchor' )),
]
################################################################
## code template for IRotateTextFeedback implementation
##class IRotateTextFeedback_Impl(object):
##    def Start(self, cursorPosition, ReferenceScale):
##        u'Begins a new feedback.'
##        #return 
##
##    def Stop(self):
##        u'Stops the feedback.'
##        #return Angle
##
##    @property
##    def Anchor(self):
##        u'The anchor point of the feedback.'
##        #return Anchor
##

class IEnumConnections(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{B196B287-BAB4-101A-B69C-00AA00341D07}')
    _idlflags_ = []
class tagCONNECTDATA(Structure):
    pass
IEnumConnections._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteNext',
              ( ['in'], c_ulong, 'cConnections' ),
              ( ['out'], POINTER(tagCONNECTDATA), 'rgcd' ),
              ( ['out'], POINTER(c_ulong), 'pcFetched' )),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'cConnections' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IEnumConnections)), 'ppEnum' )),
]
################################################################
## code template for IEnumConnections implementation
##class IEnumConnections_Impl(object):
##    def Reset(self):
##        '-no docstring-'
##        #return 
##
##    def Skip(self, cConnections):
##        '-no docstring-'
##        #return 
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppEnum
##
##    def RemoteNext(self, cConnections):
##        '-no docstring-'
##        #return rgcd, pcFetched
##

class IReshapeFeedback(IDisplayFeedback):
    _case_insensitive_ = True
    u'Provides access to members that control the reshape display feedback.'
    _iid_ = GUID('{4E315500-F4DD-11D1-8498-0000F875B9C6}')
    _idlflags_ = ['oleautomation']
IReshapeFeedback._methods_ = [
    COMMETHOD([helpstring(u'Begins a feedback operation at the point.')], HRESULT, 'Start',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPath), 'path' ),
              ( ['in'], c_int, 'index' ),
              ( ['in'], VARIANT_BOOL, 'stretch' )),
    COMMETHOD([helpstring(u'Finishes a reshape feedback operation.')], HRESULT, 'Stop',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPath)), 'path' )),
]
################################################################
## code template for IReshapeFeedback implementation
##class IReshapeFeedback_Impl(object):
##    def Start(self, path, index, stretch):
##        u'Begins a feedback operation at the point.'
##        #return 
##
##    def Stop(self):
##        u'Finishes a reshape feedback operation.'
##        #return path
##

class GlobalScreenDisplaySettings(CoClass):
    u'Display settings class.'
    _reg_clsid_ = GUID('{CC899F8F-E480-4B89-B686-790F0CC9E003}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IGlobalScreenDisplaySettings(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to screen display settings.'
    _iid_ = GUID('{8D5048AB-7030-4F0B-B14F-3AE772046D51}')
    _idlflags_ = ['oleautomation']
GlobalScreenDisplaySettings._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGlobalScreenDisplaySettings]

class BasicFillSymbol(CoClass):
    u'Basic fill symbol object.'
    _reg_clsid_ = GUID('{BC38C464-8B02-4B0C-81D5-8237847A46CE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IBasicFillSymbol(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to properties of the basic fill symbol.'
    _iid_ = GUID('{475A667D-B02A-4B58-A336-00544BABE12A}')
    _idlflags_ = ['oleautomation']
BasicFillSymbol._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IBasicSymbol, IBasicFillSymbol, IMapLevel, IGeometricEffects, IGeometricEffect, IDrawingOutline, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLVersionSupport]

class MarkerPlacementOnVertices(CoClass):
    u'Places markers on curve vertices.'
    _reg_clsid_ = GUID('{0940F9CE-4A95-46D1-B3FA-D3A197EEB19F}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IMarkerPlacement(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the marker placement.'
    _iid_ = GUID('{43A0A7C4-B01C-491A-9481-BF9EE1584D42}')
    _idlflags_ = ['oleautomation']
MarkerPlacementOnVertices._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMarkerPlacement, IGraphicAttributes, IGraphicAttributes2, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

class MultiPartColorRamp(CoClass):
    u'Defines a multi part color ramp, where ramp is defined by a list of constituent color ramps.'
    _reg_clsid_ = GUID('{BEB87099-C0B4-11D0-8379-080009B996CC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IMultiPartColorRamp(IColorRamp):
    _case_insensitive_ = True
    u'Provides access to members that control the MultiPartColorRamp. A color ramp defined by a list of constituent color ramps.'
    _iid_ = GUID('{BEB87098-C0B4-11D0-8379-080009B996CC}')
    _idlflags_ = ['oleautomation']
MultiPartColorRamp._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMultiPartColorRamp, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize]

tagCONNECTDATA._fields_ = [
    ('pUnk', POINTER(IUnknown)),
    ('dwCookie', c_ulong),
]
assert sizeof(tagCONNECTDATA) == 8, sizeof(tagCONNECTDATA)
assert alignment(tagCONNECTDATA) == 4, alignment(tagCONNECTDATA)
class IColorElements(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the Color Elements Interface.'
    _iid_ = GUID('{07ACD47E-A8A1-4274-9D58-D13B703D3A28}')
    _idlflags_ = ['oleautomation']
IColorElements._methods_ = [
    COMMETHOD(['propget', helpstring(u'The color elements count.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'The color element at the specified position.')], HRESULT, 'Element',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IColor)), 'ppColor' )),
    COMMETHOD([helpstring(u'Remove color element at the specified position.')], HRESULT, 'Remove',
              ( ['in'], c_int, 'index' )),
    COMMETHOD([helpstring(u'Remove all color elements.')], HRESULT, 'RemoveAll'),
    COMMETHOD([helpstring(u'Add a color element.')], HRESULT, 'Add',
              ( ['in'], POINTER(IColor), 'pColor' )),
    COMMETHOD([helpstring(u'Add a color element at the specified posiiton.')], HRESULT, 'Insert',
              ( ['in'], c_int, 'index' ),
              ( ['in'], POINTER(IColor), 'pColor' )),
]
################################################################
## code template for IColorElements implementation
##class IColorElements_Impl(object):
##    @property
##    def Count(self):
##        u'The color elements count.'
##        #return Count
##
##    def Insert(self, index, pColor):
##        u'Add a color element at the specified posiiton.'
##        #return 
##
##    def Remove(self, index):
##        u'Remove color element at the specified position.'
##        #return 
##
##    @property
##    def Element(self, index):
##        u'The color element at the specified position.'
##        #return ppColor
##
##    def RemoveAll(self):
##        u'Remove all color elements.'
##        #return 
##
##    def Add(self, pColor):
##        u'Add a color element.'
##        #return 
##

class IDisplayFilter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the display filter.'
    _iid_ = GUID('{19F85377-1387-11D3-B89C-00600802E603}')
    _idlflags_ = ['oleautomation']
class ITransparencyDisplayFilter(IDisplayFilter):
    _case_insensitive_ = True
    u'Provides access to members that control the Transparency Display Filter.'
    _iid_ = GUID('{19F85378-1387-11D3-B89C-00600802E603}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriDisplayFilterFlags'
esriDFExternalCache = 1
esriDisplayFilterFlags = c_int # enum
IDisplayFilter._methods_ = [
    COMMETHOD(['propput', helpstring(u'RGB value of the filter background color.')], HRESULT, 'BackgroundRGB',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_COLOR, 'RGB' )),
    COMMETHOD(['propget', helpstring(u'RGB value of the filter background color.')], HRESULT, 'BackgroundRGB',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_COLOR), 'RGB' )),
    COMMETHOD(['propput', helpstring(u'Filter flags. Multiple flags may be applied at the same time.')], HRESULT, 'Flags',
              ( ['in'], esriDisplayFilterFlags, 'Flags' )),
    COMMETHOD(['propget', helpstring(u'Filter flags. Multiple flags may be applied at the same time.')], HRESULT, 'Flags',
              ( ['retval', 'out'], POINTER(esriDisplayFilterFlags), 'Flags' )),
    COMMETHOD([helpstring(u'Takes the latest drawing found in the foreground bitmap and applies it to the background bitmap, sending the results to the destination bitmap.')], HRESULT, 'Apply',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'backgroundHDC' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'foregroundHDC' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'destinationHDC' ),
              ( ['in'], c_int, 'clipLeft' ),
              ( ['in'], c_int, 'clipTop' ),
              ( ['in'], c_int, 'clipRight' ),
              ( ['in'], c_int, 'clipBottom' ),
              ( ['in'], c_int, 'destinationLeft' ),
              ( ['in'], c_int, 'destinationTop' )),
]
################################################################
## code template for IDisplayFilter implementation
##class IDisplayFilter_Impl(object):
##    def _get(self):
##        u'RGB value of the filter background color.'
##        #return RGB
##    def _set(self, RGB):
##        u'RGB value of the filter background color.'
##    BackgroundRGB = property(_get, _set, doc = _set.__doc__)
##
##    def Apply(self, backgroundHDC, foregroundHDC, destinationHDC, clipLeft, clipTop, clipRight, clipBottom, destinationLeft, destinationTop):
##        u'Takes the latest drawing found in the foreground bitmap and applies it to the background bitmap, sending the results to the destination bitmap.'
##        #return 
##
##    def _get(self):
##        u'Filter flags. Multiple flags may be applied at the same time.'
##        #return Flags
##    def _set(self, Flags):
##        u'Filter flags. Multiple flags may be applied at the same time.'
##    Flags = property(_get, _set, doc = _set.__doc__)
##

ITransparencyDisplayFilter._methods_ = [
    COMMETHOD(['propput', helpstring(u'Transparency value (0-255).')], HRESULT, 'Transparency',
              ( ['in'], c_short, 'alpha' )),
    COMMETHOD(['propget', helpstring(u'Transparency value (0-255).')], HRESULT, 'Transparency',
              ( ['retval', 'out'], POINTER(c_short), 'alpha' )),
]
################################################################
## code template for ITransparencyDisplayFilter implementation
##class ITransparencyDisplayFilter_Impl(object):
##    def _get(self):
##        u'Transparency value (0-255).'
##        #return alpha
##    def _set(self, alpha):
##        u'Transparency value (0-255).'
##    Transparency = property(_get, _set, doc = _set.__doc__)
##

class ISelectionTracker(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the managing of selection handle tracking.'
    _iid_ = GUID('{E6BDB00C-4D35-11D0-98BE-00805F7CED21}')
    _idlflags_ = ['oleautomation']
class ICalloutTracker(ISelectionTracker):
    _case_insensitive_ = True
    u'Provides access to members that control the callout feedback.'
    _iid_ = GUID('{A761D652-065F-11D4-826F-0080C79F0371}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriTrackerLocation'
LocationNone = 0
LocationInterior = 1
LocationTopLeft = 2
LocationTopMiddle = 3
LocationTopRight = 4
LocationMiddleLeft = 5
LocationMiddleRight = 6
LocationBottomLeft = 7
LocationBottomMiddle = 8
LocationBottomRight = 9
esriTrackerLocation = c_int # enum

# values for enumeration 'esriTrackerStyle'
esriTrackerNormal = 1
esriTrackerDominant = 2
esriTrackerFocus = 4
esriTrackerActive = 8
esriTrackerStyle = c_int # enum
ISelectionTracker._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The display used by the tracker.')], HRESULT, 'Display',
              ( ['in'], POINTER(IScreenDisplay), 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Geometry used for tracking feedback.')], HRESULT, 'Geometry',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'Geometry' )),
    COMMETHOD(['propget', helpstring(u'Geometry used for tracking feedback.')], HRESULT, 'Geometry',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry)), 'Geometry' )),
    COMMETHOD(['propget', helpstring(u'The area covered by the tracker including handles.')], HRESULT, 'Bounds',
              ( ['in'], POINTER(IDisplay), 'Display' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'Bounds' )),
    COMMETHOD([helpstring(u"If the mouse is over the tracker, return an HCURSOR to indicate legal operations based on mouse's relation to selection handles: move resize, etc.  Return 0 if mouse isn't over tracker.")], HRESULT, 'QueryCursor',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' ),
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'Cursor' )),
    COMMETHOD([helpstring(u'Check if mouse is over tracker.  Return a TrackerLocation to indicate which handle mouse is over.')], HRESULT, 'HitTest',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' ),
              ( ['retval', 'out'], POINTER(esriTrackerLocation), 'location' )),
    COMMETHOD([helpstring(u'Draw selection indicater.  Usually a color outline with selection handles.')], HRESULT, 'Draw',
              ( ['in'], POINTER(IDisplay), 'Display' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDC' ),
              ( ['in'], esriTrackerStyle, 'Style' )),
    COMMETHOD([helpstring(u'Begin tracking move or resize based on the location of the mouse over the tracker handles.')], HRESULT, 'OnMouseDown',
              ( ['in'], c_int, 'button' ),
              ( ['in'], c_int, 'shift' ),
              ( ['in'], c_int, 'x' ),
              ( ['in'], c_int, 'y' )),
    COMMETHOD([helpstring(u'In process move or resize tracking.')], HRESULT, 'OnMouseMove',
              ( ['in'], c_int, 'button' ),
              ( ['in'], c_int, 'shift' ),
              ( ['in'], c_int, 'x' ),
              ( ['in'], c_int, 'y' )),
    COMMETHOD([helpstring(u'Finish move or resize tracking.')], HRESULT, 'OnMouseUp',
              ( ['in'], c_int, 'button' ),
              ( ['in'], c_int, 'shift' ),
              ( ['in'], c_int, 'x' ),
              ( ['in'], c_int, 'y' )),
    COMMETHOD([helpstring(u'Special keypress processing while tracking.')], HRESULT, 'OnKeyDown',
              ( ['in'], c_int, 'keyCode' ),
              ( ['in'], c_int, 'shift' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'complete' )),
    COMMETHOD([helpstring(u'Special keypress processing while tracking.')], HRESULT, 'OnKeyUp',
              ( ['in'], c_int, 'keyCode' ),
              ( ['in'], c_int, 'shift' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'complete' )),
    COMMETHOD([helpstring(u'Cancel tracking.')], HRESULT, 'Deactivate',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'complete' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the tracker is locked or not.  Locked means nodes cannot be moved.')], HRESULT, 'Locked',
              ( ['in'], VARIANT_BOOL, 'Locked' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the tracker is locked or not.  Locked means nodes cannot be moved.')], HRESULT, 'Locked',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Locked' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the tracker is showing handles or not.')], HRESULT, 'ShowHandles',
              ( ['in'], VARIANT_BOOL, 'ShowHandles' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the tracker is showing handles or not.')], HRESULT, 'ShowHandles',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ShowHandles' )),
    COMMETHOD([helpstring(u'The move feedback for the selection tracker.')], HRESULT, 'QueryMoveFeedback',
              ( ['in'], POINTER(POINTER(IDisplayFeedback)), 'moveFeedback' )),
    COMMETHOD([helpstring(u'The resize feedback for the selection tracker.')], HRESULT, 'QueryResizeFeedback',
              ( ['in'], POINTER(POINTER(IDisplayFeedback)), 'resizeFeedback' )),
]
################################################################
## code template for ISelectionTracker implementation
##class ISelectionTracker_Impl(object):
##    def Draw(self, Display, hDC, Style):
##        u'Draw selection indicater.  Usually a color outline with selection handles.'
##        #return 
##
##    def _get(self):
##        u'Indicates if the tracker is locked or not.  Locked means nodes cannot be moved.'
##        #return Locked
##    def _set(self, Locked):
##        u'Indicates if the tracker is locked or not.  Locked means nodes cannot be moved.'
##    Locked = property(_get, _set, doc = _set.__doc__)
##
##    def OnKeyDown(self, keyCode, shift):
##        u'Special keypress processing while tracking.'
##        #return complete
##
##    def _get(self):
##        u'Geometry used for tracking feedback.'
##        #return Geometry
##    def _set(self, Geometry):
##        u'Geometry used for tracking feedback.'
##    Geometry = property(_get, _set, doc = _set.__doc__)
##
##    def QueryCursor(self, Point):
##        u"If the mouse is over the tracker, return an HCURSOR to indicate legal operations based on mouse's relation to selection handles: move resize, etc.  Return 0 if mouse isn't over tracker."
##        #return Cursor
##
##    @property
##    def Bounds(self, Display):
##        u'The area covered by the tracker including handles.'
##        #return Bounds
##
##    def OnMouseDown(self, button, shift, x, y):
##        u'Begin tracking move or resize based on the location of the mouse over the tracker handles.'
##        #return 
##
##    def HitTest(self, Point):
##        u'Check if mouse is over tracker.  Return a TrackerLocation to indicate which handle mouse is over.'
##        #return location
##
##    def Deactivate(self):
##        u'Cancel tracking.'
##        #return complete
##
##    def QueryResizeFeedback(self, resizeFeedback):
##        u'The resize feedback for the selection tracker.'
##        #return 
##
##    def OnMouseMove(self, button, shift, x, y):
##        u'In process move or resize tracking.'
##        #return 
##
##    def OnMouseUp(self, button, shift, x, y):
##        u'Finish move or resize tracking.'
##        #return 
##
##    def OnKeyUp(self, keyCode, shift):
##        u'Special keypress processing while tracking.'
##        #return complete
##
##    def QueryMoveFeedback(self, moveFeedback):
##        u'The move feedback for the selection tracker.'
##        #return 
##
##    def Display(self, rhs):
##        u'The display used by the tracker.'
##        #return 
##
##    def _get(self):
##        u'Indicates if the tracker is showing handles or not.'
##        #return ShowHandles
##    def _set(self, ShowHandles):
##        u'Indicates if the tracker is showing handles or not.'
##    ShowHandles = property(_get, _set, doc = _set.__doc__)
##

ICalloutTracker._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The symbol containing the callout the tracker will use.')], HRESULT, 'Symbol',
              ( ['in'], POINTER(ISymbol), 'Symbol' )),
    COMMETHOD(['propget', helpstring(u'The symbol containing the callout the tracker will use.')], HRESULT, 'Symbol',
              ( ['retval', 'out'], POINTER(POINTER(ISymbol)), 'Symbol' )),
    COMMETHOD(['propput', helpstring(u'Geometry used for drawing the symbol.')], HRESULT, 'SymbolGeometry',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'SymbolGeometry' )),
    COMMETHOD(['propget', helpstring(u'Geometry used for drawing the symbol.')], HRESULT, 'SymbolGeometry',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry)), 'SymbolGeometry' )),
]
################################################################
## code template for ICalloutTracker implementation
##class ICalloutTracker_Impl(object):
##    @property
##    def Symbol(self, Symbol):
##        u'The symbol containing the callout the tracker will use.'
##        #return 
##
##    def _get(self):
##        u'Geometry used for drawing the symbol.'
##        #return SymbolGeometry
##    def _set(self, SymbolGeometry):
##        u'Geometry used for drawing the symbol.'
##    SymbolGeometry = property(_get, _set, doc = _set.__doc__)
##

class SimpleLineCallout(CoClass):
    u'A simple line that links text to a specified location.'
    _reg_clsid_ = GUID('{FA37B822-A959-4ACD-834A-0E114BF420B8}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class ICallout(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the callout.'
    _iid_ = GUID('{6A7EF980-6924-11D2-980D-0080C7E04196}')
    _idlflags_ = ['oleautomation']
class ISimpleLineCallout(ICallout):
    _case_insensitive_ = True
    u'Provides access to members that control the Simple Line Callout.'
    _iid_ = GUID('{AD134202-770B-47AB-80BD-E3457C5E3168}')
    _idlflags_ = ['oleautomation']
class ITextBackground(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the text background.'
    _iid_ = GUID('{8FEB6611-2A0D-11D1-9A44-0080C7EC5C96}')
    _idlflags_ = ['oleautomation']
class IQueryGeometry(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control geometry query.'
    _iid_ = GUID('{8E1B88F1-0A46-11D4-8276-0080C79F0371}')
    _idlflags_ = ['oleautomation']
class IDisplayName(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that return the display name of an object.'
    _iid_ = GUID('{F47B9B56-7EFE-4EE4-B7D4-445F93FF390E}')
    _idlflags_ = ['oleautomation']
SimpleLineCallout._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ISimpleLineCallout, ITextBackground, IQueryGeometry, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, IDisplayName, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize]

class IScreenDisplayBasemap(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control Screen Display Basemap drawing.'
    _iid_ = GUID('{5002ADAE-AF04-42DE-86C0-93EC8C6BE487}')
    _idlflags_ = ['oleautomation']
IScreenDisplayBasemap._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if mouse pan is enabled while in basemap mode.')], HRESULT, 'MousePanMode',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bYesNo' )),
    COMMETHOD(['propput', helpstring(u'Indicates if mouse pan is enabled while in basemap mode.')], HRESULT, 'MousePanMode',
              ( ['in'], VARIANT_BOOL, 'bYesNo' )),
    COMMETHOD(['propget', helpstring(u'Indicates if edgepan/roaming pan is enabled while in basemap mode.')], HRESULT, 'EdgePanMode',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bYesNo' )),
    COMMETHOD(['propput', helpstring(u'Indicates if edgepan/roaming pan is enabled while in basemap mode.')], HRESULT, 'EdgePanMode',
              ( ['in'], VARIANT_BOOL, 'bYesNo' )),
    COMMETHOD(['propget', helpstring(u'Indicates if basemap drawing mode is enabled.')], HRESULT, 'BasemapDrawing',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bYesNo' )),
    COMMETHOD([helpstring(u'Enables basemap continuous navigation drawing mode when set to true, disables when set to false.')], HRESULT, 'EnableBasemapMode',
              ( ['in'], VARIANT_BOOL, 'bYesNo' )),
    COMMETHOD([helpstring(u'Indicated if basemap mode is activated and continuous navigation can be performed.')], HRESULT, 'IsBasemapModeActivated',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bYesNo' )),
]
################################################################
## code template for IScreenDisplayBasemap implementation
##class IScreenDisplayBasemap_Impl(object):
##    def IsBasemapModeActivated(self):
##        u'Indicated if basemap mode is activated and continuous navigation can be performed.'
##        #return bYesNo
##
##    def EnableBasemapMode(self, bYesNo):
##        u'Enables basemap continuous navigation drawing mode when set to true, disables when set to false.'
##        #return 
##
##    @property
##    def BasemapDrawing(self):
##        u'Indicates if basemap drawing mode is enabled.'
##        #return bYesNo
##
##    def _get(self):
##        u'Indicates if edgepan/roaming pan is enabled while in basemap mode.'
##        #return bYesNo
##    def _set(self, bYesNo):
##        u'Indicates if edgepan/roaming pan is enabled while in basemap mode.'
##    EdgePanMode = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if mouse pan is enabled while in basemap mode.'
##        #return bYesNo
##    def _set(self, bYesNo):
##        u'Indicates if mouse pan is enabled while in basemap mode.'
##    MousePanMode = property(_get, _set, doc = _set.__doc__)
##

class RepresentationRuleItem(CoClass):
    u'A representation rule item object.'
    _reg_clsid_ = GUID('{A711C536-556C-4FAA-B0C1-2204D7BE546F}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IRepresentationRuleItem(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods defining a representation rule item.'
    _iid_ = GUID('{601B3FF7-F696-42C9-90F4-C9392BC96648}')
    _idlflags_ = ['oleautomation']
RepresentationRuleItem._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRepresentationRuleItem, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

class GraphicAttributeEnumType(CoClass):
    u'Enumeration graphic attribute type.'
    _reg_clsid_ = GUID('{E7B41947-0247-4DFE-983E-E4D05FA7BF31}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IGraphicAttributeType(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the behavior and properties of graphic attribute types.'
    _iid_ = GUID('{C319FF4D-0C1E-47D6-BE35-C80045FE4DCF}')
    _idlflags_ = ['oleautomation']
class IGraphicAttributeEnumType(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods accessing graphic attribute enumeration values.'
    _iid_ = GUID('{48F26326-E4C4-4DA8-B795-BF64BFB644DA}')
    _idlflags_ = ['oleautomation']
GraphicAttributeEnumType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGraphicAttributeType, IGraphicAttributeEnumType]

class IMoveBitmapFeedback(IDisplayFeedback):
    _case_insensitive_ = True
    u'Provides access to members that control the bitmap feedback.'
    _iid_ = GUID('{956B2B6B-C169-441A-9203-6E1B4C2B4FBF}')
    _idlflags_ = ['oleautomation']
IMoveBitmapFeedback._methods_ = [
    COMMETHOD([helpstring(u'Begins a new feedback.')], HRESULT, 'Start',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hBitmap' ),
              ( ['in'], c_int, 'Width' ),
              ( ['in'], c_int, 'Height' ),
              ( ['in'], c_int, 'OffsetX' ),
              ( ['in'], c_int, 'OffsetY' )),
    COMMETHOD([helpstring(u'Stops the feedback.')], HRESULT, 'Stop'),
]
################################################################
## code template for IMoveBitmapFeedback implementation
##class IMoveBitmapFeedback_Impl(object):
##    def Start(self, hBitmap, Width, Height, OffsetX, OffsetY):
##        u'Begins a new feedback.'
##        #return 
##
##    def Stop(self):
##        u'Stops the feedback.'
##        #return 
##

class ILineSymbol(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control line symbols.'
    _iid_ = GUID('{E6BDAA7D-4D35-11D0-98BE-00805F7CED21}')
    _idlflags_ = ['oleautomation']
ILineSymbol._methods_ = [
    COMMETHOD(['propget', helpstring(u'Line symbol color.')], HRESULT, 'Color',
              ( ['retval', 'out'], POINTER(POINTER(IColor)), 'Color' )),
    COMMETHOD(['propput', helpstring(u'Line symbol color.')], HRESULT, 'Color',
              ( ['in'], POINTER(IColor), 'Color' )),
    COMMETHOD(['propget', helpstring(u'Line symbol width.')], HRESULT, 'Width',
              ( ['retval', 'out'], POINTER(c_double), 'Width' )),
    COMMETHOD(['propput', helpstring(u'Line symbol width.')], HRESULT, 'Width',
              ( ['in'], c_double, 'Width' )),
]
################################################################
## code template for ILineSymbol implementation
##class ILineSymbol_Impl(object):
##    def _get(self):
##        u'Line symbol color.'
##        #return Color
##    def _set(self, Color):
##        u'Line symbol color.'
##    Color = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Line symbol width.'
##        #return Width
##    def _set(self, Width):
##        u'Line symbol width.'
##    Width = property(_get, _set, doc = _set.__doc__)
##

class DimDisplayFilter(CoClass):
    u'Esri Dim Display Filter.'
    _reg_clsid_ = GUID('{EA52E3CA-73B3-49CE-BD98-F623F959A24B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IDimDisplayFilter(IDisplayFilter):
    _case_insensitive_ = True
    u'Provides access to members that control the Dim Display Filter.'
    _iid_ = GUID('{673C151A-D04F-440B-80DB-183395E9D83F}')
    _idlflags_ = ['oleautomation']
DimDisplayFilter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDimDisplayFilter, IDisplayFilter, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone]

class SolidColorPattern(CoClass):
    u'A solid color pattern object.'
    _reg_clsid_ = GUID('{29742A05-5999-43E7-9FA1-5370C684F49E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
SolidColorPattern._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IFillPattern, IGraphicAttributes, IGraphicAttributes2, IDrawingOutline, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

class RgbColor(CoClass):
    u'A color in the RGB(Red Green Blue) color system.'
    _reg_clsid_ = GUID('{7EE9C496-D123-11D0-8383-080009B996CC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IRgbColor(IColor):
    _case_insensitive_ = True
    u'Provides access to members that control the RGB color values.'
    _iid_ = GUID('{20CD40B1-8F3D-11D0-8590-0800091A2A72}')
    _idlflags_ = ['oleautomation']
RgbColor._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRgbColor, IColor, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize]

class OutputContext(CoClass):
    u'The context provided to pass from the map context to the output device.'
    _reg_clsid_ = GUID('{1C07BBCB-98EC-4AAE-B095-DCB6B0E1851E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IOutputContext(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that allow to manage the geometry transformation from the map context to the ouput device.'
    _iid_ = GUID('{31D09585-7431-4AE1-BE2B-1FD8233473D1}')
    _idlflags_ = ['oleautomation']
OutputContext._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IOutputContext, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

class IDisplayFeedback2(IDisplayFeedback):
    _case_insensitive_ = True
    u'Properties to avoid clearing reference scale & resolution when drawing feedback with WYSIWYG symbology.'
    _iid_ = GUID('{C003BEC8-E340-42D4-9FBF-661DBC9E5B05}')
    _idlflags_ = ['oleautomation']
class IBezierDisplayFeedback(IDisplayFeedback2):
    _case_insensitive_ = True
    u'Additional Symbol properties for BezierFeedback objects.'
    _iid_ = GUID('{1697F1FD-A932-4DBB-BB44-FFC1D7A9E717}')
    _idlflags_ = ['oleautomation']
IDisplayFeedback2._methods_ = [
    COMMETHOD(['propget', helpstring(u'Determines whether the feedback symbol scales with the display.')], HRESULT, 'SymbolIsWYSIWYG',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'isWYSIWYG' )),
    COMMETHOD(['propput', helpstring(u'Determines whether the feedback symbol scales with the display.')], HRESULT, 'SymbolIsWYSIWYG',
              ( ['in'], VARIANT_BOOL, 'isWYSIWYG' )),
    COMMETHOD(['propget', helpstring(u'Determines whether the feedback symbol should respect reference scale.')], HRESULT, 'UseReferenceScale',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'respectsRefScale' )),
    COMMETHOD(['propput', helpstring(u'Determines whether the feedback symbol should respect reference scale.')], HRESULT, 'UseReferenceScale',
              ( ['in'], VARIANT_BOOL, 'respectsRefScale' )),
]
################################################################
## code template for IDisplayFeedback2 implementation
##class IDisplayFeedback2_Impl(object):
##    def _get(self):
##        u'Determines whether the feedback symbol scales with the display.'
##        #return isWYSIWYG
##    def _set(self, isWYSIWYG):
##        u'Determines whether the feedback symbol scales with the display.'
##    SymbolIsWYSIWYG = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Determines whether the feedback symbol should respect reference scale.'
##        #return respectsRefScale
##    def _set(self, respectsRefScale):
##        u'Determines whether the feedback symbol should respect reference scale.'
##    UseReferenceScale = property(_get, _set, doc = _set.__doc__)
##

IBezierDisplayFeedback._methods_ = [
    COMMETHOD(['propget', helpstring(u'The line symbol used to draw the control arms of a bezier.')], HRESULT, 'ControlArmSymbol',
              ( ['retval', 'out'], POINTER(POINTER(ISymbol)), 'Symbol' )),
    COMMETHOD(['propputref', helpstring(u'The line symbol used to draw the control arms of a bezier.')], HRESULT, 'ControlArmSymbol',
              ( ['in'], POINTER(ISymbol), 'Symbol' )),
    COMMETHOD(['propget', helpstring(u'The marker symbol used to draw the control points of a bezier.')], HRESULT, 'ControlPointSymbol',
              ( ['retval', 'out'], POINTER(POINTER(ISymbol)), 'Symbol' )),
    COMMETHOD(['propputref', helpstring(u'The marker symbol used to draw the control points of a bezier.')], HRESULT, 'ControlPointSymbol',
              ( ['in'], POINTER(ISymbol), 'Symbol' )),
]
################################################################
## code template for IBezierDisplayFeedback implementation
##class IBezierDisplayFeedback_Impl(object):
##    def ControlArmSymbol(self, Symbol):
##        u'The line symbol used to draw the control arms of a bezier.'
##        #return 
##
##    def ControlPointSymbol(self, Symbol):
##        u'The marker symbol used to draw the control points of a bezier.'
##        #return 
##

class ColorElements(CoClass):
    u'A collection of Color objects.'
    _reg_clsid_ = GUID('{41ED1649-94E6-4630-883F-9FA9F346E791}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
ColorElements._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IColorElements, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLVersionSupport]

class TimeDisplayEvents(CoClass):
    u'Helper coclass for working with the nondefault outbound ITimeDisplayEvents interface in VB.'
    _reg_clsid_ = GUID('{6DC0A159-6D65-4045-939C-0C58FA49F3EF}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class ITimeDisplayEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control Display Time Events.'
    _iid_ = GUID('{E99EC344-6801-4FB4-94D7-05E67D67451D}')
    _idlflags_ = ['oleautomation']
TimeDisplayEvents._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown]
TimeDisplayEvents._outgoing_interfaces_ = [ITimeDisplayEvents]

class RubberCircle(CoClass):
    u'Rubberbanding class for circles.'
    _reg_clsid_ = GUID('{5F796F6F-1166-4CE5-BEC8-8EBCDFB4DCA9}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
RubberCircle._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRubberBand, IRubberBand2]

class IDisplayAdmin(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control display administration.'
    _iid_ = GUID('{12E361F0-1907-11D3-80C7-0080C79F0371}')
    _idlflags_ = ['oleautomation']
IDisplayAdmin._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if the current object draws using a filter.')], HRESULT, 'UsesFilter',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'UsesFilter' )),
]
################################################################
## code template for IDisplayAdmin implementation
##class IDisplayAdmin_Impl(object):
##    @property
##    def UsesFilter(self):
##        u'Indicates if the current object draws using a filter.'
##        #return UsesFilter
##

class INewTextFeedback(IDisplayFeedback):
    _case_insensitive_ = True
    u'Provides access to members that control the rotate text feedback.'
    _iid_ = GUID('{B46B915D-D256-481B-82E8-C48ED99F4D19}')
    _idlflags_ = ['oleautomation']
INewTextFeedback._methods_ = [
    COMMETHOD([helpstring(u'Begins a new feedback.')], HRESULT, 'Start',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'cursorPosition' ),
              ( ['in'], c_double, 'ReferenceScale' )),
    COMMETHOD([helpstring(u'Stops the feedback.')], HRESULT, 'Stop'),
]
################################################################
## code template for INewTextFeedback implementation
##class INewTextFeedback_Impl(object):
##    def Start(self, cursorPosition, ReferenceScale):
##        u'Begins a new feedback.'
##        #return 
##
##    def Stop(self):
##        u'Stops the feedback.'
##        #return 
##

class IlluminationProps(CoClass):
    u'Esri Illumination Properties Class.'
    _reg_clsid_ = GUID('{1C352F40-298E-11D3-9F4F-00C04F6BC619}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IIlluminationProps(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control Illumination Properties.'
    _iid_ = GUID('{1C352F3F-298E-11D3-9F4F-00C04F6BC619}')
    _idlflags_ = ['oleautomation']
IlluminationProps._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IIlluminationProps, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone]

class TransparencyDisplayFilter(CoClass):
    u'Esri Transparency Display Filter.'
    _reg_clsid_ = GUID('{AD754A65-13B4-11D3-B89D-00600802E603}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
TransparencyDisplayFilter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ITransparencyDisplayFilter, IDisplayFilter, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone]

class IDisplayTransformation(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ITransformation):
    _case_insensitive_ = True
    u'Provides access to members that control Display Transformation.'
    _iid_ = GUID('{E6BDB000-4D35-11D0-98BE-00805F7CED21}')
    _idlflags_ = ['oleautomation']
IDisplayTransformation._methods_ = [
    COMMETHOD(['propput', helpstring(u'Full extent in world coordinates.')], HRESULT, 'Bounds',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'Bounds' )),
    COMMETHOD(['propget', helpstring(u'Full extent in world coordinates.')], HRESULT, 'Bounds',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'Bounds' )),
    COMMETHOD(['propput', helpstring(u'Visible extent in world coordinates.')], HRESULT, 'VisibleBounds',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'Bounds' )),
    COMMETHOD(['propget', helpstring(u'Visible extent in world coordinates.')], HRESULT, 'VisibleBounds',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'Bounds' )),
    COMMETHOD(['propget', helpstring(u'Device frame in world coordinates.')], HRESULT, 'FittedBounds',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'Bounds' )),
    COMMETHOD(['propget', helpstring(u'Intersection of Bounds and VisibleBounds.')], HRESULT, 'ConstrainedBounds',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'Bounds' )),
    COMMETHOD(['propput', helpstring(u'Visible extent in device coordinates.')], HRESULT, 'DeviceFrame',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.tagRECT), 'Bounds' )),
    COMMETHOD(['propget', helpstring(u'Visible extent in device coordinates.')], HRESULT, 'DeviceFrame',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.tagRECT), 'Bounds' )),
    COMMETHOD(['propput', helpstring(u'Indicates if resolution is tied to visible bounds.  If true, zooming in magnifies contents (i.e., zoom in on page).')], HRESULT, 'ZoomResolution',
              ( ['in'], VARIANT_BOOL, 'flag' )),
    COMMETHOD(['propget', helpstring(u'Indicates if resolution is tied to visible bounds.  If true, zooming in magnifies contents (i.e., zoom in on page).')], HRESULT, 'ZoomResolution',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD(['propput', helpstring(u'Resolution of the device in dots (pixels) per inch.')], HRESULT, 'Resolution',
              ( ['in'], c_double, 'pDpi' )),
    COMMETHOD(['propget', helpstring(u'Resolution of the device in dots (pixels) per inch.')], HRESULT, 'Resolution',
              ( ['retval', 'out'], POINTER(c_double), 'pDpi' )),
    COMMETHOD(['propput', helpstring(u'Rotation angle in degrees.')], HRESULT, 'Rotation',
              ( ['in'], c_double, 'degrees' )),
    COMMETHOD(['propget', helpstring(u'Rotation angle in degrees.')], HRESULT, 'Rotation',
              ( ['retval', 'out'], POINTER(c_double), 'degrees' )),
    COMMETHOD(['propget', helpstring(u'Units used by world coordinates.')], HRESULT, 'Units',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.esriUnits), 'unitsCode' )),
    COMMETHOD(['propput', helpstring(u'Units used by world coordinates.')], HRESULT, 'Units',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.esriUnits, 'unitsCode' )),
    COMMETHOD(['propget', helpstring(u'Scale between FittedBounds and DeviceFrame.')], HRESULT, 'ScaleRatio',
              ( ['retval', 'out'], POINTER(c_double), 'scale' )),
    COMMETHOD(['propput', helpstring(u'Scale between FittedBounds and DeviceFrame.')], HRESULT, 'ScaleRatio',
              ( ['in'], c_double, 'scale' )),
    COMMETHOD(['propget', helpstring(u'Reference scale for computing scaled symbol sizes.')], HRESULT, 'ReferenceScale',
              ( ['retval', 'out'], POINTER(c_double), 'scale' )),
    COMMETHOD(['propput', helpstring(u'Reference scale for computing scaled symbol sizes.')], HRESULT, 'ReferenceScale',
              ( ['in'], c_double, 'scale' )),
    COMMETHOD(['propputref', helpstring(u'Current spatial reference.')], HRESULT, 'SpatialReference',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference), 'SpatialReference' )),
    COMMETHOD(['propget', helpstring(u'Current spatial reference.')], HRESULT, 'SpatialReference',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference)), 'SpatialReference' )),
    COMMETHOD(['propget', helpstring(u'Indicates if transformation object suppresses events.')], HRESULT, 'SuppressEvents',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'SuppressEvents' )),
    COMMETHOD(['propput', helpstring(u'Indicates if transformation object suppresses events.')], HRESULT, 'SuppressEvents',
              ( ['in'], VARIANT_BOOL, 'SuppressEvents' )),
    COMMETHOD([helpstring(u'Transforms a rectangle from device to world space or vice versa.  Use the flags specified by esriDisplayTransformEnum.')], HRESULT, 'TransformRect',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'mapRect' ),
              ( ['in', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.tagRECT), 'devRect' ),
              ( ['in'], c_int, 'options' )),
    COMMETHOD([helpstring(u'Transforms a set of points or measurements from device to world space or vice versa.  Use the flags specified by esriDisplayTransformEnum.')], HRESULT, 'TransformCoords',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.WKSPoint), 'mapPoints' ),
              ( ['in'], POINTER(tagPOINT), 'devPoints' ),
              ( ['in'], c_int, 'numPoints' ),
              ( ['in'], c_int, 'options' )),
    COMMETHOD([helpstring(u'Calculates a point in map coordinates corresponding to the device point.')], HRESULT, 'ToMapPoint',
              ( ['in'], c_int, 'x' ),
              ( ['in'], c_int, 'y' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint)), 'mapPoint' )),
    COMMETHOD([helpstring(u'Calculates device coordinates corresponding to the map point.')], HRESULT, 'FromMapPoint',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'mapPoint' ),
              ( ['out'], POINTER(c_int), 'x' ),
              ( ['out'], POINTER(c_int), 'y' )),
    COMMETHOD([helpstring(u'Calculates a distance in points (1/72 inch) corresponding to the map distance.')], HRESULT, 'ToPoints',
              ( ['in'], c_double, 'mapDistance' ),
              ( ['retval', 'out'], POINTER(c_double), 'pointDistance' )),
    COMMETHOD([helpstring(u'Calculates a map distance corresponding to a point (1/72) distance.')], HRESULT, 'FromPoints',
              ( ['in'], c_double, 'pointDistance' ),
              ( ['retval', 'out'], POINTER(c_double), 'mapDistance' )),
]
################################################################
## code template for IDisplayTransformation implementation
##class IDisplayTransformation_Impl(object):
##    def _get(self):
##        u'Scale between FittedBounds and DeviceFrame.'
##        #return scale
##    def _set(self, scale):
##        u'Scale between FittedBounds and DeviceFrame.'
##    ScaleRatio = property(_get, _set, doc = _set.__doc__)
##
##    def TransformRect(self, mapRect, options):
##        u'Transforms a rectangle from device to world space or vice versa.  Use the flags specified by esriDisplayTransformEnum.'
##        #return devRect
##
##    def TransformCoords(self, mapPoints, devPoints, numPoints, options):
##        u'Transforms a set of points or measurements from device to world space or vice versa.  Use the flags specified by esriDisplayTransformEnum.'
##        #return 
##
##    def _get(self):
##        u'Indicates if transformation object suppresses events.'
##        #return SuppressEvents
##    def _set(self, SuppressEvents):
##        u'Indicates if transformation object suppresses events.'
##    SuppressEvents = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Resolution of the device in dots (pixels) per inch.'
##        #return pDpi
##    def _set(self, pDpi):
##        u'Resolution of the device in dots (pixels) per inch.'
##    Resolution = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def ConstrainedBounds(self):
##        u'Intersection of Bounds and VisibleBounds.'
##        #return Bounds
##
##    def _get(self):
##        u'Full extent in world coordinates.'
##        #return Bounds
##    def _set(self, Bounds):
##        u'Full extent in world coordinates.'
##    Bounds = property(_get, _set, doc = _set.__doc__)
##
##    def ToPoints(self, mapDistance):
##        u'Calculates a distance in points (1/72 inch) corresponding to the map distance.'
##        #return pointDistance
##
##    @property
##    def FittedBounds(self):
##        u'Device frame in world coordinates.'
##        #return Bounds
##
##    def ToMapPoint(self, x, y):
##        u'Calculates a point in map coordinates corresponding to the device point.'
##        #return mapPoint
##
##    def _get(self):
##        u'Visible extent in device coordinates.'
##        #return Bounds
##    def _set(self, Bounds):
##        u'Visible extent in device coordinates.'
##    DeviceFrame = property(_get, _set, doc = _set.__doc__)
##
##    def FromMapPoint(self, mapPoint):
##        u'Calculates device coordinates corresponding to the map point.'
##        #return x, y
##
##    def _get(self):
##        u'Indicates if resolution is tied to visible bounds.  If true, zooming in magnifies contents (i.e., zoom in on page).'
##        #return flag
##    def _set(self, flag):
##        u'Indicates if resolution is tied to visible bounds.  If true, zooming in magnifies contents (i.e., zoom in on page).'
##    ZoomResolution = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Units used by world coordinates.'
##        #return unitsCode
##    def _set(self, unitsCode):
##        u'Units used by world coordinates.'
##    Units = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Rotation angle in degrees.'
##        #return degrees
##    def _set(self, degrees):
##        u'Rotation angle in degrees.'
##    Rotation = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def SpatialReference(self, SpatialReference):
##        u'Current spatial reference.'
##        #return 
##
##    def _get(self):
##        u'Visible extent in world coordinates.'
##        #return Bounds
##    def _set(self, Bounds):
##        u'Visible extent in world coordinates.'
##    VisibleBounds = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Reference scale for computing scaled symbol sizes.'
##        #return scale
##    def _set(self, scale):
##        u'Reference scale for computing scaled symbol sizes.'
##    ReferenceScale = property(_get, _set, doc = _set.__doc__)
##
##    def FromPoints(self, pointDistance):
##        u'Calculates a map distance corresponding to a point (1/72) distance.'
##        #return mapDistance
##

class IMarkerBackground(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the marker background.'
    _iid_ = GUID('{AE41E4F0-DDE7-11D3-8216-0080C79F0371}')
    _idlflags_ = ['oleautomation']
IMarkerBackground._methods_ = [
    COMMETHOD(['propget', helpstring(u'The marker symbol.')], HRESULT, 'MarkerSymbol',
              ( ['retval', 'out'], POINTER(POINTER(IMarkerSymbol)), 'markerSym' )),
    COMMETHOD(['propputref', helpstring(u'The marker symbol.')], HRESULT, 'MarkerSymbol',
              ( ['in'], POINTER(IMarkerSymbol), 'markerSym' )),
    COMMETHOD(['propputref', helpstring(u'The marker box.')], HRESULT, 'MarkerBox',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'rhs' )),
    COMMETHOD([helpstring(u'Queries the boundary of the marker background.')], HRESULT, 'MarkerBackgroundQueryBoundary',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDC' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ITransformation), 'transform' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPolygon), 'boundary' )),
    COMMETHOD([helpstring(u'Draws the marker background.')], HRESULT, 'MarkerBackgroundDraw',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDC' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ITransformation), 'transform' )),
]
################################################################
## code template for IMarkerBackground implementation
##class IMarkerBackground_Impl(object):
##    def MarkerBackgroundDraw(self, hDC, transform):
##        u'Draws the marker background.'
##        #return 
##
##    def MarkerBackgroundQueryBoundary(self, hDC, transform, boundary):
##        u'Queries the boundary of the marker background.'
##        #return 
##
##    def MarkerSymbol(self, markerSym):
##        u'The marker symbol.'
##        #return 
##
##    def MarkerBox(self, rhs):
##        u'The marker box.'
##        #return 
##

class IDisplayAdmin2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control display administration.'
    _iid_ = GUID('{D915EC07-7B4F-47FD-B59B-3252F3A3B610}')
    _idlflags_ = ['oleautomation']
IDisplayAdmin2._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if the current object draws using a display filter.')], HRESULT, 'UsesFilter',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'UsesFilter' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the output from the drawing object requires banding. Generally this is true if the output is raster.')], HRESULT, 'RequiresBanding',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the drawing object blends its output with the background.  For example, if the object is transparent, the background becomes part of its rendering.')], HRESULT, 'DoesBlending',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
]
################################################################
## code template for IDisplayAdmin2 implementation
##class IDisplayAdmin2_Impl(object):
##    @property
##    def RequiresBanding(self):
##        u'Indicates whether the output from the drawing object requires banding. Generally this is true if the output is raster.'
##        #return flag
##
##    @property
##    def DoesBlending(self):
##        u'Indicates whether the drawing object blends its output with the background.  For example, if the object is transparent, the background becomes part of its rendering.'
##        #return flag
##
##    @property
##    def UsesFilter(self):
##        u'Indicates if the current object draws using a display filter.'
##        #return UsesFilter
##

class IDisplayFilterManager(IDisplayAdmin):
    _case_insensitive_ = True
    u'Provides access to members that control display filter management.'
    _iid_ = GUID('{F0815360-19E1-11D3-80C8-0080C79F0371}')
    _idlflags_ = ['oleautomation']
IDisplayFilterManager._methods_ = [
    COMMETHOD(['propput', helpstring(u'The display filter.')], HRESULT, 'DisplayFilter',
              ( ['in'], POINTER(IDisplayFilter), 'DisplayFilter' )),
    COMMETHOD(['propget', helpstring(u'The display filter.')], HRESULT, 'DisplayFilter',
              ( ['retval', 'out'], POINTER(POINTER(IDisplayFilter)), 'DisplayFilter' )),
]
################################################################
## code template for IDisplayFilterManager implementation
##class IDisplayFilterManager_Impl(object):
##    def _get(self):
##        u'The display filter.'
##        #return DisplayFilter
##    def _set(self, DisplayFilter):
##        u'The display filter.'
##    DisplayFilter = property(_get, _set, doc = _set.__doc__)
##

class RubberLine(CoClass):
    u'Rubberbanding class for lines.'
    _reg_clsid_ = GUID('{E6BDB104-4D35-11D0-98BE-00805F7CED21}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
RubberLine._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRubberBand, IRubberBand2]

class GeometricEffectWave(CoClass):
    u'Creates a regular wave from a curve.'
    _reg_clsid_ = GUID('{74352A97-64C6-475D-88A2-A8E05236BA07}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IEditInteraction(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods declaring how graphic attributes interact with a representation tool.'
    _iid_ = GUID('{658053AF-D86C-4A2D-8E9B-3BC7628276FB}')
    _idlflags_ = ['oleautomation']
GeometricEffectWave._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGeometricEffect, IGraphicAttributes, IGraphicAttributes2, IEditInteraction, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

class esriGDICommentBeginTextEx(Structure):
    _recordinfo_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2, 0L, '{B246A69D-281F-4279-9205-1137DDFF51CB}')
class esriGDICommentBeginText(Structure):
    _recordinfo_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2, 0L, '{22A05DF7-BB62-4218-BD51-E41A011A9698}')
esriGDICommentBeginText._fields_ = [
    ('dSignature', c_ulong),
    ('nVersion', c_ulong),
    ('textType', c_short),
]
assert sizeof(esriGDICommentBeginText) == 12, sizeof(esriGDICommentBeginText)
assert alignment(esriGDICommentBeginText) == 4, alignment(esriGDICommentBeginText)
esriGDICommentBeginTextEx._fields_ = [
    ('beginText', esriGDICommentBeginText),
    ('kerningOption', c_short),
    ('trackingVal', c_double),
    ('charWidthScale', c_double),
    ('interwordSpace', c_double),
    ('lineLeading', c_double),
    ('dwnChars', c_ulong),
]
assert sizeof(esriGDICommentBeginTextEx) == 56, sizeof(esriGDICommentBeginTextEx)
assert alignment(esriGDICommentBeginTextEx) == 8, alignment(esriGDICommentBeginTextEx)
class IAnchorPoint(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the tracker anchor point.'
    _iid_ = GUID('{71FC8720-0164-11D2-84A4-0000F875B9C6}')
    _idlflags_ = ['oleautomation']
IAnchorPoint._methods_ = [
    COMMETHOD(['propput', helpstring(u'Location of anchor point.')], HRESULT, 'Point',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
    COMMETHOD(['propget', helpstring(u'Location of anchor point.')], HRESULT, 'Point',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint)), 'Point' )),
    COMMETHOD(['propputref', helpstring(u'Anchor point symbol.')], HRESULT, 'Symbol',
              ( ['in'], POINTER(ISymbol), 'Symbol' )),
    COMMETHOD(['propget', helpstring(u'Anchor point symbol.')], HRESULT, 'Symbol',
              ( ['retval', 'out'], POINTER(POINTER(ISymbol)), 'Symbol' )),
    COMMETHOD(['propget', helpstring(u'Cursor displayed when mouse is over anchor.')], HRESULT, 'Cursor',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'Cursor' )),
    COMMETHOD([helpstring(u'Check if mouse is over anchor.')], HRESULT, 'HitTest',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' ),
              ( ['in'], c_double, 'tol' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'hit' )),
    COMMETHOD([helpstring(u'Draw the anchor.')], HRESULT, 'Draw',
              ( ['in'], POINTER(IDisplay), 'Display' )),
    COMMETHOD([helpstring(u'Move the anchor.')], HRESULT, 'MoveTo',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'pPoint' ),
              ( ['in'], POINTER(IDisplay), 'Display' )),
]
################################################################
## code template for IAnchorPoint implementation
##class IAnchorPoint_Impl(object):
##    def HitTest(self, Point, tol):
##        u'Check if mouse is over anchor.'
##        #return hit
##
##    def MoveTo(self, pPoint, Display):
##        u'Move the anchor.'
##        #return 
##
##    def _get(self):
##        u'Location of anchor point.'
##        #return Point
##    def _set(self, Point):
##        u'Location of anchor point.'
##    Point = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Symbol(self, Symbol):
##        u'Anchor point symbol.'
##        #return 
##
##    def Draw(self, Display):
##        u'Draw the anchor.'
##        #return 
##
##    @property
##    def Cursor(self):
##        u'Cursor displayed when mouse is over anchor.'
##        #return Cursor
##

class IPointCollectionTracker(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control a tracker with a point collection.'
    _iid_ = GUID('{4C929701-12F0-4CE0-BB67-F08F6B65B66B}')
    _idlflags_ = ['oleautomation']
IPointCollectionTracker._methods_ = [
    COMMETHOD([helpstring(u'Finds the node index for the vertex under the given point.  Returns -1 if the point is not within the tolerance distance of a vertex in the point collection.')], HRESULT, 'FindNodeIndex',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'cursorPosition' ),
              ( ['retval', 'out'], POINTER(c_int), 'nodeIndex' )),
]
################################################################
## code template for IPointCollectionTracker implementation
##class IPointCollectionTracker_Impl(object):
##    def FindNodeIndex(self, cursorPosition):
##        u'Finds the node index for the vertex under the given point.  Returns -1 if the point is not within the tolerance distance of a vertex in the point collection.'
##        #return nodeIndex
##

class INewEnvelopeFeedback(IDisplayFeedback):
    _case_insensitive_ = True
    u'Provides access to members that control the creation of a new envelope.'
    _iid_ = GUID('{9BF56F82-4F36-11D1-B6CD-080009B996CC}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriEnvelopeConstraints'
esriEnvelopeConstraintsNone = 0
esriEnvelopeConstraintsSquare = 1
esriEnvelopeConstraintsAspect = 2
esriEnvelopeConstraints = c_int # enum
INewEnvelopeFeedback._methods_ = [
    COMMETHOD([helpstring(u'Begins a normal feedback at the given point.')], HRESULT, 'Start',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
    COMMETHOD([helpstring(u'Stops the feedback and returns the shape.')], HRESULT, 'Stop',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'envelope' )),
    COMMETHOD(['propget', helpstring(u'The constraint on this rubberbander.')], HRESULT, 'Constraint',
              ( ['retval', 'out'], POINTER(esriEnvelopeConstraints), 'constrain' )),
    COMMETHOD(['propput', helpstring(u'The constraint on this rubberbander.')], HRESULT, 'Constraint',
              ( ['in'], esriEnvelopeConstraints, 'constrain' )),
    COMMETHOD(['propget', helpstring(u'The aspect ratio for the custom constraint type.')], HRESULT, 'AspectRatio',
              ( ['retval', 'out'], POINTER(c_double), 'AspectRatio' )),
    COMMETHOD(['propput', helpstring(u'The aspect ratio for the custom constraint type.')], HRESULT, 'AspectRatio',
              ( ['in'], c_double, 'AspectRatio' )),
]
################################################################
## code template for INewEnvelopeFeedback implementation
##class INewEnvelopeFeedback_Impl(object):
##    def Start(self, Point):
##        u'Begins a normal feedback at the given point.'
##        #return 
##
##    def _get(self):
##        u'The aspect ratio for the custom constraint type.'
##        #return AspectRatio
##    def _set(self, AspectRatio):
##        u'The aspect ratio for the custom constraint type.'
##    AspectRatio = property(_get, _set, doc = _set.__doc__)
##
##    def Stop(self):
##        u'Stops the feedback and returns the shape.'
##        #return envelope
##
##    def _get(self):
##        u'The constraint on this rubberbander.'
##        #return constrain
##    def _set(self, constrain):
##        u'The constraint on this rubberbander.'
##    Constraint = property(_get, _set, doc = _set.__doc__)
##

class IModifyCircularArcFeedback(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u"Modifies a circular arc's radius, keeping the endpoints fixed."
    _iid_ = GUID('{BFE90946-43C4-4747-B8C4-B210DC88652D}')
    _idlflags_ = ['oleautomation']
IModifyCircularArcFeedback._methods_ = [
    COMMETHOD([helpstring(u'Start the modify arc feedback.')], HRESULT, 'Start',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ICircularArc), 'Arc' ),
              ( [], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
    COMMETHOD([helpstring(u'Stop the modify arc feedback.')], HRESULT, 'Stop',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ICircularArc)), 'Arc' )),
    COMMETHOD([helpstring(u'Abort the modify arc feedback.')], HRESULT, 'Abort'),
]
################################################################
## code template for IModifyCircularArcFeedback implementation
##class IModifyCircularArcFeedback_Impl(object):
##    def Start(self, Arc, Point):
##        u'Start the modify arc feedback.'
##        #return 
##
##    def Abort(self):
##        u'Abort the modify arc feedback.'
##        #return 
##
##    def Stop(self, Point):
##        u'Stop the modify arc feedback.'
##        #return Arc
##

IDisplay._methods_ = [
    COMMETHOD(['propget', helpstring(u'The transformation used by the display.')], HRESULT, 'DisplayTransformation',
              ( ['retval', 'out'], POINTER(POINTER(IDisplayTransformation)), 'DisplayTransformation' )),
    COMMETHOD(['propput', helpstring(u'The transformation used by the display.')], HRESULT, 'DisplayTransformation',
              ( ['in'], POINTER(IDisplayTransformation), 'DisplayTransformation' )),
    COMMETHOD(['propget', helpstring(u'The bounds of the invalid region. Use after StartDrawing and before FinishDrawing.')], HRESULT, 'ClipEnvelope',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'envelope' )),
    COMMETHOD(['propget', helpstring(u'The invalid region as a set of envelopes. Use after StartDrawing and before FinishDrawing.')], HRESULT, 'ClipEnvelopes',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISet)), 'envelopes' )),
    COMMETHOD(['propget', helpstring(u'User-specified clip shape.  This shape is merged with the invalid region to arrive at the actual clip region.  Must be specified before StartDrawing.')], HRESULT, 'ClipGeometry',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry)), 'Geometry' )),
    COMMETHOD(['propput', helpstring(u'User-specified clip shape.  This shape is merged with the invalid region to arrive at the actual clip region.  Must be specified before StartDrawing.')], HRESULT, 'ClipGeometry',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'Geometry' )),
    COMMETHOD(['propget', helpstring(u'Indicates if display object suppresses events.')], HRESULT, 'SuppressEvents',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'SuppressEvents' )),
    COMMETHOD(['propput', helpstring(u'Indicates if display object suppresses events.')], HRESULT, 'SuppressEvents',
              ( ['in'], VARIANT_BOOL, 'SuppressEvents' )),
    COMMETHOD(['propget', helpstring(u'Display filter.  Must call while in a StartDrawing-FinishDrawing sequence.  Set Filter to 0 to resume normal drawing.')], HRESULT, 'Filter',
              ( ['retval', 'out'], POINTER(POINTER(IDisplayFilter)), 'Filter' )),
    COMMETHOD(['propputref', helpstring(u'Display filter.  Must call while in a StartDrawing-FinishDrawing sequence.  Set Filter to 0 to resume normal drawing.')], HRESULT, 'Filter',
              ( ['in'], POINTER(IDisplayFilter), 'Filter' )),
    COMMETHOD(['propget', helpstring(u'Palette.')], HRESULT, 'hPalette',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'hPalette' )),
    COMMETHOD(['propput', helpstring(u'Palette.')], HRESULT, 'hPalette',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hPalette' )),
    COMMETHOD([helpstring(u'Prepare the display for drawing.  Specify the device context and the cache to draw to (normally esriNoScreenCache).  The ScreenDisplay coclass will automatically create a window device context if you specify hdc = 0.')], HRESULT, 'StartDrawing',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDC' ),
              ( ['in'], c_short, 'cacheID' )),
    COMMETHOD(['propget', helpstring(u'The device context that the display is currently drawing to.  Only valid between calls to StartDrawing and FinishDrawing.')], HRESULT, 'hDC',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'hDC' )),
    COMMETHOD([helpstring(u'Completes drawing.')], HRESULT, 'FinishDrawing'),
    COMMETHOD([helpstring(u'Call frequently during drawing process.')], HRESULT, 'Progress',
              ( ['in'], c_int, 'vertexCount' )),
    COMMETHOD([helpstring(u'Draws specified point on the display.')], HRESULT, 'DrawPoint',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'Point' )),
    COMMETHOD([helpstring(u'Draws specified multipoint on the display.')], HRESULT, 'DrawMultipoint',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'multipoint' )),
    COMMETHOD([helpstring(u'Draws specified rectangle on the display.')], HRESULT, 'DrawRectangle',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'rectangle' )),
    COMMETHOD([helpstring(u'Draws specified line on the display.')], HRESULT, 'DrawPolyline',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'polyline' )),
    COMMETHOD([helpstring(u'Draws specified polygon on the display.')], HRESULT, 'DrawPolygon',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'polygon' )),
    COMMETHOD([helpstring(u'Draws specified text on the display.')], HRESULT, 'DrawText',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'shape' ),
              ( ['in'], BSTR, 'Text' )),
    COMMETHOD([helpstring(u'Sets the symbol used for drawing.  Four different symbols can be specified simultaneously: Marker, Line, Fill, Text.')], HRESULT, 'SetSymbol',
              ( ['in'], POINTER(ISymbol), 'sym' )),
    COMMETHOD(['propget', helpstring(u'Illumination properties used by the display.')], HRESULT, 'IlluminationProps',
              ( ['retval', 'out'], POINTER(POINTER(IIlluminationProps)), 'IlluminationProps' )),
    COMMETHOD(['propput', helpstring(u'Illumination properties used by the display.')], HRESULT, 'IlluminationProps',
              ( ['in'], POINTER(IIlluminationProps), 'IlluminationProps' )),
]
################################################################
## code template for IDisplay implementation
##class IDisplay_Impl(object):
##    def _get(self):
##        u'Illumination properties used by the display.'
##        #return IlluminationProps
##    def _set(self, IlluminationProps):
##        u'Illumination properties used by the display.'
##    IlluminationProps = property(_get, _set, doc = _set.__doc__)
##
##    def Filter(self, Filter):
##        u'Display filter.  Must call while in a StartDrawing-FinishDrawing sequence.  Set Filter to 0 to resume normal drawing.'
##        #return 
##
##    def DrawText(self, shape, Text):
##        u'Draws specified text on the display.'
##        #return 
##
##    def _get(self):
##        u'Palette.'
##        #return hPalette
##    def _set(self, hPalette):
##        u'Palette.'
##    hPalette = property(_get, _set, doc = _set.__doc__)
##
##    def DrawMultipoint(self, multipoint):
##        u'Draws specified multipoint on the display.'
##        #return 
##
##    def _get(self):
##        u'The transformation used by the display.'
##        #return DisplayTransformation
##    def _set(self, DisplayTransformation):
##        u'The transformation used by the display.'
##    DisplayTransformation = property(_get, _set, doc = _set.__doc__)
##
##    def FinishDrawing(self):
##        u'Completes drawing.'
##        #return 
##
##    def DrawPolygon(self, polygon):
##        u'Draws specified polygon on the display.'
##        #return 
##
##    def DrawPolyline(self, polyline):
##        u'Draws specified line on the display.'
##        #return 
##
##    @property
##    def ClipEnvelopes(self):
##        u'The invalid region as a set of envelopes. Use after StartDrawing and before FinishDrawing.'
##        #return envelopes
##
##    def DrawRectangle(self, rectangle):
##        u'Draws specified rectangle on the display.'
##        #return 
##
##    def _get(self):
##        u'User-specified clip shape.  This shape is merged with the invalid region to arrive at the actual clip region.  Must be specified before StartDrawing.'
##        #return Geometry
##    def _set(self, Geometry):
##        u'User-specified clip shape.  This shape is merged with the invalid region to arrive at the actual clip region.  Must be specified before StartDrawing.'
##    ClipGeometry = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def hDC(self):
##        u'The device context that the display is currently drawing to.  Only valid between calls to StartDrawing and FinishDrawing.'
##        #return hDC
##
##    def DrawPoint(self, Point):
##        u'Draws specified point on the display.'
##        #return 
##
##    @property
##    def ClipEnvelope(self):
##        u'The bounds of the invalid region. Use after StartDrawing and before FinishDrawing.'
##        #return envelope
##
##    def Progress(self, vertexCount):
##        u'Call frequently during drawing process.'
##        #return 
##
##    def StartDrawing(self, hDC, cacheID):
##        u'Prepare the display for drawing.  Specify the device context and the cache to draw to (normally esriNoScreenCache).  The ScreenDisplay coclass will automatically create a window device context if you specify hdc = 0.'
##        #return 
##
##    def _get(self):
##        u'Indicates if display object suppresses events.'
##        #return SuppressEvents
##    def _set(self, SuppressEvents):
##        u'Indicates if display object suppresses events.'
##    SuppressEvents = property(_get, _set, doc = _set.__doc__)
##
##    def SetSymbol(self, sym):
##        u'Sets the symbol used for drawing.  Four different symbols can be specified simultaneously: Marker, Line, Fill, Text.'
##        #return 
##


# values for enumeration 'esriEnvelopeEdge'
esriEnvelopeEdgeTopLeft = 0
esriEnvelopeEdgeTopMiddle = 1
esriEnvelopeEdgeTopRight = 2
esriEnvelopeEdgeMiddleLeft = 3
esriEnvelopeEdgeMiddleRight = 4
esriEnvelopeEdgeBottomLeft = 5
esriEnvelopeEdgeBottomMiddle = 6
esriEnvelopeEdgeBottomRight = 7
esriEnvelopeEdge = c_int # enum
class IDicerCallback(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Polygon Dicer.'
    _iid_ = GUID('{E6BDAA7F-4D35-11D0-98BE-00805F7CED21}')
    _idlflags_ = ['oleautomation']
IDicerCallback._methods_ = [
    COMMETHOD([helpstring(u'Prepare the dicer for first time use.')], HRESULT, 'OnPrepare',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDC' )),
    COMMETHOD([helpstring(u'Splits the polygon into a set of trapezoids.')], HRESULT, 'OnDice',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDC' ),
              ( ['in'], POINTER(tagPOINT), 'Points' ),
              ( ['in'], c_int, 'numPoints' )),
    COMMETHOD([helpstring(u'Finish use of dicer.')], HRESULT, 'OnComplete',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDC' ),
              ( ['in'], POINTER(tagPOINT), 'Points' ),
              ( ['in'], POINTER(c_int), 'partCounts' ),
              ( ['in'], c_int, 'numParts' )),
]
################################################################
## code template for IDicerCallback implementation
##class IDicerCallback_Impl(object):
##    def OnDice(self, hDC, Points, numPoints):
##        u'Splits the polygon into a set of trapezoids.'
##        #return 
##
##    def OnPrepare(self, hDC):
##        u'Prepare the dicer for first time use.'
##        #return 
##
##    def OnComplete(self, hDC, Points, partCounts, numParts):
##        u'Finish use of dicer.'
##        #return 
##

class ColorRampElements(CoClass):
    u'A collection of ColorRamp objects.'
    _reg_clsid_ = GUID('{CCDBF37E-7A63-4788-A7CB-2A5B0E98A180}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IColorRampElements(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the ColorRamp Elements Interface.'
    _iid_ = GUID('{5B90AACE-207F-44BA-A16B-203C494DEEFA}')
    _idlflags_ = ['oleautomation']
ColorRampElements._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IColorRampElements, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLVersionSupport]

class esriGDICommentEndFeature(Structure):
    _recordinfo_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2, 0L, '{CEC6C519-AC8C-45EB-8611-BCDBBFB9A42E}')
esriGDICommentEndFeature._fields_ = [
    ('dSignature', c_ulong),
    ('nVersion', c_ulong),
]
assert sizeof(esriGDICommentEndFeature) == 8, sizeof(esriGDICommentEndFeature)
assert alignment(esriGDICommentEndFeature) == 4, alignment(esriGDICommentEndFeature)
class NewCircleFeedback(CoClass):
    u'New circle feedback object.'
    _reg_clsid_ = GUID('{B25AFFF1-5A00-4120-92E0-452E8544E444}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class INewCircleFeedback(IDisplayFeedback):
    _case_insensitive_ = True
    u'Provides access to members that control the new circle feedback object.'
    _iid_ = GUID('{B6F4B6CB-B455-487C-84D0-6F9E2726BA20}')
    _idlflags_ = ['oleautomation']
class INewCircleFeedback2(INewCircleFeedback):
    _case_insensitive_ = True
    u'Interface for a new circle.'
    _iid_ = GUID('{739D687C-BC51-44E8-8330-20594CF5E46F}')
    _idlflags_ = ['oleautomation']
NewCircleFeedback._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, INewCircleFeedback2, IDisplayFeedback2]

class IDynamicMapEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to events that occur when the state of the dynamic display changes.'
    _iid_ = GUID('{5EA97C5F-E7AB-4EB0-8881-F2182924DF52}')
    _idlflags_ = []
class IDynamicDisplay(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to Dynamic Display.'
    _iid_ = GUID('{AF664AD1-130F-4FAE-8277-1F0F78D459AC}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriDynamicMapDrawPhase'
esriDMDPLayers = 0
esriDMDPDynamicLayers = 1
esriDMDPSelection = 2
esriDynamicMapDrawPhase = c_int # enum
IDynamicMapEvents._methods_ = [
    COMMETHOD([helpstring(u'Fired when the dynamic map starts.')], HRESULT, 'DynamicMapStarted',
              ( ['in'], POINTER(IDisplay), 'Display' ),
              ( ['in'], POINTER(IDynamicDisplay), 'dynamicDisplay' )),
    COMMETHOD([helpstring(u'Fired when the dynamic map finishes.')], HRESULT, 'DynamicMapFinished',
              ( ['in'], POINTER(IDisplay), 'Display' ),
              ( ['in'], POINTER(IDynamicDisplay), 'dynamicDisplay' )),
    COMMETHOD([helpstring(u'Fired before the specified phase is drawn.')], HRESULT, 'BeforeDynamicDraw',
              ( ['in'], esriDynamicMapDrawPhase, 'DynamicMapDrawPhase' ),
              ( ['in'], POINTER(IDisplay), 'Display' ),
              ( ['in'], POINTER(IDynamicDisplay), 'dynamicDisplay' )),
    COMMETHOD([helpstring(u'Fired after the specified phase is drawn.')], HRESULT, 'AfterDynamicDraw',
              ( ['in'], esriDynamicMapDrawPhase, 'DynamicMapDrawPhase' ),
              ( ['in'], POINTER(IDisplay), 'Display' ),
              ( ['in'], POINTER(IDynamicDisplay), 'dynamicDisplay' )),
]
################################################################
## code template for IDynamicMapEvents implementation
##class IDynamicMapEvents_Impl(object):
##    def AfterDynamicDraw(self, DynamicMapDrawPhase, Display, dynamicDisplay):
##        u'Fired after the specified phase is drawn.'
##        #return 
##
##    def DynamicMapStarted(self, Display, dynamicDisplay):
##        u'Fired when the dynamic map starts.'
##        #return 
##
##    def DynamicMapFinished(self, Display, dynamicDisplay):
##        u'Fired when the dynamic map finishes.'
##        #return 
##
##    def BeforeDynamicDraw(self, DynamicMapDrawPhase, Display, dynamicDisplay):
##        u'Fired before the specified phase is drawn.'
##        #return 
##

class esriGDICommentBeginFeatureAttribute(Structure):
    _recordinfo_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2, 0L, '{20F3001F-D320-4B5E-828B-8D09771BA090}')
esriGDICommentBeginFeatureAttribute._fields_ = [
    ('dSignature', c_ulong),
    ('nVersion', c_ulong),
]
assert sizeof(esriGDICommentBeginFeatureAttribute) == 8, sizeof(esriGDICommentBeginFeatureAttribute)
assert alignment(esriGDICommentBeginFeatureAttribute) == 4, alignment(esriGDICommentBeginFeatureAttribute)
class esriGDIFeatureHyperlink(Structure):
    _recordinfo_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2, 0L, '{0DB8EFE7-4F38-4B9B-A5DE-04EE81CA6DCF}')
esriGDIFeatureHyperlink._fields_ = [
    ('dSignature', c_ulong),
    ('nVersion', c_ulong),
    ('nURLLen', c_ulong),
]
assert sizeof(esriGDIFeatureHyperlink) == 12, sizeof(esriGDIFeatureHyperlink)
assert alignment(esriGDIFeatureHyperlink) == 4, alignment(esriGDIFeatureHyperlink)
class NewArcFeedback(CoClass):
    u'Feedback object for creating a new circular arc.'
    _reg_clsid_ = GUID('{2A5036A0-4E03-44B7-A6DF-48E0A0D4E8E6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class INewArcFeedback(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Feedback for creating a new circular arc segment.'
    _iid_ = GUID('{EA93435A-E466-4EA7-8A89-F01447536DB6}')
    _idlflags_ = ['oleautomation']
NewArcFeedback._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDisplayFeedback, IDisplayFeedback2, INewArcFeedback]

class ModifySegmentFeedback(CoClass):
    u'Feedback object for modifying a segment.'
    _reg_clsid_ = GUID('{8905F885-499D-4B92-9987-DFE6A8F0AC0C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IModifySegmentFeedback(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Feedback for Moving either the from or two point of a segment.'
    _iid_ = GUID('{6011DA0A-98F9-4568-B99B-F1AE640C2792}')
    _idlflags_ = ['oleautomation']
ModifySegmentFeedback._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDisplayFeedback, IDisplayFeedback2, IModifySegmentFeedback]

IDisplayName._methods_ = [
    COMMETHOD(['propget', helpstring(u'The display name of an object.')], HRESULT, 'NameString',
              ( ['retval', 'out'], POINTER(BSTR), 'DisplayName' )),
]
################################################################
## code template for IDisplayName implementation
##class IDisplayName_Impl(object):
##    @property
##    def NameString(self):
##        u'The display name of an object.'
##        #return DisplayName
##

class ReshapeFeedback2(CoClass):
    u'Feedback object for moving multiple vertices.'
    _reg_clsid_ = GUID('{F9E5D8D2-3CB0-44C8-8CA3-1D95FE8AE47E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IReshapeFeedback2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Moves multiple vertices in a geometry.'
    _iid_ = GUID('{163278CF-4C0E-4645-B8A5-8342B7FC900C}')
    _idlflags_ = ['oleautomation']
ReshapeFeedback2._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDisplayFeedback, IDisplayFeedback2, IReshapeFeedback2]

class esriGDICommentFeatureAttribute(Structure):
    _recordinfo_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2, 0L, '{D0E5B1AF-7079-4F1A-93E5-2D2F93991990}')
esriGDICommentFeatureAttribute._fields_ = [
    ('dSignature', c_ulong),
    ('nVersion', c_ulong),
    ('fieldType', c_ulong),
    ('nAliasLen', c_ulong),
    ('nValueLen', c_ulong),
]
assert sizeof(esriGDICommentFeatureAttribute) == 20, sizeof(esriGDICommentFeatureAttribute)
assert alignment(esriGDICommentFeatureAttribute) == 4, alignment(esriGDICommentFeatureAttribute)
class GraphicAttributeBooleanType(CoClass):
    u'Boolean graphic attribute type.'
    _reg_clsid_ = GUID('{033D684E-4CBC-48EF-89C9-E631419DFE58}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
GraphicAttributeBooleanType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGraphicAttributeType]

class esriGDICommentEndPageLayout(Structure):
    _recordinfo_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2, 0L, '{64820ACC-CA1B-4CEF-A99D-8CAC8AACC2F5}')
esriGDICommentEndPageLayout._fields_ = [
    ('dSignature', c_ulong),
    ('nVersion', c_ulong),
]
assert sizeof(esriGDICommentEndPageLayout) == 8, sizeof(esriGDICommentEndPageLayout)
assert alignment(esriGDICommentEndPageLayout) == 4, alignment(esriGDICommentEndPageLayout)
class IDraw(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control drawing.'
    _iid_ = GUID('{7EF23A93-F475-11D3-9F54-00C04F6BDF0D}')
    _idlflags_ = ['oleautomation']
IDraw._methods_ = [
    COMMETHOD([helpstring(u'Prepares the display for drawing.  Specify the device context and the cache to draw to (normally esriNoScreenCache).')], HRESULT, 'StartDrawing',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDC' ),
              ( ['in'], c_short, 'cacheID' )),
    COMMETHOD([helpstring(u'Complete drawing.')], HRESULT, 'FinishDrawing'),
    COMMETHOD([helpstring(u'Draws the specified shape.')], HRESULT, 'Draw',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'Geometry' )),
    COMMETHOD([helpstring(u'Sets the symbol used for drawing.  Four different symbols can be specified simultaneously: Marker, Line, Fill, Text.')], HRESULT, 'SetSymbol',
              ( ['in'], POINTER(ISymbol), 'sym' )),
    COMMETHOD(['propget', helpstring(u'Custom property.')], HRESULT, 'CustomProperty',
              ( ['retval', 'out'], POINTER(VARIANT), 'CustomProperty' )),
    COMMETHOD(['propput', helpstring(u'Custom property.')], HRESULT, 'CustomProperty',
              ( ['in'], VARIANT, 'CustomProperty' )),
    COMMETHOD(['propget', helpstring(u'Clipping region (polygon or envelope). Use after StartDrawing and before FinishDrawing.')], HRESULT, 'ClipRegion',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry)), 'region' )),
]
################################################################
## code template for IDraw implementation
##class IDraw_Impl(object):
##    def Draw(self, Geometry):
##        u'Draws the specified shape.'
##        #return 
##
##    def SetSymbol(self, sym):
##        u'Sets the symbol used for drawing.  Four different symbols can be specified simultaneously: Marker, Line, Fill, Text.'
##        #return 
##
##    def _get(self):
##        u'Custom property.'
##        #return CustomProperty
##    def _set(self, CustomProperty):
##        u'Custom property.'
##    CustomProperty = property(_get, _set, doc = _set.__doc__)
##
##    def FinishDrawing(self):
##        u'Complete drawing.'
##        #return 
##
##    def StartDrawing(self, hDC, cacheID):
##        u'Prepares the display for drawing.  Specify the device context and the cache to draw to (normally esriNoScreenCache).'
##        #return 
##
##    @property
##    def ClipRegion(self):
##        u'Clipping region (polygon or envelope). Use after StartDrawing and before FinishDrawing.'
##        #return region
##

class NewEnvelopeFeedback(CoClass):
    u'New Envelope Display Feedback Object.'
    _reg_clsid_ = GUID('{D2C13E54-4BEA-11D1-B6CC-080009B996CC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class INewEnvelopeFeedback2(IDisplayFeedback):
    _case_insensitive_ = True
    u'Provides access to members that control creating a new envelope.'
    _iid_ = GUID('{4E08B552-F52B-11D3-9315-00600802E603}')
    _idlflags_ = ['oleautomation']
NewEnvelopeFeedback._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, INewEnvelopeFeedback, INewEnvelopeFeedback2, IDisplayFeedback2]

class GeometricEffectTaperedPolygon(CoClass):
    u'Creates a taper polygon from a line.'
    _reg_clsid_ = GUID('{B8A7BD56-BB56-4BB7-8155-56741D01D8B5}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
GeometricEffectTaperedPolygon._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGeometricEffect, IGraphicAttributes, IGraphicAttributes2, IEditInteraction, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

class esriGDICommentEndMap(Structure):
    _recordinfo_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2, 0L, '{522511B9-05EE-47B3-A113-FA8DF46DA615}')
esriGDICommentEndMap._fields_ = [
    ('dSignature', c_ulong),
    ('nVersion', c_ulong),
]
assert sizeof(esriGDICommentEndMap) == 8, sizeof(esriGDICommentEndMap)
assert alignment(esriGDICommentEndMap) == 4, alignment(esriGDICommentEndMap)
class VertexFeedback(CoClass):
    u'Vertex Display Feedback Object.'
    _reg_clsid_ = GUID('{77748C82-73FC-11D2-8506-0000F875B9C6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IVertexFeedback(IDisplayFeedback):
    _case_insensitive_ = True
    u'Provides access to members that control the vertex feedback.'
    _iid_ = GUID('{77748C81-73FC-11D2-8506-0000F875B9C6}')
    _idlflags_ = ['oleautomation']
VertexFeedback._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IVertexFeedback]

class MoveEnvelopeFeedback(CoClass):
    u'Move Envelope Display Feedback Object.'
    _reg_clsid_ = GUID('{9BF56F83-4F36-11D1-B6CD-080009B996CC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IMoveEnvelopeFeedback(IDisplayFeedback):
    _case_insensitive_ = True
    u'Provides access to members that control the move envelope feedback.'
    _iid_ = GUID('{9BF56F81-4F36-11D1-B6CD-080009B996CC}')
    _idlflags_ = ['oleautomation']
MoveEnvelopeFeedback._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMoveEnvelopeFeedback, IDisplayFeedback, IDisplayFeedback2]

class IStyleGalleryClass(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Style Gallery Class.'
    _iid_ = GUID('{AC0E9824-91CB-11D1-8813-080009EC732A}')
    _idlflags_ = []
IStyleGalleryClass._methods_ = [
    COMMETHOD(['propget', helpstring(u'Name of the Style Gallery Class(as in the stle file).')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'Description for the Style Gallery Class.')], HRESULT, 'Description',
              ( ['retval', 'out'], POINTER(BSTR), 'Description' )),
    COMMETHOD(['propget', helpstring(u'Interface ID for the items in the class.')], HRESULT, 'ItemClass',
              ( ['retval', 'out'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'iid' )),
    COMMETHOD(['propget', helpstring(u'The available types of new items in this class.')], HRESULT, 'NewObjectTypes',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IEnumBSTR)), 'newTypes' )),
    COMMETHOD(['propget', helpstring(u'Creates a new object of the specified type.')], HRESULT, 'NewObject',
              ( ['in'], BSTR, 'newType' ),
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'NewObject' )),
    COMMETHOD(['propget', helpstring(u'The width ratio to 1 height.')], HRESULT, 'PreviewRatio',
              ( ['retval', 'out'], POINTER(c_double), 'ratio' )),
    COMMETHOD([helpstring(u'Draws a preview of a Style Gallery Item of the supported class.')], HRESULT, 'Preview',
              ( ['in'], POINTER(IUnknown), 'galleryItem' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDC' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.tagRECT), 'rectangle' )),
    COMMETHOD([helpstring(u'Edits the properties of a Style Gallery Item of the supported class.')], HRESULT, 'EditProperties',
              ( ['in'], POINTER(POINTER(IUnknown)), 'galleryItem' ),
              ( ['in'], POINTER(comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IComPropertySheetEvents), 'listener' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hWnd' ),
              ( ['out'], POINTER(VARIANT_BOOL), 'ok' )),
]
################################################################
## code template for IStyleGalleryClass implementation
##class IStyleGalleryClass_Impl(object):
##    @property
##    def ItemClass(self):
##        u'Interface ID for the items in the class.'
##        #return iid
##
##    @property
##    def Name(self):
##        u'Name of the Style Gallery Class(as in the stle file).'
##        #return Name
##
##    @property
##    def NewObjectTypes(self):
##        u'The available types of new items in this class.'
##        #return newTypes
##
##    @property
##    def PreviewRatio(self):
##        u'The width ratio to 1 height.'
##        #return ratio
##
##    def EditProperties(self, galleryItem, listener, hWnd):
##        u'Edits the properties of a Style Gallery Item of the supported class.'
##        #return ok
##
##    @property
##    def NewObject(self, newType):
##        u'Creates a new object of the specified type.'
##        #return NewObject
##
##    def Preview(self, galleryItem, hDC, rectangle):
##        u'Draws a preview of a Style Gallery Item of the supported class.'
##        #return 
##
##    @property
##    def Description(self):
##        u'Description for the Style Gallery Class.'
##        #return Description
##

class IDisplay3D(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control drawing methods specific to 3D displays.'
    _iid_ = GUID('{DC8333BD-A1D9-11D3-9F61-00C04F6BC5F4}')
    _idlflags_ = ['oleautomation']
IDisplay3D._methods_ = [
    COMMETHOD(['propput', helpstring(u'The tolerance in pixels used when picking.')], HRESULT, 'ScreenPickTolerance',
              ( ['in'], c_int, 'pixels' )),
    COMMETHOD(['propget', helpstring(u'The tolerance in pixels used when picking.')], HRESULT, 'ScreenPickTolerance',
              ( ['retval', 'out'], POINTER(c_int), 'pixels' )),
    COMMETHOD(['propput', helpstring(u'The scale for point size and line width of symbols.')], HRESULT, 'SymbolScale',
              ( ['in'], c_float, 'scale' )),
    COMMETHOD(['propget', helpstring(u'The scale for point size and line width of symbols.')], HRESULT, 'SymbolScale',
              ( ['retval', 'out'], POINTER(c_float), 'scale' )),
    COMMETHOD([helpstring(u'The limit for the size of a single texture.')], HRESULT, 'PutMaxTextureSize',
              ( ['in'], c_int, 'maxTextureWidth' ),
              ( ['in'], c_int, 'maxTextureHeight' )),
    COMMETHOD([helpstring(u'The limit for the size of a single texture.')], HRESULT, 'GetMaxTextureSize',
              ( ['out'], POINTER(c_int), 'pMaxTextureWidth' ),
              ( ['out'], POINTER(c_int), 'pMaxTextureHeight' )),
    COMMETHOD([helpstring(u'Adds a feature shape to the flash list.')], HRESULT, 'AddFlashFeature',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'pGeometry' )),
    COMMETHOD([helpstring(u'Redraws viewers flashing the features in the flash list.')], HRESULT, 'FlashFeatures'),
    COMMETHOD([helpstring(u'Redraws viewers flashing the given location.')], HRESULT, 'FlashLocation',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'pGeometry' )),
    COMMETHOD([helpstring(u'Flashes a feature shape.')], HRESULT, 'FlashGeometry',
              ( ['in'], POINTER(IUnknown), 'pOwner' ),
              ( ['in'], POINTER(IUnknown), 'feature' )),
]
################################################################
## code template for IDisplay3D implementation
##class IDisplay3D_Impl(object):
##    def FlashFeatures(self):
##        u'Redraws viewers flashing the features in the flash list.'
##        #return 
##
##    def FlashGeometry(self, pOwner, feature):
##        u'Flashes a feature shape.'
##        #return 
##
##    def FlashLocation(self, pGeometry):
##        u'Redraws viewers flashing the given location.'
##        #return 
##
##    def _get(self):
##        u'The scale for point size and line width of symbols.'
##        #return scale
##    def _set(self, scale):
##        u'The scale for point size and line width of symbols.'
##    SymbolScale = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The tolerance in pixels used when picking.'
##        #return pixels
##    def _set(self, pixels):
##        u'The tolerance in pixels used when picking.'
##    ScreenPickTolerance = property(_get, _set, doc = _set.__doc__)
##
##    def AddFlashFeature(self, pGeometry):
##        u'Adds a feature shape to the flash list.'
##        #return 
##
##    def GetMaxTextureSize(self):
##        u'The limit for the size of a single texture.'
##        #return pMaxTextureWidth, pMaxTextureHeight
##
##    def PutMaxTextureSize(self, maxTextureWidth, maxTextureHeight):
##        u'The limit for the size of a single texture.'
##        #return 
##

class ResizeEnvelopeFeedback(CoClass):
    u'Resize Envelope Display Feedback Object.'
    _reg_clsid_ = GUID('{C3182FE2-4FB0-11D1-B6CD-080009B996CC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IResizeEnvelopeFeedback(IDisplayFeedback):
    _case_insensitive_ = True
    u'Provides access to members that control the resize of an envelope.'
    _iid_ = GUID('{C3182FE1-4FB0-11D1-B6CD-080009B996CC}')
    _idlflags_ = ['oleautomation']
class IResizeEnvelopeFeedback2(IDisplayFeedback):
    _case_insensitive_ = True
    u'Provides access to members that control the resize of a rotated element.'
    _iid_ = GUID('{4E08B551-F52B-11D3-9315-00600802E603}')
    _idlflags_ = ['oleautomation']
ResizeEnvelopeFeedback._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IResizeEnvelopeFeedback, IResizeEnvelopeFeedback2, IDisplayFeedback, IDisplayFeedback2]

class esriGDICommentBeginMap(Structure):
    _recordinfo_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2, 0L, '{32F72A89-062F-4175-A759-EA1330A37443}')
esriGDICommentBeginMap._fields_ = [
    ('dSignature', c_ulong),
    ('nVersion', c_ulong),
    ('nDescription', c_ulong),
    ('nPEString', c_ulong),
    ('nViewPort', c_ulong),
    ('nTransform', c_ulong),
    ('nTransformDevice', c_ulong),
    ('nHorizon', c_ulong),
]
assert sizeof(esriGDICommentBeginMap) == 32, sizeof(esriGDICommentBeginMap)
assert alignment(esriGDICommentBeginMap) == 4, alignment(esriGDICommentBeginMap)
class ResizeTextFeedback(CoClass):
    u'Resize Text Display Feedback Object.'
    _reg_clsid_ = GUID('{3D459D38-0843-45CC-949B-BF7FE268B0ED}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IResizeTextFeedback(IDisplayFeedback):
    _case_insensitive_ = True
    u'Provides access to members that control the resize of a text element.'
    _iid_ = GUID('{1C9915FF-239B-49A1-A2F3-C9D0E4173CE1}')
    _idlflags_ = ['oleautomation']
ResizeTextFeedback._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IResizeTextFeedback, IResizeEnvelopeFeedback, IResizeEnvelopeFeedback2, IDisplayFeedback, IDisplayFeedback2]

class esriGDICommentBeginPageLayout(Structure):
    _recordinfo_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2, 0L, '{64D67DE0-6A7D-4091-B892-C48047BD2500}')
esriGDICommentBeginPageLayout._fields_ = [
    ('dSignature', c_ulong),
    ('nVersion', c_ulong),
    ('nFocusMap', c_ulong),
]
assert sizeof(esriGDICommentBeginPageLayout) == 12, sizeof(esriGDICommentBeginPageLayout)
assert alignment(esriGDICommentBeginPageLayout) == 4, alignment(esriGDICommentBeginPageLayout)
class NewLineFeedback(CoClass):
    u'New Line Display Feedback Object.'
    _reg_clsid_ = GUID('{7A8276C4-5483-11D1-B6CF-080009B996CC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class INewLineFeedback(IDisplayFeedback):
    _case_insensitive_ = True
    u'Provides access to members that control the new line display feedback.'
    _iid_ = GUID('{861A7B31-516D-11D1-B6CE-080009B996CC}')
    _idlflags_ = ['oleautomation']
class IGeodeticLineFeedback(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the geodetic properties of line display feedback.'
    _iid_ = GUID('{7C6011A5-8F17-4618-B39A-8B5B15BB7064}')
    _idlflags_ = ['oleautomation']
NewLineFeedback._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, INewLineFeedback, IDisplayFeedback2, IGeodeticLineFeedback]

class NewMultiPointFeedback(CoClass):
    u'New MultiPoint Display Feedback Object.'
    _reg_clsid_ = GUID('{7A8276C3-5483-11D1-B6CF-080009B996CC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class INewMultiPointFeedback(IDisplayFeedback):
    _case_insensitive_ = True
    u'Provides access to members that control the new multi-point display feedback.'
    _iid_ = GUID('{7A8276C1-5483-11D1-B6CF-080009B996CC}')
    _idlflags_ = ['oleautomation']
NewMultiPointFeedback._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, INewMultiPointFeedback, IDisplayFeedback2, IGeodeticLineFeedback]

class IDynamicDrawing(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'IDynamicDrawing Interface'
    _iid_ = GUID('{9D207A58-12D6-47D6-93F8-A5B097C48CA1}')
    _idlflags_ = []
IDynamicDrawing._methods_ = [
    COMMETHOD([helpstring(u'method DynamicDraw')], HRESULT, 'DynamicDraw',
              ( [], POINTER(IDisplay), 'Display' ),
              ( [], POINTER(IDynamicDisplay), 'dynamicDisplay' )),
    COMMETHOD(['propget', helpstring(u'property Get Dirty')], HRESULT, 'Dirty',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Dirty' )),
    COMMETHOD(['propput', helpstring(u'property Get Dirty')], HRESULT, 'Dirty',
              ( ['in'], VARIANT_BOOL, 'Dirty' )),
]
################################################################
## code template for IDynamicDrawing implementation
##class IDynamicDrawing_Impl(object):
##    def _get(self):
##        u'property Get Dirty'
##        #return Dirty
##    def _set(self, Dirty):
##        u'property Get Dirty'
##    Dirty = property(_get, _set, doc = _set.__doc__)
##
##    def DynamicDraw(self, Display, dynamicDisplay):
##        u'method DynamicDraw'
##        #return 
##

class IHlsColor(IColor):
    _case_insensitive_ = True
    u'Provides access to members that control the HLS color model.'
    _iid_ = GUID('{7EE9C491-D123-11D0-8383-080009B996CC}')
    _idlflags_ = ['oleautomation']
IHlsColor._methods_ = [
    COMMETHOD(['propput', helpstring(u'The hue component of an IHlsColor (0-360).')], HRESULT, 'Hue',
              ( ['in'], c_int, 'Hue' )),
    COMMETHOD(['propget', helpstring(u'The hue component of an IHlsColor (0-360).')], HRESULT, 'Hue',
              ( ['retval', 'out'], POINTER(c_int), 'Hue' )),
    COMMETHOD(['propput', helpstring(u'The lightness component of an IHlsColor (0-100).')], HRESULT, 'Lightness',
              ( ['in'], c_int, 'Lightness' )),
    COMMETHOD(['propget', helpstring(u'The lightness component of an IHlsColor (0-100).')], HRESULT, 'Lightness',
              ( ['retval', 'out'], POINTER(c_int), 'Lightness' )),
    COMMETHOD(['propput', helpstring(u'The saturation component of an HlslColor (0-100).')], HRESULT, 'Saturation',
              ( ['in'], c_int, 'Saturation' )),
    COMMETHOD(['propget', helpstring(u'The saturation component of an HlslColor (0-100).')], HRESULT, 'Saturation',
              ( ['retval', 'out'], POINTER(c_int), 'Saturation' )),
]
################################################################
## code template for IHlsColor implementation
##class IHlsColor_Impl(object):
##    def _get(self):
##        u'The hue component of an IHlsColor (0-360).'
##        #return Hue
##    def _set(self, Hue):
##        u'The hue component of an IHlsColor (0-360).'
##    Hue = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The saturation component of an HlslColor (0-100).'
##        #return Saturation
##    def _set(self, Saturation):
##        u'The saturation component of an HlslColor (0-100).'
##    Saturation = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The lightness component of an IHlsColor (0-100).'
##        #return Lightness
##    def _set(self, Lightness):
##        u'The lightness component of an IHlsColor (0-100).'
##    Lightness = property(_get, _set, doc = _set.__doc__)
##

class NewBezierCurveFeedback(CoClass):
    u'New Bezier Curve Display Feedback Object.'
    _reg_clsid_ = GUID('{CF6690BF-CDBF-11D2-9F31-00C04F6BC8DD}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class INewBezierCurveFeedback(IDisplayFeedback):
    _case_insensitive_ = True
    u'Provides access to members that control the new bezier curve display feedback.'
    _iid_ = GUID('{417AF471-CD15-11D2-9F30-00C04F6BC8DD}')
    _idlflags_ = ['oleautomation']
NewBezierCurveFeedback._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, INewBezierCurveFeedback]


# values for enumeration 'esriDraw3DMode'
esriDraw3DSilent = 1
esriDraw3DSelection = 2
esriDraw3DGeography = 4
esriDraw3DGraphics = 8
esriDraw3DOpaque = 16
esriDraw3DTransparent = 32
esriDrawIgnore3DMaterial = 64
esriDraw3DImmediate = 128
esriDraw3DMode = c_int # enum
class MoveLineFeedback(CoClass):
    u'Move Line Display Feedback Object.'
    _reg_clsid_ = GUID('{7A8276C8-5483-11D1-B6CF-080009B996CC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IMoveLineFeedback(IDisplayFeedback):
    _case_insensitive_ = True
    u'Provides access to members that control move line feedback.'
    _iid_ = GUID('{7A8276C7-5483-11D1-B6CF-080009B996CC}')
    _idlflags_ = ['oleautomation']
MoveLineFeedback._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMoveLineFeedback, IGeodeticLineFeedback]


# values for enumeration 'esriTextureInterpolationMode'
esriTexInterpolNearest = 0
esriTexInterpolBilinear = 1
esriTexInterpolMipMap = 2
esriTextureInterpolationMode = c_int # enum
class MovePointFeedback(CoClass):
    u'Move Point Display Feedback Object.'
    _reg_clsid_ = GUID('{29D782C8-2429-11D3-9F36-00C04F6BDD7F}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IMovePointFeedback(IDisplayFeedback):
    _case_insensitive_ = True
    u'Provides access to members that control the move point feedback.'
    _iid_ = GUID('{3C70BADA-2429-11D3-9F36-00C04F6BDD7F}')
    _idlflags_ = ['oleautomation']
MovePointFeedback._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMovePointFeedback, IDisplayFeedback2]


# values for enumeration 'esriColorRampAlgorithm'
esriHSVAlgorithm = 0
esriCIELabAlgorithm = 1
esriLabLChAlgorithm = 2
esriColorRampAlgorithm = c_int # enum
class MovePointFeedback2(CoClass):
    u'Move Points Display Feedback Object.'
    _reg_clsid_ = GUID('{EB5178E6-C8E8-4780-88FC-BD677BEC0E29}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IMovePointFeedback2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Moves multiple vertices in a geometry.'
    _iid_ = GUID('{87E1DDC3-1EE8-482B-86D3-44A37E62ACAB}')
    _idlflags_ = ['oleautomation']
MovePointFeedback2._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDisplayFeedback, IDisplayFeedback2, IMovePointFeedback2]

class IRasterPicture(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the raster picture.'
    _iid_ = GUID('{CFDFA1B1-D5DE-11D3-A414-0004AC1B1D86}')
    _idlflags_ = ['oleautomation']
IRasterPicture._methods_ = [
    COMMETHOD([helpstring(u'Loads the picture.')], HRESULT, 'LoadPicture',
              ( ['in'], BSTR, 'fileName' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IPicture)), 'ppPicture' )),
    COMMETHOD(['propget', helpstring(u'The transparent color if there is any.')], HRESULT, 'TransparentColor',
              ( ['retval', 'out'], POINTER(POINTER(IColor)), 'ppTransparentColor' )),
]
################################################################
## code template for IRasterPicture implementation
##class IRasterPicture_Impl(object):
##    def LoadPicture(self, fileName):
##        u'Loads the picture.'
##        #return ppPicture
##
##    @property
##    def TransparentColor(self):
##        u'The transparent color if there is any.'
##        #return ppTransparentColor
##

class BasicRasterPicture(CoClass):
    u'A lightweight object for displaying some raster formats in a simple manner.'
    _reg_clsid_ = GUID('{13098887-C5D5-436F-84A0-C45890ACBEB7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
BasicRasterPicture._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRasterPicture]

class LineMovePointFeedback(CoClass):
    u'Move Point Line Display Feedback Object.'
    _reg_clsid_ = GUID('{7A8276CC-5483-11D1-B6CF-080009B996CC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class ILineMovePointFeedback(IDisplayFeedback):
    _case_insensitive_ = True
    u'Provides access to members that control the line move point display feedback.'
    _iid_ = GUID('{7A8276CB-5483-11D1-B6CF-080009B996CC}')
    _idlflags_ = ['oleautomation']
LineMovePointFeedback._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ILineMovePointFeedback, IGeodeticLineFeedback]

class IMoveImageFeedback2(IDisplayFeedback):
    _case_insensitive_ = True
    u'Provides access to members that control feedback for moving an image.'
    _iid_ = GUID('{781E1C4C-1BFD-44DE-B524-024437710FAB}')
    _idlflags_ = ['oleautomation']
IMoveImageFeedback2._methods_ = [
    COMMETHOD([helpstring(u'Starts a move.')], HRESULT, 'Start',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Anchor' )),
    COMMETHOD(['propget', helpstring(u'The display to draw into.')], HRESULT, 'Display',
              ( ['retval', 'out'], POINTER(POINTER(IDisplay)), 'Display' )),
    COMMETHOD(['propput', helpstring(u'The bounds of the image.')], HRESULT, 'Bounds',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'rhs' )),
    COMMETHOD([helpstring(u'Clears the image.')], HRESULT, 'ClearImage'),
    COMMETHOD(['propput', helpstring(u'The bounds of the image.')], HRESULT, 'PolygonBounds',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPolygon), 'rhs' )),
]
################################################################
## code template for IMoveImageFeedback2 implementation
##class IMoveImageFeedback2_Impl(object):
##    def _set(self, rhs):
##        u'The bounds of the image.'
##    PolygonBounds = property(fset = _set, doc = _set.__doc__)
##
##    def Start(self, Anchor):
##        u'Starts a move.'
##        #return 
##
##    def ClearImage(self):
##        u'Clears the image.'
##        #return 
##
##    @property
##    def Display(self):
##        u'The display to draw into.'
##        #return Display
##
##    def _set(self, rhs):
##        u'The bounds of the image.'
##    Bounds = property(fset = _set, doc = _set.__doc__)
##

class BezierMovePointFeedback(CoClass):
    u'Move Point Bezier Display Feedback Object.'
    _reg_clsid_ = GUID('{2B9F6607-D580-11D2-9F33-00C04F6BC8DD}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
BezierMovePointFeedback._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ILineMovePointFeedback]

class MovePolygonFeedback(CoClass):
    u'Move Polygon Display Feedback Object.'
    _reg_clsid_ = GUID('{7A8276CA-5483-11D1-B6CF-080009B996CC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IMovePolygonFeedback(IDisplayFeedback):
    _case_insensitive_ = True
    u'Provides access to members that control the move polygon feedback.'
    _iid_ = GUID('{7A8276C9-5483-11D1-B6CF-080009B996CC}')
    _idlflags_ = ['oleautomation']
MovePolygonFeedback._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMovePolygonFeedback, IGeodeticLineFeedback]

IQueryGeometry._methods_ = [
    COMMETHOD([helpstring(u'Gets the actual geometry of the boundary of the object (which may or may not be a polygon).')], HRESULT, 'GetGeometry',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDC' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ITransformation), 'displayTransform' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'drawGeometry' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry)), 'outGeometry' )),
    COMMETHOD([helpstring(u'Queries the envelope of the boundary of the object.')], HRESULT, 'QueryEnvelope',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDC' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ITransformation), 'displayTransform' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'drawGeometry' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'envelope' )),
]
################################################################
## code template for IQueryGeometry implementation
##class IQueryGeometry_Impl(object):
##    def QueryEnvelope(self, hDC, displayTransform, drawGeometry, envelope):
##        u'Queries the envelope of the boundary of the object.'
##        #return 
##
##    def GetGeometry(self, hDC, displayTransform, drawGeometry):
##        u'Gets the actual geometry of the boundary of the object (which may or may not be a polygon).'
##        #return outGeometry
##

class NewPolygonFeedback(CoClass):
    u'New Polygon Display Feedback Object.'
    _reg_clsid_ = GUID('{7A8276C6-5483-11D1-B6CF-080009B996CC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class INewPolygonFeedback(IDisplayFeedback):
    _case_insensitive_ = True
    u'Provides access to members that control the new polygon display feedback.'
    _iid_ = GUID('{7A8276C5-5483-11D1-B6CF-080009B996CC}')
    _idlflags_ = ['oleautomation']
NewPolygonFeedback._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, INewPolygonFeedback, IGeodeticLineFeedback]

class ISimpleLineSymbol(ILineSymbol):
    _case_insensitive_ = True
    u'Provides access to members that control the simple line symbol.'
    _iid_ = GUID('{A9360291-5828-11D0-98BF-00805F7CED21}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriSimpleLineStyle'
esriSLSSolid = 0
esriSLSDash = 1
esriSLSDot = 2
esriSLSDashDot = 3
esriSLSDashDotDot = 4
esriSLSNull = 5
esriSLSInsideFrame = 6
esriSimpleLineStyle = c_int # enum
ISimpleLineSymbol._methods_ = [
    COMMETHOD(['propget', helpstring(u'The style of the line symbol.')], HRESULT, 'Style',
              ( ['retval', 'out'], POINTER(esriSimpleLineStyle), 'Style' )),
    COMMETHOD(['propput', helpstring(u'The style of the line symbol.')], HRESULT, 'Style',
              ( ['in'], esriSimpleLineStyle, 'Style' )),
]
################################################################
## code template for ISimpleLineSymbol implementation
##class ISimpleLineSymbol_Impl(object):
##    def _get(self):
##        u'The style of the line symbol.'
##        #return Style
##    def _set(self, Style):
##        u'The style of the line symbol.'
##    Style = property(_get, _set, doc = _set.__doc__)
##


# values for enumeration 'esriMaskStyle'
esriMSNone = 0
esriMSHalo = 1
esriMaskStyle = c_int # enum
class IPictureMarkerSymbol(IMarkerSymbol):
    _case_insensitive_ = True
    u'Provides access to members that control the raster (bitmap) marker symbol.'
    _iid_ = GUID('{7914E5E9-C892-11D0-8BB6-080009EE4E41}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriIPictureType'
esriIPictureEMF = 0
esriIPictureBitmap = 1
esriIPicturePNG = 2
esriIPictureJPG = 3
esriIPictureGIF = 4
esriIPictureType = c_int # enum
IPictureMarkerSymbol._methods_ = [
    COMMETHOD(['propget', helpstring(u'Picture used for marker symbol.')], HRESULT, 'Picture',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IPictureDisp)), 'pictureDisp' )),
    COMMETHOD(['propputref', helpstring(u'Picture used for marker symbol.')], HRESULT, 'Picture',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IPictureDisp), 'pictureDisp' )),
    COMMETHOD(['propget', helpstring(u'Background color of the picture for 1 bit images.')], HRESULT, 'BackgroundColor',
              ( ['retval', 'out'], POINTER(POINTER(IColor)), 'Color' )),
    COMMETHOD(['propput', helpstring(u'Background color of the picture for 1 bit images.')], HRESULT, 'BackgroundColor',
              ( ['in'], POINTER(IColor), 'Color' )),
    COMMETHOD(['propget', helpstring(u'Color within bitmap indicating transparency.')], HRESULT, 'BitmapTransparencyColor',
              ( ['retval', 'out'], POINTER(POINTER(IColor)), 'Color' )),
    COMMETHOD(['propput', helpstring(u'Color within bitmap indicating transparency.')], HRESULT, 'BitmapTransparencyColor',
              ( ['in'], POINTER(IColor), 'Color' )),
    COMMETHOD(['propget', helpstring(u'Indicates if foreground and background colors are swapped on 1 Bit Images Only.')], HRESULT, 'SwapForeGroundBackGroundColor',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'swap' )),
    COMMETHOD(['propput', helpstring(u'Indicates if foreground and background colors are swapped on 1 Bit Images Only.')], HRESULT, 'SwapForeGroundBackGroundColor',
              ( ['in'], VARIANT_BOOL, 'swap' )),
    COMMETHOD([helpstring(u'Create symbol from picture file.')], HRESULT, 'CreateMarkerSymbolFromFile',
              ( ['in'], esriIPictureType, 'Type' ),
              ( ['in'], BSTR, 'fileName' )),
]
################################################################
## code template for IPictureMarkerSymbol implementation
##class IPictureMarkerSymbol_Impl(object):
##    def Picture(self, pictureDisp):
##        u'Picture used for marker symbol.'
##        #return 
##
##    def _get(self):
##        u'Indicates if foreground and background colors are swapped on 1 Bit Images Only.'
##        #return swap
##    def _set(self, swap):
##        u'Indicates if foreground and background colors are swapped on 1 Bit Images Only.'
##    SwapForeGroundBackGroundColor = property(_get, _set, doc = _set.__doc__)
##
##    def CreateMarkerSymbolFromFile(self, Type, fileName):
##        u'Create symbol from picture file.'
##        #return 
##
##    def _get(self):
##        u'Background color of the picture for 1 bit images.'
##        #return Color
##    def _set(self, Color):
##        u'Background color of the picture for 1 bit images.'
##    BackgroundColor = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Color within bitmap indicating transparency.'
##        #return Color
##    def _set(self, Color):
##        u'Color within bitmap indicating transparency.'
##    BitmapTransparencyColor = property(_get, _set, doc = _set.__doc__)
##

class IMoveImageFeedback(IDisplayFeedback):
    _case_insensitive_ = True
    u'Provides access to members that control feedback for moving an image.'
    _iid_ = GUID('{8C25C471-2030-11D2-A28C-080009B6F22B}')
    _idlflags_ = ['oleautomation']
IMoveImageFeedback._methods_ = [
    COMMETHOD([helpstring(u'Starts a move.')], HRESULT, 'Start',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Anchor' )),
    COMMETHOD(['propget', helpstring(u'The display to draw into.')], HRESULT, 'Display',
              ( ['retval', 'out'], POINTER(POINTER(IDisplay)), 'Display' )),
    COMMETHOD(['propput', helpstring(u'The bounds of the image.')], HRESULT, 'Bounds',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'rhs' )),
    COMMETHOD([helpstring(u'Clears the image.')], HRESULT, 'ClearImage'),
]
################################################################
## code template for IMoveImageFeedback implementation
##class IMoveImageFeedback_Impl(object):
##    def Start(self, Anchor):
##        u'Starts a move.'
##        #return 
##
##    def ClearImage(self):
##        u'Clears the image.'
##        #return 
##
##    @property
##    def Display(self):
##        u'The display to draw into.'
##        #return Display
##
##    def _set(self, rhs):
##        u'The bounds of the image.'
##    Bounds = property(fset = _set, doc = _set.__doc__)
##

class PolygonMovePointFeedback(CoClass):
    u'Move Point Polygon Display Feedback Object.'
    _reg_clsid_ = GUID('{7A8276CE-5483-11D1-B6CF-080009B996CC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IPolygonMovePointFeedback(IDisplayFeedback):
    _case_insensitive_ = True
    u'Provides access to members that control the polygon move point display feedback.'
    _iid_ = GUID('{7A8276CD-5483-11D1-B6CF-080009B996CC}')
    _idlflags_ = ['oleautomation']
PolygonMovePointFeedback._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IPolygonMovePointFeedback, IGeodeticLineFeedback]

class GraphicAttributeDoubleType(CoClass):
    u'Double graphic attribute type.'
    _reg_clsid_ = GUID('{404A14F9-BAB3-4B6C-82B1-9536DBD57C3E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
GraphicAttributeDoubleType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGraphicAttributeType]

IRepresentationRuleInit._methods_ = [
    COMMETHOD([helpstring(u'Initializes the representation rule with a symbol.')], HRESULT, 'InitWithSymbol',
              ( ['in'], POINTER(ISymbol), 'Symbol' )),
]
################################################################
## code template for IRepresentationRuleInit implementation
##class IRepresentationRuleInit_Impl(object):
##    def InitWithSymbol(self, Symbol):
##        u'Initializes the representation rule with a symbol.'
##        #return 
##

class StretchLineFeedback(CoClass):
    u'Stretch Line Display Feedback object.'
    _reg_clsid_ = GUID('{85319ED2-A960-11D1-AE9C-0000F80372B4}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IStretchLineFeedback(IDisplayFeedback):
    _case_insensitive_ = True
    u'Provides access to members that control the stretch line display feedback.'
    _iid_ = GUID('{89967502-A95F-11D1-AE9C-0000F80372B4}')
    _idlflags_ = ['oleautomation']
StretchLineFeedback._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IStretchLineFeedback, IGeodeticLineFeedback]

class IDisplayEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control Display Events.'
    _iid_ = GUID('{E6BDB003-4D35-11D0-98BE-00805F7CED21}')
    _idlflags_ = ['oleautomation']
IDisplayEvents._methods_ = [
    COMMETHOD([helpstring(u'Notifies clients when drawing starts.')], HRESULT, 'DisplayStarted',
              ( ['in'], POINTER(IDisplay), 'Display' )),
    COMMETHOD([helpstring(u'Notifies clients when drawing completes.')], HRESULT, 'DisplayFinished',
              ( ['in'], POINTER(IDisplay), 'Display' )),
    COMMETHOD([helpstring(u'Notifies clients when display is invalidated.')], HRESULT, 'DisplayInvalidated',
              ( ['in'], POINTER(IDisplay), 'Display' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'rect' ),
              ( [], VARIANT_BOOL, 'erase' ),
              ( [], c_short, 'cacheID' )),
    COMMETHOD([helpstring(u'Notifies clients when display is scrolled.')], HRESULT, 'DisplayScrolled',
              ( ['in'], POINTER(IDisplay), 'Display' ),
              ( ['in'], c_int, 'deltaX' ),
              ( ['in'], c_int, 'deltaY' )),
]
################################################################
## code template for IDisplayEvents implementation
##class IDisplayEvents_Impl(object):
##    def DisplayInvalidated(self, Display, rect, erase, cacheID):
##        u'Notifies clients when display is invalidated.'
##        #return 
##
##    def DisplayStarted(self, Display):
##        u'Notifies clients when drawing starts.'
##        #return 
##
##    def DisplayScrolled(self, Display, deltaX, deltaY):
##        u'Notifies clients when display is scrolled.'
##        #return 
##
##    def DisplayFinished(self, Display):
##        u'Notifies clients when drawing completes.'
##        #return 
##

class IScreenDisplay2(IDisplay):
    _case_insensitive_ = True
    u'Provides access to additional members that control the Screen Display.'
    _iid_ = GUID('{DC321087-108F-43AE-932A-DFC1F7C4529E}')
    _idlflags_ = ['oleautomation']
class IScreenDisplay3(IScreenDisplay2):
    _case_insensitive_ = True
    u'Provides access to members that control Screen Display.'
    _iid_ = GUID('{E9C1AFA9-087E-46D2-B864-F9C0B4DD1199}')
    _idlflags_ = ['oleautomation']
IScreenDisplay2._methods_ = [
    COMMETHOD(['propput', helpstring(u'Associated window handle.')], HRESULT, 'hWnd',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hWnd' )),
    COMMETHOD(['propget', helpstring(u'Associated window handle.')], HRESULT, 'hWnd',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'hWnd' )),
    COMMETHOD(['propget', helpstring(u'Device context for the associated window.  Only use this between calls to StartDrawing and FinishDrawing.')], HRESULT, 'WindowDC',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'hDC' )),
    COMMETHOD([helpstring(u'Creates a new cache and return its ID.  The ID can be specified to StartDrawing to direct output to the cache.  It can also be used with a number of other methods such as DrawCache and Invalidate.')], HRESULT, 'AddCache',
              ( ['retval', 'out'], POINTER(c_short), 'cacheID' )),
    COMMETHOD([helpstring(u'Removes the specified cache.')], HRESULT, 'RemoveCache',
              ( ['in'], c_short, 'cacheID' )),
    COMMETHOD(['propget', helpstring(u'Number of screen caches.')], HRESULT, 'CacheCount',
              ( ['retval', 'out'], POINTER(c_short), 'Count' )),
    COMMETHOD([helpstring(u'Removes all caches.')], HRESULT, 'RemoveAllCaches'),
    COMMETHOD(['propget', helpstring(u'Memory device context for the specified screen cache.')], HRESULT, 'CacheMemDC',
              ( ['in'], c_short, 'index' ),
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'hDC' )),
    COMMETHOD(['propput', helpstring(u'Screen cache where drawing occurs. Use rarely.  Change cache inside StartDrawing/FinishDrawing sequence.')], HRESULT, 'ActiveCache',
              ( ['in'], c_short, 'index' )),
    COMMETHOD(['propget', helpstring(u'Screen cache where drawing occurs. Use rarely.  Change cache inside StartDrawing/FinishDrawing sequence.')], HRESULT, 'ActiveCache',
              ( ['retval', 'out'], POINTER(c_short), 'index' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the bottom cache is transparent.')], HRESULT, 'IsFirstCacheTransparent',
              ( ['in'], VARIANT_BOOL, 'flag' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the bottom cache is transparent.')], HRESULT, 'IsFirstCacheTransparent',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD([helpstring(u'Starts recording all output to the recording cache.')], HRESULT, 'StartRecording'),
    COMMETHOD([helpstring(u'Stops recording to the recording cache.')], HRESULT, 'StopRecording'),
    COMMETHOD(['propput', helpstring(u'Indicates if scrollbars should appear.')], HRESULT, 'UseScrollbars',
              ( ['in'], VARIANT_BOOL, 'flag' )),
    COMMETHOD(['propget', helpstring(u'Indicates if scrollbars should appear.')], HRESULT, 'UseScrollbars',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD([helpstring(u'Optionally specify application supplied scrollbars.')], HRESULT, 'SetScrollbarHandles',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hWndHorzScrollbar' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hWndVertScrollbar' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the contents of the screen scale when a resize occurs.  True means scale contents to fit new window size.  False means contents stays the same with more or less of it showing.')], HRESULT, 'ScaleContents',
              ( ['in'], VARIANT_BOOL, 'flag' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the contents of the screen scale when a resize occurs.  True means scale contents to fit new window size.  False means contents stays the same with more or less of it showing.')], HRESULT, 'ScaleContents',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD(['propput', helpstring(u"Indicates if display resizing is suppressed.  True means the display doesn't resize with the window.  False ensures that the display is the same size as the window.")], HRESULT, 'SuppressResize',
              ( ['in'], VARIANT_BOOL, 'SuppressResize' )),
    COMMETHOD(['propget', helpstring(u"Indicates if display resizing is suppressed.  True means the display doesn't resize with the window.  False ensures that the display is the same size as the window.")], HRESULT, 'SuppressResize',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'SuppressResize' )),
    COMMETHOD(['propget', helpstring(u'Indicates if drawing occurs in a frame rather than on the whole window.')], HRESULT, 'IsFramed',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD(['propput', helpstring(u'Indicates if drawing occurs in a frame rather than on the whole window.')], HRESULT, 'IsFramed',
              ( ['in'], VARIANT_BOOL, 'flag' )),
    COMMETHOD(['propget', helpstring(u'Cancel tracker that is associated with the display.')], HRESULT, 'CancelTracker',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel)), 'CancelTracker' )),
    COMMETHOD(['propputref', helpstring(u'Cancel tracker that is associated with the display.')], HRESULT, 'CancelTracker',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'CancelTracker' )),
    COMMETHOD([helpstring(u'Cause the specified area of the specified cache to redraw.')], HRESULT, 'Invalidate',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'rect' ),
              ( ['in'], VARIANT_BOOL, 'erase' ),
              ( ['in'], c_short, 'cacheIndex' )),
    COMMETHOD([helpstring(u'Indicates if the specified cache needs refreshing.')], HRESULT, 'IsCacheDirty',
              ( ['in'], c_short, 'cacheIndex' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD([helpstring(u'Draws the specified screen cache to the specified window device context. Pass an empty rectangle to copy the full bitmap to the DC origin.')], HRESULT, 'DrawCache',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDC' ),
              ( ['in'], c_short, 'index' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.tagRECT), 'deviceRect' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.tagRECT), 'cacheRect' )),
    COMMETHOD([helpstring(u'Scrolls the screen by the specified amount.')], HRESULT, 'DoScroll',
              ( ['in'], c_int, 'xDelta' ),
              ( ['in'], c_int, 'yDelta' ),
              ( ['in'], VARIANT_BOOL, 'updateScreen' )),
    COMMETHOD([helpstring(u'Interactively pans the screen.')], HRESULT, 'TrackPan'),
    COMMETHOD([helpstring(u'Prepares display for panning.')], HRESULT, 'PanStart',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'mouseLocation' )),
    COMMETHOD([helpstring(u'Pans to a new point.')], HRESULT, 'PanMoveTo',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'mouseLocation' )),
    COMMETHOD([helpstring(u'Stops panning and returns new visible bounds.')], HRESULT, 'PanStop',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'newExtent' )),
    COMMETHOD([helpstring(u'Interactively rotates the screen.')], HRESULT, 'TrackRotate'),
    COMMETHOD([helpstring(u'Prepares display for rotating.  If centerPt is NULL, the center of the visible bounds is used.')], HRESULT, 'RotateStart',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'mousePt' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'centerPt' )),
    COMMETHOD([helpstring(u'Rotates to new point.')], HRESULT, 'RotateMoveTo',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'pPoint' )),
    COMMETHOD([helpstring(u'Draws the rotated display. Call in response to WM_TIMER.')], HRESULT, 'RotateTimer'),
    COMMETHOD([helpstring(u'Stops rotating and returns new angle.')], HRESULT, 'RotateStop',
              ( ['retval', 'out'], POINTER(c_double), 'degrees' )),
    COMMETHOD([helpstring(u'Forces a redraw.')], HRESULT, 'UpdateWindow'),
    COMMETHOD(['propput', helpstring(u'The RGB value of the background color.  This color only appears on the screen, not on output.')], HRESULT, 'BackgroundRGB',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_COLOR, 'RGB' )),
    COMMETHOD(['propget', helpstring(u'The RGB value of the background color.  This color only appears on the screen, not on output.')], HRESULT, 'BackgroundRGB',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_COLOR), 'RGB' )),
    COMMETHOD(['propget', helpstring(u'The offset between the device origin and the active cache origin.')], HRESULT, 'DrawingOffset',
              ( ['out'], POINTER(c_int), 'x' ),
              ( ['out'], POINTER(c_int), 'y' )),
    COMMETHOD([helpstring(u'Clear dirty flag for specified cache.')], HRESULT, 'Validate',
              ( ['in'], c_short, 'cacheIndex' )),
    COMMETHOD([helpstring(u"Prepare the display for drawing selection/rubberbanding.  Drawing isn't clipped or zoomed with page. Must match with a call to FinishFeedback.")], HRESULT, 'StartFeedback'),
    COMMETHOD([helpstring(u'Ends feedback drawing.')], HRESULT, 'FinishFeedback'),
    COMMETHOD([helpstring(u'Call on frame display when container is scrolled.')], HRESULT, 'FrameScrolled',
              ( ['in'], c_int, 'x' ),
              ( ['in'], c_int, 'y' )),
]
################################################################
## code template for IScreenDisplay2 implementation
##class IScreenDisplay2_Impl(object):
##    def FrameScrolled(self, x, y):
##        u'Call on frame display when container is scrolled.'
##        #return 
##
##    def PanStart(self, mouseLocation):
##        u'Prepares display for panning.'
##        #return 
##
##    def _get(self):
##        u'Associated window handle.'
##        #return hWnd
##    def _set(self, hWnd):
##        u'Associated window handle.'
##    hWnd = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the contents of the screen scale when a resize occurs.  True means scale contents to fit new window size.  False means contents stays the same with more or less of it showing.'
##        #return flag
##    def _set(self, flag):
##        u'Indicates if the contents of the screen scale when a resize occurs.  True means scale contents to fit new window size.  False means contents stays the same with more or less of it showing.'
##    ScaleContents = property(_get, _set, doc = _set.__doc__)
##
##    def FinishFeedback(self):
##        u'Ends feedback drawing.'
##        #return 
##
##    @property
##    def WindowDC(self):
##        u'Device context for the associated window.  Only use this between calls to StartDrawing and FinishDrawing.'
##        #return hDC
##
##    def PanMoveTo(self, mouseLocation):
##        u'Pans to a new point.'
##        #return 
##
##    def RotateTimer(self):
##        u'Draws the rotated display. Call in response to WM_TIMER.'
##        #return 
##
##    def StopRecording(self):
##        u'Stops recording to the recording cache.'
##        #return 
##
##    @property
##    def CacheMemDC(self, index):
##        u'Memory device context for the specified screen cache.'
##        #return hDC
##
##    def _get(self):
##        u'Indicates if drawing occurs in a frame rather than on the whole window.'
##        #return flag
##    def _set(self, flag):
##        u'Indicates if drawing occurs in a frame rather than on the whole window.'
##    IsFramed = property(_get, _set, doc = _set.__doc__)
##
##    def Validate(self, cacheIndex):
##        u'Clear dirty flag for specified cache.'
##        #return 
##
##    def CancelTracker(self, CancelTracker):
##        u'Cancel tracker that is associated with the display.'
##        #return 
##
##    def RemoveCache(self, cacheID):
##        u'Removes the specified cache.'
##        #return 
##
##    def StartFeedback(self):
##        u"Prepare the display for drawing selection/rubberbanding.  Drawing isn't clipped or zoomed with page. Must match with a call to FinishFeedback."
##        #return 
##
##    def IsCacheDirty(self, cacheIndex):
##        u'Indicates if the specified cache needs refreshing.'
##        #return flag
##
##    def AddCache(self):
##        u'Creates a new cache and return its ID.  The ID can be specified to StartDrawing to direct output to the cache.  It can also be used with a number of other methods such as DrawCache and Invalidate.'
##        #return cacheID
##
##    def Invalidate(self, rect, erase, cacheIndex):
##        u'Cause the specified area of the specified cache to redraw.'
##        #return 
##
##    def DrawCache(self, hDC, index, deviceRect, cacheRect):
##        u'Draws the specified screen cache to the specified window device context. Pass an empty rectangle to copy the full bitmap to the DC origin.'
##        #return 
##
##    def TrackPan(self):
##        u'Interactively pans the screen.'
##        #return 
##
##    def TrackRotate(self):
##        u'Interactively rotates the screen.'
##        #return 
##
##    def _get(self):
##        u'The RGB value of the background color.  This color only appears on the screen, not on output.'
##        #return RGB
##    def _set(self, RGB):
##        u'The RGB value of the background color.  This color only appears on the screen, not on output.'
##    BackgroundRGB = property(_get, _set, doc = _set.__doc__)
##
##    def StartRecording(self):
##        u'Starts recording all output to the recording cache.'
##        #return 
##
##    def RotateMoveTo(self, pPoint):
##        u'Rotates to new point.'
##        #return 
##
##    def RotateStop(self):
##        u'Stops rotating and returns new angle.'
##        #return degrees
##
##    def UpdateWindow(self):
##        u'Forces a redraw.'
##        #return 
##
##    def _get(self):
##        u'Indicates if the bottom cache is transparent.'
##        #return flag
##    def _set(self, flag):
##        u'Indicates if the bottom cache is transparent.'
##    IsFirstCacheTransparent = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def CacheCount(self):
##        u'Number of screen caches.'
##        #return Count
##
##    def PanStop(self):
##        u'Stops panning and returns new visible bounds.'
##        #return newExtent
##
##    def _get(self):
##        u'Indicates if scrollbars should appear.'
##        #return flag
##    def _set(self, flag):
##        u'Indicates if scrollbars should appear.'
##    UseScrollbars = property(_get, _set, doc = _set.__doc__)
##
##    def RemoveAllCaches(self):
##        u'Removes all caches.'
##        #return 
##
##    def RotateStart(self, mousePt, centerPt):
##        u'Prepares display for rotating.  If centerPt is NULL, the center of the visible bounds is used.'
##        #return 
##
##    @property
##    def DrawingOffset(self):
##        u'The offset between the device origin and the active cache origin.'
##        #return x, y
##
##    def DoScroll(self, xDelta, yDelta, updateScreen):
##        u'Scrolls the screen by the specified amount.'
##        #return 
##
##    def _get(self):
##        u'Screen cache where drawing occurs. Use rarely.  Change cache inside StartDrawing/FinishDrawing sequence.'
##        #return index
##    def _set(self, index):
##        u'Screen cache where drawing occurs. Use rarely.  Change cache inside StartDrawing/FinishDrawing sequence.'
##    ActiveCache = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u"Indicates if display resizing is suppressed.  True means the display doesn't resize with the window.  False ensures that the display is the same size as the window."
##        #return SuppressResize
##    def _set(self, SuppressResize):
##        u"Indicates if display resizing is suppressed.  True means the display doesn't resize with the window.  False ensures that the display is the same size as the window."
##    SuppressResize = property(_get, _set, doc = _set.__doc__)
##
##    def SetScrollbarHandles(self, hWndHorzScrollbar, hWndVertScrollbar):
##        u'Optionally specify application supplied scrollbars.'
##        #return 
##

IScreenDisplay3._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates whether the cuser is currently navigating.')], HRESULT, 'IsNavigating',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'navigating' )),
    COMMETHOD(['propget', helpstring(u'Indicates if this is a complete or a partial redraw.')], HRESULT, 'FullRedraw',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'b' )),
]
################################################################
## code template for IScreenDisplay3 implementation
##class IScreenDisplay3_Impl(object):
##    @property
##    def IsNavigating(self):
##        u'Indicates whether the cuser is currently navigating.'
##        #return navigating
##
##    @property
##    def FullRedraw(self):
##        u'Indicates if this is a complete or a partial redraw.'
##        #return b
##

class MoveGeometryFeedback(CoClass):
    u'Display feedback for tracking geometry move.'
    _reg_clsid_ = GUID('{521B9DF4-0166-11D2-A254-080009B6F22B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IMoveGeometryFeedback(IDisplayFeedback):
    _case_insensitive_ = True
    u'Provides access to members that control feedback for moving a group of geometry.'
    _iid_ = GUID('{521B9DF3-0166-11D2-A254-080009B6F22B}')
    _idlflags_ = ['oleautomation']
MoveGeometryFeedback._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMoveGeometryFeedback, IDisplayFeedback2]

ITimeDisplayEvents._methods_ = [
    COMMETHOD([helpstring(u'Notifies clients when display time changed.')], HRESULT, 'DisplayTimeChanged',
              ( ['in'], POINTER(IDisplay), 'Display' ),
              ( [], VARIANT, 'oldValue' ),
              ( [], VARIANT, 'newValue' )),
]
################################################################
## code template for ITimeDisplayEvents implementation
##class ITimeDisplayEvents_Impl(object):
##    def DisplayTimeChanged(self, Display, oldValue, newValue):
##        u'Notifies clients when display time changed.'
##        #return 
##

class GeometricEffectSimplify(CoClass):
    u'Simplifies a geometry by eliminating vertices.'
    _reg_clsid_ = GUID('{3D19D184-B820-49FB-953E-8FF96CAD5D11}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
GeometricEffectSimplify._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGeometricEffect, IGraphicAttributes, IGraphicAttributes2, IEditInteraction, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

class GroupFeedback(CoClass):
    u'Feedback for a group of feedback objects.'
    _reg_clsid_ = GUID('{44276912-98C1-11D1-8464-0000F875B9C6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
GroupFeedback._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDisplayFeedback, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISet]

class CalloutFeedback(CoClass):
    u'Move Callout Display Feedback Object.'
    _reg_clsid_ = GUID('{E4543892-040C-11D4-8267-0080C79F0371}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class ICalloutFeedback(IDisplayFeedback):
    _case_insensitive_ = True
    u'Provides access to members that control the callout feedback.'
    _iid_ = GUID('{E4543891-040C-11D4-8267-0080C79F0371}')
    _idlflags_ = ['oleautomation']
class ICalloutFeedback2(IDisplayFeedback):
    _case_insensitive_ = True
    u'Provides access to members that control the callout feedback.'
    _iid_ = GUID('{B48FFE7A-396B-4188-B4DD-85E9D7E16B3E}')
    _idlflags_ = ['oleautomation']
CalloutFeedback._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ICalloutFeedback, ICalloutFeedback2, IGeodeticLineFeedback]

class IPictureLineSymbol(ILineSymbol):
    _case_insensitive_ = True
    u'Provides access to members that control the picture line symbol.'
    _iid_ = GUID('{22C8C5A0-84FC-11D4-834D-0080C79F0371}')
    _idlflags_ = ['oleautomation']
IPictureLineSymbol._methods_ = [
    COMMETHOD(['propget', helpstring(u'Picture used for line.')], HRESULT, 'Picture',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IPictureDisp)), 'pictureDisp' )),
    COMMETHOD(['propputref', helpstring(u'Picture used for line.')], HRESULT, 'Picture',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IPictureDisp), 'pictureDisp' )),
    COMMETHOD(['propget', helpstring(u'Line background color.')], HRESULT, 'BackgroundColor',
              ( ['retval', 'out'], POINTER(POINTER(IColor)), 'Color' )),
    COMMETHOD(['propput', helpstring(u'Line background color.')], HRESULT, 'BackgroundColor',
              ( ['in'], POINTER(IColor), 'Color' )),
    COMMETHOD(['propput', helpstring(u'Color within bitmap indicating transparency.')], HRESULT, 'BitmapTransparencyColor',
              ( ['in'], POINTER(IColor), 'Color' )),
    COMMETHOD(['propget', helpstring(u'Color within bitmap indicating transparency.')], HRESULT, 'BitmapTransparencyColor',
              ( ['retval', 'out'], POINTER(POINTER(IColor)), 'Color' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the picture is rotated to follow the line.')], HRESULT, 'Rotate',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Rotate' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the picture is rotated to follow the line.')], HRESULT, 'Rotate',
              ( ['in'], VARIANT_BOOL, 'Rotate' )),
    COMMETHOD(['propget', helpstring(u'Scale of picture along X-axis.')], HRESULT, 'XScale',
              ( ['retval', 'out'], POINTER(c_double), 'XScale' )),
    COMMETHOD(['propput', helpstring(u'Scale of picture along X-axis.')], HRESULT, 'XScale',
              ( ['in'], c_double, 'XScale' )),
    COMMETHOD(['propget', helpstring(u'Scale of picture along Y-axis.')], HRESULT, 'YScale',
              ( ['retval', 'out'], POINTER(c_double), 'YScale' )),
    COMMETHOD(['propput', helpstring(u'Scale of picture along Y-axis.')], HRESULT, 'YScale',
              ( ['in'], c_double, 'YScale' )),
    COMMETHOD(['propget', helpstring(u'Picture offset from center of line.')], HRESULT, 'Offset',
              ( ['retval', 'out'], POINTER(c_double), 'Offset' )),
    COMMETHOD(['propput', helpstring(u'Picture offset from center of line.')], HRESULT, 'Offset',
              ( ['in'], c_double, 'Offset' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the foreground and background colors are swapped on 1 Bit Images Only.')], HRESULT, 'SwapForeGroundBackGroundColor',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'swap' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the foreground and background colors are swapped on 1 Bit Images Only.')], HRESULT, 'SwapForeGroundBackGroundColor',
              ( ['in'], VARIANT_BOOL, 'swap' )),
    COMMETHOD([helpstring(u'Create line symbol from picture file.')], HRESULT, 'CreateLineSymbolFromFile',
              ( ['in'], esriIPictureType, 'Type' ),
              ( ['in'], BSTR, 'fileName' )),
]
################################################################
## code template for IPictureLineSymbol implementation
##class IPictureLineSymbol_Impl(object):
##    def Picture(self, pictureDisp):
##        u'Picture used for line.'
##        #return 
##
##    def _get(self):
##        u'Indicates if the foreground and background colors are swapped on 1 Bit Images Only.'
##        #return swap
##    def _set(self, swap):
##        u'Indicates if the foreground and background colors are swapped on 1 Bit Images Only.'
##    SwapForeGroundBackGroundColor = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the picture is rotated to follow the line.'
##        #return Rotate
##    def _set(self, Rotate):
##        u'Indicates if the picture is rotated to follow the line.'
##    Rotate = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Scale of picture along Y-axis.'
##        #return YScale
##    def _set(self, YScale):
##        u'Scale of picture along Y-axis.'
##    YScale = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Color within bitmap indicating transparency.'
##        #return Color
##    def _set(self, Color):
##        u'Color within bitmap indicating transparency.'
##    BitmapTransparencyColor = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Line background color.'
##        #return Color
##    def _set(self, Color):
##        u'Line background color.'
##    BackgroundColor = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Picture offset from center of line.'
##        #return Offset
##    def _set(self, Offset):
##        u'Picture offset from center of line.'
##    Offset = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Scale of picture along X-axis.'
##        #return XScale
##    def _set(self, XScale):
##        u'Scale of picture along X-axis.'
##    XScale = property(_get, _set, doc = _set.__doc__)
##
##    def CreateLineSymbolFromFile(self, Type, fileName):
##        u'Create line symbol from picture file.'
##        #return 
##

class IScreenDisplayOverlays(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control Screen Display Overlays.'
    _iid_ = GUID('{6701B79E-3BB2-4E01-8A21-F9B4B68AE3AB}')
    _idlflags_ = ['oleautomation']
class IScreenDisplayOverlaysCallback(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Screen Display Overlays callback for client rendering to overlay cache.'
    _iid_ = GUID('{BE14E630-1139-44FA-970B-0E35179628F2}')
    _idlflags_ = ['oleautomation']
IScreenDisplayOverlays._methods_ = [
    COMMETHOD(['propput', helpstring(u'Indicates if overlays are visible or not.')], HRESULT, 'ShowOverlays',
              ( ['in'], VARIANT_BOOL, 'bYesNo' )),
    COMMETHOD(['propget', helpstring(u'Indicates if overlays are visible or not.')], HRESULT, 'ShowOverlays',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bYesNo' )),
    COMMETHOD(['propput', helpstring(u'Set the draw call back.')], HRESULT, 'OverlaysCallback',
              ( ['in'], POINTER(IScreenDisplayOverlaysCallback), 'rhs' )),
]
################################################################
## code template for IScreenDisplayOverlays implementation
##class IScreenDisplayOverlays_Impl(object):
##    def _get(self):
##        u'Indicates if overlays are visible or not.'
##        #return bYesNo
##    def _set(self, bYesNo):
##        u'Indicates if overlays are visible or not.'
##    ShowOverlays = property(_get, _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Set the draw call back.'
##    OverlaysCallback = property(fset = _set, doc = _set.__doc__)
##

class EnvelopeTracker(CoClass):
    u'Display feedback for tracking envelope resizing.'
    _reg_clsid_ = GUID('{E6BDB107-4D35-11D0-98BE-00805F7CED21}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
EnvelopeTracker._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ISelectionTracker]

class GraphicAttributeAngleType(CoClass):
    u'Angle graphic attribute type.'
    _reg_clsid_ = GUID('{FE507891-534B-45F8-A2FF-3FE798EBE3D6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
GraphicAttributeAngleType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGraphicAttributeType]

class ILineCallout(ICallout):
    _case_insensitive_ = True
    u'Provides access to members that control the line callout.'
    _iid_ = GUID('{C8D09ED1-4FBB-11D1-9A72-0080C7EC5C96}')
    _idlflags_ = ['oleautomation']
ICallout._methods_ = [
    COMMETHOD(['propget', helpstring(u'The anchor point.')], HRESULT, 'AnchorPoint',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint)), 'Point' )),
    COMMETHOD(['propput', helpstring(u'The anchor point.')], HRESULT, 'AnchorPoint',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
    COMMETHOD(['propget', helpstring(u'The closest distance to the text the anchor point can be for the callout to draw.')], HRESULT, 'LeaderTolerance',
              ( ['retval', 'out'], POINTER(c_double), 'LeaderTolerance' )),
    COMMETHOD(['propput', helpstring(u'The closest distance to the text the anchor point can be for the callout to draw.')], HRESULT, 'LeaderTolerance',
              ( ['in'], c_double, 'LeaderTolerance' )),
]
################################################################
## code template for ICallout implementation
##class ICallout_Impl(object):
##    def _get(self):
##        u'The closest distance to the text the anchor point can be for the callout to draw.'
##        #return LeaderTolerance
##    def _set(self, LeaderTolerance):
##        u'The closest distance to the text the anchor point can be for the callout to draw.'
##    LeaderTolerance = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The anchor point.'
##        #return Point
##    def _set(self, Point):
##        u'The anchor point.'
##    AnchorPoint = property(_get, _set, doc = _set.__doc__)
##

class IFillSymbol(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control fill symbols.'
    _iid_ = GUID('{E6BDAA7E-4D35-11D0-98BE-00805F7CED21}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriLineCalloutStyle'
esriLCSBase = 0
esriLCSMidpoint = 1
esriLCSThreePoint = 2
esriLCSFourPoint = 3
esriLCSUnderline = 4
esriLCSCustom = 5
esriLCSCircularCW = 6
esriLCSCircularCCW = 7
esriLineCalloutStyle = c_int # enum
ILineCallout._methods_ = [
    COMMETHOD(['propget', helpstring(u'The fill symbol used to render the border.')], HRESULT, 'Border',
              ( ['retval', 'out'], POINTER(POINTER(IFillSymbol)), 'Border' )),
    COMMETHOD(['propputref', helpstring(u'The fill symbol used to render the border.')], HRESULT, 'Border',
              ( ['in'], POINTER(IFillSymbol), 'Border' )),
    COMMETHOD(['propget', helpstring(u'The gap.')], HRESULT, 'Gap',
              ( ['retval', 'out'], POINTER(c_double), 'Gap' )),
    COMMETHOD(['propput', helpstring(u'The gap.')], HRESULT, 'Gap',
              ( ['in'], c_double, 'Gap' )),
    COMMETHOD(['propget', helpstring(u'The line symbol used to render the accent bar.')], HRESULT, 'AccentBar',
              ( ['retval', 'out'], POINTER(POINTER(ILineSymbol)), 'AccentBar' )),
    COMMETHOD(['propputref', helpstring(u'The line symbol used to render the accent bar.')], HRESULT, 'AccentBar',
              ( ['in'], POINTER(ILineSymbol), 'AccentBar' )),
    COMMETHOD(['propget', helpstring(u'The line callout style.')], HRESULT, 'Style',
              ( ['retval', 'out'], POINTER(esriLineCalloutStyle), 'Style' )),
    COMMETHOD(['propput', helpstring(u'The line callout style.')], HRESULT, 'Style',
              ( ['in'], esriLineCalloutStyle, 'Style' )),
    COMMETHOD(['propget', helpstring(u'The line symbol used to render the leader line.')], HRESULT, 'LeaderLine',
              ( ['retval', 'out'], POINTER(POINTER(ILineSymbol)), 'LeaderLine' )),
    COMMETHOD(['propputref', helpstring(u'The line symbol used to render the leader line.')], HRESULT, 'LeaderLine',
              ( ['in'], POINTER(ILineSymbol), 'LeaderLine' )),
]
################################################################
## code template for ILineCallout implementation
##class ILineCallout_Impl(object):
##    def AccentBar(self, AccentBar):
##        u'The line symbol used to render the accent bar.'
##        #return 
##
##    def _get(self):
##        u'The line callout style.'
##        #return Style
##    def _set(self, Style):
##        u'The line callout style.'
##    Style = property(_get, _set, doc = _set.__doc__)
##
##    def LeaderLine(self, LeaderLine):
##        u'The line symbol used to render the leader line.'
##        #return 
##
##    def Border(self, Border):
##        u'The fill symbol used to render the border.'
##        #return 
##
##    def _get(self):
##        u'The gap.'
##        #return Gap
##    def _set(self, Gap):
##        u'The gap.'
##    Gap = property(_get, _set, doc = _set.__doc__)
##

class IReferenceLineSymbol(ILineSymbol):
    _case_insensitive_ = True
    u'Provides access to members that control the reference line symbol.'
    _iid_ = GUID('{7914E5DC-C892-11D0-8BB6-080009EE4E41}')
    _idlflags_ = ['oleautomation']
IReferenceLineSymbol._methods_ = [
    COMMETHOD(['propget', helpstring(u'Reference line symbol set name.')], HRESULT, 'SymbolSetName',
              ( ['retval', 'out'], POINTER(BSTR), 'SymbolSetName' )),
    COMMETHOD(['propput', helpstring(u'Reference line symbol set name.')], HRESULT, 'SymbolSetName',
              ( ['in'], BSTR, 'SymbolSetName' )),
    COMMETHOD(['propget', helpstring(u'Reference line symbol name.')], HRESULT, 'SymbolName',
              ( ['retval', 'out'], POINTER(BSTR), 'SymbolName' )),
    COMMETHOD(['propput', helpstring(u'Reference line symbol name.')], HRESULT, 'SymbolName',
              ( ['in'], BSTR, 'SymbolName' )),
]
################################################################
## code template for IReferenceLineSymbol implementation
##class IReferenceLineSymbol_Impl(object):
##    def _get(self):
##        u'Reference line symbol set name.'
##        #return SymbolSetName
##    def _set(self, SymbolSetName):
##        u'Reference line symbol set name.'
##    SymbolSetName = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Reference line symbol name.'
##        #return SymbolName
##    def _set(self, SymbolName):
##        u'Reference line symbol name.'
##    SymbolName = property(_get, _set, doc = _set.__doc__)
##

class IDisplayTransformationScales(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control Display Transformation scales.'
    _iid_ = GUID('{A709B584-9FB9-4954-8096-02068C16A677}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriScaleSnapping'
esriStandardScaleSnapping = 0
esriUserScaleSnapping = 1
esriScaleSnapping = c_int # enum
IDisplayTransformationScales._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if transform snaps the fitted bounds to a standard scale.')], HRESULT, 'ScaleSnapping',
              ( ['retval', 'out'], POINTER(esriScaleSnapping), 'setting' )),
    COMMETHOD(['propput', helpstring(u'Indicates if transform snaps the fitted bounds to a standard scale.')], HRESULT, 'ScaleSnapping',
              ( ['in'], esriScaleSnapping, 'setting' )),
    COMMETHOD(['propget', helpstring(u'Get the number of user scales.')], HRESULT, 'UserScaleCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD([helpstring(u'Get the user scales.')], HRESULT, 'GetUserScale',
              ( ['in'], c_int, 'idx' ),
              ( ['retval', 'out'], POINTER(c_double), 'scale' )),
    COMMETHOD([helpstring(u'Add a new user scale.')], HRESULT, 'AddUserScale',
              ( ['in'], c_double, 'scale' )),
    COMMETHOD([helpstring(u'Remove a user scale.')], HRESULT, 'RemoveUserScale',
              ( ['in'], c_double, 'scale' )),
    COMMETHOD([helpstring(u'Remove all the user scales.')], HRESULT, 'RemoveAllUserScales'),
    COMMETHOD([helpstring(u'Initialize user scales to defaults.')], HRESULT, 'LoadDefaultUserScales'),
    COMMETHOD([helpstring(u'Set the current set of user scales to be the defaults.')], HRESULT, 'SaveDefaultUserScales'),
    COMMETHOD([helpstring(u'Calculate the scale of the specified extent.')], HRESULT, 'CalculateScale',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'extent' ),
              ( ['retval', 'out'], POINTER(c_double), 'scale' )),
    COMMETHOD([helpstring(u'Zoom to the specified scale.  Center on extent.')], HRESULT, 'ZoomTo',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'extent' ),
              ( ['in'], c_double, 'scale' )),
    COMMETHOD([helpstring(u'Snap the specified scale to a standard scale.')], HRESULT, 'SnapScale',
              ( ['in'], c_double, 'scale' ),
              ( ['retval', 'out'], POINTER(c_double), 'snappedScale' )),
    COMMETHOD([helpstring(u'Find the nearest standard scale with a value that is higher than the specified scale.')], HRESULT, 'NextScale',
              ( ['in'], c_double, 'scale' ),
              ( ['retval', 'out'], POINTER(c_double), 'NextScale' )),
    COMMETHOD([helpstring(u'Find the nearest standard scale with a value that is lower than the specified scale.')], HRESULT, 'PreviousScale',
              ( ['in'], c_double, 'scale' ),
              ( ['retval', 'out'], POINTER(c_double), 'PreviousScale' )),
]
################################################################
## code template for IDisplayTransformationScales implementation
##class IDisplayTransformationScales_Impl(object):
##    @property
##    def UserScaleCount(self):
##        u'Get the number of user scales.'
##        #return Count
##
##    def SnapScale(self, scale):
##        u'Snap the specified scale to a standard scale.'
##        #return snappedScale
##
##    def ZoomTo(self, extent, scale):
##        u'Zoom to the specified scale.  Center on extent.'
##        #return 
##
##    def _get(self):
##        u'Indicates if transform snaps the fitted bounds to a standard scale.'
##        #return setting
##    def _set(self, setting):
##        u'Indicates if transform snaps the fitted bounds to a standard scale.'
##    ScaleSnapping = property(_get, _set, doc = _set.__doc__)
##
##    def AddUserScale(self, scale):
##        u'Add a new user scale.'
##        #return 
##
##    def SaveDefaultUserScales(self):
##        u'Set the current set of user scales to be the defaults.'
##        #return 
##
##    def RemoveUserScale(self, scale):
##        u'Remove a user scale.'
##        #return 
##
##    def CalculateScale(self, extent):
##        u'Calculate the scale of the specified extent.'
##        #return scale
##
##    def NextScale(self, scale):
##        u'Find the nearest standard scale with a value that is higher than the specified scale.'
##        #return NextScale
##
##    def PreviousScale(self, scale):
##        u'Find the nearest standard scale with a value that is lower than the specified scale.'
##        #return PreviousScale
##
##    def GetUserScale(self, idx):
##        u'Get the user scales.'
##        #return scale
##
##    def LoadDefaultUserScales(self):
##        u'Initialize user scales to defaults.'
##        #return 
##
##    def RemoveAllUserScales(self):
##        u'Remove all the user scales.'
##        #return 
##

IGeometricEffect._methods_ = [
    COMMETHOD(['propget', helpstring(u'The output type of the geometric effect.')], HRESULT, 'OutputType',
              ( ['in'], comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.esriGeometryType, 'inputType' ),
              ( ['retval', 'out'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.esriGeometryType), 'OutputType' )),
    COMMETHOD([helpstring(u'Resets the collection of generated geometries. Must be called before using NextGeometry.')], HRESULT, 'Reset',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'Geometry' )),
    COMMETHOD([helpstring(u'Accesses the next geometry generated by th effect.')], HRESULT, 'NextGeometry',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry)), 'Geometry' )),
]
################################################################
## code template for IGeometricEffect implementation
##class IGeometricEffect_Impl(object):
##    def Reset(self, Geometry):
##        u'Resets the collection of generated geometries. Must be called before using NextGeometry.'
##        #return 
##
##    def NextGeometry(self):
##        u'Accesses the next geometry generated by th effect.'
##        #return Geometry
##
##    @property
##    def OutputType(self, inputType):
##        u'The output type of the geometric effect.'
##        #return OutputType
##

class IOutputRasterSettings(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control New Raster Output Settings.'
    _iid_ = GUID('{28444834-E9CB-44F8-806A-D313373F69B8}')
    _idlflags_ = ['oleautomation']
IOutputRasterSettings._methods_ = [
    COMMETHOD(['propget', helpstring(u'This coefficient states the scale level for the raster when it goes to output. 1 means 1:1; 2 means 1:2, i.e. 2 times less than the output quality.')], HRESULT, 'ResampleRatio',
              ( ['retval', 'out'], POINTER(c_int), 'pRatio' )),
    COMMETHOD(['propput', helpstring(u'This coefficient states the scale level for the raster when it goes to output. 1 means 1:1; 2 means 1:2, i.e. 2 times less than the output quality.')], HRESULT, 'ResampleRatio',
              ( ['in'], c_int, 'pRatio' )),
]
################################################################
## code template for IOutputRasterSettings implementation
##class IOutputRasterSettings_Impl(object):
##    def _get(self):
##        u'This coefficient states the scale level for the raster when it goes to output. 1 means 1:1; 2 means 1:2, i.e. 2 times less than the output quality.'
##        #return pRatio
##    def _set(self, pRatio):
##        u'This coefficient states the scale level for the raster when it goes to output. 1 means 1:1; 2 means 1:2, i.e. 2 times less than the output quality.'
##    ResampleRatio = property(_get, _set, doc = _set.__doc__)
##

class IStyleGalleryItem(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that define items in the Style Gallery.'
    _iid_ = GUID('{AC0E9825-91CB-11D1-8813-080009EC732A}')
    _idlflags_ = ['oleautomation']
class IStyleGalleryItem2(IStyleGalleryItem):
    _case_insensitive_ = True
    u'Provides access to members that describe items in the Style Gallery.'
    _iid_ = GUID('{6BF1D82D-FE60-4639-A7F6-39C9A223CDB0}')
    _idlflags_ = ['oleautomation']
class IStyleGalleryItem3(IStyleGalleryItem2):
    _case_insensitive_ = True
    u'Provides access to members that describe items in the Style Gallery.'
    _iid_ = GUID('{4E197168-1BEB-49E1-B208-A7A3BB261FA5}')
    _idlflags_ = ['oleautomation']
IStyleGalleryItem._methods_ = [
    COMMETHOD(['propget', helpstring(u'Id for the item in the Style Gallery.')], HRESULT, 'ID',
              ( ['retval', 'out'], POINTER(c_int), 'ID' )),
    COMMETHOD(['propget', helpstring(u'The symbol or map element to be stored in the Style Gallery item.')], HRESULT, 'Item',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'Item' )),
    COMMETHOD(['propput', helpstring(u'The symbol or map element to be stored in the Style Gallery item.')], HRESULT, 'Item',
              ( ['in'], POINTER(IUnknown), 'Item' )),
    COMMETHOD(['propget', helpstring(u'The name of the item in the Style Gallery.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propput', helpstring(u'The name of the item in the Style Gallery.')], HRESULT, 'Name',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD(['propget', helpstring(u'The category of the item.')], HRESULT, 'Category',
              ( ['retval', 'out'], POINTER(BSTR), 'Category' )),
    COMMETHOD(['propput', helpstring(u'The category of the item.')], HRESULT, 'Category',
              ( ['in'], BSTR, 'Category' )),
]
################################################################
## code template for IStyleGalleryItem implementation
##class IStyleGalleryItem_Impl(object):
##    def _get(self):
##        u'The category of the item.'
##        #return Category
##    def _set(self, Category):
##        u'The category of the item.'
##    Category = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The symbol or map element to be stored in the Style Gallery item.'
##        #return Item
##    def _set(self, Item):
##        u'The symbol or map element to be stored in the Style Gallery item.'
##    Item = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def ID(self):
##        u'Id for the item in the Style Gallery.'
##        #return ID
##
##    def _get(self):
##        u'The name of the item in the Style Gallery.'
##        #return Name
##    def _set(self, Name):
##        u'The name of the item in the Style Gallery.'
##    Name = property(_get, _set, doc = _set.__doc__)
##

IStyleGalleryItem2._methods_ = [
    COMMETHOD(['propget', helpstring(u'The tags of the item.')], HRESULT, 'Tags',
              ( ['retval', 'out'], POINTER(BSTR), 'Tags' )),
    COMMETHOD(['propput', helpstring(u'The tags of the item.')], HRESULT, 'Tags',
              ( ['in'], BSTR, 'Tags' )),
]
################################################################
## code template for IStyleGalleryItem2 implementation
##class IStyleGalleryItem2_Impl(object):
##    def _get(self):
##        u'The tags of the item.'
##        #return Tags
##    def _set(self, Tags):
##        u'The tags of the item.'
##    Tags = property(_get, _set, doc = _set.__doc__)
##

IStyleGalleryItem3._methods_ = [
    COMMETHOD(['propget', helpstring(u'The default tags of the item.')], HRESULT, 'DefaultTags',
              ( ['retval', 'out'], POINTER(BSTR), 'Tags' )),
]
################################################################
## code template for IStyleGalleryItem3 implementation
##class IStyleGalleryItem3_Impl(object):
##    @property
##    def DefaultTags(self):
##        u'The default tags of the item.'
##        #return Tags
##


# values for enumeration 'esriArrowMarkerStyle'
esriAMSPlain = 0
esriArrowMarkerStyle = c_int # enum

# values for enumeration 'esriLineCapStyle'
esriLCSButt = 0
esriLCSRound = 1
esriLCSSquare = 2
esriLineCapStyle = c_int # enum
class GradientFillSymbol(CoClass):
    u'A fill symbol composed from a ramp of colors.'
    _reg_clsid_ = GUID('{7914E609-C892-11D0-8BB6-080009EE4E41}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IGradientFillSymbol(IFillSymbol):
    _case_insensitive_ = True
    u'Provides access to members that control the gradient fill symbol.'
    _iid_ = GUID('{7914E5F2-C892-11D0-8BB6-080009EE4E41}')
    _idlflags_ = ['oleautomation']
GradientFillSymbol._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGradientFillSymbol, IMapLevel, ISymbol, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySupport, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, IDisplayName]

class IRotateTracker(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the rotation tracker.'
    _iid_ = GUID('{66770313-FBC0-11D1-A24E-080009B6F22B}')
    _idlflags_ = ['oleautomation']
IRotateTracker._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The display used by the tracker.')], HRESULT, 'Display',
              ( ['in'], POINTER(IScreenDisplay), 'rhs' )),
    COMMETHOD(['propget', helpstring(u"If the mouse is over the tracker, return an HCURSOR to indicate legal operations based on mouse's relation to selection handles: move resize, etc.  Return 0 if mouse isn't over tracker.")], HRESULT, 'Cursor',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'Cursor' )),
    COMMETHOD([helpstring(u'Invalidate the portion of the screen covered by the tracker.')], HRESULT, 'Refresh'),
    COMMETHOD([helpstring(u'Begin tracking move or resize based on the location of the mouse over the tracker handles.')], HRESULT, 'OnMouseDown'),
    COMMETHOD([helpstring(u'In process move or resize tracking.')], HRESULT, 'OnMouseMove',
              ( [], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'mapPoint' )),
    COMMETHOD([helpstring(u'Finish move or resize tracking.')], HRESULT, 'OnMouseUp',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'angleChanged' )),
    COMMETHOD([helpstring(u'Special keypress processing while tracking.')], HRESULT, 'OnKeyDown',
              ( ['in'], c_int, 'keyCode' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'angleChanged' )),
    COMMETHOD([helpstring(u'Cancel tracking.')], HRESULT, 'Deactivate',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'complete' )),
    COMMETHOD(['propput', helpstring(u'The rotation origin.')], HRESULT, 'Origin',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Anchor' )),
    COMMETHOD(['propget', helpstring(u'The rotation origin.')], HRESULT, 'Origin',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint)), 'Anchor' )),
    COMMETHOD([helpstring(u'Adds a geometry to be rotated.')], HRESULT, 'AddGeometry',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'Geometry' )),
    COMMETHOD([helpstring(u'Adds a point and symbol to be rotated.')], HRESULT, 'AddPoint',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'Geometry' ),
              ( ['in'], POINTER(IMarkerSymbol), 'sym' )),
    COMMETHOD([helpstring(u'Clears all the geometries.')], HRESULT, 'ClearGeometry'),
    COMMETHOD(['propget', helpstring(u'The angle.')], HRESULT, 'Angle',
              ( ['retval', 'out'], POINTER(c_double), 'Angle' )),
]
################################################################
## code template for IRotateTracker implementation
##class IRotateTracker_Impl(object):
##    def _get(self):
##        u'The rotation origin.'
##        #return Anchor
##    def _set(self, Anchor):
##        u'The rotation origin.'
##    Origin = property(_get, _set, doc = _set.__doc__)
##
##    def AddPoint(self, Geometry, sym):
##        u'Adds a point and symbol to be rotated.'
##        #return 
##
##    @property
##    def Angle(self):
##        u'The angle.'
##        #return Angle
##
##    def Deactivate(self):
##        u'Cancel tracking.'
##        #return complete
##
##    def OnKeyDown(self, keyCode):
##        u'Special keypress processing while tracking.'
##        #return angleChanged
##
##    def Refresh(self):
##        u'Invalidate the portion of the screen covered by the tracker.'
##        #return 
##
##    def OnMouseDown(self):
##        u'Begin tracking move or resize based on the location of the mouse over the tracker handles.'
##        #return 
##
##    @property
##    def Cursor(self):
##        u"If the mouse is over the tracker, return an HCURSOR to indicate legal operations based on mouse's relation to selection handles: move resize, etc.  Return 0 if mouse isn't over tracker."
##        #return Cursor
##
##    def AddGeometry(self, Geometry):
##        u'Adds a geometry to be rotated.'
##        #return 
##
##    def OnMouseMove(self, mapPoint):
##        u'In process move or resize tracking.'
##        #return 
##
##    def OnMouseUp(self):
##        u'Finish move or resize tracking.'
##        #return angleChanged
##
##    def Display(self, rhs):
##        u'The display used by the tracker.'
##        #return 
##
##    def ClearGeometry(self):
##        u'Clears all the geometries.'
##        #return 
##

class IStyleGallery(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members modify the Style Gallery.'
    _iid_ = GUID('{AC0E9826-91CB-11D1-8813-080009EC732A}')
    _idlflags_ = ['oleautomation']
class IEnumStyleGalleryItem(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that enumerate over a set of Style Gallery items.'
    _iid_ = GUID('{AC0E9828-91CB-11D1-8813-080009EC732A}')
    _idlflags_ = ['oleautomation']
IStyleGallery._methods_ = [
    COMMETHOD(['propget', helpstring(u'Number of classes in the Style Gallery.')], HRESULT, 'ClassCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'The class at the given index.')], HRESULT, 'Class',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IStyleGalleryClass)), 'styleClass' )),
    COMMETHOD(['propget', helpstring(u'The categories within the given class.')], HRESULT, 'Categories',
              ( ['in'], BSTR, 'ClassName' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IEnumBSTR)), 'Categories' )),
    COMMETHOD(['propget', helpstring(u'The style items from the specified style file, in the specified class and category. The style set and category may be blank to return all items.')], HRESULT, 'Items',
              ( ['in'], BSTR, 'ClassName' ),
              ( ['in'], BSTR, 'styleSet' ),
              ( ['in'], BSTR, 'Category' ),
              ( ['retval', 'out'], POINTER(POINTER(IEnumStyleGalleryItem)), 'Items' )),
    COMMETHOD([helpstring(u'Adds an item to the target style file.')], HRESULT, 'AddItem',
              ( ['in'], POINTER(IStyleGalleryItem), 'Item' )),
    COMMETHOD([helpstring(u'Updates an existing item in target style file.')], HRESULT, 'UpdateItem',
              ( ['in'], POINTER(IStyleGalleryItem), 'Item' )),
    COMMETHOD([helpstring(u'Removes an item from the target style file.')], HRESULT, 'RemoveItem',
              ( ['in'], POINTER(IStyleGalleryItem), 'Item' )),
    COMMETHOD([helpstring(u'Removes all styles from the Style Gallery.')], HRESULT, 'Clear'),
    COMMETHOD([helpstring(u'Loads a style from a file. If class is specified, only items in that class will be loaded.')], HRESULT, 'LoadStyle',
              ( ['in'], BSTR, 'fileName' ),
              ( ['in'], BSTR, 'ClassName' )),
    COMMETHOD([helpstring(u'Saves the specified style to a file. If class is specified, only items in that class will be saved.')], HRESULT, 'SaveStyle',
              ( ['in'], BSTR, 'fileName' ),
              ( ['in'], BSTR, 'styleSet' ),
              ( ['in'], BSTR, 'ClassName' )),
    COMMETHOD([helpstring(u'Imports a style from a file other than a .style file.')], HRESULT, 'ImportStyle',
              ( ['in'], BSTR, 'fileName' )),
]
################################################################
## code template for IStyleGallery implementation
##class IStyleGallery_Impl(object):
##    def ImportStyle(self, fileName):
##        u'Imports a style from a file other than a .style file.'
##        #return 
##
##    def SaveStyle(self, fileName, styleSet, ClassName):
##        u'Saves the specified style to a file. If class is specified, only items in that class will be saved.'
##        #return 
##
##    def UpdateItem(self, Item):
##        u'Updates an existing item in target style file.'
##        #return 
##
##    @property
##    def ClassCount(self):
##        u'Number of classes in the Style Gallery.'
##        #return Count
##
##    @property
##    def Items(self, ClassName, styleSet, Category):
##        u'The style items from the specified style file, in the specified class and category. The style set and category may be blank to return all items.'
##        #return Items
##
##    def Clear(self):
##        u'Removes all styles from the Style Gallery.'
##        #return 
##
##    def AddItem(self, Item):
##        u'Adds an item to the target style file.'
##        #return 
##
##    def LoadStyle(self, fileName, ClassName):
##        u'Loads a style from a file. If class is specified, only items in that class will be loaded.'
##        #return 
##
##    def RemoveItem(self, Item):
##        u'Removes an item from the target style file.'
##        #return 
##
##    @property
##    def Class(self, index):
##        u'The class at the given index.'
##        #return styleClass
##
##    @property
##    def Categories(self, ClassName):
##        u'The categories within the given class.'
##        #return Categories
##

class IEnumColors(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that enumerate through Color objects.'
    _iid_ = GUID('{BEB87092-C0B4-11D0-8379-080009B996CC}')
    _idlflags_ = ['oleautomation']
IColorRamp._methods_ = [
    COMMETHOD(['propput', helpstring(u'The name of the color ramp.')], HRESULT, 'Name',
              ( ['in'], BSTR, 'pName' )),
    COMMETHOD(['propget', helpstring(u'The name of the color ramp.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pName' )),
    COMMETHOD(['propput', helpstring(u'The number of colors that will be generated by the CreateRamp method.')], HRESULT, 'Size',
              ( ['in'], c_int, 'Count' )),
    COMMETHOD(['propget', helpstring(u'The number of colors that will be generated by the CreateRamp method.')], HRESULT, 'Size',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'The list of colors.  Call CreateRamp before calling this method.')], HRESULT, 'Colors',
              ( ['retval', 'out'], POINTER(POINTER(IEnumColors)), 'enumColors' )),
    COMMETHOD(['propget', helpstring(u'The color at the given index position.  Call CreateRamp before calling this method.')], HRESULT, 'Color',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IColor)), 'Color' )),
    COMMETHOD([helpstring(u'Generates a color ramp with length determined by Size value.')], HRESULT, 'CreateRamp',
              ( ['out'], POINTER(VARIANT_BOOL), 'ok' )),
]
################################################################
## code template for IColorRamp implementation
##class IColorRamp_Impl(object):
##    @property
##    def Color(self, index):
##        u'The color at the given index position.  Call CreateRamp before calling this method.'
##        #return Color
##
##    @property
##    def Colors(self):
##        u'The list of colors.  Call CreateRamp before calling this method.'
##        #return enumColors
##
##    def _get(self):
##        u'The name of the color ramp.'
##        #return pName
##    def _set(self, pName):
##        u'The name of the color ramp.'
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    def CreateRamp(self):
##        u'Generates a color ramp with length determined by Size value.'
##        #return ok
##
##    def _get(self):
##        u'The number of colors that will be generated by the CreateRamp method.'
##        #return Count
##    def _set(self, Count):
##        u'The number of colors that will be generated by the CreateRamp method.'
##    Size = property(_get, _set, doc = _set.__doc__)
##


# values for enumeration 'esriSimpleMarkerStyle'
esriSMSCircle = 0
esriSMSSquare = 1
esriSMSCross = 2
esriSMSX = 3
esriSMSDiamond = 4
esriSimpleMarkerStyle = c_int # enum
class ICmykColor(IColor):
    _case_insensitive_ = True
    u'Provides access to members that control the CMYK color values.'
    _iid_ = GUID('{20CD40B2-8F3D-11D0-8590-0800091A2A72}')
    _idlflags_ = ['oleautomation']
ICmykColor._methods_ = [
    COMMETHOD(['propput', helpstring(u'The cyan component of an ICmykColor (0-255).')], HRESULT, 'Cyan',
              ( ['in'], c_int, 'Cyan' )),
    COMMETHOD(['propget', helpstring(u'The cyan component of an ICmykColor (0-255).')], HRESULT, 'Cyan',
              ( ['retval', 'out'], POINTER(c_int), 'Cyan' )),
    COMMETHOD(['propput', helpstring(u'The magenta component of an ICmykColor (0-255).')], HRESULT, 'Magenta',
              ( ['in'], c_int, 'Magenta' )),
    COMMETHOD(['propget', helpstring(u'The magenta component of an ICmykColor (0-255).')], HRESULT, 'Magenta',
              ( ['retval', 'out'], POINTER(c_int), 'Magenta' )),
    COMMETHOD(['propput', helpstring(u'The yellow component of an ICmykColor (0-255).')], HRESULT, 'Yellow',
              ( ['in'], c_int, 'Yellow' )),
    COMMETHOD(['propget', helpstring(u'The yellow component of an ICmykColor (0-255).')], HRESULT, 'Yellow',
              ( ['retval', 'out'], POINTER(c_int), 'Yellow' )),
    COMMETHOD(['propput', helpstring(u'The black component of an ICmykColor (0-255).')], HRESULT, 'Black',
              ( ['in'], c_int, 'Black' )),
    COMMETHOD(['propget', helpstring(u'The black component of an ICmykColor (0-255).')], HRESULT, 'Black',
              ( ['retval', 'out'], POINTER(c_int), 'Black' )),
]
################################################################
## code template for ICmykColor implementation
##class ICmykColor_Impl(object):
##    def _get(self):
##        u'The cyan component of an ICmykColor (0-255).'
##        #return Cyan
##    def _set(self, Cyan):
##        u'The cyan component of an ICmykColor (0-255).'
##    Cyan = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The magenta component of an ICmykColor (0-255).'
##        #return Magenta
##    def _set(self, Magenta):
##        u'The magenta component of an ICmykColor (0-255).'
##    Magenta = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The black component of an ICmykColor (0-255).'
##        #return Black
##    def _set(self, Black):
##        u'The black component of an ICmykColor (0-255).'
##    Black = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The yellow component of an ICmykColor (0-255).'
##        #return Yellow
##    def _set(self, Yellow):
##        u'The yellow component of an ICmykColor (0-255).'
##    Yellow = property(_get, _set, doc = _set.__doc__)
##

IEnumStyleGalleryItem._methods_ = [
    COMMETHOD([helpstring(u'Gets the next Style Gallery item.')], HRESULT, 'Next',
              ( ['retval', 'out'], POINTER(POINTER(IStyleGalleryItem)), 'Item' )),
    COMMETHOD([helpstring(u'Resets the enumerator.')], HRESULT, 'Reset'),
]
################################################################
## code template for IEnumStyleGalleryItem implementation
##class IEnumStyleGalleryItem_Impl(object):
##    def Reset(self):
##        u'Resets the enumerator.'
##        #return 
##
##    def Next(self):
##        u'Gets the next Style Gallery item.'
##        #return Item
##

class LineDecoration(CoClass):
    u'Places a marker (decoration) at a specific location along a line symbol.'
    _reg_clsid_ = GUID('{533D88F5-0A1A-11D2-B27F-0000F878229E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class ILineDecoration(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the line decoration.'
    _iid_ = GUID('{533D88F0-0A1A-11D2-B27F-0000F878229E}')
    _idlflags_ = ['oleautomation']
LineDecoration._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ILineDecoration, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone]

class SimpleLineDecorationElement(CoClass):
    u'Simple Line Decoration Element.'
    _reg_clsid_ = GUID('{533D88F3-0A1A-11D2-B27F-0000F878229E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class ILineDecorationElement(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the line decoration element.'
    _iid_ = GUID('{533D88F2-0A1A-11D2-B27F-0000F878229E}')
    _idlflags_ = ['oleautomation']
class ISimpleLineDecorationElement(ILineDecorationElement):
    _case_insensitive_ = True
    u'Provides access to members that control the simple line decoration.'
    _iid_ = GUID('{533D88F7-0A1A-11D2-B27F-0000F878229E}')
    _idlflags_ = ['oleautomation']
SimpleLineDecorationElement._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ISimpleLineDecorationElement, ILineDecorationElement, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, IDisplayName]

class IMapContext(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the context in which geometric effects and marker placements work.'
    _iid_ = GUID('{A7BE1534-8847-4A3B-BA08-4D4A94405427}')
    _idlflags_ = ['oleautomation']
IMapContext._methods_ = [
    COMMETHOD([helpstring(u'Initializes the map context using a display transformation.')], HRESULT, 'InitFromDisplay',
              ( ['in'], POINTER(IDisplayTransformation), 'displayTransform' )),
    COMMETHOD([helpstring(u'Initializes the map context.')], HRESULT, 'Init',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference), 'mapProj' ),
              ( ['in'], c_double, 'mapRefScale' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'mapExtent' )),
    COMMETHOD([helpstring(u'Converts geographic geometry to map context geometry.')], HRESULT, 'FromGeographyToMap',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'ingeom' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry)), 'outgeom' )),
    COMMETHOD([helpstring(u'Converts map context geometry to geographic geometry.')], HRESULT, 'FromMapToGeography',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'ingeom' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry)), 'outgeom' )),
    COMMETHOD(['propget', helpstring(u'The reference scale of the map.')], HRESULT, 'ReferenceScale',
              ( ['retval', 'out'], POINTER(c_double), 'refScale' )),
    COMMETHOD(['propget', helpstring(u'The spatial reference of the map.')], HRESULT, 'SpatialReference',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference)), 'spatialRef' )),
    COMMETHOD([helpstring(u'Converts a distance expressed in points into a geographic distance.')], HRESULT, 'FromPoints',
              ( ['in'], c_double, 'ptDist' ),
              ( ['retval', 'out'], POINTER(c_double), 'mapDist' )),
    COMMETHOD([helpstring(u'Converts a geographic distance into a distance expressed in points.')], HRESULT, 'ToPoints',
              ( ['in'], c_double, 'mapDist' ),
              ( ['retval', 'out'], POINTER(c_double), 'ptDist' )),
]
################################################################
## code template for IMapContext implementation
##class IMapContext_Impl(object):
##    def InitFromDisplay(self, displayTransform):
##        u'Initializes the map context using a display transformation.'
##        #return 
##
##    def ToPoints(self, mapDist):
##        u'Converts a geographic distance into a distance expressed in points.'
##        #return ptDist
##
##    @property
##    def SpatialReference(self):
##        u'The spatial reference of the map.'
##        #return spatialRef
##
##    def Init(self, mapProj, mapRefScale, mapExtent):
##        u'Initializes the map context.'
##        #return 
##
##    def FromMapToGeography(self, ingeom):
##        u'Converts map context geometry to geographic geometry.'
##        #return outgeom
##
##    def FromPoints(self, ptDist):
##        u'Converts a distance expressed in points into a geographic distance.'
##        #return mapDist
##
##    @property
##    def ReferenceScale(self):
##        u'The reference scale of the map.'
##        #return refScale
##
##    def FromGeographyToMap(self, ingeom):
##        u'Converts geographic geometry to map context geometry.'
##        #return outgeom
##


# values for enumeration 'esriTextPosition'
esriTPNormal = 0
esriTPSuperscript = 1
esriTPSubscript = 2
esriTextPosition = c_int # enum

# values for enumeration 'esriGradientFillStyle'
esriGFSLinear = 0
esriGFSRectangular = 1
esriGFSCircular = 2
esriGFSBuffered = 3
esriGradientFillStyle = c_int # enum

# values for enumeration 'esriLineJoinStyle'
esriLJSMitre = 0
esriLJSRound = 1
esriLJSBevel = 2
esriLineJoinStyle = c_int # enum
class BasicMarkerSymbol(CoClass):
    u'Basic marker symbol object.'
    _reg_clsid_ = GUID('{1BFF73A0-D134-4E88-8BC5-788BD351B12D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IBasicMarkerSymbol(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to properties of the basic marker symbol.'
    _iid_ = GUID('{5BBC04AC-9EE4-4947-A56E-C798A75DA20B}')
    _idlflags_ = ['oleautomation']
BasicMarkerSymbol._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IBasicSymbol, IBasicMarkerSymbol, IMapLevel, IGeometricEffects, IGeometricEffect, IGraphicAttributes, IGraphicAttributes2, IDrawingOutline, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLVersionSupport]


# values for enumeration 'esriMarkerFillStyle'
esriMFSGrid = 0
esriMFSRandom = 1
esriMarkerFillStyle = c_int # enum
class MarkerTextBackground(CoClass):
    u'A marker that is placed behind text.'
    _reg_clsid_ = GUID('{C5C02D50-7282-11D2-9816-0080C7E04196}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IMarkerTextBackground(ITextBackground):
    _case_insensitive_ = True
    u'Provides access to members that control the marker text background.'
    _iid_ = GUID('{A8577A00-7283-11D2-9816-0080C7E04196}')
    _idlflags_ = ['oleautomation']
class ITextBackground2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the text background.'
    _iid_ = GUID('{63FC25A7-438B-4F97-888E-105E6D461828}')
    _idlflags_ = ['oleautomation']
MarkerTextBackground._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMarkerTextBackground, ITextBackground, ITextBackground2, IQueryGeometry, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, IDisplayName, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize]

class BezierTextPath(CoClass):
    u'Helper object used to align a text string to a curve.'
    _reg_clsid_ = GUID('{2DE21000-BDEB-11D1-970B-0080C7E04196}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class ITextPath(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the text path.'
    _iid_ = GUID('{B65A3E75-2993-11D1-9A43-0080C7EC5C96}')
    _idlflags_ = ['oleautomation']
BezierTextPath._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ITextPath, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist]

class SimpleTextPath(CoClass):
    u'Helper object used to align a text string to a geometry.'
    _reg_clsid_ = GUID('{B65A3E76-2993-11D1-9A43-0080C7EC5C96}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class ITextPath2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to additional members that control the text path.'
    _iid_ = GUID('{6EA0E1E0-13E5-46D0-82AD-69F8993A67E3}')
    _idlflags_ = ['oleautomation']
SimpleTextPath._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ITextPath, ITextPath2, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist]

class IStyleGalleryStorage(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manage the files used in the Style Gallery.'
    _iid_ = GUID('{001D15B3-0F79-11D2-ADFE-080009EC732A}')
    _idlflags_ = ['oleautomation']
IStyleGalleryStorage._methods_ = [
    COMMETHOD(['propget', helpstring(u'The number of files in the Style Gallery.')], HRESULT, 'FileCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'The file at the given index.')], HRESULT, 'File',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'path' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the specified file can be updated.')], HRESULT, 'CanUpdate',
              ( ['in'], BSTR, 'path' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'CanUpdate' )),
    COMMETHOD(['propget', helpstring(u'The target output file for adding, updating and removing items.')], HRESULT, 'TargetFile',
              ( ['retval', 'out'], POINTER(BSTR), 'path' )),
    COMMETHOD(['propput', helpstring(u'The target output file for adding, updating and removing items.')], HRESULT, 'TargetFile',
              ( ['in'], BSTR, 'path' )),
    COMMETHOD([helpstring(u'Adds a file to the Style Gallery.')], HRESULT, 'AddFile',
              ( ['in'], BSTR, 'path' )),
    COMMETHOD([helpstring(u'Removes a file from the Style Gallery.')], HRESULT, 'RemoveFile',
              ( ['in'], BSTR, 'path' )),
    COMMETHOD(['propget', helpstring(u'The default file path for searching for standard styles.')], HRESULT, 'DefaultStylePath',
              ( ['retval', 'out'], POINTER(BSTR), 'path' )),
]
################################################################
## code template for IStyleGalleryStorage implementation
##class IStyleGalleryStorage_Impl(object):
##    @property
##    def CanUpdate(self, path):
##        u'Indicates if the specified file can be updated.'
##        #return CanUpdate
##
##    def AddFile(self, path):
##        u'Adds a file to the Style Gallery.'
##        #return 
##
##    def _get(self):
##        u'The target output file for adding, updating and removing items.'
##        #return path
##    def _set(self, path):
##        u'The target output file for adding, updating and removing items.'
##    TargetFile = property(_get, _set, doc = _set.__doc__)
##
##    def RemoveFile(self, path):
##        u'Removes a file from the Style Gallery.'
##        #return 
##
##    @property
##    def File(self, index):
##        u'The file at the given index.'
##        #return path
##
##    @property
##    def DefaultStylePath(self):
##        u'The default file path for searching for standard styles.'
##        #return path
##
##    @property
##    def FileCount(self):
##        u'The number of files in the Style Gallery.'
##        #return Count
##

class RepresentationMarker(CoClass):
    u'A representation marker object.'
    _reg_clsid_ = GUID('{CBD4D76F-4DA2-4839-9860-475510627CBF}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IRepresentationMarker(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control a representation marker.'
    _iid_ = GUID('{DD9693DF-153C-4290-A5EA-C4CF9E818724}')
    _idlflags_ = ['oleautomation']
class IRepresentationGraphics(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the content of a RepresentationGraphics object.'
    _iid_ = GUID('{B3EB5501-8998-498F-9B38-05CAEB8D8599}')
    _idlflags_ = ['oleautomation']
class IGraphicsOutline(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods dealing with the outline of a graphics.'
    _iid_ = GUID('{2AF790AD-4539-43C8-870E-FA75A50B9988}')
    _idlflags_ = ['oleautomation']
RepresentationMarker._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRepresentationMarker, IRepresentationGraphics, IGraphicsOutline, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLVersionSupport]

class ServerStyleGalleryItem(CoClass):
    u'An item in the Server Style Gallery.'
    _reg_clsid_ = GUID('{0B93A220-FA16-4B88-BC91-7F413B7CA433}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
ServerStyleGalleryItem._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IStyleGalleryItem, IStyleGalleryItem2, IStyleGalleryItem3, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone]

class BalloonCallout(CoClass):
    u'A filled background that is placed behind text.'
    _reg_clsid_ = GUID('{C8D09ED2-4FBB-11D1-9A72-0080C7EC5C96}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IBalloonCallout(ICallout):
    _case_insensitive_ = True
    u'Provides access to members that control the balloon callout.'
    _iid_ = GUID('{C8D09ED0-4FBB-11D1-9A72-0080C7EC5C96}')
    _idlflags_ = ['oleautomation']
class ITextMargins(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the text margins.'
    _iid_ = GUID('{6A7EF982-6924-11D2-980D-0080C7E04196}')
    _idlflags_ = ['oleautomation']
BalloonCallout._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IBalloonCallout, ITextBackground, ITextBackground2, ITextMargins, IQueryGeometry, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, IDisplayName, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize]

class MarkerPlacementPolygonCenter(CoClass):
    u'Places one marker at the center of a polygon.'
    _reg_clsid_ = GUID('{C2DA7EF9-5AE1-4D6B-95BC-AD78771962E4}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IClippingMethod(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the clipping method required by an object.'
    _iid_ = GUID('{435B4767-E029-481A-933E-D720A69D5A7D}')
    _idlflags_ = ['oleautomation']
MarkerPlacementPolygonCenter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMarkerPlacement, IGraphicAttributes, IGraphicAttributes2, IEditInteraction, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, IClippingMethod, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

class IStyleImporter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that import styles.'
    _iid_ = GUID('{17049F80-8E15-11D2-983E-0080C7E04196}')
    _idlflags_ = ['oleautomation']
IStyleImporter._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if the specified file can be imported.')], HRESULT, 'CanImport',
              ( ['in'], BSTR, 'fileName' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'CanImport' )),
    COMMETHOD([helpstring(u'Imports the specified file into the Style Gallery.')], HRESULT, 'Import',
              ( ['in'], BSTR, 'fileName' )),
    COMMETHOD(['propget', helpstring(u"The file extension(s) for files supported by this style importer. If there is more than one, then they are separated with ';'.")], HRESULT, 'FileFilter',
              ( ['retval', 'out'], POINTER(BSTR), 'fileExtension' )),
]
################################################################
## code template for IStyleImporter implementation
##class IStyleImporter_Impl(object):
##    def Import(self, fileName):
##        u'Imports the specified file into the Style Gallery.'
##        #return 
##
##    @property
##    def FileFilter(self):
##        u"The file extension(s) for files supported by this style importer. If there is more than one, then they are separated with ';'."
##        #return fileExtension
##
##    @property
##    def CanImport(self, fileName):
##        u'Indicates if the specified file can be imported.'
##        #return CanImport
##


# values for enumeration 'esriTextDirection'
esriTDHorizontal = 0
esriTDAngle = 1
esriTDVertical = 2
esriTextDirection = c_int # enum
class GeometricEffectBuffer(CoClass):
    u'Constructs a buffer polygon from any type of geometry.'
    _reg_clsid_ = GUID('{8F467AB7-8C02-42ED-9E3B-15217730405A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
GeometricEffectBuffer._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGeometricEffect, IGraphicAttributes, IGraphicAttributes2, IEditInteraction, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

class GeometryDraw(CoClass):
    u'Converts a geometry to a sequence of Win32 drawing instructions.'
    _reg_clsid_ = GUID('{40BD55F0-5F13-11D2-BCDB-0000F875BCCE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IGeometryDraw(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that convert a geometry into a sequence of Win32 drawing instructions.'
    _iid_ = GUID('{741451A0-5F13-11D2-BCDB-0000F875BCCE}')
    _idlflags_ = ['oleautomation']
GeometryDraw._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGeometryDraw, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

class EnumServerStyleGalleryItem(CoClass):
    u'An enumerator of Server Style Gallery items.'
    _reg_clsid_ = GUID('{0F41EDC3-0F2A-4351-93EB-138CE02A7360}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
EnumServerStyleGalleryItem._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IEnumStyleGalleryItem]

class IScaleTracker(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the scale tracker.'
    _iid_ = GUID('{2DC98F3B-38AA-11D3-9F3C-00C04F6BC979}')
    _idlflags_ = ['oleautomation']
IScaleTracker._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The display used by the tracker.')], HRESULT, 'Display',
              ( ['in'], POINTER(IScreenDisplay), 'rhs' )),
    COMMETHOD(['propget', helpstring(u"If the mouse is over the tracker, return an HCURSOR to indicate legal operations based on mouse's relation to selection handles: move resize, etc.  Return 0 if mouse isn't over tracker.")], HRESULT, 'Cursor',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'Cursor' )),
    COMMETHOD([helpstring(u'Invalidate the portion of the screen covered by the tracker.')], HRESULT, 'Refresh'),
    COMMETHOD([helpstring(u'Begin tracking move or resize based on the location of the mouse over the tracker handles.')], HRESULT, 'OnMouseDown'),
    COMMETHOD([helpstring(u'In process move or resize tracking.')], HRESULT, 'OnMouseMove',
              ( [], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'mapPoint' )),
    COMMETHOD([helpstring(u'Finish move or resize tracking.')], HRESULT, 'OnMouseUp',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'scaleChanged' )),
    COMMETHOD([helpstring(u'Special keypress processing while tracking.')], HRESULT, 'OnKeyDown',
              ( ['in'], c_int, 'keyCode' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'scaleChanged' )),
    COMMETHOD([helpstring(u'Cancel tracking.')], HRESULT, 'Deactivate',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'complete' )),
    COMMETHOD(['propput', helpstring(u'The scale origin.')], HRESULT, 'Origin',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Anchor' )),
    COMMETHOD(['propget', helpstring(u'The scale origin.')], HRESULT, 'Origin',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint)), 'Anchor' )),
    COMMETHOD([helpstring(u'Adds a geometry to be scaled.')], HRESULT, 'AddGeometry',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'Geometry' )),
    COMMETHOD([helpstring(u'Clears all the geometries.')], HRESULT, 'ClearGeometry'),
    COMMETHOD(['propget', helpstring(u'The scale factor.')], HRESULT, 'ScaleFactor',
              ( ['retval', 'out'], POINTER(c_double), 'factor' )),
]
################################################################
## code template for IScaleTracker implementation
##class IScaleTracker_Impl(object):
##    def _get(self):
##        u'The scale origin.'
##        #return Anchor
##    def _set(self, Anchor):
##        u'The scale origin.'
##    Origin = property(_get, _set, doc = _set.__doc__)
##
##    def Deactivate(self):
##        u'Cancel tracking.'
##        #return complete
##
##    def OnKeyDown(self, keyCode):
##        u'Special keypress processing while tracking.'
##        #return scaleChanged
##
##    def Refresh(self):
##        u'Invalidate the portion of the screen covered by the tracker.'
##        #return 
##
##    def OnMouseDown(self):
##        u'Begin tracking move or resize based on the location of the mouse over the tracker handles.'
##        #return 
##
##    @property
##    def Cursor(self):
##        u"If the mouse is over the tracker, return an HCURSOR to indicate legal operations based on mouse's relation to selection handles: move resize, etc.  Return 0 if mouse isn't over tracker."
##        #return Cursor
##
##    def AddGeometry(self, Geometry):
##        u'Adds a geometry to be scaled.'
##        #return 
##
##    def OnMouseMove(self, mapPoint):
##        u'In process move or resize tracking.'
##        #return 
##
##    def OnMouseUp(self):
##        u'Finish move or resize tracking.'
##        #return scaleChanged
##
##    @property
##    def ScaleFactor(self):
##        u'The scale factor.'
##        #return factor
##
##    def Display(self, rhs):
##        u'The display used by the tracker.'
##        #return 
##
##    def ClearGeometry(self):
##        u'Clears all the geometries.'
##        #return 
##

class LineCallout(CoClass):
    u'A series of line symbols that link text to a specified location.'
    _reg_clsid_ = GUID('{C8D09ED3-4FBB-11D1-9A72-0080C7EC5C96}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
LineCallout._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ILineCallout, ITextBackground, ITextBackground2, IMarkerBackground, ITextMargins, IQueryGeometry, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, IDisplayName, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize]

class ServerStyleGallery(CoClass):
    u'The Server Style Gallery.'
    _reg_clsid_ = GUID('{9CDCF7DA-63B8-4F23-B769-1DB1BCEADD35}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
ServerStyleGallery._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IStyleGallery, IStyleGalleryStorage, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream]


# values for enumeration 'esriSimpleFillStyle'
esriSFSSolid = 0
esriSFSNull = 1
esriSFSHollow = 1
esriSFSHorizontal = 2
esriSFSVertical = 3
esriSFSForwardDiagonal = 4
esriSFSBackwardDiagonal = 5
esriSFSCross = 6
esriSFSDiagonalCross = 7
esriSimpleFillStyle = c_int # enum
class IDynamicGlyphFactory(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to create dynamic glyphs.'
    _iid_ = GUID('{3AFB5CAB-9931-4FAA-90F5-E0BD69CF3A28}')
    _idlflags_ = ['oleautomation']
class IDynamicGlyphFactory2(IDynamicGlyphFactory):
    _case_insensitive_ = True
    u'Provides access to create dynamic glyphs.'
    _iid_ = GUID('{06C19C7C-1B78-4468-908D-2E69A9AE6D22}')
    _idlflags_ = ['oleautomation']
class IDynamicGlyph(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to handle to a resource that is used to render a dynamic symbol.'
    _iid_ = GUID('{7AC555C0-7BBA-4D36-B540-AFB13AA80050}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriDynamicGlyphType'
esriDGlyphMarker = 0
esriDGlyphLine = 1
esriDGlyphText = 2
esriDGlyphFill = 3
esriDynamicGlyphType = c_int # enum
IDynamicGlyphFactory._methods_ = [
    COMMETHOD([helpstring(u'Initialize the dynamic glyph factory.')], HRESULT, 'Init',
              ( ['in'], POINTER(IScreenDisplay), 'ScreenDisplay' )),
    COMMETHOD([helpstring(u'Creates a dynamic glyph from a symbol.')], HRESULT, 'CreateDynamicGlyph',
              ( ['in'], POINTER(ISymbol), 'Symbol' ),
              ( ['retval', 'out'], POINTER(POINTER(IDynamicGlyph)), 'glyph' )),
    COMMETHOD([helpstring(u"Deletes the dynamic glyph's resource.")], HRESULT, 'DeleteDynamicGlyph',
              ( ['in'], POINTER(IDynamicGlyph), 'glyph' )),
    COMMETHOD([helpstring(u'Creates a dynamic glyph from a file.')], HRESULT, 'CreateDynamicGlyphFromFile',
              ( ['in'], esriDynamicGlyphType, 'GlyphType' ),
              ( ['in'], BSTR, 'fileName' ),
              ( ['in'], POINTER(IColor), 'transparencyColor' ),
              ( ['retval', 'out'], POINTER(POINTER(IDynamicGlyph)), 'glyph' )),
    COMMETHOD([helpstring(u'Loads a dynamic glyph group from files.')], HRESULT, 'LoadDynamicGlyphsGroup',
              ( ['in'], BSTR, 'fileName' ),
              ( ['retval', 'out'], POINTER(c_int), 'groupId' )),
    COMMETHOD([helpstring(u'Unloads a dynamic glyph group, and any corresponding resources.')], HRESULT, 'UnloadDynamicGlyphsGroup',
              ( ['in'], c_int, 'groupId' )),
    COMMETHOD(['propget', helpstring(u'Retrieves a dynamic glyph from a glyph group.')], HRESULT, 'DynamicGlyph',
              ( ['in'], c_int, 'groupId' ),
              ( ['in'], esriDynamicGlyphType, 'GlyphType' ),
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IDynamicGlyph)), 'glyph' )),
]
################################################################
## code template for IDynamicGlyphFactory implementation
##class IDynamicGlyphFactory_Impl(object):
##    def UnloadDynamicGlyphsGroup(self, groupId):
##        u'Unloads a dynamic glyph group, and any corresponding resources.'
##        #return 
##
##    def CreateDynamicGlyphFromFile(self, GlyphType, fileName, transparencyColor):
##        u'Creates a dynamic glyph from a file.'
##        #return glyph
##
##    @property
##    def DynamicGlyph(self, groupId, GlyphType, index):
##        u'Retrieves a dynamic glyph from a glyph group.'
##        #return glyph
##
##    def Init(self, ScreenDisplay):
##        u'Initialize the dynamic glyph factory.'
##        #return 
##
##    def CreateDynamicGlyph(self, Symbol):
##        u'Creates a dynamic glyph from a symbol.'
##        #return glyph
##
##    def DeleteDynamicGlyph(self, glyph):
##        u"Deletes the dynamic glyph's resource."
##        #return 
##
##    def LoadDynamicGlyphsGroup(self, fileName):
##        u'Loads a dynamic glyph group from files.'
##        #return groupId
##

IDynamicGlyphFactory2._methods_ = [
    COMMETHOD([helpstring(u'Indicates the texture size of the created dynamic glyph.')], HRESULT, 'GetCreatedDynamicGlyphSize',
              ( ['in'], esriDynamicGlyphType, 'GlyphType' ),
              ( ['in', 'out'], POINTER(c_int), 'sizeX' ),
              ( ['in', 'out'], POINTER(c_int), 'sizeY' )),
    COMMETHOD([helpstring(u'Indicates the texture size of the created dynamic glyph.')], HRESULT, 'SetCreatedDynamicGlyphSize',
              ( ['in'], esriDynamicGlyphType, 'GlyphType' ),
              ( ['in'], c_int, 'sizeX' ),
              ( ['in'], c_int, 'sizeY' )),
    COMMETHOD([helpstring(u'Create a dynamic glyph from a bitmap handle.')], HRESULT, 'CreateDynamicGlyphFromBitmap',
              ( ['in'], esriDynamicGlyphType, 'GlyphType' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hBmp' ),
              ( ['in'], VARIANT_BOOL, 'preserveAlphaChannel' ),
              ( ['in'], POINTER(IColor), 'transparencyColor' ),
              ( ['retval', 'out'], POINTER(POINTER(IDynamicGlyph)), 'glyph' )),
]
################################################################
## code template for IDynamicGlyphFactory2 implementation
##class IDynamicGlyphFactory2_Impl(object):
##    def SetCreatedDynamicGlyphSize(self, GlyphType, sizeX, sizeY):
##        u'Indicates the texture size of the created dynamic glyph.'
##        #return 
##
##    def CreateDynamicGlyphFromBitmap(self, GlyphType, hBmp, preserveAlphaChannel, transparencyColor):
##        u'Create a dynamic glyph from a bitmap handle.'
##        #return glyph
##
##    def GetCreatedDynamicGlyphSize(self, GlyphType):
##        u'Indicates the texture size of the created dynamic glyph.'
##        #return sizeX, sizeY
##

class ILineStroke(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the line stroke.'
    _iid_ = GUID('{84F0A9DD-8B74-4B84-BD38-5EEE0154CD34}')
    _idlflags_ = ['oleautomation']
IBasicLineSymbol._methods_ = [
    COMMETHOD(['propget', helpstring(u'Line stroke of a basic line symbol.')], HRESULT, 'Stroke',
              ( ['retval', 'out'], POINTER(POINTER(ILineStroke)), 'Stroke' )),
    COMMETHOD(['propputref', helpstring(u'Line stroke of a basic line symbol.')], HRESULT, 'Stroke',
              ( ['in'], POINTER(ILineStroke), 'Stroke' )),
]
################################################################
## code template for IBasicLineSymbol implementation
##class IBasicLineSymbol_Impl(object):
##    def Stroke(self, Stroke):
##        u'Line stroke of a basic line symbol.'
##        #return 
##

class MoveImageFeedback(CoClass):
    u'Display feedback for tracking image move.'
    _reg_clsid_ = GUID('{8C25C472-2030-11D2-A28C-080009B6F22B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
MoveImageFeedback._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMoveImageFeedback, IMoveImageFeedback2]

class IEnumSymbol(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Symbol enumerator.'
    _iid_ = GUID('{2F77F380-4448-11D2-97CC-0080C7E04196}')
    _idlflags_ = ['oleautomation']
IEnumSymbol._methods_ = [
    COMMETHOD([helpstring(u'Retrieves the next symbol in the enumeration sequence.')], HRESULT, 'Next',
              ( ['retval', 'out'], POINTER(POINTER(ISymbol)), 'Symbol' )),
    COMMETHOD([helpstring(u'Resets the enumeration sequence to the beginning.')], HRESULT, 'Reset'),
]
################################################################
## code template for IEnumSymbol implementation
##class IEnumSymbol_Impl(object):
##    def Reset(self):
##        u'Resets the enumeration sequence to the beginning.'
##        #return 
##
##    def Next(self):
##        u'Retrieves the next symbol in the enumeration sequence.'
##        #return Symbol
##

class IPresetColorRamp(IColorRamp):
    _case_insensitive_ = True
    u'Provides access to members that control the PresetColorRamp. A color ramp that must contain exactly 13 preset colors.'
    _iid_ = GUID('{BEB87097-C0B4-11D0-8379-080009B996CC}')
    _idlflags_ = ['oleautomation']
IPresetColorRamp._methods_ = [
    COMMETHOD(['propput', helpstring(u'The color at the index position.')], HRESULT, 'PresetColor',
              ( ['in'], c_int, 'index' ),
              ( ['in'], POINTER(IColor), 'Color' )),
    COMMETHOD(['propget', helpstring(u'The color at the index position.')], HRESULT, 'PresetColor',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IColor)), 'Color' )),
    COMMETHOD(['propget', helpstring(u'The number of valid colors in the color ramp.  This must equal 13 before you can get values from the ramp.')], HRESULT, 'NumberOfPresetColors',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
]
################################################################
## code template for IPresetColorRamp implementation
##class IPresetColorRamp_Impl(object):
##    def _get(self, index):
##        u'The color at the index position.'
##        #return Color
##    def _set(self, index, Color):
##        u'The color at the index position.'
##    PresetColor = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def NumberOfPresetColors(self):
##        u'The number of valid colors in the color ramp.  This must equal 13 before you can get values from the ramp.'
##        #return Count
##

class GeometricEffectReverse(CoClass):
    u'Reverses the direction of a line.'
    _reg_clsid_ = GUID('{10BC917B-1FA5-4520-A4FA-D979AED15306}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
GeometricEffectReverse._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGeometricEffect, IGraphicAttributes, IGraphicAttributes2, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

class IGraphicAttributeDashType(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods dealing with dash attribute values.'
    _iid_ = GUID('{6DCFB032-AB81-4B21-A607-82ADA274516F}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriDashAttributeType'
esriDashAttributeTypeFillsAndGaps = 0
esriDashAttributeTypeOnlyGaps = 1
esriDashAttributeType = c_int # enum
IGraphicAttributeDashType._methods_ = [
    COMMETHOD(['propget', helpstring(u'Type of dash attribute.')], HRESULT, 'DashType',
              ( ['retval', 'out'], POINTER(esriDashAttributeType), 'val' )),
    COMMETHOD(['propput', helpstring(u'Type of dash attribute.')], HRESULT, 'DashType',
              ( ['in'], esriDashAttributeType, 'val' )),
]
################################################################
## code template for IGraphicAttributeDashType implementation
##class IGraphicAttributeDashType_Impl(object):
##    def _get(self):
##        u'Type of dash attribute.'
##        #return val
##    def _set(self, val):
##        u'Type of dash attribute.'
##    DashType = property(_get, _set, doc = _set.__doc__)
##

class IStyleGalleryClass2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Style Gallery Class.'
    _iid_ = GUID('{80D91E03-4A43-4659-82B4-CD80D5608003}')
    _idlflags_ = []
IStyleGalleryClass2._methods_ = [
    COMMETHOD(['propget', helpstring(u'Name of the Style Gallery Class (as in the stle file).')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'Description for the Style Gallery Class.')], HRESULT, 'Description',
              ( ['retval', 'out'], POINTER(BSTR), 'Description' )),
    COMMETHOD(['propget', helpstring(u'Interface ID for the items in the class.')], HRESULT, 'ItemClass',
              ( ['retval', 'out'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'iid' )),
    COMMETHOD(['propget', helpstring(u'The available types of new items in this class.')], HRESULT, 'NewObjectTypes',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IEnumBSTR)), 'newTypes' )),
    COMMETHOD(['propget', helpstring(u'Creates a new object of the specified type.')], HRESULT, 'NewObject',
              ( ['in'], BSTR, 'newType' ),
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'NewObject' )),
    COMMETHOD(['propget', helpstring(u'The width ratio to 1 height.')], HRESULT, 'PreviewRatio',
              ( ['retval', 'out'], POINTER(c_double), 'ratio' )),
    COMMETHOD([helpstring(u'Draws a preview of a Style Gallery Item of the supported class.')], HRESULT, 'Preview',
              ( ['in'], POINTER(IUnknown), 'galleryItem' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDC' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.tagRECT), 'rectangle' )),
    COMMETHOD([helpstring(u'Edits the properties of a Style Gallery Item of the supported class.')], HRESULT, 'EditProperties',
              ( ['in'], POINTER(POINTER(IUnknown)), 'galleryItem' ),
              ( ['in'], POINTER(comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IComPropertySheetEvents), 'listener' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hWnd' ),
              ( ['out'], POINTER(VARIANT_BOOL), 'ok' )),
    COMMETHOD(['propget', helpstring(u'Display name of the Style Gallery Class.')], HRESULT, 'DisplayName',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
]
################################################################
## code template for IStyleGalleryClass2 implementation
##class IStyleGalleryClass2_Impl(object):
##    @property
##    def ItemClass(self):
##        u'Interface ID for the items in the class.'
##        #return iid
##
##    @property
##    def DisplayName(self):
##        u'Display name of the Style Gallery Class.'
##        #return Name
##
##    @property
##    def Name(self):
##        u'Name of the Style Gallery Class (as in the stle file).'
##        #return Name
##
##    @property
##    def NewObjectTypes(self):
##        u'The available types of new items in this class.'
##        #return newTypes
##
##    @property
##    def PreviewRatio(self):
##        u'The width ratio to 1 height.'
##        #return ratio
##
##    def EditProperties(self, galleryItem, listener, hWnd):
##        u'Edits the properties of a Style Gallery Item of the supported class.'
##        #return ok
##
##    @property
##    def NewObject(self, newType):
##        u'Creates a new object of the specified type.'
##        #return NewObject
##
##    def Preview(self, galleryItem, hDC, rectangle):
##        u'Draws a preview of a Style Gallery Item of the supported class.'
##        #return 
##
##    @property
##    def Description(self):
##        u'Description for the Style Gallery Class.'
##        #return Description
##

IMoveEnvelopeFeedback._methods_ = [
    COMMETHOD([helpstring(u'Begins a move feedback of the given shape.')], HRESULT, 'Start',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'envelope' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
    COMMETHOD([helpstring(u'Stops the feedback and returns the shape.')], HRESULT, 'Stop',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'envelope' )),
]
################################################################
## code template for IMoveEnvelopeFeedback implementation
##class IMoveEnvelopeFeedback_Impl(object):
##    def Start(self, envelope, Point):
##        u'Begins a move feedback of the given shape.'
##        #return 
##
##    def Stop(self):
##        u'Stops the feedback and returns the shape.'
##        #return envelope
##

class FontSize(CoClass):
    u'The size of the text as specified in points.'
    _reg_clsid_ = GUID('{936CE290-0971-11D3-BCAD-0080C7E04196}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IFontSize(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the font size object.'
    _iid_ = GUID('{6E7CB970-0A4D-11D3-BCAF-0080C7E04196}')
    _idlflags_ = ['oleautomation']
FontSize._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IFontSize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone]


# values for enumeration 'esriGDIComments'
esriGDIComment_Begin_Text = 4097
esriGDIComment_End_Text = 4098
esriGDIComment_Set_Text_Extra = 4099
esriGDIComment_Set_Cmyk_Color = 4100
esriGDIComment_Begin_Layer = 4101
esriGDIComment_End_Layer = 4102
esriGDIComment_Begin_Group = 4103
esriGDIComment_End_Group = 4104
esriGDIComment_FillWithPattern = 4105
esriGDIComment_Mask_Layer = 4106
esriGDIComment_Mask_Layer_Before_Clipping = 4107
esriGDIComment_PlayEnhMetafileBegin = 4108
esriGDIComment_PlayEnhMetafileEnd = 4109
esriGDIComment_Set_Text_Justification = 4110
esriGDIComment_Begin_Feature_Attribute = 4111
esriGDIComment_End_Feature_Attribute = 4112
esriGDIComment_Feature_Attribute = 4113
esriGDIComment_Feature_URL = 4114
esriGDIComment_Begin_Map = 4115
esriGDIComment_End_Map = 4116
esriGDIComment_Begin_PageLayout = 4117
esriGDIComment_End_PageLayout = 4118
esriGDIComment_Begin_Feature = 4119
esriGDIComment_End_Feature = 4120
esriGDIComments = c_int # enum
IVertexFeedback._methods_ = [
    COMMETHOD([helpstring(u'Adds an edge to rubberband.')], HRESULT, 'AddSegment',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISegment), 'segment' ),
              ( ['in'], VARIANT_BOOL, 'fromPointIsAnchor' )),
]
################################################################
## code template for IVertexFeedback implementation
##class IVertexFeedback_Impl(object):
##    def AddSegment(self, segment, fromPointIsAnchor):
##        u'Adds an edge to rubberband.'
##        #return 
##

IGeodeticLineFeedback._methods_ = [
    COMMETHOD(['propget', helpstring(u'The spatial reference of the feedback line.')], HRESULT, 'SpatialReference',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference)), 'sr' )),
    COMMETHOD(['propputref', helpstring(u'The spatial reference of the feedback line.')], HRESULT, 'SpatialReference',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference), 'sr' )),
    COMMETHOD(['propget', helpstring(u'Specifies if geodetic construction will be used.')], HRESULT, 'UseGeodeticConstruction',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD(['propput', helpstring(u'Specifies if geodetic construction will be used.')], HRESULT, 'UseGeodeticConstruction',
              ( ['in'], VARIANT_BOOL, 'flag' )),
    COMMETHOD(['propget', helpstring(u'The geodetic construction method.')], HRESULT, 'GeodeticConstructionMethod',
              ( ['retval', 'out'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.esriGeodeticType), 'gType' )),
    COMMETHOD(['propput', helpstring(u'The geodetic construction method.')], HRESULT, 'GeodeticConstructionMethod',
              ( ['in'], comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.esriGeodeticType, 'gType' )),
]
################################################################
## code template for IGeodeticLineFeedback implementation
##class IGeodeticLineFeedback_Impl(object):
##    def _get(self):
##        u'Specifies if geodetic construction will be used.'
##        #return flag
##    def _set(self, flag):
##        u'Specifies if geodetic construction will be used.'
##    UseGeodeticConstruction = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The geodetic construction method.'
##        #return gType
##    def _set(self, gType):
##        u'The geodetic construction method.'
##    GeodeticConstructionMethod = property(_get, _set, doc = _set.__doc__)
##
##    def SpatialReference(self, sr):
##        u'The spatial reference of the feedback line.'
##        #return 
##

class GeometricEffectSuppress(CoClass):
    u'Suppresses part of a line or polygon outline.'
    _reg_clsid_ = GUID('{B6A152D7-A882-4014-9380-C960E524427E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
GeometricEffectSuppress._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGeometricEffect, IGraphicAttributes, IGraphicAttributes2, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

class MarkerPlacementOnPoint(CoClass):
    u'Places a marker on a point.'
    _reg_clsid_ = GUID('{160C7BFF-2237-4A67-B163-89C223DB0A1D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
MarkerPlacementOnPoint._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMarkerPlacement, IGraphicAttributes, IGraphicAttributes2, IEditInteraction, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

class MarkerPlacementInsidePolygon(CoClass):
    u'Places markers in a polygon.'
    _reg_clsid_ = GUID('{D94F6764-5D28-4A6C-90B6-3F365B6B0539}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
MarkerPlacementInsidePolygon._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMarkerPlacement, IGraphicAttributes, IGraphicAttributes2, IEditInteraction, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, IClippingMethod, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

class I3DChartSymbol(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to 3D properties of chart symbols.'
    _iid_ = GUID('{50317367-BD70-11D3-9F79-00C04F6BC709}')
    _idlflags_ = ['oleautomation']
I3DChartSymbol._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if the chart symbol is 3D.')], HRESULT, 'Display3D',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the chart symbol is 3D.')], HRESULT, 'Display3D',
              ( ['in'], VARIANT_BOOL, 'flag' )),
    COMMETHOD(['propget', helpstring(u'3D thickness of the chart symbol.')], HRESULT, 'Thickness',
              ( ['retval', 'out'], POINTER(c_double), 'Points' )),
    COMMETHOD(['propput', helpstring(u'3D thickness of the chart symbol.')], HRESULT, 'Thickness',
              ( ['in'], c_double, 'Points' )),
    COMMETHOD(['propget', helpstring(u'Tilt of 3D Display (0-90 degrees).')], HRESULT, 'Tilt',
              ( ['retval', 'out'], POINTER(c_int), 'Angle' )),
    COMMETHOD(['propput', helpstring(u'Tilt of 3D Display (0-90 degrees).')], HRESULT, 'Tilt',
              ( ['in'], c_int, 'Angle' )),
]
################################################################
## code template for I3DChartSymbol implementation
##class I3DChartSymbol_Impl(object):
##    def _get(self):
##        u'Tilt of 3D Display (0-90 degrees).'
##        #return Angle
##    def _set(self, Angle):
##        u'Tilt of 3D Display (0-90 degrees).'
##    Tilt = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the chart symbol is 3D.'
##        #return flag
##    def _set(self, flag):
##        u'Indicates if the chart symbol is 3D.'
##    Display3D = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'3D thickness of the chart symbol.'
##        #return Points
##    def _set(self, Points):
##        u'3D thickness of the chart symbol.'
##    Thickness = property(_get, _set, doc = _set.__doc__)
##

class IFillProperties(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the general fill properties.'
    _iid_ = GUID('{7914E5F3-C892-11D0-8BB6-080009EE4E41}')
    _idlflags_ = ['oleautomation']
IFillProperties._methods_ = [
    COMMETHOD(['propget', helpstring(u'Fill offset along X-axis.')], HRESULT, 'XOffset',
              ( ['retval', 'out'], POINTER(c_double), 'XOffset' )),
    COMMETHOD(['propput', helpstring(u'Fill offset along X-axis.')], HRESULT, 'XOffset',
              ( ['in'], c_double, 'XOffset' )),
    COMMETHOD(['propget', helpstring(u'Fill offset along Y-axis.')], HRESULT, 'YOffset',
              ( ['retval', 'out'], POINTER(c_double), 'YOffset' )),
    COMMETHOD(['propput', helpstring(u'Fill offset along Y-axis.')], HRESULT, 'YOffset',
              ( ['in'], c_double, 'YOffset' )),
    COMMETHOD(['propget', helpstring(u'Fill element separation along X-axis.')], HRESULT, 'XSeparation',
              ( ['retval', 'out'], POINTER(c_double), 'XSeparation' )),
    COMMETHOD(['propput', helpstring(u'Fill element separation along X-axis.')], HRESULT, 'XSeparation',
              ( ['in'], c_double, 'XSeparation' )),
    COMMETHOD(['propget', helpstring(u'Fill element separation along Y-axis.')], HRESULT, 'YSeparation',
              ( ['retval', 'out'], POINTER(c_double), 'YSeparation' )),
    COMMETHOD(['propput', helpstring(u'Fill element separation along Y-axis.')], HRESULT, 'YSeparation',
              ( ['in'], c_double, 'YSeparation' )),
]
################################################################
## code template for IFillProperties implementation
##class IFillProperties_Impl(object):
##    def _get(self):
##        u'Fill element separation along Y-axis.'
##        #return YSeparation
##    def _set(self, YSeparation):
##        u'Fill element separation along Y-axis.'
##    YSeparation = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Fill element separation along X-axis.'
##        #return XSeparation
##    def _set(self, XSeparation):
##        u'Fill element separation along X-axis.'
##    XSeparation = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Fill offset along X-axis.'
##        #return XOffset
##    def _set(self, XOffset):
##        u'Fill offset along X-axis.'
##    XOffset = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Fill offset along Y-axis.'
##        #return YOffset
##    def _set(self, YOffset):
##        u'Fill offset along Y-axis.'
##    YOffset = property(_get, _set, doc = _set.__doc__)
##

IDimDisplayFilter._methods_ = [
    COMMETHOD(['propput', helpstring(u'Dim value (0-255).')], HRESULT, 'DimValue',
              ( ['in'], c_short, 'dim' )),
    COMMETHOD(['propget', helpstring(u'Dim value (0-255).')], HRESULT, 'DimValue',
              ( ['retval', 'out'], POINTER(c_short), 'dim' )),
    COMMETHOD(['propput', helpstring(u'Opacity value (0-255).')], HRESULT, 'Opacity',
              ( ['in'], c_short, 'alpha' )),
    COMMETHOD(['propget', helpstring(u'Opacity value (0-255).')], HRESULT, 'Opacity',
              ( ['retval', 'out'], POINTER(c_short), 'alpha' )),
]
################################################################
## code template for IDimDisplayFilter implementation
##class IDimDisplayFilter_Impl(object):
##    def _get(self):
##        u'Opacity value (0-255).'
##        #return alpha
##    def _set(self, alpha):
##        u'Opacity value (0-255).'
##    Opacity = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Dim value (0-255).'
##        #return dim
##    def _set(self, dim):
##        u'Dim value (0-255).'
##    DimValue = property(_get, _set, doc = _set.__doc__)
##


# values for enumeration 'esriDynamicDrawPhase'
esriDDPImmediate = 0
esriDDPCompiled = 1
esriDynamicDrawPhase = c_int # enum

# values for enumeration 'esriDynamicSelectionMode'
esriDSMNone = 0
esriDSMLayers = 1
esriDSMBeforeDynamicDraw = 16
esriDSMAfterDynamicDraw = 256
esriDSMDynamicDrawing = 4096
esriDynamicSelectionMode = c_int # enum
class IMarkerBackgroundSupport(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the marker background support.'
    _iid_ = GUID('{9CE9D410-DDEB-11D3-8216-0080C79F0371}')
    _idlflags_ = ['oleautomation']
IMarkerBackgroundSupport._methods_ = [
    COMMETHOD(['propget', helpstring(u'The marker background.')], HRESULT, 'Background',
              ( ['retval', 'out'], POINTER(POINTER(IMarkerBackground)), 'Background' )),
    COMMETHOD(['propputref', helpstring(u'The marker background.')], HRESULT, 'Background',
              ( ['in'], POINTER(IMarkerBackground), 'Background' )),
]
################################################################
## code template for IMarkerBackgroundSupport implementation
##class IMarkerBackgroundSupport_Impl(object):
##    def Background(self, Background):
##        u'The marker background.'
##        #return 
##


# values for enumeration 'esriDynamicSymbolType'
esriDSymbolMarker = 0
esriDSymbolLine = 1
esriDSymbolText = 2
esriDSymbolFill = 3
esriDynamicSymbolType = c_int # enum
IReshapeFeedback2._methods_ = [
    COMMETHOD([helpstring(u'Specify a vertex to move.')], HRESULT, 'SelectVertex',
              ( ['in'], c_int, 'Part' ),
              ( ['in'], c_int, 'vertex' )),
    COMMETHOD([helpstring(u'Start the feedback.')], HRESULT, 'Start',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'Geometry' ),
              ( [], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' ),
              ( [], VARIANT_BOOL, 'stretch' )),
    COMMETHOD([helpstring(u'Stop the feedback.')], HRESULT, 'Stop',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry)), 'Geometry' )),
    COMMETHOD([helpstring(u'Abort the feedback.')], HRESULT, 'Abort'),
]
################################################################
## code template for IReshapeFeedback2 implementation
##class IReshapeFeedback2_Impl(object):
##    def Start(self, Geometry, Point, stretch):
##        u'Start the feedback.'
##        #return 
##
##    def Abort(self):
##        u'Abort the feedback.'
##        #return 
##
##    def Stop(self, Point):
##        u'Stop the feedback.'
##        #return Geometry
##
##    def SelectVertex(self, Part, vertex):
##        u'Specify a vertex to move.'
##        #return 
##

ILineStroke._methods_ = [
    COMMETHOD([helpstring(u'Draws the line stroke.')], HRESULT, 'Draw',
              ( ['in'], POINTER(IOutputContext), 'context' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'Geometry' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'envelope' )),
]
################################################################
## code template for ILineStroke implementation
##class ILineStroke_Impl(object):
##    def Draw(self, context, Geometry, envelope):
##        u'Draws the line stroke.'
##        #return 
##

class IResizeInteraction(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the parameters of the Resize Representation Tool.'
    _iid_ = GUID('{99A21696-2D0C-4D17-95E9-F4AC339E444B}')
    _idlflags_ = ['oleautomation']
IResizeInteraction._methods_ = [
    COMMETHOD(['propput', helpstring(u'Center of the resize operation.')], HRESULT, 'Center',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Center' )),
    COMMETHOD(['propget', helpstring(u'Center of the resize operation.')], HRESULT, 'Center',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint)), 'Center' )),
    COMMETHOD(['propput', helpstring(u'Current horizontal ratio of the resize operation.')], HRESULT, 'RatioX',
              ( ['in'], c_double, 'ratio' )),
    COMMETHOD(['propget', helpstring(u'Current horizontal ratio of the resize operation.')], HRESULT, 'RatioX',
              ( ['retval', 'out'], POINTER(c_double), 'ratio' )),
    COMMETHOD(['propput', helpstring(u'Current vertical ratio of the resize operation.')], HRESULT, 'RatioY',
              ( ['in'], c_double, 'ratio' )),
    COMMETHOD(['propget', helpstring(u'Current vertical ratio of the resize operation.')], HRESULT, 'RatioY',
              ( ['retval', 'out'], POINTER(c_double), 'ratio' )),
    COMMETHOD(['propput', helpstring(u'Indicates if representations resize around an individual anchor.')], HRESULT, 'IndividualAnchors',
              ( ['in'], VARIANT_BOOL, 'IndividualAnchors' )),
    COMMETHOD(['propget', helpstring(u'Indicates if representations resize around an individual anchor.')], HRESULT, 'IndividualAnchors',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IndividualAnchors' )),
]
################################################################
## code template for IResizeInteraction implementation
##class IResizeInteraction_Impl(object):
##    def _get(self):
##        u'Indicates if representations resize around an individual anchor.'
##        #return IndividualAnchors
##    def _set(self, IndividualAnchors):
##        u'Indicates if representations resize around an individual anchor.'
##    IndividualAnchors = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Current vertical ratio of the resize operation.'
##        #return ratio
##    def _set(self, ratio):
##        u'Current vertical ratio of the resize operation.'
##    RatioY = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Center of the resize operation.'
##        #return Center
##    def _set(self, Center):
##        u'Center of the resize operation.'
##    Center = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Current horizontal ratio of the resize operation.'
##        #return ratio
##    def _set(self, ratio):
##        u'Current horizontal ratio of the resize operation.'
##    RatioX = property(_get, _set, doc = _set.__doc__)
##

class ILayerVisible(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the layer visibility.'
    _iid_ = GUID('{D7301B50-E92E-11D2-98CE-0080C7E04196}')
    _idlflags_ = ['oleautomation']
ILayerVisible._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if the layer at the specified index is visible.')], HRESULT, 'LayerVisible',
              ( ['in'], c_int, 'layerIndex' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'visible' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the layer at the specified index is visible.')], HRESULT, 'LayerVisible',
              ( ['in'], c_int, 'layerIndex' ),
              ( ['in'], VARIANT_BOOL, 'visible' )),
    COMMETHOD([helpstring(u'Indicates if all the layers are visible or invisible.')], HRESULT, 'SetAllVisible',
              ( ['in'], VARIANT_BOOL, 'allVisible' )),
]
################################################################
## code template for ILayerVisible implementation
##class ILayerVisible_Impl(object):
##    def SetAllVisible(self, allVisible):
##        u'Indicates if all the layers are visible or invisible.'
##        #return 
##
##    def _get(self, layerIndex):
##        u'Indicates if the layer at the specified index is visible.'
##        #return visible
##    def _set(self, layerIndex, visible):
##        u'Indicates if the layer at the specified index is visible.'
##    LayerVisible = property(_get, _set, doc = _set.__doc__)
##

class ITextSymbol(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control text symbols.'
    _iid_ = GUID('{A80B5E91-7F9C-11D0-9410-080009EEBECB}')
    _idlflags_ = ['oleautomation']
class ISimpleTextSymbol(ITextSymbol):
    _case_insensitive_ = True
    u'Provides access to members that control the simple text symbol.'
    _iid_ = GUID('{A80B5E8C-7F9C-11D0-9410-080009EEBECB}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriTextVerticalAlignment'
esriTVATop = 0
esriTVACenter = 1
esriTVABaseline = 2
esriTVABottom = 3
esriTextVerticalAlignment = c_int # enum

# values for enumeration 'esriTextHorizontalAlignment'
esriTHALeft = 0
esriTHACenter = 1
esriTHARight = 2
esriTHAFull = 3
esriTextHorizontalAlignment = c_int # enum
ITextSymbol._methods_ = [
    COMMETHOD(['propget', helpstring(u'Text font.')], HRESULT, 'Font',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IFontDisp)), 'fontDisp' )),
    COMMETHOD(['propput', helpstring(u'Text font.')], HRESULT, 'Font',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IFontDisp), 'fontDisp' )),
    COMMETHOD(['propget', helpstring(u'Text size.')], HRESULT, 'Size',
              ( ['retval', 'out'], POINTER(c_double), 'Size' )),
    COMMETHOD(['propput', helpstring(u'Text size.')], HRESULT, 'Size',
              ( ['in'], c_double, 'Size' )),
    COMMETHOD(['propget', helpstring(u'Text color.')], HRESULT, 'Color',
              ( ['retval', 'out'], POINTER(POINTER(IColor)), 'Color' )),
    COMMETHOD(['propput', helpstring(u'Text color.')], HRESULT, 'Color',
              ( ['in'], POINTER(IColor), 'Color' )),
    COMMETHOD(['propget', helpstring(u'Vertical alignment style.')], HRESULT, 'VerticalAlignment',
              ( ['retval', 'out'], POINTER(esriTextVerticalAlignment), 'vertAlignment' )),
    COMMETHOD(['propput', helpstring(u'Vertical alignment style.')], HRESULT, 'VerticalAlignment',
              ( ['in'], esriTextVerticalAlignment, 'vertAlignment' )),
    COMMETHOD(['propget', helpstring(u'Horizontal alignment style.')], HRESULT, 'HorizontalAlignment',
              ( ['retval', 'out'], POINTER(esriTextHorizontalAlignment), 'horizAlignment' )),
    COMMETHOD(['propput', helpstring(u'Horizontal alignment style.')], HRESULT, 'HorizontalAlignment',
              ( ['in'], esriTextHorizontalAlignment, 'horizAlignment' )),
    COMMETHOD(['propget', helpstring(u'Text baseline angle.')], HRESULT, 'Angle',
              ( ['retval', 'out'], POINTER(c_double), 'Angle' )),
    COMMETHOD(['propput', helpstring(u'Text baseline angle.')], HRESULT, 'Angle',
              ( ['in'], c_double, 'Angle' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the text is drawn from right to left.')], HRESULT, 'RightToLeft',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'RightToLeft' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the text is drawn from right to left.')], HRESULT, 'RightToLeft',
              ( ['in'], VARIANT_BOOL, 'RightToLeft' )),
    COMMETHOD(['propget', helpstring(u'Text to draw.')], HRESULT, 'Text',
              ( ['retval', 'out'], POINTER(BSTR), 'Text' )),
    COMMETHOD(['propput', helpstring(u'Text to draw.')], HRESULT, 'Text',
              ( ['in'], BSTR, 'Text' )),
    COMMETHOD([helpstring(u"Gets the x and y dimensions of 'text' in points (1/72 inch).")], HRESULT, 'GetTextSize',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDC' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ITransformation), 'Transformation' ),
              ( ['in'], BSTR, 'Text' ),
              ( ['out'], POINTER(c_double), 'xSize' ),
              ( ['out'], POINTER(c_double), 'ySize' )),
]
################################################################
## code template for ITextSymbol implementation
##class ITextSymbol_Impl(object):
##    def _get(self):
##        u'Text baseline angle.'
##        #return Angle
##    def _set(self, Angle):
##        u'Text baseline angle.'
##    Angle = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Text color.'
##        #return Color
##    def _set(self, Color):
##        u'Text color.'
##    Color = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Text to draw.'
##        #return Text
##    def _set(self, Text):
##        u'Text to draw.'
##    Text = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the text is drawn from right to left.'
##        #return RightToLeft
##    def _set(self, RightToLeft):
##        u'Indicates if the text is drawn from right to left.'
##    RightToLeft = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Horizontal alignment style.'
##        #return horizAlignment
##    def _set(self, horizAlignment):
##        u'Horizontal alignment style.'
##    HorizontalAlignment = property(_get, _set, doc = _set.__doc__)
##
##    def GetTextSize(self, hDC, Transformation, Text):
##        u"Gets the x and y dimensions of 'text' in points (1/72 inch)."
##        #return xSize, ySize
##
##    def _get(self):
##        u'Vertical alignment style.'
##        #return vertAlignment
##    def _set(self, vertAlignment):
##        u'Vertical alignment style.'
##    VerticalAlignment = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Text font.'
##        #return fontDisp
##    def _set(self, fontDisp):
##        u'Text font.'
##    Font = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Text size.'
##        #return Size
##    def _set(self, Size):
##        u'Text size.'
##    Size = property(_get, _set, doc = _set.__doc__)
##

ISimpleTextSymbol._methods_ = [
    COMMETHOD(['propget', helpstring(u'Character to be interpreted as text line end.')], HRESULT, 'BreakCharacter',
              ( ['retval', 'out'], POINTER(c_int), 'charIndex' )),
    COMMETHOD(['propput', helpstring(u'Character to be interpreted as text line end.')], HRESULT, 'BreakCharacter',
              ( ['in'], c_int, 'charIndex' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the text will be clipped per geometry.')], HRESULT, 'Clip',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Clip' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the text will be clipped per geometry.')], HRESULT, 'Clip',
              ( ['in'], VARIANT_BOOL, 'Clip' )),
    COMMETHOD(['propget', helpstring(u'Path of text baseline.')], HRESULT, 'TextPath',
              ( ['retval', 'out'], POINTER(POINTER(ITextPath)), 'TextPath' )),
    COMMETHOD(['propputref', helpstring(u'Path of text baseline.')], HRESULT, 'TextPath',
              ( ['in'], POINTER(ITextPath), 'TextPath' )),
    COMMETHOD(['propget', helpstring(u'Text offset along X-axis.')], HRESULT, 'XOffset',
              ( ['retval', 'out'], POINTER(c_double), 'XOffset' )),
    COMMETHOD(['propput', helpstring(u'Text offset along X-axis.')], HRESULT, 'XOffset',
              ( ['in'], c_double, 'XOffset' )),
    COMMETHOD(['propget', helpstring(u'Text offset along Y-axis.')], HRESULT, 'YOffset',
              ( ['retval', 'out'], POINTER(c_double), 'YOffset' )),
    COMMETHOD(['propput', helpstring(u'Text offset along Y-axis.')], HRESULT, 'YOffset',
              ( ['in'], c_double, 'YOffset' )),
]
################################################################
## code template for ISimpleTextSymbol implementation
##class ISimpleTextSymbol_Impl(object):
##    def TextPath(self, TextPath):
##        u'Path of text baseline.'
##        #return 
##
##    def _get(self):
##        u'Character to be interpreted as text line end.'
##        #return charIndex
##    def _set(self, charIndex):
##        u'Character to be interpreted as text line end.'
##    BreakCharacter = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Text offset along X-axis.'
##        #return XOffset
##    def _set(self, XOffset):
##        u'Text offset along X-axis.'
##    XOffset = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the text will be clipped per geometry.'
##        #return Clip
##    def _set(self, Clip):
##        u'Indicates if the text will be clipped per geometry.'
##    Clip = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Text offset along Y-axis.'
##        #return YOffset
##    def _set(self, YOffset):
##        u'Text offset along Y-axis.'
##    YOffset = property(_get, _set, doc = _set.__doc__)
##

class ILayerColorLock(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the layer color locking.'
    _iid_ = GUID('{D7301B51-E92E-11D2-98CE-0080C7E04196}')
    _idlflags_ = ['oleautomation']
ILayerColorLock._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if a color lock is present for the layer at the specified index.')], HRESULT, 'LayerColorLock',
              ( ['in'], c_int, 'layerIndex' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'colorLock' )),
    COMMETHOD(['propput', helpstring(u'Indicates if a color lock is present for the layer at the specified index.')], HRESULT, 'LayerColorLock',
              ( ['in'], c_int, 'layerIndex' ),
              ( ['in'], VARIANT_BOOL, 'colorLock' )),
    COMMETHOD([helpstring(u'Indicates if the color is locked for all layers.')], HRESULT, 'SetAllColorLocked',
              ( ['in'], VARIANT_BOOL, 'allLocked' )),
]
################################################################
## code template for ILayerColorLock implementation
##class ILayerColorLock_Impl(object):
##    def _get(self, layerIndex):
##        u'Indicates if a color lock is present for the layer at the specified index.'
##        #return colorLock
##    def _set(self, layerIndex, colorLock):
##        u'Indicates if a color lock is present for the layer at the specified index.'
##    LayerColorLock = property(_get, _set, doc = _set.__doc__)
##
##    def SetAllColorLocked(self, allLocked):
##        u'Indicates if the color is locked for all layers.'
##        #return 
##

IMoveLineFeedback._methods_ = [
    COMMETHOD([helpstring(u'Begins a move feedback of the given shape.')], HRESULT, 'Start',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPolyline), 'polyline' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
    COMMETHOD([helpstring(u'Stops the feedback and returns the shape.')], HRESULT, 'Stop',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPolyline)), 'polyline' )),
]
################################################################
## code template for IMoveLineFeedback implementation
##class IMoveLineFeedback_Impl(object):
##    def Start(self, polyline, Point):
##        u'Begins a move feedback of the given shape.'
##        #return 
##
##    def Stop(self):
##        u'Stops the feedback and returns the shape.'
##        #return polyline
##

IDynamicGlyph._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates the type of dynamic glyph.')], HRESULT, 'GlyphType',
              ( ['retval', 'out'], POINTER(esriDynamicGlyphType), 'GlyphType' )),
    COMMETHOD([helpstring(u'Returns the width and height, in pixels, of the glyph.  The width of the text glyph will be the width of the space character.')], HRESULT, 'QueryDimensions',
              ( ['in', 'out'], POINTER(c_float), 'Width' ),
              ( ['in', 'out'], POINTER(c_float), 'Height' )),
    COMMETHOD([helpstring(u'Indicates the origin of the glyph from the the bottom left.')], HRESULT, 'GetAnchor',
              ( ['in', 'out'], POINTER(c_float), 'xAnchor' ),
              ( ['in', 'out'], POINTER(c_float), 'yAnchor' )),
    COMMETHOD([helpstring(u'Indicates the origin of the glyph from the the bottom left.')], HRESULT, 'SetAnchor',
              ( ['in'], c_float, 'xAnchor' ),
              ( ['in'], c_float, 'yAnchor' )),
]
################################################################
## code template for IDynamicGlyph implementation
##class IDynamicGlyph_Impl(object):
##    def SetAnchor(self, xAnchor, yAnchor):
##        u'Indicates the origin of the glyph from the the bottom left.'
##        #return 
##
##    @property
##    def GlyphType(self):
##        u'Indicates the type of dynamic glyph.'
##        #return GlyphType
##
##    def QueryDimensions(self):
##        u'Returns the width and height, in pixels, of the glyph.  The width of the text glyph will be the width of the space character.'
##        #return Width, Height
##
##    def GetAnchor(self):
##        u'Indicates the origin of the glyph from the the bottom left.'
##        #return xAnchor, yAnchor
##

IMovePointFeedback._methods_ = [
    COMMETHOD([helpstring(u'Begins a move feedback of the given shape.')], HRESULT, 'Start',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'clickPoint' )),
    COMMETHOD([helpstring(u'Stops the feedback and returns the shape.')], HRESULT, 'Stop',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint)), 'Point' )),
]
################################################################
## code template for IMovePointFeedback implementation
##class IMovePointFeedback_Impl(object):
##    def Start(self, Point, clickPoint):
##        u'Begins a move feedback of the given shape.'
##        #return 
##
##    def Stop(self):
##        u'Stops the feedback and returns the shape.'
##        #return Point
##

class ILineProperties(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the properties common to several line types.'
    _iid_ = GUID('{B04BC357-C36E-11D0-BFA1-0080C7E24280}')
    _idlflags_ = ['oleautomation']
class ITemplate(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the template.'
    _iid_ = GUID('{7914E5F4-C892-11D0-8BB6-080009EE4E41}')
    _idlflags_ = ['oleautomation']
ILineProperties._methods_ = [
    COMMETHOD(['propget', helpstring(u'Line decoration element collection.')], HRESULT, 'LineDecoration',
              ( ['retval', 'out'], POINTER(POINTER(ILineDecoration)), 'LineDecoration' )),
    COMMETHOD(['propputref', helpstring(u'Line decoration element collection.')], HRESULT, 'LineDecoration',
              ( ['in'], POINTER(ILineDecoration), 'LineDecoration' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the decoration is drawn on top.')], HRESULT, 'DecorationOnTop',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'onTop' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the decoration is drawn on top.')], HRESULT, 'DecorationOnTop',
              ( ['in'], VARIANT_BOOL, 'onTop' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the line symbol is flipped.')], HRESULT, 'Flip',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Flip' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the line symbol is flipped.')], HRESULT, 'Flip',
              ( ['in'], VARIANT_BOOL, 'Flip' )),
    COMMETHOD(['propget', helpstring(u'The line offset value.')], HRESULT, 'Offset',
              ( ['retval', 'out'], POINTER(c_double), 'Offset' )),
    COMMETHOD(['propput', helpstring(u'The line offset value.')], HRESULT, 'Offset',
              ( ['in'], c_double, 'Offset' )),
    COMMETHOD(['propget', helpstring(u'The line start offset.')], HRESULT, 'LineStartOffset',
              ( ['retval', 'out'], POINTER(c_double), 'Offset' )),
    COMMETHOD(['propput', helpstring(u'The line start offset.')], HRESULT, 'LineStartOffset',
              ( ['in'], c_double, 'Offset' )),
    COMMETHOD(['propget', helpstring(u'The line template.')], HRESULT, 'Template',
              ( ['retval', 'out'], POINTER(POINTER(ITemplate)), 'theTemplate' )),
    COMMETHOD(['propputref', helpstring(u'The line template.')], HRESULT, 'Template',
              ( ['in'], POINTER(ITemplate), 'theTemplate' )),
]
################################################################
## code template for ILineProperties implementation
##class ILineProperties_Impl(object):
##    def _get(self):
##        u'The line start offset.'
##        #return Offset
##    def _set(self, Offset):
##        u'The line start offset.'
##    LineStartOffset = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the line symbol is flipped.'
##        #return Flip
##    def _set(self, Flip):
##        u'Indicates if the line symbol is flipped.'
##    Flip = property(_get, _set, doc = _set.__doc__)
##
##    def Template(self, theTemplate):
##        u'The line template.'
##        #return 
##
##    def _get(self):
##        u'The line offset value.'
##        #return Offset
##    def _set(self, Offset):
##        u'The line offset value.'
##    Offset = property(_get, _set, doc = _set.__doc__)
##
##    def LineDecoration(self, LineDecoration):
##        u'Line decoration element collection.'
##        #return 
##
##    def _get(self):
##        u'Indicates if the decoration is drawn on top.'
##        #return onTop
##    def _set(self, onTop):
##        u'Indicates if the decoration is drawn on top.'
##    DecorationOnTop = property(_get, _set, doc = _set.__doc__)
##

class MarkerPlacementAlongLine(CoClass):
    u'Places markers along a line.'
    _reg_clsid_ = GUID('{5955E642-623B-4D55-86E9-0442C6272942}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
MarkerPlacementAlongLine._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMarkerPlacement, IGraphicAttributes, IGraphicAttributes2, IEditInteraction, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

class IArrowMarkerSymbol(IMarkerSymbol):
    _case_insensitive_ = True
    u'Provides access to members that control the arrow marker symbol.'
    _iid_ = GUID('{88539430-E06E-11D1-B277-0000F878229E}')
    _idlflags_ = ['oleautomation']
IArrowMarkerSymbol._methods_ = [
    COMMETHOD(['propget', helpstring(u'Arrow marker style.')], HRESULT, 'Style',
              ( ['retval', 'out'], POINTER(esriArrowMarkerStyle), 'Style' )),
    COMMETHOD(['propput', helpstring(u'Arrow marker style.')], HRESULT, 'Style',
              ( ['in'], esriArrowMarkerStyle, 'Style' )),
    COMMETHOD(['propget', helpstring(u'Arrow marker length.')], HRESULT, 'Length',
              ( ['retval', 'out'], POINTER(c_double), 'Length' )),
    COMMETHOD(['propput', helpstring(u'Arrow marker length.')], HRESULT, 'Length',
              ( ['in'], c_double, 'Length' )),
    COMMETHOD(['propget', helpstring(u'Arrow marker width.')], HRESULT, 'Width',
              ( ['retval', 'out'], POINTER(c_double), 'Width' )),
    COMMETHOD(['propput', helpstring(u'Arrow marker width.')], HRESULT, 'Width',
              ( ['in'], c_double, 'Width' )),
]
################################################################
## code template for IArrowMarkerSymbol implementation
##class IArrowMarkerSymbol_Impl(object):
##    def _get(self):
##        u'Arrow marker width.'
##        #return Width
##    def _set(self, Width):
##        u'Arrow marker width.'
##    Width = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Arrow marker style.'
##        #return Style
##    def _set(self, Style):
##        u'Arrow marker style.'
##    Style = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Arrow marker length.'
##        #return Length
##    def _set(self, Length):
##        u'Arrow marker length.'
##    Length = property(_get, _set, doc = _set.__doc__)
##

IResizeEnvelopeFeedback2._methods_ = [
    COMMETHOD(['propput', helpstring(u'The edge to rubberband.')], HRESULT, 'ResizeEdge',
              ( ['in'], esriEnvelopeEdge, 'edge' )),
    COMMETHOD(['propget', helpstring(u'The edge to rubberband.')], HRESULT, 'ResizeEdge',
              ( ['retval', 'out'], POINTER(esriEnvelopeEdge), 'edge' )),
    COMMETHOD(['propget', helpstring(u'The constraint on this rubberbander.')], HRESULT, 'Constraint',
              ( ['retval', 'out'], POINTER(esriEnvelopeConstraints), 'constrain' )),
    COMMETHOD(['propput', helpstring(u'The constraint on this rubberbander.')], HRESULT, 'Constraint',
              ( ['in'], esriEnvelopeConstraints, 'constrain' )),
    COMMETHOD(['propget', helpstring(u'The aspect ratio for the custom constraint type.')], HRESULT, 'AspectRatio',
              ( ['retval', 'out'], POINTER(c_double), 'AspectRatio' )),
    COMMETHOD(['propput', helpstring(u'The aspect ratio for the custom constraint type.')], HRESULT, 'AspectRatio',
              ( ['in'], c_double, 'AspectRatio' )),
    COMMETHOD([helpstring(u'Begins a resize feedback of the given shape.')], HRESULT, 'Start',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'envelope' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
    COMMETHOD([helpstring(u'Stops the feedback and returns the shape.')], HRESULT, 'Stop',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry)), 'envelope' )),
]
################################################################
## code template for IResizeEnvelopeFeedback2 implementation
##class IResizeEnvelopeFeedback2_Impl(object):
##    def Start(self, envelope, Point):
##        u'Begins a resize feedback of the given shape.'
##        #return 
##
##    def _get(self):
##        u'The aspect ratio for the custom constraint type.'
##        #return AspectRatio
##    def _set(self, AspectRatio):
##        u'The aspect ratio for the custom constraint type.'
##    AspectRatio = property(_get, _set, doc = _set.__doc__)
##
##    def Stop(self):
##        u'Stops the feedback and returns the shape.'
##        #return envelope
##
##    def _get(self):
##        u'The edge to rubberband.'
##        #return edge
##    def _set(self, edge):
##        u'The edge to rubberband.'
##    ResizeEdge = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The constraint on this rubberbander.'
##        #return constrain
##    def _set(self, constrain):
##        u'The constraint on this rubberbander.'
##    Constraint = property(_get, _set, doc = _set.__doc__)
##


# values for enumeration 'esriBalloonCalloutStyle'
esriBCSRectangle = 0
esriBCSRoundedRectangle = 1
esriBCSOval = 2
esriBalloonCalloutStyle = c_int # enum
class IPieChartSymbol(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to pie chart symbol properties.'
    _iid_ = GUID('{50317364-BD70-11D3-9F79-00C04F6BC709}')
    _idlflags_ = ['oleautomation']
IPieChartSymbol._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if the slices are drawn in a clockwise direction.')], HRESULT, 'Clockwise',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the slices are drawn in a clockwise direction.')], HRESULT, 'Clockwise',
              ( ['in'], VARIANT_BOOL, 'flag' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the outline symbol is drawn.')], HRESULT, 'UseOutline',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the outline symbol is drawn.')], HRESULT, 'UseOutline',
              ( ['in'], VARIANT_BOOL, 'flag' )),
    COMMETHOD(['propget', helpstring(u'The chart outline symbol.')], HRESULT, 'Outline',
              ( ['retval', 'out'], POINTER(POINTER(ILineSymbol)), 'Symbol' )),
    COMMETHOD(['propput', helpstring(u'The chart outline symbol.')], HRESULT, 'Outline',
              ( ['in'], POINTER(ILineSymbol), 'Symbol' )),
]
################################################################
## code template for IPieChartSymbol implementation
##class IPieChartSymbol_Impl(object):
##    def _get(self):
##        u'Indicates if the slices are drawn in a clockwise direction.'
##        #return flag
##    def _set(self, flag):
##        u'Indicates if the slices are drawn in a clockwise direction.'
##    Clockwise = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The chart outline symbol.'
##        #return Symbol
##    def _set(self, Symbol):
##        u'The chart outline symbol.'
##    Outline = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the outline symbol is drawn.'
##        #return flag
##    def _set(self, flag):
##        u'Indicates if the outline symbol is drawn.'
##    UseOutline = property(_get, _set, doc = _set.__doc__)
##

ILineMovePointFeedback._methods_ = [
    COMMETHOD([helpstring(u'Begins a move point feedback of the given shape.  PointIndex is a zero based index into the polyline.')], HRESULT, 'Start',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPolyline), 'polyline' ),
              ( ['in'], c_int, 'pointIndex' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
    COMMETHOD([helpstring(u'Stops the feedback and returns the shape.')], HRESULT, 'Stop',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPolyline)), 'polyline' )),
]
################################################################
## code template for ILineMovePointFeedback implementation
##class ILineMovePointFeedback_Impl(object):
##    def Start(self, polyline, pointIndex, Point):
##        u'Begins a move point feedback of the given shape.  PointIndex is a zero based index into the polyline.'
##        #return 
##
##    def Stop(self):
##        u'Stops the feedback and returns the shape.'
##        #return polyline
##

class ILayerTags(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the layer tags in a multilayer symbol.'
    _iid_ = GUID('{6322D37E-6B0E-4838-A146-EE463024976E}')
    _idlflags_ = ['oleautomation']
ILayerTags._methods_ = [
    COMMETHOD(['propget', helpstring(u'Tags for the layer at the specified index.')], HRESULT, 'LayerTags',
              ( ['in'], c_int, 'layerIndex' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Tags' )),
    COMMETHOD(['propput', helpstring(u'Tags for the layer at the specified index.')], HRESULT, 'LayerTags',
              ( ['in'], c_int, 'layerIndex' ),
              ( ['in'], BSTR, 'Tags' )),
]
################################################################
## code template for ILayerTags implementation
##class ILayerTags_Impl(object):
##    def _get(self, layerIndex):
##        u'Tags for the layer at the specified index.'
##        #return Tags
##    def _set(self, layerIndex, Tags):
##        u'Tags for the layer at the specified index.'
##    LayerTags = property(_get, _set, doc = _set.__doc__)
##

ITextPath2._methods_ = [
    COMMETHOD([helpstring(u'Set up items needed by text path, including character metrics information.')], HRESULT, 'SetupEx',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDC' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ITransformation), 'Transformation' ),
              ( ['in'], POINTER(ITextSymbol), 'textSym' ),
              ( ['in'], BSTR, 'Text' ),
              ( ['in'], VARIANT, 'charMetrics' )),
]
################################################################
## code template for ITextPath2 implementation
##class ITextPath2_Impl(object):
##    def SetupEx(self, hDC, Transformation, textSym, Text, charMetrics):
##        u'Set up items needed by text path, including character metrics information.'
##        #return 
##

class GeometricEffectArrow(CoClass):
    u'Constructs an arrow of a given line.'
    _reg_clsid_ = GUID('{2B195147-95ED-4863-AEBC-B876E1A4766C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
GeometricEffectArrow._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGeometricEffect, IGraphicAttributes, IGraphicAttributes2, IEditInteraction, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

INewArcFeedback._methods_ = [
    COMMETHOD([helpstring(u'Start the feedback, for an arc with the specified from point.')], HRESULT, 'Start',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
    COMMETHOD([helpstring(u'Start the feedback, fo an ar with the specified from point & tangent direction.')], HRESULT, 'StartTangent',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' ),
              ( [], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISegment), 'tangent' )),
    COMMETHOD([helpstring(u'Fix the to point of the arc.')], HRESULT, 'SetEndpoint',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
    COMMETHOD([helpstring(u'Fix a midpoint of the arc.')], HRESULT, 'SetMidpoint',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
    COMMETHOD([helpstring(u'Switch the feedback to the next solution.')], HRESULT, 'Next',
              ( ['in'], VARIANT_BOOL, 'forward' )),
    COMMETHOD(['propget', helpstring(u'The current radius of the arc.')], HRESULT, 'Radius',
              ( ['retval', 'out'], POINTER(c_double), 'Radius' )),
    COMMETHOD(['propput', helpstring(u'The current radius of the arc.')], HRESULT, 'Radius',
              ( ['in'], c_double, 'Radius' )),
    COMMETHOD(['propget', helpstring(u'The arc as it is currently being drawn.')], HRESULT, 'Arc',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ICircularArc)), 'Arc' )),
    COMMETHOD([helpstring(u'Stop the feedback, returning the final arc.')], HRESULT, 'Stop',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ICircularArc)), 'Arc' )),
    COMMETHOD([helpstring(u'Abort the feedback.')], HRESULT, 'Abort'),
]
################################################################
## code template for INewArcFeedback implementation
##class INewArcFeedback_Impl(object):
##    def SetEndpoint(self, Point):
##        u'Fix the to point of the arc.'
##        #return 
##
##    @property
##    def Arc(self):
##        u'The arc as it is currently being drawn.'
##        #return Arc
##
##    def Abort(self):
##        u'Abort the feedback.'
##        #return 
##
##    def Stop(self, Point):
##        u'Stop the feedback, returning the final arc.'
##        #return Arc
##
##    def Next(self, forward):
##        u'Switch the feedback to the next solution.'
##        #return 
##
##    def Start(self, Point):
##        u'Start the feedback, for an arc with the specified from point.'
##        #return 
##
##    def StartTangent(self, Point, tangent):
##        u'Start the feedback, fo an ar with the specified from point & tangent direction.'
##        #return 
##
##    def _get(self):
##        u'The current radius of the arc.'
##        #return Radius
##    def _set(self, Radius):
##        u'The current radius of the arc.'
##    Radius = property(_get, _set, doc = _set.__doc__)
##
##    def SetMidpoint(self, Point):
##        u'Fix a midpoint of the arc.'
##        #return 
##


# values for enumeration 'esriDynamicSymbolRotationAlignment'
esriDSRAScreen = 0
esriDSRANorth = 1
esriDynamicSymbolRotationAlignment = c_int # enum
ITemplate._methods_ = [
    COMMETHOD([helpstring(u'Set up items needed by template.')], HRESULT, 'Setup',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDC' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ITransformation), 'Transformation' ),
              ( ['in'], POINTER(ILineSymbol), 'lineSym' )),
    COMMETHOD(['propget', helpstring(u'The number of pattern elements.')], HRESULT, 'PatternElementCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD([helpstring(u'Gets pattern element properties for a given index.')], HRESULT, 'GetPatternElement',
              ( ['in'], c_int, 'index' ),
              ( ['out'], POINTER(c_double), 'mark' ),
              ( ['out'], POINTER(c_double), 'Gap' )),
    COMMETHOD([helpstring(u'Adds a pattern element.')], HRESULT, 'AddPatternElement',
              ( ['in'], c_double, 'mark' ),
              ( ['in'], c_double, 'Gap' )),
    COMMETHOD([helpstring(u'Removes the pattern element at the given index.')], HRESULT, 'DeletePatternElement',
              ( ['in'], c_int, 'index' )),
    COMMETHOD([helpstring(u'Moves a pattern element.')], HRESULT, 'MovePatternElement',
              ( ['in'], c_int, 'fromIndex' ),
              ( ['in'], c_int, 'toIndex' )),
    COMMETHOD([helpstring(u'Clears all pattern elements.')], HRESULT, 'ClearPatternElements'),
    COMMETHOD(['propget', helpstring(u'The interval.')], HRESULT, 'Interval',
              ( ['retval', 'out'], POINTER(c_double), 'Interval' )),
    COMMETHOD(['propput', helpstring(u'The interval.')], HRESULT, 'Interval',
              ( ['in'], c_double, 'Interval' )),
    COMMETHOD(['propget', helpstring(u'The pattern geometry.')], HRESULT, 'Geometry',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry)), 'ppGeometry' )),
    COMMETHOD(['propputref', helpstring(u'The pattern geometry.')], HRESULT, 'Geometry',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'ppGeometry' )),
    COMMETHOD([helpstring(u'Queries for the next point in the pattern.')], HRESULT, 'QueryNextPoint',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'pPoint' ),
              ( ['in'], POINTER(c_double), 'pAngle' )),
    COMMETHOD([helpstring(u'Queries for the next line in the pattern.')], HRESULT, 'QueryNextLine',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'pGeometry' )),
    COMMETHOD([helpstring(u'Resets the enumerator.')], HRESULT, 'Reset'),
]
################################################################
## code template for ITemplate implementation
##class ITemplate_Impl(object):
##    @property
##    def PatternElementCount(self):
##        u'The number of pattern elements.'
##        #return Count
##
##    def Reset(self):
##        u'Resets the enumerator.'
##        #return 
##
##    def MovePatternElement(self, fromIndex, toIndex):
##        u'Moves a pattern element.'
##        #return 
##
##    def DeletePatternElement(self, index):
##        u'Removes the pattern element at the given index.'
##        #return 
##
##    def Geometry(self, ppGeometry):
##        u'The pattern geometry.'
##        #return 
##
##    def Setup(self, hDC, Transformation, lineSym):
##        u'Set up items needed by template.'
##        #return 
##
##    def _get(self):
##        u'The interval.'
##        #return Interval
##    def _set(self, Interval):
##        u'The interval.'
##    Interval = property(_get, _set, doc = _set.__doc__)
##
##    def QueryNextPoint(self, pPoint, pAngle):
##        u'Queries for the next point in the pattern.'
##        #return 
##
##    def QueryNextLine(self, pGeometry):
##        u'Queries for the next line in the pattern.'
##        #return 
##
##    def GetPatternElement(self, index):
##        u'Gets pattern element properties for a given index.'
##        #return mark, Gap
##
##    def ClearPatternElements(self):
##        u'Clears all pattern elements.'
##        #return 
##
##    def AddPatternElement(self, mark, Gap):
##        u'Adds a pattern element.'
##        #return 
##

class IDynamicCompoundMarker(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to dynamic compound marker.'
    _iid_ = GUID('{F6A79F2F-A2AF-464D-A1FE-2276490FEC88}')
    _idlflags_ = ['oleautomation']
IDynamicCompoundMarker._methods_ = [
    COMMETHOD([helpstring(u'The offset of the text from the marker in pixels.')], HRESULT, 'GetMarkerToTextOffset',
              ( ['in', 'out'], POINTER(c_float), 'XOffset' ),
              ( ['in', 'out'], POINTER(c_float), 'YOffset' )),
    COMMETHOD([helpstring(u'The offset of the text from the marker in pixels.')], HRESULT, 'SetMarkerToTextOffset',
              ( ['in'], c_float, 'XOffset' ),
              ( ['in'], c_float, 'YOffset' )),
    COMMETHOD([helpstring(u'Draws specified point on the dynamic display with one string above it.')], HRESULT, 'DrawCompoundMarker1',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' ),
              ( ['in'], BSTR, 'textTop' )),
    COMMETHOD([helpstring(u'Draws specified point on the dynamic display with a string above and below.')], HRESULT, 'DrawCompoundMarker2',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' ),
              ( ['in'], BSTR, 'textTop' ),
              ( ['in'], BSTR, 'textBottom' )),
    COMMETHOD([helpstring(u'Draws specified point on the dynamic display with a text string on each side of the marker (top, bottom, left and right).')], HRESULT, 'DrawCompoundMarker4',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' ),
              ( ['in'], BSTR, 'textTop' ),
              ( ['in'], BSTR, 'textBottom' ),
              ( ['in'], BSTR, 'textLeft' ),
              ( ['in'], BSTR, 'textRight' )),
    COMMETHOD([helpstring(u'Draws specified point on the dynamic display with one string on the top of the marker, one string on the bottom and two strings on each side of the marker (left and right).')], HRESULT, 'DrawCompoundMarker6',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' ),
              ( ['in'], BSTR, 'textTop' ),
              ( ['in'], BSTR, 'textBottom' ),
              ( ['in'], BSTR, 'textLeft1' ),
              ( ['in'], BSTR, 'textLeft2' ),
              ( ['in'], BSTR, 'textRight1' ),
              ( ['in'], BSTR, 'textRight2' )),
    COMMETHOD([helpstring(u'Draws specified point on the dynamic display with one string on the top of the marker, one string on the bottom and three strings on each side of the marker (left and right).')], HRESULT, 'DrawCompoundMarker8',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' ),
              ( ['in'], BSTR, 'textTop' ),
              ( ['in'], BSTR, 'textBottom' ),
              ( ['in'], BSTR, 'textLeft1' ),
              ( ['in'], BSTR, 'textLeft2' ),
              ( ['in'], BSTR, 'textLeft3' ),
              ( ['in'], BSTR, 'textRight1' ),
              ( ['in'], BSTR, 'textRight2' ),
              ( ['in'], BSTR, 'textRight3' )),
    COMMETHOD([helpstring(u'Draws specified point on the dynamic display with one string on the top of the marker, one string on the bottom and four strings on each side of the marker (left and right).')], HRESULT, 'DrawCompoundMarker10',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' ),
              ( ['in'], BSTR, 'textTop' ),
              ( ['in'], BSTR, 'textBottom' ),
              ( ['in'], BSTR, 'textLeft1' ),
              ( ['in'], BSTR, 'textLeft2' ),
              ( ['in'], BSTR, 'textLeft3' ),
              ( ['in'], BSTR, 'textLeft4' ),
              ( ['in'], BSTR, 'textRight1' ),
              ( ['in'], BSTR, 'textRight2' ),
              ( ['in'], BSTR, 'textRight3' ),
              ( ['in'], BSTR, 'textRight4' )),
]
################################################################
## code template for IDynamicCompoundMarker implementation
##class IDynamicCompoundMarker_Impl(object):
##    def DrawCompoundMarker6(self, Point, textTop, textBottom, textLeft1, textLeft2, textRight1, textRight2):
##        u'Draws specified point on the dynamic display with one string on the top of the marker, one string on the bottom and two strings on each side of the marker (left and right).'
##        #return 
##
##    def DrawCompoundMarker4(self, Point, textTop, textBottom, textLeft, textRight):
##        u'Draws specified point on the dynamic display with a text string on each side of the marker (top, bottom, left and right).'
##        #return 
##
##    def DrawCompoundMarker2(self, Point, textTop, textBottom):
##        u'Draws specified point on the dynamic display with a string above and below.'
##        #return 
##
##    def DrawCompoundMarker1(self, Point, textTop):
##        u'Draws specified point on the dynamic display with one string above it.'
##        #return 
##
##    def GetMarkerToTextOffset(self):
##        u'The offset of the text from the marker in pixels.'
##        #return XOffset, YOffset
##
##    def SetMarkerToTextOffset(self, XOffset, YOffset):
##        u'The offset of the text from the marker in pixels.'
##        #return 
##
##    def DrawCompoundMarker8(self, Point, textTop, textBottom, textLeft1, textLeft2, textLeft3, textRight1, textRight2, textRight3):
##        u'Draws specified point on the dynamic display with one string on the top of the marker, one string on the bottom and three strings on each side of the marker (left and right).'
##        #return 
##
##    def DrawCompoundMarker10(self, Point, textTop, textBottom, textLeft1, textLeft2, textLeft3, textLeft4, textRight1, textRight2, textRight3, textRight4):
##        u'Draws specified point on the dynamic display with one string on the top of the marker, one string on the bottom and four strings on each side of the marker (left and right).'
##        #return 
##

IRepresentationGraphics._methods_ = [
    COMMETHOD([helpstring(u'Resets the enumeration of components in a representation graphic.')], HRESULT, 'Reset'),
    COMMETHOD([helpstring(u'Retrieves the next component in a representation graphic.')], HRESULT, 'Next',
              ( ['out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry)), 'Geometry' ),
              ( ['out'], POINTER(POINTER(IRepresentationRule)), 'repRule' )),
    COMMETHOD([helpstring(u'Adds a new component in a representation graphic.')], HRESULT, 'Add',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'Geometry' ),
              ( ['in'], POINTER(IRepresentationRule), 'repRule' )),
    COMMETHOD([helpstring(u'Removes a component in a representation graphic.')], HRESULT, 'Remove',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'Geometry' ),
              ( ['in'], POINTER(IRepresentationRule), 'repRule' )),
    COMMETHOD([helpstring(u'Removes all components in a representation graphic.')], HRESULT, 'RemoveAll'),
    COMMETHOD([helpstring(u'Resets the geometry enumeration in a representation graphic.')], HRESULT, 'ResetGeometry'),
    COMMETHOD([helpstring(u'Accesses the next geometry in a representation graphic.')], HRESULT, 'NextGeometry',
              ( ['out'], POINTER(c_int), 'ID' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry)), 'Geometry' )),
    COMMETHOD([helpstring(u'Changes a geometry in a representation graphic.')], HRESULT, 'ChangeGeometry',
              ( ['in'], c_int, 'ID' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'Geometry' )),
]
################################################################
## code template for IRepresentationGraphics implementation
##class IRepresentationGraphics_Impl(object):
##    def Reset(self):
##        u'Resets the enumeration of components in a representation graphic.'
##        #return 
##
##    def ResetGeometry(self):
##        u'Resets the geometry enumeration in a representation graphic.'
##        #return 
##
##    def NextGeometry(self):
##        u'Accesses the next geometry in a representation graphic.'
##        #return ID, Geometry
##
##    def ChangeGeometry(self, ID, Geometry):
##        u'Changes a geometry in a representation graphic.'
##        #return 
##
##    def Remove(self, Geometry, repRule):
##        u'Removes a component in a representation graphic.'
##        #return 
##
##    def Next(self):
##        u'Retrieves the next component in a representation graphic.'
##        #return Geometry, repRule
##
##    def RemoveAll(self):
##        u'Removes all components in a representation graphic.'
##        #return 
##
##    def Add(self, Geometry, repRule):
##        u'Adds a new component in a representation graphic.'
##        #return 
##

class IMarkerMask(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that retreive marker mask geometry.'
    _iid_ = GUID('{572D1037-7815-11D3-9F6A-00C04F6BC8DD}')
    _idlflags_ = ['oleautomation']
IMarkerMask._methods_ = [
    COMMETHOD([helpstring(u'Returns the mask geometry for the marker.')], HRESULT, 'QueryMarkerMask',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDC' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ITransformation), 'transform' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'Geometry' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPolygon), 'boundary' )),
]
################################################################
## code template for IMarkerMask implementation
##class IMarkerMask_Impl(object):
##    def QueryMarkerMask(self, hDC, transform, Geometry, boundary):
##        u'Returns the mask geometry for the marker.'
##        #return 
##

class RepresentationGraphics(CoClass):
    u'An object defining a free representation.'
    _reg_clsid_ = GUID('{97957B5F-EF1A-4A18-9AA9-E2CD1C17332A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
RepresentationGraphics._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRepresentationGraphics, IGraphicsOutline, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

class IMultiLayerMarkerSymbol(IMarkerSymbol):
    _case_insensitive_ = True
    u'Provides access to members that control the multiLayer marker symbol.'
    _iid_ = GUID('{7914E5E4-C892-11D0-8BB6-080009EE4E41}')
    _idlflags_ = ['oleautomation']
IMultiLayerMarkerSymbol._methods_ = [
    COMMETHOD(['propget', helpstring(u'Symbol layer count.')], HRESULT, 'LayerCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Marker symbol per index position.')], HRESULT, 'Layer',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IMarkerSymbol)), 'markerLayer' )),
    COMMETHOD([helpstring(u'Add marker symbol layer.')], HRESULT, 'AddLayer',
              ( ['in'], POINTER(IMarkerSymbol), 'markerLayer' )),
    COMMETHOD([helpstring(u'Delete marker symbol layer.')], HRESULT, 'DeleteLayer',
              ( ['in'], POINTER(IMarkerSymbol), 'markerLayer' )),
    COMMETHOD([helpstring(u'Change layer index position.')], HRESULT, 'MoveLayer',
              ( ['in'], POINTER(IMarkerSymbol), 'markerLayer' ),
              ( ['in'], c_int, 'toIndex' )),
    COMMETHOD([helpstring(u'Remove all symbol layers.')], HRESULT, 'ClearLayers'),
    COMMETHOD([helpstring(u'Draw a symbol layer.')], HRESULT, 'DrawLayer',
              ( ['in'], c_int, 'index' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'Geometry' )),
]
################################################################
## code template for IMultiLayerMarkerSymbol implementation
##class IMultiLayerMarkerSymbol_Impl(object):
##    @property
##    def Layer(self, index):
##        u'Marker symbol per index position.'
##        #return markerLayer
##
##    @property
##    def LayerCount(self):
##        u'Symbol layer count.'
##        #return Count
##
##    def DeleteLayer(self, markerLayer):
##        u'Delete marker symbol layer.'
##        #return 
##
##    def DrawLayer(self, index, Geometry):
##        u'Draw a symbol layer.'
##        #return 
##
##    def MoveLayer(self, markerLayer, toIndex):
##        u'Change layer index position.'
##        #return 
##
##    def ClearLayers(self):
##        u'Remove all symbol layers.'
##        #return 
##
##    def AddLayer(self, markerLayer):
##        u'Add marker symbol layer.'
##        #return 
##

class ISimpleFillSymbol(IFillSymbol):
    _case_insensitive_ = True
    u'Provides access to members that control the simple fill symbol.'
    _iid_ = GUID('{A9360292-5828-11D0-98BF-00805F7CED21}')
    _idlflags_ = ['oleautomation']
IFillSymbol._methods_ = [
    COMMETHOD(['propget', helpstring(u'Fill color.')], HRESULT, 'Color',
              ( ['retval', 'out'], POINTER(POINTER(IColor)), 'Color' )),
    COMMETHOD(['propput', helpstring(u'Fill color.')], HRESULT, 'Color',
              ( ['in'], POINTER(IColor), 'Color' )),
    COMMETHOD(['propget', helpstring(u'Line symbol of fill outline.')], HRESULT, 'Outline',
              ( ['retval', 'out'], POINTER(POINTER(ILineSymbol)), 'outlineSym' )),
    COMMETHOD(['propput', helpstring(u'Line symbol of fill outline.')], HRESULT, 'Outline',
              ( ['in'], POINTER(ILineSymbol), 'outlineSym' )),
]
################################################################
## code template for IFillSymbol implementation
##class IFillSymbol_Impl(object):
##    def _get(self):
##        u'Fill color.'
##        #return Color
##    def _set(self, Color):
##        u'Fill color.'
##    Color = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Line symbol of fill outline.'
##        #return outlineSym
##    def _set(self, outlineSym):
##        u'Line symbol of fill outline.'
##    Outline = property(_get, _set, doc = _set.__doc__)
##

ISimpleFillSymbol._methods_ = [
    COMMETHOD(['propget', helpstring(u'Fill style.')], HRESULT, 'Style',
              ( ['retval', 'out'], POINTER(esriSimpleFillStyle), 'Style' )),
    COMMETHOD(['propput', helpstring(u'Fill style.')], HRESULT, 'Style',
              ( ['in'], esriSimpleFillStyle, 'Style' )),
]
################################################################
## code template for ISimpleFillSymbol implementation
##class ISimpleFillSymbol_Impl(object):
##    def _get(self):
##        u'Fill style.'
##        #return Style
##    def _set(self, Style):
##        u'Fill style.'
##    Style = property(_get, _set, doc = _set.__doc__)
##

class ICartographicLineSymbol(ILineSymbol):
    _case_insensitive_ = True
    u'Provides access to members that control the cartographic line symbol.'
    _iid_ = GUID('{B04BC359-C36E-11D0-BFA1-0080C7E24280}')
    _idlflags_ = ['oleautomation']
ICartographicLineSymbol._methods_ = [
    COMMETHOD(['propget', helpstring(u'Line end cap style.')], HRESULT, 'Cap',
              ( ['retval', 'out'], POINTER(esriLineCapStyle), 'capStyle' )),
    COMMETHOD(['propput', helpstring(u'Line end cap style.')], HRESULT, 'Cap',
              ( ['in'], esriLineCapStyle, 'capStyle' )),
    COMMETHOD(['propget', helpstring(u'Line join style.')], HRESULT, 'Join',
              ( ['retval', 'out'], POINTER(esriLineJoinStyle), 'joinStyle' )),
    COMMETHOD(['propput', helpstring(u'Line join style.')], HRESULT, 'Join',
              ( ['in'], esriLineJoinStyle, 'joinStyle' )),
    COMMETHOD(['propget', helpstring(u'Size threshold for showing mitered line joins.')], HRESULT, 'MiterLimit',
              ( ['retval', 'out'], POINTER(c_double), 'MiterLimit' )),
    COMMETHOD(['propput', helpstring(u'Size threshold for showing mitered line joins.')], HRESULT, 'MiterLimit',
              ( ['in'], c_double, 'MiterLimit' )),
]
################################################################
## code template for ICartographicLineSymbol implementation
##class ICartographicLineSymbol_Impl(object):
##    def _get(self):
##        u'Line end cap style.'
##        #return capStyle
##    def _set(self, capStyle):
##        u'Line end cap style.'
##    Cap = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Line join style.'
##        #return joinStyle
##    def _set(self, joinStyle):
##        u'Line join style.'
##    Join = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Size threshold for showing mitered line joins.'
##        #return MiterLimit
##    def _set(self, MiterLimit):
##        u'Size threshold for showing mitered line joins.'
##    MiterLimit = property(_get, _set, doc = _set.__doc__)
##

IStretchLineFeedback._methods_ = [
    COMMETHOD([helpstring(u'Begins a move of the given shape (a polyline).')], HRESULT, 'Start',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPolyline), 'polyline' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
    COMMETHOD([helpstring(u'Stops the feedback and returns the polyline.')], HRESULT, 'Stop',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPolyline)), 'polyline' )),
    COMMETHOD(['propput', helpstring(u'The anchor point of the curve.')], HRESULT, 'Anchor',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'rhs' )),
]
################################################################
## code template for IStretchLineFeedback implementation
##class IStretchLineFeedback_Impl(object):
##    def Start(self, polyline, Point):
##        u'Begins a move of the given shape (a polyline).'
##        #return 
##
##    def Stop(self):
##        u'Stops the feedback and returns the polyline.'
##        #return polyline
##
##    def _set(self, rhs):
##        u'The anchor point of the curve.'
##    Anchor = property(fset = _set, doc = _set.__doc__)
##

IMovePolygonFeedback._methods_ = [
    COMMETHOD([helpstring(u'Begins a move feedback of the given shape.')], HRESULT, 'Start',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPolygon), 'polygon' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
    COMMETHOD([helpstring(u'Stops the feedback and returns the shape.')], HRESULT, 'Stop',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPolygon)), 'polygon' )),
]
################################################################
## code template for IMovePolygonFeedback implementation
##class IMovePolygonFeedback_Impl(object):
##    def Start(self, polygon, Point):
##        u'Begins a move feedback of the given shape.'
##        #return 
##
##    def Stop(self):
##        u'Stops the feedback and returns the shape.'
##        #return polygon
##

class IHashLineSymbol(ILineSymbol):
    _case_insensitive_ = True
    u'Provides access to members that control the hash line symbol.'
    _iid_ = GUID('{B04BC35A-C36E-11D0-BFA1-0080C7E24280}')
    _idlflags_ = ['oleautomation']
IHashLineSymbol._methods_ = [
    COMMETHOD(['propget', helpstring(u'Line symbol used for hash pattern.')], HRESULT, 'HashSymbol',
              ( ['retval', 'out'], POINTER(POINTER(ILineSymbol)), 'HashSymbol' )),
    COMMETHOD(['propputref', helpstring(u'Line symbol used for hash pattern.')], HRESULT, 'HashSymbol',
              ( ['in'], POINTER(ILineSymbol), 'HashSymbol' )),
    COMMETHOD(['propget', helpstring(u'Hash line angle.')], HRESULT, 'Angle',
              ( ['retval', 'out'], POINTER(c_double), 'Angle' )),
    COMMETHOD(['propput', helpstring(u'Hash line angle.')], HRESULT, 'Angle',
              ( ['in'], c_double, 'Angle' )),
]
################################################################
## code template for IHashLineSymbol implementation
##class IHashLineSymbol_Impl(object):
##    def _get(self):
##        u'Hash line angle.'
##        #return Angle
##    def _set(self, Angle):
##        u'Hash line angle.'
##    Angle = property(_get, _set, doc = _set.__doc__)
##
##    def HashSymbol(self, HashSymbol):
##        u'Line symbol used for hash pattern.'
##        #return 
##

class IPictureFillSymbol(IFillSymbol):
    _case_insensitive_ = True
    u'Provides access to members that control the picture fill symbol.'
    _iid_ = GUID('{D842B081-330C-11D2-9168-0000F87808EE}')
    _idlflags_ = ['oleautomation']
IPictureFillSymbol._methods_ = [
    COMMETHOD(['propget', helpstring(u'Picture used for fill.')], HRESULT, 'Picture',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IPictureDisp)), 'pictureDisp' )),
    COMMETHOD(['propputref', helpstring(u'Picture used for fill.')], HRESULT, 'Picture',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IPictureDisp), 'pictureDisp' )),
    COMMETHOD(['propget', helpstring(u'Fill background color.')], HRESULT, 'BackgroundColor',
              ( ['retval', 'out'], POINTER(POINTER(IColor)), 'Color' )),
    COMMETHOD(['propput', helpstring(u'Fill background color.')], HRESULT, 'BackgroundColor',
              ( ['in'], POINTER(IColor), 'Color' )),
    COMMETHOD(['propput', helpstring(u'Color within bitmap indicating transparency.')], HRESULT, 'BitmapTransparencyColor',
              ( ['in'], POINTER(IColor), 'Color' )),
    COMMETHOD(['propget', helpstring(u'Color within bitmap indicating transparency.')], HRESULT, 'BitmapTransparencyColor',
              ( ['retval', 'out'], POINTER(POINTER(IColor)), 'Color' )),
    COMMETHOD(['propget', helpstring(u'Angle of picture fill.')], HRESULT, 'Angle',
              ( ['retval', 'out'], POINTER(c_double), 'Angle' )),
    COMMETHOD(['propput', helpstring(u'Angle of picture fill.')], HRESULT, 'Angle',
              ( ['in'], c_double, 'Angle' )),
    COMMETHOD(['propget', helpstring(u'Scale of picture fill along X-axis.')], HRESULT, 'XScale',
              ( ['retval', 'out'], POINTER(c_double), 'XScale' )),
    COMMETHOD(['propput', helpstring(u'Scale of picture fill along X-axis.')], HRESULT, 'XScale',
              ( ['in'], c_double, 'XScale' )),
    COMMETHOD(['propget', helpstring(u'Scale of picture fill along Y-axis.')], HRESULT, 'YScale',
              ( ['retval', 'out'], POINTER(c_double), 'YScale' )),
    COMMETHOD(['propput', helpstring(u'Scale of picture fill along Y-axis.')], HRESULT, 'YScale',
              ( ['in'], c_double, 'YScale' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the foreground and background colors are swapped on 1 Bit Images Only.')], HRESULT, 'SwapForeGroundBackGroundColor',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'swap' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the foreground and background colors are swapped on 1 Bit Images Only.')], HRESULT, 'SwapForeGroundBackGroundColor',
              ( ['in'], VARIANT_BOOL, 'swap' )),
    COMMETHOD([helpstring(u'Create fill symbol from picture file.')], HRESULT, 'CreateFillSymbolFromFile',
              ( ['in'], esriIPictureType, 'Type' ),
              ( ['in'], BSTR, 'fileName' )),
]
################################################################
## code template for IPictureFillSymbol implementation
##class IPictureFillSymbol_Impl(object):
##    def Picture(self, pictureDisp):
##        u'Picture used for fill.'
##        #return 
##
##    def _get(self):
##        u'Indicates if the foreground and background colors are swapped on 1 Bit Images Only.'
##        #return swap
##    def _set(self, swap):
##        u'Indicates if the foreground and background colors are swapped on 1 Bit Images Only.'
##    SwapForeGroundBackGroundColor = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Angle of picture fill.'
##        #return Angle
##    def _set(self, Angle):
##        u'Angle of picture fill.'
##    Angle = property(_get, _set, doc = _set.__doc__)
##
##    def CreateFillSymbolFromFile(self, Type, fileName):
##        u'Create fill symbol from picture file.'
##        #return 
##
##    def _get(self):
##        u'Scale of picture fill along Y-axis.'
##        #return YScale
##    def _set(self, YScale):
##        u'Scale of picture fill along Y-axis.'
##    YScale = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Color within bitmap indicating transparency.'
##        #return Color
##    def _set(self, Color):
##        u'Color within bitmap indicating transparency.'
##    BitmapTransparencyColor = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Fill background color.'
##        #return Color
##    def _set(self, Color):
##        u'Fill background color.'
##    BackgroundColor = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Scale of picture fill along X-axis.'
##        #return XScale
##    def _set(self, XScale):
##        u'Scale of picture fill along X-axis.'
##    XScale = property(_get, _set, doc = _set.__doc__)
##

class IStyleGalleryStorageAdmin(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Private access to members that manage the files used in the Style Gallery.'
    _iid_ = GUID('{8E195081-82A9-468E-A7F9-977CCDFE11B6}')
    _idlflags_ = []
IStyleGalleryStorageAdmin._methods_ = [
    COMMETHOD([helpstring(u'Adds a file to the Style Gallery with read-only access.')], HRESULT, 'AddFileReadOnly',
              ( ['in'], BSTR, 'Name' )),
]
################################################################
## code template for IStyleGalleryStorageAdmin implementation
##class IStyleGalleryStorageAdmin_Impl(object):
##    def AddFileReadOnly(self, Name):
##        u'Adds a file to the Style Gallery with read-only access.'
##        #return 
##

class IMultiLayerFillSymbol(IFillSymbol):
    _case_insensitive_ = True
    u'Provides access to members that control the multilayer fill symbol.'
    _iid_ = GUID('{7914E5EC-C892-11D0-8BB6-080009EE4E41}')
    _idlflags_ = ['oleautomation']
IMultiLayerFillSymbol._methods_ = [
    COMMETHOD(['propget', helpstring(u'Symbol layer count.')], HRESULT, 'LayerCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Fill symbol per layer position.')], HRESULT, 'Layer',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IFillSymbol)), 'fillLayer' )),
    COMMETHOD([helpstring(u'Add fill symbol layer.')], HRESULT, 'AddLayer',
              ( ['in'], POINTER(IFillSymbol), 'fillLayer' )),
    COMMETHOD([helpstring(u'Delete fill symbol layer.')], HRESULT, 'DeleteLayer',
              ( ['in'], POINTER(IFillSymbol), 'fillLayer' )),
    COMMETHOD([helpstring(u'Change symbol layer position index.')], HRESULT, 'MoveLayer',
              ( ['in'], POINTER(IFillSymbol), 'fillLayer' ),
              ( ['in'], c_int, 'toIndex' )),
    COMMETHOD([helpstring(u'Remove all symbol layers.')], HRESULT, 'ClearLayers'),
    COMMETHOD([helpstring(u'Draw a symbol layer.')], HRESULT, 'DrawLayer',
              ( ['in'], c_int, 'index' ),
              ( [], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'Geometry' )),
]
################################################################
## code template for IMultiLayerFillSymbol implementation
##class IMultiLayerFillSymbol_Impl(object):
##    @property
##    def Layer(self, index):
##        u'Fill symbol per layer position.'
##        #return fillLayer
##
##    @property
##    def LayerCount(self):
##        u'Symbol layer count.'
##        #return Count
##
##    def DeleteLayer(self, fillLayer):
##        u'Delete fill symbol layer.'
##        #return 
##
##    def DrawLayer(self, index, Geometry):
##        u'Draw a symbol layer.'
##        #return 
##
##    def MoveLayer(self, fillLayer, toIndex):
##        u'Change symbol layer position index.'
##        #return 
##
##    def ClearLayers(self):
##        u'Remove all symbol layers.'
##        #return 
##
##    def AddLayer(self, fillLayer):
##        u'Add fill symbol layer.'
##        #return 
##

class IReferenceFillSymbol(IFillSymbol):
    _case_insensitive_ = True
    u'Provides access to members that control the reference fill symbol.'
    _iid_ = GUID('{7914E5EA-C892-11D0-8BB6-080009EE4E41}')
    _idlflags_ = ['oleautomation']
IReferenceFillSymbol._methods_ = [
    COMMETHOD(['propget', helpstring(u'Symbol set name.')], HRESULT, 'SymbolSetName',
              ( ['retval', 'out'], POINTER(BSTR), 'setName' )),
    COMMETHOD(['propput', helpstring(u'Symbol set name.')], HRESULT, 'SymbolSetName',
              ( ['in'], BSTR, 'setName' )),
    COMMETHOD(['propget', helpstring(u'Symbol name.')], HRESULT, 'SymbolName',
              ( ['retval', 'out'], POINTER(BSTR), 'symName' )),
    COMMETHOD(['propput', helpstring(u'Symbol name.')], HRESULT, 'SymbolName',
              ( ['in'], BSTR, 'symName' )),
]
################################################################
## code template for IReferenceFillSymbol implementation
##class IReferenceFillSymbol_Impl(object):
##    def _get(self):
##        u'Symbol set name.'
##        #return setName
##    def _set(self, setName):
##        u'Symbol set name.'
##    SymbolSetName = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Symbol name.'
##        #return symName
##    def _set(self, symName):
##        u'Symbol name.'
##    SymbolName = property(_get, _set, doc = _set.__doc__)
##

IPolygonMovePointFeedback._methods_ = [
    COMMETHOD([helpstring(u'Begins a move point feedback of the given shape.  PointIndex is a zero based index into the polygon.')], HRESULT, 'Start',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPolygon), 'polygon' ),
              ( ['in'], c_int, 'pointIndex' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
    COMMETHOD([helpstring(u'Stops the feedback and returns the shape.')], HRESULT, 'Stop',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPolygon)), 'polygon' )),
]
################################################################
## code template for IPolygonMovePointFeedback implementation
##class IPolygonMovePointFeedback_Impl(object):
##    def Start(self, polygon, pointIndex, Point):
##        u'Begins a move point feedback of the given shape.  PointIndex is a zero based index into the polygon.'
##        #return 
##
##    def Stop(self):
##        u'Stops the feedback and returns the shape.'
##        #return polygon
##

class ICharacterMarkerSymbol(IMarkerSymbol):
    _case_insensitive_ = True
    u'Provides access to members that control the character marker symbol.'
    _iid_ = GUID('{7914E5E7-C892-11D0-8BB6-080009EE4E41}')
    _idlflags_ = ['oleautomation']
ICharacterMarkerSymbol._methods_ = [
    COMMETHOD(['propget', helpstring(u'Font used for character symbol.')], HRESULT, 'Font',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IFontDisp)), 'fontDisp' )),
    COMMETHOD(['propput', helpstring(u'Font used for character symbol.')], HRESULT, 'Font',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IFontDisp), 'fontDisp' )),
    COMMETHOD(['propget', helpstring(u'Character index within font.')], HRESULT, 'CharacterIndex',
              ( ['retval', 'out'], POINTER(c_int), 'charIndex' )),
    COMMETHOD(['propput', helpstring(u'Character index within font.')], HRESULT, 'CharacterIndex',
              ( ['in'], c_int, 'charIndex' )),
]
################################################################
## code template for ICharacterMarkerSymbol implementation
##class ICharacterMarkerSymbol_Impl(object):
##    def _get(self):
##        u'Character index within font.'
##        #return charIndex
##    def _set(self, charIndex):
##        u'Character index within font.'
##    CharacterIndex = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Font used for character symbol.'
##        #return fontDisp
##    def _set(self, fontDisp):
##        u'Font used for character symbol.'
##    Font = property(_get, _set, doc = _set.__doc__)
##

class IDynamicSymbolProperties(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to dynamic symbol properties.'
    _iid_ = GUID('{23783EDA-6341-4E81-B129-4D4FABD94154}')
    _idlflags_ = ['oleautomation']
IDynamicSymbolProperties._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates the dynamic glyph for the specified dynamic symbol.')], HRESULT, 'DynamicGlyph',
              ( ['in'], esriDynamicSymbolType, 'dynamicSymbolType' ),
              ( ['retval', 'out'], POINTER(POINTER(IDynamicGlyph)), 'DynamicGlyph' )),
    COMMETHOD(['propputref', helpstring(u'Indicates the dynamic glyph for the specified dynamic symbol.')], HRESULT, 'DynamicGlyph',
              ( ['in'], esriDynamicSymbolType, 'dynamicSymbolType' ),
              ( ['in'], POINTER(IDynamicGlyph), 'DynamicGlyph' )),
    COMMETHOD([helpstring(u'Scales the dynamic symbol.')], HRESULT, 'GetScale',
              ( ['in'], esriDynamicSymbolType, 'dynamicSymbolType' ),
              ( ['in', 'out'], POINTER(c_float), 'scaleX' ),
              ( ['in', 'out'], POINTER(c_float), 'scaleY' )),
    COMMETHOD([helpstring(u'Scales the dynamic symbol.')], HRESULT, 'SetScale',
              ( ['in'], esriDynamicSymbolType, 'dynamicSymbolType' ),
              ( ['in'], c_float, 'scaleX' ),
              ( ['in'], c_float, 'scaleY' )),
    COMMETHOD([helpstring(u'Indicates the color for the specified dynamic symbol.')], HRESULT, 'GetColor',
              ( ['in'], esriDynamicSymbolType, 'dynamicSymbolType' ),
              ( ['in', 'out'], POINTER(c_float), 'Red' ),
              ( ['in', 'out'], POINTER(c_float), 'Green' ),
              ( ['in', 'out'], POINTER(c_float), 'Blue' ),
              ( ['in', 'out'], POINTER(c_float), 'alpha' )),
    COMMETHOD([helpstring(u'Indicates the color for the specified dynamic symbol.')], HRESULT, 'SetColor',
              ( ['in'], esriDynamicSymbolType, 'dynamicSymbolType' ),
              ( ['in'], c_float, 'Red' ),
              ( ['in'], c_float, 'Green' ),
              ( ['in'], c_float, 'Blue' ),
              ( ['in'], c_float, 'alpha' )),
    COMMETHOD(['propget', helpstring(u'Indicates the rotation alignment for the specified dynamic symbol.')], HRESULT, 'RotationAlignment',
              ( ['in'], esriDynamicSymbolType, 'dynamicSymbolType' ),
              ( ['retval', 'out'], POINTER(esriDynamicSymbolRotationAlignment), 'dynamicSymbolRotationAlignment' )),
    COMMETHOD(['propput', helpstring(u'Indicates the rotation alignment for the specified dynamic symbol.')], HRESULT, 'RotationAlignment',
              ( ['in'], esriDynamicSymbolType, 'dynamicSymbolType' ),
              ( ['in'], esriDynamicSymbolRotationAlignment, 'dynamicSymbolRotationAlignment' )),
    COMMETHOD(['propget', helpstring(u'Indicates the heading for the specified dynamic symbol, relative to the rotation alignment.')], HRESULT, 'Heading',
              ( ['in'], esriDynamicSymbolType, 'dynamicSymbolType' ),
              ( ['retval', 'out'], POINTER(c_float), 'Heading' )),
    COMMETHOD(['propput', helpstring(u'Indicates the heading for the specified dynamic symbol, relative to the rotation alignment.')], HRESULT, 'Heading',
              ( ['in'], esriDynamicSymbolType, 'dynamicSymbolType' ),
              ( ['in'], c_float, 'Heading' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the specified dynamic symbol will be smooth.')], HRESULT, 'Smooth',
              ( ['in'], esriDynamicSymbolType, 'dynamicSymbolType' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Smooth' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether the specified dynamic symbol will be smooth.')], HRESULT, 'Smooth',
              ( ['in'], esriDynamicSymbolType, 'dynamicSymbolType' ),
              ( ['in'], VARIANT_BOOL, 'Smooth' )),
    COMMETHOD(['propget', helpstring(u'Indicates the vertical alignment for the dynamic text symbol.')], HRESULT, 'TextVerticalAlignment',
              ( ['retval', 'out'], POINTER(esriTextVerticalAlignment), 'VerticalAlignment' )),
    COMMETHOD(['propput', helpstring(u'Indicates the vertical alignment for the dynamic text symbol.')], HRESULT, 'TextVerticalAlignment',
              ( ['in'], esriTextVerticalAlignment, 'VerticalAlignment' )),
    COMMETHOD(['propget', helpstring(u'Indicates the horizontal alignment for the dynamic text symbol.')], HRESULT, 'TextHorizontalAlignment',
              ( ['retval', 'out'], POINTER(esriTextHorizontalAlignment), 'HorizontalAlignment' )),
    COMMETHOD(['propput', helpstring(u'Indicates the horizontal alignment for the dynamic text symbol.')], HRESULT, 'TextHorizontalAlignment',
              ( ['in'], esriTextHorizontalAlignment, 'HorizontalAlignment' )),
]
################################################################
## code template for IDynamicSymbolProperties implementation
##class IDynamicSymbolProperties_Impl(object):
##    def SetColor(self, dynamicSymbolType, Red, Green, Blue, alpha):
##        u'Indicates the color for the specified dynamic symbol.'
##        #return 
##
##    def _get(self, dynamicSymbolType):
##        u'Indicates the rotation alignment for the specified dynamic symbol.'
##        #return dynamicSymbolRotationAlignment
##    def _set(self, dynamicSymbolType, dynamicSymbolRotationAlignment):
##        u'Indicates the rotation alignment for the specified dynamic symbol.'
##    RotationAlignment = property(_get, _set, doc = _set.__doc__)
##
##    def GetColor(self, dynamicSymbolType):
##        u'Indicates the color for the specified dynamic symbol.'
##        #return Red, Green, Blue, alpha
##
##    def _get(self, dynamicSymbolType):
##        u'Indicates whether the specified dynamic symbol will be smooth.'
##        #return Smooth
##    def _set(self, dynamicSymbolType, Smooth):
##        u'Indicates whether the specified dynamic symbol will be smooth.'
##    Smooth = property(_get, _set, doc = _set.__doc__)
##
##    def SetScale(self, dynamicSymbolType, scaleX, scaleY):
##        u'Scales the dynamic symbol.'
##        #return 
##
##    def DynamicGlyph(self, dynamicSymbolType, DynamicGlyph):
##        u'Indicates the dynamic glyph for the specified dynamic symbol.'
##        #return 
##
##    def _get(self):
##        u'Indicates the vertical alignment for the dynamic text symbol.'
##        #return VerticalAlignment
##    def _set(self, VerticalAlignment):
##        u'Indicates the vertical alignment for the dynamic text symbol.'
##    TextVerticalAlignment = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates the horizontal alignment for the dynamic text symbol.'
##        #return HorizontalAlignment
##    def _set(self, HorizontalAlignment):
##        u'Indicates the horizontal alignment for the dynamic text symbol.'
##    TextHorizontalAlignment = property(_get, _set, doc = _set.__doc__)
##
##    def GetScale(self, dynamicSymbolType):
##        u'Scales the dynamic symbol.'
##        #return scaleX, scaleY
##
##    def _get(self, dynamicSymbolType):
##        u'Indicates the heading for the specified dynamic symbol, relative to the rotation alignment.'
##        #return Heading
##    def _set(self, dynamicSymbolType, Heading):
##        u'Indicates the heading for the specified dynamic symbol, relative to the rotation alignment.'
##    Heading = property(_get, _set, doc = _set.__doc__)
##

class MarkerPlacementAtExtremities(CoClass):
    u'Places a marker on each extremity of a line.'
    _reg_clsid_ = GUID('{34B81D56-887D-448F-9EE8-4C3F52656A14}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
MarkerPlacementAtExtremities._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMarkerPlacement, IGraphicAttributes, IGraphicAttributes2, IEditInteraction, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

class ISymbol3D(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control 3D symbols.'
    _iid_ = GUID('{869331A4-A283-4DCB-A4D9-DFD02DC95F3A}')
    _idlflags_ = ['oleautomation']
ISymbol3D._methods_ = [
]
################################################################
## code template for ISymbol3D implementation
##class ISymbol3D_Impl(object):

class IMarkerLineSymbol(ILineSymbol):
    _case_insensitive_ = True
    u'Provides access to members that control the marker line symbol.'
    _iid_ = GUID('{B04BC35B-C36E-11D0-BFA1-0080C7E24280}')
    _idlflags_ = ['oleautomation']
IMarkerLineSymbol._methods_ = [
    COMMETHOD(['propget', helpstring(u'Symbol used for marker line.')], HRESULT, 'MarkerSymbol',
              ( ['retval', 'out'], POINTER(POINTER(IMarkerSymbol)), 'marker' )),
    COMMETHOD(['propputref', helpstring(u'Symbol used for marker line.')], HRESULT, 'MarkerSymbol',
              ( ['in'], POINTER(IMarkerSymbol), 'marker' )),
]
################################################################
## code template for IMarkerLineSymbol implementation
##class IMarkerLineSymbol_Impl(object):
##    def MarkerSymbol(self, marker):
##        u'Symbol used for marker line.'
##        #return 
##

class ICartographicMarkerSymbol(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the cartographic marker symbol.'
    _iid_ = GUID('{7914E5E6-C892-11D0-8BB6-080009EE4E41}')
    _idlflags_ = ['oleautomation']
ICartographicMarkerSymbol._methods_ = [
    COMMETHOD(['propget', helpstring(u'Symbol scale along X-axis.')], HRESULT, 'XScale',
              ( ['retval', 'out'], POINTER(c_double), 'XScale' )),
    COMMETHOD(['propput', helpstring(u'Symbol scale along X-axis.')], HRESULT, 'XScale',
              ( ['in'], c_double, 'XScale' )),
    COMMETHOD(['propget', helpstring(u'Symbol scale along Y-axis.')], HRESULT, 'YScale',
              ( ['retval', 'out'], POINTER(c_double), 'YScale' )),
    COMMETHOD(['propput', helpstring(u'Symbol scale along Y-axis.')], HRESULT, 'YScale',
              ( ['in'], c_double, 'YScale' )),
]
################################################################
## code template for ICartographicMarkerSymbol implementation
##class ICartographicMarkerSymbol_Impl(object):
##    def _get(self):
##        u'Symbol scale along X-axis.'
##        #return XScale
##    def _set(self, XScale):
##        u'Symbol scale along X-axis.'
##    XScale = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Symbol scale along Y-axis.'
##        #return YScale
##    def _set(self, YScale):
##        u'Symbol scale along Y-axis.'
##    YScale = property(_get, _set, doc = _set.__doc__)
##

class IDotDensityMasking(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the masking properties of a dot density fill symbol.'
    _iid_ = GUID('{758FC2B0-D2AC-11D3-81F3-0080C79F0371}')
    _idlflags_ = ['oleautomation']
IDotDensityMasking._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The geometry used for masking (can be a geometry collection).')], HRESULT, 'MaskGeometry',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'Geometry' )),
    COMMETHOD(['propget', helpstring(u'The geometry used for masking (can be a geometry collection).')], HRESULT, 'MaskGeometry',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry)), 'Geometry' )),
    COMMETHOD(['propget', helpstring(u'Indicates if masking is used.')], HRESULT, 'UseMasking',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'UseMasking' )),
    COMMETHOD(['propput', helpstring(u'Indicates if masking is used.')], HRESULT, 'UseMasking',
              ( ['in'], VARIANT_BOOL, 'UseMasking' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the dots are to be excluded from the mask area.')], HRESULT, 'ExcludeMask',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ExcludeMask' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the dots are to be excluded from the mask area.')], HRESULT, 'ExcludeMask',
              ( ['in'], VARIANT_BOOL, 'ExcludeMask' )),
]
################################################################
## code template for IDotDensityMasking implementation
##class IDotDensityMasking_Impl(object):
##    def _get(self):
##        u'Indicates if masking is used.'
##        #return UseMasking
##    def _set(self, UseMasking):
##        u'Indicates if masking is used.'
##    UseMasking = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def MaskGeometry(self, Geometry):
##        u'The geometry used for masking (can be a geometry collection).'
##        #return 
##
##    def _get(self):
##        u'Indicates if the dots are to be excluded from the mask area.'
##        #return ExcludeMask
##    def _set(self, ExcludeMask):
##        u'Indicates if the dots are to be excluded from the mask area.'
##    ExcludeMask = property(_get, _set, doc = _set.__doc__)
##

class ISimpleMarkerSymbol(IMarkerSymbol):
    _case_insensitive_ = True
    u'Provides access to members that control the simple marker symbol.'
    _iid_ = GUID('{A9360290-5828-11D0-98BF-00805F7CED21}')
    _idlflags_ = ['oleautomation']
ISimpleMarkerSymbol._methods_ = [
    COMMETHOD(['propget', helpstring(u'Marker style.')], HRESULT, 'Style',
              ( ['retval', 'out'], POINTER(esriSimpleMarkerStyle), 'Style' )),
    COMMETHOD(['propput', helpstring(u'Marker style.')], HRESULT, 'Style',
              ( ['in'], esriSimpleMarkerStyle, 'Style' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the symbol outline will draw.')], HRESULT, 'Outline',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Outline' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the symbol outline will draw.')], HRESULT, 'Outline',
              ( ['in'], VARIANT_BOOL, 'Outline' )),
    COMMETHOD(['propget', helpstring(u'Outline diameter.')], HRESULT, 'OutlineSize',
              ( ['retval', 'out'], POINTER(c_double), 'Size' )),
    COMMETHOD(['propput', helpstring(u'Outline diameter.')], HRESULT, 'OutlineSize',
              ( ['in'], c_double, 'Size' )),
    COMMETHOD(['propget', helpstring(u'Outline color.')], HRESULT, 'OutlineColor',
              ( ['retval', 'out'], POINTER(POINTER(IColor)), 'OutlineColor' )),
    COMMETHOD(['propput', helpstring(u'Outline color.')], HRESULT, 'OutlineColor',
              ( ['in'], POINTER(IColor), 'OutlineColor' )),
]
################################################################
## code template for ISimpleMarkerSymbol implementation
##class ISimpleMarkerSymbol_Impl(object):
##    def _get(self):
##        u'Marker style.'
##        #return Style
##    def _set(self, Style):
##        u'Marker style.'
##    Style = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the symbol outline will draw.'
##        #return Outline
##    def _set(self, Outline):
##        u'Indicates if the symbol outline will draw.'
##    Outline = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Outline diameter.'
##        #return Size
##    def _set(self, Size):
##        u'Outline diameter.'
##    OutlineSize = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Outline color.'
##        #return OutlineColor
##    def _set(self, OutlineColor):
##        u'Outline color.'
##    OutlineColor = property(_get, _set, doc = _set.__doc__)
##

class FontColor(CoClass):
    u'Controls text color.'
    _reg_clsid_ = GUID('{01E02EAB-80AA-4F82-8914-0AEE97F504EC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IFontColor(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to font color property.'
    _iid_ = GUID('{15D970B2-B06F-4C5C-8552-BCDD24D98423}')
    _idlflags_ = ['oleautomation']
FontColor._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IFontColor]

class IMoveInteraction(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the parameters of the Move Representation Tool.'
    _iid_ = GUID('{3DC6BB2C-D398-4CEF-934A-91FDD53288D4}')
    _idlflags_ = ['oleautomation']
IMoveInteraction._methods_ = [
    COMMETHOD(['propput', helpstring(u'Current horizontal offset expressed in points.')], HRESULT, 'OffsetX',
              ( ['in'], c_double, 'Offset' )),
    COMMETHOD(['propget', helpstring(u'Current horizontal offset expressed in points.')], HRESULT, 'OffsetX',
              ( ['retval', 'out'], POINTER(c_double), 'Offset' )),
    COMMETHOD(['propput', helpstring(u'Current vertical offset expressed in points.')], HRESULT, 'OffsetY',
              ( ['in'], c_double, 'MapOffset' )),
    COMMETHOD(['propget', helpstring(u'Current vertical offset expressed in points.')], HRESULT, 'OffsetY',
              ( ['retval', 'out'], POINTER(c_double), 'MapOffset' )),
    COMMETHOD(['propput', helpstring(u'Current horizontal offset expressed in map units.')], HRESULT, 'MapOffsetX',
              ( ['in'], c_double, 'MapOffset' )),
    COMMETHOD(['propget', helpstring(u'Current horizontal offset expressed in map units.')], HRESULT, 'MapOffsetX',
              ( ['retval', 'out'], POINTER(c_double), 'MapOffset' )),
    COMMETHOD(['propput', helpstring(u'Current vertical offset expressed in map units.')], HRESULT, 'MapOffsetY',
              ( ['in'], c_double, 'MapOffset' )),
    COMMETHOD(['propget', helpstring(u'Current vertical offset expressed in map units.')], HRESULT, 'MapOffsetY',
              ( ['retval', 'out'], POINTER(c_double), 'MapOffset' )),
]
################################################################
## code template for IMoveInteraction implementation
##class IMoveInteraction_Impl(object):
##    def _get(self):
##        u'Current vertical offset expressed in map units.'
##        #return MapOffset
##    def _set(self, MapOffset):
##        u'Current vertical offset expressed in map units.'
##    MapOffsetY = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Current horizontal offset expressed in map units.'
##        #return MapOffset
##    def _set(self, MapOffset):
##        u'Current horizontal offset expressed in map units.'
##    MapOffsetX = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Current horizontal offset expressed in points.'
##        #return Offset
##    def _set(self, Offset):
##        u'Current horizontal offset expressed in points.'
##    OffsetX = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Current vertical offset expressed in points.'
##        #return MapOffset
##    def _set(self, MapOffset):
##        u'Current vertical offset expressed in points.'
##    OffsetY = property(_get, _set, doc = _set.__doc__)
##


# values for enumeration 'esriDisplayTransformationEnum'
esriTransformPosition = 1
esriTransformSize = 2
esriTransformToMap = 4
esriTransformToDevice = 8
esriDisplayTransformationEnum = c_int # enum
IRepresentationRule._methods_ = [
    COMMETHOD(['propget', helpstring(u'Number of layers in the representation rule.')], HRESULT, 'LayerCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Layer at a given index.')], HRESULT, 'Layer',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IBasicSymbol)), 'Symbol' )),
    COMMETHOD([helpstring(u'Adds a layer to the representation rule.')], HRESULT, 'InsertLayer',
              ( ['in'], c_int, 'index' ),
              ( ['in'], POINTER(IBasicSymbol), 'Symbol' )),
    COMMETHOD([helpstring(u'Removes a layer from the representation rule.')], HRESULT, 'RemoveLayer',
              ( ['in'], c_int, 'index' )),
    COMMETHOD([helpstring(u'Draws a layer of a representation rule. If index is -1, all layers are drawn.')], HRESULT, 'Draw',
              ( ['in'], c_int, 'index' ),
              ( ['in'], POINTER(IOutputContext), 'context' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'Geometry' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'envelope' )),
]
################################################################
## code template for IRepresentationRule implementation
##class IRepresentationRule_Impl(object):
##    def InsertLayer(self, index, Symbol):
##        u'Adds a layer to the representation rule.'
##        #return 
##
##    @property
##    def Layer(self, index):
##        u'Layer at a given index.'
##        #return Symbol
##
##    def RemoveLayer(self, index):
##        u'Removes a layer from the representation rule.'
##        #return 
##
##    def Draw(self, index, context, Geometry, envelope):
##        u'Draws a layer of a representation rule. If index is -1, all layers are drawn.'
##        #return 
##
##    @property
##    def LayerCount(self):
##        u'Number of layers in the representation rule.'
##        #return Count
##

IRepresentationRule2._methods_ = [
    COMMETHOD(['propget', helpstring(u'Retrieves the identifier of an attribute list.')], HRESULT, 'IDFromAttributes',
              ( ['in'], POINTER(IGraphicAttributes), 'attrList' ),
              ( ['retval', 'out'], POINTER(c_int), 'AttrListID' )),
    COMMETHOD(['propget', helpstring(u'Retrieves the attribute list from an identifier.')], HRESULT, 'AttributesFromID',
              ( ['in'], c_int, 'AttrListID' ),
              ( ['retval', 'out'], POINTER(POINTER(IGraphicAttributes)), 'attrList' )),
    COMMETHOD(['propput', helpstring(u'Seed value to ensure stability of random effects. When drawing features, the object ID is used.')], HRESULT, 'FeatureSeed',
              ( ['in'], c_int, 'featureOID' )),
    COMMETHOD(['propget', helpstring(u'Seed value to ensure stability of random effects. When drawing features, the object ID is used.')], HRESULT, 'FeatureSeed',
              ( ['retval', 'out'], POINTER(c_int), 'featureOID' )),
]
################################################################
## code template for IRepresentationRule2 implementation
##class IRepresentationRule2_Impl(object):
##    @property
##    def AttributesFromID(self, AttrListID):
##        u'Retrieves the attribute list from an identifier.'
##        #return attrList
##
##    @property
##    def IDFromAttributes(self, attrList):
##        u'Retrieves the identifier of an attribute list.'
##        #return AttrListID
##
##    def _get(self):
##        u'Seed value to ensure stability of random effects. When drawing features, the object ID is used.'
##        #return featureOID
##    def _set(self, featureOID):
##        u'Seed value to ensure stability of random effects. When drawing features, the object ID is used.'
##    FeatureSeed = property(_get, _set, doc = _set.__doc__)
##

class IScreenDisplayZoom(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to zooming the screen display.'
    _iid_ = GUID('{F3093E1F-EC1F-4DB7-9095-F2874B0CEED0}')
    _idlflags_ = ['oleautomation']
IScreenDisplayZoom._methods_ = [
    COMMETHOD([helpstring(u'Prepares display for zooming.')], HRESULT, 'ZoomStart',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
    COMMETHOD([helpstring(u'Zooms to a new extent.')], HRESULT, 'ZoomMoveTo',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
    COMMETHOD([helpstring(u'Stops zooming and returns new visible bounds.')], HRESULT, 'ZoomStop',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'newExtent' )),
    COMMETHOD([helpstring(u'Interactively Zooms the screen.')], HRESULT, 'TrackZoom'),
]
################################################################
## code template for IScreenDisplayZoom implementation
##class IScreenDisplayZoom_Impl(object):
##    def ZoomStop(self):
##        u'Stops zooming and returns new visible bounds.'
##        #return newExtent
##
##    def ZoomStart(self, Point):
##        u'Prepares display for zooming.'
##        #return 
##
##    def TrackZoom(self):
##        u'Interactively Zooms the screen.'
##        #return 
##
##    def ZoomMoveTo(self, Point):
##        u'Zooms to a new extent.'
##        #return 
##

class IFieldOverride(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the properties of a field override.'
    _iid_ = GUID('{AABE9E0B-CABD-40D9-95B0-49DB8BCA8A57}')
    _idlflags_ = ['oleautomation']
IFieldOverride._methods_ = [
    COMMETHOD(['propget', helpstring(u'Name of the field that provides override values.')], HRESULT, 'FieldName',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'ID of the overriden graphic attribute.')], HRESULT, 'GraphicAttributeID',
              ( ['retval', 'out'], POINTER(c_int), 'ID' )),
    COMMETHOD(['propget', helpstring(u'Graphic attributes list that contains the overriden graphic attribute.')], HRESULT, 'GraphicAttributes',
              ( ['retval', 'out'], POINTER(POINTER(IGraphicAttributes)), 'Attributes' )),
]
################################################################
## code template for IFieldOverride implementation
##class IFieldOverride_Impl(object):
##    @property
##    def GraphicAttributeID(self):
##        u'ID of the overriden graphic attribute.'
##        #return ID
##
##    @property
##    def FieldName(self):
##        u'Name of the field that provides override values.'
##        #return Name
##
##    @property
##    def GraphicAttributes(self):
##        u'Graphic attributes list that contains the overriden graphic attribute.'
##        #return Attributes
##

class DotDensityFillSymbol(CoClass):
    u'Defines a dot density fill symbol, a data driven symbol commonly used with the dot density renderer.'
    _reg_clsid_ = GUID('{9A1EBA10-CDF9-11D3-81EB-0080C79F0371}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IDotDensityFillSymbol(IFillSymbol):
    _case_insensitive_ = True
    u'Provides access to the main properties of a data driven symbol commonly used with a dot density renderer.'
    _iid_ = GUID('{85E413A0-CDF9-11D3-81EB-0080C79F0371}')
    _idlflags_ = ['oleautomation']
class IDotDensityFillSymbol2(IDotDensityFillSymbol):
    _case_insensitive_ = True
    u'Provides access to further properties of a data driven symbol commonly used with a dot density renderer.'
    _iid_ = GUID('{DE641030-CFC0-4465-BEAF-33245D3EA1E9}')
    _idlflags_ = ['oleautomation']
class ISymbolArray(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that work with an array of symbols.'
    _iid_ = GUID('{6CFF7E07-0502-11D4-9F7C-00C04F6BC709}')
    _idlflags_ = ['oleautomation']
DotDensityFillSymbol._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDotDensityFillSymbol, IDotDensityFillSymbol2, IDotDensityMasking, ISymbolArray, IMapLevel, ISymbol, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySupport, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone]


# values for enumeration 'esriLineConstraints'
esriLineConstraintsNone = 0
esriLineConstraintsVertical = 1
esriLineConstraintsHorizontal = 2
esriLineConstraints = c_int # enum
INewLineFeedback._methods_ = [
    COMMETHOD([helpstring(u'Begins a normal feedback at the given point.')], HRESULT, 'Start',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
    COMMETHOD([helpstring(u'Creates a node at the given point.')], HRESULT, 'AddPoint',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
    COMMETHOD([helpstring(u'Stops the feedback and returns the shape.')], HRESULT, 'Stop',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPolyline)), 'polyline' )),
    COMMETHOD(['propget', helpstring(u'The constraint on this rubberbander.')], HRESULT, 'Constraint',
              ( ['retval', 'out'], POINTER(esriLineConstraints), 'constrain' )),
    COMMETHOD(['propput', helpstring(u'The constraint on this rubberbander.')], HRESULT, 'Constraint',
              ( ['in'], esriLineConstraints, 'constrain' )),
]
################################################################
## code template for INewLineFeedback implementation
##class INewLineFeedback_Impl(object):
##    def Start(self, Point):
##        u'Begins a normal feedback at the given point.'
##        #return 
##
##    def _get(self):
##        u'The constraint on this rubberbander.'
##        #return constrain
##    def _set(self, constrain):
##        u'The constraint on this rubberbander.'
##    Constraint = property(_get, _set, doc = _set.__doc__)
##
##    def Stop(self):
##        u'Stops the feedback and returns the shape.'
##        #return polyline
##
##    def AddPoint(self, Point):
##        u'Creates a node at the given point.'
##        #return 
##

IBasicFillSymbol._methods_ = [
    COMMETHOD(['propget', helpstring(u'Fill pattern of a basic fill symbol.')], HRESULT, 'FillPattern',
              ( ['retval', 'out'], POINTER(POINTER(IFillPattern)), 'pattern' )),
    COMMETHOD(['propputref', helpstring(u'Fill pattern of a basic fill symbol.')], HRESULT, 'FillPattern',
              ( ['in'], POINTER(IFillPattern), 'pattern' )),
]
################################################################
## code template for IBasicFillSymbol implementation
##class IBasicFillSymbol_Impl(object):
##    def FillPattern(self, pattern):
##        u'Fill pattern of a basic fill symbol.'
##        #return 
##


# values for enumeration 'esriScreenCache'
esriNoScreenCache = -1
esriAllScreenCaches = -2
esriScreenRecording = -3
esriScreenCache = c_int # enum
class GrayColor(CoClass):
    u'A color in the grayscale color system.'
    _reg_clsid_ = GUID('{7EE9C495-D123-11D0-8383-080009B996CC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
GrayColor._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGrayColor, IColor, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize]

class ISymbologyEnvironment(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the environment for certain Symbol operations.'
    _iid_ = GUID('{65856CD7-AD04-11D3-9FC2-00C04F6BC8DD}')
    _idlflags_ = ['oleautomation']
ISymbologyEnvironment._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if a GDI comment is output for CMYK colors.')], HRESULT, 'OutputGDICommentForCMYKColor',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pCmykColor' )),
    COMMETHOD(['propput', helpstring(u'Indicates if a GDI comment is output for CMYK colors.')], HRESULT, 'OutputGDICommentForCMYKColor',
              ( ['in'], VARIANT_BOOL, 'pCmykColor' )),
    COMMETHOD(['propget', helpstring(u'Indicates if a GDI comment is output for layers.')], HRESULT, 'OutputGDICommentForLayers',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'layers' )),
    COMMETHOD(['propput', helpstring(u'Indicates if a GDI comment is output for layers.')], HRESULT, 'OutputGDICommentForLayers',
              ( ['in'], VARIANT_BOOL, 'layers' )),
    COMMETHOD(['propget', helpstring(u'Indicates if a GDI comment is output for groupings.')], HRESULT, 'OutputGDICommentForGroupings',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'grouping' )),
    COMMETHOD(['propput', helpstring(u'Indicates if a GDI comment is output for groupings.')], HRESULT, 'OutputGDICommentForGroupings',
              ( ['in'], VARIANT_BOOL, 'grouping' )),
    COMMETHOD(['propget', helpstring(u'Indicates if a GDI comment is output for text.')], HRESULT, 'OutputGDICommentForText',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Text' )),
    COMMETHOD(['propput', helpstring(u'Indicates if a GDI comment is output for text.')], HRESULT, 'OutputGDICommentForText',
              ( ['in'], VARIANT_BOOL, 'Text' )),
    COMMETHOD(['propget', helpstring(u'Indicates if all geometry is clipped on output.')], HRESULT, 'GeometryClipping',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'GeometryClipping' )),
    COMMETHOD(['propput', helpstring(u'Indicates if all geometry is clipped on output.')], HRESULT, 'GeometryClipping',
              ( ['in'], VARIANT_BOOL, 'GeometryClipping' )),
    COMMETHOD(['propget', helpstring(u'Indicates if TrueType markers are stroked.')], HRESULT, 'StrokeTrueTypeMarkers',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'StrokeTrueTypeMarkers' )),
    COMMETHOD(['propput', helpstring(u'Indicates if TrueType markers are stroked.')], HRESULT, 'StrokeTrueTypeMarkers',
              ( ['in'], VARIANT_BOOL, 'StrokeTrueTypeMarkers' )),
]
################################################################
## code template for ISymbologyEnvironment implementation
##class ISymbologyEnvironment_Impl(object):
##    def _get(self):
##        u'Indicates if a GDI comment is output for groupings.'
##        #return grouping
##    def _set(self, grouping):
##        u'Indicates if a GDI comment is output for groupings.'
##    OutputGDICommentForGroupings = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if TrueType markers are stroked.'
##        #return StrokeTrueTypeMarkers
##    def _set(self, StrokeTrueTypeMarkers):
##        u'Indicates if TrueType markers are stroked.'
##    StrokeTrueTypeMarkers = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if a GDI comment is output for layers.'
##        #return layers
##    def _set(self, layers):
##        u'Indicates if a GDI comment is output for layers.'
##    OutputGDICommentForLayers = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if a GDI comment is output for CMYK colors.'
##        #return pCmykColor
##    def _set(self, pCmykColor):
##        u'Indicates if a GDI comment is output for CMYK colors.'
##    OutputGDICommentForCMYKColor = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if all geometry is clipped on output.'
##        #return GeometryClipping
##    def _set(self, GeometryClipping):
##        u'Indicates if all geometry is clipped on output.'
##    GeometryClipping = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if a GDI comment is output for text.'
##        #return Text
##    def _set(self, Text):
##        u'Indicates if a GDI comment is output for text.'
##    OutputGDICommentForText = property(_get, _set, doc = _set.__doc__)
##

ICalloutFeedback2._methods_ = [
    COMMETHOD([helpstring(u'Begins a feedback of the given symbol.')], HRESULT, 'Start',
              ( ['in'], POINTER(ISymbol), 'Symbol' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'Geometry' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' ),
              ( ['in'], c_double, 'ReferenceScale' )),
    COMMETHOD([helpstring(u'Stops the feedback and returns the shape.')], HRESULT, 'Stop',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPolyline)), 'polyline' )),
    COMMETHOD([helpstring(u'Moves the anchor point to the given point.')], HRESULT, 'MoveAnchorTo',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
]
################################################################
## code template for ICalloutFeedback2 implementation
##class ICalloutFeedback2_Impl(object):
##    def Start(self, Symbol, Geometry, Point, ReferenceScale):
##        u'Begins a feedback of the given symbol.'
##        #return 
##
##    def MoveAnchorTo(self, Point):
##        u'Moves the anchor point to the given point.'
##        #return 
##
##    def Stop(self):
##        u'Stops the feedback and returns the shape.'
##        #return polyline
##

IBasicMarkerSymbol._methods_ = [
    COMMETHOD(['propget', helpstring(u'Marker placement of a basic marker symbol.')], HRESULT, 'MarkerPlacement',
              ( ['retval', 'out'], POINTER(POINTER(IMarkerPlacement)), 'tag' )),
    COMMETHOD(['propputref', helpstring(u'Marker placement of a basic marker symbol.')], HRESULT, 'MarkerPlacement',
              ( ['in'], POINTER(IMarkerPlacement), 'tag' )),
]
################################################################
## code template for IBasicMarkerSymbol implementation
##class IBasicMarkerSymbol_Impl(object):
##    def MarkerPlacement(self, tag):
##        u'Marker placement of a basic marker symbol.'
##        #return 
##

IGlobalScreenDisplaySettings._methods_ = [
    COMMETHOD(['propput', helpstring(u'Enables continuous display updates during navigation while in a remote desktop session.')], HRESULT, 'EnableContinuousUpdatesOverRemoteDesktop',
              ( ['in'], VARIANT_BOOL, 'pbEnableInteract' )),
    COMMETHOD(['propget', helpstring(u'Enables continuous display updates during navigation while in a remote desktop session.')], HRESULT, 'EnableContinuousUpdatesOverRemoteDesktop',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbEnableInteract' )),
    COMMETHOD(['propput', helpstring(u'Enables use of hardware acceleration.')], HRESULT, 'EnableHardwareAcceleration',
              ( ['in'], VARIANT_BOOL, 'bEnableHA' )),
    COMMETHOD(['propget', helpstring(u'Enables use of hardware acceleration.')], HRESULT, 'EnableHardwareAcceleration',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bEnableHA' )),
    COMMETHOD([helpstring(u'Indicates if hardware acceleration can be enabled.')], HRESULT, 'CanEnableHardwareAcceleration',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bHA' )),
]
################################################################
## code template for IGlobalScreenDisplaySettings implementation
##class IGlobalScreenDisplaySettings_Impl(object):
##    def _get(self):
##        u'Enables continuous display updates during navigation while in a remote desktop session.'
##        #return pbEnableInteract
##    def _set(self, pbEnableInteract):
##        u'Enables continuous display updates during navigation while in a remote desktop session.'
##    EnableContinuousUpdatesOverRemoteDesktop = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Enables use of hardware acceleration.'
##        #return bEnableHA
##    def _set(self, bEnableHA):
##        u'Enables use of hardware acceleration.'
##    EnableHardwareAcceleration = property(_get, _set, doc = _set.__doc__)
##
##    def CanEnableHardwareAcceleration(self):
##        u'Indicates if hardware acceleration can be enabled.'
##        #return bHA
##

class IWordTextPath(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Indicator interface for word text path objects.'
    _iid_ = GUID('{2690CDCE-96A4-49DA-BD07-3F4ED61EFECE}')
    _idlflags_ = ['oleautomation']
IWordTextPath._methods_ = [
]
################################################################
## code template for IWordTextPath implementation
##class IWordTextPath_Impl(object):

class IEnumScreenDisplay(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Screen Display enumerator.'
    _iid_ = GUID('{1C6A7A03-E716-11D0-8681-0000F8751720}')
    _idlflags_ = ['oleautomation']
IEnumScreenDisplay._methods_ = [
    COMMETHOD([helpstring(u'Returns the next screen display in the collection.')], HRESULT, 'Next',
              ( ['retval', 'out'], POINTER(POINTER(IScreenDisplay)), 'ScreenDisplay' )),
    COMMETHOD([helpstring(u'Resets enumerator to start of collection.')], HRESULT, 'Reset'),
]
################################################################
## code template for IEnumScreenDisplay implementation
##class IEnumScreenDisplay_Impl(object):
##    def Reset(self):
##        u'Resets enumerator to start of collection.'
##        #return 
##
##    def Next(self):
##        u'Returns the next screen display in the collection.'
##        #return ScreenDisplay
##

IDynamicDisplay._methods_ = [
    COMMETHOD(['propget', helpstring(u'Retrieves the dynamic glyph factory.')], HRESULT, 'DynamicGlyphFactory',
              ( ['retval', 'out'], POINTER(POINTER(IDynamicGlyphFactory)), 'DynamicGlyphFactory' )),
    COMMETHOD([helpstring(u'Draws a marker at the specified points on the dynamic display.')], HRESULT, 'DrawMultipleMarkers',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPointCollection), 'pointCollection' )),
    COMMETHOD([helpstring(u'Draws a marker at the specified point on the dynamic display.')], HRESULT, 'DrawMarker',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
    COMMETHOD([helpstring(u'Draws specified polygon with fill and line on the dynamic display.')], HRESULT, 'DrawPolygon',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPointCollection), 'pointCollection' )),
    COMMETHOD([helpstring(u'Draws specified lines on the dynamic display.')], HRESULT, 'DrawMultipleLines',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPointCollection), 'pointCollection' )),
    COMMETHOD([helpstring(u'Draws a line between the specified points on the dynamic display.')], HRESULT, 'DrawLine',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'startPoint' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'endPoint' )),
    COMMETHOD([helpstring(u'Draws specified polyline on the dynamic display.')], HRESULT, 'DrawPolyline',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPointCollection), 'pointCollection' )),
    COMMETHOD([helpstring(u'Draws specified rectangle with fill and line on the dynamic display.')], HRESULT, 'DrawRectangle',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'envelope' )),
    COMMETHOD([helpstring(u'Draws text at the specified point on the dynamic display.')], HRESULT, 'DrawText',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' ),
              ( ['in'], BSTR, 'Text' )),
]
################################################################
## code template for IDynamicDisplay implementation
##class IDynamicDisplay_Impl(object):
##    def DrawMultipleMarkers(self, pointCollection):
##        u'Draws a marker at the specified points on the dynamic display.'
##        #return 
##
##    def DrawPolygon(self, pointCollection):
##        u'Draws specified polygon with fill and line on the dynamic display.'
##        #return 
##
##    @property
##    def DynamicGlyphFactory(self):
##        u'Retrieves the dynamic glyph factory.'
##        #return DynamicGlyphFactory
##
##    def DrawText(self, Point, Text):
##        u'Draws text at the specified point on the dynamic display.'
##        #return 
##
##    def DrawPolyline(self, pointCollection):
##        u'Draws specified polyline on the dynamic display.'
##        #return 
##
##    def DrawLine(self, startPoint, endPoint):
##        u'Draws a line between the specified points on the dynamic display.'
##        #return 
##
##    def DrawMarker(self, Point):
##        u'Draws a marker at the specified point on the dynamic display.'
##        #return 
##
##    def DrawMultipleLines(self, pointCollection):
##        u'Draws specified lines on the dynamic display.'
##        #return 
##
##    def DrawRectangle(self, envelope):
##        u'Draws specified rectangle with fill and line on the dynamic display.'
##        #return 
##

class IWordBoundaries(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to word boundaries for a text symbol.'
    _iid_ = GUID('{DF0F7BA7-1C31-44CB-975F-87FF272793AA}')
    _idlflags_ = ['oleautomation']
IWordBoundaries._methods_ = [
    COMMETHOD([helpstring(u'Fills an existing geometry bag with the boundaries of the words in the text symbol.')], HRESULT, 'QueryWordBoundaries',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDC' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ITransformation), 'displayTransform' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'Geometry' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometryBag), 'boundaries' )),
]
################################################################
## code template for IWordBoundaries implementation
##class IWordBoundaries_Impl(object):
##    def QueryWordBoundaries(self, hDC, displayTransform, Geometry, boundaries):
##        u'Fills an existing geometry bag with the boundaries of the words in the text symbol.'
##        #return 
##

class SimpleLineSymbol(CoClass):
    u'A line symbol comprised of a predefined set of styles.'
    _reg_clsid_ = GUID('{7914E5F9-C892-11D0-8BB6-080009EE4E41}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
SimpleLineSymbol._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ISimpleLineSymbol, IMapLevel, ISymbol, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySupport, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, IDisplayName, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize]

class ISymbologyEnvironment2(ISymbologyEnvironment):
    _case_insensitive_ = True
    u'Provides access to members that control the environment for certain Symbol operations.'
    _iid_ = GUID('{F8C203AE-65C9-4919-B39F-B006927B2979}')
    _idlflags_ = ['oleautomation']
ISymbologyEnvironment2._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if a GDI comment is output for feature attributes.')], HRESULT, 'OutputGDICommentForFeatureAttributes',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'featureAttributes' )),
    COMMETHOD(['propput', helpstring(u'Indicates if a GDI comment is output for feature attributes.')], HRESULT, 'OutputGDICommentForFeatureAttributes',
              ( ['in'], VARIANT_BOOL, 'featureAttributes' )),
    COMMETHOD(['propget', helpstring(u'Indicates if a GDI comment is output for hyperlinks.')], HRESULT, 'OutputGDICommentForHyperlinks',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'hyperlinks' )),
    COMMETHOD(['propput', helpstring(u'Indicates if a GDI comment is output for hyperlinks.')], HRESULT, 'OutputGDICommentForHyperlinks',
              ( ['in'], VARIANT_BOOL, 'hyperlinks' )),
    COMMETHOD(['propget', helpstring(u'Indicates if a GDI comment is output for Maps and Page Layout.')], HRESULT, 'OutputGDICommentForMapsAndLayout',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'maps' )),
    COMMETHOD(['propput', helpstring(u'Indicates if a GDI comment is output for Maps and Page Layout.')], HRESULT, 'OutputGDICommentForMapsAndLayout',
              ( ['in'], VARIANT_BOOL, 'maps' )),
]
################################################################
## code template for ISymbologyEnvironment2 implementation
##class ISymbologyEnvironment2_Impl(object):
##    def _get(self):
##        u'Indicates if a GDI comment is output for feature attributes.'
##        #return featureAttributes
##    def _set(self, featureAttributes):
##        u'Indicates if a GDI comment is output for feature attributes.'
##    OutputGDICommentForFeatureAttributes = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if a GDI comment is output for hyperlinks.'
##        #return hyperlinks
##    def _set(self, hyperlinks):
##        u'Indicates if a GDI comment is output for hyperlinks.'
##    OutputGDICommentForHyperlinks = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if a GDI comment is output for Maps and Page Layout.'
##        #return maps
##    def _set(self, maps):
##        u'Indicates if a GDI comment is output for Maps and Page Layout.'
##    OutputGDICommentForMapsAndLayout = property(_get, _set, doc = _set.__doc__)
##

class INewRectangleFeedback(IDisplayFeedback2):
    _case_insensitive_ = True
    u'Provides access to members that control the creation of a new rectangle.'
    _iid_ = GUID('{CE877344-E124-4CFB-BF38-E9E7F853B575}')
    _idlflags_ = ['oleautomation']
INewRectangleFeedback._methods_ = [
    COMMETHOD([helpstring(u'Begins a normal feedback at the given point.')], HRESULT, 'Start',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
    COMMETHOD([helpstring(u'Set the location of the second location.')], HRESULT, 'SetPoint',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
    COMMETHOD([helpstring(u'Stops the feedback and returns the shape.')], HRESULT, 'Stop',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry)), 'rectangle' )),
    COMMETHOD(['propget', helpstring(u'The length of the current rectangle being constructed.')], HRESULT, 'Length',
              ( ['retval', 'out'], POINTER(c_double), 'Length' )),
    COMMETHOD(['propput', helpstring(u'The length of the current rectangle being constructed.')], HRESULT, 'Length',
              ( ['in'], c_double, 'Length' )),
    COMMETHOD(['propget', helpstring(u'The width of the current rectangle being constructed.')], HRESULT, 'Width',
              ( ['retval', 'out'], POINTER(c_double), 'Width' )),
    COMMETHOD(['propput', helpstring(u'The width of the current rectangle being constructed.')], HRESULT, 'Width',
              ( ['in'], c_double, 'Width' )),
    COMMETHOD(['propget', helpstring(u'The angle of the current rectangle being constructed.')], HRESULT, 'Angle',
              ( ['retval', 'out'], POINTER(c_double), 'Angle' )),
    COMMETHOD(['propput', helpstring(u'The angle of the current rectangle being constructed.')], HRESULT, 'Angle',
              ( ['in'], c_double, 'Angle' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the rectangle is an envelope or angled.')], HRESULT, 'IsEnvelope',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsEnvelope' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether the rectangle is an envelope or angled.')], HRESULT, 'IsEnvelope',
              ( ['in'], VARIANT_BOOL, 'IsEnvelope' )),
    COMMETHOD(['propget', helpstring(u"Indicates whether the rectangle's length is fixed.")], HRESULT, 'SnapLength',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'SnapLength' )),
    COMMETHOD(['propput', helpstring(u"Indicates whether the rectangle's length is fixed.")], HRESULT, 'SnapLength',
              ( ['in'], VARIANT_BOOL, 'SnapLength' )),
    COMMETHOD(['propget', helpstring(u'The constraint on this rubberbander.')], HRESULT, 'Constraint',
              ( ['retval', 'out'], POINTER(esriEnvelopeConstraints), 'constrain' )),
    COMMETHOD(['propput', helpstring(u'The constraint on this rubberbander.')], HRESULT, 'Constraint',
              ( ['in'], esriEnvelopeConstraints, 'constrain' )),
    COMMETHOD(['propget', helpstring(u'The aspect ratio for the custom constraint type.')], HRESULT, 'AspectRatio',
              ( ['retval', 'out'], POINTER(c_double), 'AspectRatio' )),
    COMMETHOD(['propput', helpstring(u'The aspect ratio for the custom constraint type.')], HRESULT, 'AspectRatio',
              ( ['in'], c_double, 'AspectRatio' )),
]
################################################################
## code template for INewRectangleFeedback implementation
##class INewRectangleFeedback_Impl(object):
##    def _get(self):
##        u"Indicates whether the rectangle's length is fixed."
##        #return SnapLength
##    def _set(self, SnapLength):
##        u"Indicates whether the rectangle's length is fixed."
##    SnapLength = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The angle of the current rectangle being constructed.'
##        #return Angle
##    def _set(self, Angle):
##        u'The angle of the current rectangle being constructed.'
##    Angle = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The width of the current rectangle being constructed.'
##        #return Width
##    def _set(self, Width):
##        u'The width of the current rectangle being constructed.'
##    Width = property(_get, _set, doc = _set.__doc__)
##
##    def SetPoint(self, Point):
##        u'Set the location of the second location.'
##        #return 
##
##    def _get(self):
##        u'The constraint on this rubberbander.'
##        #return constrain
##    def _set(self, constrain):
##        u'The constraint on this rubberbander.'
##    Constraint = property(_get, _set, doc = _set.__doc__)
##
##    def Stop(self, Point):
##        u'Stops the feedback and returns the shape.'
##        #return rectangle
##
##    def Start(self, Point):
##        u'Begins a normal feedback at the given point.'
##        #return 
##
##    def _get(self):
##        u'The length of the current rectangle being constructed.'
##        #return Length
##    def _set(self, Length):
##        u'The length of the current rectangle being constructed.'
##    Length = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether the rectangle is an envelope or angled.'
##        #return IsEnvelope
##    def _set(self, IsEnvelope):
##        u'Indicates whether the rectangle is an envelope or angled.'
##    IsEnvelope = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The aspect ratio for the custom constraint type.'
##        #return AspectRatio
##    def _set(self, AspectRatio):
##        u'The aspect ratio for the custom constraint type.'
##    AspectRatio = property(_get, _set, doc = _set.__doc__)
##

class IChartSymbol(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to properties common to all type of chart symbols.'
    _iid_ = GUID('{50317363-BD70-11D3-9F79-00C04F6BC709}')
    _idlflags_ = ['oleautomation']
IChartSymbol._methods_ = [
    COMMETHOD(['propget', helpstring(u'The value at the index position.')], HRESULT, 'Value',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(c_double), 'Value' )),
    COMMETHOD(['propput', helpstring(u'The value at the index position.')], HRESULT, 'Value',
              ( ['in'], c_int, 'index' ),
              ( ['in'], c_double, 'Value' )),
    COMMETHOD(['propget', helpstring(u'The maximum value.')], HRESULT, 'MaxValue',
              ( ['retval', 'out'], POINTER(c_double), 'Value' )),
    COMMETHOD(['propput', helpstring(u'The maximum value.')], HRESULT, 'MaxValue',
              ( ['in'], c_double, 'Value' )),
]
################################################################
## code template for IChartSymbol implementation
##class IChartSymbol_Impl(object):
##    def _get(self):
##        u'The maximum value.'
##        #return Value
##    def _set(self, Value):
##        u'The maximum value.'
##    MaxValue = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self, index):
##        u'The value at the index position.'
##        #return Value
##    def _set(self, index, Value):
##        u'The value at the index position.'
##    Value = property(_get, _set, doc = _set.__doc__)
##

IFontSize._methods_ = [
    COMMETHOD(['propget', helpstring(u'The font size in points.')], HRESULT, 'Size',
              ( ['retval', 'out'], POINTER(c_double), 'Size' )),
    COMMETHOD(['propput', helpstring(u'The font size in points.')], HRESULT, 'Size',
              ( ['in'], c_double, 'Size' )),
]
################################################################
## code template for IFontSize implementation
##class IFontSize_Impl(object):
##    def _get(self):
##        u'The font size in points.'
##        #return Size
##    def _set(self, Size):
##        u'The font size in points.'
##    Size = property(_get, _set, doc = _set.__doc__)
##

class ITextDrawSupport(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control how text strings are drawn.'
    _iid_ = GUID('{BF5BD367-5223-49C0-8DB0-FBC9D7CF36BB}')
    _idlflags_ = ['oleautomation']
ITextDrawSupport._methods_ = [
    COMMETHOD([helpstring(u'Get text the way it will be drawn. Optionally gives the positions of drawn characters in the original string of characters.')], HRESULT, 'GetDrawText',
              ( ['in'], BSTR, 'origText' ),
              ( ['out'], POINTER(BSTR), 'pParsedText' ),
              ( ['out'], POINTER(VARIANT), 'pPositions' )),
    COMMETHOD([helpstring(u'Gets an array of WKSPoints which represent the position at which each line of text is drawn; pGeometry must be a point.')], HRESULT, 'GetDrawPoints',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDC' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ITransformation), 'pTransform' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'pGeometry' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'drawPoints' )),
]
################################################################
## code template for ITextDrawSupport implementation
##class ITextDrawSupport_Impl(object):
##    def GetDrawText(self, origText):
##        u'Get text the way it will be drawn. Optionally gives the positions of drawn characters in the original string of characters.'
##        #return pParsedText, pPositions
##
##    def GetDrawPoints(self, hDC, pTransform, pGeometry):
##        u'Gets an array of WKSPoints which represent the position at which each line of text is drawn; pGeometry must be a point.'
##        #return drawPoints
##

ISymbolArray._methods_ = [
    COMMETHOD(['propget', helpstring(u'The number of symbols.')], HRESULT, 'SymbolCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'The symbol at the index position.')], HRESULT, 'Symbol',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(ISymbol)), 'Symbol' )),
    COMMETHOD(['propputref', helpstring(u'The symbol at the index position.')], HRESULT, 'Symbol',
              ( ['in'], c_int, 'index' ),
              ( ['in'], POINTER(ISymbol), 'Symbol' )),
    COMMETHOD([helpstring(u'Adds a symbol to the array.')], HRESULT, 'AddSymbol',
              ( ['in'], POINTER(ISymbol), 'Symbol' )),
    COMMETHOD([helpstring(u'Delete the given symbol.')], HRESULT, 'DeleteSymbol',
              ( ['in'], POINTER(ISymbol), 'Symbol' )),
    COMMETHOD([helpstring(u'Moves the given symbol to new index position.')], HRESULT, 'MoveSymbol',
              ( ['in'], POINTER(ISymbol), 'Symbol' ),
              ( ['in'], c_int, 'toIndex' )),
    COMMETHOD([helpstring(u'Removes all symbols from the array.')], HRESULT, 'ClearSymbols'),
]
################################################################
## code template for ISymbolArray implementation
##class ISymbolArray_Impl(object):
##    @property
##    def SymbolCount(self):
##        u'The number of symbols.'
##        #return Count
##
##    def MoveSymbol(self, Symbol, toIndex):
##        u'Moves the given symbol to new index position.'
##        #return 
##
##    def Symbol(self, index, Symbol):
##        u'The symbol at the index position.'
##        #return 
##
##    def DeleteSymbol(self, Symbol):
##        u'Delete the given symbol.'
##        #return 
##
##    def ClearSymbols(self):
##        u'Removes all symbols from the array.'
##        #return 
##
##    def AddSymbol(self, Symbol):
##        u'Adds a symbol to the array.'
##        #return 
##

class IOrientInteraction(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the parameters of the Orient Representation Tool.'
    _iid_ = GUID('{5FBC1277-93FC-4826-8B06-DF9C7ECA802D}')
    _idlflags_ = ['oleautomation']
IOrientInteraction._methods_ = [
    COMMETHOD(['propput', helpstring(u'Current angle of orientation.')], HRESULT, 'Angle',
              ( ['in'], c_double, 'Angle' )),
    COMMETHOD(['propget', helpstring(u'Current angle of orientation.')], HRESULT, 'Angle',
              ( ['retval', 'out'], POINTER(c_double), 'Angle' )),
    COMMETHOD(['propput', helpstring(u'Orient Representation Tool Mode.')], HRESULT, 'Mode',
              ( ['in'], esriOrientMode, 'Mode' )),
    COMMETHOD(['propget', helpstring(u'Orient Representation Tool Mode.')], HRESULT, 'Mode',
              ( ['retval', 'out'], POINTER(esriOrientMode), 'Mode' )),
]
################################################################
## code template for IOrientInteraction implementation
##class IOrientInteraction_Impl(object):
##    def _get(self):
##        u'Current angle of orientation.'
##        #return Angle
##    def _set(self, Angle):
##        u'Current angle of orientation.'
##    Angle = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Orient Representation Tool Mode.'
##        #return Mode
##    def _set(self, Mode):
##        u'Orient Representation Tool Mode.'
##    Mode = property(_get, _set, doc = _set.__doc__)
##

class ITimeDisplay(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Time Extent.'
    _iid_ = GUID('{2045F389-B48E-4CB6-A63B-D1232C1AF39D}')
    _idlflags_ = ['oleautomation']
ITimeDisplay._methods_ = [
    COMMETHOD(['propget', helpstring(u'Time Extent for which the data has to be displayed.')], HRESULT, 'TimeValue',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITimeValue)), 'timeExtent' )),
    COMMETHOD(['propput', helpstring(u'Time Extent for which the data has to be displayed.')], HRESULT, 'TimeValue',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITimeValue), 'timeExtent' )),
    COMMETHOD(['propget', helpstring(u'Time reference using which the data has to be displayed.')], HRESULT, 'TimeReference',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITimeReference)), 'TimeReference' )),
    COMMETHOD(['propput', helpstring(u'Time reference using which the data has to be displayed.')], HRESULT, 'TimeReference',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITimeReference), 'TimeReference' )),
]
################################################################
## code template for ITimeDisplay implementation
##class ITimeDisplay_Impl(object):
##    def _get(self):
##        u'Time Extent for which the data has to be displayed.'
##        #return timeExtent
##    def _set(self, timeExtent):
##        u'Time Extent for which the data has to be displayed.'
##    TimeValue = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Time reference using which the data has to be displayed.'
##        #return TimeReference
##    def _set(self, TimeReference):
##        u'Time reference using which the data has to be displayed.'
##    TimeReference = property(_get, _set, doc = _set.__doc__)
##

class HsvColor(CoClass):
    u'A color in the HSV (Hue, Saturation, Value) color system.'
    _reg_clsid_ = GUID('{7EE9C492-D123-11D0-8383-080009B996CC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IHsvColor(IColor):
    _case_insensitive_ = True
    u'Provides access to members that control the HSV color values.'
    _iid_ = GUID('{20CD40B3-8F3D-11D0-8590-0800091A2A72}')
    _idlflags_ = ['oleautomation']
HsvColor._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IHsvColor, IColor, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize]

class IFormattedTextSymbol(ITextSymbol):
    _case_insensitive_ = True
    u'Provides access to members that control the formatted text symbol.'
    _iid_ = GUID('{B65A3E72-2993-11D1-9A43-0080C7EC5C96}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriTextCase'
esriTCNormal = 0
esriTCLowercase = 1
esriTCAllCaps = 2
esriTCSmallCaps = 3
esriTextCase = c_int # enum
IFormattedTextSymbol._methods_ = [
    COMMETHOD(['propget', helpstring(u'The shadow color.')], HRESULT, 'ShadowColor',
              ( ['retval', 'out'], POINTER(POINTER(IColor)), 'ShadowColor' )),
    COMMETHOD(['propput', helpstring(u'The shadow color.')], HRESULT, 'ShadowColor',
              ( ['in'], POINTER(IColor), 'ShadowColor' )),
    COMMETHOD(['propget', helpstring(u'The shadow X offset.')], HRESULT, 'ShadowXOffset',
              ( ['retval', 'out'], POINTER(c_double), 'XOffset' )),
    COMMETHOD(['propput', helpstring(u'The shadow X offset.')], HRESULT, 'ShadowXOffset',
              ( ['in'], c_double, 'XOffset' )),
    COMMETHOD(['propget', helpstring(u'The shadow Y offset.')], HRESULT, 'ShadowYOffset',
              ( ['retval', 'out'], POINTER(c_double), 'YOffset' )),
    COMMETHOD(['propput', helpstring(u'The shadow Y offset.')], HRESULT, 'ShadowYOffset',
              ( ['in'], c_double, 'YOffset' )),
    COMMETHOD(['propget', helpstring(u'The text position.')], HRESULT, 'Position',
              ( ['retval', 'out'], POINTER(esriTextPosition), 'textPosition' )),
    COMMETHOD(['propput', helpstring(u'The text position.')], HRESULT, 'Position',
              ( ['in'], esriTextPosition, 'textPosition' )),
    COMMETHOD(['propget', helpstring(u'The text case.')], HRESULT, 'Case',
              ( ['retval', 'out'], POINTER(esriTextCase), 'textCase' )),
    COMMETHOD(['propput', helpstring(u'The text case.')], HRESULT, 'Case',
              ( ['in'], esriTextCase, 'textCase' )),
    COMMETHOD(['propget', helpstring(u'The character spacing.')], HRESULT, 'CharacterSpacing',
              ( ['retval', 'out'], POINTER(c_double), 'CharacterSpacing' )),
    COMMETHOD(['propput', helpstring(u'The character spacing.')], HRESULT, 'CharacterSpacing',
              ( ['in'], c_double, 'CharacterSpacing' )),
    COMMETHOD(['propget', helpstring(u'The character width.')], HRESULT, 'CharacterWidth',
              ( ['retval', 'out'], POINTER(c_double), 'CharacterWidth' )),
    COMMETHOD(['propput', helpstring(u'The character width.')], HRESULT, 'CharacterWidth',
              ( ['in'], c_double, 'CharacterWidth' )),
    COMMETHOD(['propget', helpstring(u'The word spacing.')], HRESULT, 'WordSpacing',
              ( ['retval', 'out'], POINTER(c_double), 'WordSpacing' )),
    COMMETHOD(['propput', helpstring(u'The word spacing.')], HRESULT, 'WordSpacing',
              ( ['in'], c_double, 'WordSpacing' )),
    COMMETHOD(['propget', helpstring(u'Indicates if kerning is on.')], HRESULT, 'Kerning',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Kerning' )),
    COMMETHOD(['propput', helpstring(u'Indicates if kerning is on.')], HRESULT, 'Kerning',
              ( ['in'], VARIANT_BOOL, 'Kerning' )),
    COMMETHOD(['propget', helpstring(u'The character leading.')], HRESULT, 'Leading',
              ( ['retval', 'out'], POINTER(c_double), 'Leading' )),
    COMMETHOD(['propput', helpstring(u'The character leading.')], HRESULT, 'Leading',
              ( ['in'], c_double, 'Leading' )),
    COMMETHOD(['propget', helpstring(u'The text direction.')], HRESULT, 'Direction',
              ( ['retval', 'out'], POINTER(esriTextDirection), 'textDirection' )),
    COMMETHOD(['propput', helpstring(u'The text direction.')], HRESULT, 'Direction',
              ( ['in'], esriTextDirection, 'textDirection' )),
    COMMETHOD(['propget', helpstring(u'The flip angle.')], HRESULT, 'FlipAngle',
              ( ['retval', 'out'], POINTER(c_double), 'FlipAngle' )),
    COMMETHOD(['propput', helpstring(u'The flip angle.')], HRESULT, 'FlipAngle',
              ( ['in'], c_double, 'FlipAngle' )),
    COMMETHOD(['propget', helpstring(u'The text background object.')], HRESULT, 'Background',
              ( ['retval', 'out'], POINTER(POINTER(ITextBackground)), 'Background' )),
    COMMETHOD(['propputref', helpstring(u'The text background object.')], HRESULT, 'Background',
              ( ['in'], POINTER(ITextBackground), 'Background' )),
    COMMETHOD(['propget', helpstring(u'Indicates if typesetting is used.')], HRESULT, 'TypeSetting',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'TypeSetting' )),
    COMMETHOD(['propput', helpstring(u'Indicates if typesetting is used.')], HRESULT, 'TypeSetting',
              ( ['in'], VARIANT_BOOL, 'TypeSetting' )),
    COMMETHOD(['propget', helpstring(u'The fill symbol.')], HRESULT, 'FillSymbol',
              ( ['retval', 'out'], POINTER(POINTER(IFillSymbol)), 'FillSymbol' )),
    COMMETHOD(['propputref', helpstring(u'The fill symbol.')], HRESULT, 'FillSymbol',
              ( ['in'], POINTER(IFillSymbol), 'FillSymbol' )),
]
################################################################
## code template for IFormattedTextSymbol implementation
##class IFormattedTextSymbol_Impl(object):
##    def _get(self):
##        u'The text case.'
##        #return textCase
##    def _set(self, textCase):
##        u'The text case.'
##    Case = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The word spacing.'
##        #return WordSpacing
##    def _set(self, WordSpacing):
##        u'The word spacing.'
##    WordSpacing = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The text direction.'
##        #return textDirection
##    def _set(self, textDirection):
##        u'The text direction.'
##    Direction = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The character width.'
##        #return CharacterWidth
##    def _set(self, CharacterWidth):
##        u'The character width.'
##    CharacterWidth = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The flip angle.'
##        #return FlipAngle
##    def _set(self, FlipAngle):
##        u'The flip angle.'
##    FlipAngle = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The shadow X offset.'
##        #return XOffset
##    def _set(self, XOffset):
##        u'The shadow X offset.'
##    ShadowXOffset = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The shadow Y offset.'
##        #return YOffset
##    def _set(self, YOffset):
##        u'The shadow Y offset.'
##    ShadowYOffset = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if typesetting is used.'
##        #return TypeSetting
##    def _set(self, TypeSetting):
##        u'Indicates if typesetting is used.'
##    TypeSetting = property(_get, _set, doc = _set.__doc__)
##
##    def FillSymbol(self, FillSymbol):
##        u'The fill symbol.'
##        #return 
##
##    def _get(self):
##        u'The shadow color.'
##        #return ShadowColor
##    def _set(self, ShadowColor):
##        u'The shadow color.'
##    ShadowColor = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if kerning is on.'
##        #return Kerning
##    def _set(self, Kerning):
##        u'Indicates if kerning is on.'
##    Kerning = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The character spacing.'
##        #return CharacterSpacing
##    def _set(self, CharacterSpacing):
##        u'The character spacing.'
##    CharacterSpacing = property(_get, _set, doc = _set.__doc__)
##
##    def Background(self, Background):
##        u'The text background object.'
##        #return 
##
##    def _get(self):
##        u'The character leading.'
##        #return Leading
##    def _set(self, Leading):
##        u'The character leading.'
##    Leading = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The text position.'
##        #return textPosition
##    def _set(self, textPosition):
##        u'The text position.'
##    Position = property(_get, _set, doc = _set.__doc__)
##

class ITimeDisplay2(ITimeDisplay):
    _case_insensitive_ = True
    u'Provides access to members that control the Time Extent.'
    _iid_ = GUID('{DAAD3027-1474-40E2-8908-E27CEF24A526}')
    _idlflags_ = ['oleautomation']
ITimeDisplay2._methods_ = [
    COMMETHOD(['propget', helpstring(u'Time relation for the time query.')], HRESULT, 'TimeRelation',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.esriTimeRelation), 'relation' )),
    COMMETHOD(['propput', helpstring(u'Time relation for the time query.')], HRESULT, 'TimeRelation',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.esriTimeRelation, 'relation' )),
]
################################################################
## code template for ITimeDisplay2 implementation
##class ITimeDisplay2_Impl(object):
##    def _get(self):
##        u'Time relation for the time query.'
##        #return relation
##    def _set(self, relation):
##        u'Time relation for the time query.'
##    TimeRelation = property(_get, _set, doc = _set.__doc__)
##

class MultiLayerLineSymbol(CoClass):
    u'A line symbol that contains one or more layers.'
    _reg_clsid_ = GUID('{7914E5FA-C892-11D0-8BB6-080009EE4E41}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IMultiLayerLineSymbol(ILineSymbol):
    _case_insensitive_ = True
    u'Provides access to members that control the multilayer line symbol.'
    _iid_ = GUID('{7914E5DE-C892-11D0-8BB6-080009EE4E41}')
    _idlflags_ = ['oleautomation']
MultiLayerLineSymbol._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMultiLayerLineSymbol, IMapLevel, ISymbol, ILayerVisible, ILayerColorLock, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySupport, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, ILayerTags]

IGeometricEffects._methods_ = [
    COMMETHOD(['propget', helpstring(u'Number of geometric effects.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'The geometric effect at the specified position.')], HRESULT, 'Element',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IGeometricEffect)), 'geomEffect' )),
    COMMETHOD([helpstring(u'Inserts a new geometric effect.')], HRESULT, 'Insert',
              ( ['in'], c_int, 'index' ),
              ( ['in'], POINTER(IGeometricEffect), 'geomEffect' )),
    COMMETHOD([helpstring(u'Adds a new geometric effect.')], HRESULT, 'Add',
              ( ['in'], POINTER(IGeometricEffect), 'geomEffect' )),
    COMMETHOD([helpstring(u'Removes a geometric effect.')], HRESULT, 'Remove',
              ( ['in'], c_int, 'index' )),
    COMMETHOD([helpstring(u'Removes all geometric effects.')], HRESULT, 'RemoveAll'),
]
################################################################
## code template for IGeometricEffects implementation
##class IGeometricEffects_Impl(object):
##    @property
##    def Count(self):
##        u'Number of geometric effects.'
##        #return Count
##
##    def Insert(self, index, geomEffect):
##        u'Inserts a new geometric effect.'
##        #return 
##
##    def Remove(self, index):
##        u'Removes a geometric effect.'
##        #return 
##
##    @property
##    def Element(self, index):
##        u'The geometric effect at the specified position.'
##        #return geomEffect
##
##    def RemoveAll(self):
##        u'Removes all geometric effects.'
##        #return 
##
##    def Add(self, geomEffect):
##        u'Adds a new geometric effect.'
##        #return 
##

class CartographicLineSymbol(CoClass):
    u'A line symbol for drawing solid or dashed lines.'
    _reg_clsid_ = GUID('{7914E5FB-C892-11D0-8BB6-080009EE4E41}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
CartographicLineSymbol._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ICartographicLineSymbol, IMapLevel, ISymbol, ILineProperties, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySupport, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, IDisplayName]

IRgbColor._methods_ = [
    COMMETHOD(['propput', helpstring(u'The red component of an IRgbColor (0-255).')], HRESULT, 'Red',
              ( ['in'], c_int, 'Red' )),
    COMMETHOD(['propget', helpstring(u'The red component of an IRgbColor (0-255).')], HRESULT, 'Red',
              ( ['retval', 'out'], POINTER(c_int), 'Red' )),
    COMMETHOD(['propput', helpstring(u'The green component of an IRgbColor (0-255).')], HRESULT, 'Green',
              ( ['in'], c_int, 'Green' )),
    COMMETHOD(['propget', helpstring(u'The green component of an IRgbColor (0-255).')], HRESULT, 'Green',
              ( ['retval', 'out'], POINTER(c_int), 'Green' )),
    COMMETHOD(['propput', helpstring(u'The blue component of an IRgbColor (0-255).')], HRESULT, 'Blue',
              ( ['in'], c_int, 'Blue' )),
    COMMETHOD(['propget', helpstring(u'The blue component of an IRgbColor (0-255).')], HRESULT, 'Blue',
              ( ['retval', 'out'], POINTER(c_int), 'Blue' )),
]
################################################################
## code template for IRgbColor implementation
##class IRgbColor_Impl(object):
##    def _get(self):
##        u'The blue component of an IRgbColor (0-255).'
##        #return Blue
##    def _set(self, Blue):
##        u'The blue component of an IRgbColor (0-255).'
##    Blue = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The green component of an IRgbColor (0-255).'
##        #return Green
##    def _set(self, Green):
##        u'The green component of an IRgbColor (0-255).'
##    Green = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The red component of an IRgbColor (0-255).'
##        #return Red
##    def _set(self, Red):
##        u'The red component of an IRgbColor (0-255).'
##    Red = property(_get, _set, doc = _set.__doc__)
##

class MarkerLineSymbol(CoClass):
    u'A line symbol composed of repeating markers.'
    _reg_clsid_ = GUID('{7914E5FD-C892-11D0-8BB6-080009EE4E41}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
MarkerLineSymbol._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMarkerLineSymbol, ICartographicLineSymbol, IMapLevel, ISymbol, ILineProperties, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySupport, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, IDisplayName]

class PictureLineSymbol(CoClass):
    u'A line symbol composed of either a BMP or an EMF picture.'
    _reg_clsid_ = GUID('{22C8C5A1-84FC-11D4-834D-0080C79F0371}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
PictureLineSymbol._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IPictureLineSymbol, IMapLevel, ISymbol, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySupport, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, IDisplayName]

class HashLineSymbol(CoClass):
    u'A line symbol for drawing hashed or slanted lines.'
    _reg_clsid_ = GUID('{7914E5FC-C892-11D0-8BB6-080009EE4E41}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
HashLineSymbol._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IHashLineSymbol, IMapLevel, ISymbol, ICartographicLineSymbol, ILineProperties, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySupport, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, IDisplayName]

IRubberBand._methods_ = [
    COMMETHOD([helpstring(u'Call in response to mouse down event to rubberband a new shape on the specified screen.')], HRESULT, 'TrackNew',
              ( ['in'], POINTER(IScreenDisplay), 'ScreenDisplay' ),
              ( ['in'], POINTER(ISymbol), 'Symbol' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry)), 'Geometry' )),
    COMMETHOD([helpstring(u'Indicates if to move or reshape an existing shape on the specified screen in response to a mouse down event.')], HRESULT, 'TrackExisting',
              ( ['in'], POINTER(IScreenDisplay), 'ScreenDisplay' ),
              ( ['in'], POINTER(ISymbol), 'Symbol' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'Geometry' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'completed' )),
]
################################################################
## code template for IRubberBand implementation
##class IRubberBand_Impl(object):
##    def TrackExisting(self, ScreenDisplay, Symbol, Geometry):
##        u'Indicates if to move or reshape an existing shape on the specified screen in response to a mouse down event.'
##        #return completed
##
##    def TrackNew(self, ScreenDisplay, Symbol):
##        u'Call in response to mouse down event to rubberband a new shape on the specified screen.'
##        #return Geometry
##

INewCircleFeedback._methods_ = [
    COMMETHOD([helpstring(u'Begins a circular feedback at the given point.')], HRESULT, 'Start',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
    COMMETHOD([helpstring(u'Stops the feedback and returns the circle.')], HRESULT, 'Stop',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ICircularArc)), 'Circle' )),
]
################################################################
## code template for INewCircleFeedback implementation
##class INewCircleFeedback_Impl(object):
##    def Start(self, Point):
##        u'Begins a circular feedback at the given point.'
##        #return 
##
##    def Stop(self):
##        u'Stops the feedback and returns the circle.'
##        #return Circle
##

class IBarChartSymbol(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control bar chart symbol properties.'
    _iid_ = GUID('{50317365-BD70-11D3-9F79-00C04F6BC709}')
    _idlflags_ = ['oleautomation']
IBarChartSymbol._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if the bars are oriented vertically.')], HRESULT, 'VerticalBars',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the bars are oriented vertically.')], HRESULT, 'VerticalBars',
              ( ['in'], VARIANT_BOOL, 'flag' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the axis are shown.')], HRESULT, 'ShowAxes',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the axis are shown.')], HRESULT, 'ShowAxes',
              ( ['in'], VARIANT_BOOL, 'flag' )),
    COMMETHOD(['propget', helpstring(u'The axis symbol.')], HRESULT, 'Axes',
              ( ['retval', 'out'], POINTER(POINTER(ILineSymbol)), 'Symbol' )),
    COMMETHOD(['propput', helpstring(u'The axis symbol.')], HRESULT, 'Axes',
              ( ['in'], POINTER(ILineSymbol), 'Symbol' )),
    COMMETHOD(['propget', helpstring(u'The width of each bar in points.')], HRESULT, 'Width',
              ( ['retval', 'out'], POINTER(c_double), 'Points' )),
    COMMETHOD(['propput', helpstring(u'The width of each bar in points.')], HRESULT, 'Width',
              ( ['in'], c_double, 'Points' )),
    COMMETHOD(['propget', helpstring(u'The spacing between bars in points.')], HRESULT, 'Spacing',
              ( ['retval', 'out'], POINTER(c_double), 'Points' )),
    COMMETHOD(['propput', helpstring(u'The spacing between bars in points.')], HRESULT, 'Spacing',
              ( ['in'], c_double, 'Points' )),
]
################################################################
## code template for IBarChartSymbol implementation
##class IBarChartSymbol_Impl(object):
##    def _get(self):
##        u'The spacing between bars in points.'
##        #return Points
##    def _set(self, Points):
##        u'The spacing between bars in points.'
##    Spacing = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the axis are shown.'
##        #return flag
##    def _set(self, flag):
##        u'Indicates if the axis are shown.'
##    ShowAxes = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The axis symbol.'
##        #return Symbol
##    def _set(self, Symbol):
##        u'The axis symbol.'
##    Axes = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the bars are oriented vertically.'
##        #return flag
##    def _set(self, flag):
##        u'Indicates if the bars are oriented vertically.'
##    VerticalBars = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The width of each bar in points.'
##        #return Points
##    def _set(self, Points):
##        u'The width of each bar in points.'
##    Width = property(_get, _set, doc = _set.__doc__)
##

class DisplayTransformation(CoClass):
    u'Display transformation class for converting from world to device units.'
    _reg_clsid_ = GUID('{EB16E596-B4F7-11D0-865F-0000F8751720}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IDisplayTransformationAdmin(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the DisplayTransformation.'
    _iid_ = GUID('{42817971-A1F4-11D3-92DC-00600802E603}')
    _idlflags_ = ['oleautomation']
class IRasterOutputSettings(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control Raster Output Settings.'
    _iid_ = GUID('{F13AAC6F-9C3D-11D3-A644-0008C7DF8DE1}')
    _idlflags_ = ['oleautomation']
class IConnectionPointContainer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{B196B284-BAB4-101A-B69C-00AA00341D07}')
    _idlflags_ = []
class IDelayEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control Delay Events.'
    _iid_ = GUID('{5BA46487-1D16-42B8-847B-B7B9C8100B13}')
    _idlflags_ = ['oleautomation']
class ITransformEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control Transform Events.'
    _iid_ = GUID('{E6BDB001-4D35-11D0-98BE-00805F7CED21}')
    _idlflags_ = ['oleautomation']
DisplayTransformation._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ITransformationGEN, IDisplayTransformation, IDisplayTransformationAdmin, IDisplayTransformationScales, IRasterOutputSettings, IOutputRasterSettings, comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ITransformation, IConnectionPointContainer, IDelayEvents]
DisplayTransformation._outgoing_interfaces_ = [ITransformEvents]

ISimpleLineCallout._methods_ = [
    COMMETHOD(['propget', helpstring(u'The geometry used for the Callout.')], HRESULT, 'LineGeometry',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry)), 'Geometry' )),
    COMMETHOD(['propput', helpstring(u'The geometry used for the Callout.')], HRESULT, 'LineGeometry',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'Geometry' )),
    COMMETHOD(['propget', helpstring(u'The line symbol used for the Callout.')], HRESULT, 'LineSymbol',
              ( ['retval', 'out'], POINTER(POINTER(ILineSymbol)), 'LineSymbol' )),
    COMMETHOD(['propput', helpstring(u'The line symbol used for the Callout.')], HRESULT, 'LineSymbol',
              ( ['in'], POINTER(ILineSymbol), 'LineSymbol' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the auto-snap property is enabled.')], HRESULT, 'AutoSnap',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the auto-snap property is enabled.')], HRESULT, 'AutoSnap',
              ( ['in'], VARIANT_BOOL, 'flag' )),
]
################################################################
## code template for ISimpleLineCallout implementation
##class ISimpleLineCallout_Impl(object):
##    def _get(self):
##        u'The line symbol used for the Callout.'
##        #return LineSymbol
##    def _set(self, LineSymbol):
##        u'The line symbol used for the Callout.'
##    LineSymbol = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the auto-snap property is enabled.'
##        #return flag
##    def _set(self, flag):
##        u'Indicates if the auto-snap property is enabled.'
##    AutoSnap = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The geometry used for the Callout.'
##        #return Geometry
##    def _set(self, Geometry):
##        u'The geometry used for the Callout.'
##    LineGeometry = property(_get, _set, doc = _set.__doc__)
##

class ScreenDisplay(CoClass):
    u'Display class for drawing to window.'
    _reg_clsid_ = GUID('{E6BDB100-4D35-11D0-98BE-00805F7CED21}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IScreenCacheManager(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u"Provides access to a ScreenDisplay's caches."
    _iid_ = GUID('{7B3572F2-57A7-46B3-AF86-9C9BCA1C8F15}')
    _idlflags_ = ['oleautomation']
class IScreenInvalidate(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u"Provides access to a ScreenDisplay's refresh methods."
    _iid_ = GUID('{C1CCBFC2-6722-49F0-9242-BA2F312E24BF}')
    _idlflags_ = ['oleautomation']
class IDynamicScreenDisplay(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to dynamic screen display.'
    _iid_ = GUID('{D2DA3EC1-DA41-4629-9347-2CC09CE589FA}')
    _idlflags_ = ['oleautomation']
class IDisplayFiltersControl(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control filters the Display.'
    _iid_ = GUID('{37CF5545-8233-4941-B171-E623F74A2A74}')
    _idlflags_ = ['oleautomation']
ScreenDisplay._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IScreenDisplay, IScreenDisplay2, IScreenDisplay3, IScreenDisplayBasemap, IScreenDisplayOverlays, IScreenCacheManager, IScreenInvalidate, IDisplay, IDraw, ITransformEvents, IConnectionPointContainer, IDynamicScreenDisplay, IScreenDisplayZoom, IDisplayFiltersControl, ITimeDisplay, ITimeDisplay2]
ScreenDisplay._outgoing_interfaces_ = [IDisplayEvents, ITimeDisplayEvents]


# values for enumeration 'esriPictureSymbolOptions'
esriPSORasterize = 0
esriPSORasterizeIfRasterData = 1
esriPSOVectorize = 2
esriPictureSymbolOptions = c_int # enum
class IMonitorSettings(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the monitor settings.'
    _iid_ = GUID('{9DB25FDF-3C75-11D2-AAF6-00C04FA334B3}')
    _idlflags_ = ['oleautomation']
IMonitorSettings._methods_ = [
    COMMETHOD(['propput', helpstring(u'The name of the monitor.')], HRESULT, 'MonitorName',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD(['propget', helpstring(u'The name of the monitor.')], HRESULT, 'MonitorName',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propput', helpstring(u'The gamma value of the monitor. ( 1 <= gamma value <= 3).')], HRESULT, 'Gamma',
              ( ['in'], c_double, 'Gamma' )),
    COMMETHOD(['propget', helpstring(u'The gamma value of the monitor. ( 1 <= gamma value <= 3).')], HRESULT, 'Gamma',
              ( ['retval', 'out'], POINTER(c_double), 'Gamma' )),
    COMMETHOD(['propput', helpstring(u'The white point name of the monitor.')], HRESULT, 'WhitePointName',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD(['propget', helpstring(u'The white point name of the monitor.')], HRESULT, 'WhitePointName',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propput', helpstring(u'The phosphor name of the monitor.')], HRESULT, 'PhosphorName',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD(['propget', helpstring(u'The phosphor name of the monitor.')], HRESULT, 'PhosphorName',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD([helpstring(u'The white point of the monitor (0 <= x <= 1, 0 <= y <= 1.')], HRESULT, 'SetWhitePoint',
              ( ['in'], c_double, 'x' ),
              ( ['in'], c_double, 'y' )),
    COMMETHOD([helpstring(u'The white point of the monitor (0 <= x <= 1, 0 <= y <= 1.')], HRESULT, 'GetWhitePoint',
              ( ['out'], POINTER(c_double), 'x' ),
              ( ['out'], POINTER(c_double), 'y' )),
    COMMETHOD([helpstring(u'The red point of the monitor (0 <= x <= 1, 0 <= y <= 1.')], HRESULT, 'SetRedPoint',
              ( ['in'], c_double, 'x' ),
              ( ['in'], c_double, 'y' )),
    COMMETHOD([helpstring(u'The red point of the monitor (0 <= x <= 1, 0 <= y <= 1.')], HRESULT, 'GetRedPoint',
              ( ['out'], POINTER(c_double), 'x' ),
              ( ['out'], POINTER(c_double), 'y' )),
    COMMETHOD([helpstring(u'The green point of the monitor (0 <= x <= 1, 0 <= y <= 1.')], HRESULT, 'SetGreenPoint',
              ( ['in'], c_double, 'x' ),
              ( ['in'], c_double, 'y' )),
    COMMETHOD([helpstring(u'The green point of the monitor (0 <= x <= 1, 0 <= y <= 1.')], HRESULT, 'GetGreenPoint',
              ( ['out'], POINTER(c_double), 'x' ),
              ( ['out'], POINTER(c_double), 'y' )),
    COMMETHOD([helpstring(u'The blue point of the monitor (0 <= x <= 1, 0 <= y <= 1.')], HRESULT, 'SetBluePoint',
              ( ['in'], c_double, 'x' ),
              ( ['in'], c_double, 'y' )),
    COMMETHOD([helpstring(u'The blue point of the monitor (0 <= x <= 1, 0 <= y <= 1.')], HRESULT, 'GetBluePoint',
              ( ['out'], POINTER(c_double), 'x' ),
              ( ['out'], POINTER(c_double), 'y' )),
]
################################################################
## code template for IMonitorSettings implementation
##class IMonitorSettings_Impl(object):
##    def GetBluePoint(self):
##        u'The blue point of the monitor (0 <= x <= 1, 0 <= y <= 1.'
##        #return x, y
##
##    def SetGreenPoint(self, x, y):
##        u'The green point of the monitor (0 <= x <= 1, 0 <= y <= 1.'
##        #return 
##
##    def GetGreenPoint(self):
##        u'The green point of the monitor (0 <= x <= 1, 0 <= y <= 1.'
##        #return x, y
##
##    def GetWhitePoint(self):
##        u'The white point of the monitor (0 <= x <= 1, 0 <= y <= 1.'
##        #return x, y
##
##    def SetWhitePoint(self, x, y):
##        u'The white point of the monitor (0 <= x <= 1, 0 <= y <= 1.'
##        #return 
##
##    def _get(self):
##        u'The phosphor name of the monitor.'
##        #return Name
##    def _set(self, Name):
##        u'The phosphor name of the monitor.'
##    PhosphorName = property(_get, _set, doc = _set.__doc__)
##
##    def SetRedPoint(self, x, y):
##        u'The red point of the monitor (0 <= x <= 1, 0 <= y <= 1.'
##        #return 
##
##    def _get(self):
##        u'The white point name of the monitor.'
##        #return Name
##    def _set(self, Name):
##        u'The white point name of the monitor.'
##    WhitePointName = property(_get, _set, doc = _set.__doc__)
##
##    def GetRedPoint(self):
##        u'The red point of the monitor (0 <= x <= 1, 0 <= y <= 1.'
##        #return x, y
##
##    def _get(self):
##        u'The name of the monitor.'
##        #return Name
##    def _set(self, Name):
##        u'The name of the monitor.'
##    MonitorName = property(_get, _set, doc = _set.__doc__)
##
##    def SetBluePoint(self, x, y):
##        u'The blue point of the monitor (0 <= x <= 1, 0 <= y <= 1.'
##        #return 
##
##    def _get(self):
##        u'The gamma value of the monitor. ( 1 <= gamma value <= 3).'
##        #return Gamma
##    def _set(self, Gamma):
##        u'The gamma value of the monitor. ( 1 <= gamma value <= 3).'
##    Gamma = property(_get, _set, doc = _set.__doc__)
##

IHsvColor._methods_ = [
    COMMETHOD(['propput', helpstring(u'The hue component of an IhsvColor (0-360).')], HRESULT, 'Hue',
              ( ['in'], c_int, 'Hue' )),
    COMMETHOD(['propget', helpstring(u'The hue component of an IhsvColor (0-360).')], HRESULT, 'Hue',
              ( ['retval', 'out'], POINTER(c_int), 'Hue' )),
    COMMETHOD(['propput', helpstring(u'The saturation component of an IhsvColor (0-100).')], HRESULT, 'Saturation',
              ( ['in'], c_int, 'Saturation' )),
    COMMETHOD(['propget', helpstring(u'The saturation component of an IhsvColor (0-100).')], HRESULT, 'Saturation',
              ( ['retval', 'out'], POINTER(c_int), 'Saturation' )),
    COMMETHOD(['propput', helpstring(u'The value component of an IhsvColor (0-100).')], HRESULT, 'Value',
              ( ['in'], c_int, 'Value' )),
    COMMETHOD(['propget', helpstring(u'The value component of an IhsvColor (0-100).')], HRESULT, 'Value',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
]
################################################################
## code template for IHsvColor implementation
##class IHsvColor_Impl(object):
##    def _get(self):
##        u'The hue component of an IhsvColor (0-360).'
##        #return Hue
##    def _set(self, Hue):
##        u'The hue component of an IhsvColor (0-360).'
##    Hue = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The saturation component of an IhsvColor (0-100).'
##        #return Saturation
##    def _set(self, Saturation):
##        u'The saturation component of an IhsvColor (0-100).'
##    Saturation = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The value component of an IhsvColor (0-100).'
##        #return Value
##    def _set(self, Value):
##        u'The value component of an IhsvColor (0-100).'
##    Value = property(_get, _set, doc = _set.__doc__)
##

IColorRampElements._methods_ = [
    COMMETHOD(['propget', helpstring(u'The ColorRamp elements count.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'The ColorRamp element at the specified position.')], HRESULT, 'Element',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IColorRamp)), 'ppColorRamp' )),
    COMMETHOD([helpstring(u'Remove ColorRamp element at the specified position.')], HRESULT, 'Remove',
              ( ['in'], c_int, 'index' )),
    COMMETHOD([helpstring(u'Remove all ColorRamp elements.')], HRESULT, 'RemoveAll'),
    COMMETHOD([helpstring(u'Add a ColorRamp element.')], HRESULT, 'Add',
              ( ['in'], POINTER(IColorRamp), 'pColorRamp' )),
    COMMETHOD([helpstring(u'Add a ColorRamp element at the specified posiiton.')], HRESULT, 'Insert',
              ( ['in'], c_int, 'index' ),
              ( ['in'], POINTER(IColorRamp), 'pColorRamp' )),
]
################################################################
## code template for IColorRampElements implementation
##class IColorRampElements_Impl(object):
##    @property
##    def Count(self):
##        u'The ColorRamp elements count.'
##        #return Count
##
##    def Insert(self, index, pColorRamp):
##        u'Add a ColorRamp element at the specified posiiton.'
##        #return 
##
##    def Remove(self, index):
##        u'Remove ColorRamp element at the specified position.'
##        #return 
##
##    @property
##    def Element(self, index):
##        u'The ColorRamp element at the specified position.'
##        #return ppColorRamp
##
##    def RemoveAll(self):
##        u'Remove all ColorRamp elements.'
##        #return 
##
##    def Add(self, pColorRamp):
##        u'Add a ColorRamp element.'
##        #return 
##

IFieldOverrides._methods_ = [
    COMMETHOD([helpstring(u'Creates an explicit override with field content. To erase an existing field override, pass in blank field name.')], HRESULT, 'Add',
              ( ['in'], POINTER(IGraphicAttributes), 'Attributes' ),
              ( ['in'], c_int, 'graphicAttributeIndex' ),
              ( ['in'], BSTR, 'FieldName' )),
    COMMETHOD([helpstring(u'Resets the override collection, before calling Next.')], HRESULT, 'Reset'),
    COMMETHOD([helpstring(u'Accesses the next field override in the collection.')], HRESULT, 'Next',
              ( ['retval', 'out'], POINTER(POINTER(IFieldOverride)), 'override' )),
]
################################################################
## code template for IFieldOverrides implementation
##class IFieldOverrides_Impl(object):
##    def Reset(self):
##        u'Resets the override collection, before calling Next.'
##        #return 
##
##    def Add(self, Attributes, graphicAttributeIndex, FieldName):
##        u'Creates an explicit override with field content. To erase an existing field override, pass in blank field name.'
##        #return 
##
##    def Next(self):
##        u'Accesses the next field override in the collection.'
##        #return override
##

class IPictureSymbolEnvironment(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the environment for picture symbol properties.'
    _iid_ = GUID('{C6778756-976C-4761-A3A7-661B2446A7BB}')
    _idlflags_ = ['oleautomation']
IPictureSymbolEnvironment._methods_ = [
    COMMETHOD(['propget', helpstring(u'Output options for layers with picture symbols.')], HRESULT, 'PictureSymbolOptions',
              ( ['retval', 'out'], POINTER(esriPictureSymbolOptions), 'options' )),
    COMMETHOD(['propput', helpstring(u'Output options for layers with picture symbols.')], HRESULT, 'PictureSymbolOptions',
              ( ['in'], esriPictureSymbolOptions, 'options' )),
]
################################################################
## code template for IPictureSymbolEnvironment implementation
##class IPictureSymbolEnvironment_Impl(object):
##    def _get(self):
##        u'Output options for layers with picture symbols.'
##        #return options
##    def _set(self, options):
##        u'Output options for layers with picture symbols.'
##    PictureSymbolOptions = property(_get, _set, doc = _set.__doc__)
##

class IEnumConnectionPoints(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{B196B285-BAB4-101A-B69C-00AA00341D07}')
    _idlflags_ = []
class IConnectionPoint(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{B196B286-BAB4-101A-B69C-00AA00341D07}')
    _idlflags_ = []
IConnectionPointContainer._methods_ = [
    COMMETHOD([], HRESULT, 'EnumConnectionPoints',
              ( ['out'], POINTER(POINTER(IEnumConnectionPoints)), 'ppEnum' )),
    COMMETHOD([], HRESULT, 'FindConnectionPoint',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'riid' ),
              ( ['out'], POINTER(POINTER(IConnectionPoint)), 'ppCP' )),
]
################################################################
## code template for IConnectionPointContainer implementation
##class IConnectionPointContainer_Impl(object):
##    def EnumConnectionPoints(self):
##        '-no docstring-'
##        #return ppEnum
##
##    def FindConnectionPoint(self, riid):
##        '-no docstring-'
##        #return ppCP
##


# values for enumeration 'esriClippingMethod'
esriClipNoClipping = -1
esriClipBasicClipping = 0
esriClipRemoveCenterOutside = 1
esriClipRemoveBoxOutside = 2
esriClippingMethod = c_int # enum
IClippingMethod._methods_ = [
    COMMETHOD(['propget', helpstring(u'Method to be used for clipping.')], HRESULT, 'ClippingMethod',
              ( ['retval', 'out'], POINTER(esriClippingMethod), 'method' )),
]
################################################################
## code template for IClippingMethod implementation
##class IClippingMethod_Impl(object):
##    @property
##    def ClippingMethod(self):
##        u'Method to be used for clipping.'
##        #return method
##

class SimpleDisplay(CoClass):
    u'Display class for drawing to any HDC.'
    _reg_clsid_ = GUID('{E6BDB101-4D35-11D0-98BE-00805F7CED21}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
SimpleDisplay._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDisplay, IDisplayFiltersControl, IDraw, IConnectionPointContainer, ITimeDisplay, ITimeDisplay2]
SimpleDisplay._outgoing_interfaces_ = [IDisplayEvents, ITimeDisplayEvents]

class SimpleMarkerSymbol(CoClass):
    u'A marker symbol comprised of a predefined set of styles.'
    _reg_clsid_ = GUID('{7914E5FE-C892-11D0-8BB6-080009EE4E41}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class ISymbolRotation(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the symbol rotation properties.'
    _iid_ = GUID('{84A1F5C2-D0A1-4E45-842B-149E857E8A9C}')
    _idlflags_ = ['oleautomation']
SimpleMarkerSymbol._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ISimpleMarkerSymbol, IMapLevel, ISymbol, ISymbolRotation, IMarkerMask, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySupport, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, IDisplayName, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize]

class IFontsInSymbolsEnvironment(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the environment for fonts behavior in symbols.'
    _iid_ = GUID('{3B2DE5E8-95CD-4C41-97FE-8FB8884DCBE0}')
    _idlflags_ = ['oleautomation']
IFontsInSymbolsEnvironment._methods_ = [
    COMMETHOD(['propget', helpstring(u'Disabling fonts antialiasing in symbols.')], HRESULT, 'DisableFontAntialiasing',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bDisable' )),
    COMMETHOD(['propput', helpstring(u'Disabling fonts antialiasing in symbols.')], HRESULT, 'DisableFontAntialiasing',
              ( ['in'], VARIANT_BOOL, 'bDisable' )),
]
################################################################
## code template for IFontsInSymbolsEnvironment implementation
##class IFontsInSymbolsEnvironment_Impl(object):
##    def _get(self):
##        u'Disabling fonts antialiasing in symbols.'
##        #return bDisable
##    def _set(self, bDisable):
##        u'Disabling fonts antialiasing in symbols.'
##    DisableFontAntialiasing = property(_get, _set, doc = _set.__doc__)
##

INewEnvelopeFeedback2._methods_ = [
    COMMETHOD([helpstring(u'Begins a normal feedback at the given point.')], HRESULT, 'Start',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
    COMMETHOD(['propget', helpstring(u'The constraint on this rubberbander.')], HRESULT, 'Constraint',
              ( ['retval', 'out'], POINTER(esriEnvelopeConstraints), 'constrain' )),
    COMMETHOD(['propput', helpstring(u'The constraint on this rubberbander.')], HRESULT, 'Constraint',
              ( ['in'], esriEnvelopeConstraints, 'constrain' )),
    COMMETHOD(['propget', helpstring(u'The aspect ratio for the custom constraint type.')], HRESULT, 'AspectRatio',
              ( ['retval', 'out'], POINTER(c_double), 'AspectRatio' )),
    COMMETHOD(['propput', helpstring(u'The aspect ratio for the custom constraint type.')], HRESULT, 'AspectRatio',
              ( ['in'], c_double, 'AspectRatio' )),
    COMMETHOD([helpstring(u'Stops the feedback and returns the shape. Shape may not be an envelope if the display is rotated.')], HRESULT, 'Stop',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry)), 'envelope' )),
]
################################################################
## code template for INewEnvelopeFeedback2 implementation
##class INewEnvelopeFeedback2_Impl(object):
##    def Start(self, Point):
##        u'Begins a normal feedback at the given point.'
##        #return 
##
##    def _get(self):
##        u'The aspect ratio for the custom constraint type.'
##        #return AspectRatio
##    def _set(self, AspectRatio):
##        u'The aspect ratio for the custom constraint type.'
##    AspectRatio = property(_get, _set, doc = _set.__doc__)
##
##    def Stop(self):
##        u'Stops the feedback and returns the shape. Shape may not be an envelope if the display is rotated.'
##        #return envelope
##
##    def _get(self):
##        u'The constraint on this rubberbander.'
##        #return constrain
##    def _set(self, constrain):
##        u'The constraint on this rubberbander.'
##    Constraint = property(_get, _set, doc = _set.__doc__)
##

INewCircleFeedback2._methods_ = [
    COMMETHOD(['propputref', helpstring(u'Set the symbol for the radius line.')], HRESULT, 'RadiusLineSymbol',
              ( ['in'], POINTER(ISymbol), 'ppSymbol' )),
    COMMETHOD(['propget', helpstring(u'Set the symbol for the radius line.')], HRESULT, 'RadiusLineSymbol',
              ( ['retval', 'out'], POINTER(POINTER(ISymbol)), 'ppSymbol' )),
    COMMETHOD(['propget', helpstring(u'Get the current circle being constructed.')], HRESULT, 'Circle',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ICircularArc)), 'ppCircle' )),
]
################################################################
## code template for INewCircleFeedback2 implementation
##class INewCircleFeedback2_Impl(object):
##    @property
##    def RadiusLineSymbol(self, ppSymbol):
##        u'Set the symbol for the radius line.'
##        #return 
##
##    @property
##    def Circle(self):
##        u'Get the current circle being constructed.'
##        #return ppCircle
##

IEnumConnectionPoints._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteNext',
              ( ['in'], c_ulong, 'cConnections' ),
              ( ['out'], POINTER(POINTER(IConnectionPoint)), 'ppCP' ),
              ( ['out'], POINTER(c_ulong), 'pcFetched' )),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'cConnections' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IEnumConnectionPoints)), 'ppEnum' )),
]
################################################################
## code template for IEnumConnectionPoints implementation
##class IEnumConnectionPoints_Impl(object):
##    def Reset(self):
##        '-no docstring-'
##        #return 
##
##    def Skip(self, cConnections):
##        '-no docstring-'
##        #return 
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppEnum
##
##    def RemoteNext(self, cConnections):
##        '-no docstring-'
##        #return ppCP, pcFetched
##

ITransformEvents._methods_ = [
    COMMETHOD([helpstring(u'Notifies clients when the bounds is updated.')], HRESULT, 'BoundsUpdated',
              ( [], POINTER(IDisplayTransformation), 'sender' )),
    COMMETHOD([helpstring(u'Notifies clients when the visible bounds is updated.')], HRESULT, 'VisibleBoundsUpdated',
              ( [], POINTER(IDisplayTransformation), 'sender' ),
              ( [], VARIANT_BOOL, 'sizeChanged' )),
    COMMETHOD([helpstring(u'Notifies clients when the device frame is updated.')], HRESULT, 'DeviceFrameUpdated',
              ( [], POINTER(IDisplayTransformation), 'sender' ),
              ( [], VARIANT_BOOL, 'sizeChanged' )),
    COMMETHOD([helpstring(u'Notifies clients when the resolution is updated.')], HRESULT, 'ResolutionUpdated',
              ( [], POINTER(IDisplayTransformation), 'sender' )),
    COMMETHOD([helpstring(u'Notifies clients when the rotation angle is updated.')], HRESULT, 'RotationUpdated',
              ( [], POINTER(IDisplayTransformation), 'sender' )),
    COMMETHOD([helpstring(u'Notifies clients when the units are updated.')], HRESULT, 'UnitsUpdated',
              ( [], POINTER(IDisplayTransformation), 'sender' )),
]
################################################################
## code template for ITransformEvents implementation
##class ITransformEvents_Impl(object):
##    def VisibleBoundsUpdated(self, sender, sizeChanged):
##        u'Notifies clients when the visible bounds is updated.'
##        #return 
##
##    def BoundsUpdated(self, sender):
##        u'Notifies clients when the bounds is updated.'
##        #return 
##
##    def ResolutionUpdated(self, sender):
##        u'Notifies clients when the resolution is updated.'
##        #return 
##
##    def RotationUpdated(self, sender):
##        u'Notifies clients when the rotation angle is updated.'
##        #return 
##
##    def UnitsUpdated(self, sender):
##        u'Notifies clients when the units are updated.'
##        #return 
##
##    def DeviceFrameUpdated(self, sender, sizeChanged):
##        u'Notifies clients when the device frame is updated.'
##        #return 
##

IResizeEnvelopeFeedback._methods_ = [
    COMMETHOD([helpstring(u'Begins a resize feedback of the given shape.')], HRESULT, 'Start',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'envelope' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
    COMMETHOD(['propput', helpstring(u'The edge to rubberband.')], HRESULT, 'ResizeEdge',
              ( ['in'], esriEnvelopeEdge, 'edge' )),
    COMMETHOD(['propget', helpstring(u'The edge to rubberband.')], HRESULT, 'ResizeEdge',
              ( ['retval', 'out'], POINTER(esriEnvelopeEdge), 'edge' )),
    COMMETHOD([helpstring(u'Stops the feedback and returns the shape.')], HRESULT, 'Stop',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'envelope' )),
    COMMETHOD(['propget', helpstring(u'The constraint on this rubberbander.')], HRESULT, 'Constraint',
              ( ['retval', 'out'], POINTER(esriEnvelopeConstraints), 'constrain' )),
    COMMETHOD(['propput', helpstring(u'The constraint on this rubberbander.')], HRESULT, 'Constraint',
              ( ['in'], esriEnvelopeConstraints, 'constrain' )),
    COMMETHOD(['propget', helpstring(u'The aspect ratio for the custom constraint type.')], HRESULT, 'AspectRatio',
              ( ['retval', 'out'], POINTER(c_double), 'AspectRatio' )),
    COMMETHOD(['propput', helpstring(u'The aspect ratio for the custom constraint type.')], HRESULT, 'AspectRatio',
              ( ['in'], c_double, 'AspectRatio' )),
]
################################################################
## code template for IResizeEnvelopeFeedback implementation
##class IResizeEnvelopeFeedback_Impl(object):
##    def Start(self, envelope, Point):
##        u'Begins a resize feedback of the given shape.'
##        #return 
##
##    def _get(self):
##        u'The aspect ratio for the custom constraint type.'
##        #return AspectRatio
##    def _set(self, AspectRatio):
##        u'The aspect ratio for the custom constraint type.'
##    AspectRatio = property(_get, _set, doc = _set.__doc__)
##
##    def Stop(self):
##        u'Stops the feedback and returns the shape.'
##        #return envelope
##
##    def _get(self):
##        u'The edge to rubberband.'
##        #return edge
##    def _set(self, edge):
##        u'The edge to rubberband.'
##    ResizeEdge = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The constraint on this rubberbander.'
##        #return constrain
##    def _set(self, constrain):
##        u'The constraint on this rubberbander.'
##    Constraint = property(_get, _set, doc = _set.__doc__)
##

class PictureFillSymbol(CoClass):
    u'A fill symbol based on either a BMP or an EMF picture.'
    _reg_clsid_ = GUID('{D842B082-330C-11D2-9168-0000F87808EE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
PictureFillSymbol._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IPictureFillSymbol, IMapLevel, ISymbol, IFillProperties, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySupport, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, IDisplayName, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLVersionSupport]


# values for enumeration 'esriOutlineType'
esriOutlineBox = 1
esriOutlineOrientedBox = 2
esriOutlineExact = 3
esriOutlineType = c_int # enum

# values for enumeration 'esriOutlineOption'
esriOutlineNoOption = 0
esriOutlineConvex = 1
esriOutlineWithoutHoles = 2
esriOutlineOption = c_int # enum
IGraphicsOutline._methods_ = [
    COMMETHOD([helpstring(u'Tests if a point is located on the graphics outline.')], HRESULT, 'HitTest',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' ),
              ( ['in'], c_double, 'tolerance' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'hit' )),
    COMMETHOD([helpstring(u'Constructs the entire drawing outline of a graphics.')], HRESULT, 'GetAllOutlineParts',
              ( ['in'], esriOutlineType, 'Type' ),
              ( ['in'], esriOutlineOption, 'option' ),
              ( ['in'], c_double, 'buffer' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'ClipEnvelope' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry)), 'Outline' )),
    COMMETHOD([helpstring(u'Resets the collection of drawing outline parts to the beginning, before calling NextOutlinePart. To be used when drawing outline of a graphics is accessed part by part.')], HRESULT, 'Reset',
              ( ['in'], esriOutlineType, 'Type' ),
              ( ['in'], esriOutlineOption, 'option' ),
              ( ['in'], c_double, 'buffer' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'ClipEnvelope' )),
    COMMETHOD([helpstring(u'Hands back the next drawing outline part. It is necessary to call the Reset method before iterating with the NextOutlinePart method.')], HRESULT, 'NextOutlinePart',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry)), 'outlinePart' )),
]
################################################################
## code template for IGraphicsOutline implementation
##class IGraphicsOutline_Impl(object):
##    def HitTest(self, Point, tolerance):
##        u'Tests if a point is located on the graphics outline.'
##        #return hit
##
##    def Reset(self, Type, option, buffer, ClipEnvelope):
##        u'Resets the collection of drawing outline parts to the beginning, before calling NextOutlinePart. To be used when drawing outline of a graphics is accessed part by part.'
##        #return 
##
##    def NextOutlinePart(self):
##        u'Hands back the next drawing outline part. It is necessary to call the Reset method before iterating with the NextOutlinePart method.'
##        #return outlinePart
##
##    def GetAllOutlineParts(self, Type, option, buffer, ClipEnvelope):
##        u'Constructs the entire drawing outline of a graphics.'
##        #return Outline
##

class IOffsetInteraction(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the parameters of the Offset Representation Tool.'
    _iid_ = GUID('{0EB01873-1CA1-4A81-A9A1-91E1C2017856}')
    _idlflags_ = ['oleautomation']
IOffsetInteraction._methods_ = [
    COMMETHOD(['propput', helpstring(u'Current offset expressed in points.')], HRESULT, 'Offset',
              ( ['in'], c_double, 'Offset' )),
    COMMETHOD(['propget', helpstring(u'Current offset expressed in points.')], HRESULT, 'Offset',
              ( ['retval', 'out'], POINTER(c_double), 'Offset' )),
    COMMETHOD(['propput', helpstring(u'Current offset expressed in map units.')], HRESULT, 'MapOffset',
              ( ['in'], c_double, 'MapOffset' )),
    COMMETHOD(['propget', helpstring(u'Current offset expressed in map units.')], HRESULT, 'MapOffset',
              ( ['retval', 'out'], POINTER(c_double), 'MapOffset' )),
]
################################################################
## code template for IOffsetInteraction implementation
##class IOffsetInteraction_Impl(object):
##    def _get(self):
##        u'Current offset expressed in map units.'
##        #return MapOffset
##    def _set(self, MapOffset):
##        u'Current offset expressed in map units.'
##    MapOffset = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Current offset expressed in points.'
##        #return Offset
##    def _set(self, Offset):
##        u'Current offset expressed in points.'
##    Offset = property(_get, _set, doc = _set.__doc__)
##

class FontAttributeItalic(CoClass):
    u'Controls whether the text will be drawn in italics.'
    _reg_clsid_ = GUID('{03C26B18-59EC-4481-A5D7-B77AE161961E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IFontAttribute(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to FontAttribute properties.'
    _iid_ = GUID('{A37E7145-E00D-43F3-BE13-7E1CC9348329}')
    _idlflags_ = ['oleautomation']
class IItalic(IFontAttribute):
    _case_insensitive_ = True
    u'Indicator interface specifying an italic state for a FontAttribute object.'
    _iid_ = GUID('{A45F4F70-CAAA-4FE1-A96B-2F483DE67A68}')
    _idlflags_ = ['oleautomation']
FontAttributeItalic._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IFontAttribute, IItalic]

class PolygonTracker(CoClass):
    u'Display feedback for polygon tracking.'
    _reg_clsid_ = GUID('{8D1827B1-F336-11D0-83A5-080009B996CC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
PolygonTracker._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ISelectionTracker, IPointCollectionTracker]

class MarkerPlacementDecoration(CoClass):
    u'Places markers as line decorations.'
    _reg_clsid_ = GUID('{B6C20FFE-8822-4CF7-BC0D-2CE7B2353F7B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
MarkerPlacementDecoration._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMarkerPlacement, IGraphicAttributes, IGraphicAttributes2, IEditInteraction, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

class GeometricEffectJog(CoClass):
    u'Constructs an Jog effect on a given line.'
    _reg_clsid_ = GUID('{9521BCE5-B2F1-473A-A533-D8E94F0B8BED}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
GeometricEffectJog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGeometricEffect, IGraphicAttributes, IGraphicAttributes2, IEditInteraction, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

class FontAttributeBold(CoClass):
    u'Controls whether the text will be drawn in bold type.'
    _reg_clsid_ = GUID('{4C4BD4C7-2600-449E-AFA1-7A80B03FE029}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IBold(IFontAttribute):
    _case_insensitive_ = True
    u'Indicator interface specifying a bold state for a FontAttribute object.'
    _iid_ = GUID('{DF029D39-50D5-40D8-AD2F-BD30EB91418C}')
    _idlflags_ = ['oleautomation']
FontAttributeBold._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IFontAttribute, IBold]

class RubberEnvelope(CoClass):
    u'Rubberbanding class for simple envelopes.'
    _reg_clsid_ = GUID('{E6BDB102-4D35-11D0-98BE-00805F7CED21}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
RubberEnvelope._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRubberBand, IRubberBand2]

class PointTracker(CoClass):
    u'Display feedback for point tracking.'
    _reg_clsid_ = GUID('{530FD714-EF0C-11D0-83A0-080009B996CC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
PointTracker._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ISelectionTracker]

class SymbolIdentifier(CoClass):
    u'Groups a symbol with both an ID and Name.'
    _reg_clsid_ = GUID('{440B07BC-92F0-11D3-9FCC-00C04F6BC6A5}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class ISymbolIdentifier(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the members that control the symbol identifier.'
    _iid_ = GUID('{440B07BB-92F0-11D3-9FCC-00C04F6BC6A5}')
    _idlflags_ = ['oleautomation']
class ISymbolIdentifier2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the members that control the symbol identifier.'
    _iid_ = GUID('{877A260A-CACB-48F6-AAF9-A24CE3BC75FF}')
    _idlflags_ = ['oleautomation']
SymbolIdentifier._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ISymbolIdentifier, ISymbolIdentifier2]

IAlgorithmicColorRamp._methods_ = [
    COMMETHOD(['propget', helpstring(u'The first color in the color ramp.')], HRESULT, 'FromColor',
              ( ['retval', 'out'], POINTER(POINTER(IColor)), 'Color' )),
    COMMETHOD(['propput', helpstring(u'The first color in the color ramp.')], HRESULT, 'FromColor',
              ( ['in'], POINTER(IColor), 'Color' )),
    COMMETHOD(['propget', helpstring(u'The last color in the color ramp.')], HRESULT, 'ToColor',
              ( ['retval', 'out'], POINTER(POINTER(IColor)), 'Color' )),
    COMMETHOD(['propput', helpstring(u'The last color in the color ramp.')], HRESULT, 'ToColor',
              ( ['in'], POINTER(IColor), 'Color' )),
    COMMETHOD(['propput', helpstring(u'The algorithm used to ramp between the first and last colors.')], HRESULT, 'Algorithm',
              ( ['in'], esriColorRampAlgorithm, 'Algorithm' )),
    COMMETHOD(['propget', helpstring(u'The algorithm used to ramp between the first and last colors.')], HRESULT, 'Algorithm',
              ( ['retval', 'out'], POINTER(esriColorRampAlgorithm), 'Algorithm' )),
]
################################################################
## code template for IAlgorithmicColorRamp implementation
##class IAlgorithmicColorRamp_Impl(object):
##    def _get(self):
##        u'The last color in the color ramp.'
##        #return Color
##    def _set(self, Color):
##        u'The last color in the color ramp.'
##    ToColor = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The first color in the color ramp.'
##        #return Color
##    def _set(self, Color):
##        u'The first color in the color ramp.'
##    FromColor = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The algorithm used to ramp between the first and last colors.'
##        #return Algorithm
##    def _set(self, Algorithm):
##        u'The algorithm used to ramp between the first and last colors.'
##    Algorithm = property(_get, _set, doc = _set.__doc__)
##

class CalloutTracker(CoClass):
    u'Display feedback for callout tracking.'
    _reg_clsid_ = GUID('{A761D651-065F-11D4-826F-0080C79F0371}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
CalloutTracker._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ICalloutTracker]

class FontAttributeUnderline(CoClass):
    u'Controls whether the text will be underlined.'
    _reg_clsid_ = GUID('{812A8361-6403-4A96-83E3-2DC97A60F30F}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IUnderline(IFontAttribute):
    _case_insensitive_ = True
    u'Indicator interface specifying an underline state for a FontAttribute object.'
    _iid_ = GUID('{F9292DE5-7D71-41CB-8224-3685744CF564}')
    _idlflags_ = ['oleautomation']
FontAttributeUnderline._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IFontAttribute, IUnderline]

class MarkerPlacementOnLine(CoClass):
    u'Places one marker along a line.'
    _reg_clsid_ = GUID('{7C3F5F1D-CC9A-45B5-8884-EE3AEAD9E74E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
MarkerPlacementOnLine._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMarkerPlacement, IGraphicAttributes, IGraphicAttributes2, IEditInteraction, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

class EngineRotateTracker(CoClass):
    u'Engine Rotate Tracker Class.'
    _reg_clsid_ = GUID('{30F137AF-5D42-49E4-9EDD-DA8C3BE7DEDA}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
EngineRotateTracker._com_interfaces_ = [IRotateTracker]

class esriGDICommentEndGroup(Structure):
    _recordinfo_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2, 0L, '{E53E05CF-59E1-44A2-BCF0-66DA6DEC56CC}')
esriGDICommentEndGroup._fields_ = [
    ('dSignature', c_ulong),
    ('nVersion', c_ulong),
]
assert sizeof(esriGDICommentEndGroup) == 8, sizeof(esriGDICommentEndGroup)
assert alignment(esriGDICommentEndGroup) == 4, alignment(esriGDICommentEndGroup)
ITextBackground2._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The text boundary.')], HRESULT, 'TextBoundary',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPolygon), 'rhs' )),
]
################################################################
## code template for ITextBackground2 implementation
##class ITextBackground2_Impl(object):
##    def TextBoundary(self, rhs):
##        u'The text boundary.'
##        #return 
##

class SymbolCollection(CoClass):
    u'Collection of symbols and id pairs.'
    _reg_clsid_ = GUID('{0E5D8C66-8D91-11D3-9FCA-00C04F6BC6A5}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class ISymbolCollection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control a collection of symbols and id pairs.'
    _iid_ = GUID('{0E5D8C65-8D91-11D3-9FCA-00C04F6BC6A5}')
    _idlflags_ = ['oleautomation']
class ISymbolCollection2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control a collection of symbols and id pairs.'
    _iid_ = GUID('{7ED742B9-0AEF-40A0-A9A5-DE2A302692F2}')
    _idlflags_ = ['oleautomation']
SymbolCollection._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ISymbolCollection, ISymbolCollection2, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone]

class IAppDisplay(IScreenDisplay):
    _case_insensitive_ = True
    u'Provides access to members that control the Mx Display.'
    _iid_ = GUID('{534E08D6-E65A-11D0-8681-0000F8751720}')
    _idlflags_ = ['oleautomation']
IScreenDisplay._methods_ = [
    COMMETHOD(['propput', helpstring(u'Associated window handle.')], HRESULT, 'hWnd',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hWnd' )),
    COMMETHOD(['propget', helpstring(u'Associated window handle.')], HRESULT, 'hWnd',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'hWnd' )),
    COMMETHOD(['propget', helpstring(u'Device context for the associated window.  Only use this between calls to StartDrawing and FinishDrawing.')], HRESULT, 'WindowDC',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'hDC' )),
    COMMETHOD([helpstring(u'Creates a new cache and return its ID.  The ID can be specified to StartDrawing to direct output to the cache.  It can also be used with a number of other methods such as DrawCache and Invalidate.')], HRESULT, 'AddCache',
              ( ['retval', 'out'], POINTER(c_short), 'cacheID' )),
    COMMETHOD([helpstring(u'Removes the specified cache.')], HRESULT, 'RemoveCache',
              ( ['in'], c_short, 'cacheID' )),
    COMMETHOD(['propget', helpstring(u'Number of screen caches.')], HRESULT, 'CacheCount',
              ( ['retval', 'out'], POINTER(c_short), 'Count' )),
    COMMETHOD([helpstring(u'Removes all caches.')], HRESULT, 'RemoveAllCaches'),
    COMMETHOD(['propget', helpstring(u'Memory device context for the specified screen cache.')], HRESULT, 'CacheMemDC',
              ( ['in'], c_short, 'index' ),
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'hDC' )),
    COMMETHOD(['propput', helpstring(u'Screen cache where drawing occurs. Use rarely.  Change cache inside StartDrawing/FinishDrawing sequence.')], HRESULT, 'ActiveCache',
              ( ['in'], c_short, 'index' )),
    COMMETHOD(['propget', helpstring(u'Screen cache where drawing occurs. Use rarely.  Change cache inside StartDrawing/FinishDrawing sequence.')], HRESULT, 'ActiveCache',
              ( ['retval', 'out'], POINTER(c_short), 'index' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the bottom cache is transparent.')], HRESULT, 'IsFirstCacheTransparent',
              ( ['in'], VARIANT_BOOL, 'flag' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the bottom cache is transparent.')], HRESULT, 'IsFirstCacheTransparent',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD([helpstring(u'Starts recording all output to the recording cache.')], HRESULT, 'StartRecording'),
    COMMETHOD([helpstring(u'Stops recording to the recording cache.')], HRESULT, 'StopRecording'),
    COMMETHOD(['propput', helpstring(u'Indicates if scrollbars should appear.')], HRESULT, 'UseScrollbars',
              ( ['in'], VARIANT_BOOL, 'flag' )),
    COMMETHOD(['propget', helpstring(u'Indicates if scrollbars should appear.')], HRESULT, 'UseScrollbars',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD([helpstring(u'Optionally specify application supplied scrollbars.')], HRESULT, 'SetScrollbarHandles',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hWndHorzScrollbar' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hWndVertScrollbar' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the contents of the screen scale when a resize occurs.  True means scale contents to fit new window size.  False means contents stays the same with more or less of it showing.')], HRESULT, 'ScaleContents',
              ( ['in'], VARIANT_BOOL, 'flag' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the contents of the screen scale when a resize occurs.  True means scale contents to fit new window size.  False means contents stays the same with more or less of it showing.')], HRESULT, 'ScaleContents',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD(['propput', helpstring(u"Indicates if display resizing is suppressed.  True means the display doesn't resize with the window.  False ensures that the display is the same size as the window.")], HRESULT, 'SuppressResize',
              ( ['in'], VARIANT_BOOL, 'SuppressResize' )),
    COMMETHOD(['propget', helpstring(u"Indicates if display resizing is suppressed.  True means the display doesn't resize with the window.  False ensures that the display is the same size as the window.")], HRESULT, 'SuppressResize',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'SuppressResize' )),
    COMMETHOD(['propget', helpstring(u'Indicates if drawing occurs in a frame rather than on the whole window.')], HRESULT, 'IsFramed',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD(['propput', helpstring(u'Indicates if drawing occurs in a frame rather than on the whole window.')], HRESULT, 'IsFramed',
              ( ['in'], VARIANT_BOOL, 'flag' )),
    COMMETHOD(['propget', helpstring(u'Cancel tracker that is associated with the display.')], HRESULT, 'CancelTracker',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel)), 'CancelTracker' )),
    COMMETHOD(['propputref', helpstring(u'Cancel tracker that is associated with the display.')], HRESULT, 'CancelTracker',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'CancelTracker' )),
    COMMETHOD([helpstring(u'Cause the specified area of the specified cache to redraw.')], HRESULT, 'Invalidate',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'rect' ),
              ( ['in'], VARIANT_BOOL, 'erase' ),
              ( ['in'], c_short, 'cacheIndex' )),
    COMMETHOD([helpstring(u'Indicates if the specified cache needs refreshing.')], HRESULT, 'IsCacheDirty',
              ( ['in'], c_short, 'cacheIndex' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD([helpstring(u'Draws the specified screen cache to the specified window device context. Pass an empty rectangle to copy the full bitmap to the DC origin.')], HRESULT, 'DrawCache',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDC' ),
              ( ['in'], c_short, 'index' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.tagRECT), 'deviceRect' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.tagRECT), 'cacheRect' )),
    COMMETHOD([helpstring(u'Scrolls the screen by the specified amount.')], HRESULT, 'DoScroll',
              ( ['in'], c_int, 'xDelta' ),
              ( ['in'], c_int, 'yDelta' ),
              ( ['in'], VARIANT_BOOL, 'updateScreen' )),
    COMMETHOD([helpstring(u'Interactively pans the screen.')], HRESULT, 'TrackPan'),
    COMMETHOD([helpstring(u'Prepares display for panning.')], HRESULT, 'PanStart',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'mouseLocation' )),
    COMMETHOD([helpstring(u'Pans to a new point.')], HRESULT, 'PanMoveTo',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'mouseLocation' )),
    COMMETHOD([helpstring(u'Stops panning and returns new visible bounds.')], HRESULT, 'PanStop',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'newExtent' )),
    COMMETHOD([helpstring(u'Interactively rotates the screen.')], HRESULT, 'TrackRotate'),
    COMMETHOD([helpstring(u'Prepares display for rotating.  If centerPt is NULL, the center of the visible bounds is used.')], HRESULT, 'RotateStart',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'mousePt' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'centerPt' )),
    COMMETHOD([helpstring(u'Rotates to new point.')], HRESULT, 'RotateMoveTo',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'pPoint' )),
    COMMETHOD([helpstring(u'Draws the rotated display. Call in response to WM_TIMER.')], HRESULT, 'RotateTimer'),
    COMMETHOD([helpstring(u'Stops rotating and returns new angle.')], HRESULT, 'RotateStop',
              ( ['retval', 'out'], POINTER(c_double), 'degrees' )),
    COMMETHOD([helpstring(u'Forces a redraw.')], HRESULT, 'UpdateWindow'),
]
################################################################
## code template for IScreenDisplay implementation
##class IScreenDisplay_Impl(object):
##    def PanStart(self, mouseLocation):
##        u'Prepares display for panning.'
##        #return 
##
##    def _get(self):
##        u'Associated window handle.'
##        #return hWnd
##    def _set(self, hWnd):
##        u'Associated window handle.'
##    hWnd = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the contents of the screen scale when a resize occurs.  True means scale contents to fit new window size.  False means contents stays the same with more or less of it showing.'
##        #return flag
##    def _set(self, flag):
##        u'Indicates if the contents of the screen scale when a resize occurs.  True means scale contents to fit new window size.  False means contents stays the same with more or less of it showing.'
##    ScaleContents = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def WindowDC(self):
##        u'Device context for the associated window.  Only use this between calls to StartDrawing and FinishDrawing.'
##        #return hDC
##
##    def PanMoveTo(self, mouseLocation):
##        u'Pans to a new point.'
##        #return 
##
##    def RotateTimer(self):
##        u'Draws the rotated display. Call in response to WM_TIMER.'
##        #return 
##
##    def StopRecording(self):
##        u'Stops recording to the recording cache.'
##        #return 
##
##    @property
##    def CacheMemDC(self, index):
##        u'Memory device context for the specified screen cache.'
##        #return hDC
##
##    def _get(self):
##        u'Indicates if drawing occurs in a frame rather than on the whole window.'
##        #return flag
##    def _set(self, flag):
##        u'Indicates if drawing occurs in a frame rather than on the whole window.'
##    IsFramed = property(_get, _set, doc = _set.__doc__)
##
##    def CancelTracker(self, CancelTracker):
##        u'Cancel tracker that is associated with the display.'
##        #return 
##
##    def RemoveCache(self, cacheID):
##        u'Removes the specified cache.'
##        #return 
##
##    def IsCacheDirty(self, cacheIndex):
##        u'Indicates if the specified cache needs refreshing.'
##        #return flag
##
##    def AddCache(self):
##        u'Creates a new cache and return its ID.  The ID can be specified to StartDrawing to direct output to the cache.  It can also be used with a number of other methods such as DrawCache and Invalidate.'
##        #return cacheID
##
##    def Invalidate(self, rect, erase, cacheIndex):
##        u'Cause the specified area of the specified cache to redraw.'
##        #return 
##
##    def DrawCache(self, hDC, index, deviceRect, cacheRect):
##        u'Draws the specified screen cache to the specified window device context. Pass an empty rectangle to copy the full bitmap to the DC origin.'
##        #return 
##
##    def TrackPan(self):
##        u'Interactively pans the screen.'
##        #return 
##
##    def TrackRotate(self):
##        u'Interactively rotates the screen.'
##        #return 
##
##    def StartRecording(self):
##        u'Starts recording all output to the recording cache.'
##        #return 
##
##    def RotateMoveTo(self, pPoint):
##        u'Rotates to new point.'
##        #return 
##
##    def RotateStop(self):
##        u'Stops rotating and returns new angle.'
##        #return degrees
##
##    def UpdateWindow(self):
##        u'Forces a redraw.'
##        #return 
##
##    def _get(self):
##        u'Indicates if the bottom cache is transparent.'
##        #return flag
##    def _set(self, flag):
##        u'Indicates if the bottom cache is transparent.'
##    IsFirstCacheTransparent = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def CacheCount(self):
##        u'Number of screen caches.'
##        #return Count
##
##    def PanStop(self):
##        u'Stops panning and returns new visible bounds.'
##        #return newExtent
##
##    def _get(self):
##        u'Indicates if scrollbars should appear.'
##        #return flag
##    def _set(self, flag):
##        u'Indicates if scrollbars should appear.'
##    UseScrollbars = property(_get, _set, doc = _set.__doc__)
##
##    def RemoveAllCaches(self):
##        u'Removes all caches.'
##        #return 
##
##    def RotateStart(self, mousePt, centerPt):
##        u'Prepares display for rotating.  If centerPt is NULL, the center of the visible bounds is used.'
##        #return 
##
##    def DoScroll(self, xDelta, yDelta, updateScreen):
##        u'Scrolls the screen by the specified amount.'
##        #return 
##
##    def _get(self):
##        u'Screen cache where drawing occurs. Use rarely.  Change cache inside StartDrawing/FinishDrawing sequence.'
##        #return index
##    def _set(self, index):
##        u'Screen cache where drawing occurs. Use rarely.  Change cache inside StartDrawing/FinishDrawing sequence.'
##    ActiveCache = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u"Indicates if display resizing is suppressed.  True means the display doesn't resize with the window.  False ensures that the display is the same size as the window."
##        #return SuppressResize
##    def _set(self, SuppressResize):
##        u"Indicates if display resizing is suppressed.  True means the display doesn't resize with the window.  False ensures that the display is the same size as the window."
##    SuppressResize = property(_get, _set, doc = _set.__doc__)
##
##    def SetScrollbarHandles(self, hWndHorzScrollbar, hWndVertScrollbar):
##        u'Optionally specify application supplied scrollbars.'
##        #return 
##

IAppDisplay._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The ScreenDisplay associated with the main application window.  Set this property before using the other properties and methods.')], HRESULT, 'MainScreen',
              ( ['in'], POINTER(IScreenDisplay), 'MainScreen' )),
    COMMETHOD(['propget', helpstring(u'The ScreenDisplay associated with the main application window.  Set this property before using the other properties and methods.')], HRESULT, 'MainScreen',
              ( ['retval', 'out'], POINTER(POINTER(IScreenDisplay)), 'MainScreen' )),
    COMMETHOD(['propget', helpstring(u'The ScreenDisplay associated with the window the mouse is over.  May be a lens window or the main window.')], HRESULT, 'FocusScreen',
              ( ['retval', 'out'], POINTER(POINTER(IScreenDisplay)), 'FocusScreen' )),
    COMMETHOD(['propget', helpstring(u'The number of ScreenDisplays associated with the application.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'The nth ScreenDisplay associated with the application.')], HRESULT, 'ScreenDisplay',
              ( ['in'], c_int, 'idx' ),
              ( ['retval', 'out'], POINTER(POINTER(IScreenDisplay)), 'ScreenDisplay' )),
]
################################################################
## code template for IAppDisplay implementation
##class IAppDisplay_Impl(object):
##    @property
##    def Count(self):
##        u'The number of ScreenDisplays associated with the application.'
##        #return Count
##
##    @property
##    def MainScreen(self, MainScreen):
##        u'The ScreenDisplay associated with the main application window.  Set this property before using the other properties and methods.'
##        #return 
##
##    @property
##    def ScreenDisplay(self, idx):
##        u'The nth ScreenDisplay associated with the application.'
##        #return ScreenDisplay
##
##    @property
##    def FocusScreen(self):
##        u'The ScreenDisplay associated with the window the mouse is over.  May be a lens window or the main window.'
##        #return FocusScreen
##


# values for enumeration 'esriGraphicAttributeType'
esriAttributeTypeBoolean = 0
esriAttributeTypeInteger = 1
esriAttributeTypeEnum = 2
esriAttributeTypeDouble = 3
esriAttributeTypeSize = 4
esriAttributeTypeText = 5
esriAttributeTypeColor = 6
esriAttributeTypeMarker = 7
esriAttributeTypeDash = 8
esriAttributeTypeAngle = 9
esriGraphicAttributeType = c_int # enum
IGraphicAttributeType._methods_ = [
    COMMETHOD(['propget', helpstring(u'The graphic attribute type.')], HRESULT, 'Type',
              ( ['retval', 'out'], POINTER(esriGraphicAttributeType), 'Type' )),
    COMMETHOD([helpstring(u'Formats the graphic attribute value.')], HRESULT, 'FormatValue',
              ( ['in'], VARIANT, 'Value' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'val' )),
    COMMETHOD([helpstring(u'Converts text to the graphic attribute value.')], HRESULT, 'TextToValue',
              ( ['in'], BSTR, 'Text' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'Value' )),
    COMMETHOD([helpstring(u'Converts the graphic attribute value to text.')], HRESULT, 'ValueToText',
              ( ['in'], VARIANT, 'Value' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Text' )),
    COMMETHOD([helpstring(u'Draws a value on the device context.')], HRESULT, 'DrawValue',
              ( ['in'], VARIANT, 'Value' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.tagRECT), 'rect' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDC' ),
              ( ['in'], VARIANT_BOOL, 'readOnly' )),
]
################################################################
## code template for IGraphicAttributeType implementation
##class IGraphicAttributeType_Impl(object):
##    def DrawValue(self, Value, rect, hDC, readOnly):
##        u'Draws a value on the device context.'
##        #return 
##
##    def TextToValue(self, Text):
##        u'Converts text to the graphic attribute value.'
##        #return Value
##
##    def FormatValue(self, Value):
##        u'Formats the graphic attribute value.'
##        #return val
##
##    @property
##    def Type(self):
##        u'The graphic attribute type.'
##        #return Type
##
##    def ValueToText(self, Value):
##        u'Converts the graphic attribute value to text.'
##        #return Text
##

class RubberPoint(CoClass):
    u'Rubberbanding class for points.'
    _reg_clsid_ = GUID('{E6BDB103-4D35-11D0-98BE-00805F7CED21}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
RubberPoint._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRubberBand, IRubberBand2]

class OverposterTextPath(CoClass):
    u'Overposter Text Path object.'
    _reg_clsid_ = GUID('{E0554440-25CF-11D3-9F97-00C04F6BC6A5}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IOverposterTextPath(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Indicator interface for overposter text path objects.'
    _iid_ = GUID('{3E0B2E61-27F4-11D3-9F9C-00C04F6BC6A5}')
    _idlflags_ = ['oleautomation']
OverposterTextPath._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IOverposterTextPath, ITextPath, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist]

IRepresentationRuleItem._methods_ = [
    COMMETHOD(['propput', helpstring(u'The type of geometry used by the rule.')], HRESULT, 'GeometryType',
              ( ['in'], comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.esriGeometryType, 'geomType' )),
    COMMETHOD(['propget', helpstring(u'The type of geometry used by the rule.')], HRESULT, 'GeometryType',
              ( ['retval', 'out'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.esriGeometryType), 'geomType' )),
    COMMETHOD(['propputref', helpstring(u'The type of geometry used by the rule.')], HRESULT, 'RepresentationRule',
              ( ['in'], POINTER(IRepresentationRule), 'Rule' )),
    COMMETHOD(['propget', helpstring(u'The type of geometry used by the rule.')], HRESULT, 'RepresentationRule',
              ( ['retval', 'out'], POINTER(POINTER(IRepresentationRule)), 'Rule' )),
]
################################################################
## code template for IRepresentationRuleItem implementation
##class IRepresentationRuleItem_Impl(object):
##    @property
##    def RepresentationRule(self, Rule):
##        u'The type of geometry used by the rule.'
##        #return 
##
##    def _get(self):
##        u'The type of geometry used by the rule.'
##        #return geomType
##    def _set(self, geomType):
##        u'The type of geometry used by the rule.'
##    GeometryType = property(_get, _set, doc = _set.__doc__)
##

ICalloutFeedback._methods_ = [
    COMMETHOD([helpstring(u'Begins a feedback of the given symbol.')], HRESULT, 'Start',
              ( ['in'], POINTER(ISymbol), 'Symbol' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'Geometry' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
    COMMETHOD([helpstring(u'Stops the feedback and returns the shape.')], HRESULT, 'Stop',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPolyline)), 'polyline' )),
    COMMETHOD([helpstring(u'Moves the anchor point to the given point.')], HRESULT, 'MoveAnchorTo',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
]
################################################################
## code template for ICalloutFeedback implementation
##class ICalloutFeedback_Impl(object):
##    def Start(self, Symbol, Geometry, Point):
##        u'Begins a feedback of the given symbol.'
##        #return 
##
##    def MoveAnchorTo(self, Point):
##        u'Moves the anchor point to the given point.'
##        #return 
##
##    def Stop(self):
##        u'Stops the feedback and returns the shape.'
##        #return polyline
##

class MarkerPlacementRandomInPolygon(CoClass):
    u'Places markers randomly within a polygon.'
    _reg_clsid_ = GUID('{6D20682F-1A9B-4087-BCC3-0C9AA662D52D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
MarkerPlacementRandomInPolygon._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMarkerPlacement, IGraphicAttributes, IGraphicAttributes2, IEditInteraction, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, IClippingMethod, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

class GeometricEffectSmooth(CoClass):
    u'Smooth a geometry by approximation with beziers.'
    _reg_clsid_ = GUID('{CA7D653D-F035-461D-93AA-FBB2ECA565EF}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
GeometricEffectSmooth._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGeometricEffect, IGraphicAttributes, IGraphicAttributes2, IEditInteraction, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

class Template(CoClass):
    u'Stores information on the mark and gap patterns for lines.'
    _reg_clsid_ = GUID('{41093A71-CCE1-11D0-BFAA-0080C7E24280}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
Template._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ITemplate, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone]

class WordTextPath(CoClass):
    u'Word Text Path object.'
    _reg_clsid_ = GUID('{1EB7FE01-8D14-479D-A38F-30AB01B412E4}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
WordTextPath._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IWordTextPath, ITextPath, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist]

IDrawingOutline._methods_ = [
    COMMETHOD([helpstring(u'Tests if a point is located on the drawing outline.')], HRESULT, 'HitTest',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'Geometry' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' ),
              ( ['in'], c_double, 'tolerance' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'hit' )),
    COMMETHOD([helpstring(u'Constructs the entire drawing outline of a drawing rule.')], HRESULT, 'GetAllOutlineParts',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'Geometry' ),
              ( ['in'], esriOutlineType, 'Type' ),
              ( ['in'], esriOutlineOption, 'option' ),
              ( ['in'], c_double, 'buffer' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'ClipEnvelope' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry)), 'Outline' )),
    COMMETHOD([helpstring(u'Resets the outline part enumeration.')], HRESULT, 'Reset',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'Geometry' ),
              ( ['in'], esriOutlineType, 'Type' ),
              ( ['in'], esriOutlineOption, 'option' ),
              ( ['in'], c_double, 'buffer' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'ClipEnvelope' )),
    COMMETHOD([helpstring(u'Retrieves the next part of the outline.')], HRESULT, 'NextOutlinePart',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry)), 'outlinePart' )),
]
################################################################
## code template for IDrawingOutline implementation
##class IDrawingOutline_Impl(object):
##    def HitTest(self, Geometry, Point, tolerance):
##        u'Tests if a point is located on the drawing outline.'
##        #return hit
##
##    def Reset(self, Geometry, Type, option, buffer, ClipEnvelope):
##        u'Resets the outline part enumeration.'
##        #return 
##
##    def NextOutlinePart(self):
##        u'Retrieves the next part of the outline.'
##        #return outlinePart
##
##    def GetAllOutlineParts(self, Geometry, Type, option, buffer, ClipEnvelope):
##        u'Constructs the entire drawing outline of a drawing rule.'
##        #return Outline
##

class GeometricEffectRegularPolygon(CoClass):
    u'Creates a regular polygon from a point.'
    _reg_clsid_ = GUID('{E16A3AEE-A35C-461F-9A2A-BBB41C0B777F}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
GeometricEffectRegularPolygon._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGeometricEffect, IGraphicAttributes, IGraphicAttributes2, IEditInteraction, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

class SymbologyEnvironment(CoClass):
    u'Controls how symbols are drawn as Graphical Device Interface (GDI) objects.'
    _reg_clsid_ = GUID('{65856CD8-AD04-11D3-9FC2-00C04F6BC8DD}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
SymbologyEnvironment._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ISymbologyEnvironment, ISymbologyEnvironment2, IPictureSymbolEnvironment, IFontsInSymbolsEnvironment]

IDelayEvents._methods_ = [
    COMMETHOD(['propput', helpstring(u'Indicates if events are delayed.  If something changes while events are being delayed, a single event is fired when events are resumed.')], HRESULT, 'DelayEvents',
              ( ['in'], VARIANT_BOOL, 'DelayEvents' )),
    COMMETHOD(['propget', helpstring(u'Indicates if events are delayed.  If something changes while events are being delayed, a single event is fired when events are resumed.')], HRESULT, 'DelayEvents',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'DelayEvents' )),
]
################################################################
## code template for IDelayEvents implementation
##class IDelayEvents_Impl(object):
##    def _get(self):
##        u'Indicates if events are delayed.  If something changes while events are being delayed, a single event is fired when events are resumed.'
##        #return DelayEvents
##    def _set(self, DelayEvents):
##        u'Indicates if events are delayed.  If something changes while events are being delayed, a single event is fired when events are resumed.'
##    DelayEvents = property(_get, _set, doc = _set.__doc__)
##

class ReshapeFeedback(CoClass):
    u'Rubberbanding class for editing a shape.'
    _reg_clsid_ = GUID('{4E315501-F4DD-11D1-8498-0000F875B9C6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
ReshapeFeedback._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IReshapeFeedback, IDisplayFeedback, IDisplayFeedback2]


# values for enumeration 'esriDisplayCacheFlags'
esriDisplayCacheNoFlags = 0
esriDisplayCacheRequiresBackground = 1
esriDisplayCachePrivate = 2
esriDisplayCacheFlags = c_int # enum
class MapContext(CoClass):
    u'The context in which geometric effects and marker placement work.'
    _reg_clsid_ = GUID('{DB636C95-3317-4CAD-8BDC-94ADD74821EA}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
MapContext._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMapContext, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

IScreenCacheManager._methods_ = [
    COMMETHOD([helpstring(u'Creates a new cache and return its ID.  The ID can be specified to StartDrawing to direct output to the cache.  It can also be used with a number of other methods such as DrawCache and Invalidate.')], HRESULT, 'AddCache',
              ( ['retval', 'out'], POINTER(c_short), 'cacheID' )),
    COMMETHOD([helpstring(u'Removes the specified cache.')], HRESULT, 'RemoveCache',
              ( ['in'], c_short, 'cacheID' )),
    COMMETHOD(['propget', helpstring(u'Number of screen caches.')], HRESULT, 'CacheCount',
              ( ['retval', 'out'], POINTER(c_short), 'Count' )),
    COMMETHOD([helpstring(u'Removes all caches.')], HRESULT, 'RemoveAllCaches'),
    COMMETHOD(['propget', helpstring(u'Memory device context for the specified screen cache.')], HRESULT, 'CacheMemDC',
              ( ['in'], c_short, 'index' ),
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'hDC' )),
    COMMETHOD(['propput', helpstring(u'Screen cache where drawing occurs. Use rarely.  Change cache inside StartDrawing/FinishDrawing sequence.')], HRESULT, 'ActiveCache',
              ( ['in'], c_short, 'index' )),
    COMMETHOD(['propget', helpstring(u'Screen cache where drawing occurs. Use rarely.  Change cache inside StartDrawing/FinishDrawing sequence.')], HRESULT, 'ActiveCache',
              ( ['retval', 'out'], POINTER(c_short), 'index' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the bottom cache is transparent.')], HRESULT, 'IsFirstCacheTransparent',
              ( ['in'], VARIANT_BOOL, 'flag' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the bottom cache is transparent.')], HRESULT, 'IsFirstCacheTransparent',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD([helpstring(u'Get special properties of specified cache.')], HRESULT, 'GetCacheFlags',
              ( ['in'], c_short, 'cacheID' ),
              ( ['out'], POINTER(esriDisplayCacheFlags), 'Flags' )),
    COMMETHOD([helpstring(u'Set special properties of specified cache.')], HRESULT, 'ModifyCacheFlags',
              ( ['in'], c_short, 'cacheID' ),
              ( ['in'], esriDisplayCacheFlags, 'flagsToAdd' ),
              ( ['in'], esriDisplayCacheFlags, 'flagsToRemove' )),
    COMMETHOD([helpstring(u"Sets or returns the order of the specified cache.  Client's that use multiple caches may assign an order to them.  Bottom cache is 0 and top cache is n.")], HRESULT, 'PutCacheOrder',
              ( ['in'], c_short, 'cacheID' ),
              ( ['in'], c_short, 'order' )),
    COMMETHOD([helpstring(u"Sets or returns the order of the specified cache.  Client's that use multiple caches can assign an order to them.  Bottom cache is 0 and top cache is n.")], HRESULT, 'GetCacheOrder',
              ( ['in'], c_short, 'cacheID' ),
              ( ['retval', 'out'], POINTER(c_short), 'order' )),
    COMMETHOD([helpstring(u'Starts recording all output to the recording cache.')], HRESULT, 'StartRecording'),
    COMMETHOD([helpstring(u'Stops recording to the recording cache.')], HRESULT, 'StopRecording'),
    COMMETHOD([helpstring(u'Indicates if the specified cache needs refreshing.')], HRESULT, 'IsCacheDirty',
              ( ['in'], c_short, 'cacheIndex' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD([helpstring(u'Draws the specified screen cache to the specified window device context. Pass an empty rectangle to copy the full bitmap to the DC origin.')], HRESULT, 'DrawCache',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDC' ),
              ( ['in'], c_short, 'index' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.tagRECT), 'deviceRect' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.tagRECT), 'cacheRect' )),
]
################################################################
## code template for IScreenCacheManager implementation
##class IScreenCacheManager_Impl(object):
##    @property
##    def CacheCount(self):
##        u'Number of screen caches.'
##        #return Count
##
##    def IsCacheDirty(self, cacheIndex):
##        u'Indicates if the specified cache needs refreshing.'
##        #return flag
##
##    def RemoveAllCaches(self):
##        u'Removes all caches.'
##        #return 
##
##    def AddCache(self):
##        u'Creates a new cache and return its ID.  The ID can be specified to StartDrawing to direct output to the cache.  It can also be used with a number of other methods such as DrawCache and Invalidate.'
##        #return cacheID
##
##    def GetCacheOrder(self, cacheID):
##        u"Sets or returns the order of the specified cache.  Client's that use multiple caches can assign an order to them.  Bottom cache is 0 and top cache is n."
##        #return order
##
##    def DrawCache(self, hDC, index, deviceRect, cacheRect):
##        u'Draws the specified screen cache to the specified window device context. Pass an empty rectangle to copy the full bitmap to the DC origin.'
##        #return 
##
##    def StartRecording(self):
##        u'Starts recording all output to the recording cache.'
##        #return 
##
##    def StopRecording(self):
##        u'Stops recording to the recording cache.'
##        #return 
##
##    @property
##    def CacheMemDC(self, index):
##        u'Memory device context for the specified screen cache.'
##        #return hDC
##
##    def _get(self):
##        u'Screen cache where drawing occurs. Use rarely.  Change cache inside StartDrawing/FinishDrawing sequence.'
##        #return index
##    def _set(self, index):
##        u'Screen cache where drawing occurs. Use rarely.  Change cache inside StartDrawing/FinishDrawing sequence.'
##    ActiveCache = property(_get, _set, doc = _set.__doc__)
##
##    def GetCacheFlags(self, cacheID):
##        u'Get special properties of specified cache.'
##        #return Flags
##
##    def ModifyCacheFlags(self, cacheID, flagsToAdd, flagsToRemove):
##        u'Set special properties of specified cache.'
##        #return 
##
##    def PutCacheOrder(self, cacheID, order):
##        u"Sets or returns the order of the specified cache.  Client's that use multiple caches may assign an order to them.  Bottom cache is 0 and top cache is n."
##        #return 
##
##    def RemoveCache(self, cacheID):
##        u'Removes the specified cache.'
##        #return 
##
##    def _get(self):
##        u'Indicates if the bottom cache is transparent.'
##        #return flag
##    def _set(self, flag):
##        u'Indicates if the bottom cache is transparent.'
##    IsFirstCacheTransparent = property(_get, _set, doc = _set.__doc__)
##


# values for enumeration 'esriGeometricEffectAttributes'
esriGAControlPointsTolerance = 0
esriGABufferSize = 0
esriGACutCurveBegin = 0
esriGACutCurveEnd = 1
esriGACutCurveInvert = 2
esriGADashPattern = 0
esriGADashEndings = 1
esriGADashPosition = 2
esriGADashOffsetAtEnd = 3
esriGADonutWidth = 0
esriGADonutSimple = 1
esriGADonutMethod = 2
esriGAEnclosingPolygonMethod = 0
esriGAOffsetCurveOffset = 0
esriGAOffsetCurveMethod = 1
esriGAOffsetCurveSimple = 2
esriGAOffsetCurveOption = 3
esriGAOffsetCurveCount = 4
esriGARadialAngle = 0
esriGARadialLength = 1
esriGAReverse = 0
esriGASimplifyTolerance = 0
esriGASmoothTolerance = 0
esriGARegularPolygonRadius = 0
esriGARegularPolygonEdges = 1
esriGARegularPolygonAngle = 2
esriGAWavePeriod = 0
esriGAWaveWidth = 1
esriGAWaveStyle = 2
esriGAWaveSeed = 3
esriGAMoveXOffset = 0
esriGAMoveYOffset = 1
esriGAScaleXFactor = 0
esriGAScaleYFactor = 1
esriGARotateAngle = 0
esriGATaperedPolygonFromWidth = 0
esriGATaperedPolygonToWidth = 1
esriGATaperedPolygonLength = 2
esriGAArrowType = 0
esriGAArrowWidth = 1
esriGAJogLength = 0
esriGAJogAngle = 1
esriGAJogPosition = 2
esriGAExtensionOrigin = 0
esriGAExtensionDeflection = 1
esriGAExtensionLength = 2
esriGAOffsetTangentMethod = 0
esriGAOffsetTangentOffset = 1
esriGASuppressSuppress = 0
esriGeometricEffectAttributes = c_int # enum
class AnchorPoint(CoClass):
    u'Anchor point class for rubberbanding objects.'
    _reg_clsid_ = GUID('{71FC8721-0164-11D2-84A4-0000F875B9C6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
AnchorPoint._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IAnchorPoint]

class RandomColorRamp(CoClass):
    u'Defines a random color ramp, where ramp is a list of randomly picked colors.'
    _reg_clsid_ = GUID('{BEB87094-C0B4-11D0-8379-080009B996CC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IRandomColorRamp(IColorRamp):
    _case_insensitive_ = True
    u'Provides access to members that control the properties of a RandomColorRamp. A color ramp that is a list of randomly picked colors.'
    _iid_ = GUID('{BEB87095-C0B4-11D0-8379-080009B996CC}')
    _idlflags_ = ['oleautomation']
RandomColorRamp._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRandomColorRamp, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize]

class GeometricEffectRadial(CoClass):
    u'Produces a line from a point, based on direction and length.'
    _reg_clsid_ = GUID('{18D04C0A-69BF-490A-8D47-37A78548507A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
GeometricEffectRadial._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGeometricEffect, IGraphicAttributes, IGraphicAttributes2, IEditInteraction, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

class IRotateInteraction(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the parameters of the Rotate Representation Tool.'
    _iid_ = GUID('{916AD46E-CDEE-4CFF-A116-4F39BF380B26}')
    _idlflags_ = ['oleautomation']
IRotateInteraction._methods_ = [
    COMMETHOD(['propput', helpstring(u'Center of the rotate operation.')], HRESULT, 'Center',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Center' )),
    COMMETHOD(['propget', helpstring(u'Center of the rotate operation.')], HRESULT, 'Center',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint)), 'Center' )),
    COMMETHOD(['propput', helpstring(u'Current angle of the rotate operation.')], HRESULT, 'Angle',
              ( ['in'], c_double, 'Angle' )),
    COMMETHOD(['propget', helpstring(u'Current angle of the rotate operation.')], HRESULT, 'Angle',
              ( ['retval', 'out'], POINTER(c_double), 'Angle' )),
    COMMETHOD(['propput', helpstring(u'Indicates if representations rotate around an individual anchor.')], HRESULT, 'IndividualAnchors',
              ( ['in'], VARIANT_BOOL, 'IndividualAnchors' )),
    COMMETHOD(['propget', helpstring(u'Indicates if representations rotate around an individual anchor.')], HRESULT, 'IndividualAnchors',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IndividualAnchors' )),
]
################################################################
## code template for IRotateInteraction implementation
##class IRotateInteraction_Impl(object):
##    def _get(self):
##        u'Indicates if representations rotate around an individual anchor.'
##        #return IndividualAnchors
##    def _set(self, IndividualAnchors):
##        u'Indicates if representations rotate around an individual anchor.'
##    IndividualAnchors = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Current angle of the rotate operation.'
##        #return Angle
##    def _set(self, Angle):
##        u'Current angle of the rotate operation.'
##    Angle = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Center of the rotate operation.'
##        #return Center
##    def _set(self, Center):
##        u'Center of the rotate operation.'
##    Center = property(_get, _set, doc = _set.__doc__)
##

class SimpleTextParser(CoClass):
    u'Simple text parser object.'
    _reg_clsid_ = GUID('{D7099B91-E298-499E-9757-72BB39E55CF3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class ITextParser(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that parse text strings.'
    _iid_ = GUID('{55D9F654-5CDE-4842-8E47-70518079FE1A}')
    _idlflags_ = ['oleautomation']
SimpleTextParser._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ITextParser, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist]

class GraphicAttributeIntegerType(CoClass):
    u'Integer graphic attribute type.'
    _reg_clsid_ = GUID('{781BCFF2-8DB8-4D19-98D6-6D36DF3759F5}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
GraphicAttributeIntegerType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGraphicAttributeType]

IEditInteraction._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if a graphic attribute is editable by a representation tool.')], HRESULT, 'IsEditableAttribute',
              ( ['in'], VARIANT, 'editParams' ),
              ( ['in'], c_int, 'attrIndex' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'isEditable' )),
    COMMETHOD([helpstring(u'Modifies the graphic attributes according to the editing parameters of the representation tool.')], HRESULT, 'ModifyAttributes',
              ( ['in'], VARIANT, 'editParams' ),
              ( ['in'], VARIANT, 'attrArray' )),
]
################################################################
## code template for IEditInteraction implementation
##class IEditInteraction_Impl(object):
##    def ModifyAttributes(self, editParams, attrArray):
##        u'Modifies the graphic attributes according to the editing parameters of the representation tool.'
##        #return 
##
##    @property
##    def IsEditableAttribute(self, editParams, attrIndex):
##        u'Indicates if a graphic attribute is editable by a representation tool.'
##        #return isEditable
##

class IMarkerFillSymbol(IFillSymbol):
    _case_insensitive_ = True
    u'Provides access to members that control the marker fill symbol.'
    _iid_ = GUID('{7914E5F1-C892-11D0-8BB6-080009EE4E41}')
    _idlflags_ = ['oleautomation']
IMarkerFillSymbol._methods_ = [
    COMMETHOD(['propget', helpstring(u'Marker symbol used for fill.')], HRESULT, 'MarkerSymbol',
              ( ['retval', 'out'], POINTER(POINTER(IMarkerSymbol)), 'marker' )),
    COMMETHOD(['propputref', helpstring(u'Marker symbol used for fill.')], HRESULT, 'MarkerSymbol',
              ( ['in'], POINTER(IMarkerSymbol), 'marker' )),
    COMMETHOD(['propget', helpstring(u'Fill style.')], HRESULT, 'Style',
              ( ['retval', 'out'], POINTER(esriMarkerFillStyle), 'Style' )),
    COMMETHOD(['propput', helpstring(u'Fill style.')], HRESULT, 'Style',
              ( ['in'], esriMarkerFillStyle, 'Style' )),
    COMMETHOD(['propget', helpstring(u'Angle of marker position grid.')], HRESULT, 'GridAngle',
              ( ['retval', 'out'], POINTER(c_double), 'Angle' )),
    COMMETHOD(['propput', helpstring(u'Angle of marker position grid.')], HRESULT, 'GridAngle',
              ( ['in'], c_double, 'Angle' )),
]
################################################################
## code template for IMarkerFillSymbol implementation
##class IMarkerFillSymbol_Impl(object):
##    def _get(self):
##        u'Angle of marker position grid.'
##        #return Angle
##    def _set(self, Angle):
##        u'Angle of marker position grid.'
##    GridAngle = property(_get, _set, doc = _set.__doc__)
##
##    def MarkerSymbol(self, marker):
##        u'Marker symbol used for fill.'
##        #return 
##
##    def _get(self):
##        u'Fill style.'
##        #return Style
##    def _set(self, Style):
##        u'Fill style.'
##    Style = property(_get, _set, doc = _set.__doc__)
##

INewPolygonFeedback._methods_ = [
    COMMETHOD([helpstring(u'Begins a normal feedback at the given point.')], HRESULT, 'Start',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
    COMMETHOD([helpstring(u'Creates a node at the given point.')], HRESULT, 'AddPoint',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
    COMMETHOD([helpstring(u'Stops the feedback and returns the shape.')], HRESULT, 'Stop',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPolygon)), 'polyline' )),
]
################################################################
## code template for INewPolygonFeedback implementation
##class INewPolygonFeedback_Impl(object):
##    def Start(self, Point):
##        u'Begins a normal feedback at the given point.'
##        #return 
##
##    def Stop(self):
##        u'Stops the feedback and returns the shape.'
##        #return polyline
##
##    def AddPoint(self, Point):
##        u'Creates a node at the given point.'
##        #return 
##

class GeometricEffectDash(CoClass):
    u'Generates a dashed/dotted line based on a template.'
    _reg_clsid_ = GUID('{760E5233-1BE3-4C73-8C2D-7C2DBFC0488A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
GeometricEffectDash._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGeometricEffect, IGraphicAttributes, IGraphicAttributes2, IEditInteraction, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

IGradientFillSymbol._methods_ = [
    COMMETHOD(['propget', helpstring(u'Gradient fill style.')], HRESULT, 'Style',
              ( ['retval', 'out'], POINTER(esriGradientFillStyle), 'Style' )),
    COMMETHOD(['propput', helpstring(u'Gradient fill style.')], HRESULT, 'Style',
              ( ['in'], esriGradientFillStyle, 'Style' )),
    COMMETHOD(['propget', helpstring(u'Direction of fill gradient.')], HRESULT, 'GradientAngle',
              ( ['retval', 'out'], POINTER(c_double), 'Angle' )),
    COMMETHOD(['propput', helpstring(u'Direction of fill gradient.')], HRESULT, 'GradientAngle',
              ( ['in'], c_double, 'Angle' )),
    COMMETHOD(['propget', helpstring(u'Color ramp property.')], HRESULT, 'ColorRamp',
              ( ['retval', 'out'], POINTER(POINTER(IColorRamp)), 'Ramp' )),
    COMMETHOD(['propput', helpstring(u'Color ramp property.')], HRESULT, 'ColorRamp',
              ( ['in'], POINTER(IColorRamp), 'Ramp' )),
    COMMETHOD(['propget', helpstring(u'Gradient percentage - controls the bleeding effect of the fill.')], HRESULT, 'GradientPercentage',
              ( ['retval', 'out'], POINTER(c_double), 'pct' )),
    COMMETHOD(['propput', helpstring(u'Gradient percentage - controls the bleeding effect of the fill.')], HRESULT, 'GradientPercentage',
              ( ['in'], c_double, 'pct' )),
    COMMETHOD(['propget', helpstring(u'Interval count - controls number of colors in the color ramp.')], HRESULT, 'IntervalCount',
              ( ['retval', 'out'], POINTER(c_int), 'IntervalCount' )),
    COMMETHOD(['propput', helpstring(u'Interval count - controls number of colors in the color ramp.')], HRESULT, 'IntervalCount',
              ( ['in'], c_int, 'IntervalCount' )),
]
################################################################
## code template for IGradientFillSymbol implementation
##class IGradientFillSymbol_Impl(object):
##    def _get(self):
##        u'Color ramp property.'
##        #return Ramp
##    def _set(self, Ramp):
##        u'Color ramp property.'
##    ColorRamp = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Gradient fill style.'
##        #return Style
##    def _set(self, Style):
##        u'Gradient fill style.'
##    Style = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Direction of fill gradient.'
##        #return Angle
##    def _set(self, Angle):
##        u'Direction of fill gradient.'
##    GradientAngle = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Gradient percentage - controls the bleeding effect of the fill.'
##        #return pct
##    def _set(self, pct):
##        u'Gradient percentage - controls the bleeding effect of the fill.'
##    GradientPercentage = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Interval count - controls number of colors in the color ramp.'
##        #return IntervalCount
##    def _set(self, IntervalCount):
##        u'Interval count - controls number of colors in the color ramp.'
##    IntervalCount = property(_get, _set, doc = _set.__doc__)
##

class MoveTextAlongShapeFeedback(CoClass):
    u'Move Text Following Geometry Display Feedback Object.'
    _reg_clsid_ = GUID('{24D1E2B3-AD64-4B5A-9F84-A19C33C9D79D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IMoveTextAlongShapeFeedback(IDisplayFeedback):
    _case_insensitive_ = True
    u'Provides access to members that control the move text along shape feedback.'
    _iid_ = GUID('{B44637C6-F488-41B4-B222-07AA9C04A3D6}')
    _idlflags_ = ['oleautomation']
MoveTextAlongShapeFeedback._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMoveTextAlongShapeFeedback]

class GeometricEffectMove(CoClass):
    u'Applies a move transformation to a geometry.'
    _reg_clsid_ = GUID('{8E00D76E-5A54-4C2D-9218-F7F5FC069ECE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
GeometricEffectMove._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGeometricEffect, IGraphicAttributes, IGraphicAttributes2, IEditInteraction, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

class GeometricEffectAddControlPoints(CoClass):
    u'Assigns control point status to line vertices.'
    _reg_clsid_ = GUID('{F3F86FB6-F732-4580-8ED9-E99112807B1B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
GeometricEffectAddControlPoints._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGeometricEffect, IGraphicAttributes, IGraphicAttributes2, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

class MoveCurvedTextFeedback(CoClass):
    u'Move Curved Text Display Feedback Object.'
    _reg_clsid_ = GUID('{A8BECDF3-90DD-4452-8DF9-37D8577C8C94}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IMoveCurvedTextFeedback(IDisplayFeedback):
    _case_insensitive_ = True
    u'Provides access to members that control the move curved text feedback.'
    _iid_ = GUID('{4516B1D1-F799-4902-A4DD-1CBAE5035BE3}')
    _idlflags_ = ['oleautomation']
MoveCurvedTextFeedback._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMoveCurvedTextFeedback]

class GraphicAttributeDashType(CoClass):
    u'Dash graphic attribute type.'
    _reg_clsid_ = GUID('{E35A38F8-293F-462E-9D32-672D88852C2C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IGraphicAttributeTypeUsingUnits(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods dealing with graphic attribute types that are using to units. This interface is only used for UI purposes.'
    _iid_ = GUID('{4D15C7A5-3A25-4935-AAA7-F60596632A6F}')
    _idlflags_ = ['oleautomation']
GraphicAttributeDashType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGraphicAttributeType, IGraphicAttributeDashType, IGraphicAttributeTypeUsingUnits]


# values for enumeration 'esriResampleRatio'
esriRasterOutputBest = 1
esriRasterOutputNormal = 3
esriRasterOutputDraft = 5
esriResampleRatio = c_int # enum
IDotDensityFillSymbol._methods_ = [
    COMMETHOD(['propget', helpstring(u'The size of dots used to fill.')], HRESULT, 'DotSize',
              ( ['retval', 'out'], POINTER(c_double), 'DotSize' )),
    COMMETHOD(['propput', helpstring(u'The size of dots used to fill.')], HRESULT, 'DotSize',
              ( ['in'], c_double, 'DotSize' )),
    COMMETHOD(['propget', helpstring(u'The number of dots used to fill.')], HRESULT, 'DotCount',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(c_int), 'DotCount' )),
    COMMETHOD(['propput', helpstring(u'The number of dots used to fill.')], HRESULT, 'DotCount',
              ( ['in'], c_int, 'index' ),
              ( ['in'], c_int, 'DotCount' )),
    COMMETHOD(['propget', helpstring(u'The distance between dot centers, expressed as a percentage of dot size.')], HRESULT, 'DotSpacing',
              ( ['retval', 'out'], POINTER(c_double), 'DotSpacing' )),
    COMMETHOD(['propput', helpstring(u'The distance between dot centers, expressed as a percentage of dot size.')], HRESULT, 'DotSpacing',
              ( ['in'], c_double, 'DotSpacing' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the dots are always placed at the same location (the alternative is random placement).')], HRESULT, 'FixedPlacement',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'FixedPlacement' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the dots are always placed at the same location (the alternative is random placement).')], HRESULT, 'FixedPlacement',
              ( ['in'], VARIANT_BOOL, 'FixedPlacement' )),
    COMMETHOD(['propget', helpstring(u'The background color.')], HRESULT, 'BackgroundColor',
              ( ['retval', 'out'], POINTER(POINTER(IColor)), 'Color' )),
    COMMETHOD(['propput', helpstring(u'The background color.')], HRESULT, 'BackgroundColor',
              ( ['in'], POINTER(IColor), 'Color' )),
]
################################################################
## code template for IDotDensityFillSymbol implementation
##class IDotDensityFillSymbol_Impl(object):
##    def _get(self):
##        u'The background color.'
##        #return Color
##    def _set(self, Color):
##        u'The background color.'
##    BackgroundColor = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the dots are always placed at the same location (the alternative is random placement).'
##        #return FixedPlacement
##    def _set(self, FixedPlacement):
##        u'Indicates if the dots are always placed at the same location (the alternative is random placement).'
##    FixedPlacement = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self, index):
##        u'The number of dots used to fill.'
##        #return DotCount
##    def _set(self, index, DotCount):
##        u'The number of dots used to fill.'
##    DotCount = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The size of dots used to fill.'
##        #return DotSize
##    def _set(self, DotSize):
##        u'The size of dots used to fill.'
##    DotSize = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The distance between dot centers, expressed as a percentage of dot size.'
##        #return DotSpacing
##    def _set(self, DotSpacing):
##        u'The distance between dot centers, expressed as a percentage of dot size.'
##    DotSpacing = property(_get, _set, doc = _set.__doc__)
##

class IPostScriptColor(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the post script color.'
    _iid_ = GUID('{6060613E-1233-11D3-9F45-00C04F6BC709}')
    _idlflags_ = ['oleautomation']
IPostScriptColor._methods_ = [
    COMMETHOD(['propput', helpstring(u'Indicates if the color overprints.')], HRESULT, 'Overprint',
              ( ['in'], VARIANT_BOOL, 'flag' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the color overprints.')], HRESULT, 'Overprint',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the color is a spot color.')], HRESULT, 'SpotColor',
              ( ['in'], VARIANT_BOOL, 'isSpot' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the color is a spot color.')], HRESULT, 'SpotColor',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'isSpot' )),
    COMMETHOD(['propput', helpstring(u'The description of the spot plate.')], HRESULT, 'SpotDescription',
              ( ['in'], BSTR, 'desc' )),
    COMMETHOD(['propget', helpstring(u'The description of the spot plate.')], HRESULT, 'SpotDescription',
              ( ['retval', 'out'], POINTER(BSTR), 'desc' )),
    COMMETHOD(['propput', helpstring(u'The saturation of the spot plate.')], HRESULT, 'SpotPercentage',
              ( ['in'], c_short, 'percent' )),
    COMMETHOD(['propget', helpstring(u'The saturation of the spot plate.')], HRESULT, 'SpotPercentage',
              ( ['retval', 'out'], POINTER(c_short), 'percent' )),
]
################################################################
## code template for IPostScriptColor implementation
##class IPostScriptColor_Impl(object):
##    def _get(self):
##        u'The description of the spot plate.'
##        #return desc
##    def _set(self, desc):
##        u'The description of the spot plate.'
##    SpotDescription = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the color is a spot color.'
##        #return isSpot
##    def _set(self, isSpot):
##        u'Indicates if the color is a spot color.'
##    SpotColor = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The saturation of the spot plate.'
##        #return percent
##    def _set(self, percent):
##        u'The saturation of the spot plate.'
##    SpotPercentage = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the color overprints.'
##        #return flag
##    def _set(self, flag):
##        u'Indicates if the color overprints.'
##    Overprint = property(_get, _set, doc = _set.__doc__)
##

class RotateTextFeedback(CoClass):
    u'Rotate Text Display Feedback Object.'
    _reg_clsid_ = GUID('{67628250-B721-48E1-B13B-4F574B8357A3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
RotateTextFeedback._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRotateTextFeedback]

class GeometricEffectOffset(CoClass):
    u'Offsets a line by a specified distance.'
    _reg_clsid_ = GUID('{8D5E6D99-745F-424E-81AB-A2C3BFEFBEB7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
GeometricEffectOffset._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGeometricEffect, IGraphicAttributes, IGraphicAttributes2, IEditInteraction, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

class GraphicAttributeSizeType(CoClass):
    u'Size graphic attribute type.'
    _reg_clsid_ = GUID('{B4CF9489-F10C-4647-85CE-6BC3143A30EF}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
GraphicAttributeSizeType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGraphicAttributeType, IGraphicAttributeTypeUsingUnits]

class NewTextFeedback(CoClass):
    u'Move Text Display Feedback Object.'
    _reg_clsid_ = GUID('{A01A77F0-D96A-4C4C-983C-C64190828C5A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
NewTextFeedback._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, INewTextFeedback]

class ILineFillSymbol(IFillSymbol):
    _case_insensitive_ = True
    u'Provides access to members that control the line fill symbol.'
    _iid_ = GUID('{7914E5EF-C892-11D0-8BB6-080009EE4E41}')
    _idlflags_ = ['oleautomation']
ILineFillSymbol._methods_ = [
    COMMETHOD(['propget', helpstring(u'Line symbol used for fill.')], HRESULT, 'LineSymbol',
              ( ['retval', 'out'], POINTER(POINTER(ILineSymbol)), 'lineSym' )),
    COMMETHOD(['propputref', helpstring(u'Line symbol used for fill.')], HRESULT, 'LineSymbol',
              ( ['in'], POINTER(ILineSymbol), 'lineSym' )),
    COMMETHOD(['propget', helpstring(u'Line symbol angle within fill.')], HRESULT, 'Angle',
              ( ['retval', 'out'], POINTER(c_double), 'Angle' )),
    COMMETHOD(['propput', helpstring(u'Line symbol angle within fill.')], HRESULT, 'Angle',
              ( ['in'], c_double, 'Angle' )),
    COMMETHOD(['propget', helpstring(u'Line symbol separation within fill.')], HRESULT, 'Separation',
              ( ['retval', 'out'], POINTER(c_double), 'Separation' )),
    COMMETHOD(['propput', helpstring(u'Line symbol separation within fill.')], HRESULT, 'Separation',
              ( ['in'], c_double, 'Separation' )),
    COMMETHOD(['propget', helpstring(u'Line fill offset.')], HRESULT, 'Offset',
              ( ['retval', 'out'], POINTER(c_double), 'Offset' )),
    COMMETHOD(['propput', helpstring(u'Line fill offset.')], HRESULT, 'Offset',
              ( ['in'], c_double, 'Offset' )),
]
################################################################
## code template for ILineFillSymbol implementation
##class ILineFillSymbol_Impl(object):
##    def _get(self):
##        u'Line symbol angle within fill.'
##        #return Angle
##    def _set(self, Angle):
##        u'Line symbol angle within fill.'
##    Angle = property(_get, _set, doc = _set.__doc__)
##
##    def LineSymbol(self, lineSym):
##        u'Line symbol used for fill.'
##        #return 
##
##    def _get(self):
##        u'Line symbol separation within fill.'
##        #return Separation
##    def _set(self, Separation):
##        u'Line symbol separation within fill.'
##    Separation = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Line fill offset.'
##        #return Offset
##    def _set(self, Offset):
##        u'Line fill offset.'
##    Offset = property(_get, _set, doc = _set.__doc__)
##

class GeometricEffectScale(CoClass):
    u'Applies a scale transformation to a geometry.'
    _reg_clsid_ = GUID('{E9793E91-698A-4C45-8F09-B43683E49B93}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
GeometricEffectScale._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGeometricEffect, IGraphicAttributes, IGraphicAttributes2, IEditInteraction, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

class NewTextBezierCurveFeedback(CoClass):
    u'New Curved Text Display Feedback Object.'
    _reg_clsid_ = GUID('{71957F32-4D7A-4374-A117-6969F9B820D5}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class INewTextBezierCurveFeedback(IDisplayFeedback):
    _case_insensitive_ = True
    u'Provides access to members that control the new text bezier curve display feedback.'
    _iid_ = GUID('{5C3AC217-10C5-401B-B3EB-6A6D93E5D58C}')
    _idlflags_ = ['oleautomation']
NewTextBezierCurveFeedback._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, INewTextBezierCurveFeedback]

class IUpdateLegendInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to dirty flag for some legend classes.'
    _iid_ = GUID('{272369D5-140A-444B-A505-0983BDDCDBAB}')
    _idlflags_ = ['oleautomation']
IUpdateLegendInfo._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates whether legend class has been modified.')], HRESULT, 'Update',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bUpdate' )),
    COMMETHOD([helpstring(u'Clear the update flag.')], HRESULT, 'ResetUpdate'),
]
################################################################
## code template for IUpdateLegendInfo implementation
##class IUpdateLegendInfo_Impl(object):
##    def ResetUpdate(self):
##        u'Clear the update flag.'
##        #return 
##
##    @property
##    def Update(self):
##        u'Indicates whether legend class has been modified.'
##        #return bUpdate
##

class MoveBitmapFeedback(CoClass):
    u'Move Bitmap Display Feedback Object.'
    _reg_clsid_ = GUID('{4993083D-DEE5-42AB-B312-2E038296D186}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
MoveBitmapFeedback._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMoveBitmapFeedback]

class GraphicAttributeTextType(CoClass):
    u'Text graphic attribute type.'
    _reg_clsid_ = GUID('{29E48D6D-55E3-401D-A245-EE275E560423}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
GraphicAttributeTextType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGraphicAttributeType]

class GeometricEffectExtension(CoClass):
    u'Extends a line by a given distance and deflection angle.'
    _reg_clsid_ = GUID('{F1AC7478-67EB-4C77-ADC4-5491BB44F140}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
GeometricEffectExtension._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGeometricEffect, IGraphicAttributes, IGraphicAttributes2, IEditInteraction, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

IScreenDisplayOverlaysCallback._methods_ = [
    COMMETHOD(['propget', helpstring(u'Draw overlays to the specified DC.')], HRESULT, 'OverlayCount',
              ( ['retval', 'out'], POINTER(c_int), 'OverlayCount' )),
    COMMETHOD(['propget', helpstring(u'Draw overlays to the specified DC.')], HRESULT, 'OverlayExtent',
              ( ['in'], c_int, 'overlayIdx' ),
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.tagRECT), 'extent' )),
    COMMETHOD(['propget', helpstring(u'Get bitmap for the specified overlay (Optional). ')], HRESULT, 'OverlayBitmap',
              ( ['in'], c_int, 'overlayIdx' ),
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'hBitmap' )),
    COMMETHOD([helpstring(u'Draw overlays to the specified DC.')], HRESULT, 'DrawOverlay',
              ( ['in'], c_int, 'overlayIdx' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDC' )),
]
################################################################
## code template for IScreenDisplayOverlaysCallback implementation
##class IScreenDisplayOverlaysCallback_Impl(object):
##    @property
##    def OverlayCount(self):
##        u'Draw overlays to the specified DC.'
##        #return OverlayCount
##
##    @property
##    def OverlayBitmap(self, overlayIdx):
##        u'Get bitmap for the specified overlay (Optional). '
##        #return hBitmap
##
##    @property
##    def OverlayExtent(self, overlayIdx):
##        u'Draw overlays to the specified DC.'
##        #return extent
##
##    def DrawOverlay(self, overlayIdx, hDC):
##        u'Draw overlays to the specified DC.'
##        #return 
##

class GraphicAttributeMarkerType(CoClass):
    u'Marker graphic attribute type.'
    _reg_clsid_ = GUID('{238B99DC-D2E6-4C01-83AC-E0F912432DB8}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
GraphicAttributeMarkerType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGraphicAttributeType]

class NewRectangleFeedback(CoClass):
    u'New Rectangle Feedback Object.'
    _reg_clsid_ = GUID('{17180FE3-5314-40D8-8405-22EFBE28C202}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
NewRectangleFeedback._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDisplayFeedback2, INewRectangleFeedback]

IScreenInvalidate._methods_ = [
    COMMETHOD(['propget', helpstring(u'The bounds of the invalid region.')], HRESULT, 'InvalidEnvelope',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'envelope' )),
    COMMETHOD(['propget', helpstring(u'The bounds of the invalid region.')], HRESULT, 'InvalidArea',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IArea)), 'area' )),
    COMMETHOD([helpstring(u'Cause the specified area of the specified cache to redraw.')], HRESULT, 'Invalidate',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'rect' ),
              ( ['in'], VARIANT_BOOL, 'erase' ),
              ( ['in'], c_short, 'cacheIndex' )),
    COMMETHOD([helpstring(u'Cause the specified area of the specified cache to redraw.  Use symbolSizePoints to specify point sizes and line widths.')], HRESULT, 'InvalidateShape',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'pGeometry' ),
              ( ['in'], c_double, 'symbolSizePoints' ),
              ( ['in'], VARIANT_BOOL, 'erase' ),
              ( ['in'], c_short, 'cacheIndex' )),
    COMMETHOD([helpstring(u'Clear dirty flag for specified cache.')], HRESULT, 'Validate',
              ( ['in'], c_short, 'cacheIndex' )),
]
################################################################
## code template for IScreenInvalidate implementation
##class IScreenInvalidate_Impl(object):
##    @property
##    def InvalidArea(self):
##        u'The bounds of the invalid region.'
##        #return area
##
##    @property
##    def InvalidEnvelope(self):
##        u'The bounds of the invalid region.'
##        #return envelope
##
##    def Validate(self, cacheIndex):
##        u'Clear dirty flag for specified cache.'
##        #return 
##
##    def InvalidateShape(self, pGeometry, symbolSizePoints, erase, cacheIndex):
##        u'Cause the specified area of the specified cache to redraw.  Use symbolSizePoints to specify point sizes and line widths.'
##        #return 
##
##    def Invalidate(self, rect, erase, cacheIndex):
##        u'Cause the specified area of the specified cache to redraw.'
##        #return 
##

class GraphicAttributeColorType(CoClass):
    u'Color graphic attribute type.'
    _reg_clsid_ = GUID('{584739C6-22D9-4BA6-8A31-6E09196931C1}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
GraphicAttributeColorType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGraphicAttributeType]

class NewEllipseFeedback(CoClass):
    u'New Ellipse Feedback Object.'
    _reg_clsid_ = GUID('{24C40AA3-D25A-4E31-B3B0-F87662491514}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class INewEllipseFeedback(IDisplayFeedback2):
    _case_insensitive_ = True
    u'Provides access to members that control the creation of a new ellipse.'
    _iid_ = GUID('{70D00F17-C4F7-4339-B47F-A221C4E7D595}')
    _idlflags_ = ['oleautomation']
NewEllipseFeedback._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDisplayFeedback2, INewEllipseFeedback]

class GeometricEffectOffsetTangent(CoClass):
    u'Moves a line a given distance in the direction of one of its outermost segments.'
    _reg_clsid_ = GUID('{DC2E2EA2-2BCA-4D4B-95EE-51CF724380E8}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
GeometricEffectOffsetTangent._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGeometricEffect, IGraphicAttributes, IGraphicAttributes2, IEditInteraction, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

class GeometricEffectCut(CoClass):
    u'Produces a shorter line based on distances at extremities.'
    _reg_clsid_ = GUID('{BA1849B9-4640-42B2-ABCF-D7F4CBF2F3D1}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
GeometricEffectCut._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGeometricEffect, IGraphicAttributes, IGraphicAttributes2, IEditInteraction, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

class ICharacterOrientation(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to characters orientation.'
    _iid_ = GUID('{1FA841F8-A2CB-433D-88AC-10A945852320}')
    _idlflags_ = ['oleautomation']
ICharacterOrientation._methods_ = [
    COMMETHOD(['propput', helpstring(u'Indicates if CJK charcters are rotated.')], HRESULT, 'CJKCharactersRotation',
              ( ['in'], VARIANT_BOOL, 'Rotation' )),
    COMMETHOD(['propget', helpstring(u'Indicates if CJK charcters are rotated.')], HRESULT, 'CJKCharactersRotation',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Rotation' )),
]
################################################################
## code template for ICharacterOrientation implementation
##class ICharacterOrientation_Impl(object):
##    def _get(self):
##        u'Indicates if CJK charcters are rotated.'
##        #return Rotation
##    def _set(self, Rotation):
##        u'Indicates if CJK charcters are rotated.'
##    CJKCharactersRotation = property(_get, _set, doc = _set.__doc__)
##

IDisplayFiltersControl._methods_ = [
    COMMETHOD([helpstring(u'Pushes and activates the Display filter.  Must call while in a StartDrawing-FinishDrawing sequence.')], HRESULT, 'PushFilter',
              ( ['in'], POINTER(IDisplayFilter), 'Filter' )),
    COMMETHOD([helpstring(u'Pops last Display filter.  Must call while in a StartDrawing-FinishDrawing sequence.')], HRESULT, 'PopFilter'),
    COMMETHOD(['propget', helpstring(u'Gets current Display filter.  Must call while in a StartDrawing-FinishDrawing sequence.')], HRESULT, 'CurrentFilter',
              ( ['retval', 'out'], POINTER(POINTER(IDisplayFilter)), 'Filter' )),
]
################################################################
## code template for IDisplayFiltersControl implementation
##class IDisplayFiltersControl_Impl(object):
##    def PushFilter(self, Filter):
##        u'Pushes and activates the Display filter.  Must call while in a StartDrawing-FinishDrawing sequence.'
##        #return 
##
##    @property
##    def CurrentFilter(self):
##        u'Gets current Display filter.  Must call while in a StartDrawing-FinishDrawing sequence.'
##        #return Filter
##
##    def PopFilter(self):
##        u'Pops last Display filter.  Must call while in a StartDrawing-FinishDrawing sequence.'
##        #return 
##

IDotDensityFillSymbol2._methods_ = [
    COMMETHOD(['propget', helpstring(u'Defines how the random generator is initialized to draw dots randomly.')], HRESULT, 'RandomSeed',
              ( ['retval', 'out'], POINTER(VARIANT), 'Seed' )),
    COMMETHOD(['propput', helpstring(u'Defines how the random generator is initialized to draw dots randomly.')], HRESULT, 'RandomSeed',
              ( ['in'], VARIANT, 'Seed' )),
]
################################################################
## code template for IDotDensityFillSymbol2 implementation
##class IDotDensityFillSymbol2_Impl(object):
##    def _get(self):
##        u'Defines how the random generator is initialized to draw dots randomly.'
##        #return Seed
##    def _set(self, Seed):
##        u'Defines how the random generator is initialized to draw dots randomly.'
##    RandomSeed = property(_get, _set, doc = _set.__doc__)
##

class LineStroke(CoClass):
    u'A line stroke object.'
    _reg_clsid_ = GUID('{BD2A7F5C-1D8B-4221-B3B0-7F40B0305503}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
LineStroke._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ILineStroke, IGraphicAttributes, IGraphicAttributes2, IDrawingOutline, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]


# values for enumeration 'esriMarkerPlacementAttributes'
esriGAAlongLineStep = 0
esriGAAlongLineEndings = 1
esriGAAlongLineControlPoints = 2
esriGAAlongLineAngleToLine = 3
esriGAAlongLinePosition = 4
esriGAAlongLineOffsetAtEnd = 5
esriGAAtExtremitiesType = 0
esriGAAtExtremitiesOffset = 1
esriGAAtExtremitiesAngleToLine = 2
esriGADecorationNumberOfPositions = 0
esriGADecorationBeginGap = 1
esriGADecorationEndGap = 2
esriGADecorationFlipAll = 3
esriGADecorationFlipFirst = 4
esriGADecorationAngleToLine = 5
esriGAInsidePolygonXStep = 0
esriGAInsidePolygonYStep = 1
esriGAInsidePolygonGridAngle = 2
esriGAInsidePolygonShiftOddRows = 3
esriGAInsidePolygonXOffset = 4
esriGAInsidePolygonYOffset = 5
esriGAInsidePolygonClipping = 6
esriGAOnLinePosition = 0
esriGAOnLineRelativeTo = 1
esriGAOnLineAngleToLine = 2
esriGAOnPointXOffset = 0
esriGAOnPointYOffset = 1
esriGAPolygonCenterXOffset = 0
esriGAPolygonCenterYOffset = 1
esriGAPolygonCenterMethod = 2
esriGAPolygonCenterClipping = 3
esriGARandomAlongLineStep = 0
esriGARandomAlongLineEndings = 1
esriGARandomAlongLineControlPoints = 2
esriGARandomAlongLineRandom = 3
esriGARandomAlongLineSkewEffect = 4
esriGARandomAlongLineSeed = 5
esriGARandomAlongLinePosition = 6
esriGARandomAlongLineOffsetAtEnd = 7
esriGARandomInsidePolygonXOffset = 0
esriGARandomInsidePolygonYOffset = 1
esriGARandomInsidePolygonClipping = 2
esriGARandomInsidePolygonSeed = 3
esriGAVariableAlongLineStep = 0
esriGAVariableAlongLineEndings = 1
esriGAVariableAlongLineControlPoints = 2
esriGAVariableAlongLineMinZoom = 3
esriGAVariableAlongLineMaxZoom = 4
esriGAVariableAlongLineZoomNumber = 5
esriGAVariableAlongLineMethod = 6
esriGAVariableAlongLineOffset = 7
esriGAVariableAlongLineSeed = 8
esriGAOnVerticesEndPoints = 0
esriGAOnVerticesControlPoints = 1
esriGAOnVerticesRegularVertices = 2
esriGAOnVerticesAngleToLine = 3
esriMarkerPlacementAttributes = c_int # enum
ITextBackground._methods_ = [
    COMMETHOD(['propget', helpstring(u'The text symbol.')], HRESULT, 'TextSymbol',
              ( ['retval', 'out'], POINTER(POINTER(ITextSymbol)), 'textSym' )),
    COMMETHOD(['propputref', helpstring(u'The text symbol.')], HRESULT, 'TextSymbol',
              ( ['in'], POINTER(ITextSymbol), 'textSym' )),
    COMMETHOD(['propputref', helpstring(u'The text box.')], HRESULT, 'TextBox',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'rhs' )),
    COMMETHOD([helpstring(u'Queries for the boundary of the text background.')], HRESULT, 'QueryBoundary',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDC' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ITransformation), 'transform' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPolygon), 'boundary' )),
    COMMETHOD([helpstring(u'Draws the text background.')], HRESULT, 'Draw',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDC' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ITransformation), 'transform' )),
]
################################################################
## code template for ITextBackground implementation
##class ITextBackground_Impl(object):
##    def Draw(self, hDC, transform):
##        u'Draws the text background.'
##        #return 
##
##    def TextBox(self, rhs):
##        u'The text box.'
##        #return 
##
##    def QueryBoundary(self, hDC, transform, boundary):
##        u'Queries for the boundary of the text background.'
##        #return 
##
##    def TextSymbol(self, textSym):
##        u'The text symbol.'
##        #return 
##

class IDynamicDrawScreen(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to Dynamic Screen Draw.'
    _iid_ = GUID('{6F74EFD8-1CE5-4012-B5FA-CBC9DFB17132}')
    _idlflags_ = ['oleautomation']
IDynamicDrawScreen._methods_ = [
    COMMETHOD([helpstring(u'Draws a marker at the specified points on the screen.')], HRESULT, 'DrawScreenMultipleMarkers',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPointCollection), 'pointCollection' )),
    COMMETHOD([helpstring(u'Draws a marker at the specified point on the screen.')], HRESULT, 'DrawScreenMarker',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
    COMMETHOD([helpstring(u'Draws specified polygon with fill and line on the screen.')], HRESULT, 'DrawScreenPolygon',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPointCollection), 'pointCollection' )),
    COMMETHOD([helpstring(u'Draws specified lines on the screen.')], HRESULT, 'DrawScreenMultipleLines',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPointCollection), 'pointCollection' )),
    COMMETHOD([helpstring(u'Draws a line between the specified points on the screen.')], HRESULT, 'DrawScreenLine',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'startPoint' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'endPoint' )),
    COMMETHOD([helpstring(u'Draws specified polyline on the screen.')], HRESULT, 'DrawScreenPolyline',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPointCollection), 'pointCollection' )),
    COMMETHOD([helpstring(u'Draws specified rectangle with fill and line on the screen.')], HRESULT, 'DrawScreenRectangle',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'envelope' )),
    COMMETHOD([helpstring(u'Draws text at the specified point on the screen.')], HRESULT, 'DrawScreenText',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' ),
              ( ['in'], BSTR, 'Text' )),
]
################################################################
## code template for IDynamicDrawScreen implementation
##class IDynamicDrawScreen_Impl(object):
##    def DrawScreenLine(self, startPoint, endPoint):
##        u'Draws a line between the specified points on the screen.'
##        #return 
##
##    def DrawScreenText(self, Point, Text):
##        u'Draws text at the specified point on the screen.'
##        #return 
##
##    def DrawScreenPolyline(self, pointCollection):
##        u'Draws specified polyline on the screen.'
##        #return 
##
##    def DrawScreenMultipleMarkers(self, pointCollection):
##        u'Draws a marker at the specified points on the screen.'
##        #return 
##
##    def DrawScreenMarker(self, Point):
##        u'Draws a marker at the specified point on the screen.'
##        #return 
##
##    def DrawScreenPolygon(self, pointCollection):
##        u'Draws specified polygon with fill and line on the screen.'
##        #return 
##
##    def DrawScreenMultipleLines(self, pointCollection):
##        u'Draws specified lines on the screen.'
##        #return 
##
##    def DrawScreenRectangle(self, envelope):
##        u'Draws specified rectangle with fill and line on the screen.'
##        #return 
##

ITextPath._methods_ = [
    COMMETHOD([helpstring(u'Set up items needed by text path.')], HRESULT, 'Setup',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDC' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ITransformation), 'Transformation' ),
              ( ['in'], POINTER(ITextSymbol), 'textSym' )),
    COMMETHOD(['propget', helpstring(u'The geometry used for the path.')], HRESULT, 'Geometry',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry)), 'Geometry' )),
    COMMETHOD(['propputref', helpstring(u'The geometry used for the path.')], HRESULT, 'Geometry',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'Geometry' )),
    COMMETHOD(['propget', helpstring(u'The X offset value.')], HRESULT, 'XOffset',
              ( ['retval', 'out'], POINTER(c_double), 'XOffset' )),
    COMMETHOD(['propput', helpstring(u'The X offset value.')], HRESULT, 'XOffset',
              ( ['in'], c_double, 'XOffset' )),
    COMMETHOD(['propget', helpstring(u'The Y offset value.')], HRESULT, 'YOffset',
              ( ['retval', 'out'], POINTER(c_double), 'YOffset' )),
    COMMETHOD(['propput', helpstring(u'The Y offset value.')], HRESULT, 'YOffset',
              ( ['in'], c_double, 'YOffset' )),
    COMMETHOD([helpstring(u'Returns the next coordinate.')], HRESULT, 'Next',
              ( ['out'], POINTER(c_double), 'x' ),
              ( ['out'], POINTER(c_double), 'y' ),
              ( ['out'], POINTER(c_double), 'Angle' )),
    COMMETHOD([helpstring(u'Resets the coordinate enumerator.')], HRESULT, 'Reset'),
]
################################################################
## code template for ITextPath implementation
##class ITextPath_Impl(object):
##    def Reset(self):
##        u'Resets the coordinate enumerator.'
##        #return 
##
##    def Geometry(self, Geometry):
##        u'The geometry used for the path.'
##        #return 
##
##    def Setup(self, hDC, Transformation, textSym):
##        u'Set up items needed by text path.'
##        #return 
##
##    def Next(self):
##        u'Returns the next coordinate.'
##        #return x, y, Angle
##
##    def _get(self):
##        u'The Y offset value.'
##        #return YOffset
##    def _set(self, YOffset):
##        u'The Y offset value.'
##    YOffset = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The X offset value.'
##        #return XOffset
##    def _set(self, XOffset):
##        u'The X offset value.'
##    XOffset = property(_get, _set, doc = _set.__doc__)
##

class CharacterMarkerSymbol(CoClass):
    u'A marker symbol based on a character from a font.'
    _reg_clsid_ = GUID('{7914E600-C892-11D0-8BB6-080009EE4E41}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
CharacterMarkerSymbol._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ICharacterMarkerSymbol, IMapLevel, ISymbol, ICartographicMarkerSymbol, ISymbolRotation, IMarkerMask, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySupport, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, IDisplayName, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLVersionSupport]

class LineTracker(CoClass):
    u'Display feedback for line tracking.'
    _reg_clsid_ = GUID('{8AB7FBE3-D871-11D0-8389-080009B996CC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
LineTracker._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ISelectionTracker, IPointCollectionTracker]

IGraphicAttributes._methods_ = [
    COMMETHOD(['propget', helpstring(u'Number of graphic attributes.')], HRESULT, 'GraphicAttributeCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'ID of graphic attributes.')], HRESULT, 'ID',
              ( ['in'], c_int, 'attrIndex' ),
              ( ['retval', 'out'], POINTER(c_int), 'attrId' )),
    COMMETHOD(['propget', helpstring(u'Name of the graphic attribute.')], HRESULT, 'Name',
              ( ['in'], c_int, 'attrId' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'Type of the graphic attribute.')], HRESULT, 'Type',
              ( ['in'], c_int, 'attrId' ),
              ( ['retval', 'out'], POINTER(POINTER(IGraphicAttributeType)), 'Type' )),
    COMMETHOD(['propget', helpstring(u'Value of the graphic attribute. To erase override, set value to NULL or to original value.')], HRESULT, 'Value',
              ( ['in'], c_int, 'attrId' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'val' )),
    COMMETHOD(['propput', helpstring(u'Value of the graphic attribute. To erase override, set value to NULL or to original value.')], HRESULT, 'Value',
              ( ['in'], c_int, 'attrId' ),
              ( ['in'], VARIANT, 'val' )),
    COMMETHOD(['propget', helpstring(u'ID of the graphic attribute, given its name.')], HRESULT, 'IDByName',
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(c_int), 'index' )),
    COMMETHOD(['propget', helpstring(u'Class name of the graphic attribute.')], HRESULT, 'ClassName',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
]
################################################################
## code template for IGraphicAttributes implementation
##class IGraphicAttributes_Impl(object):
##    @property
##    def GraphicAttributeCount(self):
##        u'Number of graphic attributes.'
##        #return Count
##
##    @property
##    def IDByName(self, Name):
##        u'ID of the graphic attribute, given its name.'
##        #return index
##
##    def _get(self, attrId):
##        u'Value of the graphic attribute. To erase override, set value to NULL or to original value.'
##        #return val
##    def _set(self, attrId, val):
##        u'Value of the graphic attribute. To erase override, set value to NULL or to original value.'
##    Value = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def ClassName(self):
##        u'Class name of the graphic attribute.'
##        #return Name
##
##    @property
##    def Type(self, attrId):
##        u'Type of the graphic attribute.'
##        #return Type
##
##    @property
##    def ID(self, attrIndex):
##        u'ID of graphic attributes.'
##        #return attrId
##
##    @property
##    def Name(self, attrId):
##        u'Name of the graphic attribute.'
##        #return Name
##

IGraphicAttributes2._methods_ = [
    COMMETHOD(['propget', helpstring(u'Caption of the graphic attribute.')], HRESULT, 'Caption',
              ( ['in'], c_int, 'attrId' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Caption' )),
    COMMETHOD(['propget', helpstring(u'Caption of the object containing the graphic attributes.')], HRESULT, 'ClassCaption',
              ( ['in'], comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.esriGeometryType, 'geomType' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Caption' )),
]
################################################################
## code template for IGraphicAttributes2 implementation
##class IGraphicAttributes2_Impl(object):
##    @property
##    def Caption(self, attrId):
##        u'Caption of the graphic attribute.'
##        #return Caption
##
##    @property
##    def ClassCaption(self, geomType):
##        u'Caption of the object containing the graphic attributes.'
##        #return Caption
##

class HlsColor(CoClass):
    u'A color in the HLS(Hue, Luminance, Saturation) color system.'
    _reg_clsid_ = GUID('{7EE9C493-D123-11D0-8383-080009B996CC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
HlsColor._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IHlsColor, IColor, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize]

class PictureMarkerSymbol(CoClass):
    u'A marker symbol based on either a BMP or an EMF picture.'
    _reg_clsid_ = GUID('{7914E602-C892-11D0-8BB6-080009EE4E41}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
PictureMarkerSymbol._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IPictureMarkerSymbol, IMapLevel, ISymbol, ICartographicMarkerSymbol, ISymbolRotation, IMarkerMask, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySupport, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, IDisplayName, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize]

class IMoveTextFeedback(IDisplayFeedback):
    _case_insensitive_ = True
    u'Provides access to members that control the move text feedback.'
    _iid_ = GUID('{DD61D811-A912-48E6-9146-073D1264DA48}')
    _idlflags_ = ['oleautomation']
IMoveTextFeedback._methods_ = [
    COMMETHOD([helpstring(u'Specify the shape to follow.')], HRESULT, 'FollowShape',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'featureGeometry' ),
              ( ['in'], c_double, 'ReferenceScale' )),
    COMMETHOD([helpstring(u'Begins a move feedback of the given shape.')], HRESULT, 'Start',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'textGeometry' ),
              ( ['in'], c_double, 'labelWidth' ),
              ( ['in'], c_double, 'labelHeight' ),
              ( ['in'], c_double, 'ReferenceScale' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' ),
              ( ['in'], c_double, 'Offset' ),
              ( ['in'], VARIANT_BOOL, 'Parallel' ),
              ( ['in'], esriMoveTextConstraints, 'Constraint' )),
    COMMETHOD([helpstring(u'Stops the feedback and returns the shape.')], HRESULT, 'Stop',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry)), 'baseline' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether to flip the text.')], HRESULT, 'Flip',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Flip' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether to flip the text.')], HRESULT, 'Flip',
              ( ['in'], VARIANT_BOOL, 'Flip' )),
    COMMETHOD(['propget', helpstring(u'Offset the text from the geometry.')], HRESULT, 'Offset',
              ( ['retval', 'out'], POINTER(c_double), 'Offset' )),
    COMMETHOD(['propput', helpstring(u'Offset the text from the geometry.')], HRESULT, 'Offset',
              ( ['in'], c_double, 'Offset' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether to make the text parallel.')], HRESULT, 'Parallel',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Parallel' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether to make the text parallel.')], HRESULT, 'Parallel',
              ( ['in'], VARIANT_BOOL, 'Parallel' )),
    COMMETHOD(['propget', helpstring(u'Constrain the text.')], HRESULT, 'Constraint',
              ( ['retval', 'out'], POINTER(esriMoveTextConstraints), 'Constraint' )),
    COMMETHOD(['propput', helpstring(u'Constrain the text.')], HRESULT, 'Constraint',
              ( ['in'], esriMoveTextConstraints, 'Constraint' )),
]
################################################################
## code template for IMoveTextFeedback implementation
##class IMoveTextFeedback_Impl(object):
##    def FollowShape(self, featureGeometry, ReferenceScale):
##        u'Specify the shape to follow.'
##        #return 
##
##    def _get(self):
##        u'Constrain the text.'
##        #return Constraint
##    def _set(self, Constraint):
##        u'Constrain the text.'
##    Constraint = property(_get, _set, doc = _set.__doc__)
##
##    def Stop(self):
##        u'Stops the feedback and returns the shape.'
##        #return baseline
##
##    def _get(self):
##        u'Indicates whether to flip the text.'
##        #return Flip
##    def _set(self, Flip):
##        u'Indicates whether to flip the text.'
##    Flip = property(_get, _set, doc = _set.__doc__)
##
##    def Start(self, textGeometry, labelWidth, labelHeight, ReferenceScale, Point, Offset, Parallel, Constraint):
##        u'Begins a move feedback of the given shape.'
##        #return 
##
##    def _get(self):
##        u'Offset the text from the geometry.'
##        #return Offset
##    def _set(self, Offset):
##        u'Offset the text from the geometry.'
##    Offset = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether to make the text parallel.'
##        #return Parallel
##    def _set(self, Parallel):
##        u'Indicates whether to make the text parallel.'
##    Parallel = property(_get, _set, doc = _set.__doc__)
##

class ArrowMarkerSymbol(CoClass):
    u'A marker symbol created from a predefined arrow.'
    _reg_clsid_ = GUID('{88539431-E06E-11D1-B277-0000F878229E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
ArrowMarkerSymbol._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IArrowMarkerSymbol, IMapLevel, ISymbol, ISymbolRotation, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, IDisplayName, IMarkerMask, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySupport]


# values for enumeration 'esriGraphicAttribute'
esriGAVisibility = 0
esriGAMarker = 1
esriGAMarkerSize = 2
esriGAMarkerAngle = 3
esriGAMarkerRotateClockwise = 4
esriGAStrokeWidth = 0
esriGAStrokeCaps = 1
esriGAStrokeJoins = 2
esriGAStrokeColor = 3
esriGASolidColorPatternColor = 0
esriGALinePatternColor = 0
esriGALinePatternWidth = 1
esriGALinePatternAngle = 2
esriGALinePatternStep = 3
esriGALinePatternOffset = 4
esriGAGradientPatternColor1 = 0
esriGAGradientPatternColor2 = 1
esriGAGradientPatternStyle = 2
esriGAGradientPatternInterval = 3
esriGAGradientPatternPercent = 4
esriGAGradientPatternAlgorithm = 5
esriGAGradientPatternAngle = 6
esriGraphicAttribute = c_int # enum
class IFontName(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to FontName properties.'
    _iid_ = GUID('{77D415D5-5815-4322-87FF-A6940A790107}')
    _idlflags_ = ['oleautomation']
IFontName._methods_ = [
    COMMETHOD(['propget', helpstring(u'The name of the font.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propput', helpstring(u'The name of the font.')], HRESULT, 'Name',
              ( ['in'], BSTR, 'Name' )),
]
################################################################
## code template for IFontName implementation
##class IFontName_Impl(object):
##    def _get(self):
##        u'The name of the font.'
##        #return Name
##    def _set(self, Name):
##        u'The name of the font.'
##    Name = property(_get, _set, doc = _set.__doc__)
##

IFontAttribute._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if a boolean font attribute is set.')], HRESULT, 'State',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'State' )),
    COMMETHOD(['propput', helpstring(u'Indicates if a boolean font attribute is set.')], HRESULT, 'State',
              ( ['in'], VARIANT_BOOL, 'State' )),
]
################################################################
## code template for IFontAttribute implementation
##class IFontAttribute_Impl(object):
##    def _get(self):
##        u'Indicates if a boolean font attribute is set.'
##        #return State
##    def _set(self, State):
##        u'Indicates if a boolean font attribute is set.'
##    State = property(_get, _set, doc = _set.__doc__)
##

class MonitorSettings(CoClass):
    u'This object stores color settings specifically for one monitor to optimize color representation.'
    _reg_clsid_ = GUID('{9DB25FE0-3C75-11D2-AAF6-00C04FA334B3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
MonitorSettings._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMonitorSettings]

IDynamicScreenDisplay._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if dynamic display is turned on or off.')], HRESULT, 'DynamicDisplayEnabled',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'isEnable' )),
]
################################################################
## code template for IDynamicScreenDisplay implementation
##class IDynamicScreenDisplay_Impl(object):
##    @property
##    def DynamicDisplayEnabled(self):
##        u'Indicates if dynamic display is turned on or off.'
##        #return isEnable
##

IRepresentationMarker._methods_ = [
    COMMETHOD([helpstring(u'Draws the representation marker.')], HRESULT, 'Draw',
              ( ['in'], POINTER(IOutputContext), 'context' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IAffineTransformation2D), 'transfo' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'envelope' )),
    COMMETHOD(['propget', helpstring(u'The outline of the marker, returned as a polygon.')], HRESULT, 'Outline',
              ( ['in'], esriOutlineType, 'Type' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry)), 'Outline' )),
    COMMETHOD(['propget', helpstring(u'The size in points (1/72 of an inch) of the marker.')], HRESULT, 'Size',
              ( ['retval', 'out'], POINTER(c_double), 'Size' )),
    COMMETHOD(['propget', helpstring(u'The width in points (1/72 of an inch) of the marker.')], HRESULT, 'Width',
              ( ['retval', 'out'], POINTER(c_double), 'Width' )),
    COMMETHOD(['propget', helpstring(u'The height in points (1/72 of an inch) of the marker.')], HRESULT, 'Height',
              ( ['retval', 'out'], POINTER(c_double), 'Height' )),
]
################################################################
## code template for IRepresentationMarker implementation
##class IRepresentationMarker_Impl(object):
##    @property
##    def Width(self):
##        u'The width in points (1/72 of an inch) of the marker.'
##        #return Width
##
##    def Draw(self, context, transfo, envelope):
##        u'Draws the representation marker.'
##        #return 
##
##    @property
##    def Height(self):
##        u'The height in points (1/72 of an inch) of the marker.'
##        #return Height
##
##    @property
##    def Outline(self, Type):
##        u'The outline of the marker, returned as a polygon.'
##        #return Outline
##
##    @property
##    def Size(self):
##        u'The size in points (1/72 of an inch) of the marker.'
##        #return Size
##

class BarChartSymbol(CoClass):
    u'Defines a bar chart symbol.'
    _reg_clsid_ = GUID('{5031736A-BD70-11D3-9F79-00C04F6BC709}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
BarChartSymbol._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ISymbolArray, IChartSymbol, IBarChartSymbol, I3DChartSymbol, IMarkerSymbol, ISymbol, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, IMarkerBackgroundSupport]

class esriGDICommentEndFeatureAttribute(Structure):
    _recordinfo_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2, 0L, '{DE5529BB-C609-4118-90E3-EBBC1E177071}')
esriGDICommentEndFeatureAttribute._fields_ = [
    ('dSignature', c_ulong),
    ('nVersion', c_ulong),
]
assert sizeof(esriGDICommentEndFeatureAttribute) == 8, sizeof(esriGDICommentEndFeatureAttribute)
assert alignment(esriGDICommentEndFeatureAttribute) == 4, alignment(esriGDICommentEndFeatureAttribute)
class MoveTextFeedback(CoClass):
    u'Move Text Display Feedback Object.'
    _reg_clsid_ = GUID('{B8F39F30-867D-4CA7-8D26-1CEEAF530601}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
MoveTextFeedback._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMoveTextFeedback]

class CieLabConversion(CoClass):
    u'Use this class to convert colers from and to the device independent CIELab color space using the monitor settings.'
    _reg_clsid_ = GUID('{137E39DC-3E98-11D2-AAF7-00C04FA334B3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class ICieLabConversion(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the CIE Lab conversion.'
    _iid_ = GUID('{137E39DB-3E98-11D2-AAF7-00C04FA334B3}')
    _idlflags_ = ['oleautomation']
CieLabConversion._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ICieLabConversion]

IModifySegmentFeedback._methods_ = [
    COMMETHOD([helpstring(u'Start the modify segment feedback.')], HRESULT, 'Start',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISegment), 'segment' ),
              ( [], VARIANT_BOOL, 'atFrom' ),
              ( [], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
    COMMETHOD([helpstring(u'Stop the modify segment feedback.')], HRESULT, 'Stop',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISegment)), 'segment' )),
    COMMETHOD([helpstring(u'Abort the modify segment feedback.')], HRESULT, 'Abort'),
]
################################################################
## code template for IModifySegmentFeedback implementation
##class IModifySegmentFeedback_Impl(object):
##    def Start(self, segment, atFrom, Point):
##        u'Start the modify segment feedback.'
##        #return 
##
##    def Abort(self):
##        u'Abort the modify segment feedback.'
##        #return 
##
##    def Stop(self, Point):
##        u'Stop the modify segment feedback.'
##        #return segment
##

ILineDecoration._methods_ = [
    COMMETHOD([helpstring(u'Adds an element.')], HRESULT, 'AddElement',
              ( ['in'], POINTER(ILineDecorationElement), 'lineDecorationElement' )),
    COMMETHOD([helpstring(u'Deletes the element at the given index.')], HRESULT, 'DeleteElement',
              ( ['in'], c_int, 'index' )),
    COMMETHOD([helpstring(u'Moves a line decoration element to the given index.')], HRESULT, 'MoveElement',
              ( ['in'], POINTER(ILineDecorationElement), 'Element' ),
              ( ['in'], c_int, 'toIndex' )),
    COMMETHOD([helpstring(u'Clears all line decoration elements.')], HRESULT, 'ClearElements'),
    COMMETHOD(['propget', helpstring(u'The element at the given position.')], HRESULT, 'Element',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(ILineDecorationElement)), 'lineDecorationElement' )),
    COMMETHOD(['propget', helpstring(u'The number of line decoration elements.')], HRESULT, 'ElementCount',
              ( ['retval', 'out'], POINTER(c_int), 'lineDecorationElementCount' )),
    COMMETHOD([helpstring(u'Queries for the boundary of the given line geometry.')], HRESULT, 'QueryBoundary',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDC' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ITransformation), 'transform' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'LineGeometry' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPolygon), 'boundary' )),
    COMMETHOD([helpstring(u'Draws the given line geometry.')], HRESULT, 'Draw',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDC' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ITransformation), 'transform' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'LineGeometry' )),
]
################################################################
## code template for ILineDecoration implementation
##class ILineDecoration_Impl(object):
##    def ClearElements(self):
##        u'Clears all line decoration elements.'
##        #return 
##
##    def Draw(self, hDC, transform, LineGeometry):
##        u'Draws the given line geometry.'
##        #return 
##
##    def QueryBoundary(self, hDC, transform, LineGeometry, boundary):
##        u'Queries for the boundary of the given line geometry.'
##        #return 
##
##    @property
##    def Element(self, index):
##        u'The element at the given position.'
##        #return lineDecorationElement
##
##    @property
##    def ElementCount(self):
##        u'The number of line decoration elements.'
##        #return lineDecorationElementCount
##
##    def DeleteElement(self, index):
##        u'Deletes the element at the given index.'
##        #return 
##
##    def AddElement(self, lineDecorationElement):
##        u'Adds an element.'
##        #return 
##
##    def MoveElement(self, Element, toIndex):
##        u'Moves a line decoration element to the given index.'
##        #return 
##

IDisplayTransformationAdmin._methods_ = [
    COMMETHOD(['propput', helpstring(u'The scale without any recalculation.')], HRESULT, 'ScaleRatioNoRecalc',
              ( ['in'], c_double, 'rhs' )),
]
################################################################
## code template for IDisplayTransformationAdmin implementation
##class IDisplayTransformationAdmin_Impl(object):
##    def _set(self, rhs):
##        u'The scale without any recalculation.'
##    ScaleRatioNoRecalc = property(fset = _set, doc = _set.__doc__)
##

INewEllipseFeedback._methods_ = [
    COMMETHOD([helpstring(u'Begins a normal feedback at the given point.')], HRESULT, 'Start',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
    COMMETHOD([helpstring(u'Set the location of the second location.')], HRESULT, 'SetPoint',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
    COMMETHOD([helpstring(u'Stops the feedback and returns the shape.')], HRESULT, 'Stop',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry)), 'ellipse' )),
    COMMETHOD(['propget', helpstring(u'The major radius of the current ellipse being constructed.')], HRESULT, 'MajorRadius',
              ( ['retval', 'out'], POINTER(c_double), 'MajorRadius' )),
    COMMETHOD(['propput', helpstring(u'The major radius of the current ellipse being constructed.')], HRESULT, 'MajorRadius',
              ( ['in'], c_double, 'MajorRadius' )),
    COMMETHOD(['propget', helpstring(u'The minor radius of the current ellipse being constructed.')], HRESULT, 'MinorRadius',
              ( ['retval', 'out'], POINTER(c_double), 'MinorRadius' )),
    COMMETHOD(['propput', helpstring(u'The minor radius of the current ellipse being constructed.')], HRESULT, 'MinorRadius',
              ( ['in'], c_double, 'MinorRadius' )),
    COMMETHOD(['propget', helpstring(u'The angle of the current ellipse being constructed.')], HRESULT, 'Angle',
              ( ['retval', 'out'], POINTER(c_double), 'Angle' )),
    COMMETHOD(['propput', helpstring(u'The angle of the current ellipse being constructed.')], HRESULT, 'Angle',
              ( ['in'], c_double, 'Angle' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the first point indicates the center.')], HRESULT, 'StartCenter',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'StartCenter' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether the first point indicates the center.')], HRESULT, 'StartCenter',
              ( ['in'], VARIANT_BOOL, 'StartCenter' )),
    COMMETHOD(['propget', helpstring(u'The constraint on this rubberbander.')], HRESULT, 'Constraint',
              ( ['retval', 'out'], POINTER(esriEnvelopeConstraints), 'constrain' )),
    COMMETHOD(['propput', helpstring(u'The constraint on this rubberbander.')], HRESULT, 'Constraint',
              ( ['in'], esriEnvelopeConstraints, 'constrain' )),
    COMMETHOD(['propget', helpstring(u'The aspect ratio for the custom constraint type.')], HRESULT, 'AspectRatio',
              ( ['retval', 'out'], POINTER(c_double), 'AspectRatio' )),
    COMMETHOD(['propput', helpstring(u'The aspect ratio for the custom constraint type.')], HRESULT, 'AspectRatio',
              ( ['in'], c_double, 'AspectRatio' )),
]
################################################################
## code template for INewEllipseFeedback implementation
##class INewEllipseFeedback_Impl(object):
##    def _get(self):
##        u'The angle of the current ellipse being constructed.'
##        #return Angle
##    def _set(self, Angle):
##        u'The angle of the current ellipse being constructed.'
##    Angle = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The constraint on this rubberbander.'
##        #return constrain
##    def _set(self, constrain):
##        u'The constraint on this rubberbander.'
##    Constraint = property(_get, _set, doc = _set.__doc__)
##
##    def SetPoint(self, Point):
##        u'Set the location of the second location.'
##        #return 
##
##    def Stop(self, Point):
##        u'Stops the feedback and returns the shape.'
##        #return ellipse
##
##    def Start(self, Point):
##        u'Begins a normal feedback at the given point.'
##        #return 
##
##    def _get(self):
##        u'The major radius of the current ellipse being constructed.'
##        #return MajorRadius
##    def _set(self, MajorRadius):
##        u'The major radius of the current ellipse being constructed.'
##    MajorRadius = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether the first point indicates the center.'
##        #return StartCenter
##    def _set(self, StartCenter):
##        u'Indicates whether the first point indicates the center.'
##    StartCenter = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The aspect ratio for the custom constraint type.'
##        #return AspectRatio
##    def _set(self, AspectRatio):
##        u'The aspect ratio for the custom constraint type.'
##    AspectRatio = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The minor radius of the current ellipse being constructed.'
##        #return MinorRadius
##    def _set(self, MinorRadius):
##        u'The minor radius of the current ellipse being constructed.'
##    MinorRadius = property(_get, _set, doc = _set.__doc__)
##

IEnumColors._methods_ = [
    COMMETHOD([helpstring(u'Returns the next color.')], HRESULT, 'Next',
              ( ['retval', 'out'], POINTER(POINTER(IColor)), 'nextColor' )),
    COMMETHOD([helpstring(u'Resets the enumerator to the beginning.')], HRESULT, 'Reset'),
]
################################################################
## code template for IEnumColors implementation
##class IEnumColors_Impl(object):
##    def Reset(self):
##        u'Resets the enumerator to the beginning.'
##        #return 
##
##    def Next(self):
##        u'Returns the next color.'
##        #return nextColor
##

class SimpleFillSymbol(CoClass):
    u'A fill symbol comprised from a predefined set of styles.'
    _reg_clsid_ = GUID('{7914E603-C892-11D0-8BB6-080009EE4E41}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
SimpleFillSymbol._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ISimpleFillSymbol, IMapLevel, ISymbol, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySupport, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, IDisplayName, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize]

IBold._methods_ = [
]
################################################################
## code template for IBold implementation
##class IBold_Impl(object):

class PieChartSymbol(CoClass):
    u'Defines a pie chart symbol.'
    _reg_clsid_ = GUID('{50317368-BD70-11D3-9F79-00C04F6BC709}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
PieChartSymbol._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ISymbolArray, IChartSymbol, IPieChartSymbol, I3DChartSymbol, IMarkerSymbol, ISymbol, IMarkerBackgroundSupport, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone]

class MultiLayerFillSymbol(CoClass):
    u'A fill symbol that contains one or more layers.'
    _reg_clsid_ = GUID('{7914E604-C892-11D0-8BB6-080009EE4E41}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
MultiLayerFillSymbol._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMultiLayerFillSymbol, IMapLevel, ISymbol, ILayerVisible, ILayerColorLock, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySupport, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, ILayerTags]

IUnderline._methods_ = [
]
################################################################
## code template for IUnderline implementation
##class IUnderline_Impl(object):

class IDynamicSymbolProperties2(IDynamicSymbolProperties):
    _case_insensitive_ = True
    u'Provides access to dynamic symbol properties.'
    _iid_ = GUID('{B66F411F-0244-4578-803B-4DA18AEEBAAB}')
    _idlflags_ = ['oleautomation']
IDynamicSymbolProperties2._methods_ = [
    COMMETHOD([helpstring(u'Offsets the dynamic symbol.')], HRESULT, 'GetOffset',
              ( ['in'], esriDynamicSymbolType, 'dynamicSymbolType' ),
              ( ['in', 'out'], POINTER(c_float), 'OffsetX' ),
              ( ['in', 'out'], POINTER(c_float), 'OffsetY' )),
    COMMETHOD([helpstring(u'Offsets the dynamic symbol.')], HRESULT, 'SetOffset',
              ( ['in'], esriDynamicSymbolType, 'dynamicSymbolType' ),
              ( ['in'], c_float, 'OffsetX' ),
              ( ['in'], c_float, 'OffsetY' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the specified dynamic symbol will conform to map reference scale.')], HRESULT, 'UseReferenceScale',
              ( ['in'], esriDynamicSymbolType, 'dynamicSymbolType' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'UseReferenceScale' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether the specified dynamic symbol will conform to map reference scale.')], HRESULT, 'UseReferenceScale',
              ( ['in'], esriDynamicSymbolType, 'dynamicSymbolType' ),
              ( ['in'], VARIANT_BOOL, 'UseReferenceScale' )),
    COMMETHOD([helpstring(u'Indicates the text box margins for the dynamic text symbol.')], HRESULT, 'GetTextBoxMargins',
              ( ['in', 'out'], POINTER(c_float), 'Left' ),
              ( ['in', 'out'], POINTER(c_float), 'Top' ),
              ( ['in', 'out'], POINTER(c_float), 'Right' ),
              ( ['in', 'out'], POINTER(c_float), 'Bottom' )),
    COMMETHOD([helpstring(u'Indicates the text box margins for the dynamic text symbol.')], HRESULT, 'SetTextBoxMargins',
              ( ['in'], c_float, 'Left' ),
              ( ['in'], c_float, 'Top' ),
              ( ['in'], c_float, 'Right' ),
              ( ['in'], c_float, 'Bottom' )),
    COMMETHOD(['propget', helpstring(u'Indicates the text box horizontal alignment for the dynamic text symbol.')], HRESULT, 'TextBoxHorizontalAlignment',
              ( ['retval', 'out'], POINTER(esriTextHorizontalAlignment), 'TextBoxHorizontalAlignment' )),
    COMMETHOD(['propput', helpstring(u'Indicates the text box horizontal alignment for the dynamic text symbol.')], HRESULT, 'TextBoxHorizontalAlignment',
              ( ['in'], esriTextHorizontalAlignment, 'TextBoxHorizontalAlignment' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether to use the dynamic fill symbol when drawing the text.')], HRESULT, 'TextBoxUseDynamicFillSymbol',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'use' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether to use the dynamic fill symbol when drawing the text.')], HRESULT, 'TextBoxUseDynamicFillSymbol',
              ( ['in'], VARIANT_BOOL, 'use' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether to use the dynamic line symbol when drawing the text.')], HRESULT, 'TextBoxUseDynamicLineSymbol',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'use' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether to use the dynamic line symbol when drawing the text.')], HRESULT, 'TextBoxUseDynamicLineSymbol',
              ( ['in'], VARIANT_BOOL, 'use' )),
    COMMETHOD(['propget', helpstring(u'Indicates the text leading for the dynamic text symbol.')], HRESULT, 'TextLeading',
              ( ['retval', 'out'], POINTER(c_float), 'Leading' )),
    COMMETHOD(['propput', helpstring(u'Indicates the text leading for the dynamic text symbol.')], HRESULT, 'TextLeading',
              ( ['in'], c_float, 'Leading' )),
    COMMETHOD(['propget', helpstring(u'Indicates an additional space that is added to each character beyond what is defined by its character box in the TextGlyph.')], HRESULT, 'TextCharacterSpacing',
              ( ['retval', 'out'], POINTER(c_float), 'CharacterSpacing' )),
    COMMETHOD(['propput', helpstring(u'Indicates an additional space that is added to each character beyond what is defined by its character box in the TextGlyph.')], HRESULT, 'TextCharacterSpacing',
              ( ['in'], c_float, 'CharacterSpacing' )),
    COMMETHOD(['propget', helpstring(u'Indicates an additional space that is added between words of the text string.')], HRESULT, 'TextWordSpacing',
              ( ['retval', 'out'], POINTER(c_float), 'WordSpacing' )),
    COMMETHOD(['propput', helpstring(u'Indicates an additional space that is added between words of the text string.')], HRESULT, 'TextWordSpacing',
              ( ['in'], c_float, 'WordSpacing' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the text is drawn from right to left for the dynamic text symbol.')], HRESULT, 'TextRightToLeft',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'RightToLeft' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether the text is drawn from right to left for the dynamic text symbol.')], HRESULT, 'TextRightToLeft',
              ( ['in'], VARIANT_BOOL, 'RightToLeft' )),
    COMMETHOD([helpstring(u'The text size in pixel screen coordinates.')], HRESULT, 'GetTextSize',
              ( ['in'], BSTR, 'Text' ),
              ( ['in', 'out'], POINTER(c_float), 'sizeX' ),
              ( ['in', 'out'], POINTER(c_float), 'sizeY' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether the line pattern is continued or restarted, for multi parts lines drawing.')], HRESULT, 'LineContinuePattern',
              ( ['in'], VARIANT_BOOL, 'continuePattern' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the line pattern is continued or restarted, for multi parts lines drawing.')], HRESULT, 'LineContinuePattern',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'continuePattern' )),
]
################################################################
## code template for IDynamicSymbolProperties2 implementation
##class IDynamicSymbolProperties2_Impl(object):
##    def GetTextBoxMargins(self):
##        u'Indicates the text box margins for the dynamic text symbol.'
##        #return Left, Top, Right, Bottom
##
##    def _get(self):
##        u'Indicates whether the text is drawn from right to left for the dynamic text symbol.'
##        #return RightToLeft
##    def _set(self, RightToLeft):
##        u'Indicates whether the text is drawn from right to left for the dynamic text symbol.'
##    TextRightToLeft = property(_get, _set, doc = _set.__doc__)
##
##    def GetOffset(self, dynamicSymbolType):
##        u'Offsets the dynamic symbol.'
##        #return OffsetX, OffsetY
##
##    def _get(self):
##        u'Indicates whether to use the dynamic line symbol when drawing the text.'
##        #return use
##    def _set(self, use):
##        u'Indicates whether to use the dynamic line symbol when drawing the text.'
##    TextBoxUseDynamicLineSymbol = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates the text leading for the dynamic text symbol.'
##        #return Leading
##    def _set(self, Leading):
##        u'Indicates the text leading for the dynamic text symbol.'
##    TextLeading = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether the line pattern is continued or restarted, for multi parts lines drawing.'
##        #return continuePattern
##    def _set(self, continuePattern):
##        u'Indicates whether the line pattern is continued or restarted, for multi parts lines drawing.'
##    LineContinuePattern = property(_get, _set, doc = _set.__doc__)
##
##    def GetTextSize(self, Text):
##        u'The text size in pixel screen coordinates.'
##        #return sizeX, sizeY
##
##    def _get(self, dynamicSymbolType):
##        u'Indicates whether the specified dynamic symbol will conform to map reference scale.'
##        #return UseReferenceScale
##    def _set(self, dynamicSymbolType, UseReferenceScale):
##        u'Indicates whether the specified dynamic symbol will conform to map reference scale.'
##    UseReferenceScale = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates the text box horizontal alignment for the dynamic text symbol.'
##        #return TextBoxHorizontalAlignment
##    def _set(self, TextBoxHorizontalAlignment):
##        u'Indicates the text box horizontal alignment for the dynamic text symbol.'
##    TextBoxHorizontalAlignment = property(_get, _set, doc = _set.__doc__)
##
##    def SetOffset(self, dynamicSymbolType, OffsetX, OffsetY):
##        u'Offsets the dynamic symbol.'
##        #return 
##
##    def SetTextBoxMargins(self, Left, Top, Right, Bottom):
##        u'Indicates the text box margins for the dynamic text symbol.'
##        #return 
##
##    def _get(self):
##        u'Indicates an additional space that is added between words of the text string.'
##        #return WordSpacing
##    def _set(self, WordSpacing):
##        u'Indicates an additional space that is added between words of the text string.'
##    TextWordSpacing = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether to use the dynamic fill symbol when drawing the text.'
##        #return use
##    def _set(self, use):
##        u'Indicates whether to use the dynamic fill symbol when drawing the text.'
##    TextBoxUseDynamicFillSymbol = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates an additional space that is added to each character beyond what is defined by its character box in the TextGlyph.'
##        #return CharacterSpacing
##    def _set(self, CharacterSpacing):
##        u'Indicates an additional space that is added to each character beyond what is defined by its character box in the TextGlyph.'
##    TextCharacterSpacing = property(_get, _set, doc = _set.__doc__)
##

INewTextBezierCurveFeedback._methods_ = [
    COMMETHOD([helpstring(u'Begins a normal feedback at the given point.')], HRESULT, 'Start',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' ),
              ( ['in'], c_double, 'ReferenceScale' )),
    COMMETHOD([helpstring(u'Creates a node at the given point.')], HRESULT, 'AddPoint',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
    COMMETHOD([helpstring(u'Stops the feedback and returns the shape.')], HRESULT, 'Stop',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPolyline)), 'polyline' )),
    COMMETHOD(['propget', helpstring(u'The constraint on this rubberbander.')], HRESULT, 'Constraint',
              ( ['retval', 'out'], POINTER(esriLineConstraints), 'constrain' )),
    COMMETHOD(['propput', helpstring(u'The constraint on this rubberbander.')], HRESULT, 'Constraint',
              ( ['in'], esriLineConstraints, 'constrain' )),
]
################################################################
## code template for INewTextBezierCurveFeedback implementation
##class INewTextBezierCurveFeedback_Impl(object):
##    def Start(self, Point, ReferenceScale):
##        u'Begins a normal feedback at the given point.'
##        #return 
##
##    def _get(self):
##        u'The constraint on this rubberbander.'
##        #return constrain
##    def _set(self, constrain):
##        u'The constraint on this rubberbander.'
##    Constraint = property(_get, _set, doc = _set.__doc__)
##
##    def Stop(self):
##        u'Stops the feedback and returns the shape.'
##        #return polyline
##
##    def AddPoint(self, Point):
##        u'Creates a node at the given point.'
##        #return 
##

IFontColor._methods_ = [
    COMMETHOD(['propget', helpstring(u'Font color.')], HRESULT, 'Color',
              ( ['retval', 'out'], POINTER(POINTER(IColor)), 'Color' )),
    COMMETHOD(['propput', helpstring(u'Font color.')], HRESULT, 'Color',
              ( ['in'], POINTER(IColor), 'Color' )),
]
################################################################
## code template for IFontColor implementation
##class IFontColor_Impl(object):
##    def _get(self):
##        u'Font color.'
##        #return Color
##    def _set(self, Color):
##        u'Font color.'
##    Color = property(_get, _set, doc = _set.__doc__)
##

class StackedChartSymbol(CoClass):
    u'Defines a stacked chart symbol.'
    _reg_clsid_ = GUID('{50317369-BD70-11D3-9F79-00C04F6BC709}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
class IStackedChartSymbol(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to stacked chart symbol properties.'
    _iid_ = GUID('{50317366-BD70-11D3-9F79-00C04F6BC709}')
    _idlflags_ = ['oleautomation']
StackedChartSymbol._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ISymbolArray, IChartSymbol, IStackedChartSymbol, I3DChartSymbol, IMarkerSymbol, ISymbol, IMarkerBackgroundSupport, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone]

class GeometricEffectRotate(CoClass):
    u'Applies a rotate transformation to a geometry.'
    _reg_clsid_ = GUID('{ABA1F3CF-3207-4C89-8CE3-7A2A8FD8D221}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
GeometricEffectRotate._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGeometricEffect, IGraphicAttributes, IGraphicAttributes2, IEditInteraction, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

ILineDecorationElement._methods_ = [
    COMMETHOD([helpstring(u'Adds a position.')], HRESULT, 'AddPosition',
              ( ['in'], c_double, 'elementPosition' )),
    COMMETHOD([helpstring(u'Deletes a position.')], HRESULT, 'DeletePosition',
              ( ['in'], c_int, 'index' )),
    COMMETHOD([helpstring(u'Clears all positions.')], HRESULT, 'ClearPositions'),
    COMMETHOD(['propget', helpstring(u'Indicates if positions represent percentage or absolute distance along the line.')], HRESULT, 'PositionAsRatio',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'asRatio' )),
    COMMETHOD(['propput', helpstring(u'Indicates if positions represent percentage or absolute distance along the line.')], HRESULT, 'PositionAsRatio',
              ( ['in'], VARIANT_BOOL, 'asRatio' )),
    COMMETHOD(['propget', helpstring(u'The element position at the given index.')], HRESULT, 'Position',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(c_double), 'elementPos' )),
    COMMETHOD(['propget', helpstring(u'The number of positions.')], HRESULT, 'PositionCount',
              ( ['retval', 'out'], POINTER(c_int), 'PositionCount' )),
    COMMETHOD([helpstring(u'Queries for the boundary of a given line geometry.')], HRESULT, 'QueryBoundary',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDC' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ITransformation), 'transform' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'LineGeometry' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPolygon), 'boundary' )),
    COMMETHOD([helpstring(u'Draws the given line geometry.')], HRESULT, 'Draw',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDC' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ITransformation), 'transform' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'LineGeometry' )),
]
################################################################
## code template for ILineDecorationElement implementation
##class ILineDecorationElement_Impl(object):
##    def _get(self):
##        u'Indicates if positions represent percentage or absolute distance along the line.'
##        #return asRatio
##    def _set(self, asRatio):
##        u'Indicates if positions represent percentage or absolute distance along the line.'
##    PositionAsRatio = property(_get, _set, doc = _set.__doc__)
##
##    def Draw(self, hDC, transform, LineGeometry):
##        u'Draws the given line geometry.'
##        #return 
##
##    def AddPosition(self, elementPosition):
##        u'Adds a position.'
##        #return 
##
##    def DeletePosition(self, index):
##        u'Deletes a position.'
##        #return 
##
##    def ClearPositions(self):
##        u'Clears all positions.'
##        #return 
##
##    def QueryBoundary(self, hDC, transform, LineGeometry, boundary):
##        u'Queries for the boundary of a given line geometry.'
##        #return 
##
##    @property
##    def Position(self, index):
##        u'The element position at the given index.'
##        #return elementPos
##
##    @property
##    def PositionCount(self):
##        u'The number of positions.'
##        #return PositionCount
##

IMovePointFeedback2._methods_ = [
    COMMETHOD([helpstring(u'Specify a vertex to move.')], HRESULT, 'SelectVertex',
              ( ['in'], c_int, 'vertex' )),
    COMMETHOD([helpstring(u'Start the feedback.')], HRESULT, 'Start',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'Geometry' ),
              ( [], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
    COMMETHOD([helpstring(u'Stop the feedback.')], HRESULT, 'Stop',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry)), 'Geometry' )),
    COMMETHOD([helpstring(u'Abort the feedback.')], HRESULT, 'Abort'),
]
################################################################
## code template for IMovePointFeedback2 implementation
##class IMovePointFeedback2_Impl(object):
##    def Start(self, Geometry, Point):
##        u'Start the feedback.'
##        #return 
##
##    def Abort(self):
##        u'Abort the feedback.'
##        #return 
##
##    def Stop(self, Point):
##        u'Stop the feedback.'
##        #return Geometry
##
##    def SelectVertex(self, vertex):
##        u'Specify a vertex to move.'
##        #return 
##

class IDynamicDisplay2(IDynamicDisplay):
    _case_insensitive_ = True
    u'Provides access to Dynamic Display.'
    _iid_ = GUID('{8A658E89-5353-40DD-B612-BC4688D94830}')
    _idlflags_ = []
IDynamicDisplay2._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates whether display supports static drawing such as lables and graphics.')], HRESULT, 'SupportStaticDrawing',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'staticDrawing' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether display supports static drawing such as lables and graphics.')], HRESULT, 'SupportStaticDrawing',
              ( ['in'], VARIANT_BOOL, 'staticDrawing' )),
    COMMETHOD([helpstring(u'Locate named objects in the display. Provides a mechanism for hit-test, selection etc.')], HRESULT, 'Locate',
              ( ['in'], c_int, 'xView' ),
              ( ['in'], c_int, 'yView' ),
              ( ['in'], esriDynamicSelectionMode, 'selectionMode' ),
              ( ['in'], POINTER(IUnknown), 'data' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IArray)), 'hits' )),
    COMMETHOD(['propget', helpstring(u'Allocate a unique index to be used with dynamic selection.')], HRESULT, 'SelectionIdentifier',
              ( ['retval', 'out'], POINTER(c_ulong), 'identifier' )),
    COMMETHOD([helpstring(u'Add a dynamic drawing to the display at the specified Z order.')], HRESULT, 'InsertDynamicDrawing',
              ( [], POINTER(IDynamicDrawing), 'pDynamicDrawing' ),
              ( [], c_int, 'lPosition' )),
    COMMETHOD([helpstring(u'Delete a dynamic drawing.')], HRESULT, 'DeleteDynamicDrawing',
              ( [], POINTER(IDynamicDrawing), 'pDynamicDrawing' )),
]
################################################################
## code template for IDynamicDisplay2 implementation
##class IDynamicDisplay2_Impl(object):
##    def Locate(self, xView, yView, selectionMode, data):
##        u'Locate named objects in the display. Provides a mechanism for hit-test, selection etc.'
##        #return hits
##
##    def InsertDynamicDrawing(self, pDynamicDrawing, lPosition):
##        u'Add a dynamic drawing to the display at the specified Z order.'
##        #return 
##
##    def _get(self):
##        u'Indicates whether display supports static drawing such as lables and graphics.'
##        #return staticDrawing
##    def _set(self, staticDrawing):
##        u'Indicates whether display supports static drawing such as lables and graphics.'
##    SupportStaticDrawing = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def SelectionIdentifier(self):
##        u'Allocate a unique index to be used with dynamic selection.'
##        #return identifier
##
##    def DeleteDynamicDrawing(self, pDynamicDrawing):
##        u'Delete a dynamic drawing.'
##        #return 
##

IRandomColorRamp._methods_ = [
    COMMETHOD(['propput', helpstring(u'The seed of the random number generator.')], HRESULT, 'Seed',
              ( ['in'], c_int, 'Seed' )),
    COMMETHOD(['propget', helpstring(u'The seed of the random number generator.')], HRESULT, 'Seed',
              ( ['retval', 'out'], POINTER(c_int), 'Seed' )),
    COMMETHOD(['propput', helpstring(u'Indicates if a seed is used when the ramp is generated.  Set this property to True without changing the Seed to generate identical color ramps in succession.')], HRESULT, 'UseSeed',
              ( ['in'], VARIANT_BOOL, 'UseSeed' )),
    COMMETHOD(['propget', helpstring(u'Indicates if a seed is used when the ramp is generated.  Set this property to True without changing the Seed to generate identical color ramps in succession.')], HRESULT, 'UseSeed',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'UseSeed' )),
    COMMETHOD(['propput', helpstring(u'The minimum value (0-100).')], HRESULT, 'MinValue',
              ( ['in'], c_int, 'MinValue' )),
    COMMETHOD(['propget', helpstring(u'The minimum value (0-100).')], HRESULT, 'MinValue',
              ( ['retval', 'out'], POINTER(c_int), 'MinValue' )),
    COMMETHOD(['propput', helpstring(u'The maximum value (0-100).')], HRESULT, 'MaxValue',
              ( ['in'], c_int, 'MaxValue' )),
    COMMETHOD(['propget', helpstring(u'The maximum value (0-100).')], HRESULT, 'MaxValue',
              ( ['retval', 'out'], POINTER(c_int), 'MaxValue' )),
    COMMETHOD(['propput', helpstring(u'The minimum saturation (0-100).')], HRESULT, 'MinSaturation',
              ( ['in'], c_int, 'MinSaturation' )),
    COMMETHOD(['propget', helpstring(u'The minimum saturation (0-100).')], HRESULT, 'MinSaturation',
              ( ['retval', 'out'], POINTER(c_int), 'MinSaturation' )),
    COMMETHOD(['propput', helpstring(u'The maximum saturation (0-100).')], HRESULT, 'MaxSaturation',
              ( ['in'], c_int, 'MaxSaturation' )),
    COMMETHOD(['propget', helpstring(u'The maximum saturation (0-100).')], HRESULT, 'MaxSaturation',
              ( ['retval', 'out'], POINTER(c_int), 'MaxSaturation' )),
    COMMETHOD(['propput', helpstring(u'The start hue (0-360).')], HRESULT, 'StartHue',
              ( ['in'], c_int, 'StartHue' )),
    COMMETHOD(['propget', helpstring(u'The start hue (0-360).')], HRESULT, 'StartHue',
              ( ['retval', 'out'], POINTER(c_int), 'StartHue' )),
    COMMETHOD(['propput', helpstring(u'The end hue (0-360).')], HRESULT, 'EndHue',
              ( ['in'], c_int, 'EndHue' )),
    COMMETHOD(['propget', helpstring(u'The end hue (0-360).')], HRESULT, 'EndHue',
              ( ['retval', 'out'], POINTER(c_int), 'EndHue' )),
]
################################################################
## code template for IRandomColorRamp implementation
##class IRandomColorRamp_Impl(object):
##    def _get(self):
##        u'The end hue (0-360).'
##        #return EndHue
##    def _set(self, EndHue):
##        u'The end hue (0-360).'
##    EndHue = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if a seed is used when the ramp is generated.  Set this property to True without changing the Seed to generate identical color ramps in succession.'
##        #return UseSeed
##    def _set(self, UseSeed):
##        u'Indicates if a seed is used when the ramp is generated.  Set this property to True without changing the Seed to generate identical color ramps in succession.'
##    UseSeed = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The maximum value (0-100).'
##        #return MaxValue
##    def _set(self, MaxValue):
##        u'The maximum value (0-100).'
##    MaxValue = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The seed of the random number generator.'
##        #return Seed
##    def _set(self, Seed):
##        u'The seed of the random number generator.'
##    Seed = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The start hue (0-360).'
##        #return StartHue
##    def _set(self, StartHue):
##        u'The start hue (0-360).'
##    StartHue = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The maximum saturation (0-100).'
##        #return MaxSaturation
##    def _set(self, MaxSaturation):
##        u'The maximum saturation (0-100).'
##    MaxSaturation = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The minimum saturation (0-100).'
##        #return MinSaturation
##    def _set(self, MinSaturation):
##        u'The minimum saturation (0-100).'
##    MinSaturation = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The minimum value (0-100).'
##        #return MinValue
##    def _set(self, MinValue):
##        u'The minimum value (0-100).'
##    MinValue = property(_get, _set, doc = _set.__doc__)
##

class GeometricEffectDonut(CoClass):
    u'Inserts a hole into a polygon.'
    _reg_clsid_ = GUID('{A2426E37-FB61-4339-83F5-70D3F886EC3A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
GeometricEffectDonut._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGeometricEffect, IGraphicAttributes, IGraphicAttributes2, IEditInteraction, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

ISymbolRotation._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if the symbol rotates with the display.')], HRESULT, 'RotateWithTransform',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the symbol rotates with the display.')], HRESULT, 'RotateWithTransform',
              ( ['in'], VARIANT_BOOL, 'flag' )),
]
################################################################
## code template for ISymbolRotation implementation
##class ISymbolRotation_Impl(object):
##    def _get(self):
##        u'Indicates if the symbol rotates with the display.'
##        #return flag
##    def _set(self, flag):
##        u'Indicates if the symbol rotates with the display.'
##    RotateWithTransform = property(_get, _set, doc = _set.__doc__)
##

IItalic._methods_ = [
]
################################################################
## code template for IItalic implementation
##class IItalic_Impl(object):

ISymbolIdentifier._methods_ = [
    COMMETHOD(['propget', helpstring(u'The symbol associated with the symbolID.')], HRESULT, 'Symbol',
              ( ['retval', 'out'], POINTER(POINTER(ISymbol)), 'Symbol' )),
    COMMETHOD(['propputref', helpstring(u'The symbol associated with the symbolID.')], HRESULT, 'Symbol',
              ( ['in'], POINTER(ISymbol), 'Symbol' )),
    COMMETHOD(['propget', helpstring(u'The symbolID associated with the symbol.')], HRESULT, 'ID',
              ( ['retval', 'out'], POINTER(c_int), 'symbolID' )),
    COMMETHOD(['propput', helpstring(u'The symbolID associated with the symbol.')], HRESULT, 'ID',
              ( ['in'], c_int, 'symbolID' )),
]
################################################################
## code template for ISymbolIdentifier implementation
##class ISymbolIdentifier_Impl(object):
##    def Symbol(self, Symbol):
##        u'The symbol associated with the symbolID.'
##        #return 
##
##    def _get(self):
##        u'The symbolID associated with the symbol.'
##        #return symbolID
##    def _set(self, symbolID):
##        u'The symbolID associated with the symbol.'
##    ID = property(_get, _set, doc = _set.__doc__)
##


# values for enumeration 'esriRepresentationDrawingError'
REP_E_ATTRIBUTE_DOES_NOT_EXIST = -2147218431
REP_E_GEOMETRY_TYPE_NOT_SUPPORTED = -2147218430
REP_E_NO_MAP_CONTEXT = -2147218429
REP_E_INVALID_ENUM_ATTRIBUTE = -2147218428
REP_E_EMPTY_ENUM_ATTRIBUTE = -2147218427
REP_E_MAP_CONTEXT_NOT_INITIALIZED = -2147218426
REP_E_OUTPUT_CONTEXT_NOT_INITIALIZED = -2147218425
esriRepresentationDrawingError = c_int # enum
class LineFillSymbol(CoClass):
    u'A fill symbol comprised of any of the supported line symbols.'
    _reg_clsid_ = GUID('{7914E606-C892-11D0-8BB6-080009EE4E41}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
LineFillSymbol._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ILineFillSymbol, IMapLevel, ISymbol, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySupport, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, IDisplayName]

IMoveTextAlongShapeFeedback._methods_ = [
    COMMETHOD([helpstring(u'Specify the shape to follow.')], HRESULT, 'FollowShape',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'featureGeometry' ),
              ( ['in'], c_double, 'ReferenceScale' )),
    COMMETHOD([helpstring(u'Begins a move feedback of the given shape.')], HRESULT, 'StartCurved',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'fromPoint' ),
              ( ['in'], c_double, 'ReferenceScale' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'cursorPoint' ),
              ( ['in'], c_double, 'Offset' ),
              ( ['in'], esriMoveTextConstraints, 'Constraint' ),
              ( ['in'], VARIANT_BOOL, 'flipped' )),
    COMMETHOD([helpstring(u'Begins a move feedback of the given shape.')], HRESULT, 'StartStraight',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'textGeometry' ),
              ( ['in'], c_double, 'labelWidth' ),
              ( ['in'], c_double, 'labelHeight' ),
              ( ['in'], c_double, 'ReferenceScale' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' ),
              ( ['in'], c_double, 'Offset' ),
              ( ['in'], VARIANT_BOOL, 'Parallel' ),
              ( ['in'], esriMoveTextConstraints, 'Constraint' )),
    COMMETHOD([helpstring(u'Stops the feedback and returns the shape.')], HRESULT, 'Stop',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry)), 'baseline' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether to flip the text.')], HRESULT, 'Flip',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Flip' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether to flip the text.')], HRESULT, 'Flip',
              ( ['in'], VARIANT_BOOL, 'Flip' )),
    COMMETHOD(['propget', helpstring(u'Offset the text from the geometry.')], HRESULT, 'Offset',
              ( ['retval', 'out'], POINTER(c_double), 'Offset' )),
    COMMETHOD(['propput', helpstring(u'Offset the text from the geometry.')], HRESULT, 'Offset',
              ( ['in'], c_double, 'Offset' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether to make the text parallel.  Only valid for straight.')], HRESULT, 'Parallel',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Parallel' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether to make the text parallel.  Only valid for straight.')], HRESULT, 'Parallel',
              ( ['in'], VARIANT_BOOL, 'Parallel' )),
    COMMETHOD(['propget', helpstring(u'Constrain the text.')], HRESULT, 'Constraint',
              ( ['retval', 'out'], POINTER(esriMoveTextConstraints), 'Constraint' )),
    COMMETHOD(['propput', helpstring(u'Constrain the text.')], HRESULT, 'Constraint',
              ( ['in'], esriMoveTextConstraints, 'Constraint' )),
]
################################################################
## code template for IMoveTextAlongShapeFeedback implementation
##class IMoveTextAlongShapeFeedback_Impl(object):
##    def FollowShape(self, featureGeometry, ReferenceScale):
##        u'Specify the shape to follow.'
##        #return 
##
##    def _get(self):
##        u'Constrain the text.'
##        #return Constraint
##    def _set(self, Constraint):
##        u'Constrain the text.'
##    Constraint = property(_get, _set, doc = _set.__doc__)
##
##    def Stop(self):
##        u'Stops the feedback and returns the shape.'
##        #return baseline
##
##    def _get(self):
##        u'Indicates whether to flip the text.'
##        #return Flip
##    def _set(self, Flip):
##        u'Indicates whether to flip the text.'
##    Flip = property(_get, _set, doc = _set.__doc__)
##
##    def StartStraight(self, textGeometry, labelWidth, labelHeight, ReferenceScale, Point, Offset, Parallel, Constraint):
##        u'Begins a move feedback of the given shape.'
##        #return 
##
##    def _get(self):
##        u'Offset the text from the geometry.'
##        #return Offset
##    def _set(self, Offset):
##        u'Offset the text from the geometry.'
##    Offset = property(_get, _set, doc = _set.__doc__)
##
##    def StartCurved(self, fromPoint, ReferenceScale, cursorPoint, Offset, Constraint, flipped):
##        u'Begins a move feedback of the given shape.'
##        #return 
##
##    def _get(self):
##        u'Indicates whether to make the text parallel.  Only valid for straight.'
##        #return Parallel
##    def _set(self, Parallel):
##        u'Indicates whether to make the text parallel.  Only valid for straight.'
##    Parallel = property(_get, _set, doc = _set.__doc__)
##

IMoveCurvedTextFeedback._methods_ = [
    COMMETHOD([helpstring(u'Specify the shape to follow.')], HRESULT, 'FollowShape',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'featureGeometry' ),
              ( ['in'], c_double, 'ReferenceScale' )),
    COMMETHOD([helpstring(u'Begins a move feedback of the given shape.')], HRESULT, 'Start',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'fromPoint' ),
              ( ['in'], c_double, 'ReferenceScale' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'cursorPoint' ),
              ( ['in'], c_double, 'Offset' ),
              ( ['in'], esriMoveTextConstraints, 'Constraint' ),
              ( ['in'], VARIANT_BOOL, 'flipped' )),
    COMMETHOD([helpstring(u'Stops the feedback and returns the shape.')], HRESULT, 'Stop',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry)), 'baseline' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether to flip the text.')], HRESULT, 'Flip',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Flip' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether to flip the text.')], HRESULT, 'Flip',
              ( ['in'], VARIANT_BOOL, 'Flip' )),
    COMMETHOD(['propget', helpstring(u'Offset the text from the geometry.')], HRESULT, 'Offset',
              ( ['retval', 'out'], POINTER(c_double), 'Offset' )),
    COMMETHOD(['propput', helpstring(u'Offset the text from the geometry.')], HRESULT, 'Offset',
              ( ['in'], c_double, 'Offset' )),
    COMMETHOD(['propget', helpstring(u'Constrain the text.')], HRESULT, 'Constraint',
              ( ['retval', 'out'], POINTER(esriMoveTextConstraints), 'Constraint' )),
    COMMETHOD(['propput', helpstring(u'Constrain the text.')], HRESULT, 'Constraint',
              ( ['in'], esriMoveTextConstraints, 'Constraint' )),
]
################################################################
## code template for IMoveCurvedTextFeedback implementation
##class IMoveCurvedTextFeedback_Impl(object):
##    def FollowShape(self, featureGeometry, ReferenceScale):
##        u'Specify the shape to follow.'
##        #return 
##
##    def _get(self):
##        u'Constrain the text.'
##        #return Constraint
##    def _set(self, Constraint):
##        u'Constrain the text.'
##    Constraint = property(_get, _set, doc = _set.__doc__)
##
##    def Stop(self):
##        u'Stops the feedback and returns the shape.'
##        #return baseline
##
##    def _get(self):
##        u'Indicates whether to flip the text.'
##        #return Flip
##    def _set(self, Flip):
##        u'Indicates whether to flip the text.'
##    Flip = property(_get, _set, doc = _set.__doc__)
##
##    def Start(self, fromPoint, ReferenceScale, cursorPoint, Offset, Constraint, flipped):
##        u'Begins a move feedback of the given shape.'
##        #return 
##
##    def _get(self):
##        u'Offset the text from the geometry.'
##        #return Offset
##    def _set(self, Offset):
##        u'Offset the text from the geometry.'
##    Offset = property(_get, _set, doc = _set.__doc__)
##

IGraphicAttributeTypeUsingUnits._methods_ = [
    COMMETHOD([helpstring(u'Formats a graphic attribute value according to a given unit before displaying it.')], HRESULT, 'FormatForDisplay',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.esriUnits, 'Units' ),
              ( ['in', 'out'], POINTER(VARIANT), 'val' )),
    COMMETHOD([helpstring(u'Converts a graphic attribute value coming from the UI to points.')], HRESULT, 'FormatFromDisplay',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.esriUnits, 'Units' ),
              ( ['in', 'out'], POINTER(VARIANT), 'val' )),
]
################################################################
## code template for IGraphicAttributeTypeUsingUnits implementation
##class IGraphicAttributeTypeUsingUnits_Impl(object):
##    def FormatFromDisplay(self, Units):
##        u'Converts a graphic attribute value coming from the UI to points.'
##        #return val
##
##    def FormatForDisplay(self, Units):
##        u'Formats a graphic attribute value according to a given unit before displaying it.'
##        #return val
##

class IDynamicCompoundMarker2(IDynamicCompoundMarker):
    _case_insensitive_ = True
    u'Provides access to Dynamic Screen Draw.'
    _iid_ = GUID('{84075C63-F57B-474E-AD81-A07442092F31}')
    _idlflags_ = ['oleautomation']
IDynamicCompoundMarker2._methods_ = [
    COMMETHOD([helpstring(u'Indicates the offset of the text from the marker on each direction.')], HRESULT, 'GetMarkerToTextOffset2',
              ( ['in', 'out'], POINTER(c_float), 'markerToTop' ),
              ( ['in', 'out'], POINTER(c_float), 'markerToBottom' ),
              ( ['in', 'out'], POINTER(c_float), 'markerToLeft' ),
              ( ['in', 'out'], POINTER(c_float), 'markerToRight' )),
    COMMETHOD([helpstring(u'Indicates the offset of the text from the marker on each direction.')], HRESULT, 'SetMarkerToTextOffset2',
              ( ['in'], c_float, 'markerToTop' ),
              ( ['in'], c_float, 'markerToBottom' ),
              ( ['in'], c_float, 'markerToLeft' ),
              ( ['in'], c_float, 'markerToRight' )),
    COMMETHOD([helpstring(u'Indicates the spacing between each two adjacent text boxes.')], HRESULT, 'GetTextSpacing',
              ( ['in', 'out'], POINTER(c_float), 'textSpacingX' ),
              ( ['in', 'out'], POINTER(c_float), 'textSpacingY' )),
    COMMETHOD([helpstring(u'Indicates the spacing between each two adjacent text boxes.')], HRESULT, 'SetTextSpacing',
              ( ['in'], c_float, 'textSpacingX' ),
              ( ['in'], c_float, 'textSpacingY' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the text boxes are to be auto ajdusted.')], HRESULT, 'TextAutoAdjust',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'autoAdjust' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether the text boxes are to be auto ajdusted.')], HRESULT, 'TextAutoAdjust',
              ( ['in'], VARIANT_BOOL, 'autoAdjust' )),
    COMMETHOD([helpstring(u'Draws a marker in a specific point on the map with text matricies around it.')], HRESULT, 'DrawArrayMarker',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' ),
              ( ['in'], POINTER(_midlSAFEARRAY(BSTR)), 'textCenter' ),
              ( ['in'], POINTER(_midlSAFEARRAY(BSTR)), 'textLeft' ),
              ( ['in'], POINTER(_midlSAFEARRAY(BSTR)), 'textRight' ),
              ( ['in'], POINTER(_midlSAFEARRAY(BSTR)), 'textTop' ),
              ( ['in'], POINTER(_midlSAFEARRAY(BSTR)), 'textBottom' )),
    COMMETHOD([helpstring(u'Draws a marker in a specific point on the screen with text matricies around it.')], HRESULT, 'DrawScreenArrayMarker',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' ),
              ( ['in'], POINTER(_midlSAFEARRAY(BSTR)), 'textCenter' ),
              ( ['in'], POINTER(_midlSAFEARRAY(BSTR)), 'textLeft' ),
              ( ['in'], POINTER(_midlSAFEARRAY(BSTR)), 'textRight' ),
              ( ['in'], POINTER(_midlSAFEARRAY(BSTR)), 'textTop' ),
              ( ['in'], POINTER(_midlSAFEARRAY(BSTR)), 'textBottom' )),
]
################################################################
## code template for IDynamicCompoundMarker2 implementation
##class IDynamicCompoundMarker2_Impl(object):
##    def DrawScreenArrayMarker(self, Point, textCenter, textLeft, textRight, textTop, textBottom):
##        u'Draws a marker in a specific point on the screen with text matricies around it.'
##        #return 
##
##    def SetMarkerToTextOffset2(self, markerToTop, markerToBottom, markerToLeft, markerToRight):
##        u'Indicates the offset of the text from the marker on each direction.'
##        #return 
##
##    def SetTextSpacing(self, textSpacingX, textSpacingY):
##        u'Indicates the spacing between each two adjacent text boxes.'
##        #return 
##
##    def GetMarkerToTextOffset2(self):
##        u'Indicates the offset of the text from the marker on each direction.'
##        #return markerToTop, markerToBottom, markerToLeft, markerToRight
##
##    def DrawArrayMarker(self, Point, textCenter, textLeft, textRight, textTop, textBottom):
##        u'Draws a marker in a specific point on the map with text matricies around it.'
##        #return 
##
##    def _get(self):
##        u'Indicates whether the text boxes are to be auto ajdusted.'
##        #return autoAdjust
##    def _set(self, autoAdjust):
##        u'Indicates whether the text boxes are to be auto ajdusted.'
##    TextAutoAdjust = property(_get, _set, doc = _set.__doc__)
##
##    def GetTextSpacing(self):
##        u'Indicates the spacing between each two adjacent text boxes.'
##        #return textSpacingX, textSpacingY
##

class MarkerFillSymbol(CoClass):
    u'A fill symbol comprised of any of the supported marker symbols.'
    _reg_clsid_ = GUID('{7914E608-C892-11D0-8BB6-080009EE4E41}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
MarkerFillSymbol._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMarkerFillSymbol, IMapLevel, ISymbol, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySupport, IFillProperties, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, IDisplayName]

class CmykColor(CoClass):
    u'A color in the CMYK(Cyan Magenta Yellow, Black) color system.'
    _reg_clsid_ = GUID('{7EE9C497-D123-11D0-8383-080009B996CC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
CmykColor._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ICmykColor, IPostScriptColor, IColor, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize]

ISymbolCollection2._methods_ = [
    COMMETHOD(['propget', helpstring(u'The symbol associated with the symbolID.')], HRESULT, 'Symbol',
              ( ['in'], c_int, 'symbolID' ),
              ( ['retval', 'out'], POINTER(POINTER(ISymbol)), 'Symbol' )),
    COMMETHOD(['propputref', helpstring(u'The symbol associated with the symbolID.')], HRESULT, 'Symbol',
              ( ['in'], c_int, 'symbolID' ),
              ( ['in'], POINTER(ISymbol), 'Symbol' )),
    COMMETHOD([helpstring(u'Prepares the collection for Next to be called.')], HRESULT, 'Reset'),
    COMMETHOD([helpstring(u'Returns the next symbolID-symbol pair in the collection.')], HRESULT, 'Next',
              ( ['retval', 'out'], POINTER(POINTER(ISymbolIdentifier)), 'symbolID' )),
    COMMETHOD([helpstring(u'Replaces the symbol associated with the symbolID.')], HRESULT, 'Replace',
              ( ['in'], c_int, 'symbolID' ),
              ( ['in'], POINTER(ISymbol), 'Symbol' )),
    COMMETHOD([helpstring(u'Removes the symbolID-symbol pair in the collection.')], HRESULT, 'Remove',
              ( ['in'], c_int, 'symbolID' )),
    COMMETHOD([helpstring(u'Removes all the symbolID-symbol pairs in the collection.')], HRESULT, 'RemoveAll'),
    COMMETHOD([helpstring(u'Adds a symbol to the collection.  The ID will be set by the collection.')], HRESULT, 'AddSymbol',
              ( ['in'], POINTER(ISymbol), 'Symbol' ),
              ( ['in'], BSTR, 'Name' ),
              ( ['out'], POINTER(POINTER(ISymbolIdentifier2)), 'symbolID' )),
    COMMETHOD([helpstring(u'Returns the symbol with the given ID.')], HRESULT, 'GetSymbolIdentifier',
              ( ['in'], c_int, 'ID' ),
              ( ['out'], POINTER(POINTER(ISymbolIdentifier2)), 'symbolID' )),
    COMMETHOD([helpstring(u'Renames the symbol with the given ID.')], HRESULT, 'RenameSymbol',
              ( ['in'], c_int, 'symbolID' ),
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD(['propget', helpstring(u'The number of symbols in the collection.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
]
################################################################
## code template for ISymbolCollection2 implementation
##class ISymbolCollection2_Impl(object):
##    def Reset(self):
##        u'Prepares the collection for Next to be called.'
##        #return 
##
##    @property
##    def Count(self):
##        u'The number of symbols in the collection.'
##        #return Count
##
##    def Symbol(self, symbolID, Symbol):
##        u'The symbol associated with the symbolID.'
##        #return 
##
##    def Remove(self, symbolID):
##        u'Removes the symbolID-symbol pair in the collection.'
##        #return 
##
##    def Replace(self, symbolID, Symbol):
##        u'Replaces the symbol associated with the symbolID.'
##        #return 
##
##    def RemoveAll(self):
##        u'Removes all the symbolID-symbol pairs in the collection.'
##        #return 
##
##    def RenameSymbol(self, symbolID, Name):
##        u'Renames the symbol with the given ID.'
##        #return 
##
##    def AddSymbol(self, Symbol, Name):
##        u'Adds a symbol to the collection.  The ID will be set by the collection.'
##        #return symbolID
##
##    def Next(self):
##        u'Returns the next symbolID-symbol pair in the collection.'
##        #return symbolID
##
##    def GetSymbolIdentifier(self, ID):
##        u'Returns the symbol with the given ID.'
##        #return symbolID
##

IMultiPartColorRamp._methods_ = [
    COMMETHOD(['propput', helpstring(u'The color ramp at the index position.')], HRESULT, 'Ramp',
              ( ['in'], c_int, 'index' ),
              ( ['in'], POINTER(IColorRamp), 'ColorRamp' )),
    COMMETHOD(['propget', helpstring(u'The color ramp at the index position.')], HRESULT, 'Ramp',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IColorRamp)), 'ColorRamp' )),
    COMMETHOD([helpstring(u'Adds a color ramp to the list.')], HRESULT, 'AddRamp',
              ( ['in'], POINTER(IColorRamp), 'ColorRamp' )),
    COMMETHOD([helpstring(u'Removes the color ramp located at the index position.')], HRESULT, 'RemoveRamp',
              ( ['in'], c_int, 'index' )),
    COMMETHOD(['propget', helpstring(u'The number of constituent color ramps.')], HRESULT, 'NumberOfRamps',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
]
################################################################
## code template for IMultiPartColorRamp implementation
##class IMultiPartColorRamp_Impl(object):
##    def RemoveRamp(self, index):
##        u'Removes the color ramp located at the index position.'
##        #return 
##
##    def _get(self, index):
##        u'The color ramp at the index position.'
##        #return ColorRamp
##    def _set(self, index, ColorRamp):
##        u'The color ramp at the index position.'
##    Ramp = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def NumberOfRamps(self):
##        u'The number of constituent color ramps.'
##        #return Count
##
##    def AddRamp(self, ColorRamp):
##        u'Adds a color ramp to the list.'
##        #return 
##

IGraphicAttributeEnumType._methods_ = [
    COMMETHOD([helpstring(u'Resets the enumeration of values.')], HRESULT, 'Reset'),
    COMMETHOD([helpstring(u'Hands back the next value in the enumeration.')], HRESULT, 'NextValue',
              ( ['retval', 'out'], POINTER(c_int), 'val' )),
    COMMETHOD([helpstring(u'Adds a new value to the graphic attribute enumeration.')], HRESULT, 'AddValue',
              ( ['in'], c_int, 'Value' ),
              ( ['in'], BSTR, 'Text' )),
]
################################################################
## code template for IGraphicAttributeEnumType implementation
##class IGraphicAttributeEnumType_Impl(object):
##    def Reset(self):
##        u'Resets the enumeration of values.'
##        #return 
##
##    def AddValue(self, Value, Text):
##        u'Adds a new value to the graphic attribute enumeration.'
##        #return 
##
##    def NextValue(self):
##        u'Hands back the next value in the enumeration.'
##        #return val
##

class IMask(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the symbol mask.'
    _iid_ = GUID('{6A7EF984-6924-11D2-980D-0080C7E04196}')
    _idlflags_ = ['oleautomation']
IMask._methods_ = [
    COMMETHOD(['propget', helpstring(u'The mask style.')], HRESULT, 'MaskStyle',
              ( ['retval', 'out'], POINTER(esriMaskStyle), 'Style' )),
    COMMETHOD(['propput', helpstring(u'The mask style.')], HRESULT, 'MaskStyle',
              ( ['in'], esriMaskStyle, 'Style' )),
    COMMETHOD(['propget', helpstring(u'The mask size.')], HRESULT, 'MaskSize',
              ( ['retval', 'out'], POINTER(c_double), 'Size' )),
    COMMETHOD(['propput', helpstring(u'The mask size.')], HRESULT, 'MaskSize',
              ( ['in'], c_double, 'Size' )),
    COMMETHOD(['propget', helpstring(u'The mask symbol.')], HRESULT, 'MaskSymbol',
              ( ['retval', 'out'], POINTER(POINTER(IFillSymbol)), 'fillSym' )),
    COMMETHOD(['propputref', helpstring(u'The mask symbol.')], HRESULT, 'MaskSymbol',
              ( ['in'], POINTER(IFillSymbol), 'fillSym' )),
]
################################################################
## code template for IMask implementation
##class IMask_Impl(object):
##    def _get(self):
##        u'The mask size.'
##        #return Size
##    def _set(self, Size):
##        u'The mask size.'
##    MaskSize = property(_get, _set, doc = _set.__doc__)
##
##    def MaskSymbol(self, fillSym):
##        u'The mask symbol.'
##        #return 
##
##    def _get(self):
##        u'The mask style.'
##        #return Style
##    def _set(self, Style):
##        u'The mask style.'
##    MaskStyle = property(_get, _set, doc = _set.__doc__)
##

IMultiLayerLineSymbol._methods_ = [
    COMMETHOD(['propget', helpstring(u'The number of layers in the symbol.')], HRESULT, 'LayerCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Line symbol per index value.')], HRESULT, 'Layer',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(ILineSymbol)), 'lineLayer' )),
    COMMETHOD([helpstring(u'Adds a layer to the line symbol.')], HRESULT, 'AddLayer',
              ( ['in'], POINTER(ILineSymbol), 'lineLayer' )),
    COMMETHOD([helpstring(u'Deletes a layer from the line symbol.')], HRESULT, 'DeleteLayer',
              ( ['in'], POINTER(ILineSymbol), 'lineLayer' )),
    COMMETHOD([helpstring(u'Move line symbol layer to different layer position.')], HRESULT, 'MoveLayer',
              ( ['in'], POINTER(ILineSymbol), 'lineLayer' ),
              ( ['in'], c_int, 'toIndex' )),
    COMMETHOD([helpstring(u'Removes all line symbol layers.')], HRESULT, 'ClearLayers'),
    COMMETHOD([helpstring(u'Draws a line symbol layer.')], HRESULT, 'DrawLayer',
              ( ['in'], c_int, 'index' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'Geometry' )),
]
################################################################
## code template for IMultiLayerLineSymbol implementation
##class IMultiLayerLineSymbol_Impl(object):
##    @property
##    def Layer(self, index):
##        u'Line symbol per index value.'
##        #return lineLayer
##
##    @property
##    def LayerCount(self):
##        u'The number of layers in the symbol.'
##        #return Count
##
##    def DeleteLayer(self, lineLayer):
##        u'Deletes a layer from the line symbol.'
##        #return 
##
##    def DrawLayer(self, index, Geometry):
##        u'Draws a line symbol layer.'
##        #return 
##
##    def MoveLayer(self, lineLayer, toIndex):
##        u'Move line symbol layer to different layer position.'
##        #return 
##
##    def ClearLayers(self):
##        u'Removes all line symbol layers.'
##        #return 
##
##    def AddLayer(self, lineLayer):
##        u'Adds a layer to the line symbol.'
##        #return 
##

ISimpleLineDecorationElement._methods_ = [
    COMMETHOD(['propget', helpstring(u'The marker symbol.')], HRESULT, 'MarkerSymbol',
              ( ['retval', 'out'], POINTER(POINTER(IMarkerSymbol)), 'MarkerSymbol' )),
    COMMETHOD(['propput', helpstring(u'The marker symbol.')], HRESULT, 'MarkerSymbol',
              ( ['in'], POINTER(IMarkerSymbol), 'MarkerSymbol' )),
    COMMETHOD(['propget', helpstring(u'Indicates if marker symbols are rotated to follow the line.')], HRESULT, 'Rotate',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Rotate' )),
    COMMETHOD(['propput', helpstring(u'Indicates if marker symbols are rotated to follow the line.')], HRESULT, 'Rotate',
              ( ['in'], VARIANT_BOOL, 'Rotate' )),
    COMMETHOD(['propget', helpstring(u"Indicates if marker symbol in '0' position is flipped 180 degrees.")], HRESULT, 'FlipFirst',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'FlipFirst' )),
    COMMETHOD(['propput', helpstring(u"Indicates if marker symbol in '0' position is flipped 180 degrees.")], HRESULT, 'FlipFirst',
              ( ['in'], VARIANT_BOOL, 'FlipFirst' )),
    COMMETHOD(['propget', helpstring(u'Indicates if all symbols are flipped 180 degrees.')], HRESULT, 'FlipAll',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'FlipAll' )),
    COMMETHOD(['propput', helpstring(u'Indicates if all symbols are flipped 180 degrees.')], HRESULT, 'FlipAll',
              ( ['in'], VARIANT_BOOL, 'FlipAll' )),
]
################################################################
## code template for ISimpleLineDecorationElement implementation
##class ISimpleLineDecorationElement_Impl(object):
##    def _get(self):
##        u'The marker symbol.'
##        #return MarkerSymbol
##    def _set(self, MarkerSymbol):
##        u'The marker symbol.'
##    MarkerSymbol = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if marker symbols are rotated to follow the line.'
##        #return Rotate
##    def _set(self, Rotate):
##        u'Indicates if marker symbols are rotated to follow the line.'
##    Rotate = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u"Indicates if marker symbol in '0' position is flipped 180 degrees."
##        #return FlipFirst
##    def _set(self, FlipFirst):
##        u"Indicates if marker symbol in '0' position is flipped 180 degrees."
##    FlipFirst = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if all symbols are flipped 180 degrees.'
##        #return FlipAll
##    def _set(self, FlipAll):
##        u'Indicates if all symbols are flipped 180 degrees.'
##    FlipAll = property(_get, _set, doc = _set.__doc__)
##

class esriGDICommentEndText(Structure):
    _recordinfo_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2, 0L, '{E90DFCAA-5248-4A3B-8EDF-DD80BFD92B99}')
esriGDICommentEndText._fields_ = [
    ('dSignature', c_ulong),
    ('nVersion', c_ulong),
]
assert sizeof(esriGDICommentEndText) == 8, sizeof(esriGDICommentEndText)
assert alignment(esriGDICommentEndText) == 4, alignment(esriGDICommentEndText)
class MarkerPlacementVariableAlongLine(CoClass):
    u'Places markers with variable size along a line.'
    _reg_clsid_ = GUID('{A083595C-15DD-4AD2-A30C-90B7087E5DB6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
MarkerPlacementVariableAlongLine._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMarkerPlacement, IGraphicAttributes, IGraphicAttributes2, IEditInteraction, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

class PresetColorRamp(CoClass):
    u'Defines a preset color ramp, where ramp is defined by a list of exactly 13 manually specified colors.'
    _reg_clsid_ = GUID('{BEB8709A-C0B4-11D0-8379-080009B996CC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
PresetColorRamp._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IPresetColorRamp, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize]

IIlluminationProps._methods_ = [
    COMMETHOD(['propget', helpstring(u'Illumination vector as cosines of angles to X,Y,Z axes.')], HRESULT, 'SunPosition',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.WKSPointZ), 'Position' )),
    COMMETHOD(['propput', helpstring(u'Illumination vector as cosines of angles to X,Y,Z axes.')], HRESULT, 'SunPosition',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.WKSPointZ, 'Position' )),
    COMMETHOD(['propget', helpstring(u'Ratio of bright to shadow illumination.')], HRESULT, 'Contrast',
              ( ['retval', 'out'], POINTER(c_double), 'Contrast' )),
    COMMETHOD(['propput', helpstring(u'Ratio of bright to shadow illumination.')], HRESULT, 'Contrast',
              ( ['in'], c_double, 'Contrast' )),
    COMMETHOD(['propget', helpstring(u'Azimuth angle of illumination.')], HRESULT, 'Azimuth',
              ( ['retval', 'out'], POINTER(c_double), 'pAzimuth' )),
    COMMETHOD(['propput', helpstring(u'Azimuth angle of illumination.')], HRESULT, 'Azimuth',
              ( ['in'], c_double, 'pAzimuth' )),
    COMMETHOD(['propget', helpstring(u'Altitude angle of illumination.')], HRESULT, 'Altitude',
              ( ['retval', 'out'], POINTER(c_double), 'pAltitude' )),
    COMMETHOD(['propput', helpstring(u'Altitude angle of illumination.')], HRESULT, 'Altitude',
              ( ['in'], c_double, 'pAltitude' )),
]
################################################################
## code template for IIlluminationProps implementation
##class IIlluminationProps_Impl(object):
##    def _get(self):
##        u'Illumination vector as cosines of angles to X,Y,Z axes.'
##        #return Position
##    def _set(self, Position):
##        u'Illumination vector as cosines of angles to X,Y,Z axes.'
##    SunPosition = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Altitude angle of illumination.'
##        #return pAltitude
##    def _set(self, pAltitude):
##        u'Altitude angle of illumination.'
##    Altitude = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Ratio of bright to shadow illumination.'
##        #return Contrast
##    def _set(self, Contrast):
##        u'Ratio of bright to shadow illumination.'
##    Contrast = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Azimuth angle of illumination.'
##        #return pAzimuth
##    def _set(self, pAzimuth):
##        u'Azimuth angle of illumination.'
##    Azimuth = property(_get, _set, doc = _set.__doc__)
##

IOutputContext._methods_ = [
    COMMETHOD([helpstring(u'Initializes the output context.')], HRESULT, 'Init',
              ( ['in'], c_double, 'refScale' ),
              ( ['in'], c_double, 'currentScale' ),
              ( ['in'], c_double, 'Resolution' ),
              ( ['in'], c_double, 'Rotation' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'currentScreenCenter' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.tagRECT), 'deviceRect' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'outputDevice' )),
    COMMETHOD([helpstring(u'Converts map geometry to output geometry.')], HRESULT, 'FromMapToOutput',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'ingeom' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry)), 'outgeom' )),
    COMMETHOD(['propput', helpstring(u'Drawing will react on Cancel of ITrackCancel is not NULL.')], HRESULT, 'TrackCancel',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'TrackCancel' )),
    COMMETHOD(['propget', helpstring(u'Drawing will react on Cancel of ITrackCancel is not NULL.')], HRESULT, 'TrackCancel',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel)), 'TrackCancel' )),
    COMMETHOD(['propget', helpstring(u'The device context that the display is currently drawing to.')], HRESULT, 'hDC',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'hDC' )),
]
################################################################
## code template for IOutputContext implementation
##class IOutputContext_Impl(object):
##    def _get(self):
##        u'Drawing will react on Cancel of ITrackCancel is not NULL.'
##        #return TrackCancel
##    def _set(self, TrackCancel):
##        u'Drawing will react on Cancel of ITrackCancel is not NULL.'
##    TrackCancel = property(_get, _set, doc = _set.__doc__)
##
##    def Init(self, refScale, currentScale, Resolution, Rotation, currentScreenCenter, deviceRect, outputDevice):
##        u'Initializes the output context.'
##        #return 
##
##    @property
##    def hDC(self):
##        u'The device context that the display is currently drawing to.'
##        #return hDC
##
##    def FromMapToOutput(self, ingeom):
##        u'Converts map geometry to output geometry.'
##        #return outgeom
##


# values for enumeration 'esriRasterOpCode'
esriROPBlack = 1
esriROPNotMergePen = 2
esriROPMaskNotPen = 3
esriROPNotCopyPen = 4
esriROPMaskPenNot = 5
esriROPNot = 6
esriROPXOrPen = 7
esriROPNotMaskPen = 8
esriROPMaskPen = 9
esriROPNotXOrPen = 10
esriROPNOP = 11
esriROPMergeNotPen = 12
esriROPCopyPen = 13
esriROPMergePenNot = 14
esriROPMergePen = 15
esriROPWhite = 16
esriRasterOpCode = c_int # enum
IRasterOutputSettings._methods_ = [
    COMMETHOD(['propget', helpstring(u"Resolution used to output rasterized data.  A value of 0 means 'same as device'.")], HRESULT, 'RasterResolution',
              ( ['retval', 'out'], POINTER(c_double), 'dpi' )),
    COMMETHOD(['propput', helpstring(u"Resolution used to output rasterized data.  A value of 0 means 'same as device'.")], HRESULT, 'RasterResolution',
              ( ['in'], c_double, 'dpi' )),
    COMMETHOD(['propget', helpstring(u'Maximum color depth for raster output.  Specify bits per pixel, i.e., 4, 8, 16.')], HRESULT, 'MaxColorDepth',
              ( ['retval', 'out'], POINTER(c_short), 'bitsPerPixel' )),
    COMMETHOD(['propput', helpstring(u'Maximum color depth for raster output.  Specify bits per pixel, i.e., 4, 8, 16.')], HRESULT, 'MaxColorDepth',
              ( ['in'], c_short, 'bitsPerPixel' )),
    COMMETHOD(['propget', helpstring(u'Ratio between resolution and raster resolution.')], HRESULT, 'RasterRatio',
              ( ['retval', 'out'], POINTER(c_double), 'ratio' )),
]
################################################################
## code template for IRasterOutputSettings implementation
##class IRasterOutputSettings_Impl(object):
##    @property
##    def RasterRatio(self):
##        u'Ratio between resolution and raster resolution.'
##        #return ratio
##
##    def _get(self):
##        u"Resolution used to output rasterized data.  A value of 0 means 'same as device'."
##        #return dpi
##    def _set(self, dpi):
##        u"Resolution used to output rasterized data.  A value of 0 means 'same as device'."
##    RasterResolution = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Maximum color depth for raster output.  Specify bits per pixel, i.e., 4, 8, 16.'
##        #return bitsPerPixel
##    def _set(self, bitsPerPixel):
##        u'Maximum color depth for raster output.  Specify bits per pixel, i.e., 4, 8, 16.'
##    MaxColorDepth = property(_get, _set, doc = _set.__doc__)
##

class esriGDICommentSetTextExtra(Structure):
    _recordinfo_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2, 0L, '{253536F7-92CA-4A19-B7AA-4EB2A1BDA935}')
esriGDICommentSetTextExtra._fields_ = [
    ('dSignature', c_ulong),
    ('nVersion', c_ulong),
    ('dExtraSpacing', c_ulong),
]
assert sizeof(esriGDICommentSetTextExtra) == 12, sizeof(esriGDICommentSetTextExtra)
assert alignment(esriGDICommentSetTextExtra) == 4, alignment(esriGDICommentSetTextExtra)
class esriGDICommentSetCmykColor(Structure):
    _recordinfo_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2, 0L, '{6DF6074E-4773-418C-A690-4F949AAF998F}')
esriGDICommentSetCmykColor._fields_ = [
    ('dSignature', c_ulong),
    ('nVersion', c_ulong),
    ('cmykClr', c_ulong),
    ('IsSpotColor', c_short),
    ('colorType', c_short),
]
assert sizeof(esriGDICommentSetCmykColor) == 16, sizeof(esriGDICommentSetCmykColor)
assert alignment(esriGDICommentSetCmykColor) == 4, alignment(esriGDICommentSetCmykColor)
IStackedChartSymbol._methods_ = [
    COMMETHOD(['propget', helpstring(u'The width of the bar in points.')], HRESULT, 'Width',
              ( ['retval', 'out'], POINTER(c_double), 'Points' )),
    COMMETHOD(['propput', helpstring(u'The width of the bar in points.')], HRESULT, 'Width',
              ( ['in'], c_double, 'Points' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the bar is oriented vertically.')], HRESULT, 'VerticalBar',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the bar is oriented vertically.')], HRESULT, 'VerticalBar',
              ( ['in'], VARIANT_BOOL, 'flag' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the outline symbol is drawn.')], HRESULT, 'UseOutline',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the outline symbol is drawn.')], HRESULT, 'UseOutline',
              ( ['in'], VARIANT_BOOL, 'flag' )),
    COMMETHOD(['propget', helpstring(u'The symbol for the chart outline.')], HRESULT, 'Outline',
              ( ['retval', 'out'], POINTER(POINTER(ILineSymbol)), 'Symbol' )),
    COMMETHOD(['propput', helpstring(u'The symbol for the chart outline.')], HRESULT, 'Outline',
              ( ['in'], POINTER(ILineSymbol), 'Symbol' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the bars are of a fixed length (the alternative is graduated length bars).')], HRESULT, 'Fixed',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the bars are of a fixed length (the alternative is graduated length bars).')], HRESULT, 'Fixed',
              ( ['in'], VARIANT_BOOL, 'flag' )),
]
################################################################
## code template for IStackedChartSymbol implementation
##class IStackedChartSymbol_Impl(object):
##    def _get(self):
##        u'The width of the bar in points.'
##        #return Points
##    def _set(self, Points):
##        u'The width of the bar in points.'
##    Width = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the bar is oriented vertically.'
##        #return flag
##    def _set(self, flag):
##        u'Indicates if the bar is oriented vertically.'
##    VerticalBar = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the bars are of a fixed length (the alternative is graduated length bars).'
##        #return flag
##    def _set(self, flag):
##        u'Indicates if the bars are of a fixed length (the alternative is graduated length bars).'
##    Fixed = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The symbol for the chart outline.'
##        #return Symbol
##    def _set(self, Symbol):
##        u'The symbol for the chart outline.'
##    Outline = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the outline symbol is drawn.'
##        #return flag
##    def _set(self, flag):
##        u'Indicates if the outline symbol is drawn.'
##    UseOutline = property(_get, _set, doc = _set.__doc__)
##

class esriGDICommentBeginLayer(Structure):
    _recordinfo_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2, 0L, '{B492B2D7-61C6-46C8-841E-A418DD88B649}')
esriGDICommentBeginLayer._fields_ = [
    ('dSignature', c_ulong),
    ('nVersion', c_ulong),
    ('nDescription', c_ulong),
]
assert sizeof(esriGDICommentBeginLayer) == 12, sizeof(esriGDICommentBeginLayer)
assert alignment(esriGDICommentBeginLayer) == 4, alignment(esriGDICommentBeginLayer)
IOverposterTextPath._methods_ = [
]
################################################################
## code template for IOverposterTextPath implementation
##class IOverposterTextPath_Impl(object):

ISymbolIdentifier2._methods_ = [
    COMMETHOD(['propget', helpstring(u'The symbol associated with the symbolID.')], HRESULT, 'Symbol',
              ( ['retval', 'out'], POINTER(POINTER(ISymbol)), 'Symbol' )),
    COMMETHOD(['propputref', helpstring(u'The symbol associated with the symbolID.')], HRESULT, 'Symbol',
              ( ['in'], POINTER(ISymbol), 'Symbol' )),
    COMMETHOD(['propget', helpstring(u'The symbolID associated with the symbol.')], HRESULT, 'ID',
              ( ['retval', 'out'], POINTER(c_int), 'symbolID' )),
    COMMETHOD(['propput', helpstring(u'The symbolID associated with the symbol.')], HRESULT, 'ID',
              ( ['in'], c_int, 'symbolID' )),
    COMMETHOD(['propget', helpstring(u'The name associated with the symbol.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propput', helpstring(u'The name associated with the symbol.')], HRESULT, 'Name',
              ( ['in'], BSTR, 'Name' )),
]
################################################################
## code template for ISymbolIdentifier2 implementation
##class ISymbolIdentifier2_Impl(object):
##    def Symbol(self, Symbol):
##        u'The symbol associated with the symbolID.'
##        #return 
##
##    def _get(self):
##        u'The symbolID associated with the symbol.'
##        #return symbolID
##    def _set(self, symbolID):
##        u'The symbolID associated with the symbol.'
##    ID = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The name associated with the symbol.'
##        #return Name
##    def _set(self, Name):
##        u'The name associated with the symbol.'
##    Name = property(_get, _set, doc = _set.__doc__)
##

class MultiLayerMarkerSymbol(CoClass):
    u'A marker symbol that contains one or more layers.'
    _reg_clsid_ = GUID('{7914E5FF-C892-11D0-8BB6-080009EE4E41}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
MultiLayerMarkerSymbol._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMultiLayerMarkerSymbol, IMapLevel, ISymbol, ISymbolRotation, IMask, IMarkerMask, IMarkerBackgroundSupport, ILayerVisible, ILayerColorLock, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySupport, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, ILayerTags]

IResizeTextFeedback._methods_ = [
    COMMETHOD([helpstring(u'Begins a resize feedback of the given text symbol.')], HRESULT, 'Start',
              ( ['in'], POINTER(ITextSymbol), 'TextSymbol' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'textGeom' ),
              ( ['in'], c_double, 'ReferenceScale' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'envelope' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
    COMMETHOD([helpstring(u'Stops the feedback and returns the new size.')], HRESULT, 'Stop',
              ( ['retval', 'out'], POINTER(c_double), 'Size' )),
]
################################################################
## code template for IResizeTextFeedback implementation
##class IResizeTextFeedback_Impl(object):
##    def Start(self, TextSymbol, textGeom, ReferenceScale, envelope, Point):
##        u'Begins a resize feedback of the given text symbol.'
##        #return 
##
##    def Stop(self):
##        u'Stops the feedback and returns the new size.'
##        #return Size
##

class ModifyCircularArcFeedback(CoClass):
    u'Feedback object for modifying a circular arc.'
    _reg_clsid_ = GUID('{4B2D14A8-6E54-48A5-8B38-A0F174BE5ACA}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
ModifyCircularArcFeedback._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDisplayFeedback, IDisplayFeedback2, IModifyCircularArcFeedback]

IBalloonCallout._methods_ = [
    COMMETHOD(['propget', helpstring(u'The balloon callout style.')], HRESULT, 'Style',
              ( ['retval', 'out'], POINTER(esriBalloonCalloutStyle), 'Style' )),
    COMMETHOD(['propput', helpstring(u'The balloon callout style.')], HRESULT, 'Style',
              ( ['in'], esriBalloonCalloutStyle, 'Style' )),
    COMMETHOD(['propget', helpstring(u'The fill symbol.')], HRESULT, 'Symbol',
              ( ['retval', 'out'], POINTER(POINTER(IFillSymbol)), 'fillSym' )),
    COMMETHOD(['propputref', helpstring(u'The fill symbol.')], HRESULT, 'Symbol',
              ( ['in'], POINTER(IFillSymbol), 'fillSym' )),
]
################################################################
## code template for IBalloonCallout implementation
##class IBalloonCallout_Impl(object):
##    def _get(self):
##        u'The balloon callout style.'
##        #return Style
##    def _set(self, Style):
##        u'The balloon callout style.'
##    Style = property(_get, _set, doc = _set.__doc__)
##
##    def Symbol(self, fillSym):
##        u'The fill symbol.'
##        #return 
##

class esriGDICommentBeginGroup(Structure):
    _recordinfo_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2, 0L, '{D3B767CC-E9BE-4A4B-B4C2-06316A7D2559}')
esriGDICommentBeginGroup._fields_ = [
    ('dSignature', c_ulong),
    ('nVersion', c_ulong),
    ('nDescription', c_ulong),
]
assert sizeof(esriGDICommentBeginGroup) == 12, sizeof(esriGDICommentBeginGroup)
assert alignment(esriGDICommentBeginGroup) == 4, alignment(esriGDICommentBeginGroup)
class esriGDICommentEndLayer(Structure):
    _recordinfo_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2, 0L, '{A44AED04-E366-4A0D-AA6E-F43C87E84840}')
esriGDICommentEndLayer._fields_ = [
    ('dSignature', c_ulong),
    ('nVersion', c_ulong),
]
assert sizeof(esriGDICommentEndLayer) == 8, sizeof(esriGDICommentEndLayer)
assert alignment(esriGDICommentEndLayer) == 4, alignment(esriGDICommentEndLayer)
ICieLabConversion._methods_ = [
    COMMETHOD([helpstring(u'Converts an RGB color to a CIELAB color.')], HRESULT, 'RgbToLab',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_COLOR, 'RGB' ),
              ( ['out'], POINTER(c_double), 'l' ),
              ( [], POINTER(c_double), 'a' ),
              ( [], POINTER(c_double), 'b' )),
    COMMETHOD([helpstring(u'Converts a CIELAB color to an RGB color.')], HRESULT, 'LabToRgb',
              ( ['out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_COLOR), 'RGB' ),
              ( ['in'], c_double, 'l' ),
              ( [], c_double, 'a' ),
              ( [], c_double, 'b' )),
    COMMETHOD([helpstring(u'Converts an RGB color to a CIELAB color.')], HRESULT, 'HsvToLab',
              ( ['in'], c_short, 'h' ),
              ( ['in'], c_ubyte, 's' ),
              ( ['in'], c_ubyte, 'v' ),
              ( ['out'], POINTER(c_double), 'l' ),
              ( [], POINTER(c_double), 'a' ),
              ( [], POINTER(c_double), 'b' )),
    COMMETHOD([helpstring(u'Converts a CIELAB color to an RGB color.')], HRESULT, 'LabToHsv',
              ( ['out'], POINTER(c_short), 'h' ),
              ( ['out'], POINTER(c_ubyte), 's' ),
              ( ['out'], POINTER(c_ubyte), 'v' ),
              ( ['in'], c_double, 'l' ),
              ( [], c_double, 'a' ),
              ( [], c_double, 'b' )),
    COMMETHOD([helpstring(u'Gets visual difference between two CIELAB colors.')], HRESULT, 'GetDistance',
              ( ['in'], c_double, 'l1' ),
              ( [], c_double, 'a1' ),
              ( [], c_double, 'b1' ),
              ( [], c_double, 'l2' ),
              ( [], c_double, 'a2' ),
              ( [], c_double, 'b2' ),
              ( ['retval', 'out'], POINTER(c_double), 'dist' )),
    COMMETHOD([helpstring(u'Reloads the monitor settings from the registry.')], HRESULT, 'ReloadSettings'),
    COMMETHOD(['propget', helpstring(u'The monitor settings version.')], HRESULT, 'SettingsVersion',
              ( ['retval', 'out'], POINTER(c_int), 'version' )),
]
################################################################
## code template for ICieLabConversion implementation
##class ICieLabConversion_Impl(object):
##    def GetDistance(self, l1, a1, b1, l2, a2, b2):
##        u'Gets visual difference between two CIELAB colors.'
##        #return dist
##
##    def LabToRgb(self, l, a, b):
##        u'Converts a CIELAB color to an RGB color.'
##        #return RGB
##
##    def HsvToLab(self, h, s, v, a, b):
##        u'Converts an RGB color to a CIELAB color.'
##        #return l
##
##    def ReloadSettings(self):
##        u'Reloads the monitor settings from the registry.'
##        #return 
##
##    def LabToHsv(self, l, a, b):
##        u'Converts a CIELAB color to an RGB color.'
##        #return h, s, v
##
##    @property
##    def SettingsVersion(self):
##        u'The monitor settings version.'
##        #return version
##
##    def RgbToLab(self, RGB, a, b):
##        u'Converts an RGB color to a CIELAB color.'
##        #return l
##

class MarkerPlacementRandomAlongLine(CoClass):
    u'Places markers randomly along a line.'
    _reg_clsid_ = GUID('{2FDC4496-ED2B-4ECC-B557-053873FD0C03}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
MarkerPlacementRandomAlongLine._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMarkerPlacement, IGraphicAttributes, IGraphicAttributes2, IEditInteraction, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

IMarkerTextBackground._methods_ = [
    COMMETHOD(['propget', helpstring(u'The marker symbol.')], HRESULT, 'Symbol',
              ( ['retval', 'out'], POINTER(POINTER(IMarkerSymbol)), 'MarkerSymbol' )),
    COMMETHOD(['propputref', helpstring(u'The marker symbol.')], HRESULT, 'Symbol',
              ( ['in'], POINTER(IMarkerSymbol), 'MarkerSymbol' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the marker symbol is scaled to fill the text box.')], HRESULT, 'ScaleToFit',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'scale' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the marker symbol is scaled to fill the text box.')], HRESULT, 'ScaleToFit',
              ( ['in'], VARIANT_BOOL, 'scale' )),
]
################################################################
## code template for IMarkerTextBackground implementation
##class IMarkerTextBackground_Impl(object):
##    def _get(self):
##        u'Indicates if the marker symbol is scaled to fill the text box.'
##        #return scale
##    def _set(self, scale):
##        u'Indicates if the marker symbol is scaled to fill the text box.'
##    ScaleToFit = property(_get, _set, doc = _set.__doc__)
##
##    def Symbol(self, MarkerSymbol):
##        u'The marker symbol.'
##        #return 
##

class RubberRectangularPolygon(CoClass):
    u'Rubberbanding class for rectangular polygons (rotatable envelopes).'
    _reg_clsid_ = GUID('{087675C8-7F23-4CF5-A39D-BCEC1EE9C1F4}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
RubberRectangularPolygon._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRubberBand, IRubberBand2]

class esriGDICommentFillWithPattern(Structure):
    _recordinfo_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2, 0L, '{D14CFF4B-8BF0-4F92-82FC-FA4B56D212AA}')
esriGDICommentFillWithPattern._fields_ = [
    ('dSignature', c_ulong),
    ('nVersion', c_ulong),
    ('clrfFgColor', c_ulong),
    ('clrfBkColor', c_ulong),
    ('iPatterXSizePix', c_int),
    ('iPatterYSizePix', c_int),
    ('dwPatterFormat', c_ulong),
    ('dPatternTransformScaleX', c_double),
    ('dPatternTransformScaleY', c_double),
    ('dPatternTransformOffsetX', c_double),
    ('dPatternTransformOffsetY', c_double),
    ('dwPatternDataSize', c_ulong),
]
assert sizeof(esriGDICommentFillWithPattern) == 72, sizeof(esriGDICommentFillWithPattern)
assert alignment(esriGDICommentFillWithPattern) == 8, alignment(esriGDICommentFillWithPattern)
INewMultiPointFeedback._methods_ = [
    COMMETHOD([helpstring(u'Begins a normal feedback at the given point.')], HRESULT, 'Start',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPointCollection), 'Points' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
    COMMETHOD([helpstring(u'Stops the feedback and returns the shape.')], HRESULT, 'Stop'),
]
################################################################
## code template for INewMultiPointFeedback implementation
##class INewMultiPointFeedback_Impl(object):
##    def Start(self, Points, Point):
##        u'Begins a normal feedback at the given point.'
##        #return 
##
##    def Stop(self):
##        u'Stops the feedback and returns the shape.'
##        #return 
##

class Library(object):
    u'Esri Display Object Library 10.2'
    name = u'esriDisplay'
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)

class esriGDICommentPlayEnhMetafileEnd(Structure):
    _recordinfo_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2, 0L, '{D0C9AE65-4CCF-4ED3-B91B-00DB63FC6D28}')
esriGDICommentPlayEnhMetafileEnd._fields_ = [
    ('dSignature', c_ulong),
    ('nVersion', c_ulong),
]
assert sizeof(esriGDICommentPlayEnhMetafileEnd) == 8, sizeof(esriGDICommentPlayEnhMetafileEnd)
assert alignment(esriGDICommentPlayEnhMetafileEnd) == 4, alignment(esriGDICommentPlayEnhMetafileEnd)
class esriGDICommentMaskLayer(Structure):
    _recordinfo_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2, 0L, '{FD5B3C31-4346-44A8-B993-E55CA3BA3BA3}')
esriGDICommentMaskLayer._fields_ = [
    ('dSignature', c_ulong),
    ('nVersion', c_ulong),
]
assert sizeof(esriGDICommentMaskLayer) == 8, sizeof(esriGDICommentMaskLayer)
assert alignment(esriGDICommentMaskLayer) == 4, alignment(esriGDICommentMaskLayer)
class esriGDICommentMaskLayerBeforeClipping(Structure):
    _recordinfo_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2, 0L, '{79CA64B9-55B8-4BFE-939A-382D5C19004B}')
esriGDICommentMaskLayerBeforeClipping._fields_ = [
    ('dSignature', c_ulong),
    ('nVersion', c_ulong),
]
assert sizeof(esriGDICommentMaskLayerBeforeClipping) == 8, sizeof(esriGDICommentMaskLayerBeforeClipping)
assert alignment(esriGDICommentMaskLayerBeforeClipping) == 4, alignment(esriGDICommentMaskLayerBeforeClipping)
ITextMargins._methods_ = [
    COMMETHOD(['propget', helpstring(u'Value for the left margin.')], HRESULT, 'LeftMargin',
              ( ['retval', 'out'], POINTER(c_double), 'LeftMargin' )),
    COMMETHOD(['propput', helpstring(u'Value for the left margin.')], HRESULT, 'LeftMargin',
              ( ['in'], c_double, 'LeftMargin' )),
    COMMETHOD(['propget', helpstring(u'Value for the right margin.')], HRESULT, 'RightMargin',
              ( ['retval', 'out'], POINTER(c_double), 'RightMargin' )),
    COMMETHOD(['propput', helpstring(u'Value for the right margin.')], HRESULT, 'RightMargin',
              ( ['in'], c_double, 'RightMargin' )),
    COMMETHOD(['propget', helpstring(u'Value for the top margin.')], HRESULT, 'TopMargin',
              ( ['retval', 'out'], POINTER(c_double), 'TopMargin' )),
    COMMETHOD(['propput', helpstring(u'Value for the top margin.')], HRESULT, 'TopMargin',
              ( ['in'], c_double, 'TopMargin' )),
    COMMETHOD(['propget', helpstring(u'Value for the bottom margin.')], HRESULT, 'BottomMargin',
              ( ['retval', 'out'], POINTER(c_double), 'BottomMargin' )),
    COMMETHOD(['propput', helpstring(u'Value for the bottom margin.')], HRESULT, 'BottomMargin',
              ( ['in'], c_double, 'BottomMargin' )),
    COMMETHOD([helpstring(u'Sets the margins.')], HRESULT, 'PutMargins',
              ( ['in'], c_double, 'Left' ),
              ( ['in'], c_double, 'Top' ),
              ( ['in'], c_double, 'Right' ),
              ( ['in'], c_double, 'Bottom' )),
    COMMETHOD([helpstring(u'Returns the margins.')], HRESULT, 'QueryMargins',
              ( ['out'], POINTER(c_double), 'Left' ),
              ( ['out'], POINTER(c_double), 'Top' ),
              ( ['out'], POINTER(c_double), 'Right' ),
              ( ['out'], POINTER(c_double), 'Bottom' )),
]
################################################################
## code template for ITextMargins implementation
##class ITextMargins_Impl(object):
##    def _get(self):
##        u'Value for the top margin.'
##        #return TopMargin
##    def _set(self, TopMargin):
##        u'Value for the top margin.'
##    TopMargin = property(_get, _set, doc = _set.__doc__)
##
##    def PutMargins(self, Left, Top, Right, Bottom):
##        u'Sets the margins.'
##        #return 
##
##    def _get(self):
##        u'Value for the right margin.'
##        #return RightMargin
##    def _set(self, RightMargin):
##        u'Value for the right margin.'
##    RightMargin = property(_get, _set, doc = _set.__doc__)
##
##    def QueryMargins(self):
##        u'Returns the margins.'
##        #return Left, Top, Right, Bottom
##
##    def _get(self):
##        u'Value for the bottom margin.'
##        #return BottomMargin
##    def _set(self, BottomMargin):
##        u'Value for the bottom margin.'
##    BottomMargin = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Value for the left margin.'
##        #return LeftMargin
##    def _set(self, LeftMargin):
##        u'Value for the left margin.'
##    LeftMargin = property(_get, _set, doc = _set.__doc__)
##

ISymbolCollection._methods_ = [
    COMMETHOD(['propget', helpstring(u'The symbol associated with the symbolID.')], HRESULT, 'Symbol',
              ( ['in'], c_int, 'symbolID' ),
              ( ['retval', 'out'], POINTER(POINTER(ISymbol)), 'Symbol' )),
    COMMETHOD(['propputref', helpstring(u'The symbol associated with the symbolID.')], HRESULT, 'Symbol',
              ( ['in'], c_int, 'symbolID' ),
              ( ['in'], POINTER(ISymbol), 'Symbol' )),
    COMMETHOD([helpstring(u'Prepares the collection for Next to be called.')], HRESULT, 'Reset'),
    COMMETHOD([helpstring(u'Returns the next symbolID-symbol pair in the collection.')], HRESULT, 'Next',
              ( ['retval', 'out'], POINTER(POINTER(ISymbolIdentifier)), 'symbolID' )),
    COMMETHOD([helpstring(u'Replaces the symbol associated with the symbolID.')], HRESULT, 'Replace',
              ( ['in'], c_int, 'symbolID' ),
              ( ['in'], POINTER(ISymbol), 'Symbol' )),
    COMMETHOD([helpstring(u'Removes the symbolID-symbol pair in the collection.')], HRESULT, 'Remove',
              ( ['in'], c_int, 'symbolID' )),
    COMMETHOD([helpstring(u'Removes all the symbolID-symbol pairs in the collection.')], HRESULT, 'RemoveAll'),
]
################################################################
## code template for ISymbolCollection implementation
##class ISymbolCollection_Impl(object):
##    def Reset(self):
##        u'Prepares the collection for Next to be called.'
##        #return 
##
##    def Symbol(self, symbolID, Symbol):
##        u'The symbol associated with the symbolID.'
##        #return 
##
##    def Remove(self, symbolID):
##        u'Removes the symbolID-symbol pair in the collection.'
##        #return 
##
##    def Replace(self, symbolID, Symbol):
##        u'Replaces the symbol associated with the symbolID.'
##        #return 
##
##    def RemoveAll(self):
##        u'Removes all the symbolID-symbol pairs in the collection.'
##        #return 
##
##    def Next(self):
##        u'Returns the next symbolID-symbol pair in the collection.'
##        #return symbolID
##

class esriGDICommentSetTextJustification(Structure):
    _recordinfo_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2, 0L, '{39AC2DEF-2149-4807-AE4C-6DB71BAD7236}')
esriGDICommentSetTextJustification._fields_ = [
    ('dSignature', c_ulong),
    ('nVersion', c_ulong),
    ('dExtraSpacing', c_ulong),
    ('dBreakCharCount', c_ulong),
]
assert sizeof(esriGDICommentSetTextJustification) == 16, sizeof(esriGDICommentSetTextJustification)
assert alignment(esriGDICommentSetTextJustification) == 4, alignment(esriGDICommentSetTextJustification)
class esriGDICommentPlayEnhMetafileBegin(Structure):
    _recordinfo_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2, 0L, '{C6B2E45D-505D-494D-A808-97BD5C2D732B}')
esriGDICommentPlayEnhMetafileBegin._fields_ = [
    ('dSignature', c_ulong),
    ('nVersion', c_ulong),
]
assert sizeof(esriGDICommentPlayEnhMetafileBegin) == 8, sizeof(esriGDICommentPlayEnhMetafileBegin)
assert alignment(esriGDICommentPlayEnhMetafileBegin) == 4, alignment(esriGDICommentPlayEnhMetafileBegin)
class IMarginProperties(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control uniform text margin properties.'
    _iid_ = GUID('{086C95CB-4366-467F-B6A3-6F8A2B693F97}')
    _idlflags_ = ['oleautomation']
IMarginProperties._methods_ = [
    COMMETHOD(['propget', helpstring(u'Value for the margin.')], HRESULT, 'Margin',
              ( ['retval', 'out'], POINTER(c_double), 'Margin' )),
    COMMETHOD(['propput', helpstring(u'Value for the margin.')], HRESULT, 'Margin',
              ( ['in'], c_double, 'Margin' )),
]
################################################################
## code template for IMarginProperties implementation
##class IMarginProperties_Impl(object):
##    def _get(self):
##        u'Value for the margin.'
##        #return Margin
##    def _set(self, Margin):
##        u'Value for the margin.'
##    Margin = property(_get, _set, doc = _set.__doc__)
##

class GeometricEffectEnclosingPolygon(CoClass):
    u'Constructs enclosing polgon. With multipoint input, constructs a polygon that encloses all points.'
    _reg_clsid_ = GUID('{DE3B9FB3-C710-4F43-BC7E-35B5B3ADACB7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
GeometricEffectEnclosingPolygon._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGeometricEffect, IGraphicAttributes, IGraphicAttributes2, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDocumentVersionSupportGEN]

class FontName(CoClass):
    u'The name of the font.'
    _reg_clsid_ = GUID('{B4514956-AD9E-4880-9E94-A783CEE5167D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
FontName._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IFontName]

class ITextParserSupport(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the text parsing support.'
    _iid_ = GUID('{5DEA57CF-A8EF-4944-B731-87DF1B6F136D}')
    _idlflags_ = ['oleautomation']
ITextParserSupport._methods_ = [
    COMMETHOD(['propget', helpstring(u'The text parser.')], HRESULT, 'TextParser',
              ( ['retval', 'out'], POINTER(POINTER(ITextParser)), 'parser' )),
    COMMETHOD(['propputref', helpstring(u'The text parser.')], HRESULT, 'TextParser',
              ( ['in'], POINTER(ITextParser), 'parser' )),
]
################################################################
## code template for ITextParserSupport implementation
##class ITextParserSupport_Impl(object):
##    def TextParser(self, parser):
##        u'The text parser.'
##        #return 
##

IConnectionPoint._methods_ = [
    COMMETHOD([], HRESULT, 'GetConnectionInterface',
              ( ['out'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pIID' )),
    COMMETHOD([], HRESULT, 'GetConnectionPointContainer',
              ( ['out'], POINTER(POINTER(IConnectionPointContainer)), 'ppCPC' )),
    COMMETHOD([], HRESULT, 'Advise',
              ( ['in'], POINTER(IUnknown), 'pUnkSink' ),
              ( ['out'], POINTER(c_ulong), 'pdwCookie' )),
    COMMETHOD([], HRESULT, 'Unadvise',
              ( ['in'], c_ulong, 'dwCookie' )),
    COMMETHOD([], HRESULT, 'EnumConnections',
              ( ['out'], POINTER(POINTER(IEnumConnections)), 'ppEnum' )),
]
################################################################
## code template for IConnectionPoint implementation
##class IConnectionPoint_Impl(object):
##    def GetConnectionPointContainer(self):
##        '-no docstring-'
##        #return ppCPC
##
##    def Advise(self, pUnkSink):
##        '-no docstring-'
##        #return pdwCookie
##
##    def GetConnectionInterface(self):
##        '-no docstring-'
##        #return pIID
##
##    def Unadvise(self, dwCookie):
##        '-no docstring-'
##        #return 
##
##    def EnumConnections(self):
##        '-no docstring-'
##        #return ppEnum
##

class esriGDICommentBeginFeature(Structure):
    _recordinfo_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2, 0L, '{1BFC74B7-15E0-4B8F-ADC0-01AF03EA88A0}')
esriGDICommentBeginFeature._fields_ = [
    ('dSignature', c_ulong),
    ('nVersion', c_ulong),
    ('nDisplayFieldLen', c_ulong),
]
assert sizeof(esriGDICommentBeginFeature) == 12, sizeof(esriGDICommentBeginFeature)
assert alignment(esriGDICommentBeginFeature) == 4, alignment(esriGDICommentBeginFeature)
IMoveGeometryFeedback._methods_ = [
    COMMETHOD([helpstring(u'Starts a move.')], HRESULT, 'Start',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Anchor' )),
    COMMETHOD([helpstring(u'Adds a geometry to be moved.')], HRESULT, 'AddGeometry',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'Geometry' )),
    COMMETHOD([helpstring(u'Clears all the geometries.')], HRESULT, 'ClearGeometry'),
]
################################################################
## code template for IMoveGeometryFeedback implementation
##class IMoveGeometryFeedback_Impl(object):
##    def Start(self, Anchor):
##        u'Starts a move.'
##        #return 
##
##    def AddGeometry(self, Geometry):
##        u'Adds a geometry to be moved.'
##        #return 
##
##    def ClearGeometry(self):
##        u'Clears all the geometries.'
##        #return 
##

ITextParser._methods_ = [
    COMMETHOD(['propget', helpstring(u'The text symbol.')], HRESULT, 'TextSymbol',
              ( ['retval', 'out'], POINTER(POINTER(ITextSymbol)), 'textSym' )),
    COMMETHOD(['propputref', helpstring(u'The text symbol.')], HRESULT, 'TextSymbol',
              ( ['in'], POINTER(ITextSymbol), 'textSym' )),
    COMMETHOD(['propget', helpstring(u'Text to parse.')], HRESULT, 'Text',
              ( ['retval', 'out'], POINTER(BSTR), 'Text' )),
    COMMETHOD(['propput', helpstring(u'Text to parse.')], HRESULT, 'Text',
              ( ['in'], BSTR, 'Text' )),
    COMMETHOD([helpstring(u'Returns true if the text contains tags and false if it does not.')], HRESULT, 'HasTags',
              ( [], POINTER(VARIANT_BOOL), 'HasTags' )),
    COMMETHOD([helpstring(u'Parses the next tag and string and sets the TextSymbol accordingly.')], HRESULT, 'Next'),
    COMMETHOD([helpstring(u'Resets the text string tag sequence to the beginning.')], HRESULT, 'Reset'),
]
################################################################
## code template for ITextParser implementation
##class ITextParser_Impl(object):
##    def Reset(self):
##        u'Resets the text string tag sequence to the beginning.'
##        #return 
##
##    def _get(self):
##        u'Text to parse.'
##        #return Text
##    def _set(self, Text):
##        u'Text to parse.'
##    Text = property(_get, _set, doc = _set.__doc__)
##
##    def Next(self):
##        u'Parses the next tag and string and sets the TextSymbol accordingly.'
##        #return 
##
##    def HasTags(self, HasTags):
##        u'Returns true if the text contains tags and false if it does not.'
##        #return 
##
##    def TextSymbol(self, textSym):
##        u'The text symbol.'
##        #return 
##

IMapLevel._methods_ = [
    COMMETHOD(['propget', helpstring(u'Current map level for drawing multi-level symbols.')], HRESULT, 'MapLevel',
              ( ['retval', 'out'], POINTER(c_int), 'MapLevel' )),
    COMMETHOD(['propput', helpstring(u'Current map level for drawing multi-level symbols.')], HRESULT, 'MapLevel',
              ( ['in'], c_int, 'MapLevel' )),
]
################################################################
## code template for IMapLevel implementation
##class IMapLevel_Impl(object):
##    def _get(self):
##        u'Current map level for drawing multi-level symbols.'
##        #return MapLevel
##    def _set(self, MapLevel):
##        u'Current map level for drawing multi-level symbols.'
##    MapLevel = property(_get, _set, doc = _set.__doc__)
##

ISymbol._methods_ = [
    COMMETHOD([helpstring(u'Prepares the DC for drawing the symbol.')], HRESULT, 'SetupDC',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDC' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ITransformation), 'Transformation' )),
    COMMETHOD([helpstring(u'Restores DC to original state.')], HRESULT, 'ResetDC'),
    COMMETHOD([helpstring(u'Draws the specified shape.')], HRESULT, 'Draw',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'Geometry' )),
    COMMETHOD([helpstring(u'Fills an existing polygon with the boundary of the specified symbol.')], HRESULT, 'QueryBoundary',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDC' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ITransformation), 'displayTransform' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'Geometry' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPolygon), 'boundary' )),
    COMMETHOD(['propget', helpstring(u'Raster operation code for pixel drawing.')], HRESULT, 'ROP2',
              ( ['retval', 'out'], POINTER(esriRasterOpCode), 'DrawMode' )),
    COMMETHOD(['propput', helpstring(u'Raster operation code for pixel drawing.')], HRESULT, 'ROP2',
              ( ['in'], esriRasterOpCode, 'DrawMode' )),
]
################################################################
## code template for ISymbol implementation
##class ISymbol_Impl(object):
##    def Draw(self, Geometry):
##        u'Draws the specified shape.'
##        #return 
##
##    def QueryBoundary(self, hDC, displayTransform, Geometry, boundary):
##        u'Fills an existing polygon with the boundary of the specified symbol.'
##        #return 
##
##    def ResetDC(self):
##        u'Restores DC to original state.'
##        #return 
##
##    def _get(self):
##        u'Raster operation code for pixel drawing.'
##        #return DrawMode
##    def _set(self, DrawMode):
##        u'Raster operation code for pixel drawing.'
##    ROP2 = property(_get, _set, doc = _set.__doc__)
##
##    def SetupDC(self, hDC, Transformation):
##        u'Prepares the DC for drawing the symbol.'
##        #return 
##

IFillPattern._methods_ = [
    COMMETHOD([helpstring(u'Draws the fill pattern.')], HRESULT, 'Draw',
              ( ['in'], POINTER(IOutputContext), 'context' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'Geometry' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'envelope' )),
]
################################################################
## code template for IFillPattern implementation
##class IFillPattern_Impl(object):
##    def Draw(self, context, Geometry, envelope):
##        u'Draws the fill pattern.'
##        #return 
##

IGeometryDraw._methods_ = [
    COMMETHOD([helpstring(u'Draws the geometry.')], HRESULT, 'Draw',
              ( [], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDC' ),
              ( [], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'pGeometry' ),
              ( [], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ITransformation), 'pTransformation' ),
              ( [], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'pVisibleBounds' )),
    COMMETHOD([helpstring(u'Queries the geometry.')], HRESULT, 'QueryGeometryFromWin32Path',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDC' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ITransformation), 'transform' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPolygon), 'Geometry' )),
]
################################################################
## code template for IGeometryDraw implementation
##class IGeometryDraw_Impl(object):
##    def Draw(self, hDC, pGeometry, pTransformation, pVisibleBounds):
##        u'Draws the geometry.'
##        #return 
##
##    def QueryGeometryFromWin32Path(self, hDC, transform, Geometry):
##        u'Queries the geometry.'
##        #return 
##

INewBezierCurveFeedback._methods_ = [
    COMMETHOD([helpstring(u'Begins a normal feedback at the given point.')], HRESULT, 'Start',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
    COMMETHOD([helpstring(u'Creates a node at the given point.')], HRESULT, 'AddPoint',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'Point' )),
    COMMETHOD([helpstring(u'Stops the feedback and returns the shape.')], HRESULT, 'Stop',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPolyline)), 'polyline' )),
    COMMETHOD(['propget', helpstring(u'The constraint on this rubberbander.')], HRESULT, 'Constraint',
              ( ['retval', 'out'], POINTER(esriLineConstraints), 'constrain' )),
    COMMETHOD(['propput', helpstring(u'The constraint on this rubberbander.')], HRESULT, 'Constraint',
              ( ['in'], esriLineConstraints, 'constrain' )),
]
################################################################
## code template for INewBezierCurveFeedback implementation
##class INewBezierCurveFeedback_Impl(object):
##    def Start(self, Point):
##        u'Begins a normal feedback at the given point.'
##        #return 
##
##    def _get(self):
##        u'The constraint on this rubberbander.'
##        #return constrain
##    def _set(self, constrain):
##        u'The constraint on this rubberbander.'
##    Constraint = property(_get, _set, doc = _set.__doc__)
##
##    def Stop(self):
##        u'Stops the feedback and returns the shape.'
##        #return polyline
##
##    def AddPoint(self, Point):
##        u'Creates a node at the given point.'
##        #return 
##

IBasicSymbol._methods_ = [
    COMMETHOD([helpstring(u'Draws the basic symbol.')], HRESULT, 'Draw',
              ( ['in'], POINTER(IOutputContext), 'context' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'Geometry' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'envelope' )),
]
################################################################
## code template for IBasicSymbol implementation
##class IBasicSymbol_Impl(object):
##    def Draw(self, context, Geometry, envelope):
##        u'Draws the basic symbol.'
##        #return 
##

IMarkerPlacement._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if the input geometry type is valid.')], HRESULT, 'AcceptGeometryType',
              ( ['in'], comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.esriGeometryType, 'inputType' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'accept' )),
    COMMETHOD([helpstring(u'Resets the collection of transformations. Must be called before using NextTransformation.')], HRESULT, 'Reset',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry), 'geom' )),
    COMMETHOD([helpstring(u'Hands back the next transformation.')], HRESULT, 'NextTransformation',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IAffineTransformation2D)), 'transfo' )),
]
################################################################
## code template for IMarkerPlacement implementation
##class IMarkerPlacement_Impl(object):
##    def Reset(self, geom):
##        u'Resets the collection of transformations. Must be called before using NextTransformation.'
##        #return 
##
##    @property
##    def AcceptGeometryType(self, inputType):
##        u'Indicates if the input geometry type is valid.'
##        #return accept
##
##    def NextTransformation(self):
##        u'Hands back the next transformation.'
##        #return transfo
##

class TextSymbol(CoClass):
    u'A symbol that controls how text is displayed.'
    _reg_clsid_ = GUID('{B65A3E74-2993-11D1-9A43-0080C7EC5C96}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{59FCCD31-434C-4017-BDEF-DB4B7EDC9CE0}', 10, 2)
TextSymbol._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IFormattedTextSymbol, ISimpleTextSymbol, IMapLevel, ISymbol, ISymbolRotation, IMask, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, IDisplayName, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySupport, ITextParserSupport, IQueryGeometry, IMarginProperties, ITextDrawSupport, IWordBoundaries, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, ICharacterOrientation]

__all__ = ['esriEnvelopeConstraintsSquare', 'esriResampleRatio',
           'IDisplayFilter', 'esriMoveTextConstraintsOnTop',
           'esriTDAngle', 'DimDisplayFilter', 'esriROPMaskPenNot',
           'esriMoveTextConstraints', 'IMovePointFeedback2',
           'GeometricEffectMove', 'esriDrawIgnore3DMaterial',
           'esriClipBasicClipping', 'esriROPXOrPen', 'IRubberBand2',
           'esriSFSHorizontal', 'esriGADonutWidth', 'esriTVACenter',
           'esriLJSMitre', 'IEnumColors', 'IMarkerSymbol',
           'esriGAOffsetCurveMethod', 'ServerStyleGallery',
           'esriGDICommentEndFeature', 'esriGAAlongLineStep',
           'IRasterOutputSettings', 'IDotDensityMasking',
           'esriLineJoinStyle', 'tagCONNECTDATA',
           'REP_E_EMPTY_ENUM_ATTRIBUTE', 'PointTracker',
           'esriDashAttributeTypeFillsAndGaps', 'ITextSymbol',
           'FontSize', 'GeometricEffectSuppress',
           'GraphicAttributeDoubleType', 'esriTHACenter',
           'esriGDICommentBeginMap', 'ISimpleTextSymbol',
           'esriNoScreenCache', 'ILineDecorationElement',
           'IColorRampElements', 'esriRepresentationDrawingError',
           'esriDraw3DTransparent', 'GeometricEffectAddControlPoints',
           'PresetColorRamp', 'ILayerVisible',
           'esriGALinePatternAngle', 'INewBezierCurveFeedback',
           'ITextParserSupport', 'IGraphicAttributeDashType',
           'esriROPBlack', 'BasicMarkerSymbol', 'MoveLineFeedback',
           'esriDynamicDrawPhase',
           'esriGDIComment_Begin_Feature_Attribute',
           'IEnumStyleGalleryItem', 'esriMSNone', 'IDisplay3D',
           'esriCIELabAlgorithm', 'esriTCLowercase',
           'ISimpleMarkerSymbol', 'IScreenDisplay',
           'esriTextDirection', 'ITextMargins',
           'IRepresentationRule2', 'LineFillSymbol', 'IAnchorPoint',
           'IFontAttribute', 'esriDisplayCacheFlags',
           'esriGDIComment_End_Layer', 'INewEllipseFeedback',
           'INewTextBezierCurveFeedback', 'esriPictureSymbolOptions',
           'esriGDICommentSetTextJustification',
           'REP_E_NO_MAP_CONTEXT', 'NewRectangleFeedback',
           'IScreenDisplayZoom', 'esriSFSHollow', 'SimpleLineSymbol',
           'esriGAAtExtremitiesOffset', 'esriGradientFillStyle',
           'GlobalScreenDisplaySettings', 'NewEnvelopeFeedback',
           'IEnumSymbol', 'FontAttributeUnderline',
           'esriTrackerStyle', 'esriGDIComment_Mask_Layer',
           'IScreenDisplay3', 'IReferenceMarkerSymbol',
           'GraphicAttributeIntegerType', 'esriDynamicSymbolType',
           'esriSLSDashDot', 'esriGDICommentSetTextExtra',
           'esriGAOnPointXOffset', 'esriDMDPLayers',
           'esriGAVariableAlongLineZoomNumber',
           'DotDensityFillSymbol', 'esriGAMarker',
           'IStyleGalleryItem3', 'IStyleGalleryItem2',
           'REP_E_INVALID_ENUM_ATTRIBUTE', 'esriHSVAlgorithm',
           'esriMarkerFillStyle', 'GeometricEffectDonut',
           'RandomColorRamp', 'esriGAOffsetTangentOffset',
           'IMoveImageFeedback', 'ICallout',
           'esriGADecorationBeginGap', 'WordTextPath',
           'MarkerPlacementRandomInPolygon', 'IMarkerLineSymbol',
           'esriGDICommentSetCmykColor', 'IEnumConnections', 'IDraw',
           'IHashLineSymbol', 'esriGAJogPosition',
           'IPolygonMovePointFeedback', 'esriROPMaskNotPen',
           'AnchorPoint', 'ServerStyleGalleryItem', 'esriIPictureJPG',
           'esriSMSDiamond', 'NewBezierCurveFeedback',
           'esriTrackerDominant', 'esriGAEnclosingPolygonMethod',
           'PolygonMovePointFeedback', 'esriRasterOutputDraft',
           'esriGAOffsetCurveOffset', 'ISymbolRotation', 'IFontName',
           'ITextParser', 'ITransformEvents', 'IDicerCallback',
           'SymbologyEnvironment', 'esriGAStrokeWidth',
           'TimeDisplayEvents', 'esriGAArrowWidth', 'IStyleGallery',
           'esriScreenCache', 'esriGDICommentBeginGroup',
           'MarkerPlacementOnLine', 'esriSLSNull',
           'esriDisplayCacheNoFlags', 'esriTrackerActive',
           'NewPolygonFeedback', 'esriLCSThreePoint',
           'IMarkerBackground', 'esriGARandomAlongLineControlPoints',
           'esriGARotateAngle', 'IBasicLineSymbol', 'ITextPath2',
           'LocationInterior', 'esriGAOnVerticesEndPoints',
           'GeometricEffectWave', 'IMarkerPlacement',
           'esriTextHorizontalAlignment', 'IDynamicSymbolProperties',
           'esriOutlineWithoutHoles', 'IResizeEnvelopeFeedback2',
           'IMapLevel', 'esriGASolidColorPatternColor',
           'MoveCurvedTextFeedback', 'esriLCSBase',
           'REP_E_OUTPUT_CONTEXT_NOT_INITIALIZED',
           'IDynamicCompoundMarker', 'IDynamicScreenDisplay',
           'esriDynamicSelectionMode', 'IRepresentationGraphics',
           'esriDSymbolFill', 'IStyleImporter',
           'esriMoveTextConstraintsRight', 'esriLCSMidpoint',
           'esriGraphicAttribute', 'esriGAAlongLinePosition',
           'RepresentationGraphics', 'RubberPolygon',
           'IDynamicDrawing', 'esriDisplayCacheRequiresBackground',
           'esriTrackerNormal', 'ITextBackground2',
           'esriPSOVectorize', 'esriGAGradientPatternAngle',
           'esriGDICommentBeginTextEx',
           'esriGDICommentFillWithPattern',
           'esriGAGradientPatternStyle', 'esriDraw3DImmediate',
           'ISymbologyEnvironment', 'IRepresentationMarker',
           'MoveTextAlongShapeFeedback', 'IMoveTextFeedback',
           'esriGARandomAlongLinePosition', 'CancelTracker',
           'esriDynamicGlyphType', 'IBasicFillSymbol',
           'esriDashAttributeTypeOnlyGaps',
           'esriPSORasterizeIfRasterData', 'ITimeDisplay2', 'ISymbol',
           'esriEnvelopeConstraints', 'esriGAInsidePolygonXStep',
           'esriLJSRound', 'esriIPictureEMF', 'esriTrackerLocation',
           'esriGAStrokeColor', 'MonitorSettings',
           'ResizeEnvelopeFeedback', 'GraphicAttributeDashType',
           'esriLCSFourPoint', 'GeometricEffectRadial',
           'esriGAReverse', 'IColorRamp', 'ICartographicLineSymbol',
           'IArrowMarkerSymbol', 'ICalloutTracker',
           'MarkerTextBackground', 'SimpleTextPath',
           'esriGDICommentPlayEnhMetafileEnd', 'esriSFSCross',
           'BezierMovePointFeedback', 'IScreenInvalidate',
           'esriBCSRectangle', 'esriGAOnVerticesControlPoints',
           'esriEnvelopeEdgeTopLeft', 'IStyleGalleryItem',
           'ISymbolCollection2', 'esriOutlineBox',
           'esriGACutCurveInvert', 'esriPSORasterize',
           'IDisplayTransformationAdmin',
           'esriGAGradientPatternInterval', 'esriIPictureType',
           'esriGAMarkerRotateClockwise',
           'REP_E_MAP_CONTEXT_NOT_INITIALIZED',
           'TransparencyDisplayFilter', 'IDynamicDisplay',
           'esriLineCapStyle', 'esriGFSBuffered', 'LineStroke',
           'esriOutlineNoOption', 'esriGAGradientPatternPercent',
           'ITextPath', 'esriGAInsidePolygonYStep', 'NewTextFeedback',
           'MovePolygonFeedback', 'IStyleGalleryStorageAdmin',
           'IDisplayName', 'IMoveCurvedTextFeedback',
           'esriGAOnLineRelativeTo', 'esriClippingMethod',
           'esriGAWaveSeed', 'IPointCollectionTracker',
           'RepresentationRuleItem', 'esriTCAllCaps', 'esriTHARight',
           'esriGATaperedPolygonFromWidth', 'esriDSRAScreen',
           'esriGAMarkerAngle', 'esriUserScaleSnapping',
           'IDotDensityFillSymbol', 'IStyleGalleryStorage',
           'IMovePolygonFeedback', 'esriOutlineOption',
           'esriGAAlongLineControlPoints', 'ReshapeFeedback2',
           'esriGADonutMethod',
           'esriGDIComment_Mask_Layer_Before_Clipping',
           'SimpleTextParser', 'esriGADashPattern', 'HsvColor',
           'ITimeDisplayEvents', 'ITransparencyDisplayFilter',
           'GeometryDraw', 'esriGDICommentBeginPageLayout',
           'SimpleLineDecorationElement', 'IClippingMethod',
           'IMultiLayerLineSymbol', 'IDynamicDisplay2',
           'GraphicAttributeMarkerType', 'esriDDPCompiled',
           'esriDynamicSymbolRotationAlignment',
           'GeometricEffectSmooth', 'esriEnvelopeEdgeBottomMiddle',
           'esriMarkerPlacementAttributes', 'ILineMovePointFeedback',
           'IReferenceLineSymbol', 'esriGACutCurveBegin',
           'esriOrientMode', 'esriGDICommentEndLayer', 'CmykColor',
           'ILineCallout', 'esriGAAlongLineEndings',
           'MarkerPlacementPolygonCenter',
           'IGraphicAttributeEnumType',
           'esriGARandomInsidePolygonClipping',
           'esriGADecorationFlipFirst', 'esriAttributeTypeBoolean',
           'esriAttributeTypeText', 'ISymbolCollection',
           'IDotDensityFillSymbol2', 'BasicFillSymbol', 'FontColor',
           'IGraphicAttributeType', 'esriLCSRound', 'esriDSymbolText',
           'IOrientInteraction', 'IVertexFeedback',
           'esriDraw3DSilent', 'ITimeDisplay',
           'esriGAPolygonCenterYOffset',
           'esriGDIComment_End_PageLayout', 'IOverposterTextPath',
           'IDynamicMapEvents', 'ICharacterOrientation',
           'esriGDIComment_Begin_Map', 'MarkerPlacementOnVertices',
           'esriDraw3DGeography', 'IMoveInteraction', 'IColor',
           'GraphicAttributeTextType', 'MoveTextFeedback',
           'IMoveEnvelopeFeedback', 'ILineProperties',
           'IResizeTextFeedback', 'IDisplayTransformationScales',
           'IPictureSymbolEnvironment', 'esriROPWhite',
           'esriGAMoveXOffset', 'esriTexInterpolNearest',
           'ICmykColor', 'esriGARandomAlongLineRandom',
           'esriScaleSnapping', 'esriEnvelopeConstraintsNone',
           'IOutputRasterSettings', 'esriGASimplifyTolerance',
           'esriTextVerticalAlignment', 'IEditInteraction',
           'IDynamicDrawScreen', 'ICalloutFeedback2',
           'IPictureLineSymbol', 'esriGAVariableAlongLineMinZoom',
           'IDisplayFilterManager', 'esriGATaperedPolygonLength',
           'INewCircleFeedback', 'esriGAScaleYFactor',
           'PictureLineSymbol', 'esriGAOffsetTangentMethod',
           'IRasterPicture', 'IBezierDisplayFeedback',
           'GeometricEffectCut', 'esriStandardScaleSnapping',
           'esriLabLChAlgorithm', 'esriGDIComment_Begin_Feature',
           'esriGARandomInsidePolygonXOffset', 'esriSFSDiagonalCross',
           'INewCircleFeedback2', 'esriROPNOP',
           'IMultiLayerMarkerSymbol', 'SimpleFillSymbol',
           'ModifySegmentFeedback',
           'esriGAVariableAlongLineControlPoints', 'IDisplayAdmin2',
           'esriGAVariableAlongLineOffset', 'esriLCSUnderline',
           'esriGDICommentEndText', 'IlluminationProps',
           'esriOMPerpendicular', 'esriAttributeTypeSize',
           'IStyleGalleryClass', 'NewArcFeedback', 'ILineFillSymbol',
           'esriIPicturePNG', 'esriGASuppressSuppress',
           'esriSFSVertical', 'GeometricEffectBuffer',
           'esriTPSuperscript', 'esriSimpleLineStyle',
           'IEnumConnectionPoints', 'esriTCNormal', 'esriSLSDash',
           'GraphicAttributeEnumType', 'IDynamicGlyphFactory2',
           'MoveEnvelopeFeedback', 'IResizeEnvelopeFeedback',
           'esriGDIComment_FillWithPattern', 'IIlluminationProps',
           'IFillProperties', 'esriSFSSolid',
           'esriGDICommentBeginLayer', 'GradientPattern',
           'ColorRampElements', 'esriAllScreenCaches',
           'MarkerPlacementAlongLine', 'esriMFSGrid',
           'LocationBottomMiddle', 'esriDDPImmediate',
           'MarkerPlacementAtExtremities',
           'esriGDIComment_End_Feature_Attribute', 'SymbolIdentifier',
           'esriGARandomAlongLineStep', 'INewPolygonFeedback',
           'esriGARandomInsidePolygonYOffset',
           'EnumServerStyleGalleryItem',
           'esriGAVariableAlongLineMaxZoom', 'esriGADonutSimple',
           'esriGDIComment_PlayEnhMetafileEnd',
           'IScreenDisplayOverlays', 'IGraphicsOutline',
           'REP_E_GEOMETRY_TYPE_NOT_SUPPORTED', 'esriDSymbolMarker',
           'NewLineFeedback', 'IMultiPartColorRamp',
           'INewRectangleFeedback', 'esriGAJogAngle',
           'IGeometricEffect', 'IMarkerMask',
           'esriGAGradientPatternAlgorithm', 'INewMultiPointFeedback',
           'esriGDIComment_Begin_Layer', 'MultiLayerFillSymbol',
           'esriGDICommentMaskLayerBeforeClipping',
           'esriColorRampAlgorithm', 'MarkerFillSymbol',
           'ISymbolIdentifier', 'GeometricEffectOffset',
           'esriDSMBeforeDynamicDraw',
           'MarkerPlacementRandomAlongLine', 'esriTDHorizontal',
           'IOffsetInteraction', 'IDynamicGlyphFactory',
           'IMultiLayerFillSymbol', 'IStretchLineFeedback',
           'esriOutlineExact', 'LineMovePointFeedback', 'IMapContext',
           'esriGAWaveWidth', 'IResizeInteraction', 'GrayColor',
           'CalloutFeedback', 'IScaleTracker',
           'ISymbologyEnvironment2', 'SolidColorPattern',
           'esriGALinePatternOffset', 'esriIPictureGIF',
           'esriEnvelopeConstraintsAspect', 'MoveGeometryFeedback',
           'esriGAVariableAlongLineStep', 'LocationMiddleRight',
           'IBalloonCallout', 'esriSimpleFillStyle',
           'esriGraphicAttributeType', 'esriROPMergePenNot',
           'NewEllipseFeedback', 'esriGDICommentEndPageLayout',
           'esriDisplayCachePrivate', 'esriEnvelopeEdgeTopMiddle',
           'IAppDisplay', 'Template', 'LocationBottomRight', 'IMask',
           'esriSFSForwardDiagonal', 'esriLCSSquare', 'HlsColor',
           'esriGAPolygonCenterXOffset', 'ILineSymbol',
           'IBasicMarkerSymbol', 'esriGABufferSize',
           'esriSimpleMarkerStyle', 'esriDGlyphText',
           'IQueryGeometry', 'LocationTopLeft',
           'MarkerPlacementVariableAlongLine',
           'esriGARegularPolygonRadius', 'esriTexInterpolBilinear',
           'IDisplay', 'IPieChartSymbol', 'esriGDIComment_End_Map',
           'esriSLSSolid', 'IDynamicGlyph', 'esriGADecorationFlipAll',
           'IFontColor', 'esriGFSRectangular', 'IPictureFillSymbol',
           'IEnumScreenDisplay', 'esriGADecorationAngleToLine',
           'NewMultiPointFeedback', 'CieLabConversion', 'TextSymbol',
           'esriGADashOffsetAtEnd', 'CartographicLineSymbol',
           'IRotateTracker', 'esriLCSCircularCCW', 'IOutputContext',
           'esriGAJogLength', 'esriOutlineOrientedBox',
           'esriLineConstraintsNone', 'IRandomColorRamp',
           'ICieLabConversion', 'IFillPattern',
           'IMoveTextAlongShapeFeedback', 'IReshapeFeedback',
           'esriGARadialAngle', 'IUpdateLegendInfo', 'SimpleDisplay',
           'esriGDIComment_Begin_Group', 'GradientFillSymbol',
           'esriGAInsidePolygonShiftOddRows', 'esriDSMLayers',
           'MarkerPlacementOnPoint', 'IScreenDisplay2', 'MapContext',
           'IPictureMarkerSymbol', 'LinePattern',
           'esriDashAttributeType', 'esriGDICommentFeatureAttribute',
           'esriSLSInsideFrame', 'RotateTextFeedback',
           'IMarginProperties', 'esriTPSubscript', 'esriDGlyphFill',
           'esriAttributeTypeDash', 'IRotateTextFeedback',
           'esriGDICommentBeginFeature', 'IDelayEvents',
           'GeometricEffectReverse', 'esriEnvelopeEdgeMiddleRight',
           'esriROPNotCopyPen', 'IStackedChartSymbol',
           'esriEnvelopeEdgeBottomLeft', 'DisplayTransformation',
           'IMoveLineFeedback', 'esriGADecorationEndGap',
           'esriGAInsidePolygonGridAngle', 'esriTHALeft',
           'ISimpleLineCallout', 'esriBCSOval', 'IWordBoundaries',
           'LocationMiddleLeft', 'IHlsColor',
           'esriGARandomAlongLineSeed', 'IFontsInSymbolsEnvironment',
           'IGeodeticLineFeedback', 'MultiLayerLineSymbol',
           'esriSFSBackwardDiagonal', 'ISymbolArray',
           'esriAttributeTypeDouble', 'esriGALinePatternStep',
           'IConnectionPointContainer', 'GeometricEffectExtension',
           'RubberRectangularPolygon', 'IRepresentationRule',
           'esriGADashPosition', 'FontAttributeBold',
           'esriROPNotXOrPen', 'esriGAInsidePolygonXOffset',
           'esriGAWavePeriod', 'esriTVABaseline',
           'esriGAPolygonCenterClipping', 'ResizeTextFeedback',
           'IFieldOverride', 'esriGAOnVerticesRegularVertices',
           'CharacterMarkerSymbol', 'esriLineConstraints',
           'esriSLSDashDotDot', 'INewTextFeedback', 'ScreenDisplay',
           'esriEnvelopeEdgeBottomRight', 'esriGACutCurveEnd',
           'RepresentationMarker', 'GraphicAttributeAngleType',
           'esriTextPosition', 'IReferenceFillSymbol',
           'GraphicAttributeSizeType', 'esriGDICommentEndGroup',
           'BasicRasterPicture', 'IDisplayFeedback2',
           'esriGAControlPointsTolerance', 'esriDMDPDynamicLayers',
           'IBold', 'VertexFeedback', 'esriGAAlongLineAngleToLine',
           'esriROPNotMergePen', 'StackedChartSymbol',
           'NewTextBezierCurveFeedback', 'SymbolCollection',
           'esriGARandomAlongLineSkewEffect',
           'REP_E_ATTRIBUTE_DOES_NOT_EXIST', 'LineDecoration',
           'esriAttributeTypeMarker',
           'esriGDIComment_Begin_PageLayout', 'IFieldOverrides',
           'esriTPNormal', 'esriGDICommentEndMap',
           'IScreenDisplayOverlaysCallback', 'esriSMSSquare',
           'RubberPoint', 'esriGDIFeatureHyperlink',
           'MarkerPlacementInsidePolygon',
           'GraphicAttributeColorType', 'esriGDIComment_Begin_Text',
           'IRgbColor', 'ArrowMarkerSymbol',
           'IRepresentationRuleInit', 'esriTVABottom',
           'IGeometricEffects', 'esriDraw3DGraphics',
           'MultiLayerMarkerSymbol', 'esriTransformToMap',
           'ILineStroke', 'esriIPictureBitmap', 'OverposterTextPath',
           'esriMSHalo', 'ILayerColorLock', 'esriROPNot',
           'IConnectionPoint', 'PictureMarkerSymbol',
           'esriGAVisibility', 'IFillSymbol', 'esriOMParallel',
           'FontAttributeItalic', 'EnvelopeTracker',
           'MarkerPlacementDecoration', 'IMoveBitmapFeedback',
           'PieChartSymbol', 'IDimDisplayFilter',
           'esriDisplayFilterFlags', 'esriGAMoveYOffset',
           'MoveImageFeedback', 'esriDSRANorth',
           'ModifyCircularArcFeedback', 'esriDMDPSelection',
           'esriDSMDynamicDrawing', 'IMonitorSettings',
           'esriOutlineConvex', 'esriGAMarkerSize', 'IHsvColor',
           'esriGAPolygonCenterMethod',
           'esriGDIComment_Set_Cmyk_Color', 'LocationTopMiddle',
           'esriDraw3DOpaque', 'INewEnvelopeFeedback2',
           'IDisplayTransformation', 'ICartographicMarkerSymbol',
           'IMarkerFillSymbol', 'esriGADashEndings',
           'esriEnvelopeEdgeTopRight', 'LocationNone',
           'GeometricEffectRotate', 'IRotateInteraction',
           'esriGAExtensionLength', 'esriGARegularPolygonEdges',
           'esriGARandomInsidePolygonSeed', 'esriMaskStyle',
           'IGraphicAttributeTypeUsingUnits',
           'IGlobalScreenDisplaySettings', 'esriTrackerFocus',
           'AlgorithmicColorRamp', 'IFontSize',
           'esriGDICommentEndFeatureAttribute', 'GeometricEffectDash',
           'esriGAStrokeCaps', 'IBasicSymbol', 'esriTCSmallCaps',
           'IReshapeFeedback2', 'esriTHAFull', 'SimpleLineCallout',
           'INewArcFeedback', 'esriROPMergePen', 'RubberLine',
           'GroupFeedback', 'GeometricEffectTaperedPolygon',
           'esriGDIComment_End_Text', 'IDisplayEvents', 'IGrayColor',
           'esriROPMergeNotPen', 'IMarkerTextBackground',
           'StretchLineFeedback', 'RubberEnvelope', 'esriGFSLinear',
           'EngineRotateTracker', 'esriTransformSize', 'esriSMSCross',
           'esriGARandomAlongLineOffsetAtEnd', 'BezierTextPath',
           'LocationTopRight', 'IBarChartSymbol', 'esriDSymbolLine',
           'esriEnvelopeEdgeMiddleLeft', 'MarkerLineSymbol',
           'esriGAOnVerticesAngleToLine', 'esriGAOnLineAngleToLine',
           'ISimpleLineSymbol', 'IDynamicCompoundMarker2',
           'ILayerTags', 'esriRasterOutputBest', 'esriDGlyphMarker',
           'OutputContext', 'IGraphicAttributes',
           'esriBCSRoundedRectangle', 'GeometricEffectArrow',
           'esriGFSCircular', 'esriMoveTextConstraintsCursor',
           'MovePointFeedback', 'esriGDIComment_PlayEnhMetafileBegin',
           'PictureFillSymbol', 'esriGAAtExtremitiesType',
           'esriAttributeTypeColor', 'esriGASmoothTolerance',
           'IUnderline', 'esriTextCase',
           'esriGATaperedPolygonToWidth', 'esriRasterOpCode',
           'ColorElements', 'esriAttributeTypeInteger',
           'NewCircleFeedback', 'esriGAAlongLineOffsetAtEnd',
           'esriEnvelopeEdge', 'ISelectionTracker',
           'IPresetColorRamp', 'ISimpleLineDecorationElement',
           'esriArrowMarkerStyle', 'esriTexInterpolMipMap',
           'ISymbol3D', 'esriTransformToDevice', 'esriGAWaveStyle',
           'IMovePointFeedback', 'esriLineCalloutStyle',
           'ISimpleFillSymbol', 'IItalic',
           'esriGARegularPolygonAngle', 'IRepresentationRuleItem',
           'GeometricEffectOffsetTangent', 'GeometricEffectSimplify',
           'IRubberBand', 'ITextBackground', 'ReshapeFeedback',
           'esriGAOffsetCurveOption', 'esriLCSCustom',
           'esriAttributeTypeAngle',
           'esriGDICommentPlayEnhMetafileBegin', 'MoveBitmapFeedback',
           'esriGAArrowType', 'ICharacterMarkerSymbol', 'esriSLSDot',
           'IModifySegmentFeedback', 'IWordTextPath',
           'esriMoveTextConstraintsLeft', 'esriDSMAfterDynamicDraw',
           'ICalloutFeedback', 'esriClipRemoveBoxOutside',
           'ITemplate', 'LineTracker', 'IColorElements',
           'IScreenDisplayBasemap', 'esriGAScaleXFactor',
           'esriROPMaskPen', 'PolygonTracker', 'ILineDecoration',
           'IDisplayFiltersControl', 'esriMFSRandom',
           'esriGDIComments', 'IModifyCircularArcFeedback',
           'IChartSymbol', 'esriDynamicMapDrawPhase',
           'esriTransformPosition', 'IMoveGeometryFeedback',
           'esriDraw3DMode', 'esriGDICommentMaskLayer',
           'esriGAOffsetCurveSimple', 'FontName', 'CalloutTracker',
           'esriDisplayTransformationEnum',
           'esriGAVariableAlongLineMethod',
           'IMarkerBackgroundSupport', 'IPostScriptColor',
           'esriGARandomAlongLineEndings', 'IDisplayFeedback',
           'IFormattedTextSymbol', 'esriSFSNull',
           'esriGALinePatternWidth',
           'esriGDICommentBeginFeatureAttribute', 'esriROPNotMaskPen',
           'esriTVATop', 'esriGAExtensionOrigin',
           'IGradientFillSymbol', 'RubberCircle',
           'GeometricEffectJog', 'esriGAInsidePolygonYOffset',
           'esriGALinePatternColor', 'BarChartSymbol',
           'ISymbolIdentifier2', 'LocationBottomLeft',
           'esriTextureInterpolationMode', 'esriAMSPlain',
           'esriLineConstraintsVertical', 'BasicLineSymbol',
           'esriDGlyphLine', 'esriGeometricEffectAttributes',
           'GeometricEffectEnclosingPolygon', 'IGeometryDraw',
           'esriGDICommentBeginText', 'esriROPCopyPen',
           'IAlgorithmicColorRamp', 'IGraphicAttributes2',
           'IStyleGalleryClass2', 'esriDFExternalCache',
           'esriLJSBevel', 'esriGDIComment_Feature_URL',
           'esriGARadialLength', 'esriGDIComment_End_Group',
           'esriLineConstraintsHorizontal', 'esriTDVertical',
           'MovePointFeedback2', 'esriGAVariableAlongLineSeed',
           'esriGDIComment_End_Feature', 'esriLCSButt',
           'HashLineSymbol', 'esriGDIComment_Set_Text_Extra',
           'RepresentationRule', 'esriGAOffsetCurveCount',
           'esriGAStrokeJoins', 'esriClipRemoveCenterOutside',
           'esriGAGradientPatternColor2',
           'esriGAGradientPatternColor1',
           'GeometricEffectRegularPolygon', 'esriBalloonCalloutStyle',
           'IScreenCacheManager', 'esriRasterOutputNormal',
           'esriGAExtensionDeflection', 'esriClipNoClipping',
           'esriOutlineType', 'esriGDIComment_Set_Text_Justification',
           'GeometricEffectScale', 'SimpleMarkerSymbol',
           'esriSMSCircle', 'esriGAVariableAlongLineEndings',
           'GraphicAttributeBooleanType',
           'esriGDIComment_Feature_Attribute', 'esriGAOnPointYOffset',
           'esriSMSX', 'esriDraw3DSelection',
           'esriGAAtExtremitiesAngleToLine',
           'IDynamicSymbolProperties2', 'ITextDrawSupport',
           'I3DChartSymbol', 'INewLineFeedback', 'LineCallout',
           'IDrawingOutline', 'esriGAOnLinePosition',
           'INewEnvelopeFeedback', 'esriAttributeTypeEnum',
           'esriGAInsidePolygonClipping', 'esriLCSCircularCW',
           'RgbColor', 'IMoveImageFeedback2', 'IDisplayAdmin',
           'esriDSMNone', 'esriGADecorationNumberOfPositions',
           'esriScreenRecording', 'MultiPartColorRamp',
           'BalloonCallout']
from comtypes import _check_version; _check_version('501')

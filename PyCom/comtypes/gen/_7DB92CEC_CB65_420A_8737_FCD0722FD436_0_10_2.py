# -*- coding: mbcs -*-
typelib_path = u'C:\\Program Files (x86)\\ArcGIS\\Engine10.2\\com\\esriOutput.olb'
_lcid = 0 # change this if required
from ctypes import *
import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0
from comtypes import GUID
from ctypes.wintypes import VARIANT_BOOL
from ctypes import HRESULT
from comtypes import helpstring
from comtypes import COMMETHOD
from comtypes import dispid
from comtypes import CoClass
import comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2
import comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2
import comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2
from comtypes import BSTR
from comtypes.automation import VARIANT


class IExportVectorOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Vector Export Options.'
    _iid_ = GUID('{1C16BCAC-81DD-4662-A6AB-810A205FC645}')
    _idlflags_ = ['oleautomation']
IExportVectorOptions._methods_ = [
    COMMETHOD(['propput', helpstring(u'Polygonize (represent as vectors instead of fonts) marker symbols option.')], HRESULT, 'PolygonizeMarkers',
              ( ['in'], VARIANT_BOOL, 'bPolygonizeMarkers' )),
    COMMETHOD(['propget', helpstring(u'Polygonize (represent as vectors instead of fonts) marker symbols option.')], HRESULT, 'PolygonizeMarkers',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bPolygonizeMarkers' )),
    COMMETHOD(['propput', helpstring(u'Maximum number of vertices in feature.')], HRESULT, 'MaxVertexNumber',
              ( ['in'], c_int, 'lMaxVertices' )),
    COMMETHOD(['propget', helpstring(u'Maximum number of vertices in feature.')], HRESULT, 'MaxVertexNumber',
              ( ['retval', 'out'], POINTER(c_int), 'lMaxVertices' )),
]
################################################################
## code template for IExportVectorOptions implementation
##class IExportVectorOptions_Impl(object):
##    def _get(self):
##        u'Polygonize (represent as vectors instead of fonts) marker symbols option.'
##        #return bPolygonizeMarkers
##    def _set(self, bPolygonizeMarkers):
##        u'Polygonize (represent as vectors instead of fonts) marker symbols option.'
##    PolygonizeMarkers = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Maximum number of vertices in feature.'
##        #return lMaxVertices
##    def _set(self, lMaxVertices):
##        u'Maximum number of vertices in feature.'
##    MaxVertexNumber = property(_get, _set, doc = _set.__doc__)
##

class ExportTIFF(CoClass):
    u'Class used to export maps to TIFF (Tagged Image File Format).'
    _reg_clsid_ = GUID('{77C648D5-C2E1-4EC5-8764-9034181F9858}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7DB92CEC-CB65-420A-8737-FCD0722FD436}', 10, 2)
class IExportImage(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Image Export.'
    _iid_ = GUID('{4BF7D12A-5C15-4671-A9E2-11FCE89F0873}')
    _idlflags_ = ['oleautomation']
class IExportTIFF(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the TIFF (Tagged Image File Format) Export.'
    _iid_ = GUID('{B13D58C7-603F-4610-8538-5B501908EE26}')
    _idlflags_ = ['oleautomation']
class IExport(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Export.'
    _iid_ = GUID('{55C11165-0C2D-4E2D-AFEA-10B4186C4364}')
    _idlflags_ = ['oleautomation']
class IWorldFileSettings(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the settings of the World File Exporter.'
    _iid_ = GUID('{27BF29CA-71A8-422A-A66D-FF875A9DE13B}')
    _idlflags_ = ['oleautomation']
class IWorldFileSettings2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the additional settings of the World File Exporter.'
    _iid_ = GUID('{167806FC-6BCB-491E-9FB0-827BAF2C3DEC}')
    _idlflags_ = ['oleautomation']
class ISettingsInRegistry(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control storing/restoring of object settings to/from the registry.'
    _iid_ = GUID('{BB518176-E7E3-420A-9787-AE6E3487EB68}')
    _idlflags_ = ['oleautomation']
ExportTIFF._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IExportImage, IExportTIFF, IExport, IWorldFileSettings, IWorldFileSettings2, ISettingsInRegistry, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

class FontMap(CoClass):
    u'Class used to map a font from a TrueType Font to a resident Adobe Type 1 Font for the PostScript Printer Driver, EPS Export Driver and PDF Export Driver.'
    _reg_clsid_ = GUID('{0710508F-2D9E-11D3-9FC6-00C04F6BC8DD}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7DB92CEC-CB65-420A-8737-FCD0722FD436}', 10, 2)
class IFontMap(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Font Map Object.'
    _iid_ = GUID('{7539E7DC-2D89-11D3-9FC6-00C04F6BC8DD}')
    _idlflags_ = ['oleautomation']
class IFontMap2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Font Map 2 Object.'
    _iid_ = GUID('{E4F70D20-046D-490D-A5E3-066E681AB5B1}')
    _idlflags_ = ['oleautomation']
FontMap._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IFontMap, IFontMap2]

class IFontMapCollection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control a Collection of Font Map Objects.'
    _iid_ = GUID('{7539E7DD-2D89-11D3-9FC6-00C04F6BC8DD}')
    _idlflags_ = ['oleautomation']
IFontMapCollection._methods_ = [
    COMMETHOD(['propget', helpstring(u'The count of the FontMap collection.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'An IFontMap from the FontMap collection.')], HRESULT, 'FontMap',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IFontMap)), 'FontMap' )),
    COMMETHOD([helpstring(u'Add an IFontMap to the FontMap collection.')], HRESULT, 'Add',
              ( ['in'], POINTER(IFontMap), 'FontMap' )),
    COMMETHOD([helpstring(u'Insert an IFontMap into the FontMap collection at position index.')], HRESULT, 'Insert',
              ( ['in'], c_int, 'index' ),
              ( ['in'], POINTER(IFontMap), 'FontMap' )),
    COMMETHOD([helpstring(u'Removes IFontMap at index from the FontMap collection.')], HRESULT, 'Remove',
              ( ['in'], c_int, 'index' )),
    COMMETHOD([helpstring(u'Removes all IFontMaps from the FontMap collection.')], HRESULT, 'RemoveAll'),
]
################################################################
## code template for IFontMapCollection implementation
##class IFontMapCollection_Impl(object):
##    @property
##    def Count(self):
##        u'The count of the FontMap collection.'
##        #return Count
##
##    def Insert(self, index, FontMap):
##        u'Insert an IFontMap into the FontMap collection at position index.'
##        #return 
##
##    @property
##    def FontMap(self, index):
##        u'An IFontMap from the FontMap collection.'
##        #return FontMap
##
##    def Remove(self, index):
##        u'Removes IFontMap at index from the FontMap collection.'
##        #return 
##
##    def RemoveAll(self):
##        u'Removes all IFontMaps from the FontMap collection.'
##        #return 
##
##    def Add(self, FontMap):
##        u'Add an IFontMap to the FontMap collection.'
##        #return 
##

class ExportGIF(CoClass):
    u'Class used to export maps to GIF (Graphics Interchange Format).'
    _reg_clsid_ = GUID('{167D909E-2528-4E5D-B5EE-C2E4B553B224}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7DB92CEC-CB65-420A-8737-FCD0722FD436}', 10, 2)
class IExportGIF(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the GIF (Graphics Interchange Format) Export.'
    _iid_ = GUID('{6C43EC0F-352C-42EF-9BD6-83D37529E3E5}')
    _idlflags_ = ['oleautomation']
ExportGIF._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IExportImage, IExportGIF, IExport, IWorldFileSettings, IWorldFileSettings2, ISettingsInRegistry, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

class Library(object):
    u'Esri Output Object Library 10.2'
    name = u'esriOutput'
    _reg_typelib_ = ('{7DB92CEC-CB65-420A-8737-FCD0722FD436}', 10, 2)

class IPrinterMPage(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members for controlling multipage printing.'
    _iid_ = GUID('{4004040C-A184-4C77-BA78-0475D93A3803}')
    _idlflags_ = ['oleautomation']
IPrinterMPage._methods_ = [
    COMMETHOD([helpstring(u'Begin map document. Document consists of one or more pages.')], HRESULT, 'StartMapDocument'),
    COMMETHOD([helpstring(u'Start new page output.')], HRESULT, 'StartPage',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'PixelBounds' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDcPrinter' ),
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'hDcRet' )),
    COMMETHOD([helpstring(u'Finalize current page output.')], HRESULT, 'EndPage'),
    COMMETHOD([helpstring(u'End map document.')], HRESULT, 'EndMapDocument'),
]
################################################################
## code template for IPrinterMPage implementation
##class IPrinterMPage_Impl(object):
##    def StartPage(self, PixelBounds, hDcPrinter):
##        u'Start new page output.'
##        #return hDcRet
##
##    def StartMapDocument(self):
##        u'Begin map document. Document consists of one or more pages.'
##        #return 
##
##    def EndMapDocument(self):
##        u'End map document.'
##        #return 
##
##    def EndPage(self):
##        u'Finalize current page output.'
##        #return 
##

class IExporterPriority(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Superseded by IExport. Provides access to members that control the Base Exporter Priority.'
    _iid_ = GUID('{10AAE67F-D5AB-4905-A0BF-82636BA2ED02}')
    _idlflags_ = ['oleautomation']
IExporterPriority._methods_ = [
    COMMETHOD(['propget', helpstring(u"Exporter's priority - the order of appearance in the user interface.")], HRESULT, 'Priority',
              ( ['retval', 'out'], POINTER(c_int), 'pPriority' )),
]
################################################################
## code template for IExporterPriority implementation
##class IExporterPriority_Impl(object):
##    @property
##    def Priority(self):
##        u"Exporter's priority - the order of appearance in the user interface."
##        #return pPriority
##


# values for enumeration 'esriPDFExtensionSecurityEncryptionOption'
esriPDFExtensionSecurityEncryptionOptionAllContent = 1
esriPDFExtensionSecurityEncryptionOptionNoMetaData = 2
esriPDFExtensionSecurityEncryptionOptionFileAttachmentOnly = 3
esriPDFExtensionSecurityEncryptionOption = c_int # enum
class IExportVector(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Vector Export.'
    _iid_ = GUID('{D29AA471-3E7C-41EC-B502-9E888A3D4BCB}')
    _idlflags_ = ['oleautomation']
IExportVector._methods_ = [
]
################################################################
## code template for IExportVector implementation
##class IExportVector_Impl(object):

class IPaper(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the default printer page settings.'
    _iid_ = GUID('{387BC1D1-3F54-11D1-885E-0000F87808EE}')
    _idlflags_ = ['oleautomation']
IPaper._methods_ = [
    COMMETHOD(['propget', helpstring(u'The units used by the other properties.')], HRESULT, 'Units',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.esriUnits), 'Units' )),
    COMMETHOD(['propget', helpstring(u'The area of the printer page that can be printed on.')], HRESULT, 'PrintableBounds',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'bounds' )),
    COMMETHOD(['propget', helpstring(u'The printer page orientation (1 = portrait.  2 = landscape).')], HRESULT, 'Orientation',
              ( ['retval', 'out'], POINTER(c_short), 'Orientation' )),
    COMMETHOD(['propput', helpstring(u'The printer page orientation (1 = portrait.  2 = landscape).')], HRESULT, 'Orientation',
              ( ['in'], c_short, 'Orientation' )),
    COMMETHOD(['propget', helpstring(u'Enumerate forms supported by the printer.')], HRESULT, 'Forms',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IEnumNamedID)), 'Forms' )),
    COMMETHOD(['propget', helpstring(u'The Form Name.')], HRESULT, 'FormName',
              ( ['retval', 'out'], POINTER(BSTR), 'FormName' )),
    COMMETHOD(['propget', helpstring(u'The printer page form. Use Win32 DMPAPER_xxx constants.')], HRESULT, 'FormID',
              ( ['retval', 'out'], POINTER(c_short), 'FormID' )),
    COMMETHOD(['propput', helpstring(u'The printer page form. Use Win32 DMPAPER_xxx constants.')], HRESULT, 'FormID',
              ( ['in'], c_short, 'FormID' )),
    COMMETHOD(['propget', helpstring(u'Enumerate trays supported by the printer.')], HRESULT, 'Trays',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IEnumNamedID)), 'Trays' )),
    COMMETHOD(['propget', helpstring(u'The printer tray. Use Win32 DMBIN_xxx constants.')], HRESULT, 'TrayID',
              ( ['retval', 'out'], POINTER(c_short), 'TrayID' )),
    COMMETHOD(['propput', helpstring(u'The printer tray. Use Win32 DMBIN_xxx constants.')], HRESULT, 'TrayID',
              ( ['in'], c_short, 'TrayID' )),
    COMMETHOD(['propget', helpstring(u'The Printer Name.')], HRESULT, 'PrinterName',
              ( ['retval', 'out'], POINTER(BSTR), 'PrinterName' )),
    COMMETHOD(['propput', helpstring(u'The Printer Name.')], HRESULT, 'PrinterName',
              ( ['in'], BSTR, 'PrinterName' )),
    COMMETHOD([helpstring(u'Attach object to specified DEVMODE and DEVNAMES structures. This must be called before using other properties and methods.')], HRESULT, 'Attach',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDevMode' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDevNames' )),
    COMMETHOD([helpstring(u'Returns the size of the printer paper. Units property specifies measurement units.')], HRESULT, 'QueryPaperSize',
              ( ['out'], POINTER(c_double), 'Width' ),
              ( ['out'], POINTER(c_double), 'Height' )),
    COMMETHOD(['propget', helpstring(u'Display the Print Setup Dialog.')], HRESULT, 'PrinterInfo',
              ( ['out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'hDevMode' ),
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'hDevNames' )),
]
################################################################
## code template for IPaper implementation
##class IPaper_Impl(object):
##    def _get(self):
##        u'The printer tray. Use Win32 DMBIN_xxx constants.'
##        #return TrayID
##    def _set(self, TrayID):
##        u'The printer tray. Use Win32 DMBIN_xxx constants.'
##    TrayID = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def PrintableBounds(self):
##        u'The area of the printer page that can be printed on.'
##        #return bounds
##
##    def _get(self):
##        u'The Printer Name.'
##        #return PrinterName
##    def _set(self, PrinterName):
##        u'The Printer Name.'
##    PrinterName = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def PrinterInfo(self):
##        u'Display the Print Setup Dialog.'
##        #return hDevMode, hDevNames
##
##    def _get(self):
##        u'The printer page form. Use Win32 DMPAPER_xxx constants.'
##        #return FormID
##    def _set(self, FormID):
##        u'The printer page form. Use Win32 DMPAPER_xxx constants.'
##    FormID = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Forms(self):
##        u'Enumerate forms supported by the printer.'
##        #return Forms
##
##    def Attach(self, hDevMode, hDevNames):
##        u'Attach object to specified DEVMODE and DEVNAMES structures. This must be called before using other properties and methods.'
##        #return 
##
##    def QueryPaperSize(self):
##        u'Returns the size of the printer paper. Units property specifies measurement units.'
##        #return Width, Height
##
##    def _get(self):
##        u'The printer page orientation (1 = portrait.  2 = landscape).'
##        #return Orientation
##    def _set(self, Orientation):
##        u'The printer page orientation (1 = portrait.  2 = landscape).'
##    Orientation = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Units(self):
##        u'The units used by the other properties.'
##        #return Units
##
##    @property
##    def Trays(self):
##        u'Enumerate trays supported by the printer.'
##        #return Trays
##
##    @property
##    def FormName(self):
##        u'The Form Name.'
##        #return FormName
##

class IExportEMF(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the EMF (Windows Enhanced Metafile) Export.'
    _iid_ = GUID('{94123BCD-EAE7-42A9-9FEF-D09A57B87A0F}')
    _idlflags_ = ['oleautomation']
IExportEMF._methods_ = [
    COMMETHOD(['propget', helpstring(u'Handle to in-memory metafile. Client must call DeleteEnhMetafile in order to release the handle. Subsequent calls to this routine will return 0.')], HRESULT, 'Handle',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'pHandle' )),
    COMMETHOD(['propput', helpstring(u'A description string to embed in the file.')], HRESULT, 'Description',
              ( ['in'], BSTR, 'pDescription' )),
    COMMETHOD(['propget', helpstring(u'A description string to embed in the file.')], HRESULT, 'Description',
              ( ['retval', 'out'], POINTER(BSTR), 'pDescription' )),
]
################################################################
## code template for IExportEMF implementation
##class IExportEMF_Impl(object):
##    @property
##    def Handle(self):
##        u'Handle to in-memory metafile. Client must call DeleteEnhMetafile in order to release the handle. Subsequent calls to this routine will return 0.'
##        #return pHandle
##
##    def _get(self):
##        u'A description string to embed in the file.'
##        #return pDescription
##    def _set(self, pDescription):
##        u'A description string to embed in the file.'
##    Description = property(_get, _set, doc = _set.__doc__)
##

class IColorCorrection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Color Correction.'
    _iid_ = GUID('{80B77A31-4DB6-11D3-B654-0080C8EA4FD5}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriColorCorrectionDataType'
esriColorCorrectionDataTypeTotal = 1
esriColorCorrectionDataTypeRaster = 2
esriColorCorrectionDataTypeVector = 4
esriColorCorrectionDataType = c_int # enum

# values for enumeration 'esriCMYKIndex'
esriCMYKIndexCyan = 0
esriCMYKIndexMagenta = 1
esriCMYKIndexYellow = 2
esriCMYKIndexBlack = 3
esriCMYKIndex = c_int # enum
IColorCorrection._methods_ = [
    COMMETHOD(['propget', helpstring(u'The dataType supported: 1 Total, 2 Raster, 4 Vector.')], HRESULT, 'SupportedColorCorrections',
              ( ['retval', 'out'], POINTER(c_short), 'val' )),
    COMMETHOD(['propget', helpstring(u'The Lightness Value of the HLS Color Model.')], HRESULT, 'Lightness',
              ( ['in'], esriColorCorrectionDataType, 'dataType' ),
              ( ['retval', 'out'], POINTER(c_short), 'val' )),
    COMMETHOD(['propput', helpstring(u'The Lightness Value of the HLS Color Model.')], HRESULT, 'Lightness',
              ( ['in'], esriColorCorrectionDataType, 'dataType' ),
              ( ['in'], c_short, 'val' )),
    COMMETHOD(['propget', helpstring(u'The Saturation Value of the HLS Color Model.')], HRESULT, 'Saturation',
              ( ['in'], esriColorCorrectionDataType, 'dataType' ),
              ( ['retval', 'out'], POINTER(c_short), 'val' )),
    COMMETHOD(['propput', helpstring(u'The Saturation Value of the HLS Color Model.')], HRESULT, 'Saturation',
              ( ['in'], esriColorCorrectionDataType, 'dataType' ),
              ( ['in'], c_short, 'val' )),
    COMMETHOD(['propget', helpstring(u'The Undercolor Removal Value.')], HRESULT, 'UnderColorRemoval',
              ( ['in'], esriColorCorrectionDataType, 'dataType' ),
              ( ['retval', 'out'], POINTER(c_short), 'val' )),
    COMMETHOD(['propput', helpstring(u'The Undercolor Removal Value.')], HRESULT, 'UnderColorRemoval',
              ( ['in'], esriColorCorrectionDataType, 'dataType' ),
              ( ['in'], c_short, 'val' )),
    COMMETHOD(['propget', helpstring(u'The Color Correction for the CMYK color model.')], HRESULT, 'CMYKCorrection',
              ( ['in'], esriColorCorrectionDataType, 'dataType' ),
              ( ['in'], esriCMYKIndex, 'index' ),
              ( ['retval', 'out'], POINTER(c_short), 'val' )),
    COMMETHOD(['propput', helpstring(u'The Color Correction for the CMYK color model.')], HRESULT, 'CMYKCorrection',
              ( ['in'], esriColorCorrectionDataType, 'dataType' ),
              ( ['in'], esriCMYKIndex, 'index' ),
              ( ['in'], c_short, 'val' )),
]
################################################################
## code template for IColorCorrection implementation
##class IColorCorrection_Impl(object):
##    def _get(self, dataType):
##        u'The Undercolor Removal Value.'
##        #return val
##    def _set(self, dataType, val):
##        u'The Undercolor Removal Value.'
##    UnderColorRemoval = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self, dataType):
##        u'The Saturation Value of the HLS Color Model.'
##        #return val
##    def _set(self, dataType, val):
##        u'The Saturation Value of the HLS Color Model.'
##    Saturation = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self, dataType):
##        u'The Lightness Value of the HLS Color Model.'
##        #return val
##    def _set(self, dataType, val):
##        u'The Lightness Value of the HLS Color Model.'
##    Lightness = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self, dataType, index):
##        u'The Color Correction for the CMYK color model.'
##        #return val
##    def _set(self, dataType, index, val):
##        u'The Color Correction for the CMYK color model.'
##    CMYKCorrection = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def SupportedColorCorrections(self):
##        u'The dataType supported: 1 Total, 2 Raster, 4 Vector.'
##        #return val
##

class Paper(CoClass):
    u'The default printer page settings.'
    _reg_clsid_ = GUID('{E28C4E63-3F55-11D1-885E-0000F87808EE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7DB92CEC-CB65-420A-8737-FCD0722FD436}', 10, 2)
class IPaper2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the default printer page settings.'
    _iid_ = GUID('{6A319332-D3E2-413A-97F4-F25CE438FEDA}')
    _idlflags_ = ['oleautomation']
Paper._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IPaper, IPaper2, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

class PrintAndExportPageOptions(CoClass):
    u'Print and Export Page Options.'
    _reg_clsid_ = GUID('{36673B39-2ECF-4BB9-8304-98F58D829054}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7DB92CEC-CB65-420A-8737-FCD0722FD436}', 10, 2)
class IPrintAndExportPageOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to multiple page settings for printing and export.'
    _iid_ = GUID('{1F685F17-704A-4755-834F-4C0D67303A2F}')
    _idlflags_ = ['oleautomation']
PrintAndExportPageOptions._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IPrintAndExportPageOptions]

class EmfPrinter(CoClass):
    u'Class used to print maps with the EMF (Windows Enhanced Metafile) Printer Driver.'
    _reg_clsid_ = GUID('{AE064D01-D6CE-11D0-867A-0000F8751720}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7DB92CEC-CB65-420A-8737-FCD0722FD436}', 10, 2)
class IEmfPrinter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Indicator interface that identifies the EMF (Windows Enhanced Metafile) Printer Driver.'
    _iid_ = GUID('{DE6DCD81-3F54-11D1-885E-0000F87808EE}')
    _idlflags_ = ['oleautomation']
class IPrinter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Printer Driver.'
    _iid_ = GUID('{2AB49820-9406-11D0-87EF-080009EC732A}')
    _idlflags_ = ['oleautomation']
class IOutputCleanup(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u"Superseded by IExport. Provides access to members that control the object's cleanup process (removing temporary files, memory release, etc.)."
    _iid_ = GUID('{2B8765EC-8808-474C-8FD3-869D08DF20F6}')
    _idlflags_ = ['oleautomation']
class ITrackCancelSetup(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that set up the Track Cancel.'
    _iid_ = GUID('{5E091C46-D015-471F-8187-F774C7AD9D48}')
    _idlflags_ = ['oleautomation']
EmfPrinter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IEmfPrinter, IPrinter, IPrinterMPage, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo, IOutputCleanup, ITrackCancelSetup]


# values for enumeration 'esriExportPSImage'
esriExportPSImagePositive = 0
esriExportPSImageNegative = 1
esriExportPSImage = c_int # enum
class IPsPrinter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Indicator interface that identifies the PostScript Printer Driver.'
    _iid_ = GUID('{DE6DCD82-3F54-11D1-885E-0000F87808EE}')
    _idlflags_ = ['oleautomation']
IPsPrinter._methods_ = [
    COMMETHOD(['propput', helpstring(u'The PPD file for the PostScript file.')], HRESULT, 'PPDFile',
              ( ['in'], BSTR, 'PPDFile' )),
    COMMETHOD(['propget', helpstring(u'The PPD file for the PostScript file.')], HRESULT, 'PPDFile',
              ( ['retval', 'out'], POINTER(BSTR), 'PPDFile' )),
]
################################################################
## code template for IPsPrinter implementation
##class IPsPrinter_Impl(object):
##    def _get(self):
##        u'The PPD file for the PostScript file.'
##        #return PPDFile
##    def _set(self, PPDFile):
##        u'The PPD file for the PostScript file.'
##    PPDFile = property(_get, _set, doc = _set.__doc__)
##


# values for enumeration 'esriExportColorspace'
esriExportColorspaceRGB = 0
esriExportColorspaceCMYK = 1
esriExportColorspace = c_int # enum
class IExportPS(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the PS (PostScript) and EPS (Encapsulated PostScript) Exports.'
    _iid_ = GUID('{EFCD8D47-8D2A-47A4-B35B-15CA74BCE73C}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriExportPSEmulsion'
esriExportPSEmulsionUp = 0
esriExportPSEmulsionDown = 1
esriExportPSEmulsion = c_int # enum

# values for enumeration 'esriExportPSLanguageLevel'
esriExportPSLevel2 = 2
esriExportPSLevel3 = 3
esriExportPSLanguageLevel = c_int # enum

# values for enumeration 'esriExportImageCompression'
esriExportImageCompressionNone = 0
esriExportImageCompressionRLE = 1
esriExportImageCompressionDeflate = 2
esriExportImageCompressionLZW = 3
esriExportImageCompressionJPEG = 4
esriExportImageCompressionAdaptive = -2147483648
esriExportImageCompression = c_int # enum
IExportPS._methods_ = [
    COMMETHOD(['propput', helpstring(u'The Emulsion setting for the PostScript.')], HRESULT, 'Emulsion',
              ( ['in'], esriExportPSEmulsion, 'Emulsion' )),
    COMMETHOD(['propget', helpstring(u'The Emulsion setting for the PostScript.')], HRESULT, 'Emulsion',
              ( ['retval', 'out'], POINTER(esriExportPSEmulsion), 'Emulsion' )),
    COMMETHOD(['propput', helpstring(u'The Image setting for the PostScript.')], HRESULT, 'Image',
              ( ['in'], esriExportPSImage, 'Image' )),
    COMMETHOD(['propget', helpstring(u'The Image setting for the PostScript.')], HRESULT, 'Image',
              ( ['retval', 'out'], POINTER(esriExportPSImage), 'Image' )),
    COMMETHOD(['propput', helpstring(u'The PostScript Language Level.')], HRESULT, 'LanguageLevel',
              ( ['in'], esriExportPSLanguageLevel, 'pslevel' )),
    COMMETHOD(['propget', helpstring(u'The PostScript Language Level.')], HRESULT, 'LanguageLevel',
              ( ['retval', 'out'], POINTER(esriExportPSLanguageLevel), 'pslevel' )),
    COMMETHOD(['propput', helpstring(u'The PostScript Image Compression.')], HRESULT, 'ImageCompression',
              ( ['in'], esriExportImageCompression, 'compression' )),
    COMMETHOD(['propget', helpstring(u'The PostScript Image Compression.')], HRESULT, 'ImageCompression',
              ( ['retval', 'out'], POINTER(esriExportImageCompression), 'compression' )),
    COMMETHOD(['propput', helpstring(u'The Embed Fonts option.')], HRESULT, 'EmbedFonts',
              ( ['in'], VARIANT_BOOL, 'EmbedFonts' )),
    COMMETHOD(['propget', helpstring(u'The Embed Fonts option.')], HRESULT, 'EmbedFonts',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'EmbedFonts' )),
]
################################################################
## code template for IExportPS implementation
##class IExportPS_Impl(object):
##    def _get(self):
##        u'The Embed Fonts option.'
##        #return EmbedFonts
##    def _set(self, EmbedFonts):
##        u'The Embed Fonts option.'
##    EmbedFonts = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The Image setting for the PostScript.'
##        #return Image
##    def _set(self, Image):
##        u'The Image setting for the PostScript.'
##    Image = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The PostScript Language Level.'
##        #return pslevel
##    def _set(self, pslevel):
##        u'The PostScript Language Level.'
##    LanguageLevel = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The Emulsion setting for the PostScript.'
##        #return Emulsion
##    def _set(self, Emulsion):
##        u'The Emulsion setting for the PostScript.'
##    Emulsion = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The PostScript Image Compression.'
##        #return compression
##    def _set(self, compression):
##        u'The PostScript Image Compression.'
##    ImageCompression = property(_get, _set, doc = _set.__doc__)
##

class IPDFExporter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Superseded by IExportPDF. Provides access to the indicator interface that identifies the PDF (Portable Document Format) Exporter.'
    _iid_ = GUID('{76712D91-28CB-11D3-B616-0080C8EA4FD5}')
    _idlflags_ = ['oleautomation']
IPDFExporter._methods_ = [
]
################################################################
## code template for IPDFExporter implementation
##class IPDFExporter_Impl(object):

class ISpotPlateCollection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Collection of Spot Plates.'
    _iid_ = GUID('{F480E790-2B0F-11D3-9FC3-00C04F6BC8DD}')
    _idlflags_ = ['oleautomation']
class ISpotPlate(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Spot Color Plate.'
    _iid_ = GUID('{481614E4-9407-11D1-9127-0000F87808EE}')
    _idlflags_ = ['oleautomation']
ISpotPlateCollection._methods_ = [
    COMMETHOD(['propget', helpstring(u'The count of the Spot Plate collection.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'An ISpotPlate from the Spot Plate collection.')], HRESULT, 'SpotPlate',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(ISpotPlate)), 'SpotPlate' )),
    COMMETHOD([helpstring(u'Add an ISpotPlate to the Spot Plate collection.')], HRESULT, 'Add',
              ( ['in'], POINTER(ISpotPlate), 'SpotPlate' )),
    COMMETHOD([helpstring(u'Insert an ISpotPlate into the Spot Plate collection at position index.')], HRESULT, 'Insert',
              ( ['in'], c_int, 'index' ),
              ( ['in'], POINTER(ISpotPlate), 'SpotPlate' )),
    COMMETHOD([helpstring(u'Remove ISpotPlate at index from the Spot Plate collection.')], HRESULT, 'Remove',
              ( ['in'], c_int, 'index' )),
    COMMETHOD([helpstring(u'Remove all ISpotPlates from the Spot Plate collection.')], HRESULT, 'RemoveAll'),
]
################################################################
## code template for ISpotPlateCollection implementation
##class ISpotPlateCollection_Impl(object):
##    @property
##    def Count(self):
##        u'The count of the Spot Plate collection.'
##        #return Count
##
##    def Insert(self, index, SpotPlate):
##        u'Insert an ISpotPlate into the Spot Plate collection at position index.'
##        #return 
##
##    @property
##    def SpotPlate(self, index):
##        u'An ISpotPlate from the Spot Plate collection.'
##        #return SpotPlate
##
##    def Remove(self, index):
##        u'Remove ISpotPlate at index from the Spot Plate collection.'
##        #return 
##
##    def RemoveAll(self):
##        u'Remove all ISpotPlates from the Spot Plate collection.'
##        #return 
##
##    def Add(self, SpotPlate):
##        u'Add an ISpotPlate to the Spot Plate collection.'
##        #return 
##

class IExportBMP(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the BMP (Windows Bitmap) Export.'
    _iid_ = GUID('{759BE840-8EB9-45A0-B511-2A297096344B}')
    _idlflags_ = ['oleautomation']
IExportBMP._methods_ = [
    COMMETHOD(['propget', helpstring(u'The Windows Bitmap handle.')], HRESULT, 'Bitmap',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'phBmp' )),
    COMMETHOD(['propget', helpstring(u'The Windows Bitmap color palette.')], HRESULT, 'Palette',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'phPal' )),
    COMMETHOD(['propput', helpstring(u'The Windows Bitmap compression scheme for 8 bits per pixel and 4 bits per pixel.')], HRESULT, 'RLECompression',
              ( ['in'], VARIANT_BOOL, 'compression' )),
    COMMETHOD(['propget', helpstring(u'The Windows Bitmap compression scheme for 8 bits per pixel and 4 bits per pixel.')], HRESULT, 'RLECompression',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'compression' )),
    COMMETHOD(['propput', helpstring(u'The Threshold value for BiLevel images. The Threshold value will be used if esriExportImageType is equal to esriExportImageTypeBiLevelThreshold.')], HRESULT, 'BiLevelThreshold',
              ( ['in'], c_int, 'threshold' )),
    COMMETHOD(['propget', helpstring(u'The Threshold value for BiLevel images. The Threshold value will be used if esriExportImageType is equal to esriExportImageTypeBiLevelThreshold.')], HRESULT, 'BiLevelThreshold',
              ( ['retval', 'out'], POINTER(c_int), 'threshold' )),
]
################################################################
## code template for IExportBMP implementation
##class IExportBMP_Impl(object):
##    def _get(self):
##        u'The Threshold value for BiLevel images. The Threshold value will be used if esriExportImageType is equal to esriExportImageTypeBiLevelThreshold.'
##        #return threshold
##    def _set(self, threshold):
##        u'The Threshold value for BiLevel images. The Threshold value will be used if esriExportImageType is equal to esriExportImageTypeBiLevelThreshold.'
##    BiLevelThreshold = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Palette(self):
##        u'The Windows Bitmap color palette.'
##        #return phPal
##
##    def _get(self):
##        u'The Windows Bitmap compression scheme for 8 bits per pixel and 4 bits per pixel.'
##        #return compression
##    def _set(self, compression):
##        u'The Windows Bitmap compression scheme for 8 bits per pixel and 4 bits per pixel.'
##    RLECompression = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Bitmap(self):
##        u'The Windows Bitmap handle.'
##        #return phBmp
##

class IExportPNG(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the PNG (Portable Network Graphics) Export.'
    _iid_ = GUID('{3B12AC60-9D1A-45C8-BDE5-A2B4CDCED76F}')
    _idlflags_ = ['oleautomation']
IExportPNG._methods_ = [
    COMMETHOD(['propput', helpstring(u'The interlaced PNG export mode.')], HRESULT, 'InterlaceMode',
              ( ['in'], VARIANT_BOOL, 'interlace' )),
    COMMETHOD(['propget', helpstring(u'The interlaced PNG export mode.')], HRESULT, 'InterlaceMode',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'interlace' )),
    COMMETHOD(['propput', helpstring(u'The color that is marked as transparent in the export image.')], HRESULT, 'TransparentColor',
              ( ['in'], POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IColor), 'Color' )),
    COMMETHOD(['propget', helpstring(u'The color that is marked as transparent in the export image.')], HRESULT, 'TransparentColor',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IColor)), 'Color' )),
    COMMETHOD(['propput', helpstring(u'The Threshold value for BiLevel images. The Threshold value will be used if esriExportImageType equal to esriExportImageTypeBiLevelThreshold.')], HRESULT, 'BiLevelThreshold',
              ( ['in'], c_int, 'threshold' )),
    COMMETHOD(['propget', helpstring(u'The Threshold value for BiLevel images. The Threshold value will be used if esriExportImageType equal to esriExportImageTypeBiLevelThreshold.')], HRESULT, 'BiLevelThreshold',
              ( ['retval', 'out'], POINTER(c_int), 'threshold' )),
]
################################################################
## code template for IExportPNG implementation
##class IExportPNG_Impl(object):
##    def _get(self):
##        u'The Threshold value for BiLevel images. The Threshold value will be used if esriExportImageType equal to esriExportImageTypeBiLevelThreshold.'
##        #return threshold
##    def _set(self, threshold):
##        u'The Threshold value for BiLevel images. The Threshold value will be used if esriExportImageType equal to esriExportImageTypeBiLevelThreshold.'
##    BiLevelThreshold = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The color that is marked as transparent in the export image.'
##        #return Color
##    def _set(self, Color):
##        u'The color that is marked as transparent in the export image.'
##    TransparentColor = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The interlaced PNG export mode.'
##        #return interlace
##    def _set(self, interlace):
##        u'The interlaced PNG export mode.'
##    InterlaceMode = property(_get, _set, doc = _set.__doc__)
##

class PsPrinter(CoClass):
    u'Class used to print maps with the PostScript Printer Driver.'
    _reg_clsid_ = GUID('{E28C4E61-3F55-11D1-885E-0000F87808EE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7DB92CEC-CB65-420A-8737-FCD0722FD436}', 10, 2)
class IPSDriver(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the PostScript Driver.'
    _iid_ = GUID('{CD754684-A222-11D0-A68F-080009D57B9A}')
    _idlflags_ = ['oleautomation']
class IPSDriver2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the other options of the PostScript Driver.'
    _iid_ = GUID('{25164BC3-56DA-4AF1-A195-1506ECFEC53C}')
    _idlflags_ = ['oleautomation']
class IFontMapEnvironment(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Font Mapping Environment.'
    _iid_ = GUID('{9ECB85B2-6CAA-11D3-B685-0080C8EA4FD5}')
    _idlflags_ = ['oleautomation']
PsPrinter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IPsPrinter, IPrinter, IPrinterMPage, IPSDriver, IPSDriver2, ISpotPlateCollection, IColorCorrection, IFontMapEnvironment, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo, IOutputCleanup, ITrackCancelSetup]

class IEmfExporter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Superseded by IExportEMF. Provides access to members that control the EMF (Windows Enhanced Metafile) Exporter.'
    _iid_ = GUID('{7D4881E3-57C6-11D1-945E-080009EEBECB}')
    _idlflags_ = ['oleautomation']
IEmfExporter._methods_ = [
    COMMETHOD(['propput', helpstring(u'Indicates if the metafile will be written to memory.')], HRESULT, 'IsInMemory',
              ( ['in'], VARIANT_BOOL, 'pIsInMemory' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the metafile will be written to memory.')], HRESULT, 'IsInMemory',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pIsInMemory' )),
    COMMETHOD(['propget', helpstring(u'Handle to in-memory metafile. Valid only after ReleaseDC has been called.')], HRESULT, 'HENHMETAFILE',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'pHandle' )),
    COMMETHOD([helpstring(u'Returns the handle to the in-memory metafile. Valid only after ReleaseDC has been called. Ownership of the handle is transferred to the client who must call DeleteEnhMetafile on the returned handle. Subsequent calls to this routine will return 0.')], HRESULT, 'TakeHENHMETAFILE',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'pHandle' )),
    COMMETHOD(['propput', helpstring(u'A description string to embed in the file.')], HRESULT, 'Description',
              ( ['in'], BSTR, 'pDescription' )),
    COMMETHOD(['propget', helpstring(u'A description string to embed in the file.')], HRESULT, 'Description',
              ( ['retval', 'out'], POINTER(BSTR), 'pDescription' )),
]
################################################################
## code template for IEmfExporter implementation
##class IEmfExporter_Impl(object):
##    def _get(self):
##        u'Indicates if the metafile will be written to memory.'
##        #return pIsInMemory
##    def _set(self, pIsInMemory):
##        u'Indicates if the metafile will be written to memory.'
##    IsInMemory = property(_get, _set, doc = _set.__doc__)
##
##    def TakeHENHMETAFILE(self):
##        u'Returns the handle to the in-memory metafile. Valid only after ReleaseDC has been called. Ownership of the handle is transferred to the client who must call DeleteEnhMetafile on the returned handle. Subsequent calls to this routine will return 0.'
##        #return pHandle
##
##    @property
##    def HENHMETAFILE(self):
##        u'Handle to in-memory metafile. Valid only after ReleaseDC has been called.'
##        #return pHandle
##
##    def _get(self):
##        u'A description string to embed in the file.'
##        #return pDescription
##    def _set(self, pDescription):
##        u'A description string to embed in the file.'
##    Description = property(_get, _set, doc = _set.__doc__)
##


# values for enumeration 'esriAIDriverOptions'
esriAIMapFonts = 1
esriAIPolygonizeMarkers = 2
esriAIDriverOptions = c_int # enum

# values for enumeration 'esriOutputSelection'
esriOutputAll = 0
esriOutputSelected = 1
esriOutputCurrent = 2
esriOutputRange = 3
esriOutputWhereClause = 4
esriOutputSelection = c_int # enum
IExport._methods_ = [
    COMMETHOD(['propget', helpstring(u'The Name of the Exporter.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'Filter String used in the CFileDialog class.')], HRESULT, 'Filter',
              ( ['retval', 'out'], POINTER(BSTR), 'Filter' )),
    COMMETHOD(['propget', helpstring(u"Exporter's priority - the order of appearance in the user interface.")], HRESULT, 'Priority',
              ( ['retval', 'out'], POINTER(c_int), 'pPriority' )),
    COMMETHOD(['propputref', helpstring(u'Export will update a Progress Bar if StepProgressor is not NULL.')], HRESULT, 'StepProgressor',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStepProgressor), 'rhs' )),
    COMMETHOD(['propputref', helpstring(u'Export will react on Cancel if TrackCancel is not NULL.')], HRESULT, 'TrackCancel',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'rhs' )),
    COMMETHOD(['propput', helpstring(u'The Export Bounds in Pixels (The Pixel Bounds of the Export surface).')], HRESULT, 'PixelBounds',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'PixelBounds' )),
    COMMETHOD(['propget', helpstring(u'The Export Bounds in Pixels (The Pixel Bounds of the Export surface).')], HRESULT, 'PixelBounds',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'PixelBounds' )),
    COMMETHOD(['propput', helpstring(u'The Export File Name.')], HRESULT, 'ExportFileName',
              ( ['in'], BSTR, 'fileName' )),
    COMMETHOD(['propget', helpstring(u'The Export File Name.')], HRESULT, 'ExportFileName',
              ( ['retval', 'out'], POINTER(BSTR), 'fileName' )),
    COMMETHOD(['propput', helpstring(u'The Export Resolution.')], HRESULT, 'Resolution',
              ( ['in'], c_double, 'res' )),
    COMMETHOD(['propget', helpstring(u'The Export Resolution.')], HRESULT, 'Resolution',
              ( ['retval', 'out'], POINTER(c_double), 'res' )),
    COMMETHOD([helpstring(u'Initializes the Exporter.')], HRESULT, 'StartExporting',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'hDC' )),
    COMMETHOD([helpstring(u'Shuts down the Exporter.')], HRESULT, 'FinishExporting'),
    COMMETHOD([helpstring(u'Cleanup should clean all temporary files, free used memory, etc...')], HRESULT, 'Cleanup'),
]
################################################################
## code template for IExport implementation
##class IExport_Impl(object):
##    def TrackCancel(self, rhs):
##        u'Export will react on Cancel if TrackCancel is not NULL.'
##        #return 
##
##    @property
##    def Priority(self):
##        u"Exporter's priority - the order of appearance in the user interface."
##        #return pPriority
##
##    @property
##    def Name(self):
##        u'The Name of the Exporter.'
##        #return Name
##
##    def _get(self):
##        u'The Export Bounds in Pixels (The Pixel Bounds of the Export surface).'
##        #return PixelBounds
##    def _set(self, PixelBounds):
##        u'The Export Bounds in Pixels (The Pixel Bounds of the Export surface).'
##    PixelBounds = property(_get, _set, doc = _set.__doc__)
##
##    def StartExporting(self):
##        u'Initializes the Exporter.'
##        #return hDC
##
##    def FinishExporting(self):
##        u'Shuts down the Exporter.'
##        #return 
##
##    @property
##    def Filter(self):
##        u'Filter String used in the CFileDialog class.'
##        #return Filter
##
##    def Cleanup(self):
##        u'Cleanup should clean all temporary files, free used memory, etc...'
##        #return 
##
##    def StepProgressor(self, rhs):
##        u'Export will update a Progress Bar if StepProgressor is not NULL.'
##        #return 
##
##    def _get(self):
##        u'The Export Resolution.'
##        #return res
##    def _set(self, res):
##        u'The Export Resolution.'
##    Resolution = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The Export File Name.'
##        #return fileName
##    def _set(self, fileName):
##        u'The Export File Name.'
##    ExportFileName = property(_get, _set, doc = _set.__doc__)
##

class IExportPDF3(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides extended access to members that control the PDF (Portable Document Format) export.'
    _iid_ = GUID('{083BC81C-E835-4103-AAD6-454AA037966B}')
    _idlflags_ = ['oleautomation']
IExportPDF3._methods_ = [
    COMMETHOD(['propput', helpstring(u'Specifies the raster image quality setting, when JPEG compression is used.')], HRESULT, 'JPEGCompressionQuality',
              ( ['in'], c_short, 'pImageQuality' )),
    COMMETHOD(['propget', helpstring(u'Specifies the raster image quality setting, when JPEG compression is used.')], HRESULT, 'JPEGCompressionQuality',
              ( ['retval', 'out'], POINTER(c_short), 'pImageQuality' )),
]
################################################################
## code template for IExportPDF3 implementation
##class IExportPDF3_Impl(object):
##    def _get(self):
##        u'Specifies the raster image quality setting, when JPEG compression is used.'
##        #return pImageQuality
##    def _set(self, pImageQuality):
##        u'Specifies the raster image quality setting, when JPEG compression is used.'
##    JPEGCompressionQuality = property(_get, _set, doc = _set.__doc__)
##

class IExportPDF(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the PDF (Portable Document Format) Export.'
    _iid_ = GUID('{6A2A0820-E1B6-4EB0-AF9B-6449DAE7A952}')
    _idlflags_ = ['oleautomation']
IExportPDF._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if the PDF should be compressed.')], HRESULT, 'Compressed',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Compressed' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the PDF should be compressed.')], HRESULT, 'Compressed',
              ( ['in'], VARIANT_BOOL, 'Compressed' )),
    COMMETHOD(['propput', helpstring(u'The PDF Image Compression.')], HRESULT, 'ImageCompression',
              ( ['in'], esriExportImageCompression, 'compression' )),
    COMMETHOD(['propget', helpstring(u'The PDF Image Compression.')], HRESULT, 'ImageCompression',
              ( ['retval', 'out'], POINTER(esriExportImageCompression), 'compression' )),
    COMMETHOD(['propput', helpstring(u'The Embed Fonts option.')], HRESULT, 'EmbedFonts',
              ( ['in'], VARIANT_BOOL, 'EmbedFonts' )),
    COMMETHOD(['propget', helpstring(u'The Embed Fonts option.')], HRESULT, 'EmbedFonts',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'EmbedFonts' )),
]
################################################################
## code template for IExportPDF implementation
##class IExportPDF_Impl(object):
##    def _get(self):
##        u'The Embed Fonts option.'
##        #return EmbedFonts
##    def _set(self, EmbedFonts):
##        u'The Embed Fonts option.'
##    EmbedFonts = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the PDF should be compressed.'
##        #return Compressed
##    def _set(self, Compressed):
##        u'Indicates if the PDF should be compressed.'
##    Compressed = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The PDF Image Compression.'
##        #return compression
##    def _set(self, compression):
##        u'The PDF Image Compression.'
##    ImageCompression = property(_get, _set, doc = _set.__doc__)
##

class IExportPS2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides extended access to members that control the PostScript export.'
    _iid_ = GUID('{36CE3F37-30C9-4544-AFA6-89A7315ABCE7}')
    _idlflags_ = ['oleautomation']
IExportPS2._methods_ = [
    COMMETHOD(['propput', helpstring(u'Specifies the raster image quality setting, when JPEG compression is used.')], HRESULT, 'JPEGCompressionQuality',
              ( ['in'], c_short, 'pImageQuality' )),
    COMMETHOD(['propget', helpstring(u'Specifies the raster image quality setting, when JPEG compression is used.')], HRESULT, 'JPEGCompressionQuality',
              ( ['retval', 'out'], POINTER(c_short), 'pImageQuality' )),
]
################################################################
## code template for IExportPS2 implementation
##class IExportPS2_Impl(object):
##    def _get(self):
##        u'Specifies the raster image quality setting, when JPEG compression is used.'
##        #return pImageQuality
##    def _set(self, pImageQuality):
##        u'Specifies the raster image quality setting, when JPEG compression is used.'
##    JPEGCompressionQuality = property(_get, _set, doc = _set.__doc__)
##

class FontMapEnvironment(CoClass):
    u'A global collection of font mapping settings.'
    _reg_clsid_ = GUID('{9ECB85B1-6CAA-11D3-B685-0080C8EA4FD5}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7DB92CEC-CB65-420A-8737-FCD0722FD436}', 10, 2)
FontMapEnvironment._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IFontMapEnvironment]


# values for enumeration 'esriTIFFCompression'
esriTIFFCompressionNone = 0
esriTIFFCompressionPackBits = 1
esriTIFFCompressionJPEG = 2
esriTIFFCompressionLZW = 3
esriTIFFCompressionDeflate = 4
esriTIFFCompressionFax4 = 5
esriTIFFCompression = c_int # enum
IExportTIFF._methods_ = [
    COMMETHOD(['propput', helpstring(u'The TIFF Compression type.')], HRESULT, 'CompressionType',
              ( ['in'], esriTIFFCompression, 'type' )),
    COMMETHOD(['propget', helpstring(u'The TIFF Compression type.')], HRESULT, 'CompressionType',
              ( ['retval', 'out'], POINTER(esriTIFFCompression), 'type' )),
    COMMETHOD(['propput', helpstring(u'The option to write GeoTIFF tags.')], HRESULT, 'GeoTiff',
              ( ['in'], VARIANT_BOOL, 'bGeoTiff' )),
    COMMETHOD(['propget', helpstring(u'The option to write GeoTIFF tags.')], HRESULT, 'GeoTiff',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bGeoTiff' )),
    COMMETHOD(['propput', helpstring(u'This option controls the Quality setting for Flate or JPEG compression options.  Range (0..100). Default is 100 (best compression for flate / best quality for JPEG).  Higher values result in smaller files for flate, and larger files for JPEG.')], HRESULT, 'JPEGOrDeflateQuality',
              ( ['in'], c_short, 'Quality' )),
    COMMETHOD(['propget', helpstring(u'This option controls the Quality setting for Flate or JPEG compression options.  Range (0..100). Default is 100 (best compression for flate / best quality for JPEG).  Higher values result in smaller files for flate, and larger files for JPEG.')], HRESULT, 'JPEGOrDeflateQuality',
              ( ['retval', 'out'], POINTER(c_short), 'Quality' )),
    COMMETHOD(['propput', helpstring(u'The Threshold value for BiLevel images. The Threshold value will be used if esriExportImageType equal to esriExportImageTypeBiLevelThreshold.')], HRESULT, 'BiLevelThreshold',
              ( ['in'], c_int, 'threshold' )),
    COMMETHOD(['propget', helpstring(u'The Threshold value for BiLevel images. The Threshold value will be used if esriExportImageType equal to esriExportImageTypeBiLevelThreshold.')], HRESULT, 'BiLevelThreshold',
              ( ['retval', 'out'], POINTER(c_int), 'threshold' )),
]
################################################################
## code template for IExportTIFF implementation
##class IExportTIFF_Impl(object):
##    def _get(self):
##        u'The Threshold value for BiLevel images. The Threshold value will be used if esriExportImageType equal to esriExportImageTypeBiLevelThreshold.'
##        #return threshold
##    def _set(self, threshold):
##        u'The Threshold value for BiLevel images. The Threshold value will be used if esriExportImageType equal to esriExportImageTypeBiLevelThreshold.'
##    BiLevelThreshold = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The TIFF Compression type.'
##        #return type
##    def _set(self, type):
##        u'The TIFF Compression type.'
##    CompressionType = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'This option controls the Quality setting for Flate or JPEG compression options.  Range (0..100). Default is 100 (best compression for flate / best quality for JPEG).  Higher values result in smaller files for flate, and larger files for JPEG.'
##        #return Quality
##    def _set(self, Quality):
##        u'This option controls the Quality setting for Flate or JPEG compression options.  Range (0..100). Default is 100 (best compression for flate / best quality for JPEG).  Higher values result in smaller files for flate, and larger files for JPEG.'
##    JPEGOrDeflateQuality = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The option to write GeoTIFF tags.'
##        #return bGeoTiff
##    def _set(self, bGeoTiff):
##        u'The option to write GeoTIFF tags.'
##    GeoTiff = property(_get, _set, doc = _set.__doc__)
##

class PSDriver(CoClass):
    u'Class used to print maps with the PostScript Driver.'
    _reg_clsid_ = GUID('{CD754683-A222-11D0-A68F-080009D57B9A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7DB92CEC-CB65-420A-8737-FCD0722FD436}', 10, 2)
PSDriver._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IPSDriver, IPSDriver2, ISpotPlateCollection, IColorCorrection, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo, ITrackCancelSetup]

class IExportPDF2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides extended access to members that control the PDF (Portable Document Format) Export.'
    _iid_ = GUID('{86D86855-631D-4A75-AD19-725B460208C7}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriExportPDFLayerOptions'
esriExportPDFLayerOptionsNone = 0
esriExportPDFLayerOptionsLayersOnly = 1
esriExportPDFLayerOptionsLayersAndFeatureAttributes = 2
esriExportPDFLayerOptions = c_int # enum
IExportPDF2._methods_ = [
    COMMETHOD(['propput', helpstring(u'PDF Layers and Feature Attributes option.')], HRESULT, 'ExportPDFLayersAndFeatureAttributes',
              ( ['in'], esriExportPDFLayerOptions, 'pOption' )),
    COMMETHOD(['propget', helpstring(u'PDF Layers and Feature Attributes option.')], HRESULT, 'ExportPDFLayersAndFeatureAttributes',
              ( ['retval', 'out'], POINTER(esriExportPDFLayerOptions), 'pOption' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether geographic coordinate and measurement information is exported.')], HRESULT, 'ExportMeasureInfo',
              ( ['in'], VARIANT_BOOL, 'pbMeasureInformation' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether geographic coordinate and measurement information is exported.')], HRESULT, 'ExportMeasureInfo',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbMeasureInformation' )),
]
################################################################
## code template for IExportPDF2 implementation
##class IExportPDF2_Impl(object):
##    def _get(self):
##        u'PDF Layers and Feature Attributes option.'
##        #return pOption
##    def _set(self, pOption):
##        u'PDF Layers and Feature Attributes option.'
##    ExportPDFLayersAndFeatureAttributes = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether geographic coordinate and measurement information is exported.'
##        #return pbMeasureInformation
##    def _set(self, pbMeasureInformation):
##        u'Indicates whether geographic coordinate and measurement information is exported.'
##    ExportMeasureInfo = property(_get, _set, doc = _set.__doc__)
##


# values for enumeration 'esriExportImageType'
esriExportImageTypeBiLevelMask = 1
esriExportImageTypeBiLevelThreshold = 2
esriExportImageTypeGrayscale = 7
esriExportImageTypeIndexed = 8
esriExportImageTypeTrueColor = 24
esriExportImageType = c_int # enum
IExportImage._methods_ = [
    COMMETHOD(['propput', helpstring(u'Export Image Type.')], HRESULT, 'ImageType',
              ( ['in'], esriExportImageType, 'pimageType' )),
    COMMETHOD(['propget', helpstring(u'Export Image Type.')], HRESULT, 'ImageType',
              ( ['retval', 'out'], POINTER(esriExportImageType), 'pimageType' )),
    COMMETHOD(['propput', helpstring(u'The background color of the Image.')], HRESULT, 'BackgroundColor',
              ( ['in'], POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IColor), 'ppBackgroundColor' )),
    COMMETHOD(['propget', helpstring(u'The background color of the Image.')], HRESULT, 'BackgroundColor',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IColor)), 'ppBackgroundColor' )),
    COMMETHOD(['propput', helpstring(u'The width of the Image. If width is zero, screen width is used.')], HRESULT, 'Width',
              ( ['in'], c_int, 'pWidth' )),
    COMMETHOD(['propget', helpstring(u'The width of the Image. If width is zero, screen width is used.')], HRESULT, 'Width',
              ( ['retval', 'out'], POINTER(c_int), 'pWidth' )),
    COMMETHOD(['propput', helpstring(u'The height of the Image. If height is zero, screen height is used.')], HRESULT, 'Height',
              ( ['in'], c_int, 'pHeight' )),
    COMMETHOD(['propget', helpstring(u'The height of the Image. If height is zero, screen height is used.')], HRESULT, 'Height',
              ( ['retval', 'out'], POINTER(c_int), 'pHeight' )),
]
################################################################
## code template for IExportImage implementation
##class IExportImage_Impl(object):
##    def _get(self):
##        u'The width of the Image. If width is zero, screen width is used.'
##        #return pWidth
##    def _set(self, pWidth):
##        u'The width of the Image. If width is zero, screen width is used.'
##    Width = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The background color of the Image.'
##        #return ppBackgroundColor
##    def _set(self, ppBackgroundColor):
##        u'The background color of the Image.'
##    BackgroundColor = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Export Image Type.'
##        #return pimageType
##    def _set(self, pimageType):
##        u'Export Image Type.'
##    ImageType = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The height of the Image. If height is zero, screen height is used.'
##        #return pHeight
##    def _set(self, pHeight):
##        u'The height of the Image. If height is zero, screen height is used.'
##    Height = property(_get, _set, doc = _set.__doc__)
##

class IExportSVG(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the SVG (Scalable Vector Graphics) Export.'
    _iid_ = GUID('{0A149C8E-5D95-4A5C-9F48-5D30B3F12FA2}')
    _idlflags_ = ['oleautomation']
IExportSVG._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if the SVG file is compressed.')], HRESULT, 'Compressed',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Compressed' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the SVG file is compressed.')], HRESULT, 'Compressed',
              ( ['in'], VARIANT_BOOL, 'Compressed' )),
    COMMETHOD(['propput', helpstring(u'The Embed Fonts option.')], HRESULT, 'EmbedFonts',
              ( ['in'], VARIANT_BOOL, 'EmbedFonts' )),
    COMMETHOD(['propget', helpstring(u'The Embed Fonts option.')], HRESULT, 'EmbedFonts',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'EmbedFonts' )),
]
################################################################
## code template for IExportSVG implementation
##class IExportSVG_Impl(object):
##    def _get(self):
##        u'The Embed Fonts option.'
##        #return EmbedFonts
##    def _set(self, EmbedFonts):
##        u'The Embed Fonts option.'
##    EmbedFonts = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the SVG file is compressed.'
##        #return Compressed
##    def _set(self, Compressed):
##        u'Indicates if the SVG file is compressed.'
##    Compressed = property(_get, _set, doc = _set.__doc__)
##

class JpegExporter(CoClass):
    u'Superseded by ExportJPEG. Class used to export maps to JPEG (Joint Photographic Experts Group) format.'
    _reg_clsid_ = GUID('{511FF07A-55C4-11D3-9FFD-00C04F6BC8DD}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7DB92CEC-CB65-420A-8737-FCD0722FD436}', 10, 2)
class IJpegExporter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Superseded by IExportJPEG. Provides access to members that control the JPEG (Joint Photographic Experts Group) Exporter.'
    _iid_ = GUID('{511FF079-55C4-11D3-9FFD-00C04F6BC8DD}')
    _idlflags_ = ['oleautomation']
class IExporter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Superseded by IExport. Provides access to members that control the Base Exporter.'
    _iid_ = GUID('{7D4881E2-57C6-11D1-945E-080009EEBECB}')
    _idlflags_ = ['oleautomation']
class IStepProgressorSetup(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that set up the Step Progressor.'
    _iid_ = GUID('{1C538193-8806-489C-8A79-4B54C8C18B37}')
    _idlflags_ = ['oleautomation']
JpegExporter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IJpegExporter, IExporter, IExporterPriority, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo, IOutputCleanup, IStepProgressorSetup, ITrackCancelSetup]

class ExportPDF(CoClass):
    u'Class used to export maps to PDF (Portable Document Format) format.'
    _reg_clsid_ = GUID('{A0D673EF-BCB9-4C6D-9226-214E4142FBC7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7DB92CEC-CB65-420A-8737-FCD0722FD436}', 10, 2)
class IExportVectorOptionsEx(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the extra Vector Export Options.'
    _iid_ = GUID('{CCF50555-74E3-4F29-9FFE-1FC489D1552C}')
    _idlflags_ = ['oleautomation']
class IExportPagesMultipleFile(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides extended access to members that control the PDF (Portable Document Format) export.'
    _iid_ = GUID('{1A551946-895A-4809-80D8-D417D654F3AC}')
    _idlflags_ = ['oleautomation']
class IExportPDFPasswordSecurity(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides extended access to members that control the PDF (Portable Document Format) export.'
    _iid_ = GUID('{6C9A13E6-F9EC-4EBF-AF52-BB1D822622DF}')
    _idlflags_ = ['oleautomation']
class IExportColorspaceSettings(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Destination Colorspace for Export.'
    _iid_ = GUID('{C42431DC-237A-4628-996A-39A89AF74158}')
    _idlflags_ = ['oleautomation']
ExportPDF._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IExportVector, IExportVectorOptions, IExportVectorOptionsEx, IExportPDF, IExportPDF2, IExportPDF3, IExportPagesMultipleFile, IExportPDFPasswordSecurity, IExport, ISettingsInRegistry, IExportColorspaceSettings, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IOutputRasterSettings]

class IExportAI2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control advanced settings of AI (Adobe Illustrator) exporting.'
    _iid_ = GUID('{0AB19CC6-7C0B-4916-8D8D-8B6B9C4E4A8A}')
    _idlflags_ = ['oleautomation']
IExportAI2._methods_ = [
    COMMETHOD(['propput'], HRESULT, 'ExportFeatureName',
              ( ['in'], VARIANT_BOOL, 'pExportAttrs' )),
    COMMETHOD(['propget'], HRESULT, 'ExportFeatureName',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pExportAttrs' )),
]
################################################################
## code template for IExportAI2 implementation
##class IExportAI2_Impl(object):
##    def _get(self):
##        '-no docstring-'
##        #return pExportAttrs
##    def _set(self, pExportAttrs):
##        '-no docstring-'
##    ExportFeatureName = property(_get, _set, doc = _set.__doc__)
##

class EmfExporter(CoClass):
    u'Superseded by ExportEMF. Class used to export maps to Windows Enhanced Metafile (EMF) format.'
    _reg_clsid_ = GUID('{20CD4011-8F3D-11D0-8590-0800091A2A72}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7DB92CEC-CB65-420A-8737-FCD0722FD436}', 10, 2)
EmfExporter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IEmfExporter, IExporter, IExporterPriority, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo, IOutputCleanup]

class ExportSVG(CoClass):
    u'Class used to export maps to SVG (Scalable Vector Graphics) format.'
    _reg_clsid_ = GUID('{637180AF-72CF-4E99-AFCE-887B9A1091C3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7DB92CEC-CB65-420A-8737-FCD0722FD436}', 10, 2)
ExportSVG._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IExportVector, IExportVectorOptions, IExportVectorOptionsEx, IExportSVG, IExport, ISettingsInRegistry, IExportColorspaceSettings, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IOutputRasterSettings]


# values for enumeration 'esriPSDriverImageCompression'
esriPSDriverPSLevel1NoCompress = 0
esriPSDriverPSLevel1Compress = 1
esriPSDriverPSLevel2NoCompress = 2
esriPSDriverPSLevel2Compress = 3
esriPSDriverImageCompression = c_int # enum

# values for enumeration 'esriPSDriverHalfTone'
esriPSDriverDPI = 0
esriPSDriverLPI = 1
esriPSDriverLastHalfTone = 2
esriPSDriverHalfTone = c_int # enum

# values for enumeration 'esriPSDriverEmulsion'
esriPSDriverEmulUP = 0
esriPSDriverEmulDOWN = 1
esriPSDriverEmulsion = c_int # enum

# values for enumeration 'esriPSDriverImage'
esriPSDriverImagePOS = 0
esriPSDriverImageNEG = 1
esriPSDriverImage = c_int # enum

# values for enumeration 'esriPSDriverPSLanguageLevel'
esriPSDriverPSLevel2 = 0
esriPSDriverPSLevel3 = 1
esriPSDriverPSLanguageLevel = c_int # enum
IPSDriver._methods_ = [
    COMMETHOD(['propget', helpstring(u'The Image Compression of the PostScript Driver.')], HRESULT, 'ImageCompression',
              ( ['retval', 'out'], POINTER(esriPSDriverImageCompression), 'ImageCompression' )),
    COMMETHOD(['propput', helpstring(u'The Image Compression of the PostScript Driver.')], HRESULT, 'ImageCompression',
              ( ['in'], esriPSDriverImageCompression, 'ImageCompression' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether a separate Image file should be created for ArcPress.')], HRESULT, 'ArcPressSeparateImage',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'sepImage' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether a separate Image file should be created for ArcPress.')], HRESULT, 'ArcPressSeparateImage',
              ( ['in'], VARIANT_BOOL, 'sepImage' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the Image should be rotated 90 degress for ArcPress.')], HRESULT, 'ArcPressSeparateImageRotate',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'sepImage' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether the Image should be rotated 90 degress for ArcPress.')], HRESULT, 'ArcPressSeparateImageRotate',
              ( ['in'], VARIANT_BOOL, 'sepImage' )),
    COMMETHOD(['propget', helpstring(u'The Font Map Collection for Font Mapping.')], HRESULT, 'FontMapCollection',
              ( ['retval', 'out'], POINTER(POINTER(IFontMapCollection)), 'FontMapCollection' )),
    COMMETHOD(['propputref', helpstring(u'The Font Map Collection for Font Mapping.')], HRESULT, 'FontMapCollection',
              ( ['in'], POINTER(IFontMapCollection), 'FontMapCollection' )),
    COMMETHOD(['propget', helpstring(u'The PPD (PostScript Printer Description) file to be used.')], HRESULT, 'PPDFile',
              ( ['retval', 'out'], POINTER(BSTR), 'PPDFile' )),
    COMMETHOD(['propput', helpstring(u'The PPD (PostScript Printer Description) file to be used.')], HRESULT, 'PPDFile',
              ( ['in'], BSTR, 'PPDFile' )),
    COMMETHOD(['propget', helpstring(u'The PostScript Marks.')], HRESULT, 'Marks',
              ( ['retval', 'out'], POINTER(c_short), 'Marks' )),
    COMMETHOD(['propput', helpstring(u'The PostScript Marks.')], HRESULT, 'Marks',
              ( ['in'], c_short, 'Marks' )),
    COMMETHOD(['propget', helpstring(u'The Halftone DPI / LPI.')], HRESULT, 'HalfTone',
              ( ['in'], esriPSDriverHalfTone, 'HalfTone' ),
              ( ['retval', 'out'], POINTER(c_int), 'value' )),
    COMMETHOD(['propput', helpstring(u'The Halftone DPI / LPI.')], HRESULT, 'HalfTone',
              ( ['in'], esriPSDriverHalfTone, 'HalfTone' ),
              ( ['in'], c_int, 'value' )),
    COMMETHOD(['propget', helpstring(u'The printer page form. Use Win32 DMPAPER_xxx constants.')], HRESULT, 'FormName',
              ( ['retval', 'out'], POINTER(BSTR), 'FormName' )),
    COMMETHOD(['propput', helpstring(u'The printer page form. Use Win32 DMPAPER_xxx constants.')], HRESULT, 'FormName',
              ( ['in'], BSTR, 'FormName' )),
    COMMETHOD(['propget', helpstring(u'The printers Printable Bounds - Used for Marks.')], HRESULT, 'PrintableBounds',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'ppBounds' )),
    COMMETHOD(['propput', helpstring(u'The printers Printable Bounds - Used for Marks.')], HRESULT, 'PrintableBounds',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'ppBounds' )),
    COMMETHOD(['propget', helpstring(u'The printer page orientation (1 = portrait.  2 = landscape).')], HRESULT, 'Orientation',
              ( ['retval', 'out'], POINTER(c_short), 'Orientation' )),
    COMMETHOD(['propput', helpstring(u'The printer page orientation (1 = portrait.  2 = landscape).')], HRESULT, 'Orientation',
              ( ['in'], c_short, 'Orientation' )),
    COMMETHOD(['propget', helpstring(u'The Emulsion setting for the PostScript Driver.')], HRESULT, 'Emulsion',
              ( ['retval', 'out'], POINTER(esriPSDriverEmulsion), 'Emulsion' )),
    COMMETHOD(['propput', helpstring(u'The Emulsion setting for the PostScript Driver.')], HRESULT, 'Emulsion',
              ( ['in'], esriPSDriverEmulsion, 'Emulsion' )),
    COMMETHOD(['propget', helpstring(u'The Image setting (Positive or Negative) for the PostScript Driver.')], HRESULT, 'Image',
              ( ['retval', 'out'], POINTER(esriPSDriverImage), 'Image' )),
    COMMETHOD(['propput', helpstring(u'The Image setting (Positive or Negative) for the PostScript Driver.')], HRESULT, 'Image',
              ( ['in'], esriPSDriverImage, 'Image' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the 1-bit Image Transparency setting for the PostScript Driver is set to true.')], HRESULT, 'OneBitImageTransparency',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'imageTransparency' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the 1-bit Image Transparency setting for the PostScript Driver is set to true.')], HRESULT, 'OneBitImageTransparency',
              ( ['in'], VARIANT_BOOL, 'imageTransparency' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the PostScript Driver should use the ENHMETAHEADER rclFrame instead of rclBounds for the PostScript Bounding Box.')], HRESULT, 'UseEMFFrameBoxForPSBoundingBox',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'useFrameBox' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether the PostScript Driver should use the ENHMETAHEADER rclFrame instead of rclBounds for the PostScript Bounding Box.')], HRESULT, 'UseEMFFrameBoxForPSBoundingBox',
              ( ['in'], VARIANT_BOOL, 'useFrameBox' )),
    COMMETHOD(['propget', helpstring(u'The PostScript Driver Language Level.')], HRESULT, 'PSLanguageLevel',
              ( ['retval', 'out'], POINTER(esriPSDriverPSLanguageLevel), 'pslevel' )),
    COMMETHOD(['propput', helpstring(u'The PostScript Driver Language Level.')], HRESULT, 'PSLanguageLevel',
              ( ['in'], esriPSDriverPSLanguageLevel, 'pslevel' )),
    COMMETHOD(['propput', helpstring(u'PostScript Driver will update a Progress Bar.')], HRESULT, 'StepProgressor',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStepProgressor), 'rhs' )),
    COMMETHOD([helpstring(u'Converts the EMF file to a EPS File.')], HRESULT, 'CreatePS',
              ( ['in'], BSTR, 'InputFileName' ),
              ( ['in'], BSTR, 'OutputFileName' )),
]
################################################################
## code template for IPSDriver implementation
##class IPSDriver_Impl(object):
##    def _get(self):
##        u'Indicates if the 1-bit Image Transparency setting for the PostScript Driver is set to true.'
##        #return imageTransparency
##    def _set(self, imageTransparency):
##        u'Indicates if the 1-bit Image Transparency setting for the PostScript Driver is set to true.'
##    OneBitImageTransparency = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The printers Printable Bounds - Used for Marks.'
##        #return ppBounds
##    def _set(self, ppBounds):
##        u'The printers Printable Bounds - Used for Marks.'
##    PrintableBounds = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether the Image should be rotated 90 degress for ArcPress.'
##        #return sepImage
##    def _set(self, sepImage):
##        u'Indicates whether the Image should be rotated 90 degress for ArcPress.'
##    ArcPressSeparateImageRotate = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The Image setting (Positive or Negative) for the PostScript Driver.'
##        #return Image
##    def _set(self, Image):
##        u'The Image setting (Positive or Negative) for the PostScript Driver.'
##    Image = property(_get, _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'PostScript Driver will update a Progress Bar.'
##    StepProgressor = property(fset = _set, doc = _set.__doc__)
##
##    def _get(self, HalfTone):
##        u'The Halftone DPI / LPI.'
##        #return value
##    def _set(self, HalfTone, value):
##        u'The Halftone DPI / LPI.'
##    HalfTone = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The PostScript Driver Language Level.'
##        #return pslevel
##    def _set(self, pslevel):
##        u'The PostScript Driver Language Level.'
##    PSLanguageLevel = property(_get, _set, doc = _set.__doc__)
##
##    def CreatePS(self, InputFileName, OutputFileName):
##        u'Converts the EMF file to a EPS File.'
##        #return 
##
##    def _get(self):
##        u'The Emulsion setting for the PostScript Driver.'
##        #return Emulsion
##    def _set(self, Emulsion):
##        u'The Emulsion setting for the PostScript Driver.'
##    Emulsion = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The PostScript Marks.'
##        #return Marks
##    def _set(self, Marks):
##        u'The PostScript Marks.'
##    Marks = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether a separate Image file should be created for ArcPress.'
##        #return sepImage
##    def _set(self, sepImage):
##        u'Indicates whether a separate Image file should be created for ArcPress.'
##    ArcPressSeparateImage = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The PPD (PostScript Printer Description) file to be used.'
##        #return PPDFile
##    def _set(self, PPDFile):
##        u'The PPD (PostScript Printer Description) file to be used.'
##    PPDFile = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The printer page orientation (1 = portrait.  2 = landscape).'
##        #return Orientation
##    def _set(self, Orientation):
##        u'The printer page orientation (1 = portrait.  2 = landscape).'
##    Orientation = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The printer page form. Use Win32 DMPAPER_xxx constants.'
##        #return FormName
##    def _set(self, FormName):
##        u'The printer page form. Use Win32 DMPAPER_xxx constants.'
##    FormName = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether the PostScript Driver should use the ENHMETAHEADER rclFrame instead of rclBounds for the PostScript Bounding Box.'
##        #return useFrameBox
##    def _set(self, useFrameBox):
##        u'Indicates whether the PostScript Driver should use the ENHMETAHEADER rclFrame instead of rclBounds for the PostScript Bounding Box.'
##    UseEMFFrameBoxForPSBoundingBox = property(_get, _set, doc = _set.__doc__)
##
##    def FontMapCollection(self, FontMapCollection):
##        u'The Font Map Collection for Font Mapping.'
##        #return 
##
##    def _get(self):
##        u'The Image Compression of the PostScript Driver.'
##        #return ImageCompression
##    def _set(self, ImageCompression):
##        u'The Image Compression of the PostScript Driver.'
##    ImageCompression = property(_get, _set, doc = _set.__doc__)
##


# values for enumeration 'esriExportErrorReturnCodes'
E_CGMVERSION3NEEDED = -2147220735
E_LICENSENOTAVAILABLE = -2147220734
E_OBJECTSETUP = -2147220733
E_TEMPMETAFILE = -2147220732
E_MAPMETAFILE = -2147220731
E_PAPERREFREQ = -2147220730
E_DRIVERNOTMATCH = -2147220729
E_PARAMETER = -2147220728
E_REGISTRYSETTINGS = -2147220727
E_FILECREATION = -2147220726
E_METAFILEPARSING = -2147220725
E_OPENPRINTER = -2147220724
E_BITMAPOUTOFMEMORY = -2147220723
E_STARTPRINTING = -2147220722
E_WASNOTACTIVATED = -2147220721
E_OUTPUTFILENAME = -2147220720
E_PIXELBOUNDS = -2147220719
esriExportErrorReturnCodes = c_int # enum

# values for enumeration 'esriExportMultipleFiles'
esriExportMultipleFiles_None = 0
esriExportMultipleFiles_PageNames = 1
esriExportMultipleFiles_PageIndex = 2
esriExportMultipleFiles = c_int # enum
IExportPagesMultipleFile._methods_ = [
    COMMETHOD(['propput', helpstring(u'Specify how multipage pdf to be exported.')], HRESULT, 'MultipleFileOutput',
              ( ['in'], esriExportMultipleFiles, 'pOption' )),
    COMMETHOD(['propget', helpstring(u'Specify how multipage pdf to be exported.')], HRESULT, 'MultipleFileOutput',
              ( ['retval', 'out'], POINTER(esriExportMultipleFiles), 'pOption' )),
]
################################################################
## code template for IExportPagesMultipleFile implementation
##class IExportPagesMultipleFile_Impl(object):
##    def _get(self):
##        u'Specify how multipage pdf to be exported.'
##        #return pOption
##    def _set(self, pOption):
##        u'Specify how multipage pdf to be exported.'
##    MultipleFileOutput = property(_get, _set, doc = _set.__doc__)
##

class IDibExporter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Superseded by IExportBMP. Provides access to members that control the DIB (Windows Device Independent Bitmap) Exporter.'
    _iid_ = GUID('{7D4881E5-57C6-11D1-945E-080009EEBECB}')
    _idlflags_ = ['oleautomation']
IDibExporter._methods_ = [
    COMMETHOD(['propput', helpstring(u'Indicates if the bitmap should be written to memory. If false, it is written to a file specified by Path. If true, use HDIB to get the memory handle after ReleaseDC has been called.')], HRESULT, 'IsInMemory',
              ( ['in'], VARIANT_BOOL, 'pIsInMemory' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the bitmap should be written to memory. If false, it is written to a file specified by Path. If true, use HDIB to get the memory handle after ReleaseDC has been called.')], HRESULT, 'IsInMemory',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pIsInMemory' )),
    COMMETHOD(['propget', helpstring(u'Handle to in-memory DIB. Valid only after ReleaseDC has been called.')], HRESULT, 'HDIB',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'pHandle' )),
    COMMETHOD(['propput', helpstring(u'The color depth of the DIB.')], HRESULT, 'BitsPerPixel',
              ( ['in'], c_short, 'pBitsPerPixel' )),
    COMMETHOD(['propget', helpstring(u'The color depth of the DIB.')], HRESULT, 'BitsPerPixel',
              ( ['retval', 'out'], POINTER(c_short), 'pBitsPerPixel' )),
    COMMETHOD(['propput', helpstring(u'The background color of the DIB.')], HRESULT, 'BackgroundColor',
              ( ['in'], POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IColor), 'ppBackgroundColor' )),
    COMMETHOD(['propget', helpstring(u'The background color of the DIB.')], HRESULT, 'BackgroundColor',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IColor)), 'ppBackgroundColor' )),
    COMMETHOD(['propput', helpstring(u'The width of the DIB. If width or height is zero, screen size is used.')], HRESULT, 'Width',
              ( ['in'], c_short, 'pWidth' )),
    COMMETHOD(['propget', helpstring(u'The width of the DIB. If width or height is zero, screen size is used.')], HRESULT, 'Width',
              ( ['retval', 'out'], POINTER(c_short), 'pWidth' )),
    COMMETHOD(['propput', helpstring(u'The height of the DIB. If width or height is zero, screen size is used.')], HRESULT, 'Height',
              ( ['in'], c_short, 'pHeight' )),
    COMMETHOD(['propget', helpstring(u'The height of the DIB. If width or height is zero, screen size is used.')], HRESULT, 'Height',
              ( ['retval', 'out'], POINTER(c_short), 'pHeight' )),
]
################################################################
## code template for IDibExporter implementation
##class IDibExporter_Impl(object):
##    def _get(self):
##        u'The width of the DIB. If width or height is zero, screen size is used.'
##        #return pWidth
##    def _set(self, pWidth):
##        u'The width of the DIB. If width or height is zero, screen size is used.'
##    Width = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the bitmap should be written to memory. If false, it is written to a file specified by Path. If true, use HDIB to get the memory handle after ReleaseDC has been called.'
##        #return pIsInMemory
##    def _set(self, pIsInMemory):
##        u'Indicates if the bitmap should be written to memory. If false, it is written to a file specified by Path. If true, use HDIB to get the memory handle after ReleaseDC has been called.'
##    IsInMemory = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The color depth of the DIB.'
##        #return pBitsPerPixel
##    def _set(self, pBitsPerPixel):
##        u'The color depth of the DIB.'
##    BitsPerPixel = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The height of the DIB. If width or height is zero, screen size is used.'
##        #return pHeight
##    def _set(self, pHeight):
##        u'The height of the DIB. If width or height is zero, screen size is used.'
##    Height = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def HDIB(self):
##        u'Handle to in-memory DIB. Valid only after ReleaseDC has been called.'
##        #return pHandle
##
##    def _get(self):
##        u'The background color of the DIB.'
##        #return ppBackgroundColor
##    def _set(self, ppBackgroundColor):
##        u'The background color of the DIB.'
##    BackgroundColor = property(_get, _set, doc = _set.__doc__)
##

IExportVectorOptionsEx._methods_ = [
    COMMETHOD(['propput', helpstring(u'Options describing what to do with Picture Symbol on export.')], HRESULT, 'ExportPictureSymbolOptions',
              ( ['in'], comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.esriPictureSymbolOptions, 'opt' )),
    COMMETHOD(['propget', helpstring(u'Options describing what to do with Picture Symbol on export.')], HRESULT, 'ExportPictureSymbolOptions',
              ( ['retval', 'out'], POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.esriPictureSymbolOptions), 'opt' )),
]
################################################################
## code template for IExportVectorOptionsEx implementation
##class IExportVectorOptionsEx_Impl(object):
##    def _get(self):
##        u'Options describing what to do with Picture Symbol on export.'
##        #return opt
##    def _set(self, opt):
##        u'Options describing what to do with Picture Symbol on export.'
##    ExportPictureSymbolOptions = property(_get, _set, doc = _set.__doc__)
##

class IPsExporter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Superseded by IExportPS. Provides access to members that control the EPS (Encapsulated PostScript) Exporter.'
    _iid_ = GUID('{7D4881E6-57C6-11D1-945E-080009EEBECB}')
    _idlflags_ = ['oleautomation']
IPsExporter._methods_ = [
    COMMETHOD([helpstring(u'Returns Interface IPSDriver.')], HRESULT, 'QueryPSDriver',
              ( ['retval', 'out'], POINTER(POINTER(IPSDriver)), 'PSDriver' )),
]
################################################################
## code template for IPsExporter implementation
##class IPsExporter_Impl(object):
##    def QueryPSDriver(self):
##        u'Returns Interface IPSDriver.'
##        #return PSDriver
##

IFontMapEnvironment._methods_ = [
    COMMETHOD(['propput', helpstring(u'Indicates whether to save font mappings.')], HRESULT, 'SaveMappings',
              ( ['in'], VARIANT_BOOL, 'SaveMappings' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether to save font mappings.')], HRESULT, 'SaveMappings',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'SaveMappings' )),
    COMMETHOD(['propget', helpstring(u'The FontMap Collection.')], HRESULT, 'FontMapCollection',
              ( ['retval', 'out'], POINTER(POINTER(IFontMapCollection)), 'FontMapCollection' )),
    COMMETHOD(['propput', helpstring(u'The Default Mapping Choices for Font Substitution.')], HRESULT, 'DefaultMappingsChoices',
              ( ['in'], VARIANT, 'defaultMappingChoices' )),
    COMMETHOD(['propget', helpstring(u'The Default Mapping Choices for Font Substitution.')], HRESULT, 'DefaultMappingsChoices',
              ( ['retval', 'out'], POINTER(VARIANT), 'defaultMappingChoices' )),
    COMMETHOD(['propput', helpstring(u'The Default Font Mapping string.')], HRESULT, 'DefaultMapping',
              ( ['in'], BSTR, 'DefaultMapping' )),
    COMMETHOD(['propget', helpstring(u'The Default Font Mapping string.')], HRESULT, 'DefaultMapping',
              ( ['retval', 'out'], POINTER(BSTR), 'DefaultMapping' )),
    COMMETHOD(['propput', helpstring(u'The Font Mapping checkbox description string.')], HRESULT, 'ApplyDefaultMappingDesc',
              ( ['in'], BSTR, 'ApplyDefaultMappingDesc' )),
    COMMETHOD(['propget', helpstring(u'The Font Mapping checkbox description string.')], HRESULT, 'ApplyDefaultMappingDesc',
              ( ['retval', 'out'], POINTER(BSTR), 'ApplyDefaultMappingDesc' )),
]
################################################################
## code template for IFontMapEnvironment implementation
##class IFontMapEnvironment_Impl(object):
##    def _get(self):
##        u'The Default Font Mapping string.'
##        #return DefaultMapping
##    def _set(self, DefaultMapping):
##        u'The Default Font Mapping string.'
##    DefaultMapping = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether to save font mappings.'
##        #return SaveMappings
##    def _set(self, SaveMappings):
##        u'Indicates whether to save font mappings.'
##    SaveMappings = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The Font Mapping checkbox description string.'
##        #return ApplyDefaultMappingDesc
##    def _set(self, ApplyDefaultMappingDesc):
##        u'The Font Mapping checkbox description string.'
##    ApplyDefaultMappingDesc = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The Default Mapping Choices for Font Substitution.'
##        #return defaultMappingChoices
##    def _set(self, defaultMappingChoices):
##        u'The Default Mapping Choices for Font Substitution.'
##    DefaultMappingsChoices = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def FontMapCollection(self):
##        u'The FontMap Collection.'
##        #return FontMapCollection
##

class IExportAI(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the AI (Adobe Illustrator) Export.'
    _iid_ = GUID('{69822E67-C74B-4138-AB20-AA4E00CB87DD}')
    _idlflags_ = ['oleautomation']
IExportAI._methods_ = [
    COMMETHOD(['propput', helpstring(u'The Embed Fonts option.')], HRESULT, 'EmbedFonts',
              ( ['in'], VARIANT_BOOL, 'EmbedFonts' )),
    COMMETHOD(['propget', helpstring(u'The Embed Fonts option.')], HRESULT, 'EmbedFonts',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'EmbedFonts' )),
]
################################################################
## code template for IExportAI implementation
##class IExportAI_Impl(object):
##    def _get(self):
##        u'The Embed Fonts option.'
##        #return EmbedFonts
##    def _set(self, EmbedFonts):
##        u'The Embed Fonts option.'
##    EmbedFonts = property(_get, _set, doc = _set.__doc__)
##

IExporter._methods_ = [
    COMMETHOD(['propget', helpstring(u'The Name of the Exporter.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'Filter String used in the CFileDialog class.')], HRESULT, 'Filter',
              ( ['retval', 'out'], POINTER(BSTR), 'Filter' )),
    COMMETHOD(['propget', helpstring(u'File Extension associated with Exporter.')], HRESULT, 'FileExtension',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propput', helpstring(u'The Pixel Bounds of the Exporter.')], HRESULT, 'PixelBounds',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'PixelBounds' )),
    COMMETHOD(['propget', helpstring(u'The Pixel Bounds of the Exporter.')], HRESULT, 'PixelBounds',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'PixelBounds' )),
    COMMETHOD(['propput', helpstring(u'The Export File Name.')], HRESULT, 'ExportFileName',
              ( ['in'], BSTR, 'fileName' )),
    COMMETHOD(['propget', helpstring(u'The Export File Name.')], HRESULT, 'ExportFileName',
              ( ['retval', 'out'], POINTER(BSTR), 'fileName' )),
    COMMETHOD(['propget', helpstring(u'The Resolution of the Exporter.')], HRESULT, 'Resolution',
              ( ['retval', 'out'], POINTER(c_short), 'res' )),
    COMMETHOD(['propput', helpstring(u'The Resolution of the Exporter.')], HRESULT, 'Resolution',
              ( ['in'], c_short, 'res' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the Output will be clipped to the Graphics Extent.')], HRESULT, 'ClipToGraphicExtent',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'clipToGraphicsExtent' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the Output will be clipped to the Graphics Extent.')], HRESULT, 'ClipToGraphicExtent',
              ( ['in'], VARIANT_BOOL, 'clipToGraphicsExtent' )),
    COMMETHOD([helpstring(u'Initializes the Exporter.')], HRESULT, 'StartExporting',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'hDC' )),
    COMMETHOD([helpstring(u'Shuts down the Exporter.')], HRESULT, 'FinishExporting'),
]
################################################################
## code template for IExporter implementation
##class IExporter_Impl(object):
##    def _get(self):
##        u'Indicates if the Output will be clipped to the Graphics Extent.'
##        #return clipToGraphicsExtent
##    def _set(self, clipToGraphicsExtent):
##        u'Indicates if the Output will be clipped to the Graphics Extent.'
##    ClipToGraphicExtent = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Name(self):
##        u'The Name of the Exporter.'
##        #return Name
##
##    def _get(self):
##        u'The Pixel Bounds of the Exporter.'
##        #return PixelBounds
##    def _set(self, PixelBounds):
##        u'The Pixel Bounds of the Exporter.'
##    PixelBounds = property(_get, _set, doc = _set.__doc__)
##
##    def StartExporting(self):
##        u'Initializes the Exporter.'
##        #return hDC
##
##    def FinishExporting(self):
##        u'Shuts down the Exporter.'
##        #return 
##
##    @property
##    def Filter(self):
##        u'Filter String used in the CFileDialog class.'
##        #return Filter
##
##    @property
##    def FileExtension(self):
##        u'File Extension associated with Exporter.'
##        #return Name
##
##    def _get(self):
##        u'The Resolution of the Exporter.'
##        #return res
##    def _set(self, res):
##        u'The Resolution of the Exporter.'
##    Resolution = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The Export File Name.'
##        #return fileName
##    def _set(self, fileName):
##        u'The Export File Name.'
##    ExportFileName = property(_get, _set, doc = _set.__doc__)
##

class IOutputPageOptionsAdmin(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Private interface to output page options.'
    _iid_ = GUID('{1F685F18-704A-4755-834F-4C0D67303A2F}')
    _idlflags_ = ['oleautomation']
IOutputPageOptionsAdmin._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if layout is being output.')], HRESULT, 'OutputtingPageLayout',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD(['propput', helpstring(u'Indicates if layout is being output.')], HRESULT, 'OutputtingPageLayout',
              ( ['in'], VARIANT_BOOL, 'flag' )),
    COMMETHOD(['propget', helpstring(u'Indicates if a page selection exists.')], HRESULT, 'PageSelectionExists',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD(['propput', helpstring(u'Indicates if a page selection exists.')], HRESULT, 'PageSelectionExists',
              ( ['in'], VARIANT_BOOL, 'flag' )),
    COMMETHOD(['propget', helpstring(u'Indicates the number of pages to the export dialog. Other clients should use the PageIndex.PageCount.')], HRESULT, 'PageCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propput', helpstring(u'Indicates the number of pages to the export dialog. Other clients should use the PageIndex.PageCount.')], HRESULT, 'PageCount',
              ( ['in'], c_int, 'Count' )),
    COMMETHOD(['propget', helpstring(u'Indicates the number of selected pages to the export dialog. Other clients should use the PageIndex.PageCount.')], HRESULT, 'SelectedPageCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propput', helpstring(u'Indicates the number of selected pages to the export dialog. Other clients should use the PageIndex.PageCount.')], HRESULT, 'SelectedPageCount',
              ( ['in'], c_int, 'Count' )),
    COMMETHOD(['propget', helpstring(u'Index of the current page.')], HRESULT, 'CurrentIndex',
              ( ['retval', 'out'], POINTER(c_int), 'index' )),
    COMMETHOD(['propput', helpstring(u'Index of the current page.')], HRESULT, 'CurrentIndex',
              ( ['in'], c_int, 'index' )),
]
################################################################
## code template for IOutputPageOptionsAdmin implementation
##class IOutputPageOptionsAdmin_Impl(object):
##    def _get(self):
##        u'Indicates the number of selected pages to the export dialog. Other clients should use the PageIndex.PageCount.'
##        #return Count
##    def _set(self, Count):
##        u'Indicates the number of selected pages to the export dialog. Other clients should use the PageIndex.PageCount.'
##    SelectedPageCount = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if layout is being output.'
##        #return flag
##    def _set(self, flag):
##        u'Indicates if layout is being output.'
##    OutputtingPageLayout = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Index of the current page.'
##        #return index
##    def _set(self, index):
##        u'Index of the current page.'
##    CurrentIndex = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if a page selection exists.'
##        #return flag
##    def _set(self, flag):
##        u'Indicates if a page selection exists.'
##    PageSelectionExists = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates the number of pages to the export dialog. Other clients should use the PageIndex.PageCount.'
##        #return Count
##    def _set(self, Count):
##        u'Indicates the number of pages to the export dialog. Other clients should use the PageIndex.PageCount.'
##    PageCount = property(_get, _set, doc = _set.__doc__)
##

class PsExporter(CoClass):
    u'Superseded by ExportPS. Class used to export maps to EPS (Encapsulated PostScript) format.'
    _reg_clsid_ = GUID('{20CD4014-8F3D-11D0-8590-0800091A2A72}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7DB92CEC-CB65-420A-8737-FCD0722FD436}', 10, 2)
PsExporter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IPsExporter, IExporter, IExporterPriority, IFontMapEnvironment, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo, IOutputCleanup, IStepProgressorSetup, ITrackCancelSetup]


# values for enumeration 'esriOutputErrorReturnCodes'
E_INTERNALERROR = -2147220686
E_REQUESTEDFUNCTIONALITYDOESNOTSUPPORTED = -2147220685
E_MEMORYOUT = -2147220684
E_MEMORYERROR = -2147220683
E_INVALIDORCURRUPTFILE = -2147220682
E_FILEREADINGERROR = -2147220681
E_FILEWRITINGERROR = -2147220680
E_FILEOPENINGERROR = -2147220679
E_FILECREATIONERROR = -2147220678
E_IMAGEDIRECTORYREADINGERROR = -2147220677
E_IMAGEDIRECTORYWRITINGERROR = -2147220676
E_CANNOTCOMPRESSORDECOMPRESS = -2147220675
E_READORWRITEJPEGMARKER = -2147220674
E_INCOMPATIBLEZLIB = -2147220673
E_INVALIDIMAGEPARAMETERS = -2147220672
E_INVALIDPARAMETERS = -2147220671
E_CLASSSETTEDUPINCORRECTLY = -2147220670
S_SAVEDPRINTERNOTFOUND = 262979
S_NOPRINTERSINSTALLED = 262980
esriOutputErrorReturnCodes = c_int # enum
ITrackCancelSetup._methods_ = [
    COMMETHOD(['propput', helpstring(u'Reacts to a Cancel.')], HRESULT, 'TrackCancel',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'rhs' )),
]
################################################################
## code template for ITrackCancelSetup implementation
##class ITrackCancelSetup_Impl(object):
##    def _set(self, rhs):
##        u'Reacts to a Cancel.'
##    TrackCancel = property(fset = _set, doc = _set.__doc__)
##

IJpegExporter._methods_ = [
    COMMETHOD(['propput', helpstring(u'The background color of the JPEG.')], HRESULT, 'BackgroundColor',
              ( ['in'], POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IColor), 'ppBackgroundColor' )),
    COMMETHOD(['propget', helpstring(u'The background color of the JPEG.')], HRESULT, 'BackgroundColor',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IColor)), 'ppBackgroundColor' )),
    COMMETHOD(['propput', helpstring(u'The width of the JPEG. If width or height is zero, screen size is used.')], HRESULT, 'Width',
              ( ['in'], c_short, 'pWidth' )),
    COMMETHOD(['propget', helpstring(u'The width of the JPEG. If width or height is zero, screen size is used.')], HRESULT, 'Width',
              ( ['retval', 'out'], POINTER(c_short), 'pWidth' )),
    COMMETHOD(['propput', helpstring(u'The height of the JPEG. If width or height is zero, screen size is used.')], HRESULT, 'Height',
              ( ['in'], c_short, 'pHeight' )),
    COMMETHOD(['propget', helpstring(u'The height of the JPEG. If width or height is zero, screen size is used.')], HRESULT, 'Height',
              ( ['retval', 'out'], POINTER(c_short), 'pHeight' )),
    COMMETHOD(['propput', helpstring(u'The JPEG compression / image quality.')], HRESULT, 'Quality',
              ( ['in'], c_short, 'Quality' )),
    COMMETHOD(['propget', helpstring(u'The JPEG compression / image quality.')], HRESULT, 'Quality',
              ( ['retval', 'out'], POINTER(c_short), 'Quality' )),
]
################################################################
## code template for IJpegExporter implementation
##class IJpegExporter_Impl(object):
##    def _get(self):
##        u'The width of the JPEG. If width or height is zero, screen size is used.'
##        #return pWidth
##    def _set(self, pWidth):
##        u'The width of the JPEG. If width or height is zero, screen size is used.'
##    Width = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The JPEG compression / image quality.'
##        #return Quality
##    def _set(self, Quality):
##        u'The JPEG compression / image quality.'
##    Quality = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The background color of the JPEG.'
##        #return ppBackgroundColor
##    def _set(self, ppBackgroundColor):
##        u'The background color of the JPEG.'
##    BackgroundColor = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The height of the JPEG. If width or height is zero, screen size is used.'
##        #return pHeight
##    def _set(self, pHeight):
##        u'The height of the JPEG. If width or height is zero, screen size is used.'
##    Height = property(_get, _set, doc = _set.__doc__)
##


# values for enumeration 'esriPDFExtensionErrorCodes'
E_PDFEXTENSIONERROR = -2147220667
E_NEEDPASSWD = -2147220666
E_INSUFFICIENTMEMORY = -2147220665
E_TOOMANYPAGESFOROPEN = -2147220664
E_OPNOTPERMITTED = -2147220663
E_UNABLEOPENDOC = -2147220662
E_UNABLEOPENDOCFORWRITING = -2147220661
E_UNABLEWRITINGDOC = -2147220660
E_UNABLERENTEMPFILE = -2147220659
E_UNABLEREADILE = -2147220658
E_UNKNOWNFILETYPE = -2147220657
E_FILEALREADYOPEN = -2147220656
E_NOSPACEFORTEMPFILE = -2147220655
E_TOOMANYPAGESFORINSERT = -2147220655
E_AFTERSAVE = -2147220654
E_FILEERROR = -2147220653
E_DIRFULL = -2147220652
E_DISKFULL = -2147220651
E_FILEIO = -2147220650
E_FILEREAD = -2147220649
E_FILEWRITE = -2147220648
E_FILELOCKED = -2147220647
E_FILEEXISTS = -2147220646
E_FILEINUSE = -2147220645
E_FILEACCESSDENIED = -2147220644
E_FILEACCESSNOWRITE = -2147220643
E_FILENOTFOUND = -2147220642
E_FILEOPENFAILED = -2147220641
E_METADATABADXMP = -2147220640
E_METADATASYNTXERR = -2147220639
E_XAPCREATIONERR = -2147220638
E_METADATAINTERNAL = -2147220637
E_INTERROR = -2147220636
E_OUTMEMORY = -2147220635
E_BADPARAMETER = -2147220634
E_USERCANCEL = -2147220633
esriPDFExtensionErrorCodes = c_int # enum

# values for enumeration 'esriPDFExtensionSecurityPermission'
esriPDFExtensionSecurityPermissionNone = 0
esriPDFExtensionSecurityPermissionOpen = 1
esriPDFExtensionSecurityPermissionSecure = 2
esriPDFExtensionSecurityPermissionPrint = 4
esriPDFExtensionSecurityPermissionEdit = 8
esriPDFExtensionSecurityPermissionCopy = 16
esriPDFExtensionSecurityPermissionEditNotes = 32
esriPDFExtensionSecurityPermissionFillAndSign = 256
esriPDFExtensionSecurityPermissionAccessible = 512
esriPDFExtensionSecurityPermissionDocAssembly = 1024
esriPDFExtensionSecurityPermissionHighPrint = 2052
esriPDFExtensionSecurityFormSpawnTempl = 131072
esriPDFExtensionSecurityPermissionAll = -268435457
esriPDFExtensionSecurityPermissionAllMaster = 2108
esriPDFExtensionSecurityPermission = c_int # enum
IOutputCleanup._methods_ = [
    COMMETHOD([helpstring(u'Cleanup should clean all temporary files, free used memory, etc...')], HRESULT, 'Cleanup'),
]
################################################################
## code template for IOutputCleanup implementation
##class IOutputCleanup_Impl(object):
##    def Cleanup(self):
##        u'Cleanup should clean all temporary files, free used memory, etc...'
##        #return 
##

class IPDFDriver(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Superseded by IExportPDF. Provides access to members that control the PDF (Portable Document Format) Driver.'
    _iid_ = GUID('{0201602D-1521-11D3-9F97-00C04F6BC8DD}')
    _idlflags_ = ['oleautomation']
IPDFDriver._methods_ = [
    COMMETHOD(['propget', helpstring(u'The Font Map Collection for Font Mapping.')], HRESULT, 'FontMapCollection',
              ( ['retval', 'out'], POINTER(POINTER(IFontMapCollection)), 'FontMapCollection' )),
    COMMETHOD(['propputref', helpstring(u'The Font Map Collection for Font Mapping.')], HRESULT, 'FontMapCollection',
              ( ['in'], POINTER(IFontMapCollection), 'FontMapCollection' )),
    COMMETHOD([helpstring(u'Converts the EMF file to a PDF File.')], HRESULT, 'CreatePDF',
              ( ['in'], BSTR, 'InputFileName' ),
              ( ['in'], BSTR, 'OutputFileName' )),
]
################################################################
## code template for IPDFDriver implementation
##class IPDFDriver_Impl(object):
##    def FontMapCollection(self, FontMapCollection):
##        u'The Font Map Collection for Font Mapping.'
##        #return 
##
##    def CreatePDF(self, InputFileName, OutputFileName):
##        u'Converts the EMF file to a PDF File.'
##        #return 
##


# values for enumeration 'esriPSDriverSeparates'
esriPSDriverSeparateCyan = 1
esriPSDriverSeparateMagenta = 2
esriPSDriverSeparateYellow = 3
esriPSDriverSeparateBlack = 4
esriPSDriverSeparateCustom = 5
esriPSDriverSeparates = c_int # enum
class TiffExporter(CoClass):
    u'Superseded by ExportTIFF. Class used to export maps to TIFF (Tag Image File Format).'
    _reg_clsid_ = GUID('{39C10487-B0FA-4F2B-AC7B-C76E0BCE9A95}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7DB92CEC-CB65-420A-8737-FCD0722FD436}', 10, 2)
class IExporter2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Superseded by IExport. Provides access to members that control the Base Exporter 2.'
    _iid_ = GUID('{B87AD35E-1242-4C30-B67F-FF3CFA2F1928}')
    _idlflags_ = ['oleautomation']
class ITiffExporter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Superseded by IExportTIFF. Provides access to members that control the TIFF exporter.'
    _iid_ = GUID('{71001418-565A-4588-90B7-3FFB04B74BE7}')
    _idlflags_ = ['oleautomation']
TiffExporter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IExporter, IExporter2, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo, ITiffExporter, IExporterPriority, IOutputCleanup, IStepProgressorSetup, ITrackCancelSetup, IWorldFileSettings]

class IBmpExporter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Superseded by IExportBMP. Provides access to members that control the BMP (Windows Bitmap) Exporter.'
    _iid_ = GUID('{4C59F34D-DB32-11D3-9FF6-00C04F6BC8DD}')
    _idlflags_ = ['oleautomation']
IBmpExporter._methods_ = [
    COMMETHOD(['propget', helpstring(u'The Windows Bitmap handle.')], HRESULT, 'Bitmap',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'hBmp' )),
    COMMETHOD(['propget', helpstring(u'The Windows Bitmap color palette.')], HRESULT, 'Palette',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'hPal' )),
]
################################################################
## code template for IBmpExporter implementation
##class IBmpExporter_Impl(object):
##    @property
##    def Palette(self):
##        u'The Windows Bitmap color palette.'
##        #return hPal
##
##    @property
##    def Bitmap(self):
##        u'The Windows Bitmap handle.'
##        #return hBmp
##


# values for enumeration 'esriPDFExtensionSecurityEncryptionMethod'
esriPDFExtensionSecurityEncryptionMethodRC4_V2 = 2
esriPDFExtensionSecurityEncryptionMethodAES_V1 = 5
esriPDFExtensionSecurityEncryptionMethodAES_V2 = 6
esriPDFExtensionSecurityEncryptionMethod = c_int # enum
IExportPDFPasswordSecurity._methods_ = [
    COMMETHOD(['propput', helpstring(u'User password, allows to open the PDF document.')], HRESULT, 'UserPassword',
              ( ['in'], BSTR, 'pPasswd' )),
    COMMETHOD(['propget', helpstring(u'User password, allows to open the PDF document.')], HRESULT, 'UserPassword',
              ( ['retval', 'out'], POINTER(BSTR), 'pPasswd' )),
    COMMETHOD(['propput', helpstring(u'Master password, allows to restrict editing security and permission settings of PDF document.')], HRESULT, 'MasterPassword',
              ( ['in'], BSTR, 'pPasswd' )),
    COMMETHOD(['propget', helpstring(u'Master password, allows to restrict editing security and permission settings of PDF document.')], HRESULT, 'MasterPassword',
              ( ['retval', 'out'], POINTER(BSTR), 'pPasswd' )),
    COMMETHOD(['propput', helpstring(u'PDF security permissions.')], HRESULT, 'SecurityPermissions',
              ( ['in'], c_int, 'pPermission' )),
    COMMETHOD(['propget', helpstring(u'PDF security permissions.')], HRESULT, 'SecurityPermissions',
              ( ['retval', 'out'], POINTER(c_int), 'pPermission' )),
    COMMETHOD(['propput', helpstring(u'PDF security encryption options.')], HRESULT, 'SecurityEncryptionOption',
              ( ['in'], esriPDFExtensionSecurityEncryptionOption, 'pEncryptionOption' )),
    COMMETHOD(['propget', helpstring(u'PDF security encryption options.')], HRESULT, 'SecurityEncryptionOption',
              ( ['retval', 'out'], POINTER(esriPDFExtensionSecurityEncryptionOption), 'pEncryptionOption' )),
    COMMETHOD(['propput', helpstring(u'PDF security encryption methods.')], HRESULT, 'SecurityEncryptionMethod',
              ( ['in'], esriPDFExtensionSecurityEncryptionMethod, 'pEncryptionMethod' )),
    COMMETHOD(['propget', helpstring(u'PDF security encryption methods.')], HRESULT, 'SecurityEncryptionMethod',
              ( ['retval', 'out'], POINTER(esriPDFExtensionSecurityEncryptionMethod), 'pEncryptionMethod' )),
]
################################################################
## code template for IExportPDFPasswordSecurity implementation
##class IExportPDFPasswordSecurity_Impl(object):
##    def _get(self):
##        u'PDF security permissions.'
##        #return pPermission
##    def _set(self, pPermission):
##        u'PDF security permissions.'
##    SecurityPermissions = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'User password, allows to open the PDF document.'
##        #return pPasswd
##    def _set(self, pPasswd):
##        u'User password, allows to open the PDF document.'
##    UserPassword = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'PDF security encryption options.'
##        #return pEncryptionOption
##    def _set(self, pEncryptionOption):
##        u'PDF security encryption options.'
##    SecurityEncryptionOption = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'PDF security encryption methods.'
##        #return pEncryptionMethod
##    def _set(self, pEncryptionMethod):
##        u'PDF security encryption methods.'
##    SecurityEncryptionMethod = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Master password, allows to restrict editing security and permission settings of PDF document.'
##        #return pPasswd
##    def _set(self, pPasswd):
##        u'Master password, allows to restrict editing security and permission settings of PDF document.'
##    MasterPassword = property(_get, _set, doc = _set.__doc__)
##

IFontMap._methods_ = [
    COMMETHOD(['propget', helpstring(u'Creates an association between the TrueType Font and the Mapped Font.')], HRESULT, 'TrueTypeFont',
              ( ['retval', 'out'], POINTER(BSTR), 'font' )),
    COMMETHOD(['propget', helpstring(u'Creates an association between the TrueType Font and the Mapped Font.')], HRESULT, 'MappedFont',
              ( ['retval', 'out'], POINTER(BSTR), 'font' )),
    COMMETHOD(['propput', helpstring(u'Creates an association between the TrueType Font and the Mapped Font.')], HRESULT, 'Mapping',
              ( ['in'], BSTR, 'TrueTypeFont' ),
              ( ['in'], BSTR, 'rhs' )),
]
################################################################
## code template for IFontMap implementation
##class IFontMap_Impl(object):
##    @property
##    def TrueTypeFont(self):
##        u'Creates an association between the TrueType Font and the Mapped Font.'
##        #return font
##
##    @property
##    def MappedFont(self):
##        u'Creates an association between the TrueType Font and the Mapped Font.'
##        #return font
##
##    def _set(self, TrueTypeFont, rhs):
##        u'Creates an association between the TrueType Font and the Mapped Font.'
##    Mapping = property(fset = _set, doc = _set.__doc__)
##

class FontMapCollection(CoClass):
    u'A collection of font mappings.'
    _reg_clsid_ = GUID('{EB0E7543-2D97-11D3-9FC6-00C04F6BC8DD}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7DB92CEC-CB65-420A-8737-FCD0722FD436}', 10, 2)
FontMapCollection._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IFontMapCollection]


# values for enumeration 'esriGIFCompression'
esriGIFCompressionNone = 0
esriGIFCompressionRLE = 1
esriGIFCompressionLZW = 3
esriGIFCompression = c_int # enum
IExportGIF._methods_ = [
    COMMETHOD(['propput', helpstring(u'The interlaced GIF export mode.')], HRESULT, 'InterlaceMode',
              ( ['in'], VARIANT_BOOL, 'interlace' )),
    COMMETHOD(['propget', helpstring(u'The interlaced GIF export mode.')], HRESULT, 'InterlaceMode',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'interlace' )),
    COMMETHOD(['propput', helpstring(u'The GIF Compression type.')], HRESULT, 'CompressionType',
              ( ['in'], esriGIFCompression, 'type' )),
    COMMETHOD(['propget', helpstring(u'The GIF Compression type.')], HRESULT, 'CompressionType',
              ( ['retval', 'out'], POINTER(esriGIFCompression), 'type' )),
    COMMETHOD(['propput', helpstring(u'The color that is marked as transparent in the export image.')], HRESULT, 'TransparentColor',
              ( ['in'], POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IColor), 'Color' )),
    COMMETHOD(['propget', helpstring(u'The color that is marked as transparent in the export image.')], HRESULT, 'TransparentColor',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IColor)), 'Color' )),
    COMMETHOD(['propput', helpstring(u'The Threshold value for BiLevel images. The Threshold value will be used if esriExportImageType equal to esriExportImageTypeBiLevelThreshold.')], HRESULT, 'BiLevelThreshold',
              ( ['in'], c_int, 'threshold' )),
    COMMETHOD(['propget', helpstring(u'The Threshold value for BiLevel images. The Threshold value will be used if esriExportImageType equal to esriExportImageTypeBiLevelThreshold.')], HRESULT, 'BiLevelThreshold',
              ( ['retval', 'out'], POINTER(c_int), 'threshold' )),
]
################################################################
## code template for IExportGIF implementation
##class IExportGIF_Impl(object):
##    def _get(self):
##        u'The Threshold value for BiLevel images. The Threshold value will be used if esriExportImageType equal to esriExportImageTypeBiLevelThreshold.'
##        #return threshold
##    def _set(self, threshold):
##        u'The Threshold value for BiLevel images. The Threshold value will be used if esriExportImageType equal to esriExportImageTypeBiLevelThreshold.'
##    BiLevelThreshold = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The GIF Compression type.'
##        #return type
##    def _set(self, type):
##        u'The GIF Compression type.'
##    CompressionType = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The color that is marked as transparent in the export image.'
##        #return Color
##    def _set(self, Color):
##        u'The color that is marked as transparent in the export image.'
##    TransparentColor = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The interlaced GIF export mode.'
##        #return interlace
##    def _set(self, interlace):
##        u'The interlaced GIF export mode.'
##    InterlaceMode = property(_get, _set, doc = _set.__doc__)
##

IPaper2._methods_ = [
    COMMETHOD(['propget', helpstring(u'The print resolution.')], HRESULT, 'Resolution',
              ( ['retval', 'out'], POINTER(c_short), 'Resolution' )),
]
################################################################
## code template for IPaper2 implementation
##class IPaper2_Impl(object):
##    @property
##    def Resolution(self):
##        u'The print resolution.'
##        #return Resolution
##

class IExportJPEG(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the JPEG (Joint Photographic Experts Group) Export.'
    _iid_ = GUID('{8746BB14-4C79-42F0-B0F1-3327651EB378}')
    _idlflags_ = ['oleautomation']
IExportJPEG._methods_ = [
    COMMETHOD(['propput', helpstring(u'The JPEG compression / image quality. Range (0..100). Default is 100 (no compression / best quality).')], HRESULT, 'Quality',
              ( ['in'], c_short, 'Quality' )),
    COMMETHOD(['propget', helpstring(u'The JPEG compression / image quality. Range (0..100). Default is 100 (no compression / best quality).')], HRESULT, 'Quality',
              ( ['retval', 'out'], POINTER(c_short), 'Quality' )),
    COMMETHOD(['propput', helpstring(u'The progressive JPEG export mode.')], HRESULT, 'ProgressiveMode',
              ( ['in'], VARIANT_BOOL, 'bprogressive' )),
    COMMETHOD(['propget', helpstring(u'The progressive JPEG export mode.')], HRESULT, 'ProgressiveMode',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bprogressive' )),
]
################################################################
## code template for IExportJPEG implementation
##class IExportJPEG_Impl(object):
##    def _get(self):
##        u'The JPEG compression / image quality. Range (0..100). Default is 100 (no compression / best quality).'
##        #return Quality
##    def _set(self, Quality):
##        u'The JPEG compression / image quality. Range (0..100). Default is 100 (no compression / best quality).'
##    Quality = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The progressive JPEG export mode.'
##        #return bprogressive
##    def _set(self, bprogressive):
##        u'The progressive JPEG export mode.'
##    ProgressiveMode = property(_get, _set, doc = _set.__doc__)
##

ISettingsInRegistry._methods_ = [
    COMMETHOD([helpstring(u'Restore object settings.')], HRESULT, 'RestoreForCurrentUser',
              ( ['in'], BSTR, 'bstrRegPath' )),
    COMMETHOD([helpstring(u'Store object settings.')], HRESULT, 'StoreForCurrentUser',
              ( ['in'], BSTR, 'bstrRegPath' )),
    COMMETHOD([helpstring(u'Restore the default object settings.')], HRESULT, 'RestoreDefault'),
]
################################################################
## code template for ISettingsInRegistry implementation
##class ISettingsInRegistry_Impl(object):
##    def StoreForCurrentUser(self, bstrRegPath):
##        u'Store object settings.'
##        #return 
##
##    def RestoreDefault(self):
##        u'Restore the default object settings.'
##        #return 
##
##    def RestoreForCurrentUser(self, bstrRegPath):
##        u'Restore object settings.'
##        #return 
##

class SpotPlate(CoClass):
    u'Class used to print maps with a PostScript Spot Plate.'
    _reg_clsid_ = GUID('{481614E5-9407-11D1-9127-0000F87808EE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7DB92CEC-CB65-420A-8737-FCD0722FD436}', 10, 2)
SpotPlate._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ISpotPlate, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

IPrinter._methods_ = [
    COMMETHOD(['propget', helpstring(u'Name of the IPrinter Driver.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'Filter used in CFileDialog.')], HRESULT, 'Filter',
              ( ['retval', 'out'], POINTER(BSTR), 'Filter' )),
    COMMETHOD(['propget', helpstring(u'File Extension associated with the Printer Driver.')], HRESULT, 'FileExtension',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propput', helpstring(u'The name of file if saving to Disk.')], HRESULT, 'PrintToFile',
              ( ['in'], BSTR, 'fileName' )),
    COMMETHOD(['propget', helpstring(u'The name of file if saving to Disk.')], HRESULT, 'PrintToFile',
              ( ['retval', 'out'], POINTER(BSTR), 'fileName' )),
    COMMETHOD(['propget', helpstring(u'The name of Windows Printer Driver.')], HRESULT, 'DriverName',
              ( ['retval', 'out'], POINTER(BSTR), 'DriverName' )),
    COMMETHOD(['propput', helpstring(u'The Spool File Name which shows up in the Print Manager.')], HRESULT, 'SpoolFileName',
              ( ['in'], BSTR, 'SpoolFileName' )),
    COMMETHOD(['propget', helpstring(u'The Spool File Name which shows up in the Print Manager.')], HRESULT, 'SpoolFileName',
              ( ['retval', 'out'], POINTER(BSTR), 'SpoolFileName' )),
    COMMETHOD(['propput', helpstring(u'The Printer Driver Resolution.')], HRESULT, 'Resolution',
              ( ['in'], c_short, 'res' )),
    COMMETHOD(['propget', helpstring(u'The Printer Driver Resolution.')], HRESULT, 'Resolution',
              ( ['retval', 'out'], POINTER(c_short), 'res' )),
    COMMETHOD(['propput', helpstring(u'Updates a Progress Bar is set.')], HRESULT, 'StepProgressor',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStepProgressor), 'rhs' )),
    COMMETHOD(['propputref', helpstring(u'The IPaper interface.')], HRESULT, 'Paper',
              ( ['in'], POINTER(IPaper), 'Paper' )),
    COMMETHOD(['propget', helpstring(u'The IPaper interface.')], HRESULT, 'Paper',
              ( ['retval', 'out'], POINTER(POINTER(IPaper)), 'Paper' )),
    COMMETHOD([helpstring(u'Returns Page Size for Printer.')], HRESULT, 'QueryPaperSize',
              ( ['out'], POINTER(c_double), 'Width' ),
              ( ['out'], POINTER(c_double), 'Height' )),
    COMMETHOD(['propget', helpstring(u'The area of the printer page that can be printed on.')], HRESULT, 'PrintableBounds',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'bounds' )),
    COMMETHOD(['propget', helpstring(u'The units for PaperSize and PrintableBounds.')], HRESULT, 'Units',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.esriUnits), 'Units' )),
    COMMETHOD([helpstring(u"Indicates if the Printer Driver should validate Printer Driver's local settings.")], HRESULT, 'VerifyDriverSettings',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ok' )),
    COMMETHOD([helpstring(u'Indicates if the Printer Name passed into function is supported by the IPrinter Driver.')], HRESULT, 'DoesDriverSupportPrinter',
              ( ['in'], BSTR, 'PrinterName' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'supported' )),
    COMMETHOD([helpstring(u'Initialize Printing.')], HRESULT, 'StartPrinting',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'PixelBounds' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hDcPrinter' ),
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'hDcRet' )),
    COMMETHOD([helpstring(u'Finish up Printing.')], HRESULT, 'FinishPrinting'),
]
################################################################
## code template for IPrinter implementation
##class IPrinter_Impl(object):
##    def FinishPrinting(self):
##        u'Finish up Printing.'
##        #return 
##
##    def DoesDriverSupportPrinter(self, PrinterName):
##        u'Indicates if the Printer Name passed into function is supported by the IPrinter Driver.'
##        #return supported
##
##    def _get(self):
##        u'The Spool File Name which shows up in the Print Manager.'
##        #return SpoolFileName
##    def _set(self, SpoolFileName):
##        u'The Spool File Name which shows up in the Print Manager.'
##    SpoolFileName = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Name(self):
##        u'Name of the IPrinter Driver.'
##        #return Name
##
##    def QueryPaperSize(self):
##        u'Returns Page Size for Printer.'
##        #return Width, Height
##
##    @property
##    def Filter(self):
##        u'Filter used in CFileDialog.'
##        #return Filter
##
##    @property
##    def Units(self):
##        u'The units for PaperSize and PrintableBounds.'
##        #return Units
##
##    def StartPrinting(self, PixelBounds, hDcPrinter):
##        u'Initialize Printing.'
##        #return hDcRet
##
##    @property
##    def Paper(self, Paper):
##        u'The IPaper interface.'
##        #return 
##
##    @property
##    def DriverName(self):
##        u'The name of Windows Printer Driver.'
##        #return DriverName
##
##    def _get(self):
##        u'The name of file if saving to Disk.'
##        #return fileName
##    def _set(self, fileName):
##        u'The name of file if saving to Disk.'
##    PrintToFile = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def FileExtension(self):
##        u'File Extension associated with the Printer Driver.'
##        #return Name
##
##    def _set(self, rhs):
##        u'Updates a Progress Bar is set.'
##    StepProgressor = property(fset = _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The Printer Driver Resolution.'
##        #return res
##    def _set(self, res):
##        u'The Printer Driver Resolution.'
##    Resolution = property(_get, _set, doc = _set.__doc__)
##
##    def VerifyDriverSettings(self):
##        u"Indicates if the Printer Driver should validate Printer Driver's local settings."
##        #return ok
##
##    @property
##    def PrintableBounds(self):
##        u'The area of the printer page that can be printed on.'
##        #return bounds
##

IExportColorspaceSettings._methods_ = [
    COMMETHOD(['propput', helpstring(u'Colorspace option.')], HRESULT, 'Colorspace',
              ( ['in'], esriExportColorspace, 'pcolorspace' )),
    COMMETHOD(['propget', helpstring(u'Colorspace option.')], HRESULT, 'Colorspace',
              ( ['retval', 'out'], POINTER(esriExportColorspace), 'pcolorspace' )),
]
################################################################
## code template for IExportColorspaceSettings implementation
##class IExportColorspaceSettings_Impl(object):
##    def _get(self):
##        u'Colorspace option.'
##        #return pcolorspace
##    def _set(self, pcolorspace):
##        u'Colorspace option.'
##    Colorspace = property(_get, _set, doc = _set.__doc__)
##

class DibExporter(CoClass):
    u'Superseded by ExportBMP. Class used to export maps to DIB (Device Independant Bitmap) format. Format also known as BMP.'
    _reg_clsid_ = GUID('{20CD4013-8F3D-11D0-8590-0800091A2A72}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7DB92CEC-CB65-420A-8737-FCD0722FD436}', 10, 2)
DibExporter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDibExporter, IBmpExporter, IExporter, IExporter2, IExporterPriority, IWorldFileSettings, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo, IOutputCleanup, IStepProgressorSetup, ITrackCancelSetup]

IPSDriver2._methods_ = [
    COMMETHOD(['propget', helpstring(u'The number of copies.')], HRESULT, 'Copies',
              ( ['retval', 'out'], POINTER(c_short), 'Copies' )),
    COMMETHOD(['propput', helpstring(u'The number of copies.')], HRESULT, 'Copies',
              ( ['in'], c_short, 'Copies' )),
    COMMETHOD(['propget', helpstring(u'The Image Compression of the PostScript Driver.')], HRESULT, 'ImageCompression',
              ( ['retval', 'out'], POINTER(esriPSDriverImageCompression), 'ImageCompression' )),
    COMMETHOD(['propput', helpstring(u'The Image Compression of the PostScript Driver.')], HRESULT, 'ImageCompression',
              ( ['in'], esriPSDriverImageCompression, 'ImageCompression' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether a separate Image file should be created for ArcPress.')], HRESULT, 'ArcPressSeparateImage',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'sepImage' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether a separate Image file should be created for ArcPress.')], HRESULT, 'ArcPressSeparateImage',
              ( ['in'], VARIANT_BOOL, 'sepImage' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the Image should be rotated 90 degress for ArcPress.')], HRESULT, 'ArcPressSeparateImageRotate',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'sepImage' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether the Image should be rotated 90 degress for ArcPress.')], HRESULT, 'ArcPressSeparateImageRotate',
              ( ['in'], VARIANT_BOOL, 'sepImage' )),
    COMMETHOD(['propget', helpstring(u'The Font Map Collection for Font Mapping.')], HRESULT, 'FontMapCollection',
              ( ['retval', 'out'], POINTER(POINTER(IFontMapCollection)), 'FontMapCollection' )),
    COMMETHOD(['propputref', helpstring(u'The Font Map Collection for Font Mapping.')], HRESULT, 'FontMapCollection',
              ( ['in'], POINTER(IFontMapCollection), 'FontMapCollection' )),
    COMMETHOD(['propget', helpstring(u'The PPD (PostScript Printer Description) file to be used.')], HRESULT, 'PPDFile',
              ( ['retval', 'out'], POINTER(BSTR), 'PPDFile' )),
    COMMETHOD(['propput', helpstring(u'The PPD (PostScript Printer Description) file to be used.')], HRESULT, 'PPDFile',
              ( ['in'], BSTR, 'PPDFile' )),
    COMMETHOD(['propget', helpstring(u'The PostScript Marks.')], HRESULT, 'Marks',
              ( ['retval', 'out'], POINTER(c_short), 'Marks' )),
    COMMETHOD(['propput', helpstring(u'The PostScript Marks.')], HRESULT, 'Marks',
              ( ['in'], c_short, 'Marks' )),
    COMMETHOD(['propget', helpstring(u'The Halftone DPI / LPI.')], HRESULT, 'HalfTone',
              ( ['in'], esriPSDriverHalfTone, 'HalfTone' ),
              ( ['retval', 'out'], POINTER(c_int), 'value' )),
    COMMETHOD(['propput', helpstring(u'The Halftone DPI / LPI.')], HRESULT, 'HalfTone',
              ( ['in'], esriPSDriverHalfTone, 'HalfTone' ),
              ( ['in'], c_int, 'value' )),
    COMMETHOD(['propget', helpstring(u'The printer page form. Use Win32 DMPAPER_xxx constants.')], HRESULT, 'FormName',
              ( ['retval', 'out'], POINTER(BSTR), 'FormName' )),
    COMMETHOD(['propput', helpstring(u'The printer page form. Use Win32 DMPAPER_xxx constants.')], HRESULT, 'FormName',
              ( ['in'], BSTR, 'FormName' )),
    COMMETHOD(['propget', helpstring(u'The printers Printable Bounds - Used for Marks.')], HRESULT, 'PrintableBounds',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'ppBounds' )),
    COMMETHOD(['propput', helpstring(u'The printers Printable Bounds - Used for Marks.')], HRESULT, 'PrintableBounds',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'ppBounds' )),
    COMMETHOD(['propget', helpstring(u'The printer page orientation (1 = portrait.  2 = landscape).')], HRESULT, 'Orientation',
              ( ['retval', 'out'], POINTER(c_short), 'Orientation' )),
    COMMETHOD(['propput', helpstring(u'The printer page orientation (1 = portrait.  2 = landscape).')], HRESULT, 'Orientation',
              ( ['in'], c_short, 'Orientation' )),
    COMMETHOD(['propget', helpstring(u'The Emulsion setting for the PostScript Driver.')], HRESULT, 'Emulsion',
              ( ['retval', 'out'], POINTER(esriPSDriverEmulsion), 'Emulsion' )),
    COMMETHOD(['propput', helpstring(u'The Emulsion setting for the PostScript Driver.')], HRESULT, 'Emulsion',
              ( ['in'], esriPSDriverEmulsion, 'Emulsion' )),
    COMMETHOD(['propget', helpstring(u'The Image setting (Positive or Negative) for the PostScript Driver.')], HRESULT, 'Image',
              ( ['retval', 'out'], POINTER(esriPSDriverImage), 'Image' )),
    COMMETHOD(['propput', helpstring(u'The Image setting (Positive or Negative) for the PostScript Driver.')], HRESULT, 'Image',
              ( ['in'], esriPSDriverImage, 'Image' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the 1-bit Image Transparency setting for the PostScript Driver is set to true.')], HRESULT, 'OneBitImageTransparency',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'imageTransparency' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the 1-bit Image Transparency setting for the PostScript Driver is set to true.')], HRESULT, 'OneBitImageTransparency',
              ( ['in'], VARIANT_BOOL, 'imageTransparency' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the PostScript Driver should use the ENHMETAHEADER rclFrame instead of rclBounds for the PostScript Bounding Box.')], HRESULT, 'UseEMFFrameBoxForPSBoundingBox',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'useFrameBox' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether the PostScript Driver should use the ENHMETAHEADER rclFrame instead of rclBounds for the PostScript Bounding Box.')], HRESULT, 'UseEMFFrameBoxForPSBoundingBox',
              ( ['in'], VARIANT_BOOL, 'useFrameBox' )),
    COMMETHOD(['propget', helpstring(u'The PostScript Driver Language Level.')], HRESULT, 'PSLanguageLevel',
              ( ['retval', 'out'], POINTER(esriPSDriverPSLanguageLevel), 'pslevel' )),
    COMMETHOD(['propput', helpstring(u'The PostScript Driver Language Level.')], HRESULT, 'PSLanguageLevel',
              ( ['in'], esriPSDriverPSLanguageLevel, 'pslevel' )),
    COMMETHOD(['propput', helpstring(u'PostScript Driver will update a Progress Bar.')], HRESULT, 'StepProgressor',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStepProgressor), 'rhs' )),
    COMMETHOD([helpstring(u'Converts the EMF file to a EPS File.')], HRESULT, 'CreatePS',
              ( ['in'], BSTR, 'InputFileName' ),
              ( ['in'], BSTR, 'OutputFileName' )),
]
################################################################
## code template for IPSDriver2 implementation
##class IPSDriver2_Impl(object):
##    def _get(self):
##        u'Indicates if the 1-bit Image Transparency setting for the PostScript Driver is set to true.'
##        #return imageTransparency
##    def _set(self, imageTransparency):
##        u'Indicates if the 1-bit Image Transparency setting for the PostScript Driver is set to true.'
##    OneBitImageTransparency = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The printers Printable Bounds - Used for Marks.'
##        #return ppBounds
##    def _set(self, ppBounds):
##        u'The printers Printable Bounds - Used for Marks.'
##    PrintableBounds = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether the Image should be rotated 90 degress for ArcPress.'
##        #return sepImage
##    def _set(self, sepImage):
##        u'Indicates whether the Image should be rotated 90 degress for ArcPress.'
##    ArcPressSeparateImageRotate = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The Image setting (Positive or Negative) for the PostScript Driver.'
##        #return Image
##    def _set(self, Image):
##        u'The Image setting (Positive or Negative) for the PostScript Driver.'
##    Image = property(_get, _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'PostScript Driver will update a Progress Bar.'
##    StepProgressor = property(fset = _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The number of copies.'
##        #return Copies
##    def _set(self, Copies):
##        u'The number of copies.'
##    Copies = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self, HalfTone):
##        u'The Halftone DPI / LPI.'
##        #return value
##    def _set(self, HalfTone, value):
##        u'The Halftone DPI / LPI.'
##    HalfTone = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The PostScript Driver Language Level.'
##        #return pslevel
##    def _set(self, pslevel):
##        u'The PostScript Driver Language Level.'
##    PSLanguageLevel = property(_get, _set, doc = _set.__doc__)
##
##    def CreatePS(self, InputFileName, OutputFileName):
##        u'Converts the EMF file to a EPS File.'
##        #return 
##
##    def _get(self):
##        u'The Emulsion setting for the PostScript Driver.'
##        #return Emulsion
##    def _set(self, Emulsion):
##        u'The Emulsion setting for the PostScript Driver.'
##    Emulsion = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The PostScript Marks.'
##        #return Marks
##    def _set(self, Marks):
##        u'The PostScript Marks.'
##    Marks = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether a separate Image file should be created for ArcPress.'
##        #return sepImage
##    def _set(self, sepImage):
##        u'Indicates whether a separate Image file should be created for ArcPress.'
##    ArcPressSeparateImage = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The PPD (PostScript Printer Description) file to be used.'
##        #return PPDFile
##    def _set(self, PPDFile):
##        u'The PPD (PostScript Printer Description) file to be used.'
##    PPDFile = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The printer page orientation (1 = portrait.  2 = landscape).'
##        #return Orientation
##    def _set(self, Orientation):
##        u'The printer page orientation (1 = portrait.  2 = landscape).'
##    Orientation = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The printer page form. Use Win32 DMPAPER_xxx constants.'
##        #return FormName
##    def _set(self, FormName):
##        u'The printer page form. Use Win32 DMPAPER_xxx constants.'
##    FormName = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether the PostScript Driver should use the ENHMETAHEADER rclFrame instead of rclBounds for the PostScript Bounding Box.'
##        #return useFrameBox
##    def _set(self, useFrameBox):
##        u'Indicates whether the PostScript Driver should use the ENHMETAHEADER rclFrame instead of rclBounds for the PostScript Bounding Box.'
##    UseEMFFrameBoxForPSBoundingBox = property(_get, _set, doc = _set.__doc__)
##
##    def FontMapCollection(self, FontMapCollection):
##        u'The Font Map Collection for Font Mapping.'
##        #return 
##
##    def _get(self):
##        u'The Image Compression of the PostScript Driver.'
##        #return ImageCompression
##    def _set(self, ImageCompression):
##        u'The Image Compression of the PostScript Driver.'
##    ImageCompression = property(_get, _set, doc = _set.__doc__)
##

ITiffExporter._methods_ = [
    COMMETHOD(['propput', helpstring(u'The background color of the TIFF.')], HRESULT, 'BackgroundColor',
              ( ['in'], POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IColor), 'ppBackgroundColor' )),
    COMMETHOD(['propget', helpstring(u'The background color of the TIFF.')], HRESULT, 'BackgroundColor',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IColor)), 'ppBackgroundColor' )),
    COMMETHOD(['propput', helpstring(u'The width of the TIFF.  If width or height is zero, screen size is used.')], HRESULT, 'Width',
              ( ['in'], c_short, 'pWidth' )),
    COMMETHOD(['propget', helpstring(u'The width of the TIFF.  If width or height is zero, screen size is used.')], HRESULT, 'Width',
              ( ['retval', 'out'], POINTER(c_short), 'pWidth' )),
    COMMETHOD(['propput', helpstring(u'The height of the TIFF.  If width or height is zero, screen size is used.')], HRESULT, 'Height',
              ( ['in'], c_short, 'pHeight' )),
    COMMETHOD(['propget', helpstring(u'The height of the TIFF.  If width or height is zero, screen size is used.')], HRESULT, 'Height',
              ( ['retval', 'out'], POINTER(c_short), 'pHeight' )),
]
################################################################
## code template for ITiffExporter implementation
##class ITiffExporter_Impl(object):
##    def _get(self):
##        u'The width of the TIFF.  If width or height is zero, screen size is used.'
##        #return pWidth
##    def _set(self, pWidth):
##        u'The width of the TIFF.  If width or height is zero, screen size is used.'
##    Width = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The background color of the TIFF.'
##        #return ppBackgroundColor
##    def _set(self, ppBackgroundColor):
##        u'The background color of the TIFF.'
##    BackgroundColor = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The height of the TIFF.  If width or height is zero, screen size is used.'
##        #return pHeight
##    def _set(self, pHeight):
##        u'The height of the TIFF.  If width or height is zero, screen size is used.'
##    Height = property(_get, _set, doc = _set.__doc__)
##

IPrintAndExportPageOptions._methods_ = [
    COMMETHOD(['propput', helpstring(u'Specify which pages to output.')], HRESULT, 'OutputSelection',
              ( ['in'], esriOutputSelection, 'pOption' )),
    COMMETHOD(['propget', helpstring(u'Specify which pages to output.')], HRESULT, 'OutputSelection',
              ( ['retval', 'out'], POINTER(esriOutputSelection), 'pOption' )),
    COMMETHOD(['propput', helpstring(u'Specify range or query string when OutputSelection is set to range or query.')], HRESULT, 'PageRange',
              ( ['in'], BSTR, 'range' )),
    COMMETHOD(['propget', helpstring(u'Specify range or query string when OutputSelection is set to range or query.')], HRESULT, 'PageRange',
              ( ['retval', 'out'], POINTER(BSTR), 'range' )),
    COMMETHOD(['propget', helpstring(u'Indicates if selection symbology should be output.')], HRESULT, 'OutputPageSelection',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD(['propput', helpstring(u'Indicates if selection symbology should be output.')], HRESULT, 'OutputPageSelection',
              ( ['in'], VARIANT_BOOL, 'flag' )),
]
################################################################
## code template for IPrintAndExportPageOptions implementation
##class IPrintAndExportPageOptions_Impl(object):
##    def _get(self):
##        u'Specify which pages to output.'
##        #return pOption
##    def _set(self, pOption):
##        u'Specify which pages to output.'
##    OutputSelection = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Specify range or query string when OutputSelection is set to range or query.'
##        #return range
##    def _set(self, range):
##        u'Specify range or query string when OutputSelection is set to range or query.'
##    PageRange = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if selection symbology should be output.'
##        #return flag
##    def _set(self, flag):
##        u'Indicates if selection symbology should be output.'
##    OutputPageSelection = property(_get, _set, doc = _set.__doc__)
##

class PDFDriver(CoClass):
    u'Superseded by ExportPDF. Class used to print maps with the PDF (Portable Document Format) driver.'
    _reg_clsid_ = GUID('{02016031-1521-11D3-9F97-00C04F6BC8DD}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7DB92CEC-CB65-420A-8737-FCD0722FD436}', 10, 2)
PDFDriver._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IPDFDriver, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo, IStepProgressorSetup, ITrackCancelSetup, IFontMapEnvironment]

class PDFExporter(CoClass):
    u'Superseded by ExportPDF. Provides access to the PDF (Portable Document Format) exporter.'
    _reg_clsid_ = GUID('{4AA8CC0E-151D-11D3-9F97-00C04F6BC8DD}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7DB92CEC-CB65-420A-8737-FCD0722FD436}', 10, 2)
PDFExporter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IPDFExporter, IExporter, IExporterPriority, IFontMapEnvironment, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo, IOutputCleanup, IStepProgressorSetup, ITrackCancelSetup]

class IAIDriver(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Superseded by IExportAI. Provides access to members controlling Adobe Illustrator Driver options.'
    _iid_ = GUID('{9E790106-4047-4FB3-BE12-8F29106A1F86}')
    _idlflags_ = ['oleautomation']
IAIDriver._methods_ = [
    COMMETHOD([helpstring(u'Converts the EMF file to a AI File.')], HRESULT, 'CreateAI',
              ( ['in'], BSTR, 'InputFileName' ),
              ( ['in'], BSTR, 'OutputFileName' )),
    COMMETHOD(['propget', helpstring(u'Adobe Illustrator Driver options.')], HRESULT, 'AIDriverOptions',
              ( ['retval', 'out'], POINTER(esriAIDriverOptions), 'aiOptions' )),
    COMMETHOD(['propput', helpstring(u'Adobe Illustrator Driver options.')], HRESULT, 'AIDriverOptions',
              ( ['in'], esriAIDriverOptions, 'aiOptions' )),
]
################################################################
## code template for IAIDriver implementation
##class IAIDriver_Impl(object):
##    def _get(self):
##        u'Adobe Illustrator Driver options.'
##        #return aiOptions
##    def _set(self, aiOptions):
##        u'Adobe Illustrator Driver options.'
##    AIDriverOptions = property(_get, _set, doc = _set.__doc__)
##
##    def CreateAI(self, InputFileName, OutputFileName):
##        u'Converts the EMF file to a AI File.'
##        #return 
##

ISpotPlate._methods_ = [
    COMMETHOD(['propput', helpstring(u'The Color for Separation.')], HRESULT, 'Color',
              ( ['in'], POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IPostScriptColor), 'Color' )),
    COMMETHOD(['propget', helpstring(u'The Color for Separation.')], HRESULT, 'Color',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IPostScriptColor)), 'Color' )),
    COMMETHOD(['propput', helpstring(u'The Separation will be used.')], HRESULT, 'Separate',
              ( ['in'], esriPSDriverSeparates, 'Separate' )),
    COMMETHOD(['propget', helpstring(u'The Separation will be used.')], HRESULT, 'Separate',
              ( ['retval', 'out'], POINTER(esriPSDriverSeparates), 'Separate' )),
    COMMETHOD(['propput', helpstring(u'The Screen Angle for the Separation.')], HRESULT, 'ScreenAngle',
              ( ['in'], c_double, 'angle' )),
    COMMETHOD(['propget', helpstring(u'The Screen Angle for the Separation.')], HRESULT, 'ScreenAngle',
              ( ['retval', 'out'], POINTER(c_double), 'angle' )),
]
################################################################
## code template for ISpotPlate implementation
##class ISpotPlate_Impl(object):
##    def _get(self):
##        u'The Color for Separation.'
##        #return Color
##    def _set(self, Color):
##        u'The Color for Separation.'
##    Color = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The Screen Angle for the Separation.'
##        #return angle
##    def _set(self, angle):
##        u'The Screen Angle for the Separation.'
##    ScreenAngle = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The Separation will be used.'
##        #return Separate
##    def _set(self, Separate):
##        u'The Separation will be used.'
##    Separate = property(_get, _set, doc = _set.__doc__)
##

IExporter2._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The Export Extent.')], HRESULT, 'ExportExtent',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'rhs' )),
    COMMETHOD(['propget', helpstring(u'The Name of the Exporter.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'Filter String used in the CFileDialog class.')], HRESULT, 'Filter',
              ( ['retval', 'out'], POINTER(BSTR), 'Filter' )),
    COMMETHOD(['propget', helpstring(u'File Extension associated with Exporter.')], HRESULT, 'FileExtension',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propput', helpstring(u'The Pixel Bounds of the Exporter.')], HRESULT, 'PixelBounds',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'PixelBounds' )),
    COMMETHOD(['propget', helpstring(u'The Pixel Bounds of the Exporter.')], HRESULT, 'PixelBounds',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'PixelBounds' )),
    COMMETHOD(['propput', helpstring(u'The Export File Name.')], HRESULT, 'ExportFileName',
              ( ['in'], BSTR, 'fileName' )),
    COMMETHOD(['propget', helpstring(u'The Export File Name.')], HRESULT, 'ExportFileName',
              ( ['retval', 'out'], POINTER(BSTR), 'fileName' )),
    COMMETHOD(['propget', helpstring(u'The Resolution of the Exporter.')], HRESULT, 'Resolution',
              ( ['retval', 'out'], POINTER(c_short), 'res' )),
    COMMETHOD(['propput', helpstring(u'The Resolution of the Exporter.')], HRESULT, 'Resolution',
              ( ['in'], c_short, 'res' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the Output will be clipped to the Graphics Extent.')], HRESULT, 'ClipToGraphicExtent',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'clipToGraphicsExtent' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the Output will be clipped to the Graphics Extent.')], HRESULT, 'ClipToGraphicExtent',
              ( ['in'], VARIANT_BOOL, 'clipToGraphicsExtent' )),
    COMMETHOD([helpstring(u'Initializes the Exporter.')], HRESULT, 'StartExporting',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'hDC' )),
    COMMETHOD([helpstring(u'Shuts down the Exporter.')], HRESULT, 'FinishExporting'),
]
################################################################
## code template for IExporter2 implementation
##class IExporter2_Impl(object):
##    def _get(self):
##        u'Indicates if the Output will be clipped to the Graphics Extent.'
##        #return clipToGraphicsExtent
##    def _set(self, clipToGraphicsExtent):
##        u'Indicates if the Output will be clipped to the Graphics Extent.'
##    ClipToGraphicExtent = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Name(self):
##        u'The Name of the Exporter.'
##        #return Name
##
##    def _get(self):
##        u'The Pixel Bounds of the Exporter.'
##        #return PixelBounds
##    def _set(self, PixelBounds):
##        u'The Pixel Bounds of the Exporter.'
##    PixelBounds = property(_get, _set, doc = _set.__doc__)
##
##    def StartExporting(self):
##        u'Initializes the Exporter.'
##        #return hDC
##
##    def FinishExporting(self):
##        u'Shuts down the Exporter.'
##        #return 
##
##    @property
##    def Filter(self):
##        u'Filter String used in the CFileDialog class.'
##        #return Filter
##
##    def ExportExtent(self, rhs):
##        u'The Export Extent.'
##        #return 
##
##    @property
##    def FileExtension(self):
##        u'File Extension associated with Exporter.'
##        #return Name
##
##    def _get(self):
##        u'The Resolution of the Exporter.'
##        #return res
##    def _set(self, res):
##        u'The Resolution of the Exporter.'
##    Resolution = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The Export File Name.'
##        #return fileName
##    def _set(self, fileName):
##        u'The Export File Name.'
##    ExportFileName = property(_get, _set, doc = _set.__doc__)
##

class ExportBMP(CoClass):
    u'Class used to export maps to BMP (Windows Bitmap) format.'
    _reg_clsid_ = GUID('{058D2242-918D-4941-A048-8B259AAA1AA7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7DB92CEC-CB65-420A-8737-FCD0722FD436}', 10, 2)
ExportBMP._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IExportImage, IExportBMP, IExport, IWorldFileSettings, IWorldFileSettings2, ISettingsInRegistry, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

class ExportPS(CoClass):
    u'Class used to export maps to PS (PostScript) and EPS (Encapsulated PostScript) format.'
    _reg_clsid_ = GUID('{1918F0E0-69FF-4D19-B06D-4C2F8C6067A3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7DB92CEC-CB65-420A-8737-FCD0722FD436}', 10, 2)
ExportPS._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IExportVector, IExportVectorOptions, IExportVectorOptionsEx, IExportPS, IExportPS2, IExport, ISettingsInRegistry, IExportColorspaceSettings, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IOutputRasterSettings]

class ExportJPEG(CoClass):
    u'Class used to export maps to JPEG (Joint Photographic Experts Group) format.'
    _reg_clsid_ = GUID('{8E29F55C-F8D2-48B3-8227-34B279DE8358}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7DB92CEC-CB65-420A-8737-FCD0722FD436}', 10, 2)
ExportJPEG._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IExportImage, IExportJPEG, IExport, IWorldFileSettings, IWorldFileSettings2, ISettingsInRegistry, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

IWorldFileSettings._methods_ = [
    COMMETHOD(['propput', helpstring(u'The Map Extent.')], HRESULT, 'MapExtent',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope), 'MapExtent' )),
    COMMETHOD(['propget', helpstring(u'The Map Extent.')], HRESULT, 'MapExtent',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'MapExtent' )),
    COMMETHOD(['propput', helpstring(u'Indicates if a World File will be created.')], HRESULT, 'OutputWorldFile',
              ( ['in'], VARIANT_BOOL, 'OutputWorldFile' )),
    COMMETHOD(['propget', helpstring(u'Indicates if a World File will be created.')], HRESULT, 'OutputWorldFile',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'OutputWorldFile' )),
]
################################################################
## code template for IWorldFileSettings implementation
##class IWorldFileSettings_Impl(object):
##    def _get(self):
##        u'Indicates if a World File will be created.'
##        #return OutputWorldFile
##    def _set(self, OutputWorldFile):
##        u'Indicates if a World File will be created.'
##    OutputWorldFile = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The Map Extent.'
##        #return MapExtent
##    def _set(self, MapExtent):
##        u'The Map Extent.'
##    MapExtent = property(_get, _set, doc = _set.__doc__)
##


# values for enumeration 'esriPSDriverMarks'
esriPSDriverNone = 0
esriPSDriverRegistration = 1
esriPSDriverCrop = 2
esriPSDriverLabel = 4
esriPSDriverGrayScale = 8
esriPSDriverMarks = c_int # enum
IWorldFileSettings2._methods_ = [
    COMMETHOD(['propput', helpstring(u'The Map rotation angle in degrees.')], HRESULT, 'MapRotation',
              ( ['in'], c_double, 'mapRotAngle' )),
    COMMETHOD(['propget', helpstring(u'The Map rotation angle in degrees.')], HRESULT, 'MapRotation',
              ( ['retval', 'out'], POINTER(c_double), 'mapRotAngle' )),
]
################################################################
## code template for IWorldFileSettings2 implementation
##class IWorldFileSettings2_Impl(object):
##    def _get(self):
##        u'The Map rotation angle in degrees.'
##        #return mapRotAngle
##    def _set(self, mapRotAngle):
##        u'The Map rotation angle in degrees.'
##    MapRotation = property(_get, _set, doc = _set.__doc__)
##

class ExportEMF(CoClass):
    u'Class used to export maps to EMF (Windows Enhanced Metafile) format.'
    _reg_clsid_ = GUID('{B4D7AE22-1D09-4B5B-8D37-4FF7D5F9233A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7DB92CEC-CB65-420A-8737-FCD0722FD436}', 10, 2)
ExportEMF._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IExportVector, IExportVectorOptions, IExportVectorOptionsEx, IExportEMF, IExport, ISettingsInRegistry, IExportColorspaceSettings, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IOutputRasterSettings]

class IAIExporter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Superseded by IExportAI. Provides access to members that control the AI (Adobe Illustrator) export driver.'
    _iid_ = GUID('{722A2714-CD07-4C68-B07A-86A8D7B925E3}')
    _idlflags_ = ['oleautomation']
IAIExporter._methods_ = [
    COMMETHOD([helpstring(u'Returns Interface IAIDriver.')], HRESULT, 'QueryAIDriver',
              ( ['retval', 'out'], POINTER(POINTER(IAIDriver)), 'AIDriver' )),
]
################################################################
## code template for IAIExporter implementation
##class IAIExporter_Impl(object):
##    def QueryAIDriver(self):
##        u'Returns Interface IAIDriver.'
##        #return AIDriver
##

class ExportPNG(CoClass):
    u'Class used to export maps to PNG (Portable Network Graphics) format.'
    _reg_clsid_ = GUID('{69FA668C-58D9-4FD4-805C-964B5C383C8B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7DB92CEC-CB65-420A-8737-FCD0722FD436}', 10, 2)
ExportPNG._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IExportImage, IExportPNG, IExport, IWorldFileSettings, IWorldFileSettings2, ISettingsInRegistry, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

IStepProgressorSetup._methods_ = [
    COMMETHOD(['propput', helpstring(u'Updates a Progress Bar.')], HRESULT, 'StepProgressor',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStepProgressor), 'rhs' )),
]
################################################################
## code template for IStepProgressorSetup implementation
##class IStepProgressorSetup_Impl(object):
##    def _set(self, rhs):
##        u'Updates a Progress Bar.'
##    StepProgressor = property(fset = _set, doc = _set.__doc__)
##

class AIDriver(CoClass):
    u'Superseded by ExportAI. Adobe Illustator Driver Class.'
    _reg_clsid_ = GUID('{2BD83BF2-ECA7-4B7F-9B41-3AD52EAE1B1D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7DB92CEC-CB65-420A-8737-FCD0722FD436}', 10, 2)
AIDriver._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IAIDriver, IStepProgressorSetup, ITrackCancelSetup]

IFontMap2._methods_ = [
    COMMETHOD([helpstring(u'Creates an association between the TrueType Font and the Mapped Font.')], HRESULT, 'SetMapping',
              ( ['in'], BSTR, 'TrueTypeFont' ),
              ( ['in'], BSTR, 'MappedFont' )),
    COMMETHOD(['propget', helpstring(u'Creates an association between the TrueType Font and the Mapped Font.')], HRESULT, 'TrueTypeFont',
              ( ['retval', 'out'], POINTER(BSTR), 'font' )),
    COMMETHOD(['propget', helpstring(u'Creates an association between the TrueType Font and the Mapped Font.')], HRESULT, 'MappedFont',
              ( ['retval', 'out'], POINTER(BSTR), 'font' )),
    COMMETHOD(['propput', helpstring(u'Creates an association between the TrueType Font and the Mapped Font.')], HRESULT, 'Mapping',
              ( ['in'], BSTR, 'TrueTypeFont' ),
              ( ['in'], BSTR, 'rhs' )),
]
################################################################
## code template for IFontMap2 implementation
##class IFontMap2_Impl(object):
##    def SetMapping(self, TrueTypeFont, MappedFont):
##        u'Creates an association between the TrueType Font and the Mapped Font.'
##        #return 
##
##    @property
##    def TrueTypeFont(self):
##        u'Creates an association between the TrueType Font and the Mapped Font.'
##        #return font
##
##    @property
##    def MappedFont(self):
##        u'Creates an association between the TrueType Font and the Mapped Font.'
##        #return font
##
##    def _set(self, TrueTypeFont, rhs):
##        u'Creates an association between the TrueType Font and the Mapped Font.'
##    Mapping = property(fset = _set, doc = _set.__doc__)
##

class ExportAI(CoClass):
    u'Class used to export maps to AI (Adobe Illustrator) format.'
    _reg_clsid_ = GUID('{C5F4E89D-20FC-4C43-922C-B165D09C12AA}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7DB92CEC-CB65-420A-8737-FCD0722FD436}', 10, 2)
ExportAI._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IExportVector, IExportVectorOptions, IExportVectorOptionsEx, IExportAI, IExportAI2, IExport, ISettingsInRegistry, IExportColorspaceSettings, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IOutputRasterSettings]

class AIExporter(CoClass):
    u'Superseded by ExportAI. Class used to export maps to AI (Adobe Illustrator) format.'
    _reg_clsid_ = GUID('{94512290-B913-4A0B-A509-03F803F19922}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{7DB92CEC-CB65-420A-8737-FCD0722FD436}', 10, 2)
AIExporter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IAIExporter, IExporter, IExporterPriority, IOutputCleanup, IStepProgressorSetup, ITrackCancelSetup]

IEmfPrinter._methods_ = [
]
################################################################
## code template for IEmfPrinter implementation
##class IEmfPrinter_Impl(object):

__all__ = ['esriExportPSLevel2', 'esriExportPSLevel3',
           'esriPDFExtensionSecurityPermissionEditNotes',
           'esriExportColorspace', 'ExportJPEG',
           'esriExportPDFLayerOptionsNone',
           'esriPSDriverPSLevel1NoCompress', 'E_NOSPACEFORTEMPFILE',
           'IExporter', 'IAIDriver', 'esriExportErrorReturnCodes',
           'E_UNABLEOPENDOC', 'E_FILENOTFOUND', 'E_XAPCREATIONERR',
           'IExportBMP', 'IPDFDriver', 'IExportPS2',
           'esriPDFExtensionSecurityEncryptionMethodRC4_V2',
           'E_DIRFULL', 'IWorldFileSettings', 'ISettingsInRegistry',
           'TiffExporter', 'E_INVALIDIMAGEPARAMETERS',
           'esriPDFExtensionSecurityEncryptionOptionFileAttachmentOnly',
           'IPrinter', 'esriColorCorrectionDataTypeVector',
           'IColorCorrection', 'esriExportPSEmulsion', 'IExportGIF',
           'PSDriver', 'IPaper2', 'E_FILEACCESSDENIED',
           'esriPDFExtensionSecurityEncryptionOptionNoMetaData',
           'esriPSDriverImagePOS', 'esriOutputRange',
           'esriExportMultipleFiles', 'E_TEMPMETAFILE',
           'esriColorCorrectionDataTypeRaster', 'E_USERCANCEL',
           'esriExportPSImage', 'esriPSDriverImageCompression',
           'esriPSDriverSeparates',
           'esriPDFExtensionSecurityEncryptionMethodAES_V1',
           'esriPDFExtensionSecurityPermissionAll', 'ExportAI',
           'esriPDFExtensionSecurityFormSpawnTempl',
           'esriPSDriverLastHalfTone', 'IExportPDFPasswordSecurity',
           'ExportTIFF', 'esriPDFExtensionSecurityPermissionNone',
           'esriExportPSEmulsionUp',
           'esriPDFExtensionSecurityEncryptionMethod', 'E_FILEEXISTS',
           'esriOutputWhereClause', 'E_PDFEXTENSIONERROR',
           'esriExportPSImageNegative',
           'E_IMAGEDIRECTORYREADINGERROR', 'esriGIFCompressionNone',
           'esriPSDriverSeparateMagenta', 'E_BADPARAMETER',
           'esriPDFExtensionSecurityPermissionPrint',
           'E_TOOMANYPAGESFORINSERT', 'IExportPDF', 'IExport',
           'JpegExporter', 'ITiffExporter',
           'esriColorCorrectionDataType', 'IExportJPEG', 'IPSDriver',
           'E_METADATASYNTXERR', 'esriExportPDFLayerOptions',
           'IPsPrinter', 'ISpotPlate', 'ITrackCancelSetup',
           'PsPrinter', 'esriExportImageCompressionNone',
           'esriExportColorspaceCMYK', 'E_PIXELBOUNDS', 'IExportAI',
           'IExportVectorOptions', 'E_FILEACCESSNOWRITE',
           'esriTIFFCompressionDeflate',
           'E_REQUESTEDFUNCTIONALITYDOESNOTSUPPORTED',
           'E_FILEOPENFAILED', 'IExportEMF',
           'esriOutputErrorReturnCodes', 'E_OBJECTSETUP',
           'esriTIFFCompressionFax4', 'PDFDriver',
           'E_INCOMPATIBLEZLIB', 'E_OPNOTPERMITTED',
           'esriExportMultipleFiles_PageNames', 'ExportSVG',
           'IExportTIFF', 'IPsExporter', 'FontMap', 'E_AFTERSAVE',
           'esriExportImageCompressionLZW', 'esriPSDriverEmulsion',
           'esriExportImageTypeBiLevelMask',
           'esriExportMultipleFiles_None', 'IFontMap',
           'E_UNKNOWNFILETYPE', 'esriPSDriverPSLanguageLevel',
           'esriExportImageCompressionJPEG', 'E_OUTMEMORY',
           'esriExportImageCompression',
           'esriPSDriverPSLevel2NoCompress', 'AIDriver',
           'esriOutputSelection',
           'esriPDFExtensionSecurityPermissionAccessible',
           'E_CANNOTCOMPRESSORDECOMPRESS', 'esriGIFCompression',
           'E_FILEOPENINGERROR', 'ISpotPlateCollection', 'PsExporter',
           'ExportBMP', 'E_UNABLEOPENDOCFORWRITING',
           'E_REGISTRYSETTINGS', 'E_FILEREADINGERROR', 'E_FILEWRITE',
           'esriExportImageCompressionDeflate',
           'esriExportPSEmulsionDown', 'esriTIFFCompressionJPEG',
           'IFontMap2', 'ExportPNG', 'E_FILEINUSE',
           'esriPSDriverNone', 'EmfExporter',
           'esriExportImageTypeIndexed', 'IPrinterMPage',
           'FontMapEnvironment', 'esriTIFFCompressionNone', 'IPaper',
           'EmfPrinter', 'esriExportImageCompressionRLE',
           'IPDFExporter', 'Paper', 'S_SAVEDPRINTERNOTFOUND',
           'IStepProgressorSetup', 'E_MAPMETAFILE',
           'esriCMYKIndexCyan', 'esriExportImageType',
           'E_PAPERREFREQ', 'esriPSDriverImageNEG',
           'esriPDFExtensionSecurityPermissionOpen',
           'esriPSDriverPSLevel2Compress', 'esriCMYKIndexYellow',
           'esriPDFExtensionErrorCodes',
           'esriExportImageTypeGrayscale', 'esriPSDriverRegistration',
           'E_FILEREAD', 'IAIExporter', 'esriTIFFCompressionLZW',
           'esriPSDriverGrayScale', 'E_DISKFULL',
           'E_CGMVERSION3NEEDED', 'esriPSDriverLPI',
           'esriGIFCompressionRLE', 'FontMapCollection',
           'IJpegExporter', 'esriExportPDFLayerOptionsLayersOnly',
           'E_CLASSSETTEDUPINCORRECTLY', 'esriGIFCompressionLZW',
           'esriPDFExtensionSecurityEncryptionOption',
           'esriExportPDFLayerOptionsLayersAndFeatureAttributes',
           'IExportSVG', 'IPrintAndExportPageOptions',
           'esriCMYKIndexBlack',
           'esriPDFExtensionSecurityPermissionFillAndSign',
           'E_WASNOTACTIVATED', 'E_INTERNALERROR', 'E_MEMORYERROR',
           'esriColorCorrectionDataTypeTotal',
           'esriPSDriverSeparateBlack',
           'esriPDFExtensionSecurityPermissionCopy',
           'esriPSDriverMarks', 'IExportImage', 'esriPSDriverImage',
           'E_OUTPUTFILENAME', 'esriPSDriverEmulDOWN',
           'esriPSDriverSeparateCyan', 'E_NEEDPASSWD',
           'esriCMYKIndexMagenta', 'E_INVALIDORCURRUPTFILE',
           'IOutputCleanup', 'ExportPDF',
           'esriPDFExtensionSecurityEncryptionOptionAllContent',
           'esriPSDriverSeparateYellow', 'IPSDriver2',
           'E_OPENPRINTER', 'ExportEMF', 'AIExporter',
           'E_IMAGEDIRECTORYWRITINGERROR', 'DibExporter',
           'esriExportPSLanguageLevel', 'IExportColorspaceSettings',
           'esriPDFExtensionSecurityPermissionHighPrint',
           'esriOutputCurrent',
           'esriPDFExtensionSecurityEncryptionMethodAES_V2',
           'ExportGIF', 'IExportPagesMultipleFile',
           'esriExportMultipleFiles_PageIndex', 'esriCMYKIndex',
           'IExportPS', 'IExportVectorOptionsEx',
           'PrintAndExportPageOptions',
           'esriPDFExtensionSecurityPermissionEdit',
           'E_METAFILEPARSING', 'E_UNABLEREADILE',
           'esriPSDriverPSLevel1Compress',
           'esriPDFExtensionSecurityPermissionDocAssembly',
           'E_FILEERROR', 'esriOutputAll', 'IEmfExporter',
           'esriPSDriverPSLevel3', 'IWorldFileSettings2',
           'E_MEMORYOUT', 'E_INTERROR', 'esriPSDriverCrop',
           'E_METADATAINTERNAL', 'IOutputPageOptionsAdmin',
           'E_DRIVERNOTMATCH', 'esriOutputSelected',
           'esriPSDriverEmulUP', 'IExporterPriority',
           'esriTIFFCompressionPackBits', 'esriPSDriverLabel',
           'SpotPlate', 'E_FILECREATION', 'esriAIPolygonizeMarkers',
           'E_METADATABADXMP', 'IFontMapEnvironment',
           'E_INVALIDPARAMETERS', 'S_NOPRINTERSINSTALLED',
           'E_BITMAPOUTOFMEMORY', 'esriExportPSImagePositive',
           'IFontMapCollection', 'E_TOOMANYPAGESFOROPEN',
           'E_UNABLEWRITINGDOC', 'esriExportColorspaceRGB',
           'IExportVector', 'esriTIFFCompression',
           'E_FILEWRITINGERROR', 'IEmfPrinter',
           'esriExportImageTypeTrueColor', 'esriAIDriverOptions',
           'ExportPS', 'E_FILEIO', 'E_READORWRITEJPEGMARKER',
           'IExporter2', 'E_PARAMETER', 'esriAIMapFonts',
           'IExportPDF2', 'IExportPDF3', 'esriPSDriverSeparateCustom',
           'E_FILELOCKED', 'E_FILECREATIONERROR',
           'E_LICENSENOTAVAILABLE', 'IDibExporter',
           'E_UNABLERENTEMPFILE', 'PDFExporter', 'E_FILEALREADYOPEN',
           'E_STARTPRINTING', 'IExportAI2',
           'esriPDFExtensionSecurityPermission', 'esriPSDriverDPI',
           'esriPSDriverPSLevel2',
           'esriPDFExtensionSecurityPermissionSecure',
           'esriExportImageCompressionAdaptive',
           'esriPDFExtensionSecurityPermissionAllMaster',
           'IBmpExporter', 'esriExportImageTypeBiLevelThreshold',
           'esriPSDriverHalfTone', 'IExportPNG',
           'E_INSUFFICIENTMEMORY']
from comtypes import _check_version; _check_version('501')

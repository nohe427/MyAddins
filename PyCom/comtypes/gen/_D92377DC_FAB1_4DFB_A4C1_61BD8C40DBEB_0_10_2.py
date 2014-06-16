# -*- coding: mbcs -*-
typelib_path = u'C:\\Program Files (x86)\\ArcGIS\\Desktop10.2\\com\\esriCartoUI.olb'
_lcid = 0 # change this if required
from ctypes import *
from comtypes import GUID
from comtypes import CoClass
import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0
import comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2
import comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2
import comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2
from ctypes import HRESULT
from comtypes import helpstring
from comtypes import COMMETHOD
from comtypes import dispid
import comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2
from ctypes.wintypes import VARIANT_BOOL
import comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2
from comtypes import BSTR
import comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2
import comtypes.gen._C0FC1503_7E6F_11D2_AABF_00C04FA375F1_0_10_2
from comtypes.automation import VARIANT
from comtypes.automation import VARIANT
import comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2
import comtypes.gen._7BA654FE_F55E_4EE5_8CF2_FAEFFBC04A61_0_10_2
from comtypes import IUnknown


class AnnotationClassesFLPropertyPage(CoClass):
    u'Property page for managing annotation extension properties for feature linked annotation layers.'
    _reg_clsid_ = GUID('{80AE1AC1-A94C-4D6A-B21C-4F5536B32ADA}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
AnnotationClassesFLPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class OverposterGeneralPropertyPage(CoClass):
    u'Annotate map properties page.'
    _reg_clsid_ = GUID('{5EE19849-1E82-4BAC-9D20-46F11E774782}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
OverposterGeneralPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class UniqueValuePropertyPage(CoClass):
    u"Renderer property page for managing properties associated with the 'Unique values' layer symbology option."
    _reg_clsid_ = GUID('{683C994E-A17B-11D1-8816-080009EC732A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
class IRendererPropertyPage(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control renderer property pages.'
    _iid_ = GUID('{44BD4D21-5F47-11D0-92DA-00805F7C28B0}')
    _idlflags_ = ['oleautomation']
UniqueValuePropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, IRendererPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class AnnotationSublayerInfoPropertyPage(CoClass):
    u'Annotation sublayer properties page.'
    _reg_clsid_ = GUID('{D0B93F47-5284-4ECE-9EF4-7ECBE562CC39}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
AnnotationSublayerInfoPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class TextElementPropertyPage(CoClass):
    u'Text graphic element property page.'
    _reg_clsid_ = GUID('{9BCE2BA1-FDF3-11D0-83B5-080009B996CC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
TextElementPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class AnnotationExpressionProperties(CoClass):
    u'An Esri annotation expression properties.'
    _reg_clsid_ = GUID('{582F83F4-1ECD-48C1-82A9-EA18429C151D}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
class IAnnotationExpressionProperties(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the annotation (labeling) expression properties proxy.'
    _iid_ = GUID('{161BE4C0-1A11-11D4-80D7-00C04F601565}')
    _idlflags_ = ['oleautomation']
AnnotationExpressionProperties._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IAnnotationExpressionProperties]

class LayerLabelsPropertyPage(CoClass):
    u'Property page for managing labelling properties for a feature layer.'
    _reg_clsid_ = GUID('{1476C781-6F57-11D2-A2C6-080009B6F22B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
LayerLabelsPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class INewGeoTransformationDialog2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to instantiate the default transformation in New GeoTransformation dialog.'
    _iid_ = GUID('{B0BD3480-60A4-425A-A264-557BAD0CCD34}')
    _idlflags_ = ['oleautomation']
INewGeoTransformationDialog2._methods_ = [
    COMMETHOD([helpstring(u'Sets a transformation in the New GeoTransformation dialog to work with.')], HRESULT, 'SetDefault',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeoTransformation), 'pGT' )),
]
################################################################
## code template for INewGeoTransformationDialog2 implementation
##class INewGeoTransformationDialog2_Impl(object):
##    def SetDefault(self, pGT):
##        u'Sets a transformation in the New GeoTransformation dialog to work with.'
##        #return 
##

class FeatureLayerSelectionPropertyPage(CoClass):
    u'Property page for managing selection properties for a feature layer.'
    _reg_clsid_ = GUID('{BB708287-C171-11D2-AAF6-000000000000}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
FeatureLayerSelectionPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class ILabelPriorityRankingDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Label Priority Ranking Dialog.'
    _iid_ = GUID('{D7F13B7D-9E08-4534-ACC1-C3685C5BF004}')
    _idlflags_ = ['oleautomation']
ILabelPriorityRankingDialog._methods_ = [
    COMMETHOD([helpstring(u'Shows the Label Priority Ranking Dialog.')], HRESULT, 'DoModal',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMap), 'pMap' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hwnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ok' )),
]
################################################################
## code template for ILabelPriorityRankingDialog implementation
##class ILabelPriorityRankingDialog_Impl(object):
##    def DoModal(self, pMap, hwnd):
##        u'Shows the Label Priority Ranking Dialog.'
##        #return ok
##

class ILabelWeightRankingDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Label Weight Ranking Dialog.'
    _iid_ = GUID('{18A61CB3-26C4-430F-8092-364C860ECFF1}')
    _idlflags_ = ['oleautomation']
ILabelWeightRankingDialog._methods_ = [
    COMMETHOD([helpstring(u'Shows the Label Weight Ranking Dialog.')], HRESULT, 'DoModal',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMap), 'pMap' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hwnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ok' )),
]
################################################################
## code template for ILabelWeightRankingDialog implementation
##class ILabelWeightRankingDialog_Impl(object):
##    def DoModal(self, pMap, hwnd):
##        u'Shows the Label Weight Ranking Dialog.'
##        #return ok
##

class ILabelManagerDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Label Manager Dialog.'
    _iid_ = GUID('{6688A44B-36D8-469F-852F-403A4C6E967E}')
    _idlflags_ = ['oleautomation']
ILabelManagerDialog._methods_ = [
    COMMETHOD([helpstring(u'Shows the Label Manager.')], HRESULT, 'DoModal',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMap), 'pMap' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hwnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ok' )),
]
################################################################
## code template for ILabelManagerDialog implementation
##class ILabelManagerDialog_Impl(object):
##    def DoModal(self, pMap, hwnd):
##        u'Shows the Label Manager.'
##        #return ok
##

class ScaleTracker(CoClass):
    u'Tracker for scale operations.'
    _reg_clsid_ = GUID('{2DC98F3A-38AA-11D3-9F3C-00C04F6BC979}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
ScaleTracker._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IScaleTracker]

class ILabelStyleSelector(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control a Label Style Selector.'
    _iid_ = GUID('{DF8C493C-24F3-4EBA-AC21-D07F600569B1}')
    _idlflags_ = ['oleautomation']
ILabelStyleSelector._methods_ = [
    COMMETHOD([helpstring(u'Indicates if this label style selector can be used with the specified label style.')], HRESULT, 'Applies',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILabelStyle), 'style' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Applies' )),
]
################################################################
## code template for ILabelStyleSelector implementation
##class ILabelStyleSelector_Impl(object):
##    def Applies(self, style):
##        u'Indicates if this label style selector can be used with the specified label style.'
##        #return Applies
##

class ISQLQueryDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the SQL Query Dialog.'
    _iid_ = GUID('{6C609945-CAC4-454C-87B1-9A27A40AEDD0}')
    _idlflags_ = ['oleautomation']
ISQLQueryDialog._methods_ = [
    COMMETHOD(['propget', helpstring(u'The SQL query entered in the dialog.')], HRESULT, 'SQLQuery',
              ( ['retval', 'out'], POINTER(BSTR), 'val' )),
    COMMETHOD([helpstring(u'Shows the SQL query dialog.')], HRESULT, 'DoModal',
              ( ['in'], BSTR, 'initialSqlQuery' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'pFeatureClass' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hwnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ok' )),
]
################################################################
## code template for ISQLQueryDialog implementation
##class ISQLQueryDialog_Impl(object):
##    @property
##    def SQLQuery(self):
##        u'The SQL query entered in the dialog.'
##        #return val
##
##    def DoModal(self, initialSqlQuery, pFeatureClass, hwnd):
##        u'Shows the SQL query dialog.'
##        #return ok
##

class MeasuredGridFactory(CoClass):
    u'Measured grid factory class.'
    _reg_clsid_ = GUID('{D7A07C92-F9A1-11D1-ADEC-080009EC732A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
class IMapGridFactory(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of the map grid factory.'
    _iid_ = GUID('{D7A07C90-F9A1-11D1-ADEC-080009EC732A}')
    _idlflags_ = ['oleautomation']
MeasuredGridFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMapGridFactory]

class LineElementPropertyPage(CoClass):
    u'Line graphic element property page.'
    _reg_clsid_ = GUID('{FF44A615-DCF6-11D0-838B-080009B996CC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
LineElementPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class IndexGridFactory(CoClass):
    u'Index grid factory class.'
    _reg_clsid_ = GUID('{D7A07C93-F9A1-11D1-ADEC-080009EC732A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
IndexGridFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMapGridFactory]

class GraticuleFactory(CoClass):
    u'Graticule factory class.'
    _reg_clsid_ = GUID('{D7A07C91-F9A1-11D1-ADEC-080009EC732A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
GraticuleFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMapGridFactory]

class LayerDefinitionQueryPropertyPage(CoClass):
    u"Property page for managing a feature layer's definition query."
    _reg_clsid_ = GUID('{1476C788-6F57-11D2-A2C6-080009B6F22B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
LayerDefinitionQueryPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class ISQLQueryDialog2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the SQL Query Dialog.'
    _iid_ = GUID('{D21925A7-1B01-4143-85CE-4700D643F6FA}')
    _idlflags_ = ['oleautomation']
ISQLQueryDialog2._methods_ = [
    COMMETHOD(['propget', helpstring(u'The SQL query entered in the dialog.')], HRESULT, 'SQLQuery',
              ( ['retval', 'out'], POINTER(BSTR), 'val' )),
    COMMETHOD([helpstring(u'Shows the SQL query dialog.')], HRESULT, 'DoModal',
              ( ['in'], BSTR, 'initialSqlQuery' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'pFeatureClass' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hwnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ok' )),
    COMMETHOD([helpstring(u'Shows the SQL query dialog.')], HRESULT, 'DoModalEx',
              ( ['in'], BSTR, 'initialSqlQuery' ),
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IFeatureLayer), 'pLayer' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hwnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ok' )),
]
################################################################
## code template for ISQLQueryDialog2 implementation
##class ISQLQueryDialog2_Impl(object):
##    @property
##    def SQLQuery(self):
##        u'The SQL query entered in the dialog.'
##        #return val
##
##    def DoModal(self, initialSqlQuery, pFeatureClass, hwnd):
##        u'Shows the SQL query dialog.'
##        #return ok
##
##    def DoModalEx(self, initialSqlQuery, pLayer, hwnd):
##        u'Shows the SQL query dialog.'
##        #return ok
##

class GroupLayerPropertyPage(CoClass):
    u'Property page for a group layer.'
    _reg_clsid_ = GUID('{1476C784-6F57-11D2-A2C6-080009B6F22B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
GroupLayerPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class GroupLayerDisplayPropertyPage(CoClass):
    u"Property page for managing a group layer's display properties)."
    _reg_clsid_ = GUID('{27DB7366-3F51-4641-A26B-9352793643EE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
GroupLayerDisplayPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class AreaSeriesProperties(CoClass):
    u'A container for the display and manipulation of area graph series.'
    _reg_clsid_ = GUID('{12A28A19-8D8B-4EDF-9010-CF9D77B94E5D}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
AreaSeriesProperties._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ISeriesProperties, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IAreaSeriesProperties, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDataSortSeriesProperties, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IFeatureLayerSelectionEvents, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ISelectionEvents, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDefinitionExpressionEvents]

class ILabelScaleRangeDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Label Scale Range Dialog.'
    _iid_ = GUID('{8A76F73C-88E2-448C-872D-762C59FF76C5}')
    _idlflags_ = ['oleautomation']
ILabelScaleRangeDialog._methods_ = [
    COMMETHOD(['propget', helpstring(u'The minimum scale entered in the dialog.')], HRESULT, 'MinimumScale',
              ( ['retval', 'out'], POINTER(c_double), 'val' )),
    COMMETHOD(['propget', helpstring(u'The maximum scale entered in the dialog.')], HRESULT, 'MaximumScale',
              ( ['retval', 'out'], POINTER(c_double), 'val' )),
    COMMETHOD([helpstring(u'Shows the SQL query dialog.')], HRESULT, 'DoModal',
              ( ['in'], c_double, 'initialMinimumScale' ),
              ( ['in'], c_double, 'initialMaximumScale' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hwnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ok' )),
]
################################################################
## code template for ILabelScaleRangeDialog implementation
##class ILabelScaleRangeDialog_Impl(object):
##    @property
##    def MaximumScale(self):
##        u'The maximum scale entered in the dialog.'
##        #return val
##
##    def DoModal(self, initialMinimumScale, initialMaximumScale, hwnd):
##        u'Shows the SQL query dialog.'
##        #return ok
##
##    @property
##    def MinimumScale(self):
##        u'The minimum scale entered in the dialog.'
##        #return val
##

class FramePropertyPage(CoClass):
    u'Property page for frames.'
    _reg_clsid_ = GUID('{AF5279B2-0B8B-11D2-A26E-080009B6F22B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
FramePropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class ScaleTextPropertyPage(CoClass):
    u'Property page for scale text.'
    _reg_clsid_ = GUID('{59EEFF10-FBEC-11D1-878A-0000F8751720}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
ScaleTextPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class MapGridSystemPropertyPage(CoClass):
    u'Property page for map grid coordinate systems.'
    _reg_clsid_ = GUID('{520D8051-DA49-11D2-AB02-000000000000}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
MapGridSystemPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class IDataFrameAreaOfInterestDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u"Provides access to the data frame's area of interest property."
    _iid_ = GUID('{58F2AE0F-3D5F-4C62-8765-541604432C05}')
    _idlflags_ = ['oleautomation']
IDataFrameAreaOfInterestDialog._methods_ = [
    COMMETHOD([helpstring(u"Specify data frame's area of interest.")], HRESULT, 'DoModal',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMapFrame), 'pMapFrame' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentWindow' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ok' )),
]
################################################################
## code template for IDataFrameAreaOfInterestDialog implementation
##class IDataFrameAreaOfInterestDialog_Impl(object):
##    def DoModal(self, pMapFrame, parentWindow):
##        u"Specify data frame's area of interest."
##        #return ok
##

class DmsLabelPropertyPage(CoClass):
    u'Property page for DMS grid labels.'
    _reg_clsid_ = GUID('{AD1F2DC0-A2BC-11D2-AAE1-000000000000}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
DmsLabelPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class MapGridStyleGalleryClass(CoClass):
    u'Map Grid gallery class.'
    _reg_clsid_ = GUID('{17DFF3D3-E26D-11D2-AB07-000000000000}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
MapGridStyleGalleryClass._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IStyleGalleryClass, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IStyleGalleryClass2]

class MixedFontLabelPropertyPage(CoClass):
    u'Property page for mixed font grid labels.'
    _reg_clsid_ = GUID('{5642D2AB-A3FE-11D2-AE80-080009EC732A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
MixedFontLabelPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class IndexTabPropertyPage(CoClass):
    u'Property page for index grid tabs.'
    _reg_clsid_ = GUID('{AD1F2DBF-A2BC-11D2-AAE1-000000000000}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
IndexTabPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class LegendWizard(CoClass):
    u'Legend wizard.'
    _reg_clsid_ = GUID('{0F220A18-FABB-11D3-9FE4-00C04F6BC78E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
class ILegendWizard(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of the legend wizard.'
    _iid_ = GUID('{0F220A17-FABB-11D3-9FE4-00C04F6BC78E}')
    _idlflags_ = ['oleautomation']
LegendWizard._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ILegendWizard]

class IndexGridPropertyPage(CoClass):
    u'Property page for index grid cells and labels.'
    _reg_clsid_ = GUID('{A74BD95B-A5E1-11D2-AAE2-000000000000}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
IndexGridPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class DataFrameShapeDialog(CoClass):
    u'Data Frame Shape Dialog.'
    _reg_clsid_ = GUID('{50650922-1BDB-4C4F-A351-7C57192725FE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
DataFrameShapeDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._C0FC1503_7E6F_11D2_AABF_00C04FA375F1_0_10_2.IDataFrameShapeDialog, comtypes.gen._C0FC1503_7E6F_11D2_AABF_00C04FA375F1_0_10_2.IDataFrameShapeDialog2]

class CalibratedBorderPropertyPage(CoClass):
    u'Property page for calibrated grid borders.'
    _reg_clsid_ = GUID('{C4ADB337-E869-11D2-9F55-00C04F6BC78E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
CalibratedBorderPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class DataFrameAreaOfInterestDialog(CoClass):
    u'Data frame fixed bounds dialog.'
    _reg_clsid_ = GUID('{6DB491E0-9854-46E0-9F0A-29F5F3BF30CF}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
DataFrameAreaOfInterestDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDataFrameAreaOfInterestDialog, comtypes.gen._C0FC1503_7E6F_11D2_AABF_00C04FA375F1_0_10_2.IDataFrameShapeDialog]

class DataFrameClippingDialog(CoClass):
    u'Data frame clipping dialog.'
    _reg_clsid_ = GUID('{C6BB8296-763B-426E-8AF5-D80254DDCAD7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
class IDataFrameClippingDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of the data frame clipping dialog.'
    _iid_ = GUID('{5BE42E7D-B0D8-49FC-B812-BA7D81B43319}')
    _idlflags_ = ['oleautomation']
DataFrameClippingDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDataFrameClippingDialog, comtypes.gen._C0FC1503_7E6F_11D2_AABF_00C04FA375F1_0_10_2.IDataFrameShapeDialog]

class DataFrameFixedExtentDialog(CoClass):
    u'Data frame fixed bounds dialog.'
    _reg_clsid_ = GUID('{6DB491DF-9854-46E0-9F0A-29F5F3BF30CF}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
class IDataFrameFixedExtentDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u"Provides access to the data frame's fixed bounds property."
    _iid_ = GUID('{58F2AE0E-3D5F-4C62-8765-541604432C05}')
    _idlflags_ = ['oleautomation']
DataFrameFixedExtentDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDataFrameFixedExtentDialog, comtypes.gen._C0FC1503_7E6F_11D2_AABF_00C04FA375F1_0_10_2.IDataFrameShapeDialog]

class MapGraphicsLayerPropertyPage(CoClass):
    u'Basic Graphics Layer property page for a map.'
    _reg_clsid_ = GUID('{53353FC1-A719-11D2-A301-080009B6F22B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
MapGraphicsLayerPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class LabelDefinitionPropertyPage(CoClass):
    u'Property page for managing a label definition.'
    _reg_clsid_ = GUID('{0FD4D253-9DD3-41B3-ADBB-DBB52318E5C0}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
LabelDefinitionPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class SymbolLevelDialog(CoClass):
    u'Dialog to set pre 9.0 style Symbol Levels for a Map.'
    _reg_clsid_ = GUID('{51CF4CF1-C37F-11D2-9F22-00C04F6BC709}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
class ISymbolLevelDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the Symbol Level Dialog.'
    _iid_ = GUID('{51CF4CF0-C37F-11D2-9F22-00C04F6BC709}')
    _idlflags_ = ['oleautomation']
SymbolLevelDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ISymbolLevelDialog]

class DataExclusionPropertyPage(CoClass):
    u'Data exclusion property page for working with legend properties.'
    _reg_clsid_ = GUID('{301A4421-A76C-11D2-AB27-00C04FA334B3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
DataExclusionPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class FillShapeElementPropertyPage(CoClass):
    u'Fill Shape graphic element property page.'
    _reg_clsid_ = GUID('{204034D1-F6EA-11D0-83AD-080009B996CC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
FillShapeElementPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class IHistogram(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control histogram objects created from different data sources.'
    _iid_ = GUID('{962BD9AB-1EC8-11D3-9F4D-00C04F6BC709}')
    _idlflags_ = ['oleautomation']
IHistogram._methods_ = [
    COMMETHOD([helpstring(u'Histogram as an array of values (doubles) and a paired array of frequencies (longs).')], HRESULT, 'GetHistogram',
              ( ['out'], POINTER(VARIANT), 'doubleArrayValues' ),
              ( ['out'], POINTER(VARIANT), 'longArrayFrequencies' )),
    COMMETHOD(['propput', helpstring(u'Custom minimum.')], HRESULT, 'CustomMin',
              ( ['in'], c_double, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Custom maximum.')], HRESULT, 'CustomMax',
              ( ['in'], c_double, 'rhs' )),
    COMMETHOD([helpstring(u'Resets custom minimum and maximum.')], HRESULT, 'ResetCustomMinMax'),
    COMMETHOD([helpstring(u'Shows the exclusion dialog for the histogram.')], HRESULT, 'ExclusionDoModal',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentHWnd' ),
              ( [], POINTER(VARIANT_BOOL), 'ok' )),
    COMMETHOD([helpstring(u'Indicates if the histogram uses exclusion.')], HRESULT, 'HasExclusion',
              ( [], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD([helpstring(u'Shows the sampling dialog for the histogram.')], HRESULT, 'SamplingDoModal',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentHWnd' ),
              ( [], POINTER(VARIANT_BOOL), 'ok' )),
    COMMETHOD([helpstring(u'Indicates if the histogram uses data sampling.')], HRESULT, 'HasSampling',
              ( [], POINTER(VARIANT_BOOL), 'flag' )),
]
################################################################
## code template for IHistogram implementation
##class IHistogram_Impl(object):
##    def _set(self, rhs):
##        u'Custom minimum.'
##    CustomMin = property(fset = _set, doc = _set.__doc__)
##
##    def HasExclusion(self, flag):
##        u'Indicates if the histogram uses exclusion.'
##        #return 
##
##    def GetHistogram(self):
##        u'Histogram as an array of values (doubles) and a paired array of frequencies (longs).'
##        #return doubleArrayValues, longArrayFrequencies
##
##    def SamplingDoModal(self, parentHWnd, ok):
##        u'Shows the sampling dialog for the histogram.'
##        #return 
##
##    def ExclusionDoModal(self, parentHWnd, ok):
##        u'Shows the exclusion dialog for the histogram.'
##        #return 
##
##    def HasSampling(self, flag):
##        u'Indicates if the histogram uses data sampling.'
##        #return 
##
##    def _set(self, rhs):
##        u'Custom maximum.'
##    CustomMax = property(fset = _set, doc = _set.__doc__)
##
##    def ResetCustomMinMax(self):
##        u'Resets custom minimum and maximum.'
##        #return 
##

class AdvancedDrawingDialog(CoClass):
    u'Dialog to set advanced drawing options for the Map.'
    _reg_clsid_ = GUID('{DF63951D-0156-4849-B308-653CF4192ABF}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
class IAdvancedDrawingDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the Advanced Drawing Dialog.'
    _iid_ = GUID('{66A13AF5-8396-49C7-AE45-255738059B42}')
    _idlflags_ = ['oleautomation']
AdvancedDrawingDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IAdvancedDrawingDialog]

class DataGraphTHorizontalAxisProperties(CoClass):
    u'A container for the display and manipulation of graph horizontal axis properties.'
    _reg_clsid_ = GUID('{0176E471-5C06-45A2-8D88-3EE0F6AAF584}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
DataGraphTHorizontalAxisProperties._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDataGraphTAxisProperties]

class IDataHistogram(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members used to create a histogram from data values.'
    _iid_ = GUID('{FD21F231-67A6-11D3-9F66-00C04F6BC709}')
    _idlflags_ = ['oleautomation']
IDataHistogram._methods_ = [
    COMMETHOD([helpstring(u'Sets data from a array of values (doubles).')], HRESULT, 'SetData',
              ( ['in'], VARIANT, 'doubleArrayValues' )),
    COMMETHOD([helpstring(u'Sets data from a histogram; an array of values (doubles) and a paired array of frequencies (longs).')], HRESULT, 'SetHistogramData',
              ( ['in'], VARIANT, 'doubleArrayValues' ),
              ( ['in'], VARIANT, 'longArrayFrequencies' )),
]
################################################################
## code template for IDataHistogram implementation
##class IDataHistogram_Impl(object):
##    def SetHistogramData(self, doubleArrayValues, longArrayFrequencies):
##        u'Sets data from a histogram; an array of values (doubles) and a paired array of frequencies (longs).'
##        #return 
##
##    def SetData(self, doubleArrayValues):
##        u'Sets data from a array of values (doubles).'
##        #return 
##

class IClassificationDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control a dialog for working with properties of a classification.'
    _iid_ = GUID('{3E055F75-2288-11D3-9F4F-00C04F6BC709}')
    _idlflags_ = ['oleautomation']
IClassificationDialog._methods_ = [
    COMMETHOD(['propput', helpstring(u'Array of class breaks (double). ClassBreaks(0) is the minimum value in the dataset, and subsequent breaks represent the upper limit of each class.')], HRESULT, 'ClassBreaks',
              ( ['in'], VARIANT, 'doubleArrayBreaks' )),
    COMMETHOD(['propget', helpstring(u'Array of class breaks (double). ClassBreaks(0) is the minimum value in the dataset, and subsequent breaks represent the upper limit of each class.')], HRESULT, 'ClassBreaks',
              ( ['retval', 'out'], POINTER(VARIANT), 'doubleArrayBreaks' )),
    COMMETHOD([helpstring(u'Sets data to the dialog via a histogram.')], HRESULT, 'SetHistogramData',
              ( ['in'], POINTER(IHistogram), 'histo' )),
    COMMETHOD([helpstring(u'Sets data to the dialog via an array of values.')], HRESULT, 'SetData',
              ( ['in'], VARIANT, 'doubleArrayValues' )),
    COMMETHOD(['propput', helpstring(u'Number format options.')], HRESULT, 'NumberFormat',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.INumberFormat), 'rhs' )),
    COMMETHOD([helpstring(u'Sets the minimum and maximum allowed number of classes.')], HRESULT, 'SetClassLimits',
              ( ['in'], c_int, 'minClasses' ),
              ( ['in'], c_int, 'maxClasses' )),
    COMMETHOD(['propput', helpstring(u'Upper bound of the last class (commonly set to the last ClassBreak).')], HRESULT, 'UpperThreshold',
              ( ['in'], c_int, 'threshold' )),
    COMMETHOD(['propget', helpstring(u'Upper bound of the last class (commonly set to the last ClassBreak).')], HRESULT, 'UpperThreshold',
              ( ['retval', 'out'], POINTER(c_int), 'threshold' )),
    COMMETHOD(['propput', helpstring(u'Lower bound of the first class.')], HRESULT, 'LowerThreshold',
              ( ['in'], c_int, 'threshold' )),
    COMMETHOD(['propget', helpstring(u'Lower bound of the first class.')], HRESULT, 'LowerThreshold',
              ( ['retval', 'out'], POINTER(c_int), 'threshold' )),
    COMMETHOD(['propput', helpstring(u'Classification object.')], HRESULT, 'Classification',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID), 'clsid' )),
    COMMETHOD(['propget', helpstring(u'Classification object.')], HRESULT, 'Classification',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID)), 'clsid' )),
    COMMETHOD([helpstring(u'Shows the dialog modally.')], HRESULT, 'DoModal',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentHWnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ok' )),
]
################################################################
## code template for IClassificationDialog implementation
##class IClassificationDialog_Impl(object):
##    def SetHistogramData(self, histo):
##        u'Sets data to the dialog via a histogram.'
##        #return 
##
##    def _set(self, rhs):
##        u'Number format options.'
##    NumberFormat = property(fset = _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Upper bound of the last class (commonly set to the last ClassBreak).'
##        #return threshold
##    def _set(self, threshold):
##        u'Upper bound of the last class (commonly set to the last ClassBreak).'
##    UpperThreshold = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Lower bound of the first class.'
##        #return threshold
##    def _set(self, threshold):
##        u'Lower bound of the first class.'
##    LowerThreshold = property(_get, _set, doc = _set.__doc__)
##
##    def SetClassLimits(self, minClasses, maxClasses):
##        u'Sets the minimum and maximum allowed number of classes.'
##        #return 
##
##    def _get(self):
##        u'Classification object.'
##        #return clsid
##    def _set(self, clsid):
##        u'Classification object.'
##    Classification = property(_get, _set, doc = _set.__doc__)
##
##    def DoModal(self, parentHWnd):
##        u'Shows the dialog modally.'
##        #return ok
##
##    def _get(self):
##        u'Array of class breaks (double). ClassBreaks(0) is the minimum value in the dataset, and subsequent breaks represent the upper limit of each class.'
##        #return doubleArrayBreaks
##    def _set(self, doubleArrayBreaks):
##        u'Array of class breaks (double). ClassBreaks(0) is the minimum value in the dataset, and subsequent breaks represent the upper limit of each class.'
##    ClassBreaks = property(_get, _set, doc = _set.__doc__)
##
##    def SetData(self, doubleArrayValues):
##        u'Sets data to the dialog via an array of values.'
##        #return 
##

class AnnotationClassPropertyPage(CoClass):
    u'Property page for managing annotation extension properties for graphics layers.'
    _reg_clsid_ = GUID('{38E095F5-AC47-440C-8295-0B108C82F8C5}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
AnnotationClassPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class CovAnnoFontPropertyPage(CoClass):
    u'Coverage annotation layer property page for fonts.'
    _reg_clsid_ = GUID('{891F0819-DD5D-11D2-9F49-00C04F6BC78E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
CovAnnoFontPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class IAVObjectConverter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the ArcView (3.x) object converter.'
    _iid_ = GUID('{049EADD3-DD95-11D3-9FD4-00C04F6BC78E}')
    _idlflags_ = ['oleautomation']
class IAVObject(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the ArcView (3.x) object.'
    _iid_ = GUID('{049EADD1-DD95-11D3-9FD4-00C04F6BC78E}')
    _idlflags_ = ['oleautomation']
IAVObjectConverter._methods_ = [
    COMMETHOD([helpstring(u'Reads an ArcView 3.x ODL file.')], HRESULT, 'ReadObjects',
              ( ['in'], BSTR, 'filePath' )),
    COMMETHOD([helpstring(u'Returns the next object in the project.')], HRESULT, 'NextObject',
              ( ['retval', 'out'], POINTER(POINTER(IAVObject)), 'obj' )),
    COMMETHOD([helpstring(u'Resets the enumerator.')], HRESULT, 'Reset'),
    COMMETHOD([helpstring(u'Imports a view from an APR file.')], HRESULT, 'ImportView',
              ( ['in'], BSTR, 'viewName' ),
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMap), 'pMap' )),
    COMMETHOD([helpstring(u'Imports a layout from an APR file.')], HRESULT, 'ImportLayout',
              ( ['in'], BSTR, 'layoutName' ),
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IPageLayout), 'pLayout' )),
    COMMETHOD([helpstring(u'Returns the named property object associated with the given object.')], HRESULT, 'QueryObjectProperty',
              ( ['in'], POINTER(IAVObject), 'obj' ),
              ( ['in'], BSTR, 'propertyName' ),
              ( ['retval', 'out'], POINTER(POINTER(IAVObject)), 'propertyObject' )),
    COMMETHOD([helpstring(u'Returns the object specified by the given object id.')], HRESULT, 'QueryObjectByID',
              ( ['in'], c_int, 'objID' ),
              ( ['retval', 'out'], POINTER(POINTER(IAVObject)), 'obj' )),
    COMMETHOD([helpstring(u'Returns a feature class with the same properties as the input feature theme object.')], HRESULT, 'QueryFeatureClass',
              ( ['in'], POINTER(IAVObject), 'fThemeObject' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass)), 'fclass' )),
    COMMETHOD([helpstring(u"Sets the layer symbology for a given feature layer, based on a feature theme's legend.")], HRESULT, 'SetFeatureSymbology',
              ( ['in'], POINTER(IAVObject), 'themeObject' ),
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IFeatureLayer), 'flayer' )),
    COMMETHOD([helpstring(u'Returns a Renderer from an ArcView legend object.')], HRESULT, 'ConvertLegend',
              ( ['in'], POINTER(IAVObject), 'legendObject' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IFeatureRenderer)), 'Renderer' )),
    COMMETHOD([helpstring(u'Returns a symbol from an ArcView symbol object.')], HRESULT, 'ConvertSymbol',
              ( ['in'], POINTER(IAVObject), 'symbolObj' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.ISymbol)), 'Symbol' )),
    COMMETHOD([helpstring(u'Converts an AV color object.')], HRESULT, 'ConvertColor',
              ( ['in'], POINTER(IAVObject), 'colorObject' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IColor)), 'color' )),
    COMMETHOD([helpstring(u'Converts an AV font object.')], HRESULT, 'ConvertFont',
              ( ['in'], POINTER(IAVObject), 'fontObject' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IFontDisp)), 'fontDisp' )),
    COMMETHOD([helpstring(u"Converts an AV graphic object into an element.  All elements except MapSurrounds are converted when 'pass' is 0.  Only MapSurrounds are converted when 'pass' is 1.")], HRESULT, 'ConvertElement',
              ( ['in'], POINTER(IAVObject), 'graphicObject' ),
              ( ['in'], c_double, 'xOrigin' ),
              ( ['in'], c_double, 'yOrigin' ),
              ( ['in'], c_short, 'pass' ),
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IGraphicsContainer), 'gContainer' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IElement)), 'outElement' )),
    COMMETHOD([helpstring(u'Converts an AV rectangle (or MapDpy) object to an envelope.')], HRESULT, 'ConvertBounds',
              ( ['in'], POINTER(IAVObject), 'rectObject' ),
              ( ['in'], c_double, 'xOrigin' ),
              ( ['in'], c_double, 'yOrigin' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IEnvelope)), 'bounds' )),
    COMMETHOD([helpstring(u'Converts an AV shape object to a geometry object.')], HRESULT, 'ConvertGeometry',
              ( ['in'], POINTER(IAVObject), 'shapeObject' ),
              ( ['in'], c_double, 'xOrigin' ),
              ( ['in'], c_double, 'yOrigin' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeometry)), 'geometry' )),
    COMMETHOD([helpstring(u'Converts an AV projection object to a spatial reference object.')], HRESULT, 'ConvertProjection',
              ( ['in'], POINTER(IAVObject), 'projectionObj' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference)), 'spatialRef' )),
    COMMETHOD([helpstring(u'Returns the map associated with an AV view object.')], HRESULT, 'ConnectToView',
              ( ['in'], POINTER(IAVObject), 'viewObject' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMap)), 'Map' )),
    COMMETHOD(['propget', helpstring(u'The number of maps converted.')], HRESULT, 'MapCount',
              ( ['retval', 'out'], POINTER(c_int), 'count' )),
    COMMETHOD(['propget', helpstring(u'The converted map at the given index.')], HRESULT, 'Map',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMap)), 'Map' )),
]
################################################################
## code template for IAVObjectConverter implementation
##class IAVObjectConverter_Impl(object):
##    def Reset(self):
##        u'Resets the enumerator.'
##        #return 
##
##    def ImportLayout(self, layoutName, pLayout):
##        u'Imports a layout from an APR file.'
##        #return 
##
##    def ConvertBounds(self, rectObject, xOrigin, yOrigin):
##        u'Converts an AV rectangle (or MapDpy) object to an envelope.'
##        #return bounds
##
##    def ConvertColor(self, colorObject):
##        u'Converts an AV color object.'
##        #return color
##
##    def QueryFeatureClass(self, fThemeObject):
##        u'Returns a feature class with the same properties as the input feature theme object.'
##        #return fclass
##
##    def ConvertFont(self, fontObject):
##        u'Converts an AV font object.'
##        #return fontDisp
##
##    def ImportView(self, viewName, pMap):
##        u'Imports a view from an APR file.'
##        #return 
##
##    def ConnectToView(self, viewObject):
##        u'Returns the map associated with an AV view object.'
##        #return Map
##
##    def ConvertSymbol(self, symbolObj):
##        u'Returns a symbol from an ArcView symbol object.'
##        #return Symbol
##
##    def QueryObjectByID(self, objID):
##        u'Returns the object specified by the given object id.'
##        #return obj
##
##    def ConvertProjection(self, projectionObj):
##        u'Converts an AV projection object to a spatial reference object.'
##        #return spatialRef
##
##    def NextObject(self):
##        u'Returns the next object in the project.'
##        #return obj
##
##    def ConvertGeometry(self, shapeObject, xOrigin, yOrigin):
##        u'Converts an AV shape object to a geometry object.'
##        #return geometry
##
##    def ConvertElement(self, graphicObject, xOrigin, yOrigin, pass, gContainer):
##        u"Converts an AV graphic object into an element.  All elements except MapSurrounds are converted when 'pass' is 0.  Only MapSurrounds are converted when 'pass' is 1."
##        #return outElement
##
##    @property
##    def Map(self, index):
##        u'The converted map at the given index.'
##        #return Map
##
##    def ConvertLegend(self, legendObject):
##        u'Returns a Renderer from an ArcView legend object.'
##        #return Renderer
##
##    def ReadObjects(self, filePath):
##        u'Reads an ArcView 3.x ODL file.'
##        #return 
##
##    @property
##    def MapCount(self):
##        u'The number of maps converted.'
##        #return count
##
##    def QueryObjectProperty(self, obj, propertyName):
##        u'Returns the named property object associated with the given object.'
##        #return propertyObject
##
##    def SetFeatureSymbology(self, themeObject, flayer):
##        u"Sets the layer symbology for a given feature layer, based on a feature theme's legend."
##        #return 
##

class Library(object):
    u'Esri CartoUI Object Library 10.2'
    name = u'esriCartoUI'
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)

class CovAnnoLevelPropertyPage(CoClass):
    u'Coverage annotation layer property page for levels.'
    _reg_clsid_ = GUID('{891F081A-DD5D-11D2-9F49-00C04F6BC78E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
CovAnnoLevelPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class IHistogram2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control histogram objects created from different data sources.'
    _iid_ = GUID('{233A0652-5AD8-4FA8-A61F-65DE6260C4EB}')
    _idlflags_ = ['oleautomation']
IHistogram2._methods_ = [
    COMMETHOD([helpstring(u'Invalidates the Histogram.')], HRESULT, 'Invalidate'),
]
################################################################
## code template for IHistogram2 implementation
##class IHistogram2_Impl(object):
##    def Invalidate(self):
##        u'Invalidates the Histogram.'
##        #return 
##

class HorizontalBarLegendItemPropertyPage(CoClass):
    u'Property page for managing the properties of horizontal bar legend items.'
    _reg_clsid_ = GUID('{130D219D-CAC3-11D3-92FB-00600802E603}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
HorizontalBarLegendItemPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class ShadowSelector(CoClass):
    u'Shadow style selector.'
    _reg_clsid_ = GUID('{00205997-7B00-4D5C-9330-B795CD5BD8BD}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
ShadowSelector._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IStyleSelector, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IComPropertySheetEvents]

class NetworkTrafficRendererPropertyPage(CoClass):
    u'Property page for managing the properties of the NetworkTrafficRenderer object.'
    _reg_clsid_ = GUID('{2B4BF9F2-391A-4ACA-AD6D-40132953CAF9}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
class INetworkRendererPropertyPage(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the NetworkRendererPropertyPage.'
    _iid_ = GUID('{B5857613-2B30-4070-86D3-6785AF49A04C}')
    _idlflags_ = ['oleautomation']
NetworkTrafficRendererPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, INetworkRendererPropertyPage]

class MarkerRotationDialog(CoClass):
    u'A dialog for working with the rotation properties of a renderer.'
    _reg_clsid_ = GUID('{463DDE70-A9ED-11D2-AAE6-000000000000}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
class IRendererUIDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control dialogs for managing transparency and rotation related renderer properties.'
    _iid_ = GUID('{463DDE6F-A9ED-11D2-AAE6-000000000000}')
    _idlflags_ = ['oleautomation']
class IRendererUIDialog2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control a dialog for working with the size properties of chart symbols.'
    _iid_ = GUID('{98DD7039-FEB4-11D3-9F7C-00C04F6BC709}')
    _idlflags_ = ['oleautomation']
MarkerRotationDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRendererUIDialog, IRendererUIDialog2]

class IFeatureAdjustmentAssociationPage(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the cadastral feature adjustment association page.'
    _iid_ = GUID('{55E1F778-8B27-42E1-9201-DFB265FD57AF}')
    _idlflags_ = ['oleautomation']
IFeatureAdjustmentAssociationPage._methods_ = [
    COMMETHOD(['propput', helpstring(u'Store the Cadastral Fabric which is to be modified.')], HRESULT, 'CadastralFabric',
              ( ['in'], POINTER(comtypes.gen._7BA654FE_F55E_4EE5_8CF2_FAEFFBC04A61_0_10_2.ICadastralFabric), 'ppCadastralFabric' )),
    COMMETHOD(['propget', helpstring(u'Store the Cadastral Fabric which is to be modified.')], HRESULT, 'CadastralFabric',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._7BA654FE_F55E_4EE5_8CF2_FAEFFBC04A61_0_10_2.ICadastralFabric)), 'ppCadastralFabric' )),
    COMMETHOD([helpstring(u'Save changes made to the adjustment page.')], HRESULT, 'SaveAdjustmentSettings'),
]
################################################################
## code template for IFeatureAdjustmentAssociationPage implementation
##class IFeatureAdjustmentAssociationPage_Impl(object):
##    def _get(self):
##        u'Store the Cadastral Fabric which is to be modified.'
##        #return ppCadastralFabric
##    def _set(self, ppCadastralFabric):
##        u'Store the Cadastral Fabric which is to be modified.'
##    CadastralFabric = property(_get, _set, doc = _set.__doc__)
##
##    def SaveAdjustmentSettings(self):
##        u'Save changes made to the adjustment page.'
##        #return 
##

class MarkerSizeDialog(CoClass):
    u'A dialog for working with the size properties of a renderer.'
    _reg_clsid_ = GUID('{22790C09-6229-4387-819A-818DC4EB51C4}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
MarkerSizeDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRendererUIDialog, IRendererUIDialog2]

class CFSourcePage(CoClass):
    u'Cadastral Fabric Source property page.'
    _reg_clsid_ = GUID('{F70BBBB4-68B5-4AEE-9293-D72F79B622BD}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
CFSourcePage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext]

class MaplexAnnoLEPropsStrategyPropertyPage(CoClass):
    u'Maplex Label engine layer properties conflict property page.'
    _reg_clsid_ = GUID('{20664808-6892-3F5B-BC55-7EFBB0B01235}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
MaplexAnnoLEPropsStrategyPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class GxBrowserFactory(CoClass):
    u'A factory for creating layers based on feature classes and layer files.'
    _reg_clsid_ = GUID('{808D7BD5-EAA2-11D1-ADE5-080009EC732A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
GxBrowserFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayerFactory]

class CFDataSourcePageExtension(CoClass):
    u'.'
    _reg_clsid_ = GUID('{CD962D3A-935F-448F-A54B-3B0EC967E4BD}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
class IFeatureLayerSourcePageExtension(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u"Provides access to members that control a dialog for setting a feature layer's data source."
    _iid_ = GUID('{2AAD86BE-5EEB-4284-9A29-8F8EF40E040B}')
    _idlflags_ = ['oleautomation']
CFDataSourcePageExtension._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IFeatureLayerSourcePageExtension, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ICFDataSourcePageExtension, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream]

class TimeDataPropertyPage(CoClass):
    u"Property page for managing a layer's time related properties."
    _reg_clsid_ = GUID('{1C3DDB97-36C7-4B6D-849E-376B1BC25B0B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
TimeDataPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class ICreateHyperlinkMacroDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Create Hyperlink Macro Dialog.'
    _iid_ = GUID('{C356B499-7819-41A9-BF14-EEF6D3DAE4BB}')
    _idlflags_ = ['oleautomation']
ICreateHyperlinkMacroDialog._methods_ = [
    COMMETHOD(['propget', helpstring(u'The text entered in the document field of the dialog.')], HRESULT, 'DocumentText',
              ( ['retval', 'out'], POINTER(BSTR), 'text' )),
    COMMETHOD(['propget', helpstring(u'The text entered in the module field of the dialog.')], HRESULT, 'ModuleText',
              ( ['retval', 'out'], POINTER(BSTR), 'text' )),
    COMMETHOD(['propget', helpstring(u'The text entered in the macro field of the dialog.')], HRESULT, 'MacroText',
              ( ['retval', 'out'], POINTER(BSTR), 'text' )),
    COMMETHOD([helpstring(u'Shows the SQL query dialog.')], HRESULT, 'DoModal',
              ( ['in'], POINTER(comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IApplication), 'pApp' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hwnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ok' )),
]
################################################################
## code template for ICreateHyperlinkMacroDialog implementation
##class ICreateHyperlinkMacroDialog_Impl(object):
##    @property
##    def MacroText(self):
##        u'The text entered in the macro field of the dialog.'
##        #return text
##
##    def DoModal(self, pApp, hwnd):
##        u'Shows the SQL query dialog.'
##        #return ok
##
##    @property
##    def DocumentText(self):
##        u'The text entered in the document field of the dialog.'
##        #return text
##
##    @property
##    def ModuleText(self):
##        u'The text entered in the module field of the dialog.'
##        #return text
##

class CFAssociationsPage(CoClass):
    u'Cadastral fabric associations property page.'
    _reg_clsid_ = GUID('{539C9EE7-CA85-498E-840B-C22D9FD8C454}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
CFAssociationsPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext]

class TransparencyFieldDialog(CoClass):
    u'A dialog for working with the transparency by field properties of a renderer.'
    _reg_clsid_ = GUID('{FB20665E-DB1C-11D2-9F2E-00C04F6BC709}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
TransparencyFieldDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRendererUIDialog, IRendererUIDialog2]

class CFSubClassesPage(CoClass):
    u'Property page for cadastral fabric sub classes.'
    _reg_clsid_ = GUID('{2C542B7B-76F2-45FC-B1F2-E8416DBC15C0}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
CFSubClassesPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext]

class PieSizeDialog(CoClass):
    u'A dialog for working with the size properties of a PieChartSymbol object.'
    _reg_clsid_ = GUID('{98DD703A-FEB4-11D3-9F7C-00C04F6BC709}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
PieSizeDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRendererUIDialog2]

class CFEditEnvironmentPage(CoClass):
    u'Cadastral fabric edit environment property page.'
    _reg_clsid_ = GUID('{50AB8D54-BCB5-441F-8263-8EB31F270C87}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
CFEditEnvironmentPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext]

class BarSizeDialog(CoClass):
    u'A dialog for working with the size properties of BarChartSymbol and StackedChartSymbol objects.'
    _reg_clsid_ = GUID('{98DD7044-FEB4-11D3-9F7C-00C04F6BC709}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
BarSizeDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRendererUIDialog2]

class DotDensitySymbolUIDialog(CoClass):
    u'A dialog for working with some properties of a DotDensitySymbol object.'
    _reg_clsid_ = GUID('{5370F8D0-E41F-11D3-822A-0080C79F0371}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
class IDotDensitySymbolUIDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control a dialog for working with some properties of a DotDensitySymbol object.'
    _iid_ = GUID('{DB4EC7B0-E41D-11D3-822A-0080C79F0371}')
    _idlflags_ = ['oleautomation']
DotDensitySymbolUIDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDotDensitySymbolUIDialog]

class LayerFieldsPropertyPage(CoClass):
    u"Property page for managing properties associated with a feature layer's fields."
    _reg_clsid_ = GUID('{1476C787-6F57-11D2-A2C6-080009B6F22B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
LayerFieldsPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class LabelPriorityRankingDialog(CoClass):
    u'Esri Label Priority Ranking Dialog.'
    _reg_clsid_ = GUID('{A18E67C5-9DB9-4950-975F-ABB976445F51}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
LabelPriorityRankingDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ILabelPriorityRankingDialog]

class IMapGridSelector(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the map grid selector.'
    _iid_ = GUID('{D4FD105B-E2FC-11D2-9F50-00C04F6BC78E}')
    _idlflags_ = ['oleautomation']
IMapGridSelector._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The map frame whose map grids are edited.')], HRESULT, 'MapFrame',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMapFrame), 'rhs' )),
]
################################################################
## code template for IMapGridSelector implementation
##class IMapGridSelector_Impl(object):
##    def MapFrame(self, rhs):
##        u'The map frame whose map grids are edited.'
##        #return 
##

class CadastralFabricLayerHistoryPropPage(CoClass):
    u'Property page for managing cadastral fabric layer history properties.'
    _reg_clsid_ = GUID('{30213DC0-69BA-45B2-B19D-E19C8D2B72D6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
CadastralFabricLayerHistoryPropPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

ILegendWizard._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The page layout containing the map frame.')], HRESULT, 'PageLayout',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IPageLayout), 'rhs' )),
    COMMETHOD(['propput', helpstring(u'The initial legend frame (optional).')], HRESULT, 'InitialLegendFrame',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMapSurroundFrame), 'rhs' )),
    COMMETHOD(['propget', helpstring(u'The legend frame (valid after calling DoModal).')], HRESULT, 'LegendFrame',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMapSurroundFrame)), 'resultLegendFrame' )),
    COMMETHOD([helpstring(u'Displays the legend wizard.')], HRESULT, 'DoModal',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentHWnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ok' )),
]
################################################################
## code template for ILegendWizard implementation
##class ILegendWizard_Impl(object):
##    def _set(self, rhs):
##        u'The initial legend frame (optional).'
##    InitialLegendFrame = property(fset = _set, doc = _set.__doc__)
##
##    def PageLayout(self, rhs):
##        u'The page layout containing the map frame.'
##        #return 
##
##    @property
##    def LegendFrame(self):
##        u'The legend frame (valid after calling DoModal).'
##        #return resultLegendFrame
##
##    def DoModal(self, parentHWnd):
##        u'Displays the legend wizard.'
##        #return ok
##

class FeatureAdjustmentAssociationPage(CoClass):
    u'Cadastral Feature Adjustment Association Page.'
    _reg_clsid_ = GUID('{4B0B0A06-0954-4A95-9A24-B51DCF9C0F7A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
FeatureAdjustmentAssociationPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, IFeatureAdjustmentAssociationPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

IDataFrameClippingDialog._methods_ = [
    COMMETHOD([helpstring(u'Specify clip shape to data frame.')], HRESULT, 'DoModal',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMapFrame), 'pMapFrame' ),
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IGraphicsContainer), 'pContainer' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentWindow' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ok' )),
]
################################################################
## code template for IDataFrameClippingDialog implementation
##class IDataFrameClippingDialog_Impl(object):
##    def DoModal(self, pMapFrame, pContainer, parentWindow):
##        u'Specify clip shape to data frame.'
##        #return ok
##

class ScaleBarLabelsAndMarksPropertyPage(CoClass):
    u"Property page for a scale bar's labels and marks."
    _reg_clsid_ = GUID('{17D0529E-1CF6-11D3-B8A6-00600802E603}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
ScaleBarLabelsAndMarksPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class NorthArrowElementPropertyPage(CoClass):
    u'Property page for north arrow elements.'
    _reg_clsid_ = GUID('{48980FF4-F493-11D1-8788-0000F8751720}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
NorthArrowElementPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

IDataFrameFixedExtentDialog._methods_ = [
    COMMETHOD([helpstring(u"Specify data frame's fixed bounds.")], HRESULT, 'DoModal',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMapFrame), 'pMapFrame' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentWindow' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ok' )),
]
################################################################
## code template for IDataFrameFixedExtentDialog implementation
##class IDataFrameFixedExtentDialog_Impl(object):
##    def DoModal(self, pMapFrame, parentWindow):
##        u"Specify data frame's fixed bounds."
##        #return ok
##

class NestedLegendItemPropertyPage(CoClass):
    u'Property page for managing the properties of nested legend items.'
    _reg_clsid_ = GUID('{130D219E-CAC3-11D3-92FB-00600802E603}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
NestedLegendItemPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

IRendererUIDialog._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The renderer.')], HRESULT, 'Renderer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IFeatureRenderer), 'rhs' )),
    COMMETHOD(['propputref', helpstring(u'The feature class.')], HRESULT, 'FeatureClass',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'rhs' )),
    COMMETHOD([helpstring(u'Displays the dialog.')], HRESULT, 'DoModal',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentHWnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ok' )),
]
################################################################
## code template for IRendererUIDialog implementation
##class IRendererUIDialog_Impl(object):
##    def DoModal(self, parentHWnd):
##        u'Displays the dialog.'
##        #return ok
##
##    def Renderer(self, rhs):
##        u'The renderer.'
##        #return 
##
##    def FeatureClass(self, rhs):
##        u'The feature class.'
##        #return 
##

class MapFrameLocatorPropertyPage(CoClass):
    u'Property page for map frame locator.'
    _reg_clsid_ = GUID('{48980FF5-F493-11D1-8788-0000F8751720}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
MapFrameLocatorPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class DisplayStringPropPage(CoClass):
    u'Simple property page for Display String manipulation.'
    _reg_clsid_ = GUID('{41E1DE11-184A-4BA8-8DE0-66623F874F0C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
DisplayStringPropPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class MapProjectionPropPage(CoClass):
    u'Property page for map projections.'
    _reg_clsid_ = GUID('{E8458D0D-EA9C-11D1-8782-0000F8751720}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
MapProjectionPropPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

IAdvancedDrawingDialog._methods_ = [
    COMMETHOD([helpstring(u'Shows the Advanced Drawing Dialog.')], HRESULT, 'DoModal',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentHWnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ok' )),
    COMMETHOD(['propputref', helpstring(u'The data frame whose layers are to be masked.')], HRESULT, 'DataFrame',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMap), 'rhs' )),
]
################################################################
## code template for IAdvancedDrawingDialog implementation
##class IAdvancedDrawingDialog_Impl(object):
##    def DoModal(self, parentHWnd):
##        u'Shows the Advanced Drawing Dialog.'
##        #return ok
##
##    def DataFrame(self, rhs):
##        u'The data frame whose layers are to be masked.'
##        #return 
##

class DatumChecker(CoClass):
    u'Datum checker.'
    _reg_clsid_ = GUID('{C3F131C6-2596-11D3-9F9D-00C04F6BC78E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
class IDatumChecker(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that check for datum inconsistencies.'
    _iid_ = GUID('{C3F131C5-2596-11D3-9F9D-00C04F6BC78E}')
    _idlflags_ = ['oleautomation']
class IDatumChecker2(IDatumChecker):
    _case_insensitive_ = True
    u'Provides basic map access to members that check for datum inconsistencies.'
    _iid_ = GUID('{016FB9F5-81FF-4467-8AE5-35CCF3315A93}')
    _idlflags_ = ['oleautomation']
DatumChecker._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDatumChecker, IDatumChecker2]

class AnnoLEPropsConflictPropertyPage(CoClass):
    u'A label engine layer properties conflict detection property page.'
    _reg_clsid_ = GUID('{DA1C4077-6892-4F5B-BC95-7EFBB0B043A9}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
AnnoLEPropsConflictPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

IDatumChecker._methods_ = [
    COMMETHOD([helpstring(u'Adds a layer and checks for datum inconsistencies.')], HRESULT, 'AddLayerCheck',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMap), 'Map' ),
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer), 'Layer' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentHWnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'okToAdd' )),
    COMMETHOD([helpstring(u'Resets an AddLayer loop.')], HRESULT, 'AddLayerReset'),
    COMMETHOD([helpstring(u"Checks for a change to the data frame's spatial reference.")], HRESULT, 'SetSpatialReferenceCheck',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMap), 'Map' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference), 'spatialReference' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentHWnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'okToChange' )),
]
################################################################
## code template for IDatumChecker implementation
##class IDatumChecker_Impl(object):
##    def AddLayerCheck(self, Map, Layer, parentHWnd):
##        u'Adds a layer and checks for datum inconsistencies.'
##        #return okToAdd
##
##    def AddLayerReset(self):
##        u'Resets an AddLayer loop.'
##        #return 
##
##    def SetSpatialReferenceCheck(self, Map, spatialReference, parentHWnd):
##        u"Checks for a change to the data frame's spatial reference."
##        #return okToChange
##

class LabelEngineChecker(CoClass):
    u'Label engine checker.'
    _reg_clsid_ = GUID('{45CEC780-554A-12D4-76DE-18EE4F66DC59}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
class ILabelEngineChecker(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides basic map access to members that check for label engine inconsistencies.'
    _iid_ = GUID('{73FE63E8-700A-4BB3-04FE-FE9927EAB23A}')
    _idlflags_ = []
LabelEngineChecker._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ILabelEngineChecker]

class MapGridWizard(CoClass):
    u'Map grid wizard.'
    _reg_clsid_ = GUID('{DE76FAD8-EE01-11D3-9FDB-00C04F6BC78E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
class IMapGridWizard(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of the map grid wizard.'
    _iid_ = GUID('{DE76FAD7-EE01-11D3-9FDB-00C04F6BC78E}')
    _idlflags_ = ['oleautomation']
MapGridWizard._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMapGridWizard]

IDatumChecker2._methods_ = [
    COMMETHOD([helpstring(u'Adds a layer and checks for datum inconsistencies.')], HRESULT, 'AddLayerCheckBasic',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IBasicMap), 'BasicMap' ),
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer), 'Layer' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentHWnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'okToAdd' )),
    COMMETHOD([helpstring(u"Checks for a change to the data frame's spatial reference.")], HRESULT, 'SetSpatialReferenceCheckBasic',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IBasicMap), 'BasicMap' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference), 'spatialReference' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentHWnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'okToChange' )),
    COMMETHOD([helpstring(u'Sets name of application for registry key lookup.')], HRESULT, 'SetAppRegKey',
              ( ['in'], BSTR, 'appName' )),
]
################################################################
## code template for IDatumChecker2 implementation
##class IDatumChecker2_Impl(object):
##    def SetSpatialReferenceCheckBasic(self, BasicMap, spatialReference, parentHWnd):
##        u"Checks for a change to the data frame's spatial reference."
##        #return okToChange
##
##    def AddLayerCheckBasic(self, BasicMap, Layer, parentHWnd):
##        u'Adds a layer and checks for datum inconsistencies.'
##        #return okToAdd
##
##    def SetAppRegKey(self, appName):
##        u'Sets name of application for registry key lookup.'
##        #return 
##

class QueryWizard(CoClass):
    u'Query wizard.'
    _reg_clsid_ = GUID('{3686D1FC-FE89-11D3-9FE6-00C04F6BC78E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
class IQueryWizard(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of the query wizard.'
    _iid_ = GUID('{3686D1FB-FE89-11D3-9FE6-00C04F6BC78E}')
    _idlflags_ = ['oleautomation']
QueryWizard._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IQueryWizard]

class RowIdentifyObject(CoClass):
    u'Row Identify Object.'
    _reg_clsid_ = GUID('{061BDED2-1486-11D4-9FEC-00C04F6BC78E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
RowIdentifyObject._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IRowIdentifyObject, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IIdentifyObj]

ISymbolLevelDialog._methods_ = [
    COMMETHOD([helpstring(u'Shows the Symbol Level Dialog.')], HRESULT, 'DoModal',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentHWnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ok' )),
    COMMETHOD(['propputref', helpstring(u'The data frame whose symbol levels are edited.')], HRESULT, 'DataFrame',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMap), 'rhs' )),
]
################################################################
## code template for ISymbolLevelDialog implementation
##class ISymbolLevelDialog_Impl(object):
##    def DoModal(self, parentHWnd):
##        u'Shows the Symbol Level Dialog.'
##        #return ok
##
##    def DataFrame(self, rhs):
##        u'The data frame whose symbol levels are edited.'
##        #return 
##

class MaplexAnnoLEPropsStackingPropertyPage(CoClass):
    u'Maplex Label engine layer properties stacking property page.'
    _reg_clsid_ = GUID('{20664808-6122-334B-BC55-7EF340B01233}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
MaplexAnnoLEPropsStackingPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class NewGeoTransformationDialog(CoClass):
    u'New geographic transformation dialog.'
    _reg_clsid_ = GUID('{EE02B625-6A44-11D4-A643-0008C711C8C1}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
class INewGeoTransformationDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the members that create a new geographic transformation.'
    _iid_ = GUID('{3A964D76-2AB1-11D4-A632-0008C711C8C1}')
    _idlflags_ = ['oleautomation']
NewGeoTransformationDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, INewGeoTransformationDialog, INewGeoTransformationDialog2]

class MgrsGridFactory(CoClass):
    u'MGRS grid factory class.'
    _reg_clsid_ = GUID('{205733E3-0C63-4DC9-A3C5-A44397FA881F}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
MgrsGridFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMapGridFactory]

class PrincipalDigitsPropertyPage(CoClass):
    u'Property page for grid labels that highlight the principal digits of the label values.'
    _reg_clsid_ = GUID('{6E3EAC2C-9699-4505-BB82-E41F986DE11A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
PrincipalDigitsPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class MgrsGridPropertyPage(CoClass):
    u'Property page for MGRS grids.'
    _reg_clsid_ = GUID('{B6021439-7B2E-4CDF-906A-DD0AF5E6C6D8}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
MgrsGridPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class CornerLabelPropertyPage(CoClass):
    u'Property page for corner grid labels.'
    _reg_clsid_ = GUID('{E2CBE513-53EF-4474-AAA7-3B5C54A7CECE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
CornerLabelPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class GridHatchPropertyPage(CoClass):
    u'Property page for grid hatching.'
    _reg_clsid_ = GUID('{884EE217-35D0-4BFF-8776-5925046EC487}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
GridHatchPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

IMapGridWizard._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The map frame the grid will be added to.')], HRESULT, 'MapFrame',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMapFrame), 'rhs' )),
    COMMETHOD(['propputref', helpstring(u'The page layout containing the map frame.')], HRESULT, 'PageLayout',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IPageLayout), 'rhs' )),
    COMMETHOD(['propput', helpstring(u'The initial map grid (optional).')], HRESULT, 'InitialGrid',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMapGrid), 'rhs' )),
    COMMETHOD(['propget', helpstring(u'The specified grid (valid after calling DoModal).')], HRESULT, 'MapGrid',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMapGrid)), 'MapGrid' )),
    COMMETHOD(['propget', helpstring(u'The generated graphic element, if any (valid after calling DoModal).')], HRESULT, 'GraphicElement',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IElement)), 'outputGraphic' )),
    COMMETHOD([helpstring(u'Shows the map grid wizard.')], HRESULT, 'DoModal',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentHWnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ok' )),
]
################################################################
## code template for IMapGridWizard implementation
##class IMapGridWizard_Impl(object):
##    def PageLayout(self, rhs):
##        u'The page layout containing the map frame.'
##        #return 
##
##    @property
##    def GraphicElement(self):
##        u'The generated graphic element, if any (valid after calling DoModal).'
##        #return outputGraphic
##
##    def _set(self, rhs):
##        u'The initial map grid (optional).'
##    InitialGrid = property(fset = _set, doc = _set.__doc__)
##
##    @property
##    def MapGrid(self):
##        u'The specified grid (valid after calling DoModal).'
##        #return MapGrid
##
##    def MapFrame(self, rhs):
##        u'The map frame the grid will be added to.'
##        #return 
##
##    def DoModal(self, parentHWnd):
##        u'Shows the map grid wizard.'
##        #return ok
##

INewGeoTransformationDialog._methods_ = [
    COMMETHOD([helpstring(u'Shows the New GeoTransformation dialog.')], HRESULT, 'DoModal',
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeographicCoordinateSystem), 'pSourceGCS' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeographicCoordinateSystem), 'pTargetGCS' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IGeoTransformation)), 'ppGT' )),
]
################################################################
## code template for INewGeoTransformationDialog implementation
##class INewGeoTransformationDialog_Impl(object):
##    def DoModal(self, pSourceGCS, pTargetGCS):
##        u'Shows the New GeoTransformation dialog.'
##        #return ppGT
##

IQueryWizard._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The map.')], HRESULT, 'Map',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMap), 'rhs' )),
    COMMETHOD(['propputref', helpstring(u'The initial layer (optional).')], HRESULT, 'InitialLayer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer), 'rhs' )),
    COMMETHOD(['propget', helpstring(u'The layer selected (valid after calling DoModal).')], HRESULT, 'Layer',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer)), 'resultLayer' )),
    COMMETHOD(['propget', helpstring(u'The generated WHERE clause (valid after calling DoModal).')], HRESULT, 'WhereClause',
              ( ['retval', 'out'], POINTER(BSTR), 'WhereClause' )),
    COMMETHOD(['propget', helpstring(u'The selected combination method (valid after calling DoModal).')], HRESULT, 'CombinationMethod',
              ( ['retval', 'out'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.esriSelectionResultEnum), 'comboMethod' )),
    COMMETHOD([helpstring(u'Shows the query wizard.')], HRESULT, 'DoModal',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentHWnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ok' )),
]
################################################################
## code template for IQueryWizard implementation
##class IQueryWizard_Impl(object):
##    def Map(self, rhs):
##        u'The map.'
##        #return 
##
##    @property
##    def Layer(self):
##        u'The layer selected (valid after calling DoModal).'
##        #return resultLayer
##
##    def InitialLayer(self, rhs):
##        u'The initial layer (optional).'
##        #return 
##
##    @property
##    def WhereClause(self):
##        u'The generated WHERE clause (valid after calling DoModal).'
##        #return WhereClause
##
##    def DoModal(self, parentHWnd):
##        u'Shows the query wizard.'
##        #return ok
##
##    @property
##    def CombinationMethod(self):
##        u'The selected combination method (valid after calling DoModal).'
##        #return comboMethod
##

IMapGridFactory._methods_ = [
    COMMETHOD(['propget', helpstring(u'The name of the map grid class.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD([helpstring(u'Creates a map grid.')], HRESULT, 'Create',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMapFrame), 'MapFrame' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMapGrid)), 'MapGrid' )),
]
################################################################
## code template for IMapGridFactory implementation
##class IMapGridFactory_Impl(object):
##    def Create(self, MapFrame):
##        u'Creates a map grid.'
##        #return MapGrid
##
##    @property
##    def Name(self):
##        u'The name of the map grid class.'
##        #return Name
##

class PictureElementPropertyPage(CoClass):
    u'Picture graphic element property page.'
    _reg_clsid_ = GUID('{5994C051-D2F9-11D1-9142-0000F87808EE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
PictureElementPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class IMaplexWeightRankingDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Maplex Weight Ranking Dialog.'
    _iid_ = GUID('{F1D4F6EE-2AD0-42FE-BA7C-D4D4906962AF}')
    _idlflags_ = ['oleautomation']
IMaplexWeightRankingDialog._methods_ = [
    COMMETHOD([helpstring(u'Shows the Maplex Weight Ranking Dialog.')], HRESULT, 'DoModal',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMap), 'pMap' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hwnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ok' )),
]
################################################################
## code template for IMaplexWeightRankingDialog implementation
##class IMaplexWeightRankingDialog_Impl(object):
##    def DoModal(self, pMap, hwnd):
##        u'Shows the Maplex Weight Ranking Dialog.'
##        #return ok
##

class LegendElementPropertyPage(CoClass):
    u'Property page for legends.'
    _reg_clsid_ = GUID('{59EEFF07-FBEC-11D1-878A-0000F8751720}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
LegendElementPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class SizeAndPositionPropertyPage(CoClass):
    u'Property page for positioning graphic elements.'
    _reg_clsid_ = GUID('{A4B3E6D3-EF1C-11D1-8786-0000F8751720}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
SizeAndPositionPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class MaplexExpressionPropertyPage(CoClass):
    u'A Maplex label engine layer properties expression property page.'
    _reg_clsid_ = GUID('{70F0DAB1-59F2-53E1-BBA1-1750D28FFE7A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
MaplexExpressionPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class MapFramePropertyPage(CoClass):
    u'Property page for the map frame.'
    _reg_clsid_ = GUID('{48980FF1-F493-11D1-8788-0000F8751720}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
MapFramePropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class LegendElementItemsPropertyPage(CoClass):
    u"Property page for a legend's items."
    _reg_clsid_ = GUID('{59EEFF08-FBEC-11D1-878A-0000F8751720}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
LegendElementItemsPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class MapGridIntervalsPropertyPage(CoClass):
    u'Property page for map grid intervals.'
    _reg_clsid_ = GUID('{31F26E71-A038-11D2-AE7E-080009EC732A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
MapGridIntervalsPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class LegendLayoutPropertyPage(CoClass):
    u'Property page for legends.'
    _reg_clsid_ = GUID('{6B6575F3-1AB2-4147-8FD1-3582195D959A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
LegendLayoutPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class SymbolBorderPropertyPage(CoClass):
    u'Property page for Symbol Borders.'
    _reg_clsid_ = GUID('{BBCFA855-DE33-11D2-B868-00600802E603}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
SymbolBorderPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class MaplexAnnoLEPropsPlacementPropertyPage(CoClass):
    u'Maplex Label engine layer properties placement property page.'
    _reg_clsid_ = GUID('{20664808-0F77-11D2-A270-080009B6F22B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
MaplexAnnoLEPropsPlacementPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class IMaplexKeyNumberGroupDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Maplex Key Number Group Dialog.'
    _iid_ = GUID('{6F4D3BE1-8F20-08F1-4D3D-86C4FCE448B3}')
    _idlflags_ = ['oleautomation']
IMaplexKeyNumberGroupDialog._methods_ = [
    COMMETHOD([helpstring(u'Shows the Key Number Group Dialog.')], HRESULT, 'DoModal',
              ( ['in'], VARIANT_BOOL, 'readOnly' ),
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMaplexKeyNumberGroups), 'pGroups' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hwnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ok' )),
]
################################################################
## code template for IMaplexKeyNumberGroupDialog implementation
##class IMaplexKeyNumberGroupDialog_Impl(object):
##    def DoModal(self, readOnly, pGroups, hwnd):
##        u'Shows the Key Number Group Dialog.'
##        #return ok
##

class ScaleTextElementPropertyPage(CoClass):
    u'Property page for scale text elements.'
    _reg_clsid_ = GUID('{48980FF2-F493-11D1-8788-0000F8751720}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
ScaleTextElementPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class MaplexAnnoLEPropsConflictPropertyPage(CoClass):
    u'Maplex Label engine layer properties conflict detection property page.'
    _reg_clsid_ = GUID('{20664808-6891-4F5B-BC95-7EFBB0B043A9}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
MaplexAnnoLEPropsConflictPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class BorderSelector(CoClass):
    u'Border style selector.'
    _reg_clsid_ = GUID('{EE23A189-DE16-11D2-B868-00600802E603}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
BorderSelector._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IStyleSelector, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IComPropertySheetEvents]

class MaplexAnnoLEPropsDensityPropertyPage(CoClass):
    u'Maplex Label engine layer properties density property page.'
    _reg_clsid_ = GUID('{BC96DE18-B4C1-0AC3-99D1-DD65C36B26CA}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
MaplexAnnoLEPropsDensityPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class ScaleBarScalePropertyPage(CoClass):
    u"Property page for a scale bar's scale and units."
    _reg_clsid_ = GUID('{17D0529D-1CF6-11D3-B8A6-00600802E603}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
ScaleBarScalePropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class TableHistogram(CoClass):
    u'A histogram data structure that is created from table data.  Use this to pass data to a classification object.'
    _reg_clsid_ = GUID('{962BD9AA-1EC8-11D3-9F4D-00C04F6BC709}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
TableHistogram._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IBasicHistogram, IHistogram, IHistogram2, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ITableHistogram, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDataNormalization, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStatisticsResults]

class ClassificationDialog(CoClass):
    u'A dialog for working with properties of a classification.'
    _reg_clsid_ = GUID('{3E055F76-2288-11D3-9F4F-00C04F6BC709}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
ClassificationDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IClassificationDialog]

class MaplexAnnoLEPropsAdvancedPropertyPage(CoClass):
    u'Maplex Label engine layer properties advanced property page.'
    _reg_clsid_ = GUID('{AFC14898-D832-2A8B-DCF5-3EE2CBA0B781}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
MaplexAnnoLEPropsAdvancedPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class CustomOverlayGridFactory(CoClass):
    u'Custom overlay grid factory class.'
    _reg_clsid_ = GUID('{FBECFD5F-D7D7-11D2-9F44-00C04F6BC78E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
CustomOverlayGridFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMapGridFactory]

class BackgroundSelector(CoClass):
    u'Background style selector.'
    _reg_clsid_ = GUID('{EE23A18A-DE16-11D2-B868-00600802E603}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
BackgroundSelector._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IStyleSelector, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IComPropertySheetEvents]

class DataExclusionQueryPropertyPage(CoClass):
    u'Data exclusion property page for working with query properties.'
    _reg_clsid_ = GUID('{F4ADC64F-A76D-11D2-AB27-00C04FA334B3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
DataExclusionQueryPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

IAVObject._methods_ = [
    COMMETHOD(['propget', helpstring(u'Type of object.')], HRESULT, 'Type',
              ( ['retval', 'out'], POINTER(BSTR), 'Type' )),
    COMMETHOD(['propput', helpstring(u'Type of object.')], HRESULT, 'Type',
              ( ['in'], BSTR, 'Type' )),
    COMMETHOD(['propget', helpstring(u'Number of properties for the object.')], HRESULT, 'PropertyCount',
              ( ['retval', 'out'], POINTER(c_int), 'count' )),
    COMMETHOD(['propget', helpstring(u'The properties at the given index.')], HRESULT, 'Property',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IProperty)), 'prop' )),
    COMMETHOD([helpstring(u'Adds a property to the object.')], HRESULT, 'AddProperty',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IProperty), 'prop' )),
    COMMETHOD([helpstring(u"Returns the value of one of the object's properties.  Only valid if you're expecting a single property with the given name.")], HRESULT, 'QueryPropertyValue',
              ( ['in'], BSTR, 'propertyName' ),
              ( ['retval', 'out'], POINTER(BSTR), 'value' )),
    COMMETHOD([helpstring(u'Clears out all of the properties of the object.')], HRESULT, 'ClearProperties'),
]
################################################################
## code template for IAVObject implementation
##class IAVObject_Impl(object):
##    def ClearProperties(self):
##        u'Clears out all of the properties of the object.'
##        #return 
##
##    def AddProperty(self, prop):
##        u'Adds a property to the object.'
##        #return 
##
##    def QueryPropertyValue(self, propertyName):
##        u"Returns the value of one of the object's properties.  Only valid if you're expecting a single property with the given name."
##        #return value
##
##    @property
##    def Property(self, index):
##        u'The properties at the given index.'
##        #return prop
##
##    def _get(self):
##        u'Type of object.'
##        #return Type
##    def _set(self, Type):
##        u'Type of object.'
##    Type = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def PropertyCount(self):
##        u'Number of properties for the object.'
##        #return count
##

class ScaleBarFormatPropertyPage(CoClass):
    u"Property page for a scale bar's format."
    _reg_clsid_ = GUID('{17D0529F-1CF6-11D3-B8A6-00600802E603}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
ScaleBarFormatPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

ILabelEngineChecker._methods_ = [
    COMMETHOD([helpstring(u'Checks for label engine inconsistencies for a set of layers and displays the dialog if necessary.')], HRESULT, 'CheckForLabelEngine',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMap), 'Map' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IArray), 'Layers' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentHWnd' )),
]
################################################################
## code template for ILabelEngineChecker implementation
##class ILabelEngineChecker_Impl(object):
##    def CheckForLabelEngine(self, Map, Layers, parentHWnd):
##        u'Checks for label engine inconsistencies for a set of layers and displays the dialog if necessary.'
##        #return 
##

class GraphicsLayerAnnoPropertyPage(CoClass):
    u'Property page for managing annotation properties for read-only graphics layers.'
    _reg_clsid_ = GUID('{57BC7953-0FD7-11D3-9F83-00C04F6BC6A5}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
GraphicsLayerAnnoPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class SymbolBackgroundPropertyPage(CoClass):
    u'Property page for Symbol Backgrounds.'
    _reg_clsid_ = GUID('{BBCFA856-DE33-11D2-B868-00600802E603}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
SymbolBackgroundPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class MaplexAnnoPlacementPropertyPluginPage(CoClass):
    u'An annotation placement properties page designed to be plugged into a host dialog.'
    _reg_clsid_ = GUID('{5C4FFB3B-6B31-4510-8237-CD5289F4F72F}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
MaplexAnnoPlacementPropertyPluginPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class DataSamplingPropertyPage(CoClass):
    u'Data sampling property page.'
    _reg_clsid_ = GUID('{5A51E1DF-2DAF-11D3-9F52-00C04F6BC709}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
DataSamplingPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class SymbolShadowPropertyPage(CoClass):
    u'Property page for Symbol Shadows.'
    _reg_clsid_ = GUID('{F667263B-C1B9-4EB0-B0A3-220786D14804}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
SymbolShadowPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class IIdentifyDialogProps(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control Identify dialog properties.'
    _iid_ = GUID('{2442004F-03FE-11D4-9FE9-00C04F6BC78E}')
    _idlflags_ = ['oleautomation']
IIdentifyDialogProps._methods_ = [
    COMMETHOD(['propget', helpstring(u'The layers eligible for searching.')], HRESULT, 'Layers',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IEnumLayer)), 'Layers' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the search stops once a result has been found.')], HRESULT, 'TopmostOnly',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD(['propget', helpstring(u'The flash effect.')], HRESULT, 'FlashEffect',
              ( ['retval', 'out'], POINTER(c_short), 'effect' )),
    COMMETHOD(['propput', helpstring(u'The flash effect.')], HRESULT, 'FlashEffect',
              ( ['in'], c_short, 'effect' )),
]
################################################################
## code template for IIdentifyDialogProps implementation
##class IIdentifyDialogProps_Impl(object):
##    @property
##    def Layers(self):
##        u'The layers eligible for searching.'
##        #return Layers
##
##    @property
##    def TopmostOnly(self):
##        u'Indicates if the search stops once a result has been found.'
##        #return flag
##
##    def _get(self):
##        u'The flash effect.'
##        #return effect
##    def _set(self, effect):
##        u'The flash effect.'
##    FlashEffect = property(_get, _set, doc = _set.__doc__)
##

class AreaGraphicPropertyPage(CoClass):
    u'Area graphic element property page.'
    _reg_clsid_ = GUID('{F1E616F2-13CE-4B0A-8132-BCE093D8566D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
AreaGraphicPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class ColumnAndMarginPropertyPage(CoClass):
    u'Property page for Columns and Margins.'
    _reg_clsid_ = GUID('{ADA81873-9E76-4A5C-A4A4-40F6369E0BDB}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
ColumnAndMarginPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class LabelManagerDialog(CoClass):
    u'Esri Label Manager Dialog.'
    _reg_clsid_ = GUID('{F2C2000F-930C-44C3-92F1-339996823014}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
LabelManagerDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ILabelManagerDialog]

class InteriorLabelsPropertyPage(CoClass):
    u'Property page for interior grid labels.'
    _reg_clsid_ = GUID('{A699C566-C325-4380-874F-82EB2CAF89B7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
InteriorLabelsPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class LabelStylePropertyPage(CoClass):
    u'A label Style property page.'
    _reg_clsid_ = GUID('{4C90DE7C-CB77-11D2-9F34-00C04F6BC6A5}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
LabelStylePropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class FunctionSeriesProperties(CoClass):
    u'A container for the display and manipulation of function graph series.'
    _reg_clsid_ = GUID('{98C74457-BA05-4284-A0F8-D5B45711176A}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
FunctionSeriesProperties._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ISeriesProperties, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IFunctionSeriesProperties, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IFeatureLayerSelectionEvents, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ISelectionEvents, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDefinitionExpressionEvents]

class DataGraphTLegendProperties(CoClass):
    u'A container for the display and manipulation of graph legend properties.'
    _reg_clsid_ = GUID('{29EB4BCD-314F-4F09-B40A-908F34C6F695}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
DataGraphTLegendProperties._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDataGraphTLegendProperties]

class DataGraphTGeneralProperties(CoClass):
    u'A container for the display and manipulation of graph general  properties.'
    _reg_clsid_ = GUID('{79AF7A4B-249F-48C0-9191-3E3B25A36D2D}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
DataGraphTGeneralProperties._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDataGraphTGeneralProperties]

class LabelWeightRankingDialog(CoClass):
    u'Esri Label Weight Ranking Dialog.'
    _reg_clsid_ = GUID('{9936A70D-5A1F-42CE-81D7-B1C120415C7D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
LabelWeightRankingDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ILabelWeightRankingDialog]

class AVObject(CoClass):
    u'An ArcView (3.x) generic object.'
    _reg_clsid_ = GUID('{049EADD2-DD95-11D3-9FD4-00C04F6BC78E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
AVObject._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IAVObject]

class CadAnnotationLayerFactory(CoClass):
    u'Esri CAD Annotation Layer Factory.'
    _reg_clsid_ = GUID('{26D73023-A5FE-11D4-A216-444553547777}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
CadAnnotationLayerFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayerFactory]

class AVObjectConverter(CoClass):
    u'An ArcView (3.x) object converter.'
    _reg_clsid_ = GUID('{049EADD4-DD95-11D3-9FD4-00C04F6BC78E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
AVObjectConverter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IAVObjectConverter]

class AnnoPlacementPropertyPluginPage(CoClass):
    u'An annotation placement properties page designed to be plugged into a host dialog.'
    _reg_clsid_ = GUID('{2C73BCC0-D23D-43B4-A081-CD0F17A0FE58}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
AnnoPlacementPropertyPluginPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class SQLQueryDialog(CoClass):
    u'Esri SQL Query Dialog.'
    _reg_clsid_ = GUID('{4EA8EB39-E784-4A23-BCBF-2462CE9D6975}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
SQLQueryDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ISQLQueryDialog, ISQLQueryDialog2]

class DataGraphTVerticalAxisProperties(CoClass):
    u'A container for the display and manipulation of graph vertical axis properties.'
    _reg_clsid_ = GUID('{8A0E82DD-2010-4AEB-9734-B2643ED82CA8}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
DataGraphTVerticalAxisProperties._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDataGraphTAxisProperties]

class LabelWeightsPropertyPage(CoClass):
    u'Esri label engine weights ranking property page.'
    _reg_clsid_ = GUID('{F457915F-4A4D-4FD3-9E52-68F6ECA3B870}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
LabelWeightsPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class DataGraphTPenProperties(CoClass):
    u'A container for the display and manipulation of graph series pen properties.'
    _reg_clsid_ = GUID('{73919A85-F719-47C9-9947-A9C143E15C86}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
DataGraphTPenProperties._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDataGraphTPenProperties]

class DataGraphT(CoClass):
    u'A container for the display and manipulation of graph series.'
    _reg_clsid_ = GUID('{58B570A4-02AE-44FC-B36F-630AE32EA4E4}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
DataGraphT._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDataGraphBase, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDataGraphT, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IConnectionPointContainer, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceEditEvents]
DataGraphT._outgoing_interfaces_ = [comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDataGraphTEvents]

class DataGraphTScatterPlotMatrix(CoClass):
    u'A container for the display and manipulation of ScatterPlotMatrix graph.'
    _reg_clsid_ = GUID('{022964B5-AA6B-4A10-91E9-801AFF8788E6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
DataGraphTScatterPlotMatrix._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDataGraphBase, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDataGraphT, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IConnectionPointContainer, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceEditEvents]
DataGraphTScatterPlotMatrix._outgoing_interfaces_ = [comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDataGraphTEvents]

class AnnoDisplayPropertyPage(CoClass):
    u'Property page for managing display properties of annotation.'
    _reg_clsid_ = GUID('{B2F1FE6E-13DC-4D8C-9C16-646AEE52F2FC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
AnnoDisplayPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class ScaleFormatPropertyPage(CoClass):
    u'Property page for scale format.'
    _reg_clsid_ = GUID('{E7715239-A7F7-41CE-B33F-EE14D21B1F2D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
ScaleFormatPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class DataGraphTSymbolProperties(CoClass):
    u'A container for the display and manipulation of graph series symbol properties.'
    _reg_clsid_ = GUID('{168D3A1B-0CB0-48A6-A3EE-F75F74D2A3E5}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
DataGraphTSymbolProperties._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDataGraphTSymbolProperties]

class MapScalePropertyPage(CoClass):
    u'Property page for standard scales.'
    _reg_clsid_ = GUID('{E771523A-A7F7-41CE-B33F-EE14D21B1F2D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
MapScalePropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class DataGraphTElement(CoClass):
    u'A container for the display and manipulation of data graph graphic element on the ArcMap layout view.'
    _reg_clsid_ = GUID('{0A27330E-E388-4ADB-BB9E-AB301A2BD1DA}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
DataGraphTElement._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IElement, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IElementProperties, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IElementProperties2, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IElementProperties3, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDataGraphTElement, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IGraphicElement, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IBoundsProperties, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IGraphicsContainerProperty, comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ITransform2D, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IActiveViewEvents, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySupport, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDataGraphTEvents]

class ScatterPlotMatrixSeriesProperties(CoClass):
    u'A container for the display and manipulation of scatter plot matrix graph.'
    _reg_clsid_ = GUID('{ED97CD19-8F2B-419F-BA80-87866F59C29D}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
ScatterPlotMatrixSeriesProperties._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IScatterPlotMatrixSeriesProperties, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ISeriesProperties, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IHistogramSeriesProperties, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IPointSeriesProperties, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IFeatureLayerSelectionEvents, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ISelectionEvents, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDefinitionExpressionEvents]

class AnnoLabelClassesPropertyPage(CoClass):
    u'Property page for managing label classes in annotation layers.'
    _reg_clsid_ = GUID('{D5B08F1B-D160-468A-8CC1-8D58A74CFB4B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
AnnoLabelClassesPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class FeatureLayerHTMLPropertyPage(CoClass):
    u"Property page for managing a feature layer's HTML popup properties."
    _reg_clsid_ = GUID('{E08E0FB1-FA43-4119-8B4B-539FB6726D38}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
FeatureLayerHTMLPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class CFGeneralPage(CoClass):
    u'Cadastral fabric general property page.'
    _reg_clsid_ = GUID('{1FFE7AFC-E311-42B9-AB29-4A4AA9CC8F27}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
CFGeneralPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext]

IRendererUIDialog2._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The renderer.')], HRESULT, 'Renderer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IFeatureRenderer), 'rhs' )),
    COMMETHOD(['propputref', helpstring(u'The feature layer.')], HRESULT, 'FeatureLayer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IFeatureLayer), 'rhs' )),
    COMMETHOD([helpstring(u'Displays the dialog.')], HRESULT, 'DoModal',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentHWnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ok' )),
]
################################################################
## code template for IRendererUIDialog2 implementation
##class IRendererUIDialog2_Impl(object):
##    def DoModal(self, parentHWnd):
##        u'Displays the dialog.'
##        #return ok
##
##    def Renderer(self, rhs):
##        u'The renderer.'
##        #return 
##
##    def FeatureLayer(self, rhs):
##        u'The feature layer.'
##        #return 
##

class TimeTablePropertyPage(CoClass):
    u"Property page for managing a layer's time definition related properties."
    _reg_clsid_ = GUID('{1F6FB35E-E52B-4B78-830E-9316F7511B2B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
TimeTablePropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class GeneralLayerPropPage(CoClass):
    u'General property page for managing layer properties.'
    _reg_clsid_ = GUID('{49C65517-D260-11D2-9F48-00C04F8ED21A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
GeneralLayerPropPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class AnnoSymbologyPropertyPage(CoClass):
    u'Property page for managing symbology in annotation layers.'
    _reg_clsid_ = GUID('{383C40A7-31A4-4BBF-9F77-BBB28A9A3F3C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
AnnoSymbologyPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class IIdentifyDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control Identifying layers by OID or a point.'
    _iid_ = GUID('{F8AAB777-8B1E-11D3-9F7A-00C04F6BC886}')
    _idlflags_ = ['oleautomation']
IIdentifyDialog._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The map of identifying layers.')], HRESULT, 'Map',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMap), 'rhs' )),
    COMMETHOD(['propputref', helpstring(u'The display.')], HRESULT, 'Display',
              ( ['in'], POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IDisplay), 'rhs' )),
    COMMETHOD([helpstring(u'Clear shown layers.')], HRESULT, 'ClearLayers'),
    COMMETHOD([helpstring(u'Add layer and show objects that contain the given point.')], HRESULT, 'AddLayerIdentifyPoint',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer), 'pLayer' ),
              ( ['in'], c_int, 'x' ),
              ( ['in'], c_int, 'y' )),
    COMMETHOD([helpstring(u'Add layer and show object of the given OID.')], HRESULT, 'AddLayerIdentifyOID',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer), 'pLayer' ),
              ( ['in'], c_int, 'oid' )),
    COMMETHOD([helpstring(u'Show dialog.')], HRESULT, 'Show'),
]
################################################################
## code template for IIdentifyDialog implementation
##class IIdentifyDialog_Impl(object):
##    def Map(self, rhs):
##        u'The map of identifying layers.'
##        #return 
##
##    def AddLayerIdentifyOID(self, pLayer, oid):
##        u'Add layer and show object of the given OID.'
##        #return 
##
##    def Show(self):
##        u'Show dialog.'
##        #return 
##
##    def AddLayerIdentifyPoint(self, pLayer, x, y):
##        u'Add layer and show objects that contain the given point.'
##        #return 
##
##    def ClearLayers(self):
##        u'Clear shown layers.'
##        #return 
##
##    def Display(self, rhs):
##        u'The display.'
##        #return 
##

class IProtectNameCartoUI(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to dummy methods protecting name correctness.'
    _iid_ = GUID('{AD403ACA-007E-4B02-BC21-933F083EBFF3}')
    _idlflags_ = []
IProtectNameCartoUI._methods_ = [
    COMMETHOD([], HRESULT, 'ProtectOLE_HANDLE',
              ( [], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'aHandle' )),
    COMMETHOD([], HRESULT, 'ProtectOLE_COLOR',
              ( [], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_COLOR, 'aColor' )),
]
################################################################
## code template for IProtectNameCartoUI implementation
##class IProtectNameCartoUI_Impl(object):
##    def ProtectOLE_COLOR(self, aColor):
##        '-no docstring-'
##        #return 
##
##    def ProtectOLE_HANDLE(self, aHandle):
##        '-no docstring-'
##        #return 
##

class MarkerElementPropertyPage(CoClass):
    u'Marker graphic element property page.'
    _reg_clsid_ = GUID('{70D40611-F15D-11D0-83A0-080009B996CC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
MarkerElementPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

IAnnotationExpressionProperties._methods_ = [
    COMMETHOD(['propget', helpstring(u'The expression.')], HRESULT, 'Expression',
              ( ['retval', 'out'], POINTER(BSTR), 'Expression' )),
    COMMETHOD(['propput', helpstring(u'The expression.')], HRESULT, 'Expression',
              ( ['in'], BSTR, 'Expression' )),
    COMMETHOD(['propput', helpstring(u'Indicates if expression is simple.')], HRESULT, 'IsExpressionSimple',
              ( ['in'], VARIANT_BOOL, 'isSimple' )),
    COMMETHOD(['propget', helpstring(u'Indicates if expression is simple.')], HRESULT, 'IsExpressionSimple',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'isSimple' )),
    COMMETHOD(['propputref', helpstring(u'The expression parser.')], HRESULT, 'ExpressionParser',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IAnnotationExpressionEngine), 'parser' )),
    COMMETHOD(['propget', helpstring(u'The expression parser.')], HRESULT, 'ExpressionParser',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IAnnotationExpressionEngine)), 'parser' )),
    COMMETHOD(['propputref', helpstring(u'Feature class for testing the expression.')], HRESULT, 'DisplayFeatureClass',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass), 'FeatureClass' )),
    COMMETHOD(['propget', helpstring(u'Feature class for testing the expression.')], HRESULT, 'DisplayFeatureClass',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass)), 'FeatureClass' )),
]
################################################################
## code template for IAnnotationExpressionProperties implementation
##class IAnnotationExpressionProperties_Impl(object):
##    def _get(self):
##        u'Indicates if expression is simple.'
##        #return isSimple
##    def _set(self, isSimple):
##        u'Indicates if expression is simple.'
##    IsExpressionSimple = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def DisplayFeatureClass(self, FeatureClass):
##        u'Feature class for testing the expression.'
##        #return 
##
##    def _get(self):
##        u'The expression.'
##        #return Expression
##    def _set(self, Expression):
##        u'The expression.'
##    Expression = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def ExpressionParser(self, parser):
##        u'The expression parser.'
##        #return 
##

class MarkerLocationPropertyPage(CoClass):
    u'Marker location property page.'
    _reg_clsid_ = GUID('{70D40612-F15D-11D0-83A0-080009B996CC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
MarkerLocationPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class BarSeriesProperties(CoClass):
    u'A container for the display and manipulation of bar graph series.'
    _reg_clsid_ = GUID('{94463E3F-696E-4D47-93B0-CE05B3C05909}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
BarSeriesProperties._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ISeriesProperties, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IBarSeriesProperties, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDataSortSeriesProperties, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IFeatureLayerSelectionEvents, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ISelectionEvents, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDefinitionExpressionEvents]

class BoxPlotSeriesProperties(CoClass):
    u'A container for the display and manipulation of box plot graph series.'
    _reg_clsid_ = GUID('{04FE20CB-B9AA-4F9D-962B-E3FFC70D1F0D}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
BoxPlotSeriesProperties._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ISeriesProperties, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IBoxPlotSeriesProperties, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IFeatureLayerSelectionEvents, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ISelectionEvents, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDefinitionExpressionEvents]

class DataHistogram(CoClass):
    u'A histogram data structure that is created from data values.  Use this to pass data to a classification object.'
    _reg_clsid_ = GUID('{FD21F232-67A6-11D3-9F66-00C04F6BC709}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
DataHistogram._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IHistogram, IDataHistogram, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStatisticsResults]

class AnnotationClassesPropertyPage(CoClass):
    u'Property page for managing annotation extension properties for non-feature linked annotation layers.'
    _reg_clsid_ = GUID('{DFA5265E-0FC8-433A-81DC-8A168B0D138E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
AnnotationClassesPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class HistogramSeriesProperties(CoClass):
    u'A container for the display and manipulation of histogram graph series.'
    _reg_clsid_ = GUID('{C5177DF4-6816-4A3E-8BBA-F355D4EF0F8B}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
HistogramSeriesProperties._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ISeriesProperties, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IHistogramSeriesProperties, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IFeatureLayerSelectionEvents, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ISelectionEvents, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDefinitionExpressionEvents]

class PieSeriesProperties(CoClass):
    u'A container for the display and manipulation of pie graph series.'
    _reg_clsid_ = GUID('{D2EC88BD-06F8-4A72-802B-ED855A6CD8B0}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
PieSeriesProperties._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ISeriesProperties, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IPieSeriesProperties, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDataSortSeriesProperties, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IFeatureLayerSelectionEvents, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ISelectionEvents, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDefinitionExpressionEvents]

class LineSeriesProperties(CoClass):
    u'A container for the display and manipulation of line graph series.'
    _reg_clsid_ = GUID('{A281C113-88CA-47E9-8986-4BB645983090}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
LineSeriesProperties._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ISeriesProperties, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILineSeriesProperties, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDataSortSeriesProperties, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDataGroupSeriesProperties, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IFeatureLayerSelectionEvents, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ISelectionEvents, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDefinitionExpressionEvents]

class AnnoClassScaleRangeDialog(CoClass):
    u'Esri Annotation Feature Class Scale Range Dialog.'
    _reg_clsid_ = GUID('{E9612330-C5E4-40D8-82F0-3479AD382717}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
class ILabelScaleRangeDialog2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Label Scale Range Dialog.'
    _iid_ = GUID('{8A76F73D-88E2-448C-872D-762C59FF76C5}')
    _idlflags_ = ['oleautomation']
AnnoClassScaleRangeDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ILabelScaleRangeDialog, ILabelScaleRangeDialog2]

class CreateHyperlinkMacroDialog(CoClass):
    u'Hyperlink Macro Dialog.'
    _reg_clsid_ = GUID('{6E32E2F3-C6DA-4B90-B34C-613953001B62}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
CreateHyperlinkMacroDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ICreateHyperlinkMacroDialog]

class LayerDrawingPropertyPage(CoClass):
    u"Property page for managing a feature layer's drawing properties (symbology)."
    _reg_clsid_ = GUID('{1476C785-6F57-11D2-A2C6-080009B6F22B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
LayerDrawingPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class IIdentifyDialog2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control Identifying tables by OID.'
    _iid_ = GUID('{8329391F-1606-11D4-A69B-0008C7D3AE8D}')
    _idlflags_ = ['oleautomation']
IIdentifyDialog2._methods_ = [
    COMMETHOD([helpstring(u'Add table and show row of the given OID.')], HRESULT, 'AddTableIdentifyOID',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable), 'pSTable' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable), 'pNewOIDCopyTable' ),
              ( ['in'], c_int, 'oid' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the Identify Dialog is visible.')], HRESULT, 'Visible',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'vis' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the Identify Dialog is visible.')], HRESULT, 'Visible',
              ( ['in'], VARIANT_BOOL, 'vis' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether to hide Layers ComboBox in Identify Dialog.')], HRESULT, 'HideLayersComboBox',
              ( ['in'], VARIANT_BOOL, 'pHide' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether to hide Layers ComboBox in Identify Dialog.')], HRESULT, 'HideLayersComboBox',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pHide' )),
    COMMETHOD(['propputref', helpstring(u'The basic map of identifying layers.')], HRESULT, 'BasicMap',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IBasicMap), 'rhs' )),
    COMMETHOD([helpstring(u'Add layer and show objects that contain the given point.')], HRESULT, 'AddLayerIdentifyPoint',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer), 'pLayer' ),
              ( ['in'], c_int, 'x' ),
              ( ['in'], c_int, 'y' ),
              ( ['in'], c_int, 'tolerance' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'trackCancel' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the context menu for identify results should be hidden when the user right-clicks.')], HRESULT, 'HideContextMenu',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'hide' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the context menu for identify results should be hidden when the user right-clicks.')], HRESULT, 'HideContextMenu',
              ( ['in'], VARIANT_BOOL, 'hide' )),
    COMMETHOD([helpstring(u'Add layer and show object hit at given location.')], HRESULT, 'AddLayerIdentifyObject',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer), 'pLayer' ),
              ( ['in'], POINTER(IUnknown), 'object' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.IPoint), 'location' )),
    COMMETHOD([helpstring(u'Select a specific layer in the combobox. This only works if the dialog is visible.')], HRESULT, 'SelectLayer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer), 'pLayer' )),
]
################################################################
## code template for IIdentifyDialog2 implementation
##class IIdentifyDialog2_Impl(object):
##    def _get(self):
##        u'Indicates if the context menu for identify results should be hidden when the user right-clicks.'
##        #return hide
##    def _set(self, hide):
##        u'Indicates if the context menu for identify results should be hidden when the user right-clicks.'
##    HideContextMenu = property(_get, _set, doc = _set.__doc__)
##
##    def SelectLayer(self, pLayer):
##        u'Select a specific layer in the combobox. This only works if the dialog is visible.'
##        #return 
##
##    def BasicMap(self, rhs):
##        u'The basic map of identifying layers.'
##        #return 
##
##    def AddLayerIdentifyPoint(self, pLayer, x, y, tolerance, trackCancel):
##        u'Add layer and show objects that contain the given point.'
##        #return 
##
##    def _get(self):
##        u'Indicates if the Identify Dialog is visible.'
##        #return vis
##    def _set(self, vis):
##        u'Indicates if the Identify Dialog is visible.'
##    Visible = property(_get, _set, doc = _set.__doc__)
##
##    def AddLayerIdentifyObject(self, pLayer, object, location):
##        u'Add layer and show object hit at given location.'
##        #return 
##
##    def _get(self):
##        u'Indicates whether to hide Layers ComboBox in Identify Dialog.'
##        #return pHide
##    def _set(self, pHide):
##        u'Indicates whether to hide Layers ComboBox in Identify Dialog.'
##    HideLayersComboBox = property(_get, _set, doc = _set.__doc__)
##
##    def AddTableIdentifyOID(self, pSTable, pNewOIDCopyTable, oid):
##        u'Add table and show row of the given OID.'
##        #return 
##

class LabelScaleRangeDialog(CoClass):
    u'Esri Label Scale Range Dialog.'
    _reg_clsid_ = GUID('{F7488013-F1BA-4C6B-9EED-DC21C7D3E994}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
LabelScaleRangeDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ILabelScaleRangeDialog, ILabelScaleRangeDialog2]

class INetworkLayerUINames(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Protect names interface. Do not use.'
    _iid_ = GUID('{C675E8FD-1F2E-41F3-A35E-8D6A08653037}')
    _idlflags_ = ['hidden']
INetworkLayerUINames._methods_ = [
    COMMETHOD([helpstring(u'Protect names method. Do not use.')], HRESULT, 'AttributeValue'),
]
################################################################
## code template for INetworkLayerUINames implementation
##class INetworkLayerUINames_Impl(object):
##    def AttributeValue(self):
##        u'Protect names method. Do not use.'
##        #return 
##

class IAVThemeImporter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the ArcView (3.x) theme importer.'
    _iid_ = GUID('{56BBC8A2-E583-11D3-9FD8-00C04F6BC78E}')
    _idlflags_ = ['oleautomation']
IAVThemeImporter._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if the importer supports the given type of AV theme object.')], HRESULT, 'CanImport',
              ( ['in'], POINTER(IAVObject), 'themeObject' ),
              ( ['in'], POINTER(IAVObjectConverter), 'pConverter' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD([helpstring(u'Imports the AV theme object into a layer object.')], HRESULT, 'Import',
              ( ['in'], POINTER(IAVObject), 'themeObject' ),
              ( ['in'], POINTER(IAVObjectConverter), 'pConverter' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer)), 'Layer' )),
]
################################################################
## code template for IAVThemeImporter implementation
##class IAVThemeImporter_Impl(object):
##    def Import(self, themeObject, pConverter):
##        u'Imports the AV theme object into a layer object.'
##        #return Layer
##
##    @property
##    def CanImport(self, themeObject, pConverter):
##        u'Indicates if the importer supports the given type of AV theme object.'
##        #return flag
##

ILabelScaleRangeDialog2._methods_ = [
    COMMETHOD(['propget', helpstring(u'The minimum scale entered in the dialog.')], HRESULT, 'MinimumScale',
              ( ['retval', 'out'], POINTER(c_double), 'val' )),
    COMMETHOD(['propget', helpstring(u'The maximum scale entered in the dialog.')], HRESULT, 'MaximumScale',
              ( ['retval', 'out'], POINTER(c_double), 'val' )),
    COMMETHOD([helpstring(u'Shows the SQL query dialog.')], HRESULT, 'DoModal',
              ( ['in'], c_double, 'initialMinimumScale' ),
              ( ['in'], c_double, 'initialMaximumScale' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hwnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ok' )),
    COMMETHOD(['propputref', helpstring(u'Optional map. Set this before calling DoModal.')], HRESULT, 'Map',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMap), 'rhs' )),
]
################################################################
## code template for ILabelScaleRangeDialog2 implementation
##class ILabelScaleRangeDialog2_Impl(object):
##    @property
##    def MaximumScale(self):
##        u'The maximum scale entered in the dialog.'
##        #return val
##
##    def DoModal(self, initialMinimumScale, initialMaximumScale, hwnd):
##        u'Shows the SQL query dialog.'
##        #return ok
##
##    @property
##    def MinimumScale(self):
##        u'The minimum scale entered in the dialog.'
##        #return val
##
##    def Map(self, rhs):
##        u'Optional map. Set this before calling DoModal.'
##        #return 
##

class AnnoLEPropsExpressionPropertyPage(CoClass):
    u'A label engine layer properties expression property page.'
    _reg_clsid_ = GUID('{1D5849F5-0D33-11D2-A26F-080009B6F22B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
AnnoLEPropsExpressionPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class CombiUniqueValuePropertyPage(CoClass):
    u"Renderer property page for managing properties associated with the 'Unique values based on many fields' layer symbology option."
    _reg_clsid_ = GUID('{68E95091-E60D-11D2-9F31-00C04F6BC709}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
CombiUniqueValuePropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, IRendererPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class MaplexLabelStylePropertyPage(CoClass):
    u'A Maplex label Style property page.'
    _reg_clsid_ = GUID('{20664808-CB77-1AD2-9F34-0AC04D6EC6A5}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
MaplexLabelStylePropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class MaplexLabelStyleSelector(CoClass):
    u'Style selector for Maplex labels.'
    _reg_clsid_ = GUID('{20664808-CA09-1ADA-9FA4-0AB04DCBC6A5}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
MaplexLabelStyleSelector._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IStyleSelector, ILabelStyleSelector, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IComPropertySheetEvents]

class PointSeriesProperties(CoClass):
    u'A container for the display and manipulation of scatter plot graph series.'
    _reg_clsid_ = GUID('{08EBFEB4-0705-4C85-A940-A5EF65E5DCA0}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
PointSeriesProperties._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ISeriesProperties, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IPointSeriesProperties, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IFeatureLayerSelectionEvents, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ISelectionEvents, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IDefinitionExpressionEvents]

class CadUniqueValuePropertyPage(CoClass):
    u"Renderer property page for managing properties associated with the 'Cad fields' layer symbology option."
    _reg_clsid_ = GUID('{6CACDFE6-AED2-49B0-812E-085169DD4917}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
CadUniqueValuePropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, IRendererPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class MapGridSelector(CoClass):
    u'Style selector for map grids.'
    _reg_clsid_ = GUID('{17DFF3D4-E26D-11D2-AB07-000000000000}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
MapGridSelector._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IStyleSelector, IMapGridSelector, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IComPropertySheetEvents]

class MaplexOverposterOptionsPropertyPage(CoClass):
    u'Maplex overposter options properties page.'
    _reg_clsid_ = GUID('{E2364829-F464-45FF-B825-DE12E0CBA316}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
MaplexOverposterOptionsPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class PieChartPropertyPage(CoClass):
    u"Renderer property page for managing properties associated with the 'Pie charts' layer symbology option."
    _reg_clsid_ = GUID('{98DD7040-FEB4-11D3-9F7C-00C04F6BC709}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
PieChartPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, IRendererPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class MaplexWeightRankingDialog(CoClass):
    u'Esri Maplex Weight Ranking Dialog.'
    _reg_clsid_ = GUID('{D9C171EE-4FDF-4935-B4B6-4F2338347842}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
MaplexWeightRankingDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMaplexWeightRankingDialog]

class BarChartPropertyPage(CoClass):
    u"Renderer property page for managing properties associated with the 'Bar charts' layer symbology option."
    _reg_clsid_ = GUID('{98DD703F-FEB4-11D3-9F7C-00C04F6BC709}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
BarChartPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, IRendererPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class MaplexDictionaryDialog(CoClass):
    u'Esri Maplex Dictionary Dialog.'
    _reg_clsid_ = GUID('{26D5CF30-8040-4D69-8474-11F9D8ED57E6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
class IMaplexDictionaryDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Maplex Dictionary Dialog.'
    _iid_ = GUID('{E09F2EDA-B2C6-4367-95EC-F46B49FEF7EE}')
    _idlflags_ = ['oleautomation']
class IMaplexDictionaryDialog2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Maplex Dictionary Dialog.'
    _iid_ = GUID('{FE327AEA-66EA-87CB-BDD1-85D3F1AB2010}')
    _idlflags_ = ['oleautomation']
MaplexDictionaryDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMaplexDictionaryDialog, IMaplexDictionaryDialog2]

class AnnoLEPropsPlacementPropertyPage(CoClass):
    u'A label engine layer properties placement property page.'
    _reg_clsid_ = GUID('{027F41B1-0F77-11D2-A270-080009B6F22B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
AnnoLEPropsPlacementPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class StackedChartPropertyPage(CoClass):
    u"Renderer property page for managing properties associated with the 'Stacked charts' layer symbology option."
    _reg_clsid_ = GUID('{98DD7041-FEB4-11D3-9F7C-00C04F6BC709}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
StackedChartPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, IRendererPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class MaplexKeyNumberGroupDialog(CoClass):
    u'Esri Maplex Key Number Group Dialog.'
    _reg_clsid_ = GUID('{28EAB290-BE20-020A-FF5A-75DE4EA207AA}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
MaplexKeyNumberGroupDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMaplexKeyNumberGroupDialog]

class LengthGraphicPropertyPage(CoClass):
    u'Length graphic element property page.'
    _reg_clsid_ = GUID('{ECC02510-2F09-4421-A2FF-52011BC1BC55}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
LengthGraphicPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2]

class ProportionalSymbolPropertyPage(CoClass):
    u"Renderer property page for managing properties associated with the 'Proportional symbols' layer symbology option."
    _reg_clsid_ = GUID('{F891FE58-E796-11D2-9F31-00C04F6BC709}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
ProportionalSymbolPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, IRendererPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class MultiDotDensityPropertyPage(CoClass):
    u"Renderer property page for managing properties associated with the 'Dot density' layer symbology option."
    _reg_clsid_ = GUID('{D2025F16-0502-11D4-9F7C-00C04F6BC709}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
MultiDotDensityPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, IRendererPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

INetworkRendererPropertyPage._methods_ = [
    COMMETHOD(['propget', helpstring(u'Description of the renderer.')], HRESULT, 'Description',
              ( ['retval', 'out'], POINTER(BSTR), 'desc' )),
    COMMETHOD(['propget', helpstring(u'Renderer name for the specified renderer type.')], HRESULT, 'Name',
              ( ['in'], comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.esriNetworkRendererType, 'rendererType' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'Category for the renderer property page.')], HRESULT, 'Category',
              ( ['retval', 'out'], POINTER(BSTR), 'Category' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the property page is applicable to the specified renderer type.')], HRESULT, 'AppliesTo',
              ( ['in'], comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.esriNetworkRendererType, 'rendererType' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD(['propget', helpstring(u'Preview bitmap for the renderer that appears on the page.')], HRESULT, 'PreviewImage',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'hBitmap' )),
    COMMETHOD(['propget', helpstring(u'Renderer class id (unique identifier object).')], HRESULT, 'RendererClassID',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID)), 'clsid' )),
    COMMETHOD(['propget', helpstring(u'Property page class id (unique identifier object).')], HRESULT, 'ClassID',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID)), 'clsid' )),
    COMMETHOD([helpstring(u'Indicates if the network renderer can be edited by the property page.')], HRESULT, 'CanEdit',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.INetworkRenderer), 'obj' ),
              ( ['in', 'out'], POINTER(VARIANT_BOOL), 'result' )),
]
################################################################
## code template for INetworkRendererPropertyPage implementation
##class INetworkRendererPropertyPage_Impl(object):
##    @property
##    def Category(self):
##        u'Category for the renderer property page.'
##        #return Category
##
##    @property
##    def ClassID(self):
##        u'Property page class id (unique identifier object).'
##        #return clsid
##
##    @property
##    def Description(self):
##        u'Description of the renderer.'
##        #return desc
##
##    @property
##    def AppliesTo(self, rendererType):
##        u'Indicates if the property page is applicable to the specified renderer type.'
##        #return flag
##
##    @property
##    def PreviewImage(self):
##        u'Preview bitmap for the renderer that appears on the page.'
##        #return hBitmap
##
##    @property
##    def RendererClassID(self):
##        u'Renderer class id (unique identifier object).'
##        #return clsid
##
##    def CanEdit(self, obj):
##        u'Indicates if the network renderer can be edited by the property page.'
##        #return result
##
##    @property
##    def Name(self, rendererType):
##        u'Renderer name for the specified renderer type.'
##        #return Name
##

class GeneralLegendItemPropertyPage(CoClass):
    u'Property page for managing general legend item properties.'
    _reg_clsid_ = GUID('{C734D617-7A46-11D2-87D5-0000F8751720}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
GeneralLegendItemPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class VerticalLegendItemPropertyPage(CoClass):
    u'Property page for managing the properties of stacked legend items.'
    _reg_clsid_ = GUID('{C734D619-7A46-11D2-87D5-0000F8751720}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
VerticalLegendItemPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class NetworkDirtyAreaRendererPropertyPage(CoClass):
    u'Property page for managing the properties of the NetworkDirtyAreaRenderer object.'
    _reg_clsid_ = GUID('{20959F32-BFB5-4792-9C95-9DBCFCCF6637}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
NetworkDirtyAreaRendererPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, INetworkRendererPropertyPage]

class HorizontalLegendItemPropertyPage(CoClass):
    u'Property page for managing the properties of horizontal legend items.'
    _reg_clsid_ = GUID('{C734D618-7A46-11D2-87D5-0000F8751720}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
HorizontalLegendItemPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class IAVFSrcImporter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the ArcView (3.x) FSrc importer.'
    _iid_ = GUID('{56BBC8A3-E583-11D3-9FD8-00C04F6BC78E}')
    _idlflags_ = ['oleautomation']
IAVFSrcImporter._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if the importer supports the given type of AV FSrc object.')], HRESULT, 'CanImport',
              ( ['in'], POINTER(IAVObject), 'fsrcObj' ),
              ( ['in'], POINTER(IAVObjectConverter), 'pConverter' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD([helpstring(u'Imports the AV FSrc object into a FeatureClass object.')], HRESULT, 'Import',
              ( ['in'], POINTER(IAVObject), 'fsrcObj' ),
              ( ['in'], POINTER(IAVObjectConverter), 'pConverter' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass)), 'fclass' )),
]
################################################################
## code template for IAVFSrcImporter implementation
##class IAVFSrcImporter_Impl(object):
##    def Import(self, fsrcObj, pConverter):
##        u'Imports the AV FSrc object into a FeatureClass object.'
##        #return fclass
##
##    @property
##    def CanImport(self, fsrcObj, pConverter):
##        u'Indicates if the importer supports the given type of AV FSrc object.'
##        #return flag
##

class SimpleNetworkRendererPropertyPage(CoClass):
    u'Property page for managing the properties of the SimpleNetworkRenderer object.'
    _reg_clsid_ = GUID('{F454286D-ACEC-42B0-871B-C8C3489871A5}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
SimpleNetworkRendererPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, INetworkRendererPropertyPage]

class NorthArrowSelector(CoClass):
    u'Style selector for north arrows.'
    _reg_clsid_ = GUID('{A340840D-797F-11D2-87D4-0000F8751720}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
NorthArrowSelector._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IStyleSelector, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IComPropertySheetEvents]

class ScaleBarSelector(CoClass):
    u'Style selector for scalebars.'
    _reg_clsid_ = GUID('{A340840E-797F-11D2-87D4-0000F8751720}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
ScaleBarSelector._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IStyleSelector, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IComPropertySheetEvents]

class RotateTracker(CoClass):
    u'Tracker for rotation operations.'
    _reg_clsid_ = GUID('{66770312-FBC0-11D1-A24E-080009B6F22B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
RotateTracker._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IRotateTracker]

class LegendItemSelector(CoClass):
    u'Style selector for legend items.'
    _reg_clsid_ = GUID('{A340840F-797F-11D2-87D4-0000F8751720}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
LegendItemSelector._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IStyleSelector, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IComPropertySheetEvents]

class BiUniqueValuePropertyPage(CoClass):
    u"Renderer property page for managing properties associated with the 'Quantity by category' layer symbology option."
    _reg_clsid_ = GUID('{AE1248B6-CD1E-11D2-9F25-00C04F6BC709}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
BiUniqueValuePropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, IRendererPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class FeatureLayerSourcePropertyPage(CoClass):
    u"Property page for managing a feature layer's source."
    _reg_clsid_ = GUID('{A1A37857-D673-11D2-9F42-00C04F6BC78E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
FeatureLayerSourcePropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

IDotDensitySymbolUIDialog._methods_ = [
    COMMETHOD(['propputref', helpstring(u'Dot density fill symbol.')], HRESULT, 'Symbol',
              ( ['in'], POINTER(comtypes.gen._59FCCD31_434C_4017_BDEF_DB4B7EDC9CE0_0_10_2.IDotDensityFillSymbol), 'rhs' )),
    COMMETHOD(['propputref', helpstring(u'Layers available to the user for dot density masking.')], HRESULT, 'Layers',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IEnumLayer), 'rhs' )),
    COMMETHOD(['propget', helpstring(u'Dot density masking layer (i.e. the control layer).')], HRESULT, 'Layer',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer)), 'Layer' )),
    COMMETHOD([helpstring(u'Displays the dialog.')], HRESULT, 'DoModal',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentHWnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ok' )),
]
################################################################
## code template for IDotDensitySymbolUIDialog implementation
##class IDotDensitySymbolUIDialog_Impl(object):
##    def Layers(self, rhs):
##        u'Layers available to the user for dot density masking.'
##        #return 
##
##    def DoModal(self, parentHWnd):
##        u'Displays the dialog.'
##        #return ok
##
##    def Symbol(self, rhs):
##        u'Dot density fill symbol.'
##        #return 
##
##    @property
##    def Layer(self):
##        u'Dot density masking layer (i.e. the control layer).'
##        #return Layer
##

class QueryLayerSourcePropertyPage(CoClass):
    u"Property page for managing a query layer's source."
    _reg_clsid_ = GUID('{DA96B9F2-F1A7-4CC8-ABFE-68BF69EB8EED}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
QueryLayerSourcePropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class ScaleTextSelector(CoClass):
    u'Style selector for scale text.'
    _reg_clsid_ = GUID('{A3408410-797F-11D2-87D4-0000F8751720}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
ScaleTextSelector._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IStyleSelector, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IComPropertySheetEvents]

class LabelStyleSelector(CoClass):
    u'Style selector for labels.'
    _reg_clsid_ = GUID('{12CA6D17-CC09-11D2-9F34-00C04F6BC6A5}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
LabelStyleSelector._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IStyleSelector, ILabelStyleSelector, comtypes.gen._4ECCA6E2_B16B_4ACA_BD17_E74CAE4C150A_0_10_2.IComPropertySheetEvents]

class DefaultFeatureLayerSymbology(CoClass):
    u'Defines the default feature layer symbology.'
    _reg_clsid_ = GUID('{CA98D4ED-B734-4B61-92A1-8F922DAC54B1}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
DefaultFeatureLayerSymbology._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IFeatureLayerSymbology]

class LookupSymbolPropertyPage(CoClass):
    u"Renderer property page for managing properties associated with the 'Match to symbols in a style' layer symbology option."
    _reg_clsid_ = GUID('{90C47E6F-A102-11D2-AB24-00C04FA334B3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
LookupSymbolPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, IRendererPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class SingleSymbolPropertyPage(CoClass):
    u"Renderer property page for managing properties associated with the 'Single symbol' layer symbology option."
    _reg_clsid_ = GUID('{4EAB5691-8F9C-11D2-AB21-00C04FA334B3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
SingleSymbolPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, IRendererPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class GraticuleIntervalsPropertyPage(CoClass):
    u'Property page for graticule intervals.'
    _reg_clsid_ = GUID('{5F7E1D44-3DEA-411B-838A-49FC718201A2}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
GraticuleIntervalsPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class FeatureIdentifyObject(CoClass):
    u'Feature Identify Object.'
    _reg_clsid_ = GUID('{92B0C6D0-D361-11D2-8CD0-00C04F5B951E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
FeatureIdentifyObject._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IFeatureIdentifyObj, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IBasicMapIdentifyObject, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMapIdentifyObject, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IIdentifyObj, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IRowIdentifyObject]

class LegendPatchPropertyPage(CoClass):
    u'Property page for managing legend patch properties.'
    _reg_clsid_ = GUID('{12BA3732-4FF2-11D3-B8BD-00600802E603}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
LegendPatchPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class IdentifyDialog(CoClass):
    u'Identifying layers by OID or a point.'
    _reg_clsid_ = GUID('{F8AAB776-8B1E-11D3-9F7A-00C04F6BC886}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
IdentifyDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IIdentifyDialog, IIdentifyDialog2, IIdentifyDialogProps]

IRendererPropertyPage._methods_ = [
    COMMETHOD(['propget', helpstring(u'Renderer type. Used to group renderers into categories.')], HRESULT, 'Type',
              ( ['retval', 'out'], POINTER(BSTR), 'Type' )),
    COMMETHOD(['propget', helpstring(u'Renderer description.')], HRESULT, 'Description',
              ( ['retval', 'out'], POINTER(BSTR), 'desc' )),
    COMMETHOD(['propget', helpstring(u'Name of the renderer.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'Preview bitmap for the renderer that appears on the page.')], HRESULT, 'PreviewImage',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE), 'hBitmap' )),
    COMMETHOD(['propget', helpstring(u'Renderer class id (unique identifier object).')], HRESULT, 'RendererClassID',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID)), 'clsid' )),
    COMMETHOD(['propget', helpstring(u'Property page class id (unique identifier object).')], HRESULT, 'ClassID',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IUID)), 'clsid' )),
    COMMETHOD([helpstring(u'Indicates if the property page can modify the properties of the specified renderer.')], HRESULT, 'CanEdit',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IFeatureRenderer), 'obj' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'result' )),
]
################################################################
## code template for IRendererPropertyPage implementation
##class IRendererPropertyPage_Impl(object):
##    @property
##    def ClassID(self):
##        u'Property page class id (unique identifier object).'
##        #return clsid
##
##    @property
##    def Description(self):
##        u'Renderer description.'
##        #return desc
##
##    @property
##    def PreviewImage(self):
##        u'Preview bitmap for the renderer that appears on the page.'
##        #return hBitmap
##
##    @property
##    def RendererClassID(self):
##        u'Renderer class id (unique identifier object).'
##        #return clsid
##
##    @property
##    def Type(self):
##        u'Renderer type. Used to group renderers into categories.'
##        #return Type
##
##    def CanEdit(self, obj):
##        u'Indicates if the property page can modify the properties of the specified renderer.'
##        #return result
##
##    @property
##    def Name(self):
##        u'Name of the renderer.'
##        #return Name
##

class MapGridAxesPropertyPage(CoClass):
    u'Property page for map grid axes.'
    _reg_clsid_ = GUID('{B2F62B5F-A067-11D2-AAE0-000000000000}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
MapGridAxesPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class MapGridLinesPropertyPage(CoClass):
    u'Property page for map grid lines.'
    _reg_clsid_ = GUID('{8AF09A6B-A0DD-11D2-AE7F-080009EC732A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
MapGridLinesPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class GraduatedColorPropertyPage(CoClass):
    u"Renderer property page for managing properties associated with the 'Graduated colors' layer symbology option."
    _reg_clsid_ = GUID('{683C994F-A17B-11D1-8816-080009EC732A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
GraduatedColorPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, IRendererPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class CadLayerFactory(CoClass):
    u'Esri CAD Layer Factory.'
    _reg_clsid_ = GUID('{E299ADC3-A5C3-11D2-9B10-00C04FA33299}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
CadLayerFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayerFactory]

class CadFeatureLayerFactory(CoClass):
    u'Esri CAD Feature Layer Factory'
    _reg_clsid_ = GUID('{E0F384B5-E0C1-11D2-9B30-00C04FA33299}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
CadFeatureLayerFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayerFactory]

class MapGridLabelsPropertyPage(CoClass):
    u'Property page for map grid labels.'
    _reg_clsid_ = GUID('{8AF09A6F-A0DD-11D2-AE7F-080009EC732A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
MapGridLabelsPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class GraduatedSymbolPropertyPage(CoClass):
    u"Renderer property page for managing properties associated with the 'Graduated symbols' layer symbology option."
    _reg_clsid_ = GUID('{F891FE57-E796-11D2-9F31-00C04F6BC709}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
GraduatedSymbolPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, IRendererPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

IFeatureLayerSourcePageExtension._methods_ = [
    COMMETHOD(['propput', helpstring(u'The default description text.')], HRESULT, 'Description',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IFeatureLayer), 'pLayer' ),
              ( ['in'], BSTR, 'text' )),
    COMMETHOD(['propget', helpstring(u'The default description text.')], HRESULT, 'Description',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IFeatureLayer), 'pLayer' ),
              ( ['retval', 'out'], POINTER(BSTR), 'text' )),
    COMMETHOD([helpstring(u'Shows a custom dialog to change the data source.')], HRESULT, 'ShowDialog',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IFeatureLayer), 'pLayer' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentHWnd' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the data source can be changed.')], HRESULT, 'DataSourceReadOnly',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
]
################################################################
## code template for IFeatureLayerSourcePageExtension implementation
##class IFeatureLayerSourcePageExtension_Impl(object):
##    @property
##    def DataSourceReadOnly(self):
##        u'Indicates if the data source can be changed.'
##        #return flag
##
##    def _get(self, pLayer):
##        u'The default description text.'
##        #return text
##    def _set(self, pLayer, text):
##        u'The default description text.'
##    Description = property(_get, _set, doc = _set.__doc__)
##
##    def ShowDialog(self, pLayer, parentHWnd):
##        u'Shows a custom dialog to change the data source.'
##        #return 
##

class MapGridOverlayPropertyPage(CoClass):
    u'Property page for custom overlay grids.'
    _reg_clsid_ = GUID('{FBECFD60-D7D7-11D2-9F44-00C04F6BC78E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
MapGridOverlayPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

IMaplexDictionaryDialog._methods_ = [
    COMMETHOD([helpstring(u'Shows the Maplex Dictionary Dialog.')], HRESULT, 'DoModal',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMaplexDictionaries), 'pDictionaries' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hwnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ok' )),
]
################################################################
## code template for IMaplexDictionaryDialog implementation
##class IMaplexDictionaryDialog_Impl(object):
##    def DoModal(self, pDictionaries, hwnd):
##        u'Shows the Maplex Dictionary Dialog.'
##        #return ok
##

class SymbolLevelsDialog(CoClass):
    u'A dialog for setting symbol levels.'
    _reg_clsid_ = GUID('{C6F0AD3E-FA72-4110-A5AF-1B43857C6550}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
class ISymbolLevelsDialog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control a dialog for setting symbol levels.'
    _iid_ = GUID('{0F7205E2-7F9E-402E-9E2E-E8265D83FBF5}')
    _idlflags_ = ['oleautomation']
SymbolLevelsDialog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ISymbolLevelsDialog]

class MapCachePropertyPage(CoClass):
    u'Esri Feature Cache property page.'
    _reg_clsid_ = GUID('{554A9795-B465-4DE6-AEE8-D6B139A56B48}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
MapCachePropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

ISymbolLevelsDialog._methods_ = [
    COMMETHOD(['propput', helpstring(u'The Layer for which the symbol levels should be displayed.')], HRESULT, 'Layer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer), 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Add data to populate the symbol level list control.')], HRESULT, 'Symbols',
              ( ['in'], VARIANT, 'vSymbols' ),
              ( ['in'], VARIANT, 'vLabelNames' ),
              ( ['in'], VARIANT, 'vLayerNames' ),
              ( ['in'], VARIANT, 'rhs' )),
    COMMETHOD(['propget', helpstring(u'Provides access to the modified symbols from the dialog.')], HRESULT, 'SymbolArray',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IArray)), 'ppArray' )),
    COMMETHOD(['propput', helpstring(u'Indicates if symbol levels are used.')], HRESULT, 'UseSymbolLevels',
              ( ['in'], VARIANT_BOOL, 'pbUsesLevels' )),
    COMMETHOD(['propget', helpstring(u'Indicates if symbol levels are used.')], HRESULT, 'UseSymbolLevels',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbUsesLevels' )),
    COMMETHOD([helpstring(u'Enable apply button in dialog and pass map to refresh if apply is pressed. ')], HRESULT, 'EnableApplyButton',
              ( ['in'], VARIANT_BOOL, 'bEnable' ),
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMap), 'pMap' )),
    COMMETHOD(['propput', helpstring(u'Inform the dialog about a layer that controls the symbol levels at a more global scope.')], HRESULT, 'ControlLayer',
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayer), 'rhs' )),
    COMMETHOD([helpstring(u'Displays the dialog.')], HRESULT, 'DoModal',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'parentHWnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ok' )),
]
################################################################
## code template for ISymbolLevelsDialog implementation
##class ISymbolLevelsDialog_Impl(object):
##    def _set(self, rhs):
##        u'The Layer for which the symbol levels should be displayed.'
##    Layer = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Inform the dialog about a layer that controls the symbol levels at a more global scope.'
##    ControlLayer = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, vSymbols, vLabelNames, vLayerNames, rhs):
##        u'Add data to populate the symbol level list control.'
##    Symbols = property(fset = _set, doc = _set.__doc__)
##
##    def EnableApplyButton(self, bEnable, pMap):
##        u'Enable apply button in dialog and pass map to refresh if apply is pressed. '
##        #return 
##
##    @property
##    def SymbolArray(self):
##        u'Provides access to the modified symbols from the dialog.'
##        #return ppArray
##
##    def DoModal(self, parentHWnd):
##        u'Displays the dialog.'
##        #return ok
##
##    def _get(self):
##        u'Indicates if symbol levels are used.'
##        #return pbUsesLevels
##    def _set(self, pbUsesLevels):
##        u'Indicates if symbol levels are used.'
##    UseSymbolLevels = property(_get, _set, doc = _set.__doc__)
##

IMaplexDictionaryDialog2._methods_ = [
    COMMETHOD([helpstring(u'Shows the Maplex Dictionary Dialog.')], HRESULT, 'DoModal',
              ( ['in'], VARIANT_BOOL, 'readOnly' ),
              ( ['in'], POINTER(comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.IMaplexDictionaries), 'pDictionaries' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'hwnd' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ok' )),
]
################################################################
## code template for IMaplexDictionaryDialog2 implementation
##class IMaplexDictionaryDialog2_Impl(object):
##    def DoModal(self, readOnly, pDictionaries, hwnd):
##        u'Shows the Maplex Dictionary Dialog.'
##        #return ok
##

class FeatureLayerDisplayPropertyPage(CoClass):
    u"Property page for managing a feature layer's display properties."
    _reg_clsid_ = GUID('{A1A37858-D673-11D2-9F42-00C04F6BC78E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
FeatureLayerDisplayPropertyPage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPage, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IPropertyPageContext, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage2, comtypes.gen._866AE5D3_530C_11D2_A2BD_0000F8774FB5_0_10_2.IComPropertyPage]

class CoverageAnnotationLayerFactory(CoClass):
    u'A factory for creating coverage annotation layers.'
    _reg_clsid_ = GUID('{0C22A4C8-DAFD-11D2-9F46-00C04F6BC78E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{D92377DC-FAB1-4DFB-A4C1-61BD8C40DBEB}', 10, 2)
CoverageAnnotationLayerFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ILayerFactory, comtypes.gen._45AC68FF_DEFF_4884_B3A9_7D882EDCAEF1_0_10_2.ICoverageAnnotationLayerFactory]

__all__ = ['DataFrameShapeDialog', 'IAVObject',
           'GeneralLayerPropPage', 'IndexGridPropertyPage',
           'IClassificationDialog', 'DataGraphTElement', 'DataGraphT',
           'LabelStyleSelector', 'GraticuleFactory',
           'DataExclusionQueryPropertyPage',
           'MaplexLabelStyleSelector',
           'MaplexAnnoPlacementPropertyPluginPage',
           'CFDataSourcePageExtension', 'GraduatedSymbolPropertyPage',
           'IMapGridFactory', 'IProtectNameCartoUI',
           'MapGridLabelsPropertyPage', 'CreateHyperlinkMacroDialog',
           'IDataHistogram', 'QueryWizard', 'LineElementPropertyPage',
           'SymbolBorderPropertyPage', 'CalibratedBorderPropertyPage',
           'LabelPriorityRankingDialog',
           'AnnoLEPropsPlacementPropertyPage',
           'FeatureAdjustmentAssociationPage',
           'AnnoSymbologyPropertyPage', 'AreaGraphicPropertyPage',
           'LabelScaleRangeDialog', 'LabelDefinitionPropertyPage',
           'IDatumChecker', 'LookupSymbolPropertyPage',
           'LayerDrawingPropertyPage', 'SizeAndPositionPropertyPage',
           'ILabelWeightRankingDialog', 'IIdentifyDialog',
           'NorthArrowSelector', 'AnnoLabelClassesPropertyPage',
           'ILabelPriorityRankingDialog',
           'DataGraphTScatterPlotMatrix', 'BarSeriesProperties',
           'CustomOverlayGridFactory', 'IMaplexDictionaryDialog2',
           'IAVFSrcImporter', 'SymbolLevelDialog',
           'ScaleBarFormatPropertyPage',
           'NorthArrowElementPropertyPage', 'CornerLabelPropertyPage',
           'ProportionalSymbolPropertyPage', 'ILabelStyleSelector',
           'ScaleBarScalePropertyPage', 'MapFramePropertyPage',
           'CadLayerFactory', 'IndexGridFactory',
           'INewGeoTransformationDialog2', 'DataSamplingPropertyPage',
           'IMaplexDictionaryDialog', 'IQueryWizard',
           'MapScalePropertyPage', 'StackedChartPropertyPage',
           'LineSeriesProperties', 'GridHatchPropertyPage',
           'MaplexAnnoLEPropsStrategyPropertyPage',
           'PieChartPropertyPage',
           'IFeatureAdjustmentAssociationPage',
           'CombiUniqueValuePropertyPage',
           'MaplexExpressionPropertyPage',
           'MixedFontLabelPropertyPage', 'LabelManagerDialog',
           'AnnotationSublayerInfoPropertyPage',
           'TimeTablePropertyPage', 'IMaplexWeightRankingDialog',
           'IAdvancedDrawingDialog', 'MapGridAxesPropertyPage',
           'MaplexAnnoLEPropsStackingPropertyPage',
           'GroupLayerPropertyPage', 'MapGridLinesPropertyPage',
           'IDotDensitySymbolUIDialog', 'ColumnAndMarginPropertyPage',
           'LabelEngineChecker', 'NewGeoTransformationDialog',
           'InteriorLabelsPropertyPage',
           'CadastralFabricLayerHistoryPropPage',
           'DataGraphTGeneralProperties', 'ISQLQueryDialog2',
           'IMapGridWizard', 'OverposterGeneralPropertyPage',
           'LabelWeightRankingDialog', 'IHistogram',
           'DmsLabelPropertyPage', 'MarkerSizeDialog',
           'ILabelScaleRangeDialog', 'DataFrameAreaOfInterestDialog',
           'MgrsGridFactory', 'IAVObjectConverter',
           'CovAnnoLevelPropertyPage', 'IdentifyDialog',
           'AnnoClassScaleRangeDialog', 'ScaleBarSelector',
           'GraticuleIntervalsPropertyPage',
           'LayerLabelsPropertyPage', 'DotDensitySymbolUIDialog',
           'IDatumChecker2', 'AreaSeriesProperties',
           'MaplexAnnoLEPropsDensityPropertyPage',
           'AnnoLEPropsConflictPropertyPage', 'MeasuredGridFactory',
           'CoverageAnnotationLayerFactory', 'MaplexDictionaryDialog',
           'TableHistogram', 'DisplayStringPropPage',
           'IAVThemeImporter', 'IDataFrameClippingDialog',
           'IRendererUIDialog', 'AnnotationClassPropertyPage',
           'PieSeriesProperties', 'MarkerLocationPropertyPage',
           'TextElementPropertyPage', 'MapCachePropertyPage',
           'IndexTabPropertyPage', 'MarkerRotationDialog',
           'LabelStylePropertyPage', 'IHistogram2', 'CFSourcePage',
           'INetworkRendererPropertyPage', 'IRendererPropertyPage',
           'GraphicsLayerAnnoPropertyPage',
           'MapGridSystemPropertyPage', 'DataGraphTPenProperties',
           'FeatureLayerDisplayPropertyPage', 'SQLQueryDialog',
           'ScaleTextSelector', 'PieSizeDialog',
           'ScaleFormatPropertyPage', 'LegendLayoutPropertyPage',
           'CFSubClassesPage', 'MapGridWizard',
           'HorizontalBarLegendItemPropertyPage',
           'LegendElementPropertyPage', 'MaplexWeightRankingDialog',
           'IMaplexKeyNumberGroupDialog', 'IIdentifyDialogProps',
           'ILegendWizard', 'ISymbolLevelsDialog',
           'INetworkLayerUINames', 'BiUniqueValuePropertyPage',
           'CadFeatureLayerFactory', 'INewGeoTransformationDialog',
           'NestedLegendItemPropertyPage',
           'LayerDefinitionQueryPropertyPage',
           'ScaleBarLabelsAndMarksPropertyPage',
           'AnnotationClassesFLPropertyPage', 'GxBrowserFactory',
           'AVObjectConverter', 'LegendElementItemsPropertyPage',
           'FeatureLayerHTMLPropertyPage',
           'DataGraphTVerticalAxisProperties', 'RotateTracker',
           'ScaleTextElementPropertyPage',
           'MaplexAnnoLEPropsConflictPropertyPage',
           'MapGraphicsLayerPropertyPage',
           'GroupLayerDisplayPropertyPage',
           'VerticalLegendItemPropertyPage',
           'AnnotationClassesPropertyPage', 'DataFrameClippingDialog',
           'SingleSymbolPropertyPage', 'LegendPatchPropertyPage',
           'MaplexOverposterOptionsPropertyPage',
           'CadAnnotationLayerFactory', 'MultiDotDensityPropertyPage',
           'CFAssociationsPage', 'AdvancedDrawingDialog',
           'DataGraphTHorizontalAxisProperties', 'DataHistogram',
           'ILabelManagerDialog', 'DatumChecker',
           'TimeDataPropertyPage', 'AnnotationExpressionProperties',
           'TransparencyFieldDialog',
           'FeatureLayerSelectionPropertyPage',
           'BoxPlotSeriesProperties', 'CFEditEnvironmentPage',
           'AnnoDisplayPropertyPage', 'PictureElementPropertyPage',
           'GeneralLegendItemPropertyPage', 'ISymbolLevelDialog',
           'LayerFieldsPropertyPage',
           'NetworkDirtyAreaRendererPropertyPage',
           'HistogramSeriesProperties', 'PrincipalDigitsPropertyPage',
           'MapGridIntervalsPropertyPage',
           'MapGridOverlayPropertyPage',
           'IDataFrameAreaOfInterestDialog', 'IIdentifyDialog2',
           'CovAnnoFontPropertyPage', 'IDataFrameFixedExtentDialog',
           'LengthGraphicPropertyPage', 'BarChartPropertyPage',
           'MaplexKeyNumberGroupDialog', 'SymbolLevelsDialog',
           'ScatterPlotMatrixSeriesProperties', 'LegendWizard',
           'MaplexAnnoLEPropsPlacementPropertyPage',
           'FillShapeElementPropertyPage',
           'MapFrameLocatorPropertyPage',
           'CadUniqueValuePropertyPage', 'MapGridStyleGalleryClass',
           'BarSizeDialog', 'FeatureLayerSourcePropertyPage',
           'MaplexAnnoLEPropsAdvancedPropertyPage', 'ShadowSelector',
           'DefaultFeatureLayerSymbology',
           'HorizontalLegendItemPropertyPage', 'RowIdentifyObject',
           'UniqueValuePropertyPage', 'MaplexLabelStylePropertyPage',
           'ILabelEngineChecker', 'ILabelScaleRangeDialog2',
           'MapGridSelector', 'ISQLQueryDialog', 'BorderSelector',
           'AVObject', 'IRendererUIDialog2',
           'LabelWeightsPropertyPage',
           'AnnoLEPropsExpressionPropertyPage',
           'AnnoPlacementPropertyPluginPage', 'PointSeriesProperties',
           'NetworkTrafficRendererPropertyPage',
           'DataFrameFixedExtentDialog', 'DataGraphTLegendProperties',
           'FunctionSeriesProperties', 'QueryLayerSourcePropertyPage',
           'MgrsGridPropertyPage', 'IFeatureLayerSourcePageExtension',
           'DataGraphTSymbolProperties', 'MapProjectionPropPage',
           'FeatureIdentifyObject', 'GraduatedColorPropertyPage',
           'CFGeneralPage', 'SimpleNetworkRendererPropertyPage',
           'LegendItemSelector', 'FramePropertyPage',
           'ClassificationDialog', 'IMapGridSelector',
           'MarkerElementPropertyPage', 'ScaleTextPropertyPage',
           'ScaleTracker', 'DataExclusionPropertyPage',
           'SymbolShadowPropertyPage', 'BackgroundSelector',
           'ICreateHyperlinkMacroDialog',
           'SymbolBackgroundPropertyPage',
           'IAnnotationExpressionProperties']
from comtypes import _check_version; _check_version('501')

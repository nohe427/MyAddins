# -*- coding: mbcs -*-
typelib_path = u'C:\\Program Files (x86)\\ArcGIS\\Engine10.2\\com\\esriDataSourcesNetCDF.olb'
_lcid = 0 # change this if required
from ctypes import *
import comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2
import comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2
import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0
from comtypes import GUID
from ctypes import HRESULT
from comtypes import helpstring
from comtypes import COMMETHOD
from comtypes import dispid
from comtypes import BSTR
from comtypes.automation import VARIANT
import comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2
from comtypes import CoClass


class Library(object):
    u'Esri DataSourcesNetCDF Object Library 10.2'
    name = u'esriDataSourcesNetCDF'
    _reg_typelib_ = ('{28ED84CD-FB06-41A0-9A55-E196441D169A}', 10, 2)

class IProtectNamesDataSourcesNetCDF(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{00E0F03E-D94D-4CB0-A711-7F7C59C51196}')
    _idlflags_ = ['hidden']
IProtectNamesDataSourcesNetCDF._methods_ = [
    COMMETHOD([], HRESULT, 'Variable'),
]
################################################################
## code template for IProtectNamesDataSourcesNetCDF implementation
##class IProtectNamesDataSourcesNetCDF_Impl(object):
##    def Variable(self):
##        '-no docstring-'
##        #return 
##

class IMDDatasetView(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'The Multi Dimension DatasetView Interface.'
    _iid_ = GUID('{4656178F-0EDA-4446-9D51-900E96EFD27C}')
    _idlflags_ = ['oleautomation']
IMDDatasetView._methods_ = [
    COMMETHOD([helpstring(u'Selects the dimension for viewing by a value.')], HRESULT, 'SelectDimensionByValue',
              ( ['in'], BSTR, 'dim' ),
              ( ['in'], VARIANT, 'vValue' )),
    COMMETHOD([helpstring(u'Selects the dimension for viewing by an index.')], HRESULT, 'SelectDimensionByIndex',
              ( ['in'], BSTR, 'dim' ),
              ( ['in'], c_int, 'index' )),
    COMMETHOD([helpstring(u'The selected dimension value for a dimension name.')], HRESULT, 'GetDimensionValue',
              ( ['in'], BSTR, 'dim' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD([helpstring(u'The selected dimension index for a dimension name.')], HRESULT, 'GetDimensionIndex',
              ( ['in'], BSTR, 'dim' ),
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD([helpstring(u'The selected dimension names.')], HRESULT, 'GetSelectedDimensions',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'ppNames' )),
    COMMETHOD([helpstring(u'The selected dimension values.')], HRESULT, 'GetSelectedDimensionValues',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IVariantArray)), 'ppValues' )),
    COMMETHOD([helpstring(u'Indices for the values of selected dimensions.')], HRESULT, 'GetSelectedDimensionIndices',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray)), 'ppIndices' )),
    COMMETHOD([helpstring(u'Clears a selected list of dimensions and values/indices.')], HRESULT, 'ClearSelectedDimensions'),
    COMMETHOD([helpstring(u'All dimensions which may be used to select values/indices.')], HRESULT, 'GetDimensions',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'ppDims' )),
]
################################################################
## code template for IMDDatasetView implementation
##class IMDDatasetView_Impl(object):
##    def GetDimensionIndex(self, dim):
##        u'The selected dimension index for a dimension name.'
##        #return pVal
##
##    def GetDimensionValue(self, dim):
##        u'The selected dimension value for a dimension name.'
##        #return pVal
##
##    def GetSelectedDimensionIndices(self):
##        u'Indices for the values of selected dimensions.'
##        #return ppIndices
##
##    def GetDimensions(self):
##        u'All dimensions which may be used to select values/indices.'
##        #return ppDims
##
##    def ClearSelectedDimensions(self):
##        u'Clears a selected list of dimensions and values/indices.'
##        #return 
##
##    def GetSelectedDimensions(self):
##        u'The selected dimension names.'
##        #return ppNames
##
##    def GetSelectedDimensionValues(self):
##        u'The selected dimension values.'
##        #return ppValues
##
##    def SelectDimensionByIndex(self, dim, index):
##        u'Selects the dimension for viewing by an index.'
##        #return 
##
##    def SelectDimensionByValue(self, dim, vValue):
##        u'Selects the dimension for viewing by a value.'
##        #return 
##

class IMDFeatureClassView(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'The Multi Dimension FeatureClassView Interface.'
    _iid_ = GUID('{F065307E-3ADF-4B57-B59D-4BA1465BB40C}')
    _idlflags_ = ['oleautomation']
IMDFeatureClassView._methods_ = [
    COMMETHOD(['propget', helpstring(u'The list of variables used.')], HRESULT, 'VariableList',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'ppVars' )),
    COMMETHOD(['propput', helpstring(u'The list of variables used.')], HRESULT, 'VariableList',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray), 'ppVars' )),
    COMMETHOD(['propget', helpstring(u'The x-dimension item used.')], HRESULT, 'XDimension',
              ( ['retval', 'out'], POINTER(BSTR), 'pXDim' )),
    COMMETHOD(['propput', helpstring(u'The x-dimension item used.')], HRESULT, 'XDimension',
              ( ['in'], BSTR, 'pXDim' )),
    COMMETHOD(['propget', helpstring(u'The y-dimension item used.')], HRESULT, 'YDimension',
              ( ['retval', 'out'], POINTER(BSTR), 'pYDim' )),
    COMMETHOD(['propput', helpstring(u'The y-dimension item used.')], HRESULT, 'YDimension',
              ( ['in'], BSTR, 'pYDim' )),
    COMMETHOD(['propget', helpstring(u'The list of row dimensions used.')], HRESULT, 'RowDimensionList',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'ppRowDims' )),
    COMMETHOD(['propput', helpstring(u'The list of row dimensions used.')], HRESULT, 'RowDimensionList',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray), 'ppRowDims' )),
    COMMETHOD(['propget', helpstring(u'The Z variable or dimension item used.')], HRESULT, 'ZItem',
              ( ['retval', 'out'], POINTER(BSTR), 'pZItem' )),
    COMMETHOD(['propput', helpstring(u'The Z variable or dimension item used.')], HRESULT, 'ZItem',
              ( ['in'], BSTR, 'pZItem' )),
    COMMETHOD(['propget', helpstring(u'The M variable or dimension item used.')], HRESULT, 'MItem',
              ( ['retval', 'out'], POINTER(BSTR), 'pMItem' )),
    COMMETHOD(['propput', helpstring(u'The M variable or dimension item used.')], HRESULT, 'MItem',
              ( ['in'], BSTR, 'pMItem' )),
]
################################################################
## code template for IMDFeatureClassView implementation
##class IMDFeatureClassView_Impl(object):
##    def _get(self):
##        u'The list of row dimensions used.'
##        #return ppRowDims
##    def _set(self, ppRowDims):
##        u'The list of row dimensions used.'
##    RowDimensionList = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The list of variables used.'
##        #return ppVars
##    def _set(self, ppVars):
##        u'The list of variables used.'
##    VariableList = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The y-dimension item used.'
##        #return pYDim
##    def _set(self, pYDim):
##        u'The y-dimension item used.'
##    YDimension = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The x-dimension item used.'
##        #return pXDim
##    def _set(self, pXDim):
##        u'The x-dimension item used.'
##    XDimension = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The Z variable or dimension item used.'
##        #return pZItem
##    def _set(self, pZItem):
##        u'The Z variable or dimension item used.'
##    ZItem = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The M variable or dimension item used.'
##        #return pMItem
##    def _set(self, pMItem):
##        u'The M variable or dimension item used.'
##    MItem = property(_get, _set, doc = _set.__doc__)
##


# values for enumeration 'esriNetCDFError'
E_NETCDF_FILE_NOT_FOUND = -2147217407
E_NETCDF_FILE_INVALID_EXTENSION = -2147217406
E_NETCDF_RENDERER_INVALID_BAND_INDEX = -2147217405
E_NETCDF_FILE_FAILED_TO_RENAME = -2147217404
E_NETCDF_FILE_FAILED_TO_COPY = -2147217403
E_NETCDF_ACCESS_IS_DENIED = -2147217402
E_NETCDF_DATASET_EXIST = -2147217401
E_NETCDF_UNKNOWN_ERROR = -2147217408
esriNetCDFError = c_int # enum
class IMDTableView(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'The Multi Dimension TableView Interface.'
    _iid_ = GUID('{6C4F3247-039E-4D7B-A815-DF16A04B9827}')
    _idlflags_ = ['oleautomation']
IMDTableView._methods_ = [
    COMMETHOD(['propget', helpstring(u'The list of variables used.')], HRESULT, 'VariableList',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'ppVars' )),
    COMMETHOD(['propput', helpstring(u'The list of variables used.')], HRESULT, 'VariableList',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray), 'ppVars' )),
    COMMETHOD(['propget', helpstring(u'The list of dimensions used.')], HRESULT, 'DimensionList',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'ppDims' )),
    COMMETHOD(['propput', helpstring(u'The list of dimensions used.')], HRESULT, 'DimensionList',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray), 'ppDims' )),
]
################################################################
## code template for IMDTableView implementation
##class IMDTableView_Impl(object):
##    def _get(self):
##        u'The list of dimensions used.'
##        #return ppDims
##    def _set(self, ppDims):
##        u'The list of dimensions used.'
##    DimensionList = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The list of variables used.'
##        #return ppVars
##    def _set(self, ppVars):
##        u'The list of variables used.'
##    VariableList = property(_get, _set, doc = _set.__doc__)
##

class INetCDFWorkspace(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control a NetCDF workspace.'
    _iid_ = GUID('{2D289EA0-E56E-44E9-BDB7-1BC829222CC3}')
    _idlflags_ = ['oleautomation']
INetCDFWorkspace._methods_ = [
    COMMETHOD([helpstring(u'The array of variable strings.')], HRESULT, 'GetVariables',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'ppOut' )),
    COMMETHOD([helpstring(u'The array of dimension items.')], HRESULT, 'GetDimensions',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'ppOut' )),
    COMMETHOD([helpstring(u'The array of global or variable specific attribute names.')], HRESULT, 'GetAttributeNames',
              ( ['in'], BSTR, 'varName' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'ppAttNames' )),
    COMMETHOD([helpstring(u'The size or length of a specified dimension.')], HRESULT, 'GetDimensionSize',
              ( ['in'], BSTR, 'dimName' ),
              ( ['retval', 'out'], POINTER(c_int), 'dimSize' )),
    COMMETHOD([helpstring(u'The dimension items for a specified variable.')], HRESULT, 'GetDimensionsByVariable',
              ( ['in'], BSTR, 'varName' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'ppOut' )),
    COMMETHOD([helpstring(u'All variables having the specified dimension name.')], HRESULT, 'GetVariablesByDimension',
              ( ['in'], BSTR, 'dimName' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'ppOut' )),
    COMMETHOD([helpstring(u'The dimension value for a specified dimension and index.')], HRESULT, 'GetDimensionValue',
              ( ['in'], BSTR, 'dimName' ),
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'vValue' )),
    COMMETHOD([helpstring(u'The dimension index for a specified dimension and value.')], HRESULT, 'GetDimensionIndex',
              ( ['in'], BSTR, 'dimName' ),
              ( ['in'], VARIANT, 'vValue' ),
              ( ['retval', 'out'], POINTER(c_int), 'index' )),
    COMMETHOD([helpstring(u'The attribute value for a specified variable and an attribute name or keyword.')], HRESULT, 'GetAttributeValue',
              ( ['in'], BSTR, 'varName' ),
              ( ['in'], BSTR, 'attName' ),
              ( ['in'], c_int, 'valueIndex' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'pValue' )),
    COMMETHOD([helpstring(u'The values for a specified dimension.')], HRESULT, 'GetDimensionValues',
              ( ['in'], BSTR, 'dimName' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IVariantArray)), 'ppValues' )),
    COMMETHOD([helpstring(u'The spatial reference for a variable.')], HRESULT, 'GetSpatialReference',
              ( ['in'], BSTR, 'varName' ),
              ( ['in'], BSTR, 'xDim' ),
              ( ['in'], BSTR, 'yDim' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference)), 'ppSpatRef' )),
    COMMETHOD([helpstring(u'The field type of a variable or dimension.')], HRESULT, 'GetFieldType',
              ( ['in'], BSTR, 'name' ),
              ( ['retval', 'out'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriFieldType), 'fieldType' )),
    COMMETHOD([helpstring(u'The dimension or variable value for a given index.')], HRESULT, 'GetValueFromIndex',
              ( ['in'], c_int, 'index' ),
              ( ['in'], BSTR, 'name' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD([helpstring(u'Return the index of a specified variable or dimension value.')], HRESULT, 'GetIndexFromValue',
              ( ['in'], BSTR, 'name' ),
              ( ['in'], VARIANT, 'value' ),
              ( ['retval', 'out'], POINTER(c_int), 'index' )),
]
################################################################
## code template for INetCDFWorkspace implementation
##class INetCDFWorkspace_Impl(object):
##    def GetSpatialReference(self, varName, xDim, yDim):
##        u'The spatial reference for a variable.'
##        #return ppSpatRef
##
##    def GetIndexFromValue(self, name, value):
##        u'Return the index of a specified variable or dimension value.'
##        #return index
##
##    def GetAttributeNames(self, varName):
##        u'The array of global or variable specific attribute names.'
##        #return ppAttNames
##
##    def GetDimensionValue(self, dimName, index):
##        u'The dimension value for a specified dimension and index.'
##        #return vValue
##
##    def GetVariables(self):
##        u'The array of variable strings.'
##        #return ppOut
##
##    def GetDimensions(self):
##        u'The array of dimension items.'
##        #return ppOut
##
##    def GetVariablesByDimension(self, dimName):
##        u'All variables having the specified dimension name.'
##        #return ppOut
##
##    def GetDimensionValues(self, dimName):
##        u'The values for a specified dimension.'
##        #return ppValues
##
##    def GetDimensionIndex(self, dimName, vValue):
##        u'The dimension index for a specified dimension and value.'
##        #return index
##
##    def GetFieldType(self, name):
##        u'The field type of a variable or dimension.'
##        #return fieldType
##
##    def GetAttributeValue(self, varName, attName, valueIndex):
##        u'The attribute value for a specified variable and an attribute name or keyword.'
##        #return pValue
##
##    def GetValueFromIndex(self, index, name):
##        u'The dimension or variable value for a given index.'
##        #return pVal
##
##    def GetDimensionSize(self, dimName):
##        u'The size or length of a specified dimension.'
##        #return dimSize
##
##    def GetDimensionsByVariable(self, varName):
##        u'The dimension items for a specified variable.'
##        #return ppOut
##

class NetCDFWorkspace(CoClass):
    u'The NetCDF workspace object.'
    _reg_clsid_ = GUID('{434116CC-611E-44BE-A194-E4594C2FC926}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{28ED84CD-FB06-41A0-9A55-E196441D169A}', 10, 2)
class IMDWorkspace(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'The Multi Dimension Workspace Interface.'
    _iid_ = GUID('{88B7B494-1C1D-4B6C-A1DB-28900AFA96EC}')
    _idlflags_ = ['oleautomation']
NetCDFWorkspace._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspace, INetCDFWorkspace, IMDWorkspace, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataset, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceProperties]

class NetCDFFeatureClassName(CoClass):
    u'A container for name information about a NetCDF feature class.'
    _reg_clsid_ = GUID('{EE5EF168-7B62-4ED5-89BB-FF73D390AF93}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{28ED84CD-FB06-41A0-9A55-E196441D169A}', 10, 2)
NetCDFFeatureClassName._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetName, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, IMDDatasetView, IMDFeatureClassView]

IMDWorkspace._methods_ = [
    COMMETHOD([helpstring(u'Creates a dataset from a view definition.')], HRESULT, 'CreateView',
              ( ['in'], BSTR, 'viewName' ),
              ( ['in'], POINTER(IMDDatasetView), 'pView' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataset)), 'ppOut' )),
]
################################################################
## code template for IMDWorkspace implementation
##class IMDWorkspace_Impl(object):
##    def CreateView(self, viewName, pView):
##        u'Creates a dataset from a view definition.'
##        #return ppOut
##

class NetCDFTableName(CoClass):
    u'A container for name information about a NetCDF table.'
    _reg_clsid_ = GUID('{2D597A23-A989-43C1-9B1B-19E75BBFB78F}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{28ED84CD-FB06-41A0-9A55-E196441D169A}', 10, 2)
NetCDFTableName._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITableName, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, IMDDatasetView, IMDTableView]

class IMDRasterDatasetView(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'The Multi Dimension RasterDatasetView Interface.'
    _iid_ = GUID('{08CEBFB9-DB3E-433B-BF80-84ADF3424FB0}')
    _idlflags_ = ['oleautomation']
IMDRasterDatasetView._methods_ = [
    COMMETHOD(['propget', helpstring(u'The x-dimension item used.')], HRESULT, 'XDimension',
              ( ['retval', 'out'], POINTER(BSTR), 'pXDim' )),
    COMMETHOD(['propput', helpstring(u'The x-dimension item used.')], HRESULT, 'XDimension',
              ( ['in'], BSTR, 'pXDim' )),
    COMMETHOD(['propget', helpstring(u'The y-dimension item used.')], HRESULT, 'YDimension',
              ( ['retval', 'out'], POINTER(BSTR), 'pYDim' )),
    COMMETHOD(['propput', helpstring(u'The y-dimension item used.')], HRESULT, 'YDimension',
              ( ['in'], BSTR, 'pYDim' )),
    COMMETHOD(['propget', helpstring(u'The band dimension item used.')], HRESULT, 'BandDimension',
              ( ['retval', 'out'], POINTER(BSTR), 'pBandDim' )),
    COMMETHOD(['propput', helpstring(u'The band dimension item used.')], HRESULT, 'BandDimension',
              ( ['in'], BSTR, 'pBandDim' )),
    COMMETHOD(['propget', helpstring(u'The variable used.')], HRESULT, 'Variable',
              ( ['retval', 'out'], POINTER(BSTR), 'pVar' )),
    COMMETHOD(['propput', helpstring(u'The variable used.')], HRESULT, 'Variable',
              ( ['in'], BSTR, 'pVar' )),
]
################################################################
## code template for IMDRasterDatasetView implementation
##class IMDRasterDatasetView_Impl(object):
##    def _get(self):
##        u'The band dimension item used.'
##        #return pBandDim
##    def _set(self, pBandDim):
##        u'The band dimension item used.'
##    BandDimension = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The variable used.'
##        #return pVar
##    def _set(self, pVar):
##        u'The variable used.'
##    Variable = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The y-dimension item used.'
##        #return pYDim
##    def _set(self, pYDim):
##        u'The y-dimension item used.'
##    YDimension = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The x-dimension item used.'
##        #return pXDim
##    def _set(self, pXDim):
##        u'The x-dimension item used.'
##    XDimension = property(_get, _set, doc = _set.__doc__)
##

class NetCDFRasterDatasetName(CoClass):
    u'A container for name information about a NetCDF raster dataset.'
    _reg_clsid_ = GUID('{8CB4AA2B-58CE-438F-8CD8-F5F0BEF41AAF}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{28ED84CD-FB06-41A0-9A55-E196441D169A}', 10, 2)
NetCDFRasterDatasetName._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetName, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRasterDatasetName, IMDDatasetView, IMDRasterDatasetView, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadataEdit, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.INativeTypeInfo, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetNameFileStat, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetNameFileSize]

class NetCDFWorkspaceFactory(CoClass):
    u'Provides access to members that control creation of NetCDF workspaces.'
    _reg_clsid_ = GUID('{DF61A9E1-B8E2-498F-BDE5-98DE42E801F9}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{28ED84CD-FB06-41A0-9A55-E196441D169A}', 10, 2)
NetCDFWorkspaceFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceFactory, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceFactory2, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

__all__ = ['IMDRasterDatasetView', 'IMDTableView', 'NetCDFTableName',
           'NetCDFWorkspaceFactory', 'E_NETCDF_UNKNOWN_ERROR',
           'E_NETCDF_FILE_FAILED_TO_COPY',
           'E_NETCDF_FILE_INVALID_EXTENSION',
           'E_NETCDF_RENDERER_INVALID_BAND_INDEX',
           'NetCDFRasterDatasetName', 'IMDWorkspace',
           'E_NETCDF_DATASET_EXIST', 'NetCDFWorkspace',
           'IMDFeatureClassView', 'INetCDFWorkspace',
           'E_NETCDF_FILE_NOT_FOUND', 'IMDDatasetView',
           'E_NETCDF_ACCESS_IS_DENIED',
           'E_NETCDF_FILE_FAILED_TO_RENAME',
           'IProtectNamesDataSourcesNetCDF', 'esriNetCDFError',
           'NetCDFFeatureClassName']
from comtypes import _check_version; _check_version('501')

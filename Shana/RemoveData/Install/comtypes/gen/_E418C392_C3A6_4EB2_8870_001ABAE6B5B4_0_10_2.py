# -*- coding: mbcs -*-
typelib_path = u'C:\\Program Files (x86)\\ArcGIS\\Desktop10.2\\com\\esriSearch.olb'
_lcid = 0 # change this if required
from ctypes import *
import comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2
from comtypes import GUID
from comtypes import CoClass
import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0
import comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2
import comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2
from comtypes import BSTR
from ctypes.wintypes import VARIANT_BOOL
from ctypes import HRESULT
from comtypes import helpstring
from comtypes import COMMETHOD
from comtypes import dispid
import comtypes.gen._18F2FC71_6B30_45B9_B101_037A8B868B66_0_10_2
import comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2
import comtypes.gen._1CE6AC65_43F5_4529_8FC0_D7ED298E4F1A_0_10_2


class SearchServerIP(CoClass):
    u'Search Server Message Proxy.'
    _reg_clsid_ = GUID('{27649117-93FF-4E04-B3EB-1C94D11C160B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E418C392-C3A6-4EB2-8870-001ABAE6B5B4}', 10, 2)
class ISearchServer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to search server object.'
    _iid_ = GUID('{1B8A0E7C-63DA-4D43-8463-DD64FF779849}')
    _idlflags_ = ['oleautomation']
SearchServerIP._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IAGSServerObject2, comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IAGSServerObject, ISearchServer, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

class SearchServerObjectDescription(CoClass):
    u'SearchServer Object Description Class.'
    _reg_clsid_ = GUID('{1B34B850-528C-4F12-A2F4-0F139EB2619C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E418C392-C3A6-4EB2-8870-001ABAE6B5B4}', 10, 2)
SearchServerObjectDescription._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IServerObjectDescription]

class IGPItemIndexer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to GP Indexer.'
    _iid_ = GUID('{289EA2B6-D185-40F7-B1E7-B2234AE1C9F6}')
    _idlflags_ = ['oleautomation']
IGPItemIndexer._methods_ = [
    COMMETHOD([helpstring(u'The Build ItemInfos..')], HRESULT, 'IndexItems',
              ( ['in'], BSTR, 'Path' ),
              ( ['in'], VARIANT_BOOL, 'ReplaceIndex' ),
              ( ['in'], VARIANT_BOOL, 'Recursive' ),
              ( ['in'], VARIANT_BOOL, 'UseStaging' ),
              ( ['in'], BSTR, 'indexPath' ),
              ( ['in'], VARIANT_BOOL, 'UseQueue' )),
    COMMETHOD([helpstring(u'Add ItemInfo to Index File.')], HRESULT, 'AddItemInfo',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IItemInfo), 'pItemInfo' ),
              ( ['in'], VARIANT_BOOL, 'ReplaceItems' ),
              ( ['in'], BSTR, 'indexPath' ),
              ( ['in'], BSTR, 'SDEConnection' ),
              ( ['in'], POINTER(BSTR), 'pGuid' )),
    COMMETHOD([helpstring(u'Delete ItemInfo from Index File.')], HRESULT, 'DeleteItemInfo',
              ( ['in'], BSTR, 'indexPath' ),
              ( ['in'], BSTR, 'pGuid' )),
    COMMETHOD([helpstring(u'Update the index.')], HRESULT, 'UpdateItemInfo',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IItemInfo), 'pItemInfo' )),
    COMMETHOD([helpstring(u'Index Item without children with passed in catalogpath.')], HRESULT, 'IndexItem',
              ( ['in'], BSTR, 'Path' )),
    COMMETHOD([helpstring(u'Update Thumbnail of a ItemInfo by passing in a catalogpath.')], HRESULT, 'UpdateThumbnailInIndex',
              ( ['in'], BSTR, 'Path' )),
    COMMETHOD(['propget', helpstring(u'Total indexed items count.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'pCount' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the ancestor of this ItemInfo has been registered to be indexed.')], HRESULT, 'IsAncestorRegistered',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IItemInfo), 'pItemInfo' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pRegistered' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the current item has been indexed.')], HRESULT, 'HasBeenIndexed',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IItemInfo), 'pItemInfo' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pIndexed' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether staging is used during index.')], HRESULT, 'UseStaging',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pUseStaging' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether staging is used during index.')], HRESULT, 'UseStaging',
              ( ['in'], VARIANT_BOOL, 'pUseStaging' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether queue is used during index.')], HRESULT, 'UseQueue',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'UseQueue' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether queue is used during index.')], HRESULT, 'UseQueue',
              ( ['in'], VARIANT_BOOL, 'UseQueue' )),
    COMMETHOD(['propget', helpstring(u'Name of the index folder.')], HRESULT, 'IndexFolder',
              ( ['retval', 'out'], POINTER(BSTR), 'pFolderName' )),
    COMMETHOD(['propput', helpstring(u'Name of the index folder.')], HRESULT, 'IndexFolder',
              ( ['in'], BSTR, 'pFolderName' )),
    COMMETHOD(['propget', helpstring(u'Name of the index.')], HRESULT, 'IndexName',
              ( ['retval', 'out'], POINTER(BSTR), 'pName' )),
    COMMETHOD(['propput', helpstring(u'Name of the index.')], HRESULT, 'IndexName',
              ( ['in'], BSTR, 'pName' )),
    COMMETHOD(['propget', helpstring(u'SDE Connection file.')], HRESULT, 'SDEConnection',
              ( ['retval', 'out'], POINTER(BSTR), 'pName' )),
    COMMETHOD(['propput', helpstring(u'SDE Connection file.')], HRESULT, 'SDEConnection',
              ( ['in'], BSTR, 'pName' )),
]
################################################################
## code template for IGPItemIndexer implementation
##class IGPItemIndexer_Impl(object):
##    @property
##    def Count(self):
##        u'Total indexed items count.'
##        #return pCount
##
##    def _get(self):
##        u'SDE Connection file.'
##        #return pName
##    def _set(self, pName):
##        u'SDE Connection file.'
##    SDEConnection = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Name of the index.'
##        #return pName
##    def _set(self, pName):
##        u'Name of the index.'
##    IndexName = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def HasBeenIndexed(self, pItemInfo):
##        u'Indicates whether the current item has been indexed.'
##        #return pIndexed
##
##    def _get(self):
##        u'Name of the index folder.'
##        #return pFolderName
##    def _set(self, pFolderName):
##        u'Name of the index folder.'
##    IndexFolder = property(_get, _set, doc = _set.__doc__)
##
##    def IndexItems(self, Path, ReplaceIndex, Recursive, UseStaging, indexPath, UseQueue):
##        u'The Build ItemInfos..'
##        #return 
##
##    def _get(self):
##        u'Indicates whether staging is used during index.'
##        #return pUseStaging
##    def _set(self, pUseStaging):
##        u'Indicates whether staging is used during index.'
##    UseStaging = property(_get, _set, doc = _set.__doc__)
##
##    def IndexItem(self, Path):
##        u'Index Item without children with passed in catalogpath.'
##        #return 
##
##    def UpdateThumbnailInIndex(self, Path):
##        u'Update Thumbnail of a ItemInfo by passing in a catalogpath.'
##        #return 
##
##    def AddItemInfo(self, pItemInfo, ReplaceItems, indexPath, SDEConnection, pGuid):
##        u'Add ItemInfo to Index File.'
##        #return 
##
##    def _get(self):
##        u'Indicates whether queue is used during index.'
##        #return UseQueue
##    def _set(self, UseQueue):
##        u'Indicates whether queue is used during index.'
##    UseQueue = property(_get, _set, doc = _set.__doc__)
##
##    def UpdateItemInfo(self, pItemInfo):
##        u'Update the index.'
##        #return 
##
##    @property
##    def IsAncestorRegistered(self, pItemInfo):
##        u'Indicates whether the ancestor of this ItemInfo has been registered to be indexed.'
##        #return pRegistered
##
##    def DeleteItemInfo(self, indexPath, pGuid):
##        u'Delete ItemInfo from Index File.'
##        #return 
##

class IItemIndexAdmin(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members to administrate indexing process.'
    _iid_ = GUID('{CB225681-C42D-4A5F-B26E-F4A790CEF7A7}')
    _idlflags_ = ['oleautomation']
IItemIndexAdmin._methods_ = [
    COMMETHOD(['propget', helpstring(u'Name of the index folder.')], HRESULT, 'IndexFolder',
              ( ['retval', 'out'], POINTER(BSTR), 'pFolderName' )),
    COMMETHOD(['propput', helpstring(u'Name of the index folder.')], HRESULT, 'IndexFolder',
              ( ['in'], BSTR, 'pFolderName' )),
    COMMETHOD(['propget', helpstring(u'Name of the index.')], HRESULT, 'IndexName',
              ( ['retval', 'out'], POINTER(BSTR), 'pName' )),
    COMMETHOD(['propput', helpstring(u'Name of the index.')], HRESULT, 'IndexName',
              ( ['in'], BSTR, 'pName' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether to use staging during index.')], HRESULT, 'UseStaging',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pUseStaging' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether to use staging during index.')], HRESULT, 'UseStaging',
              ( ['in'], VARIANT_BOOL, 'pUseStaging' )),
    COMMETHOD([helpstring(u'Prepare and start indexing.')], HRESULT, 'StartIndexing',
              ( ['in'], VARIANT_BOOL, 'ReplaceIndex' ),
              ( ['in'], VARIANT_BOOL, 'ReplaceItems' )),
    COMMETHOD([helpstring(u'Close and end indexing.')], HRESULT, 'EndIndexing'),
]
################################################################
## code template for IItemIndexAdmin implementation
##class IItemIndexAdmin_Impl(object):
##    def EndIndexing(self):
##        u'Close and end indexing.'
##        #return 
##
##    def _get(self):
##        u'Indicates whether to use staging during index.'
##        #return pUseStaging
##    def _set(self, pUseStaging):
##        u'Indicates whether to use staging during index.'
##    UseStaging = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Name of the index folder.'
##        #return pFolderName
##    def _set(self, pFolderName):
##        u'Name of the index folder.'
##    IndexFolder = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Name of the index.'
##        #return pName
##    def _set(self, pName):
##        u'Name of the index.'
##    IndexName = property(_get, _set, doc = _set.__doc__)
##
##    def StartIndexing(self, ReplaceIndex, ReplaceItems):
##        u'Prepare and start indexing.'
##        #return 
##

class SearchServerConfigurationFactory(CoClass):
    u'SearchServer Configuration Factory Class.'
    _reg_clsid_ = GUID('{34DAF65A-3A86-4A76-B7CD-7614906626C5}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E418C392-C3A6-4EB2-8870-001ABAE6B5B4}', 10, 2)
SearchServerConfigurationFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._18F2FC71_6B30_45B9_B101_037A8B868B66_0_10_2.IConfigurationFactory, comtypes.gen._18F2FC71_6B30_45B9_B101_037A8B868B66_0_10_2.IConfigurationFactory2, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

class IIndexingConfiguration(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the IndexingConfiguration Interface.'
    _iid_ = GUID('{804C00D1-DCD8-4C7A-8F95-0AF743E22EE0}')
    _idlflags_ = ['oleautomation']
IIndexingConfiguration._methods_ = [
    COMMETHOD(['propget', helpstring(u'The target paths to be indexed.')], HRESULT, 'Paths',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'ppPaths' )),
    COMMETHOD(['propput', helpstring(u'The target paths to be indexed.')], HRESULT, 'Paths',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray), 'ppPaths' )),
    COMMETHOD(['propget', helpstring(u'File extensions to be filtered out.')], HRESULT, 'Filter',
              ( ['retval', 'out'], POINTER(BSTR), 'pFilter' )),
    COMMETHOD(['propput', helpstring(u'File extensions to be filtered out.')], HRESULT, 'Filter',
              ( ['in'], BSTR, 'pFilter' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether to recursively get the children of target path.')], HRESULT, 'Recursive',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pRecursive' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether to recursively get the children of target path.')], HRESULT, 'Recursive',
              ( ['in'], VARIANT_BOOL, 'pRecursive' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether to replace existing index.')], HRESULT, 'ReplaceIndex',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pReplaceIndex' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether to replace existing index.')], HRESULT, 'ReplaceIndex',
              ( ['in'], VARIANT_BOOL, 'pReplaceIndex' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether to replace existing items.')], HRESULT, 'ReplaceItems',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pReplaceItems' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether to replace existing items.')], HRESULT, 'ReplaceItems',
              ( ['in'], VARIANT_BOOL, 'pReplaceItems' )),
    COMMETHOD(['propget', helpstring(u'Incremental index interval.')], HRESULT, 'IncrementalIndexInterval',
              ( ['retval', 'out'], POINTER(c_int), 'pInterval' )),
    COMMETHOD(['propput', helpstring(u'Incremental index interval.')], HRESULT, 'IncrementalIndexInterval',
              ( ['in'], c_int, 'pInterval' )),
    COMMETHOD(['propget', helpstring(u'Full index interval.')], HRESULT, 'FullIndexInterval',
              ( ['retval', 'out'], POINTER(c_int), 'pInterval' )),
    COMMETHOD(['propput', helpstring(u'Full index interval.')], HRESULT, 'FullIndexInterval',
              ( ['in'], c_int, 'pInterval' )),
    COMMETHOD(['propget', helpstring(u'Index start time.')], HRESULT, 'StartTime',
              ( ['retval', 'out'], POINTER(BSTR), 'StartTime' )),
    COMMETHOD(['propput', helpstring(u'Index start time.')], HRESULT, 'StartTime',
              ( ['in'], BSTR, 'StartTime' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether to skip connection files (sde, ags, wcs, wms, etc) copied to non-default locations.')], HRESULT, 'SkipConnections',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pSkip' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether to skip connection files (sde, ags, wcs, wms, etc) copied to non-default locations.')], HRESULT, 'SkipConnections',
              ( ['in'], VARIANT_BOOL, 'pSkip' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether to pause indexing until instructed to resume.')], HRESULT, 'IsPaused',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pPaused' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether to pause indexing until instructed to resume.')], HRESULT, 'IsPaused',
              ( ['in'], VARIANT_BOOL, 'pPaused' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the indexer was running when it was paused.')], HRESULT, 'WasRunning',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pRunning' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether the indexer was running when it was paused.')], HRESULT, 'WasRunning',
              ( ['in'], VARIANT_BOOL, 'pRunning' )),
]
################################################################
## code template for IIndexingConfiguration implementation
##class IIndexingConfiguration_Impl(object):
##    def _get(self):
##        u'Indicates whether to replace existing index.'
##        #return pReplaceIndex
##    def _set(self, pReplaceIndex):
##        u'Indicates whether to replace existing index.'
##    ReplaceIndex = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The target paths to be indexed.'
##        #return ppPaths
##    def _set(self, ppPaths):
##        u'The target paths to be indexed.'
##    Paths = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether to recursively get the children of target path.'
##        #return pRecursive
##    def _set(self, pRecursive):
##        u'Indicates whether to recursively get the children of target path.'
##    Recursive = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether the indexer was running when it was paused.'
##        #return pRunning
##    def _set(self, pRunning):
##        u'Indicates whether the indexer was running when it was paused.'
##    WasRunning = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Full index interval.'
##        #return pInterval
##    def _set(self, pInterval):
##        u'Full index interval.'
##    FullIndexInterval = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether to replace existing items.'
##        #return pReplaceItems
##    def _set(self, pReplaceItems):
##        u'Indicates whether to replace existing items.'
##    ReplaceItems = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Incremental index interval.'
##        #return pInterval
##    def _set(self, pInterval):
##        u'Incremental index interval.'
##    IncrementalIndexInterval = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'File extensions to be filtered out.'
##        #return pFilter
##    def _set(self, pFilter):
##        u'File extensions to be filtered out.'
##    Filter = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether to skip connection files (sde, ags, wcs, wms, etc) copied to non-default locations.'
##        #return pSkip
##    def _set(self, pSkip):
##        u'Indicates whether to skip connection files (sde, ags, wcs, wms, etc) copied to non-default locations.'
##    SkipConnections = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Index start time.'
##        #return StartTime
##    def _set(self, StartTime):
##        u'Index start time.'
##    StartTime = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether to pause indexing until instructed to resume.'
##        #return pPaused
##    def _set(self, pPaused):
##        u'Indicates whether to pause indexing until instructed to resume.'
##    IsPaused = property(_get, _set, doc = _set.__doc__)
##

class Library(object):
    u'Esri Search Object Library 10.2'
    name = u'esriSearch'
    _reg_typelib_ = ('{E418C392-C3A6-4EB2-8870-001ABAE6B5B4}', 10, 2)

class IIndexingConfiguration2(IIndexingConfiguration):
    _case_insensitive_ = True
    u'Provides access to the IndexingConfiguration Interface.'
    _iid_ = GUID('{800FEC88-4FED-40A5-9798-9BE7BF73E051}')
    _idlflags_ = ['oleautomation']
class IIndexingConfiguration3(IIndexingConfiguration2):
    _case_insensitive_ = True
    u'Provides access to the IndexingConfiguration Interface.'
    _iid_ = GUID('{56E962F0-2A97-4189-B69F-CBBBB7694D2C}')
    _idlflags_ = ['oleautomation']
IIndexingConfiguration2._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates whether to generate thumbnails after indexing.')], HRESULT, 'GenerateThumbnails',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'GenerateThumbnails' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether to generate thumbnails after indexing.')], HRESULT, 'GenerateThumbnails',
              ( ['in'], VARIANT_BOOL, 'GenerateThumbnails' )),
    COMMETHOD([helpstring(u'Loads current index configuration settings.')], HRESULT, 'LoadConfigFile'),
    COMMETHOD([helpstring(u'Deletes existing index configuration file and creates a new one with default settings.')], HRESULT, 'ResetConfigFile'),
]
################################################################
## code template for IIndexingConfiguration2 implementation
##class IIndexingConfiguration2_Impl(object):
##    def LoadConfigFile(self):
##        u'Loads current index configuration settings.'
##        #return 
##
##    def _get(self):
##        u'Indicates whether to generate thumbnails after indexing.'
##        #return GenerateThumbnails
##    def _set(self, GenerateThumbnails):
##        u'Indicates whether to generate thumbnails after indexing.'
##    GenerateThumbnails = property(_get, _set, doc = _set.__doc__)
##
##    def ResetConfigFile(self):
##        u'Deletes existing index configuration file and creates a new one with default settings.'
##        #return 
##

IIndexingConfiguration3._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates whether to skip mosaic dataset items when indexing.')], HRESULT, 'SkipMosaicItems',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pSkipMosaicItems' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether to skip mosaic dataset items when indexing.')], HRESULT, 'SkipMosaicItems',
              ( ['in'], VARIANT_BOOL, 'pSkipMosaicItems' )),
    COMMETHOD(['propget', helpstring(u'The number of indexing threads.')], HRESULT, 'ThreadCount',
              ( ['retval', 'out'], POINTER(c_int), 'pCount' )),
    COMMETHOD(['propput', helpstring(u'The number of indexing threads.')], HRESULT, 'ThreadCount',
              ( ['in'], c_int, 'pCount' )),
]
################################################################
## code template for IIndexingConfiguration3 implementation
##class IIndexingConfiguration3_Impl(object):
##    def _get(self):
##        u'Indicates whether to skip mosaic dataset items when indexing.'
##        #return pSkipMosaicItems
##    def _set(self, pSkipMosaicItems):
##        u'Indicates whether to skip mosaic dataset items when indexing.'
##    SkipMosaicItems = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The number of indexing threads.'
##        #return pCount
##    def _set(self, pCount):
##        u'The number of indexing threads.'
##    ThreadCount = property(_get, _set, doc = _set.__doc__)
##

class IProtectNameSearch(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to dummy methods protecting name correctness.'
    _iid_ = GUID('{4F37BE4D-3CC6-421D-BDE9-F73D48FF5CB9}')
    _idlflags_ = []
IProtectNameSearch._methods_ = [
    COMMETHOD([], HRESULT, 'ProtectOLE_HANDLE',
              ( [], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_HANDLE, 'aHandle' )),
    COMMETHOD([], HRESULT, 'ProtectOLE_COLOR',
              ( [], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.OLE_COLOR, 'aColor' )),
]
################################################################
## code template for IProtectNameSearch implementation
##class IProtectNameSearch_Impl(object):
##    def ProtectOLE_COLOR(self, aColor):
##        '-no docstring-'
##        #return 
##
##    def ProtectOLE_HANDLE(self, aHandle):
##        '-no docstring-'
##        #return 
##

class IGPItemIndexer2(IGPItemIndexer):
    _case_insensitive_ = True
    u'Provides access to GP Indexer.'
    _iid_ = GUID('{E76ACE8C-074C-4B5C-84B1-04ED7C5B2A7C}')
    _idlflags_ = ['oleautomation']
class IItemIndex(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to helper functions for indexing.'
    _iid_ = GUID('{ACF9354C-05DB-4A70-B5F3-48D2822CB400}')
    _idlflags_ = ['oleautomation']
IGPItemIndexer2._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates whether to skip connection files (sde, ags, wcs, wms, etc) copied to non-default locations.')], HRESULT, 'SkipConnections',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pSkipConnections' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether to skip connection files (sde, ags, wcs, wms, etc) copied to non-default locations.')], HRESULT, 'SkipConnections',
              ( ['in'], VARIANT_BOOL, 'pSkipConnections' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether to skip mosaic dataset items when indexing.')], HRESULT, 'SkipMosaicItems',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pSkipMosaicItems' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether to skip mosaic dataset items when indexing.')], HRESULT, 'SkipMosaicItems',
              ( ['in'], VARIANT_BOOL, 'pSkipMosaicItems' )),
    COMMETHOD(['propget', helpstring(u'The native item index.')], HRESULT, 'ItemIndex',
              ( ['retval', 'out'], POINTER(POINTER(IItemIndex)), 'ppItemIndex' )),
]
################################################################
## code template for IGPItemIndexer2 implementation
##class IGPItemIndexer2_Impl(object):
##    def _get(self):
##        u'Indicates whether to skip connection files (sde, ags, wcs, wms, etc) copied to non-default locations.'
##        #return pSkipConnections
##    def _set(self, pSkipConnections):
##        u'Indicates whether to skip connection files (sde, ags, wcs, wms, etc) copied to non-default locations.'
##    SkipConnections = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether to skip mosaic dataset items when indexing.'
##        #return pSkipMosaicItems
##    def _set(self, pSkipMosaicItems):
##        u'Indicates whether to skip mosaic dataset items when indexing.'
##    SkipMosaicItems = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def ItemIndex(self):
##        u'The native item index.'
##        #return ppItemIndex
##

class DataSourceConfiguration(CoClass):
    u'DataSource Configuration object.'
    _reg_clsid_ = GUID('{5D6268D0-9E95-4A1D-9F1E-E943B47E2588}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E418C392-C3A6-4EB2-8870-001ABAE6B5B4}', 10, 2)
class IDataSourceConfiguration(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to data source configuration.'
    _iid_ = GUID('{CC8F1331-2BF5-4CAD-B30C-FFCB95EB96B0}')
    _idlflags_ = ['oleautomation']
DataSourceConfiguration._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDataSourceConfiguration, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist]

IItemIndex._methods_ = [
    COMMETHOD([helpstring(u'Add item info to index.')], HRESULT, 'AddItemInfo',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IItemInfo), 'pItemInfo' )),
    COMMETHOD([helpstring(u'Delete item info from index.')], HRESULT, 'DeleteItemInfo',
              ( ['in'], BSTR, 'catalogPath' )),
    COMMETHOD([helpstring(u'Delete item infos from index.')], HRESULT, 'DeleteItemInfos',
              ( ['in'], BSTR, 'catalogPath' )),
    COMMETHOD([helpstring(u'Update the specified item info in index.')], HRESULT, 'UpdateItemInfo',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IItemInfo), 'pItemInfo' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether to check a particular iteminfo exists or not.')], HRESULT, 'ItemInfoExists',
              ( ['in'], BSTR, 'catalogPath' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbExsits' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether to check index exists or not.')], HRESULT, 'ItemInfoCount',
              ( ['retval', 'out'], POINTER(c_int), 'pCount' )),
]
################################################################
## code template for IItemIndex implementation
##class IItemIndex_Impl(object):
##    def AddItemInfo(self, pItemInfo):
##        u'Add item info to index.'
##        #return 
##
##    def DeleteItemInfos(self, catalogPath):
##        u'Delete item infos from index.'
##        #return 
##
##    @property
##    def ItemInfoCount(self):
##        u'Indicates whether to check index exists or not.'
##        #return pCount
##
##    @property
##    def ItemInfoExists(self, catalogPath):
##        u'Indicates whether to check a particular iteminfo exists or not.'
##        #return pbExsits
##
##    def UpdateItemInfo(self, pItemInfo):
##        u'Update the specified item info in index.'
##        #return 
##
##    def DeleteItemInfo(self, catalogPath):
##        u'Delete item info from index.'
##        #return 
##

class IDSCStatusArray(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to Array of DSCStatus.'
    _iid_ = GUID('{855C8D89-4AD8-403D-A78D-FB62A19A2BE9}')
    _idlflags_ = ['oleautomation']
class IDSCStatus(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to SDCStatus object.'
    _iid_ = GUID('{1B933540-819B-492B-9A0B-498ED4307E8C}')
    _idlflags_ = ['oleautomation']
IDSCStatusArray._methods_ = [
    COMMETHOD(['propget', helpstring(u'DSCStatus Object count.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'The DSCStatus Object at the specified position.')], HRESULT, 'Element',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IDSCStatus)), 'dataObject' )),
    COMMETHOD([helpstring(u'Removes the DSCStatus Object at the specified position.')], HRESULT, 'Remove',
              ( ['in'], c_int, 'index' )),
    COMMETHOD([helpstring(u'Removes all DSCStatus Objects.')], HRESULT, 'RemoveAll'),
    COMMETHOD([helpstring(u'Adds a DSCStatus.')], HRESULT, 'Add',
              ( ['in'], POINTER(IDSCStatus), 'pDSCStatus' )),
    COMMETHOD([helpstring(u'Adds a DSCStatus Object at the specified position.')], HRESULT, 'Insert',
              ( ['in'], c_int, 'index' ),
              ( ['in'], POINTER(IDSCStatus), 'DSCStatus' )),
]
################################################################
## code template for IDSCStatusArray implementation
##class IDSCStatusArray_Impl(object):
##    @property
##    def Count(self):
##        u'DSCStatus Object count.'
##        #return Count
##
##    def Insert(self, index, DSCStatus):
##        u'Adds a DSCStatus Object at the specified position.'
##        #return 
##
##    def Remove(self, index):
##        u'Removes the DSCStatus Object at the specified position.'
##        #return 
##
##    @property
##    def Element(self, index):
##        u'The DSCStatus Object at the specified position.'
##        #return dataObject
##
##    def RemoveAll(self):
##        u'Removes all DSCStatus Objects.'
##        #return 
##
##    def Add(self, pDSCStatus):
##        u'Adds a DSCStatus.'
##        #return 
##

class IndexingStatus(CoClass):
    u'Indexing Status object.'
    _reg_clsid_ = GUID('{9FEC3A52-230C-4337-AAF4-24AC06FC6E30}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E418C392-C3A6-4EB2-8870-001ABAE6B5B4}', 10, 2)
class IIndexingStatus(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to indexing status.'
    _iid_ = GUID('{3AED1CD7-B3E8-446B-81B3-F35C466994DB}')
    _idlflags_ = ['oleautomation']
IndexingStatus._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IIndexingStatus, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist]

class SearchConfiguration(CoClass):
    u'Provides access to members of SearchConfiguration.'
    _reg_clsid_ = GUID('{0B7BF27E-0AFF-4C1B-B695-FB3EE0EA51CD}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E418C392-C3A6-4EB2-8870-001ABAE6B5B4}', 10, 2)
class ISearchConfiguration(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the search configuration object.'
    _iid_ = GUID('{EE2DF519-39A5-48F6-AB24-BE147EBDD4BD}')
    _idlflags_ = ['oleautomation']
SearchConfiguration._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ISearchConfiguration]

class IGPItemInfoHelper(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to helper functions for item info.'
    _iid_ = GUID('{AF93FAAE-E112-4CD3-BB3F-1B0690FC7D57}')
    _idlflags_ = ['oleautomation']
IGPItemInfoHelper._methods_ = [
    COMMETHOD(['propget', helpstring(u'Provides access to ItemInfo Helper object. User can get item info from it.')], HRESULT, 'ItemInfoByDataElement',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElement), 'pDE' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IItemInfo)), 'ppItemInfo' )),
    COMMETHOD(['propget', helpstring(u'Create item info from Data Element and Geometry Types.')], HRESULT, 'ItemInfoByDataElement2',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElement), 'pDE' ),
              ( ['in'], comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.esriGeometryType, 'geoType' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IItemInfo)), 'ppItemInfo' )),
    COMMETHOD(['propget', helpstring(u'Create item info from Dataset.')], HRESULT, 'ItemInfoByDataset',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataset), 'pDataset' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IItemInfo)), 'ppItemInfo' )),
    COMMETHOD(['propget', helpstring(u'Create item info from DatesetName.')], HRESULT, 'ItemInfoByDatasetName',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetName), 'pDatasetName' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IItemInfo)), 'ppItemInfo' )),
    COMMETHOD(['propget', helpstring(u'Create item info from Catalog path.')], HRESULT, 'ItemInfoByCatalogPathAndType',
              ( ['in'], BSTR, 'catalogPath' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDataType), 'pDataType' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IItemInfo)), 'ppItemInfo' )),
    COMMETHOD(['propget', helpstring(u'Create item infos from a catalog path.')], HRESULT, 'ItemInfoByCatalogPath',
              ( ['in'], BSTR, 'catalogPath' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IItemInfos)), 'ppItemInfos' )),
    COMMETHOD(['propget', helpstring(u'Create item infos from layer.')], HRESULT, 'ItemInfoByGPLayer',
              ( ['in'], POINTER(comtypes.gen._1CE6AC65_43F5_4529_8FC0_D7ED298E4F1A_0_10_2.IGPLayer), 'pGPLayer' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IItemInfo)), 'ppItemInfo' )),
    COMMETHOD([helpstring(u'Update the item info of the specified object.')], HRESULT, 'UpdateItemInfoByMetadata',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata), 'pMetadata' ),
              ( ['in', 'out'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IItemInfo), 'pItemInfo' )),
    COMMETHOD([helpstring(u'Update the item info of the specified object.')], HRESULT, 'UpdateItemInfoByDataElement',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElement), 'pDE' ),
              ( ['in', 'out'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IItemInfo), 'pItemInfo' )),
    COMMETHOD([helpstring(u'Update the item info of the specified object.')], HRESULT, 'UpdateItemInfoByDataset',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataset), 'pDataset' ),
              ( ['in', 'out'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IItemInfo), 'pItemInfo' )),
    COMMETHOD([helpstring(u'Update the item info of the specified object.')], HRESULT, 'UpdateItemInfoByDatasetName',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDatasetName), 'pDatasetName' ),
              ( ['in', 'out'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IItemInfo), 'pItemInfo' )),
    COMMETHOD([helpstring(u'Update the item info of the specified object.')], HRESULT, 'UpdateItemInfoByCatalogPathAndType',
              ( ['in'], BSTR, 'catalogPath' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPDataType), 'pDataType' ),
              ( ['in', 'out'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IItemInfo), 'pItemInfo' )),
    COMMETHOD([helpstring(u'Update the item info of the specified object.')], HRESULT, 'UpdateItemInfoByGPLayer',
              ( ['in'], POINTER(comtypes.gen._1CE6AC65_43F5_4529_8FC0_D7ED298E4F1A_0_10_2.IGPLayer), 'pGPLayer' ),
              ( ['in', 'out'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IItemInfo), 'pItemInfo' )),
    COMMETHOD([helpstring(u'Extract user defined Item Info from metadata.')], HRESULT, 'ExtractItemInfoFromMetadata',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IMetadata), 'pMetadata' ),
              ( ['in', 'out'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IItemInfo), 'pItemInfo' )),
    COMMETHOD([helpstring(u'Converts the coordinates of the item info extent to WGS84.')], HRESULT, 'ConvertExtentToWGS84',
              ( ['in', 'out'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IItemInfo), 'pItemInfo' )),
]
################################################################
## code template for IGPItemInfoHelper implementation
##class IGPItemInfoHelper_Impl(object):
##    def UpdateItemInfoByDataset(self, pDataset):
##        u'Update the item info of the specified object.'
##        #return pItemInfo
##
##    def ExtractItemInfoFromMetadata(self, pMetadata):
##        u'Extract user defined Item Info from metadata.'
##        #return pItemInfo
##
##    @property
##    def ItemInfoByCatalogPathAndType(self, catalogPath, pDataType):
##        u'Create item info from Catalog path.'
##        #return ppItemInfo
##
##    @property
##    def ItemInfoByDatasetName(self, pDatasetName):
##        u'Create item info from DatesetName.'
##        #return ppItemInfo
##
##    def UpdateItemInfoByDataElement(self, pDE):
##        u'Update the item info of the specified object.'
##        #return pItemInfo
##
##    @property
##    def ItemInfoByCatalogPath(self, catalogPath):
##        u'Create item infos from a catalog path.'
##        #return ppItemInfos
##
##    def ConvertExtentToWGS84(self):
##        u'Converts the coordinates of the item info extent to WGS84.'
##        #return pItemInfo
##
##    def UpdateItemInfoByGPLayer(self, pGPLayer):
##        u'Update the item info of the specified object.'
##        #return pItemInfo
##
##    def UpdateItemInfoByDatasetName(self, pDatasetName):
##        u'Update the item info of the specified object.'
##        #return pItemInfo
##
##    @property
##    def ItemInfoByGPLayer(self, pGPLayer):
##        u'Create item infos from layer.'
##        #return ppItemInfo
##
##    def UpdateItemInfoByCatalogPathAndType(self, catalogPath, pDataType):
##        u'Update the item info of the specified object.'
##        #return pItemInfo
##
##    @property
##    def ItemInfoByDataElement2(self, pDE, geoType):
##        u'Create item info from Data Element and Geometry Types.'
##        #return ppItemInfo
##
##    @property
##    def ItemInfoByDataset(self, pDataset):
##        u'Create item info from Dataset.'
##        #return ppItemInfo
##
##    def UpdateItemInfoByMetadata(self, pMetadata):
##        u'Update the item info of the specified object.'
##        #return pItemInfo
##
##    @property
##    def ItemInfoByDataElement(self, pDE):
##        u'Provides access to ItemInfo Helper object. User can get item info from it.'
##        #return ppItemInfo
##

class SearchServerLP(CoClass):
    u'Map Server LAN Proxy.'
    _reg_clsid_ = GUID('{E6BCDBC4-EFBF-46E3-9F13-E5B9BBFCD99D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E418C392-C3A6-4EB2-8870-001ABAE6B5B4}', 10, 2)
SearchServerLP._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IAGSServerObject2, comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IAGSServerObject, ISearchServer, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

class DSCStatusArray(CoClass):
    u'Data source status Array.'
    _reg_clsid_ = GUID('{980AA1E3-11BF-45AF-BE11-5A69FA2ABE5F}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E418C392-C3A6-4EB2-8870-001ABAE6B5B4}', 10, 2)
DSCStatusArray._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDSCStatusArray, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLVersionSupport, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist]

class ItemIndex(CoClass):
    u'Provides access to the ItemIndex object.'
    _reg_clsid_ = GUID('{9866E6C3-41EA-4AFE-9921-AF94435817CB}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E418C392-C3A6-4EB2-8870-001ABAE6B5B4}', 10, 2)
class IItemIndex2(IItemIndex):
    _case_insensitive_ = True
    u'Provides access to update thumbnail in index.'
    _iid_ = GUID('{FCAF5F49-FDA4-4DD6-87E9-743E139DBBCB}')
    _idlflags_ = ['oleautomation']
class IItemIndex3(IItemIndex2):
    _case_insensitive_ = True
    u'Provides access to members for merging index.'
    _iid_ = GUID('{2A2148D1-4653-4658-B4D6-A50BF3B7EA78}')
    _idlflags_ = ['oleautomation']
ItemIndex._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IItemIndex, IItemIndex2, IItemIndex3, IItemIndexAdmin]

class IIndexingOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to indexing options object.'
    _iid_ = GUID('{1F12DC45-A7A1-4504-AC1B-6E52DD5B12F9}')
    _idlflags_ = ['oleautomation']
ISearchServer._methods_ = [
    COMMETHOD([helpstring(u'Register data source to index.')], HRESULT, 'RegisterDataSource',
              ( ['in'], POINTER(IDataSourceConfiguration), 'DataSourceConfiguration' )),
    COMMETHOD([helpstring(u'Unregister Data Source.')], HRESULT, 'UnregisterDataSource',
              ( ['in'], BSTR, 'Path' )),
    COMMETHOD([helpstring(u'The list of dataSource path.')], HRESULT, 'GetDataSourceList',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'ppDataSourceList' )),
    COMMETHOD([helpstring(u'The indexing options.')], HRESULT, 'GetIndexingOptions',
              ( ['retval', 'out'], POINTER(POINTER(IIndexingOptions)), 'ppIndexingOptions' )),
    COMMETHOD([helpstring(u'The indexing options.')], HRESULT, 'SetIndexingOptions',
              ( ['in'], POINTER(IIndexingOptions), 'pIndexingOptions' )),
    COMMETHOD([helpstring(u'The indexing status.')], HRESULT, 'GetIndexingStatus',
              ( ['retval', 'out'], POINTER(POINTER(IIndexingStatus)), 'ppIndexingStatus' )),
]
################################################################
## code template for ISearchServer implementation
##class ISearchServer_Impl(object):
##    def SetIndexingOptions(self, pIndexingOptions):
##        u'The indexing options.'
##        #return 
##
##    def GetIndexingStatus(self):
##        u'The indexing status.'
##        #return ppIndexingStatus
##
##    def UnregisterDataSource(self, Path):
##        u'Unregister Data Source.'
##        #return 
##
##    def RegisterDataSource(self, DataSourceConfiguration):
##        u'Register data source to index.'
##        #return 
##
##    def GetIndexingOptions(self):
##        u'The indexing options.'
##        #return ppIndexingOptions
##
##    def GetDataSourceList(self):
##        u'The list of dataSource path.'
##        #return ppDataSourceList
##

ISearchConfiguration._methods_ = [
    COMMETHOD([helpstring(u'Load configuration settings from the specificed location.')], HRESULT, 'LoadFromFile',
              ( ['in'], BSTR, 'Path' )),
    COMMETHOD([helpstring(u'Save configuration settings to the specificed location.')], HRESULT, 'SaveToFile',
              ( ['in'], BSTR, 'Path' )),
    COMMETHOD(['propget', helpstring(u'The count of search services.')], HRESULT, 'ServicesCount',
              ( ['retval', 'out'], POINTER(c_int), 'pCount' )),
    COMMETHOD(['propget', helpstring(u'The search service object name at the specified index.')], HRESULT, 'ServiceName',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IAGSServerObjectName)), 'ppSON' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether a service is selected.')], HRESULT, 'IsServiceSelected',
              ( ['in'], POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IAGSServerObjectName), 'pSON' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bSelected' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether a service is selected.')], HRESULT, 'IsServiceSelected',
              ( ['in'], POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IAGSServerObjectName), 'pSON' ),
              ( ['in'], VARIANT_BOOL, 'bSelected' )),
    COMMETHOD([helpstring(u'Add search service name.')], HRESULT, 'AddServiceName',
              ( ['in'], POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IAGSServerObjectName), 'pSON' )),
    COMMETHOD([helpstring(u'Delete search service name.')], HRESULT, 'DeleteServiceName',
              ( ['in'], POINTER(comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IAGSServerObjectName), 'pSON' )),
    COMMETHOD([helpstring(u'Reset to default value and clean service names array.')], HRESULT, 'Empty'),
    COMMETHOD(['propget', helpstring(u'The maximum number of search result per page.')], HRESULT, 'MaxResultsPerPage',
              ( ['retval', 'out'], POINTER(c_int), 'pCount' )),
    COMMETHOD(['propput', helpstring(u'The maximum number of search result per page.')], HRESULT, 'MaxResultsPerPage',
              ( ['in'], c_int, 'pCount' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether to show pop-up in search result page.')], HRESULT, 'ShowPopup',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pShow' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether to show pop-up in search result page.')], HRESULT, 'ShowPopup',
              ( ['in'], VARIANT_BOOL, 'pShow' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether to zoom to the select text based spatial search location.')], HRESULT, 'ZoomToSelectedLocation',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pZoomToSelectedLocation' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether to zoom to the select text based spatial search location.')], HRESULT, 'ZoomToSelectedLocation',
              ( ['in'], VARIANT_BOOL, 'pZoomToSelectedLocation' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether to use the built in WordNet synonyms.')], HRESULT, 'CheckSynonymsWordNet',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pCheckSynonymsWordNet' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether to use the built in WordNet synonyms.')], HRESULT, 'CheckSynonymsWordNet',
              ( ['in'], VARIANT_BOOL, 'pCheckSynonymsWordNet' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether to use custom synonyms.')], HRESULT, 'CheckSynonymsUserDefined',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pCheckSynonymsUserDefined' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether to use custom synonyms.')], HRESULT, 'CheckSynonymsUserDefined',
              ( ['in'], VARIANT_BOOL, 'pCheckSynonymsUserDefined' )),
    COMMETHOD([helpstring(u'Resets the default values of the search options page.')], HRESULT, 'EmptySearchOptions'),
    COMMETHOD([helpstring(u'Resets the default values of the advanced options page and cleans the array of service names.')], HRESULT, 'EmptyAdvancedOptions'),
]
################################################################
## code template for ISearchConfiguration implementation
##class ISearchConfiguration_Impl(object):
##    def _get(self):
##        u'Indicates whether to use custom synonyms.'
##        #return pCheckSynonymsUserDefined
##    def _set(self, pCheckSynonymsUserDefined):
##        u'Indicates whether to use custom synonyms.'
##    CheckSynonymsUserDefined = property(_get, _set, doc = _set.__doc__)
##
##    def SaveToFile(self, Path):
##        u'Save configuration settings to the specificed location.'
##        #return 
##
##    def _get(self):
##        u'Indicates whether to use the built in WordNet synonyms.'
##        #return pCheckSynonymsWordNet
##    def _set(self, pCheckSynonymsWordNet):
##        u'Indicates whether to use the built in WordNet synonyms.'
##    CheckSynonymsWordNet = property(_get, _set, doc = _set.__doc__)
##
##    def AddServiceName(self, pSON):
##        u'Add search service name.'
##        #return 
##
##    def LoadFromFile(self, Path):
##        u'Load configuration settings from the specificed location.'
##        #return 
##
##    def EmptyAdvancedOptions(self):
##        u'Resets the default values of the advanced options page and cleans the array of service names.'
##        #return 
##
##    def _get(self):
##        u'Indicates whether to zoom to the select text based spatial search location.'
##        #return pZoomToSelectedLocation
##    def _set(self, pZoomToSelectedLocation):
##        u'Indicates whether to zoom to the select text based spatial search location.'
##    ZoomToSelectedLocation = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self, pSON):
##        u'Indicates whether a service is selected.'
##        #return bSelected
##    def _set(self, pSON, bSelected):
##        u'Indicates whether a service is selected.'
##    IsServiceSelected = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def ServiceName(self, index):
##        u'The search service object name at the specified index.'
##        #return ppSON
##
##    def Empty(self):
##        u'Reset to default value and clean service names array.'
##        #return 
##
##    @property
##    def ServicesCount(self):
##        u'The count of search services.'
##        #return pCount
##
##    def _get(self):
##        u'The maximum number of search result per page.'
##        #return pCount
##    def _set(self, pCount):
##        u'The maximum number of search result per page.'
##    MaxResultsPerPage = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether to show pop-up in search result page.'
##        #return pShow
##    def _set(self, pShow):
##        u'Indicates whether to show pop-up in search result page.'
##    ShowPopup = property(_get, _set, doc = _set.__doc__)
##
##    def EmptySearchOptions(self):
##        u'Resets the default values of the search options page.'
##        #return 
##
##    def DeleteServiceName(self, pSON):
##        u'Delete search service name.'
##        #return 
##

class IItemIndexer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members of indexer.'
    _iid_ = GUID('{B1213E5F-D10A-45DC-9413-6C39CFE1254E}')
    _idlflags_ = ['oleautomation']
IItemIndexer._methods_ = [
    COMMETHOD(['propget', helpstring(u'Name of the indexer.')], HRESULT, 'IndexerName',
              ( ['retval', 'out'], POINTER(BSTR), 'pName' )),
    COMMETHOD(['propput', helpstring(u'Name of the indexer.')], HRESULT, 'IndexerName',
              ( ['in'], BSTR, 'pName' )),
    COMMETHOD([helpstring(u'Build index with indexing helper.')], HRESULT, 'BuildIndex',
              ( ['in'], POINTER(IIndexingConfiguration), 'pConfig' ),
              ( ['in'], POINTER(IItemIndex), 'pIItemIndex' )),
]
################################################################
## code template for IItemIndexer implementation
##class IItemIndexer_Impl(object):
##    def _get(self):
##        u'Name of the indexer.'
##        #return pName
##    def _set(self, pName):
##        u'Name of the indexer.'
##    IndexerName = property(_get, _set, doc = _set.__doc__)
##
##    def BuildIndex(self, pConfig, pIItemIndex):
##        u'Build index with indexing helper.'
##        #return 
##

class ISearchServerAdmin(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to search server admin information.'
    _iid_ = GUID('{92CA4211-1C08-4A8E-A592-27A00C37D308}')
    _idlflags_ = ['oleautomation']
ISearchServerAdmin._methods_ = [
    COMMETHOD(['propget', helpstring(u'Search index location.')], HRESULT, 'SearchIndexLocation',
              ( ['retval', 'out'], POINTER(BSTR), 'SearchIndexLocation' )),
]
################################################################
## code template for ISearchServerAdmin implementation
##class ISearchServerAdmin_Impl(object):
##    @property
##    def SearchIndexLocation(self):
##        u'Search index location.'
##        #return SearchIndexLocation
##


# values for enumeration 'esriIndexingType'
esriIndexingTypeFirstTimeFull = 0
esriIndexingTypeFull = 1
esriIndexingTypeIncremental = 2
esriIndexingType = c_int # enum
IIndexingStatus._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates the indexing type.')], HRESULT, 'IndexingType',
              ( ['retval', 'out'], POINTER(esriIndexingType), 'IndexingType' )),
    COMMETHOD(['propput', helpstring(u'Indicates the indexing type.')], HRESULT, 'IndexingType',
              ( ['in'], esriIndexingType, 'IndexingType' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the index tasks is running.')], HRESULT, 'IsRunning',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pValid' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the index tasks is running.')], HRESULT, 'IsRunning',
              ( ['in'], VARIANT_BOOL, 'pValid' )),
    COMMETHOD(['propget', helpstring(u'Index start time.')], HRESULT, 'StartTime',
              ( ['retval', 'out'], POINTER(BSTR), 'StartTime' )),
    COMMETHOD(['propput', helpstring(u'Index start time.')], HRESULT, 'StartTime',
              ( ['in'], BSTR, 'StartTime' )),
    COMMETHOD(['propget', helpstring(u'Time used for indexing.')], HRESULT, 'TimeUsed',
              ( ['retval', 'out'], POINTER(c_int), 'TimeUsed' )),
    COMMETHOD(['propput', helpstring(u'Time used for indexing.')], HRESULT, 'TimeUsed',
              ( ['in'], c_int, 'TimeUsed' )),
    COMMETHOD(['propput', helpstring(u'Indicators whether items are indexed.')], HRESULT, 'ItemsIndexed',
              ( ['in'], c_int, 'ItemsIndexed' )),
    COMMETHOD(['propget', helpstring(u'Indicators whether items are indexed.')], HRESULT, 'ItemsIndexed',
              ( ['retval', 'out'], POINTER(c_int), 'ItemsIndexed' )),
    COMMETHOD(['propget', helpstring(u'Next Full indexing start time.')], HRESULT, 'NextFullIndexingStartTime',
              ( ['retval', 'out'], POINTER(BSTR), 'NextFullIndexingStartTime' )),
    COMMETHOD(['propput', helpstring(u'Next Full indexing start time.')], HRESULT, 'NextFullIndexingStartTime',
              ( ['in'], BSTR, 'NextFullIndexingStartTime' )),
    COMMETHOD(['propget', helpstring(u'Next Incremetal indexing start time.')], HRESULT, 'NextIncrementalIndexingStartTime',
              ( ['retval', 'out'], POINTER(BSTR), 'nextIncremetalIndexingStartTime' )),
    COMMETHOD(['propput', helpstring(u'Next Incremetal indexing start time.')], HRESULT, 'NextIncrementalIndexingStartTime',
              ( ['in'], BSTR, 'nextIncremetalIndexingStartTime' )),
    COMMETHOD(['propget', helpstring(u'Indicates next indexing type.')], HRESULT, 'NextIndexingType',
              ( ['retval', 'out'], POINTER(esriIndexingType), 'IndexingType' )),
    COMMETHOD(['propput', helpstring(u'Indicates next indexing type.')], HRESULT, 'NextIndexingType',
              ( ['in'], esriIndexingType, 'IndexingType' )),
]
################################################################
## code template for IIndexingStatus implementation
##class IIndexingStatus_Impl(object):
##    def _get(self):
##        u'Indicates the indexing type.'
##        #return IndexingType
##    def _set(self, IndexingType):
##        u'Indicates the indexing type.'
##    IndexingType = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Next Incremetal indexing start time.'
##        #return nextIncremetalIndexingStartTime
##    def _set(self, nextIncremetalIndexingStartTime):
##        u'Next Incremetal indexing start time.'
##    NextIncrementalIndexingStartTime = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Next Full indexing start time.'
##        #return NextFullIndexingStartTime
##    def _set(self, NextFullIndexingStartTime):
##        u'Next Full indexing start time.'
##    NextFullIndexingStartTime = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates next indexing type.'
##        #return IndexingType
##    def _set(self, IndexingType):
##        u'Indicates next indexing type.'
##    NextIndexingType = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the index tasks is running.'
##        #return pValid
##    def _set(self, pValid):
##        u'Indicates if the index tasks is running.'
##    IsRunning = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Time used for indexing.'
##        #return TimeUsed
##    def _set(self, TimeUsed):
##        u'Time used for indexing.'
##    TimeUsed = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Index start time.'
##        #return StartTime
##    def _set(self, StartTime):
##        u'Index start time.'
##    StartTime = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicators whether items are indexed.'
##        #return ItemsIndexed
##    def _set(self, ItemsIndexed):
##        u'Indicators whether items are indexed.'
##    ItemsIndexed = property(_get, _set, doc = _set.__doc__)
##

class IndexingConfiguration(CoClass):
    u'Provide access to the IndexingConfiguration object.'
    _reg_clsid_ = GUID('{95572BB7-BC6D-4185-9CB2-CDF7E459DD9A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E418C392-C3A6-4EB2-8870-001ABAE6B5B4}', 10, 2)
IndexingConfiguration._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IIndexingConfiguration]

class DSCStatus(CoClass):
    u'Data source status object.'
    _reg_clsid_ = GUID('{CAD5A673-3499-4D43-842F-37CE02A9ECEA}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E418C392-C3A6-4EB2-8870-001ABAE6B5B4}', 10, 2)
DSCStatus._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDSCStatus, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLVersionSupport]

class GPItemInfoHelper(CoClass):
    u'Item Info Helper.'
    _reg_clsid_ = GUID('{2EF6232E-2202-4FCF-A36E-31B3FA4AAA80}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E418C392-C3A6-4EB2-8870-001ABAE6B5B4}', 10, 2)
GPItemInfoHelper._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGPItemInfoHelper]

IItemIndex2._methods_ = [
    COMMETHOD([helpstring(u'Update thumbnail info in index.')], HRESULT, 'UpdateThumbnail',
              ( ['in'], BSTR, 'catalogPath' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IThumbnailInfo), 'pThumbInfo' )),
    COMMETHOD(['propget', helpstring(u'The CatalogPaths without thumbnail info.')], HRESULT, 'ItemsMissingThumbnails',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'ppCatalogPaths' )),
]
################################################################
## code template for IItemIndex2 implementation
##class IItemIndex2_Impl(object):
##    @property
##    def ItemsMissingThumbnails(self):
##        u'The CatalogPaths without thumbnail info.'
##        #return ppCatalogPaths
##
##    def UpdateThumbnail(self, catalogPath, pThumbInfo):
##        u'Update thumbnail info in index.'
##        #return 
##


# values for enumeration 'esriDataSourceType'
esriDataSourceTypeDatabase = 0
esriDataSourceTypeFolder = 1
esriDataSourceTypeServer = 2
esriDataSourceType = c_int # enum
IItemIndex3._methods_ = [
    COMMETHOD([helpstring(u'Adds another index.')], HRESULT, 'AddIndex',
              ( ['in'], BSTR, 'indexDirectory' ),
              ( ['in'], VARIANT_BOOL, 'dedup' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether if a give prefix matches any catalog path.')], HRESULT, 'PrefixExists',
              ( ['in'], BSTR, 'prefix' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbExsits' )),
    COMMETHOD([helpstring(u'Compares with another index.')], HRESULT, 'Compare',
              ( ['in'], BSTR, 'indexDirectory' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'ppDiffs' )),
]
################################################################
## code template for IItemIndex3 implementation
##class IItemIndex3_Impl(object):
##    @property
##    def PrefixExists(self, prefix):
##        u'Indicates whether if a give prefix matches any catalog path.'
##        #return pbExsits
##
##    def Compare(self, indexDirectory):
##        u'Compares with another index.'
##        #return ppDiffs
##
##    def AddIndex(self, indexDirectory, dedup):
##        u'Adds another index.'
##        #return 
##

class GPItemIndexer(CoClass):
    u'GPItemIndexer object.'
    _reg_clsid_ = GUID('{3FCA2200-95F0-4B78-A575-4F0AAA04FCCE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E418C392-C3A6-4EB2-8870-001ABAE6B5B4}', 10, 2)
class IGPMultithreadedItemIndexer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to multithreaded GP Indexer.'
    _iid_ = GUID('{DB185959-C37D-4B82-A6D4-CDDE04C8373B}')
    _idlflags_ = ['oleautomation']
GPItemIndexer._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IItemIndexer, IGPItemIndexer, IGPItemIndexer2, IGPMultithreadedItemIndexer]

IGPMultithreadedItemIndexer._methods_ = [
    COMMETHOD(['propget', helpstring(u'The number of instances for index creation.')], HRESULT, 'ThreadCount',
              ( ['retval', 'out'], POINTER(c_int), 'pThreadCount' )),
    COMMETHOD(['propput', helpstring(u'The number of instances for index creation.')], HRESULT, 'ThreadCount',
              ( ['in'], c_int, 'pThreadCount' )),
    COMMETHOD(['propget', helpstring(u'The ArcGIS server object to perform index creation.')], HRESULT, 'ServerObjectName',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName)), 'ppName' )),
    COMMETHOD(['propputref', helpstring(u'The ArcGIS server object to perform index creation.')], HRESULT, 'ServerObjectName',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IName), 'ppName' )),
    COMMETHOD([helpstring(u'Indexes items from an array of data sources.')], HRESULT, 'IndexItems',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray), 'pPaths' ),
              ( ['in'], VARIANT_BOOL, 'ReplaceIndex' ),
              ( ['in'], VARIANT_BOOL, 'Recursive' ),
              ( ['in'], BSTR, 'indexPath' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'pTrackCancel' )),
]
################################################################
## code template for IGPMultithreadedItemIndexer implementation
##class IGPMultithreadedItemIndexer_Impl(object):
##    def ServerObjectName(self, ppName):
##        u'The ArcGIS server object to perform index creation.'
##        #return 
##
##    def IndexItems(self, pPaths, ReplaceIndex, Recursive, indexPath, pTrackCancel):
##        u'Indexes items from an array of data sources.'
##        #return 
##
##    def _get(self):
##        u'The number of instances for index creation.'
##        #return pThreadCount
##    def _set(self, pThreadCount):
##        u'The number of instances for index creation.'
##    ThreadCount = property(_get, _set, doc = _set.__doc__)
##

class IndexingOptions(CoClass):
    u'Indexing Options object.'
    _reg_clsid_ = GUID('{63B1F04D-A050-4DA8-957D-397FF55CBCD9}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E418C392-C3A6-4EB2-8870-001ABAE6B5B4}', 10, 2)
IndexingOptions._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IIndexingOptions, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist]

class IGPItemThumbnailIndexer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides to members for adding thumbnails to index.'
    _iid_ = GUID('{C1E4C2D8-1C52-4E53-B9AA-3C6B71F70E68}')
    _idlflags_ = ['oleautomation']
IGPItemThumbnailIndexer._methods_ = [
    COMMETHOD([helpstring(u'Generate thumbnails in Index')], HRESULT, 'GenerateThumbnails'),
    COMMETHOD(['propget', helpstring(u'Percent of updated thumbnails.')], HRESULT, 'Percent',
              ( ['retval', 'out'], POINTER(c_int), 'pPercent' )),
]
################################################################
## code template for IGPItemThumbnailIndexer implementation
##class IGPItemThumbnailIndexer_Impl(object):
##    @property
##    def Percent(self):
##        u'Percent of updated thumbnails.'
##        #return pPercent
##
##    def GenerateThumbnails(self):
##        u'Generate thumbnails in Index'
##        #return 
##

IDataSourceConfiguration._methods_ = [
    COMMETHOD(['propget', helpstring(u'Data source type.')], HRESULT, 'Type',
              ( ['retval', 'out'], POINTER(esriDataSourceType), 'Type' )),
    COMMETHOD(['propput', helpstring(u'Data source type.')], HRESULT, 'Type',
              ( ['in'], esriDataSourceType, 'Type' )),
    COMMETHOD(['propget', helpstring(u'Catalogpath of Data source.')], HRESULT, 'Path',
              ( ['retval', 'out'], POINTER(BSTR), 'Path' )),
    COMMETHOD(['propput', helpstring(u'Catalogpath of Data source.')], HRESULT, 'Path',
              ( ['in'], BSTR, 'Path' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether it is revursive index.')], HRESULT, 'Recursive',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Recursive' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether it is revursive index.')], HRESULT, 'Recursive',
              ( ['in'], VARIANT_BOOL, 'Recursive' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether it replaces existing index.')], HRESULT, 'ReplaceItems',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ReplaceItems' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether it replaces existing index.')], HRESULT, 'ReplaceItems',
              ( ['in'], VARIANT_BOOL, 'ReplaceItems' )),
    COMMETHOD(['propget', helpstring(u'Indexing start  time.')], HRESULT, 'StartTime',
              ( ['retval', 'out'], POINTER(BSTR), 'StartTime' )),
    COMMETHOD(['propput', helpstring(u'Indexing start  time.')], HRESULT, 'StartTime',
              ( ['in'], BSTR, 'StartTime' )),
    COMMETHOD(['propget', helpstring(u'Repeat interval of indexing.')], HRESULT, 'RepeatInterval',
              ( ['retval', 'out'], POINTER(c_int), 'RepeatInterval' )),
    COMMETHOD(['propput', helpstring(u'Repeat interval of indexing.')], HRESULT, 'RepeatInterval',
              ( ['in'], c_int, 'RepeatInterval' )),
]
################################################################
## code template for IDataSourceConfiguration implementation
##class IDataSourceConfiguration_Impl(object):
##    def _get(self):
##        u'Repeat interval of indexing.'
##        #return RepeatInterval
##    def _set(self, RepeatInterval):
##        u'Repeat interval of indexing.'
##    RepeatInterval = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether it is revursive index.'
##        #return Recursive
##    def _set(self, Recursive):
##        u'Indicates whether it is revursive index.'
##    Recursive = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether it replaces existing index.'
##        #return ReplaceItems
##    def _set(self, ReplaceItems):
##        u'Indicates whether it replaces existing index.'
##    ReplaceItems = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indexing start  time.'
##        #return StartTime
##    def _set(self, StartTime):
##        u'Indexing start  time.'
##    StartTime = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Catalogpath of Data source.'
##        #return Path
##    def _set(self, Path):
##        u'Catalogpath of Data source.'
##    Path = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Data source type.'
##        #return Type
##    def _set(self, Type):
##        u'Data source type.'
##    Type = property(_get, _set, doc = _set.__doc__)
##

IIndexingOptions._methods_ = [
    COMMETHOD(['propget', helpstring(u'Incremental index interval.')], HRESULT, 'IncrementalIndexInterval',
              ( ['retval', 'out'], POINTER(c_int), 'pInterval' )),
    COMMETHOD(['propput', helpstring(u'Incremental index interval.')], HRESULT, 'IncrementalIndexInterval',
              ( ['in'], c_int, 'pInterval' )),
    COMMETHOD(['propget', helpstring(u'Full index interval.')], HRESULT, 'FullIndexInterval',
              ( ['retval', 'out'], POINTER(c_int), 'pInterval' )),
    COMMETHOD(['propput', helpstring(u'Full index interval.')], HRESULT, 'FullIndexInterval',
              ( ['in'], c_int, 'pInterval' )),
    COMMETHOD(['propget', helpstring(u'Index start time.')], HRESULT, 'StartTime',
              ( ['retval', 'out'], POINTER(BSTR), 'StartTime' )),
    COMMETHOD(['propput', helpstring(u'Index start time.')], HRESULT, 'StartTime',
              ( ['in'], BSTR, 'StartTime' )),
]
################################################################
## code template for IIndexingOptions implementation
##class IIndexingOptions_Impl(object):
##    def _get(self):
##        u'Full index interval.'
##        #return pInterval
##    def _set(self, pInterval):
##        u'Full index interval.'
##    FullIndexInterval = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Index start time.'
##        #return StartTime
##    def _set(self, StartTime):
##        u'Index start time.'
##    StartTime = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Incremental index interval.'
##        #return pInterval
##    def _set(self, pInterval):
##        u'Incremental index interval.'
##    IncrementalIndexInterval = property(_get, _set, doc = _set.__doc__)
##

IDSCStatus._methods_ = [
    COMMETHOD(['propget', helpstring(u'Catalog Path of Data Source.')], HRESULT, 'Path',
              ( ['retval', 'out'], POINTER(BSTR), 'Path' )),
    COMMETHOD(['propput', helpstring(u'Catalog Path of Data Source.')], HRESULT, 'Path',
              ( ['in'], BSTR, 'Path' )),
    COMMETHOD(['propget', helpstring(u'Job ID of the Data Source.')], HRESULT, 'JobID',
              ( ['retval', 'out'], POINTER(BSTR), 'JobID' )),
    COMMETHOD(['propput', helpstring(u'Job ID of the Data Source.')], HRESULT, 'JobID',
              ( ['in'], BSTR, 'JobID' )),
    COMMETHOD(['propget', helpstring(u'JobStatus of the Data Source.')], HRESULT, 'JobStatus',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.esriJobStatus), 'JobID' )),
    COMMETHOD(['propput', helpstring(u'JobStatus of the Data Source.')], HRESULT, 'JobStatus',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.esriJobStatus, 'JobID' )),
]
################################################################
## code template for IDSCStatus implementation
##class IDSCStatus_Impl(object):
##    def _get(self):
##        u'Catalog Path of Data Source.'
##        #return Path
##    def _set(self, Path):
##        u'Catalog Path of Data Source.'
##    Path = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'JobStatus of the Data Source.'
##        #return JobID
##    def _set(self, JobID):
##        u'JobStatus of the Data Source.'
##    JobStatus = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Job ID of the Data Source.'
##        #return JobID
##    def _set(self, JobID):
##        u'Job ID of the Data Source.'
##    JobID = property(_get, _set, doc = _set.__doc__)
##

class IDataSourceConfiguration2(IDataSourceConfiguration):
    _case_insensitive_ = True
    u'Provides access to data source configuration.'
    _iid_ = GUID('{A1CA9D07-71B5-4D6B-B6FA-663345FBC4FE}')
    _idlflags_ = ['oleautomation']
IDataSourceConfiguration2._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates whether to skip connection files (sde, ags, wcs, wms, etc) copied to non-default locations.')], HRESULT, 'SkipConnections',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pSkipConnections' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether to skip connection files (sde, ags, wcs, wms, etc) copied to non-default locations.')], HRESULT, 'SkipConnections',
              ( ['in'], VARIANT_BOOL, 'pSkipConnections' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether to skip mosaic dataset items when indexing.')], HRESULT, 'SkipMosaicItems',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pSkipMosaicItems' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether to skip mosaic dataset items when indexing.')], HRESULT, 'SkipMosaicItems',
              ( ['in'], VARIANT_BOOL, 'pSkipMosaicItems' )),
]
################################################################
## code template for IDataSourceConfiguration2 implementation
##class IDataSourceConfiguration2_Impl(object):
##    def _get(self):
##        u'Indicates whether to skip connection files (sde, ags, wcs, wms, etc) copied to non-default locations.'
##        #return pSkipConnections
##    def _set(self, pSkipConnections):
##        u'Indicates whether to skip connection files (sde, ags, wcs, wms, etc) copied to non-default locations.'
##    SkipConnections = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether to skip mosaic dataset items when indexing.'
##        #return pSkipMosaicItems
##    def _set(self, pSkipMosaicItems):
##        u'Indicates whether to skip mosaic dataset items when indexing.'
##    SkipMosaicItems = property(_get, _set, doc = _set.__doc__)
##

__all__ = ['IItemIndex3', 'IItemIndex2', 'IDataSourceConfiguration2',
           'esriDataSourceTypeFolder', 'GPItemIndexer', 'IDSCStatus',
           'ISearchConfiguration', 'IGPItemInfoHelper', 'DSCStatus',
           'IIndexingOptions', 'IIndexingConfiguration2',
           'IIndexingConfiguration3', 'SearchServerObjectDescription',
           'IIndexingStatus', 'GPItemInfoHelper', 'IItemIndexer',
           'ISearchServer', 'IDSCStatusArray',
           'esriIndexingTypeFirstTimeFull',
           'esriDataSourceTypeDatabase', 'SearchServerIP',
           'IGPItemIndexer2', 'SearchConfiguration',
           'IIndexingConfiguration', 'IProtectNameSearch',
           'esriIndexingTypeIncremental', 'SearchServerLP',
           'IndexingStatus', 'esriIndexingType',
           'esriIndexingTypeFull', 'IndexingOptions',
           'IGPItemIndexer', 'IItemIndexAdmin',
           'IGPItemThumbnailIndexer', 'DataSourceConfiguration',
           'DSCStatusArray', 'ItemIndex', 'esriDataSourceTypeServer',
           'IItemIndex', 'IndexingConfiguration',
           'esriDataSourceType', 'IGPMultithreadedItemIndexer',
           'SearchServerConfigurationFactory', 'ISearchServerAdmin',
           'IDataSourceConfiguration']
from comtypes import _check_version; _check_version('501')

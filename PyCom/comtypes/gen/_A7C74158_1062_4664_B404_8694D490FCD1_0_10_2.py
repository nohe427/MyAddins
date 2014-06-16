# -*- coding: mbcs -*-
typelib_path = u'C:\\Program Files (x86)\\ArcGIS\\Engine10.2\\com\\esriGeoDatabaseDistributed.olb'
_lcid = 0 # change this if required
from ctypes import *
import comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2
import comtypes.gen._18F2FC71_6B30_45B9_B101_037A8B868B66_0_10_2
import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0
from comtypes import GUID
from ctypes import HRESULT
from comtypes import IUnknown
from ctypes.wintypes import VARIANT_BOOL
import comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2
from comtypes import helpstring
from comtypes import COMMETHOD
from comtypes import dispid
from comtypes import BSTR
from comtypes import CoClass
from comtypes.automation import _midlSAFEARRAY
import comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2
from comtypes.automation import VARIANT
import comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2
from comtypes.automation import VARIANT


class ISchemaChangeInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the replica schema change info.'
    _iid_ = GUID('{B5CCF6D9-D034-4177-8827-F1493785DE8F}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriSchemaChangeType'
esriSchemaChangeTypeNoChange = 0
esriSchemaChangeTypeAny = 1
esriSchemaChangeTypeNewFeatureDataset = 2
esriSchemaChangeTypeUpdateFeatureDataset = 3
esriSchemaChangeTypeDeleteFeatureDataset = 4
esriSchemaChangeTypeNewTable = 5
esriSchemaChangeTypeDeleteTable = 6
esriSchemaChangeTypeUpdateTable = 7
esriSchemaChangeTypeNewRelationshipClass = 8
esriSchemaChangeTypeDeleteRelationshipClass = 9
esriSchemaChangeTypeUpdateRelationshipClass = 10
esriSchemaChangeTypeNewField = 11
esriSchemaChangeTypeUpdateField = 12
esriSchemaChangeTypeDeleteField = 13
esriSchemaChangeTypeNewDomain = 14
esriSchemaChangeTypeUpdateDomain = 15
esriSchemaChangeTypeDeleteDomain = 16
esriSchemaChangeTypeUpdateFields = 17
esriSchemaChangeTypeUpdateDomains = 18
esriSchemaChangeTypeNewGeometricNetwork = 19
esriSchemaChangeTypeUpdateGeometricNetwork = 20
esriSchemaChangeTypeDeleteGeometricNetwork = 21
esriSchemaChangeTypeNewTopology = 22
esriSchemaChangeTypeUpdateTopology = 23
esriSchemaChangeTypeDeleteTopology = 24
esriSchemaChangeType = c_int # enum
class IEnumSchemaChange(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the replica schema changes.'
    _iid_ = GUID('{52B0879B-28C4-4904-A402-91378488B867}')
    _idlflags_ = ['oleautomation']
ISchemaChangeInfo._methods_ = [
    COMMETHOD(['propget', helpstring(u'Type of schema change.')], HRESULT, 'SchemaChangeType',
              ( ['retval', 'out'], POINTER(esriSchemaChangeType), 'SchemaChangeType' )),
    COMMETHOD(['propget', helpstring(u'The source replicas representation of the schema.')], HRESULT, 'FromObject',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'ChangedObject' )),
    COMMETHOD(['propget', helpstring(u'The target replicas representation of the schema.')], HRESULT, 'ToObject',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'TargetObject' )),
    COMMETHOD(['propget', helpstring(u'The parent container of the schema change object.')], HRESULT, 'ToParent',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'Parent' )),
    COMMETHOD(['propget', helpstring(u'Indicates if schema changes will be applied.')], HRESULT, 'ApplySchemaChange',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ApplySchemaChange' )),
    COMMETHOD(['propput', helpstring(u'Indicates if schema changes will be applied.')], HRESULT, 'ApplySchemaChange',
              ( ['in'], VARIANT_BOOL, 'ApplySchemaChange' )),
    COMMETHOD([helpstring(u'The schema changes.')], HRESULT, 'GetChanges',
              ( ['retval', 'out'], POINTER(POINTER(IEnumSchemaChange)), 'SchemaChanges' )),
    COMMETHOD(['propget', helpstring(u'Properties associated with the schema change object.')], HRESULT, 'ExtendedProperties',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'ExtendedProperties' )),
]
################################################################
## code template for ISchemaChangeInfo implementation
##class ISchemaChangeInfo_Impl(object):
##    @property
##    def ExtendedProperties(self):
##        u'Properties associated with the schema change object.'
##        #return ExtendedProperties
##
##    @property
##    def FromObject(self):
##        u'The source replicas representation of the schema.'
##        #return ChangedObject
##
##    def _get(self):
##        u'Indicates if schema changes will be applied.'
##        #return ApplySchemaChange
##    def _set(self, ApplySchemaChange):
##        u'Indicates if schema changes will be applied.'
##    ApplySchemaChange = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def ToObject(self):
##        u'The target replicas representation of the schema.'
##        #return TargetObject
##
##    @property
##    def ToParent(self):
##        u'The parent container of the schema change object.'
##        #return Parent
##
##    def GetChanges(self):
##        u'The schema changes.'
##        #return SchemaChanges
##
##    @property
##    def SchemaChangeType(self):
##        u'Type of schema change.'
##        #return SchemaChangeType
##

class IDeltaDataChangesInit(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that initialize a DeltaDataChanges object.'
    _iid_ = GUID('{725451C9-CD9D-4431-8020-C9ED11BB40F0}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriExportDataChangesOption'
esriExportToAccess = 1
esriExportToXML = 2
esriExportToFileGDB = 3
esriExportToSqliteGDB = 4
esriExportDataChangesOption = c_int # enum
IDeltaDataChangesInit._methods_ = [
    COMMETHOD([helpstring(u'Initializes the class by setting delta database file name and export option.')], HRESULT, 'Init',
              ( ['in'], BSTR, 'changesFileName' ),
              ( ['in'], esriExportDataChangesOption, 'exportOption' )),
]
################################################################
## code template for IDeltaDataChangesInit implementation
##class IDeltaDataChangesInit_Impl(object):
##    def Init(self, changesFileName, exportOption):
##        u'Initializes the class by setting delta database file name and export option.'
##        #return 
##

class IGeoDataServerInit(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that support initializing a GeoDataServer.'
    _iid_ = GUID('{841BDC30-FE10-46AF-B67B-582252BC16B8}')
    _idlflags_ = ['oleautomation']
IGeoDataServerInit._methods_ = [
    COMMETHOD([helpstring(u'Initializes a GeoDataServer object with a map document.')], HRESULT, 'InitFromMap',
              ( ['in'], BSTR, 'filePath' )),
    COMMETHOD([helpstring(u'Initializes a GeoDataServer object from a geodatabase or an sde connection file (*.sde).')], HRESULT, 'InitFromFile',
              ( ['in'], BSTR, 'file' )),
    COMMETHOD([helpstring(u'Initializes a GeoDataServer object from a connection string to a geodatabase.')], HRESULT, 'InitFromConnectionString',
              ( ['in'], BSTR, 'connectionString' )),
    COMMETHOD([helpstring(u'Initializes a GeoDataServer object with a workspace.')], HRESULT, 'InitWithWorkspace',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspace), 'pWorkspace' )),
    COMMETHOD(['propput', helpstring(u'The physical directory for output files.')], HRESULT, 'PhysicalOutputDirectory',
              ( ['in'], BSTR, 'dirPath' )),
    COMMETHOD(['propget', helpstring(u'The physical directory for output files.')], HRESULT, 'PhysicalOutputDirectory',
              ( ['retval', 'out'], POINTER(BSTR), 'dirPath' )),
    COMMETHOD(['propput', helpstring(u'The virtual directory for output files.')], HRESULT, 'VirtualOutputDirectory',
              ( ['in'], BSTR, 'dirPath' )),
    COMMETHOD(['propget', helpstring(u'The virtual directory for output files.')], HRESULT, 'VirtualOutputDirectory',
              ( ['retval', 'out'], POINTER(BSTR), 'dirPath' )),
    COMMETHOD(['propget', helpstring(u'The maximum number of records returned for query results.')], HRESULT, 'MaxRecordCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propput', helpstring(u'The maximum number of records returned for query results.')], HRESULT, 'MaxRecordCount',
              ( ['in'], c_int, 'Count' )),
]
################################################################
## code template for IGeoDataServerInit implementation
##class IGeoDataServerInit_Impl(object):
##    def _get(self):
##        u'The maximum number of records returned for query results.'
##        #return Count
##    def _set(self, Count):
##        u'The maximum number of records returned for query results.'
##    MaxRecordCount = property(_get, _set, doc = _set.__doc__)
##
##    def InitFromMap(self, filePath):
##        u'Initializes a GeoDataServer object with a map document.'
##        #return 
##
##    def InitFromConnectionString(self, connectionString):
##        u'Initializes a GeoDataServer object from a connection string to a geodatabase.'
##        #return 
##
##    def _get(self):
##        u'The physical directory for output files.'
##        #return dirPath
##    def _set(self, dirPath):
##        u'The physical directory for output files.'
##    PhysicalOutputDirectory = property(_get, _set, doc = _set.__doc__)
##
##    def InitWithWorkspace(self, pWorkspace):
##        u'Initializes a GeoDataServer object with a workspace.'
##        #return 
##
##    def _get(self):
##        u'The virtual directory for output files.'
##        #return dirPath
##    def _set(self, dirPath):
##        u'The virtual directory for output files.'
##    VirtualOutputDirectory = property(_get, _set, doc = _set.__doc__)
##
##    def InitFromFile(self, file):
##        u'Initializes a GeoDataServer object from a geodatabase or an sde connection file (*.sde).'
##        #return 
##

class CheckInDataSynchronizer(CoClass):
    u'Synchronizes changes from a check-out with the master geodatabase.'
    _reg_clsid_ = GUID('{0B998A30-B009-41C6-A086-6DC29BA71CD4}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{A7C74158-1062-4664-B404-8694D490FCD1}', 10, 2)
class ICheckInDataSynchronizer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that synchronize changes from a check-out geodatabase or delta database with the master geodatabase.'
    _iid_ = GUID('{73987267-11C4-477B-AE52-3DFB7DC62918}')
    _idlflags_ = ['oleautomation']
class ICheckInDataSynchronizer2(ICheckInDataSynchronizer):
    _case_insensitive_ = True
    u'Provides access to members that synchronize changes from a check-out geodatabase or delta database with the master geodatabase.'
    _iid_ = GUID('{BB18B086-729B-4990-AB3E-A457CC584548}')
    _idlflags_ = ['oleautomation']
class IReplicaProgress(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that monitor the progress of a check-out.'
    _iid_ = GUID('{5435D16A-5AA0-427F-BDAD-24BD6AABF858}')
    _idlflags_ = ['oleautomation']
CheckInDataSynchronizer._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ICheckInDataSynchronizer, ICheckInDataSynchronizer2]
CheckInDataSynchronizer._outgoing_interfaces_ = [comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureProgress, IReplicaProgress]

IEnumSchemaChange._methods_ = [
    COMMETHOD([helpstring(u'Resets the enumeration sequence to the beginning.')], HRESULT, 'Reset'),
    COMMETHOD([helpstring(u'The next schema change in the enumeration sequence.')], HRESULT, 'Next',
              ( ['retval', 'out'], POINTER(POINTER(ISchemaChangeInfo)), 'SchemaChangeInfo' )),
    COMMETHOD([helpstring(u'The schema changes for a specific domain.')], HRESULT, 'GetDomainChanges',
              ( ['in'], BSTR, 'domainName' ),
              ( ['retval', 'out'], POINTER(POINTER(ISchemaChangeInfo)), 'ppInfo' )),
    COMMETHOD([helpstring(u'The schema changes for a specific dataset.')], HRESULT, 'GetDatasetChanges',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriDatasetType, 'dsType' ),
              ( ['retval', 'out'], POINTER(POINTER(ISchemaChangeInfo)), 'ppInfo' )),
    COMMETHOD([helpstring(u'Indicates if there are schema changes.')], HRESULT, 'HasChanges',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pHasSchemaChanges' )),
    COMMETHOD(['propget', helpstring(u'The replica the schema changes will be applied to.')], HRESULT, 'ToReplica',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IReplica)), 'ToReplica' )),
]
################################################################
## code template for IEnumSchemaChange implementation
##class IEnumSchemaChange_Impl(object):
##    def Reset(self):
##        u'Resets the enumeration sequence to the beginning.'
##        #return 
##
##    def GetDomainChanges(self, domainName):
##        u'The schema changes for a specific domain.'
##        #return ppInfo
##
##    @property
##    def ToReplica(self):
##        u'The replica the schema changes will be applied to.'
##        #return ToReplica
##
##    def HasChanges(self):
##        u'Indicates if there are schema changes.'
##        #return pHasSchemaChanges
##
##    def GetDatasetChanges(self, Name, dsType):
##        u'The schema changes for a specific dataset.'
##        #return ppInfo
##
##    def Next(self):
##        u'The next schema change in the enumeration sequence.'
##        #return SchemaChangeInfo
##


# values for enumeration 'esriWFSServerMessageCodeEnum'
esriWFSServerMessageCode_SkippedDataset = 92000
esriWFSServerMessageCode_FailedToGenerateTransactionResponse = 92001
esriWFSServerMessageCode_FailedToDeleteLock = 92002
esriWFSServerMessageCode_FailedToDeleteOutstandingTransactionVersions = 92003
esriWFSServerMessageCode_NotLicensed = 92004
esriWFSServerMessageCode_GetRequest = 92005
esriWFSServerMessageCode_PostRequest = 92006
esriWFSServerMessageCode_WFSExceptionReport = 92007
esriWFSServerMessageCode_Debug = 92008
esriWFSServerMessageCode_FailedToReleaseLocks = 92009
esriWFSServerMessageCode_ConstructStart = 92010
esriWFSServerMessageCode_ErrorInvalidAppSchemaNamespace = 92011
esriWFSServerMessageCode_ErrorInvalidAppSchemaPrefix = 92012
esriWFSServerMessageCode_ErrorInvalidDefaultLockExpiration = 92013
esriWFSServerMessageCode_ErrorPublishedWorkspaceIsntVersioned = 92014
esriWFSServerMessageCode_ConstructEnded = 92015
esriWFSServerMessageCode_ErrorInvalid10AxisOrder = 92016
esriWFSServerMessageCode_ErrorInvalid11AxisOrder = 92017
esriWFSServerMessageCode_ErrorInvalidUseSRSNameFormat = 92018
esriWFSServerMessageCode_FailedToReconcileAgainstSelf = 92019
esriWFSServerMessageCode_FailedToStopEditing = 92020
esriWFSServerMessageCode_ServerTooBusyToProcessTransaction = 92021
esriWFSServerMessageCode_FailedToImportTransactionChanges = 92022
esriWFSServerMessageCode_FailedCreatingTransactionResponse = 92023
esriWFSServerMessageCode_TransactionFailedStoppingEditOperation = 92024
esriWFSServerMessageCode_FailedToStartEditing = 92025
esriWFSServerMessageCode_ConflictDetected = 92026
esriWFSServerMessageCodeEnum = c_int # enum
class IGDSData(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods supported by a GDSReplicaData object.'
    _iid_ = GUID('{BDFD716D-E902-4907-9C97-65DA73F02AE9}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriGDSTransportType'
esriGDSTransportTypeEmbedded = 0
esriGDSTransportTypeUrl = 1
esriGDSTransportTypeUpload = 2
esriGDSTransportType = c_int # enum
IGDSData._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates whether the data has been compressed.')], HRESULT, 'Compressed',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'comp' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether the data has been compressed.')], HRESULT, 'Compressed',
              ( ['in'], VARIANT_BOOL, 'comp' )),
    COMMETHOD(['propget', helpstring(u'The transport type used to transfer the replica data.')], HRESULT, 'TransportType',
              ( ['retval', 'out'], POINTER(esriGDSTransportType), 'pTransport' )),
    COMMETHOD(['propput', helpstring(u'The transport type used to transfer the replica data.')], HRESULT, 'TransportType',
              ( ['in'], esriGDSTransportType, 'pTransport' )),
    COMMETHOD(['propget', helpstring(u'The url where the replica data is located.')], HRESULT, 'URL',
              ( ['retval', 'out'], POINTER(BSTR), 'URL' )),
    COMMETHOD(['propput', helpstring(u'The url where the replica data is located.')], HRESULT, 'URL',
              ( ['in'], BSTR, 'URL' )),
    COMMETHOD(['propget', helpstring(u'The embedded replica data.')], HRESULT, 'EmbeddedData',
              ( ['retval', 'out'], POINTER(_midlSAFEARRAY(c_ubyte)), 'data' )),
    COMMETHOD(['propput', helpstring(u'The embedded replica data.')], HRESULT, 'EmbeddedData',
              ( ['in'], POINTER(_midlSAFEARRAY(c_ubyte)), 'data' )),
    COMMETHOD(['propputref', helpstring(u'The properties to be used when downloading the data (if transport type is URL).')], HRESULT, 'ConnectionProperties',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'connProps' )),
    COMMETHOD(['propget', helpstring(u'The properties to be used when downloading the data (if transport type is URL).')], HRESULT, 'ConnectionProperties',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'connProps' )),
]
################################################################
## code template for IGDSData implementation
##class IGDSData_Impl(object):
##    def _get(self):
##        u'The url where the replica data is located.'
##        #return URL
##    def _set(self, URL):
##        u'The url where the replica data is located.'
##    URL = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The embedded replica data.'
##        #return data
##    def _set(self, data):
##        u'The embedded replica data.'
##    EmbeddedData = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The transport type used to transfer the replica data.'
##        #return pTransport
##    def _set(self, pTransport):
##        u'The transport type used to transfer the replica data.'
##    TransportType = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def ConnectionProperties(self, connProps):
##        u'The properties to be used when downloading the data (if transport type is URL).'
##        #return 
##
##    def _get(self):
##        u'Indicates whether the data has been compressed.'
##        #return comp
##    def _set(self, comp):
##        u'Indicates whether the data has been compressed.'
##    Compressed = property(_get, _set, doc = _set.__doc__)
##


# values for enumeration 'esriGDSImportFormat'
esriGDSImportFormatXmlWorkspace = 0
esriGDSImportFormatFileGDB = 1
esriGDSImportFormatPersonalGdb = 2
esriGDSImportFormat = c_int # enum
class DataChangesImporter(CoClass):
    u'Imports edits or checks in from a delta file to a geodatabase.'
    _reg_clsid_ = GUID('{CE014FAF-2B6D-4D74-8177-00980BA739AE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{A7C74158-1062-4664-B404-8694D490FCD1}', 10, 2)
class IImportDataChanges(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that import edits or check in from a delta file to a geodatabase.'
    _iid_ = GUID('{3EEA0FB7-0478-400B-BF5C-122EA29C50A4}')
    _idlflags_ = ['oleautomation']
class IImportDataChanges2(IImportDataChanges):
    _case_insensitive_ = True
    u'Provides access to members that import edits or check in from a delta file to a geodatabase.'
    _iid_ = GUID('{27FA7510-E45D-49A2-8D57-7753DB605D04}')
    _idlflags_ = ['oleautomation']
DataChangesImporter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IImportDataChanges, IImportDataChanges2]
DataChangesImporter._outgoing_interfaces_ = [comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureProgress, IReplicaProgress]


# values for enumeration 'esriReplicationAgentReconcilePolicy'
esriRADetectConflicts = 0
esriRAResolveConflictsInFavorOfReplica1 = 1
esriRAResolveConflictsInFavorOfReplica2 = 2
esriRAResolveConflictsNone = 3
esriReplicationAgentReconcilePolicy = c_int # enum
class IGeoDataServer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods supported by a GeoDataServer Object.'
    _iid_ = GUID('{B59DEDDD-065F-4C9F-942A-AF79E8AB3FBC}')
    _idlflags_ = ['oleautomation']
class IGeoDataServer2(IGeoDataServer):
    _case_insensitive_ = True
    u'Provides access to methods supported by a GeoDataServer Object.'
    _iid_ = GUID('{5906A736-62ED-4FB6-B84F-191131DFAB07}')
    _idlflags_ = ['oleautomation']
class IGDSExportOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods that control replica export.'
    _iid_ = GUID('{FC23FBC0-DC6A-41FC-8914-36677FBA6855}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriExportGenerationsOption'
esriExportGenerationsUnAcknowledged = 1
esriExportGenerationsNew = 2
esriExportGenerationsAll = 3
esriExportGenerationsNone = 4
esriExportGenerationsOption = c_int # enum

# values for enumeration 'esriReExportGenerationsOption'
esriReExportGenerationsAllUnAcknowledged = 1
esriReExportGenerationsLastUnAcknowledged = 2
esriReExportGenerationsOption = c_int # enum

# values for enumeration 'esriGDSReplicaImportSource'
esriGDSReplicaImportSourceDeltaXmlFile = 0
esriGDSReplicaImportSourceDeltaPersonalGDB = 1
esriGDSReplicaImportSourceDeltaFileGDB = 2
esriGDSReplicaImportSourceDeltaSqliteGDB = 3
esriGDSReplicaImportSource = c_int # enum
class IGDSQueryResultPortion(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to elements of a result portion.'
    _iid_ = GUID('{6BABAF1E-D1A3-487F-BDE1-58A206503DBC}')
    _idlflags_ = ['oleautomation']
IGeoDataServer._methods_ = [
    COMMETHOD(['propget', helpstring(u'The maximum number of records to be returned by a search.')], HRESULT, 'MaxRecordCount',
              ( ['retval', 'out'], POINTER(c_int), 'maxCount' )),
    COMMETHOD(['propget', helpstring(u'The data elements in the workspace.')], HRESULT, 'DataElements',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDEBrowseOptions), 'pBrowseOptions' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDataElements)), 'DataElements' )),
    COMMETHOD(['propget', helpstring(u'The versions in the workspace.')], HRESULT, 'Versions',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPVersionInfos)), 'versionInfos' )),
    COMMETHOD(['propget', helpstring(u'The replicas in the workspace.')], HRESULT, 'Replicas',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPReplicas)), 'Replicas' )),
    COMMETHOD(['propget', helpstring(u'The default working version for all operations/methods.')], HRESULT, 'DefaultWorkingVersion',
              ( ['retval', 'out'], POINTER(BSTR), 'DefaultWorkingVersion' )),
    COMMETHOD(['propget', helpstring(u'The type of the geodatabase the geodataserver operates on.')], HRESULT, 'WrappedWorkspaceType',
              ( ['retval', 'out'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriWorkspaceType), 'wsType' )),
    COMMETHOD([helpstring(u'Extract Data.')], HRESULT, 'ExtractData',
              ( ['in'], BSTR, 'versionName' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPReplicaDescription), 'replicaDesc' ),
              ( ['in'], POINTER(IGDSExportOptions), 'options' ),
              ( ['in'], esriGDSTransportType, 'TransportType' ),
              ( ['retval', 'out'], POINTER(POINTER(IGDSData)), 'result' )),
    COMMETHOD([helpstring(u'Creates a Replica.')], HRESULT, 'CreateReplica',
              ( ['in'], BSTR, 'parentVersion' ),
              ( ['in'], BSTR, 'ReplicaName' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPReplicaDescription), 'replicaDesc' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPReplicaOptions), 'repOptions' ),
              ( ['in'], POINTER(IGDSExportOptions), 'exportOptions' ),
              ( ['in'], esriGDSTransportType, 'TransportType' ),
              ( ['retval', 'out'], POINTER(POINTER(IGDSData)), 'result' )),
    COMMETHOD([helpstring(u'Expands a set of replica datasets taking into consideration geodatabase constructs (topologies, relationship classes, etc.).')], HRESULT, 'ExpandReplicaDatasets',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPReplicaDatasets), 'repDatasets' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPReplicaDatasets)), 'expandedRepDatasets' )),
    COMMETHOD([helpstring(u'Imports data into the workspace.')], HRESULT, 'ImportData',
              ( ['in'], POINTER(IGDSData), 'pData' ),
              ( ['in'], esriGDSImportFormat, 'fmt' )),
    COMMETHOD([helpstring(u'Exports data changes for a replica.')], HRESULT, 'ExportReplicaDataChanges',
              ( ['in'], BSTR, 'ReplicaName' ),
              ( ['in'], POINTER(IGDSExportOptions), 'options' ),
              ( ['in'], esriGDSTransportType, 'TransportType' ),
              ( ['in'], esriExportGenerationsOption, 'generationsToExport' ),
              ( ['in'], VARIANT_BOOL, 'switchRole' ),
              ( ['retval', 'out'], POINTER(POINTER(IGDSData)), 'result' )),
    COMMETHOD([helpstring(u'Re-exports data changes for a replica.')], HRESULT, 'ReExportReplicaDataChanges',
              ( ['in'], BSTR, 'ReplicaName' ),
              ( ['in'], POINTER(IGDSExportOptions), 'options' ),
              ( ['in'], esriGDSTransportType, 'TransportType' ),
              ( ['in'], esriReExportGenerationsOption, 'gensToExport' ),
              ( ['retval', 'out'], POINTER(POINTER(IGDSData)), 'result' )),
    COMMETHOD([helpstring(u'Import the data changes for a replica.')], HRESULT, 'ImportReplicaDataChanges',
              ( ['in'], esriGDSReplicaImportSource, 'sourceType' ),
              ( ['in'], comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriReplicaReconcilePolicyType, 'reconcilePolicy' ),
              ( ['in'], VARIANT_BOOL, 'columnLevel' ),
              ( ['in'], POINTER(IGDSData), 'data' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'conflictsFound' )),
    COMMETHOD([helpstring(u'Export an acknowledgement message for a replica.')], HRESULT, 'ExportAcknowledgement',
              ( ['in'], BSTR, 'ReplicaName' ),
              ( ['in'], esriGDSTransportType, 'TransportType' ),
              ( ['retval', 'out'], POINTER(POINTER(IGDSData)), 'result' )),
    COMMETHOD([helpstring(u'Import an acknowledgement message for a replica.')], HRESULT, 'ImportAcknowledgement',
              ( ['in'], POINTER(IGDSData), 'data' )),
    COMMETHOD([helpstring(u'Unregisters the replica.')], HRESULT, 'UnregisterReplica',
              ( ['in'], BSTR, 'ReplicaName' )),
    COMMETHOD([helpstring(u'Returns the records satisfying the specified query.')], HRESULT, 'TableSearch',
              ( ['in'], BSTR, 'versionName' ),
              ( ['in'], BSTR, 'tableName' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IQueryFilter), 'queryFilter' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IResultPortionInfo), 'queryRange' ),
              ( ['retval', 'out'], POINTER(POINTER(IGDSQueryResultPortion)), 'resultPortion' )),
    COMMETHOD([helpstring(u'Gets the next portion of the results.')], HRESULT, 'GetNextResultPortion',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IResultPortionInfo), 'desiredRange' ),
              ( ['retval', 'out'], POINTER(POINTER(IGDSQueryResultPortion)), 'resultPortion' )),
    COMMETHOD([helpstring(u'Exports the schema of a replica to an Xml document.')], HRESULT, 'ExportReplicaSchema',
              ( ['in'], BSTR, 'ReplicaName' ),
              ( ['in'], esriGDSTransportType, 'TransportType' ),
              ( ['retval', 'out'], POINTER(POINTER(IGDSData)), 'replicaSchemaDoc' )),
    COMMETHOD([helpstring(u'Compares the schema of a replica with that of its relative, and returns a schema changes XML document.')], HRESULT, 'CompareReplicaSchema',
              ( ['in'], POINTER(IGDSData), 'relativeReplicaSchemaDoc' ),
              ( ['in'], esriGDSTransportType, 'TransportType' ),
              ( ['retval', 'out'], POINTER(POINTER(IGDSData)), 'schemaChangesDoc' )),
    COMMETHOD([helpstring(u'Updates the schema of the replica with the changes in an schema changes XML document.')], HRESULT, 'ImportReplicaSchemaChanges',
              ( ['in'], POINTER(IGDSData), 'schemaChangesDoc' )),
]
################################################################
## code template for IGeoDataServer implementation
##class IGeoDataServer_Impl(object):
##    @property
##    def MaxRecordCount(self):
##        u'The maximum number of records to be returned by a search.'
##        #return maxCount
##
##    @property
##    def DefaultWorkingVersion(self):
##        u'The default working version for all operations/methods.'
##        #return DefaultWorkingVersion
##
##    def ExpandReplicaDatasets(self, repDatasets):
##        u'Expands a set of replica datasets taking into consideration geodatabase constructs (topologies, relationship classes, etc.).'
##        #return expandedRepDatasets
##
##    def TableSearch(self, versionName, tableName, queryFilter, queryRange):
##        u'Returns the records satisfying the specified query.'
##        #return resultPortion
##
##    def ImportAcknowledgement(self, data):
##        u'Import an acknowledgement message for a replica.'
##        #return 
##
##    def CreateReplica(self, parentVersion, ReplicaName, replicaDesc, repOptions, exportOptions, TransportType):
##        u'Creates a Replica.'
##        #return result
##
##    @property
##    def Replicas(self):
##        u'The replicas in the workspace.'
##        #return Replicas
##
##    def ReExportReplicaDataChanges(self, ReplicaName, options, TransportType, gensToExport):
##        u'Re-exports data changes for a replica.'
##        #return result
##
##    def CompareReplicaSchema(self, relativeReplicaSchemaDoc, TransportType):
##        u'Compares the schema of a replica with that of its relative, and returns a schema changes XML document.'
##        #return schemaChangesDoc
##
##    @property
##    def Versions(self):
##        u'The versions in the workspace.'
##        #return versionInfos
##
##    def ExtractData(self, versionName, replicaDesc, options, TransportType):
##        u'Extract Data.'
##        #return result
##
##    def GetNextResultPortion(self, desiredRange):
##        u'Gets the next portion of the results.'
##        #return resultPortion
##
##    @property
##    def WrappedWorkspaceType(self):
##        u'The type of the geodatabase the geodataserver operates on.'
##        #return wsType
##
##    def ImportReplicaSchemaChanges(self, schemaChangesDoc):
##        u'Updates the schema of the replica with the changes in an schema changes XML document.'
##        #return 
##
##    def ImportData(self, pData, fmt):
##        u'Imports data into the workspace.'
##        #return 
##
##    def ExportReplicaDataChanges(self, ReplicaName, options, TransportType, generationsToExport, switchRole):
##        u'Exports data changes for a replica.'
##        #return result
##
##    def ExportAcknowledgement(self, ReplicaName, TransportType):
##        u'Export an acknowledgement message for a replica.'
##        #return result
##
##    def ImportReplicaDataChanges(self, sourceType, reconcilePolicy, columnLevel, data):
##        u'Import the data changes for a replica.'
##        #return conflictsFound
##
##    def UnregisterReplica(self, ReplicaName):
##        u'Unregisters the replica.'
##        #return 
##
##    def ExportReplicaSchema(self, ReplicaName, TransportType):
##        u'Exports the schema of a replica to an Xml document.'
##        #return replicaSchemaDoc
##
##    @property
##    def DataElements(self, pBrowseOptions):
##        u'The data elements in the workspace.'
##        #return DataElements
##

IGeoDataServer2._methods_ = [
    COMMETHOD([helpstring(u'Expands a set of replica datasets taking into consideration geodatabase constructs (topologies, relationship classes, etc.).')], HRESULT, 'ExpandReplicaDatasets2',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPReplicaDatasets), 'GPReplicaDatasets' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPReplicaOptions), 'ReplicaOptions' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPReplicaDatasets)), 'ExpandGPReplicaDatasets' )),
    COMMETHOD(['propget', helpstring(u'Return the replica in the workspace that has a specific name.')], HRESULT, 'Replica',
              ( ['in'], BSTR, 'ReplicaName' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPReplica)), 'GPReplica' )),
]
################################################################
## code template for IGeoDataServer2 implementation
##class IGeoDataServer2_Impl(object):
##    def ExpandReplicaDatasets2(self, GPReplicaDatasets, ReplicaOptions):
##        u'Expands a set of replica datasets taking into consideration geodatabase constructs (topologies, relationship classes, etc.).'
##        #return ExpandGPReplicaDatasets
##
##    @property
##    def Replica(self, ReplicaName):
##        u'Return the replica in the workspace that has a specific name.'
##        #return GPReplica
##

class CheckOut(CoClass):
    u'Checks out data from a master geodatabase to a check-out geodatabase.'
    _reg_clsid_ = GUID('{DE0DDADD-814D-4C8A-ACFE-691E499ED8F3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{A7C74158-1062-4664-B404-8694D490FCD1}', 10, 2)
class ICheckOut(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that perform a check out.'
    _iid_ = GUID('{D0571EBD-D55C-46EF-90A1-246C40486DCA}')
    _idlflags_ = ['oleautomation']
CheckOut._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ICheckOut]
CheckOut._outgoing_interfaces_ = [comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureProgress, IReplicaProgress]

class CheckIn(CoClass):
    u'Checks in changes from a check-out geodatabase or a delta database to a master geodatabase.'
    _reg_clsid_ = GUID('{DB456BF9-03AC-4A72-9162-1E8FD73DE22E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{A7C74158-1062-4664-B404-8694D490FCD1}', 10, 2)
class ICheckIn(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that perform a check in.'
    _iid_ = GUID('{15C5F91A-A992-42C6-A64E-53B4965FCA46}')
    _idlflags_ = ['oleautomation']
class ICheckIn2(ICheckIn):
    _case_insensitive_ = True
    u'Provides access to members that perform a check in.'
    _iid_ = GUID('{27FCE3EE-891D-407D-A36F-4D37AD14B3F6}')
    _idlflags_ = ['oleautomation']
CheckIn._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ICheckIn, ICheckIn2]
CheckIn._outgoing_interfaces_ = [comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureProgress, IReplicaProgress]

class DataChangesExporter(CoClass):
    u'Exports edits in a check-out geodatabase or modified rows in versions to a delta file.'
    _reg_clsid_ = GUID('{FE5E515A-FC19-45E8-8E2D-46EDE0554E52}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{A7C74158-1062-4664-B404-8694D490FCD1}', 10, 2)
class IExportDataChanges(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that export edits from versions or a check-out geodatabase to a delta file.'
    _iid_ = GUID('{E290F6A3-535F-49A9-8FD4-C60FC44BF109}')
    _idlflags_ = ['oleautomation']
class IExportDataChanges2(IExportDataChanges):
    _case_insensitive_ = True
    u'Provides access to members that export edits from a version or from a check-out, one way or two way replica to a data changes file.'
    _iid_ = GUID('{8EC3471A-80E3-4552-9CC7-DFCE334CC809}')
    _idlflags_ = ['oleautomation']
DataChangesExporter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IExportDataChanges, IExportDataChanges2]


# values for enumeration 'esriReplicaProgress'
esriRPExtractSchema = 1
esriRPExtractData = 2
esriRPExtractSchemaAndData = 4
esriRPFetchRelatedObjects = 8
esriRPFetchRelatedNObjects = 16
esriRPBuildGeometricNetworks = 32
esriRPFetchTopologyObjects = 64
esriRPRegisteringCheckOut = 128
esriRPCreateCOVersions = 256
esriRPTransferChanges = 512
esriRPUpdateRelatedObjects = 1024
esriRPRebuildCIConnectivity = 2048
esriRPReconcileWithParent = 4096
esriRPUnregisteringCheckOut = 8192
esriRPCreatingCheckOut = 16384
esriRPSynchronizingCheckOut = 32768
esriRPSynchronizingReplica = 65536
esriRPCreatingReplica = 131072
esriRPRegisteringReplica = 262144
esriRPCreatingSchemaCheckOut = 524288
esriRPExportingToXML = 1048576
esriRPSavingToXMLFile = 2097152
esriRPImportingDataChanges = 4194304
esriReplicaProgress = c_int # enum
IReplicaProgress._methods_ = [
    COMMETHOD([helpstring(u'Initiate the check-out progress utility.')], HRESULT, 'Startup',
              ( ['in'], esriReplicaProgress, 'rProgress' )),
    COMMETHOD(['propput', helpstring(u'The current operation in a check-out process.')], HRESULT, 'CurrentReplicaOperation',
              ( ['in'], esriReplicaProgress, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'The number of operations to perform in a check-out.')], HRESULT, 'ReplicaOperations',
              ( ['in'], c_int, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'The number of objects to check-out.')], HRESULT, 'ReplicaObjectCount',
              ( ['in'], c_int, 'rhs' )),
]
################################################################
## code template for IReplicaProgress implementation
##class IReplicaProgress_Impl(object):
##    def _set(self, rhs):
##        u'The number of objects to check-out.'
##    ReplicaObjectCount = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'The current operation in a check-out process.'
##    CurrentReplicaOperation = property(fset = _set, doc = _set.__doc__)
##
##    def Startup(self, rProgress):
##        u'Initiate the check-out progress utility.'
##        #return 
##
##    def _set(self, rhs):
##        u'The number of operations to perform in a check-out.'
##    ReplicaOperations = property(fset = _set, doc = _set.__doc__)
##

ICheckIn._methods_ = [
    COMMETHOD([helpstring(u'Checks in changes from a check-out database.')], HRESULT, 'CheckInFromGDB',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceName), 'parentDB' ),
              ( ['in'], BSTR, 'checkoutName' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceName), 'checkOutDB' ),
              ( ['in'], VARIANT_BOOL, 'reconcileCheckout' ),
              ( ['in'], VARIANT_BOOL, 'createOIDMappingTable' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'conflicts_detected' )),
    COMMETHOD([helpstring(u'Checks in changes from a delta database.')], HRESULT, 'CheckInFromDeltaFile',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceName), 'parentDB' ),
              ( ['in'], BSTR, 'checkoutName' ),
              ( ['in'], BSTR, 'fileName' ),
              ( ['in'], esriExportDataChangesOption, 'dcOption' ),
              ( ['in'], VARIANT_BOOL, 'reconcileCheckout' ),
              ( ['in'], VARIANT_BOOL, 'createOIDMappingTable' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'conflicts_detected' )),
]
################################################################
## code template for ICheckIn implementation
##class ICheckIn_Impl(object):
##    def CheckInFromDeltaFile(self, parentDB, checkoutName, fileName, dcOption, reconcileCheckout, createOIDMappingTable):
##        u'Checks in changes from a delta database.'
##        #return conflicts_detected
##
##    def CheckInFromGDB(self, parentDB, checkoutName, checkOutDB, reconcileCheckout, createOIDMappingTable):
##        u'Checks in changes from a check-out database.'
##        #return conflicts_detected
##

class ReplicaSchemaExporter(CoClass):
    u'Esri Replica Schema Exporter object.'
    _reg_clsid_ = GUID('{B3C4FBD5-E496-479A-B567-5B2D3E5790EA}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{A7C74158-1062-4664-B404-8694D490FCD1}', 10, 2)
class IExportSchema(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that export schema from a replica.'
    _iid_ = GUID('{BFD3912E-421E-477B-B324-5E66C552AC1B}')
    _idlflags_ = ['oleautomation']
ReplicaSchemaExporter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IExportSchema]

class IEnumTableDataChanges(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the TablesDataChanges objects.'
    _iid_ = GUID('{B2573E22-0229-4F28-B33E-85573F974240}')
    _idlflags_ = ['oleautomation']
class ITableDataChangesInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that initialize a TableDataChanges object.'
    _iid_ = GUID('{387ADB2E-328B-464D-B6D6-548D0FD4447D}')
    _idlflags_ = ['oleautomation']
IEnumTableDataChanges._methods_ = [
    COMMETHOD([helpstring(u'The next table data changes in the enumeration.')], HRESULT, 'Next',
              ( ['retval', 'out'], POINTER(POINTER(ITableDataChangesInfo)), 'TableDataChanges' )),
    COMMETHOD([helpstring(u'Reset the enumeration.')], HRESULT, 'Reset'),
]
################################################################
## code template for IEnumTableDataChanges implementation
##class IEnumTableDataChanges_Impl(object):
##    def Reset(self):
##        u'Reset the enumeration.'
##        #return 
##
##    def Next(self):
##        u'The next table data changes in the enumeration.'
##        #return TableDataChanges
##

class IGDSData2(IGDSData):
    _case_insensitive_ = True
    u'Provides access to methods supported by a GDSReplicaData object.'
    _iid_ = GUID('{74A172D5-7D99-41E1-9840-415193B5F58C}')
    _idlflags_ = ['oleautomation']
IGDSData2._methods_ = [
    COMMETHOD(['propget', helpstring(u'The ID of the uploaded data.')], HRESULT, 'UploadID',
              ( ['retval', 'out'], POINTER(BSTR), 'UploadID' )),
    COMMETHOD(['propput', helpstring(u'The ID of the uploaded data.')], HRESULT, 'UploadID',
              ( ['in'], BSTR, 'UploadID' )),
]
################################################################
## code template for IGDSData2 implementation
##class IGDSData2_Impl(object):
##    def _get(self):
##        u'The ID of the uploaded data.'
##        #return UploadID
##    def _set(self, UploadID):
##        u'The ID of the uploaded data.'
##    UploadID = property(_get, _set, doc = _set.__doc__)
##


# values for enumeration 'esriGeoDataServerMessageCodeEnum'
esriGeoDataServerMessageCode_NotLicensed = 90000
esriGeoDataServerMessageCode_ConstructStart = 90001
esriGeoDataServerMessageCode_ConstructFinish = 90002
esriGeoDataServerMessageCode_ErrorInvalidConfiguration = 90003
esriGeoDataServerMessageCode_ErrorUnableToInitFromGdb = 90004
esriGeoDataServerMessageCode_ConnectedToWS = 90005
esriGeoDataServerMessageCode_RequestNotSupported = 90006
esriGeoDataServerMessageCode_CapabilityNotSupported = 90007
esriGeoDataServerMessageCode_InitFromMapStarts = 90008
esriGeoDataServerMessageCode_InitFromMapEnded = 90009
esriGeoDataServerMessageCode_ErrorInvalidOutputDir = 90010
esriGeoDataServerMessageCode_ErrorInvalidVirtualDir = 90011
esriGeoDataServerMessageCode_ErrorMessage = 90012
esriGeoDataServerMessageCode_WarningMessage = 90013
esriGeoDataServerMessageCode_InfoMessage = 90014
esriGeoDataServerMessageCode_DebugMessage = 90015
esriGeoDataServerMessageCodeEnum = c_int # enum
class IDeltaDataChangesInit2(IDeltaDataChangesInit):
    _case_insensitive_ = True
    u'Provides access to members that initialize a DeltaDataChanges object with the ability to access its file content randomly.'
    _iid_ = GUID('{4C7FD0CF-FA09-4D49-B168-4767CF945C14}')
    _idlflags_ = ['oleautomation']
IDeltaDataChangesInit2._methods_ = [
    COMMETHOD([helpstring(u'Initializes the class by setting delta database file name, export option, and the ability to access the file content randomly.')], HRESULT, 'Init2',
              ( ['in'], BSTR, 'changesFileName' ),
              ( ['in'], esriExportDataChangesOption, 'exportOption' ),
              ( ['in'], VARIANT_BOOL, 'RandomAccess' )),
]
################################################################
## code template for IDeltaDataChangesInit2 implementation
##class IDeltaDataChangesInit2_Impl(object):
##    def Init2(self, changesFileName, exportOption, RandomAccess):
##        u'Initializes the class by setting delta database file name, export option, and the ability to access the file content randomly.'
##        #return 
##

class IVersionDataChangesInit(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that initialize a VersionDataChanges object.'
    _iid_ = GUID('{51DDD7AC-B00B-420A-ADB9-30540C7E81D4}')
    _idlflags_ = ['oleautomation']
IVersionDataChangesInit._methods_ = [
    COMMETHOD([helpstring(u'Initializes the class by setting the versioned workspace and one of its ancestor versioned workspace.')], HRESULT, 'Init',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceName), 'SourceVersionedWorkspace' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceName), 'TargetVersionedWorkspace' )),
]
################################################################
## code template for IVersionDataChangesInit implementation
##class IVersionDataChangesInit_Impl(object):
##    def Init(self, SourceVersionedWorkspace, TargetVersionedWorkspace):
##        u'Initializes the class by setting the versioned workspace and one of its ancestor versioned workspace.'
##        #return 
##


# values for enumeration 'esriGDSExportFormat'
esriGDSExportFormatPersonalGdb = 0
esriGDSExportFormatXml = 1
esriGDSExportFormatFileGDB = 2
esriGDSExportFormatFileGDBTransport = 3
esriGDSExportFormatSqliteGDB = 4
esriGDSExportFormat = c_int # enum
IGDSExportOptions._methods_ = [
    COMMETHOD(['propget', helpstring(u'The format to export to.')], HRESULT, 'ExportFormat',
              ( ['retval', 'out'], POINTER(esriGDSExportFormat), 'ExportFormat' )),
    COMMETHOD(['propput', helpstring(u'The format to export to.')], HRESULT, 'ExportFormat',
              ( ['in'], esriGDSExportFormat, 'ExportFormat' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the data should be compressed.')], HRESULT, 'Compressed',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'comp' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether the data should be compressed.')], HRESULT, 'Compressed',
              ( ['in'], VARIANT_BOOL, 'comp' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the geometry should be exported in binary format (valid for XML export).')], HRESULT, 'BinaryGeometry',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'BinaryGeometry' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the geometry should be exported in binary format (valid for XML export).')], HRESULT, 'BinaryGeometry',
              ( ['in'], VARIANT_BOOL, 'BinaryGeometry' )),
]
################################################################
## code template for IGDSExportOptions implementation
##class IGDSExportOptions_Impl(object):
##    def _get(self):
##        u'The format to export to.'
##        #return ExportFormat
##    def _set(self, ExportFormat):
##        u'The format to export to.'
##    ExportFormat = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether the data should be compressed.'
##        #return comp
##    def _set(self, comp):
##        u'Indicates whether the data should be compressed.'
##    Compressed = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the geometry should be exported in binary format (valid for XML export).'
##        #return BinaryGeometry
##    def _set(self, BinaryGeometry):
##        u'Indicates if the geometry should be exported in binary format (valid for XML export).'
##    BinaryGeometry = property(_get, _set, doc = _set.__doc__)
##

class ReplicaValidator(CoClass):
    u'Validates a check-out with the master geodatabase.'
    _reg_clsid_ = GUID('{FD8C8ADE-6425-474E-AE33-70D3F098077A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{A7C74158-1062-4664-B404-8694D490FCD1}', 10, 2)
class IReplicaValidation(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that validate a check-out.'
    _iid_ = GUID('{059A0B29-8D46-475F-A4D8-77F220EC2CBB}')
    _idlflags_ = ['oleautomation']
class IReplicaValidation2(IReplicaValidation):
    _case_insensitive_ = True
    u'Provides access to members that validate a replica.'
    _iid_ = GUID('{90B7C766-754E-47E9-BC42-7C03A336C82F}')
    _idlflags_ = ['oleautomation']
ReplicaValidator._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IReplicaValidation, IReplicaValidation2]

class DataChanges(CoClass):
    u'The edits in check-outs, modified rows in versions or edits in a delta file.'
    _reg_clsid_ = GUID('{A1CB6E77-022B-4886-A41A-7F97AA08A722}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{A7C74158-1062-4664-B404-8694D490FCD1}', 10, 2)
class IDataChanges(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that return information needed to check in or import edits.'
    _iid_ = GUID('{E0951743-0D52-42FF-AB5E-32D07B5B8951}')
    _idlflags_ = ['oleautomation']
DataChanges._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDataChanges]

IGDSQueryResultPortion._methods_ = [
    COMMETHOD(['propget', helpstring(u'The records corresponding to the query result portion.')], HRESULT, 'Records',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRecordSet)), 'recordSet' )),
    COMMETHOD(['propputref', helpstring(u'The records corresponding to the query result portion.')], HRESULT, 'Records',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IRecordSet), 'recordSet' )),
]
################################################################
## code template for IGDSQueryResultPortion implementation
##class IGDSQueryResultPortion_Impl(object):
##    def Records(self, recordSet):
##        u'The records corresponding to the query result portion.'
##        #return 
##

class CheckOutDataChanges(CoClass):
    u'The information needed to perform a check in from a check-out database.'
    _reg_clsid_ = GUID('{9FE24070-7DF5-4F93-A52D-EB32BCB8BF88}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{A7C74158-1062-4664-B404-8694D490FCD1}', 10, 2)
class IDataChanges2(IDataChanges):
    _case_insensitive_ = True
    u'Provides access to return the model type of the edits in the check-out.'
    _iid_ = GUID('{5F8F332E-316D-4FC0-9454-B2628CB9D546}')
    _idlflags_ = ['oleautomation']
class IReplicaDataChanges(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that identify a data changes object based on a replica.'
    _iid_ = GUID('{8612B096-C19B-4197-80AC-86961AC9426C}')
    _idlflags_ = ['oleautomation']
class IReplicaDataChangesInit(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that initialize a Replica DataChanges object.'
    _iid_ = GUID('{E513366A-6FE2-42D4-AC95-40DEC7122F57}')
    _idlflags_ = ['oleautomation']
CheckOutDataChanges._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDataChanges, IDataChanges2, IReplicaDataChanges, IReplicaDataChangesInit]

class GeoDataServer(CoClass):
    u'The GeoDataServer component provides programmatic access to a geodatabase.'
    _reg_clsid_ = GUID('{A61F2A53-878A-4703-AB50-50FC0B8FEEEF}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{A7C74158-1062-4664-B404-8694D490FCD1}', 10, 2)
class IGeoDataServerObjects(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to fine grained objects that are part of a GeoDataServer.'
    _iid_ = GUID('{F3B8E8CA-FDCC-4F3B-A581-AB11258CB801}')
    _idlflags_ = ['oleautomation']
GeoDataServer._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGeoDataServer, IGeoDataServer2, IGeoDataServerInit, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IObjectConstruct, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IRequestHandler, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IRequestHandler2, IGeoDataServerObjects, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IObjectActivate, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILogSupport, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo, comtypes.gen._18F2FC71_6B30_45B9_B101_037A8B868B66_0_10_2.IServerObject, comtypes.gen._18F2FC71_6B30_45B9_B101_037A8B868B66_0_10_2.IServerObjectExtensionManager, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IRESTRequestHandler]

class DeltaDataChanges(CoClass):
    u'The information needed to check in from a delta file or import edits from a delta file.'
    _reg_clsid_ = GUID('{50FFE4DC-0E25-4D5B-9BDF-D6A2B3169CA6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{A7C74158-1062-4664-B404-8694D490FCD1}', 10, 2)
class IDeltaDataChanges(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that identify a data changes object based on a delta container.'
    _iid_ = GUID('{A598405F-8302-42B8-A6A2-121CBB2B3E0A}')
    _idlflags_ = ['oleautomation']
class IDeltaDataChanges2(IDeltaDataChanges):
    _case_insensitive_ = True
    u'Provides access to members that identify a data changes object based on a delta container.'
    _iid_ = GUID('{288AC87D-ED18-460B-B720-DC4D082DA610}')
    _idlflags_ = ['oleautomation']
class IDeltaDataChangesRelease(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that return the release version of the geodatabase from which the edits originated.'
    _iid_ = GUID('{CB41732D-EC82-4E84-BFC1-A9A1135B02B5}')
    _idlflags_ = ['oleautomation']
DeltaDataChanges._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDataChanges, IDataChanges2, IDeltaDataChanges, IDeltaDataChanges2, IDeltaDataChangesInit, IDeltaDataChangesInit2, IDeltaDataChangesRelease]

class IReplicaMessageHandler(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that return information about a replica data change message.'
    _iid_ = GUID('{CE6FE713-7B5A-4E27-808F-97ECFA588F2B}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriReplicaMessageType'
esriReplicaMessageTypeDC = 1
esriReplicaMessageTypeAck = 2
esriReplicaMessageTypeDCWFD = 3
esriReplicaMessageType = c_int # enum
IReplicaMessageHandler._methods_ = [
    COMMETHOD([helpstring(u'Init replica message handler.')], HRESULT, 'Init',
              ( ['in'], BSTR, 'MsgFileName' ),
              ( ['in'], esriExportDataChangesOption, 'MsgExportOption' )),
    COMMETHOD(['propget', helpstring(u'Replica guid.')], HRESULT, 'ReplicaGuid',
              ( ['retval', 'out'], POINTER(BSTR), 'GUID' )),
    COMMETHOD(['propget', helpstring(u'Replica message type.')], HRESULT, 'MessageType',
              ( ['retval', 'out'], POINTER(esriReplicaMessageType), 'MsgType' )),
    COMMETHOD(['propget', helpstring(u'Replica generation number.')], HRESULT, 'MyGenerationNumber',
              ( ['retval', 'out'], POINTER(c_int), 'GenerationNumber' )),
    COMMETHOD(['propget', helpstring(u'Replica sibling generation number.')], HRESULT, 'SibGenerationNumber',
              ( ['retval', 'out'], POINTER(c_int), 'SibGen' )),
    COMMETHOD(['propget', helpstring(u'Delta data changes.')], HRESULT, 'DeltaDataChanges',
              ( ['retval', 'out'], POINTER(POINTER(IDeltaDataChanges)), 'DeltaDC' )),
]
################################################################
## code template for IReplicaMessageHandler implementation
##class IReplicaMessageHandler_Impl(object):
##    @property
##    def ReplicaGuid(self):
##        u'Replica guid.'
##        #return GUID
##
##    @property
##    def SibGenerationNumber(self):
##        u'Replica sibling generation number.'
##        #return SibGen
##
##    @property
##    def MessageType(self):
##        u'Replica message type.'
##        #return MsgType
##
##    @property
##    def DeltaDataChanges(self):
##        u'Delta data changes.'
##        #return DeltaDC
##
##    def Init(self, MsgFileName, MsgExportOption):
##        u'Init replica message handler.'
##        #return 
##
##    @property
##    def MyGenerationNumber(self):
##        u'Replica generation number.'
##        #return GenerationNumber
##


# values for enumeration 'esriDisconnectedEditingError'
S_DE_OK = 0
E_CHECK_OUT_NON_VERSIONED_DATA = -2147219455
E_CHECK_IN_INVALID_GEODATABASE = -2147219454
E_GEODATABASE_HAS_CHECK_OUT = -2147219453
E_INVALID_REPLICA_DESCRIPTION = -2147219452
E_CHECK_OUT_NOT_SUPPORTED_IN_RELEASE = -2147219451
E_CHECK_IN_NOT_SUPPORTED_IN_RELEASE = -2147219450
E_CAN_NOT_REUSE_SCHEMA_OF_VERSIONED_DATA = -2147219449
E_CHECK_OUT_INVALID_DATA = -2147219448
E_CAN_NOT_REUSE_SCHEMA_WITH_OUTPUT_SPATIAL_REFERENCE = -2147219447
E_CHECK_OUT_UNREGISTER_FAILED = -2147219446
E_CHECK_OUT_INVALID_SOURCE_WORKSPACE = -2147219445
E_SYNCHRONIZE_INVALID_RELEASES = -2147219444
E_UPDATEGRAM_TOPOLOGY_DEFINITION_ACCESSING = -2147219443
esriDisconnectedEditingError = c_int # enum

# values for enumeration 'esriGeoDataServerErrors'
GDS_E_IMPORTXMLWS_CONFLICTS_FOUND = -2147208551
GDS_E_CANTEXPORT_TO_NONCOMPRESSED_FILEGDB = -2147208550
GDS_E_REQUESTEDCOUNT_TOO_LARGE = -2147208549
GDS_E_INVALID_FORMAT_FOR_CREATEREPLICA = -2147208548
GDS_E_MISSING_PARAMETER = -2147208547
GDS_E_CANTIMPORT_ACKMSG_AS_DATACHANGESMSG = -2147208546
GDS_E_INVALID_COUNT_REQUESTED = -2147208545
GDS_E_INVALID_START_INDEX = -2147208544
GDS_E_NULL_QUERYID = -2147208543
GDS_E_INVALID_RECONCILE_POLICY_FOR_DIRECTION = -2147208542
GDS_E_REPLICAS_DONT_MATCH = -2147208541
GDS_E_SYNCH_DIRECTION_BOTH_INVALID_FOR_CHECKOUTS = -2147208540
GDS_E_IMPORTDATAWS_CONFLICTS_FOUND = -2147208539
esriGeoDataServerErrors = c_int # enum
class IReplicationAgentCancelControl(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods that control how cancellation of methods in the replication agent.'
    _iid_ = GUID('{FE61BEF1-7AE3-45C6-84DE-A9D6019A4D77}')
    _idlflags_ = ['oleautomation']
IReplicationAgentCancelControl._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The cancel tracker to inspect for user cancellations.')], HRESULT, 'CancelTracker',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ITrackCancel), 'rhs' )),
]
################################################################
## code template for IReplicationAgentCancelControl implementation
##class IReplicationAgentCancelControl_Impl(object):
##    def CancelTracker(self, rhs):
##        u'The cancel tracker to inspect for user cancellations.'
##        #return 
##

class DataExtraction(CoClass):
    u'Extracts data from one geodatabase to another geodatabase.'
    _reg_clsid_ = GUID('{8BA238F5-AA25-423B-9C59-4AB4988E8BC6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{A7C74158-1062-4664-B404-8694D490FCD1}', 10, 2)
class IDataExtraction(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that extract schema and/or data from one geodatabase to another geodatabase.'
    _iid_ = GUID('{CF7E4CF0-E0C0-4302-AB42-C32899835602}')
    _idlflags_ = ['oleautomation']
class IXMLDocumentVersion(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the version of the XML documents being generated.'
    _iid_ = GUID('{80EFFD28-C665-47D2-AA21-C4196EFCC9D3}')
    _idlflags_ = ['oleautomation']
DataExtraction._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDataExtraction, IXMLDocumentVersion]
DataExtraction._outgoing_interfaces_ = [comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureProgress, IReplicaProgress]

class GdbImporter(CoClass):
    u'Esri Geodatabase Importer object.'
    _reg_clsid_ = GUID('{109CA64F-DE77-46F0-9D73-720BFF4111A3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{A7C74158-1062-4664-B404-8694D490FCD1}', 10, 2)
class IGdbXmlImport(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that support importing a geodatabase from XML.'
    _iid_ = GUID('{56CB26FB-6ABF-4EB7-9F39-9EC7248C0873}')
    _idlflags_ = ['oleautomation']
class IOperationProgress(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that monitor the progress of an operation such as exporting geodatabase to XML.'
    _iid_ = GUID('{7E1F4A6F-A857-475F-82EA-A089122DBDD4}')
    _idlflags_ = ['oleautomation']
GdbImporter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGdbXmlImport, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]
GdbImporter._outgoing_interfaces_ = [comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureProgress, IOperationProgress]

class ReplicasExporter(CoClass):
    u'Esri Replicas Exporter object.'
    _reg_clsid_ = GUID('{6E482C9F-8BBB-4832-9576-EBDE86F32CA0}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{A7C74158-1062-4664-B404-8694D490FCD1}', 10, 2)
class IReplicasExporter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to export replicas description in a geodatabase.'
    _iid_ = GUID('{28C7AF79-0A93-4ED1-832B-D1E1AEC0FF75}')
    _idlflags_ = ['oleautomation']
ReplicasExporter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IReplicasExporter]

class IReplicationAgent(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to replica operations.'
    _iid_ = GUID('{AB9F2C3D-9298-480B-A57C-4AFCC8D7C498}')
    _idlflags_ = ['oleautomation']
class IReplicationAgent2(IReplicationAgent):
    _case_insensitive_ = True
    u'Provides access to replica operations.'
    _iid_ = GUID('{FC1D0CBB-38EE-44B7-BE6E-80049E06F855}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriReplicaSynchronizeDirection'
esriReplicaSynchronizeFromReplica1ToReplica2 = 1
esriReplicaSynchronizeFromReplica2ToReplica1 = 2
esriReplicaSynchronizeBoth = 3
esriReplicaSynchronizeDirection = c_int # enum
IReplicationAgent._methods_ = [
    COMMETHOD([helpstring(u'Creates a replica pair in the workspaces bound to the input geodataservers.')], HRESULT, 'CreateReplica',
              ( ['in'], BSTR, 'versionName' ),
              ( ['in'], POINTER(IGeoDataServer), 'srcGDS' ),
              ( ['in'], POINTER(IGeoDataServer), 'destGDS' ),
              ( ['in'], BSTR, 'ReplicaName' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPReplicaDescription), 'desc' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPReplicaOptions), 'repOptions' )),
    COMMETHOD([helpstring(u'Synchronizes a replica pair.')], HRESULT, 'SynchronizeReplica',
              ( ['in'], POINTER(IGeoDataServer), 'gds1' ),
              ( ['in'], POINTER(IGeoDataServer), 'gds2' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPReplica), 'rep1' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPReplica), 'rep2' ),
              ( ['in'], esriReplicationAgentReconcilePolicy, 'pol' ),
              ( ['in'], esriReplicaSynchronizeDirection, 'dir' ),
              ( ['in'], VARIANT_BOOL, 'columnLevel' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'conflictsDetected' )),
    COMMETHOD([helpstring(u'Extracts data from the source geodata server into the destination geodata server.')], HRESULT, 'ExtractData',
              ( ['in'], BSTR, 'versionName' ),
              ( ['in'], POINTER(IGeoDataServer), 'srcGDS' ),
              ( ['in'], POINTER(IGeoDataServer), 'destGDS' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPReplicaDescription), 'desc' )),
]
################################################################
## code template for IReplicationAgent implementation
##class IReplicationAgent_Impl(object):
##    def SynchronizeReplica(self, gds1, gds2, rep1, rep2, pol, dir, columnLevel):
##        u'Synchronizes a replica pair.'
##        #return conflictsDetected
##
##    def ExtractData(self, versionName, srcGDS, destGDS, desc):
##        u'Extracts data from the source geodata server into the destination geodata server.'
##        #return 
##
##    def CreateReplica(self, versionName, srcGDS, destGDS, ReplicaName, desc, repOptions):
##        u'Creates a replica pair in the workspaces bound to the input geodataservers.'
##        #return 
##

IReplicationAgent2._methods_ = [
    COMMETHOD([helpstring(u'Creates a replica pair and optionally layers in the workspaces bound to the input geodataservers.')], HRESULT, 'CreateReplica2',
              ( ['in'], BSTR, 'versionName' ),
              ( ['in'], POINTER(IGeoDataServer), 'srcGDS' ),
              ( ['in'], POINTER(IGeoDataServer), 'destGDS' ),
              ( ['in'], BSTR, 'ReplicaName' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPReplicaDescription), 'desc' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPReplicaOptions), 'repOptions' ),
              ( ['in'], BSTR, 'layersFolder' )),
]
################################################################
## code template for IReplicationAgent2 implementation
##class IReplicationAgent2_Impl(object):
##    def CreateReplica2(self, versionName, srcGDS, destGDS, ReplicaName, desc, repOptions, layersFolder):
##        u'Creates a replica pair and optionally layers in the workspaces bound to the input geodataservers.'
##        #return 
##

class GdbExporter(CoClass):
    u'Esri Geodatabase Exporter object.'
    _reg_clsid_ = GUID('{1143EDD2-A736-4129-8345-E237F7BC1B19}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{A7C74158-1062-4664-B404-8694D490FCD1}', 10, 2)
class IGdbXmlExport(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that support exporting a geodatabase to XML.'
    _iid_ = GUID('{1F88E412-18CE-4324-A1E5-D1A32D5DFF4A}')
    _idlflags_ = ['oleautomation']
class IGdbXmlExportEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to callback events when exporting geodatabase to XML.'
    _iid_ = GUID('{17CE60D7-24F8-49CC-8FC4-94471DBAF723}')
    _idlflags_ = ['oleautomation']
GdbExporter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGdbXmlExport, IXMLDocumentVersion]
GdbExporter._outgoing_interfaces_ = [comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureProgress, IOperationProgress, IGdbXmlExportEvents]

class GdbSchemaCreator(CoClass):
    u'Esri Geodatabase Schema Creator object.'
    _reg_clsid_ = GUID('{3705E682-7E35-4A8D-B4B0-02A8E768C632}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{A7C74158-1062-4664-B404-8694D490FCD1}', 10, 2)
class IGdbSchemaCreator(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that support geodatabase schema creation.'
    _iid_ = GUID('{077F55BF-9A00-44B3-9D6F-5E1D0FC822E7}')
    _idlflags_ = ['oleautomation']
GdbSchemaCreator._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGdbSchemaCreator, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo]

class VersionDataChanges(CoClass):
    u'The information needed to export modified rows in versions to a delta file.'
    _reg_clsid_ = GUID('{C20CF99C-7021-496B-A0C5-34AFC905E5B8}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{A7C74158-1062-4664-B404-8694D490FCD1}', 10, 2)
class IDataChangesInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the set of changed IDs for a class.'
    _iid_ = GUID('{BF34062D-82CB-47DB-BE39-8C8902E8A05A}')
    _idlflags_ = ['oleautomation']
VersionDataChanges._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDataChanges, IVersionDataChangesInit, IDataChangesInfo]

class SchemaChangeInfo(CoClass):
    u'Esri Schema Change Info object.'
    _reg_clsid_ = GUID('{26C46E0A-FEA6-498D-AED9-ED0A3EB53CFD}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{A7C74158-1062-4664-B404-8694D490FCD1}', 10, 2)
SchemaChangeInfo._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ISchemaChangeInfo, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLVersionSupport]

IImportDataChanges._methods_ = [
    COMMETHOD([helpstring(u'Imports data.')], HRESULT, 'ImportDataChanges',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceName), 'WorkspaceName' ),
              ( ['in'], POINTER(IDeltaDataChanges), 'DeltaDataChanges' ),
              ( ['in'], VARIANT_BOOL, 'ReconcileWithParent' ),
              ( ['in'], VARIANT_BOOL, 'acceptDefaultConflictResolution' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pConflictDetected' )),
]
################################################################
## code template for IImportDataChanges implementation
##class IImportDataChanges_Impl(object):
##    def ImportDataChanges(self, WorkspaceName, DeltaDataChanges, ReconcileWithParent, acceptDefaultConflictResolution):
##        u'Imports data.'
##        #return pConflictDetected
##

IReplicaDataChangesInit._methods_ = [
    COMMETHOD([helpstring(u'Initializes the class by using the replica and the replica workspace.')], HRESULT, 'Init',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IReplica), 'Replica' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceName), 'checkoutWorkspace' )),
]
################################################################
## code template for IReplicaDataChangesInit implementation
##class IReplicaDataChangesInit_Impl(object):
##    def Init(self, Replica, checkoutWorkspace):
##        u'Initializes the class by using the replica and the replica workspace.'
##        #return 
##

class TableDataChangesInfo(CoClass):
    u'The information needed to export changes.'
    _reg_clsid_ = GUID('{E7F8C959-E5D8-453D-AF20-28C609CCC27D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{A7C74158-1062-4664-B404-8694D490FCD1}', 10, 2)
TableDataChangesInfo._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ITableDataChangesInfo]

class IReplicaMessageHandler2(IReplicaMessageHandler):
    _case_insensitive_ = True
    _iid_ = GUID('{37D98D2A-97E0-4252-86AC-AF3395581877}')
    _idlflags_ = ['oleautomation']
IReplicaMessageHandler2._methods_ = [
    COMMETHOD(['propget', helpstring(u'Replica myTime.')], HRESULT, 'MyTime',
              ( ['retval', 'out'], POINTER(VARIANT), 'MyTime' )),
    COMMETHOD(['propget', helpstring(u'Replica sibTime.')], HRESULT, 'SibTime',
              ( ['retval', 'out'], POINTER(VARIANT), 'SibTime' )),
    COMMETHOD(['propget', helpstring(u'Replica sibMyTime.')], HRESULT, 'SibMyTime',
              ( ['retval', 'out'], POINTER(VARIANT), 'SibMyTime' )),
]
################################################################
## code template for IReplicaMessageHandler2 implementation
##class IReplicaMessageHandler2_Impl(object):
##    @property
##    def SibTime(self):
##        u'Replica sibTime.'
##        #return SibTime
##
##    @property
##    def SibMyTime(self):
##        u'Replica sibMyTime.'
##        #return SibMyTime
##
##    @property
##    def MyTime(self):
##        u'Replica myTime.'
##        #return MyTime
##

class TablesDataChanges(CoClass):
    u'The information needed to export changes.'
    _reg_clsid_ = GUID('{8BB5759A-EF1F-4119-8EB4-89524ACA69E0}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{A7C74158-1062-4664-B404-8694D490FCD1}', 10, 2)
class ITablesDataChanges(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that initialize a TablesDataChanges object.'
    _iid_ = GUID('{244F9CD3-873D-42AF-88A9-3F740079D4F9}')
    _idlflags_ = ['oleautomation']
TablesDataChanges._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDataChanges, IDataChanges2, ITablesDataChanges, IEnumTableDataChanges]

class Library(object):
    u'Esri GeoDatabaseDistributed Object Library 10.2'
    name = u'esriGeoDatabaseDistributed'
    _reg_typelib_ = ('{A7C74158-1062-4664-B404-8694D490FCD1}', 10, 2)

IGdbXmlImport._methods_ = [
    COMMETHOD([helpstring(u'Generate a list of objects to import.')], HRESULT, 'GenerateNameMapping',
              ( ['in'], BSTR, 'inFile' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspace), 'Workspace' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IEnumNameMapping)), 'EnumNameMapping' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'HasConflict' )),
    COMMETHOD([helpstring(u'Imports a workspace from XML.')], HRESULT, 'ImportWorkspace',
              ( ['in'], BSTR, 'inFile' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IEnumNameMapping), 'EnumNameMapping' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspace), 'pWorkspace' ),
              ( ['in'], VARIANT_BOOL, 'schemaOnly' )),
    COMMETHOD([helpstring(u'Loading data from xml recordset.')], HRESULT, 'ImportRecordSet',
              ( ['in'], BSTR, 'inFile' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFields), 'SourceFields' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFields), 'TargetMappedFields' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable), 'pTable' )),
    COMMETHOD([helpstring(u'Generate a fieldset to load from xml.')], HRESULT, 'GetRecordSetFields',
              ( ['in'], BSTR, 'inFile' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFields)), 'Fields' )),
]
################################################################
## code template for IGdbXmlImport implementation
##class IGdbXmlImport_Impl(object):
##    def GetRecordSetFields(self, inFile):
##        u'Generate a fieldset to load from xml.'
##        #return Fields
##
##    def ImportRecordSet(self, inFile, SourceFields, TargetMappedFields, pTable):
##        u'Loading data from xml recordset.'
##        #return 
##
##    def GenerateNameMapping(self, inFile, Workspace):
##        u'Generate a list of objects to import.'
##        #return EnumNameMapping, HasConflict
##
##    def ImportWorkspace(self, inFile, EnumNameMapping, pWorkspace, schemaOnly):
##        u'Imports a workspace from XML.'
##        #return 
##

class OperationProgress(CoClass):
    u'Helper coclass for working with the nondefault outbound IOperationProgress interface in VB.'
    _reg_clsid_ = GUID('{06C8603D-2650-4888-B60B-258D09A46CA4}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{A7C74158-1062-4664-B404-8694D490FCD1}', 10, 2)
OperationProgress._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown]
OperationProgress._outgoing_interfaces_ = [IOperationProgress]

class GDSQueryResultPortion(CoClass):
    u'An object used to return results of queries made against a GeoDataServer.'
    _reg_clsid_ = GUID('{A53BEA9A-142F-4AA7-82EE-F8C3F7ED9F1B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{A7C74158-1062-4664-B404-8694D490FCD1}', 10, 2)
GDSQueryResultPortion._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGDSQueryResultPortion, comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IResultPortion, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLVersionSupport]

class GDSExportOptions(CoClass):
    u'An object used to specify GeoDataServer export options.'
    _reg_clsid_ = GUID('{14B1AA05-52E9-4A46-8E1F-901DA5A9A4F7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{A7C74158-1062-4664-B404-8694D490FCD1}', 10, 2)
GDSExportOptions._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGDSExportOptions, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLVersionSupport]

class GDSData(CoClass):
    u'An object that transports GeoDataServer data.'
    _reg_clsid_ = GUID('{8B77E69C-2A95-42E3-88E3-22A612B69752}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{A7C74158-1062-4664-B404-8694D490FCD1}', 10, 2)
GDSData._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGDSData, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLSerialize, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersistStream, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPersist, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IClone, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLVersionSupport]

class IDataChanges3(IDataChanges2):
    _case_insensitive_ = True
    u'Provides access to members that get data changes from a check-out or replica.'
    _iid_ = GUID('{A289BD00-E42E-4820-9AF0-C9BC64F707A8}')
    _idlflags_ = ['oleautomation']
class IEnumModifiedClassInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that enumerate modified classes with edits to check in or import.'
    _iid_ = GUID('{B3924A28-0D3A-47C6-9D63-71544F1634DA}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriDataChangeType'
esriDataChangeTypeInsert = 0
esriDataChangeTypeUpdate = 1
esriDataChangeTypeDelete = 2
esriDataChangeType = c_int # enum
IDataChanges._methods_ = [
    COMMETHOD([helpstring(u'Returns an enumeration listing of the feature classes and tables with edits.')], HRESULT, 'GetModifiedClassesInfo',
              ( ['retval', 'out'], POINTER(POINTER(IEnumModifiedClassInfo)), 'enumModifiedClasses' )),
    COMMETHOD([helpstring(u'Lists the edits in each feature class or table.')], HRESULT, 'Extract',
              ( ['in'], BSTR, 'tableName' ),
              ( ['in'], esriDataChangeType, 'changeType' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IDifferenceCursor)), 'cursor' )),
    COMMETHOD(['propget', helpstring(u'Workspace of the master geodatabase.')], HRESULT, 'ParentWorkspaceName',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceName)), 'ParentWorkspaceName' )),
    COMMETHOD(['propget', helpstring(u'ID for the replica in the parent geodatabase.')], HRESULT, 'ParentReplicaID',
              ( ['retval', 'out'], POINTER(c_int), 'ParentReplicaID' )),
    COMMETHOD(['propget', helpstring(u'GUID identifying the child/parent replica pair.')], HRESULT, 'ReplicaGuid',
              ( ['retval', 'out'], POINTER(BSTR), 'ReplicaGuid' )),
]
################################################################
## code template for IDataChanges implementation
##class IDataChanges_Impl(object):
##    @property
##    def ReplicaGuid(self):
##        u'GUID identifying the child/parent replica pair.'
##        #return ReplicaGuid
##
##    @property
##    def ParentWorkspaceName(self):
##        u'Workspace of the master geodatabase.'
##        #return ParentWorkspaceName
##
##    def Extract(self, tableName, changeType):
##        u'Lists the edits in each feature class or table.'
##        #return cursor
##
##    def GetModifiedClassesInfo(self):
##        u'Returns an enumeration listing of the feature classes and tables with edits.'
##        #return enumModifiedClasses
##
##    @property
##    def ParentReplicaID(self):
##        u'ID for the replica in the parent geodatabase.'
##        #return ParentReplicaID
##

IDataChanges2._methods_ = [
    COMMETHOD(['propget', helpstring(u'Geodabase model type, simple or full.')], HRESULT, 'ChangesModelType',
              ( ['retval', 'out'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriReplicaModelType), 'ModelType' )),
]
################################################################
## code template for IDataChanges2 implementation
##class IDataChanges2_Impl(object):
##    @property
##    def ChangesModelType(self):
##        u'Geodabase model type, simple or full.'
##        #return ModelType
##

IDataChanges3._methods_ = [
    COMMETHOD(['propget', helpstring(u'Source and target generation numbers for replica.')], HRESULT, 'GenerationNumbers',
              ( ['out'], POINTER(c_int), 'sourceGenBegin' ),
              ( ['out'], POINTER(c_int), 'sourceGenEnd' ),
              ( ['out'], POINTER(c_int), 'targetGen' )),
    COMMETHOD(['propget', helpstring(u'The state of the replica that is the source of the data changes.')], HRESULT, 'ReplicaState',
              ( ['retval', 'out'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriReplicaState), 'ReplicaState' )),
]
################################################################
## code template for IDataChanges3 implementation
##class IDataChanges3_Impl(object):
##    @property
##    def GenerationNumbers(self):
##        u'Source and target generation numbers for replica.'
##        #return sourceGenBegin, sourceGenEnd, targetGen
##
##    @property
##    def ReplicaState(self):
##        u'The state of the replica that is the source of the data changes.'
##        #return ReplicaState
##

class ReplicaProgress(CoClass):
    u'Helper coclass for working with the nondefault outbound IReplicaProgress interface in VB.'
    _reg_clsid_ = GUID('{CBD8CB96-30E1-4F82-8E90-885B86AA8EC9}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{A7C74158-1062-4664-B404-8694D490FCD1}', 10, 2)
ReplicaProgress._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown]
ReplicaProgress._outgoing_interfaces_ = [IReplicaProgress]

class GeoDataServerIP(CoClass):
    u'The internet proxy for the geodata server.'
    _reg_clsid_ = GUID('{74F9A30C-D127-4880-88B9-D79DE091B8A6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{A7C74158-1062-4664-B404-8694D490FCD1}', 10, 2)
GeoDataServerIP._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IAGSServerObject, comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IAGSServerObject2, IGeoDataServer, IGeoDataServer2]

ITablesDataChanges._methods_ = [
    COMMETHOD([helpstring(u'The changes model type.')], HRESULT, 'Init',
              ( ['in'], comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriReplicaModelType, 'ModelType' )),
    COMMETHOD([helpstring(u'Add table data changes.')], HRESULT, 'Add',
              ( ['in'], POINTER(ITableDataChangesInfo), 'TableDataChanges' )),
    COMMETHOD([helpstring(u'Remove table data changes.')], HRESULT, 'Remove',
              ( ['in'], BSTR, 'TargetName' )),
    COMMETHOD([helpstring(u'A TableDataChangesInfo object for the target feature class.')], HRESULT, 'FindTableChangesInfo',
              ( ['in'], BSTR, 'TargetName' ),
              ( ['retval', 'out'], POINTER(POINTER(ITableDataChangesInfo)), 'TableDataChanges' )),
    COMMETHOD(['propget', helpstring(u'The number of TableDataChangesInfo objects that have been added.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
]
################################################################
## code template for ITablesDataChanges implementation
##class ITablesDataChanges_Impl(object):
##    @property
##    def Count(self):
##        u'The number of TableDataChangesInfo objects that have been added.'
##        #return Count
##
##    def Init(self, ModelType):
##        u'The changes model type.'
##        #return 
##
##    def Add(self, TableDataChanges):
##        u'Add table data changes.'
##        #return 
##
##    def Remove(self, TargetName):
##        u'Remove table data changes.'
##        #return 
##
##    def FindTableChangesInfo(self, TargetName):
##        u'A TableDataChangesInfo object for the target feature class.'
##        #return TableDataChanges
##

class GeoDataServerConfigurationFactory(CoClass):
    u'GeoDataServer Configuration Factory Class.'
    _reg_clsid_ = GUID('{7D7DDCAA-3F9C-4290-9351-3B8EBCEF9C65}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{A7C74158-1062-4664-B404-8694D490FCD1}', 10, 2)
GeoDataServerConfigurationFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._18F2FC71_6B30_45B9_B101_037A8B868B66_0_10_2.IConfigurationFactory2, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILogSupport]

ICheckOut._methods_ = [
    COMMETHOD([helpstring(u'Checks out schema and data from a master geodatabase.')], HRESULT, 'CheckOutData',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IReplicaDescription), 'rDDescriptions' ),
              ( ['in'], VARIANT_BOOL, 'transferRelObjects' ),
              ( ['in'], BSTR, 'checkoutName' )),
    COMMETHOD([helpstring(u'Checks out only the schema of the selected datasets from a master geodatabase.')], HRESULT, 'CheckOutSchema',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IReplicaDescription), 'rDDescription' ),
              ( ['in'], BSTR, 'checkoutName' )),
]
################################################################
## code template for ICheckOut implementation
##class ICheckOut_Impl(object):
##    def CheckOutData(self, rDDescriptions, transferRelObjects, checkoutName):
##        u'Checks out schema and data from a master geodatabase.'
##        #return 
##
##    def CheckOutSchema(self, rDDescription, checkoutName):
##        u'Checks out only the schema of the selected datasets from a master geodatabase.'
##        #return 
##

class ReplicationAgent(CoClass):
    u'A class used to perform replica operations.'
    _reg_clsid_ = GUID('{F530AFCD-D953-4A5C-A00D-4F6749357F00}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{A7C74158-1062-4664-B404-8694D490FCD1}', 10, 2)
ReplicationAgent._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IReplicationAgent, IReplicationAgent2, IReplicationAgentCancelControl]
ReplicationAgent._outgoing_interfaces_ = [comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureProgress]

class ISchemaChanges(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the replica schema changes.'
    _iid_ = GUID('{D14B724A-AC95-4CD2-9242-7235F4FB5587}')
    _idlflags_ = ['oleautomation']
IExportSchema._methods_ = [
    COMMETHOD([helpstring(u'Export schema info.')], HRESULT, 'ExportSchema',
              ( ['in'], BSTR, 'exportFileName' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IReplica), 'Replica' )),
    COMMETHOD([helpstring(u'Export schema differences between replica pair.')], HRESULT, 'ExportSchemaDifferences',
              ( ['in'], BSTR, 'exportFileName' ),
              ( ['in'], POINTER(ISchemaChanges), 'SchemaChanges' )),
]
################################################################
## code template for IExportSchema implementation
##class IExportSchema_Impl(object):
##    def ExportSchemaDifferences(self, exportFileName, SchemaChanges):
##        u'Export schema differences between replica pair.'
##        #return 
##
##    def ExportSchema(self, exportFileName, Replica):
##        u'Export schema info.'
##        #return 
##


# values for enumeration 'esriCheckInSourceType'
esriPersonalDeltaFile = 1
esriXMLDeltaFile = 2
esriCheckOutGDB = 3
esriFileGDBDelta = 4
esriCheckInSourceType = c_int # enum
IReplicaValidation._methods_ = [
    COMMETHOD([helpstring(u'Indicates if the check-out in a check-out database is valid.')], HRESULT, 'ValidateReplicaPair',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceName), 'parentDB' ),
              ( ['in'], BSTR, 'ReplicaName' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceName), 'checkOutDB' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'isValid' )),
    COMMETHOD([helpstring(u'Indicates if the check-out in a delta database is valid.')], HRESULT, 'ValidateDeltaFile',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceName), 'parentDB' ),
              ( ['in'], BSTR, 'ReplicaName' ),
              ( ['in'], BSTR, 'DeltaFileName' ),
              ( ['in'], esriCheckInSourceType, 'sourceType' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'isValid' )),
]
################################################################
## code template for IReplicaValidation implementation
##class IReplicaValidation_Impl(object):
##    def ValidateReplicaPair(self, parentDB, ReplicaName, checkOutDB):
##        u'Indicates if the check-out in a check-out database is valid.'
##        #return isValid
##
##    def ValidateDeltaFile(self, parentDB, ReplicaName, DeltaFileName, sourceType):
##        u'Indicates if the check-out in a delta database is valid.'
##        #return isValid
##

IReplicaValidation2._methods_ = [
    COMMETHOD([helpstring(u'Validates a replicas schema in the geodatabase.')], HRESULT, 'ValidateReplicaSchema',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IReplica), 'Replica' )),
]
################################################################
## code template for IReplicaValidation2 implementation
##class IReplicaValidation2_Impl(object):
##    def ValidateReplicaSchema(self, Replica):
##        u'Validates a replicas schema in the geodatabase.'
##        #return 
##

IXMLDocumentVersion._methods_ = [
    COMMETHOD(['propput', helpstring(u'The namespace (version) to export to.')], HRESULT, 'NamespaceToExportTo',
              ( ['in'], BSTR, 'rhs' )),
]
################################################################
## code template for IXMLDocumentVersion implementation
##class IXMLDocumentVersion_Impl(object):
##    def _set(self, rhs):
##        u'The namespace (version) to export to.'
##    NamespaceToExportTo = property(fset = _set, doc = _set.__doc__)
##


# values for enumeration 'esriOperationProgress'
esriImportXMLWorkspace = 1
esriImportXMLWorkspaceSchema = 2
esriExtractSchema = 4
esriExtractData = 8
esriBuildGeometricNetworks = 16
esriBuildTopologies = 32
esriExportXMLWorkspace = 64
esriExportXMLWorkspaceSchema = 128
esriExportXMLWorkspaceDefinition = 256
esriExportXMLWorkspaceData = 512
esriImportXMLWorkspaceData = 1024
esriXMLRegisterReplica = 2048
esriOperationProgress = c_int # enum
IOperationProgress._methods_ = [
    COMMETHOD([helpstring(u'Initiate the operation progress utility.')], HRESULT, 'Startup',
              ( ['in'], esriOperationProgress, 'rProgress' )),
    COMMETHOD(['propput', helpstring(u'The current operation process.')], HRESULT, 'CurrentOperation',
              ( ['in'], esriOperationProgress, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'The number of operations to perform.')], HRESULT, 'Operations',
              ( ['in'], c_int, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'The number of objects in an operation.')], HRESULT, 'ObjectCount',
              ( ['in'], c_int, 'rhs' )),
]
################################################################
## code template for IOperationProgress implementation
##class IOperationProgress_Impl(object):
##    def _set(self, rhs):
##        u'The number of operations to perform.'
##    Operations = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'The number of objects in an operation.'
##    ObjectCount = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'The current operation process.'
##    CurrentOperation = property(fset = _set, doc = _set.__doc__)
##
##    def Startup(self, rProgress):
##        u'Initiate the operation progress utility.'
##        #return 
##

class ReplicaMessageHandler(CoClass):
    u'The ReplicaMessageHandler object.'
    _reg_clsid_ = GUID('{BF4E20AD-2BD9-47B2-8256-364DC4548326}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{A7C74158-1062-4664-B404-8694D490FCD1}', 10, 2)
ReplicaMessageHandler._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IReplicaMessageHandler, IReplicaMessageHandler2]

IImportDataChanges2._methods_ = [
    COMMETHOD([helpstring(u'Imports data.')], HRESULT, 'ImportDataChanges2',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceName), 'WorkspaceName' ),
              ( ['in'], POINTER(IDeltaDataChanges), 'DeltaDataChanges' ),
              ( ['in'], VARIANT_BOOL, 'ReconcileWithParent' ),
              ( ['in'], comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriReplicaReconcilePolicyType, 'reconcilePolicy' ),
              ( ['in'], VARIANT_BOOL, 'columnLevel' ),
              ( ['in'], VARIANT_BOOL, 'createOIDMappingTable' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pConflictDetected' )),
]
################################################################
## code template for IImportDataChanges2 implementation
##class IImportDataChanges2_Impl(object):
##    def ImportDataChanges2(self, WorkspaceName, DeltaDataChanges, ReconcileWithParent, reconcilePolicy, columnLevel, createOIDMappingTable):
##        u'Imports data.'
##        #return pConflictDetected
##

IDeltaDataChangesRelease._methods_ = [
    COMMETHOD(['propget', helpstring(u'Major version level of the source geodatabase.')], HRESULT, 'MajorVersion',
              ( ['retval', 'out'], POINTER(c_int), 'versionNumber' )),
    COMMETHOD(['propget', helpstring(u'Minor version level of the source geodatabase.')], HRESULT, 'MinorVersion',
              ( ['retval', 'out'], POINTER(c_int), 'versionNumber' )),
    COMMETHOD(['propget', helpstring(u'Bugfix version level of the source geodatabase.')], HRESULT, 'BugfixVersion',
              ( ['retval', 'out'], POINTER(c_int), 'versionNumber' )),
]
################################################################
## code template for IDeltaDataChangesRelease implementation
##class IDeltaDataChangesRelease_Impl(object):
##    @property
##    def BugfixVersion(self):
##        u'Bugfix version level of the source geodatabase.'
##        #return versionNumber
##
##    @property
##    def MajorVersion(self):
##        u'Major version level of the source geodatabase.'
##        #return versionNumber
##
##    @property
##    def MinorVersion(self):
##        u'Minor version level of the source geodatabase.'
##        #return versionNumber
##

IExportDataChanges._methods_ = [
    COMMETHOD([helpstring(u'Exports the edits to a delta file.')], HRESULT, 'ExportDataChanges',
              ( ['in'], BSTR, 'exportFileName' ),
              ( ['in'], esriExportDataChangesOption, 'exportOption' ),
              ( ['in'], POINTER(IDataChanges), 'DataChanges' ),
              ( ['in'], VARIANT_BOOL, 'OverwriteIfExists' )),
]
################################################################
## code template for IExportDataChanges implementation
##class IExportDataChanges_Impl(object):
##    def ExportDataChanges(self, exportFileName, exportOption, DataChanges, OverwriteIfExists):
##        u'Exports the edits to a delta file.'
##        #return 
##

IExportDataChanges2._methods_ = [
    COMMETHOD([helpstring(u'Exports the edits to a delta file.')], HRESULT, 'ExportDataChanges2',
              ( ['in'], BSTR, 'exportFileName' ),
              ( ['in'], esriExportDataChangesOption, 'exportOption' ),
              ( ['in'], POINTER(IDataChanges), 'DataChanges' ),
              ( ['in'], VARIANT_BOOL, 'OverwriteIfExists' ),
              ( ['in'], VARIANT_BOOL, 'Compressed' ),
              ( ['in'], VARIANT_BOOL, 'BinaryGeometry' ),
              ( ['in'], VARIANT_BOOL, 'LastSend' )),
    COMMETHOD([helpstring(u'Exports the edits to a delta file.')], HRESULT, 'ReExportDataChanges',
              ( ['in'], BSTR, 'exportFileName' ),
              ( ['in'], esriExportDataChangesOption, 'exportOption' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IReplica2), 'SourceReplica' ),
              ( ['in'], esriReExportGenerationsOption, 'GenOption' ),
              ( ['in'], VARIANT_BOOL, 'OverwriteIfExists' ),
              ( ['in'], VARIANT_BOOL, 'Compressed' ),
              ( ['in'], VARIANT_BOOL, 'BinaryGeometry' )),
]
################################################################
## code template for IExportDataChanges2 implementation
##class IExportDataChanges2_Impl(object):
##    def ExportDataChanges2(self, exportFileName, exportOption, DataChanges, OverwriteIfExists, Compressed, BinaryGeometry, LastSend):
##        u'Exports the edits to a delta file.'
##        #return 
##
##    def ReExportDataChanges(self, exportFileName, exportOption, SourceReplica, GenOption, OverwriteIfExists, Compressed, BinaryGeometry):
##        u'Exports the edits to a delta file.'
##        #return 
##

IGeoDataServerObjects._methods_ = [
    COMMETHOD(['propget', helpstring(u'The default working workspace for the geodata server.')], HRESULT, 'DefaultWorkingWorkspace',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspace)), 'Workspace' )),
]
################################################################
## code template for IGeoDataServerObjects implementation
##class IGeoDataServerObjects_Impl(object):
##    @property
##    def DefaultWorkingWorkspace(self):
##        u'The default working workspace for the geodata server.'
##        #return Workspace
##

IGdbSchemaCreator._methods_ = [
    COMMETHOD([helpstring(u'Generates a name mapping enumeration for the arrays of data elements and domains.')], HRESULT, 'GenerateNameMapping',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspace), 'pWorkspace' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IArray), 'pDataElements' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IArray), 'pDomains' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IEnumNameMapping)), 'ppENM' ),
              ( ['out'], POINTER(VARIANT_BOOL), 'pHasConflict' )),
    COMMETHOD([helpstring(u'Creates the schema for the data elements in the name mapping enumeration.')], HRESULT, 'CreateSchema',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspace), 'pWorkspace' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IEnumNameMapping), 'pENM' )),
]
################################################################
## code template for IGdbSchemaCreator implementation
##class IGdbSchemaCreator_Impl(object):
##    def CreateSchema(self, pWorkspace, pENM):
##        u'Creates the schema for the data elements in the name mapping enumeration.'
##        #return 
##
##    def GenerateNameMapping(self, pWorkspace, pDataElements, pDomains):
##        u'Generates a name mapping enumeration for the arrays of data elements and domains.'
##        #return ppENM, pHasConflict
##

ISchemaChanges._methods_ = [
    COMMETHOD([helpstring(u'An enumeration of the replica schema changes.')], HRESULT, 'GetChanges',
              ( ['retval', 'out'], POINTER(POINTER(IEnumSchemaChange)), 'SchemaChanges' )),
    COMMETHOD(['propget', helpstring(u'The replica thatis the source of the schema changes.')], HRESULT, 'FromReplica',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPReplica)), 'FromReplica' )),
    COMMETHOD(['propget', helpstring(u'The replica that is the target for the schema changes.')], HRESULT, 'ToReplica',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IGPReplica)), 'ToReplica' )),
]
################################################################
## code template for ISchemaChanges implementation
##class ISchemaChanges_Impl(object):
##    @property
##    def ToReplica(self):
##        u'The replica that is the target for the schema changes.'
##        #return ToReplica
##
##    def GetChanges(self):
##        u'An enumeration of the replica schema changes.'
##        #return SchemaChanges
##
##    @property
##    def FromReplica(self):
##        u'The replica thatis the source of the schema changes.'
##        #return FromReplica
##

IDataChangesInfo._methods_ = [
    COMMETHOD(['propget', helpstring(u'IDs of rows that changed between two versions.')], HRESULT, 'ChangedIDs',
              ( ['in'], BSTR, 'className' ),
              ( ['in'], esriDataChangeType, 'diffType' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFIDSet)), 'ppFIDSet' )),
]
################################################################
## code template for IDataChangesInfo implementation
##class IDataChangesInfo_Impl(object):
##    @property
##    def ChangedIDs(self, className, diffType):
##        u'IDs of rows that changed between two versions.'
##        #return ppFIDSet
##

IDataExtraction._methods_ = [
    COMMETHOD([helpstring(u'Extracts schema and data from one geodatabase to another geodatabase.')], HRESULT, 'Extract',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IReplicaDescription), 'rDDescription' ),
              ( ['in'], VARIANT_BOOL, 'transferRelObjects' )),
    COMMETHOD([helpstring(u'Extracts schema only from one geodatabase to another geodatabase.')], HRESULT, 'ExtractSchema',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IReplicaDescription), 'rSDescription' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference), 'outputSpatialReference' )),
]
################################################################
## code template for IDataExtraction implementation
##class IDataExtraction_Impl(object):
##    def ExtractSchema(self, rSDescription, outputSpatialReference):
##        u'Extracts schema only from one geodatabase to another geodatabase.'
##        #return 
##
##    def Extract(self, rDDescription, transferRelObjects):
##        u'Extracts schema and data from one geodatabase to another geodatabase.'
##        #return 
##

class IImportDataChanges3(IImportDataChanges2):
    _case_insensitive_ = True
    u'Provides access to members that import edits or check in from a delta file to a geodatabase.'
    _iid_ = GUID('{A2F2DBA2-0515-4FA3-882C-3633480BD24A}')
    _idlflags_ = ['oleautomation']
IImportDataChanges3._methods_ = [
    COMMETHOD([helpstring(u'Imports data.')], HRESULT, 'ImportDataChanges3',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceName), 'WorkspaceName' ),
              ( ['in'], POINTER(IDataChanges), 'DataChanges' ),
              ( ['in'], VARIANT_BOOL, 'ReconcileWithParent' ),
              ( ['in'], comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriReplicaReconcilePolicyType, 'reconcilePolicy' ),
              ( ['in'], VARIANT_BOOL, 'columnLevel' ),
              ( ['in'], VARIANT_BOOL, 'createOIDMappingTable' ),
              ( ['in'], VARIANT_BOOL, 'PreserveGlobalIDs' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pConflictDetected' )),
]
################################################################
## code template for IImportDataChanges3 implementation
##class IImportDataChanges3_Impl(object):
##    def ImportDataChanges3(self, WorkspaceName, DataChanges, ReconcileWithParent, reconcilePolicy, columnLevel, createOIDMappingTable, PreserveGlobalIDs):
##        u'Imports data.'
##        #return pConflictDetected
##

class GeoDataServerObjectDescription(CoClass):
    u'A class that describes the proxies for the geodata server.'
    _reg_clsid_ = GUID('{60E1A6AE-AF1B-4B41-866F-870FD2F607D9}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{A7C74158-1062-4664-B404-8694D490FCD1}', 10, 2)
GeoDataServerObjectDescription._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IServerObjectDescription]

IDeltaDataChanges._methods_ = [
    COMMETHOD(['propget', helpstring(u'The container, which can be a workspace or an XML document, in which the delta changes are stored.')], HRESULT, 'Container',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'Container' )),
]
################################################################
## code template for IDeltaDataChanges implementation
##class IDeltaDataChanges_Impl(object):
##    @property
##    def Container(self):
##        u'The container, which can be a workspace or an XML document, in which the delta changes are stored.'
##        #return Container
##

IReplicasExporter._methods_ = [
    COMMETHOD([helpstring(u'Exports the information for the replicas in a geodatabase into an output feature class.')], HRESULT, 'ExportReplicasInfo',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspace), 'pFromWS' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspace), 'pDestWS' ),
              ( ['in'], BSTR, 'fcName' ),
              ( ['in'], POINTER(comtypes.gen._C4B094C2_FF32_4FA1_ABCB_7820F8D6FB68_0_10_2.ISpatialReference), 'SR' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFeatureClass)), 'ppFC' )),
]
################################################################
## code template for IReplicasExporter implementation
##class IReplicasExporter_Impl(object):
##    def ExportReplicasInfo(self, pFromWS, pDestWS, fcName, SR):
##        u'Exports the information for the replicas in a geodatabase into an output feature class.'
##        #return ppFC
##

IReplicaDataChanges._methods_ = [
    COMMETHOD(['propget', helpstring(u'The workspace holding the replica from which the changes are being reported.')], HRESULT, 'Workspace',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspace)), 'pWorkspace' )),
]
################################################################
## code template for IReplicaDataChanges implementation
##class IReplicaDataChanges_Impl(object):
##    @property
##    def Workspace(self):
##        u'The workspace holding the replica from which the changes are being reported.'
##        #return pWorkspace
##

IDeltaDataChanges2._methods_ = [
    COMMETHOD(['propget', helpstring(u'Identifies the replica message type of the data changes object.')], HRESULT, 'ReplicaMessageType',
              ( ['retval', 'out'], POINTER(esriReplicaMessageType), 'MessageType' )),
]
################################################################
## code template for IDeltaDataChanges2 implementation
##class IDeltaDataChanges2_Impl(object):
##    @property
##    def ReplicaMessageType(self):
##        u'Identifies the replica message type of the data changes object.'
##        #return MessageType
##

class ReplicationDataChanges(CoClass):
    u'The replicadatachanges object.'
    _reg_clsid_ = GUID('{0B2A0B89-DC53-43DB-B14B-4DF0F3F5C0DE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{A7C74158-1062-4664-B404-8694D490FCD1}', 10, 2)
class IReplicaDataChangesInit2(IReplicaDataChangesInit):
    _case_insensitive_ = True
    u'Provides access to members that initialize a multi-generation Replica DataChanges object.'
    _iid_ = GUID('{92267EE9-0766-43EA-BA8B-7DFD5C8E8517}')
    _idlflags_ = ['oleautomation']
ReplicationDataChanges._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDataChanges3, IReplicaDataChangesInit, IReplicaDataChangesInit2, IReplicaDataChanges]

class IWFSServer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the available WFS Server properties and methods.'
    _iid_ = GUID('{CA2B76EB-FFE1-46D7-9E13-99A7184AB450}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriWFSHttpVerb'
esriWFSGet = 0
esriWFSPost = 1
esriWFSHttpVerb = c_int # enum
IWFSServer._methods_ = [
    COMMETHOD([helpstring(u'Handle a WFS request.')], HRESULT, 'GetData',
              ( ['in'], esriWFSHttpVerb, 'httpVerb' ),
              ( ['in'], BSTR, 'request' ),
              ( ['retval', 'out'], POINTER(BSTR), 'responseUrl' )),
    COMMETHOD([helpstring(u'Handle setting WFS Server parameter.')], HRESULT, 'SetParameter',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], BSTR, 'value' )),
]
################################################################
## code template for IWFSServer implementation
##class IWFSServer_Impl(object):
##    def SetParameter(self, Name, value):
##        u'Handle setting WFS Server parameter.'
##        #return 
##
##    def GetData(self, httpVerb, request):
##        u'Handle a WFS request.'
##        #return responseUrl
##

class IModifiedClassInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that return information about feature classes and tables with edits.'
    _iid_ = GUID('{0952A2D7-FA43-4740-AEA5-D6C902EB6A2C}')
    _idlflags_ = ['oleautomation']
IEnumModifiedClassInfo._methods_ = [
    COMMETHOD([helpstring(u'Resets the enumerator to the beginning.')], HRESULT, 'Reset'),
    COMMETHOD([helpstring(u'Returns the next object containing information about a modified class with edits to check in or import.')], HRESULT, 'Next',
              ( ['retval', 'out'], POINTER(POINTER(IModifiedClassInfo)), 'ModifiedClassInfo' )),
]
################################################################
## code template for IEnumModifiedClassInfo implementation
##class IEnumModifiedClassInfo_Impl(object):
##    def Reset(self):
##        u'Resets the enumerator to the beginning.'
##        #return 
##
##    def Next(self):
##        u'Returns the next object containing information about a modified class with edits to check in or import.'
##        #return ModifiedClassInfo
##

ITableDataChangesInfo._methods_ = [
    COMMETHOD([helpstring(u'Initializes the class by setting the inserts, updates, and deletes table.')], HRESULT, 'Init',
              ( ['in'], BSTR, 'TargetName' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable), 'Inserts' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable), 'Updates' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable), 'Deletes' )),
    COMMETHOD([helpstring(u'The filter for the inserts table.')], HRESULT, 'SetFilter',
              ( ['in'], esriDataChangeType, 'changeType' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IQueryFilter), 'Filter' )),
    COMMETHOD([helpstring(u'The filter for the inserts table.')], HRESULT, 'GetFilter',
              ( ['in'], esriDataChangeType, 'changeType' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IQueryFilter)), 'Filter' )),
    COMMETHOD(['propget', helpstring(u'The changes target name.')], HRESULT, 'TargetName',
              ( ['retval', 'out'], POINTER(BSTR), 'TargetName' )),
    COMMETHOD(['propget', helpstring(u'The insert changes table.')], HRESULT, 'Inserts',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable)), 'Table' )),
    COMMETHOD(['propget', helpstring(u'The updates changes table.')], HRESULT, 'Updates',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable)), 'Table' )),
    COMMETHOD(['propget', helpstring(u'The delete changes table.')], HRESULT, 'Deletes',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITable)), 'Deletes' )),
    COMMETHOD([helpstring(u'The deleted ids.')], HRESULT, 'SetDeletedIDs',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray), 'DeletedIDs' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray), 'DeletedGIDs' )),
    COMMETHOD([helpstring(u'The deleted ids.')], HRESULT, 'GetDeletedIDs',
              ( ['out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILongArray)), 'DeletedIDs' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'DeletedGIDs' )),
]
################################################################
## code template for ITableDataChangesInfo implementation
##class ITableDataChangesInfo_Impl(object):
##    @property
##    def Inserts(self):
##        u'The insert changes table.'
##        #return Table
##
##    def GetDeletedIDs(self):
##        u'The deleted ids.'
##        #return DeletedIDs, DeletedGIDs
##
##    def GetFilter(self, changeType):
##        u'The filter for the inserts table.'
##        #return Filter
##
##    def SetDeletedIDs(self, DeletedIDs, DeletedGIDs):
##        u'The deleted ids.'
##        #return 
##
##    def Init(self, TargetName, Inserts, Updates, Deletes):
##        u'Initializes the class by setting the inserts, updates, and deletes table.'
##        #return 
##
##    @property
##    def Updates(self):
##        u'The updates changes table.'
##        #return Table
##
##    @property
##    def Deletes(self):
##        u'The delete changes table.'
##        #return Deletes
##
##    @property
##    def TargetName(self):
##        u'The changes target name.'
##        #return TargetName
##
##    def SetFilter(self, changeType, Filter):
##        u'The filter for the inserts table.'
##        #return 
##

class GeoDataServerLP(CoClass):
    u'The lan proxy for the geodata server.'
    _reg_clsid_ = GUID('{15BCF3A2-ED45-4D22-A368-9F0123F9F8A9}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{A7C74158-1062-4664-B404-8694D490FCD1}', 10, 2)
GeoDataServerLP._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IAGSServerObject, comtypes.gen._746F6817_89BB_4490_9829_83CA25FD505A_0_10_2.IAGSServerObject2, IGeoDataServer, IGeoDataServer2]

class IDataChangesExt(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that get data changes from a check-out or replica.'
    _iid_ = GUID('{FAFBFA81-B7BD-4C25-A456-0108E11EA25B}')
    _idlflags_ = ['oleautomation']
IDataChangesExt._methods_ = [
    COMMETHOD([helpstring(u'Extract the original rows that have changes.')], HRESULT, 'ExtractOriginalRows',
              ( ['in'], BSTR, 'tableName' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IFIDSet), 'IDs' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ICursor)), 'OriginalRows' )),
]
################################################################
## code template for IDataChangesExt implementation
##class IDataChangesExt_Impl(object):
##    def ExtractOriginalRows(self, tableName, IDs):
##        u'Extract the original rows that have changes.'
##        #return OriginalRows
##

ICheckInDataSynchronizer._methods_ = [
    COMMETHOD([helpstring(u'Synchronizes the changes in the check-out geodatabase or delta database with the master geodatabase.')], HRESULT, 'Synchronize',
              ( ['in'], POINTER(IDataChanges), 'DataChanges' ),
              ( ['in'], BSTR, 'editVersionName' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceName), 'ParentWorkspace' ),
              ( ['in'], VARIANT_BOOL, 'reconcileCheckout' ),
              ( ['in'], VARIANT_BOOL, 'createOIDMappingTable' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'conflictsDetected' )),
]
################################################################
## code template for ICheckInDataSynchronizer implementation
##class ICheckInDataSynchronizer_Impl(object):
##    def Synchronize(self, DataChanges, editVersionName, ParentWorkspace, reconcileCheckout, createOIDMappingTable):
##        u'Synchronizes the changes in the check-out geodatabase or delta database with the master geodatabase.'
##        #return conflictsDetected
##

class ReplicaSchemaImporter(CoClass):
    u'Esri Replica Schema Importer object.'
    _reg_clsid_ = GUID('{82823FC8-F978-4E83-A84E-FFF5A96AE6C5}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{A7C74158-1062-4664-B404-8694D490FCD1}', 10, 2)
class IImportSchema(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that import schema changes to a replica.'
    _iid_ = GUID('{BE88729B-0719-45B6-A60B-C977E4041C7B}')
    _idlflags_ = ['oleautomation']
ReplicaSchemaImporter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IImportSchema]

IGdbXmlExport._methods_ = [
    COMMETHOD([helpstring(u'Exports a workspace to XML.')], HRESULT, 'ExportWorkspace',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspace), 'Workspace' ),
              ( ['in'], BSTR, 'outFile' ),
              ( ['in'], VARIANT_BOOL, 'BinaryGeometry' ),
              ( ['in'], VARIANT_BOOL, 'Compressed' ),
              ( ['in'], VARIANT_BOOL, 'retrieveMetadata' )),
    COMMETHOD([helpstring(u'Exports a workspace schema to XML.')], HRESULT, 'ExportWorkspaceSchema',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspace), 'Workspace' ),
              ( ['in'], BSTR, 'outFile' ),
              ( ['in'], VARIANT_BOOL, 'Compressed' ),
              ( ['in'], VARIANT_BOOL, 'retrieveMetadata' )),
    COMMETHOD([helpstring(u'Exports datasets to XML.')], HRESULT, 'ExportDatasets',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IEnumNameMapping), 'EnumNameMapping' ),
              ( ['in'], BSTR, 'outFile' ),
              ( ['in'], VARIANT_BOOL, 'BinaryGeometry' ),
              ( ['in'], VARIANT_BOOL, 'Compressed' ),
              ( ['in'], VARIANT_BOOL, 'retrieveMetadata' )),
    COMMETHOD([helpstring(u'Exports datasets schema to XML.')], HRESULT, 'ExportDatasetsSchema',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IEnumNameMapping), 'EnumNameMapping' ),
              ( ['in'], BSTR, 'outFile' ),
              ( ['in'], VARIANT_BOOL, 'Compressed' ),
              ( ['in'], VARIANT_BOOL, 'retrieveMetadata' )),
    COMMETHOD([helpstring(u'Exports a single tabular dataset to XML.')], HRESULT, 'ExportRecordSet',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.ITableName), 'pTableName' ),
              ( ['in'], BSTR, 'outFile' ),
              ( ['in'], VARIANT_BOOL, 'BinaryGeometry' ),
              ( ['in'], VARIANT_BOOL, 'Compressed' )),
]
################################################################
## code template for IGdbXmlExport implementation
##class IGdbXmlExport_Impl(object):
##    def ExportRecordSet(self, pTableName, outFile, BinaryGeometry, Compressed):
##        u'Exports a single tabular dataset to XML.'
##        #return 
##
##    def ExportWorkspace(self, Workspace, outFile, BinaryGeometry, Compressed, retrieveMetadata):
##        u'Exports a workspace to XML.'
##        #return 
##
##    def ExportDatasets(self, EnumNameMapping, outFile, BinaryGeometry, Compressed, retrieveMetadata):
##        u'Exports datasets to XML.'
##        #return 
##
##    def ExportDatasetsSchema(self, EnumNameMapping, outFile, Compressed, retrieveMetadata):
##        u'Exports datasets schema to XML.'
##        #return 
##
##    def ExportWorkspaceSchema(self, Workspace, outFile, Compressed, retrieveMetadata):
##        u'Exports a workspace schema to XML.'
##        #return 
##

IReplicaDataChangesInit2._methods_ = [
    COMMETHOD([helpstring(u'Initializes the class by using the replica, generation option and the replica workspace.')], HRESULT, 'Init2',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IReplica), 'Replica' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceName), 'checkoutWorkspace' ),
              ( ['in'], esriExportGenerationsOption, 'GenOption' )),
]
################################################################
## code template for IReplicaDataChangesInit2 implementation
##class IReplicaDataChangesInit2_Impl(object):
##    def Init2(self, Replica, checkoutWorkspace, GenOption):
##        u'Initializes the class by using the replica, generation option and the replica workspace.'
##        #return 
##

IGdbXmlExportEvents._methods_ = [
    COMMETHOD([helpstring(u'Called before writing an XML workspace document.')], HRESULT, 'BeforeStartElement',
              ( ['in'], BSTR, 'Element' ),
              ( ['in'], BSTR, 'URL' ),
              ( ['in'], POINTER(IUnknown), 'Object' ),
              ( [], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLWriter), 'pXMLWriter' )),
    COMMETHOD([helpstring(u'Called after writing an XML workspace document.')], HRESULT, 'AfterEndElement',
              ( ['in'], BSTR, 'Element' ),
              ( ['in'], BSTR, 'URL' ),
              ( ['in'], POINTER(IUnknown), 'Object' ),
              ( [], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IXMLWriter), 'pXMLWriter' )),
]
################################################################
## code template for IGdbXmlExportEvents implementation
##class IGdbXmlExportEvents_Impl(object):
##    def BeforeStartElement(self, Element, URL, Object, pXMLWriter):
##        u'Called before writing an XML workspace document.'
##        #return 
##
##    def AfterEndElement(self, Element, URL, Object, pXMLWriter):
##        u'Called after writing an XML workspace document.'
##        #return 
##

class SchemaChanges(CoClass):
    u'Esri Schema Changes object.'
    _reg_clsid_ = GUID('{ED337BE8-C03C-4D0B-A29F-727565609B4E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{A7C74158-1062-4664-B404-8694D490FCD1}', 10, 2)
class ISchemaChangesInit(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that initialize schema changes of a replica.'
    _iid_ = GUID('{E94E335A-E1F0-4A55-9E8D-E6492B033333}')
    _idlflags_ = ['oleautomation']
SchemaChanges._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ISchemaChanges, ISchemaChangesInit]

ISchemaChangesInit._methods_ = [
    COMMETHOD([helpstring(u'Initializes the object using the replica and the target replica workspace.')], HRESULT, 'Init',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IReplica), 'Replica' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceName), 'TargetWorkspaceName' )),
    COMMETHOD([helpstring(u'Initializes the object using a replica schema document and a target replica workspace.')], HRESULT, 'InitFromSchemaDocument',
              ( ['in'], BSTR, 'xmlFile' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceName), 'TargetWorkspaceName' )),
    COMMETHOD([helpstring(u'Initializes the object using a schema differences document and a target replica workspace.')], HRESULT, 'InitFromSchemaDifferencesDocument',
              ( ['in'], BSTR, 'xmlFile' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceName), 'TargetWorkspaceName' )),
]
################################################################
## code template for ISchemaChangesInit implementation
##class ISchemaChangesInit_Impl(object):
##    def Init(self, Replica, TargetWorkspaceName):
##        u'Initializes the object using the replica and the target replica workspace.'
##        #return 
##
##    def InitFromSchemaDocument(self, xmlFile, TargetWorkspaceName):
##        u'Initializes the object using a replica schema document and a target replica workspace.'
##        #return 
##
##    def InitFromSchemaDifferencesDocument(self, xmlFile, TargetWorkspaceName):
##        u'Initializes the object using a schema differences document and a target replica workspace.'
##        #return 
##

class ArchivingDataChanges(CoClass):
    _reg_clsid_ = GUID('{2638A9A0-C033-4714-A8EE-E8C9E1C2C0FD}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{A7C74158-1062-4664-B404-8694D490FCD1}', 10, 2)
ArchivingDataChanges._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDataChanges3, IReplicaDataChangesInit, IReplicaDataChangesInit2, IReplicaDataChanges]

ICheckIn2._methods_ = [
    COMMETHOD([helpstring(u'Checks in changes from a check-out database.')], HRESULT, 'CheckInFromGDB2',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceName), 'parentDB' ),
              ( ['in'], BSTR, 'checkoutName' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceName), 'checkOutDB' ),
              ( ['in'], VARIANT_BOOL, 'reconcileCheckout' ),
              ( ['in'], comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriReplicaReconcilePolicyType, 'childReconcilePolicy' ),
              ( ['in'], VARIANT_BOOL, 'columnLevel' ),
              ( ['in'], VARIANT_BOOL, 'createOIDMappingTable' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'conflicts_detected' )),
    COMMETHOD([helpstring(u'Checks in changes from a delta database.')], HRESULT, 'CheckInFromDeltaFile2',
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceName), 'parentDB' ),
              ( ['in'], BSTR, 'checkoutName' ),
              ( ['in'], BSTR, 'fileName' ),
              ( ['in'], esriExportDataChangesOption, 'dcOption' ),
              ( ['in'], VARIANT_BOOL, 'reconcileCheckout' ),
              ( ['in'], comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriReplicaReconcilePolicyType, 'childReconcilePolicy' ),
              ( ['in'], VARIANT_BOOL, 'columnLevel' ),
              ( ['in'], VARIANT_BOOL, 'createOIDMappingTable' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'conflicts_detected' )),
]
################################################################
## code template for ICheckIn2 implementation
##class ICheckIn2_Impl(object):
##    def CheckInFromDeltaFile2(self, parentDB, checkoutName, fileName, dcOption, reconcileCheckout, childReconcilePolicy, columnLevel, createOIDMappingTable):
##        u'Checks in changes from a delta database.'
##        #return conflicts_detected
##
##    def CheckInFromGDB2(self, parentDB, checkoutName, checkOutDB, reconcileCheckout, childReconcilePolicy, columnLevel, createOIDMappingTable):
##        u'Checks in changes from a check-out database.'
##        #return conflicts_detected
##

class WFSServer(CoClass):
    u'The WFS Server Object Extension.'
    _reg_clsid_ = GUID('{E3743059-D297-4C6A-9A4A-30BDF5035F2D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{A7C74158-1062-4664-B404-8694D490FCD1}', 10, 2)
WFSServer._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._18F2FC71_6B30_45B9_B101_037A8B868B66_0_10_2.IServerObjectExtension, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IObjectConstruct, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IObjectActivate, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILogSupport, IWFSServer, comtypes.gen._18F2FC71_6B30_45B9_B101_037A8B868B66_0_10_2.IServerObjectConfigurationManager, comtypes.gen._18F2FC71_6B30_45B9_B101_037A8B868B66_0_10_2.IServerObjectConfigurationManager2, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IWebRequestHandler]

ICheckInDataSynchronizer2._methods_ = [
    COMMETHOD([helpstring(u'Synchronizes the changes in the check-out geodatabase or delta database with the master geodatabase.')], HRESULT, 'Synchronize2',
              ( ['in'], POINTER(IDataChanges), 'DataChanges' ),
              ( ['in'], BSTR, 'editVersionName' ),
              ( ['in'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.IWorkspaceName), 'ParentWorkspace' ),
              ( ['in'], VARIANT_BOOL, 'reconcileCheckout' ),
              ( ['in'], comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriReplicaReconcilePolicyType, 'reconcilePolicy' ),
              ( ['in'], VARIANT_BOOL, 'columnLevel' ),
              ( ['in'], VARIANT_BOOL, 'createOIDMappingTable' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'conflictsDetected' )),
]
################################################################
## code template for ICheckInDataSynchronizer2 implementation
##class ICheckInDataSynchronizer2_Impl(object):
##    def Synchronize2(self, DataChanges, editVersionName, ParentWorkspace, reconcileCheckout, reconcilePolicy, columnLevel, createOIDMappingTable):
##        u'Synchronizes the changes in the check-out geodatabase or delta database with the master geodatabase.'
##        #return conflictsDetected
##

IModifiedClassInfo._methods_ = [
    COMMETHOD(['propget', helpstring(u'The name of the feature class or table.')], HRESULT, 'ChildClassName',
              ( ['retval', 'out'], POINTER(BSTR), 'cClassName' )),
    COMMETHOD(['propget', helpstring(u'The ID assigned to the feature class or table in the geodatabase.')], HRESULT, 'ClassID',
              ( ['retval', 'out'], POINTER(c_int), 'ChildClassID' )),
    COMMETHOD(['propget', helpstring(u'Name of the checked out feature class or table in the master database.')], HRESULT, 'ParentClassName',
              ( ['retval', 'out'], POINTER(BSTR), 'rName' )),
    COMMETHOD(['propget', helpstring(u'The type of data.')], HRESULT, 'DatasetType',
              ( ['retval', 'out'], POINTER(comtypes.gen._0475BDB1_E5B2_4CA2_9127_B4B1683E70C2_0_10_2.esriDatasetType), 'dType' )),
    COMMETHOD(['propget', helpstring(u'Name of the database where the checked out feature class or table is stored in the master database.')], HRESULT, 'ParentDatabase',
              ( ['retval', 'out'], POINTER(BSTR), 'ParentDatabase' )),
    COMMETHOD(['propget', helpstring(u'Name of the database user that owns the checked out feature class or table in the master database.')], HRESULT, 'ParentOwner',
              ( ['retval', 'out'], POINTER(BSTR), 'ParentOwner' )),
]
################################################################
## code template for IModifiedClassInfo implementation
##class IModifiedClassInfo_Impl(object):
##    @property
##    def ClassID(self):
##        u'The ID assigned to the feature class or table in the geodatabase.'
##        #return ChildClassID
##
##    @property
##    def ParentDatabase(self):
##        u'Name of the database where the checked out feature class or table is stored in the master database.'
##        #return ParentDatabase
##
##    @property
##    def ParentClassName(self):
##        u'Name of the checked out feature class or table in the master database.'
##        #return rName
##
##    @property
##    def ParentOwner(self):
##        u'Name of the database user that owns the checked out feature class or table in the master database.'
##        #return ParentOwner
##
##    @property
##    def ChildClassName(self):
##        u'The name of the feature class or table.'
##        #return cClassName
##
##    @property
##    def DatasetType(self):
##        u'The type of data.'
##        #return dType
##

IImportSchema._methods_ = [
    COMMETHOD([helpstring(u'Import schema info.')], HRESULT, 'ImportSchema',
              ( ['in'], POINTER(ISchemaChanges), 'SchemaChanges' )),
]
################################################################
## code template for IImportSchema implementation
##class IImportSchema_Impl(object):
##    def ImportSchema(self, SchemaChanges):
##        u'Import schema info.'
##        #return 
##

__all__ = ['esriRPSavingToXMLFile', 'ISchemaChanges',
           'ReplicaProgress', 'IXMLDocumentVersion',
           'esriRPFetchRelatedObjects', 'IImportDataChanges3',
           'esriSchemaChangeTypeNewDomain', 'esriWFSHttpVerb',
           'IGdbXmlImport', 'IImportDataChanges2',
           'esriWFSServerMessageCode_FailedToGenerateTransactionResponse',
           'IGeoDataServerInit', 'esriRPExtractSchema',
           'esriExportGenerationsAll', 'ReplicaSchemaImporter',
           'esriSchemaChangeTypeDeleteTable', 'GDSData',
           'E_CAN_NOT_REUSE_SCHEMA_OF_VERSIONED_DATA',
           'GDS_E_IMPORTXMLWS_CONFLICTS_FOUND',
           'esriCheckInSourceType', 'esriImportXMLWorkspaceData',
           'esriReplicaSynchronizeBoth', 'VersionDataChanges',
           'E_CHECK_IN_INVALID_GEODATABASE',
           'esriGDSTransportTypeEmbedded', 'IOperationProgress',
           'GDS_E_CANTIMPORT_ACKMSG_AS_DATACHANGESMSG',
           'esriGeoDataServerMessageCode_ErrorInvalidVirtualDir',
           'GDS_E_NULL_QUERYID', 'esriSchemaChangeTypeAny',
           'esriSchemaChangeTypeNewTable',
           'esriWFSServerMessageCode_FailedToStopEditing',
           'esriSchemaChangeTypeNewGeometricNetwork', 'GdbImporter',
           'esriOperationProgress', 'esriGDSReplicaImportSource',
           'esriGeoDataServerMessageCode_CapabilityNotSupported',
           'esriSchemaChangeTypeDeleteGeometricNetwork',
           'IReplicaDataChangesInit',
           'E_CHECK_OUT_NOT_SUPPORTED_IN_RELEASE',
           'E_UPDATEGRAM_TOPOLOGY_DEFINITION_ACCESSING',
           'IDeltaDataChanges2', 'esriWFSServerMessageCodeEnum',
           'esriWFSServerMessageCode_ErrorInvalidUseSRSNameFormat',
           'GDS_E_IMPORTDATAWS_CONFLICTS_FOUND',
           'esriRPRegisteringReplica',
           'esriWFSServerMessageCode_ServerTooBusyToProcessTransaction',
           'IGeoDataServer2', 'esriRPImportingDataChanges',
           'E_CHECK_OUT_UNREGISTER_FAILED', 'ArchivingDataChanges',
           'GDS_E_REPLICAS_DONT_MATCH',
           'esriGeoDataServerMessageCode_ConnectedToWS', 'ICheckOut',
           'esriExportToXML',
           'esriReExportGenerationsLastUnAcknowledged',
           'esriGeoDataServerMessageCode_ErrorUnableToInitFromGdb',
           'esriExportGenerationsOption',
           'esriSchemaChangeTypeUpdateDomain', 'IGDSData2',
           'esriRADetectConflicts', 'esriGDSTransportType',
           'esriWFSServerMessageCode_FailedToReconcileAgainstSelf',
           'GDSExportOptions', 'IEnumModifiedClassInfo',
           'IGeoDataServer', 'esriRPCreatingSchemaCheckOut',
           'IReplicaValidation', 'IDataChanges',
           'esriWFSServerMessageCode_ErrorPublishedWorkspaceIsntVersioned',
           'IDataChanges2', 'esriBuildTopologies',
           'esriWFSServerMessageCode_ConflictDetected',
           'esriWFSServerMessageCode_ConstructEnded',
           'esriExportToAccess', 'DataChangesExporter',
           'esriGDSReplicaImportSourceDeltaSqliteGDB',
           'SchemaChanges', 'IDeltaDataChangesRelease',
           'ISchemaChangesInit', 'esriRPCreatingReplica',
           'esriExtractData',
           'esriWFSServerMessageCode_ErrorInvalidAppSchemaPrefix',
           'esriWFSServerMessageCode_ErrorInvalidAppSchemaNamespace',
           'esriGeoDataServerMessageCode_InfoMessage',
           'esriSchemaChangeTypeDeleteRelationshipClass',
           'IReplicaDataChanges', 'CheckInDataSynchronizer',
           'IReplicasExporter', 'esriWFSGet',
           'esriGeoDataServerMessageCode_ErrorMessage',
           'esriGDSImportFormatFileGDB', 'IGDSQueryResultPortion',
           'esriReplicationAgentReconcilePolicy', 'ISchemaChangeInfo',
           'esriDataChangeTypeDelete', 'esriDataChangeTypeUpdate',
           'esriXMLRegisterReplica', 'GeoDataServerIP',
           'esriExtractSchema', 'esriGDSExportFormatFileGDB',
           'esriDisconnectedEditingError',
           'esriRPExtractSchemaAndData', 'IGdbSchemaCreator',
           'DeltaDataChanges',
           'esriGeoDataServerMessageCode_ConstructStart',
           'esriRAResolveConflictsInFavorOfReplica1',
           'esriRAResolveConflictsInFavorOfReplica2',
           'IVersionDataChangesInit', 'esriRPRebuildCIConnectivity',
           'esriPersonalDeltaFile', 'esriRPFetchTopologyObjects',
           'IReplicaProgress',
           'esriWFSServerMessageCode_FailedToReleaseLocks',
           'GDS_E_INVALID_FORMAT_FOR_CREATEREPLICA', 'esriWFSPost',
           'IEnumTableDataChanges',
           'esriGeoDataServerMessageCode_WarningMessage',
           'esriCheckOutGDB', 'IReplicaMessageHandler',
           'esriExportXMLWorkspace', 'esriRPTransferChanges',
           'esriRPSynchronizingCheckOut',
           'esriWFSServerMessageCode_NotLicensed',
           'esriRPUnregisteringCheckOut',
           'GeoDataServerObjectDescription',
           'esriGDSExportFormatFileGDBTransport',
           'esriReplicaMessageTypeAck', 'DataExtraction',
           'DataChangesImporter', 'esriExportDataChangesOption',
           'esriGDSReplicaImportSourceDeltaPersonalGDB',
           'GDS_E_REQUESTEDCOUNT_TOO_LARGE', 'IEnumSchemaChange',
           'esriSchemaChangeTypeNewFeatureDataset',
           'esriRPExportingToXML', 'ICheckIn',
           'esriGeoDataServerMessageCode_ConstructFinish',
           'GDS_E_INVALID_COUNT_REQUESTED',
           'esriExportXMLWorkspaceData',
           'E_GEODATABASE_HAS_CHECK_OUT',
           'esriReplicaSynchronizeDirection',
           'E_CHECK_OUT_INVALID_DATA', 'IGeoDataServerObjects',
           'esriGeoDataServerMessageCode_NotLicensed',
           'esriGeoDataServerMessageCode_DebugMessage',
           'esriSchemaChangeTypeNewField',
           'esriReplicaSynchronizeFromReplica1ToReplica2',
           'esriGDSExportFormatXml', 'GDSQueryResultPortion',
           'esriGDSImportFormat', 'E_SYNCHRONIZE_INVALID_RELEASES',
           'esriSchemaChangeTypeUpdateTable',
           'GDS_E_CANTEXPORT_TO_NONCOMPRESSED_FILEGDB',
           'esriSchemaChangeTypeDeleteField', 'ReplicasExporter',
           'esriWFSServerMessageCode_ErrorInvalid11AxisOrder',
           'esriSchemaChangeTypeUpdateGeometricNetwork',
           'IImportDataChanges',
           'esriSchemaChangeTypeUpdateRelationshipClass',
           'esriGeoDataServerMessageCode_RequestNotSupported',
           'esriSchemaChangeTypeNewTopology', 'ReplicationAgent',
           'TableDataChangesInfo',
           'esriWFSServerMessageCode_PostRequest', 'ICheckIn2',
           'ReplicaValidator', 'GDS_E_INVALID_START_INDEX',
           'GDS_E_SYNCH_DIRECTION_BOTH_INVALID_FOR_CHECKOUTS',
           'esriSchemaChangeTypeNoChange',
           'GDS_E_INVALID_RECONCILE_POLICY_FOR_DIRECTION',
           'E_CHECK_IN_NOT_SUPPORTED_IN_RELEASE', 'esriRPExtractData',
           'IGDSExportOptions', 'esriRAResolveConflictsNone',
           'GDS_E_MISSING_PARAMETER', 'IDataExtraction',
           'esriRPCreatingCheckOut', 'esriReplicaMessageType',
           'esriSchemaChangeTypeDeleteTopology',
           'esriGDSExportFormatSqliteGDB',
           'esriGDSImportFormatPersonalGdb',
           'esriRPSynchronizingReplica',
           'E_CHECK_OUT_NON_VERSIONED_DATA', 'IDeltaDataChangesInit2',
           'IGDSData', 'esriSchemaChangeTypeDeleteFeatureDataset',
           'IExportDataChanges', 'esriImportXMLWorkspace',
           'esriSchemaChangeTypeNewRelationshipClass',
           'esriBuildGeometricNetworks',
           'esriReplicaSynchronizeFromReplica2ToReplica1',
           'esriExportToSqliteGDB', 'ReplicaSchemaExporter',
           'ReplicationDataChanges',
           'esriExportXMLWorkspaceDefinition',
           'esriExportXMLWorkspaceSchema', 'IExportSchema',
           'GdbExporter', 'esriSchemaChangeTypeUpdateDomains',
           'esriSchemaChangeTypeUpdateFields',
           'GeoDataServerConfigurationFactory',
           'esriImportXMLWorkspaceSchema',
           'esriGDSReplicaImportSourceDeltaFileGDB',
           'esriWFSServerMessageCode_GetRequest', 'S_DE_OK',
           'IReplicationAgent', 'ITableDataChangesInfo', 'IWFSServer',
           'OperationProgress', 'DataChanges',
           'esriRPRegisteringCheckOut', 'IGdbXmlExportEvents',
           'esriWFSServerMessageCode_FailedToStartEditing',
           'ICheckInDataSynchronizer', 'esriGDSExportFormat',
           'IImportSchema', 'esriSchemaChangeTypeUpdateField',
           'IDeltaDataChanges', 'esriRPUpdateRelatedObjects',
           'GdbSchemaCreator', 'ReplicaMessageHandler',
           'esriGeoDataServerMessageCodeEnum',
           'esriRPCreateCOVersions',
           'E_CAN_NOT_REUSE_SCHEMA_WITH_OUTPUT_SPATIAL_REFERENCE',
           'IDataChanges3', 'esriExportToFileGDB',
           'IReplicaValidation2', 'esriGDSTransportTypeUrl',
           'esriGDSImportFormatXmlWorkspace',
           'esriGeoDataServerMessageCode_ErrorInvalidConfiguration',
           'GeoDataServer', 'esriExportGenerationsNew',
           'esriGeoDataServerMessageCode_InitFromMapStarts',
           'esriExportGenerationsUnAcknowledged',
           'esriGDSExportFormatPersonalGdb',
           'esriSchemaChangeTypeUpdateFeatureDataset',
           'GeoDataServerLP', 'IDeltaDataChangesInit',
           'esriGDSReplicaImportSourceDeltaXmlFile',
           'CheckOutDataChanges',
           'esriGeoDataServerMessageCode_ErrorInvalidOutputDir',
           'esriSchemaChangeType',
           'esriWFSServerMessageCode_FailedCreatingTransactionResponse',
           'esriExportGenerationsNone',
           'esriWFSServerMessageCode_WFSExceptionReport',
           'esriWFSServerMessageCode_ErrorInvalid10AxisOrder',
           'esriReExportGenerationsAllUnAcknowledged',
           'ITablesDataChanges', 'esriRPFetchRelatedNObjects',
           'IReplicaMessageHandler2', 'IDataChangesExt',
           'esriRPBuildGeometricNetworks', 'esriFileGDBDelta',
           'esriGeoDataServerErrors', 'WFSServer',
           'esriSchemaChangeTypeDeleteDomain', 'CheckOut',
           'esriReplicaProgress', 'esriDataChangeType',
           'IGdbXmlExport', 'E_CHECK_OUT_INVALID_SOURCE_WORKSPACE',
           'esriGDSTransportTypeUpload',
           'esriWFSServerMessageCode_ConstructStart', 'CheckIn',
           'esriGeoDataServerMessageCode_InitFromMapEnded',
           'ICheckInDataSynchronizer2', 'IDataChangesInfo',
           'esriReplicaMessageTypeDCWFD',
           'esriWFSServerMessageCode_FailedToDeleteLock',
           'esriXMLDeltaFile', 'IReplicaDataChangesInit2',
           'SchemaChangeInfo', 'esriSchemaChangeTypeUpdateTopology',
           'esriReExportGenerationsOption', 'TablesDataChanges',
           'esriWFSServerMessageCode_Debug', 'IModifiedClassInfo',
           'esriWFSServerMessageCode_FailedToDeleteOutstandingTransactionVersions',
           'esriWFSServerMessageCode_TransactionFailedStoppingEditOperation',
           'esriWFSServerMessageCode_FailedToImportTransactionChanges',
           'esriWFSServerMessageCode_SkippedDataset',
           'IReplicationAgent2', 'esriRPReconcileWithParent',
           'IReplicationAgentCancelControl',
           'esriDataChangeTypeInsert',
           'E_INVALID_REPLICA_DESCRIPTION',
           'esriWFSServerMessageCode_ErrorInvalidDefaultLockExpiration',
           'esriReplicaMessageTypeDC', 'IExportDataChanges2']
from comtypes import _check_version; _check_version('501')

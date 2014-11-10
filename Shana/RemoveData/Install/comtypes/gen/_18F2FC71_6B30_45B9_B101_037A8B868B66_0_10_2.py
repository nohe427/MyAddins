# -*- coding: mbcs -*-
typelib_path = u'C:\\Program Files (x86)\\ArcGIS\\Engine10.2\\com\\esriServer.olb'
_lcid = 0 # change this if required
from ctypes import *
from comtypes import GUID
from comtypes import CoClass
import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0
from ctypes import HRESULT
from comtypes import BSTR
import comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2
from comtypes import helpstring
from comtypes import COMMETHOD
from comtypes import dispid
from ctypes.wintypes import VARIANT_BOOL
from comtypes.automation import _midlSAFEARRAY
from comtypes import IUnknown


class ServerObjectManager(CoClass):
    u'The ServerObjectManager object which creates ServerContext, ServerObjectConfigurationInfo and ServerObjectTypeInfo objects.'
    _reg_clsid_ = GUID('{5C3D041C-5D21-4B0C-935C-B1D7AA10C81C}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{18F2FC71-6B30-45B9-B101-037A8B868B66}', 10, 2)
class IServerObjectManager(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u"Provides access to properties and members of the ArcGIS server's server object manager."
    _iid_ = GUID('{CF25EA7A-B5BC-47AA-94B2-4CD598B0C428}')
    _idlflags_ = ['oleautomation']
class IServerObjectManager2(IServerObjectManager):
    _case_insensitive_ = True
    u"Provides access to properties and members of the ArcGIS server's server object manager for server object extensions."
    _iid_ = GUID('{2E3707F3-DAE3-45BA-AC15-47EF7EC69946}')
    _idlflags_ = ['oleautomation']
class IServerObjectManager3(IServerObjectManager2):
    _case_insensitive_ = True
    u"Provides access to properties and members of the ArcGIS server's server object manager for server object extensions."
    _iid_ = GUID('{0F25131D-5521-4E06-9A7F-BB246F25309C}')
    _idlflags_ = ['oleautomation']
class IServerObjectManager4(IServerObjectManager3):
    _case_insensitive_ = True
    u"Provides access to properties and members of the ArcGIS server's server object manager."
    _iid_ = GUID('{B87E5523-E612-4D71-A37F-89BE65D783FD}')
    _idlflags_ = ['oleautomation']
class IPermissionsManager(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides managerial access to the Permissions Store.'
    _iid_ = GUID('{05D95968-651A-4C97-B63E-D26F2BB0E97B}')
    _idlflags_ = ['oleautomation']
ServerObjectManager._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IServerObjectManager, IServerObjectManager2, IServerObjectManager3, IServerObjectManager4, IPermissionsManager]

class IServerObjectAdmin(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that administer the ArcGIS server.'
    _iid_ = GUID('{01F6DB39-6458-4C12-BCC7-30F1021075E2}')
    _idlflags_ = ['oleautomation']
class IServerObjectAdmin2(IServerObjectAdmin):
    _case_insensitive_ = True
    u'Provides access to members that administer the ArcGIS server.'
    _iid_ = GUID('{4BC97A90-0B03-478C-8EB8-2BA647297BF7}')
    _idlflags_ = ['oleautomation']
class IServerObjectAdmin3(IServerObjectAdmin2):
    _case_insensitive_ = True
    u'Provides access to members that administer the ArcGIS server.'
    _iid_ = GUID('{E5079624-E7C9-4B12-9DF7-2BC1C341A2B7}')
    _idlflags_ = ['oleautomation']
class IServerObjectAdmin4(IServerObjectAdmin3):
    _case_insensitive_ = True
    u'Provides access to members that administer the ArcGIS server.'
    _iid_ = GUID('{6FA1268D-0DD4-46B6-B890-02E20FC6341F}')
    _idlflags_ = ['oleautomation']
class IServerDirectory(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the behavior and properties of a server directory to administrators.'
    _iid_ = GUID('{E7402A4C-0962-4E2E-BA8F-E90B6DABFCB2}')
    _idlflags_ = ['oleautomation']
class IEnumServerDirectory(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that enumerate through ServerDirectories.'
    _iid_ = GUID('{4250C367-25DC-426C-AE90-817A8E892DB5}')
    _idlflags_ = ['oleautomation']
class IServerObjectConfiguration(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to administrators to members that control the behavior and properties of a server object configuration.'
    _iid_ = GUID('{832DAB4C-A03D-429E-8C14-401E3F807284}')
    _idlflags_ = ['oleautomation']
class IEnumServerObjectConfiguration(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that enumerate through ServerObjectConfigurations.'
    _iid_ = GUID('{815FED35-EC76-432C-9FB0-9EAD763D2F50}')
    _idlflags_ = ['oleautomation']
class IServerObjectConfigurationStatus(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u"Provides access to properties of a server object configuration's status to administrators."
    _iid_ = GUID('{096B178F-2576-4AEF-9CFA-8107D529BBFF}')
    _idlflags_ = ['oleautomation']
class IEnumServerObjectType(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that enumerate through ServerObjectTypes.'
    _iid_ = GUID('{E7FE5EAB-11EC-49AA-80F4-34AA200913B0}')
    _idlflags_ = ['oleautomation']
class IServerMachine(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to properties of a server host machine for administrators.'
    _iid_ = GUID('{2DBBD5D1-193F-4CB0-893F-98DFFFDADF1F}')
    _idlflags_ = ['oleautomation']
class IEnumServerMachine(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that enumerate through ServerMachines.'
    _iid_ = GUID('{0F89530A-8BA4-4AB6-9B4A-78541EE88525}')
    _idlflags_ = ['oleautomation']
IServerObjectAdmin._methods_ = [
    COMMETHOD([helpstring(u'Creates a new server directory.')], HRESULT, 'CreateServerDirectory',
              ( ['retval', 'out'], POINTER(POINTER(IServerDirectory)), 'ppSD' )),
    COMMETHOD([helpstring(u'Adds a server directory (created with CreateServerDirectory) to the GIS server.')], HRESULT, 'AddServerDirectory',
              ( ['in'], POINTER(IServerDirectory), 'pSD' )),
    COMMETHOD([helpstring(u'Updates the properties of a server directory.')], HRESULT, 'UpdateServerDirectory',
              ( ['in'], POINTER(IServerDirectory), 'pSD' )),
    COMMETHOD([helpstring(u'Deletes a server directory such that its cleanup is no longer managed by the GIS server. It does not delete the physical directory from disk.')], HRESULT, 'DeleteServerDirectory',
              ( ['in'], BSTR, 'Path' )),
    COMMETHOD([helpstring(u'Get the server directory with the specified Path.')], HRESULT, 'GetServerDirectory',
              ( ['in'], BSTR, 'Path' ),
              ( ['retval', 'out'], POINTER(POINTER(IServerDirectory)), 'ppSD' )),
    COMMETHOD([helpstring(u"An enumerator over the GIS server's output directories.")], HRESULT, 'GetServerDirectories',
              ( ['retval', 'out'], POINTER(POINTER(IEnumServerDirectory)), 'ppEnum' )),
    COMMETHOD([helpstring(u'Creates a new server object configuration.')], HRESULT, 'CreateConfiguration',
              ( ['retval', 'out'], POINTER(POINTER(IServerObjectConfiguration)), 'config' )),
    COMMETHOD([helpstring(u'Adds a server object configuration (created with CreateConfiguration) to the GIS server.')], HRESULT, 'AddConfiguration',
              ( ['in'], POINTER(IServerObjectConfiguration), 'config' )),
    COMMETHOD([helpstring(u'Get the server object configuration with the specified Name and TypeName.')], HRESULT, 'GetConfiguration',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], BSTR, 'TypeName' ),
              ( ['retval', 'out'], POINTER(POINTER(IServerObjectConfiguration)), 'config' )),
    COMMETHOD([helpstring(u'Updates the properties of a server object configuration.')], HRESULT, 'UpdateConfiguration',
              ( ['in'], POINTER(IServerObjectConfiguration), 'config' )),
    COMMETHOD([helpstring(u'Deletes a server object configuration from the GIS server.')], HRESULT, 'DeleteConfiguration',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], BSTR, 'TypeName' )),
    COMMETHOD([helpstring(u'An enumerator over all the server object configurations.')], HRESULT, 'GetConfigurations',
              ( ['retval', 'out'], POINTER(POINTER(IEnumServerObjectConfiguration)), 'ppConfigs' )),
    COMMETHOD([helpstring(u'Get the configuration status for a server object configuration with the specified Name and TypeName.')], HRESULT, 'GetConfigurationStatus',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], BSTR, 'TypeName' ),
              ( ['retval', 'out'], POINTER(POINTER(IServerObjectConfigurationStatus)), 'ppStatus' )),
    COMMETHOD([helpstring(u'An enumerator over all the server object types.')], HRESULT, 'GetTypes',
              ( ['retval', 'out'], POINTER(POINTER(IEnumServerObjectType)), 'ppTypes' )),
    COMMETHOD([helpstring(u'Starts a server object configuration and makes it available to clients for processing requests.')], HRESULT, 'StartConfiguration',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], BSTR, 'TypeName' )),
    COMMETHOD([helpstring(u'Stops a server object configuration and shuts down any running instances of server objects defined by the configuration.')], HRESULT, 'StopConfiguration',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], BSTR, 'TypeName' )),
    COMMETHOD([helpstring(u'Makes the configuration unavailable to clients for processing requests, but does not shut down running instances of server objects, or interrupt requests in progress.')], HRESULT, 'PauseConfiguration',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], BSTR, 'TypeName' )),
    COMMETHOD([helpstring(u'Creates a new host machine.')], HRESULT, 'CreateMachine',
              ( ['retval', 'out'], POINTER(POINTER(IServerMachine)), 'Machine' )),
    COMMETHOD([helpstring(u'Adds a host machine (created with CreateMachine) to the GIS server.')], HRESULT, 'AddMachine',
              ( ['in'], POINTER(IServerMachine), 'Machine' )),
    COMMETHOD([helpstring(u"An enumerator over all the GIS server's host machines.")], HRESULT, 'GetMachines',
              ( ['retval', 'out'], POINTER(POINTER(IEnumServerMachine)), 'machines' )),
    COMMETHOD([helpstring(u'Deletes a host machine from the GIS server, making it unavailable to host server objects.')], HRESULT, 'DeleteMachine',
              ( ['in'], BSTR, 'MachineName' )),
    COMMETHOD([helpstring(u'Get the host machine with the specified Name.')], HRESULT, 'GetMachine',
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(POINTER(IServerMachine)), 'Machine' )),
    COMMETHOD([helpstring(u'Updates the properties of a host machine.')], HRESULT, 'UpdateMachine',
              ( ['in'], POINTER(IServerMachine), 'Machine' )),
    COMMETHOD(['propget', helpstring(u'The properties for the GIS server.')], HRESULT, 'Properties',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'props' )),
    COMMETHOD(['propput', helpstring(u'The properties for the GIS server.')], HRESULT, 'Properties',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'props' )),
]
################################################################
## code template for IServerObjectAdmin implementation
##class IServerObjectAdmin_Impl(object):
##    def DeleteConfiguration(self, Name, TypeName):
##        u'Deletes a server object configuration from the GIS server.'
##        #return 
##
##    def AddConfiguration(self, config):
##        u'Adds a server object configuration (created with CreateConfiguration) to the GIS server.'
##        #return 
##
##    def GetConfigurationStatus(self, Name, TypeName):
##        u'Get the configuration status for a server object configuration with the specified Name and TypeName.'
##        #return ppStatus
##
##    def CreateServerDirectory(self):
##        u'Creates a new server directory.'
##        #return ppSD
##
##    def UpdateMachine(self, Machine):
##        u'Updates the properties of a host machine.'
##        #return 
##
##    def CreateConfiguration(self):
##        u'Creates a new server object configuration.'
##        #return config
##
##    def UpdateServerDirectory(self, pSD):
##        u'Updates the properties of a server directory.'
##        #return 
##
##    def StopConfiguration(self, Name, TypeName):
##        u'Stops a server object configuration and shuts down any running instances of server objects defined by the configuration.'
##        #return 
##
##    def GetMachine(self, Name):
##        u'Get the host machine with the specified Name.'
##        #return Machine
##
##    def DeleteServerDirectory(self, Path):
##        u'Deletes a server directory such that its cleanup is no longer managed by the GIS server. It does not delete the physical directory from disk.'
##        #return 
##
##    def GetConfigurations(self):
##        u'An enumerator over all the server object configurations.'
##        #return ppConfigs
##
##    def DeleteMachine(self, MachineName):
##        u'Deletes a host machine from the GIS server, making it unavailable to host server objects.'
##        #return 
##
##    def GetMachines(self):
##        u"An enumerator over all the GIS server's host machines."
##        #return machines
##
##    def _get(self):
##        u'The properties for the GIS server.'
##        #return props
##    def _set(self, props):
##        u'The properties for the GIS server.'
##    Properties = property(_get, _set, doc = _set.__doc__)
##
##    def GetTypes(self):
##        u'An enumerator over all the server object types.'
##        #return ppTypes
##
##    def GetServerDirectory(self, Path):
##        u'Get the server directory with the specified Path.'
##        #return ppSD
##
##    def AddServerDirectory(self, pSD):
##        u'Adds a server directory (created with CreateServerDirectory) to the GIS server.'
##        #return 
##
##    def GetServerDirectories(self):
##        u"An enumerator over the GIS server's output directories."
##        #return ppEnum
##
##    def GetConfiguration(self, Name, TypeName):
##        u'Get the server object configuration with the specified Name and TypeName.'
##        #return config
##
##    def AddMachine(self, Machine):
##        u'Adds a host machine (created with CreateMachine) to the GIS server.'
##        #return 
##
##    def UpdateConfiguration(self, config):
##        u'Updates the properties of a server object configuration.'
##        #return 
##
##    def CreateMachine(self):
##        u'Creates a new host machine.'
##        #return Machine
##
##    def StartConfiguration(self, Name, TypeName):
##        u'Starts a server object configuration and makes it available to clients for processing requests.'
##        #return 
##
##    def PauseConfiguration(self, Name, TypeName):
##        u'Makes the configuration unavailable to clients for processing requests, but does not shut down running instances of server objects, or interrupt requests in progress.'
##        #return 
##

class IEnumServerObjectExtensionType(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that enumerate through the registered server object extension types.'
    _iid_ = GUID('{3A2ED9B4-BA20-47E8-8052-2E00A8E86869}')
    _idlflags_ = ['oleautomation']
class IServerLog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that query and retrieve log records.'
    _iid_ = GUID('{44DC928C-0350-4BDB-9970-4D5CA68B4117}')
    _idlflags_ = ['oleautomation']
class IServerObjectExtensionType(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to properties, for administrators, of a server object extension type.'
    _iid_ = GUID('{47CB8511-3AA6-4DA6-9095-B6F70237ACEE}')
    _idlflags_ = ['oleautomation']
IServerObjectAdmin2._methods_ = [
    COMMETHOD([helpstring(u'An enumerator over all the server object extension types.')], HRESULT, 'GetExtensionTypes',
              ( ['in'], BSTR, 'SOTypeName' ),
              ( ['retval', 'out'], POINTER(POINTER(IEnumServerObjectExtensionType)), 'ppTypes' )),
    COMMETHOD(['propget', helpstring(u'Retrieves a reference to the ArcGIS Server logs.')], HRESULT, 'ServerLog',
              ( ['retval', 'out'], POINTER(POINTER(IServerLog)), 'ppLog' )),
    COMMETHOD([helpstring(u'Enables a disabled SOM.')], HRESULT, 'Enable'),
    COMMETHOD([helpstring(u'Disables a started SOM.')], HRESULT, 'Disable'),
    COMMETHOD([helpstring(u'Creates a new empty server object extension type.')], HRESULT, 'CreateExtensionType',
              ( ['retval', 'out'], POINTER(POINTER(IServerObjectExtensionType)), 'ppSOEType' )),
    COMMETHOD([helpstring(u'Registers a new server object extension type with the server object type indicated in the argument list.')], HRESULT, 'AddExtensionType',
              ( ['in'], BSTR, 'SOTypeName' ),
              ( ['in'], POINTER(IServerObjectExtensionType), 'pSOEType' )),
    COMMETHOD([helpstring(u'Unregisters a server object extension type from the server object type indicated in the argument list.')], HRESULT, 'DeleteExtensionType',
              ( ['in'], BSTR, 'SOTypeName' ),
              ( ['in'], BSTR, 'SOETypeName' )),
    COMMETHOD([helpstring(u'Creates a server configuration folder.')], HRESULT, 'CreateFolder',
              ( ['in'], BSTR, 'folderName' )),
    COMMETHOD([helpstring(u'Deletes a server configuration folder.')], HRESULT, 'DeleteFolder',
              ( ['in'], BSTR, 'folderName' )),
    COMMETHOD([helpstring(u'Renames a server configuration folder.')], HRESULT, 'RenameFolder',
              ( ['in'], BSTR, 'folderName' ),
              ( ['in'], BSTR, 'newName' )),
    COMMETHOD([helpstring(u'An array of folder names in the server configuration folder.')], HRESULT, 'GetFolders',
              ( ['in'], BSTR, 'folderName' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IEnumBSTR)), 'ppEnum' )),
    COMMETHOD(['propget', helpstring(u'Properties associated with a server configuration folder.')], HRESULT, 'FolderInfo',
              ( ['in'], BSTR, 'folderName' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'ppInfo' )),
    COMMETHOD(['propput', helpstring(u'Properties associated with a server configuration folder.')], HRESULT, 'FolderInfo',
              ( ['in'], BSTR, 'folderName' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'ppInfo' )),
    COMMETHOD([helpstring(u'An enumerator over all the server object configurations in a server configuration folder.')], HRESULT, 'GetConfigurationsEx',
              ( ['in'], BSTR, 'folderName' ),
              ( ['retval', 'out'], POINTER(POINTER(IEnumServerObjectConfiguration)), 'ppEnum' )),
    COMMETHOD([helpstring(u'Validates server object configuration.')], HRESULT, 'ValidateConfiguration',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], BSTR, 'TypeName' )),
]
################################################################
## code template for IServerObjectAdmin2 implementation
##class IServerObjectAdmin2_Impl(object):
##    def RenameFolder(self, folderName, newName):
##        u'Renames a server configuration folder.'
##        #return 
##
##    def Enable(self):
##        u'Enables a disabled SOM.'
##        #return 
##
##    def ValidateConfiguration(self, Name, TypeName):
##        u'Validates server object configuration.'
##        #return 
##
##    def CreateFolder(self, folderName):
##        u'Creates a server configuration folder.'
##        #return 
##
##    def _get(self, folderName):
##        u'Properties associated with a server configuration folder.'
##        #return ppInfo
##    def _set(self, folderName, ppInfo):
##        u'Properties associated with a server configuration folder.'
##    FolderInfo = property(_get, _set, doc = _set.__doc__)
##
##    def DeleteExtensionType(self, SOTypeName, SOETypeName):
##        u'Unregisters a server object extension type from the server object type indicated in the argument list.'
##        #return 
##
##    @property
##    def ServerLog(self):
##        u'Retrieves a reference to the ArcGIS Server logs.'
##        #return ppLog
##
##    def GetFolders(self, folderName):
##        u'An array of folder names in the server configuration folder.'
##        #return ppEnum
##
##    def Disable(self):
##        u'Disables a started SOM.'
##        #return 
##
##    def AddExtensionType(self, SOTypeName, pSOEType):
##        u'Registers a new server object extension type with the server object type indicated in the argument list.'
##        #return 
##
##    def GetConfigurationsEx(self, folderName):
##        u'An enumerator over all the server object configurations in a server configuration folder.'
##        #return ppEnum
##
##    def CreateExtensionType(self):
##        u'Creates a new empty server object extension type.'
##        #return ppSOEType
##
##    def DeleteFolder(self, folderName):
##        u'Deletes a server configuration folder.'
##        #return 
##
##    def GetExtensionTypes(self, SOTypeName):
##        u'An enumerator over all the server object extension types.'
##        #return ppTypes
##


# values for enumeration 'esriConfigurationStatus'
esriCSStarted = 0
esriCSPaused = 1
esriCSStopped = 2
esriCSStarting = 3
esriCSStopping = 4
esriCSDeleted = 5
esriConfigurationStatus = c_int # enum
IServerObjectAdmin3._methods_ = [
    COMMETHOD([helpstring(u'An enumerator over all the server object configurations in a server configuration folder.')], HRESULT, 'GetConfigurationsEx2',
              ( ['in'], BSTR, 'folderName' ),
              ( ['in'], esriConfigurationStatus, 'stat' ),
              ( ['retval', 'out'], POINTER(POINTER(IEnumServerObjectConfiguration)), 'ppEnum' )),
]
################################################################
## code template for IServerObjectAdmin3 implementation
##class IServerObjectAdmin3_Impl(object):
##    def GetConfigurationsEx2(self, folderName, stat):
##        u'An enumerator over all the server object configurations in a server configuration folder.'
##        #return ppEnum
##

IServerObjectAdmin4._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates whether security is switched on or off.')], HRESULT, 'IsSecurityEnabled',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether security is switched on or off.')], HRESULT, 'IsSecurityEnabled',
              ( ['in'], VARIANT_BOOL, 'pVal' )),
]
################################################################
## code template for IServerObjectAdmin4 implementation
##class IServerObjectAdmin4_Impl(object):
##    def _get(self):
##        u'Indicates whether security is switched on or off.'
##        #return pVal
##    def _set(self, pVal):
##        u'Indicates whether security is switched on or off.'
##    IsSecurityEnabled = property(_get, _set, doc = _set.__doc__)
##

class IServerObjectExtensionManager(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that help locate installed server object extensions.'
    _iid_ = GUID('{25D8B9DD-C7E8-4DA4-BF4B-08A67087CEEA}')
    _idlflags_ = ['oleautomation']
class IServerObjectExtension(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the members that control a server object extension.'
    _iid_ = GUID('{DE9A3831-3861-43DA-A35F-2E82900DB74E}')
    _idlflags_ = ['oleautomation']
IServerObjectExtensionManager._methods_ = [
    COMMETHOD([helpstring(u'Returns a server object extension found using a string representation of its class ID.')], HRESULT, 'FindExtensionByCLSID',
              ( ['in'], BSTR, 'CLSID' ),
              ( ['retval', 'out'], POINTER(POINTER(IServerObjectExtension)), 'ppSOE' )),
    COMMETHOD([helpstring(u'Returns a server object extension found using its type name.')], HRESULT, 'FindExtensionByTypeName',
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(POINTER(IServerObjectExtension)), 'ppSOE' )),
]
################################################################
## code template for IServerObjectExtensionManager implementation
##class IServerObjectExtensionManager_Impl(object):
##    def FindExtensionByTypeName(self, Name):
##        u'Returns a server object extension found using its type name.'
##        #return ppSOE
##
##    def FindExtensionByCLSID(self, CLSID):
##        u'Returns a server object extension found using a string representation of its class ID.'
##        #return ppSOE
##

class IResponseStreamer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'An interface for streaming responses.'
    _iid_ = GUID('{E7B4F042-DD12-3CE9-A801-0F47BC498F47}')
    _idlflags_ = ['oleautomation']
IResponseStreamer._methods_ = [
    COMMETHOD([helpstring(u'Initializes the Response streamer.')], HRESULT, 'Init',
              ( ['in'], BSTR, 'contentType' ),
              ( ['in'], BSTR, 'contentEncoding' )),
    COMMETHOD([helpstring(u'Writes a byte array as a response stream.')], HRESULT, 'Write',
              ( ['in'], _midlSAFEARRAY(c_ubyte), 'bytes' )),
    COMMETHOD([helpstring(u'The size of each response chunk that the client will receive.')], HRESULT, 'GetBufferSize',
              ( ['retval', 'out'], POINTER(c_int), 'size' )),
    COMMETHOD([helpstring(u'Closes the response stream.')], HRESULT, 'Close'),
]
################################################################
## code template for IResponseStreamer implementation
##class IResponseStreamer_Impl(object):
##    def Write(self, bytes):
##        u'Writes a byte array as a response stream.'
##        #return 
##
##    def GetBufferSize(self):
##        u'The size of each response chunk that the client will receive.'
##        #return size
##
##    def Init(self, contentType, contentEncoding):
##        u'Initializes the Response streamer.'
##        #return 
##
##    def Close(self):
##        u'Closes the response stream.'
##        #return 
##

class ServerP(CoClass):
    u'Private Server'
    _reg_clsid_ = GUID('{5116FA19-C21A-4C9F-816D-A4490C246D56}')
    _idlflags_ = ['hidden']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{18F2FC71-6B30-45B9-B101-037A8B868B66}', 10, 2)
class IServer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that connect to a GIS server.'
    _iid_ = GUID('{425B0A5B-BF1B-4F0E-9E75-37324A12E5F9}')
    _idlflags_ = ['oleautomation', 'hidden']
class IServerInit(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Server initialization.'
    _iid_ = GUID('{A49DD957-AADB-4FE4-89C1-D80BB586970A}')
    _idlflags_ = ['oleautomation', 'hidden']
class IServerInit2(IServerInit):
    _case_insensitive_ = True
    u'Server initialization.'
    _iid_ = GUID('{30D53022-C566-4854-87D8-2B9022829211}')
    _idlflags_ = ['oleautomation', 'hidden']
ServerP._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IServer, IServerInit, IServerInit2]

class IServerContext(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members for managing a server context, and the objects running within that server context.'
    _iid_ = GUID('{A87FDD99-6112-410C-B75E-FEFFF5EACE35}')
    _idlflags_ = ['oleautomation']
class IServerObject(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to properties of a map or geocode server object.'
    _iid_ = GUID('{0AD6AB40-9D6A-4BF8-8B86-EB89406DFC6C}')
    _idlflags_ = ['oleautomation']
IServerContext._methods_ = [
    COMMETHOD(['propget', helpstring(u'The map or geocode server object running in the server context.')], HRESULT, 'ServerObject',
              ( ['retval', 'out'], POINTER(POINTER(IServerObject)), 'obj' )),
    COMMETHOD([helpstring(u'Create an object in the server context whose type is specified by the CLSID.')], HRESULT, 'CreateObject',
              ( ['in'], BSTR, 'CLSID' ),
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'ppObj' )),
    COMMETHOD([helpstring(u'Create an object in the server context from a string that was created by saving an object using SaveObject.')], HRESULT, 'LoadObject',
              ( ['in'], BSTR, 'str' ),
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'obj' )),
    COMMETHOD([helpstring(u'Save an object in the server context to a string.')], HRESULT, 'SaveObject',
              ( ['in'], POINTER(IUnknown), 'obj' ),
              ( ['retval', 'out'], POINTER(BSTR), 'str' )),
    COMMETHOD([helpstring(u"Get a reference to an object in the server context's object dictionary by its Name.")], HRESULT, 'GetObject',
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'obj' )),
    COMMETHOD([helpstring(u"Add an object running in the server context to the context's object dictionary.")], HRESULT, 'SetObject',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], POINTER(IUnknown), 'obj' )),
    COMMETHOD([helpstring(u"Remove an object from the server context's object dictionary.")], HRESULT, 'Remove',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD([helpstring(u"Remove all objects from the server context's object dictionary.")], HRESULT, 'RemoveAll'),
    COMMETHOD([helpstring(u'Release the server context back to the server so it can be used by another client (if pooled), or so it can be destroyed (if non-pooled).')], HRESULT, 'ReleaseContext'),
]
################################################################
## code template for IServerContext implementation
##class IServerContext_Impl(object):
##    def RemoveAll(self):
##        u"Remove all objects from the server context's object dictionary."
##        #return 
##
##    def ReleaseContext(self):
##        u'Release the server context back to the server so it can be used by another client (if pooled), or so it can be destroyed (if non-pooled).'
##        #return 
##
##    def SetObject(self, Name, obj):
##        u"Add an object running in the server context to the context's object dictionary."
##        #return 
##
##    @property
##    def ServerObject(self):
##        u'The map or geocode server object running in the server context.'
##        #return obj
##
##    def CreateObject(self, CLSID):
##        u'Create an object in the server context whose type is specified by the CLSID.'
##        #return ppObj
##
##    def Remove(self, Name):
##        u"Remove an object from the server context's object dictionary."
##        #return 
##
##    def GetObject(self, Name):
##        u"Get a reference to an object in the server context's object dictionary by its Name."
##        #return obj
##
##    def LoadObject(self, str):
##        u'Create an object in the server context from a string that was created by saving an object using SaveObject.'
##        #return obj
##
##    def SaveObject(self, obj):
##        u'Save an object in the server context to a string.'
##        #return str
##

class IServerObjectHelper(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to a holder for a reference to a server object.'
    _iid_ = GUID('{F241E441-CC73-40E2-BAF0-B30EBE0EF8DC}')
    _idlflags_ = ['oleautomation']
IServerObjectExtension._methods_ = [
    COMMETHOD([helpstring(u'Initializes and starts the server object specified by the IServerObjectHelper reference.')], HRESULT, 'Init',
              ( ['in'], POINTER(IServerObjectHelper), 'pSOH' )),
    COMMETHOD([helpstring(u'Stops the server object specified by the IServerObjectHelper reference.')], HRESULT, 'Shutdown'),
]
################################################################
## code template for IServerObjectExtension implementation
##class IServerObjectExtension_Impl(object):
##    def Init(self, pSOH):
##        u'Initializes and starts the server object specified by the IServerObjectHelper reference.'
##        #return 
##
##    def Shutdown(self):
##        u'Stops the server object specified by the IServerObjectHelper reference.'
##        #return 
##

class IServerObjectAdmin5(IServerObjectAdmin4):
    _case_insensitive_ = True
    u'Provides access to members that administer the ArcGIS server.'
    _iid_ = GUID('{A7B0B4B3-1001-49AD-AD44-AA6441D7300A}')
    _idlflags_ = ['oleautomation']
class IServerObjectAdmin6(IServerObjectAdmin5):
    _case_insensitive_ = True
    u'Provides access to members that administer the ArcGIS server.'
    _iid_ = GUID('{DC0E02CD-E386-4324-B31F-56B2C5D22363}')
    _idlflags_ = ['oleautomation']
IServerObjectAdmin5._methods_ = [
    COMMETHOD([helpstring(u'Retrieves properties of server object configuration.')], HRESULT, 'GetConfigurationProperties',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], BSTR, 'Type' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'ppProps' )),
    COMMETHOD([helpstring(u'Updates properties of server object configuration.')], HRESULT, 'UpdateConfigurationProperties',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], BSTR, 'Type' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'pProps' )),
]
################################################################
## code template for IServerObjectAdmin5 implementation
##class IServerObjectAdmin5_Impl(object):
##    def UpdateConfigurationProperties(self, Name, Type, pProps):
##        u'Updates properties of server object configuration.'
##        #return 
##
##    def GetConfigurationProperties(self, Name, Type):
##        u'Retrieves properties of server object configuration.'
##        #return ppProps
##

IServerObjectAdmin6._methods_ = [
    COMMETHOD([helpstring(u'Returns the input directory for the given Server Object Configuration.')], HRESULT, 'GetInputDir',
              ( ['in'], BSTR, 'cfgName' ),
              ( ['in'], BSTR, 'cfgType' ),
              ( ['retval', 'out'], POINTER(BSTR), 'dir' )),
    COMMETHOD([helpstring(u'Checks if at least one service is currently using the input directory')], HRESULT, 'IsInputDirInUse',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD([helpstring(u'Uploads data to server and saves it as a file in the input directory of the given configuration.')], HRESULT, 'UploadData',
              ( ['in'], BSTR, 'cfgName' ),
              ( ['in'], BSTR, 'cfgType' ),
              ( ['in'], BSTR, 'fileName' ),
              ( ['in'], POINTER(_midlSAFEARRAY(c_ubyte)), 'data' )),
]
################################################################
## code template for IServerObjectAdmin6 implementation
##class IServerObjectAdmin6_Impl(object):
##    def UploadData(self, cfgName, cfgType, fileName, data):
##        u'Uploads data to server and saves it as a file in the input directory of the given configuration.'
##        #return 
##
##    def IsInputDirInUse(self):
##        u'Checks if at least one service is currently using the input directory'
##        #return pVal
##
##    def GetInputDir(self, cfgName, cfgType):
##        u'Returns the input directory for the given Server Object Configuration.'
##        #return dir
##

class IServerObjectExtensionType2(IServerObjectExtensionType):
    _case_insensitive_ = True
    u'Provides access to properties, for administrators, of a server object extension type.'
    _iid_ = GUID('{552ACCD0-D000-49A7-BEEF-BF9849B22141}')
    _idlflags_ = ['oleautomation']
class IServerObjectExtensionType3(IServerObjectExtensionType2):
    _case_insensitive_ = True
    u'Provides access to properties, for administrators, of a server object extension type.'
    _iid_ = GUID('{BC0EECAB-48DD-439E-8ECA-F2C4E3F37BEB}')
    _idlflags_ = ['oleautomation']
IServerObjectExtensionType._methods_ = [
    COMMETHOD(['propget', helpstring(u'The name of the extension type.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'The name of the extension type.')], HRESULT, 'Name',
              ( ['in'], BSTR, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'The description of the extension type.')], HRESULT, 'Description',
              ( ['retval', 'out'], POINTER(BSTR), 'desc' )),
    COMMETHOD(['propput', helpstring(u'The description of the extension type.')], HRESULT, 'Description',
              ( ['in'], BSTR, 'desc' )),
    COMMETHOD(['propget', helpstring(u'The class ID of the extension type.')], HRESULT, 'CLSID',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'The class ID of the extension type.')], HRESULT, 'CLSID',
              ( ['in'], BSTR, 'pVal' )),
]
################################################################
## code template for IServerObjectExtensionType implementation
##class IServerObjectExtensionType_Impl(object):
##    def _get(self):
##        u'The name of the extension type.'
##        #return pVal
##    def _set(self, pVal):
##        u'The name of the extension type.'
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The class ID of the extension type.'
##        #return pVal
##    def _set(self, pVal):
##        u'The class ID of the extension type.'
##    CLSID = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The description of the extension type.'
##        #return desc
##    def _set(self, desc):
##        u'The description of the extension type.'
##    Description = property(_get, _set, doc = _set.__doc__)
##

IServerObjectExtensionType2._methods_ = [
    COMMETHOD(['propget', helpstring(u'Display name of the server object extension type.')], HRESULT, 'DisplayName',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Display name of the server object extension type.')], HRESULT, 'DisplayName',
              ( ['in'], BSTR, 'pVal' )),
]
################################################################
## code template for IServerObjectExtensionType2 implementation
##class IServerObjectExtensionType2_Impl(object):
##    def _get(self):
##        u'Display name of the server object extension type.'
##        #return pVal
##    def _set(self, pVal):
##        u'Display name of the server object extension type.'
##    DisplayName = property(_get, _set, doc = _set.__doc__)
##

IServerObjectExtensionType3._methods_ = [
    COMMETHOD(['propget', helpstring(u'Properties for the server object extension type.')], HRESULT, 'Properties',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'props' )),
    COMMETHOD(['propputref', helpstring(u'Properties for the server object extension type.')], HRESULT, 'Properties',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'props' )),
    COMMETHOD(['propget', helpstring(u'Auxiliary information for the server objects extension type ?passive properties only.')], HRESULT, 'Info',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'props' )),
    COMMETHOD(['propputref', helpstring(u'Auxiliary information for the server objects extension type ?passive properties only.')], HRESULT, 'Info',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'props' )),
    COMMETHOD(['propget', helpstring(u'Configuration Factory CLSID.')], HRESULT, 'ConfigurationFactoryCLSID',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Configuration Factory CLSID.')], HRESULT, 'ConfigurationFactoryCLSID',
              ( ['in'], BSTR, 'pVal' )),
]
################################################################
## code template for IServerObjectExtensionType3 implementation
##class IServerObjectExtensionType3_Impl(object):
##    def Info(self, props):
##        u'Auxiliary information for the server objects extension type ?passive properties only.'
##        #return 
##
##    def Properties(self, props):
##        u'Properties for the server object extension type.'
##        #return 
##
##    def _get(self):
##        u'Configuration Factory CLSID.'
##        #return pVal
##    def _set(self, pVal):
##        u'Configuration Factory CLSID.'
##    ConfigurationFactoryCLSID = property(_get, _set, doc = _set.__doc__)
##

class ServerObjectAdmin(CoClass):
    u'The ServerObjectAdmin object which administrates the GIS Server.'
    _reg_clsid_ = GUID('{D317CF58-EB65-4D4C-A18B-FCB477A91AC9}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{18F2FC71-6B30-45B9-B101-037A8B868B66}', 10, 2)
class IServerObjectAdmin7(IServerObjectAdmin6):
    _case_insensitive_ = True
    u'Provides access to members that administer the ArcGIS server.'
    _iid_ = GUID('{C6CFC4DF-7928-4EC2-9F34-87EED2BAC0A3}')
    _idlflags_ = ['oleautomation']
class IServerObjectAdmin8(IServerObjectAdmin7):
    _case_insensitive_ = True
    u'Provides access to members that administer the ArcGIS server.'
    _iid_ = GUID('{22930007-4A01-479F-8CB6-33C8AC33CCF4}')
    _idlflags_ = ['oleautomation']
class IServerStatistics(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that report statistics for a GIS server to administrators.'
    _iid_ = GUID('{A0500A17-B797-41F3-94EB-66A32FCF8D80}')
    _idlflags_ = ['oleautomation']
class IPermissionsAdmin(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides administrative access to the Permissions Store.'
    _iid_ = GUID('{1D869AB1-DB39-4CB8-9E95-A64AC2BEB029}')
    _idlflags_ = ['oleautomation']
class IPermissionsAdmin2(IPermissionsAdmin):
    _case_insensitive_ = True
    u'Provides administrative access to the Permissions Store.'
    _iid_ = GUID('{8F6CE835-8644-420D-A2A3-2A84E2C29BFD}')
    _idlflags_ = ['oleautomation']
class IServerErrorReports(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to Server error reporting settings.'
    _iid_ = GUID('{A0C0005D-C630-4A08-9805-5B3E4C446DBB}')
    _idlflags_ = ['oleautomation']
ServerObjectAdmin._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IServerObjectAdmin, IServerObjectAdmin2, IServerObjectAdmin3, IServerObjectAdmin4, IServerObjectAdmin5, IServerObjectAdmin6, IServerObjectAdmin7, IServerObjectAdmin8, IServerStatistics, IPermissionsAdmin, IPermissionsAdmin2, IServerErrorReports]

class ServerObjectConfiguration(CoClass):
    u'The ServerObjectConfiguration object which defines the properties and behavior for server objects running in the GIS server.'
    _reg_clsid_ = GUID('{061AFFB5-AE19-4A72-896C-EF59E415697B}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{18F2FC71-6B30-45B9-B101-037A8B868B66}', 10, 2)
class IServerObjectConfiguration2(IServerObjectConfiguration):
    _case_insensitive_ = True
    u'Provides access to administrators to members that control the behavior and properties of a server object configuration with extensions.'
    _iid_ = GUID('{2D81B707-95B1-4EFA-A0FA-5AB49B051D0B}')
    _idlflags_ = ['oleautomation']
class IServerObjectConfiguration3(IServerObjectConfiguration2):
    _case_insensitive_ = True
    u'Provides access to administrators to members that control the behavior and properties of a server object configuration with extensions.'
    _iid_ = GUID('{35BCF76E-686F-4CB2-B0B8-F615754E79D3}')
    _idlflags_ = ['oleautomation']
class IServerObjectConfiguration4(IServerObjectConfiguration3):
    _case_insensitive_ = True
    u'Provides access to administrators to members that control the behavior and properties of a server object configuration with extensions.'
    _iid_ = GUID('{AC7687E9-A00E-4281-ABAA-B889A5D7B1A6}')
    _idlflags_ = ['oleautomation']
ServerObjectConfiguration._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IServerObjectConfiguration, IServerObjectConfiguration2, IServerObjectConfiguration3, IServerObjectConfiguration4]

class IServerObjectConfigurationInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to properties of a server object configuration.'
    _iid_ = GUID('{6C7EEC75-0D7D-4EC1-8B58-4D88F11FD4FA}')
    _idlflags_ = ['oleautomation']
IServerObjectConfigurationInfo._methods_ = [
    COMMETHOD(['propget', helpstring(u'Name of the server object configuration.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'Type of the server object configuration (MapServer or GeocodeServer).')], HRESULT, 'TypeName',
              ( ['retval', 'out'], POINTER(BSTR), 'TypeName' )),
    COMMETHOD(['propget', helpstring(u'Description of the server object configuration.')], HRESULT, 'Description',
              ( ['retval', 'out'], POINTER(BSTR), 'desc' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the server objects defined by this configuration are pooled.')], HRESULT, 'IsPooled',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsPooled' )),
]
################################################################
## code template for IServerObjectConfigurationInfo implementation
##class IServerObjectConfigurationInfo_Impl(object):
##    @property
##    def TypeName(self):
##        u'Type of the server object configuration (MapServer or GeocodeServer).'
##        #return TypeName
##
##    @property
##    def IsPooled(self):
##        u'Indicates whether the server objects defined by this configuration are pooled.'
##        #return IsPooled
##
##    @property
##    def Name(self):
##        u'Name of the server object configuration.'
##        #return Name
##
##    @property
##    def Description(self):
##        u'Description of the server object configuration.'
##        #return desc
##

class IServerMachine2(IServerMachine):
    _case_insensitive_ = True
    u'Provides access to properties of a server host machine for administrators.'
    _iid_ = GUID('{7CDDDB35-6819-41F6-B2C3-8197F95F65B0}')
    _idlflags_ = ['oleautomation']
IServerMachine._methods_ = [
    COMMETHOD(['propget', helpstring(u'The name of the machine that can host server objects for the GIS server.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propput', helpstring(u'The name of the machine that can host server objects for the GIS server.')], HRESULT, 'Name',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD(['propget', helpstring(u'The description of the host machine.')], HRESULT, 'Description',
              ( ['retval', 'out'], POINTER(BSTR), 'desc' )),
    COMMETHOD(['propput', helpstring(u'The description of the host machine.')], HRESULT, 'Description',
              ( ['in'], BSTR, 'desc' )),
]
################################################################
## code template for IServerMachine implementation
##class IServerMachine_Impl(object):
##    def _get(self):
##        u'The name of the machine that can host server objects for the GIS server.'
##        #return Name
##    def _set(self, Name):
##        u'The name of the machine that can host server objects for the GIS server.'
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The description of the host machine.'
##        #return desc
##    def _set(self, desc):
##        u'The description of the host machine.'
##    Description = property(_get, _set, doc = _set.__doc__)
##

IServerMachine2._methods_ = [
    COMMETHOD(['propget', helpstring(u'The number of desired concurrently available configurations (the capacity) of the ArcGIS Server.')], HRESULT, 'Capacity',
              ( ['retval', 'out'], POINTER(c_int), 'Val' )),
    COMMETHOD(['propput', helpstring(u'The number of desired concurrently available configurations (the capacity) of the ArcGIS Server.')], HRESULT, 'Capacity',
              ( ['in'], c_int, 'Val' )),
]
################################################################
## code template for IServerMachine2 implementation
##class IServerMachine2_Impl(object):
##    def _get(self):
##        u'The number of desired concurrently available configurations (the capacity) of the ArcGIS Server.'
##        #return Val
##    def _set(self, Val):
##        u'The number of desired concurrently available configurations (the capacity) of the ArcGIS Server.'
##    Capacity = property(_get, _set, doc = _set.__doc__)
##

class Server(CoClass):
    u'The Server object for connecting to the GIS server and getting the ServerObjectManager and ServerObjectAdmin.'
    _reg_clsid_ = GUID('{379376DB-AEA6-40D1-9491-9345E61EF6BE}')
    _idlflags_ = ['hidden']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{18F2FC71-6B30-45B9-B101-037A8B868B66}', 10, 2)
class IServer2(IServer):
    _case_insensitive_ = True
    u'Provides access to methods that connect a specified user to an ArcGIS server.'
    _iid_ = GUID('{0741D66C-C157-4B4D-AF5E-C74C68BA8386}')
    _idlflags_ = ['oleautomation', 'hidden']
Server._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IServer, IServer2]

class ServerLogImpl(CoClass):
    u'The ServerLogImp1 object which methods to query and retrieve records from the ArcGIS Server logs.'
    _reg_clsid_ = GUID('{3E32107F-4F36-4D50-A5D2-9EC7C0986CC0}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{18F2FC71-6B30-45B9-B101-037A8B868B66}', 10, 2)
class IServerLog2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that query and retrieve log records.'
    _iid_ = GUID('{B7729AB3-6FD1-402D-9162-AE21B9EC545E}')
    _idlflags_ = ['oleautomation']
ServerLogImpl._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IServerLog, IServerLog2]

class IServerHelper(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Helper interface for Server.'
    _iid_ = GUID('{7BAAE10C-1933-45BE-A723-E71C9D6B6941}')
    _idlflags_ = ['oleautomation']
IServerHelper._methods_ = [
    COMMETHOD([helpstring(u"Returns a service's configured status.")], HRESULT, 'GetServerObjectConfigurationStatus',
              ( ['in'], BSTR, 'cfgName' ),
              ( ['in'], BSTR, 'cfgType' ),
              ( ['retval', 'out'], POINTER(POINTER(IServerObjectConfigurationStatus)), 'ppCfgStatus' )),
]
################################################################
## code template for IServerHelper implementation
##class IServerHelper_Impl(object):
##    def GetServerObjectConfigurationStatus(self, cfgName, cfgType):
##        u"Returns a service's configured status."
##        #return ppCfgStatus
##

class IServerObjectType(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods, for administrators, that control the behavior and properties of a server object type.'
    _iid_ = GUID('{9AD7BECA-FBC3-494A-BEC6-790FF0E6946E}')
    _idlflags_ = ['oleautomation']
class IServerObjectType2(IServerObjectType):
    _case_insensitive_ = True
    u'Provides access to methods, for administrators, that control the behavior and properties of a server object type.'
    _iid_ = GUID('{42472792-5345-4B93-B132-3977C24BACB4}')
    _idlflags_ = ['oleautomation']
IServerObjectType._methods_ = [
    COMMETHOD(['propget', helpstring(u'Name of the server object type.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Name of the server object type.')], HRESULT, 'Name',
              ( ['in'], BSTR, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Description of the server object type.')], HRESULT, 'Description',
              ( ['retval', 'out'], POINTER(BSTR), 'desc' )),
    COMMETHOD(['propput', helpstring(u'Description of the server object type.')], HRESULT, 'Description',
              ( ['in'], BSTR, 'desc' )),
    COMMETHOD(['propget', helpstring(u'The GUID of the COM class corresponding to the server object type.')], HRESULT, 'CLSID',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'The GUID of the COM class corresponding to the server object type.')], HRESULT, 'CLSID',
              ( ['in'], BSTR, 'pVal' )),
]
################################################################
## code template for IServerObjectType implementation
##class IServerObjectType_Impl(object):
##    def _get(self):
##        u'Name of the server object type.'
##        #return pVal
##    def _set(self, pVal):
##        u'Name of the server object type.'
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The GUID of the COM class corresponding to the server object type.'
##        #return pVal
##    def _set(self, pVal):
##        u'The GUID of the COM class corresponding to the server object type.'
##    CLSID = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Description of the server object type.'
##        #return desc
##    def _set(self, desc):
##        u'Description of the server object type.'
##    Description = property(_get, _set, doc = _set.__doc__)
##


# values for enumeration 'esriServerIsolationLevel'
esriServerIsolationHigh = 0
esriServerIsolationLow = 1
esriServerIsolationAny = 2
esriServerIsolationLevel = c_int # enum
IServerObjectType2._methods_ = [
    COMMETHOD(['propget', helpstring(u'The isolation level of the server objects supported by the server object type.')], HRESULT, 'IsolationLevel',
              ( ['retval', 'out'], POINTER(esriServerIsolationLevel), 'isoLevel' )),
    COMMETHOD(['propput', helpstring(u'The isolation level of the server objects supported by the server object type.')], HRESULT, 'IsolationLevel',
              ( ['in'], esriServerIsolationLevel, 'isoLevel' )),
    COMMETHOD(['propget', helpstring(u'Display name of the server object type.')], HRESULT, 'DisplayName',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Display name of the server object type.')], HRESULT, 'DisplayName',
              ( ['in'], BSTR, 'pVal' )),
]
################################################################
## code template for IServerObjectType2 implementation
##class IServerObjectType2_Impl(object):
##    def _get(self):
##        u'Display name of the server object type.'
##        #return pVal
##    def _set(self, pVal):
##        u'Display name of the server object type.'
##    DisplayName = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The isolation level of the server objects supported by the server object type.'
##        #return isoLevel
##    def _set(self, isoLevel):
##        u'The isolation level of the server objects supported by the server object type.'
##    IsolationLevel = property(_get, _set, doc = _set.__doc__)
##

class IGISServerConnection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that connect to a GIS server.'
    _iid_ = GUID('{E3105184-0AAD-4706-9269-DCB5FF52036D}')
    _idlflags_ = ['oleautomation']
IGISServerConnection._methods_ = [
    COMMETHOD([helpstring(u'Connects to the GIS server specified by the machineName.')], HRESULT, 'Connect',
              ( ['in'], BSTR, 'MachineName' )),
    COMMETHOD(['propget', helpstring(u'The server object manager for the connected GIS server.')], HRESULT, 'ServerObjectManager',
              ( ['retval', 'out'], POINTER(POINTER(IServerObjectManager)), 'mgr' )),
    COMMETHOD(['propget', helpstring(u'The server object admin for the connected GIS server.')], HRESULT, 'ServerObjectAdmin',
              ( ['retval', 'out'], POINTER(POINTER(IServerObjectAdmin)), 'admin' )),
]
################################################################
## code template for IGISServerConnection implementation
##class IGISServerConnection_Impl(object):
##    @property
##    def ServerObjectAdmin(self):
##        u'The server object admin for the connected GIS server.'
##        #return admin
##
##    def Connect(self, MachineName):
##        u'Connects to the GIS server specified by the machineName.'
##        #return 
##
##    @property
##    def ServerObjectManager(self):
##        u'The server object manager for the connected GIS server.'
##        #return mgr
##

class ServerObjectExtensionTypeInfo(CoClass):
    u'The ServerObjectExtensionTypeInfo object which provides information about server object extension types to users without administrative privileges to the ArcGIS server.'
    _reg_clsid_ = GUID('{91C3D839-CE1E-4750-BF23-63A4BBB4880E}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{18F2FC71-6B30-45B9-B101-037A8B868B66}', 10, 2)
class IServerObjectExtensionTypeInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the properties of a server object extentsion type.'
    _iid_ = GUID('{B5D6FDA3-B063-4174-9E70-2764D55BCCB4}')
    _idlflags_ = ['oleautomation']
class IServerObjectExtensionTypeInfo2(IServerObjectExtensionTypeInfo):
    _case_insensitive_ = True
    u'Provides access to the properties of a server object extentsion type.'
    _iid_ = GUID('{94D56C57-00DF-4336-8707-CF4197A890EF}')
    _idlflags_ = ['oleautomation']
ServerObjectExtensionTypeInfo._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IServerObjectExtensionTypeInfo, IServerObjectExtensionTypeInfo2]

class IServiceDescription(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the properties of an ArcGIS Server web service description.'
    _iid_ = GUID('{99EA4F91-10A1-4901-A695-86E31090F3C1}')
    _idlflags_ = ['oleautomation']
class IServiceDescription2(IServiceDescription):
    _case_insensitive_ = True
    u'Provides access to members that control the properties of an ArcGIS Server web service description.'
    _iid_ = GUID('{081C203C-3B90-4DE2-AF43-7C30BBFE22E9}')
    _idlflags_ = ['oleautomation']
IServiceDescription._methods_ = [
    COMMETHOD(['propget', helpstring(u'The name of the web service.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'The name of the web service.')], HRESULT, 'Name',
              ( ['in'], BSTR, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'The type of the web service (MapServer or GeocodeServer).')], HRESULT, 'Type',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'The type of the web service (MapServer or GeocodeServer).')], HRESULT, 'Type',
              ( ['in'], BSTR, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'The URL of the web service.')], HRESULT, 'URL',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'The URL of the web service.')], HRESULT, 'URL',
              ( ['in'], BSTR, 'pVal' )),
]
################################################################
## code template for IServiceDescription implementation
##class IServiceDescription_Impl(object):
##    def _get(self):
##        u'The URL of the web service.'
##        #return pVal
##    def _set(self, pVal):
##        u'The URL of the web service.'
##    URL = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The type of the web service (MapServer or GeocodeServer).'
##        #return pVal
##    def _set(self, pVal):
##        u'The type of the web service (MapServer or GeocodeServer).'
##    Type = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The name of the web service.'
##        #return pVal
##    def _set(self, pVal):
##        u'The name of the web service.'
##    Name = property(_get, _set, doc = _set.__doc__)
##

IServiceDescription2._methods_ = [
    COMMETHOD(['propget', helpstring(u'The type of service this extension is associated with.')], HRESULT, 'ParentType',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'The type of service this extension is associated with.')], HRESULT, 'ParentType',
              ( ['in'], BSTR, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'The capabilities of the web service.')], HRESULT, 'Capabilities',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'The capabilities of the web service.')], HRESULT, 'Capabilities',
              ( ['in'], BSTR, 'pVal' )),
]
################################################################
## code template for IServiceDescription2 implementation
##class IServiceDescription2_Impl(object):
##    def _get(self):
##        u'The type of service this extension is associated with.'
##        #return pVal
##    def _set(self, pVal):
##        u'The type of service this extension is associated with.'
##    ParentType = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The capabilities of the web service.'
##        #return pVal
##    def _set(self, pVal):
##        u'The capabilities of the web service.'
##    Capabilities = property(_get, _set, doc = _set.__doc__)
##

class IGISServerConnection2(IGISServerConnection):
    _case_insensitive_ = True
    u'Provides access to methods that connect a specified user to an ArcGIS server.'
    _iid_ = GUID('{F6616298-396A-41F2-9A5B-0EED59AF2E40}')
    _idlflags_ = ['oleautomation']
IGISServerConnection2._methods_ = [
    COMMETHOD([helpstring(u'Connects the user specified by userInfo to the GIS server given by machineName.')], HRESULT, 'Connect2',
              ( ['in'], BSTR, 'UserInfo' ),
              ( ['in'], BSTR, 'MachineName' )),
]
################################################################
## code template for IGISServerConnection2 implementation
##class IGISServerConnection2_Impl(object):
##    def Connect2(self, UserInfo, MachineName):
##        u'Connects the user specified by userInfo to the GIS server given by machineName.'
##        #return 
##

class GISServerConnection(CoClass):
    u'The ServerConnection object for connecting to the GIS server and getting the ServerObjectManager and ServerObjectAdmin.'
    _reg_clsid_ = GUID('{CD57B642-1B4A-4E02-A1D0-FFDBCF0E5A41}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{18F2FC71-6B30-45B9-B101-037A8B868B66}', 10, 2)
GISServerConnection._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGISServerConnection, IGISServerConnection2]

class IServerMachine3(IServerMachine2):
    _case_insensitive_ = True
    u'Provides access to properties of a server host machine for administrators.'
    _iid_ = GUID('{C0445F7E-124C-487D-A364-6506E3574865}')
    _idlflags_ = ['oleautomation']
IServerMachine3._methods_ = [
    COMMETHOD(['propget', helpstring(u'The admin URL of the server machine.')], HRESULT, 'AdminURL',
              ( ['retval', 'out'], POINTER(BSTR), 'pUrl' )),
    COMMETHOD(['propput', helpstring(u'The admin URL of the server machine.')], HRESULT, 'AdminURL',
              ( ['in'], BSTR, 'pUrl' )),
    COMMETHOD(['propget', helpstring(u'The platform of the server machine.')], HRESULT, 'Platform',
              ( ['retval', 'out'], POINTER(BSTR), 'pPlatform' )),
    COMMETHOD(['propput', helpstring(u'The platform of the server machine.')], HRESULT, 'Platform',
              ( ['in'], BSTR, 'pPlatform' )),
    COMMETHOD(['propget', helpstring(u'The total count of ports.')], HRESULT, 'PortCount',
              ( ['retval', 'out'], POINTER(c_int), 'pCount' )),
    COMMETHOD(['propget', helpstring(u'The port names.')], HRESULT, 'PortNames',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IEnumBSTR)), 'ppNames' )),
    COMMETHOD(['propget', helpstring(u'The port number of a port.')], HRESULT, 'PortNumber',
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(c_int), 'pNumber' )),
]
################################################################
## code template for IServerMachine3 implementation
##class IServerMachine3_Impl(object):
##    def _get(self):
##        u'The admin URL of the server machine.'
##        #return pUrl
##    def _set(self, pUrl):
##        u'The admin URL of the server machine.'
##    AdminURL = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The platform of the server machine.'
##        #return pPlatform
##    def _set(self, pPlatform):
##        u'The platform of the server machine.'
##    Platform = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def PortNames(self):
##        u'The port names.'
##        #return ppNames
##
##    @property
##    def PortNumber(self, Name):
##        u'The port number of a port.'
##        #return pNumber
##
##    @property
##    def PortCount(self):
##        u'The total count of ports.'
##        #return pCount
##

class ServerEnvironmentXHelper(CoClass):
    _reg_clsid_ = GUID('{C779A894-BBFA-4CCE-8906-ED950348BEBB}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{18F2FC71-6B30-45B9-B101-037A8B868B66}', 10, 2)
class IServerEnvironmentXHelper(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Helper interface to set properties on the server environment.'
    _iid_ = GUID('{9FC0C623-186B-4A67-A4C9-5DEC2FB8377D}')
    _idlflags_ = ['oleautomation']
ServerEnvironmentXHelper._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo, IServerEnvironmentXHelper]

class ServerObjectFactoryX(CoClass):
    _reg_clsid_ = GUID('{14E85554-5EEE-410E-AD86-FFECE038F1A3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{18F2FC71-6B30-45B9-B101-037A8B868B66}', 10, 2)
class IServerObjectFactoryX(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Factory interface to create server objects.'
    _iid_ = GUID('{D4B031BA-AD7D-438B-811C-A362F8B2D818}')
    _idlflags_ = ['oleautomation']
ServerObjectFactoryX._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo, IServerObjectFactoryX]

class ServerObject(CoClass):
    u'The ServerObject object which runs within a server context in the GIS server.'
    _reg_clsid_ = GUID('{D43BEE68-F44F-4C90-A72F-41B469BE5A6B}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{18F2FC71-6B30-45B9-B101-037A8B868B66}', 10, 2)
ServerObject._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IServerObject, IServerObjectExtensionManager, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IObjectConstruct, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IObjectActivate, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILogSupport]

class GPServerHelper(CoClass):
    _reg_clsid_ = GUID('{31A080FC-E398-415E-9F12-550127217487}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{18F2FC71-6B30-45B9-B101-037A8B868B66}', 10, 2)
class IGPServerHelper(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Helper interface to process Geoprocessing requests.'
    _iid_ = GUID('{E5A9A155-937E-4025-8CE6-42690D964C42}')
    _idlflags_ = ['oleautomation']
GPServerHelper._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo, IGPServerHelper]

class ServerContext(CoClass):
    u'The ServerContext object used for working with ArcObjects in the GIS server.'
    _reg_clsid_ = GUID('{FCCB4713-2958-4284-9D99-7E25A0BBB423}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{18F2FC71-6B30-45B9-B101-037A8B868B66}', 10, 2)
ServerContext._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IServerContext]

class IEnumServerObjectConfigurationInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that enumerate through ServerObjectConfigurationInfos.'
    _iid_ = GUID('{B810B79F-1777-4555-886D-DC6297FB2891}')
    _idlflags_ = ['oleautomation']
class IEnumServerObjectTypeInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that enumerate through ServerObjectTypeInfos.'
    _iid_ = GUID('{E9407DB1-0C60-47EF-A20C-7EA37EF0AEC5}')
    _idlflags_ = ['oleautomation']
class IEnumServerDirectoryInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that enumerate through ServerDirectoryInfos.'
    _iid_ = GUID('{E3A6F4A0-28CA-45B8-86B3-36888FB5466B}')
    _idlflags_ = ['oleautomation']
IServerObjectManager._methods_ = [
    COMMETHOD([helpstring(u'Gets a reference to a server context. The server context can be based on a specified server object configuration, or can be an empty server context if no server object configuration is specified.')], HRESULT, 'CreateServerContext',
              ( ['in'], BSTR, 'configName' ),
              ( ['in'], BSTR, 'TypeName' ),
              ( ['retval', 'out'], POINTER(POINTER(IServerContext)), 'context' )),
    COMMETHOD([helpstring(u'Gets the ServerObjectConfigurationInfo for the specified Name and TypeName.')], HRESULT, 'GetConfigurationInfo',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], BSTR, 'TypeName' ),
              ( ['retval', 'out'], POINTER(POINTER(IServerObjectConfigurationInfo)), 'ppInfo' )),
    COMMETHOD([helpstring(u"An enumerator over all the GIS server's ServerObjectConfigurationInfos.")], HRESULT, 'GetConfigurationInfos',
              ( ['retval', 'out'], POINTER(POINTER(IEnumServerObjectConfigurationInfo)), 'infos' )),
    COMMETHOD([helpstring(u"An enumerator over all the GIS server's ServerObjectTypeInfos.")], HRESULT, 'GetTypeInfos',
              ( ['retval', 'out'], POINTER(POINTER(IEnumServerObjectTypeInfo)), 'infos' )),
    COMMETHOD([helpstring(u"An enumerator over all the GIS server's ServerDirectoryInfos.")], HRESULT, 'GetServerDirectoryInfos',
              ( ['retval', 'out'], POINTER(POINTER(IEnumServerDirectoryInfo)), 'ppEnum' )),
]
################################################################
## code template for IServerObjectManager implementation
##class IServerObjectManager_Impl(object):
##    def GetConfigurationInfos(self):
##        u"An enumerator over all the GIS server's ServerObjectConfigurationInfos."
##        #return infos
##
##    def CreateServerContext(self, configName, TypeName):
##        u'Gets a reference to a server context. The server context can be based on a specified server object configuration, or can be an empty server context if no server object configuration is specified.'
##        #return context
##
##    def GetServerDirectoryInfos(self):
##        u"An enumerator over all the GIS server's ServerDirectoryInfos."
##        #return ppEnum
##
##    def GetConfigurationInfo(self, Name, TypeName):
##        u'Gets the ServerObjectConfigurationInfo for the specified Name and TypeName.'
##        #return ppInfo
##
##    def GetTypeInfos(self):
##        u"An enumerator over all the GIS server's ServerObjectTypeInfos."
##        #return infos
##

class IServiceCatalog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to properties of an ArcGIS Server web service catalog.'
    _iid_ = GUID('{89D60975-FDCF-4CEA-B981-73FE406A2D2B}')
    _idlflags_ = ['oleautomation']
class IServiceCatalog2(IServiceCatalog):
    _case_insensitive_ = True
    u'Provides access to properties of an ArcGIS Server web service catalog.'
    _iid_ = GUID('{46C52546-7C26-477F-BDC1-B1C254625F81}')
    _idlflags_ = ['oleautomation']
class IServiceCatalog3(IServiceCatalog2):
    _case_insensitive_ = True
    u'Provides access to properties of an ArcGIS Server web service catalog.'
    _iid_ = GUID('{BB163DC2-8EC3-4536-8B0C-7FFE7B91B7B0}')
    _idlflags_ = ['oleautomation']
class IServiceDescriptionArray(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the contents of web services description array.'
    _iid_ = GUID('{EEF9BC6F-4560-43AB-9D8C-F8EADFAD5C70}')
    _idlflags_ = ['oleautomation']
IServiceCatalog._methods_ = [
    COMMETHOD(['propget', helpstring(u'An array of the web service descriptions in the web service catalog.')], HRESULT, 'ServiceDescriptions',
              ( ['retval', 'out'], POINTER(POINTER(IServiceDescriptionArray)), 'pVal' )),
]
################################################################
## code template for IServiceCatalog implementation
##class IServiceCatalog_Impl(object):
##    @property
##    def ServiceDescriptions(self):
##        u'An array of the web service descriptions in the web service catalog.'
##        #return pVal
##


# values for enumeration 'esriServiceCatalogMessageFormat'
esriServiceCatalogMessageFormatSoap = 1
esriServiceCatalogMessageFormatBin = 2
esriServiceCatalogMessageFormatSoapOrBin = 3
esriServiceCatalogMessageFormat = c_int # enum
IServiceCatalog2._methods_ = [
    COMMETHOD(['propget', helpstring(u'The message version this server version supports.')], HRESULT, 'MessageVersion',
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.esriArcGISVersion), 'ver' )),
    COMMETHOD(['propget', helpstring(u'The message formats supported by the web services in the catalog.')], HRESULT, 'MessageFormats',
              ( ['retval', 'out'], POINTER(esriServiceCatalogMessageFormat), 'msgFormats' )),
    COMMETHOD(['propget', helpstring(u'An array of the web service descriptions in the web service catalog.')], HRESULT, 'ServiceDescriptionsEx',
              ( ['in'], BSTR, 'folderName' ),
              ( ['retval', 'out'], POINTER(POINTER(IServiceDescriptionArray)), 'pVal' )),
    COMMETHOD([helpstring(u'Gets an IStringArray of service folder names.')], HRESULT, 'GetFolders',
              ( ['in'], BSTR, 'folderName' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'pVal' )),
]
################################################################
## code template for IServiceCatalog2 implementation
##class IServiceCatalog2_Impl(object):
##    def GetFolders(self, folderName):
##        u'Gets an IStringArray of service folder names.'
##        #return pVal
##
##    @property
##    def MessageVersion(self):
##        u'The message version this server version supports.'
##        #return ver
##
##    @property
##    def ServiceDescriptionsEx(self, folderName):
##        u'An array of the web service descriptions in the web service catalog.'
##        #return pVal
##
##    @property
##    def MessageFormats(self):
##        u'The message formats supported by the web services in the catalog.'
##        #return msgFormats
##

IServiceCatalog3._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates whether the service catalog requires tokens for authentication.')], HRESULT, 'RequiresTokens',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'RequiresTokens' )),
    COMMETHOD(['propget', helpstring(u'Token service url.')], HRESULT, 'TokenServiceURL',
              ( ['retval', 'out'], POINTER(BSTR), 'TokenServiceURL' )),
]
################################################################
## code template for IServiceCatalog3 implementation
##class IServiceCatalog3_Impl(object):
##    @property
##    def TokenServiceURL(self):
##        u'Token service url.'
##        #return TokenServiceURL
##
##    @property
##    def RequiresTokens(self):
##        u'Indicates whether the service catalog requires tokens for authentication.'
##        #return RequiresTokens
##

class IServiceDescription3(IServiceDescription2):
    _case_insensitive_ = True
    u'Provides access to members that control the properties of an ArcGIS Server web service description.'
    _iid_ = GUID('{E6CE2E4A-2F2B-4D2B-82B8-85FA5AECFFBC}')
    _idlflags_ = ['oleautomation']
IServiceDescription3._methods_ = [
    COMMETHOD(['propget', helpstring(u'The description of the service.')], HRESULT, 'Description',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'The description of the service.')], HRESULT, 'Description',
              ( ['in'], BSTR, 'pVal' )),
]
################################################################
## code template for IServiceDescription3 implementation
##class IServiceDescription3_Impl(object):
##    def _get(self):
##        u'The description of the service.'
##        #return pVal
##    def _set(self, pVal):
##        u'The description of the service.'
##    Description = property(_get, _set, doc = _set.__doc__)
##

class Role(CoClass):
    _reg_clsid_ = GUID('{A6A0C990-8EAE-4EE5-8A29-10A897661B8F}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{18F2FC71-6B30-45B9-B101-037A8B868B66}', 10, 2)
class IRole(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Interface that represents a role in the role store.'
    _iid_ = GUID('{CA90AF27-E384-4E25-9F75-0B33F8F6148B}')
    _idlflags_ = ['oleautomation']
Role._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo, IRole]

class IServerDirectoryInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to properties of a server directory.'
    _iid_ = GUID('{CF180145-BCFE-4D6F-AC53-3B9E127AF840}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriServerDirectoryCleaningMode'
esriSDCNone = 0
esriSDCSliding = 1
esriSDCAbsolute = 2
esriServerDirectoryCleaningMode = c_int # enum
IServerDirectoryInfo._methods_ = [
    COMMETHOD(['propget', helpstring(u'The path of the output directory.')], HRESULT, 'Path',
              ( ['retval', 'out'], POINTER(BSTR), 'pPath' )),
    COMMETHOD(['propget', helpstring(u'The URL of the virtual directory that maps to the physical directory as described by the Path property.')], HRESULT, 'URL',
              ( ['retval', 'out'], POINTER(BSTR), 'pUrl' )),
    COMMETHOD(['propget', helpstring(u'The description of the server directory.')], HRESULT, 'Description',
              ( ['retval', 'out'], POINTER(BSTR), 'pText' )),
    COMMETHOD(['propget', helpstring(u'The mode by which the files in the server directory are cleaned (by age, by size or none).')], HRESULT, 'CleaningMode',
              ( ['retval', 'out'], POINTER(esriServerDirectoryCleaningMode), 'pMode' )),
    COMMETHOD(['propget', helpstring(u'The maximum age (in seconds) a file can be in the server directory before it is deleted, if the cleaning mode is by file age.')], HRESULT, 'MaxFileAge',
              ( ['retval', 'out'], POINTER(c_int), 'pAge' )),
]
################################################################
## code template for IServerDirectoryInfo implementation
##class IServerDirectoryInfo_Impl(object):
##    @property
##    def URL(self):
##        u'The URL of the virtual directory that maps to the physical directory as described by the Path property.'
##        #return pUrl
##
##    @property
##    def Path(self):
##        u'The path of the output directory.'
##        #return pPath
##
##    @property
##    def MaxFileAge(self):
##        u'The maximum age (in seconds) a file can be in the server directory before it is deleted, if the cleaning mode is by file age.'
##        #return pAge
##
##    @property
##    def CleaningMode(self):
##        u'The mode by which the files in the server directory are cleaned (by age, by size or none).'
##        #return pMode
##
##    @property
##    def Description(self):
##        u'The description of the server directory.'
##        #return pText
##

class ServerObjectTypeInfo(CoClass):
    u'The ServerObjectTypeInfo object which provides information about server object types to users without administrative privileges to the ArcGIS server.'
    _reg_clsid_ = GUID('{C28C537E-1ECF-4CEF-B29A-C9B0082C5F0C}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{18F2FC71-6B30-45B9-B101-037A8B868B66}', 10, 2)
class IServerObjectTypeInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to properties of a server object type.'
    _iid_ = GUID('{1EF2395D-81EB-41FD-AA34-33E9FE2D8968}')
    _idlflags_ = ['oleautomation']
class IServerObjectTypeInfo2(IServerObjectTypeInfo):
    _case_insensitive_ = True
    u'Provides access to properties of a server object type.'
    _iid_ = GUID('{9EE9AA24-DFCB-4DE5-9091-FCABAC13A7E1}')
    _idlflags_ = ['oleautomation']
class IServerObjectTypeInfo3(IServerObjectTypeInfo2):
    _case_insensitive_ = True
    u'Provides access to properties of a server object type.'
    _iid_ = GUID('{AC43C070-1627-4C6D-9532-BC80CFD82C71}')
    _idlflags_ = ['oleautomation']
ServerObjectTypeInfo._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IServerObjectTypeInfo, IServerObjectTypeInfo2, IServerObjectTypeInfo3]

class IServiceCatalogAdmin(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the contents of an ArcGIS Server web services catalog.'
    _iid_ = GUID('{34013770-2AEF-4A0E-93A3-6C7D1BFC0A6A}')
    _idlflags_ = ['oleautomation']
IServiceCatalogAdmin._methods_ = [
    COMMETHOD([helpstring(u'Creates a new web service description.')], HRESULT, 'CreateServiceDescription',
              ( ['retval', 'out'], POINTER(POINTER(IServiceDescription)), 'ServiceDescription' )),
    COMMETHOD([helpstring(u'Creates a new array of web service descriptions.')], HRESULT, 'CreateServiceDescriptionArray',
              ( ['retval', 'out'], POINTER(POINTER(IServiceDescriptionArray)), 'array' )),
    COMMETHOD(['propputref', helpstring(u'The array of the web service descriptions for the web service catalog.')], HRESULT, 'ServiceDescriptions',
              ( ['in'], POINTER(IServiceDescriptionArray), 'rhs' )),
    COMMETHOD([helpstring(u'The WSDL for a specified service.')], HRESULT, 'GetDescriptionDocument',
              ( ['in'], BSTR, 'serviceName' ),
              ( ['in'], BSTR, 'serviceType' ),
              ( ['in'], BSTR, 'serviceURL' ),
              ( ['retval', 'out'], POINTER(_midlSAFEARRAY(c_ubyte)), 'doc' )),
    COMMETHOD([helpstring(u'The WSDL for the Service Catalog.')], HRESULT, 'GetCatalogDescriptionDocument',
              ( ['in'], BSTR, 'catalogName' ),
              ( ['in'], BSTR, 'catalogUrl' ),
              ( ['retval', 'out'], POINTER(_midlSAFEARRAY(c_ubyte)), 'doc' )),
]
################################################################
## code template for IServiceCatalogAdmin implementation
##class IServiceCatalogAdmin_Impl(object):
##    def CreateServiceDescription(self):
##        u'Creates a new web service description.'
##        #return ServiceDescription
##
##    def GetCatalogDescriptionDocument(self, catalogName, catalogUrl):
##        u'The WSDL for the Service Catalog.'
##        #return doc
##
##    def GetDescriptionDocument(self, serviceName, serviceType, serviceURL):
##        u'The WSDL for a specified service.'
##        #return doc
##
##    def CreateServiceDescriptionArray(self):
##        u'Creates a new array of web service descriptions.'
##        #return array
##
##    def ServiceDescriptions(self, rhs):
##        u'The array of the web service descriptions for the web service catalog.'
##        #return 
##

IEnumServerObjectTypeInfo._methods_ = [
    COMMETHOD([helpstring(u'Returns the next ServerObjectTypeInfo in the enumeration.')], HRESULT, 'Next',
              ( ['retval', 'out'], POINTER(POINTER(IServerObjectTypeInfo)), 'nextInfo' )),
    COMMETHOD([helpstring(u'Starts the enumeration at the beginning.')], HRESULT, 'Reset'),
    COMMETHOD(['propget', helpstring(u'The number of ServerObjectTypeInfos in the enumeration.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
]
################################################################
## code template for IEnumServerObjectTypeInfo implementation
##class IEnumServerObjectTypeInfo_Impl(object):
##    def Reset(self):
##        u'Starts the enumeration at the beginning.'
##        #return 
##
##    @property
##    def Count(self):
##        u'The number of ServerObjectTypeInfos in the enumeration.'
##        #return pVal
##
##    def Next(self):
##        u'Returns the next ServerObjectTypeInfo in the enumeration.'
##        #return nextInfo
##

class IServerObjectConfigurationInfo2(IServerObjectConfigurationInfo):
    _case_insensitive_ = True
    u'Provides access to the properties of a server object configuration with extensions.'
    _iid_ = GUID('{765EE3DB-2A65-41ED-9619-482BBC48192D}')
    _idlflags_ = ['oleautomation']
IServerObjectConfigurationInfo2._methods_ = [
    COMMETHOD(['propget', helpstring(u'An array of the registered server object extensions for a given configuration.')], HRESULT, 'Extensions',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IEnumBSTR)), 'ppEnum' )),
    COMMETHOD(['propget', helpstring(u'Auxiliary Information for the server objects created by the server object configuration ?passive properties only.')], HRESULT, 'Info',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'ppInfo' )),
    COMMETHOD(['propget', helpstring(u'The extension-dependent info for the server object configuration.')], HRESULT, 'ExtensionInfo',
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'ppExtProperties' )),
]
################################################################
## code template for IServerObjectConfigurationInfo2 implementation
##class IServerObjectConfigurationInfo2_Impl(object):
##    @property
##    def Info(self):
##        u'Auxiliary Information for the server objects created by the server object configuration ?passive properties only.'
##        #return ppInfo
##
##    @property
##    def ExtensionInfo(self, Name):
##        u'The extension-dependent info for the server object configuration.'
##        #return ppExtProperties
##
##    @property
##    def Extensions(self):
##        u'An array of the registered server object extensions for a given configuration.'
##        #return ppEnum
##

class IServerTimeRange(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that report the actual time range for GIS server statistics reported by IServerStatstics to administrators.'
    _iid_ = GUID('{37786A30-FEC4-4EA4-953E-DAC6B69C716D}')
    _idlflags_ = ['oleautomation']
IServerTimeRange._methods_ = [
    COMMETHOD(['propget', helpstring(u'The start time for the period that the statistics represent.')], HRESULT, 'StartTime',
              ( ['retval', 'out'], POINTER(c_double), 'pTime' )),
    COMMETHOD(['propget', helpstring(u'The end time for the period that the statistics represent.')], HRESULT, 'EndTime',
              ( ['retval', 'out'], POINTER(c_double), 'pTime' )),
]
################################################################
## code template for IServerTimeRange implementation
##class IServerTimeRange_Impl(object):
##    @property
##    def EndTime(self):
##        u'The end time for the period that the statistics represent.'
##        #return pTime
##
##    @property
##    def StartTime(self):
##        u'The start time for the period that the statistics represent.'
##        #return pTime
##

class IServerObjectType3(IServerObjectType2):
    _case_insensitive_ = True
    u'Provides access to methods, for administrators, that control the behavior and properties of a server object type.'
    _iid_ = GUID('{C54DD682-295A-4F38-93E3-7DA20DCA88C8}')
    _idlflags_ = ['oleautomation']
class IServerObjectType4(IServerObjectType3):
    _case_insensitive_ = True
    u'Provides access to methods, for administrators, that control the behavior and properties of a server object type.'
    _iid_ = GUID('{6640B74D-69CE-4D7F-8222-AD46936C1799}')
    _idlflags_ = ['oleautomation']
IServerObjectType3._methods_ = [
    COMMETHOD(['propget', helpstring(u'Limits the number of configurations that can be created of this server object type.')], HRESULT, 'ConfigurationsLimit',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Limits the number of configurations that can be created of this server object type.')], HRESULT, 'ConfigurationsLimit',
              ( ['in'], c_int, 'pVal' )),
]
################################################################
## code template for IServerObjectType3 implementation
##class IServerObjectType3_Impl(object):
##    def _get(self):
##        u'Limits the number of configurations that can be created of this server object type.'
##        #return pVal
##    def _set(self, pVal):
##        u'Limits the number of configurations that can be created of this server object type.'
##    ConfigurationsLimit = property(_get, _set, doc = _set.__doc__)
##

IServerObjectType4._methods_ = [
    COMMETHOD(['propputref', helpstring(u'Auxiliary information for the server objects type.')], HRESULT, 'Info',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'props' )),
    COMMETHOD(['propget', helpstring(u'Auxiliary information for the server objects type.')], HRESULT, 'Info',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'props' )),
]
################################################################
## code template for IServerObjectType4 implementation
##class IServerObjectType4_Impl(object):
##    @property
##    def Info(self, props):
##        u'Auxiliary information for the server objects type.'
##        #return 
##

class IServerMachineStatus(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the properties of the status of a specific SOC machine.'
    _iid_ = GUID('{67E836A4-01F1-450C-97BE-21AB9A3F3C11}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriAccessLevel'
esriAccessAll = 0
esriAccessPublic = 1
esriAccessPrivate = 2
esriAccessLevel = c_int # enum
IServerMachineStatus._methods_ = [
    COMMETHOD(['propget', helpstring(u'The number of server object instances currently running in this SOC machine.')], HRESULT, 'InstanceCount',
              ( ['in'], esriAccessLevel, 'access' ),
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD(['propget', helpstring(u'The number of currently running server object instances in use by clients of this SOC machine.')], HRESULT, 'InstanceInUseCount',
              ( ['in'], esriAccessLevel, 'access' ),
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Indicates if machine is connected and can be used by server(true) or not(false).')], HRESULT, 'Enabled',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
]
################################################################
## code template for IServerMachineStatus implementation
##class IServerMachineStatus_Impl(object):
##    @property
##    def Enabled(self):
##        u'Indicates if machine is connected and can be used by server(true) or not(false).'
##        #return pVal
##
##    @property
##    def InstanceCount(self, access):
##        u'The number of server object instances currently running in this SOC machine.'
##        #return pVal
##
##    @property
##    def InstanceInUseCount(self, access):
##        u'The number of currently running server object instances in use by clients of this SOC machine.'
##        #return pVal
##

IServerObjectTypeInfo._methods_ = [
    COMMETHOD(['propget', helpstring(u'Name of the server object type.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'Description of the server object type.')], HRESULT, 'Description',
              ( ['retval', 'out'], POINTER(BSTR), 'desc' )),
]
################################################################
## code template for IServerObjectTypeInfo implementation
##class IServerObjectTypeInfo_Impl(object):
##    @property
##    def Name(self):
##        u'Name of the server object type.'
##        #return Name
##
##    @property
##    def Description(self):
##        u'Description of the server object type.'
##        #return desc
##

class IServerMachineInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides information about specific Server Machine.'
    _iid_ = GUID('{76C3BBA1-AACF-40A1-BDEE-B3FA28840979}')
    _idlflags_ = ['oleautomation']
IServerMachineInfo._methods_ = [
    COMMETHOD(['propget', helpstring(u'Number of processors.')], HRESULT, 'NumberOfProcessors',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
]
################################################################
## code template for IServerMachineInfo implementation
##class IServerMachineInfo_Impl(object):
##    @property
##    def NumberOfProcessors(self):
##        u'Number of processors.'
##        #return pVal
##

class ServerStatisticsResults(CoClass):
    u'The ServerStatisticsResults object which returns a set of statistics, such as count, min, max, mean, for a single time period.'
    _reg_clsid_ = GUID('{893C42FD-C4B0-4B8C-B5B1-05C567867E40}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{18F2FC71-6B30-45B9-B101-037A8B868B66}', 10, 2)
ServerStatisticsResults._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStatisticsResults, IServerTimeRange]

class ServerMachineStatus(CoClass):
    u'The ServerMachineStatus object which reports the status of a server host machine.'
    _reg_clsid_ = GUID('{98053471-7D09-49D5-A3E0-D235E682331F}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{18F2FC71-6B30-45B9-B101-037A8B868B66}', 10, 2)
ServerMachineStatus._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IServerMachineStatus, IServerMachineInfo]

IServerObjectHelper._methods_ = [
    COMMETHOD(['propget', helpstring(u'Reference to a server object.')], HRESULT, 'ServerObject',
              ( ['retval', 'out'], POINTER(POINTER(IServerObject)), 'ppSO' )),
]
################################################################
## code template for IServerObjectHelper implementation
##class IServerObjectHelper_Impl(object):
##    @property
##    def ServerObject(self):
##        u'Reference to a server object.'
##        #return ppSO
##

class IServerLogQuery(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that configure a query to the ArcGIS Server logs.'
    _iid_ = GUID('{97D02AC6-AABB-4030-85F1-7280F28785DE}')
    _idlflags_ = ['oleautomation']
IServerLog._methods_ = [
    COMMETHOD([helpstring(u'Creates an IServerLogQuery for interrogating the ArcGIS server logs.')], HRESULT, 'CreateQuery',
              ( ['retval', 'out'], POINTER(POINTER(IServerLogQuery)), 'ppQuery' )),
    COMMETHOD([helpstring(u'Retrieves ArcGIS Server log records using an IServerLogQuery.')], HRESULT, 'GetLogRecords',
              ( ['in'], POINTER(IServerLogQuery), 'pQuery' ),
              ( ['retval', 'out'], POINTER(BSTR), 'results' )),
]
################################################################
## code template for IServerLog implementation
##class IServerLog_Impl(object):
##    def CreateQuery(self):
##        u'Creates an IServerLogQuery for interrogating the ArcGIS server logs.'
##        #return ppQuery
##
##    def GetLogRecords(self, pQuery):
##        u'Retrieves ArcGIS Server log records using an IServerLogQuery.'
##        #return results
##

class ServerObjectConfigurationStatus(CoClass):
    u'The ServerObjectConfgurationStatus object which reports the status of a server object configuration.'
    _reg_clsid_ = GUID('{DA266136-E040-4D0C-9B67-BA2553FB3E16}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{18F2FC71-6B30-45B9-B101-037A8B868B66}', 10, 2)
ServerObjectConfigurationStatus._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IServerObjectConfigurationStatus]

IGPServerHelper._methods_ = [
    COMMETHOD([helpstring(u'Initializes the helper with the job registery and jobs directory.')], HRESULT, 'Init',
              ( ['in'], BSTR, 'jobRegistryPath' ),
              ( ['in'], BSTR, 'jobsDirectoryPath' )),
    COMMETHOD([helpstring(u'Writes a SOAP job result to the job directory.')], HRESULT, 'WriteStringJobResult',
              ( ['in'], BSTR, 'jobID' ),
              ( ['in'], BSTR, 'serviceName' ),
              ( ['in'], BSTR, 'serviceType' ),
              ( ['in'], BSTR, 'result' )),
    COMMETHOD([helpstring(u'Writes a binary job result to the job directory.')], HRESULT, 'WriteBinaryJobResult',
              ( ['in'], BSTR, 'jobID' ),
              ( ['in'], BSTR, 'serviceName' ),
              ( ['in'], BSTR, 'serviceType' ),
              ( ['in'], _midlSAFEARRAY(c_ubyte), 'result' )),
    COMMETHOD([helpstring(u'Writes a REST job result to the job directory.')], HRESULT, 'WriteRESTJobResult',
              ( ['in'], BSTR, 'jobID' ),
              ( ['in'], BSTR, 'serviceName' ),
              ( ['in'], BSTR, 'serviceType' ),
              ( ['in'], BSTR, 'responseProperties' ),
              ( ['in'], _midlSAFEARRAY(c_ubyte), 'result' )),
    COMMETHOD([helpstring(u'Gets the type of the request from a string message.')], HRESULT, 'GetStringRequestMessageType',
              ( ['in'], BSTR, 'request' ),
              ( ['retval', 'out'], POINTER(BSTR), 'pType' )),
    COMMETHOD([helpstring(u'Gets the type of the request from a binary message.')], HRESULT, 'GetBinaryRequestMessageType',
              ( ['in'], _midlSAFEARRAY(c_ubyte), 'request' ),
              ( ['retval', 'out'], POINTER(BSTR), 'pType' )),
    COMMETHOD([helpstring(u'Extracts the job ID from a Soap message that conatins this information.')], HRESULT, 'GetJobIDFromStringResponse',
              ( ['in'], BSTR, 'response' ),
              ( ['retval', 'out'], POINTER(BSTR), 'pJobID' )),
    COMMETHOD([helpstring(u'Extracts the job ID from a binary message that contains this information.')], HRESULT, 'GetJobIDFromBinaryResponse',
              ( ['in'], _midlSAFEARRAY(c_ubyte), 'response' ),
              ( ['retval', 'out'], POINTER(BSTR), 'pJobID' )),
    COMMETHOD([helpstring(u'Gets the string job definition for given a job ID.')], HRESULT, 'GetStringJobDefinition',
              ( ['in'], BSTR, 'jobID' ),
              ( ['in'], BSTR, 'serviceName' ),
              ( ['in'], BSTR, 'serviceType' ),
              ( ['retval', 'out'], POINTER(BSTR), 'pJobDefinition' )),
    COMMETHOD([helpstring(u'Gets the binary job definition for a given job ID.')], HRESULT, 'GetBinaryJobDefinition',
              ( ['in'], BSTR, 'jobID' ),
              ( ['in'], BSTR, 'serviceName' ),
              ( ['in'], BSTR, 'serviceType' ),
              ( ['retval', 'out'], POINTER(_midlSAFEARRAY(c_ubyte)), 'ppJobDefinition' )),
    COMMETHOD([helpstring(u'Returns the REST job definition for a given job ID.')], HRESULT, 'GetRESTJobDefinition',
              ( ['in'], BSTR, 'jobID' ),
              ( ['in'], BSTR, 'serviceName' ),
              ( ['in'], BSTR, 'serviceType' ),
              ( ['out'], POINTER(BSTR), 'resourceName' ),
              ( ['out'], POINTER(BSTR), 'operationName' ),
              ( ['out'], POINTER(BSTR), 'operationInput' ),
              ( ['out'], POINTER(BSTR), 'outputFormat' ),
              ( ['out'], POINTER(BSTR), 'requestProperties' )),
    COMMETHOD([helpstring(u'Writes a specific job message and status for a given job ID.')], HRESULT, 'WriteJobStatusAndMessage',
              ( ['in'], BSTR, 'jobID' ),
              ( ['in'], BSTR, 'serviceName' ),
              ( ['in'], BSTR, 'serviceType' ),
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.esriJobStatus, 'Status' ),
              ( ['in'], BSTR, 'message' )),
    COMMETHOD([helpstring(u'Returns the status of a job.')], HRESULT, 'GetJobStatus',
              ( ['in'], BSTR, 'jobID' ),
              ( ['in'], BSTR, 'serviceName' ),
              ( ['in'], BSTR, 'serviceType' ),
              ( ['retval', 'out'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.esriJobStatus), 'pStatus' )),
]
################################################################
## code template for IGPServerHelper implementation
##class IGPServerHelper_Impl(object):
##    def WriteStringJobResult(self, jobID, serviceName, serviceType, result):
##        u'Writes a SOAP job result to the job directory.'
##        #return 
##
##    def WriteBinaryJobResult(self, jobID, serviceName, serviceType, result):
##        u'Writes a binary job result to the job directory.'
##        #return 
##
##    def GetBinaryRequestMessageType(self, request):
##        u'Gets the type of the request from a binary message.'
##        #return pType
##
##    def GetJobIDFromBinaryResponse(self, response):
##        u'Extracts the job ID from a binary message that contains this information.'
##        #return pJobID
##
##    def WriteJobStatusAndMessage(self, jobID, serviceName, serviceType, Status, message):
##        u'Writes a specific job message and status for a given job ID.'
##        #return 
##
##    def Init(self, jobRegistryPath, jobsDirectoryPath):
##        u'Initializes the helper with the job registery and jobs directory.'
##        #return 
##
##    def GetJobIDFromStringResponse(self, response):
##        u'Extracts the job ID from a Soap message that conatins this information.'
##        #return pJobID
##
##    def GetStringJobDefinition(self, jobID, serviceName, serviceType):
##        u'Gets the string job definition for given a job ID.'
##        #return pJobDefinition
##
##    def GetStringRequestMessageType(self, request):
##        u'Gets the type of the request from a string message.'
##        #return pType
##
##    def WriteRESTJobResult(self, jobID, serviceName, serviceType, responseProperties, result):
##        u'Writes a REST job result to the job directory.'
##        #return 
##
##    def GetRESTJobDefinition(self, jobID, serviceName, serviceType):
##        u'Returns the REST job definition for a given job ID.'
##        #return resourceName, operationName, operationInput, outputFormat, requestProperties
##
##    def GetBinaryJobDefinition(self, jobID, serviceName, serviceType):
##        u'Gets the binary job definition for a given job ID.'
##        #return ppJobDefinition
##
##    def GetJobStatus(self, jobID, serviceName, serviceType):
##        u'Returns the status of a job.'
##        #return pStatus
##

IServer._methods_ = [
    COMMETHOD(['propget', helpstring(u'Gets the server object manager for the connected GIS server.')], HRESULT, 'ServerObjectManager',
              ( ['retval', 'out'], POINTER(POINTER(IServerObjectManager)), 'mgr' )),
    COMMETHOD(['propget', helpstring(u'Gets the server object admin for the connected GIS server.')], HRESULT, 'ServerObjectAdmin',
              ( ['retval', 'out'], POINTER(POINTER(IServerObjectAdmin)), 'admin' )),
]
################################################################
## code template for IServer implementation
##class IServer_Impl(object):
##    @property
##    def ServerObjectAdmin(self):
##        u'Gets the server object admin for the connected GIS server.'
##        #return admin
##
##    @property
##    def ServerObjectManager(self):
##        u'Gets the server object manager for the connected GIS server.'
##        #return mgr
##

IServer2._methods_ = [
    COMMETHOD(['propget', helpstring(u'Gets the server objcet manager of the connected ArcGIS server for the user specified by userInfo.')], HRESULT, 'ServerObjectManager2',
              ( ['in'], BSTR, 'UserInfo' ),
              ( ['retval', 'out'], POINTER(POINTER(IServerObjectManager)), 'mgr' )),
]
################################################################
## code template for IServer2 implementation
##class IServer2_Impl(object):
##    @property
##    def ServerObjectManager2(self, UserInfo):
##        u'Gets the server objcet manager of the connected ArcGIS server for the user specified by userInfo.'
##        #return mgr
##

class IEnumServerObjectExtensionTypeInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that enumerate through the registered server object extension types.'
    _iid_ = GUID('{975D6F9A-0849-4DE7-BD0D-9615925A098D}')
    _idlflags_ = ['oleautomation']
IServerObjectManager2._methods_ = [
    COMMETHOD(['propget', helpstring(u'The properties of the underlying system hardware and software.')], HRESULT, 'SystemInfo',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'ppInfo' )),
    COMMETHOD([helpstring(u"An enumerator over all the ArcGIS server's ServerObjectExtensionTypeInfos.")], HRESULT, 'GetExtensionTypeInfos',
              ( ['in'], BSTR, 'SOTypeName' ),
              ( ['retval', 'out'], POINTER(POINTER(IEnumServerObjectExtensionTypeInfo)), 'ppInfos' )),
    COMMETHOD([helpstring(u"An enumerator over all the ArcGIS server's ServerObjectExtensionInfos in a given folder.")], HRESULT, 'GetConfigurationInfosEx',
              ( ['in'], BSTR, 'folderName' ),
              ( ['retval', 'out'], POINTER(POINTER(IEnumServerObjectConfigurationInfo)), 'ppEnum' )),
    COMMETHOD([helpstring(u'An array of folder names in the server configuration folder.')], HRESULT, 'GetFolders',
              ( ['in'], BSTR, 'folderName' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IEnumBSTR)), 'ppEnum' )),
    COMMETHOD(['propget', helpstring(u'Properties associated with a server configuration folder.')], HRESULT, 'FolderInfo',
              ( ['in'], BSTR, 'folderName' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'ppInfo' )),
    COMMETHOD([helpstring(u'Get the configuration status for a server object configuration with the specified Name and TypeName.')], HRESULT, 'GetConfigurationStatus',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], BSTR, 'TypeName' ),
              ( ['retval', 'out'], POINTER(POINTER(IServerObjectConfigurationStatus)), 'ppStatus' )),
]
################################################################
## code template for IServerObjectManager2 implementation
##class IServerObjectManager2_Impl(object):
##    @property
##    def FolderInfo(self, folderName):
##        u'Properties associated with a server configuration folder.'
##        #return ppInfo
##
##    def GetFolders(self, folderName):
##        u'An array of folder names in the server configuration folder.'
##        #return ppEnum
##
##    @property
##    def SystemInfo(self):
##        u'The properties of the underlying system hardware and software.'
##        #return ppInfo
##
##    def GetConfigurationStatus(self, Name, TypeName):
##        u'Get the configuration status for a server object configuration with the specified Name and TypeName.'
##        #return ppStatus
##
##    def GetConfigurationInfosEx(self, folderName):
##        u"An enumerator over all the ArcGIS server's ServerObjectExtensionInfos in a given folder."
##        #return ppEnum
##
##    def GetExtensionTypeInfos(self, SOTypeName):
##        u"An enumerator over all the ArcGIS server's ServerObjectExtensionTypeInfos."
##        #return ppInfos
##

IServerObjectManager3._methods_ = [
    COMMETHOD([helpstring(u"An enumerator over the ArcGIS server's ServerObjectExtensionInfos in a given folder.")], HRESULT, 'GetConfigurationInfosEx2',
              ( ['in'], BSTR, 'folderName' ),
              ( ['in'], esriConfigurationStatus, 'stat' ),
              ( ['retval', 'out'], POINTER(POINTER(IEnumServerObjectConfigurationInfo)), 'ppEnum' )),
]
################################################################
## code template for IServerObjectManager3 implementation
##class IServerObjectManager3_Impl(object):
##    def GetConfigurationInfosEx2(self, folderName, stat):
##        u"An enumerator over the ArcGIS server's ServerObjectExtensionInfos in a given folder."
##        #return ppEnum
##

class ServerObjectType(CoClass):
    u'The ServerObjectType object which defines the properties and behavior for server object types supported by the GIS server.'
    _reg_clsid_ = GUID('{3CF5C550-0D4F-4EB8-9E75-A65B274F3100}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{18F2FC71-6B30-45B9-B101-037A8B868B66}', 10, 2)
ServerObjectType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IServerObjectType, IServerObjectType2, IServerObjectType3, IServerObjectType4]


# values for enumeration 'esriServerStatEvent'
esriSSEContextCreated = 0
esriSSEContextCreationFailed = 1
esriSSEContextCreationTimeout = 2
esriSSEContextReleased = 3
esriSSEContextUsageTimeout = 4
esriSSEServerObjectCreated = 5
esriSSEServerObjectCreationFailed = 6
esriSSELogError = 7
esriSSELogWarning = 8
esriServerStatEvent = c_int # enum

# values for enumeration 'esriServerStatFunction'
esriSSFCount = 0
esriSSFMinimum = 1
esriSSFMaximum = 2
esriSSFSum = 3
esriSSFSumSquares = 4
esriSSFMean = 5
esriSSFStandardDeviation = 6
esriServerStatFunction = c_int # enum

# values for enumeration 'esriServerTimePeriod'
esriSTPNone = 0
esriSTPSecond = 1
esriSTPMinute = 2
esriSTPHour = 3
esriSTPDay = 4
esriServerTimePeriod = c_int # enum
IServerStatistics._methods_ = [
    COMMETHOD([helpstring(u'Clears out the currently gathered statistics.')], HRESULT, 'Reset'),
    COMMETHOD([helpstring(u'Gets a specific statistic (such as total count of server contexts created) for a specified time period.')], HRESULT, 'GetSpecificStatisticForTimeIntervals',
              ( ['in'], esriServerStatEvent, 'event' ),
              ( ['in'], esriServerStatFunction, 'function' ),
              ( ['in'], esriServerTimePeriod, 'period' ),
              ( ['in'], c_int, 'index' ),
              ( ['in'], c_int, 'length' ),
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], BSTR, 'Type' ),
              ( ['in'], BSTR, 'Machine' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDoubleArray)), 'ppArray' )),
    COMMETHOD([helpstring(u'Gets a set of statistics, such as count, min, max, mean for an event (such as context usage time) for a specified time period.')], HRESULT, 'GetAllStatisticsForTimeInterval',
              ( ['in'], esriServerStatEvent, 'event' ),
              ( ['in'], esriServerTimePeriod, 'period' ),
              ( ['in'], c_int, 'index' ),
              ( ['in'], c_int, 'length' ),
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], BSTR, 'Type' ),
              ( ['in'], BSTR, 'Machine' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStatisticsResults)), 'ppResults' )),
]
################################################################
## code template for IServerStatistics implementation
##class IServerStatistics_Impl(object):
##    def Reset(self):
##        u'Clears out the currently gathered statistics.'
##        #return 
##
##    def GetSpecificStatisticForTimeIntervals(self, event, function, period, index, length, Name, Type, Machine):
##        u'Gets a specific statistic (such as total count of server contexts created) for a specified time period.'
##        #return ppArray
##
##    def GetAllStatisticsForTimeInterval(self, event, period, index, length, Name, Type, Machine):
##        u'Gets a set of statistics, such as count, min, max, mean for an event (such as context usage time) for a specified time period.'
##        #return ppResults
##

class ISOMController(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that start and stop ArcGIS server.'
    _iid_ = GUID('{E869D31E-F218-4CF7-BD51-AB5424FB7FB8}')
    _idlflags_ = ['oleautomation']
ISOMController._methods_ = [
    COMMETHOD([helpstring(u'Starts the SOM.')], HRESULT, 'Start'),
    COMMETHOD([helpstring(u'Stops the SOM.')], HRESULT, 'Stop'),
    COMMETHOD(['propget', helpstring(u'Indicates if the server is started(true) or not(false).')], HRESULT, 'Started',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
]
################################################################
## code template for ISOMController implementation
##class ISOMController_Impl(object):
##    @property
##    def Started(self):
##        u'Indicates if the server is started(true) or not(false).'
##        #return pVal
##
##    def Start(self):
##        u'Starts the SOM.'
##        #return 
##
##    def Stop(self):
##        u'Stops the SOM.'
##        #return 
##

class IUser(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Interface that represents a user in the user store.'
    _iid_ = GUID('{2B8A2B7F-01BF-4951-8AA7-5161AD46EF35}')
    _idlflags_ = ['oleautomation']
IUser._methods_ = [
    COMMETHOD([helpstring(u'Sets the user name.')], HRESULT, 'SetUsername',
              ( ['in'], BSTR, 'UserName' )),
    COMMETHOD([helpstring(u'Returns the user name.')], HRESULT, 'GetUsername',
              ( ['retval', 'out'], POINTER(BSTR), 'UserName' )),
    COMMETHOD([helpstring(u'Sets the user password.')], HRESULT, 'SetPassword',
              ( ['in'], BSTR, 'Password' )),
    COMMETHOD([helpstring(u'Returns the user password.')], HRESULT, 'GetPassword',
              ( ['retval', 'out'], POINTER(BSTR), 'Password' )),
    COMMETHOD([helpstring(u'Sets the user description.')], HRESULT, 'SetDescription',
              ( ['in'], BSTR, 'Description' )),
    COMMETHOD([helpstring(u'Returns the user description.')], HRESULT, 'GetDescription',
              ( ['retval', 'out'], POINTER(BSTR), 'Description' )),
    COMMETHOD([helpstring(u"Sets the user's email.")], HRESULT, 'SetEmail',
              ( ['in'], BSTR, 'email' )),
    COMMETHOD([helpstring(u"Returns the user's email.")], HRESULT, 'GetEmail',
              ( ['retval', 'out'], POINTER(BSTR), 'email' )),
    COMMETHOD([helpstring(u"Sets the user's full name.")], HRESULT, 'SetFullname',
              ( ['in'], BSTR, 'fullname' )),
    COMMETHOD([helpstring(u"Returns the user's full name.")], HRESULT, 'GetFullname',
              ( ['retval', 'out'], POINTER(BSTR), 'fullname' )),
    COMMETHOD([helpstring(u"Sets the user's secret question.")], HRESULT, 'SetSecretQuestion',
              ( ['in'], BSTR, 'secretQuestion' )),
    COMMETHOD([helpstring(u"Returns the user's secret question.")], HRESULT, 'GetSecretQuestion',
              ( ['retval', 'out'], POINTER(BSTR), 'secretQuestion' )),
    COMMETHOD([helpstring(u"Sets the user's answer to the secret question.")], HRESULT, 'SetSecretAnswer',
              ( ['in'], BSTR, 'secretAnswer' )),
    COMMETHOD([helpstring(u"Returns the user's answer to secret question.")], HRESULT, 'GetSecretAnswer',
              ( ['retval', 'out'], POINTER(BSTR), 'secretAnswer' )),
]
################################################################
## code template for IUser implementation
##class IUser_Impl(object):
##    def SetDescription(self, Description):
##        u'Sets the user description.'
##        #return 
##
##    def SetSecretQuestion(self, secretQuestion):
##        u"Sets the user's secret question."
##        #return 
##
##    def SetUsername(self, UserName):
##        u'Sets the user name.'
##        #return 
##
##    def GetPassword(self):
##        u'Returns the user password.'
##        #return Password
##
##    def SetSecretAnswer(self, secretAnswer):
##        u"Sets the user's answer to the secret question."
##        #return 
##
##    def GetSecretQuestion(self):
##        u"Returns the user's secret question."
##        #return secretQuestion
##
##    def GetDescription(self):
##        u'Returns the user description.'
##        #return Description
##
##    def SetEmail(self, email):
##        u"Sets the user's email."
##        #return 
##
##    def GetSecretAnswer(self):
##        u"Returns the user's answer to secret question."
##        #return secretAnswer
##
##    def GetFullname(self):
##        u"Returns the user's full name."
##        #return fullname
##
##    def SetFullname(self, fullname):
##        u"Sets the user's full name."
##        #return 
##
##    def SetPassword(self, Password):
##        u'Sets the user password.'
##        #return 
##
##    def GetEmail(self):
##        u"Returns the user's email."
##        #return email
##
##    def GetUsername(self):
##        u'Returns the user name.'
##        #return UserName
##

class IDataStoreValidator(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Tests access to the data store.'
    _iid_ = GUID('{E7AD5E02-E595-4CB9-9B06-EC4F09122A3E}')
    _idlflags_ = ['oleautomation']
IDataStoreValidator._methods_ = [
    COMMETHOD([helpstring(u'Tests access to the data store.')], HRESULT, 'ValidateAccess',
              ( ['in'], BSTR, 'dataStore' ),
              ( ['in'], BSTR, 'dataStoreType' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'isValid' )),
]
################################################################
## code template for IDataStoreValidator implementation
##class IDataStoreValidator_Impl(object):
##    def ValidateAccess(self, dataStore, dataStoreType):
##        u'Tests access to the data store.'
##        #return isValid
##

IEnumServerObjectConfigurationInfo._methods_ = [
    COMMETHOD([helpstring(u'Returns the next ServerObjectConfigurationInfo in the enumeration.')], HRESULT, 'Next',
              ( ['retval', 'out'], POINTER(POINTER(IServerObjectConfigurationInfo)), 'nextInfo' )),
    COMMETHOD([helpstring(u'Starts the enumeration at the beginning.')], HRESULT, 'Reset'),
    COMMETHOD(['propget', helpstring(u'The number of ServerObjectConfigurationInfos in the enumeration.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
]
################################################################
## code template for IEnumServerObjectConfigurationInfo implementation
##class IEnumServerObjectConfigurationInfo_Impl(object):
##    def Reset(self):
##        u'Starts the enumeration at the beginning.'
##        #return 
##
##    @property
##    def Count(self):
##        u'The number of ServerObjectConfigurationInfos in the enumeration.'
##        #return pVal
##
##    def Next(self):
##        u'Returns the next ServerObjectConfigurationInfo in the enumeration.'
##        #return nextInfo
##


# values for enumeration 'esriServerDirectoryType'
esriSDTypeOutput = 0
esriSDTypeCache = 1
esriSDTypeJobs = 2
esriSDTypeIndex = 3
esriSDTypeInput = 4
esriSDTypeSystem = 5
esriSDTypeUploads = 6
esriSDTypeKML = 7
esriSDTypeJobRegistry = 8
esriSDTypeUnknown = 9
esriServerDirectoryType = c_int # enum
IServerEnvironmentXHelper._methods_ = [
    COMMETHOD([helpstring(u'Changes the log level for the logger configured in the server environment.')], HRESULT, 'ChangeLogLevel',
              ( ['in'], BSTR, 'newLogLevel' )),
    COMMETHOD([helpstring(u'Resets the job ID.')], HRESULT, 'ResetJobID'),
    COMMETHOD([helpstring(u'Sets the job ID in the server environment.')], HRESULT, 'SetJobID',
              ( ['in'], BSTR, 'jobID' )),
    COMMETHOD([helpstring(u'Adds a new server directory into the server environment.')], HRESULT, 'AddServerDirectory',
              ( ['in'], BSTR, 'dirPath' ),
              ( ['in'], BSTR, 'URL' ),
              ( ['in'], BSTR, 'Description' ),
              ( ['in'], esriServerDirectoryCleaningMode, 'CleaningMode' ),
              ( ['in'], c_int, 'MaxFileAge' ),
              ( ['in'], esriServerDirectoryType, 'Type' )),
    COMMETHOD([helpstring(u'Removes a server directory from the server environment.')], HRESULT, 'RemoveServerDirectory',
              ( ['in'], BSTR, 'dirPath' )),
    COMMETHOD([helpstring(u'Sets the user information into the server environment.')], HRESULT, 'SetUserInfo',
              ( ['in'], BSTR, 'UserInfo' )),
    COMMETHOD([helpstring(u'Sets the environment properties.')], HRESULT, 'SetEnvProperties',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'ipProps' )),
    COMMETHOD([helpstring(u'Adds or updates a property into the server environment.')], HRESULT, 'AddEnvProperty',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], BSTR, 'value' )),
    COMMETHOD([helpstring(u'Removes a property from the server environment.')], HRESULT, 'RemoveEnvProperty',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD([helpstring(u'Changes the machine name for the logger configured in the server environment.')], HRESULT, 'ChangeLogMachineName',
              ( ['in'], BSTR, 'newMachineName' )),
    COMMETHOD([helpstring(u'Changes the log directory for the logger configured in the server environment.')], HRESULT, 'ChangeLogDirectory',
              ( ['in'], BSTR, 'newLogDirectory' )),
    COMMETHOD([helpstring(u'Change the max log file size')], HRESULT, 'ChangeMaxLogFileSize',
              ( ['in'], c_int, 'maxLogFileSize' )),
    COMMETHOD([helpstring(u'Enable crash dump files generation')], HRESULT, 'EnableCrashDumpGeneration',
              ( ['in'], VARIANT_BOOL, 'bEnable' )),
]
################################################################
## code template for IServerEnvironmentXHelper implementation
##class IServerEnvironmentXHelper_Impl(object):
##    def ChangeLogDirectory(self, newLogDirectory):
##        u'Changes the log directory for the logger configured in the server environment.'
##        #return 
##
##    def SetJobID(self, jobID):
##        u'Sets the job ID in the server environment.'
##        #return 
##
##    def AddServerDirectory(self, dirPath, URL, Description, CleaningMode, MaxFileAge, Type):
##        u'Adds a new server directory into the server environment.'
##        #return 
##
##    def ChangeLogLevel(self, newLogLevel):
##        u'Changes the log level for the logger configured in the server environment.'
##        #return 
##
##    def ChangeLogMachineName(self, newMachineName):
##        u'Changes the machine name for the logger configured in the server environment.'
##        #return 
##
##    def SetEnvProperties(self, ipProps):
##        u'Sets the environment properties.'
##        #return 
##
##    def RemoveEnvProperty(self, Name):
##        u'Removes a property from the server environment.'
##        #return 
##
##    def RemoveServerDirectory(self, dirPath):
##        u'Removes a server directory from the server environment.'
##        #return 
##
##    def ChangeMaxLogFileSize(self, maxLogFileSize):
##        u'Change the max log file size'
##        #return 
##
##    def SetUserInfo(self, UserInfo):
##        u'Sets the user information into the server environment.'
##        #return 
##
##    def EnableCrashDumpGeneration(self, bEnable):
##        u'Enable crash dump files generation'
##        #return 
##
##    def ResetJobID(self):
##        u'Resets the job ID.'
##        #return 
##
##    def AddEnvProperty(self, Name, value):
##        u'Adds or updates a property into the server environment.'
##        #return 
##

class ServerStatisticsArray(CoClass):
    u'The ServerStatisticsArray object which returns an array of a specific statistic over a range of time periods.'
    _reg_clsid_ = GUID('{E6AF2747-73EE-43E4-A4B9-B0FE5EA33517}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{18F2FC71-6B30-45B9-B101-037A8B868B66}', 10, 2)
ServerStatisticsArray._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IDoubleArray, IServerTimeRange]

class IServerObjectHelper2(IServerObjectHelper):
    _case_insensitive_ = True
    u'Provides access to a holder for a reference to a server object.'
    _iid_ = GUID('{6EE30361-F7C6-4635-882E-FABC7A772BC4}')
    _idlflags_ = ['oleautomation']
IServerObjectHelper2._methods_ = [
    COMMETHOD(['propget', helpstring(u'Server object property.')], HRESULT, 'ServerObjectProperty',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'ppProps' )),
]
################################################################
## code template for IServerObjectHelper2 implementation
##class IServerObjectHelper2_Impl(object):
##    @property
##    def ServerObjectProperty(self):
##        u'Server object property.'
##        #return ppProps
##

class ServerDirectoryInfo(CoClass):
    u'The ServerDirectoryInfo object which provides access to properties of a server output directory.'
    _reg_clsid_ = GUID('{65997EFB-8ADB-49FF-9481-8B90CB84A5BF}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{18F2FC71-6B30-45B9-B101-037A8B868B66}', 10, 2)
class IServerDirectoryInfo2(IServerDirectoryInfo):
    _case_insensitive_ = True
    u'Provides access to properties of a server directory.'
    _iid_ = GUID('{2B0CC34C-E861-46EF-8BF0-308AB6113CE8}')
    _idlflags_ = ['oleautomation']
ServerDirectoryInfo._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IServerDirectoryInfo, IServerDirectoryInfo2]

class IRoleStore(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'An interface to access the role repository.'
    _iid_ = GUID('{5AC20C1A-CF77-44C7-9EAE-7BCD859E5AB8}')
    _idlflags_ = ['oleautomation']
IRoleStore._methods_ = [
    COMMETHOD([helpstring(u'Tests the connection to the role store.')], HRESULT, 'TestConnection',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'pProps' )),
    COMMETHOD([helpstring(u'Connects to a role store.')], HRESULT, 'Initialize',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'pProps' )),
    COMMETHOD([helpstring(u'Tests the connection to the role store.')], HRESULT, 'IsReadOnly',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsReadOnly' )),
    COMMETHOD([helpstring(u'Add a new role to the role store.')], HRESULT, 'AddRole',
              ( ['in'], POINTER(IRole), 'pRole' )),
    COMMETHOD([helpstring(u'Update an existing role in the role store.')], HRESULT, 'UpdateRole',
              ( ['in'], POINTER(IRole), 'pRole' )),
    COMMETHOD([helpstring(u'Deletes a role from role store.')], HRESULT, 'DeleteRole',
              ( ['in'], BSTR, 'rolename' )),
    COMMETHOD([helpstring(u'Returns a role from the role store.')], HRESULT, 'GetRole',
              ( ['in'], BSTR, 'rolename' ),
              ( ['retval', 'out'], POINTER(POINTER(IRole)), 'pRole' )),
    COMMETHOD([helpstring(u'Returns the total number of roles in the role store.')], HRESULT, 'GetTotalRoles',
              ( ['retval', 'out'], POINTER(c_int), 'totalRoles' )),
    COMMETHOD([helpstring(u'Returns a maxCount of roles from the role store that match a particular filter.')], HRESULT, 'GetAllRoles',
              ( ['in'], BSTR, 'filter' ),
              ( ['in'], c_int, 'maxCount' ),
              ( ['out'], POINTER(_midlSAFEARRAY(POINTER(IRole))), 'roles' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'hasMore' )),
    COMMETHOD([helpstring(u'Returns a pageSize of roles from the role store from the startIndex.')], HRESULT, 'GetAllRolesPaged',
              ( ['in'], c_int, 'StartIndex' ),
              ( ['in'], c_int, 'pageSize' ),
              ( ['out'], POINTER(_midlSAFEARRAY(POINTER(IRole))), 'roles' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'hasMore' )),
    COMMETHOD([helpstring(u'Assigns roles to a user.')], HRESULT, 'AssignRoles',
              ( ['in'], BSTR, 'UserName' ),
              ( ['in'], POINTER(_midlSAFEARRAY(BSTR)), 'rolenames' )),
    COMMETHOD([helpstring(u'Removes roles assigned to a user.')], HRESULT, 'RemoveRoles',
              ( ['in'], BSTR, 'UserName' ),
              ( ['in'], POINTER(_midlSAFEARRAY(BSTR)), 'rolenames' )),
    COMMETHOD([helpstring(u'Returns roles assigned to a user that match a filter upto a maxCount number.')], HRESULT, 'GetRolesForUser',
              ( ['in'], BSTR, 'UserName' ),
              ( ['in'], BSTR, 'filter' ),
              ( ['in'], c_int, 'maxCount' ),
              ( ['out'], POINTER(_midlSAFEARRAY(BSTR)), 'rolenames' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'hasMore' )),
    COMMETHOD([helpstring(u'Returns users within a role that match a filter upto a maxCount number.')], HRESULT, 'GetUsersWithinRole',
              ( ['in'], BSTR, 'rolename' ),
              ( ['in'], BSTR, 'filter' ),
              ( ['in'], c_int, 'maxCount' ),
              ( ['out'], POINTER(_midlSAFEARRAY(BSTR)), 'usernames' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'hasMore' )),
    COMMETHOD([helpstring(u'Adds users to a role.')], HRESULT, 'AddUsersToRole',
              ( ['in'], BSTR, 'rolename' ),
              ( ['in'], POINTER(_midlSAFEARRAY(BSTR)), 'usernames' )),
    COMMETHOD([helpstring(u'Removes users from a role.')], HRESULT, 'RemoveUsersFromRole',
              ( ['in'], BSTR, 'rolename' ),
              ( ['in'], POINTER(_midlSAFEARRAY(BSTR)), 'usernames' )),
]
################################################################
## code template for IRoleStore implementation
##class IRoleStore_Impl(object):
##    def RemoveUsersFromRole(self, rolename, usernames):
##        u'Removes users from a role.'
##        #return 
##
##    def GetUsersWithinRole(self, rolename, filter, maxCount):
##        u'Returns users within a role that match a filter upto a maxCount number.'
##        #return usernames, hasMore
##
##    def UpdateRole(self, pRole):
##        u'Update an existing role in the role store.'
##        #return 
##
##    def IsReadOnly(self):
##        u'Tests the connection to the role store.'
##        #return IsReadOnly
##
##    def GetAllRoles(self, filter, maxCount):
##        u'Returns a maxCount of roles from the role store that match a particular filter.'
##        #return roles, hasMore
##
##    def GetRolesForUser(self, UserName, filter, maxCount):
##        u'Returns roles assigned to a user that match a filter upto a maxCount number.'
##        #return rolenames, hasMore
##
##    def DeleteRole(self, rolename):
##        u'Deletes a role from role store.'
##        #return 
##
##    def RemoveRoles(self, UserName, rolenames):
##        u'Removes roles assigned to a user.'
##        #return 
##
##    def GetTotalRoles(self):
##        u'Returns the total number of roles in the role store.'
##        #return totalRoles
##
##    def TestConnection(self, pProps):
##        u'Tests the connection to the role store.'
##        #return 
##
##    def AddUsersToRole(self, rolename, usernames):
##        u'Adds users to a role.'
##        #return 
##
##    def Initialize(self, pProps):
##        u'Connects to a role store.'
##        #return 
##
##    def AddRole(self, pRole):
##        u'Add a new role to the role store.'
##        #return 
##
##    def GetRole(self, rolename):
##        u'Returns a role from the role store.'
##        #return pRole
##
##    def AssignRoles(self, UserName, rolenames):
##        u'Assigns roles to a user.'
##        #return 
##
##    def GetAllRolesPaged(self, StartIndex, pageSize):
##        u'Returns a pageSize of roles from the role store from the startIndex.'
##        #return roles, hasMore
##

class SOMController(CoClass):
    u'The SOMController object which provides access to members that start and stop ArcGIS server.'
    _reg_clsid_ = GUID('{049FC901-5750-46F2-8674-B883C99166C4}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{18F2FC71-6B30-45B9-B101-037A8B868B66}', 10, 2)
SOMController._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ISOMController]

class Library(object):
    u'Esri Server Object Library 10.2'
    name = u'esriServer'
    _reg_typelib_ = ('{18F2FC71-6B30-45B9-B101-037A8B868B66}', 10, 2)

IServerObject._methods_ = [
    COMMETHOD(['propget', helpstring(u'Name of the server object configuration that defines the server object.')], HRESULT, 'ConfigurationName',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'Type of the server object (MapServer or GeocodeServer).')], HRESULT, 'TypeName',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
]
################################################################
## code template for IServerObject implementation
##class IServerObject_Impl(object):
##    @property
##    def TypeName(self):
##        u'Type of the server object (MapServer or GeocodeServer).'
##        #return Name
##
##    @property
##    def ConfigurationName(self):
##        u'Name of the server object configuration that defines the server object.'
##        #return Name
##


# values for enumeration 'esriServerExceptionHandlingMode'
esriServerExceptionHandlingMode_Normal = 0
esriServerExceptionHandlingMode_ExitOnException = 1
esriServerExceptionHandlingMode_ExitOnExceptionAndDump = 2
esriServerExceptionHandlingMode_Dump = 3
esriServerExceptionHandlingMode = c_int # enum
class IManagerWebService(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manage a collection of IGISServer objects in the Manager web service catalog.'
    _iid_ = GUID('{C260325F-C891-4DFF-89C1-58AEACC7E361}')
    _idlflags_ = ['oleautomation']
class IGISServers(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manage the collection of IGISServer objects.'
    _iid_ = GUID('{20DAE966-D7DA-41E9-9334-D9D8AB7AB83E}')
    _idlflags_ = ['oleautomation']
class IGISServer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manage the collection of IGISServer objects.'
    _iid_ = GUID('{D9C910B6-4C6E-475D-BAE6-5EACD1C4E9C2}')
    _idlflags_ = ['oleautomation']
IManagerWebService._methods_ = [
    COMMETHOD(['propget', helpstring(u'Gets the IGISServers object holding the IGISServerInfos for the Manager web service catalog.')], HRESULT, 'GISServers',
              ( ['retval', 'out'], POINTER(POINTER(IGISServers)), 'servers' )),
    COMMETHOD([helpstring(u'Adds an IGISServer object to the GISServers in this Manager web service catalog.')], HRESULT, 'AddGISServer',
              ( ['in'], POINTER(IGISServer), 'Server' )),
    COMMETHOD([helpstring(u'Deletes an IGISServer object to the GISServers in this Manager web service catalog.')], HRESULT, 'DeleteGISServer',
              ( ['in'], BSTR, 'aliasName' )),
    COMMETHOD([helpstring(u'Refreshes the service info on all services in all of the GISServers in this Manager web service catalog.')], HRESULT, 'RefreshServiceInfo'),
]
################################################################
## code template for IManagerWebService implementation
##class IManagerWebService_Impl(object):
##    def RefreshServiceInfo(self):
##        u'Refreshes the service info on all services in all of the GISServers in this Manager web service catalog.'
##        #return 
##
##    def AddGISServer(self, Server):
##        u'Adds an IGISServer object to the GISServers in this Manager web service catalog.'
##        #return 
##
##    def DeleteGISServer(self, aliasName):
##        u'Deletes an IGISServer object to the GISServers in this Manager web service catalog.'
##        #return 
##
##    @property
##    def GISServers(self):
##        u'Gets the IGISServers object holding the IGISServerInfos for the Manager web service catalog.'
##        #return servers
##

class IServerMachineEnvironment(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{C1A7FBAB-48D4-49DA-9AAC-B28D3B982A9D}')
    _idlflags_ = ['oleautomation']
IServerMachineEnvironment._methods_ = [
    COMMETHOD([], HRESULT, 'GetEnvVariable',
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
]
################################################################
## code template for IServerMachineEnvironment implementation
##class IServerMachineEnvironment_Impl(object):
##    def GetEnvVariable(self, Name):
##        '-no docstring-'
##        #return pVal
##

class IServerEnvironmentImpl(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{73E0F44F-9E93-4309-A29B-2D6FDDE36536}')
    _idlflags_ = ['oleautomation']
class IServerEnvironmentImpl2(IServerEnvironmentImpl):
    _case_insensitive_ = True
    _iid_ = GUID('{E027774D-CA6E-430E-97C0-6F4B1C67CC82}')
    _idlflags_ = ['oleautomation']
class IServerJobManager(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{66210BAB-F71D-4ECC-8823-6BF8431A5BB4}')
    _idlflags_ = ['oleautomation']
IServerEnvironmentImpl._methods_ = [
    COMMETHOD(['propput'], HRESULT, 'CurrentJobID',
              ( ['in'], BSTR, 'rhs' )),
    COMMETHOD(['propput'], HRESULT, 'IsAdmin',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD(['propget'], HRESULT, 'JobCatalog',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IJobCatalog)), 'ppJC' )),
    COMMETHOD(['propget'], HRESULT, 'ServerJobManager',
              ( ['retval', 'out'], POINTER(POINTER(IServerJobManager)), 'ppSJM' )),
    COMMETHOD(['propget'], HRESULT, 'ServerObjectAdmin',
              ( ['retval', 'out'], POINTER(POINTER(IServerObjectAdmin)), 'ppSOA' )),
    COMMETHOD(['propget'], HRESULT, 'JobRegistry',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IJobRegistry)), 'ppJR' )),
    COMMETHOD(['propget'], HRESULT, 'StorageConnectionString',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
]
################################################################
## code template for IServerEnvironmentImpl implementation
##class IServerEnvironmentImpl_Impl(object):
##    @property
##    def ServerJobManager(self):
##        '-no docstring-'
##        #return ppSJM
##
##    @property
##    def JobRegistry(self):
##        '-no docstring-'
##        #return ppJR
##
##    def _set(self, rhs):
##        '-no docstring-'
##    CurrentJobID = property(fset = _set, doc = _set.__doc__)
##
##    @property
##    def JobCatalog(self):
##        '-no docstring-'
##        #return ppJC
##
##    def _set(self, rhs):
##        '-no docstring-'
##    IsAdmin = property(fset = _set, doc = _set.__doc__)
##
##    @property
##    def StorageConnectionString(self):
##        '-no docstring-'
##        #return pVal
##
##    @property
##    def ServerObjectAdmin(self):
##        '-no docstring-'
##        #return ppSOA
##

IServerEnvironmentImpl2._methods_ = [
    COMMETHOD(['propput'], HRESULT, 'Log',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ILog), 'rhs' )),
    COMMETHOD(['propput'], HRESULT, 'Properties',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'rhs' )),
    COMMETHOD(['propput'], HRESULT, 'JobTracker',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IJobTracker), 'rhs' )),
    COMMETHOD(['propput'], HRESULT, 'JobRegistry',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IJobRegistry), 'rhs' )),
    COMMETHOD(['propput'], HRESULT, 'ServerJobManager',
              ( ['in'], POINTER(IServerJobManager), 'rhs' )),
    COMMETHOD(['propput'], HRESULT, 'ServerObjectAdmin',
              ( ['in'], POINTER(IServerObjectAdmin), 'rhs' )),
    COMMETHOD(['propput'], HRESULT, 'UserInfo',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IServerUserInfo), 'rhs' )),
]
################################################################
## code template for IServerEnvironmentImpl2 implementation
##class IServerEnvironmentImpl2_Impl(object):
##    def _set(self, rhs):
##        '-no docstring-'
##    ServerJobManager = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        '-no docstring-'
##    Log = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        '-no docstring-'
##    JobRegistry = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        '-no docstring-'
##    JobTracker = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        '-no docstring-'
##    UserInfo = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        '-no docstring-'
##    ServerObjectAdmin = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        '-no docstring-'
##    Properties = property(fset = _set, doc = _set.__doc__)
##

class IServiceCatalogAdmin2(IServiceCatalogAdmin):
    _case_insensitive_ = True
    u'Provides access to members that control the contents of an ArcGIS Server web services catalog.'
    _iid_ = GUID('{5ABA2EF8-DEA3-4B86-AE3B-F2F711B85196}')
    _idlflags_ = ['oleautomation']
class IServiceCatalogAdmin3(IServiceCatalogAdmin2):
    _case_insensitive_ = True
    u'Provides access to members that control the contents of an ArcGIS Server web services catalog.'
    _iid_ = GUID('{214DF7E7-4A43-4F8F-9A13-436AFC4D2A5F}')
    _idlflags_ = ['oleautomation']
IServiceCatalogAdmin2._methods_ = [
    COMMETHOD(['propput', helpstring(u'The message formats supported by the web services in the catalog.')], HRESULT, 'MessageFormats',
              ( ['in'], esriServiceCatalogMessageFormat, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'The message version supported by the server.')], HRESULT, 'MessageVersion',
              ( ['in'], comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.esriArcGISVersion, 'rhs' )),
    COMMETHOD([helpstring(u'Creates a new array of web service folders.')], HRESULT, 'CreateServiceFolderArray',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'array' )),
    COMMETHOD(['propputref', helpstring(u'The array of the web service folders for the web service catalog.')], HRESULT, 'ServiceFolders',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray), 'rhs' )),
]
################################################################
## code template for IServiceCatalogAdmin2 implementation
##class IServiceCatalogAdmin2_Impl(object):
##    def CreateServiceFolderArray(self):
##        u'Creates a new array of web service folders.'
##        #return array
##
##    def ServiceFolders(self, rhs):
##        u'The array of the web service folders for the web service catalog.'
##        #return 
##
##    def _set(self, rhs):
##        u'The message formats supported by the web services in the catalog.'
##    MessageFormats = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'The message version supported by the server.'
##    MessageVersion = property(fset = _set, doc = _set.__doc__)
##

IServiceCatalogAdmin3._methods_ = [
    COMMETHOD(['propput', helpstring(u'Token service url.')], HRESULT, 'TokenServiceURL',
              ( ['in'], BSTR, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether the service catalog should require tokens for authentication.')], HRESULT, 'RequiresTokens',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
]
################################################################
## code template for IServiceCatalogAdmin3 implementation
##class IServiceCatalogAdmin3_Impl(object):
##    def _set(self, rhs):
##        u'Token service url.'
##    TokenServiceURL = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Indicates whether the service catalog should require tokens for authentication.'
##    RequiresTokens = property(fset = _set, doc = _set.__doc__)
##

class User(CoClass):
    _reg_clsid_ = GUID('{6B05FD91-C29D-4317-9866-E34B1EE699ED}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{18F2FC71-6B30-45B9-B101-037A8B868B66}', 10, 2)
User._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.ISupportErrorInfo, IUser]

IServerInit._methods_ = [
    COMMETHOD([helpstring(u'Initializes Private Server.')], HRESULT, 'InitPrivateServer',
              ( ['in'], BSTR, 'dir' )),
]
################################################################
## code template for IServerInit implementation
##class IServerInit_Impl(object):
##    def InitPrivateServer(self, dir):
##        u'Initializes Private Server.'
##        #return 
##

IServerInit2._methods_ = [
    COMMETHOD([helpstring(u'Initializes Private Server.')], HRESULT, 'InitPrivateServerEx',
              ( ['in'], BSTR, 'serverDir' ),
              ( ['in'], BSTR, 'logDir' )),
]
################################################################
## code template for IServerInit2 implementation
##class IServerInit2_Impl(object):
##    def InitPrivateServerEx(self, serverDir, logDir):
##        u'Initializes Private Server.'
##        #return 
##

class IIdentity(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that define a user.'
    _iid_ = GUID('{0710484B-62EC-42C4-8A3D-3186E2D8DA36}')
    _idlflags_ = ['oleautomation']
IIdentity._methods_ = [
    COMMETHOD(['propput', helpstring(u'The username of the user.')], HRESULT, 'UserName',
              ( ['in'], BSTR, 'UserName' )),
    COMMETHOD(['propget', helpstring(u'The username of the user.')], HRESULT, 'UserName',
              ( ['retval', 'out'], POINTER(BSTR), 'UserName' )),
    COMMETHOD(['propput', helpstring(u'The domain name of the user.')], HRESULT, 'DomainName',
              ( ['in'], BSTR, 'DomainName' )),
    COMMETHOD(['propget', helpstring(u'The domain name of the user.')], HRESULT, 'DomainName',
              ( ['retval', 'out'], POINTER(BSTR), 'DomainName' )),
    COMMETHOD(['propput', helpstring(u'The clear-text user password.')], HRESULT, 'Password',
              ( ['in'], BSTR, 'Password' )),
    COMMETHOD(['propget', helpstring(u'The clear-text user password.')], HRESULT, 'Password',
              ( ['retval', 'out'], POINTER(BSTR), 'Password' )),
    COMMETHOD(['propput', helpstring(u'The base64 encoded copy of the encrypted password.')], HRESULT, 'EncodedString',
              ( ['in'], BSTR, 'Password' )),
    COMMETHOD(['propget', helpstring(u'The base64 encoded copy of the encrypted password.')], HRESULT, 'EncodedString',
              ( ['retval', 'out'], POINTER(BSTR), 'Password' )),
]
################################################################
## code template for IIdentity implementation
##class IIdentity_Impl(object):
##    def _get(self):
##        u'The username of the user.'
##        #return UserName
##    def _set(self, UserName):
##        u'The username of the user.'
##    UserName = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The clear-text user password.'
##        #return Password
##    def _set(self, Password):
##        u'The clear-text user password.'
##    Password = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The base64 encoded copy of the encrypted password.'
##        #return Password
##    def _set(self, Password):
##        u'The base64 encoded copy of the encrypted password.'
##    EncodedString = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The domain name of the user.'
##        #return DomainName
##    def _set(self, DomainName):
##        u'The domain name of the user.'
##    DomainName = property(_get, _set, doc = _set.__doc__)
##

IEnumServerObjectExtensionTypeInfo._methods_ = [
    COMMETHOD([helpstring(u'Returns the next extension type in the enumeration.')], HRESULT, 'Next',
              ( ['retval', 'out'], POINTER(POINTER(IServerObjectExtensionTypeInfo)), 'nextInfo' )),
    COMMETHOD([helpstring(u'Starts the enumeration at the beginning.')], HRESULT, 'Reset'),
    COMMETHOD(['propget', helpstring(u'The number of extension types in the enumeration.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
]
################################################################
## code template for IEnumServerObjectExtensionTypeInfo implementation
##class IEnumServerObjectExtensionTypeInfo_Impl(object):
##    def Reset(self):
##        u'Starts the enumeration at the beginning.'
##        #return 
##
##    @property
##    def Count(self):
##        u'The number of extension types in the enumeration.'
##        #return pVal
##
##    def Next(self):
##        u'Returns the next extension type in the enumeration.'
##        #return nextInfo
##

class IServerDirectory2(IServerDirectory):
    _case_insensitive_ = True
    u'Provides access to members that control the behavior and properties of a server directory to administrators.'
    _iid_ = GUID('{F284D482-F71B-4542-9C93-1DC4B7E79881}')
    _idlflags_ = ['oleautomation']
IServerDirectory._methods_ = [
    COMMETHOD(['propget', helpstring(u'The path of the server directory.')], HRESULT, 'Path',
              ( ['retval', 'out'], POINTER(BSTR), 'pPath' )),
    COMMETHOD(['propput', helpstring(u'The path of the server directory.')], HRESULT, 'Path',
              ( ['in'], BSTR, 'pPath' )),
    COMMETHOD(['propget', helpstring(u'The URL of the virtual directory that maps to the physical directory as described by the Path property.')], HRESULT, 'URL',
              ( ['retval', 'out'], POINTER(BSTR), 'pUrl' )),
    COMMETHOD(['propput', helpstring(u'The URL of the virtual directory that maps to the physical directory as described by the Path property.')], HRESULT, 'URL',
              ( ['in'], BSTR, 'pUrl' )),
    COMMETHOD(['propget', helpstring(u'The description of the server directory.')], HRESULT, 'Description',
              ( ['retval', 'out'], POINTER(BSTR), 'pText' )),
    COMMETHOD(['propput', helpstring(u'The description of the server directory.')], HRESULT, 'Description',
              ( ['in'], BSTR, 'pText' )),
    COMMETHOD(['propget', helpstring(u'The mode by which the files in the server directory are cleaned (by age, by size or none).')], HRESULT, 'CleaningMode',
              ( ['retval', 'out'], POINTER(esriServerDirectoryCleaningMode), 'pMode' )),
    COMMETHOD(['propput', helpstring(u'The mode by which the files in the server directory are cleaned (by age, by size or none).')], HRESULT, 'CleaningMode',
              ( ['in'], esriServerDirectoryCleaningMode, 'pMode' )),
    COMMETHOD(['propget', helpstring(u'The maximum age (in seconds) a file can be in the server directory before it is deleted, if the cleaning mode is by file age.')], HRESULT, 'MaxFileAge',
              ( ['retval', 'out'], POINTER(c_int), 'pAge' )),
    COMMETHOD(['propput', helpstring(u'The maximum age (in seconds) a file can be in the server directory before it is deleted, if the cleaning mode is by file age.')], HRESULT, 'MaxFileAge',
              ( ['in'], c_int, 'pAge' )),
]
################################################################
## code template for IServerDirectory implementation
##class IServerDirectory_Impl(object):
##    def _get(self):
##        u'The URL of the virtual directory that maps to the physical directory as described by the Path property.'
##        #return pUrl
##    def _set(self, pUrl):
##        u'The URL of the virtual directory that maps to the physical directory as described by the Path property.'
##    URL = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The path of the server directory.'
##        #return pPath
##    def _set(self, pPath):
##        u'The path of the server directory.'
##    Path = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The maximum age (in seconds) a file can be in the server directory before it is deleted, if the cleaning mode is by file age.'
##        #return pAge
##    def _set(self, pAge):
##        u'The maximum age (in seconds) a file can be in the server directory before it is deleted, if the cleaning mode is by file age.'
##    MaxFileAge = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The mode by which the files in the server directory are cleaned (by age, by size or none).'
##        #return pMode
##    def _set(self, pMode):
##        u'The mode by which the files in the server directory are cleaned (by age, by size or none).'
##    CleaningMode = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The description of the server directory.'
##        #return pText
##    def _set(self, pText):
##        u'The description of the server directory.'
##    Description = property(_get, _set, doc = _set.__doc__)
##

IServerDirectory2._methods_ = [
    COMMETHOD(['propget', helpstring(u'The Type of server directory.')], HRESULT, 'Type',
              ( ['retval', 'out'], POINTER(esriServerDirectoryType), 'pType' )),
    COMMETHOD(['propput', helpstring(u'The Type of server directory.')], HRESULT, 'Type',
              ( ['in'], esriServerDirectoryType, 'pType' )),
]
################################################################
## code template for IServerDirectory2 implementation
##class IServerDirectory2_Impl(object):
##    def _get(self):
##        u'The Type of server directory.'
##        #return pType
##    def _set(self, pType):
##        u'The Type of server directory.'
##    Type = property(_get, _set, doc = _set.__doc__)
##

class IConfigurationFactory(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that can be called during server object configuration events.'
    _iid_ = GUID('{94E42963-1A3B-4413-847E-AFA37EE24A5A}')
    _idlflags_ = ['oleautomation']
IServerObjectFactoryX._methods_ = [
    COMMETHOD([helpstring(u'Adds a folder to the Add In folder processing list.')], HRESULT, 'AddAddInFolder',
              ( ['in'], BSTR, 'addInFolderPath' )),
    COMMETHOD([helpstring(u'Removes a folder from the Add In folder processing list.')], HRESULT, 'RemoveAddInFolder',
              ( ['in'], BSTR, 'addInFolderPath' )),
    COMMETHOD([helpstring(u'Sets the product code.')], HRESULT, 'SetProductCode',
              ( ['in'], c_int, 'productCode' )),
    COMMETHOD([helpstring(u'Sets the path to the job registry maintained on disk.')], HRESULT, 'SetJobRegistryPath',
              ( ['in'], BSTR, 'jobRegPath' )),
    COMMETHOD([helpstring(u'Gets the path to the job registry that was set on the factory.')], HRESULT, 'GetJobRegistryPath',
              ( ['retval', 'out'], POINTER(BSTR), 'pJobRegPath' )),
    COMMETHOD([helpstring(u'Sets the path to the log directory.')], HRESULT, 'SetLogDirectoryPath',
              ( ['in'], BSTR, 'logDirPath' )),
    COMMETHOD([helpstring(u'Gets the path to the log directory that was set on the factory.')], HRESULT, 'GetLogDirectoryPath',
              ( ['retval', 'out'], POINTER(BSTR), 'pLogDirPath' )),
    COMMETHOD([helpstring(u'Sets the log level.')], HRESULT, 'SetLogLevel',
              ( ['in'], BSTR, 'LogLevel' )),
    COMMETHOD([helpstring(u'Gets the log level that was set on the factory.')], HRESULT, 'GetLogLevel',
              ( ['retval', 'out'], POINTER(BSTR), 'pLogLevel' )),
    COMMETHOD([helpstring(u'Sets the maximum size of the log file.')], HRESULT, 'SetMaxLogFileSize',
              ( ['in'], c_int, 'maxLogFileSize' )),
    COMMETHOD([helpstring(u'Gets the maximum size of the log file that was set on the factory.')], HRESULT, 'GetMaxLogFileSize',
              ( ['retval', 'out'], POINTER(c_int), 'pMaxLogFileSize' )),
    COMMETHOD([helpstring(u'Creates a new server object given a CLSID.')], HRESULT, 'CreateServerObject',
              ( ['in'], BSTR, 'CLSID' ),
              ( ['in'], BSTR, 'cfgName' ),
              ( ['in'], BSTR, 'cfgType' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'ipProps' ),
              ( ['retval', 'out'], POINTER(POINTER(IServerObject)), 'ppSO' )),
    COMMETHOD([helpstring(u'Creates a new server configuration factory for a given type.')], HRESULT, 'CreateConfigurationFactory',
              ( ['in'], BSTR, 'cfgName' ),
              ( ['in'], BSTR, 'cfgType' ),
              ( ['in'], BSTR, 'CLSID' ),
              ( ['retval', 'out'], POINTER(POINTER(IConfigurationFactory)), 'ppCF' )),
    COMMETHOD([helpstring(u'Creates an instance of an AddIn given a CLSID.')], HRESULT, 'CreateObject',
              ( ['in'], BSTR, 'CLSID' ),
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'ppUnk' )),
    COMMETHOD([helpstring(u'Cleanup routine that indicates a shutdown of the STA thread thats hosting factory.')], HRESULT, 'Shutdown'),
    COMMETHOD([helpstring(u'Cleanup routine that calls ShutDown on the Server object and extensions.')], HRESULT, 'ShutdownEx',
              ( ['in'], POINTER(IServerObject), 'ipSO' )),
    COMMETHOD([helpstring(u'Sets the process id.')], HRESULT, 'SetProcessId',
              ( ['in'], c_ulong, 'ProcessId' )),
]
################################################################
## code template for IServerObjectFactoryX implementation
##class IServerObjectFactoryX_Impl(object):
##    def GetLogDirectoryPath(self):
##        u'Gets the path to the log directory that was set on the factory.'
##        #return pLogDirPath
##
##    def SetProductCode(self, productCode):
##        u'Sets the product code.'
##        #return 
##
##    def RemoveAddInFolder(self, addInFolderPath):
##        u'Removes a folder from the Add In folder processing list.'
##        #return 
##
##    def CreateConfigurationFactory(self, cfgName, cfgType, CLSID):
##        u'Creates a new server configuration factory for a given type.'
##        #return ppCF
##
##    def SetLogLevel(self, LogLevel):
##        u'Sets the log level.'
##        #return 
##
##    def GetMaxLogFileSize(self):
##        u'Gets the maximum size of the log file that was set on the factory.'
##        #return pMaxLogFileSize
##
##    def AddAddInFolder(self, addInFolderPath):
##        u'Adds a folder to the Add In folder processing list.'
##        #return 
##
##    def CreateObject(self, CLSID):
##        u'Creates an instance of an AddIn given a CLSID.'
##        #return ppUnk
##
##    def SetJobRegistryPath(self, jobRegPath):
##        u'Sets the path to the job registry maintained on disk.'
##        #return 
##
##    def Shutdown(self):
##        u'Cleanup routine that indicates a shutdown of the STA thread thats hosting factory.'
##        #return 
##
##    def GetJobRegistryPath(self):
##        u'Gets the path to the job registry that was set on the factory.'
##        #return pJobRegPath
##
##    def SetMaxLogFileSize(self, maxLogFileSize):
##        u'Sets the maximum size of the log file.'
##        #return 
##
##    def SetProcessId(self, ProcessId):
##        u'Sets the process id.'
##        #return 
##
##    def ShutdownEx(self, ipSO):
##        u'Cleanup routine that calls ShutDown on the Server object and extensions.'
##        #return 
##
##    def SetLogDirectoryPath(self, logDirPath):
##        u'Sets the path to the log directory.'
##        #return 
##
##    def CreateServerObject(self, CLSID, cfgName, cfgType, ipProps):
##        u'Creates a new server object given a CLSID.'
##        #return ppSO
##
##    def GetLogLevel(self):
##        u'Gets the log level that was set on the factory.'
##        #return pLogLevel
##

IServerObjectTypeInfo2._methods_ = [
    COMMETHOD(['propget', helpstring(u'Display name of the server object type.')], HRESULT, 'DisplayName',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
]
################################################################
## code template for IServerObjectTypeInfo2 implementation
##class IServerObjectTypeInfo2_Impl(object):
##    @property
##    def DisplayName(self):
##        u'Display name of the server object type.'
##        #return Name
##

IServerObjectTypeInfo3._methods_ = [
    COMMETHOD(['propget', helpstring(u'Limits the number of configurations that can be created of this server object type.')], HRESULT, 'ConfigurationsLimit',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
]
################################################################
## code template for IServerObjectTypeInfo3 implementation
##class IServerObjectTypeInfo3_Impl(object):
##    @property
##    def ConfigurationsLimit(self):
##        u'Limits the number of configurations that can be created of this server object type.'
##        #return pVal
##

class IServerDirectory3(IServerDirectory2):
    _case_insensitive_ = True
    u'Provides access to members that control the behavior and properties of a server directory to administrators.'
    _iid_ = GUID('{2F2823A9-97D5-4287-BCEC-0D9802A4B115}')
    _idlflags_ = ['oleautomation']
IServerDirectory3._methods_ = [
    COMMETHOD(['propget', helpstring(u'The name of server directory.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pName' )),
    COMMETHOD(['propput', helpstring(u'The name of server directory.')], HRESULT, 'Name',
              ( ['in'], BSTR, 'pName' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether this is a private server directory.')], HRESULT, 'IsPrivate',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pIsPrivate' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether we can add a new server directory of this type.')], HRESULT, 'CanAddNew',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pCanAddNew' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether this server directory can be deleted.')], HRESULT, 'CanDelete',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pCanDelete' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether this server directory can be edited.')], HRESULT, 'CanEdit',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pCanEdit' )),
]
################################################################
## code template for IServerDirectory3 implementation
##class IServerDirectory3_Impl(object):
##    @property
##    def IsPrivate(self):
##        u'Indicates whether this is a private server directory.'
##        #return pIsPrivate
##
##    @property
##    def CanEdit(self):
##        u'Indicates whether this server directory can be edited.'
##        #return pCanEdit
##
##    def _get(self):
##        u'The name of server directory.'
##        #return pName
##    def _set(self, pName):
##        u'The name of server directory.'
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def CanAddNew(self):
##        u'Indicates whether we can add a new server directory of this type.'
##        #return pCanAddNew
##
##    @property
##    def CanDelete(self):
##        u'Indicates whether this server directory can be deleted.'
##        #return pCanDelete
##

IEnumServerObjectType._methods_ = [
    COMMETHOD([helpstring(u'Returns the next type in the enumeration.')], HRESULT, 'Next',
              ( ['retval', 'out'], POINTER(POINTER(IServerObjectType)), 'nextType' )),
    COMMETHOD([helpstring(u'Starts the enumeration at the beginning.')], HRESULT, 'Reset'),
    COMMETHOD(['propget', helpstring(u'The number of types in the enumeration.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
]
################################################################
## code template for IEnumServerObjectType implementation
##class IEnumServerObjectType_Impl(object):
##    def Reset(self):
##        u'Starts the enumeration at the beginning.'
##        #return 
##
##    @property
##    def Count(self):
##        u'The number of types in the enumeration.'
##        #return pVal
##
##    def Next(self):
##        u'Returns the next type in the enumeration.'
##        #return nextType
##

IServerErrorReports._methods_ = [
    COMMETHOD(['propput', helpstring(u'Exception handling mode of SOC processes.')], HRESULT, 'ErrorReportMode',
              ( ['in'], esriServerExceptionHandlingMode, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Exception handling mode of SOC processes.')], HRESULT, 'ErrorReportMode',
              ( ['retval', 'out'], POINTER(esriServerExceptionHandlingMode), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Exception handling mode of SOM process.')], HRESULT, 'ErrorReportModeSOM',
              ( ['in'], esriServerExceptionHandlingMode, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Exception handling mode of SOM process.')], HRESULT, 'ErrorReportModeSOM',
              ( ['retval', 'out'], POINTER(esriServerExceptionHandlingMode), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Crash dump type.')], HRESULT, 'ErrorReportType',
              ( ['in'], c_ulong, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Crash dump type.')], HRESULT, 'ErrorReportType',
              ( ['retval', 'out'], POINTER(c_ulong), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Crash dump directory.')], HRESULT, 'ErrorReportDir',
              ( ['in'], BSTR, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Crash dump directory.')], HRESULT, 'ErrorReportDir',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Maximum number of stored crash dumps.')], HRESULT, 'ErrorReportCacheSize',
              ( ['in'], c_ulong, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Maximum number of stored crash dumps.')], HRESULT, 'ErrorReportCacheSize',
              ( ['retval', 'out'], POINTER(c_ulong), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether error reporting is enabled.')], HRESULT, 'ErrorReportEnableUpload',
              ( ['in'], VARIANT_BOOL, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether error reporting is enabled.')], HRESULT, 'ErrorReportEnableUpload',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'E-mail address of server administrator.')], HRESULT, 'ErrorReportEmailAddress',
              ( ['in'], BSTR, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'E-mail address of server administrator.')], HRESULT, 'ErrorReportEmailAddress',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Interval at which SOM checks crash dumps and uploads error reports.')], HRESULT, 'ErrorReportInterval',
              ( ['in'], c_ulong, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Interval at which SOM checks crash dumps and uploads error reports.')], HRESULT, 'ErrorReportInterval',
              ( ['retval', 'out'], POINTER(c_ulong), 'pVal' )),
    COMMETHOD([helpstring(u'Uploads stored error reports to the reporting web service.')], HRESULT, 'ReportErrors'),
]
################################################################
## code template for IServerErrorReports implementation
##class IServerErrorReports_Impl(object):
##    def _get(self):
##        u'Maximum number of stored crash dumps.'
##        #return pVal
##    def _set(self, pVal):
##        u'Maximum number of stored crash dumps.'
##    ErrorReportCacheSize = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Interval at which SOM checks crash dumps and uploads error reports.'
##        #return pVal
##    def _set(self, pVal):
##        u'Interval at which SOM checks crash dumps and uploads error reports.'
##    ErrorReportInterval = property(_get, _set, doc = _set.__doc__)
##
##    def ReportErrors(self):
##        u'Uploads stored error reports to the reporting web service.'
##        #return 
##
##    def _get(self):
##        u'Exception handling mode of SOC processes.'
##        #return pVal
##    def _set(self, pVal):
##        u'Exception handling mode of SOC processes.'
##    ErrorReportMode = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'E-mail address of server administrator.'
##        #return pVal
##    def _set(self, pVal):
##        u'E-mail address of server administrator.'
##    ErrorReportEmailAddress = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether error reporting is enabled.'
##        #return pVal
##    def _set(self, pVal):
##        u'Indicates whether error reporting is enabled.'
##    ErrorReportEnableUpload = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Exception handling mode of SOM process.'
##        #return pVal
##    def _set(self, pVal):
##        u'Exception handling mode of SOM process.'
##    ErrorReportModeSOM = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Crash dump directory.'
##        #return pVal
##    def _set(self, pVal):
##        u'Crash dump directory.'
##    ErrorReportDir = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Crash dump type.'
##        #return pVal
##    def _set(self, pVal):
##        u'Crash dump type.'
##    ErrorReportType = property(_get, _set, doc = _set.__doc__)
##

IServerObjectExtensionTypeInfo._methods_ = [
    COMMETHOD(['propget', helpstring(u'The name of the extension type.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'The description of the extension type.')], HRESULT, 'Description',
              ( ['retval', 'out'], POINTER(BSTR), 'desc' )),
]
################################################################
## code template for IServerObjectExtensionTypeInfo implementation
##class IServerObjectExtensionTypeInfo_Impl(object):
##    @property
##    def Name(self):
##        u'The name of the extension type.'
##        #return Name
##
##    @property
##    def Description(self):
##        u'The description of the extension type.'
##        #return desc
##

IServerObjectExtensionTypeInfo2._methods_ = [
    COMMETHOD(['propget', helpstring(u'Display name of the server object extension type.')], HRESULT, 'DisplayName',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
]
################################################################
## code template for IServerObjectExtensionTypeInfo2 implementation
##class IServerObjectExtensionTypeInfo2_Impl(object):
##    @property
##    def DisplayName(self):
##        u'Display name of the server object extension type.'
##        #return pVal
##

IEnumServerDirectory._methods_ = [
    COMMETHOD([helpstring(u'Returns the next ServerDirectory in the enumeration.')], HRESULT, 'Next',
              ( ['retval', 'out'], POINTER(POINTER(IServerDirectory)), 'Next' )),
    COMMETHOD([helpstring(u'Starts the enumeration at the beginning.')], HRESULT, 'Reset'),
    COMMETHOD(['propget', helpstring(u'The number of ServerDirectories in the enumeration.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
]
################################################################
## code template for IEnumServerDirectory implementation
##class IEnumServerDirectory_Impl(object):
##    def Reset(self):
##        u'Starts the enumeration at the beginning.'
##        #return 
##
##    @property
##    def Count(self):
##        u'The number of ServerDirectories in the enumeration.'
##        #return pVal
##
##    def Next(self):
##        u'Returns the next ServerDirectory in the enumeration.'
##        #return Next
##

IServerJobManager._methods_ = [
    COMMETHOD([], HRESULT, 'ExecuteJob',
              ( ['in'], BSTR, 'cfgName' ),
              ( ['in'], BSTR, 'cfgType' ),
              ( ['in'], BSTR, 'jobID' )),
    COMMETHOD([], HRESULT, 'CheckJob',
              ( ['in'], BSTR, 'jobID' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bRes' )),
    COMMETHOD([], HRESULT, 'CancelJob',
              ( ['in'], BSTR, 'jobID' )),
]
################################################################
## code template for IServerJobManager implementation
##class IServerJobManager_Impl(object):
##    def ExecuteJob(self, cfgName, cfgType, jobID):
##        '-no docstring-'
##        #return 
##
##    def CheckJob(self, jobID):
##        '-no docstring-'
##        #return bRes
##
##    def CancelJob(self, jobID):
##        '-no docstring-'
##        #return 
##


# values for enumeration 'esriServerConnectionType'
esriServerConnectionTypeRoundRobin = 1
esriServerConnectionTypeFailOver = 2
esriServerConnectionType = c_int # enum
class IServerInfos(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that manage the collection of IServerInfo objects (SOMs in a GIS Server).'
    _iid_ = GUID('{23C5169B-11C2-4750-836E-2EBBDC9E7008}')
    _idlflags_ = ['oleautomation']
class IServerInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that define a SOM (Server Object Manager).'
    _iid_ = GUID('{FA70A9E1-A5FC-448E-AE33-6C78B1014966}')
    _idlflags_ = ['oleautomation']
IServerInfos._methods_ = [
    COMMETHOD(['propget', helpstring(u'Gets the number of IServerInfo objects in the collection.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Returns the IServerInfo at the specified index.')], HRESULT, 'Element',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IServerInfo)), 'serverInfo' )),
    COMMETHOD([helpstring(u'Removes the IServerInfo at the specified index.')], HRESULT, 'Remove',
              ( ['in'], c_int, 'index' )),
    COMMETHOD([helpstring(u'Removes all of the IServerInfo objects in the collection.')], HRESULT, 'RemoveAll'),
    COMMETHOD([helpstring(u'Adds an IServerInfo object to the end of the collection.')], HRESULT, 'Add',
              ( ['in'], POINTER(IServerInfo), 'serverInfo' )),
    COMMETHOD([helpstring(u'Inserts an IServerInfo object into the collection at the specified index.')], HRESULT, 'Insert',
              ( ['in'], c_int, 'index' ),
              ( ['in'], POINTER(IServerInfo), 'serverInfo' )),
]
################################################################
## code template for IServerInfos implementation
##class IServerInfos_Impl(object):
##    @property
##    def Count(self):
##        u'Gets the number of IServerInfo objects in the collection.'
##        #return Count
##
##    def Insert(self, index, serverInfo):
##        u'Inserts an IServerInfo object into the collection at the specified index.'
##        #return 
##
##    def Remove(self, index):
##        u'Removes the IServerInfo at the specified index.'
##        #return 
##
##    @property
##    def Element(self, index):
##        u'Returns the IServerInfo at the specified index.'
##        #return serverInfo
##
##    def RemoveAll(self):
##        u'Removes all of the IServerInfo objects in the collection.'
##        #return 
##
##    def Add(self, serverInfo):
##        u'Adds an IServerInfo object to the end of the collection.'
##        #return 
##

IServerObjectManager4._methods_ = [
    COMMETHOD([helpstring(u'Gets the ServiceCatalog for the services running on the server.')], HRESULT, 'CreateServiceCatalog',
              ( ['retval', 'out'], POINTER(POINTER(IServiceCatalog2)), 'ppCatalog' )),
]
################################################################
## code template for IServerObjectManager4 implementation
##class IServerObjectManager4_Impl(object):
##    def CreateServiceCatalog(self):
##        u'Gets the ServiceCatalog for the services running on the server.'
##        #return ppCatalog
##

IServerInfo._methods_ = [
    COMMETHOD(['propput', helpstring(u'The name of the SOM.')], HRESULT, 'ServerName',
              ( ['in'], BSTR, 'ServerName' )),
    COMMETHOD(['propget', helpstring(u'The name of the SOM.')], HRESULT, 'ServerName',
              ( ['retval', 'out'], POINTER(BSTR), 'ServerName' )),
    COMMETHOD(['propput', helpstring(u'The user identity of the client (httpHandler) adding the SOM.')], HRESULT, 'Identity',
              ( ['in'], POINTER(IIdentity), 'ppIdentity' )),
    COMMETHOD(['propget', helpstring(u'The user identity of the client (httpHandler) adding the SOM.')], HRESULT, 'Identity',
              ( ['retval', 'out'], POINTER(POINTER(IIdentity)), 'ppIdentity' )),
]
################################################################
## code template for IServerInfo implementation
##class IServerInfo_Impl(object):
##    def _get(self):
##        u'The name of the SOM.'
##        #return ServerName
##    def _set(self, ServerName):
##        u'The name of the SOM.'
##    ServerName = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The user identity of the client (httpHandler) adding the SOM.'
##        #return ppIdentity
##    def _set(self, ppIdentity):
##        u'The user identity of the client (httpHandler) adding the SOM.'
##    Identity = property(_get, _set, doc = _set.__doc__)
##


# values for enumeration 'esriStartupType'
esriSTAutomatic = 0
esriSTManual = 1
esriStartupType = c_int # enum
IServerObjectConfiguration._methods_ = [
    COMMETHOD(['propget', helpstring(u'Name of the server object configuration.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propput', helpstring(u'Name of the server object configuration.')], HRESULT, 'Name',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD(['propget', helpstring(u'Type of the server object configuration (MapServer or GeocodeServer).')], HRESULT, 'TypeName',
              ( ['retval', 'out'], POINTER(BSTR), 'TypeName' )),
    COMMETHOD(['propput', helpstring(u'Type of the server object configuration (MapServer or GeocodeServer).')], HRESULT, 'TypeName',
              ( ['in'], BSTR, 'TypeName' )),
    COMMETHOD(['propget', helpstring(u'Description of the server object configuration.')], HRESULT, 'Description',
              ( ['retval', 'out'], POINTER(BSTR), 'desc' )),
    COMMETHOD(['propput', helpstring(u'Description of the server object configuration.')], HRESULT, 'Description',
              ( ['in'], BSTR, 'desc' )),
    COMMETHOD(['propget', helpstring(u'Initialization parameters and properties for the server objects created by the server object configuration.')], HRESULT, 'Properties',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'props' )),
    COMMETHOD(['propputref', helpstring(u'Initialization parameters and properties for the server objects created by the server object configuration.')], HRESULT, 'Properties',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'props' )),
    COMMETHOD(['propget', helpstring(u'The recycling properties for the server object configuration.')], HRESULT, 'RecycleProperties',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'props' )),
    COMMETHOD(['propputref', helpstring(u'The recycling properties for the server object configuration.')], HRESULT, 'RecycleProperties',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'props' )),
    COMMETHOD(['propget', helpstring(u'The minimum number of server object instances for a server object configuration.')], HRESULT, 'MinInstances',
              ( ['retval', 'out'], POINTER(c_int), 'instances' )),
    COMMETHOD(['propput', helpstring(u'The minimum number of server object instances for a server object configuration.')], HRESULT, 'MinInstances',
              ( ['in'], c_int, 'instances' )),
    COMMETHOD(['propget', helpstring(u'The maximum number of server object instances for a server object configuration.')], HRESULT, 'MaxInstances',
              ( ['retval', 'out'], POINTER(c_int), 'instances' )),
    COMMETHOD(['propput', helpstring(u'The maximum number of server object instances for a server object configuration.')], HRESULT, 'MaxInstances',
              ( ['in'], c_int, 'instances' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the server objects defined by this configuration are pooled.')], HRESULT, 'IsPooled',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsPooled' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether the server objects defined by this configuration are pooled.')], HRESULT, 'IsPooled',
              ( ['in'], VARIANT_BOOL, 'IsPooled' )),
    COMMETHOD(['propget', helpstring(u'The isolation level of the server objects defined by the server object configuration.')], HRESULT, 'IsolationLevel',
              ( ['retval', 'out'], POINTER(esriServerIsolationLevel), 'isoLevel' )),
    COMMETHOD(['propput', helpstring(u'The isolation level of the server objects defined by the server object configuration.')], HRESULT, 'IsolationLevel',
              ( ['in'], esriServerIsolationLevel, 'isoLevel' )),
    COMMETHOD(['propget', helpstring(u'The startup type for this server object configuration. Startup type describes whether the server object configuration is started when the server object manager service is started for the GIS server.')], HRESULT, 'StartupType',
              ( ['retval', 'out'], POINTER(esriStartupType), 'Type' )),
    COMMETHOD(['propput', helpstring(u'The startup type for this server object configuration. Startup type describes whether the server object configuration is started when the server object manager service is started for the GIS server.')], HRESULT, 'StartupType',
              ( ['in'], esriStartupType, 'Type' )),
    COMMETHOD(['propget', helpstring(u'Maximum time (in seconds) a client will wait for an instance of a server object for this server object configuration using the CreateServerContext method on IServerObjectManager before timing out.')], HRESULT, 'WaitTimeout',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Maximum time (in seconds) a client will wait for an instance of a server object for this server object configuration using the CreateServerContext method on IServerObjectManager before timing out.')], HRESULT, 'WaitTimeout',
              ( ['in'], c_int, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Maximum time (in seconds) a client can hold onto an instance of a server object for this server object configuration before releasing it back to the server. It is the maximum time allowed between calling CreateServerContext and ReleaseServerContext.')], HRESULT, 'UsageTimeout',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Maximum time (in seconds) a client can hold onto an instance of a server object for this server object configuration before releasing it back to the server. It is the maximum time allowed between calling CreateServerContext and ReleaseServerContext.')], HRESULT, 'UsageTimeout',
              ( ['in'], c_int, 'pVal' )),
]
################################################################
## code template for IServerObjectConfiguration implementation
##class IServerObjectConfiguration_Impl(object):
##    def _get(self):
##        u'Name of the server object configuration.'
##        #return Name
##    def _set(self, Name):
##        u'Name of the server object configuration.'
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The maximum number of server object instances for a server object configuration.'
##        #return instances
##    def _set(self, instances):
##        u'The maximum number of server object instances for a server object configuration.'
##    MaxInstances = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The startup type for this server object configuration. Startup type describes whether the server object configuration is started when the server object manager service is started for the GIS server.'
##        #return Type
##    def _set(self, Type):
##        u'The startup type for this server object configuration. Startup type describes whether the server object configuration is started when the server object manager service is started for the GIS server.'
##    StartupType = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The isolation level of the server objects defined by the server object configuration.'
##        #return isoLevel
##    def _set(self, isoLevel):
##        u'The isolation level of the server objects defined by the server object configuration.'
##    IsolationLevel = property(_get, _set, doc = _set.__doc__)
##
##    def RecycleProperties(self, props):
##        u'The recycling properties for the server object configuration.'
##        #return 
##
##    def _get(self):
##        u'Type of the server object configuration (MapServer or GeocodeServer).'
##        #return TypeName
##    def _set(self, TypeName):
##        u'Type of the server object configuration (MapServer or GeocodeServer).'
##    TypeName = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Maximum time (in seconds) a client can hold onto an instance of a server object for this server object configuration before releasing it back to the server. It is the maximum time allowed between calling CreateServerContext and ReleaseServerContext.'
##        #return pVal
##    def _set(self, pVal):
##        u'Maximum time (in seconds) a client can hold onto an instance of a server object for this server object configuration before releasing it back to the server. It is the maximum time allowed between calling CreateServerContext and ReleaseServerContext.'
##    UsageTimeout = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether the server objects defined by this configuration are pooled.'
##        #return IsPooled
##    def _set(self, IsPooled):
##        u'Indicates whether the server objects defined by this configuration are pooled.'
##    IsPooled = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The minimum number of server object instances for a server object configuration.'
##        #return instances
##    def _set(self, instances):
##        u'The minimum number of server object instances for a server object configuration.'
##    MinInstances = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Maximum time (in seconds) a client will wait for an instance of a server object for this server object configuration using the CreateServerContext method on IServerObjectManager before timing out.'
##        #return pVal
##    def _set(self, pVal):
##        u'Maximum time (in seconds) a client will wait for an instance of a server object for this server object configuration using the CreateServerContext method on IServerObjectManager before timing out.'
##    WaitTimeout = property(_get, _set, doc = _set.__doc__)
##
##    def Properties(self, props):
##        u'Initialization parameters and properties for the server objects created by the server object configuration.'
##        #return 
##
##    def _get(self):
##        u'Description of the server object configuration.'
##        #return desc
##    def _set(self, desc):
##        u'Description of the server object configuration.'
##    Description = property(_get, _set, doc = _set.__doc__)
##

IServerObjectConfiguration2._methods_ = [
    COMMETHOD([helpstring(u'Serializes the server object configuration into a string.')], HRESULT, 'Serialize',
              ( ['retval', 'out'], POINTER(BSTR), 'str' )),
    COMMETHOD([helpstring(u'Deserializes the server object configuration from a string.')], HRESULT, 'Deserialize',
              ( ['in'], BSTR, 'str' )),
    COMMETHOD(['propget', helpstring(u'The extension-dependent properties for the server object configuration.')], HRESULT, 'ExtensionProperties',
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'ppExtProperties' )),
    COMMETHOD(['propputref', helpstring(u'The extension-dependent properties for the server object configuration.')], HRESULT, 'ExtensionProperties',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'ppExtProperties' )),
    COMMETHOD(['propget', helpstring(u'The extension-dependent info for the server object configuration.')], HRESULT, 'ExtensionInfo',
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'ppExtProperties' )),
    COMMETHOD(['propputref', helpstring(u'The extension-dependent info for the server object configuration.')], HRESULT, 'ExtensionInfo',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'ppExtProperties' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the state of the named extension is Enabled (true) or Disabled (false).')], HRESULT, 'ExtensionEnabled',
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether the state of the named extension is Enabled (true) or Disabled (false).')], HRESULT, 'ExtensionEnabled',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], VARIANT_BOOL, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Maximum time (in seconds) that a SOC process will remain active to allow its no longer used server object threads to shut down gracefully before terminating them.')], HRESULT, 'CleanupTimeout',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Maximum time (in seconds) that a SOC process will remain active to allow its no longer used server object threads to shut down gracefully before terminating them.')], HRESULT, 'CleanupTimeout',
              ( ['in'], c_int, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Maximum time (in seconds) that a SOC process will wait for an instance of a server object to start.')], HRESULT, 'StartupTimeout',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Maximum time (in seconds) that a SOC process will wait for an instance of a server object to start.')], HRESULT, 'StartupTimeout',
              ( ['in'], c_int, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Auxiliary Information for the server objects created by the server object configuration ?passive properties only.')], HRESULT, 'Info',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'props' )),
    COMMETHOD(['propputref', helpstring(u'Auxiliary Information for the server objects created by the server object configuration ?passive properties only.')], HRESULT, 'Info',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'props' )),
]
################################################################
## code template for IServerObjectConfiguration2 implementation
##class IServerObjectConfiguration2_Impl(object):
##    def Info(self, props):
##        u'Auxiliary Information for the server objects created by the server object configuration ?passive properties only.'
##        #return 
##
##    def ExtensionInfo(self, Name, ppExtProperties):
##        u'The extension-dependent info for the server object configuration.'
##        #return 
##
##    def Deserialize(self, str):
##        u'Deserializes the server object configuration from a string.'
##        #return 
##
##    def _get(self):
##        u'Maximum time (in seconds) that a SOC process will wait for an instance of a server object to start.'
##        #return pVal
##    def _set(self, pVal):
##        u'Maximum time (in seconds) that a SOC process will wait for an instance of a server object to start.'
##    StartupTimeout = property(_get, _set, doc = _set.__doc__)
##
##    def Serialize(self):
##        u'Serializes the server object configuration into a string.'
##        #return str
##
##    def _get(self, Name):
##        u'Indicates whether the state of the named extension is Enabled (true) or Disabled (false).'
##        #return pVal
##    def _set(self, Name, pVal):
##        u'Indicates whether the state of the named extension is Enabled (true) or Disabled (false).'
##    ExtensionEnabled = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Maximum time (in seconds) that a SOC process will remain active to allow its no longer used server object threads to shut down gracefully before terminating them.'
##        #return pVal
##    def _set(self, pVal):
##        u'Maximum time (in seconds) that a SOC process will remain active to allow its no longer used server object threads to shut down gracefully before terminating them.'
##    CleanupTimeout = property(_get, _set, doc = _set.__doc__)
##
##    def ExtensionProperties(self, Name, ppExtProperties):
##        u'The extension-dependent properties for the server object configuration.'
##        #return 
##

IServerObjectConfiguration3._methods_ = [
    COMMETHOD(['propget', helpstring(u'Maximum time (in seconds) an instance of a server object for this server object configuration can remain idle.')], HRESULT, 'IdleTimeout',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Maximum time (in seconds) an instance of a server object for this server object configuration can remain idle.')], HRESULT, 'IdleTimeout',
              ( ['in'], c_int, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Number of instances in a single low isolation container.')], HRESULT, 'InstancesPerContainer',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Number of instances in a single low isolation container.')], HRESULT, 'InstancesPerContainer',
              ( ['in'], c_int, 'pVal' )),
]
################################################################
## code template for IServerObjectConfiguration3 implementation
##class IServerObjectConfiguration3_Impl(object):
##    def _get(self):
##        u'Number of instances in a single low isolation container.'
##        #return pVal
##    def _set(self, pVal):
##        u'Number of instances in a single low isolation container.'
##    InstancesPerContainer = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Maximum time (in seconds) an instance of a server object for this server object configuration can remain idle.'
##        #return pVal
##    def _set(self, pVal):
##        u'Maximum time (in seconds) an instance of a server object for this server object configuration can remain idle.'
##    IdleTimeout = property(_get, _set, doc = _set.__doc__)
##

class IServerConfigurationStorage(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{53011377-69EF-42E5-93C8-26735B801969}')
    _idlflags_ = ['oleautomation']
IServerConfigurationStorage._methods_ = [
    COMMETHOD([], HRESULT, 'Connect',
              ( ['in'], BSTR, 'connectionString' )),
    COMMETHOD([], HRESULT, 'GetUpdateIDs',
              ( ['out'], POINTER(BSTR), 'pServerUpdateID' ),
              ( ['out'], POINTER(BSTR), 'pServicesUpdateID' ),
              ( ['out'], POINTER(BSTR), 'pFoldersUpdateID' ),
              ( ['out'], POINTER(BSTR), 'pPermissionsUpdateID' ),
              ( ['out'], POINTER(BSTR), 'pLogUpdateID' ),
              ( ['out'], POINTER(BSTR), 'pGDBUpdateID' )),
    COMMETHOD([], HRESULT, 'GetServerProperty',
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([], HRESULT, 'PutServerProperty',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], BSTR, 'Val' )),
    COMMETHOD(['propget'], HRESULT, 'ServerProperties',
              ( ['retval', 'out'], POINTER(BSTR), 'pList' )),
    COMMETHOD([], HRESULT, 'AddFolder',
              ( ['in'], BSTR, 'folderName' ),
              ( ['in'], BSTR, 'Info' )),
    COMMETHOD([], HRESULT, 'DeleteFolder',
              ( ['in'], BSTR, 'folderName' )),
    COMMETHOD([], HRESULT, 'RenameFolder',
              ( ['in'], BSTR, 'OldName' ),
              ( ['in'], BSTR, 'newName' )),
    COMMETHOD(['propget'], HRESULT, 'Folders',
              ( ['retval', 'out'], POINTER(BSTR), 'pList' )),
    COMMETHOD([], HRESULT, 'GetFolderInfo',
              ( ['in'], BSTR, 'folderName' ),
              ( ['out'], POINTER(BSTR), 'pUpdateID' ),
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([], HRESULT, 'PutFolderInfo',
              ( ['in'], BSTR, 'folderName' ),
              ( ['in'], BSTR, 'Val' )),
    COMMETHOD([], HRESULT, 'AddService',
              ( ['in'], BSTR, 'ID' ),
              ( ['in'], BSTR, 'definition' )),
    COMMETHOD([], HRESULT, 'DeleteService',
              ( ['in'], BSTR, 'ID' )),
    COMMETHOD(['propget'], HRESULT, 'Services',
              ( ['retval', 'out'], POINTER(BSTR), 'pList' )),
    COMMETHOD([], HRESULT, 'GetServiceDefinition',
              ( ['in'], BSTR, 'ID' ),
              ( ['out'], POINTER(BSTR), 'pUpdateID' ),
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([], HRESULT, 'PutServiceDefinition',
              ( ['in'], BSTR, 'ID' ),
              ( ['in'], BSTR, 'Val' )),
    COMMETHOD([], HRESULT, 'GetServiceIsStarted',
              ( ['in'], BSTR, 'ID' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD([], HRESULT, 'PutServiceIsStarted',
              ( ['in'], BSTR, 'ID' ),
              ( ['in'], VARIANT_BOOL, 'Val' )),
    COMMETHOD([], HRESULT, 'AddPermission',
              ( ['in'], BSTR, 'ResourceID' ),
              ( ['in'], BSTR, 'acl' )),
    COMMETHOD([], HRESULT, 'DeletePermission',
              ( ['in'], BSTR, 'ResourceID' )),
    COMMETHOD(['propget'], HRESULT, 'Permissions',
              ( ['retval', 'out'], POINTER(BSTR), 'pList' )),
    COMMETHOD([], HRESULT, 'GetACL',
              ( ['in'], BSTR, 'ResourceID' ),
              ( ['out'], POINTER(BSTR), 'pUpdateID' ),
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([], HRESULT, 'PutACL',
              ( ['in'], BSTR, 'ResourceID' ),
              ( ['in'], BSTR, 'Val' )),
    COMMETHOD([], HRESULT, 'AddGeodatabase',
              ( ['in'], BSTR, 'gdbName' ),
              ( ['in'], BSTR, 'Val' )),
    COMMETHOD([], HRESULT, 'DeleteGeodatabase',
              ( ['in'], BSTR, 'gdbName' )),
    COMMETHOD(['propget'], HRESULT, 'Geodatabases',
              ( ['retval', 'out'], POINTER(BSTR), 'pList' )),
    COMMETHOD([], HRESULT, 'GetGeodatabase',
              ( ['in'], BSTR, 'gdbName' ),
              ( ['out'], POINTER(BSTR), 'pUpdateID' ),
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([], HRESULT, 'PutGeodatabase',
              ( ['in'], BSTR, 'gdbName' ),
              ( ['in'], BSTR, 'Val' )),
    COMMETHOD(['propget'], HRESULT, 'LogFiles',
              ( ['retval', 'out'], POINTER(BSTR), 'pList' )),
    COMMETHOD([], HRESULT, 'PutLogFile',
              ( ['in'], BSTR, 'fileName' ),
              ( ['in'], c_double, 'DateCreated' ),
              ( ['in'], c_double, 'DateModified' ),
              ( ['in'], BSTR, 'Log' )),
    COMMETHOD([], HRESULT, 'GetLogFile',
              ( ['in'], BSTR, 'fileName' ),
              ( ['out'], POINTER(c_double), 'pDateCreated' ),
              ( ['out'], POINTER(c_double), 'pDateModified' ),
              ( ['retval', 'out'], POINTER(BSTR), 'pLog' )),
    COMMETHOD([], HRESULT, 'DeleteLogFile',
              ( ['in'], BSTR, 'fileName' )),
]
################################################################
## code template for IServerConfigurationStorage implementation
##class IServerConfigurationStorage_Impl(object):
##    def GetLogFile(self, fileName):
##        '-no docstring-'
##        #return pDateCreated, pDateModified, pLog
##
##    def GetServiceDefinition(self, ID):
##        '-no docstring-'
##        #return pUpdateID, pVal
##
##    def DeleteService(self, ID):
##        '-no docstring-'
##        #return 
##
##    def GetServiceIsStarted(self, ID):
##        '-no docstring-'
##        #return pVal
##
##    def PutGeodatabase(self, gdbName, Val):
##        '-no docstring-'
##        #return 
##
##    @property
##    def Folders(self):
##        '-no docstring-'
##        #return pList
##
##    def GetGeodatabase(self, gdbName):
##        '-no docstring-'
##        #return pUpdateID, pVal
##
##    def GetServerProperty(self, Name):
##        '-no docstring-'
##        #return pVal
##
##    def DeletePermission(self, ResourceID):
##        '-no docstring-'
##        #return 
##
##    def PutFolderInfo(self, folderName, Val):
##        '-no docstring-'
##        #return 
##
##    @property
##    def LogFiles(self):
##        '-no docstring-'
##        #return pList
##
##    def PutServerProperty(self, Name, Val):
##        '-no docstring-'
##        #return 
##
##    def AddPermission(self, ResourceID, acl):
##        '-no docstring-'
##        #return 
##
##    def PutLogFile(self, fileName, DateCreated, DateModified, Log):
##        '-no docstring-'
##        #return 
##
##    @property
##    def Services(self):
##        '-no docstring-'
##        #return pList
##
##    @property
##    def Permissions(self):
##        '-no docstring-'
##        #return pList
##
##    def GetFolderInfo(self, folderName):
##        '-no docstring-'
##        #return pUpdateID, pVal
##
##    def RenameFolder(self, OldName, newName):
##        '-no docstring-'
##        #return 
##
##    def AddFolder(self, folderName, Info):
##        '-no docstring-'
##        #return 
##
##    def AddGeodatabase(self, gdbName, Val):
##        '-no docstring-'
##        #return 
##
##    def GetACL(self, ResourceID):
##        '-no docstring-'
##        #return pUpdateID, pVal
##
##    def GetUpdateIDs(self):
##        '-no docstring-'
##        #return pServerUpdateID, pServicesUpdateID, pFoldersUpdateID, pPermissionsUpdateID, pLogUpdateID, pGDBUpdateID
##
##    def DeleteFolder(self, folderName):
##        '-no docstring-'
##        #return 
##
##    def DeleteGeodatabase(self, gdbName):
##        '-no docstring-'
##        #return 
##
##    def DeleteLogFile(self, fileName):
##        '-no docstring-'
##        #return 
##
##    @property
##    def Geodatabases(self):
##        '-no docstring-'
##        #return pList
##
##    def PutACL(self, ResourceID, Val):
##        '-no docstring-'
##        #return 
##
##    def PutServiceIsStarted(self, ID, Val):
##        '-no docstring-'
##        #return 
##
##    def Connect(self, connectionString):
##        '-no docstring-'
##        #return 
##
##    @property
##    def ServerProperties(self):
##        '-no docstring-'
##        #return pList
##
##    def AddService(self, ID, definition):
##        '-no docstring-'
##        #return 
##
##    def PutServiceDefinition(self, ID, Val):
##        '-no docstring-'
##        #return 
##


# values for enumeration 'esriMachineStatus'
esriMStarted = 0
esriMSStopped = 1
esriMachineStatus = c_int # enum
IServerObjectAdmin7._methods_ = [
    COMMETHOD([helpstring(u'Checks if given user is a member of agsadmin group.')], HRESULT, 'IsAdminUser',
              ( ['in'], BSTR, 'UserName' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
]
################################################################
## code template for IServerObjectAdmin7 implementation
##class IServerObjectAdmin7_Impl(object):
##    def IsAdminUser(self, UserName):
##        u'Checks if given user is a member of agsadmin group.'
##        #return pVal
##

IServerObjectAdmin8._methods_ = [
    COMMETHOD([helpstring(u'Add Geodatabase.')], HRESULT, 'AddGeodatabase',
              ( ['in'], BSTR, 'gdbName' ),
              ( ['in'], BSTR, 'Val' )),
    COMMETHOD([helpstring(u'Delete Geodatabase.')], HRESULT, 'DeleteGeodatabase',
              ( ['in'], BSTR, 'gdbName' )),
    COMMETHOD(['propget', helpstring(u'Get Geodatabases.')], HRESULT, 'Geodatabases',
              ( ['retval', 'out'], POINTER(BSTR), 'pList' )),
    COMMETHOD([helpstring(u'Get Geodatabase.')], HRESULT, 'GetGeodatabase',
              ( ['in'], BSTR, 'gdbName' ),
              ( ['out'], POINTER(BSTR), 'pUpdateID' ),
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([helpstring(u'Put Geodatabase.')], HRESULT, 'PutGeodatabase',
              ( ['in'], BSTR, 'gdbName' ),
              ( ['in'], BSTR, 'Val' )),
]
################################################################
## code template for IServerObjectAdmin8 implementation
##class IServerObjectAdmin8_Impl(object):
##    def DeleteGeodatabase(self, gdbName):
##        u'Delete Geodatabase.'
##        #return 
##
##    def GetGeodatabase(self, gdbName):
##        u'Get Geodatabase.'
##        #return pUpdateID, pVal
##
##    def PutGeodatabase(self, gdbName, Val):
##        u'Put Geodatabase.'
##        #return 
##
##    def AddGeodatabase(self, gdbName, Val):
##        u'Add Geodatabase.'
##        #return 
##
##    @property
##    def Geodatabases(self):
##        u'Get Geodatabases.'
##        #return pList
##

IConfigurationFactory._methods_ = [
    COMMETHOD([helpstring(u'Is called when the configuration is added.')], HRESULT, 'OnAdd',
              ( ['in'], POINTER(IServerObjectAdmin), 'pAdmin' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'pProps' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'ppNewProps' )),
    COMMETHOD([helpstring(u'Is called when the configuration is removed.')], HRESULT, 'OnRemove'),
    COMMETHOD([helpstring(u'Is called when the configuration is started.')], HRESULT, 'OnStart',
              ( ['in'], POINTER(IServerObjectAdmin), 'pAdmin' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'props' )),
    COMMETHOD([helpstring(u'Is called when the configuration is stopped.')], HRESULT, 'OnStop',
              ( ['in'], POINTER(IServerObjectAdmin), 'pAdmin' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'props' )),
]
################################################################
## code template for IConfigurationFactory implementation
##class IConfigurationFactory_Impl(object):
##    def OnRemove(self):
##        u'Is called when the configuration is removed.'
##        #return 
##
##    def OnAdd(self, pAdmin, pProps):
##        u'Is called when the configuration is added.'
##        #return ppNewProps
##
##    def OnStart(self, pAdmin, props):
##        u'Is called when the configuration is started.'
##        #return 
##
##    def OnStop(self, pAdmin, props):
##        u'Is called when the configuration is stopped.'
##        #return 
##

IServerLog2._methods_ = [
    COMMETHOD([helpstring(u'Release the server log back to the server so it can be used by another client.')], HRESULT, 'ReleaseLog'),
]
################################################################
## code template for IServerLog2 implementation
##class IServerLog2_Impl(object):
##    def ReleaseLog(self):
##        u'Release the server log back to the server so it can be used by another client.'
##        #return 
##

class ServerObjectFactory(CoClass):
    u'The factory object used to create server objects in the server. '
    _reg_clsid_ = GUID('{6C20CA3D-F8C1-44EE-BF7F-5B866D86483F}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{18F2FC71-6B30-45B9-B101-037A8B868B66}', 10, 2)
class IServerObjectFactory(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the method used to create a server object outside a server object container.'
    _iid_ = GUID('{1FC365CC-E2E8-4F83-AFC9-834B33148E29}')
    _idlflags_ = ['oleautomation']
ServerObjectFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IServerObjectFactory]

IGISServers._methods_ = [
    COMMETHOD(['propget', helpstring(u'Gets the number of IGISServer objects in the collection.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Returns the IGISServer at the specified index.')], HRESULT, 'Element',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IGISServer)), 'Server' )),
    COMMETHOD([helpstring(u'Removes the IGISServer at the specified index.')], HRESULT, 'Remove',
              ( ['in'], c_int, 'index' )),
    COMMETHOD([helpstring(u'Removes all of the IGISServer objects in the collection.')], HRESULT, 'RemoveAll'),
    COMMETHOD([helpstring(u'Adds an IGISServer object to the end of the collection.')], HRESULT, 'Add',
              ( ['in'], POINTER(IGISServer), 'Server' )),
    COMMETHOD([helpstring(u'Inserts an IGISServer into the collection at the specified index.')], HRESULT, 'Insert',
              ( ['in'], c_int, 'index' ),
              ( ['in'], POINTER(IGISServer), 'Server' )),
]
################################################################
## code template for IGISServers implementation
##class IGISServers_Impl(object):
##    @property
##    def Count(self):
##        u'Gets the number of IGISServer objects in the collection.'
##        #return Count
##
##    def Insert(self, index, Server):
##        u'Inserts an IGISServer into the collection at the specified index.'
##        #return 
##
##    def Remove(self, index):
##        u'Removes the IGISServer at the specified index.'
##        #return 
##
##    @property
##    def Element(self, index):
##        u'Returns the IGISServer at the specified index.'
##        #return Server
##
##    def RemoveAll(self):
##        u'Removes all of the IGISServer objects in the collection.'
##        #return 
##
##    def Add(self, Server):
##        u'Adds an IGISServer object to the end of the collection.'
##        #return 
##

IPermissionsAdmin._methods_ = [
    COMMETHOD([helpstring(u'Grants permission to the specified principal to perform the given operation on the indicated resource.')], HRESULT, 'AllowPermission',
              ( ['in'], BSTR, 'Principal' ),
              ( ['in'], BSTR, 'resource' ),
              ( ['in'], BSTR, 'operation' )),
    COMMETHOD([helpstring(u'Revokes permission from the specified principal to perform the given operation on the indicated resource.')], HRESULT, 'DenyPermission',
              ( ['in'], BSTR, 'Principal' ),
              ( ['in'], BSTR, 'resource' ),
              ( ['in'], BSTR, 'operation' )),
    COMMETHOD([helpstring(u'Enumrates all princiapls in the Permissions Store.')], HRESULT, 'GetAllPrincipals',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IEnumBSTR)), 'ppEnum' )),
]
################################################################
## code template for IPermissionsAdmin implementation
##class IPermissionsAdmin_Impl(object):
##    def GetAllPrincipals(self):
##        u'Enumrates all princiapls in the Permissions Store.'
##        #return ppEnum
##
##    def DenyPermission(self, Principal, resource, operation):
##        u'Revokes permission from the specified principal to perform the given operation on the indicated resource.'
##        #return 
##
##    def AllowPermission(self, Principal, resource, operation):
##        u'Grants permission to the specified principal to perform the given operation on the indicated resource.'
##        #return 
##

IPermissionsAdmin2._methods_ = [
    COMMETHOD([helpstring(u'Removes all permissions for a particular principal.')], HRESULT, 'CleanPermissions',
              ( ['in'], BSTR, 'Principal' )),
]
################################################################
## code template for IPermissionsAdmin2 implementation
##class IPermissionsAdmin2_Impl(object):
##    def CleanPermissions(self, Principal):
##        u'Removes all permissions for a particular principal.'
##        #return 
##

class ServerMachine(CoClass):
    u'The ServerMachine object which provides information about the ServerMachine.'
    _reg_clsid_ = GUID('{39F4800B-7B54-457F-BEA0-7DFCDEF37FF7}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{18F2FC71-6B30-45B9-B101-037A8B868B66}', 10, 2)
ServerMachine._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IServerMachine, IServerMachine2, IServerMachine3]

class IServerObjectConfiguration5(IServerObjectConfiguration4):
    _case_insensitive_ = True
    u'Provides access to administrators to members that control the behavior and properties of a server object configuration with extensions.'
    _iid_ = GUID('{6CA0FE13-3ACF-49E5-9632-2381A96CA0AE}')
    _idlflags_ = ['oleautomation']
IServerObjectConfiguration4._methods_ = [
    COMMETHOD(['propget', helpstring(u'Interval at which SOM calls IObjectActivate on ServerObject, thus allowing instances with stale data connections to be recycled.')], HRESULT, 'ServiceKeepAliveInterval',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Interval at which SOM calls IObjectActivate on ServerObject, thus allowing instances with stale data connections to be recycled.')], HRESULT, 'ServiceKeepAliveInterval',
              ( ['in'], c_int, 'pVal' )),
]
################################################################
## code template for IServerObjectConfiguration4 implementation
##class IServerObjectConfiguration4_Impl(object):
##    def _get(self):
##        u'Interval at which SOM calls IObjectActivate on ServerObject, thus allowing instances with stale data connections to be recycled.'
##        #return pVal
##    def _set(self, pVal):
##        u'Interval at which SOM calls IObjectActivate on ServerObject, thus allowing instances with stale data connections to be recycled.'
##    ServiceKeepAliveInterval = property(_get, _set, doc = _set.__doc__)
##


# values for enumeration 'esriLoadBalancing'
esriLoadBalancingRoundRobin = 0
esriLoadBalancingNone = 1
esriLoadBalancing = c_int # enum
IServerObjectConfiguration5._methods_ = [
    COMMETHOD(['propput', helpstring(u'Status of the server object configuration. This status indicates whether the server object configuration is started, stopped, paused, etc.')], HRESULT, 'Status',
              ( ['in'], esriConfigurationStatus, 'pStatus' )),
    COMMETHOD(['propget', helpstring(u'Status of the server object configuration. This status indicates whether the server object configuration is started, stopped, paused, etc.')], HRESULT, 'Status',
              ( ['retval', 'out'], POINTER(esriConfigurationStatus), 'pStatus' )),
    COMMETHOD(['propget', helpstring(u'The extension names of this server object configuration.')], HRESULT, 'ExtensionNames',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'ppExtNames' )),
    COMMETHOD(['propput', helpstring(u'The dataset names associated with configuration.')], HRESULT, 'DatasetNames',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray), 'ppDTNames' )),
    COMMETHOD(['propget', helpstring(u'The dataset names associated with configuration.')], HRESULT, 'DatasetNames',
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IStringArray)), 'ppDTNames' )),
    COMMETHOD(['propput', helpstring(u'The target cluster for this service to be published to.')], HRESULT, 'TargetCluster',
              ( ['in'], BSTR, 'pName' )),
    COMMETHOD(['propget', helpstring(u'The target cluster for this service to be published to.')], HRESULT, 'TargetCluster',
              ( ['retval', 'out'], POINTER(BSTR), 'pName' )),
    COMMETHOD(['propput', helpstring(u'The service load balancing type.')], HRESULT, 'LoadBalancing',
              ( ['in'], esriLoadBalancing, 'pType' )),
    COMMETHOD(['propget', helpstring(u'The service load balancing type.')], HRESULT, 'LoadBalancing',
              ( ['retval', 'out'], POINTER(esriLoadBalancing), 'pType' )),
]
################################################################
## code template for IServerObjectConfiguration5 implementation
##class IServerObjectConfiguration5_Impl(object):
##    def _get(self):
##        u'Status of the server object configuration. This status indicates whether the server object configuration is started, stopped, paused, etc.'
##        #return pStatus
##    def _set(self, pStatus):
##        u'Status of the server object configuration. This status indicates whether the server object configuration is started, stopped, paused, etc.'
##    Status = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The service load balancing type.'
##        #return pType
##    def _set(self, pType):
##        u'The service load balancing type.'
##    LoadBalancing = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def ExtensionNames(self):
##        u'The extension names of this server object configuration.'
##        #return ppExtNames
##
##    def _get(self):
##        u'The dataset names associated with configuration.'
##        #return ppDTNames
##    def _set(self, ppDTNames):
##        u'The dataset names associated with configuration.'
##    DatasetNames = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The target cluster for this service to be published to.'
##        #return pName
##    def _set(self, pName):
##        u'The target cluster for this service to be published to.'
##    TargetCluster = property(_get, _set, doc = _set.__doc__)
##

IGISServer._methods_ = [
    COMMETHOD(['propput', helpstring(u'The alias used to designate this server.')], HRESULT, 'Alias',
              ( ['in'], BSTR, 'Alias' )),
    COMMETHOD(['propget', helpstring(u'The alias used to designate this server.')], HRESULT, 'Alias',
              ( ['retval', 'out'], POINTER(BSTR), 'Alias' )),
    COMMETHOD(['propput', helpstring(u'Returns the collection of ServerInfo objects (SOMs) associated with this server.')], HRESULT, 'ServerInfos',
              ( ['in'], POINTER(IServerInfos), 'ServerInfos' )),
    COMMETHOD(['propget', helpstring(u'Returns the collection of ServerInfo objects (SOMs) associated with this server.')], HRESULT, 'ServerInfos',
              ( ['retval', 'out'], POINTER(POINTER(IServerInfos)), 'ServerInfos' )),
    COMMETHOD(['propput', helpstring(u'The type of connection to the SOMs of this ArcGIS Server (Round Robin or FailOver).')], HRESULT, 'ConnectionType',
              ( ['in'], esriServerConnectionType, 'ServerInfos' )),
    COMMETHOD(['propget', helpstring(u'The type of connection to the SOMs of this ArcGIS Server (Round Robin or FailOver).')], HRESULT, 'ConnectionType',
              ( ['retval', 'out'], POINTER(esriServerConnectionType), 'ServerInfos' )),
    COMMETHOD(['propput', helpstring(u'The maximum length of a SOAP or Binary request that can be sent to this server.')], HRESULT, 'MaxRequestLength',
              ( ['in'], c_int, 'MaxRequestLength' )),
    COMMETHOD(['propget', helpstring(u'The maximum length of a SOAP or Binary request that can be sent to this server.')], HRESULT, 'MaxRequestLength',
              ( ['retval', 'out'], POINTER(c_int), 'MaxRequestLength' )),
    COMMETHOD(['propput', helpstring(u'The format, SOAP/Binary or both, of messages that are to be sent to the server.')], HRESULT, 'MessageFormat',
              ( ['in'], esriServiceCatalogMessageFormat, 'msgFormat' )),
    COMMETHOD(['propget', helpstring(u'The format, SOAP/Binary or both, of messages that are to be sent to the server.')], HRESULT, 'MessageFormat',
              ( ['retval', 'out'], POINTER(esriServiceCatalogMessageFormat), 'msgFormat' )),
]
################################################################
## code template for IGISServer implementation
##class IGISServer_Impl(object):
##    def _get(self):
##        u'The maximum length of a SOAP or Binary request that can be sent to this server.'
##        #return MaxRequestLength
##    def _set(self, MaxRequestLength):
##        u'The maximum length of a SOAP or Binary request that can be sent to this server.'
##    MaxRequestLength = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The alias used to designate this server.'
##        #return Alias
##    def _set(self, Alias):
##        u'The alias used to designate this server.'
##    Alias = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The format, SOAP/Binary or both, of messages that are to be sent to the server.'
##        #return msgFormat
##    def _set(self, msgFormat):
##        u'The format, SOAP/Binary or both, of messages that are to be sent to the server.'
##    MessageFormat = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The type of connection to the SOMs of this ArcGIS Server (Round Robin or FailOver).'
##        #return ServerInfos
##    def _set(self, ServerInfos):
##        u'The type of connection to the SOMs of this ArcGIS Server (Round Robin or FailOver).'
##    ConnectionType = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Returns the collection of ServerInfo objects (SOMs) associated with this server.'
##        #return ServerInfos
##    def _set(self, ServerInfos):
##        u'Returns the collection of ServerInfo objects (SOMs) associated with this server.'
##    ServerInfos = property(_get, _set, doc = _set.__doc__)
##

IServiceDescriptionArray._methods_ = [
    COMMETHOD(['propget', helpstring(u'The number of items in the array.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'pCount' )),
    COMMETHOD(['propget', helpstring(u'The Element at the specified index.')], HRESULT, 'Element',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IServiceDescription)), 'Element' )),
    COMMETHOD([helpstring(u'Add an element to the array.')], HRESULT, 'Add',
              ( ['in'], POINTER(IServiceDescription), 'Element' )),
    COMMETHOD([helpstring(u'Remove an element from the array.')], HRESULT, 'Remove',
              ( ['in'], c_int, 'index' )),
    COMMETHOD([helpstring(u'Remove all elements from the array.')], HRESULT, 'RemoveAll'),
    COMMETHOD([helpstring(u'Insert an element into the array.')], HRESULT, 'Insert',
              ( ['in'], c_int, 'index' ),
              ( ['in'], POINTER(IServiceDescription), 'Element' )),
    COMMETHOD(['propput', helpstring(u'The Element at the specified index.')], HRESULT, 'Element',
              ( ['in'], c_int, 'index' ),
              ( ['in'], POINTER(IServiceDescription), 'Element' )),
]
################################################################
## code template for IServiceDescriptionArray implementation
##class IServiceDescriptionArray_Impl(object):
##    @property
##    def Count(self):
##        u'The number of items in the array.'
##        #return pCount
##
##    def Insert(self, index, Element):
##        u'Insert an element into the array.'
##        #return 
##
##    def Remove(self, index):
##        u'Remove an element from the array.'
##        #return 
##
##    def _get(self, index):
##        u'The Element at the specified index.'
##        #return Element
##    def _set(self, index, Element):
##        u'The Element at the specified index.'
##    Element = property(_get, _set, doc = _set.__doc__)
##
##    def RemoveAll(self):
##        u'Remove all elements from the array.'
##        #return 
##
##    def Add(self, Element):
##        u'Add an element to the array.'
##        #return 
##

class IServerObjectConfigurationManager(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to additional members that support initializing a server object.'
    _iid_ = GUID('{181F5A7E-25C9-4FBF-9166-75D638ACC930}')
    _idlflags_ = ['oleautomation']
IServerObjectConfigurationManager._methods_ = [
    COMMETHOD([helpstring(u'Is called when the configuration is added.')], HRESULT, 'OnAdd',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'pProps' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'ppNewProps' )),
    COMMETHOD([helpstring(u'Is called when the configuration is removed.')], HRESULT, 'OnRemove'),
]
################################################################
## code template for IServerObjectConfigurationManager implementation
##class IServerObjectConfigurationManager_Impl(object):
##    def OnRemove(self):
##        u'Is called when the configuration is removed.'
##        #return 
##
##    def OnAdd(self, pProps):
##        u'Is called when the configuration is added.'
##        #return ppNewProps
##

class ResponseStreamer(CoClass):
    _reg_clsid_ = GUID('{552DC8B3-B3E7-3B06-A772-72BB30C8BCC6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{18F2FC71-6B30-45B9-B101-037A8B868B66}', 10, 2)
ResponseStreamer._com_interfaces_ = [IResponseStreamer]

IEnumServerMachine._methods_ = [
    COMMETHOD([helpstring(u'Returns the next ServerMachine in the enumeration.')], HRESULT, 'Next',
              ( ['retval', 'out'], POINTER(POINTER(IServerMachine)), 'nextMachine' )),
    COMMETHOD([helpstring(u'Starts the enumeration at the beginning.')], HRESULT, 'Reset'),
    COMMETHOD(['propget', helpstring(u'The number of ServerMachines in the enumeration.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
]
################################################################
## code template for IEnumServerMachine implementation
##class IEnumServerMachine_Impl(object):
##    def Reset(self):
##        u'Starts the enumeration at the beginning.'
##        #return 
##
##    @property
##    def Count(self):
##        u'The number of ServerMachines in the enumeration.'
##        #return pVal
##
##    def Next(self):
##        u'Returns the next ServerMachine in the enumeration.'
##        #return nextMachine
##

class IUserStore(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'An interface to access the user repository.'
    _iid_ = GUID('{85D81926-F224-480F-A0AA-576D87EE0363}')
    _idlflags_ = ['oleautomation']
IUserStore._methods_ = [
    COMMETHOD([helpstring(u'Tests the connection to the user store.')], HRESULT, 'TestConnection',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'pProps' )),
    COMMETHOD([helpstring(u'Connects to a user store.')], HRESULT, 'Initialize',
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'pProps' )),
    COMMETHOD([helpstring(u'Tests the connection to the user store.')], HRESULT, 'IsReadOnly',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsReadOnly' )),
    COMMETHOD([helpstring(u'Add a new user to the user store.')], HRESULT, 'AddUser',
              ( ['in'], POINTER(IUser), 'pUser' )),
    COMMETHOD([helpstring(u'Updates a user account in the user store.')], HRESULT, 'UpdateUser',
              ( ['in'], POINTER(IUser), 'pUser' )),
    COMMETHOD([helpstring(u'Deletes a user account from the user store.')], HRESULT, 'DeleteUser',
              ( ['in'], BSTR, 'UserName' )),
    COMMETHOD([helpstring(u'Returns a user account from the user store.')], HRESULT, 'GetUser',
              ( ['in'], BSTR, 'UserName' ),
              ( ['retval', 'out'], POINTER(POINTER(IUser)), 'pUser' )),
    COMMETHOD([helpstring(u'Returns the total number of users in the user store.')], HRESULT, 'GetTotalUsers',
              ( ['retval', 'out'], POINTER(c_int), 'totalUsers' )),
    COMMETHOD([helpstring(u'Returns a maxCount of users from the user store that match a particular filter.')], HRESULT, 'GetAllUsers',
              ( ['in'], BSTR, 'filter' ),
              ( ['in'], c_int, 'maxCount' ),
              ( ['out'], POINTER(_midlSAFEARRAY(POINTER(IUser))), 'users' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'hasMore' )),
    COMMETHOD([helpstring(u'Returns a pageSize of users from the user store from the startIndex.')], HRESULT, 'GetAllUsersPaged',
              ( ['in'], c_int, 'StartIndex' ),
              ( ['in'], c_int, 'pageSize' ),
              ( ['out'], POINTER(_midlSAFEARRAY(POINTER(IUser))), 'users' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'hasMore' )),
    COMMETHOD([helpstring(u'Validates the credentials of the user against the user store.')], HRESULT, 'ValidateUser',
              ( ['in'], BSTR, 'UserName' ),
              ( ['in'], BSTR, 'Password' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'isValid' )),
]
################################################################
## code template for IUserStore implementation
##class IUserStore_Impl(object):
##    def UpdateUser(self, pUser):
##        u'Updates a user account in the user store.'
##        #return 
##
##    def DeleteUser(self, UserName):
##        u'Deletes a user account from the user store.'
##        #return 
##
##    def AddUser(self, pUser):
##        u'Add a new user to the user store.'
##        #return 
##
##    def IsReadOnly(self):
##        u'Tests the connection to the user store.'
##        #return IsReadOnly
##
##    def GetUser(self, UserName):
##        u'Returns a user account from the user store.'
##        #return pUser
##
##    def GetAllUsersPaged(self, StartIndex, pageSize):
##        u'Returns a pageSize of users from the user store from the startIndex.'
##        #return users, hasMore
##
##    def TestConnection(self, pProps):
##        u'Tests the connection to the user store.'
##        #return 
##
##    def Initialize(self, pProps):
##        u'Connects to a user store.'
##        #return 
##
##    def ValidateUser(self, UserName, Password):
##        u'Validates the credentials of the user against the user store.'
##        #return isValid
##
##    def GetAllUsers(self, filter, maxCount):
##        u'Returns a maxCount of users from the user store that match a particular filter.'
##        #return users, hasMore
##
##    def GetTotalUsers(self):
##        u'Returns the total number of users in the user store.'
##        #return totalUsers
##

class ServerObjectExtensionType(CoClass):
    u'The ServerObjectExtensionType object which provides information about server object extension types to users with administrative privileges to the ArcGIS server.'
    _reg_clsid_ = GUID('{087E165B-17B8-40AB-9FE6-3C912E4FD7DD}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{18F2FC71-6B30-45B9-B101-037A8B868B66}', 10, 2)
ServerObjectExtensionType._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IServerObjectExtensionType, IServerObjectExtensionType2, IServerObjectExtensionType3]

IRole._methods_ = [
    COMMETHOD([helpstring(u'Sets the role name.')], HRESULT, 'SetRolename',
              ( ['in'], BSTR, 'rolename' )),
    COMMETHOD([helpstring(u'Returns the role name.')], HRESULT, 'GetRolename',
              ( ['retval', 'out'], POINTER(BSTR), 'rolename' )),
    COMMETHOD([helpstring(u'Sets the role description.')], HRESULT, 'SetDescription',
              ( ['in'], BSTR, 'Description' )),
    COMMETHOD([helpstring(u'Returns the role description.')], HRESULT, 'GetDescription',
              ( ['retval', 'out'], POINTER(BSTR), 'Description' )),
]
################################################################
## code template for IRole implementation
##class IRole_Impl(object):
##    def SetDescription(self, Description):
##        u'Sets the role description.'
##        #return 
##
##    def SetRolename(self, rolename):
##        u'Sets the role name.'
##        #return 
##
##    def GetDescription(self):
##        u'Returns the role description.'
##        #return Description
##
##    def GetRolename(self):
##        u'Returns the role name.'
##        #return rolename
##

class IWPISilentConfig(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that configure the web services post install silently.'
    _iid_ = GUID('{89816982-DEDC-4A5A-922A-D2FBBCF53877}')
    _idlflags_ = []
IWPISilentConfig._methods_ = [
    COMMETHOD([helpstring(u'Configures the server post install with the specified server name, instance name, SOM name and name and domain of user with which the webservices authenticate against the SOM.')], HRESULT, 'Configure',
              ( ['in'], BSTR, 'WebServerName' ),
              ( ['in'], BSTR, 'instanceName' ),
              ( ['in'], BSTR, 'computerName' ),
              ( ['in'], BSTR, 'UserName' ),
              ( ['in'], BSTR, 'userPass' ),
              ( ['in'], BSTR, 'DomainName' ),
              ( ['in'], BSTR, 'port' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'success' )),
]
################################################################
## code template for IWPISilentConfig implementation
##class IWPISilentConfig_Impl(object):
##    def Configure(self, WebServerName, instanceName, computerName, UserName, userPass, DomainName, port):
##        u'Configures the server post install with the specified server name, instance name, SOM name and name and domain of user with which the webservices authenticate against the SOM.'
##        #return success
##

class IServerEnvironmentEx(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to Server configuration information.'
    _iid_ = GUID('{AB1FFDAE-9B92-4E97-B3DA-EA251258D8AF}')
    _idlflags_ = ['oleautomation']
IServerEnvironmentEx._methods_ = [
    COMMETHOD([helpstring(u"An enumerator over all the GIS server's ServerDirectoryInfos.")], HRESULT, 'GetServerDirectoryInfos',
              ( ['retval', 'out'], POINTER(POINTER(IEnumServerDirectoryInfo)), 'ppEnum' )),
]
################################################################
## code template for IServerEnvironmentEx implementation
##class IServerEnvironmentEx_Impl(object):
##    def GetServerDirectoryInfos(self):
##        u"An enumerator over all the GIS server's ServerDirectoryInfos."
##        #return ppEnum
##

class ServiceCatalog(CoClass):
    u'The ServiceCatalog object, which implements the Service Catalog.'
    _reg_clsid_ = GUID('{AC58DB7E-196F-4206-B4C6-2CE6AEFD6ED3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{18F2FC71-6B30-45B9-B101-037A8B868B66}', 10, 2)
ServiceCatalog._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IServiceCatalog, IServiceCatalog2, IServiceCatalogAdmin, IServiceCatalogAdmin2, comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IRequestHandler]

class IConfigurationFactory2(IConfigurationFactory):
    _case_insensitive_ = True
    u'Provides access to members that can be called during server object configuration events.'
    _iid_ = GUID('{702ECF93-89D3-438D-B218-F1686C813F0F}')
    _idlflags_ = ['oleautomation']
IConfigurationFactory2._methods_ = [
    COMMETHOD([helpstring(u'Is called before the configuration is started.')], HRESULT, 'BeforeStart',
              ( ['in'], POINTER(IServerObjectAdmin), 'pAdmin' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'props' )),
    COMMETHOD([helpstring(u'Is called before the configuration is stopped.')], HRESULT, 'BeforeStop',
              ( ['in'], POINTER(IServerObjectAdmin), 'pAdmin' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'props' )),
    COMMETHOD([helpstring(u'Is called when the configuration is removed.')], HRESULT, 'OnRemoveEx',
              ( ['in'], POINTER(IServerObjectAdmin), 'pAdmin' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'props' )),
]
################################################################
## code template for IConfigurationFactory2 implementation
##class IConfigurationFactory2_Impl(object):
##    def BeforeStart(self, pAdmin, props):
##        u'Is called before the configuration is started.'
##        #return 
##
##    def BeforeStop(self, pAdmin, props):
##        u'Is called before the configuration is stopped.'
##        #return 
##
##    def OnRemoveEx(self, pAdmin, props):
##        u'Is called when the configuration is removed.'
##        #return 
##

class ConfigFactory(CoClass):
    u'The Configuration Factory object for implementing server object configuration events.'
    _reg_clsid_ = GUID('{4750135F-AFBF-4DA5-A128-2EB939E87BD7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{18F2FC71-6B30-45B9-B101-037A8B868B66}', 10, 2)
ConfigFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IConfigurationFactory]

class ServerDirectory(CoClass):
    u'The ServerDirectory object which provides information about the ServerDirectory.'
    _reg_clsid_ = GUID('{A6622DC3-1817-4420-86D6-9B3CEBD33778}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{18F2FC71-6B30-45B9-B101-037A8B868B66}', 10, 2)
ServerDirectory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IServerDirectory, IServerDirectory2]

IEnumServerObjectConfiguration._methods_ = [
    COMMETHOD([helpstring(u'Returns the next configuration in the enumeration.')], HRESULT, 'Next',
              ( ['retval', 'out'], POINTER(POINTER(IServerObjectConfiguration)), 'nextConfig' )),
    COMMETHOD([helpstring(u'Starts the enumeration at the beginning.')], HRESULT, 'Reset'),
    COMMETHOD(['propget', helpstring(u'The number of configurations in the enumeration.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
]
################################################################
## code template for IEnumServerObjectConfiguration implementation
##class IEnumServerObjectConfiguration_Impl(object):
##    def Reset(self):
##        u'Starts the enumeration at the beginning.'
##        #return 
##
##    @property
##    def Count(self):
##        u'The number of configurations in the enumeration.'
##        #return pVal
##
##    def Next(self):
##        u'Returns the next configuration in the enumeration.'
##        #return nextConfig
##

class IServerStatus(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the properties of the status of the ArcGIS Server.'
    _iid_ = GUID('{DE94C160-5101-49A4-BAB4-6893745F01CE}')
    _idlflags_ = ['oleautomation']
IServerStatus._methods_ = [
    COMMETHOD(['propget', helpstring(u'The number of server object instances currently running in the ArcGIS server.')], HRESULT, 'InstanceCount',
              ( ['in'], esriAccessLevel, 'access' ),
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD(['propget', helpstring(u'The number of currently running server object instances in use by clients of the ArcGIS server.')], HRESULT, 'InstanceInUseCount',
              ( ['in'], esriAccessLevel, 'access' ),
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD([helpstring(u'Gets the configuration status for the server object configuration with the specified Name and TypeName.')], HRESULT, 'GetConfigurationStatus',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], BSTR, 'TypeName' ),
              ( ['retval', 'out'], POINTER(POINTER(IServerObjectConfigurationStatus)), 'ppStatus' )),
    COMMETHOD([helpstring(u'Gets the status for an ArcGIS Server host machine.')], HRESULT, 'GetMachineStatus',
              ( ['in'], BSTR, 'Machine' ),
              ( ['retval', 'out'], POINTER(POINTER(IServerMachineStatus)), 'ppStatus' )),
    COMMETHOD(['propget', helpstring(u'The time that the server was started.')], HRESULT, 'StartTime',
              ( ['retval', 'out'], POINTER(c_double), 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the server is started and enabled(true) or not(false).')], HRESULT, 'Enabled',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
]
################################################################
## code template for IServerStatus implementation
##class IServerStatus_Impl(object):
##    def GetMachineStatus(self, Machine):
##        u'Gets the status for an ArcGIS Server host machine.'
##        #return ppStatus
##
##    @property
##    def InstanceCount(self, access):
##        u'The number of server object instances currently running in the ArcGIS server.'
##        #return pVal
##
##    @property
##    def Enabled(self):
##        u'Indicates if the server is started and enabled(true) or not(false).'
##        #return pVal
##
##    def GetConfigurationStatus(self, Name, TypeName):
##        u'Gets the configuration status for the server object configuration with the specified Name and TypeName.'
##        #return ppStatus
##
##    @property
##    def StartTime(self):
##        u'The time that the server was started.'
##        #return pVal
##
##    @property
##    def InstanceInUseCount(self, access):
##        u'The number of currently running server object instances in use by clients of the ArcGIS server.'
##        #return pVal
##

IServerDirectoryInfo2._methods_ = [
    COMMETHOD(['propget', helpstring(u'The Type of server directory.')], HRESULT, 'Type',
              ( ['retval', 'out'], POINTER(esriServerDirectoryType), 'pType' )),
]
################################################################
## code template for IServerDirectoryInfo2 implementation
##class IServerDirectoryInfo2_Impl(object):
##    @property
##    def Type(self):
##        u'The Type of server directory.'
##        #return pType
##

class IServerCLRHost(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to a method that cleans CLR managed objects.'
    _iid_ = GUID('{562704EE-3A20-4C6D-A501-8468A1DBC55A}')
    _idlflags_ = ['oleautomation']
IServerCLRHost._methods_ = [
    COMMETHOD([helpstring(u'Uses Garbage Collector to clean all managed objects.')], HRESULT, 'Cleanup'),
]
################################################################
## code template for IServerCLRHost implementation
##class IServerCLRHost_Impl(object):
##    def Cleanup(self):
##        u'Uses Garbage Collector to clean all managed objects.'
##        #return 
##

IEnumServerObjectExtensionType._methods_ = [
    COMMETHOD([helpstring(u'Returns the next extension type in the enumeration.')], HRESULT, 'Next',
              ( ['retval', 'out'], POINTER(POINTER(IServerObjectExtensionType)), 'nextType' )),
    COMMETHOD([helpstring(u'Starts the enumeration at the beginning.')], HRESULT, 'Reset'),
    COMMETHOD(['propget', helpstring(u'The number of extension types in the enumeration.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
]
################################################################
## code template for IEnumServerObjectExtensionType implementation
##class IEnumServerObjectExtensionType_Impl(object):
##    def Reset(self):
##        u'Starts the enumeration at the beginning.'
##        #return 
##
##    @property
##    def Count(self):
##        u'The number of extension types in the enumeration.'
##        #return pVal
##
##    def Next(self):
##        u'Returns the next extension type in the enumeration.'
##        #return nextType
##

class IServerObjectConfigurationManager2(IServerObjectConfigurationManager):
    _case_insensitive_ = True
    u'Provides access to additional members that support initializing a server object.'
    _iid_ = GUID('{3130F209-598D-4269-B404-DF6B13804742}')
    _idlflags_ = ['oleautomation']
IServerObjectConfigurationManager2._methods_ = [
    COMMETHOD([helpstring(u'Is called when the configuration is started.')], HRESULT, 'OnStart',
              ( ['in'], POINTER(IServerObjectAdmin), 'pAdmin' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'pProps' )),
    COMMETHOD([helpstring(u'Is called when the configuration is stopped.')], HRESULT, 'OnStop',
              ( ['in'], POINTER(IServerObjectAdmin), 'pAdmin' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'pProps' )),
    COMMETHOD([helpstring(u'Is called when the configuration is removed.')], HRESULT, 'OnRemoveEx',
              ( ['in'], POINTER(IServerObjectAdmin), 'pAdmin' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'props' )),
    COMMETHOD([helpstring(u'Is called before the configuration is started.')], HRESULT, 'BeforeStart',
              ( ['in'], POINTER(IServerObjectAdmin), 'pAdmin' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'props' )),
    COMMETHOD([helpstring(u'Is called before the configuration is stopped.')], HRESULT, 'BeforeStop',
              ( ['in'], POINTER(IServerObjectAdmin), 'pAdmin' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'props' )),
]
################################################################
## code template for IServerObjectConfigurationManager2 implementation
##class IServerObjectConfigurationManager2_Impl(object):
##    def BeforeStart(self, pAdmin, props):
##        u'Is called before the configuration is started.'
##        #return 
##
##    def OnRemoveEx(self, pAdmin, props):
##        u'Is called when the configuration is removed.'
##        #return 
##
##    def BeforeStop(self, pAdmin, props):
##        u'Is called before the configuration is stopped.'
##        #return 
##
##    def OnStop(self, pAdmin, pProps):
##        u'Is called when the configuration is stopped.'
##        #return 
##
##    def OnStart(self, pAdmin, pProps):
##        u'Is called when the configuration is started.'
##        #return 
##

IServerLogQuery._methods_ = [
    COMMETHOD(['propget', helpstring(u'The start time in the ArcGIS Server logs at which to begin the query.')], HRESULT, 'StartTime',
              ( ['retval', 'out'], POINTER(c_double), 'pTime' )),
    COMMETHOD(['propput', helpstring(u'The start time in the ArcGIS Server logs at which to begin the query.')], HRESULT, 'StartTime',
              ( ['in'], c_double, 'pTime' )),
    COMMETHOD(['propget', helpstring(u'The end time in the ArcGIS Server logs at which to end the query.')], HRESULT, 'EndTime',
              ( ['retval', 'out'], POINTER(c_double), 'pTime' )),
    COMMETHOD(['propput', helpstring(u'The end time in the ArcGIS Server logs at which to end the query.')], HRESULT, 'EndTime',
              ( ['in'], c_double, 'pTime' )),
    COMMETHOD(['propget', helpstring(u'The log target name.')], HRESULT, 'Target',
              ( ['retval', 'out'], POINTER(BSTR), 'pName' )),
    COMMETHOD(['propput', helpstring(u'The log target name.')], HRESULT, 'Target',
              ( ['in'], BSTR, 'pName' )),
    COMMETHOD(['propget', helpstring(u'The machine name for which to query.')], HRESULT, 'Machine',
              ( ['retval', 'out'], POINTER(BSTR), 'pMachine' )),
    COMMETHOD(['propput', helpstring(u'The machine name for which to query.')], HRESULT, 'Machine',
              ( ['in'], BSTR, 'pMachine' )),
    COMMETHOD(['propget', helpstring(u'The log level at which to query (1-5).')], HRESULT, 'Level',
              ( ['retval', 'out'], POINTER(c_int), 'pLevel' )),
    COMMETHOD(['propput', helpstring(u'The log level at which to query (1-5).')], HRESULT, 'Level',
              ( ['in'], c_int, 'pLevel' )),
    COMMETHOD(['propget', helpstring(u'The maximum number of records to retrieve with the query.')], HRESULT, 'MaxRecords',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'The maximum number of records to retrieve with the query.')], HRESULT, 'MaxRecords',
              ( ['in'], c_int, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'The starting index at which to start retrieving records from the query.')], HRESULT, 'StartIndex',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'The starting index at which to start retrieving records from the query.')], HRESULT, 'StartIndex',
              ( ['in'], c_int, 'pVal' )),
]
################################################################
## code template for IServerLogQuery implementation
##class IServerLogQuery_Impl(object):
##    def _get(self):
##        u'The log target name.'
##        #return pName
##    def _set(self, pName):
##        u'The log target name.'
##    Target = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The log level at which to query (1-5).'
##        #return pLevel
##    def _set(self, pLevel):
##        u'The log level at which to query (1-5).'
##    Level = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The starting index at which to start retrieving records from the query.'
##        #return pVal
##    def _set(self, pVal):
##        u'The starting index at which to start retrieving records from the query.'
##    StartIndex = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The machine name for which to query.'
##        #return pMachine
##    def _set(self, pMachine):
##        u'The machine name for which to query.'
##    Machine = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The maximum number of records to retrieve with the query.'
##        #return pVal
##    def _set(self, pVal):
##        u'The maximum number of records to retrieve with the query.'
##    MaxRecords = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The start time in the ArcGIS Server logs at which to begin the query.'
##        #return pTime
##    def _set(self, pTime):
##        u'The start time in the ArcGIS Server logs at which to begin the query.'
##    StartTime = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The end time in the ArcGIS Server logs at which to end the query.'
##        #return pTime
##    def _set(self, pTime):
##        u'The end time in the ArcGIS Server logs at which to end the query.'
##    EndTime = property(_get, _set, doc = _set.__doc__)
##

IPermissionsManager._methods_ = [
    COMMETHOD([helpstring(u'Checks whether the specified principal has permission to perform the given operation on the indicated resource.')], HRESULT, 'CheckPermission',
              ( ['in'], BSTR, 'Principal' ),
              ( ['in'], BSTR, 'resource' ),
              ( ['in'], BSTR, 'operation' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbRes' )),
    COMMETHOD([helpstring(u'Enumerates all principals having permission to perform the specified operation on the given resource.')], HRESULT, 'GetPrincipalsWithPermissionOnResource',
              ( ['in'], BSTR, 'resource' ),
              ( ['in'], BSTR, 'operation' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IEnumBSTR)), 'ppEnum' )),
    COMMETHOD([helpstring(u'Checks whether the specified principal has different permissions among the descendents of the specified parent resource/operation combination.')], HRESULT, 'CheckForDescendentsWithDifferentPermissions',
              ( ['in'], BSTR, 'Principal' ),
              ( ['in'], BSTR, 'resource' ),
              ( ['in'], BSTR, 'operation' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbRes' )),
]
################################################################
## code template for IPermissionsManager implementation
##class IPermissionsManager_Impl(object):
##    def CheckForDescendentsWithDifferentPermissions(self, Principal, resource, operation):
##        u'Checks whether the specified principal has different permissions among the descendents of the specified parent resource/operation combination.'
##        #return pbRes
##
##    def CheckPermission(self, Principal, resource, operation):
##        u'Checks whether the specified principal has permission to perform the given operation on the indicated resource.'
##        #return pbRes
##
##    def GetPrincipalsWithPermissionOnResource(self, resource, operation):
##        u'Enumerates all principals having permission to perform the specified operation on the given resource.'
##        #return ppEnum
##

class ServerObjectConfigurationInfo(CoClass):
    u'The ServerObjectConfigurationInfo object which provides information about server object configurations to users without administrative privileges to the GIS server.'
    _reg_clsid_ = GUID('{CD8D4F2F-C833-47E1-98A6-B80C3A4F4428}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{18F2FC71-6B30-45B9-B101-037A8B868B66}', 10, 2)
ServerObjectConfigurationInfo._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IServerObjectConfigurationInfo, IServerObjectConfigurationInfo2]

IEnumServerDirectoryInfo._methods_ = [
    COMMETHOD([helpstring(u'Returns the next ServerDirectoryInfo in the enumeration.')], HRESULT, 'Next',
              ( ['retval', 'out'], POINTER(POINTER(IServerDirectoryInfo)), 'nextInfo' )),
    COMMETHOD([helpstring(u'Starts the enumeration at the beginning.')], HRESULT, 'Reset'),
    COMMETHOD(['propget', helpstring(u'The number of ServerDirectoryInfos in the enumeration.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
]
################################################################
## code template for IEnumServerDirectoryInfo implementation
##class IEnumServerDirectoryInfo_Impl(object):
##    def Reset(self):
##        u'Starts the enumeration at the beginning.'
##        #return 
##
##    @property
##    def Count(self):
##        u'The number of ServerDirectoryInfos in the enumeration.'
##        #return pVal
##
##    def Next(self):
##        u'Returns the next ServerDirectoryInfo in the enumeration.'
##        #return nextInfo
##

class IConfigurationFactory3(IConfigurationFactory2):
    _case_insensitive_ = True
    u'Provides access to members that can be called during server object configuration events.'
    _iid_ = GUID('{1EDFA167-4404-4295-B5BB-CC06A062F55C}')
    _idlflags_ = ['oleautomation']
IConfigurationFactory3._methods_ = [
    COMMETHOD([helpstring(u'Is called when configuration is renamed.')], HRESULT, 'OnRename',
              ( ['in'], POINTER(IServerObjectAdmin), 'pAdmin' ),
              ( ['in'], POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet), 'props' ),
              ( ['retval', 'out'], POINTER(POINTER(comtypes.gen._5E1F7BC3_67C5_4AEE_8EC6_C4B73AAC42ED_0_10_2.IPropertySet)), 'ppNewProps' )),
]
################################################################
## code template for IConfigurationFactory3 implementation
##class IConfigurationFactory3_Impl(object):
##    def OnRename(self, pAdmin, props):
##        u'Is called when configuration is renamed.'
##        #return ppNewProps
##

IServerObjectConfigurationStatus._methods_ = [
    COMMETHOD(['propget', helpstring(u'Number of instances of server objects for a particular configuration that are currently running in the GIS server.')], HRESULT, 'InstanceCount',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Number of running instances of server objects for a particular configuration that are in currently use by clients of the GIS server.')], HRESULT, 'InstanceInUseCount',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Status of the server object configuration. This status indicates whether the server object configuration is started, stopped, paused, etc.')], HRESULT, 'Status',
              ( ['retval', 'out'], POINTER(esriConfigurationStatus), 'pStatus' )),
]
################################################################
## code template for IServerObjectConfigurationStatus implementation
##class IServerObjectConfigurationStatus_Impl(object):
##    @property
##    def Status(self):
##        u'Status of the server object configuration. This status indicates whether the server object configuration is started, stopped, paused, etc.'
##        #return pStatus
##
##    @property
##    def InstanceCount(self):
##        u'Number of instances of server objects for a particular configuration that are currently running in the GIS server.'
##        #return pVal
##
##    @property
##    def InstanceInUseCount(self):
##        u'Number of running instances of server objects for a particular configuration that are in currently use by clients of the GIS server.'
##        #return pVal
##


# values for enumeration 'esriServerInstallType'
esriServerInstallTypeJava = 0
esriServerInstallTypeDotnet = 1
esriServerInstallTypeUnknown = 2
esriServerInstallType = c_int # enum
IServerObjectFactory._methods_ = [
    COMMETHOD([helpstring(u'Creates a server object outside of the server environment.')], HRESULT, 'CreateServerObject',
              ( ['in'], BSTR, 'CLSID' ),
              ( ['in'], BSTR, 'cfgName' ),
              ( ['in'], BSTR, 'cfgType' ),
              ( ['retval', 'out'], POINTER(POINTER(IServerObject)), 'ppSO' )),
]
################################################################
## code template for IServerObjectFactory implementation
##class IServerObjectFactory_Impl(object):
##    def CreateServerObject(self, CLSID, cfgName, cfgType):
##        u'Creates a server object outside of the server environment.'
##        #return ppSO
##

__all__ = ['IServerObjectConfigurationInfo2', 'IServerInfo',
           'ServerObjectType', 'esriServerIsolationAny',
           'ResponseStreamer', 'Role', 'ServerDirectoryInfo',
           'esriSSEServerObjectCreationFailed', 'IUserStore',
           'esriServerInstallTypeUnknown', 'ServerMachineStatus',
           'SOMController', 'IGISServer', 'IGISServers',
           'IServerLogQuery', 'IEnumServerObjectConfigurationInfo',
           'esriSSFStandardDeviation', 'esriSSFSum', 'IServerMachine',
           'IServerObjectTypeInfo', 'IEnumServerObjectExtensionType',
           'esriSTAutomatic', 'esriServerStatFunction',
           'IServerMachine2', 'IServerMachine3',
           'IServerObjectConfiguration2', 'IManagerWebService',
           'esriServiceCatalogMessageFormatSoapOrBin',
           'esriServerExceptionHandlingMode_Normal', 'esriSDTypeKML',
           'IServiceCatalogAdmin3', 'esriAccessAll',
           'esriSDTypeOutput', 'IServerObjectAdmin',
           'ServerObjectExtensionTypeInfo', 'IServerDirectoryInfo2',
           'esriSTPMinute', 'IWPISilentConfig',
           'IServerObjectManager', 'esriCSStarting',
           'IServiceCatalogAdmin', 'esriSDTypeJobRegistry',
           'IEnumServerObjectExtensionTypeInfo',
           'esriServerStatEvent',
           'esriServiceCatalogMessageFormatBin', 'esriSSFMinimum',
           'esriSDTypeUnknown', 'esriSDTypeUploads', 'IServerLog2',
           'esriServiceCatalogMessageFormatSoap',
           'esriSSEServerObjectCreated', 'IDataStoreValidator',
           'IServerObjectConfiguration', 'IGISServerConnection2',
           'esriSDTypeIndex', 'esriSDTypeJobs', 'ServerMachine',
           'IServiceDescription2', 'IServiceDescription3',
           'IServerObject', 'ConfigFactory', 'ServerDirectory',
           'esriServerInstallTypeDotnet', 'IGPServerHelper',
           'esriMSStopped', 'IServerDirectory',
           'ServerEnvironmentXHelper', 'ServerStatisticsResults',
           'IPermissionsManager', 'IRole', 'IRoleStore',
           'esriSDTypeCache', 'ServiceCatalog', 'esriSTPSecond',
           'IServerObjectType', 'esriSDTypeSystem',
           'ServerObjectConfiguration', 'IServerDirectoryInfo',
           'ServerLogImpl', 'IResponseStreamer', 'esriCSStopped',
           'IUser', 'esriServerConnectionTypeFailOver',
           'IServerEnvironmentXHelper', 'esriSSFMaximum',
           'IServerObjectExtensionType3',
           'IServerObjectExtensionType2', 'ServerP', 'Server',
           'esriSDTypeInput', 'esriSSEContextReleased',
           'GPServerHelper', 'esriSTPHour', 'ServerObjectAdmin',
           'esriMachineStatus', 'IServerObjectAdmin8',
           'esriServerInstallType', 'ServerObjectManager',
           'esriSSELogError', 'IServerMachineInfo',
           'IServerObjectExtension', 'esriStartupType',
           'IServiceDescription', 'IIdentity', 'IServiceCatalog3',
           'IServerObjectAdmin4', 'esriCSStarted', 'esriAccessPublic',
           'esriAccessPrivate', 'IServiceCatalogAdmin2',
           'esriSDCSliding', 'IServiceCatalog',
           'ServerStatisticsArray', 'esriServerTimePeriod',
           'IServerJobManager', 'esriSDCNone', 'IEnumServerMachine',
           'IServerErrorReports', 'IServerInit2',
           'IServerObjectHelper', 'IServerObjectAdmin2',
           'esriLoadBalancing', 'ISOMController',
           'IServerEnvironmentImpl',
           'esriServiceCatalogMessageFormat', 'IConfigurationFactory',
           'IServerObjectTypeInfo3',
           'IServerObjectConfigurationManager2', 'esriCSStopping',
           'IServerObjectAdmin5', 'IServerMachineStatus',
           'IServerObjectAdmin7', 'IServerObjectAdmin6',
           'IServerObjectAdmin3', 'IEnumServerObjectTypeInfo',
           'IServerStatistics', 'IServerObjectConfiguration5',
           'IServerStatus', 'User', 'esriServerDirectoryCleaningMode',
           'esriSTPDay', 'IServerObjectFactory', 'IServerLog',
           'esriSSFMean', 'IServerObjectConfiguration3',
           'ServerContext', 'esriServerExceptionHandlingMode',
           'esriSSFSumSquares', 'IServerObjectType4', 'esriSTPNone',
           'IServerObjectType3', 'IServerObjectType2',
           'ServerObjectTypeInfo', 'esriSSELogWarning',
           'esriAccessLevel', 'IServerInfos',
           'IServerObjectExtensionTypeInfo', 'esriServerIsolationLow',
           'esriServerConnectionTypeRoundRobin', 'esriSTManual',
           'IServerContext', 'IPermissionsAdmin2',
           'IEnumServerDirectory', 'ServerObjectExtensionType',
           'IServerCLRHost', 'IServerObjectHelper2',
           'IServerEnvironmentImpl2', 'IServerMachineEnvironment',
           'IServerObjectConfiguration4',
           'IServerObjectExtensionTypeInfo2', 'IServerEnvironmentEx',
           'IConfigurationFactory3', 'IConfigurationFactory2',
           'ServerObject', 'IServerConfigurationStorage',
           'esriSSEContextCreated', 'IServerHelper',
           'esriServerIsolationLevel', 'esriServerInstallTypeJava',
           'esriConfigurationStatus', 'IEnumServerObjectType',
           'ServerObjectConfigurationInfo',
           'esriSSEContextCreationFailed',
           'esriSSEContextCreationTimeout', 'IPermissionsAdmin',
           'esriLoadBalancingRoundRobin',
           'ServerObjectConfigurationStatus',
           'esriServerDirectoryType', 'IServer2',
           'IServerObjectConfigurationManager', 'IServerInit',
           'esriSSEContextUsageTimeout', 'IServerObjectExtensionType',
           'ServerObjectFactory', 'esriSSFCount',
           'IServerObjectConfigurationStatus',
           'IEnumServerObjectConfiguration', 'esriSDCAbsolute',
           'IServerTimeRange', 'IServiceCatalog2',
           'esriServerIsolationHigh', 'GISServerConnection',
           'ServerObjectFactoryX', 'esriCSPaused',
           'IServiceDescriptionArray', 'IGISServerConnection',
           'esriServerExceptionHandlingMode_ExitOnException',
           'IServer', 'IServerObjectExtensionManager',
           'IServerObjectTypeInfo2', 'IServerObjectConfigurationInfo',
           'esriLoadBalancingNone',
           'esriServerExceptionHandlingMode_Dump',
           'esriServerConnectionType', 'IServerObjectManager3',
           'IServerObjectManager2',
           'esriServerExceptionHandlingMode_ExitOnExceptionAndDump',
           'IEnumServerDirectoryInfo', 'esriCSDeleted',
           'IServerObjectFactoryX', 'IServerObjectManager4',
           'IServerDirectory2', 'IServerDirectory3', 'esriMStarted']
from comtypes import _check_version; _check_version('501')

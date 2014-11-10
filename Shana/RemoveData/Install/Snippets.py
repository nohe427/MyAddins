import _winreg
import arcpy

def GetLibPath():
    ##return "C:/Program Files/ArcGIS/com/"
    import _winreg
    keyESRI = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, \
                              "SOFTWARE\\ESRI\\ArcGIS")
    #return "C:\\Program Files (x86)\\ArcGIS\\Desktop10.2\\com\\"
    return _winreg.QueryValueEx(keyESRI, "InstallDir")[0] + "com\\"

def InitStandalone():
    pInit = NewObj(esriSystem.AoInitialize, \
                   esriSystem.IAoInitialize)
    eProduct = esriSystem.esriLicenseProductCodeArcEditor
    licenseStatus = pInit.IsProductCodeAvailable(eProduct)
    if licenseStatus == esriSystem.esriLicenseAvailable:
        licenseStatus = pInit.Initialize(eProduct)
        return (licenseStatus == esriSystem.esriLicenseCheckedOut)

def NewObj (MyClass, MyInterface):
    from comtypes.client import CreateObject
    try:
        ptr = CreateObject(MyClass, interface=MyInterface)
        return ptr
    except:
        return None
    
def CType(obj, interface):
    try:
        newobj = obj.QueryInterface(interface)
        return newobj
    except:
        return None

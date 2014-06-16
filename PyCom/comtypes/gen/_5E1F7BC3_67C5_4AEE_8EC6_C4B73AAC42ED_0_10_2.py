# -*- coding: mbcs -*-
typelib_path = u'C:\\Program Files (x86)\\ArcGIS\\Engine10.2\\com\\esriSystem.olb'
_lcid = 0 # change this if required
from ctypes import *
from comtypes import GUID
from comtypes import CoClass
import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0
from comtypes.automation import VARIANT
from ctypes import HRESULT
from comtypes import BSTR
from comtypes import helpstring
from comtypes import COMMETHOD
from comtypes import dispid
from ctypes import Array
from ctypes.wintypes import VARIANT_BOOL
from comtypes import IUnknown
from comtypes.automation import _midlSAFEARRAY
from ctypes.wintypes import _LARGE_INTEGER
from comtypes import IPersist
from ctypes.wintypes import _ULARGE_INTEGER
from ctypes.wintypes import _ULARGE_INTEGER
OLE_COLOR = c_int
OLE_HANDLE = c_int
from ctypes.wintypes import _FILETIME
WSTRING = c_wchar_p
from ctypes.wintypes import tagRECT
from ctypes.wintypes import tagRECT


class _WKSEnvelope(Structure):
    pass
_WKSEnvelope._fields_ = [
    ('XMin', c_double),
    ('YMin', c_double),
    ('XMax', c_double),
    ('YMax', c_double),
]
assert sizeof(_WKSEnvelope) == 32, sizeof(_WKSEnvelope)
assert alignment(_WKSEnvelope) == 8, alignment(_WKSEnvelope)
class InputDeviceManager(CoClass):
    u'Input Device Manager - a singleton.'
    _reg_clsid_ = GUID('{71D66954-D2BF-4FDD-86C6-68B062402780}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class IInputDeviceManager(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that give life to Input Devices.'
    _iid_ = GUID('{52620D38-E275-4725-A976-65BCDD2C93FD}')
    _idlflags_ = ['oleautomation']
InputDeviceManager._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IInputDeviceManager]

class IClassify(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the classification methods.'
    _iid_ = GUID('{D5C7A525-DFB8-11D1-AAAD-00C04FA334B3}')
    _idlflags_ = ['oleautomation']
class IUID(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Provides access to members that work with globally unique identifier objects.'
    _iid_ = GUID('{1714D59B-FB22-11D1-94A2-080009EEBECB}')
    _idlflags_ = ['dual', 'oleautomation', 'hidden']
IClassify._methods_ = [
    COMMETHOD([helpstring(u'Adds data in form of a histogram (array of values (doubles) and a paired array of frequencies (longs)) to the classification.')], HRESULT, 'SetHistogramData',
              ( ['in'], VARIANT, 'doubleArrayValues' ),
              ( ['in'], VARIANT, 'longArrayFrequencies' )),
    COMMETHOD([helpstring(u'Classifies data into the specified number of classes.')], HRESULT, 'Classify',
              ( ['in', 'out'], POINTER(c_int), 'numClasses' )),
    COMMETHOD(['propget', helpstring(u'The array of class breaks (double).  ClassBreaks(0) is the minimum value in the dataset, and subsequent breaks represent the upper limit of each class.')], HRESULT, 'ClassBreaks',
              ( ['retval', 'out'], POINTER(VARIANT), 'doubleArrayBreaks' )),
    COMMETHOD(['propget', helpstring(u'The name of the classification method (based on choice of classification object).')], HRESULT, 'MethodName',
              ( ['retval', 'out'], POINTER(BSTR), 'txt' )),
    COMMETHOD(['propget', helpstring(u'The CLSID for the classification object.')], HRESULT, 'ClassID',
              ( ['retval', 'out'], POINTER(POINTER(IUID)), 'clsid' )),
]
################################################################
## code template for IClassify implementation
##class IClassify_Impl(object):
##    @property
##    def ClassID(self):
##        u'The CLSID for the classification object.'
##        #return clsid
##
##    @property
##    def MethodName(self):
##        u'The name of the classification method (based on choice of classification object).'
##        #return txt
##
##    def Classify(self):
##        u'Classifies data into the specified number of classes.'
##        #return numClasses
##
##    def SetHistogramData(self, doubleArrayValues, longArrayFrequencies):
##        u'Adds data in form of a histogram (array of values (doubles) and a paired array of frequencies (longs)) to the classification.'
##        #return 
##
##    @property
##    def ClassBreaks(self):
##        u'The array of class breaks (double).  ClassBreaks(0) is the minimum value in the dataset, and subsequent breaks represent the upper limit of each class.'
##        #return doubleArrayBreaks
##

class _WKSEnvelopeZ(Structure):
    pass
WKSEnvelopeZ = _WKSEnvelopeZ
class IJobFilter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods of job filter.'
    _iid_ = GUID('{2C2D291A-51FD-4BFD-99A5-DB889FCEE9F2}')
    _idlflags_ = ['oleautomation']
class ILongArray(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control long arrays.'
    _iid_ = GUID('{54F9FFB6-E91F-11D2-9F81-00C04F8ECE27}')
    _idlflags_ = ['oleautomation']
IJobFilter._methods_ = [
    COMMETHOD(['propget', helpstring(u'statuses of the jobs to search')], HRESULT, 'JobStatuses',
              ( ['retval', 'out'], POINTER(POINTER(ILongArray)), 'ppStatusArray' )),
    COMMETHOD(['propputref', helpstring(u'statuses of the jobs to search')], HRESULT, 'JobStatuses',
              ( ['in'], POINTER(ILongArray), 'ppStatusArray' )),
]
################################################################
## code template for IJobFilter implementation
##class IJobFilter_Impl(object):
##    def JobStatuses(self, ppStatusArray):
##        u'statuses of the jobs to search'
##        #return 
##

class Set(CoClass):
    u'Generic set of objects.'
    _reg_clsid_ = GUID('{33848E03-983B-11D1-8463-0000F875B9C6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class ISet(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control a simple set of objects.'
    _iid_ = GUID('{33848E02-983B-11D1-8463-0000F875B9C6}')
    _idlflags_ = ['oleautomation']
Set._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ISet]

class _esriPointAttributesEx(Structure):
    pass
esriPointAttributesEx = _esriPointAttributesEx
class ITimeDuration(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Time Duration.'
    _iid_ = GUID('{953DC994-AA0D-4193-9C1F-469B60D61711}')
    _idlflags_ = ['oleautomation']
class _WKSTimeDuration(Structure):
    pass
WKSTimeDuration = _WKSTimeDuration
ITimeDuration._methods_ = [
    COMMETHOD(['propget', helpstring(u'The time duration days component.')], HRESULT, 'Days',
              ( ['retval', 'out'], POINTER(c_int), 'Days' )),
    COMMETHOD(['propput', helpstring(u'The time duration days component.')], HRESULT, 'Days',
              ( ['in'], c_int, 'Days' )),
    COMMETHOD(['propget', helpstring(u'The time duration hours component.')], HRESULT, 'Hours',
              ( ['retval', 'out'], POINTER(c_int), 'Hours' )),
    COMMETHOD(['propput', helpstring(u'The time duration hours component.')], HRESULT, 'Hours',
              ( ['in'], c_int, 'Hours' )),
    COMMETHOD(['propget', helpstring(u'The time duration minutes component.')], HRESULT, 'Minutes',
              ( ['retval', 'out'], POINTER(c_int), 'Minutes' )),
    COMMETHOD(['propput', helpstring(u'The time duration minutes component.')], HRESULT, 'Minutes',
              ( ['in'], c_int, 'Minutes' )),
    COMMETHOD(['propget', helpstring(u'The time duration seconds component.')], HRESULT, 'Seconds',
              ( ['retval', 'out'], POINTER(c_int), 'Seconds' )),
    COMMETHOD(['propput', helpstring(u'The time duration seconds component.')], HRESULT, 'Seconds',
              ( ['in'], c_int, 'Seconds' )),
    COMMETHOD(['propget', helpstring(u'The time duration nanoseconds component.')], HRESULT, 'Nanoseconds',
              ( ['retval', 'out'], POINTER(c_int), 'Nanoseconds' )),
    COMMETHOD(['propput', helpstring(u'The time duration nanoseconds component.')], HRESULT, 'Nanoseconds',
              ( ['in'], c_int, 'Nanoseconds' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the time duration value is positive or negative.')], HRESULT, 'Positive',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Positive' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether the time duration value is positive or negative.')], HRESULT, 'Positive',
              ( ['in'], VARIANT_BOOL, 'Positive' )),
    COMMETHOD([helpstring(u'Obtains time as a WKSTimeDuration.')], HRESULT, 'QueryWKSTimeDuration',
              ( ['retval', 'out'], POINTER(WKSTimeDuration), 'TimeDuration' )),
    COMMETHOD([helpstring(u'Writes the time from a given WKSTimeDuration value.')], HRESULT, 'SetFromWKSTimeDuration',
              ( ['in'], POINTER(WKSTimeDuration), 'TimeDuration' )),
    COMMETHOD([helpstring(u'Obtains the time duration as an XML time duration string.')], HRESULT, 'QueryXMLTimeDurationString',
              ( ['retval', 'out'], POINTER(BSTR), 'xmlTimeDurationString' )),
    COMMETHOD([helpstring(u'Writes the time duration from an XML time duration string.')], HRESULT, 'SetFromXMLTimeDurationString',
              ( ['in'], BSTR, 'xmlTimeDurationString' )),
    COMMETHOD([helpstring(u'Adds the input amount of weeks to the time duration.')], HRESULT, 'AddWeeks',
              ( ['in'], c_double, 'Value' )),
    COMMETHOD([helpstring(u'Adds the input amount of days to the time duration.')], HRESULT, 'AddDays',
              ( ['in'], c_double, 'Value' )),
    COMMETHOD([helpstring(u'Adds the input amount of hours to the time duration.')], HRESULT, 'AddHours',
              ( ['in'], c_double, 'Value' )),
    COMMETHOD([helpstring(u'Adds the input amount of minutes to the time duration.')], HRESULT, 'AddMinutes',
              ( ['in'], c_double, 'Value' )),
    COMMETHOD([helpstring(u'Adds the input amount of seconds to the time duration.')], HRESULT, 'AddSeconds',
              ( ['in'], c_double, 'Value' )),
    COMMETHOD([helpstring(u'Adds the input amount of milliseconds to the time duration.')], HRESULT, 'AddMilliseconds',
              ( ['in'], c_double, 'Value' )),
    COMMETHOD([helpstring(u'Adds the input amount of nanoseconds to the time duration.')], HRESULT, 'AddNanoseconds',
              ( ['in'], c_longlong, 'Value' )),
    COMMETHOD([helpstring(u'Obtains the time duration as total days floating point value.')], HRESULT, 'QueryTotalDays',
              ( ['retval', 'out'], POINTER(c_double), 'totalDays' )),
    COMMETHOD([helpstring(u'Obtains the time duration as total hours floating point value.')], HRESULT, 'QueryTotalHours',
              ( ['retval', 'out'], POINTER(c_double), 'totalHours' )),
    COMMETHOD([helpstring(u'Obtains the time duration as total minutes floating point value.')], HRESULT, 'QueryTotalMinutes',
              ( ['retval', 'out'], POINTER(c_double), 'totalMinutes' )),
    COMMETHOD([helpstring(u'Obtains the time duration as total seconds floating point value.')], HRESULT, 'QueryTotalSeconds',
              ( ['retval', 'out'], POINTER(c_double), 'totalSeconds' )),
    COMMETHOD([helpstring(u'The time duration day fraction portion as a day fraction. Corresponds to the Hour, Minute, Second, and Nanoseconds properties.')], HRESULT, 'QueryDayFraction',
              ( ['retval', 'out'], POINTER(c_double), 'dayFraction' )),
    COMMETHOD([helpstring(u'The time duration day fraction portion as a day fraction. Corresponds to the Hour, Minute, Second, and Nanoseconds properties.')], HRESULT, 'SetDayFraction',
              ( ['in'], c_double, 'dayFraction' )),
    COMMETHOD([helpstring(u'The time duration day fraction portion as the number of nanoseconds elapsed since midnight. Corresponds to the Hour, Minute, Second, and Nanoseconds properties.')], HRESULT, 'QueryDayFractionNanoseconds',
              ( ['retval', 'out'], POINTER(c_longlong), 'dayFractionNanoseconds' )),
    COMMETHOD([helpstring(u'The time duration day fraction portion as the number of nanoseconds elapsed since midnight. Corresponds to the Hour, Minute, Second, and Nanoseconds properties.')], HRESULT, 'SetDayFractionNanoseconds',
              ( ['in'], c_longlong, 'dayFractionNanoseconds' )),
    COMMETHOD([helpstring(u'Obtains the time duration as the number of ticks.')], HRESULT, 'QueryTicks',
              ( ['retval', 'out'], POINTER(c_longlong), 'ticks' )),
    COMMETHOD([helpstring(u'Writes the time duration from a given number of ticks.')], HRESULT, 'SetFromTicks',
              ( ['in'], c_longlong, 'ticks' )),
    COMMETHOD([helpstring(u'Reset the time duration to zero.')], HRESULT, 'Reset'),
    COMMETHOD([helpstring(u'Scales the time duration by a scale factor.')], HRESULT, 'Scale',
              ( ['in'], c_double, 'scaleFactor' )),
    COMMETHOD([helpstring(u'Adds a time duration.')], HRESULT, 'AddDuration',
              ( ['in'], POINTER(ITimeDuration), 'TimeDuration' )),
    COMMETHOD([helpstring(u'Subtracts a time duration.')], HRESULT, 'SubtractDuration',
              ( ['in'], POINTER(ITimeDuration), 'TimeDuration' )),
    COMMETHOD([helpstring(u"Indicates whether the time duration's value is zero.")], HRESULT, 'IsZero',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsZero' )),
    COMMETHOD([helpstring(u"Compares this time duration to the other time duration. Returns -1 if this time duration's value is less, 1 if greater, and 0 otherwise.")], HRESULT, 'Compare',
              ( ['in'], POINTER(ITimeDuration), 'otherDuration' ),
              ( ['retval', 'out'], POINTER(c_int), 'Result' )),
]
################################################################
## code template for ITimeDuration implementation
##class ITimeDuration_Impl(object):
##    def AddSeconds(self, Value):
##        u'Adds the input amount of seconds to the time duration.'
##        #return 
##
##    def Scale(self, scaleFactor):
##        u'Scales the time duration by a scale factor.'
##        #return 
##
##    def AddHours(self, Value):
##        u'Adds the input amount of hours to the time duration.'
##        #return 
##
##    def _get(self):
##        u'Indicates whether the time duration value is positive or negative.'
##        #return Positive
##    def _set(self, Positive):
##        u'Indicates whether the time duration value is positive or negative.'
##    Positive = property(_get, _set, doc = _set.__doc__)
##
##    def QueryTicks(self):
##        u'Obtains the time duration as the number of ticks.'
##        #return ticks
##
##    def QueryWKSTimeDuration(self):
##        u'Obtains time as a WKSTimeDuration.'
##        #return TimeDuration
##
##    def AddNanoseconds(self, Value):
##        u'Adds the input amount of nanoseconds to the time duration.'
##        #return 
##
##    def QueryTotalSeconds(self):
##        u'Obtains the time duration as total seconds floating point value.'
##        #return totalSeconds
##
##    def _get(self):
##        u'The time duration hours component.'
##        #return Hours
##    def _set(self, Hours):
##        u'The time duration hours component.'
##    Hours = property(_get, _set, doc = _set.__doc__)
##
##    def QueryXMLTimeDurationString(self):
##        u'Obtains the time duration as an XML time duration string.'
##        #return xmlTimeDurationString
##
##    def QueryDayFractionNanoseconds(self):
##        u'The time duration day fraction portion as the number of nanoseconds elapsed since midnight. Corresponds to the Hour, Minute, Second, and Nanoseconds properties.'
##        #return dayFractionNanoseconds
##
##    def _get(self):
##        u'The time duration seconds component.'
##        #return Seconds
##    def _set(self, Seconds):
##        u'The time duration seconds component.'
##    Seconds = property(_get, _set, doc = _set.__doc__)
##
##    def QueryTotalMinutes(self):
##        u'Obtains the time duration as total minutes floating point value.'
##        #return totalMinutes
##
##    def SetDayFractionNanoseconds(self, dayFractionNanoseconds):
##        u'The time duration day fraction portion as the number of nanoseconds elapsed since midnight. Corresponds to the Hour, Minute, Second, and Nanoseconds properties.'
##        #return 
##
##    def QueryDayFraction(self):
##        u'The time duration day fraction portion as a day fraction. Corresponds to the Hour, Minute, Second, and Nanoseconds properties.'
##        #return dayFraction
##
##    def Reset(self):
##        u'Reset the time duration to zero.'
##        #return 
##
##    def AddWeeks(self, Value):
##        u'Adds the input amount of weeks to the time duration.'
##        #return 
##
##    def SetFromWKSTimeDuration(self, TimeDuration):
##        u'Writes the time from a given WKSTimeDuration value.'
##        #return 
##
##    def _get(self):
##        u'The time duration days component.'
##        #return Days
##    def _set(self, Days):
##        u'The time duration days component.'
##    Days = property(_get, _set, doc = _set.__doc__)
##
##    def SetDayFraction(self, dayFraction):
##        u'The time duration day fraction portion as a day fraction. Corresponds to the Hour, Minute, Second, and Nanoseconds properties.'
##        #return 
##
##    def AddDuration(self, TimeDuration):
##        u'Adds a time duration.'
##        #return 
##
##    def IsZero(self):
##        u"Indicates whether the time duration's value is zero."
##        #return IsZero
##
##    def _get(self):
##        u'The time duration minutes component.'
##        #return Minutes
##    def _set(self, Minutes):
##        u'The time duration minutes component.'
##    Minutes = property(_get, _set, doc = _set.__doc__)
##
##    def SetFromTicks(self, ticks):
##        u'Writes the time duration from a given number of ticks.'
##        #return 
##
##    def AddMinutes(self, Value):
##        u'Adds the input amount of minutes to the time duration.'
##        #return 
##
##    def QueryTotalDays(self):
##        u'Obtains the time duration as total days floating point value.'
##        #return totalDays
##
##    def _get(self):
##        u'The time duration nanoseconds component.'
##        #return Nanoseconds
##    def _set(self, Nanoseconds):
##        u'The time duration nanoseconds component.'
##    Nanoseconds = property(_get, _set, doc = _set.__doc__)
##
##    def AddDays(self, Value):
##        u'Adds the input amount of days to the time duration.'
##        #return 
##
##    def SetFromXMLTimeDurationString(self, xmlTimeDurationString):
##        u'Writes the time duration from an XML time duration string.'
##        #return 
##
##    def AddMilliseconds(self, Value):
##        u'Adds the input amount of milliseconds to the time duration.'
##        #return 
##
##    def QueryTotalHours(self):
##        u'Obtains the time duration as total hours floating point value.'
##        #return totalHours
##
##    def SubtractDuration(self, TimeDuration):
##        u'Subtracts a time duration.'
##        #return 
##
##    def Compare(self, otherDuration):
##        u"Compares this time duration to the other time duration. Returns -1 if this time duration's value is less, 1 if greater, and 0 otherwise."
##        #return Result
##

class _esriPointAttributes(Structure):
    pass
_esriPointAttributes._fields_ = [
    ('pointZ', c_double),
    ('pointM', c_double),
    ('pointID', c_int),
    ('awarenessInfo', c_char),
]
assert sizeof(_esriPointAttributes) == 24, sizeof(_esriPointAttributes)
assert alignment(_esriPointAttributes) == 8, alignment(_esriPointAttributes)
_esriPointAttributesEx._fields_ = [
    ('awarenessInfo', c_int),
    ('arraySize', c_int),
    ('attributeArray', POINTER(c_ubyte)),
]
assert sizeof(_esriPointAttributesEx) == 12, sizeof(_esriPointAttributesEx)
assert alignment(_esriPointAttributesEx) == 4, alignment(_esriPointAttributesEx)
class IXMLPersistedObject(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members to set or retrieve an object to be serialized to XML. The object must support IPersistStream or IPersistVariant.'
    _iid_ = GUID('{E2015546-27B9-4AC4-BB8B-64B429513D44}')
    _idlflags_ = ['oleautomation']
IXMLPersistedObject._methods_ = [
    COMMETHOD(['propget', helpstring(u'The object to be serialized to or deserialized from XML.')], HRESULT, 'Object',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'ppObject' )),
    COMMETHOD(['propputref', helpstring(u'The object to be serialized to or deserialized from XML.')], HRESULT, 'Object',
              ( ['in'], POINTER(IUnknown), 'ppObject' )),
]
################################################################
## code template for IXMLPersistedObject implementation
##class IXMLPersistedObject_Impl(object):
##    def Object(self, ppObject):
##        u'The object to be serialized to or deserialized from XML.'
##        #return 
##

class IGlobeCompression(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to compress and uncompress JPEG data used by ArcGlobe.'
    _iid_ = GUID('{650FC137-7869-4414-A511-F7E176D3301E}')
    _idlflags_ = []
IGlobeCompression._methods_ = [
    COMMETHOD([helpstring(u'Initialize for the compression of Globe JPEG data.')], HRESULT, 'InitGlobeCompression'),
    COMMETHOD([helpstring(u'End the compression of Globe JPEG data.')], HRESULT, 'EndGlobeCompression'),
    COMMETHOD([helpstring(u'Compress rgba data to Globe JPEG format.')], HRESULT, 'GlobeToJPEG',
              ( ['in'], c_int, 'inputSize' ),
              ( ['in'], POINTER(c_ubyte), 'pSrcData' ),
              ( ['in'], c_int, 'quality' ),
              ( ['out'], POINTER(c_int), 'pOutputSize' ),
              ( ['out'], POINTER(c_ubyte), 'pDestData' )),
    COMMETHOD([helpstring(u'UnCompress the Globe JPEG format to rgba data.')], HRESULT, 'GlobeFromJPEG',
              ( ['in'], c_int, 'inputSize' ),
              ( ['in'], POINTER(c_ubyte), 'pSrcData' ),
              ( ['in'], VARIANT_BOOL, 'use5551' ),
              ( ['out'], POINTER(c_int), 'pOutputSize' ),
              ( ['out'], POINTER(c_ubyte), 'pDestData' )),
]
################################################################
## code template for IGlobeCompression implementation
##class IGlobeCompression_Impl(object):
##    def InitGlobeCompression(self):
##        u'Initialize for the compression of Globe JPEG data.'
##        #return 
##
##    def GlobeFromJPEG(self, inputSize, pSrcData, use5551):
##        u'UnCompress the Globe JPEG format to rgba data.'
##        #return pOutputSize, pDestData
##
##    def GlobeToJPEG(self, inputSize, pSrcData, quality):
##        u'Compress rgba data to Globe JPEG format.'
##        #return pOutputSize, pDestData
##
##    def EndGlobeCompression(self):
##        u'End the compression of Globe JPEG data.'
##        #return 
##

class ObjectStream(CoClass):
    u'Specialized kind of IStream for objects.'
    _reg_clsid_ = GUID('{043731D0-A7CF-11D1-8BD1-080009EE4E41}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class ISequentialStream(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0C733A30-2A1C-11CE-ADE5-00AA0044773D}')
    _idlflags_ = []
class IStream(ISequentialStream):
    _case_insensitive_ = True
    _iid_ = GUID('{0000000C-0000-0000-C000-000000000046}')
    _idlflags_ = []
class IObjectStream(IStream):
    _case_insensitive_ = True
    u'Provides access to members used to make objects and object references persistant.  Use of this interface allows multiple references to the same object to be stored properly.'
    _iid_ = GUID('{18A45BA7-1266-11D1-86AD-0000F8751720}')
    _idlflags_ = []
class IDocumentVersion(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the document version.'
    _iid_ = GUID('{ECC43C55-0148-4EC1-BF87-B9A183C5DC98}')
    _idlflags_ = []
ObjectStream._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IObjectStream, IDocumentVersion]

class IESRIScriptEngine(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the ESRIScriptEngine.'
    _iid_ = GUID('{52B13A57-AA06-49BE-A4D0-3CDDAC943EBE}')
    _idlflags_ = ['oleautomation']
IESRIScriptEngine._methods_ = [
    COMMETHOD(['propget', helpstring(u'The Script Language.')], HRESULT, 'Language',
              ( ['retval', 'out'], POINTER(BSTR), 'pLanguage' )),
    COMMETHOD(['propput', helpstring(u'The Script Language.')], HRESULT, 'Language',
              ( ['in'], BSTR, 'pLanguage' )),
    COMMETHOD(['propget', helpstring(u'The AllowUI method.')], HRESULT, 'AllowUI',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pAllowUI' )),
    COMMETHOD(['propput', helpstring(u'The AllowUI method.')], HRESULT, 'AllowUI',
              ( ['in'], VARIANT_BOOL, 'pAllowUI' )),
    COMMETHOD([helpstring(u'The AddCode method.')], HRESULT, 'AddCode',
              ( ['in'], BSTR, 'scriptCode' )),
    COMMETHOD([helpstring(u'The Run method.')], HRESULT, 'Run',
              ( ['in'], BSTR, 'procedureName' ),
              ( ['in'], POINTER(_midlSAFEARRAY(POINTER(BSTR))), 'pParameters' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'pResult' )),
    COMMETHOD(['propget', helpstring(u'The Error method.')], HRESULT, 'Error',
              ( ['in'], POINTER(c_int), 'pLineNumber' ),
              ( ['in'], POINTER(c_int), 'pCharacterPosition' ),
              ( ['in'], POINTER(BSTR), 'pErrorSourceCode' ),
              ( ['in'], POINTER(BSTR), 'pErrorDescription' )),
]
################################################################
## code template for IESRIScriptEngine implementation
##class IESRIScriptEngine_Impl(object):
##    def AddCode(self, scriptCode):
##        u'The AddCode method.'
##        #return 
##
##    def _get(self):
##        u'The AllowUI method.'
##        #return pAllowUI
##    def _set(self, pAllowUI):
##        u'The AllowUI method.'
##    AllowUI = property(_get, _set, doc = _set.__doc__)
##
##    def Run(self, procedureName, pParameters):
##        u'The Run method.'
##        #return pResult
##
##    def _get(self):
##        u'The Script Language.'
##        #return pLanguage
##    def _set(self, pLanguage):
##        u'The Script Language.'
##    Language = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Error(self, pLineNumber, pCharacterPosition, pErrorSourceCode, pErrorDescription):
##        u'The Error method.'
##        #return 
##

class _esriSegmentModifier(Structure):
    pass
esriSegmentModifier = _esriSegmentModifier
class IXMLSerialize(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that XML serialize and deserialize an object to/from XML.'
    _iid_ = GUID('{C8545045-6615-48E3-AF27-52A0E5FC35E2}')
    _idlflags_ = ['oleautomation']
class IXMLSerializeData(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that serialize and deserialize data from XML.'
    _iid_ = GUID('{5BB4A18D-43BC-41C5-987A-2206FD15488F}')
    _idlflags_ = ['oleautomation']
IXMLSerialize._methods_ = [
    COMMETHOD([helpstring(u'Serializes an object to XML.')], HRESULT, 'Serialize',
              ( ['in'], POINTER(IXMLSerializeData), 'data' )),
    COMMETHOD([helpstring(u'Deserializes an object from XML.')], HRESULT, 'Deserialize',
              ( ['in'], POINTER(IXMLSerializeData), 'data' )),
]
################################################################
## code template for IXMLSerialize implementation
##class IXMLSerialize_Impl(object):
##    def Serialize(self, data):
##        u'Serializes an object to XML.'
##        #return 
##
##    def Deserialize(self, data):
##        u'Deserializes an object from XML.'
##        #return 
##

class IJobDefinition(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to properties of job definition.'
    _iid_ = GUID('{C24F654B-B929-443B-9FA1-A2A83BBCE14B}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriAGSInternetMessageFormat'
esriAGSInternetMessageFormatSoap = 1
esriAGSInternetMessageFormatBin = 2
esriAGSInternetMessageFormat = c_int # enum
IJobDefinition._methods_ = [
    COMMETHOD(['propget', helpstring(u'Format of request.')], HRESULT, 'RequestFormat',
              ( ['retval', 'out'], POINTER(esriAGSInternetMessageFormat), 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Request message in SOAP format.')], HRESULT, 'StringRequest',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Request message in SOAP format.')], HRESULT, 'StringRequest',
              ( ['in'], BSTR, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Request message in binary format.')], HRESULT, 'BinaryRequest',
              ( ['retval', 'out'], POINTER(_midlSAFEARRAY(c_ubyte)), 'ppVal' )),
    COMMETHOD(['propput', helpstring(u'Request message in binary format.')], HRESULT, 'BinaryRequest',
              ( ['in'], _midlSAFEARRAY(c_ubyte), 'ppVal' )),
    COMMETHOD(['propget', helpstring(u'Required capabilities of job processor.')], HRESULT, 'Capabilities',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Required capabilities of job processor.')], HRESULT, 'Capabilities',
              ( ['in'], BSTR, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'REST Format of request.')], HRESULT, 'IsRESTFormat',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD([helpstring(u'Request message in REST format.')], HRESULT, 'GetRESTRequest',
              ( ['out'], POINTER(BSTR), 'pResourceName' ),
              ( ['out'], POINTER(BSTR), 'pRperationName' ),
              ( ['out'], POINTER(BSTR), 'pRperationInput' ),
              ( ['out'], POINTER(BSTR), 'pOutputFormat' ),
              ( ['out'], POINTER(BSTR), 'pRequestProperties' )),
    COMMETHOD([helpstring(u'Request message in REST format.')], HRESULT, 'SetRESTRequest',
              ( ['in'], BSTR, 'resourceName' ),
              ( ['in'], BSTR, 'operationName' ),
              ( ['in'], BSTR, 'operationInput' ),
              ( ['in'], BSTR, 'outputFormat' ),
              ( ['in'], BSTR, 'requestProperties' )),
]
################################################################
## code template for IJobDefinition implementation
##class IJobDefinition_Impl(object):
##    def _get(self):
##        u'Request message in SOAP format.'
##        #return pVal
##    def _set(self, pVal):
##        u'Request message in SOAP format.'
##    StringRequest = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Request message in binary format.'
##        #return ppVal
##    def _set(self, ppVal):
##        u'Request message in binary format.'
##    BinaryRequest = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Required capabilities of job processor.'
##        #return pVal
##    def _set(self, pVal):
##        u'Required capabilities of job processor.'
##    Capabilities = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def RequestFormat(self):
##        u'Format of request.'
##        #return pVal
##
##    def GetRESTRequest(self):
##        u'Request message in REST format.'
##        #return pResourceName, pRperationName, pRperationInput, pOutputFormat, pRequestProperties
##
##    @property
##    def IsRESTFormat(self):
##        u'REST Format of request.'
##        #return pVal
##
##    def SetRESTRequest(self, resourceName, operationName, operationInput, outputFormat, requestProperties):
##        u'Request message in REST format.'
##        #return 
##


# values for enumeration 'esriArcGISVersion'
esriArcGISVersion83 = 0
esriArcGISVersion90 = 1
esriArcGISVersion92 = 2
esriArcGISVersion93 = 3
esriArcGISVersion10 = 4
esriArcGISVersion101 = 5
esriArcGISVersionCurrent = 5
esriArcGISVersion = c_int # enum
IDocumentVersion._methods_ = [
    COMMETHOD(['propput', helpstring(u'The version of the document to save.')], HRESULT, 'DocumentVersion',
              ( ['in'], esriArcGISVersion, 'docVersion' )),
    COMMETHOD(['propget', helpstring(u'The version of the document to save.')], HRESULT, 'DocumentVersion',
              ( ['retval', 'out'], POINTER(esriArcGISVersion), 'docVersion' )),
]
################################################################
## code template for IDocumentVersion implementation
##class IDocumentVersion_Impl(object):
##    def _get(self):
##        u'The version of the document to save.'
##        #return docVersion
##    def _set(self, docVersion):
##        u'The version of the document to save.'
##    DocumentVersion = property(_get, _set, doc = _set.__doc__)
##

_esriSegmentModifier._fields_ = [
    ('FromPoint', c_int),
    ('SegmentType', c_int),
    ('SegmentInfo', c_ubyte * 1),
]
assert sizeof(_esriSegmentModifier) == 12, sizeof(_esriSegmentModifier)
assert alignment(_esriSegmentModifier) == 4, alignment(_esriSegmentModifier)
class IPropertySet(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members for managing a PropertySet.'
    _iid_ = GUID('{F0BA6ABC-8E9F-11D0-B4AB-0000F8037368}')
    _idlflags_ = ['oleautomation']
IXMLSerializeData._methods_ = [
    COMMETHOD(['propget', helpstring(u'XML type of the object.')], HRESULT, 'TypeName',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'XML type namespace of the object.')], HRESULT, 'TypeNamespaceURI',
              ( ['retval', 'out'], POINTER(BSTR), 'ns' )),
    COMMETHOD(['propput', helpstring(u'XML type of the object.')], HRESULT, 'TypeName',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD(['propput', helpstring(u'XML type namespace of the object.')], HRESULT, 'TypeNamespaceURI',
              ( ['in'], BSTR, 'ns' )),
    COMMETHOD(['propget', helpstring(u'Properties for serialization and deserialization.')], HRESULT, 'Properties',
              ( ['retval', 'out'], POINTER(POINTER(IPropertySet)), 'props' )),
    COMMETHOD(['propputref', helpstring(u'Properties for serialization and deserialization.')], HRESULT, 'Properties',
              ( ['in'], POINTER(IPropertySet), 'props' )),
    COMMETHOD([helpstring(u'Finds an XML element by name.')], HRESULT, 'Find',
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(c_int), 'index' )),
    COMMETHOD(['propget', helpstring(u'Number of XML elements.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD([helpstring(u'Obtains element value as a string.')], HRESULT, 'GetString',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([helpstring(u'Obtains element value as a boolean.')], HRESULT, 'GetBoolean',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([helpstring(u'Obtains element value as a byte.')], HRESULT, 'GetByte',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(c_ubyte), 'Value' )),
    COMMETHOD([helpstring(u'Obtains element value as a short.')], HRESULT, 'GetShort',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(c_short), 'Value' )),
    COMMETHOD([helpstring(u'Obtains element value as an integer.')], HRESULT, 'GetInteger',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([helpstring(u'Obtains element value as a float.')], HRESULT, 'GetFloat',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(c_float), 'Value' )),
    COMMETHOD([helpstring(u'Obtains element value as a double.')], HRESULT, 'GetDouble',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(c_double), 'Value' )),
    COMMETHOD([helpstring(u'Obtains element value as a date.')], HRESULT, 'GetDate',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(c_double), 'Value' )),
    COMMETHOD([helpstring(u'Obtains element value as an object instance.')], HRESULT, 'GetObject',
              ( ['in'], c_int, 'index' ),
              ( ['in'], BSTR, 'typeNamespace' ),
              ( ['in'], BSTR, 'TypeName' ),
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'Value' )),
    COMMETHOD([helpstring(u'Obtains element value as an array of bytes.')], HRESULT, 'GetBinary',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(_midlSAFEARRAY(c_ubyte)), 'Value' )),
    COMMETHOD([helpstring(u'Obtains element value as a variant.')], HRESULT, 'GetVariant',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'Value' )),
    COMMETHOD([helpstring(u'Adds element value as a string.')], HRESULT, 'AddString',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], BSTR, 'Value' )),
    COMMETHOD([helpstring(u'Adds element value as a boolean.')], HRESULT, 'AddBoolean',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], VARIANT_BOOL, 'Value' )),
    COMMETHOD([helpstring(u'Adds element value as a byte.')], HRESULT, 'AddByte',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], c_ubyte, 'Value' )),
    COMMETHOD([helpstring(u'Adds element value as a short.')], HRESULT, 'AddShort',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], c_short, 'Value' )),
    COMMETHOD([helpstring(u'Adds element value as an integer.')], HRESULT, 'AddInteger',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([helpstring(u'Adds element value as a float.')], HRESULT, 'AddFloat',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], c_float, 'Value' )),
    COMMETHOD([helpstring(u'Adds element value as a double.')], HRESULT, 'AddDouble',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], c_double, 'Value' )),
    COMMETHOD([helpstring(u'Adds element value as a date.')], HRESULT, 'AddDate',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], c_double, 'Value' )),
    COMMETHOD([helpstring(u'Adds element value as an object.')], HRESULT, 'AddObject',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], POINTER(IUnknown), 'Value' )),
    COMMETHOD([helpstring(u'Adds element value as an array of bytes.')], HRESULT, 'AddBinary',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], POINTER(_midlSAFEARRAY(c_ubyte)), 'Value' )),
    COMMETHOD([helpstring(u'Adds element value as a variant.')], HRESULT, 'AddVariant',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], VARIANT, 'Value' )),
    COMMETHOD([helpstring(u'Writes the value for a serialization flag.')], HRESULT, 'SetFlag',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], VARIANT_BOOL, 'FlagValue' )),
    COMMETHOD([helpstring(u'Obtains the value for a serialization flag.')], HRESULT, 'GetFlag',
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'FlagValue' )),
]
################################################################
## code template for IXMLSerializeData implementation
##class IXMLSerializeData_Impl(object):
##    def GetFloat(self, index):
##        u'Obtains element value as a float.'
##        #return Value
##
##    def AddVariant(self, Name, Value):
##        u'Adds element value as a variant.'
##        #return 
##
##    def GetInteger(self, index):
##        u'Obtains element value as an integer.'
##        #return Value
##
##    def AddDate(self, Name, Value):
##        u'Adds element value as a date.'
##        #return 
##
##    def GetDouble(self, index):
##        u'Obtains element value as a double.'
##        #return Value
##
##    def _get(self):
##        u'XML type namespace of the object.'
##        #return ns
##    def _set(self, ns):
##        u'XML type namespace of the object.'
##    TypeNamespaceURI = property(_get, _set, doc = _set.__doc__)
##
##    def AddBoolean(self, Name, Value):
##        u'Adds element value as a boolean.'
##        #return 
##
##    def GetBoolean(self, index):
##        u'Obtains element value as a boolean.'
##        #return Value
##
##    def AddDouble(self, Name, Value):
##        u'Adds element value as a double.'
##        #return 
##
##    def GetFlag(self, Name):
##        u'Obtains the value for a serialization flag.'
##        #return FlagValue
##
##    def GetString(self, index):
##        u'Obtains element value as a string.'
##        #return Value
##
##    def GetObject(self, index, typeNamespace, TypeName):
##        u'Obtains element value as an object instance.'
##        #return Value
##
##    def _get(self):
##        u'XML type of the object.'
##        #return Name
##    def _set(self, Name):
##        u'XML type of the object.'
##    TypeName = property(_get, _set, doc = _set.__doc__)
##
##    def GetVariant(self, index):
##        u'Obtains element value as a variant.'
##        #return Value
##
##    def AddShort(self, Name, Value):
##        u'Adds element value as a short.'
##        #return 
##
##    def GetBinary(self, index):
##        u'Obtains element value as an array of bytes.'
##        #return Value
##
##    def AddInteger(self, Name, Value):
##        u'Adds element value as an integer.'
##        #return 
##
##    def Properties(self, props):
##        u'Properties for serialization and deserialization.'
##        #return 
##
##    @property
##    def Count(self):
##        u'Number of XML elements.'
##        #return Count
##
##    def AddBinary(self, Name, Value):
##        u'Adds element value as an array of bytes.'
##        #return 
##
##    def SetFlag(self, Name, FlagValue):
##        u'Writes the value for a serialization flag.'
##        #return 
##
##    def AddString(self, Name, Value):
##        u'Adds element value as a string.'
##        #return 
##
##    def GetShort(self, index):
##        u'Obtains element value as a short.'
##        #return Value
##
##    def GetDate(self, index):
##        u'Obtains element value as a date.'
##        #return Value
##
##    def AddObject(self, Name, Value):
##        u'Adds element value as an object.'
##        #return 
##
##    def GetByte(self, index):
##        u'Obtains element value as a byte.'
##        #return Value
##
##    def AddFloat(self, Name, Value):
##        u'Adds element value as a float.'
##        #return 
##
##    def AddByte(self, Name, Value):
##        u'Adds element value as a byte.'
##        #return 
##
##    def Find(self, Name):
##        u'Finds an XML element by name.'
##        #return index
##

class IClassID(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods identifying class ID.'
    _iid_ = GUID('{9F9650F1-5F49-4041-BA0F-D10BAFF1D7BC}')
    _idlflags_ = []
IClassID._methods_ = [
    COMMETHOD([helpstring(u'Identify class ID for an object.')], HRESULT, 'GetCLSID',
              ( ['retval', 'out'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pCLSID' )),
    COMMETHOD([helpstring(u'Identify ProgID for an object.')], HRESULT, 'GetProgID',
              ( ['retval', 'out'], POINTER(BSTR), 'pProgID' )),
]
################################################################
## code template for IClassID implementation
##class IClassID_Impl(object):
##    def GetProgID(self):
##        u'Identify ProgID for an object.'
##        #return pProgID
##
##    def GetCLSID(self):
##        u'Identify class ID for an object.'
##        #return pCLSID
##

_WKSTimeDuration._fields_ = [
    ('Positive', VARIANT_BOOL),
    ('Days', c_int),
    ('Hours', c_int),
    ('Minutes', c_int),
    ('Seconds', c_int),
    ('Nanoseconds', c_int),
]
assert sizeof(_WKSTimeDuration) == 24, sizeof(_WKSTimeDuration)
assert alignment(_WKSTimeDuration) == 4, alignment(_WKSTimeDuration)
class NameFactory(CoClass):
    u'Name Object Factory.'
    _reg_clsid_ = GUID('{DB1ECCC0-C6C6-11D2-9F24-00C04F6BC69E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class INameFactory(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that work with the Name factory.'
    _iid_ = GUID('{51AD0A33-C607-11D2-9F23-00C04F6BC69E}')
    _idlflags_ = ['oleautomation']
NameFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, INameFactory]

class _WKSPoint(Structure):
    pass
WKSPoint = _WKSPoint
class IJobResults(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to properties of job results.'
    _iid_ = GUID('{4D919E2D-F6C1-47BA-BA1F-6F2C29A86E22}')
    _idlflags_ = ['oleautomation']
IJobResults._methods_ = [
    COMMETHOD(['propget', helpstring(u'Format of job results.')], HRESULT, 'ResultsFormat',
              ( ['retval', 'out'], POINTER(esriAGSInternetMessageFormat), 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Job results in SOAP format.')], HRESULT, 'StringResults',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Job results in SOAP format.')], HRESULT, 'StringResults',
              ( ['in'], BSTR, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Job results in binary format.')], HRESULT, 'BinaryResults',
              ( ['retval', 'out'], POINTER(_midlSAFEARRAY(c_ubyte)), 'ppVal' )),
    COMMETHOD(['propput', helpstring(u'Job results in binary format.')], HRESULT, 'BinaryResults',
              ( ['in'], _midlSAFEARRAY(c_ubyte), 'ppVal' )),
    COMMETHOD(['propget', helpstring(u'REST Format of job results.')], HRESULT, 'IsRESTFormat',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD([helpstring(u'Job results in REST format.')], HRESULT, 'GetRESTResults',
              ( ['out'], POINTER(BSTR), 'pVal' ),
              ( ['out'], POINTER(_midlSAFEARRAY(c_ubyte)), 'ppVal' )),
    COMMETHOD([helpstring(u'Job results in REST format.')], HRESULT, 'SetRESTResults',
              ( ['in'], BSTR, 'Val' ),
              ( ['in'], _midlSAFEARRAY(c_ubyte), 'pVal' )),
]
################################################################
## code template for IJobResults implementation
##class IJobResults_Impl(object):
##    @property
##    def ResultsFormat(self):
##        u'Format of job results.'
##        #return pVal
##
##    def SetRESTResults(self, Val, pVal):
##        u'Job results in REST format.'
##        #return 
##
##    def _get(self):
##        u'Job results in SOAP format.'
##        #return pVal
##    def _set(self, pVal):
##        u'Job results in SOAP format.'
##    StringResults = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def IsRESTFormat(self):
##        u'REST Format of job results.'
##        #return pVal
##
##    def _get(self):
##        u'Job results in binary format.'
##        #return ppVal
##    def _set(self, ppVal):
##        u'Job results in binary format.'
##    BinaryResults = property(_get, _set, doc = _set.__doc__)
##
##    def GetRESTResults(self):
##        u'Job results in REST format.'
##        #return pVal, ppVal
##

class IExtensionConfig(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that describe an extension.'
    _iid_ = GUID('{12A4C258-CC9D-4CA7-9F29-79DED88DD45F}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriExtensionState'
esriESEnabled = 1
esriESDisabled = 2
esriESUnavailable = 4
esriExtensionState = c_int # enum
IExtensionConfig._methods_ = [
    COMMETHOD(['propget', helpstring(u'Name of the extension.')], HRESULT, 'ProductName',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'Detailed description of the extension.')], HRESULT, 'Description',
              ( ['retval', 'out'], POINTER(BSTR), 'Description' )),
    COMMETHOD(['propget', helpstring(u'The state of the extension.')], HRESULT, 'State',
              ( ['retval', 'out'], POINTER(esriExtensionState), 'State' )),
    COMMETHOD(['propput', helpstring(u'The state of the extension.')], HRESULT, 'State',
              ( ['in'], esriExtensionState, 'State' )),
]
################################################################
## code template for IExtensionConfig implementation
##class IExtensionConfig_Impl(object):
##    def _get(self):
##        u'The state of the extension.'
##        #return State
##    def _set(self, State):
##        u'The state of the extension.'
##    State = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Description(self):
##        u'Detailed description of the extension.'
##        #return Description
##
##    @property
##    def ProductName(self):
##        u'Name of the extension.'
##        #return Name
##


# values for enumeration 'scriptEngineError'
SCRIPTENGINE_E_CANNOT_COCREATE_VBSCRIPT_CONTROL = -2147219711
SCRIPTENGINE_E_CANNOT_COCREATE_JSCRIPT_CONTROL = -2147219710
scriptEngineError = c_int # enum
class ESRIScriptEngine(CoClass):
    u'An object that creates ESRIScriptEngine instances.'
    _reg_clsid_ = GUID('{8C82D73F-A962-43F7-A377-26557C3143DF}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
ESRIScriptEngine._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IESRIScriptEngine]

class ILocaleInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the locale information.'
    _iid_ = GUID('{53325BDA-65FA-4DE0-901E-2B23FFFB8764}')
    _idlflags_ = ['oleautomation']
ILocaleInfo._methods_ = [
    COMMETHOD(['propget', helpstring(u'Obtains locale unique identifier.')], HRESULT, 'LocaleID',
              ( ['retval', 'out'], POINTER(c_int), 'LocaleID' )),
    COMMETHOD(['propput', helpstring(u'Obtains locale unique identifier.')], HRESULT, 'LocaleID',
              ( ['in'], c_int, 'LocaleID' )),
    COMMETHOD(['propget', helpstring(u'Obtains language identifier.')], HRESULT, 'LanguageID',
              ( ['retval', 'out'], POINTER(c_int), 'LanguageID' )),
    COMMETHOD(['propput', helpstring(u'Obtains language identifier.')], HRESULT, 'LanguageID',
              ( ['in'], c_int, 'LanguageID' )),
    COMMETHOD(['propget', helpstring(u'Obtains country identifier.')], HRESULT, 'CountryID',
              ( ['retval', 'out'], POINTER(c_int), 'CountryID' )),
    COMMETHOD(['propput', helpstring(u'Obtains country identifier.')], HRESULT, 'CountryID',
              ( ['in'], c_int, 'CountryID' )),
    COMMETHOD(['propget', helpstring(u'English name of language.')], HRESULT, 'LanguageName',
              ( ['retval', 'out'], POINTER(BSTR), 'Language' )),
    COMMETHOD(['propput', helpstring(u'English name of language.')], HRESULT, 'LanguageName',
              ( ['in'], BSTR, 'Language' )),
    COMMETHOD(['propget', helpstring(u'English name of country.')], HRESULT, 'CountryName',
              ( ['retval', 'out'], POINTER(BSTR), 'country' )),
    COMMETHOD(['propput', helpstring(u'English name of country.')], HRESULT, 'CountryName',
              ( ['in'], BSTR, 'country' )),
    COMMETHOD(['propget', helpstring(u'English display name of the locale.')], HRESULT, 'DisplayName',
              ( ['retval', 'out'], POINTER(BSTR), 'DisplayName' )),
    COMMETHOD(['propput', helpstring(u'English display name of the locale.')], HRESULT, 'DisplayName',
              ( ['in'], BSTR, 'DisplayName' )),
    COMMETHOD(['propget', helpstring(u'Localized name of language.')], HRESULT, 'LocalizedLanguageName',
              ( ['retval', 'out'], POINTER(BSTR), 'Language' )),
    COMMETHOD(['propput', helpstring(u'Localized name of language.')], HRESULT, 'LocalizedLanguageName',
              ( ['in'], BSTR, 'Language' )),
    COMMETHOD(['propget', helpstring(u'Localized name of country.')], HRESULT, 'LocalizedCountryName',
              ( ['retval', 'out'], POINTER(BSTR), 'country' )),
    COMMETHOD(['propput', helpstring(u'Localized name of country.')], HRESULT, 'LocalizedCountryName',
              ( ['in'], BSTR, 'country' )),
    COMMETHOD(['propget', helpstring(u'Localized display name of the locale.')], HRESULT, 'LocalizedDisplayName',
              ( ['retval', 'out'], POINTER(BSTR), 'DisplayName' )),
    COMMETHOD(['propput', helpstring(u'Localized display name of the locale.')], HRESULT, 'LocalizedDisplayName',
              ( ['in'], BSTR, 'DisplayName' )),
    COMMETHOD(['propget', helpstring(u'Native name of language.')], HRESULT, 'NativeLanguageName',
              ( ['retval', 'out'], POINTER(BSTR), 'Language' )),
    COMMETHOD(['propput', helpstring(u'Native name of language.')], HRESULT, 'NativeLanguageName',
              ( ['in'], BSTR, 'Language' )),
    COMMETHOD(['propget', helpstring(u'Native name of country.')], HRESULT, 'NativeCountryName',
              ( ['retval', 'out'], POINTER(BSTR), 'country' )),
    COMMETHOD(['propput', helpstring(u'Native name of country.')], HRESULT, 'NativeCountryName',
              ( ['in'], BSTR, 'country' )),
]
################################################################
## code template for ILocaleInfo implementation
##class ILocaleInfo_Impl(object):
##    def _get(self):
##        u'English display name of the locale.'
##        #return DisplayName
##    def _set(self, DisplayName):
##        u'English display name of the locale.'
##    DisplayName = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Obtains locale unique identifier.'
##        #return LocaleID
##    def _set(self, LocaleID):
##        u'Obtains locale unique identifier.'
##    LocaleID = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Obtains language identifier.'
##        #return LanguageID
##    def _set(self, LanguageID):
##        u'Obtains language identifier.'
##    LanguageID = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'English name of country.'
##        #return country
##    def _set(self, country):
##        u'English name of country.'
##    CountryName = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Native name of country.'
##        #return country
##    def _set(self, country):
##        u'Native name of country.'
##    NativeCountryName = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Localized name of language.'
##        #return Language
##    def _set(self, Language):
##        u'Localized name of language.'
##    LocalizedLanguageName = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Localized display name of the locale.'
##        #return DisplayName
##    def _set(self, DisplayName):
##        u'Localized display name of the locale.'
##    LocalizedDisplayName = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'English name of language.'
##        #return Language
##    def _set(self, Language):
##        u'English name of language.'
##    LanguageName = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Native name of language.'
##        #return Language
##    def _set(self, Language):
##        u'Native name of language.'
##    NativeLanguageName = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Obtains country identifier.'
##        #return CountryID
##    def _set(self, CountryID):
##        u'Obtains country identifier.'
##    CountryID = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Localized name of country.'
##        #return country
##    def _set(self, country):
##        u'Localized name of country.'
##    LocalizedCountryName = property(_get, _set, doc = _set.__doc__)
##

class IXMLTypeMapper(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that convert to and from XML to native types.'
    _iid_ = GUID('{A9A5DE92-E3C9-4940-B0F4-6D93CDF2602B}')
    _idlflags_ = ['oleautomation']
class IXMLTypeMapper2(IXMLTypeMapper):
    _case_insensitive_ = True
    u'Provides access to members that convert to and from XML to native types.'
    _iid_ = GUID('{39FDB45D-2B8E-4E07-A24C-55D722BC4BAC}')
    _idlflags_ = ['oleautomation']
IXMLTypeMapper._methods_ = [
    COMMETHOD([helpstring(u'Creates an object based on XML type information.')], HRESULT, 'ToObject',
              ( ['in'], BSTR, 'NamespaceURI' ),
              ( ['in'], BSTR, 'TypeName' ),
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'Value' )),
    COMMETHOD([helpstring(u'Converts an XML integer to a long.')], HRESULT, 'ToInteger',
              ( ['in'], BSTR, 'Text' ),
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([helpstring(u'Converts an XML boolean to a boolean.')], HRESULT, 'ToBoolean',
              ( ['in'], BSTR, 'Text' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([helpstring(u'Converts an XML short to a short.')], HRESULT, 'ToShort',
              ( ['in'], BSTR, 'Text' ),
              ( ['retval', 'out'], POINTER(c_short), 'Value' )),
    COMMETHOD([helpstring(u'Converts an XML byte to a byte.')], HRESULT, 'ToByte',
              ( ['in'], BSTR, 'Text' ),
              ( ['retval', 'out'], POINTER(c_ubyte), 'Value' )),
    COMMETHOD([helpstring(u'Converts an XML float to a float.')], HRESULT, 'ToFloat',
              ( ['in'], BSTR, 'Text' ),
              ( ['retval', 'out'], POINTER(c_float), 'Value' )),
    COMMETHOD([helpstring(u'Converts an XML double to a double.')], HRESULT, 'ToDouble',
              ( ['in'], BSTR, 'Text' ),
              ( ['retval', 'out'], POINTER(c_double), 'Value' )),
    COMMETHOD([helpstring(u'Converts an XML date to a date.')], HRESULT, 'ToDate',
              ( ['in'], BSTR, 'Text' ),
              ( ['retval', 'out'], POINTER(c_double), 'Value' )),
    COMMETHOD([helpstring(u'Converts an XML byte array to a byte array.')], HRESULT, 'ToBinary',
              ( ['in'], BSTR, 'Text' ),
              ( ['retval', 'out'], POINTER(_midlSAFEARRAY(c_ubyte)), 'Value' )),
    COMMETHOD([helpstring(u'Converts a long to an XML integer.')], HRESULT, 'FromInteger',
              ( ['in'], c_int, 'Value' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Text' )),
    COMMETHOD([helpstring(u'Converts a boolean to an XML boolean.')], HRESULT, 'FromBoolean',
              ( ['in'], VARIANT_BOOL, 'Value' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Text' )),
    COMMETHOD([helpstring(u'Converts a short to an XML short.')], HRESULT, 'FromShort',
              ( ['in'], c_short, 'Value' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Text' )),
    COMMETHOD([helpstring(u'Converts a byte to an XML byte.')], HRESULT, 'FromByte',
              ( ['in'], c_ubyte, 'Value' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Text' )),
    COMMETHOD([helpstring(u'Converts a float to an XML float.')], HRESULT, 'FromFloat',
              ( ['in'], c_float, 'Value' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Text' )),
    COMMETHOD([helpstring(u'Converts a double to an XML double.')], HRESULT, 'FromDouble',
              ( ['in'], c_double, 'Value' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Text' )),
    COMMETHOD([helpstring(u'Converts a date to an XML date.')], HRESULT, 'FromDate',
              ( ['in'], c_double, 'Value' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Text' )),
    COMMETHOD([helpstring(u'Converts a byte array to an XML byte array.')], HRESULT, 'FromBinary',
              ( ['in'], POINTER(_midlSAFEARRAY(c_ubyte)), 'Value' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Text' )),
]
################################################################
## code template for IXMLTypeMapper implementation
##class IXMLTypeMapper_Impl(object):
##    def ToDate(self, Text):
##        u'Converts an XML date to a date.'
##        #return Value
##
##    def FromDouble(self, Value):
##        u'Converts a double to an XML double.'
##        #return Text
##
##    def ToByte(self, Text):
##        u'Converts an XML byte to a byte.'
##        #return Value
##
##    def ToShort(self, Text):
##        u'Converts an XML short to a short.'
##        #return Value
##
##    def ToObject(self, NamespaceURI, TypeName):
##        u'Creates an object based on XML type information.'
##        #return Value
##
##    def FromFloat(self, Value):
##        u'Converts a float to an XML float.'
##        #return Text
##
##    def ToFloat(self, Text):
##        u'Converts an XML float to a float.'
##        #return Value
##
##    def FromBinary(self, Value):
##        u'Converts a byte array to an XML byte array.'
##        #return Text
##
##    def FromShort(self, Value):
##        u'Converts a short to an XML short.'
##        #return Text
##
##    def ToBinary(self, Text):
##        u'Converts an XML byte array to a byte array.'
##        #return Value
##
##    def ToDouble(self, Text):
##        u'Converts an XML double to a double.'
##        #return Value
##
##    def FromInteger(self, Value):
##        u'Converts a long to an XML integer.'
##        #return Text
##
##    def FromByte(self, Value):
##        u'Converts a byte to an XML byte.'
##        #return Text
##
##    def ToBoolean(self, Text):
##        u'Converts an XML boolean to a boolean.'
##        #return Value
##
##    def FromDate(self, Value):
##        u'Converts a date to an XML date.'
##        #return Text
##
##    def ToInteger(self, Text):
##        u'Converts an XML integer to a long.'
##        #return Value
##
##    def FromBoolean(self, Value):
##        u'Converts a boolean to an XML boolean.'
##        #return Text
##

IXMLTypeMapper2._methods_ = [
    COMMETHOD([helpstring(u'Converts an int64 to an XML integer.')], HRESULT, 'FromInt64',
              ( ['in'], c_longlong, 'Value' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Text' )),
    COMMETHOD([helpstring(u'Converts an XML integer to an int64.')], HRESULT, 'ToInt64',
              ( ['in'], BSTR, 'Text' ),
              ( ['retval', 'out'], POINTER(c_longlong), 'Value' )),
]
################################################################
## code template for IXMLTypeMapper2 implementation
##class IXMLTypeMapper2_Impl(object):
##    def FromInt64(self, Value):
##        u'Converts an int64 to an XML integer.'
##        #return Text
##
##    def ToInt64(self, Text):
##        u'Converts an XML integer to an int64.'
##        #return Value
##

class IClassifyMinMax(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the classification methods that require only a minimum and maximum value to classify.'
    _iid_ = GUID('{AC6C5899-241B-11D3-9F50-00C04F6BC709}')
    _idlflags_ = ['oleautomation']
IClassifyMinMax._methods_ = [
    COMMETHOD(['propput', helpstring(u'The minimum value.')], HRESULT, 'Minimum',
              ( ['in'], c_double, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'The maximum value.')], HRESULT, 'Maximum',
              ( ['in'], c_double, 'rhs' )),
]
################################################################
## code template for IClassifyMinMax implementation
##class IClassifyMinMax_Impl(object):
##    def _set(self, rhs):
##        u'The minimum value.'
##    Minimum = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'The maximum value.'
##    Maximum = property(fset = _set, doc = _set.__doc__)
##

class IClassifyMinMax2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the classification methods that require a data range only.'
    _iid_ = GUID('{B42E7156-F8A5-415B-ABB4-230CA421F4B2}')
    _idlflags_ = ['oleautomation']
IClassifyMinMax2._methods_ = [
    COMMETHOD([helpstring(u'Classifies a data range defined by a minimum and maximum value into the specified number of classes.')], HRESULT, 'ClassifyMinMax',
              ( ['in'], c_double, 'min' ),
              ( ['in'], c_double, 'max' ),
              ( ['in', 'out'], POINTER(c_int), 'numClasses' )),
]
################################################################
## code template for IClassifyMinMax2 implementation
##class IClassifyMinMax2_Impl(object):
##    def ClassifyMinMax(self, min, max):
##        u'Classifies a data range defined by a minimum and maximum value into the specified number of classes.'
##        #return numClasses
##

class IIntervalRange(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control classifications that need an interval range.'
    _iid_ = GUID('{62144BE6-E05E-11D1-AAAE-00C04FA334B3}')
    _idlflags_ = ['oleautomation']
IIntervalRange._methods_ = [
    COMMETHOD(['propput', helpstring(u'The Interval Range. Call before Classify.')], HRESULT, 'IntervalRange',
              ( ['in'], c_double, 'rhs' )),
    COMMETHOD(['propget', helpstring(u'The Default Range for the data. Data must be added before calling.')], HRESULT, 'Default',
              ( ['retval', 'out'], POINTER(c_double), 'range' )),
]
################################################################
## code template for IIntervalRange implementation
##class IIntervalRange_Impl(object):
##    @property
##    def Default(self):
##        u'The Default Range for the data. Data must be added before calling.'
##        #return range
##
##    def _set(self, rhs):
##        u'The Interval Range. Call before Classify.'
##    IntervalRange = property(fset = _set, doc = _set.__doc__)
##

class IJobMessages(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods that control an array of job messages.'
    _iid_ = GUID('{08125E66-7BF8-4618-87F2-77D9E364F35A}')
    _idlflags_ = ['oleautomation']
class IJobMessage(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to properties of the job message.'
    _iid_ = GUID('{B611D33A-01A3-47E3-AE7D-44076C727ABC}')
    _idlflags_ = ['oleautomation']
IJobMessages._methods_ = [
    COMMETHOD(['propget', helpstring(u'Number of messages.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Method to return job message at given index.')], HRESULT, 'Element',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IJobMessage)), 'ppMsg' )),
    COMMETHOD([helpstring(u'Adds job message to the end of the array.')], HRESULT, 'Add',
              ( ['in'], POINTER(IJobMessage), 'pMsg' )),
    COMMETHOD([helpstring(u'Inserts job message at the given index.')], HRESULT, 'Insert',
              ( ['in'], c_int, 'index' ),
              ( ['in'], POINTER(IJobMessage), 'pMsg' )),
    COMMETHOD([helpstring(u'Removes job message at the given index.')], HRESULT, 'Remove',
              ( ['in'], c_int, 'index' )),
    COMMETHOD([helpstring(u'Removes all job messages from the array.')], HRESULT, 'RemoveAll'),
]
################################################################
## code template for IJobMessages implementation
##class IJobMessages_Impl(object):
##    @property
##    def Count(self):
##        u'Number of messages.'
##        #return Count
##
##    def Insert(self, index, pMsg):
##        u'Inserts job message at the given index.'
##        #return 
##
##    def Remove(self, index):
##        u'Removes job message at the given index.'
##        #return 
##
##    @property
##    def Element(self, index):
##        u'Method to return job message at given index.'
##        #return ppMsg
##
##    def RemoveAll(self):
##        u'Removes all job messages from the array.'
##        #return 
##
##    def Add(self, pMsg):
##        u'Adds job message to the end of the array.'
##        #return 
##

class IIntervalRange2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control classifications that need an interval range.'
    _iid_ = GUID('{29697055-D00B-45AB-91BF-1543D4438086}')
    _idlflags_ = ['oleautomation']
IIntervalRange2._methods_ = [
    COMMETHOD(['propput', helpstring(u'The Interval Range. Call before Classify.')], HRESULT, 'IntervalRange',
              ( ['in'], c_double, 'rhs' )),
    COMMETHOD(['propget', helpstring(u'The Default Range for the data.')], HRESULT, 'Default',
              ( [], VARIANT, 'values' ),
              ( [], VARIANT, 'frequencies' ),
              ( ['retval', 'out'], POINTER(c_double), 'range' )),
]
################################################################
## code template for IIntervalRange2 implementation
##class IIntervalRange2_Impl(object):
##    @property
##    def Default(self, values, frequencies):
##        u'The Default Range for the data.'
##        #return range
##
##    def _set(self, rhs):
##        u'The Interval Range. Call before Classify.'
##    IntervalRange = property(fset = _set, doc = _set.__doc__)
##


# values for enumeration 'esriTimeStringFormat'
esriTSFYearThruSubSecondWithSlash = 0
esriTSFYearThruSecondWithSlash = 1
esriTSFYearThruMinuteWithSlash = 2
esriTSFYearThruHourWithSlash = 3
esriTSFYearThruDayWithSlash = 4
esriTSFYearThruMonthWithSlash = 5
esriTSFYearThruSubSecondWithDash = 6
esriTSFYearThruSecondWithDash = 7
esriTSFYearThruMinuteWithDash = 8
esriTSFYearThruHourWithDash = 9
esriTSFYearThruDayWithDash = 10
esriTSFYearThruMonthWithDash = 11
esriTSFYearThruSubSecond = 12
esriTSFYearThruSecond = 13
esriTSFYearThruMinute = 14
esriTSFYearThruHour = 15
esriTSFYearThruDay = 16
esriTSFYearThruMonth = 17
esriTSFYearOnly = 18
esriTimeStringFormat = c_int # enum
class ByteSwapStreamIO(CoClass):
    u'Helper object that performs byte swapping of data read and written to stream.'
    _reg_clsid_ = GUID('{74D3B3A0-E54F-46D2-B9E8-4167A0B21F87}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class IByteSwapStreamIO(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that support the Byte Swap Helper object.'
    _iid_ = GUID('{E718734D-D494-4E44-92C8-E2212B4A2F8D}')
    _idlflags_ = ['oleautomation']
ByteSwapStreamIO._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IByteSwapStreamIO]

class IDirectionFormat(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that format directions.'
    _iid_ = GUID('{11D7B4C8-DBDF-4B98-AC6D-8C419EFD2C24}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriDirectionUnits'
esriDURadians = 9101
esriDUDecimalDegrees = 2
esriDUDegreesMinutesSeconds = 3
esriDUGradians = 9105
esriDUGons = 9106
esriDirectionUnits = c_int # enum

# values for enumeration 'esriDirectionType'
esriDTNorthAzimuth = 1
esriDTSouthAzimuth = 2
esriDTPolar = 3
esriDTQuadrantBearing = 4
esriDirectionType = c_int # enum

# values for enumeration 'esriDirectionFormatEnum'
esriDFDegreesMinutesSeconds = 0
esriDFQuadrantBearing = 1
esriDirectionFormatEnum = c_int # enum
IDirectionFormat._methods_ = [
    COMMETHOD(['propput', helpstring(u'Indicates Direction Unit for the ValueToString argument.')], HRESULT, 'DirectionUnits',
              ( ['in'], esriDirectionUnits, 'unit' )),
    COMMETHOD(['propget', helpstring(u'Indicates Direction Unit for the ValueToString argument.')], HRESULT, 'DirectionUnits',
              ( ['retval', 'out'], POINTER(esriDirectionUnits), 'unit' )),
    COMMETHOD(['propput', helpstring(u'Indicates the direction of the argument in ValueToString.')], HRESULT, 'DirectionType',
              ( ['in'], esriDirectionType, 'direction' )),
    COMMETHOD(['propget', helpstring(u'Indicates the direction of the argument in ValueToString.')], HRESULT, 'DirectionType',
              ( ['retval', 'out'], POINTER(esriDirectionType), 'direction' )),
    COMMETHOD(['propput', helpstring(u'Indicates how to display the direction value.')], HRESULT, 'DisplayFormat',
              ( ['in'], esriDirectionFormatEnum, 'DirectionFormat' )),
    COMMETHOD(['propget', helpstring(u'Indicates how to display the direction value.')], HRESULT, 'DisplayFormat',
              ( ['retval', 'out'], POINTER(esriDirectionFormatEnum), 'DirectionFormat' )),
    COMMETHOD(['propput', helpstring(u'The number of decimal digits in a seconds part of the formatted number.')], HRESULT, 'DecimalPlaces',
              ( ['in'], c_int, 'num' )),
    COMMETHOD(['propget', helpstring(u'The number of decimal digits in a seconds part of the formatted number.')], HRESULT, 'DecimalPlaces',
              ( ['retval', 'out'], POINTER(c_int), 'num' )),
]
################################################################
## code template for IDirectionFormat implementation
##class IDirectionFormat_Impl(object):
##    def _get(self):
##        u'The number of decimal digits in a seconds part of the formatted number.'
##        #return num
##    def _set(self, num):
##        u'The number of decimal digits in a seconds part of the formatted number.'
##    DecimalPlaces = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates how to display the direction value.'
##        #return DirectionFormat
##    def _set(self, DirectionFormat):
##        u'Indicates how to display the direction value.'
##    DisplayFormat = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates the direction of the argument in ValueToString.'
##        #return direction
##    def _set(self, direction):
##        u'Indicates the direction of the argument in ValueToString.'
##    DirectionType = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates Direction Unit for the ValueToString argument.'
##        #return unit
##    def _set(self, unit):
##        u'Indicates Direction Unit for the ValueToString argument.'
##    DirectionUnits = property(_get, _set, doc = _set.__doc__)
##

class IDeviationInterval(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the classification methods that require a standard deviation based range.'
    _iid_ = GUID('{62144BE7-E05E-11D1-AAAE-00C04FA334B3}')
    _idlflags_ = ['oleautomation']
IDeviationInterval._methods_ = [
    COMMETHOD(['propput', helpstring(u'The deviation interval (1/4 <= value <= 1).')], HRESULT, 'DeviationInterval',
              ( ['in'], c_double, 'Value' )),
    COMMETHOD(['propget', helpstring(u'The deviation interval (1/4 <= value <= 1).')], HRESULT, 'DeviationInterval',
              ( ['retval', 'out'], POINTER(c_double), 'Value' )),
    COMMETHOD(['propput', helpstring(u'The mean value.')], HRESULT, 'Mean',
              ( ['in'], c_double, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'The standard deviation.')], HRESULT, 'StandardDev',
              ( ['in'], c_double, 'rhs' )),
]
################################################################
## code template for IDeviationInterval implementation
##class IDeviationInterval_Impl(object):
##    def _set(self, rhs):
##        u'The standard deviation.'
##    StandardDev = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'The mean value.'
##    Mean = property(fset = _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The deviation interval (1/4 <= value <= 1).'
##        #return Value
##    def _set(self, Value):
##        u'The deviation interval (1/4 <= value <= 1).'
##    DeviationInterval = property(_get, _set, doc = _set.__doc__)
##

class XMLSerializer(CoClass):
    u'An XML serializer and deserializer of objects.'
    _reg_clsid_ = GUID('{4FE5C28E-35E6-403F-8431-E16B1F99AE4E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class IXMLSerializer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the XML serialization and deserialization of objects.'
    _iid_ = GUID('{DEA199D0-371C-4955-844C-B67705E1EDB2}')
    _idlflags_ = ['oleautomation']
class ISupportErrorInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{DF0B3D60-548F-101B-8E65-08002B2BD119}')
    _idlflags_ = []
XMLSerializer._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IXMLSerializer, ISupportErrorInfo]

class Library(object):
    u'Esri System Object Library 10.2'
    name = u'esriSystem'
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)

class XMLFlags(CoClass):
    u'A collection of XML flags.'
    _reg_clsid_ = GUID('{23D488E6-6C77-47E8-948B-CCEEE3589CA2}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class IXMLFlags(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control XML flags.'
    _iid_ = GUID('{647F4C09-3699-4868-A74C-108122A968DC}')
    _idlflags_ = ['oleautomation']
XMLFlags._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IXMLFlags]

class IESRILicenseInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that check software licenses.'
    _iid_ = GUID('{FCF1E388-5C7E-4BF3-AF4B-155D93F8297F}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriProductCode'
esriProductCodeReader = 90
esriProductCodeReaderPro = 91
esriProductCodeBasic = 100
esriProductCodeStandard = 200
esriProductCodeAdvanced = 300
esriProductCodeArcPress = 4
esriProductCodeTIFFLZW = 5
esriProductCodeGeoStats = 6
esriProductCodeMrSID = 7
esriProductCodeNetwork = 8
esriProductCodeTIN = 9
esriProductCodeGrid = 10
esriProductCodeStreetMap = 12
esriProductCodeCOGO = 13
esriProductCodeMLE = 14
esriProductCodePublisher = 15
esriProductCodeAllEurope = 16
esriProductCodeAustria = 17
esriProductCodeBelgium = 18
esriProductCodeDenmark = 19
esriProductCodeFrance = 20
esriProductCodeGermany = 21
esriProductCodeItaly = 22
esriProductCodeLuxembourg = 23
esriProductCodeNetherlands = 24
esriProductCodePortugal = 25
esriProductCodeSpain = 26
esriProductCodeSweden = 27
esriProductCodeSwitzerland = 28
esriProductCodeUnitedKingdom = 29
esriProductPostCodesMajorRoads = 30
esriProductCodeArcMapServer = 31
esriProductCodeTracking = 32
esriProductCodeBusinessStandard = 33
esriProductCodeArcScan = 34
esriProductCodeBusiness = 35
esriProductCodeSchematics = 36
esriProductCodeSchematicsSDK = 37
esriProductCodeVirtualEarthEng = 38
esriProductCodeVBAExtension = 39
esriProductCodeWorkflowManager = 40
esriProductCodeDesigner = 43
esriProductCodeVector = 44
esriProductCodeDataInteroperability = 45
esriProductCodeProductionMapping = 46
esriProductCodeDataReViewer = 47
esriProductCodeMPSAtlas = 48
esriProductCodeDefense = 49
esriProductCodeNautical = 50
esriProductCodeIntelAgency = 51
esriProductCodeMappingAgency = 52
esriProductCodeAeronautical = 53
esriProductCodeVirtualEarth = 54
esriProductCodeServerStandardEdition = 55
esriProductCodeServerAdvancedEdition = 56
esriProductCodeServerEnterprise = 57
esriProductCodeImageExt = 58
esriProductCodeBingMaps = 59
esriProductCodeBingMapsEng = 60
esriProductCodeDefenseUS = 61
esriProductCodeDefenseINTL = 62
esriProductCodeAGINSPIRE = 63
esriProductCodeRuntimeBasic = 64
esriProductCodeRuntimeStandard = 65
esriProductCodeRuntimeAdvanced = 66
esriProductCodeHighways = 67
esriProductCodeVideo = 68
esriProductCodeBathymetry = 69
esriProductCodeAirports = 70
esriProductCode = c_int # enum
IESRILicenseInfo._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates the product code that will be used on the current machine.')], HRESULT, 'DefaultProduct',
              ( ['retval', 'out'], POINTER(esriProductCode), 'ProductCode' )),
    COMMETHOD([helpstring(u'Indicates if the specified product is licensed.')], HRESULT, 'IsLicensed',
              ( ['in'], esriProductCode, 'ProductCode' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'licensed' )),
]
################################################################
## code template for IESRILicenseInfo implementation
##class IESRILicenseInfo_Impl(object):
##    @property
##    def DefaultProduct(self):
##        u'Indicates the product code that will be used on the current machine.'
##        #return ProductCode
##
##    def IsLicensed(self, ProductCode):
##        u'Indicates if the specified product is licensed.'
##        #return licensed
##

class XMLSerializerAlt(CoClass):
    u'XML serializer of objects.'
    _reg_clsid_ = GUID('{364EEF73-3C3C-493C-B99A-76DBE62F6FC6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class IXMLSerializerAlt(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to load an object from an XML string.'
    _iid_ = GUID('{4DEB2C9D-2162-4443-908E-25B6CB7FB6DF}')
    _idlflags_ = ['oleautomation']
XMLSerializerAlt._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IXMLSerializerAlt, ISupportErrorInfo]

class JSONObject(CoClass):
    u'Simplified JSON API coclass'
    _reg_clsid_ = GUID('{DB25E387-8D9F-4D79-B1DF-8F65694465F0}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class IJSONObject(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides simplified DOM-like JSON serialization and de-serialization API.'
    _iid_ = GUID('{EEA70515-FA6B-4DEE-AB79-D7935BF3A838}')
    _idlflags_ = ['oleautomation']
JSONObject._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IJSONObject, ISupportErrorInfo]

class IJSONWriter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the sequential writing of JSON.'
    _iid_ = GUID('{408CD30C-B7A6-4793-A07C-4181035C66E7}')
    _idlflags_ = ['oleautomation']
IJSONWriter._methods_ = [
    COMMETHOD([helpstring(u'Specifies output JSON stream.')], HRESULT, 'WriteTo',
              ( ['in'], POINTER(IStream), 'outputStream' )),
    COMMETHOD([helpstring(u'Redirects writing to internal string buffer.')], HRESULT, 'WriteToString'),
    COMMETHOD([helpstring(u'Obtains copy of string buffer. Encoding is UTF8.')], HRESULT, 'GetStringBuffer',
              ( ['retval', 'out'], POINTER(_midlSAFEARRAY(c_ubyte)), 'buf' )),
    COMMETHOD(['propget', helpstring(u'Obtains underlying stream. If WriteTo() is not called yet, will return NULL. Also will return NULL if WriteToString() was called.')], HRESULT, 'Stream',
              ( ['retval', 'out'], POINTER(POINTER(IStream)), 'ppStream' )),
    COMMETHOD([helpstring(u"Writes 'pretty' formatting on or off.")], HRESULT, 'SetFormatted',
              ( [], VARIANT_BOOL, 'Value' )),
    COMMETHOD([helpstring(u"Writes indent for 'pretty' formatting. Default is 2.")], HRESULT, 'SetIndent',
              ( [], c_int, 'Value' )),
    COMMETHOD([helpstring(u'Starts writing an object.')], HRESULT, 'StartObject',
              ( [], BSTR, 'Name' )),
    COMMETHOD([helpstring(u'Ends writing of an object.')], HRESULT, 'EndObject'),
    COMMETHOD([helpstring(u'Starts an array.')], HRESULT, 'StartArray',
              ( [], BSTR, 'Name' )),
    COMMETHOD([helpstring(u'Ends an array.')], HRESULT, 'EndArray'),
    COMMETHOD([helpstring(u'Writes a variant valued property.')], HRESULT, 'WriteVariant',
              ( [], BSTR, 'Name' ),
              ( [], VARIANT, 'Value' )),
    COMMETHOD([helpstring(u'Writes a string property.')], HRESULT, 'WriteString',
              ( [], BSTR, 'Name' ),
              ( [], BSTR, 'Value' )),
    COMMETHOD([helpstring(u'Writes a boolean.')], HRESULT, 'WriteBoolean',
              ( [], BSTR, 'Name' ),
              ( [], VARIANT_BOOL, 'Value' )),
    COMMETHOD([helpstring(u'Writes a byte.')], HRESULT, 'WriteByte',
              ( [], BSTR, 'Name' ),
              ( [], c_ubyte, 'Value' )),
    COMMETHOD([helpstring(u'Writes a short.')], HRESULT, 'WriteShort',
              ( [], BSTR, 'Name' ),
              ( [], c_short, 'Value' )),
    COMMETHOD([helpstring(u'Writes an integer.')], HRESULT, 'WriteInteger',
              ( [], BSTR, 'Name' ),
              ( [], c_int, 'Value' )),
    COMMETHOD([helpstring(u'Writes a float.')], HRESULT, 'WriteFloat',
              ( [], BSTR, 'Name' ),
              ( [], c_float, 'Value' )),
    COMMETHOD([helpstring(u'Writes a double.')], HRESULT, 'WriteDouble',
              ( [], BSTR, 'Name' ),
              ( [], c_double, 'Value' )),
    COMMETHOD([helpstring(u'Writes a date.')], HRESULT, 'WriteDate',
              ( [], BSTR, 'Name' ),
              ( [], c_double, 'Value' ),
              ( [], VARIANT_BOOL, 'asString' )),
    COMMETHOD([helpstring(u'Writes a byte array.')], HRESULT, 'WriteBinary',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], POINTER(_midlSAFEARRAY(c_ubyte)), 'Value' )),
    COMMETHOD([helpstring(u'Writes null property.')], HRESULT, 'WriteNull',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD([helpstring(u'Writes a variant in array.')], HRESULT, 'WriteVariantVal',
              ( [], VARIANT, 'Value' )),
    COMMETHOD([helpstring(u'Writes a string in array.')], HRESULT, 'WriteStringVal',
              ( [], BSTR, 'Value' )),
    COMMETHOD([helpstring(u'Writes a boolean in array.')], HRESULT, 'WriteBooleanVal',
              ( [], VARIANT_BOOL, 'Value' )),
    COMMETHOD([helpstring(u'Writes a byte in array.')], HRESULT, 'WriteByteVal',
              ( [], c_ubyte, 'Value' )),
    COMMETHOD([helpstring(u'Writes a short int in array.')], HRESULT, 'WriteShortVal',
              ( [], c_short, 'Value' )),
    COMMETHOD([helpstring(u'Writes an integer in array.')], HRESULT, 'WriteIntegerVal',
              ( [], c_int, 'Value' )),
    COMMETHOD([helpstring(u'Writes a float in array.')], HRESULT, 'WriteFloatVal',
              ( [], c_float, 'Value' )),
    COMMETHOD([helpstring(u'Writes a double in array.')], HRESULT, 'WriteDoubleVal',
              ( [], c_double, 'Value' )),
    COMMETHOD([helpstring(u'Writes a date in array.')], HRESULT, 'WriteDateVal',
              ( [], c_double, 'Value' ),
              ( [], VARIANT_BOOL, 'asString' )),
    COMMETHOD([helpstring(u'Writes a byte array.')], HRESULT, 'WriteBinaryVal',
              ( ['in'], POINTER(_midlSAFEARRAY(c_ubyte)), 'Value' )),
    COMMETHOD([helpstring(u'Writes null value in array.')], HRESULT, 'WriteNullVal'),
]
################################################################
## code template for IJSONWriter implementation
##class IJSONWriter_Impl(object):
##    def WriteFloatVal(self, Value):
##        u'Writes a float in array.'
##        #return 
##
##    def WriteIntegerVal(self, Value):
##        u'Writes an integer in array.'
##        #return 
##
##    def WriteNullVal(self):
##        u'Writes null value in array.'
##        #return 
##
##    def WriteVariantVal(self, Value):
##        u'Writes a variant in array.'
##        #return 
##
##    def WriteDate(self, Name, Value, asString):
##        u'Writes a date.'
##        #return 
##
##    def WriteString(self, Name, Value):
##        u'Writes a string property.'
##        #return 
##
##    def WriteShort(self, Name, Value):
##        u'Writes a short.'
##        #return 
##
##    def SetFormatted(self, Value):
##        u"Writes 'pretty' formatting on or off."
##        #return 
##
##    def WriteTo(self, outputStream):
##        u'Specifies output JSON stream.'
##        #return 
##
##    def WriteNull(self, Name):
##        u'Writes null property.'
##        #return 
##
##    def WriteByteVal(self, Value):
##        u'Writes a byte in array.'
##        #return 
##
##    def StartObject(self, Name):
##        u'Starts writing an object.'
##        #return 
##
##    def EndArray(self):
##        u'Ends an array.'
##        #return 
##
##    def WriteToString(self):
##        u'Redirects writing to internal string buffer.'
##        #return 
##
##    def WriteDouble(self, Name, Value):
##        u'Writes a double.'
##        #return 
##
##    def WriteDateVal(self, Value, asString):
##        u'Writes a date in array.'
##        #return 
##
##    def WriteFloat(self, Name, Value):
##        u'Writes a float.'
##        #return 
##
##    def WriteBinaryVal(self, Value):
##        u'Writes a byte array.'
##        #return 
##
##    def WriteShortVal(self, Value):
##        u'Writes a short int in array.'
##        #return 
##
##    def WriteVariant(self, Name, Value):
##        u'Writes a variant valued property.'
##        #return 
##
##    def GetStringBuffer(self):
##        u'Obtains copy of string buffer. Encoding is UTF8.'
##        #return buf
##
##    def WriteBoolean(self, Name, Value):
##        u'Writes a boolean.'
##        #return 
##
##    def WriteDoubleVal(self, Value):
##        u'Writes a double in array.'
##        #return 
##
##    @property
##    def Stream(self):
##        u'Obtains underlying stream. If WriteTo() is not called yet, will return NULL. Also will return NULL if WriteToString() was called.'
##        #return ppStream
##
##    def SetIndent(self, Value):
##        u"Writes indent for 'pretty' formatting. Default is 2."
##        #return 
##
##    def WriteStringVal(self, Value):
##        u'Writes a string in array.'
##        #return 
##
##    def StartArray(self, Name):
##        u'Starts an array.'
##        #return 
##
##    def WriteBooleanVal(self, Value):
##        u'Writes a boolean in array.'
##        #return 
##
##    def WriteByte(self, Name, Value):
##        u'Writes a byte.'
##        #return 
##
##    def EndObject(self):
##        u'Ends writing of an object.'
##        #return 
##
##    def WriteInteger(self, Name, Value):
##        u'Writes an integer.'
##        #return 
##
##    def WriteBinary(self, Name, Value):
##        u'Writes a byte array.'
##        #return 
##


# values for enumeration 'esriTimeLocaleFormat'
esriTLFDefaultDateTime = 0
esriTLFLongDate = 1
esriTLFShortDate = 2
esriTLFLongTime = 3
esriTLFShortTime = 4
esriTimeLocaleFormat = c_int # enum
class ILicenseInformation(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to retrieve the name for license product code.'
    _iid_ = GUID('{EBE6BD5B-2F03-48F0-B68B-6DE8C4BDEF32}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriLicenseProductCode'
esriLicenseProductCodeEngine = 10
esriLicenseProductCodeEngineGeoDB = 20
esriLicenseProductCodeArcServer = 30
esriLicenseProductCodeBasic = 40
esriLicenseProductCodeStandard = 50
esriLicenseProductCodeAdvanced = 60
esriLicenseProductCode = c_int # enum

# values for enumeration 'esriLicenseExtensionCode'
esriLicenseExtensionCodeArcPress = 4
esriLicenseExtensionCodeTIFFLZW = 5
esriLicenseExtensionCodeGeoStats = 6
esriLicenseExtensionCodeMrSID = 7
esriLicenseExtensionCodeNetwork = 8
esriLicenseExtensionCode3DAnalyst = 9
esriLicenseExtensionCodeSpatialAnalyst = 10
esriLicenseExtensionCodeStreetMap = 12
esriLicenseExtensionCodeCOGO = 13
esriLicenseExtensionCodeMLE = 14
esriLicenseExtensionCodePublisher = 15
esriLicenseExtensionCodeArcMapServer = 31
esriLicenseExtensionCodeTracking = 32
esriLicenseExtensionCodeBusinessStandard = 33
esriLicenseExtensionCodeArcScan = 34
esriLicenseExtensionCodeBusiness = 35
esriLicenseExtensionCodeSchematics = 36
esriLicenseExtensionCodeSchematicsSDK = 37
esriLicenseExtensionCodeVirtualEarthEng = 38
esriLicenseExtensionCodeVBAExtension = 39
esriLicenseExtensionCodeWorkflowManager = 40
esriLicenseExtensionCodeDesigner = 43
esriLicenseExtensionCodeVector = 44
esriLicenseExtensionCodeDataInteroperability = 45
esriLicenseExtensionCodeProductionMapping = 46
esriLicenseExtensionCodeDataReViewer = 47
esriLicenseExtensionCodeMPSAtlas = 48
esriLicenseExtensionCodeDefense = 49
esriLicenseExtensionCodeNautical = 50
esriLicenseExtensionCodeIntelAgency = 51
esriLicenseExtensionCodeMappingAgency = 52
esriLicenseExtensionCodeAeronautical = 53
esriLicenseExtensionCodeVirtualEarth = 54
esriLicenseExtensionCodeServerStandardEdition = 55
esriLicenseExtensionCodeServerAdvancedEdition = 56
esriLicenseExtensionCodeServerEnterprise = 57
esriLicenseExtensionCodeImageExt = 58
esriLicenseExtensionCodeBingMaps = 59
esriLicenseExtensionCodeBingMapsEng = 60
esriLicenseExtensionCodeDefenseUS = 61
esriLicenseExtensionCodeDefenseINTL = 62
esriLicenseExtensionCodeAGINSPIRE = 63
esriLicenseExtensionCodeRuntimeBasic = 64
esriLicenseExtensionCodeRuntimeStandard = 65
esriLicenseExtensionCodeRuntimeAdvanced = 66
esriLicenseExtensionCodeHighways = 67
esriLicenseExtensionCodeVideo = 68
esriLicenseExtensionCodeBathymetry = 69
esriLicenseExtensionCodeAirports = 70
esriLicenseExtensionCode = c_int # enum
class ILicenseInfoEnum(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to retrieve the extension code.'
    _iid_ = GUID('{A681B61D-D891-474C-9E45-9B24C6677DB6}')
    _idlflags_ = ['oleautomation']
ILicenseInformation._methods_ = [
    COMMETHOD([helpstring(u'Retrieve the name license product code.')], HRESULT, 'GetLicenseProductName',
              ( ['in'], esriLicenseProductCode, 'ProductCode' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ProductName' )),
    COMMETHOD([helpstring(u'Retrieve the name license extension code.')], HRESULT, 'GetLicenseExtensionName',
              ( ['in'], esriLicenseExtensionCode, 'extensionCode' ),
              ( ['retval', 'out'], POINTER(BSTR), 'extensionName' )),
    COMMETHOD([helpstring(u'Enumerate the extensions supported the product.')], HRESULT, 'GetProductExtensions',
              ( ['in'], esriLicenseProductCode, 'ProductCode' ),
              ( ['retval', 'out'], POINTER(POINTER(ILicenseInfoEnum)), 'extensionName' )),
]
################################################################
## code template for ILicenseInformation implementation
##class ILicenseInformation_Impl(object):
##    def GetLicenseProductName(self, ProductCode):
##        u'Retrieve the name license product code.'
##        #return ProductName
##
##    def GetProductExtensions(self, ProductCode):
##        u'Enumerate the extensions supported the product.'
##        #return extensionName
##
##    def GetLicenseExtensionName(self, extensionCode):
##        u'Retrieve the name license extension code.'
##        #return extensionName
##

class IParseNameString(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that parse Name strings.'
    _iid_ = GUID('{DB1ECCBF-C6C6-11D2-9F24-00C04F6BC69E}')
    _idlflags_ = ['oleautomation']
class IName(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that work with Name objects.'
    _iid_ = GUID('{4BA33331-D55F-11D1-8882-0000F877762D}')
    _idlflags_ = ['oleautomation']
IParseNameString._methods_ = [
    COMMETHOD([helpstring(u'Indicates if the given name string can be parsed by this parser.')], HRESULT, 'CanParse',
              ( ['in'], BSTR, 'NameString' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'CanParse' )),
    COMMETHOD([helpstring(u'Parses the name string and returns a new Name object.')], HRESULT, 'Parse',
              ( ['in'], BSTR, 'NameString' ),
              ( ['retval', 'out'], POINTER(POINTER(IName)), 'Name' )),
]
################################################################
## code template for IParseNameString implementation
##class IParseNameString_Impl(object):
##    def Parse(self, NameString):
##        u'Parses the name string and returns a new Name object.'
##        #return Name
##
##    def CanParse(self, NameString):
##        u'Indicates if the given name string can be parsed by this parser.'
##        #return CanParse
##

class IVariantStream(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that store values to and retrieve values from a stream.'
    _iid_ = GUID('{67A4D650-69E0-11D2-8500-0000F875B9C6}')
    _idlflags_ = ['oleautomation']
IVariantStream._methods_ = [
    COMMETHOD([helpstring(u'Reads a value from a stream.')], HRESULT, 'Read',
              ( ['retval', 'out'], POINTER(VARIANT), 'Value' )),
    COMMETHOD([helpstring(u'Writes a value to a stream.')], HRESULT, 'Write',
              ( ['in'], VARIANT, 'Value' )),
]
################################################################
## code template for IVariantStream implementation
##class IVariantStream_Impl(object):
##    def Read(self):
##        u'Reads a value from a stream.'
##        #return Value
##
##    def Write(self, Value):
##        u'Writes a value to a stream.'
##        #return 
##

class IJSONWriter2(IJSONWriter):
    _case_insensitive_ = True
    _iid_ = GUID('{677FCBB1-C272-4616-B476-2CA3DCE8D292}')
    _idlflags_ = ['oleautomation']
IJSONWriter2._methods_ = [
    COMMETHOD([helpstring(u"Resets IJSONWriter's internal state.")], HRESULT, 'Reset'),
    COMMETHOD([helpstring(u'Writes a raw property without any processing. Use to insert JSON sub-object or sub-array strings only.')], HRESULT, 'WriteRawString',
              ( [], BSTR, 'Name' ),
              ( [], BSTR, 'Value' )),
    COMMETHOD([helpstring(u'Writes a raw value without any processing. Use to insert JSON sub-object or sub-array strings only.')], HRESULT, 'WriteRawStringVal',
              ( [], BSTR, 'Value' )),
    COMMETHOD([helpstring(u'Writes a double in array with specified number of digits after decimal point.')], HRESULT, 'WriteDoubleValEx',
              ( [], c_double, 'Value' ),
              ( [], c_int, 'precision' )),
    COMMETHOD([helpstring(u'Writes a double with specified number of digits after decimal point.')], HRESULT, 'WriteDoubleEx',
              ( [], BSTR, 'Name' ),
              ( [], c_double, 'Value' ),
              ( [], c_int, 'precision' )),
]
################################################################
## code template for IJSONWriter2 implementation
##class IJSONWriter2_Impl(object):
##    def Reset(self):
##        u"Resets IJSONWriter's internal state."
##        #return 
##
##    def WriteRawString(self, Name, Value):
##        u'Writes a raw property without any processing. Use to insert JSON sub-object or sub-array strings only.'
##        #return 
##
##    def WriteRawStringVal(self, Value):
##        u'Writes a raw value without any processing. Use to insert JSON sub-object or sub-array strings only.'
##        #return 
##
##    def WriteDoubleValEx(self, Value, precision):
##        u'Writes a double in array with specified number of digits after decimal point.'
##        #return 
##
##    def WriteDoubleEx(self, Name, Value, precision):
##        u'Writes a double with specified number of digits after decimal point.'
##        #return 
##

class IVariantStreamIO(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that support the VariantStream Helper object.'
    _iid_ = GUID('{76BE2722-B1F7-4FE4-B358-BFD2198CDA62}')
    _idlflags_ = ['oleautomation']
IVariantStreamIO._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The stream to perform variant stream reads and writes to.')], HRESULT, 'Stream',
              ( ['in'], POINTER(IStream), 'rhs' )),
]
################################################################
## code template for IVariantStreamIO implementation
##class IVariantStreamIO_Impl(object):
##    def Stream(self, rhs):
##        u'The stream to perform variant stream reads and writes to.'
##        #return 
##


# values for enumeration 'esriDrawPhase'
esriDPGeography = 1
esriDPAnnotation = 2
esriDPSelection = 4
esriDrawPhase = c_int # enum
class IDocumentVersionSupportGEN(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to extend the IObjectStream interface with methods to hande saving objects that did not exist in previous versions of the software.'
    _iid_ = GUID('{BB75DA81-8DFE-4122-A9C2-86F07C539AD5}')
    _idlflags_ = ['oleautomation']
IDocumentVersionSupportGEN._methods_ = [
    COMMETHOD([helpstring(u'Is this object valid at the given document version.')], HRESULT, 'IsSupportedAtVersion',
              ( ['in'], esriArcGISVersion, 'docVersion' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'supported' )),
    COMMETHOD([helpstring(u'Convert the object to another object that is supported.')], HRESULT, 'ConvertToSupportedObject',
              ( ['in'], esriArcGISVersion, 'docVersion' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'convertedObject' )),
]
################################################################
## code template for IDocumentVersionSupportGEN implementation
##class IDocumentVersionSupportGEN_Impl(object):
##    def IsSupportedAtVersion(self, docVersion):
##        u'Is this object valid at the given document version.'
##        #return supported
##
##    def ConvertToSupportedObject(self, docVersion):
##        u'Convert the object to another object that is supported.'
##        #return convertedObject
##

class IJSONReader(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to Sequential JSON Reader.'
    _iid_ = GUID('{48105A80-E0DC-4D69-BB61-3DF74CAFA52C}')
    _idlflags_ = ['oleautomation']
class IJSONReader2(IJSONReader):
    _case_insensitive_ = True
    _iid_ = GUID('{2C573605-C449-47E3-A483-F441192840FA}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'JSONTokenType'
JSONUndefined = -1
JSONString = 1
JSONNumber = 2
JSONBoolean = 3
JSONNull = 4
JSONStartOfObject = 5
JSONEndOfObject = 6
JSONStartOfArray = 7
JSONEndOfArray = 8
JSONPropertyValueDelimiter = 9
JSONValueDelimiter = 10
JSONTokenType = c_int # enum
class IStringArray(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control string arrays.'
    _iid_ = GUID('{206216C9-7253-4A4D-92DD-60329FD9D792}')
    _idlflags_ = ['oleautomation']
IJSONReader._methods_ = [
    COMMETHOD([helpstring(u'Specifies input stream.')], HRESULT, 'ReadFrom',
              ( ['in'], POINTER(IStream), 'inputStream' )),
    COMMETHOD([helpstring(u'Specifies input as string.')], HRESULT, 'ReadFromString',
              ( ['in'], BSTR, 'Text' )),
    COMMETHOD(['propget', helpstring(u'Obtains underlying stream.')], HRESULT, 'Stream',
              ( ['retval', 'out'], POINTER(POINTER(IStream)), 'ppStream' )),
    COMMETHOD([helpstring(u'Reads next JSON token.')], HRESULT, 'Read'),
    COMMETHOD(['propget', helpstring(u'Obtains type of current token.')], HRESULT, 'CurrentTokenType',
              ( ['retval', 'out'], POINTER(JSONTokenType), 'pVal' )),
    COMMETHOD([helpstring(u"Indicates true if current token is '{'.")], HRESULT, 'IsStartOfObject',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD([helpstring(u"Indicates true if current token is '}'.")], HRESULT, 'IsEndOfObject',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD([helpstring(u"Indicates true if current token is '['.")], HRESULT, 'IsStartOfArray',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD([helpstring(u"Indicates true if current token is ']'.")], HRESULT, 'IsEndOfArray',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD([helpstring(u'Indicates true if current token is a property value or array value of type string.')], HRESULT, 'IsString',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD([helpstring(u'Indicates true if current token is a property value or array value of numeric type.')], HRESULT, 'IsNumber',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD([helpstring(u'Indicates true if current token is a property value or array value of boolean type.')], HRESULT, 'IsBoolean',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD([helpstring(u'Indicates true if current token is a property value or array value and equals to null.')], HRESULT, 'IsNull',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD([helpstring(u'Obtains array or property value as Variant. Advances to the next token.')], HRESULT, 'ReadValue',
              ( ['retval', 'out'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD([helpstring(u'Obtains property name. Advances to the next token.')], HRESULT, 'ReadPropertyName',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([helpstring(u'Obtains property or array value as string. Advances to the next token. If property value cannot be coerced to string, returns E_FAIL.')], HRESULT, 'ReadValueAsString',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([helpstring(u'Obtains property or array value as number. Advances to the next token. If property value cannot be coerced to long, returns E_FAIL.')], HRESULT, 'ReadValueAsLong',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD([helpstring(u'Obtains property or array value as number. Advances to the next token. If property value cannot be coerced to double, returns E_FAIL.')], HRESULT, 'ReadValueAsDouble',
              ( ['retval', 'out'], POINTER(c_double), 'pVal' )),
    COMMETHOD([helpstring(u'Obtains array or property value as boolean. Advances to the next token. If property value cannot be coerced to boolean, returns E_FAIL.')], HRESULT, 'ReadValueAsBoolean',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD([helpstring(u'Obtains property or array value as date. Advances to the next token. If property value cannot be coerced to datetime, returns E_FAIL.')], HRESULT, 'ReadValueAsDate',
              ( ['retval', 'out'], POINTER(c_double), 'pVal' )),
    COMMETHOD([helpstring(u'Reads current object until property name matches or object ends. Case is ignored.')], HRESULT, 'FindProperty',
              ( ['in'], BSTR, 'propname' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'found' )),
    COMMETHOD([helpstring(u'Reads current object until one of property names matches. Case is ignored. Return value is an index of property name that matched, otherwise -1.')], HRESULT, 'FindProperties',
              ( ['in'], POINTER(IStringArray), 'propnames' ),
              ( ['retval', 'out'], POINTER(c_int), 'index' )),
    COMMETHOD([helpstring(u'Skips the rest of the current object, including closing bracket.')], HRESULT, 'SkipUntilObjectEnds'),
    COMMETHOD([helpstring(u'Skips the rest of the current object, including closing bracket.')], HRESULT, 'SkipUntilArrayEnds'),
]
################################################################
## code template for IJSONReader implementation
##class IJSONReader_Impl(object):
##    def IsString(self):
##        u'Indicates true if current token is a property value or array value of type string.'
##        #return pVal
##
##    def ReadFromString(self, Text):
##        u'Specifies input as string.'
##        #return 
##
##    def ReadPropertyName(self):
##        u'Obtains property name. Advances to the next token.'
##        #return pVal
##
##    def IsEndOfArray(self):
##        u"Indicates true if current token is ']'."
##        #return pVal
##
##    def FindProperties(self, propnames):
##        u'Reads current object until one of property names matches. Case is ignored. Return value is an index of property name that matched, otherwise -1.'
##        #return index
##
##    def ReadValue(self):
##        u'Obtains array or property value as Variant. Advances to the next token.'
##        #return pVal
##
##    def SkipUntilArrayEnds(self):
##        u'Skips the rest of the current object, including closing bracket.'
##        #return 
##
##    def Read(self):
##        u'Reads next JSON token.'
##        #return 
##
##    def SkipUntilObjectEnds(self):
##        u'Skips the rest of the current object, including closing bracket.'
##        #return 
##
##    def ReadValueAsString(self):
##        u'Obtains property or array value as string. Advances to the next token. If property value cannot be coerced to string, returns E_FAIL.'
##        #return pVal
##
##    def IsEndOfObject(self):
##        u"Indicates true if current token is '}'."
##        #return pVal
##
##    def IsBoolean(self):
##        u'Indicates true if current token is a property value or array value of boolean type.'
##        #return pVal
##
##    @property
##    def CurrentTokenType(self):
##        u'Obtains type of current token.'
##        #return pVal
##
##    def IsStartOfArray(self):
##        u"Indicates true if current token is '['."
##        #return pVal
##
##    def ReadValueAsBoolean(self):
##        u'Obtains array or property value as boolean. Advances to the next token. If property value cannot be coerced to boolean, returns E_FAIL.'
##        #return pVal
##
##    def FindProperty(self, propname):
##        u'Reads current object until property name matches or object ends. Case is ignored.'
##        #return found
##
##    def ReadValueAsDate(self):
##        u'Obtains property or array value as date. Advances to the next token. If property value cannot be coerced to datetime, returns E_FAIL.'
##        #return pVal
##
##    def ReadValueAsLong(self):
##        u'Obtains property or array value as number. Advances to the next token. If property value cannot be coerced to long, returns E_FAIL.'
##        #return pVal
##
##    @property
##    def Stream(self):
##        u'Obtains underlying stream.'
##        #return ppStream
##
##    def IsNull(self):
##        u'Indicates true if current token is a property value or array value and equals to null.'
##        #return pVal
##
##    def ReadValueAsDouble(self):
##        u'Obtains property or array value as number. Advances to the next token. If property value cannot be coerced to double, returns E_FAIL.'
##        #return pVal
##
##    def IsStartOfObject(self):
##        u"Indicates true if current token is '{'."
##        #return pVal
##
##    def IsNumber(self):
##        u'Indicates true if current token is a property value or array value of numeric type.'
##        #return pVal
##
##    def ReadFrom(self, inputStream):
##        u'Specifies input stream.'
##        #return 
##

IJSONReader2._methods_ = [
    COMMETHOD([helpstring(u"Parses JSON string into memory. Returns either IJSONObject or IJSONArray in a 'root' parameter. Doesn't change state of existing IJSONReader2 instance.")], HRESULT, 'ParseJSONString',
              ( ['in'], BSTR, 'json' ),
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'root' )),
    COMMETHOD([helpstring(u'Creates a bookmark on the current token and assigns it a name. Only works if you use ReadFromString(), otherwise returns E_FAIL.')], HRESULT, 'SetBookmark',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD([helpstring(u'Moves the reader back to a token that has a bookmark with the given name.')], HRESULT, 'ReturnToBookmark',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD([helpstring(u'Moves the reader back to a token that has a bookmark with the given name.')], HRESULT, 'RemoveBookmark',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD([helpstring(u'Removes all bookmarks.')], HRESULT, 'RemoveAllBookmarks'),
    COMMETHOD([helpstring(u'Obtains array or property value as Variant along with precision if it is a double. Advances to the next token.')], HRESULT, 'ReadValueEx',
              ( ['out'], POINTER(VARIANT), 'pVal' ),
              ( ['out'], POINTER(c_int), 'precision' )),
]
################################################################
## code template for IJSONReader2 implementation
##class IJSONReader2_Impl(object):
##    def SetBookmark(self, Name):
##        u'Creates a bookmark on the current token and assigns it a name. Only works if you use ReadFromString(), otherwise returns E_FAIL.'
##        #return 
##
##    def RemoveAllBookmarks(self):
##        u'Removes all bookmarks.'
##        #return 
##
##    def ReadValueEx(self):
##        u'Obtains array or property value as Variant along with precision if it is a double. Advances to the next token.'
##        #return pVal, precision
##
##    def ParseJSONString(self, json):
##        u"Parses JSON string into memory. Returns either IJSONObject or IJSONArray in a 'root' parameter. Doesn't change state of existing IJSONReader2 instance."
##        #return root
##
##    def RemoveBookmark(self, Name):
##        u'Moves the reader back to a token that has a bookmark with the given name.'
##        #return 
##
##    def ReturnToBookmark(self, Name):
##        u'Moves the reader back to a token that has a bookmark with the given name.'
##        #return 
##

class IPersistVariant(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members used for storage of an object through VARIANTs.'
    _iid_ = GUID('{67A4D651-69E0-11D2-8500-0000F875B9C6}')
    _idlflags_ = ['oleautomation']
IPersistVariant._methods_ = [
    COMMETHOD(['propget', helpstring(u'The ID of the object.')], HRESULT, 'ID',
              ( ['retval', 'out'], POINTER(POINTER(IUID)), 'objectID' )),
    COMMETHOD([helpstring(u'Loads the object properties from the stream.')], HRESULT, 'Load',
              ( ['in'], POINTER(IVariantStream), 'Stream' )),
    COMMETHOD([helpstring(u'Saves the object properties to the stream.')], HRESULT, 'Save',
              ( ['in'], POINTER(IVariantStream), 'Stream' )),
]
################################################################
## code template for IPersistVariant implementation
##class IPersistVariant_Impl(object):
##    def Load(self, Stream):
##        u'Loads the object properties from the stream.'
##        #return 
##
##    def Save(self, Stream):
##        u'Saves the object properties to the stream.'
##        #return 
##
##    @property
##    def ID(self):
##        u'The ID of the object.'
##        #return objectID
##

class JSONArray(CoClass):
    u'Simplified JSON API coclass'
    _reg_clsid_ = GUID('{7F763998-814E-45BD-9EBD-28CDA2A10FC6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class IJSONArray(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides simplified DOM-like JSON serialization and de-serialization API.'
    _iid_ = GUID('{4ABE3BC0-6D3C-4FBA-9C55-C9AC7C32D9B1}')
    _idlflags_ = ['oleautomation']
JSONArray._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IJSONArray, ISupportErrorInfo]

class IJobCatalog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods that control a catalog of jobs.'
    _iid_ = GUID('{5C395AAC-EBBC-4FFD-BB1E-C99858E168E0}')
    _idlflags_ = ['oleautomation']
class IJobRegistry(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods that control a Jobs Registry.'
    _iid_ = GUID('{E65C015E-E176-4419-96BF-4C0E45B3DB7D}')
    _idlflags_ = ['oleautomation']
class IJob(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to properties of job.'
    _iid_ = GUID('{72AD9072-FACE-4EC8-A7FD-23B41E58E2B7}')
    _idlflags_ = ['oleautomation']
class IEnumBSTR(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that enumerate over a set of strings.'
    _iid_ = GUID('{18A45BA8-1266-11D1-86AD-0000F8751720}')
    _idlflags_ = ['oleautomation']
IJobCatalog._methods_ = [
    COMMETHOD([helpstring(u'Initializes the job catalog.')], HRESULT, 'Init',
              ( ['in'], BSTR, 'root' ),
              ( ['in'], BSTR, 'JobProcessorName' ),
              ( ['in'], BSTR, 'JobProcessorType' )),
    COMMETHOD(['propput', helpstring(u'Job Registry.')], HRESULT, 'JobRegistry',
              ( ['in'], POINTER(IJobRegistry), 'rhs' )),
    COMMETHOD([helpstring(u'Creates a job and adds it to the catalog.')], HRESULT, 'CreateJob',
              ( ['retval', 'out'], POINTER(POINTER(IJob)), 'ppJob' )),
    COMMETHOD([helpstring(u'Creates a filter used for searching jobs.')], HRESULT, 'CreateJobFilter',
              ( ['retval', 'out'], POINTER(POINTER(IJobFilter)), 'ppFilter' )),
    COMMETHOD([helpstring(u'Retrieves job with given id from the catalog.')], HRESULT, 'GetJob',
              ( ['in'], BSTR, 'JobID' ),
              ( ['in'], VARIANT_BOOL, 'bLock' ),
              ( ['retval', 'out'], POINTER(POINTER(IJob)), 'ppJob' )),
    COMMETHOD([helpstring(u'Removes job with given id from the catalog.')], HRESULT, 'RemoveJob',
              ( ['in'], BSTR, 'JobID' )),
    COMMETHOD([helpstring(u'Returns ids of all jobs in the catalog that match specified filter.')], HRESULT, 'GetJobIDs',
              ( ['in'], POINTER(IJobFilter), 'pFilter' ),
              ( ['retval', 'out'], POINTER(POINTER(IEnumBSTR)), 'ppJobIDs' )),
]
################################################################
## code template for IJobCatalog implementation
##class IJobCatalog_Impl(object):
##    def RemoveJob(self, JobID):
##        u'Removes job with given id from the catalog.'
##        #return 
##
##    def CreateJob(self):
##        u'Creates a job and adds it to the catalog.'
##        #return ppJob
##
##    def _set(self, rhs):
##        u'Job Registry.'
##    JobRegistry = property(fset = _set, doc = _set.__doc__)
##
##    def GetJobIDs(self, pFilter):
##        u'Returns ids of all jobs in the catalog that match specified filter.'
##        #return ppJobIDs
##
##    def Init(self, root, JobProcessorName, JobProcessorType):
##        u'Initializes the job catalog.'
##        #return 
##
##    def GetJob(self, JobID, bLock):
##        u'Retrieves job with given id from the catalog.'
##        #return ppJob
##
##    def CreateJobFilter(self):
##        u'Creates a filter used for searching jobs.'
##        #return ppFilter
##


# values for enumeration 'esriJobStatus'
esriJobNew = 0
esriJobSubmitted = 1
esriJobWaiting = 2
esriJobExecuting = 3
esriJobSucceeded = 4
esriJobFailed = 5
esriJobTimedOut = 6
esriJobCancelling = 7
esriJobCancelled = 8
esriJobDeleting = 9
esriJobDeleted = 10
esriJobStatus = c_int # enum
class JSONWriter(CoClass):
    u'A sequential JSON Writer.'
    _reg_clsid_ = GUID('{BEC303DC-37AE-4EB3-92F5-397E5B6E7509}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
JSONWriter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IJSONWriter, IJSONWriter2, ISupportErrorInfo]

class IExternalSerializer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to high-level JSON serialization methods.'
    _iid_ = GUID('{E760E960-F144-4B30-930B-5F8056E4E305}')
    _idlflags_ = ['oleautomation']
IExternalSerializer._methods_ = [
    COMMETHOD([helpstring(u'Serializes an object.')], HRESULT, 'WriteObject',
              ( ['in'], POINTER(IUnknown), 'pUnk' ),
              ( ['in'], POINTER(IPropertySet), 'pProps' )),
]
################################################################
## code template for IExternalSerializer implementation
##class IExternalSerializer_Impl(object):
##    def WriteObject(self, pUnk, pProps):
##        u'Serializes an object.'
##        #return 
##

class ILogSupport(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods for initializing an object for logging.'
    _iid_ = GUID('{4F6EE3E2-25D7-4957-B008-3A5E9CE28180}')
    _idlflags_ = ['oleautomation']
class ILog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods for accessing a log.'
    _iid_ = GUID('{6F39C621-470B-4E6D-9033-A8598E286CAB}')
    _idlflags_ = ['oleautomation']
ILogSupport._methods_ = [
    COMMETHOD([helpstring(u'Initializes an object with a log.')], HRESULT, 'InitLogging',
              ( ['in'], POINTER(ILog), 'Log' )),
]
################################################################
## code template for ILogSupport implementation
##class ILogSupport_Impl(object):
##    def InitLogging(self, Log):
##        u'Initializes an object with a log.'
##        #return 
##

class AMFWriter(CoClass):
    u'A sequential AMF Writer.'
    _reg_clsid_ = GUID('{E312A49E-4A72-4766-9E5B-4B3FE8CA2EEC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class IAMFWriter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the sequential writing of AMF.'
    _iid_ = GUID('{3EB8C519-D125-48D4-AEB6-608074316AD4}')
    _idlflags_ = ['oleautomation']
AMFWriter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IAMFWriter, ISupportErrorInfo]

class IExternalDeserializer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to high-level JSON serialization methods.'
    _iid_ = GUID('{09134DE8-4147-4564-82BD-6CC18414C389}')
    _idlflags_ = ['oleautomation']
IExternalDeserializer._methods_ = [
    COMMETHOD([helpstring(u'Deserialize an object. riid references an interface to use. If interface is not supported, E_NOTIMPL is returned.')], HRESULT, 'ReadObject',
              ( ['in'], comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID, 'riid' ),
              ( ['in'], POINTER(IPropertySet), 'pProps' ),
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'ppUnk' )),
]
################################################################
## code template for IExternalDeserializer implementation
##class IExternalDeserializer_Impl(object):
##    def ReadObject(self, riid, pProps):
##        u'Deserialize an object. riid references an interface to use. If interface is not supported, E_NOTIMPL is returned.'
##        #return ppUnk
##

class ITime(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Time.'
    _iid_ = GUID('{66810D21-8DE0-44EE-B26E-465AC09F161F}')
    _idlflags_ = ['oleautomation']
class ITime2(ITime):
    _case_insensitive_ = True
    u'Provides access to members that control the Time.'
    _iid_ = GUID('{30EAE8E1-26B2-4E57-A3F2-8AE7C7DB2455}')
    _idlflags_ = ['oleautomation']
class ITimeReference(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Time Reference.'
    _iid_ = GUID('{F6CBA4A3-BC48-47BC-9F15-2A561B9E6C71}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriIntegerTimeFormat'
esriITFYearThruSecond = 0
esriITFYearThruMinute = 1
esriITFYearThruHour = 2
esriITFYearThruDay = 3
esriITFYearThruMonth = 4
esriITFYearOnly = 5
esriIntegerTimeFormat = c_int # enum
class _WKSDateTime(Structure):
    pass
WKSDateTime = _WKSDateTime
ITime._methods_ = [
    COMMETHOD(['propget', helpstring(u"The time's gregorian year.")], HRESULT, 'Year',
              ( ['retval', 'out'], POINTER(c_short), 'Year' )),
    COMMETHOD(['propput', helpstring(u"The time's gregorian year.")], HRESULT, 'Year',
              ( ['in'], c_short, 'Year' )),
    COMMETHOD(['propget', helpstring(u"The time's gregorian month.")], HRESULT, 'Month',
              ( ['retval', 'out'], POINTER(c_short), 'Month' )),
    COMMETHOD(['propput', helpstring(u"The time's gregorian month.")], HRESULT, 'Month',
              ( ['in'], c_short, 'Month' )),
    COMMETHOD(['propget', helpstring(u"The time's gregorian day.")], HRESULT, 'Day',
              ( ['retval', 'out'], POINTER(c_short), 'Day' )),
    COMMETHOD(['propput', helpstring(u"The time's gregorian day.")], HRESULT, 'Day',
              ( ['in'], c_short, 'Day' )),
    COMMETHOD(['propget', helpstring(u"The time's hour.")], HRESULT, 'Hour',
              ( ['retval', 'out'], POINTER(c_short), 'Hour' )),
    COMMETHOD(['propput', helpstring(u"The time's hour.")], HRESULT, 'Hour',
              ( ['in'], c_short, 'Hour' )),
    COMMETHOD(['propget', helpstring(u"The time's minute.")], HRESULT, 'Minute',
              ( ['retval', 'out'], POINTER(c_short), 'Minute' )),
    COMMETHOD(['propput', helpstring(u"The time's minute.")], HRESULT, 'Minute',
              ( ['in'], c_short, 'Minute' )),
    COMMETHOD(['propget', helpstring(u"The time's second.")], HRESULT, 'Second',
              ( ['retval', 'out'], POINTER(c_short), 'Second' )),
    COMMETHOD(['propput', helpstring(u"The time's second.")], HRESULT, 'Second',
              ( ['in'], c_short, 'Second' )),
    COMMETHOD(['propget', helpstring(u"The time's nanoseconds.")], HRESULT, 'Nanoseconds',
              ( ['retval', 'out'], POINTER(c_int), 'Nanoseconds' )),
    COMMETHOD(['propput', helpstring(u"The time's nanoseconds.")], HRESULT, 'Nanoseconds',
              ( ['in'], c_int, 'Nanoseconds' )),
    COMMETHOD([helpstring(u"The Time's date portion as a julian (Julius Scaliger) day number. Corresponds to the Year, Month, and Day properties.")], HRESULT, 'QueryJulianDayNumber',
              ( ['retval', 'out'], POINTER(c_int), 'julianDayNumber' )),
    COMMETHOD([helpstring(u"The Time's date portion as a julian (Julius Scaliger) day number. Corresponds to the Year, Month, and Day properties.")], HRESULT, 'SetJulianDayNumber',
              ( ['in'], c_int, 'julianDayNumber' )),
    COMMETHOD([helpstring(u"The time's time portion as a day fraction. Corresponds to the Hour, Minute, Second, and Nanoseconds properties.")], HRESULT, 'QueryDayFraction',
              ( ['retval', 'out'], POINTER(c_double), 'dayFraction' )),
    COMMETHOD([helpstring(u"The time's time portion as a day fraction. Corresponds to the Hour, Minute, Second, and Nanoseconds properties.")], HRESULT, 'SetDayFraction',
              ( ['in'], c_double, 'dayFraction' )),
    COMMETHOD([helpstring(u"The time's time portion as the number of nanoseconds elapsed since midnight. Corresponds to the Hour, Minute, Second, and Nanoseconds properties.")], HRESULT, 'QueryNanosecondsSinceMidnight',
              ( ['retval', 'out'], POINTER(c_longlong), 'nanosecondsSinceMidnight' )),
    COMMETHOD([helpstring(u"The time's time portion as the number of nanoseconds elapsed since midnight. Corresponds to the Hour, Minute, Second, and Nanoseconds properties.")], HRESULT, 'SetNanosecondsSinceMidnight',
              ( ['in'], c_longlong, 'nanosecondsSinceMidnight' )),
    COMMETHOD([helpstring(u'Subtracts a given time, and returns the time duration result.')], HRESULT, 'SubtractTime',
              ( ['in'], POINTER(ITime), 'Time' ),
              ( ['retval', 'out'], POINTER(POINTER(ITimeDuration)), 'TimeDuration' )),
    COMMETHOD([helpstring(u'Adjust the day value, to the last day in the current month and year.')], HRESULT, 'SnapToEndOfMonth'),
    COMMETHOD([helpstring(u'Converts the time from local (to this machine) time value to Coordinated Universal Time (UTC).')], HRESULT, 'ToUTC'),
    COMMETHOD([helpstring(u'Converts the time from Coordinated Universal Time (UTC) value to local (to this machine) time.')], HRESULT, 'ToLocal'),
    COMMETHOD([helpstring(u'Obtains the time as a string, based on the given time string format.')], HRESULT, 'QueryTimeString',
              ( ['in'], esriTimeStringFormat, 'timeStringFormat' ),
              ( ['retval', 'out'], POINTER(BSTR), 'timeString' )),
    COMMETHOD([helpstring(u'Writes the time from a string, based on the given time string format.')], HRESULT, 'SetFromTimeString',
              ( ['in'], esriTimeStringFormat, 'timeStringFormat' ),
              ( ['in'], BSTR, 'timeString' )),
    COMMETHOD([helpstring(u'Obtains the time as a string, based on the current locale.')], HRESULT, 'QueryTimeStringCurrentLocale',
              ( ['in'], esriTimeLocaleFormat, 'timeLocaleFormat' ),
              ( ['retval', 'out'], POINTER(BSTR), 'timeString' )),
    COMMETHOD([helpstring(u'Obtains the time from a string, based on the current locale.')], HRESULT, 'SetFromTimeStringCurrentLocale',
              ( ['in'], esriTimeLocaleFormat, 'timeLocaleFormat' ),
              ( ['in'], BSTR, 'timeString' )),
    COMMETHOD([helpstring(u'Obtains the time as a string, based on the given custom time string format, and locale properties.')], HRESULT, 'QueryTimeStringCustom',
              ( ['in'], BSTR, 'timeStringFormat' ),
              ( ['in'], c_int, 'LocaleID' ),
              ( ['in'], BSTR, 'amSymbol' ),
              ( ['in'], BSTR, 'pmSymbol' ),
              ( ['retval', 'out'], POINTER(BSTR), 'timeString' )),
    COMMETHOD([helpstring(u'Writes the time from a string, based on the given custom time string formats, and locale properties.')], HRESULT, 'SetFromTimeStringCustom',
              ( ['in'], BSTR, 'timeStringFormat' ),
              ( ['in'], c_int, 'LocaleID' ),
              ( ['in'], BSTR, 'amSymbol' ),
              ( ['in'], BSTR, 'pmSymbol' ),
              ( ['in'], BSTR, 'timeString' )),
    COMMETHOD([helpstring(u'Obtains the time as an XML time string.')], HRESULT, 'QueryXMLTimeString',
              ( ['in'], POINTER(ITimeReference), 'TimeReference' ),
              ( ['retval', 'out'], POINTER(BSTR), 'xmlTimeString' )),
    COMMETHOD([helpstring(u'Writes the time from an XML time string.')], HRESULT, 'SetFromXMLTimeString',
              ( ['in'], BSTR, 'xmlTimeString' ),
              ( ['retval', 'out'], POINTER(c_int), 'timeZoneBiasFromUTC' )),
    COMMETHOD([helpstring(u'Obtains the time as an integer time.')], HRESULT, 'QueryIntegerTime',
              ( ['in'], esriIntegerTimeFormat, 'integerTimeFormat' ),
              ( ['retval', 'out'], POINTER(c_longlong), 'integerTime' )),
    COMMETHOD([helpstring(u'Writes the time from an integer time.')], HRESULT, 'SetFromIntegerTime',
              ( ['in'], esriIntegerTimeFormat, 'integerTimeFormat' ),
              ( ['in'], c_longlong, 'integerTime' )),
    COMMETHOD([helpstring(u'Writes the time from a variant object.')], HRESULT, 'SetFromObject',
              ( ['in'], VARIANT, 'Object' )),
    COMMETHOD([helpstring(u'Obtains the time as an OLE automation date object.')], HRESULT, 'QueryOleTime',
              ( ['retval', 'out'], POINTER(c_double), 'oleTime' )),
    COMMETHOD([helpstring(u'Writes the time from an OLE automation date object.')], HRESULT, 'SetFromOleTime',
              ( ['in'], c_double, 'oleTime' )),
    COMMETHOD([helpstring(u'Obtains the time as a gregorian date and time.')], HRESULT, 'QueryGregorianTime',
              ( ['retval', 'out'], POINTER(WKSDateTime), 'gregorianTime' )),
    COMMETHOD([helpstring(u'Obtains the time from a given gregorian date and time value.')], HRESULT, 'SetFromGregorianTime',
              ( ['in'], POINTER(WKSDateTime), 'gregorianTime' )),
    COMMETHOD([helpstring(u'Obtains the time as the number of ticks since January 1, 0001 AD (Anno Domini).')], HRESULT, 'QueryTicks',
              ( ['retval', 'out'], POINTER(c_longlong), 'ticks' )),
    COMMETHOD([helpstring(u'Writes the time from a given number of ticks since January 1, 0001 AD (Anno Domini) value.')], HRESULT, 'SetFromTicks',
              ( ['in'], c_longlong, 'ticks' )),
    COMMETHOD([helpstring(u'Writes the time to the current date and time on this machine, expressed as the local time.')], HRESULT, 'SetFromCurrentLocalTime'),
    COMMETHOD([helpstring(u'Writes the time to the current date and time on this machine, expressed as the Coordinated Universal Time (UTC).')], HRESULT, 'SetFromCurrentUtcTime'),
    COMMETHOD([helpstring(u"Compares this time to the other time. Returns -1 if this time's value is less, 1 if greater, and 0 otherwise.")], HRESULT, 'Compare',
              ( ['in'], POINTER(ITime), 'otherTime' ),
              ( ['retval', 'out'], POINTER(c_int), 'Result' )),
]
################################################################
## code template for ITime implementation
##class ITime_Impl(object):
##    def SetFromObject(self, Object):
##        u'Writes the time from a variant object.'
##        #return 
##
##    def ToLocal(self):
##        u'Converts the time from Coordinated Universal Time (UTC) value to local (to this machine) time.'
##        #return 
##
##    def QueryGregorianTime(self):
##        u'Obtains the time as a gregorian date and time.'
##        #return gregorianTime
##
##    def SnapToEndOfMonth(self):
##        u'Adjust the day value, to the last day in the current month and year.'
##        #return 
##
##    def QueryIntegerTime(self, integerTimeFormat):
##        u'Obtains the time as an integer time.'
##        #return integerTime
##
##    def QueryTimeStringCustom(self, timeStringFormat, LocaleID, amSymbol, pmSymbol):
##        u'Obtains the time as a string, based on the given custom time string format, and locale properties.'
##        #return timeString
##
##    def QueryTimeString(self, timeStringFormat):
##        u'Obtains the time as a string, based on the given time string format.'
##        #return timeString
##
##    def SetFromTimeString(self, timeStringFormat, timeString):
##        u'Writes the time from a string, based on the given time string format.'
##        #return 
##
##    def QueryJulianDayNumber(self):
##        u"The Time's date portion as a julian (Julius Scaliger) day number. Corresponds to the Year, Month, and Day properties."
##        #return julianDayNumber
##
##    def SetFromTimeStringCustom(self, timeStringFormat, LocaleID, amSymbol, pmSymbol, timeString):
##        u'Writes the time from a string, based on the given custom time string formats, and locale properties.'
##        #return 
##
##    def SetFromGregorianTime(self, gregorianTime):
##        u'Obtains the time from a given gregorian date and time value.'
##        #return 
##
##    def ToUTC(self):
##        u'Converts the time from local (to this machine) time value to Coordinated Universal Time (UTC).'
##        #return 
##
##    def QueryDayFraction(self):
##        u"The time's time portion as a day fraction. Corresponds to the Hour, Minute, Second, and Nanoseconds properties."
##        #return dayFraction
##
##    def _get(self):
##        u"The time's gregorian day."
##        #return Day
##    def _set(self, Day):
##        u"The time's gregorian day."
##    Day = property(_get, _set, doc = _set.__doc__)
##
##    def SetNanosecondsSinceMidnight(self, nanosecondsSinceMidnight):
##        u"The time's time portion as the number of nanoseconds elapsed since midnight. Corresponds to the Hour, Minute, Second, and Nanoseconds properties."
##        #return 
##
##    def SetJulianDayNumber(self, julianDayNumber):
##        u"The Time's date portion as a julian (Julius Scaliger) day number. Corresponds to the Year, Month, and Day properties."
##        #return 
##
##    def QueryXMLTimeString(self, TimeReference):
##        u'Obtains the time as an XML time string.'
##        #return xmlTimeString
##
##    def _get(self):
##        u"The time's hour."
##        #return Hour
##    def _set(self, Hour):
##        u"The time's hour."
##    Hour = property(_get, _set, doc = _set.__doc__)
##
##    def QueryOleTime(self):
##        u'Obtains the time as an OLE automation date object.'
##        #return oleTime
##
##    def SetFromXMLTimeString(self, xmlTimeString):
##        u'Writes the time from an XML time string.'
##        #return timeZoneBiasFromUTC
##
##    def QueryNanosecondsSinceMidnight(self):
##        u"The time's time portion as the number of nanoseconds elapsed since midnight. Corresponds to the Hour, Minute, Second, and Nanoseconds properties."
##        #return nanosecondsSinceMidnight
##
##    def Compare(self, otherTime):
##        u"Compares this time to the other time. Returns -1 if this time's value is less, 1 if greater, and 0 otherwise."
##        #return Result
##
##    def SetDayFraction(self, dayFraction):
##        u"The time's time portion as a day fraction. Corresponds to the Hour, Minute, Second, and Nanoseconds properties."
##        #return 
##
##    def SubtractTime(self, Time):
##        u'Subtracts a given time, and returns the time duration result.'
##        #return TimeDuration
##
##    def SetFromIntegerTime(self, integerTimeFormat, integerTime):
##        u'Writes the time from an integer time.'
##        #return 
##
##    def SetFromTimeStringCurrentLocale(self, timeLocaleFormat, timeString):
##        u'Obtains the time from a string, based on the current locale.'
##        #return 
##
##    def SetFromTicks(self, ticks):
##        u'Writes the time from a given number of ticks since January 1, 0001 AD (Anno Domini) value.'
##        #return 
##
##    def QueryTimeStringCurrentLocale(self, timeLocaleFormat):
##        u'Obtains the time as a string, based on the current locale.'
##        #return timeString
##
##    def _get(self):
##        u"The time's nanoseconds."
##        #return Nanoseconds
##    def _set(self, Nanoseconds):
##        u"The time's nanoseconds."
##    Nanoseconds = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u"The time's gregorian month."
##        #return Month
##    def _set(self, Month):
##        u"The time's gregorian month."
##    Month = property(_get, _set, doc = _set.__doc__)
##
##    def QueryTicks(self):
##        u'Obtains the time as the number of ticks since January 1, 0001 AD (Anno Domini).'
##        #return ticks
##
##    def SetFromCurrentUtcTime(self):
##        u'Writes the time to the current date and time on this machine, expressed as the Coordinated Universal Time (UTC).'
##        #return 
##
##    def _get(self):
##        u"The time's second."
##        #return Second
##    def _set(self, Second):
##        u"The time's second."
##    Second = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u"The time's minute."
##        #return Minute
##    def _set(self, Minute):
##        u"The time's minute."
##    Minute = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u"The time's gregorian year."
##        #return Year
##    def _set(self, Year):
##        u"The time's gregorian year."
##    Year = property(_get, _set, doc = _set.__doc__)
##
##    def SetFromCurrentLocalTime(self):
##        u'Writes the time to the current date and time on this machine, expressed as the local time.'
##        #return 
##
##    def SetFromOleTime(self, oleTime):
##        u'Writes the time from an OLE automation date object.'
##        #return 
##

ITime2._methods_ = [
    COMMETHOD(['propget', helpstring(u'The day number of the week, starting with 1 for Sunday.')], HRESULT, 'DayOfWeek',
              ( ['retval', 'out'], POINTER(c_short), 'dayNumber' )),
    COMMETHOD(['propget', helpstring(u'The day number of the year, starting with 1 for the first day of the year.')], HRESULT, 'DayOfYear',
              ( ['retval', 'out'], POINTER(c_short), 'dayNumber' )),
    COMMETHOD(['propget', helpstring(u'The week number of the month, starting with 1 for the first week of the month. Use startDayOfWeek = 1 to specify that weeks start on Sunday, and 2 on Monday.')], HRESULT, 'WeekOfMonth',
              ( ['in'], c_short, 'startDayOfWeek' ),
              ( ['retval', 'out'], POINTER(c_short), 'weekNumber' )),
    COMMETHOD(['propget', helpstring(u'The week number of the year, starting with 1 for first week of the year. Use startDayOfWeek = 1 to specify that weeks start on Sunday, and 2 on Monday.')], HRESULT, 'WeekOfYear',
              ( ['in'], c_short, 'startDayOfWeek' ),
              ( ['retval', 'out'], POINTER(c_short), 'weekNumber' )),
]
################################################################
## code template for ITime2 implementation
##class ITime2_Impl(object):
##    @property
##    def DayOfWeek(self):
##        u'The day number of the week, starting with 1 for Sunday.'
##        #return dayNumber
##
##    @property
##    def DayOfYear(self):
##        u'The day number of the year, starting with 1 for the first day of the year.'
##        #return dayNumber
##
##    @property
##    def WeekOfMonth(self, startDayOfWeek):
##        u'The week number of the month, starting with 1 for the first week of the month. Use startDayOfWeek = 1 to specify that weeks start on Sunday, and 2 on Monday.'
##        #return weekNumber
##
##    @property
##    def WeekOfYear(self, startDayOfWeek):
##        u'The week number of the year, starting with 1 for first week of the year. Use startDayOfWeek = 1 to specify that weeks start on Sunday, and 2 on Monday.'
##        #return weekNumber
##

class IArray(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control a simple array of objects.'
    _iid_ = GUID('{AAFB54D9-AAF8-11D2-87F3-0000F8751720}')
    _idlflags_ = ['oleautomation']
IArray._methods_ = [
    COMMETHOD(['propget', helpstring(u'The element count of the array.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Searches for the object in the array.')], HRESULT, 'Element',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'unk' )),
    COMMETHOD([helpstring(u'Adds an object to the array.')], HRESULT, 'Add',
              ( ['in'], POINTER(IUnknown), 'unk' )),
    COMMETHOD([helpstring(u'Adds an object to the array at the specified index.')], HRESULT, 'Insert',
              ( ['in'], c_int, 'index' ),
              ( ['in'], POINTER(IUnknown), 'unk' )),
    COMMETHOD([helpstring(u'Removes an object from the array.')], HRESULT, 'Remove',
              ( ['in'], c_int, 'index' )),
    COMMETHOD([helpstring(u'Removes all objects from the array.')], HRESULT, 'RemoveAll'),
]
################################################################
## code template for IArray implementation
##class IArray_Impl(object):
##    @property
##    def Count(self):
##        u'The element count of the array.'
##        #return Count
##
##    def Insert(self, index, unk):
##        u'Adds an object to the array at the specified index.'
##        #return 
##
##    def Remove(self, index):
##        u'Removes an object from the array.'
##        #return 
##
##    @property
##    def Element(self, index):
##        u'Searches for the object in the array.'
##        #return unk
##
##    def RemoveAll(self):
##        u'Removes all objects from the array.'
##        #return 
##
##    def Add(self, unk):
##        u'Adds an object to the array.'
##        #return 
##

class IDoubleArray(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control double arrays.'
    _iid_ = GUID('{60C06CA6-E09E-11D2-9F7B-00C04F8ECE27}')
    _idlflags_ = ['oleautomation']
IDoubleArray._methods_ = [
    COMMETHOD(['propget', helpstring(u'The number of elements in the array.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'pCount' )),
    COMMETHOD([helpstring(u'Removes an element from the array.')], HRESULT, 'Remove',
              ( ['in'], c_int, 'index' )),
    COMMETHOD([helpstring(u'Removes all elements from the array.')], HRESULT, 'RemoveAll'),
    COMMETHOD(['propget', helpstring(u'An element from the array.')], HRESULT, 'Element',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(c_double), 'pElement' )),
    COMMETHOD(['propput', helpstring(u'An element from the array.')], HRESULT, 'Element',
              ( ['in'], c_int, 'index' ),
              ( ['in'], c_double, 'pElement' )),
    COMMETHOD([helpstring(u'Adds an element to the array.')], HRESULT, 'Add',
              ( ['in'], c_double, 'Element' )),
    COMMETHOD([helpstring(u'Inserts an element to the array.')], HRESULT, 'Insert',
              ( ['in'], c_int, 'index' ),
              ( ['in'], c_double, 'Element' )),
]
################################################################
## code template for IDoubleArray implementation
##class IDoubleArray_Impl(object):
##    @property
##    def Count(self):
##        u'The number of elements in the array.'
##        #return pCount
##
##    def Insert(self, index, Element):
##        u'Inserts an element to the array.'
##        #return 
##
##    def Remove(self, index):
##        u'Removes an element from the array.'
##        #return 
##
##    def _get(self, index):
##        u'An element from the array.'
##        #return pElement
##    def _set(self, index, pElement):
##        u'An element from the array.'
##    Element = property(_get, _set, doc = _set.__doc__)
##
##    def RemoveAll(self):
##        u'Removes all elements from the array.'
##        #return 
##
##    def Add(self, Element):
##        u'Adds an element to the array.'
##        #return 
##

class JobMessage(CoClass):
    u'The JobMessage object which defines properties and behaviour og job messages.'
    _reg_clsid_ = GUID('{512E6A8A-3C50-4DEC-B681-7254FEDE4109}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class IPersistStream(IPersist):
    _case_insensitive_ = True
    _iid_ = GUID('{00000109-0000-0000-C000-000000000046}')
    _idlflags_ = []
JobMessage._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IJobMessage, IXMLSerialize, IPersistStream]

class ITimeZoneInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the time zone information.'
    _iid_ = GUID('{0F8FD6AB-CE6D-4BB2-A5EF-2F6035E304C5}')
    _idlflags_ = ['oleautomation']
ITimeReference._methods_ = [
    COMMETHOD(['propget', helpstring(u'The time zone information associated with the time reference.')], HRESULT, 'TimeZoneInfo',
              ( ['retval', 'out'], POINTER(POINTER(ITimeZoneInfo)), 'timeZone' )),
    COMMETHOD(['propputref', helpstring(u'The time zone information associated with the time reference.')], HRESULT, 'TimeZoneInfo',
              ( ['in'], POINTER(ITimeZoneInfo), 'timeZone' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the time reference respects daylight saving time.')], HRESULT, 'RespectsDaylightSavingTime',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'RespectsDaylightSavingTime' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether the time reference respects daylight saving time.')], HRESULT, 'RespectsDaylightSavingTime',
              ( ['in'], VARIANT_BOOL, 'RespectsDaylightSavingTime' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the time reference respects dynamic adjustment rules.')], HRESULT, 'RespectsDynamicAdjustmentRules',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'RespectsDynamicAdjustmentRules' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether the time reference respects dynamic adjustment rules.')], HRESULT, 'RespectsDynamicAdjustmentRules',
              ( ['in'], VARIANT_BOOL, 'RespectsDynamicAdjustmentRules' )),
    COMMETHOD([helpstring(u'Projects a given time, from this time reference, to a given time reference.')], HRESULT, 'Project',
              ( ['in'], POINTER(ITime), 'Time' ),
              ( ['in'], POINTER(ITimeReference), 'otherTimeReference' )),
    COMMETHOD([helpstring(u'Projects a given time, from this time reference, to UTC.')], HRESULT, 'ProjectToUTC',
              ( ['in'], POINTER(ITime), 'Time' )),
    COMMETHOD([helpstring(u'Projects a given time, from UTC to this time reference.')], HRESULT, 'ProjectFromUTC',
              ( ['in'], POINTER(ITime), 'Time' )),
]
################################################################
## code template for ITimeReference implementation
##class ITimeReference_Impl(object):
##    def _get(self):
##        u'Indicates whether the time reference respects dynamic adjustment rules.'
##        #return RespectsDynamicAdjustmentRules
##    def _set(self, RespectsDynamicAdjustmentRules):
##        u'Indicates whether the time reference respects dynamic adjustment rules.'
##    RespectsDynamicAdjustmentRules = property(_get, _set, doc = _set.__doc__)
##
##    def ProjectFromUTC(self, Time):
##        u'Projects a given time, from UTC to this time reference.'
##        #return 
##
##    def ProjectToUTC(self, Time):
##        u'Projects a given time, from this time reference, to UTC.'
##        #return 
##
##    def Project(self, Time, otherTimeReference):
##        u'Projects a given time, from this time reference, to a given time reference.'
##        #return 
##
##    def TimeZoneInfo(self, timeZone):
##        u'The time zone information associated with the time reference.'
##        #return 
##
##    def _get(self):
##        u'Indicates whether the time reference respects daylight saving time.'
##        #return RespectsDaylightSavingTime
##    def _set(self, RespectsDaylightSavingTime):
##        u'Indicates whether the time reference respects daylight saving time.'
##    RespectsDaylightSavingTime = property(_get, _set, doc = _set.__doc__)
##

IAMFWriter._methods_ = [
    COMMETHOD([helpstring(u'Specifies output AMF stream.')], HRESULT, 'WriteTo',
              ( ['in'], POINTER(IStream), 'outputStream' )),
    COMMETHOD(['propget', helpstring(u'Obtains underlying stream.')], HRESULT, 'Stream',
              ( ['retval', 'out'], POINTER(POINTER(IStream)), 'ppStream' )),
    COMMETHOD([helpstring(u'Writes undefined value.')], HRESULT, 'WriteAMF3Undefined'),
    COMMETHOD([helpstring(u'Writes null value.')], HRESULT, 'WriteAMF3Null'),
    COMMETHOD([helpstring(u'Writes boolean value.')], HRESULT, 'WriteAMF3Bool',
              ( ['in'], VARIANT_BOOL, 'Value' )),
    COMMETHOD([helpstring(u'Writes integer (32-bit) value.')], HRESULT, 'WriteAMF3Int',
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([helpstring(u'Writes double (64-bit) value.')], HRESULT, 'WriteAMF3Double',
              ( ['in'], c_double, 'Value' )),
    COMMETHOD([helpstring(u'Writes string value. Returns string reference index.')], HRESULT, 'WriteAMF3String',
              ( ['in'], BSTR, 'Value' ),
              ( ['out'], POINTER(c_int), 'string_ref' )),
    COMMETHOD([helpstring(u'Writes string value by reference.')], HRESULT, 'WriteAMF3StringRef',
              ( ['in'], c_int, 'string_ref' )),
    COMMETHOD([helpstring(u'Writes XML document. Returns object reference index.')], HRESULT, 'WriteAMF3XmlDoc',
              ( ['in'], BSTR, 'Value' ),
              ( ['out'], POINTER(c_int), 'obj_ref' )),
    COMMETHOD([helpstring(u'Writes XML document by reference.')], HRESULT, 'WriteAMF3XmlDocRef',
              ( ['in'], c_int, 'obj_ref' )),
    COMMETHOD([helpstring(u'Writes XML. Returns object reference index.')], HRESULT, 'WriteAMF3Xml',
              ( ['in'], BSTR, 'Value' ),
              ( ['out'], POINTER(c_int), 'obj_ref' )),
    COMMETHOD([helpstring(u'Writes XML by reference.')], HRESULT, 'WriteAMF3XmlRef',
              ( ['in'], c_int, 'obj_ref' )),
    COMMETHOD([helpstring(u'Writes date. Returns object reference index.')], HRESULT, 'WriteAMF3Date',
              ( ['in'], c_double, 'Value' ),
              ( ['in'], VARIANT_BOOL, 'asJsonNumber' ),
              ( ['out'], POINTER(c_int), 'obj_ref' )),
    COMMETHOD([helpstring(u'Writes date by reference. Important: do not use this method if you send dates as JSON numbers, references will be incorrect.')], HRESULT, 'WriteAMF3DateRef',
              ( ['in'], c_int, 'obj_ref' )),
    COMMETHOD([helpstring(u'Writes byte array. Returns object reference index. Note that this is not an AMF3 array but another type - AMF3 byte array.')], HRESULT, 'WriteAMF3ByteArray',
              ( ['in'], POINTER(_midlSAFEARRAY(c_ubyte)), 'ppArray' ),
              ( ['out'], POINTER(c_int), 'obj_ref' )),
    COMMETHOD([helpstring(u'Writes byte array by reference. Note that this is not an AMF3 array but another type - AMF3 byte array.')], HRESULT, 'WriteAMF3ByteArrayRef',
              ( ['in'], c_int, 'obj_ref' )),
    COMMETHOD([helpstring(u'Writes value types (excluding array and object), may return string or object reference index. If reference is not applicable, value_ref is set to -1.')], HRESULT, 'WriteAMF3Variant',
              ( ['in'], VARIANT, 'Value' ),
              ( ['out'], POINTER(c_int), 'value_ref' )),
    COMMETHOD([helpstring(u'Starts writing of array. Returns object reference index.')], HRESULT, 'StartAMF3Array',
              ( ['in'], c_int, 'denseCount' ),
              ( ['out'], POINTER(c_int), 'obj_ref' )),
    COMMETHOD([helpstring(u'Switches from writing of associative portion of an array to dense portion.')], HRESULT, 'WriteAMF3ArrayDenseMarker'),
    COMMETHOD([helpstring(u'Finishes writing an array.')], HRESULT, 'EndAMF3Array'),
    COMMETHOD([helpstring(u'Writes an array by reference.')], HRESULT, 'WriteAMF3ArrayRef',
              ( ['in'], c_int, 'obj_ref' )),
    COMMETHOD([helpstring(u'Starst writing a custom object. Contents of this kind of objects are user-defined.')], HRESULT, 'StartAMF3CustomObject',
              ( ['in'], BSTR, 'classname' ),
              ( ['out'], POINTER(c_int), 'obj_ref' )),
    COMMETHOD([helpstring(u'Starts writing an object, sends traits by reference. Returns object reference index.')], HRESULT, 'StartAMF3Object',
              ( ['in'], c_int, 'traits_ref' ),
              ( ['out'], POINTER(c_int), 'obj_ref' )),
    COMMETHOD([helpstring(u'Start writing an object with traits. Returns trait reference index end object reference index.')], HRESULT, 'StartAMF3ObjectWithTraits',
              ( ['in'], BSTR, 'classname' ),
              ( ['in'], c_int, 'MemberCount' ),
              ( ['in'], VARIANT_BOOL, 'dynamic' ),
              ( ['out'], POINTER(c_int), 'traits_ref' ),
              ( ['out'], POINTER(c_int), 'obj_ref' )),
    COMMETHOD([helpstring(u'Call this method to finish writing object traits and switch to writing members.')], HRESULT, 'EndAMF3ObjectTraits'),
    COMMETHOD([helpstring(u'Finishes writing object.')], HRESULT, 'EndAMF3Object'),
    COMMETHOD([helpstring(u'Writes object by reference.')], HRESULT, 'WriteAMF3ObjectRef',
              ( ['in'], c_int, 'obj_ref' )),
    COMMETHOD([helpstring(u'This method is required if you want to write member names in traits.')], HRESULT, 'WriteAMF3_UTF8',
              ( ['in'], BSTR, 'Value' ),
              ( ['out'], POINTER(c_int), 'string_ref' )),
    COMMETHOD([helpstring(u'This method is required if you want to write member names in traits by reference.')], HRESULT, 'WriteAMF3_UTF8Ref',
              ( ['in'], c_int, 'string_ref' )),
    COMMETHOD([helpstring(u"Writes a byte. AMF0 format only. Don't use this method for AMF3 objects.")], HRESULT, 'WriteU8',
              ( ['in'], c_ubyte, 'b' )),
    COMMETHOD([helpstring(u"Writes short integer. AMF0 format only. Don't use this method for AMF3 objects.")], HRESULT, 'WriteU16',
              ( ['in'], c_short, 'b' )),
    COMMETHOD([helpstring(u"Writes an integer. AMF0 format only. Don't use this method for AMF3 objects.")], HRESULT, 'WriteU32',
              ( ['in'], c_int, 'b' )),
    COMMETHOD([helpstring(u"This method is used to write AMF0 strings. AMF0 format only. Don't use this method for AMF3 objects.")], HRESULT, 'WriteUTF8',
              ( ['in'], BSTR, 'Value' )),
    COMMETHOD([helpstring(u'Clones IAMFWriter. Useful when you want to preserve traits and object, string and trait references.')], HRESULT, 'GetCopy',
              ( ['out'], POINTER(POINTER(IAMFWriter)), 'ppOutWriter' )),
]
################################################################
## code template for IAMFWriter implementation
##class IAMFWriter_Impl(object):
##    def WriteU8(self, b):
##        u"Writes a byte. AMF0 format only. Don't use this method for AMF3 objects."
##        #return 
##
##    def StartAMF3ObjectWithTraits(self, classname, MemberCount, dynamic):
##        u'Start writing an object with traits. Returns trait reference index end object reference index.'
##        #return traits_ref, obj_ref
##
##    def WriteU16(self, b):
##        u"Writes short integer. AMF0 format only. Don't use this method for AMF3 objects."
##        #return 
##
##    def WriteUTF8(self, Value):
##        u"This method is used to write AMF0 strings. AMF0 format only. Don't use this method for AMF3 objects."
##        #return 
##
##    def WriteU32(self, b):
##        u"Writes an integer. AMF0 format only. Don't use this method for AMF3 objects."
##        #return 
##
##    def StartAMF3CustomObject(self, classname):
##        u'Starst writing a custom object. Contents of this kind of objects are user-defined.'
##        #return obj_ref
##
##    def WriteAMF3DateRef(self, obj_ref):
##        u'Writes date by reference. Important: do not use this method if you send dates as JSON numbers, references will be incorrect.'
##        #return 
##
##    def WriteTo(self, outputStream):
##        u'Specifies output AMF stream.'
##        #return 
##
##    def WriteAMF3Undefined(self):
##        u'Writes undefined value.'
##        #return 
##
##    def EndAMF3ObjectTraits(self):
##        u'Call this method to finish writing object traits and switch to writing members.'
##        #return 
##
##    def WriteAMF3Date(self, Value, asJsonNumber):
##        u'Writes date. Returns object reference index.'
##        #return obj_ref
##
##    def WriteAMF3Null(self):
##        u'Writes null value.'
##        #return 
##
##    def WriteAMF3String(self, Value):
##        u'Writes string value. Returns string reference index.'
##        #return string_ref
##
##    def WriteAMF3ByteArrayRef(self, obj_ref):
##        u'Writes byte array by reference. Note that this is not an AMF3 array but another type - AMF3 byte array.'
##        #return 
##
##    def GetCopy(self):
##        u'Clones IAMFWriter. Useful when you want to preserve traits and object, string and trait references.'
##        #return ppOutWriter
##
##    def WriteAMF3ByteArray(self, ppArray):
##        u'Writes byte array. Returns object reference index. Note that this is not an AMF3 array but another type - AMF3 byte array.'
##        #return obj_ref
##
##    def WriteAMF3Bool(self, Value):
##        u'Writes boolean value.'
##        #return 
##
##    def WriteAMF3Variant(self, Value):
##        u'Writes value types (excluding array and object), may return string or object reference index. If reference is not applicable, value_ref is set to -1.'
##        #return value_ref
##
##    def WriteAMF3Int(self, Value):
##        u'Writes integer (32-bit) value.'
##        #return 
##
##    def WriteAMF3XmlRef(self, obj_ref):
##        u'Writes XML by reference.'
##        #return 
##
##    def WriteAMF3ArrayDenseMarker(self):
##        u'Switches from writing of associative portion of an array to dense portion.'
##        #return 
##
##    def WriteAMF3_UTF8Ref(self, string_ref):
##        u'This method is required if you want to write member names in traits by reference.'
##        #return 
##
##    def EndAMF3Array(self):
##        u'Finishes writing an array.'
##        #return 
##
##    def WriteAMF3XmlDoc(self, Value):
##        u'Writes XML document. Returns object reference index.'
##        #return obj_ref
##
##    @property
##    def Stream(self):
##        u'Obtains underlying stream.'
##        #return ppStream
##
##    def WriteAMF3ArrayRef(self, obj_ref):
##        u'Writes an array by reference.'
##        #return 
##
##    def EndAMF3Object(self):
##        u'Finishes writing object.'
##        #return 
##
##    def WriteAMF3Xml(self, Value):
##        u'Writes XML. Returns object reference index.'
##        #return obj_ref
##
##    def WriteAMF3ObjectRef(self, obj_ref):
##        u'Writes object by reference.'
##        #return 
##
##    def StartAMF3Array(self, denseCount):
##        u'Starts writing of array. Returns object reference index.'
##        #return obj_ref
##
##    def WriteAMF3StringRef(self, string_ref):
##        u'Writes string value by reference.'
##        #return 
##
##    def StartAMF3Object(self, traits_ref):
##        u'Starts writing an object, sends traits by reference. Returns object reference index.'
##        #return obj_ref
##
##    def WriteAMF3XmlDocRef(self, obj_ref):
##        u'Writes XML document by reference.'
##        #return 
##
##    def WriteAMF3_UTF8(self, Value):
##        u'This method is required if you want to write member names in traits.'
##        #return string_ref
##
##    def WriteAMF3Double(self, Value):
##        u'Writes double (64-bit) value.'
##        #return 
##


# values for enumeration 'xmlSerializeError'
XML_SERIALIZE_E_UNKNOWN = -2147209115
XML_SERIALIZE_E_INVALIDENUMVALUE = -2147209114
XML_SERIALIZE_E_CONVFAILED = -2147209113
XML_SERIALIZE_E_CANT_MAP_XMLTYPE_TO_CLASS = -2147209112
xmlSerializeError = c_int # enum
class _TimeZoneTransitionTime(Structure):
    pass
TimeZoneTransitionTime = _TimeZoneTransitionTime
class ITimeValue(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Time Value.'
    _iid_ = GUID('{4CE86E17-E819-4C72-BD98-E55AE59B0317}')
    _idlflags_ = ['oleautomation']
ITimeValue._methods_ = [
    COMMETHOD(['propget', helpstring(u'The time reference associated with the time value.')], HRESULT, 'TimeReference',
              ( ['retval', 'out'], POINTER(POINTER(ITimeReference)), 'TimeReference' )),
    COMMETHOD(['propputref', helpstring(u'The time reference associated with the time value.')], HRESULT, 'TimeReference',
              ( ['in'], POINTER(ITimeReference), 'TimeReference' )),
    COMMETHOD([helpstring(u'Projects this time value from its time reference, to a given time reference.')], HRESULT, 'Project',
              ( ['in'], POINTER(ITimeReference), 'TimeReference' )),
    COMMETHOD([helpstring(u'Projects this time value from its time reference, to UTC.')], HRESULT, 'ProjectToUTC'),
    COMMETHOD([helpstring(u'Projects this time value from UTC, to its time reference.')], HRESULT, 'ProjectFromUTC'),
]
################################################################
## code template for ITimeValue implementation
##class ITimeValue_Impl(object):
##    def Project(self, TimeReference):
##        u'Projects this time value from its time reference, to a given time reference.'
##        #return 
##
##    def ProjectFromUTC(self):
##        u'Projects this time value from UTC, to its time reference.'
##        #return 
##
##    def ProjectToUTC(self):
##        u'Projects this time value from its time reference, to UTC.'
##        #return 
##
##    def TimeReference(self, TimeReference):
##        u'The time reference associated with the time value.'
##        #return 
##

class IEnumRESTOperation(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'REST operation enumerator.'
    _iid_ = GUID('{DAF01FBE-A62E-4924-86B3-E257006A92ED}')
    _idlflags_ = ['oleautomation']
class IRESTOperation(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'REST operation metadata object.'
    _iid_ = GUID('{2853CA57-AE88-4B5D-ADA3-4CF6F938A0E0}')
    _idlflags_ = ['oleautomation']
IEnumRESTOperation._methods_ = [
    COMMETHOD([helpstring(u'Resets the enumerator')], HRESULT, 'Reset'),
    COMMETHOD([helpstring(u'Gets next item.')], HRESULT, 'Next',
              ( ['retval', 'out'], POINTER(POINTER(IRESTOperation)), 'ppOp' )),
]
################################################################
## code template for IEnumRESTOperation implementation
##class IEnumRESTOperation_Impl(object):
##    def Reset(self):
##        u'Resets the enumerator'
##        #return 
##
##    def Next(self):
##        u'Gets next item.'
##        #return ppOp
##

class IFileNames2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to retrieve subsets based on extension.'
    _iid_ = GUID('{1F1197E3-B3BB-4D9C-B530-923E39EFCE11}')
    _idlflags_ = ['oleautomation']
class IFileNames(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control an array of filenames.'
    _iid_ = GUID('{F6ED3377-94F5-11D1-9AB0-080009EC734B}')
    _idlflags_ = ['oleautomation']
IFileNames2._methods_ = [
    COMMETHOD([helpstring(u'Loads the collection with files from the specified path.')], HRESULT, 'LoadFromPath',
              ( ['in'], BSTR, 'Path' )),
    COMMETHOD([helpstring(u'Obtains a subset based on a delimited set of extensions.')], HRESULT, 'GetSubset',
              ( ['in'], BSTR, 'extSet' ),
              ( ['retval', 'out'], POINTER(POINTER(IFileNames)), 'ppFileNames' )),
    COMMETHOD([helpstring(u'Obtains a delimited set of extensions contained within the collection.')], HRESULT, 'GetContainedExtensions',
              ( ['retval', 'out'], POINTER(BSTR), 'extSet' )),
    COMMETHOD([helpstring(u'Advances the current postion to the specified file if it exists.')], HRESULT, 'Find',
              ( ['in'], BSTR, 'FileName' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pFound' )),
]
################################################################
## code template for IFileNames2 implementation
##class IFileNames2_Impl(object):
##    def Find(self, FileName):
##        u'Advances the current postion to the specified file if it exists.'
##        #return pFound
##
##    def GetSubset(self, extSet):
##        u'Obtains a subset based on a delimited set of extensions.'
##        #return ppFileNames
##
##    def LoadFromPath(self, Path):
##        u'Loads the collection with files from the specified path.'
##        #return 
##
##    def GetContainedExtensions(self):
##        u'Obtains a delimited set of extensions contained within the collection.'
##        #return extSet
##

class IProgressor(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that report progress.'
    _iid_ = GUID('{3141F2F1-38E2-11D1-8809-080009EC732A}')
    _idlflags_ = ['oleautomation']
class IStepProgressor(IProgressor):
    _case_insensitive_ = True
    u'Provides access to members that report progress in stepped increments.'
    _iid_ = GUID('{CCDAD2C7-8EBC-11D1-8732-0000F8751720}')
    _idlflags_ = ['oleautomation']
class ICheckProgressor(IStepProgressor):
    _case_insensitive_ = True
    u'Provides access to members that report progress in stepped increments with checkmarks.'
    _iid_ = GUID('{BDE22C32-1113-11D2-A272-080009B6F22B}')
    _idlflags_ = ['oleautomation']
IProgressor._methods_ = [
    COMMETHOD(['propput', helpstring(u'The message displayed by the progressor.')], HRESULT, 'Message',
              ( ['in'], BSTR, 'Message' )),
    COMMETHOD(['propget', helpstring(u'The message displayed by the progressor.')], HRESULT, 'Message',
              ( ['retval', 'out'], POINTER(BSTR), 'Message' )),
    COMMETHOD([helpstring(u'Shows the progressor.')], HRESULT, 'Show'),
    COMMETHOD([helpstring(u'Animates or steps the progressor.')], HRESULT, 'Step'),
    COMMETHOD([helpstring(u'Hides the progressor.')], HRESULT, 'Hide'),
]
################################################################
## code template for IProgressor implementation
##class IProgressor_Impl(object):
##    def _get(self):
##        u'The message displayed by the progressor.'
##        #return Message
##    def _set(self, Message):
##        u'The message displayed by the progressor.'
##    Message = property(_get, _set, doc = _set.__doc__)
##
##    def Hide(self):
##        u'Hides the progressor.'
##        #return 
##
##    def Step(self):
##        u'Animates or steps the progressor.'
##        #return 
##
##    def Show(self):
##        u'Shows the progressor.'
##        #return 
##

IStepProgressor._methods_ = [
    COMMETHOD(['propput', helpstring(u'The minimum range of the progression.')], HRESULT, 'MinRange',
              ( ['in'], c_int, 'MinRange' )),
    COMMETHOD(['propget', helpstring(u'The minimum range of the progression.')], HRESULT, 'MinRange',
              ( ['retval', 'out'], POINTER(c_int), 'MinRange' )),
    COMMETHOD(['propput', helpstring(u'The maximum range of the progression.')], HRESULT, 'MaxRange',
              ( ['in'], c_int, 'MaxRange' )),
    COMMETHOD(['propget', helpstring(u'The maximum range of the progression.')], HRESULT, 'MaxRange',
              ( ['retval', 'out'], POINTER(c_int), 'MaxRange' )),
    COMMETHOD(['propput', helpstring(u'The step increment of the progression.')], HRESULT, 'StepValue',
              ( ['in'], c_int, 'Step' )),
    COMMETHOD(['propget', helpstring(u'The step increment of the progression.')], HRESULT, 'StepValue',
              ( ['retval', 'out'], POINTER(c_int), 'Step' )),
    COMMETHOD(['propput', helpstring(u'The current position of the progression.')], HRESULT, 'Position',
              ( ['in'], c_int, 'Position' )),
    COMMETHOD(['propget', helpstring(u'The current position of the progression.')], HRESULT, 'Position',
              ( ['retval', 'out'], POINTER(c_int), 'Position' )),
    COMMETHOD([helpstring(u'Offsets the position of the progression.')], HRESULT, 'OffsetPosition',
              ( ['in'], c_int, 'offsetValue' ),
              ( ['retval', 'out'], POINTER(c_int), 'prevPos' )),
]
################################################################
## code template for IStepProgressor implementation
##class IStepProgressor_Impl(object):
##    def _get(self):
##        u'The step increment of the progression.'
##        #return Step
##    def _set(self, Step):
##        u'The step increment of the progression.'
##    StepValue = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The maximum range of the progression.'
##        #return MaxRange
##    def _set(self, MaxRange):
##        u'The maximum range of the progression.'
##    MaxRange = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The minimum range of the progression.'
##        #return MinRange
##    def _set(self, MinRange):
##        u'The minimum range of the progression.'
##    MinRange = property(_get, _set, doc = _set.__doc__)
##
##    def OffsetPosition(self, offsetValue):
##        u'Offsets the position of the progression.'
##        #return prevPos
##
##    def _get(self):
##        u'The current position of the progression.'
##        #return Position
##    def _set(self, Position):
##        u'The current position of the progression.'
##    Position = property(_get, _set, doc = _set.__doc__)
##

ICheckProgressor._methods_ = [
    COMMETHOD([helpstring(u'Adds a field that a checkmark can be added to.')], HRESULT, 'AddCheck',
              ( ['in'], c_int, 'index' ),
              ( ['in'], BSTR, 'msg' )),
    COMMETHOD([helpstring(u'Displays the checkmark.')], HRESULT, 'ShowCheck',
              ( ['in'], c_int, 'index' )),
    COMMETHOD([helpstring(u'Hides the checkmark.')], HRESULT, 'HideCheck',
              ( ['in'], c_int, 'index' )),
]
################################################################
## code template for ICheckProgressor implementation
##class ICheckProgressor_Impl(object):
##    def ShowCheck(self, index):
##        u'Displays the checkmark.'
##        #return 
##
##    def HideCheck(self, index):
##        u'Hides the checkmark.'
##        #return 
##
##    def AddCheck(self, index, msg):
##        u'Adds a field that a checkmark can be added to.'
##        #return 
##

class ITimeZoneRule(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Time Zone Rule.'
    _iid_ = GUID('{2CBFDCB1-C991-4F68-B5B1-919B1B1E6A25}')
    _idlflags_ = ['oleautomation']
ITimeZoneInfo._methods_ = [
    COMMETHOD(['propget', helpstring(u'Time zone Windows ID name.')], HRESULT, 'WindowsID',
              ( ['retval', 'out'], POINTER(BSTR), 'WindowsID' )),
    COMMETHOD(['propput', helpstring(u'Time zone Windows ID name.')], HRESULT, 'WindowsID',
              ( ['in'], BSTR, 'WindowsID' )),
    COMMETHOD(['propget', helpstring(u'Descriptive display name of the time zone.')], HRESULT, 'DisplayName',
              ( ['retval', 'out'], POINTER(BSTR), 'DisplayName' )),
    COMMETHOD(['propput', helpstring(u'Descriptive display name of the time zone.')], HRESULT, 'DisplayName',
              ( ['in'], BSTR, 'DisplayName' )),
    COMMETHOD(['propget', helpstring(u'Custom description for the time zone.')], HRESULT, 'CustomDescription',
              ( ['retval', 'out'], POINTER(BSTR), 'DisplayName' )),
    COMMETHOD(['propput', helpstring(u'Custom description for the time zone.')], HRESULT, 'CustomDescription',
              ( ['in'], BSTR, 'DisplayName' )),
    COMMETHOD(['propget', helpstring(u'The time zone name during daylight time.')], HRESULT, 'DaylightTimeName',
              ( ['retval', 'out'], POINTER(BSTR), 'DaylightTimeName' )),
    COMMETHOD(['propput', helpstring(u'The time zone name during daylight time.')], HRESULT, 'DaylightTimeName',
              ( ['in'], BSTR, 'DaylightTimeName' )),
    COMMETHOD(['propget', helpstring(u'The time zone name during standard time.')], HRESULT, 'StandardTimeName',
              ( ['retval', 'out'], POINTER(BSTR), 'StandardTimeName' )),
    COMMETHOD(['propput', helpstring(u'The time zone name during standard time.')], HRESULT, 'StandardTimeName',
              ( ['in'], BSTR, 'StandardTimeName' )),
    COMMETHOD(['propget', helpstring(u'The default time zone adjustment rule.')], HRESULT, 'DefaultRule',
              ( ['retval', 'out'], POINTER(POINTER(ITimeZoneRule)), 'defaultTimeZoneRule' )),
    COMMETHOD(['propput', helpstring(u'The default time zone adjustment rule.')], HRESULT, 'DefaultRule',
              ( ['in'], POINTER(ITimeZoneRule), 'defaultTimeZoneRule' )),
    COMMETHOD(['propget', helpstring(u'Number of dynamic adjustment rules for the time zone.')], HRESULT, 'DynamicRulesCount',
              ( ['retval', 'out'], POINTER(c_int), 'DynamicRulesCount' )),
    COMMETHOD(['propget', helpstring(u'The first dynamic adjustment rule year.')], HRESULT, 'FirstDynamicRuleYear',
              ( ['retval', 'out'], POINTER(c_int), 'FirstDynamicRuleYear' )),
    COMMETHOD(['propget', helpstring(u'The last dynamic adjustment rule year.')], HRESULT, 'LastDynamicRuleYear',
              ( ['retval', 'out'], POINTER(c_int), 'LastDynamicRuleYear' )),
    COMMETHOD(['propget', helpstring(u'The next dynamic adjustment rule year that cyclicly proceeds the given dynamic adjustment rule year.')], HRESULT, 'NextDynamicRuleYear',
              ( ['in'], c_int, 'currentDynamicRuleYear' ),
              ( ['retval', 'out'], POINTER(c_int), 'NextDynamicRuleYear' )),
    COMMETHOD(['propget', helpstring(u'The dynamic adjustment rule for a specific year.')], HRESULT, 'DynamicRule',
              ( ['in'], c_int, 'Year' ),
              ( ['retval', 'out'], POINTER(POINTER(ITimeZoneRule)), 'DynamicRule' )),
    COMMETHOD([helpstring(u'Adds a dynamic adjustment to the time zone.')], HRESULT, 'AddDynamicRule',
              ( ['in'], POINTER(ITimeZoneRule), 'DynamicRule' )),
]
################################################################
## code template for ITimeZoneInfo implementation
##class ITimeZoneInfo_Impl(object):
##    @property
##    def DynamicRulesCount(self):
##        u'Number of dynamic adjustment rules for the time zone.'
##        #return DynamicRulesCount
##
##    def _get(self):
##        u'Time zone Windows ID name.'
##        #return WindowsID
##    def _set(self, WindowsID):
##        u'Time zone Windows ID name.'
##    WindowsID = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Descriptive display name of the time zone.'
##        #return DisplayName
##    def _set(self, DisplayName):
##        u'Descriptive display name of the time zone.'
##    DisplayName = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def LastDynamicRuleYear(self):
##        u'The last dynamic adjustment rule year.'
##        #return LastDynamicRuleYear
##
##    @property
##    def NextDynamicRuleYear(self, currentDynamicRuleYear):
##        u'The next dynamic adjustment rule year that cyclicly proceeds the given dynamic adjustment rule year.'
##        #return NextDynamicRuleYear
##
##    @property
##    def FirstDynamicRuleYear(self):
##        u'The first dynamic adjustment rule year.'
##        #return FirstDynamicRuleYear
##
##    def AddDynamicRule(self, DynamicRule):
##        u'Adds a dynamic adjustment to the time zone.'
##        #return 
##
##    def _get(self):
##        u'The default time zone adjustment rule.'
##        #return defaultTimeZoneRule
##    def _set(self, defaultTimeZoneRule):
##        u'The default time zone adjustment rule.'
##    DefaultRule = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Custom description for the time zone.'
##        #return DisplayName
##    def _set(self, DisplayName):
##        u'Custom description for the time zone.'
##    CustomDescription = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The time zone name during standard time.'
##        #return StandardTimeName
##    def _set(self, StandardTimeName):
##        u'The time zone name during standard time.'
##    StandardTimeName = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def DynamicRule(self, Year):
##        u'The dynamic adjustment rule for a specific year.'
##        #return DynamicRule
##
##    def _get(self):
##        u'The time zone name during daylight time.'
##        #return DaylightTimeName
##    def _set(self, DaylightTimeName):
##        u'The time zone name during daylight time.'
##    DaylightTimeName = property(_get, _set, doc = _set.__doc__)
##

class IEnumNameEdit(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that create of an enumeration of Name objects.'
    _iid_ = GUID('{FDAFAD91-67FE-11D4-8155-00C04F686238}')
    _idlflags_ = ['oleautomation']
IEnumNameEdit._methods_ = [
    COMMETHOD([helpstring(u'Adds a Name in the list.')], HRESULT, 'Add',
              ( ['in'], POINTER(IName), 'Name' )),
    COMMETHOD([helpstring(u'Removes a Name from the list.')], HRESULT, 'Remove',
              ( ['in'], POINTER(IName), 'Name' )),
    COMMETHOD([helpstring(u'Removes current name from the list (when enumerating).')], HRESULT, 'RemoveCurrent'),
]
################################################################
## code template for IEnumNameEdit implementation
##class IEnumNameEdit_Impl(object):
##    def Add(self, Name):
##        u'Adds a Name in the list.'
##        #return 
##
##    def RemoveCurrent(self):
##        u'Removes current name from the list (when enumerating).'
##        #return 
##
##    def Remove(self, Name):
##        u'Removes a Name from the list.'
##        #return 
##

class DefinedInterval(CoClass):
    u'Defines a defined interval classification method.'
    _reg_clsid_ = GUID('{62144BE8-E05E-11D1-AAAE-00C04FA334B3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class IClassifyGEN(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control classification.'
    _iid_ = GUID('{CBA26148-CD2C-44AC-BBF5-B228B55A198D}')
    _idlflags_ = ['oleautomation']
DefinedInterval._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IClassifyGEN, IClassify, IClassifyMinMax, IClassifyMinMax2, IIntervalRange, IIntervalRange2]

class EqualInterval(CoClass):
    u'Defines an equal interval classification method.'
    _reg_clsid_ = GUID('{62144BE1-E05E-11D1-AAAE-00C04FA334B3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
EqualInterval._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IClassifyGEN, IClassify, IClassifyMinMax, IClassifyMinMax2]

class Quantile(CoClass):
    u'Defines a quantile classification method.'
    _reg_clsid_ = GUID('{62144BE9-E05E-11D1-AAAE-00C04FA334B3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
Quantile._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IClassifyGEN, IClassify]

class GeometricalInterval(CoClass):
    u'Defines a geometrical interval classification method.'
    _reg_clsid_ = GUID('{C79EB120-E98E-4AF9-903D-70273E0C140E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
GeometricalInterval._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IClassifyGEN, IClassify]

class NaturalBreaks(CoClass):
    u'Defines a natural breaks classification method.'
    _reg_clsid_ = GUID('{62144BEA-E05E-11D1-AAAE-00C04FA334B3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
NaturalBreaks._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IClassifyGEN, IClassify]

class IXMLWriter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the sequential writing of XML.'
    _iid_ = GUID('{5F50E520-1278-4C7A-937C-AE5874548431}')
    _idlflags_ = ['oleautomation']
class IXMLReader(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the sequential reading of XML.'
    _iid_ = GUID('{D405F844-8057-4DF4-B2DA-DF25DEDEBF4C}')
    _idlflags_ = ['oleautomation']
IXMLSerializer._methods_ = [
    COMMETHOD([helpstring(u'Writes an object as XML.')], HRESULT, 'WriteObject',
              ( ['in'], POINTER(IXMLWriter), 'pWriter' ),
              ( ['in'], POINTER(IPropertySet), 'environment' ),
              ( ['in'], POINTER(IXMLFlags), 'flags' ),
              ( ['in'], BSTR, 'elementName' ),
              ( ['in'], BSTR, 'elementNamespaceURI' ),
              ( ['in'], POINTER(IUnknown), 'obj' )),
    COMMETHOD([helpstring(u'Reads an object from XML.')], HRESULT, 'ReadObject',
              ( ['in'], POINTER(IXMLReader), 'pReader' ),
              ( ['in'], POINTER(IPropertySet), 'environment' ),
              ( ['in'], POINTER(IXMLFlags), 'flags' ),
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'obj' )),
    COMMETHOD([helpstring(u'Loads an object from an XML string.')], HRESULT, 'LoadFromString',
              ( ['in'], BSTR, 'XML' ),
              ( ['in'], POINTER(IPropertySet), 'environment' ),
              ( ['in'], POINTER(IXMLFlags), 'flags' ),
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'obj' )),
    COMMETHOD([helpstring(u'Saves an object to an XML string.')], HRESULT, 'SaveToString',
              ( ['in'], POINTER(IUnknown), 'obj' ),
              ( ['in'], POINTER(IPropertySet), 'environment' ),
              ( ['in'], POINTER(IXMLFlags), 'flags' ),
              ( ['retval', 'out'], POINTER(BSTR), 'XML' )),
    COMMETHOD([helpstring(u'Reads an object from XML given an XML type.')], HRESULT, 'ReadObjectByType',
              ( ['in'], POINTER(IXMLReader), 'pReader' ),
              ( ['in'], POINTER(IPropertySet), 'environment' ),
              ( ['in'], POINTER(IXMLFlags), 'flags' ),
              ( ['in'], BSTR, 'typeNamespace' ),
              ( ['in'], BSTR, 'TypeName' ),
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'obj' )),
]
################################################################
## code template for IXMLSerializer implementation
##class IXMLSerializer_Impl(object):
##    def SaveToString(self, obj, environment, flags):
##        u'Saves an object to an XML string.'
##        #return XML
##
##    def LoadFromString(self, XML, environment, flags):
##        u'Loads an object from an XML string.'
##        #return obj
##
##    def ReadObjectByType(self, pReader, environment, flags, typeNamespace, TypeName):
##        u'Reads an object from XML given an XML type.'
##        #return obj
##
##    def ReadObject(self, pReader, environment, flags):
##        u'Reads an object from XML.'
##        #return obj
##
##    def WriteObject(self, pWriter, environment, flags, elementName, elementNamespaceURI, obj):
##        u'Writes an object as XML.'
##        #return 
##

class StandardDeviation(CoClass):
    u'Defines a standard deviation classification method.'
    _reg_clsid_ = GUID('{DC6D8015-49C2-11D2-AAFF-00C04FA334B3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
StandardDeviation._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IClassifyGEN, IClassify, IDeviationInterval]

IEnumBSTR._methods_ = [
    COMMETHOD([helpstring(u'Obtains the next string in the list.')], HRESULT, 'Next',
              ( ['retval', 'out'], POINTER(BSTR), 'pBSTR' )),
    COMMETHOD([helpstring(u'Resets the string so the next returned string is the first.')], HRESULT, 'Reset'),
]
################################################################
## code template for IEnumBSTR implementation
##class IEnumBSTR_Impl(object):
##    def Reset(self):
##        u'Resets the string so the next returned string is the first.'
##        #return 
##
##    def Next(self):
##        u'Obtains the next string in the list.'
##        #return pBSTR
##

class ICustomNumberFormat(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that format numbers in a customizable way.'
    _iid_ = GUID('{7E4F4718-8E54-11D2-AAD8-000000000000}')
    _idlflags_ = ['oleautomation']
ICustomNumberFormat._methods_ = [
    COMMETHOD(['propput', helpstring(u'A user-defined format expression.')], HRESULT, 'FormatString',
              ( ['in'], BSTR, 'str' )),
    COMMETHOD(['propget', helpstring(u'A user-defined format expression.')], HRESULT, 'FormatString',
              ( ['retval', 'out'], POINTER(BSTR), 'str' )),
]
################################################################
## code template for ICustomNumberFormat implementation
##class ICustomNumberFormat_Impl(object):
##    def _get(self):
##        u'A user-defined format expression.'
##        #return str
##    def _set(self, str):
##        u'A user-defined format expression.'
##    FormatString = property(_get, _set, doc = _set.__doc__)
##


# values for enumeration 'esriLicenseServerEdition'
esriLicenseServerEditionBasic = 100
esriLicenseServerEditionStandard = 200
esriLicenseServerEditionAdvanced = 300
esriLicenseServerEdition = c_int # enum
IXMLSerializerAlt._methods_ = [
    COMMETHOD([helpstring(u'Loads an object from an XML string.')], HRESULT, 'LoadFromString',
              ( ['in'], BSTR, 'XML' ),
              ( ['in'], BSTR, 'TypeName' ),
              ( ['in'], BSTR, 'TypeNamespaceURI' ),
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'obj' )),
]
################################################################
## code template for IXMLSerializerAlt implementation
##class IXMLSerializerAlt_Impl(object):
##    def LoadFromString(self, XML, TypeName, TypeNamespaceURI):
##        u'Loads an object from an XML string.'
##        #return obj
##

class XMLReader(CoClass):
    u'An XML sequential document reader.'
    _reg_clsid_ = GUID('{B853965E-FD52-4ED2-80C2-F0E27A2C6E8A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class IXMLReader2(IXMLReader):
    _case_insensitive_ = True
    u'Provides access to members that control the sequential reading of XML.'
    _iid_ = GUID('{93C1AC3B-4520-450D-B005-95FD01B50C4A}')
    _idlflags_ = ['oleautomation']
XMLReader._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IXMLReader, IXMLReader2, ISupportErrorInfo]

class IEnumVariantSimple(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that enumerate over a set of VARIANTs.'
    _iid_ = GUID('{0F0A3D86-8690-4D41-9DF7-EFEFE99C4EC5}')
    _idlflags_ = ['oleautomation']
IEnumVariantSimple._methods_ = [
    COMMETHOD([helpstring(u'Obtains the next VARIANT in the set.')], HRESULT, 'Next',
              ( ['retval', 'out'], POINTER(VARIANT), 'nextVariant' )),
    COMMETHOD([helpstring(u'Resets the internal cursor back to the beginning of the set.')], HRESULT, 'Reset'),
]
################################################################
## code template for IEnumVariantSimple implementation
##class IEnumVariantSimple_Impl(object):
##    def Reset(self):
##        u'Resets the internal cursor back to the beginning of the set.'
##        #return 
##
##    def Next(self):
##        u'Obtains the next VARIANT in the set.'
##        #return nextVariant
##


# values for enumeration 'esriRoundingOptionEnum'
esriRoundNumberOfDecimals = 0
esriRoundNumberOfSignificantDigits = 1
esriRoundingOptionEnum = c_int # enum

# values for enumeration 'esriNumericAlignmentEnum'
esriAlignRight = 0
esriAlignLeft = 1
esriNumericAlignmentEnum = c_int # enum
class INumericFormat(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that format numbers.'
    _iid_ = GUID('{7E4F4710-8E54-11D2-AAD8-000000000000}')
    _idlflags_ = ['oleautomation']
INumericFormat._methods_ = [
    COMMETHOD(['propput', helpstring(u'The rounding option applied to the ValueToString method.')], HRESULT, 'RoundingOption',
              ( ['in'], esriRoundingOptionEnum, 'pption' )),
    COMMETHOD(['propget', helpstring(u'The rounding option applied to the ValueToString method.')], HRESULT, 'RoundingOption',
              ( ['retval', 'out'], POINTER(esriRoundingOptionEnum), 'pption' )),
    COMMETHOD(['propput', helpstring(u'The rounding value, whose meaning depends on the rounding option.')], HRESULT, 'RoundingValue',
              ( ['in'], c_int, 'Value' )),
    COMMETHOD(['propget', helpstring(u'The rounding value, whose meaning depends on the rounding option.')], HRESULT, 'RoundingValue',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD(['propput', helpstring(u'The alignment option applied to the ValueToString method.')], HRESULT, 'AlignmentOption',
              ( ['in'], esriNumericAlignmentEnum, 'option' )),
    COMMETHOD(['propget', helpstring(u'The alignment option applied to the ValueToString method.')], HRESULT, 'AlignmentOption',
              ( ['retval', 'out'], POINTER(esriNumericAlignmentEnum), 'option' )),
    COMMETHOD(['propput', helpstring(u'The alignment width applied to the ValueToString method.')], HRESULT, 'AlignmentWidth',
              ( ['in'], c_int, 'width' )),
    COMMETHOD(['propget', helpstring(u'The alignment width applied to the ValueToString method.')], HRESULT, 'AlignmentWidth',
              ( ['retval', 'out'], POINTER(c_int), 'width' )),
    COMMETHOD(['propput', helpstring(u'Indicates if formatted numbers contain digit grouping symbols.')], HRESULT, 'UseSeparator',
              ( ['in'], VARIANT_BOOL, 'sep' )),
    COMMETHOD(['propget', helpstring(u'Indicates if formatted numbers contain digit grouping symbols.')], HRESULT, 'UseSeparator',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'sep' )),
    COMMETHOD(['propput', helpstring(u'Indicates if formatted numbers contain padded zeros to the right of the decimal.')], HRESULT, 'ZeroPad',
              ( ['in'], VARIANT_BOOL, 'pad' )),
    COMMETHOD(['propget', helpstring(u'Indicates if formatted numbers contain padded zeros to the right of the decimal.')], HRESULT, 'ZeroPad',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pad' )),
    COMMETHOD(['propput', helpstring(u'Indicates if formatted numbers contain a plus sign for positive numbers.')], HRESULT, 'ShowPlusSign',
              ( ['in'], VARIANT_BOOL, 'Show' )),
    COMMETHOD(['propget', helpstring(u'Indicates if formatted numbers contain a plus sign for positive numbers.')], HRESULT, 'ShowPlusSign',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Show' )),
]
################################################################
## code template for INumericFormat implementation
##class INumericFormat_Impl(object):
##    def _get(self):
##        u'The alignment option applied to the ValueToString method.'
##        #return option
##    def _set(self, option):
##        u'The alignment option applied to the ValueToString method.'
##    AlignmentOption = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if formatted numbers contain a plus sign for positive numbers.'
##        #return Show
##    def _set(self, Show):
##        u'Indicates if formatted numbers contain a plus sign for positive numbers.'
##    ShowPlusSign = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The rounding value, whose meaning depends on the rounding option.'
##        #return Value
##    def _set(self, Value):
##        u'The rounding value, whose meaning depends on the rounding option.'
##    RoundingValue = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if formatted numbers contain padded zeros to the right of the decimal.'
##        #return pad
##    def _set(self, pad):
##        u'Indicates if formatted numbers contain padded zeros to the right of the decimal.'
##    ZeroPad = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The rounding option applied to the ValueToString method.'
##        #return pption
##    def _set(self, pption):
##        u'The rounding option applied to the ValueToString method.'
##    RoundingOption = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if formatted numbers contain digit grouping symbols.'
##        #return sep
##    def _set(self, sep):
##        u'Indicates if formatted numbers contain digit grouping symbols.'
##    UseSeparator = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The alignment width applied to the ValueToString method.'
##        #return width
##    def _set(self, width):
##        u'The alignment width applied to the ValueToString method.'
##    AlignmentWidth = property(_get, _set, doc = _set.__doc__)
##

class IPercentageFormat(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that format percentages.'
    _iid_ = GUID('{7E4F4711-8E54-11D2-AAD8-000000000000}')
    _idlflags_ = ['oleautomation']
IPercentageFormat._methods_ = [
    COMMETHOD(['propput', helpstring(u'Indicates if ValueToString agument is treated as a fraction or a percentage.')], HRESULT, 'AdjustPercentage',
              ( ['in'], VARIANT_BOOL, 'adjust' )),
    COMMETHOD(['propget', helpstring(u'Indicates if ValueToString agument is treated as a fraction or a percentage.')], HRESULT, 'AdjustPercentage',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'adjust' )),
]
################################################################
## code template for IPercentageFormat implementation
##class IPercentageFormat_Impl(object):
##    def _get(self):
##        u'Indicates if ValueToString agument is treated as a fraction or a percentage.'
##        #return adjust
##    def _set(self, adjust):
##        u'Indicates if ValueToString agument is treated as a fraction or a percentage.'
##    AdjustPercentage = property(_get, _set, doc = _set.__doc__)
##


# values for enumeration 'messageSupportError'
MESSAGESUPPORT_E_BAD_REQUEST = -2147220991
MESSAGESUPPORT_E_UNAUTHORIZED = -2147220990
MESSAGESUPPORT_E_FORBIDDEN = -2147220989
MESSAGESUPPORT_E_NOT_FOUND = -2147220988
MESSAGESUPPORT_E_METHOD_NOT_ALLOWED = -2147220987
MESSAGESUPPORT_E_PROXY_AUTHENTICATION_REQUIRED = -2147220986
MESSAGESUPPORT_E_REQUEST_TIMEOUT = -2147220985
MESSAGESUPPORT_E_INTERNAL_SERVER_ERROR = -2147220984
MESSAGESUPPORT_E_NOT_IMPLEMENTED = -2147220983
MESSAGESUPPORT_E_BAD_GATEWAY = -2147220982
MESSAGESUPPORT_E_SERVICE_NOT_AVAILABLE = -2147220981
MESSAGESUPPORT_E_UNSUPPORTED_PROTOCOL = -2147220980
MESSAGESUPPORT_E_URL_MALFORMAT = -2147220979
MESSAGESUPPORT_E_COULDNT_RESOLVE_PROXY = -2147220978
MESSAGESUPPORT_E_COULDNT_RESOLVE_HOST = -2147220977
MESSAGESUPPORT_E_COULDNT_CONNECT = -2147220976
MESSAGESUPPORT_E_REQUEST_TOLARGE = -2147220975
MESSAGESUPPORT_E_NO_CONTENT = -2147220974
MESSAGESUPPORT_E_SSL_CACERT = -2147220973
MESSAGESUPPORT_E_SSL_CONNECT_ERROR = -2147220972
MESSAGESUPPORT_E_SSL_PEER_CERTIFICATE = -2147220971
MESSAGESUPPORT_E_INVALID_GET_FILE = -2147220970
MESSAGESUPPORT_E_OPERATION_TIMEDOUT = -2147220969
MESSAGESUPPORT_E_MEM_ALLOC_FAILED = -2147220968
MESSAGESUPPORT_E_AUTH_TOKEN_FAILURE = -2147220967
MESSAGESUPPORT_E_AUTH_TOKEN_REQUIRED = -2147220966
MESSAGESUPPORT_E_GET_TOKEN_FAILED = -2147220965
MESSAGESUPPORT_E_PROXY_GATEWAY_ERROR = -2147220964
MESSAGESUPPORT_E_NOT_ACCEPTABLE = -2147220963
messageSupportError = c_int # enum
_WKSDateTime._fields_ = [
    ('Year', c_short),
    ('Month', c_short),
    ('Day', c_short),
    ('Hour', c_short),
    ('Minute', c_short),
    ('Second', c_short),
    ('Nanoseconds', c_int),
]
assert sizeof(_WKSDateTime) == 16, sizeof(_WKSDateTime)
assert alignment(_WKSDateTime) == 4, alignment(_WKSDateTime)
class IXMLObjectElement(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control writing objects to XML.'
    _iid_ = GUID('{77D57DDA-E1E3-459A-91D1-192126BC344A}')
    _idlflags_ = ['oleautomation']
IXMLObjectElement._methods_ = [
    COMMETHOD([helpstring(u'Writes the object to XML.')], HRESULT, 'WriteXML',
              ( ['in'], POINTER(IXMLWriter), 'pWriter' ),
              ( ['in'], POINTER(IPropertySet), 'environment' ),
              ( ['in'], POINTER(IXMLFlags), 'flags' ),
              ( ['in'], BSTR, 'elementName' ),
              ( ['in'], BSTR, 'elementNamespaceURI' )),
    COMMETHOD([helpstring(u'Reads the object from XML.')], HRESULT, 'ReadXML',
              ( ['in'], POINTER(IXMLReader), 'pReader' ),
              ( ['in'], POINTER(IPropertySet), 'environment' ),
              ( ['in'], POINTER(IXMLFlags), 'flags' )),
]
################################################################
## code template for IXMLObjectElement implementation
##class IXMLObjectElement_Impl(object):
##    def ReadXML(self, pReader, environment, flags):
##        u'Reads the object from XML.'
##        #return 
##
##    def WriteXML(self, pWriter, environment, flags, elementName, elementNamespaceURI):
##        u'Writes the object to XML.'
##        #return 
##

class JSONReader(CoClass):
    u'A sequential JSON Reader.'
    _reg_clsid_ = GUID('{B4578901-05DE-4BDA-AAEB-849EC52102B1}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
JSONReader._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IJSONReader, IJSONReader2, ISupportErrorInfo]

class IErrorCollection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control an Error Collection.'
    _iid_ = GUID('{66353C17-DF5D-11D3-9FA0-00C04F6BDF0C}')
    _idlflags_ = ['oleautomation']
IErrorCollection._methods_ = [
    COMMETHOD(['propget', helpstring(u'The count of error records.')], HRESULT, 'ErrorCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'The description of the specified error record.')], HRESULT, 'ErrorDescription',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Description' )),
]
################################################################
## code template for IErrorCollection implementation
##class IErrorCollection_Impl(object):
##    @property
##    def ErrorDescription(self, index):
##        u'The description of the specified error record.'
##        #return Description
##
##    @property
##    def ErrorCount(self):
##        u'The count of error records.'
##        #return Count
##

ISet._methods_ = [
    COMMETHOD([helpstring(u'Adds an object to the set.')], HRESULT, 'Add',
              ( ['in'], POINTER(IUnknown), 'unk' )),
    COMMETHOD([helpstring(u'Removes the object from the set.')], HRESULT, 'Remove',
              ( ['in'], POINTER(IUnknown), 'unk' )),
    COMMETHOD([helpstring(u'Removes all objects from the set.')], HRESULT, 'RemoveAll'),
    COMMETHOD([helpstring(u'Searches for the object in the set.')], HRESULT, 'Find',
              ( ['in'], POINTER(IUnknown), 'unk' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'found' )),
    COMMETHOD([helpstring(u'Obtains the next object in the set.')], HRESULT, 'Next',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'unk' )),
    COMMETHOD([helpstring(u'Resets the set for enumerating through the objects with Next.')], HRESULT, 'Reset'),
    COMMETHOD(['propget', helpstring(u'The element count of the set.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
]
################################################################
## code template for ISet implementation
##class ISet_Impl(object):
##    def Reset(self):
##        u'Resets the set for enumerating through the objects with Next.'
##        #return 
##
##    @property
##    def Count(self):
##        u'The element count of the set.'
##        #return Count
##
##    def Remove(self, unk):
##        u'Removes the object from the set.'
##        #return 
##
##    def Next(self):
##        u'Obtains the next object in the set.'
##        #return unk
##
##    def RemoveAll(self):
##        u'Removes all objects from the set.'
##        #return 
##
##    def Add(self, unk):
##        u'Adds an object to the set.'
##        #return 
##
##    def Find(self, unk):
##        u'Searches for the object in the set.'
##        #return found
##

class IAnimationProgressor(IProgressor):
    _case_insensitive_ = True
    u'Provides access to members that report progress using an animation.'
    _iid_ = GUID('{80CB7E35-85E4-11D1-872C-0000F8751720}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriAnimations'
esriAnimationDrawing = 0
esriAnimationPrinting = 1
esriAnimationOther = 2
esriAnimationLast = 3
esriAnimations = c_int # enum
IAnimationProgressor._methods_ = [
    COMMETHOD(['propput', helpstring(u'The animation displayed by the progressor as one of the esriAnimation constants. (Not implemented).')], HRESULT, 'Animation',
              ( ['in'], esriAnimations, 'Animation' )),
    COMMETHOD(['propget', helpstring(u'The animation displayed by the progressor as one of the esriAnimation constants. (Not implemented).')], HRESULT, 'Animation',
              ( ['retval', 'out'], POINTER(esriAnimations), 'Animation' )),
    COMMETHOD([helpstring(u'Opens the AVI file specified in the path and displays its first frame. The AVI file specified must not contain audio.')], HRESULT, 'OpenPath',
              ( ['in'], BSTR, 'animationPath' )),
    COMMETHOD([helpstring(u'Plays the animation.')], HRESULT, 'Play',
              ( ['in', 'optional'], c_int, 'frameFrom', 0 ),
              ( ['in', 'optional'], c_int, 'frameTo', -1 ),
              ( ['in', 'optional'], c_int, 'repeat', -1 )),
    COMMETHOD([helpstring(u'Moves to the specified frame of the animation. The animation starts at this frame the next time it is played.')], HRESULT, 'Seek',
              ( ['in'], c_int, 'frameTo' )),
    COMMETHOD([helpstring(u'Stops the animation.')], HRESULT, 'Stop'),
]
################################################################
## code template for IAnimationProgressor implementation
##class IAnimationProgressor_Impl(object):
##    def Stop(self):
##        u'Stops the animation.'
##        #return 
##
##    def Play(self, frameFrom, frameTo, repeat):
##        u'Plays the animation.'
##        #return 
##
##    def _get(self):
##        u'The animation displayed by the progressor as one of the esriAnimation constants. (Not implemented).'
##        #return Animation
##    def _set(self, Animation):
##        u'The animation displayed by the progressor as one of the esriAnimation constants. (Not implemented).'
##    Animation = property(_get, _set, doc = _set.__doc__)
##
##    def Seek(self, frameTo):
##        u'Moves to the specified frame of the animation. The animation starts at this frame the next time it is played.'
##        #return 
##
##    def OpenPath(self, animationPath):
##        u'Opens the AVI file specified in the path and displays its first frame. The AVI file specified must not contain audio.'
##        #return 
##


# values for enumeration 'esriTimeUnits'
esriTimeUnitsUnknown = 0
esriTimeUnitsMilliseconds = 1
esriTimeUnitsSeconds = 2
esriTimeUnitsMinutes = 3
esriTimeUnitsHours = 4
esriTimeUnitsDays = 5
esriTimeUnitsWeeks = 6
esriTimeUnitsMonths = 7
esriTimeUnitsYears = 8
esriTimeUnitsDecades = 9
esriTimeUnitsCenturies = 10
esriTimeUnits = c_int # enum
class IXMLStream(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control an in-memory XML stream.'
    _iid_ = GUID('{498A5F91-65D1-4A25-AD2B-462E7DF8B358}')
    _idlflags_ = ['oleautomation']
IXMLStream._methods_ = [
    COMMETHOD([helpstring(u'Loads from a string.')], HRESULT, 'LoadFromString',
              ( ['in'], BSTR, 'XML' )),
    COMMETHOD([helpstring(u'Loads from a file path.')], HRESULT, 'LoadFromFile',
              ( ['in'], BSTR, 'filePath' )),
    COMMETHOD([helpstring(u'Loads from a UTF-8 byte array.')], HRESULT, 'LoadFromBytes',
              ( ['in'], POINTER(_midlSAFEARRAY(c_ubyte)), 'bytes' )),
    COMMETHOD([helpstring(u'Saves to a string.')], HRESULT, 'SaveToString',
              ( ['retval', 'out'], POINTER(BSTR), 'XML' )),
    COMMETHOD([helpstring(u'Saves to a file path.')], HRESULT, 'SaveToFile',
              ( ['in'], BSTR, 'filePath' )),
    COMMETHOD([helpstring(u'Saves to a UTF-8 byte array.')], HRESULT, 'SaveToBytes',
              ( ['retval', 'out'], POINTER(_midlSAFEARRAY(c_ubyte)), 'bytes' )),
    COMMETHOD([helpstring(u'Resets the stream to the beginning.')], HRESULT, 'Reset'),
]
################################################################
## code template for IXMLStream implementation
##class IXMLStream_Impl(object):
##    def Reset(self):
##        u'Resets the stream to the beginning.'
##        #return 
##
##    def SaveToFile(self, filePath):
##        u'Saves to a file path.'
##        #return 
##
##    def LoadFromFile(self, filePath):
##        u'Loads from a file path.'
##        #return 
##
##    def SaveToBytes(self):
##        u'Saves to a UTF-8 byte array.'
##        #return bytes
##
##    def LoadFromBytes(self, bytes):
##        u'Loads from a UTF-8 byte array.'
##        #return 
##
##    def SaveToString(self):
##        u'Saves to a string.'
##        #return XML
##
##    def LoadFromString(self, XML):
##        u'Loads from a string.'
##        #return 
##

class IEnumName(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that enumerate over a set of name objects.'
    _iid_ = GUID('{EF237A51-CB69-11D2-9F26-00C04F6BC69E}')
    _idlflags_ = ['oleautomation']
IEnumName._methods_ = [
    COMMETHOD([helpstring(u'Obtains the next Name in the list.')], HRESULT, 'Next',
              ( ['retval', 'out'], POINTER(POINTER(IName)), 'Name' )),
    COMMETHOD([helpstring(u'Resets the current position to the beginning.')], HRESULT, 'Reset'),
]
################################################################
## code template for IEnumName implementation
##class IEnumName_Impl(object):
##    def Reset(self):
##        u'Resets the current position to the beginning.'
##        #return 
##
##    def Next(self):
##        u'Obtains the next Name in the list.'
##        #return Name
##

class IFractionFormat(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that format fractions.'
    _iid_ = GUID('{7E4F4713-8E54-11D2-AAD8-000000000000}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'esriFractionOptionEnum'
esriSpecifyFractionDigits = 0
esriSpecifyFractionDenominator = 1
esriFractionOptionEnum = c_int # enum
IFractionFormat._methods_ = [
    COMMETHOD(['propput', helpstring(u'The fraction option determines how the numerator and denominator of the fraction are treated.')], HRESULT, 'FractionOption',
              ( ['in'], esriFractionOptionEnum, 'option' )),
    COMMETHOD(['propget', helpstring(u'The fraction option determines how the numerator and denominator of the fraction are treated.')], HRESULT, 'FractionOption',
              ( ['retval', 'out'], POINTER(esriFractionOptionEnum), 'option' )),
    COMMETHOD(['propput', helpstring(u'The maximum number of digits for the numerator or denominator, or the denominator of the formatted fraction.')], HRESULT, 'FractionFactor',
              ( ['in'], c_int, 'factor' )),
    COMMETHOD(['propget', helpstring(u'The maximum number of digits for the numerator or denominator, or the denominator of the formatted fraction.')], HRESULT, 'FractionFactor',
              ( ['retval', 'out'], POINTER(c_int), 'factor' )),
]
################################################################
## code template for IFractionFormat implementation
##class IFractionFormat_Impl(object):
##    def _get(self):
##        u'The maximum number of digits for the numerator or denominator, or the denominator of the formatted fraction.'
##        #return factor
##    def _set(self, factor):
##        u'The maximum number of digits for the numerator or denominator, or the denominator of the formatted fraction.'
##    FractionFactor = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The fraction option determines how the numerator and denominator of the fraction are treated.'
##        #return option
##    def _set(self, option):
##        u'The fraction option determines how the numerator and denominator of the fraction are treated.'
##    FractionOption = property(_get, _set, doc = _set.__doc__)
##

class IStatusBar(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that define the application statusbar.'
    _iid_ = GUID('{828100C1-CC80-11D0-8380-080009B996CC}')
    _idlflags_ = ['oleautomation']
IStatusBar._methods_ = [
    COMMETHOD(['propput', helpstring(u'The message displayed by one of the status bar panes.')], HRESULT, 'Message',
              ( ['in'], c_int, 'pane' ),
              ( ['in'], BSTR, 'Message' )),
    COMMETHOD(['propget', helpstring(u'The message displayed by one of the status bar panes.')], HRESULT, 'Message',
              ( ['in'], c_int, 'pane' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Message' )),
    COMMETHOD(['propput', helpstring(u'Indicates which standard panes are shown by the status bar. Use a combination of esriStatusBarPanes constants.')], HRESULT, 'Panes',
              ( ['in'], c_int, 'Panes' )),
    COMMETHOD(['propget', helpstring(u'Indicates which standard panes are shown by the status bar. Use a combination of esriStatusBarPanes constants.')], HRESULT, 'Panes',
              ( ['retval', 'out'], POINTER(c_int), 'Panes' )),
    COMMETHOD(['propget', helpstring(u'The progress bar object on the statusbar.')], HRESULT, 'ProgressBar',
              ( ['retval', 'out'], POINTER(POINTER(IStepProgressor)), 'ProgressBar' )),
    COMMETHOD(['propget', helpstring(u'The progress animation object on the statusbar.')], HRESULT, 'ProgressAnimation',
              ( ['retval', 'out'], POINTER(POINTER(IAnimationProgressor)), 'ProgressAnimation' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the statusbar is visible.')], HRESULT, 'Visible',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Visible' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the statusbar is visible.')], HRESULT, 'Visible',
              ( ['in'], VARIANT_BOOL, 'Visible' )),
    COMMETHOD([helpstring(u'Makes the progress bar visible.')], HRESULT, 'ShowProgressBar',
              ( ['in'], BSTR, 'Message' ),
              ( ['in'], c_int, 'min' ),
              ( ['in'], c_int, 'max' ),
              ( ['in'], c_int, 'Step' ),
              ( ['in'], VARIANT_BOOL, 'onePanel' )),
    COMMETHOD([helpstring(u'Steps the progress bar to the next position.')], HRESULT, 'StepProgressBar'),
    COMMETHOD([helpstring(u'Hides the progress bar.')], HRESULT, 'HideProgressBar'),
    COMMETHOD([helpstring(u'Makes the progress animation visible.')], HRESULT, 'ShowProgressAnimation',
              ( ['in'], BSTR, 'Message' ),
              ( ['in'], BSTR, 'animationPath' )),
    COMMETHOD([helpstring(u'Plays the progress animation if the parameter is true; otherwise stops it.')], HRESULT, 'PlayProgressAnimation',
              ( ['in'], VARIANT_BOOL, 'playAnim' )),
    COMMETHOD([helpstring(u'Hides the progress animation.')], HRESULT, 'HideProgressAnimation'),
]
################################################################
## code template for IStatusBar implementation
##class IStatusBar_Impl(object):
##    def _get(self):
##        u'Indicates which standard panes are shown by the status bar. Use a combination of esriStatusBarPanes constants.'
##        #return Panes
##    def _set(self, Panes):
##        u'Indicates which standard panes are shown by the status bar. Use a combination of esriStatusBarPanes constants.'
##    Panes = property(_get, _set, doc = _set.__doc__)
##
##    def HideProgressBar(self):
##        u'Hides the progress bar.'
##        #return 
##
##    def ShowProgressBar(self, Message, min, max, Step, onePanel):
##        u'Makes the progress bar visible.'
##        #return 
##
##    @property
##    def ProgressBar(self):
##        u'The progress bar object on the statusbar.'
##        #return ProgressBar
##
##    def _get(self):
##        u'Indicates if the statusbar is visible.'
##        #return Visible
##    def _set(self, Visible):
##        u'Indicates if the statusbar is visible.'
##    Visible = property(_get, _set, doc = _set.__doc__)
##
##    def PlayProgressAnimation(self, playAnim):
##        u'Plays the progress animation if the parameter is true; otherwise stops it.'
##        #return 
##
##    def ShowProgressAnimation(self, Message, animationPath):
##        u'Makes the progress animation visible.'
##        #return 
##
##    @property
##    def ProgressAnimation(self):
##        u'The progress animation object on the statusbar.'
##        #return ProgressAnimation
##
##    def StepProgressBar(self):
##        u'Steps the progress bar to the next position.'
##        #return 
##
##    def _get(self, pane):
##        u'The message displayed by one of the status bar panes.'
##        #return Message
##    def _set(self, pane, Message):
##        u'The message displayed by one of the status bar panes.'
##    Message = property(_get, _set, doc = _set.__doc__)
##
##    def HideProgressAnimation(self):
##        u'Hides the progress animation.'
##        #return 
##

class IXMLAttributes(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control XML attributes.'
    _iid_ = GUID('{3E23A49E-9F66-42D5-9982-5E3E5C0821E0}')
    _idlflags_ = ['oleautomation']
IXMLAttributes._methods_ = [
    COMMETHOD([helpstring(u'Adds an attribute to the element.')], HRESULT, 'AddAttribute',
              ( ['in'], BSTR, 'LocalName' ),
              ( ['in'], BSTR, 'NamespaceURI' ),
              ( ['in'], BSTR, 'Value' )),
    COMMETHOD([helpstring(u'Deletes an attribute from the element.')], HRESULT, 'DeleteAttribute',
              ( ['in'], BSTR, 'LocalName' ),
              ( ['in'], BSTR, 'NamespaceURI' )),
    COMMETHOD([helpstring(u'Finds an attribute by name and namespace.')], HRESULT, 'FindAttribute',
              ( ['in'], BSTR, 'LocalName' ),
              ( ['in'], BSTR, 'NamespaceURI' ),
              ( ['retval', 'out'], POINTER(c_int), 'index' )),
    COMMETHOD(['propget', helpstring(u'Number of attributes.')], HRESULT, 'AttributeCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Name of the attribute.')], HRESULT, 'LocalName',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'Namespace of the attribute.')], HRESULT, 'NamespaceURI',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'uri' )),
    COMMETHOD(['propget', helpstring(u'Value of the attribute.')], HRESULT, 'Value',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
]
################################################################
## code template for IXMLAttributes implementation
##class IXMLAttributes_Impl(object):
##    def DeleteAttribute(self, LocalName, NamespaceURI):
##        u'Deletes an attribute from the element.'
##        #return 
##
##    def FindAttribute(self, LocalName, NamespaceURI):
##        u'Finds an attribute by name and namespace.'
##        #return index
##
##    @property
##    def AttributeCount(self):
##        u'Number of attributes.'
##        #return Count
##
##    @property
##    def Value(self, index):
##        u'Value of the attribute.'
##        #return Value
##
##    def AddAttribute(self, LocalName, NamespaceURI, Value):
##        u'Adds an attribute to the element.'
##        #return 
##
##    @property
##    def NamespaceURI(self, index):
##        u'Namespace of the attribute.'
##        #return uri
##
##    @property
##    def LocalName(self, index):
##        u'Name of the attribute.'
##        #return Name
##

class XMLStream(CoClass):
    u'An in-memory XML stream.'
    _reg_clsid_ = GUID('{DB2CDE6F-A264-4129-A4CE-99F9A47F1830}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
XMLStream._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IXMLStream, IStream]

IPropertySet._methods_ = [
    COMMETHOD(['propget', helpstring(u'The number of properties contained in the property set.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD([helpstring(u'The value of the specified property.')], HRESULT, 'GetProperty',
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'Value' )),
    COMMETHOD([helpstring(u'The values of the specified properties.')], HRESULT, 'GetProperties',
              ( ['in'], VARIANT, 'names' ),
              ( ['out'], POINTER(VARIANT), 'values' )),
    COMMETHOD([helpstring(u'The name and value of all the properties in the property set.')], HRESULT, 'GetAllProperties',
              ( ['out'], POINTER(VARIANT), 'names' ),
              ( ['out'], POINTER(VARIANT), 'values' )),
    COMMETHOD([helpstring(u'The value of the specified property.')], HRESULT, 'SetProperty',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], VARIANT, 'Value' )),
    COMMETHOD([helpstring(u'The values of the specified properties.')], HRESULT, 'SetProperties',
              ( ['in'], VARIANT, 'names' ),
              ( ['in'], VARIANT, 'values' )),
    COMMETHOD([helpstring(u'True if the property set is the same as the input property set.')], HRESULT, 'IsEqual',
              ( ['in'], POINTER(IPropertySet), 'PropertySet' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsEqual' )),
    COMMETHOD([helpstring(u'Removes a property from the set.')], HRESULT, 'RemoveProperty',
              ( ['in'], BSTR, 'Name' )),
]
################################################################
## code template for IPropertySet implementation
##class IPropertySet_Impl(object):
##    @property
##    def Count(self):
##        u'The number of properties contained in the property set.'
##        #return Count
##
##    def GetProperty(self, Name):
##        u'The value of the specified property.'
##        #return Value
##
##    def RemoveProperty(self, Name):
##        u'Removes a property from the set.'
##        #return 
##
##    def GetProperties(self, names):
##        u'The values of the specified properties.'
##        #return values
##
##    def IsEqual(self, PropertySet):
##        u'True if the property set is the same as the input property set.'
##        #return IsEqual
##
##    def SetProperty(self, Name, Value):
##        u'The value of the specified property.'
##        #return 
##
##    def GetAllProperties(self):
##        u'The name and value of all the properties in the property set.'
##        #return names, values
##
##    def SetProperties(self, names, values):
##        u'The values of the specified properties.'
##        #return 
##

INameFactory._methods_ = [
    COMMETHOD([helpstring(u'Finds the correct name-string parser for the given name string, and uses it to create a new Name object.')], HRESULT, 'Create',
              ( ['in'], BSTR, 'NameString' ),
              ( ['retval', 'out'], POINTER(POINTER(IName)), 'Name' )),
    COMMETHOD([helpstring(u'Packages the set of names into a VARIANT (typically for initiating a drag operation).')], HRESULT, 'PackageNames',
              ( ['in'], POINTER(IEnumName), 'names' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'bytesArray' )),
    COMMETHOD([helpstring(u'Unpackages the given VARIANT into a set of Name objects (typically for responding to a drop operation).')], HRESULT, 'UnpackageNames',
              ( ['in'], POINTER(VARIANT), 'bytesArray' ),
              ( ['retval', 'out'], POINTER(POINTER(IEnumName)), 'names' )),
]
################################################################
## code template for INameFactory implementation
##class INameFactory_Impl(object):
##    def Create(self, NameString):
##        u'Finds the correct name-string parser for the given name string, and uses it to create a new Name object.'
##        #return Name
##
##    def PackageNames(self, names):
##        u'Packages the set of names into a VARIANT (typically for initiating a drag operation).'
##        #return bytesArray
##
##    def UnpackageNames(self, bytesArray):
##        u'Unpackages the given VARIANT into a set of Name objects (typically for responding to a drop operation).'
##        #return names
##

class XMLWriter(CoClass):
    u'An XML sequential document writer.'
    _reg_clsid_ = GUID('{105A5345-85F8-4B27-A1D2-5D2262C6D27E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class IXMLWriter2(IXMLWriter):
    _case_insensitive_ = True
    u'Provides access to members that control the sequential writing of XML.'
    _iid_ = GUID('{034900A2-4DB4-4074-8A7B-3A0885B844A2}')
    _idlflags_ = ['oleautomation']
XMLWriter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IXMLWriter, IXMLWriter2, ISupportErrorInfo]

class IRequestHandler(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control handing of request messages.'
    _iid_ = GUID('{46A0E2EA-3B64-4A46-BD78-88A1660F35BB}')
    _idlflags_ = ['oleautomation']
IRequestHandler._methods_ = [
    COMMETHOD([helpstring(u'Handles a binary request.')], HRESULT, 'HandleBinaryRequest',
              ( ['in'], POINTER(_midlSAFEARRAY(c_ubyte)), 'request' ),
              ( ['retval', 'out'], POINTER(_midlSAFEARRAY(c_ubyte)), 'response' )),
    COMMETHOD([helpstring(u'Handles a SOAP string request.')], HRESULT, 'HandleStringRequest',
              ( ['in'], BSTR, 'Capabilities' ),
              ( ['in'], BSTR, 'request' ),
              ( ['retval', 'out'], POINTER(BSTR), 'response' )),
]
################################################################
## code template for IRequestHandler implementation
##class IRequestHandler_Impl(object):
##    def HandleBinaryRequest(self, request):
##        u'Handles a binary request.'
##        #return response
##
##    def HandleStringRequest(self, Capabilities, request):
##        u'Handles a SOAP string request.'
##        #return response
##

class XMLAttributes(CoClass):
    u'A collection of XML element attributes.'
    _reg_clsid_ = GUID('{176EDC78-13AD-474C-9F42-083D86FFBA33}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
XMLAttributes._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IXMLAttributes]

class XMLNamespaces(CoClass):
    u'A collection of XML namespace declarations.'
    _reg_clsid_ = GUID('{95547DD2-8871-498B-918B-CF10EAF50F63}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class IXMLNamespaces(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control XML namespaces.'
    _iid_ = GUID('{032B72DC-E0FB-4BB1-8626-1797E25A72A0}')
    _idlflags_ = ['oleautomation']
XMLNamespaces._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IXMLNamespaces]

class ILatLonFormat(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that format Latitudes and Longitudes.'
    _iid_ = GUID('{7E4F4714-8E54-11D2-AAD8-000000000000}')
    _idlflags_ = ['oleautomation']
ILatLonFormat._methods_ = [
    COMMETHOD(['propput', helpstring(u'Indicates if a directional letter (N-S-E-W) is appended to the formatted number.')], HRESULT, 'ShowDirections',
              ( ['in'], VARIANT_BOOL, 'Show' )),
    COMMETHOD(['propget', helpstring(u'Indicates if a directional letter (N-S-E-W) is appended to the formatted number.')], HRESULT, 'ShowDirections',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Show' )),
    COMMETHOD(['propput', helpstring(u'Indicates if a formatted number is a latitude or not.')], HRESULT, 'IsLatitude',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD([helpstring(u'Obtains the degrees, minutes, and seconds for a lat/lon number.')], HRESULT, 'GetDMS',
              ( ['in'], c_double, 'Value' ),
              ( ['out'], POINTER(c_int), 'degrees' ),
              ( ['out'], POINTER(c_int), 'Minutes' ),
              ( ['out'], POINTER(c_double), 'Seconds' )),
    COMMETHOD(['propput', helpstring(u'Indicates if zero minutes are included in formatted output.')], HRESULT, 'ShowZeroMinutes',
              ( ['in'], VARIANT_BOOL, 'Show' )),
    COMMETHOD(['propget', helpstring(u'Indicates if zero minutes are included in formatted output.')], HRESULT, 'ShowZeroMinutes',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Show' )),
    COMMETHOD(['propput', helpstring(u'Indicates if zero seconds are included in formatted output.')], HRESULT, 'ShowZeroSeconds',
              ( ['in'], VARIANT_BOOL, 'Show' )),
    COMMETHOD(['propget', helpstring(u'Indicates if zero seconds are included in formatted output.')], HRESULT, 'ShowZeroSeconds',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Show' )),
]
################################################################
## code template for ILatLonFormat implementation
##class ILatLonFormat_Impl(object):
##    def _set(self, rhs):
##        u'Indicates if a formatted number is a latitude or not.'
##    IsLatitude = property(fset = _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if a directional letter (N-S-E-W) is appended to the formatted number.'
##        #return Show
##    def _set(self, Show):
##        u'Indicates if a directional letter (N-S-E-W) is appended to the formatted number.'
##    ShowDirections = property(_get, _set, doc = _set.__doc__)
##
##    def GetDMS(self, Value):
##        u'Obtains the degrees, minutes, and seconds for a lat/lon number.'
##        #return degrees, Minutes, Seconds
##
##    def _get(self):
##        u'Indicates if zero seconds are included in formatted output.'
##        #return Show
##    def _set(self, Show):
##        u'Indicates if zero seconds are included in formatted output.'
##    ShowZeroSeconds = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if zero minutes are included in formatted output.'
##        #return Show
##    def _set(self, Show):
##        u'Indicates if zero minutes are included in formatted output.'
##    ShowZeroMinutes = property(_get, _set, doc = _set.__doc__)
##

class XMLTypeMapper(CoClass):
    u'A type converter for XML and native types.'
    _reg_clsid_ = GUID('{DCB0F748-2D17-40B5-90C2-7D0B39660405}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
XMLTypeMapper._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IXMLTypeMapper, IXMLTypeMapper2, ISupportErrorInfo]

class IObjectValidate(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods for validating an object.'
    _iid_ = GUID('{55446BEB-10CA-40A4-9F40-261CA4A7F35A}')
    _idlflags_ = ['oleautomation']
IObjectValidate._methods_ = [
    COMMETHOD([helpstring(u'Validates an object.')], HRESULT, 'Validate',
              ( ['in'], POINTER(IPropertySet), 'props' )),
]
################################################################
## code template for IObjectValidate implementation
##class IObjectValidate_Impl(object):
##    def Validate(self, props):
##        u'Validates an object.'
##        #return 
##

IXMLReader._methods_ = [
    COMMETHOD([helpstring(u'Specifies the input XML stream.')], HRESULT, 'ReadFrom',
              ( ['in'], POINTER(IStream), 'inputStream' )),
    COMMETHOD(['propget', helpstring(u'Local name of current element.')], HRESULT, 'LocalName',
              ( ['retval', 'out'], POINTER(BSTR), 'LocalName' )),
    COMMETHOD(['propget', helpstring(u'Namespace URI of current element.')], HRESULT, 'NamespaceURI',
              ( ['retval', 'out'], POINTER(BSTR), 'uri' )),
    COMMETHOD(['propget', helpstring(u'Namespace prefix of current element.')], HRESULT, 'NamespacePrefix',
              ( ['retval', 'out'], POINTER(BSTR), 'Prefix' )),
    COMMETHOD(['propget', helpstring(u'Namespace declarations of current element.')], HRESULT, 'NamespaceDeclarations',
              ( ['retval', 'out'], POINTER(POINTER(IXMLNamespaces)), 'namespaces' )),
    COMMETHOD(['propget', helpstring(u'Attributes of current element.')], HRESULT, 'Attributes',
              ( ['retval', 'out'], POINTER(POINTER(IXMLAttributes)), 'Attributes' )),
    COMMETHOD(['propget', helpstring(u'Text value of current element.')], HRESULT, 'Text',
              ( ['retval', 'out'], POINTER(BSTR), 'Text' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the current element has child elements.')], HRESULT, 'HasElementChildren',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'hasChildren' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the current element is the last child element of its parent.')], HRESULT, 'IsLastChild',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'isLast' )),
    COMMETHOD([helpstring(u'Moves position to next element.')], HRESULT, 'NextElement'),
    COMMETHOD([helpstring(u'Moves position to first child element.')], HRESULT, 'OpenElement'),
    COMMETHOD([helpstring(u'Moves position to parent element.')], HRESULT, 'CloseElement'),
    COMMETHOD([helpstring(u'Obtains the prefix for a declared URI.')], HRESULT, 'LookupPrefix',
              ( ['in'], BSTR, 'Prefix' ),
              ( ['retval', 'out'], POINTER(BSTR), 'uri' )),
    COMMETHOD([helpstring(u'Reads the current element value as a boolean.')], HRESULT, 'ReadBoolean',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([helpstring(u'Reads the current element value as a byte.')], HRESULT, 'ReadByte',
              ( ['retval', 'out'], POINTER(c_ubyte), 'Value' )),
    COMMETHOD([helpstring(u'Reads the current element value as a short.')], HRESULT, 'ReadShort',
              ( ['retval', 'out'], POINTER(c_short), 'Value' )),
    COMMETHOD([helpstring(u'Reads the current element value as a long.')], HRESULT, 'ReadInteger',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([helpstring(u'Reads the current element value as a float.')], HRESULT, 'ReadFloat',
              ( ['retval', 'out'], POINTER(c_float), 'Value' )),
    COMMETHOD([helpstring(u'Reads the current element value as a double.')], HRESULT, 'ReadDouble',
              ( ['retval', 'out'], POINTER(c_double), 'Value' )),
    COMMETHOD([helpstring(u'Reads the current element value as a date.')], HRESULT, 'ReadDate',
              ( ['retval', 'out'], POINTER(c_double), 'Value' )),
    COMMETHOD([helpstring(u'Reads the current element value as a binary array.')], HRESULT, 'ReadBinary',
              ( ['retval', 'out'], POINTER(_midlSAFEARRAY(c_ubyte)), 'Value' )),
    COMMETHOD([helpstring(u'Reads the current element value as a variant.')], HRESULT, 'ReadVariant',
              ( ['retval', 'out'], POINTER(VARIANT), 'Value' )),
]
################################################################
## code template for IXMLReader implementation
##class IXMLReader_Impl(object):
##    @property
##    def NamespaceURI(self):
##        u'Namespace URI of current element.'
##        #return uri
##
##    @property
##    def Attributes(self):
##        u'Attributes of current element.'
##        #return Attributes
##
##    @property
##    def IsLastChild(self):
##        u'Indicates whether the current element is the last child element of its parent.'
##        #return isLast
##
##    def LookupPrefix(self, Prefix):
##        u'Obtains the prefix for a declared URI.'
##        #return uri
##
##    def ReadDate(self):
##        u'Reads the current element value as a date.'
##        #return Value
##
##    def NextElement(self):
##        u'Moves position to next element.'
##        #return 
##
##    def OpenElement(self):
##        u'Moves position to first child element.'
##        #return 
##
##    @property
##    def NamespaceDeclarations(self):
##        u'Namespace declarations of current element.'
##        #return namespaces
##
##    def ReadByte(self):
##        u'Reads the current element value as a byte.'
##        #return Value
##
##    def ReadFloat(self):
##        u'Reads the current element value as a float.'
##        #return Value
##
##    def ReadBoolean(self):
##        u'Reads the current element value as a boolean.'
##        #return Value
##
##    def ReadInteger(self):
##        u'Reads the current element value as a long.'
##        #return Value
##
##    @property
##    def LocalName(self):
##        u'Local name of current element.'
##        #return LocalName
##
##    def ReadVariant(self):
##        u'Reads the current element value as a variant.'
##        #return Value
##
##    def ReadBinary(self):
##        u'Reads the current element value as a binary array.'
##        #return Value
##
##    def ReadShort(self):
##        u'Reads the current element value as a short.'
##        #return Value
##
##    @property
##    def HasElementChildren(self):
##        u'Indicates whether the current element has child elements.'
##        #return hasChildren
##
##    def CloseElement(self):
##        u'Moves position to parent element.'
##        #return 
##
##    @property
##    def Text(self):
##        u'Text value of current element.'
##        #return Text
##
##    @property
##    def NamespacePrefix(self):
##        u'Namespace prefix of current element.'
##        #return Prefix
##
##    def ReadDouble(self):
##        u'Reads the current element value as a double.'
##        #return Value
##
##    def ReadFrom(self, inputStream):
##        u'Specifies the input XML stream.'
##        #return 
##

class IProxyServerInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control proxy server configuration.'
    _iid_ = GUID('{FC221FF0-1240-43A0-8D76-3E917D029CE6}')
    _idlflags_ = ['oleautomation']
class IProxyServerInfo2(IProxyServerInfo):
    _case_insensitive_ = True
    u'Provides access to additional ProxyServerInfo methods.'
    _iid_ = GUID('{E724E8B4-F2FB-40EA-BF7E-EB296DB6ACDA}')
    _idlflags_ = ['oleautomation']
IProxyServerInfo._methods_ = [
    COMMETHOD(['propget', helpstring(u'Proxy server user name.')], HRESULT, 'UserName',
              ( ['retval', 'out'], POINTER(BSTR), 'UserName' )),
    COMMETHOD(['propput', helpstring(u'Proxy server user name.')], HRESULT, 'UserName',
              ( ['in'], BSTR, 'UserName' )),
    COMMETHOD(['propget', helpstring(u'Proxy server user password.')], HRESULT, 'Password',
              ( ['retval', 'out'], POINTER(BSTR), 'Password' )),
    COMMETHOD(['propput', helpstring(u'Proxy server user password.')], HRESULT, 'Password',
              ( ['in'], BSTR, 'Password' )),
    COMMETHOD(['propget', helpstring(u'Proxy server address.')], HRESULT, 'ProxyServer',
              ( ['retval', 'out'], POINTER(BSTR), 'ProxyServer' )),
    COMMETHOD(['propput', helpstring(u'Proxy server address.')], HRESULT, 'ProxyServer',
              ( ['in'], BSTR, 'ProxyServer' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether a proxy server is required.')], HRESULT, 'Enabled',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Enabled' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether a proxy server is required.')], HRESULT, 'Enabled',
              ( ['in'], VARIANT_BOOL, 'Enabled' )),
    COMMETHOD([helpstring(u'Read proxy server configuration from the registry.')], HRESULT, 'ReadProxyServerInfo'),
    COMMETHOD([helpstring(u'Write proxy server configuration to the registry.')], HRESULT, 'WriteProxyServerInfo'),
]
################################################################
## code template for IProxyServerInfo implementation
##class IProxyServerInfo_Impl(object):
##    def _get(self):
##        u'Proxy server user name.'
##        #return UserName
##    def _set(self, UserName):
##        u'Proxy server user name.'
##    UserName = property(_get, _set, doc = _set.__doc__)
##
##    def ReadProxyServerInfo(self):
##        u'Read proxy server configuration from the registry.'
##        #return 
##
##    def _get(self):
##        u'Indicates whether a proxy server is required.'
##        #return Enabled
##    def _set(self, Enabled):
##        u'Indicates whether a proxy server is required.'
##    Enabled = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Proxy server address.'
##        #return ProxyServer
##    def _set(self, ProxyServer):
##        u'Proxy server address.'
##    ProxyServer = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Proxy server user password.'
##        #return Password
##    def _set(self, Password):
##        u'Proxy server user password.'
##    Password = property(_get, _set, doc = _set.__doc__)
##
##    def WriteProxyServerInfo(self):
##        u'Write proxy server configuration to the registry.'
##        #return 
##

IProxyServerInfo2._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates credentials cancel state.')], HRESULT, 'CredentialsCancelled',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD(['propput', helpstring(u'Indicates credentials cancel state.')], HRESULT, 'CredentialsCancelled',
              ( ['in'], VARIANT_BOOL, 'Value' )),
    COMMETHOD([helpstring(u'Cache proxy credentials.')], HRESULT, 'CacheProxyCredentials'),
]
################################################################
## code template for IProxyServerInfo2 implementation
##class IProxyServerInfo2_Impl(object):
##    def CacheProxyCredentials(self):
##        u'Cache proxy credentials.'
##        #return 
##
##    def _get(self):
##        u'Indicates credentials cancel state.'
##        #return Value
##    def _set(self, Value):
##        u'Indicates credentials cancel state.'
##    CredentialsCancelled = property(_get, _set, doc = _set.__doc__)
##

class FileNames(CoClass):
    u'FileNames object maintains an array of file paths.'
    _reg_clsid_ = GUID('{A3DCEA3A-EBD5-11D4-A656-0008C711C8C1}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
FileNames._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IFileNames, IFileNames2]

class LongArray(CoClass):
    u'An object for holding a Long array.'
    _reg_clsid_ = GUID('{98BFB808-E91F-11D2-9F81-00C04F8ECE27}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
LongArray._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ILongArray, IXMLSerialize, IPersist, IPersistStream]

class PropertySet(CoClass):
    u'Esri Property Set object.'
    _reg_clsid_ = GUID('{588E5A11-D09B-11D1-AA7C-00C04FA33A15}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class IPropertySet2(IPropertySet):
    _case_insensitive_ = True
    u'Provides access to members for managing a PropertySet.'
    _iid_ = GUID('{613C41D5-3325-11D4-8141-00C04F686238}')
    _idlflags_ = ['oleautomation']
class IClone(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control cloning of objects.'
    _iid_ = GUID('{9BFF8AEB-E415-11D0-943C-080009EEBECB}')
    _idlflags_ = ['oleautomation']
PropertySet._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IPropertySet, IPropertySet2, IXMLSerialize, IPersist, IPersistStream, IClone]

class SSLInfo(CoClass):
    u'A utility class for setting SSL configuration information.'
    _reg_clsid_ = GUID('{D5853DC9-D6A6-467A-9577-3357CCCD786A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class ISSLInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control HTTPS configuration.'
    _iid_ = GUID('{0DBCFAFE-4724-416C-A4CD-C0EED8CA7D87}')
    _idlflags_ = ['oleautomation']
SSLInfo._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ISSLInfo]

class EnvironmentManager(CoClass):
    u'Singleton object that manages different environments (collections of configuration information).'
    _reg_clsid_ = GUID('{8A626D49-5F5E-47D9-9463-0B802E9C4167}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class IEnvironmentManager(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to environments.'
    _iid_ = GUID('{3551EB0B-AE83-40A3-A048-02AB9FFBEE0D}')
    _idlflags_ = ['oleautomation']
EnvironmentManager._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IEnvironmentManager]

class ComponentCategoryManager(CoClass):
    u'Component Category Manager Object.'
    _reg_clsid_ = GUID('{D9B58742-322D-11D2-A29A-080009B6F22B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class IComponentCategoryManager(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that work with the component category manager.'
    _iid_ = GUID('{D9B58741-322D-11D2-A29A-080009B6F22B}')
    _idlflags_ = ['oleautomation']
class IComponentCategoryInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that work with the component category manager.'
    _iid_ = GUID('{C5185FD4-557C-4E07-9A75-ABF060F2EF41}')
    _idlflags_ = ['oleautomation']
ComponentCategoryManager._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IComponentCategoryManager, IComponentCategoryInfo]

class DoubleArray(CoClass):
    u'An object for holding a Double array.'
    _reg_clsid_ = GUID('{60C06CA7-E09E-11D2-9F7B-00C04F8ECE27}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
DoubleArray._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IDoubleArray, IXMLSerialize, IPersist, IPersistStream]

class UID(CoClass):
    u'Unique Identifier Object.'
    _reg_clsid_ = GUID('{78FF7FA1-FB2F-11D1-94A2-080009EEBECB}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
UID._com_interfaces_ = [IUID, IPersist, IPersistStream, IXMLSerialize]

class VariantStreamIO(CoClass):
    u'Helper object that performs stream IO for Variants.'
    _reg_clsid_ = GUID('{12DADD0E-4D96-4599-B4BA-F9246A8AD312}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
VariantStreamIO._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IVariantStreamIO, IVariantStream, IDocumentVersion]

class IEnumUID(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to an enumerator over a set of component IDs.'
    _iid_ = GUID('{CD5F0F7D-38EE-4DE5-8EFD-41FDB542B501}')
    _idlflags_ = ['oleautomation']
IEnumUID._methods_ = [
    COMMETHOD([helpstring(u'Obtains the next component ID in the collection.')], HRESULT, 'Next',
              ( ['retval', 'out'], POINTER(POINTER(IUID)), 'pComponentID' )),
    COMMETHOD([helpstring(u'Resets the enumerator back to the beginning of the collection.')], HRESULT, 'Reset'),
]
################################################################
## code template for IEnumUID implementation
##class IEnumUID_Impl(object):
##    def Reset(self):
##        u'Resets the enumerator back to the beginning of the collection.'
##        #return 
##
##    def Next(self):
##        u'Obtains the next component ID in the collection.'
##        #return pComponentID
##

class StrArray(CoClass):
    u'An object for holding a String array.'
    _reg_clsid_ = GUID('{A7F92065-36CE-47B6-A463-4763DA947CC2}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
StrArray._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IStringArray, IXMLSerialize, IPersist, IPersistStream]

class VarArray(CoClass):
    u'An object for holding a Variant array.'
    _reg_clsid_ = GUID('{762F0474-ECA2-475B-99F4-26678D79436E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class IVariantArray(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control variant arrays.'
    _iid_ = GUID('{3A10189D-0377-4DDF-8C05-A2672AF6A403}')
    _idlflags_ = ['oleautomation']
VarArray._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IVariantArray, IXMLSerialize, IPersist, IPersistStream]

class PropertySetArray(CoClass):
    u'A collection of IPropertySet objects.'
    _reg_clsid_ = GUID('{C94BBD8A-EC33-4921-8EC3-6AD4B33232C3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class IPropertySetArray(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the IPropertySetArray Interface.'
    _iid_ = GUID('{93FC737F-8C92-4C92-B0D7-75E71FD753C9}')
    _idlflags_ = ['oleautomation']
class IXMLVersionSupport(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that help in serializing an object to different namespaces (versions).'
    _iid_ = GUID('{72CA65B9-13DE-48B7-8443-717B69B72A99}')
    _idlflags_ = ['oleautomation']
PropertySetArray._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IPropertySetArray, IXMLSerialize, IPersistStream, IPersist, IXMLVersionSupport]

class UnitConverter(CoClass):
    u'Helper CoClass to convert units.'
    _reg_clsid_ = GUID('{2F65C2F2-701B-4E11-9157-FC4A3D0B6069}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class IUnitConverter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members used for converting units.'
    _iid_ = GUID('{1F3FBCA9-6611-4567-88E4-E0FA8B6FB26D}')
    _idlflags_ = ['oleautomation']
UnitConverter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IUnitConverter]

class AngularConverter(CoClass):
    u'Converts angle measurement from one unit to another.'
    _reg_clsid_ = GUID('{4D380153-9B16-41AC-8F9F-A23D9C2DDFE4}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class IAngularConverter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods that allow an angle to be converted from one direction unit to another.'
    _iid_ = GUID('{1B64B6B4-1434-4172-8666-BBF83E5C467B}')
    _idlflags_ = ['oleautomation']
class IAngularConverter2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods that allow an angle to be converted from one direction unit to another.'
    _iid_ = GUID('{95674BA9-3CD5-429D-A5AC-9D105A099CF7}')
    _idlflags_ = ['oleautomation']
AngularConverter._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IAngularConverter, IAngularConverter2]

IPersistStream._methods_ = [
    COMMETHOD([], HRESULT, 'IsDirty'),
    COMMETHOD([], HRESULT, 'Load',
              ( ['in'], POINTER(IStream), 'pstm' )),
    COMMETHOD([], HRESULT, 'Save',
              ( ['in'], POINTER(IStream), 'pstm' ),
              ( ['in'], c_int, 'fClearDirty' )),
    COMMETHOD([], HRESULT, 'GetSizeMax',
              ( ['out'], POINTER(_ULARGE_INTEGER), 'pcbSize' )),
]
################################################################
## code template for IPersistStream implementation
##class IPersistStream_Impl(object):
##    def Load(self, pstm):
##        '-no docstring-'
##        #return 
##
##    def GetSizeMax(self):
##        '-no docstring-'
##        #return pcbSize
##
##    def Save(self, pstm, fClearDirty):
##        '-no docstring-'
##        #return 
##
##    def IsDirty(self):
##        '-no docstring-'
##        #return 
##

class ScaleFormat(CoClass):
    u'A utility object for formatting scale.'
    _reg_clsid_ = GUID('{7B759B6D-DF88-4AED-ADD7-6F53105B47A4}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class IScaleFormat(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to scale formatting options.'
    _iid_ = GUID('{AE9EDA31-A9F0-4687-B3A5-8C061C92D3EB}')
    _idlflags_ = ['oleautomation']
ScaleFormat._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IScaleFormat, IPersistStream, IPersist, IClone, IDocumentVersionSupportGEN]


# values for enumeration 'esriHttpMethod'
esriHttpMethodPost = 0
esriHttpMethodGet = 1
esriHttpMethodPut = 2
esriHttpMethodDelete = 3
esriHttpMethodHead = 4
esriHttpMethodTrace = 5
esriHttpMethodOptions = 6
esriHttpMethod = c_int # enum
IJobRegistry._methods_ = [
    COMMETHOD([helpstring(u'Initializes the jobs registry.')], HRESULT, 'Init',
              ( ['in'], BSTR, 'Path' )),
    COMMETHOD([helpstring(u'Registers job.')], HRESULT, 'RegisterJob',
              ( ['in'], BSTR, 'JobID' ),
              ( ['in'], BSTR, 'jobDir' )),
    COMMETHOD([helpstring(u'Unregisters job.')], HRESULT, 'UnregisterJob',
              ( ['in'], BSTR, 'JobID' )),
    COMMETHOD([helpstring(u"Returns path to job's directory.")], HRESULT, 'GetJobDirectory',
              ( ['in'], BSTR, 'JobID' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Path' )),
]
################################################################
## code template for IJobRegistry implementation
##class IJobRegistry_Impl(object):
##    def Init(self, Path):
##        u'Initializes the jobs registry.'
##        #return 
##
##    def RegisterJob(self, JobID, jobDir):
##        u'Registers job.'
##        #return 
##
##    def GetJobDirectory(self, JobID):
##        u"Returns path to job's directory."
##        #return Path
##
##    def UnregisterJob(self, JobID):
##        u'Unregisters job.'
##        #return 
##

IXMLVersionSupport._methods_ = [
    COMMETHOD(['propget', helpstring(u'The minimum namespace the class can serialize to (eg the 90 namespace).')], HRESULT, 'MinNamespaceSupported',
              ( ['retval', 'out'], POINTER(BSTR), 'NamespaceURI' )),
]
################################################################
## code template for IXMLVersionSupport implementation
##class IXMLVersionSupport_Impl(object):
##    @property
##    def MinNamespaceSupported(self):
##        u'The minimum namespace the class can serialize to (eg the 90 namespace).'
##        #return NamespaceURI
##

class CategoryFactory(CoClass):
    u'Component Category Factory.'
    _reg_clsid_ = GUID('{A8253EB1-9381-11D2-8521-0000F875B9C6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class ICategoryFactory(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that work with the category factory.'
    _iid_ = GUID('{A8253EB0-9381-11D2-8521-0000F875B9C6}')
    _idlflags_ = ['oleautomation']
CategoryFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ICategoryFactory]

class IAMFSerializer(IExternalSerializer):
    _case_insensitive_ = True
    u'Provides access to high-level AMF serialization methods.'
    _iid_ = GUID('{8F6F56FC-A942-44F5-AF7D-5312FDF0C0C6}')
    _idlflags_ = ['oleautomation']
IAMFSerializer._methods_ = [
    COMMETHOD(['propget', helpstring(u'Obtains AMF Writer.')], HRESULT, 'Writer',
              ( ['retval', 'out'], POINTER(POINTER(IAMFWriter)), 'ppWriter' )),
    COMMETHOD([helpstring(u'Write serialization options.')], HRESULT, 'InitSerializer',
              ( ['in'], POINTER(IAMFWriter), 'pWriter' ),
              ( ['in'], POINTER(IPropertySet), 'pProps' )),
    COMMETHOD([helpstring(u'AMF message packet #1 call. Write AMF0 message version.')], HRESULT, 'WriteAMF0MessageVersion',
              ( ['in'], c_short, 'sVersion' )),
    COMMETHOD([helpstring(u'AMF message packet #2 call. Write header count. Use zero to skip headers.')], HRESULT, 'WriteAMF0HeaderCount',
              ( ['in'], c_short, 'headerCount' )),
    COMMETHOD([helpstring(u'AMF message packet #2a call. Write header(s).')], HRESULT, 'WriteAMF0Header',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], VARIANT_BOOL, 'mustUnderstand' ),
              ( ['in'], VARIANT, 'Value' )),
    COMMETHOD([helpstring(u'AMF message packet #3 call. Write message count.')], HRESULT, 'WriteAMF0MessageCount',
              ( ['in'], c_short, 'messageCount' )),
    COMMETHOD([helpstring(u'AMF message packet #3a call. Write message(s). Set isAMF3content to true if you are sending AMF3 data in the message.')], HRESULT, 'WriteAMF0MessageHeader',
              ( ['in'], BSTR, 'targetURI' ),
              ( ['in'], BSTR, 'respURI' ),
              ( ['in'], c_int, 'length' )),
]
################################################################
## code template for IAMFSerializer implementation
##class IAMFSerializer_Impl(object):
##    @property
##    def Writer(self):
##        u'Obtains AMF Writer.'
##        #return ppWriter
##
##    def InitSerializer(self, pWriter, pProps):
##        u'Write serialization options.'
##        #return 
##
##    def WriteAMF0HeaderCount(self, headerCount):
##        u'AMF message packet #2 call. Write header count. Use zero to skip headers.'
##        #return 
##
##    def WriteAMF0Header(self, Name, mustUnderstand, Value):
##        u'AMF message packet #2a call. Write header(s).'
##        #return 
##
##    def WriteAMF0MessageCount(self, messageCount):
##        u'AMF message packet #3 call. Write message count.'
##        #return 
##
##    def WriteAMF0MessageHeader(self, targetURI, respURI, length):
##        u'AMF message packet #3a call. Write message(s). Set isAMF3content to true if you are sending AMF3 data in the message.'
##        #return 
##
##    def WriteAMF0MessageVersion(self, sVersion):
##        u'AMF message packet #1 call. Write AMF0 message version.'
##        #return 
##

class BaseStatistics(CoClass):
    u'Base statistics class for generating and reporting statistics.'
    _reg_clsid_ = GUID('{B9C4358C-78B8-11D2-AE60-080009EC732A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class IGenerateStatistics(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members used for generating statistics.'
    _iid_ = GUID('{B9C43589-78B8-11D2-AE60-080009EC732A}')
    _idlflags_ = ['oleautomation']
class IStatisticsResults(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members used for reporting statistics.'
    _iid_ = GUID('{B9C4358A-78B8-11D2-AE60-080009EC732A}')
    _idlflags_ = ['oleautomation']
class IFrequencyStatistics(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members used for reporting frequency statistics.'
    _iid_ = GUID('{B9C4358B-78B8-11D2-AE60-080009EC732A}')
    _idlflags_ = ['oleautomation']
BaseStatistics._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IGenerateStatistics, IStatisticsResults, IFrequencyStatistics]

class FileStream(CoClass):
    u'Specialized kind of IStream for files.'
    _reg_clsid_ = GUID('{381D1AA1-C06F-11D2-9F82-00C04F8ED211}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class IBlobStream(IStream):
    _case_insensitive_ = True
    u'Provides access to members that control a Blob Stream.'
    _iid_ = GUID('{BC92995E-E736-11D0-9A93-080009EC734B}')
    _idlflags_ = []
class IFile(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to a method that opens a file.'
    _iid_ = GUID('{381D1AA2-C06F-11D2-9F82-00C04F8ED211}')
    _idlflags_ = ['oleautomation']
FileStream._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IBlobStream, IFile, IDocumentVersion]

class LicenseInfoEnum(CoClass):
    u'Enumerator of extension licenses supported by a product.'
    _reg_clsid_ = GUID('{E495E958-5244-4F9B-BF02-42C276964953}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
LicenseInfoEnum._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ILicenseInfoEnum]

class AoInitialize(CoClass):
    u'Class initializes ArcObject components runtime environment.   This class must be the first ArcObject created.'
    _reg_clsid_ = GUID('{E01BE902-CC85-4B13-A828-02E789E0DDA9}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class IAoInitialize(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that initialize licensing for ArcGIS Desktop, Engine, and Server.'
    _iid_ = GUID('{9AB6A638-ACA8-4820-830C-463EA11C8722}')
    _idlflags_ = ['oleautomation']
AoInitialize._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IAoInitialize, ISupportErrorInfo, ILicenseInformation]

IClone._methods_ = [
    COMMETHOD([helpstring(u'Clones the receiver and assigns the result to *clone.')], HRESULT, 'Clone',
              ( ['retval', 'out'], POINTER(POINTER(IClone)), 'Clone' )),
    COMMETHOD([helpstring(u'Assigns the properties of src to the receiver.')], HRESULT, 'Assign',
              ( ['in'], POINTER(IClone), 'src' )),
    COMMETHOD([helpstring(u'Indicates if the receiver and other have the same properties.')], HRESULT, 'IsEqual',
              ( ['in'], POINTER(IClone), 'other' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'equal' )),
    COMMETHOD([helpstring(u'Indicates if the receiver and other are the same object.')], HRESULT, 'IsIdentical',
              ( ['in'], POINTER(IClone), 'other' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'identical' )),
]
################################################################
## code template for IClone implementation
##class IClone_Impl(object):
##    def Clone(self):
##        u'Clones the receiver and assigns the result to *clone.'
##        #return Clone
##
##    def IsIdentical(self, other):
##        u'Indicates if the receiver and other are the same object.'
##        #return identical
##
##    def Assign(self, src):
##        u'Assigns the properties of src to the receiver.'
##        #return 
##
##    def IsEqual(self, other):
##        u'Indicates if the receiver and other have the same properties.'
##        #return equal
##

class ExtensionManager(CoClass):
    u'Extension Manager - a singleton.'
    _reg_clsid_ = GUID('{6120BC0A-3D90-4274-97CA-713C41F1FAFF}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class IExtensionManager(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that query extension.'
    _iid_ = GUID('{05C71634-D9D5-4D6F-B68E-D7661142FA06}')
    _idlflags_ = ['oleautomation']
class IExtensionManagerAdmin(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that give life to the extensions.'
    _iid_ = GUID('{262C00F9-114D-45F8-BC9D-A0DD208DC9E1}')
    _idlflags_ = ['oleautomation']
class IJITExtensionManager(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the Just In Time Extension Manager.'
    _iid_ = GUID('{0E3B4663-4CA5-4638-AA4A-7D89878209E5}')
    _idlflags_ = ['oleautomation']
ExtensionManager._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IExtensionManager, IExtensionManagerAdmin, ISupportErrorInfo, IJITExtensionManager]

class MemoryBlobStream(CoClass):
    u'Memory blob stream object.'
    _reg_clsid_ = GUID('{BC929960-E736-11D0-9A93-080009EC734B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class IMemoryBlobStream(IBlobStream):
    _case_insensitive_ = True
    u'Provides access to members that control the Blob Stream.'
    _iid_ = GUID('{BC92995F-E736-11D0-9A93-080009EC734B}')
    _idlflags_ = []
class IMemoryBlobStream2(IMemoryBlobStream):
    _case_insensitive_ = True
    u'Provides access to members that control the Blob Stream.'
    _iid_ = GUID('{5CE09F2C-9C93-4A3B-83AD-E12FB6A67AD4}')
    _idlflags_ = []
class IMemoryBlobStreamVariant(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods for importing and exporting variants to and from a MemoryBlobStream.'
    _iid_ = GUID('{68F0AB65-E2B7-40D8-AA3B-3B7764607DD3}')
    _idlflags_ = ['oleautomation']
MemoryBlobStream._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMemoryBlobStream, IMemoryBlobStream2, IMemoryBlobStreamVariant, IDocumentVersion, ISupportErrorInfo]

class FileName(CoClass):
    u'File Name Object.'
    _reg_clsid_ = GUID('{53DA75DF-D01A-11D2-9F27-00C04F6BC69E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class IFileName(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the pathnames of files.'
    _iid_ = GUID('{53DA75E0-D01A-11D2-9F27-00C04F6BC69E}')
    _idlflags_ = ['oleautomation']
FileName._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IName, IFileName, IPersistStream]

class IJobInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to info properties of the job.'
    _iid_ = GUID('{4A106E7E-D1E7-420F-AECF-CBC867A7FF17}')
    _idlflags_ = ['oleautomation']
IJob._methods_ = [
    COMMETHOD(['propget', helpstring(u'Job id.')], HRESULT, 'JobID',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Job definition.')], HRESULT, 'JobDefinition',
              ( ['retval', 'out'], POINTER(POINTER(IJobDefinition)), 'ppVal' )),
    COMMETHOD(['propput', helpstring(u'Job definition.')], HRESULT, 'JobDefinition',
              ( ['in'], POINTER(IJobDefinition), 'ppVal' )),
    COMMETHOD(['propget', helpstring(u'Job info.')], HRESULT, 'JobInfo',
              ( ['retval', 'out'], POINTER(POINTER(IJobInfo)), 'ppVal' )),
    COMMETHOD(['propput', helpstring(u'Job info.')], HRESULT, 'JobInfo',
              ( ['in'], POINTER(IJobInfo), 'ppVal' )),
    COMMETHOD(['propget', helpstring(u'Job results.')], HRESULT, 'JobResults',
              ( ['retval', 'out'], POINTER(POINTER(IJobResults)), 'ppVal' )),
    COMMETHOD(['propput', helpstring(u'Job results.')], HRESULT, 'JobResults',
              ( ['in'], POINTER(IJobResults), 'ppVal' )),
    COMMETHOD(['propget', helpstring(u'Job messages.')], HRESULT, 'JobMessages',
              ( ['retval', 'out'], POINTER(POINTER(IJobMessages)), 'ppVal' )),
    COMMETHOD(['propput', helpstring(u'Job messages.')], HRESULT, 'JobMessages',
              ( ['in'], POINTER(IJobMessages), 'ppVal' )),
    COMMETHOD(['propget', helpstring(u'Job status.')], HRESULT, 'JobStatus',
              ( ['retval', 'out'], POINTER(esriJobStatus), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Job status.')], HRESULT, 'JobStatus',
              ( ['in'], esriJobStatus, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Job directory.')], HRESULT, 'JobDirectory',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
]
################################################################
## code template for IJob implementation
##class IJob_Impl(object):
##    def _get(self):
##        u'Job results.'
##        #return ppVal
##    def _set(self, ppVal):
##        u'Job results.'
##    JobResults = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def JobDirectory(self):
##        u'Job directory.'
##        #return pVal
##
##    def _get(self):
##        u'Job status.'
##        #return pVal
##    def _set(self, pVal):
##        u'Job status.'
##    JobStatus = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def JobID(self):
##        u'Job id.'
##        #return pVal
##
##    def _get(self):
##        u'Job messages.'
##        #return ppVal
##    def _set(self, ppVal):
##        u'Job messages.'
##    JobMessages = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Job definition.'
##        #return ppVal
##    def _set(self, ppVal):
##        u'Job definition.'
##    JobDefinition = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Job info.'
##        #return ppVal
##    def _set(self, ppVal):
##        u'Job info.'
##    JobInfo = property(_get, _set, doc = _set.__doc__)
##

class AoAuthorizeLicense(CoClass):
    u'Class performs license authorization.'
    _reg_clsid_ = GUID('{6DBE8BF8-6000-4734-B1A8-C81C69651C06}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class IAuthorizeLicense(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that authorize Esri licenses.'
    _iid_ = GUID('{46EBBB64-19B8-437A-8DF4-4378D88F6731}')
    _idlflags_ = ['oleautomation']
AoAuthorizeLicense._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IAuthorizeLicense]

class ObjectCopy(CoClass):
    u'CoClass to copy objects by value.'
    _reg_clsid_ = GUID('{9C3673EB-BC0A-11D5-A9DF-00104BB6FC1C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class IObjectCopy(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members to copy objects by value. The object must support IPersistStream to be copied.'
    _iid_ = GUID('{9C3673EA-BC0A-11D5-A9DF-00104BB6FC1C}')
    _idlflags_ = ['oleautomation']
ObjectCopy._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IObjectCopy]

class XMLPersistedObject(CoClass):
    u'CoClass to serialize objects to XML.'
    _reg_clsid_ = GUID('{C0D4AD6B-ADB3-4B98-8927-1F0EC039BB5E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
XMLPersistedObject._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IXMLPersistedObject, IXMLSerialize]

ISequentialStream._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteRead',
              ( ['out'], POINTER(c_ubyte), 'pv' ),
              ( ['in'], c_ulong, 'cb' ),
              ( ['out'], POINTER(c_ulong), 'pcbRead' )),
    COMMETHOD([], HRESULT, 'RemoteWrite',
              ( ['in'], POINTER(c_ubyte), 'pv' ),
              ( ['in'], c_ulong, 'cb' ),
              ( ['out'], POINTER(c_ulong), 'pcbWritten' )),
]
################################################################
## code template for ISequentialStream implementation
##class ISequentialStream_Impl(object):
##    def RemoteRead(self, cb):
##        '-no docstring-'
##        #return pv, pcbRead
##
##    def RemoteWrite(self, pv, cb):
##        '-no docstring-'
##        #return pcbWritten
##

class tagSTATSTG(Structure):
    pass
IStream._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteSeek',
              ( ['in'], _LARGE_INTEGER, 'dlibMove' ),
              ( ['in'], c_ulong, 'dwOrigin' ),
              ( ['out'], POINTER(_ULARGE_INTEGER), 'plibNewPosition' )),
    COMMETHOD([], HRESULT, 'SetSize',
              ( ['in'], _ULARGE_INTEGER, 'libNewSize' )),
    COMMETHOD([], HRESULT, 'RemoteCopyTo',
              ( ['in'], POINTER(IStream), 'pstm' ),
              ( ['in'], _ULARGE_INTEGER, 'cb' ),
              ( ['out'], POINTER(_ULARGE_INTEGER), 'pcbRead' ),
              ( ['out'], POINTER(_ULARGE_INTEGER), 'pcbWritten' )),
    COMMETHOD([], HRESULT, 'Commit',
              ( ['in'], c_ulong, 'grfCommitFlags' )),
    COMMETHOD([], HRESULT, 'Revert'),
    COMMETHOD([], HRESULT, 'LockRegion',
              ( ['in'], _ULARGE_INTEGER, 'libOffset' ),
              ( ['in'], _ULARGE_INTEGER, 'cb' ),
              ( ['in'], c_ulong, 'dwLockType' )),
    COMMETHOD([], HRESULT, 'UnlockRegion',
              ( ['in'], _ULARGE_INTEGER, 'libOffset' ),
              ( ['in'], _ULARGE_INTEGER, 'cb' ),
              ( ['in'], c_ulong, 'dwLockType' )),
    COMMETHOD([], HRESULT, 'Stat',
              ( ['out'], POINTER(tagSTATSTG), 'pstatstg' ),
              ( ['in'], c_ulong, 'grfStatFlag' )),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IStream)), 'ppstm' )),
]
################################################################
## code template for IStream implementation
##class IStream_Impl(object):
##    def RemoteSeek(self, dlibMove, dwOrigin):
##        '-no docstring-'
##        #return plibNewPosition
##
##    def Stat(self, grfStatFlag):
##        '-no docstring-'
##        #return pstatstg
##
##    def UnlockRegion(self, libOffset, cb, dwLockType):
##        '-no docstring-'
##        #return 
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppstm
##
##    def Revert(self):
##        '-no docstring-'
##        #return 
##
##    def RemoteCopyTo(self, pstm, cb):
##        '-no docstring-'
##        #return pcbRead, pcbWritten
##
##    def LockRegion(self, libOffset, cb, dwLockType):
##        '-no docstring-'
##        #return 
##
##    def Commit(self, grfCommitFlags):
##        '-no docstring-'
##        #return 
##
##    def SetSize(self, libNewSize):
##        '-no docstring-'
##        #return 
##

IBlobStream._methods_ = [
    COMMETHOD(['propget', helpstring(u'The size of the stream.')], HRESULT, 'Size',
              ( ['retval', 'out'], POINTER(c_ulong), 'Size' )),
    COMMETHOD(['propput', helpstring(u'The size of the stream.')], HRESULT, 'Size',
              ( ['in'], c_ulong, 'Size' )),
    COMMETHOD([helpstring(u'Saves the stream to the specified file.')], HRESULT, 'SaveToFile',
              ( ['in'], BSTR, 'FileName' )),
    COMMETHOD([helpstring(u'Loads a stream from the specified file.')], HRESULT, 'LoadFromFile',
              ( ['in'], BSTR, 'FileName' )),
]
################################################################
## code template for IBlobStream implementation
##class IBlobStream_Impl(object):
##    def LoadFromFile(self, FileName):
##        u'Loads a stream from the specified file.'
##        #return 
##
##    def SaveToFile(self, FileName):
##        u'Saves the stream to the specified file.'
##        #return 
##
##    def _get(self):
##        u'The size of the stream.'
##        #return Size
##    def _set(self, Size):
##        u'The size of the stream.'
##    Size = property(_get, _set, doc = _set.__doc__)
##

IMemoryBlobStream._methods_ = [
    COMMETHOD([helpstring(u'Attaches the stream to memory. If transferOwnership is true, memory must be allocated with HeapAlloc() using GetProcessHeap().')], HRESULT, 'AttachToMemory',
              ( ['in'], POINTER(c_ubyte), 'blobMemory' ),
              ( [], c_ulong, 'Size' ),
              ( [], c_int, 'transferOwnership' )),
    COMMETHOD([helpstring(u'Import using another blob.')], HRESULT, 'ImportFromMemory',
              ( ['in'], POINTER(c_ubyte), 'blobMemory' ),
              ( [], c_ulong, 'Size' )),
    COMMETHOD(['propget', helpstring(u'The memory of the blob stream.')], HRESULT, 'Memory',
              ( ['out'], POINTER(POINTER(c_ubyte)), 'blobMemory' ),
              ( ['out'], POINTER(c_ulong), 'Size' )),
]
################################################################
## code template for IMemoryBlobStream implementation
##class IMemoryBlobStream_Impl(object):
##    def ImportFromMemory(self, blobMemory, Size):
##        u'Import using another blob.'
##        #return 
##
##    def AttachToMemory(self, blobMemory, Size, transferOwnership):
##        u'Attaches the stream to memory. If transferOwnership is true, memory must be allocated with HeapAlloc() using GetProcessHeap().'
##        #return 
##
##    @property
##    def Memory(self):
##        u'The memory of the blob stream.'
##        #return blobMemory, Size
##

class _WKSPointZ(Structure):
    pass
_WKSPointZ._fields_ = [
    ('X', c_double),
    ('Y', c_double),
    ('Z', c_double),
]
assert sizeof(_WKSPointZ) == 24, sizeof(_WKSPointZ)
assert alignment(_WKSPointZ) == 8, alignment(_WKSPointZ)

# values for enumeration 'esriWebResponseDataType'
esriWRDTPayload = 0
esriWRDTFileToReturn = 1
esriWebResponseDataType = c_int # enum
class ShortcutName(CoClass):
    u'GxObject that represents the shortcut Name Object.'
    _reg_clsid_ = GUID('{3BEB09E4-3941-4A07-9D1A-EC2B43BA7D50}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class IShortcutName(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that define the target for the shortcut name.'
    _iid_ = GUID('{E29B3C76-E7B2-458E-8732-E929391DA234}')
    _idlflags_ = ['oleautomation']
ShortcutName._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IName, IFileName, IShortcutName, IPersistStream]

WKSPointZ = _WKSPointZ
class ArcGISLocale(CoClass):
    u'Class for accessing ArcGIS locale.'
    _reg_clsid_ = GUID('{495EC746-46D4-4A6E-BD06-3A08C38465CA}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class IArcGISLocale(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members for the ArcGIS locale.'
    _iid_ = GUID('{69467533-F25B-4EF3-B680-229B4DC6087B}')
    _idlflags_ = ['oleautomation']
ArcGISLocale._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IArcGISLocale]

IMemoryBlobStream2._methods_ = [
    COMMETHOD(['propget', helpstring(u'The allocated size of the stream.')], HRESULT, 'AllocSize',
              ( ['retval', 'out'], POINTER(c_ulong), 'Size' )),
    COMMETHOD(['propput', helpstring(u'The allocated size of the stream.')], HRESULT, 'AllocSize',
              ( ['in'], c_ulong, 'Size' )),
    COMMETHOD(['propget', helpstring(u'The allocated size of the stream.')], HRESULT, 'PaddingSize',
              ( ['retval', 'out'], POINTER(c_ulong), 'Size' )),
    COMMETHOD(['propput', helpstring(u'The allocated size of the stream.')], HRESULT, 'PaddingSize',
              ( ['in'], c_ulong, 'Size' )),
]
################################################################
## code template for IMemoryBlobStream2 implementation
##class IMemoryBlobStream2_Impl(object):
##    def _get(self):
##        u'The allocated size of the stream.'
##        #return Size
##    def _set(self, Size):
##        u'The allocated size of the stream.'
##    AllocSize = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The allocated size of the stream.'
##        #return Size
##    def _set(self, Size):
##        u'The allocated size of the stream.'
##    PaddingSize = property(_get, _set, doc = _set.__doc__)
##

class ESRILicenseInfo(CoClass):
    u'Esri License Info.'
    _reg_clsid_ = GUID('{2CCA83E3-EFE4-4CBA-9852-6C0C7521AD8E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
ESRILicenseInfo._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IESRILicenseInfo]

ISupportErrorInfo._methods_ = [
    COMMETHOD([], HRESULT, 'InterfaceSupportsErrorInfo',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'riid' )),
]
################################################################
## code template for ISupportErrorInfo implementation
##class ISupportErrorInfo_Impl(object):
##    def InterfaceSupportsErrorInfo(self, riid):
##        '-no docstring-'
##        #return 
##

class IJSONSerializer(IExternalSerializer):
    _case_insensitive_ = True
    u'Provides access to high-level JSON serialization methods.'
    _iid_ = GUID('{AB718CDF-0C06-4D18-9AA4-A6C54B2BC28C}')
    _idlflags_ = ['oleautomation']
IJSONSerializer._methods_ = [
    COMMETHOD(['propget', helpstring(u'Obtains JSON Writer.')], HRESULT, 'Writer',
              ( ['retval', 'out'], POINTER(POINTER(IJSONWriter)), 'ppWriter' )),
    COMMETHOD([helpstring(u'Writes serialization options.')], HRESULT, 'InitSerializer',
              ( ['in'], POINTER(IJSONWriter), 'pWriter' ),
              ( ['in'], POINTER(IPropertySet), 'pProps' )),
]
################################################################
## code template for IJSONSerializer implementation
##class IJSONSerializer_Impl(object):
##    @property
##    def Writer(self):
##        u'Obtains JSON Writer.'
##        #return ppWriter
##
##    def InitSerializer(self, pWriter, pProps):
##        u'Writes serialization options.'
##        #return 
##

_WKSPoint._fields_ = [
    ('X', c_double),
    ('Y', c_double),
]
assert sizeof(_WKSPoint) == 16, sizeof(_WKSPoint)
assert alignment(_WKSPoint) == 8, alignment(_WKSPoint)
WKSEnvelope = _WKSEnvelope
class IExtension(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that define an extension.'
    _iid_ = GUID('{7F657EC9-DBF1-11D2-9F2F-00C04F6BC69E}')
    _idlflags_ = ['oleautomation']
IExtension._methods_ = [
    COMMETHOD(['propget', helpstring(u'The name of the extension.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'extensionName' )),
    COMMETHOD([helpstring(u'Starts up the extension with the given initialization data.')], HRESULT, 'Startup',
              ( ['in'], POINTER(VARIANT), 'initializationData' )),
    COMMETHOD([helpstring(u'Shuts down the extension.')], HRESULT, 'Shutdown'),
]
################################################################
## code template for IExtension implementation
##class IExtension_Impl(object):
##    def Startup(self, initializationData):
##        u'Starts up the extension with the given initialization data.'
##        #return 
##
##    @property
##    def Name(self):
##        u'The name of the extension.'
##        #return extensionName
##
##    def Shutdown(self):
##        u'Shuts down the extension.'
##        #return 
##

class IMessage(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the properties of a Message.'
    _iid_ = GUID('{E4E5591D-C47E-4A2D-856E-8A1847547A97}')
    _idlflags_ = ['oleautomation']
class IErrorInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{1CF2B120-547D-101B-8E65-08002B2BD119}')
    _idlflags_ = []
IMessage._methods_ = [
    COMMETHOD(['propget', helpstring(u'Name of the message.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'messageName' )),
    COMMETHOD(['propput', helpstring(u'Name of the message.')], HRESULT, 'Name',
              ( ['in'], BSTR, 'messageName' )),
    COMMETHOD(['propget', helpstring(u'Namespace of the message.')], HRESULT, 'NamespaceURI',
              ( ['retval', 'out'], POINTER(BSTR), 'uri' )),
    COMMETHOD(['propput', helpstring(u'Namespace of the message.')], HRESULT, 'NamespaceURI',
              ( ['in'], BSTR, 'uri' )),
    COMMETHOD(['propget', helpstring(u'Parameters of the message.')], HRESULT, 'Parameters',
              ( ['retval', 'out'], POINTER(POINTER(IXMLSerializeData)), 'data' )),
    COMMETHOD(['propget', helpstring(u'Properties of the message.')], HRESULT, 'Properties',
              ( ['retval', 'out'], POINTER(POINTER(IPropertySet)), 'props' )),
    COMMETHOD(['propputref', helpstring(u'Properties of the message.')], HRESULT, 'Properties',
              ( ['in'], POINTER(IPropertySet), 'props' )),
    COMMETHOD(['propget', helpstring(u'HRESULT of the Message.')], HRESULT, 'Result',
              ( ['retval', 'out'], POINTER(c_int), 'hresult' )),
    COMMETHOD(['propget', helpstring(u'Valid when the message is a fault.')], HRESULT, 'ErrorInfo',
              ( ['retval', 'out'], POINTER(POINTER(IErrorInfo)), 'ErrorInfo' )),
    COMMETHOD([helpstring(u'Writes error information.')], HRESULT, 'SetError',
              ( ['in'], c_int, 'hresult' ),
              ( ['in'], POINTER(IErrorInfo), 'pErrorInfo' )),
    COMMETHOD([helpstring(u'Reads an XML input stream for a message.')], HRESULT, 'ReadXML',
              ( ['in'], POINTER(IStream), 'Stream' )),
    COMMETHOD([helpstring(u'Writes an XML output stream for a message.')], HRESULT, 'WriteXML',
              ( ['in'], POINTER(IStream), 'Stream' )),
]
################################################################
## code template for IMessage implementation
##class IMessage_Impl(object):
##    def ReadXML(self, Stream):
##        u'Reads an XML input stream for a message.'
##        #return 
##
##    def _get(self):
##        u'Name of the message.'
##        #return messageName
##    def _set(self, messageName):
##        u'Name of the message.'
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Parameters(self):
##        u'Parameters of the message.'
##        #return data
##
##    def WriteXML(self, Stream):
##        u'Writes an XML output stream for a message.'
##        #return 
##
##    def _get(self):
##        u'Namespace of the message.'
##        #return uri
##    def _set(self, uri):
##        u'Namespace of the message.'
##    NamespaceURI = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Result(self):
##        u'HRESULT of the Message.'
##        #return hresult
##
##    def SetError(self, hresult, pErrorInfo):
##        u'Writes error information.'
##        #return 
##
##    @property
##    def ErrorInfo(self):
##        u'Valid when the message is a fault.'
##        #return ErrorInfo
##
##    def Properties(self, props):
##        u'Properties of the message.'
##        #return 
##

class IExtensionAccelerators(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to a method that creates extension accelerators.'
    _iid_ = GUID('{35D9879A-DB68-4A2F-87CC-7206F0060B71}')
    _idlflags_ = ['oleautomation']
IExtensionAccelerators._methods_ = [
    COMMETHOD([helpstring(u'Called to create the keyboard accelerators for this extension.')], HRESULT, 'CreateAccelerators'),
]
################################################################
## code template for IExtensionAccelerators implementation
##class IExtensionAccelerators_Impl(object):
##    def CreateAccelerators(self):
##        u'Called to create the keyboard accelerators for this extension.'
##        #return 
##

class IRESTCallback(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'REST handler callback interface.'
    _iid_ = GUID('{5D203D0E-D444-4201-BA8F-4F60FE0E4998}')
    _idlflags_ = ['oleautomation']
IRESTCallback._methods_ = [
    COMMETHOD([helpstring(u'Callback for REST resource handling.')], HRESULT, 'HandleResource',
              ( ['in'], BSTR, 'Capabilities' ),
              ( ['in'], BSTR, 'resourceName' ),
              ( ['in'], POINTER(IPropertySet), 'boundVariables' ),
              ( ['in'], BSTR, 'inputJSON' ),
              ( ['in'], BSTR, 'outputFormat' ),
              ( ['in'], POINTER(IJSONObject), 'requestProps' ),
              ( ['out'], POINTER(POINTER(IJSONObject)), 'responseProps' ),
              ( ['out'], POINTER(VARIANT), 'outputData' )),
    COMMETHOD([helpstring(u'Callback for REST operation handling.')], HRESULT, 'HandleOperation',
              ( ['in'], BSTR, 'Capabilities' ),
              ( ['in'], BSTR, 'resourceName' ),
              ( ['in'], BSTR, 'operationName' ),
              ( ['in'], POINTER(IPropertySet), 'boundVariables' ),
              ( ['in'], BSTR, 'inputJSON' ),
              ( ['in'], BSTR, 'outputFormat' ),
              ( ['in'], POINTER(IJSONObject), 'requestProps' ),
              ( ['out'], POINTER(POINTER(IJSONObject)), 'responseProps' ),
              ( ['out'], POINTER(VARIANT), 'outputData' )),
]
################################################################
## code template for IRESTCallback implementation
##class IRESTCallback_Impl(object):
##    def HandleResource(self, Capabilities, resourceName, boundVariables, inputJSON, outputFormat, requestProps):
##        u'Callback for REST resource handling.'
##        #return responseProps, outputData
##
##    def HandleOperation(self, Capabilities, resourceName, operationName, boundVariables, inputJSON, outputFormat, requestProps):
##        u'Callback for REST operation handling.'
##        #return responseProps, outputData
##

class ProxyServerInfo(CoClass):
    u'A utility class for setting proxy server configuration information.'
    _reg_clsid_ = GUID('{F36507F2-7EF4-4119-A449-81998DE36AD1}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
ProxyServerInfo._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IProxyServerInfo, IProxyServerInfo2]

class ILatLonFormat2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that format Latitudes and Longitudes.'
    _iid_ = GUID('{127B0952-E8B4-428C-AC39-58DE4D1F17DE}')
    _idlflags_ = ['oleautomation']
ILatLonFormat2._methods_ = [
    COMMETHOD(['propput', helpstring(u'Indicates if a directional letter (N-S-E-W) is appended to the formatted number.')], HRESULT, 'ShowDirections',
              ( ['in'], VARIANT_BOOL, 'Show' )),
    COMMETHOD(['propget', helpstring(u'Indicates if a directional letter (N-S-E-W) is appended to the formatted number.')], HRESULT, 'ShowDirections',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Show' )),
    COMMETHOD(['propput', helpstring(u'Indicates if a formatted number is a latitude or not.')], HRESULT, 'IsLatitude',
              ( ['in'], VARIANT_BOOL, 'isLat' )),
    COMMETHOD([helpstring(u'Obtains the degrees, minutes, and seconds for a lat/lon number.')], HRESULT, 'GetDMS',
              ( ['in'], c_double, 'Value' ),
              ( ['out'], POINTER(c_int), 'degrees' ),
              ( ['out'], POINTER(c_int), 'Minutes' ),
              ( ['out'], POINTER(c_double), 'Seconds' )),
    COMMETHOD(['propput', helpstring(u'Indicates if zero minutes are included in formatted output.')], HRESULT, 'ShowZeroMinutes',
              ( ['in'], VARIANT_BOOL, 'Show' )),
    COMMETHOD(['propget', helpstring(u'Indicates if zero minutes are included in formatted output.')], HRESULT, 'ShowZeroMinutes',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Show' )),
    COMMETHOD(['propput', helpstring(u'Indicates if zero seconds are included in formatted output.')], HRESULT, 'ShowZeroSeconds',
              ( ['in'], VARIANT_BOOL, 'Show' )),
    COMMETHOD(['propget', helpstring(u'Indicates if zero seconds are included in formatted output.')], HRESULT, 'ShowZeroSeconds',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Show' )),
    COMMETHOD(['propget', helpstring(u'Indicates if a formatted number is a latitude or not.')], HRESULT, 'IsLatitude',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'isLat' )),
]
################################################################
## code template for ILatLonFormat2 implementation
##class ILatLonFormat2_Impl(object):
##    def _get(self):
##        u'Indicates if a formatted number is a latitude or not.'
##        #return isLat
##    def _set(self, isLat):
##        u'Indicates if a formatted number is a latitude or not.'
##    IsLatitude = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if a directional letter (N-S-E-W) is appended to the formatted number.'
##        #return Show
##    def _set(self, Show):
##        u'Indicates if a directional letter (N-S-E-W) is appended to the formatted number.'
##    ShowDirections = property(_get, _set, doc = _set.__doc__)
##
##    def GetDMS(self, Value):
##        u'Obtains the degrees, minutes, and seconds for a lat/lon number.'
##        #return degrees, Minutes, Seconds
##
##    def _get(self):
##        u'Indicates if zero seconds are included in formatted output.'
##        #return Show
##    def _set(self, Show):
##        u'Indicates if zero seconds are included in formatted output.'
##    ShowZeroSeconds = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if zero minutes are included in formatted output.'
##        #return Show
##    def _set(self, Show):
##        u'Indicates if zero minutes are included in formatted output.'
##    ShowZeroMinutes = property(_get, _set, doc = _set.__doc__)
##

class IEnumRESTResource(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'REST resource enumerator.'
    _iid_ = GUID('{7502C3EC-249D-4616-BABB-DA81F7B5C71E}')
    _idlflags_ = ['oleautomation']
class IRESTResource(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'REST resource metadata object.'
    _iid_ = GUID('{B5561EA3-2950-4E21-9E4F-B1003B2A1BAF}')
    _idlflags_ = ['oleautomation']
IEnumRESTResource._methods_ = [
    COMMETHOD([helpstring(u'Resets the enumerator')], HRESULT, 'Reset'),
    COMMETHOD([helpstring(u'Gets next item.')], HRESULT, 'Next',
              ( ['retval', 'out'], POINTER(POINTER(IRESTResource)), 'ppRes' )),
]
################################################################
## code template for IEnumRESTResource implementation
##class IEnumRESTResource_Impl(object):
##    def Reset(self):
##        u'Resets the enumerator'
##        #return 
##
##    def Next(self):
##        u'Gets next item.'
##        #return ppRes
##

class IObjectActivate(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods for activating and deactivating objects.'
    _iid_ = GUID('{E3B78022-143E-4E61-9099-ED319EC061E7}')
    _idlflags_ = ['oleautomation']
IObjectActivate._methods_ = [
    COMMETHOD([helpstring(u'Activates the object.')], HRESULT, 'Activate'),
    COMMETHOD([helpstring(u'Deactivates the object.')], HRESULT, 'Deactivate'),
]
################################################################
## code template for IObjectActivate implementation
##class IObjectActivate_Impl(object):
##    def Deactivate(self):
##        u'Deactivates the object.'
##        #return 
##
##    def Activate(self):
##        u'Activates the object.'
##        #return 
##

class ITimeExtent(ITimeValue):
    _case_insensitive_ = True
    u'Provides access to members that control the Time Extent.'
    _iid_ = GUID('{BD724B95-018F-4367-9883-9560D92293A7}')
    _idlflags_ = ['oleautomation']
ITimeExtent._methods_ = [
    COMMETHOD(['propget', helpstring(u"The time extent's start time.")], HRESULT, 'StartTime',
              ( ['retval', 'out'], POINTER(POINTER(ITime)), 'StartTime' )),
    COMMETHOD(['propput', helpstring(u"The time extent's start time.")], HRESULT, 'StartTime',
              ( ['in'], POINTER(ITime), 'StartTime' )),
    COMMETHOD(['propget', helpstring(u"The time extent's end time.")], HRESULT, 'EndTime',
              ( ['retval', 'out'], POINTER(POINTER(ITime)), 'EndTime' )),
    COMMETHOD(['propput', helpstring(u"The time extent's end time.")], HRESULT, 'EndTime',
              ( ['in'], POINTER(ITime), 'EndTime' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the time extent is empty.')], HRESULT, 'Empty',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Empty' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether the time extent is empty.')], HRESULT, 'Empty',
              ( ['in'], VARIANT_BOOL, 'Empty' )),
    COMMETHOD([helpstring(u'Writes start and end time, with copies of the input time values.')], HRESULT, 'SetExtent',
              ( ['in'], POINTER(ITime), 'StartTime' ),
              ( ['in'], POINTER(ITime), 'EndTime' )),
    COMMETHOD([helpstring(u"Obtains the time extent's time duration.")], HRESULT, 'QueryTimeDuration',
              ( ['retval', 'out'], POINTER(POINTER(ITimeDuration)), 'TimeDuration' )),
    COMMETHOD([helpstring(u'Adjust to ovelap the input time value.')], HRESULT, 'Union',
              ( ['in'], POINTER(ITimeValue), 'otherTimeValue' )),
    COMMETHOD([helpstring(u'Adjust to intersect with the input time value.')], HRESULT, 'Intersect',
              ( ['in'], POINTER(ITimeValue), 'otherTimeValue' )),
]
################################################################
## code template for ITimeExtent implementation
##class ITimeExtent_Impl(object):
##    def Intersect(self, otherTimeValue):
##        u'Adjust to intersect with the input time value.'
##        #return 
##
##    def Union(self, otherTimeValue):
##        u'Adjust to ovelap the input time value.'
##        #return 
##
##    def _get(self):
##        u'Indicates whether the time extent is empty.'
##        #return Empty
##    def _set(self, Empty):
##        u'Indicates whether the time extent is empty.'
##    Empty = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u"The time extent's start time."
##        #return StartTime
##    def _set(self, StartTime):
##        u"The time extent's start time."
##    StartTime = property(_get, _set, doc = _set.__doc__)
##
##    def SetExtent(self, StartTime, EndTime):
##        u'Writes start and end time, with copies of the input time values.'
##        #return 
##
##    def _get(self):
##        u"The time extent's end time."
##        #return EndTime
##    def _set(self, EndTime):
##        u"The time extent's end time."
##    EndTime = property(_get, _set, doc = _set.__doc__)
##
##    def QueryTimeDuration(self):
##        u"Obtains the time extent's time duration."
##        #return TimeDuration
##

class Message(CoClass):
    u'A serializable object that represents a request or response message.'
    _reg_clsid_ = GUID('{5FAC2741-5EF9-47D8-AFB5-5EE5E679143C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
Message._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IMessage, ISupportErrorInfo]

IErrorInfo._methods_ = [
    COMMETHOD([], HRESULT, 'GetGUID',
              ( ['out'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pGuid' )),
    COMMETHOD([], HRESULT, 'GetSource',
              ( ['out'], POINTER(BSTR), 'pBstrSource' )),
    COMMETHOD([], HRESULT, 'GetDescription',
              ( ['out'], POINTER(BSTR), 'pBstrDescription' )),
    COMMETHOD([], HRESULT, 'GetHelpFile',
              ( ['out'], POINTER(BSTR), 'pBstrHelpFile' )),
    COMMETHOD([], HRESULT, 'GetHelpContext',
              ( ['out'], POINTER(c_ulong), 'pdwHelpContext' )),
]
################################################################
## code template for IErrorInfo implementation
##class IErrorInfo_Impl(object):
##    def GetHelpFile(self):
##        '-no docstring-'
##        #return pBstrHelpFile
##
##    def GetDescription(self):
##        '-no docstring-'
##        #return pBstrDescription
##
##    def GetSource(self):
##        '-no docstring-'
##        #return pBstrSource
##
##    def GetGUID(self):
##        '-no docstring-'
##        #return pGuid
##
##    def GetHelpContext(self):
##        '-no docstring-'
##        #return pdwHelpContext
##

class IRESTRequestHandler(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to REST request for SO or SOE.'
    _iid_ = GUID('{9D66A418-D54A-48ED-88BD-043A25FA9C83}')
    _idlflags_ = ['oleautomation']
class IRESTDispatcher(IRESTRequestHandler):
    _case_insensitive_ = True
    u'REST dispatcher object.'
    _iid_ = GUID('{1538E2DC-8192-412E-A801-2B8655492AAE}')
    _idlflags_ = ['oleautomation']
IRESTRequestHandler._methods_ = [
    COMMETHOD([helpstring(u'Handles REST request for SO or SOE.')], HRESULT, 'HandleRESTRequest',
              ( ['in'], BSTR, 'Capabilities' ),
              ( ['in'], BSTR, 'resourceName' ),
              ( ['in'], BSTR, 'operationName' ),
              ( ['in'], BSTR, 'operationInput' ),
              ( ['in'], BSTR, 'outputFormat' ),
              ( ['in'], BSTR, 'requestProperties' ),
              ( ['out'], POINTER(BSTR), 'responseProperties' ),
              ( ['retval', 'out'], POINTER(_midlSAFEARRAY(c_ubyte)), 'responseData' )),
    COMMETHOD([helpstring(u'Obtains REST request schema.')], HRESULT, 'GetSchema',
              ( ['retval', 'out'], POINTER(BSTR), 'schema' )),
]
################################################################
## code template for IRESTRequestHandler implementation
##class IRESTRequestHandler_Impl(object):
##    def GetSchema(self):
##        u'Obtains REST request schema.'
##        #return schema
##
##    def HandleRESTRequest(self, Capabilities, resourceName, operationName, operationInput, outputFormat, requestProperties):
##        u'Handles REST request for SO or SOE.'
##        #return responseProperties, responseData
##

IRESTDispatcher._methods_ = [
    COMMETHOD([helpstring(u'Initialization method.')], HRESULT, 'Init',
              ( ['in'], POINTER(IRESTResource), 'root' ),
              ( [], POINTER(IRESTCallback), 'handler' )),
]
################################################################
## code template for IRESTDispatcher implementation
##class IRESTDispatcher_Impl(object):
##    def Init(self, root, handler):
##        u'Initialization method.'
##        #return 
##

class IChildExtension(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the parent extension of this extension.  Indicates that this extension has a parent extension.'
    _iid_ = GUID('{1D45017C-2A13-4CDF-AFC7-59F9D0C17C71}')
    _idlflags_ = ['oleautomation']
IChildExtension._methods_ = [
    COMMETHOD(['propget', helpstring(u'The parent extension of this extension.')], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(IExtension)), 'Parent' )),
]
################################################################
## code template for IChildExtension implementation
##class IChildExtension_Impl(object):
##    @property
##    def Parent(self):
##        u'The parent extension of this extension.'
##        #return Parent
##

class DirectionFormat(CoClass):
    u'An object for formatting numbers in a direction format.'
    _reg_clsid_ = GUID('{36D7E361-B440-4FEB-B2AC-FEDE1A2FD7A7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class INumberFormat(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that format numbers.'
    _iid_ = GUID('{7E4F470D-8E54-11D2-AAD8-000000000000}')
    _idlflags_ = ['oleautomation']
class INumberFormatOperations(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to common operations on formatted numbers.'
    _iid_ = GUID('{5EF43B7E-3BC1-4B25-A5C0-08218C75BE06}')
    _idlflags_ = ['oleautomation']
DirectionFormat._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, INumberFormat, INumberFormatOperations, IDirectionFormat, IClone, IPersist, IPersistStream]

class IParentExtension(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the child extensions of this extension.  Indicates that this extension has child extensions.'
    _iid_ = GUID('{D3AE4638-5C68-4F1B-AADF-8BEC8DEB4F8B}')
    _idlflags_ = ['oleautomation']
IParentExtension._methods_ = [
    COMMETHOD(['propget', helpstring(u'The number of child extensions.')], HRESULT, 'ChildCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'The indicated child extension.')], HRESULT, 'Child',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IExtension)), 'Child' )),
]
################################################################
## code template for IParentExtension implementation
##class IParentExtension_Impl(object):
##    @property
##    def ChildCount(self):
##        u'The number of child extensions.'
##        #return Count
##
##    @property
##    def Child(self, index):
##        u'The indicated child extension.'
##        #return Child
##

class IAutoExtension(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Indicator interface that identifies an extension that automatically enables and disables as needed.'
    _iid_ = GUID('{A5009874-E58F-42DF-BE62-873A7661ECDF}')
    _idlflags_ = ['oleautomation']
IAutoExtension._methods_ = [
]
################################################################
## code template for IAutoExtension implementation
##class IAutoExtension_Impl(object):

class IEnumNamedID(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that enumerate over a set of named IDs.'
    _iid_ = GUID('{51959A4B-D4A5-11D1-8771-0000F8751720}')
    _idlflags_ = ['oleautomation']
IEnumNamedID._methods_ = [
    COMMETHOD([helpstring(u'Obtains the next name-ID pair in the set.')], HRESULT, 'Next',
              ( ['out'], POINTER(BSTR), 'nextName' ),
              ( ['retval', 'out'], POINTER(c_int), 'identifier' )),
    COMMETHOD([helpstring(u'Resets internal cursor so that the next call to Next returns the first pair in the set.')], HRESULT, 'Reset'),
]
################################################################
## code template for IEnumNamedID implementation
##class IEnumNamedID_Impl(object):
##    def Reset(self):
##        u'Resets internal cursor so that the next call to Next returns the first pair in the set.'
##        #return 
##
##    def Next(self):
##        u'Obtains the next name-ID pair in the set.'
##        #return nextName, identifier
##

class IParentLicenseExtension(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u"Indicator interface that identifies that this parent extension controls the licenses of it's children."
    _iid_ = GUID('{8A1A05F8-1521-435C-9B0E-1F2B148E0AE4}')
    _idlflags_ = ['oleautomation']
IParentLicenseExtension._methods_ = [
]
################################################################
## code template for IParentLicenseExtension implementation
##class IParentLicenseExtension_Impl(object):

class ITimeInstant(ITimeValue):
    _case_insensitive_ = True
    u'Provides access to members that control the Time Instant.'
    _iid_ = GUID('{81899EE9-2E12-4E6C-94F1-2BA31D3CDBC5}')
    _idlflags_ = ['oleautomation']
ITimeInstant._methods_ = [
    COMMETHOD(['propget', helpstring(u'The time instant time value.')], HRESULT, 'Time',
              ( ['retval', 'out'], POINTER(POINTER(ITime)), 'Time' )),
    COMMETHOD(['propput', helpstring(u'The time instant time value.')], HRESULT, 'Time',
              ( ['in'], POINTER(ITime), 'Time' )),
]
################################################################
## code template for ITimeInstant implementation
##class ITimeInstant_Impl(object):
##    def _get(self):
##        u'The time instant time value.'
##        #return Time
##    def _set(self, Time):
##        u'The time instant time value.'
##    Time = property(_get, _set, doc = _set.__doc__)
##

class ITimeZoneFactory(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Time Zone Factory.'
    _iid_ = GUID('{1B4768DD-508E-4946-AB04-E042DFCEB29F}')
    _idlflags_ = ['oleautomation']
ITimeZoneFactory._methods_ = [
    COMMETHOD([helpstring(u'Creates a time zone info from a windows ID.')], HRESULT, 'CreateTimeZoneInfoFromWindowsID',
              ( ['in'], BSTR, 'WindowsID' ),
              ( ['retval', 'out'], POINTER(POINTER(ITimeZoneInfo)), 'TimeZoneInfo' )),
    COMMETHOD([helpstring(u'Creates a time reference from a windows ID.')], HRESULT, 'CreateTimeReferenceFromWindowsID',
              ( ['in'], BSTR, 'WindowsID' ),
              ( ['retval', 'out'], POINTER(POINTER(ITimeReference)), 'TimeReference' )),
    COMMETHOD([helpstring(u'Returns the time zone windows ID that corresponds to the given olson time zone ID.')], HRESULT, 'QueryTimeZoneWindowsIDFromOlsonID',
              ( ['in'], BSTR, 'olsonID' ),
              ( ['retval', 'out'], POINTER(BSTR), 'WindowsID' )),
    COMMETHOD([helpstring(u'Obtains all the olson time zone IDs that correspond to the given time zone windows ID.')], HRESULT, 'QueryTimeZoneOlsonIDsFromWindowsID',
              ( ['in'], BSTR, 'WindowsID' ),
              ( ['retval', 'out'], POINTER(_midlSAFEARRAY(BSTR)), 'olsonIDs' )),
    COMMETHOD([helpstring(u"Obtains the machine's current local time zone Windows ID.")], HRESULT, 'QueryLocalTimeZoneWindowsID',
              ( ['retval', 'out'], POINTER(BSTR), 'localTimeZoneWindowsID' )),
    COMMETHOD(['propget', helpstring(u'The first time zone windows ID.')], HRESULT, 'FirstTimeZoneWindowsID',
              ( ['retval', 'out'], POINTER(BSTR), 'FirstTimeZoneWindowsID' )),
    COMMETHOD(['propget', helpstring(u'The time zone windows ID that cyclicly proceeds the given time zone windows ID.')], HRESULT, 'NextTimeZoneWindowsID',
              ( ['in'], BSTR, 'currentTimeZoneWindowsID' ),
              ( ['retval', 'out'], POINTER(BSTR), 'NextTimeZoneWindowsID' )),
    COMMETHOD(['propget', helpstring(u'The first locale ID.')], HRESULT, 'FirstLocaleID',
              ( ['retval', 'out'], POINTER(c_int), 'FirstLocaleID' )),
    COMMETHOD(['propget', helpstring(u'The locale ID that cyclicly proceeds the given locale ID.')], HRESULT, 'NextLocaleID',
              ( ['in'], c_int, 'currenteLocaleID' ),
              ( ['retval', 'out'], POINTER(c_int), 'NextLocaleID' )),
    COMMETHOD([helpstring(u'Obtains the locale display name that corresponds to the given locale ID.')], HRESULT, 'CreateLocaleInfoFromLocaleID',
              ( ['in'], c_int, 'LocaleID' ),
              ( ['retval', 'out'], POINTER(POINTER(ILocaleInfo)), 'LocaleInfo' )),
    COMMETHOD([helpstring(u'Returns whether a given time zone windows ID is valid for creating a time zone info or a time reference.')], HRESULT, 'IsValidTimeZoneWindowsID',
              ( ['in'], BSTR, 'WindowsID' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'isValid' )),
    COMMETHOD([helpstring(u'Returns whether a given locale ID is valid for creating a locale info.')], HRESULT, 'IsValidLocaleID',
              ( ['in'], c_int, 'LocaleID' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'isValid' )),
]
################################################################
## code template for ITimeZoneFactory implementation
##class ITimeZoneFactory_Impl(object):
##    def IsValidTimeZoneWindowsID(self, WindowsID):
##        u'Returns whether a given time zone windows ID is valid for creating a time zone info or a time reference.'
##        #return isValid
##
##    def QueryLocalTimeZoneWindowsID(self):
##        u"Obtains the machine's current local time zone Windows ID."
##        #return localTimeZoneWindowsID
##
##    @property
##    def NextLocaleID(self, currenteLocaleID):
##        u'The locale ID that cyclicly proceeds the given locale ID.'
##        #return NextLocaleID
##
##    def CreateLocaleInfoFromLocaleID(self, LocaleID):
##        u'Obtains the locale display name that corresponds to the given locale ID.'
##        #return LocaleInfo
##
##    def QueryTimeZoneWindowsIDFromOlsonID(self, olsonID):
##        u'Returns the time zone windows ID that corresponds to the given olson time zone ID.'
##        #return WindowsID
##
##    @property
##    def NextTimeZoneWindowsID(self, currentTimeZoneWindowsID):
##        u'The time zone windows ID that cyclicly proceeds the given time zone windows ID.'
##        #return NextTimeZoneWindowsID
##
##    def QueryTimeZoneOlsonIDsFromWindowsID(self, WindowsID):
##        u'Obtains all the olson time zone IDs that correspond to the given time zone windows ID.'
##        #return olsonIDs
##
##    @property
##    def FirstLocaleID(self):
##        u'The first locale ID.'
##        #return FirstLocaleID
##
##    def IsValidLocaleID(self, LocaleID):
##        u'Returns whether a given locale ID is valid for creating a locale info.'
##        #return isValid
##
##    def CreateTimeReferenceFromWindowsID(self, WindowsID):
##        u'Creates a time reference from a windows ID.'
##        #return TimeReference
##
##    @property
##    def FirstTimeZoneWindowsID(self):
##        u'The first time zone windows ID.'
##        #return FirstTimeZoneWindowsID
##
##    def CreateTimeZoneInfoFromWindowsID(self, WindowsID):
##        u'Creates a time zone info from a windows ID.'
##        #return TimeZoneInfo
##

class IZipArchive(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods and properties to create and manage zip archives.'
    _iid_ = GUID('{55DF03AE-B4F8-4387-B8B5-6FB22B15DDAC}')
    _idlflags_ = ['oleautomation']
IZipArchive._methods_ = [
    COMMETHOD([helpstring(u'Opens an existing archive.')], HRESULT, 'OpenArchive',
              ( ['in'], BSTR, 'archiveName' )),
    COMMETHOD([helpstring(u'Creates a new archive.')], HRESULT, 'CreateArchive',
              ( ['in'], BSTR, 'archiveName' )),
    COMMETHOD([helpstring(u'Closes the archive.')], HRESULT, 'CloseArchive'),
    COMMETHOD([helpstring(u'Compresses a file and adds it to the archive.')], HRESULT, 'AddFile',
              ( ['in'], BSTR, 'inputFile' )),
    COMMETHOD([helpstring(u'Obtains the list of files in the archive.')], HRESULT, 'GetFileNames',
              ( ['retval', 'out'], POINTER(POINTER(IEnumBSTR)), 'FileNames' )),
    COMMETHOD([helpstring(u'Extracts a file from the archive to the output directory.')], HRESULT, 'ExtractFile',
              ( ['in'], BSTR, 'file' ),
              ( ['in'], BSTR, 'outputDir' )),
    COMMETHOD([helpstring(u'Extracts all items in the archive to the output directory.')], HRESULT, 'Extract',
              ( ['in'], BSTR, 'outputDir' )),
]
################################################################
## code template for IZipArchive implementation
##class IZipArchive_Impl(object):
##    def CloseArchive(self):
##        u'Closes the archive.'
##        #return 
##
##    def AddFile(self, inputFile):
##        u'Compresses a file and adds it to the archive.'
##        #return 
##
##    def OpenArchive(self, archiveName):
##        u'Opens an existing archive.'
##        #return 
##
##    def CreateArchive(self, archiveName):
##        u'Creates a new archive.'
##        #return 
##
##    def ExtractFile(self, file, outputDir):
##        u'Extracts a file from the archive to the output directory.'
##        #return 
##
##    def Extract(self, outputDir):
##        u'Extracts all items in the archive to the output directory.'
##        #return 
##
##    def GetFileNames(self):
##        u'Obtains the list of files in the archive.'
##        #return FileNames
##

class CoRESTResource(CoClass):
    u'IRESTResource coclass'
    _reg_clsid_ = GUID('{C5F365F0-9AC8-4872-AFD0-E9383AFF0F2E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
CoRESTResource._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRESTResource]

IExtensionManager._methods_ = [
    COMMETHOD(['propget', helpstring(u'The number of extensions loaded in the application.')], HRESULT, 'ExtensionCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'The extension at the specified index.')], HRESULT, 'Extension',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IExtension)), 'Extension' )),
    COMMETHOD(['propget', helpstring(u'The CLSID of the extension at the specified index.')], HRESULT, 'ExtensionCLSID',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IUID)), 'ClassID' )),
    COMMETHOD([helpstring(u'Finds the extension by CLSID (IUID) or name (String).')], HRESULT, 'FindExtension',
              ( ['in'], VARIANT, 'nameOrID' ),
              ( ['retval', 'out'], POINTER(POINTER(IExtension)), 'Extension' )),
]
################################################################
## code template for IExtensionManager implementation
##class IExtensionManager_Impl(object):
##    def FindExtension(self, nameOrID):
##        u'Finds the extension by CLSID (IUID) or name (String).'
##        #return Extension
##
##    @property
##    def ExtensionCount(self):
##        u'The number of extensions loaded in the application.'
##        #return Count
##
##    @property
##    def ExtensionCLSID(self, index):
##        u'The CLSID of the extension at the specified index.'
##        #return ClassID
##
##    @property
##    def Extension(self, index):
##        u'The extension at the specified index.'
##        #return Extension
##

class ITimeOffsetOperator(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to time operations.'
    _iid_ = GUID('{7CBBB8EA-7708-464A-A6C8-96DB06521B3A}')
    _idlflags_ = ['oleautomation']
ITimeOffsetOperator._methods_ = [
    COMMETHOD([helpstring(u'Adds a time duration.')], HRESULT, 'AddDuration',
              ( ['in'], POINTER(ITimeDuration), 'TimeDuration' )),
    COMMETHOD([helpstring(u'Subtracts a time duration.')], HRESULT, 'SubtractDuration',
              ( ['in'], POINTER(ITimeDuration), 'TimeDuration' )),
    COMMETHOD([helpstring(u'Adds the input amount of years.')], HRESULT, 'AddYears',
              ( ['in'], c_double, 'Value' ),
              ( ['in'], VARIANT_BOOL, 'preserveEndOfMonth' ),
              ( ['in'], VARIANT_BOOL, 'goForwardOnInvalidDate' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'dateWasAdjusted' )),
    COMMETHOD([helpstring(u'Adds the input amount of months.')], HRESULT, 'AddMonths',
              ( ['in'], c_double, 'Value' ),
              ( ['in'], VARIANT_BOOL, 'preserveEndOfMonth' ),
              ( ['in'], VARIANT_BOOL, 'goForwardOnInvalidDate' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'dateWasAdjusted' )),
    COMMETHOD([helpstring(u'Adds the input amount of weeks.')], HRESULT, 'AddWeeks',
              ( ['in'], c_double, 'Value' )),
    COMMETHOD([helpstring(u'Adds the input amount of days.')], HRESULT, 'AddDays',
              ( ['in'], c_double, 'Value' )),
    COMMETHOD([helpstring(u'Adds the input amount of hours.')], HRESULT, 'AddHours',
              ( ['in'], c_double, 'Value' )),
    COMMETHOD([helpstring(u'Adds the input amount of minutes.')], HRESULT, 'AddMinutes',
              ( ['in'], c_double, 'Value' )),
    COMMETHOD([helpstring(u'Adds the input amount of seconds.')], HRESULT, 'AddSeconds',
              ( ['in'], c_double, 'Value' )),
    COMMETHOD([helpstring(u'Adds the input amount of milliseconds.')], HRESULT, 'AddMilliseconds',
              ( ['in'], c_double, 'Value' )),
    COMMETHOD([helpstring(u'Adds the input amount of nanoseconds.')], HRESULT, 'AddNanoseconds',
              ( ['in'], c_longlong, 'Value' )),
]
################################################################
## code template for ITimeOffsetOperator implementation
##class ITimeOffsetOperator_Impl(object):
##    def AddMinutes(self, Value):
##        u'Adds the input amount of minutes.'
##        #return 
##
##    def AddHours(self, Value):
##        u'Adds the input amount of hours.'
##        #return 
##
##    def AddWeeks(self, Value):
##        u'Adds the input amount of weeks.'
##        #return 
##
##    def AddDays(self, Value):
##        u'Adds the input amount of days.'
##        #return 
##
##    def AddMonths(self, Value, preserveEndOfMonth, goForwardOnInvalidDate):
##        u'Adds the input amount of months.'
##        #return dateWasAdjusted
##
##    def AddMilliseconds(self, Value):
##        u'Adds the input amount of milliseconds.'
##        #return 
##
##    def AddSeconds(self, Value):
##        u'Adds the input amount of seconds.'
##        #return 
##
##    def AddNanoseconds(self, Value):
##        u'Adds the input amount of nanoseconds.'
##        #return 
##
##    def AddDuration(self, TimeDuration):
##        u'Adds a time duration.'
##        #return 
##
##    def SubtractDuration(self, TimeDuration):
##        u'Subtracts a time duration.'
##        #return 
##
##    def AddYears(self, Value, preserveEndOfMonth, goForwardOnInvalidDate):
##        u'Adds the input amount of years.'
##        #return dateWasAdjusted
##


# values for enumeration 'esriTextureCompressionType'
esriTextureCompressionNever = 1
esriTextureCompressionNone = 2
esriTextureCompressionJPEG = 3
esriTextureCompressionJPEGPlus = 4
esriTextureCompressionType = c_int # enum

# values for enumeration 'esriCoreErrorReturnCodes'
E_NOTLICENSED = -2147221247
E_NO_PRODUCT_LICENSE = -2147221246
E_NO_EXTENSION_LICENSE = -2147221245
E_REQUIRES_SERVER_STANDARD_EDITION = -2147221244
E_REQUIRES_SERVER_ADVANCED_EDITION = -2147221243
esriCoreErrorReturnCodes = c_int # enum
class CoRESTOperation(CoClass):
    u'IRESTOperation coclass'
    _reg_clsid_ = GUID('{FDA271D6-59E0-40EC-97F2-0CE6A392F12C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
CoRESTOperation._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRESTOperation]

class ZipArchive(CoClass):
    u'The ZipArchive object which manages zip archives.'
    _reg_clsid_ = GUID('{3C1841DB-3625-464F-B216-41811A7E8A6C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
ZipArchive._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IZipArchive]

class IZipArchiveEx(IZipArchive):
    _case_insensitive_ = True
    u'Provides access to methods and properties to create and manage 7-zip archives.'
    _iid_ = GUID('{F088433D-0167-4866-A846-55CAB2FB76B0}')
    _idlflags_ = ['oleautomation']
IZipArchiveEx._methods_ = [
    COMMETHOD([helpstring(u'Compresses a file and adds it to the archive preserving the sub-folder off the root folder.')], HRESULT, 'AddFileEx',
              ( ['in'], BSTR, 'inputFile' ),
              ( ['in'], BSTR, 'rootFolder' )),
    COMMETHOD([helpstring(u'Compress a folder and add it to the archive.')], HRESULT, 'AddFolder',
              ( ['in'], BSTR, 'inputFolder' ),
              ( ['in'], VARIANT_BOOL, 'recursive' )),
]
################################################################
## code template for IZipArchiveEx implementation
##class IZipArchiveEx_Impl(object):
##    def AddFileEx(self, inputFile, rootFolder):
##        u'Compresses a file and adds it to the archive preserving the sub-folder off the root folder.'
##        #return 
##
##    def AddFolder(self, inputFolder, recursive):
##        u'Compress a folder and add it to the archive.'
##        #return 
##

class ITimeZoneFactory2(ITimeZoneFactory):
    _case_insensitive_ = True
    u'Provides access to members that control the Time Zone Factory.'
    _iid_ = GUID('{4CAA06BE-7199-40B3-ADB6-78BAE35D5227}')
    _idlflags_ = ['oleautomation']
ITimeZoneFactory2._methods_ = [
    COMMETHOD([helpstring(u"Obtains the machine's current local time reference. Set exactMatch to true to ensure exact retrieval of a customized machine's local time reference, or to false to obtain a pre-defined time reference, which is the closest match to the machine's current local tZ\xd0?\x08?&")], HRESULT, 'QueryLocalTimeReference',
              ( ['in'], VARIANT_BOOL, 'exactMatch' ),
              ( ['retval', 'out'], POINTER(POINTER(ITimeReference)), 'localTimeReference' )),
    COMMETHOD([helpstring(u'Reload time zones.')], HRESULT, 'ReloadTimeZones',
              ( ['in'], BSTR, 'FileName' )),
    COMMETHOD([helpstring(u'Save time zones.')], HRESULT, 'SaveTimeZones',
              ( ['in'], BSTR, 'FileName' )),
]
################################################################
## code template for ITimeZoneFactory2 implementation
##class ITimeZoneFactory2_Impl(object):
##    def SaveTimeZones(self, FileName):
##        u'Save time zones.'
##        #return 
##
##    def ReloadTimeZones(self, FileName):
##        u'Reload time zones.'
##        #return 
##
##    def QueryLocalTimeReference(self, exactMatch):
##        u"Obtains the machine's current local time reference. Set exactMatch to true to ensure exact retrieval of a customized machine's local time reference, or to false to obtain a pre-defined time reference, which is the closest match to the machine's current local tZ\xd0?\x08?&"
##        #return localTimeReference
##

class CoRESTDispatcher(CoClass):
    u'IRESTDispatcher coclass'
    _reg_clsid_ = GUID('{0D52FCD9-6647-432C-B15B-B141AB0A349F}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
CoRESTDispatcher._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IRESTDispatcher]


# values for enumeration 'esriUnits'
esriUnknownUnits = 0
esriInches = 1
esriPoints = 2
esriFeet = 3
esriYards = 4
esriMiles = 5
esriNauticalMiles = 6
esriMillimeters = 7
esriCentimeters = 8
esriMeters = 9
esriKilometers = 10
esriDecimalDegrees = 11
esriDecimeters = 12
esriUnitsLast = 13
esriUnits = c_int # enum
IExtensionManagerAdmin._methods_ = [
    COMMETHOD([helpstring(u'Creates and starts the extensions for the given component category, passing initializationData to each in IExtension::Startup.')], HRESULT, 'StartupExtensions',
              ( ['in'], POINTER(IUID), 'componentCategory' ),
              ( ['in'], POINTER(IUID), 'jitCategory' ),
              ( ['in'], POINTER(VARIANT), 'initializationData' )),
    COMMETHOD([helpstring(u'Shuts down and releases the extensions that are loaded and calls IExtension::Shutdown.')], HRESULT, 'ShutdownExtensions'),
    COMMETHOD([helpstring(u'Creates a single extension given the CLSID, then passes initializationData to IExtension::Startup.')], HRESULT, 'AddExtension',
              ( ['in'], POINTER(IUID), 'ExtensionCLSID' ),
              ( ['in'], POINTER(VARIANT), 'initializationData' )),
]
################################################################
## code template for IExtensionManagerAdmin implementation
##class IExtensionManagerAdmin_Impl(object):
##    def AddExtension(self, ExtensionCLSID, initializationData):
##        u'Creates a single extension given the CLSID, then passes initializationData to IExtension::Startup.'
##        #return 
##
##    def ShutdownExtensions(self):
##        u'Shuts down and releases the extensions that are loaded and calls IExtension::Shutdown.'
##        #return 
##
##    def StartupExtensions(self, componentCategory, jitCategory, initializationData):
##        u'Creates and starts the extensions for the given component category, passing initializationData to each in IExtension::Startup.'
##        #return 
##

class IZlibCompression(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to compress and uncompress texture data.'
    _iid_ = GUID('{FEE4D81C-25D9-4389-A20C-16821EC90719}')
    _idlflags_ = []
IZlibCompression._methods_ = [
    COMMETHOD(['propget', helpstring(u'Estimated buffer size of compress/uncompress texture data.')], HRESULT, 'BufferSize',
              ( ['in'], c_int, 'Size' ),
              ( ['retval', 'out'], POINTER(c_int), 'pSize' )),
    COMMETHOD([helpstring(u'Compress the current the input buffer. Uses best compression.')], HRESULT, 'Compress',
              ( ['in'], c_int, 'inSize' ),
              ( ['in'], POINTER(c_ubyte), 'pInBuff' ),
              ( ['in', 'out'], POINTER(c_int), 'pOutSize' ),
              ( ['in', 'out'], POINTER(c_ubyte), 'pOutBuff' )),
    COMMETHOD([helpstring(u'Compress the current the input buffer by level.  If level less than 0, use default, if greater than best use best.')], HRESULT, 'CompressByLevel',
              ( ['in'], c_int, 'inSize' ),
              ( ['in'], POINTER(c_ubyte), 'pInBuff' ),
              ( ['in'], c_int, 'level' ),
              ( ['in', 'out'], POINTER(c_int), 'pOutSize' ),
              ( ['in', 'out'], POINTER(c_ubyte), 'pOutBuff' )),
    COMMETHOD([helpstring(u'UnCompress the current the input buffer.')], HRESULT, 'UnCompress',
              ( ['in'], c_int, 'inSize' ),
              ( ['in'], POINTER(c_ubyte), 'pInBuff' ),
              ( ['in', 'out'], POINTER(c_int), 'pOutSize' ),
              ( ['in', 'out'], POINTER(c_ubyte), 'pOutBuff' )),
]
################################################################
## code template for IZlibCompression implementation
##class IZlibCompression_Impl(object):
##    def CompressByLevel(self, inSize, pInBuff, level):
##        u'Compress the current the input buffer by level.  If level less than 0, use default, if greater than best use best.'
##        #return pOutSize, pOutBuff
##
##    @property
##    def BufferSize(self, Size):
##        u'Estimated buffer size of compress/uncompress texture data.'
##        #return pSize
##
##    def Compress(self, inSize, pInBuff):
##        u'Compress the current the input buffer. Uses best compression.'
##        #return pOutSize, pOutBuff
##
##    def UnCompress(self, inSize, pInBuff):
##        u'UnCompress the current the input buffer.'
##        #return pOutSize, pOutBuff
##

class ITextureCompression(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to compress and uncompress texture data.'
    _iid_ = GUID('{B5F3860A-FCE1-4E71-8F12-BC5C6BB0F280}')
    _idlflags_ = []
ITextureCompression._methods_ = [
    COMMETHOD([helpstring(u'Compress the current the input buffer.')], HRESULT, 'CompressTexture',
              ( ['in'], esriTextureCompressionType, 'type' ),
              ( ['in'], c_int, 'width' ),
              ( ['in'], c_int, 'height' ),
              ( ['in'], c_int, 'channels' ),
              ( ['in'], POINTER(c_ubyte), 'pInData' ),
              ( ['out'], POINTER(c_int), 'pByteCount' ),
              ( ['out'], POINTER(POINTER(c_ubyte)), 'ppOutBuff' )),
    COMMETHOD([helpstring(u'UnCompress the current the input buffer.')], HRESULT, 'UnCompressTexture',
              ( ['in'], esriTextureCompressionType, 'type' ),
              ( ['in'], c_int, 'width' ),
              ( ['in'], c_int, 'height' ),
              ( ['in'], c_int, 'channels' ),
              ( ['in'], c_int, 'Size' ),
              ( ['in'], POINTER(c_ubyte), 'pInData' ),
              ( ['out'], POINTER(c_ubyte), 'pOutBuff' )),
    COMMETHOD(['propput', helpstring(u'Compression quality of texture data.')], HRESULT, 'CompressionQuality',
              ( ['in'], c_int, 'quality' )),
    COMMETHOD(['propget', helpstring(u'Compression quality of texture data.')], HRESULT, 'CompressionQuality',
              ( ['retval', 'out'], POINTER(c_int), 'quality' )),
    COMMETHOD([helpstring(u'Free the Compression buffer created in Compress texture.')], HRESULT, 'FreeCompressData',
              ( ['in'], POINTER(c_ubyte), 'pInData' )),
    COMMETHOD(['propget', helpstring(u'Indicates output should be packed in BSQ pixel interleave format.')], HRESULT, 'BSQ',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pBSQ' )),
    COMMETHOD(['propput', helpstring(u'Indicates output should be packed in BSQ pixel interleave format.')], HRESULT, 'BSQ',
              ( ['in'], VARIANT_BOOL, 'pBSQ' )),
]
################################################################
## code template for ITextureCompression implementation
##class ITextureCompression_Impl(object):
##    def CompressTexture(self, type, width, height, channels, pInData):
##        u'Compress the current the input buffer.'
##        #return pByteCount, ppOutBuff
##
##    def UnCompressTexture(self, type, width, height, channels, Size, pInData):
##        u'UnCompress the current the input buffer.'
##        #return pOutBuff
##
##    def _get(self):
##        u'Indicates output should be packed in BSQ pixel interleave format.'
##        #return pBSQ
##    def _set(self, pBSQ):
##        u'Indicates output should be packed in BSQ pixel interleave format.'
##    BSQ = property(_get, _set, doc = _set.__doc__)
##
##    def FreeCompressData(self, pInData):
##        u'Free the Compression buffer created in Compress texture.'
##        #return 
##
##    def _get(self):
##        u'Compression quality of texture data.'
##        #return quality
##    def _set(self, quality):
##        u'Compression quality of texture data.'
##    CompressionQuality = property(_get, _set, doc = _set.__doc__)
##

class IArray2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to replace an object in the array.'
    _iid_ = GUID('{C4B2BFC5-EB46-4909-801C-C32A6EDE120D}')
    _idlflags_ = ['oleautomation']
IArray2._methods_ = [
    COMMETHOD([helpstring(u'Replaces an object in the array.')], HRESULT, 'Replace',
              ( ['in'], c_int, 'index' ),
              ( ['in'], POINTER(IUnknown), 'unk' )),
]
################################################################
## code template for IArray2 implementation
##class IArray2_Impl(object):
##    def Replace(self, index, unk):
##        u'Replaces an object in the array.'
##        #return 
##

IMemoryBlobStreamVariant._methods_ = [
    COMMETHOD([helpstring(u'Copies the memory to a variant that contains an array of bytes.')], HRESULT, 'ExportToVariant',
              ( ['out'], POINTER(VARIANT), 'Value' )),
    COMMETHOD([helpstring(u'Imports from the array of bytes in the variant.')], HRESULT, 'ImportFromVariant',
              ( ['in'], VARIANT, 'Value' )),
]
################################################################
## code template for IMemoryBlobStreamVariant implementation
##class IMemoryBlobStreamVariant_Impl(object):
##    def ExportToVariant(self):
##        u'Copies the memory to a variant that contains an array of bytes.'
##        #return Value
##
##    def ImportFromVariant(self, Value):
##        u'Imports from the array of bytes in the variant.'
##        #return 
##

IJobInfo._methods_ = [
    COMMETHOD(['propget', helpstring(u'Job description.')], HRESULT, 'Description',
              ( ['retval', 'out'], POINTER(BSTR), 'desc' )),
    COMMETHOD(['propput', helpstring(u'Job description.')], HRESULT, 'Description',
              ( ['in'], BSTR, 'desc' )),
    COMMETHOD(['propget', helpstring(u'Name of the user who submitted the job.')], HRESULT, 'SubmittedBy',
              ( ['retval', 'out'], POINTER(BSTR), 'UserName' )),
    COMMETHOD(['propput', helpstring(u'Name of the user who submitted the job.')], HRESULT, 'SubmittedBy',
              ( ['in'], BSTR, 'UserName' )),
    COMMETHOD(['propget', helpstring(u'Time when the job was submitted.')], HRESULT, 'SubmittingTime',
              ( ['retval', 'out'], POINTER(c_double), 'Time' )),
    COMMETHOD(['propput', helpstring(u'Time when the job was submitted.')], HRESULT, 'SubmittingTime',
              ( ['in'], c_double, 'Time' )),
    COMMETHOD(['propget', helpstring(u'Time when the job execution started.')], HRESULT, 'StartingTime',
              ( ['retval', 'out'], POINTER(c_double), 'Time' )),
    COMMETHOD(['propput', helpstring(u'Time when the job execution started.')], HRESULT, 'StartingTime',
              ( ['in'], c_double, 'Time' )),
    COMMETHOD(['propget', helpstring(u'Time when job execution ended.')], HRESULT, 'EndingTime',
              ( ['retval', 'out'], POINTER(c_double), 'Time' )),
    COMMETHOD(['propput', helpstring(u'Time when job execution ended.')], HRESULT, 'EndingTime',
              ( ['in'], c_double, 'Time' )),
]
################################################################
## code template for IJobInfo implementation
##class IJobInfo_Impl(object):
##    def _get(self):
##        u'Time when the job was submitted.'
##        #return Time
##    def _set(self, Time):
##        u'Time when the job was submitted.'
##    SubmittingTime = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Time when the job execution started.'
##        #return Time
##    def _set(self, Time):
##        u'Time when the job execution started.'
##    StartingTime = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Time when job execution ended.'
##        #return Time
##    def _set(self, Time):
##        u'Time when job execution ended.'
##    EndingTime = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Job description.'
##        #return desc
##    def _set(self, desc):
##        u'Job description.'
##    Description = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Name of the user who submitted the job.'
##        #return UserName
##    def _set(self, UserName):
##        u'Name of the user who submitted the job.'
##    SubmittedBy = property(_get, _set, doc = _set.__doc__)
##

class CurrencyFormat(CoClass):
    u'An object for formatting numbers in a currency format.'
    _reg_clsid_ = GUID('{7E4F471A-8E54-11D2-AAD8-000000000000}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
CurrencyFormat._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, INumberFormat, INumberFormatOperations, IClone, IPersist, IPersistStream]

ISSLInfo._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates whether or not to verify the peer.')], HRESULT, 'VerifyPeer',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bVerifyPeer' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether or not to verify the peer.')], HRESULT, 'VerifyPeer',
              ( ['in'], VARIANT_BOOL, 'bVerifyPeer' )),
    COMMETHOD(['propget', helpstring(u'Path to certificate bundle.')], HRESULT, 'CertPath',
              ( ['retval', 'out'], POINTER(BSTR), 'CertPath' )),
    COMMETHOD(['propput', helpstring(u'Path to certificate bundle.')], HRESULT, 'CertPath',
              ( ['in'], BSTR, 'CertPath' )),
    COMMETHOD([helpstring(u'Read HTTPs configuration from the registry.')], HRESULT, 'ReadSSLInfo'),
    COMMETHOD([helpstring(u'Write HTTPs configuration to the registry.')], HRESULT, 'WriteSSLInfo'),
]
################################################################
## code template for ISSLInfo implementation
##class ISSLInfo_Impl(object):
##    def _get(self):
##        u'Indicates whether or not to verify the peer.'
##        #return bVerifyPeer
##    def _set(self, bVerifyPeer):
##        u'Indicates whether or not to verify the peer.'
##    VerifyPeer = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Path to certificate bundle.'
##        #return CertPath
##    def _set(self, CertPath):
##        u'Path to certificate bundle.'
##    CertPath = property(_get, _set, doc = _set.__doc__)
##
##    def ReadSSLInfo(self):
##        u'Read HTTPs configuration from the registry.'
##        #return 
##
##    def WriteSSLInfo(self):
##        u'Write HTTPs configuration to the registry.'
##        #return 
##

class PercentageFormat(CoClass):
    u'An object for formatting numbers in a percentage format.'
    _reg_clsid_ = GUID('{7E4F471B-8E54-11D2-AAD8-000000000000}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
PercentageFormat._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, INumberFormat, INumericFormat, IPercentageFormat, INumberFormatOperations, IClone, IPersist, IPersistStream]

class LatLonFormat(CoClass):
    u'An object for formatting numbers in a lat/lon format.'
    _reg_clsid_ = GUID('{7E4F471D-8E54-11D2-AAD8-000000000000}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
LatLonFormat._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, INumberFormat, INumericFormat, INumberFormatOperations, ILatLonFormat, ILatLonFormat2, IClone, IPersist, IPersistStream]

IPropertySet2._methods_ = [
    COMMETHOD([helpstring(u'True if the property set is the same as the input property set.')], HRESULT, 'IsEqualNoCase',
              ( ['in'], POINTER(IPropertySet), 'PropertySet' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsEqual' )),
]
################################################################
## code template for IPropertySet2 implementation
##class IPropertySet2_Impl(object):
##    def IsEqualNoCase(self, PropertySet):
##        u'True if the property set is the same as the input property set.'
##        #return IsEqual
##

IUID._methods_ = [
    COMMETHOD([dispid(0), helpstring(u'The value of the UID object.'), 'propget'], HRESULT, 'Value',
              ( ['retval', 'out'], POINTER(VARIANT), 'guidAsString' )),
    COMMETHOD([dispid(0), helpstring(u'The value of the UID object.'), 'propput'], HRESULT, 'Value',
              ( ['in'], VARIANT, 'guidAsString' )),
    COMMETHOD([dispid(1), helpstring(u'Creates a new globally unique value for the UID object.')], HRESULT, 'Generate'),
    COMMETHOD([dispid(2), helpstring(u'The subtype of the UID object.'), 'propget'], HRESULT, 'SubType',
              ( ['retval', 'out'], POINTER(c_int), 'SubType' )),
    COMMETHOD([dispid(2), helpstring(u'The subtype of the UID object.'), 'propput'], HRESULT, 'SubType',
              ( ['in'], c_int, 'SubType' )),
    COMMETHOD([dispid(3), helpstring(u'Indicates if the two UID objects represent the same globally unique identifier.')], HRESULT, 'Compare',
              ( ['in'], POINTER(IUID), 'otherID' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bEqual' )),
]
################################################################
## code template for IUID implementation
##class IUID_Impl(object):
##    def _get(self):
##        u'The subtype of the UID object.'
##        #return SubType
##    def _set(self, SubType):
##        u'The subtype of the UID object.'
##    SubType = property(_get, _set, doc = _set.__doc__)
##
##    def Compare(self, otherID):
##        u'Indicates if the two UID objects represent the same globally unique identifier.'
##        #return bEqual
##
##    def Generate(self):
##        u'Creates a new globally unique value for the UID object.'
##        #return 
##
##    def _get(self):
##        u'The value of the UID object.'
##        #return guidAsString
##    def _set(self, guidAsString):
##        u'The value of the UID object.'
##    Value = property(_get, _set, doc = _set.__doc__)
##

class ITrackCancel(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that control the Cancel Tracker.'
    _iid_ = GUID('{34C20005-4D3C-11D0-92D8-00805F7C28B0}')
    _idlflags_ = ['oleautomation']
class ITrackCancel2(ITrackCancel):
    _case_insensitive_ = True
    u'Provides access to members that control the Cancel Tracker.'
    _iid_ = GUID('{73F93CBA-5D93-4D2D-B27E-30EEB4CA3B64}')
    _idlflags_ = ['oleautomation']
ITrackCancel._methods_ = [
    COMMETHOD(['propput', helpstring(u'The interval at which the operation will be interrupted to advance progressors and process messages.')], HRESULT, 'CheckTime',
              ( ['in'], c_int, 'Milliseconds' )),
    COMMETHOD(['propget', helpstring(u'The interval at which the operation will be interrupted to advance progressors and process messages.')], HRESULT, 'CheckTime',
              ( ['retval', 'out'], POINTER(c_int), 'Milliseconds' )),
    COMMETHOD(['propput', helpstring(u'The progressor used to show progress during lengthy operations.')], HRESULT, 'Progressor',
              ( ['in'], POINTER(IProgressor), 'Progressor' )),
    COMMETHOD(['propget', helpstring(u'The progressor used to show progress during lengthy operations.')], HRESULT, 'Progressor',
              ( ['retval', 'out'], POINTER(POINTER(IProgressor)), 'Progressor' )),
    COMMETHOD([helpstring(u'Cancels the associated operation.')], HRESULT, 'Cancel'),
    COMMETHOD([helpstring(u'Resets the manager after the associated operation is finished.')], HRESULT, 'Reset'),
    COMMETHOD([helpstring(u'Called frequently while associated operation is progressing. A return value of false indicates that the operation should stop.')], HRESULT, 'Continue',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'keepGoing' )),
    COMMETHOD(['propput', helpstring(u'An obsolete method.')], HRESULT, 'ProcessMessages',
              ( ['in'], VARIANT_BOOL, 'ProcessMessages' )),
    COMMETHOD(['propget', helpstring(u'An obsolete method.')], HRESULT, 'ProcessMessages',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ProcessMessages' )),
    COMMETHOD([helpstring(u'An obsolete method.')], HRESULT, 'StartTimer',
              ( ['in'], c_int, 'hWnd' ),
              ( ['in'], c_int, 'Milliseconds' )),
    COMMETHOD(['propget', helpstring(u'An obsolete method.')], HRESULT, 'TimerFired',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'TimerFired' )),
    COMMETHOD([helpstring(u'An obsolete method.')], HRESULT, 'StopTimer'),
    COMMETHOD(['propget', helpstring(u'Indicates whether mouse clicks should cancel the operation.')], HRESULT, 'CancelOnClick',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pCancelOnClick' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether mouse clicks should cancel the operation.')], HRESULT, 'CancelOnClick',
              ( ['in'], VARIANT_BOOL, 'pCancelOnClick' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the escape key and spacebar should cancel the operation.')], HRESULT, 'CancelOnKeyPress',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pCancelOnKeyPress' )),
    COMMETHOD(['propput', helpstring(u'Indicates whether the escape key and spacebar should cancel the operation.')], HRESULT, 'CancelOnKeyPress',
              ( ['in'], VARIANT_BOOL, 'pCancelOnKeyPress' )),
]
################################################################
## code template for ITrackCancel implementation
##class ITrackCancel_Impl(object):
##    def Reset(self):
##        u'Resets the manager after the associated operation is finished.'
##        #return 
##
##    def _get(self):
##        u'An obsolete method.'
##        #return ProcessMessages
##    def _set(self, ProcessMessages):
##        u'An obsolete method.'
##    ProcessMessages = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The interval at which the operation will be interrupted to advance progressors and process messages.'
##        #return Milliseconds
##    def _set(self, Milliseconds):
##        u'The interval at which the operation will be interrupted to advance progressors and process messages.'
##    CheckTime = property(_get, _set, doc = _set.__doc__)
##
##    def StartTimer(self, hWnd, Milliseconds):
##        u'An obsolete method.'
##        #return 
##
##    def StopTimer(self):
##        u'An obsolete method.'
##        #return 
##
##    @property
##    def TimerFired(self):
##        u'An obsolete method.'
##        #return TimerFired
##
##    def _get(self):
##        u'The progressor used to show progress during lengthy operations.'
##        #return Progressor
##    def _set(self, Progressor):
##        u'The progressor used to show progress during lengthy operations.'
##    Progressor = property(_get, _set, doc = _set.__doc__)
##
##    def Continue(self):
##        u'Called frequently while associated operation is progressing. A return value of false indicates that the operation should stop.'
##        #return keepGoing
##
##    def _get(self):
##        u'Indicates whether the escape key and spacebar should cancel the operation.'
##        #return pCancelOnKeyPress
##    def _set(self, pCancelOnKeyPress):
##        u'Indicates whether the escape key and spacebar should cancel the operation.'
##    CancelOnKeyPress = property(_get, _set, doc = _set.__doc__)
##
##    def Cancel(self):
##        u'Cancels the associated operation.'
##        #return 
##
##    def _get(self):
##        u'Indicates whether mouse clicks should cancel the operation.'
##        #return pCancelOnClick
##    def _set(self, pCancelOnClick):
##        u'Indicates whether mouse clicks should cancel the operation.'
##    CancelOnClick = property(_get, _set, doc = _set.__doc__)
##

ITrackCancel2._methods_ = [
    COMMETHOD(['propput', helpstring(u'The time out in ms interval for a lengthy operation. The negative value means no timeout.')], HRESULT, 'Timeout',
              ( ['in'], c_int, 'timeoutMS' )),
    COMMETHOD(['propget', helpstring(u'The time out in ms interval for a lengthy operation. The negative value means no timeout.')], HRESULT, 'Timeout',
              ( ['retval', 'out'], POINTER(c_int), 'timeoutMS' )),
    COMMETHOD([helpstring(u'Turns on/off tracking of mouse movements. If bYesNo is true, the cancel is triggered by the mouse move.')], HRESULT, 'TrackMouseMove',
              ( ['in'], VARIANT_BOOL, 'bYesNo' )),
    COMMETHOD([helpstring(u'Turns on/off tracking of navigation keys. If bYesNo is true, the cancel is triggered by the navigation key press.')], HRESULT, 'TrackNavigationKeys',
              ( ['in'], VARIANT_BOOL, 'bYesNo' )),
]
################################################################
## code template for ITrackCancel2 implementation
##class ITrackCancel2_Impl(object):
##    def TrackNavigationKeys(self, bYesNo):
##        u'Turns on/off tracking of navigation keys. If bYesNo is true, the cancel is triggered by the navigation key press.'
##        #return 
##
##    def TrackMouseMove(self, bYesNo):
##        u'Turns on/off tracking of mouse movements. If bYesNo is true, the cancel is triggered by the mouse move.'
##        #return 
##
##    def _get(self):
##        u'The time out in ms interval for a lengthy operation. The negative value means no timeout.'
##        #return timeoutMS
##    def _set(self, timeoutMS):
##        u'The time out in ms interval for a lengthy operation. The negative value means no timeout.'
##    Timeout = property(_get, _set, doc = _set.__doc__)
##

class ProductInstalled(CoClass):
    u'Class checks the installed ArcGIS products on the machine.'
    _reg_clsid_ = GUID('{872135D9-837D-48D6-8D25-81E874D8AE82}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class IProductInstalled(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to check what ArcGIS product installed on the machine.'
    _iid_ = GUID('{673B47DC-3CDF-4131-BA1B-5261CD171EF7}')
    _idlflags_ = ['oleautomation']
ProductInstalled._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IProductInstalled]

class ScientificFormat(CoClass):
    u'An object for formatting numbers in a scientific format.'
    _reg_clsid_ = GUID('{7E4F471F-8E54-11D2-AAD8-000000000000}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class IScientificNumberFormat(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that format scientific numbers.'
    _iid_ = GUID('{D4F5C355-76B8-11D3-9FC3-00C04F6BC78E}')
    _idlflags_ = ['oleautomation']
ScientificFormat._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, INumberFormat, INumberFormatOperations, IScientificNumberFormat, IClone, IPersist, IPersistStream]

class RateFormat(CoClass):
    u'An object for formatting numbers in a rate format.'
    _reg_clsid_ = GUID('{7E4F4721-8E54-11D2-AAD8-000000000000}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class IRateFormat(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that format rates.'
    _iid_ = GUID('{7E4F4717-8E54-11D2-AAD8-000000000000}')
    _idlflags_ = ['oleautomation']
RateFormat._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, INumberFormat, INumericFormat, INumberFormatOperations, IRateFormat, IClone, IPersist, IPersistStream]

ILongArray._methods_ = [
    COMMETHOD(['propget', helpstring(u'The number of elements in the array.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'pCount' )),
    COMMETHOD([helpstring(u'Removes an element from the array.')], HRESULT, 'Remove',
              ( ['in'], c_int, 'index' )),
    COMMETHOD([helpstring(u'Removes all elements from the array.')], HRESULT, 'RemoveAll'),
    COMMETHOD(['propget', helpstring(u'An element in the array.')], HRESULT, 'Element',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(c_int), 'pElement' )),
    COMMETHOD(['propput', helpstring(u'An element in the array.')], HRESULT, 'Element',
              ( ['in'], c_int, 'index' ),
              ( ['in'], c_int, 'pElement' )),
    COMMETHOD([helpstring(u'Adds an element to the array.')], HRESULT, 'Add',
              ( ['in'], c_int, 'Element' )),
    COMMETHOD([helpstring(u'Inserts an element to the array.')], HRESULT, 'Insert',
              ( ['in'], c_int, 'index' ),
              ( ['in'], c_int, 'Element' )),
]
################################################################
## code template for ILongArray implementation
##class ILongArray_Impl(object):
##    @property
##    def Count(self):
##        u'The number of elements in the array.'
##        #return pCount
##
##    def Insert(self, index, Element):
##        u'Inserts an element to the array.'
##        #return 
##
##    def Remove(self, index):
##        u'Removes an element from the array.'
##        #return 
##
##    def _get(self, index):
##        u'An element in the array.'
##        #return pElement
##    def _set(self, index, pElement):
##        u'An element in the array.'
##    Element = property(_get, _set, doc = _set.__doc__)
##
##    def RemoveAll(self):
##        u'Removes all elements from the array.'
##        #return 
##
##    def Add(self, Element):
##        u'Adds an element to the array.'
##        #return 
##

class IPropertySupport(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that set a default property on an object.'
    _iid_ = GUID('{8A11AD55-2F4F-11D3-9FA0-00C04F6BC6A5}')
    _idlflags_ = ['oleautomation']
IPropertySupport._methods_ = [
    COMMETHOD([helpstring(u'Indicates if the receiver can apply the given object at any given time.')], HRESULT, 'Applies',
              ( ['in'], POINTER(IUnknown), 'pUnk' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Applies' )),
    COMMETHOD([helpstring(u'Indicates if the receiver can apply the given object at that particular moment.')], HRESULT, 'CanApply',
              ( ['in'], POINTER(IUnknown), 'pUnk' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'CanApply' )),
    COMMETHOD(['propget', helpstring(u'The object currently being used.')], HRESULT, 'Current',
              ( ['in'], POINTER(IUnknown), 'pUnk' ),
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'currentObject' )),
    COMMETHOD([helpstring(u'Applies the given property to the receiver and returns the old object.')], HRESULT, 'Apply',
              ( ['in'], POINTER(IUnknown), 'newObject' ),
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'oldObject' )),
]
################################################################
## code template for IPropertySupport implementation
##class IPropertySupport_Impl(object):
##    @property
##    def Current(self, pUnk):
##        u'The object currently being used.'
##        #return currentObject
##
##    def Apply(self, newObject):
##        u'Applies the given property to the receiver and returns the old object.'
##        #return oldObject
##
##    def CanApply(self, pUnk):
##        u'Indicates if the receiver can apply the given object at that particular moment.'
##        #return CanApply
##
##    def Applies(self, pUnk):
##        u'Indicates if the receiver can apply the given object at any given time.'
##        #return Applies
##

IVariantArray._methods_ = [
    COMMETHOD(['propget', helpstring(u'The element count.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'An element in the array.')], HRESULT, 'Element',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'Element' )),
    COMMETHOD(['propput', helpstring(u'An element in the array.')], HRESULT, 'Element',
              ( ['in'], c_int, 'index' ),
              ( ['in'], VARIANT, 'Element' )),
    COMMETHOD([helpstring(u'Removes element at the specified position.')], HRESULT, 'Remove',
              ( ['in'], c_int, 'index' )),
    COMMETHOD([helpstring(u'Removes all elements.')], HRESULT, 'RemoveAll'),
    COMMETHOD([helpstring(u'Add an element.')], HRESULT, 'Add',
              ( ['in'], VARIANT, 'Element' )),
    COMMETHOD([helpstring(u'Add an element at the specified posiiton.')], HRESULT, 'Insert',
              ( ['in'], c_int, 'index' ),
              ( ['in'], VARIANT, 'Element' )),
]
################################################################
## code template for IVariantArray implementation
##class IVariantArray_Impl(object):
##    @property
##    def Count(self):
##        u'The element count.'
##        #return Count
##
##    def Insert(self, index, Element):
##        u'Add an element at the specified posiiton.'
##        #return 
##
##    def Remove(self, index):
##        u'Removes element at the specified position.'
##        #return 
##
##    def _get(self, index):
##        u'An element in the array.'
##        #return Element
##    def _set(self, index, Element):
##        u'An element in the array.'
##    Element = property(_get, _set, doc = _set.__doc__)
##
##    def RemoveAll(self):
##        u'Removes all elements.'
##        #return 
##
##    def Add(self, Element):
##        u'Add an element.'
##        #return 
##

IRateFormat._methods_ = [
    COMMETHOD(['propput', helpstring(u'The rate factor applied to the ValueToSring and StringToValue methods.')], HRESULT, 'RateFactor',
              ( ['in'], c_double, 'factor' )),
    COMMETHOD(['propget', helpstring(u'The rate factor applied to the ValueToSring and StringToValue methods.')], HRESULT, 'RateFactor',
              ( ['retval', 'out'], POINTER(c_double), 'factor' )),
    COMMETHOD(['propput', helpstring(u'The label appended to the formatted rate number.')], HRESULT, 'RateString',
              ( ['in'], BSTR, 'str' )),
    COMMETHOD(['propget', helpstring(u'The label appended to the formatted rate number.')], HRESULT, 'RateString',
              ( ['retval', 'out'], POINTER(BSTR), 'str' )),
]
################################################################
## code template for IRateFormat implementation
##class IRateFormat_Impl(object):
##    def _get(self):
##        u'The label appended to the formatted rate number.'
##        #return str
##    def _set(self, str):
##        u'The label appended to the formatted rate number.'
##    RateString = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The rate factor applied to the ValueToSring and StringToValue methods.'
##        #return factor
##    def _set(self, factor):
##        u'The rate factor applied to the ValueToSring and StringToValue methods.'
##    RateFactor = property(_get, _set, doc = _set.__doc__)
##

class CustomNumberFormat(CoClass):
    u'An object for formatting numbers in a user-defined format.'
    _reg_clsid_ = GUID('{7E4F4722-8E54-11D2-AAD8-000000000000}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
CustomNumberFormat._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, INumberFormat, ICustomNumberFormat, INumberFormatOperations, IClone, IPersist, IPersistStream]

class Time(CoClass):
    u'An object that represents a date and time value.'
    _reg_clsid_ = GUID('{E1721810-8210-45B1-8590-FC4C911FBA20}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
Time._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ITime, ITime2, ITimeOffsetOperator, IXMLSerialize, IXMLVersionSupport, IClone, IPersistStream, IDocumentVersionSupportGEN]

class IAngleFormat(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that format angles.'
    _iid_ = GUID('{7E4F4716-8E54-11D2-AAD8-000000000000}')
    _idlflags_ = ['oleautomation']
IAngleFormat._methods_ = [
    COMMETHOD(['propput', helpstring(u'Indicates if the ValueToString argument is in degrees.')], HRESULT, 'AngleInDegrees',
              ( ['in'], VARIANT_BOOL, 'deg' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the ValueToString argument is in degrees.')], HRESULT, 'AngleInDegrees',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'deg' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the formatted number is an angle in degrees.')], HRESULT, 'DisplayDegrees',
              ( ['in'], VARIANT_BOOL, 'deg' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the formatted number is an angle in degrees.')], HRESULT, 'DisplayDegrees',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'deg' )),
]
################################################################
## code template for IAngleFormat implementation
##class IAngleFormat_Impl(object):
##    def _get(self):
##        u'Indicates if the formatted number is an angle in degrees.'
##        #return deg
##    def _set(self, deg):
##        u'Indicates if the formatted number is an angle in degrees.'
##    DisplayDegrees = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates if the ValueToString argument is in degrees.'
##        #return deg
##    def _set(self, deg):
##        u'Indicates if the ValueToString argument is in degrees.'
##    AngleInDegrees = property(_get, _set, doc = _set.__doc__)
##


# values for enumeration 'esriProductInstalled'
esriProductsInstalledDesktop = 10
esriProductsInstalledEngineRuntime = 20
esriProductsInstalledReader = 30
esriProductsInstalledServerNET = 40
esriProductsInstalledServerJAVA = 50
esriProductInstalled = c_int # enum
IProductInstalled._methods_ = [
    COMMETHOD([helpstring(u'Check if the Product is installed on the machine.')], HRESULT, 'IsProductInstalled',
              ( ['in'], esriProductInstalled, 'ProductInstalled' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bInstalled' )),
]
################################################################
## code template for IProductInstalled implementation
##class IProductInstalled_Impl(object):
##    def IsProductInstalled(self, ProductInstalled):
##        u'Check if the Product is installed on the machine.'
##        #return bInstalled
##

IObjectStream._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The aggregated stream object.')], HRESULT, 'Stream',
              ( ['in'], POINTER(IStream), 'ppStream' )),
    COMMETHOD(['propget', helpstring(u'The aggregated stream object.')], HRESULT, 'Stream',
              ( ['retval', 'out'], POINTER(POINTER(IStream)), 'ppStream' )),
    COMMETHOD([helpstring(u'Store an object to the specified stream.  The first time the object is stored, the full object is written to the stream.  When the object is subsequently stored, a reference is stored.')], HRESULT, 'SaveObject',
              ( ['in'], POINTER(IUnknown), 'pUnk' )),
    COMMETHOD([helpstring(u'Load an object from the specified stream.  The first time an object is encountered, it is loaded from the stream.  When subsequent references to the object are loaded, a pointer to the first object is returned.')], HRESULT, 'LoadObject',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'riid' ),
              ( ['in'], POINTER(IUnknown), 'pUnkOuter' ),
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'ppUnk' )),
    COMMETHOD([helpstring(u'Replaces the current object with the object in the the specified stream.')], HRESULT, 'ReplaceObject',
              ( ['in'], POINTER(IUnknown), 'unknown' )),
    COMMETHOD(['propput', helpstring(u'The software version for the stream.')], HRESULT, 'Version',
              ( ['in'], BSTR, 'versionSpecifier' )),
    COMMETHOD(['propget', helpstring(u'The software version for the stream.')], HRESULT, 'Version',
              ( ['retval', 'out'], POINTER(BSTR), 'versionSpecifier' )),
]
################################################################
## code template for IObjectStream implementation
##class IObjectStream_Impl(object):
##    def ReplaceObject(self, unknown):
##        u'Replaces the current object with the object in the the specified stream.'
##        #return 
##
##    def LoadObject(self, riid, pUnkOuter):
##        u'Load an object from the specified stream.  The first time an object is encountered, it is loaded from the stream.  When subsequent references to the object are loaded, a pointer to the first object is returned.'
##        #return ppUnk
##
##    def SaveObject(self, pUnk):
##        u'Store an object to the specified stream.  The first time the object is stored, the full object is written to the stream.  When the object is subsequently stored, a reference is stored.'
##        #return 
##
##    def _get(self):
##        u'The software version for the stream.'
##        #return versionSpecifier
##    def _set(self, versionSpecifier):
##        u'The software version for the stream.'
##    Version = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Stream(self, ppStream):
##        u'The aggregated stream object.'
##        #return 
##

class IXMLSerializeData2(IXMLSerializeData):
    _case_insensitive_ = True
    u'Provides access to members that serialize and deserialize data from XML.'
    _iid_ = GUID('{E9A0F087-F1F7-455B-9489-FF34E16B9CC7}')
    _idlflags_ = ['oleautomation']
IXMLSerializeData2._methods_ = [
    COMMETHOD([helpstring(u'Adds element value as an int64.')], HRESULT, 'AddInt64',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], c_longlong, 'Value' )),
    COMMETHOD([helpstring(u'Obtains element value as an int64.')], HRESULT, 'GetInt64',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(c_longlong), 'Value' )),
]
################################################################
## code template for IXMLSerializeData2 implementation
##class IXMLSerializeData2_Impl(object):
##    def AddInt64(self, Name, Value):
##        u'Adds element value as an int64.'
##        #return 
##
##    def GetInt64(self, index):
##        u'Obtains element value as an int64.'
##        #return Value
##

class TimeInstant(CoClass):
    u'An object that represents a time-referenced instant in time.'
    _reg_clsid_ = GUID('{06BD7287-0785-4294-BD72-F2933B7FD00D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
class ITimeRelationalOperator(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to time operations.'
    _iid_ = GUID('{7CFFA76A-6552-4516-8599-98225065249E}')
    _idlflags_ = ['oleautomation']
TimeInstant._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ITimeInstant, ITimeValue, ITimeRelationalOperator, ITimeOffsetOperator, IXMLSerialize, IXMLVersionSupport, IClone, IPersistStream, IDocumentVersionSupportGEN]

class TimeExtent(CoClass):
    u'An object that represents a time-referenced time extent.'
    _reg_clsid_ = GUID('{5DC783DE-283A-4963-AB53-25A05C5D76CC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
TimeExtent._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ITimeExtent, ITimeValue, ITimeRelationalOperator, ITimeOffsetOperator, IXMLSerialize, IXMLVersionSupport, IClone, IPersistStream, IDocumentVersionSupportGEN]

class TimeZoneRule(CoClass):
    u'An object that represents a time zone dynamic adjustments rule.'
    _reg_clsid_ = GUID('{1897B0EF-94DA-4037-8156-145D63CD480D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
TimeZoneRule._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ITimeZoneRule, IXMLSerialize, IXMLVersionSupport, IClone, IPersistStream, IDocumentVersionSupportGEN]

IFileNames._methods_ = [
    COMMETHOD([helpstring(u'Adds a filename to the array.')], HRESULT, 'Add',
              ( ['in'], BSTR, 'FileName' )),
    COMMETHOD([helpstring(u'Removes the current filename from the array.')], HRESULT, 'Remove'),
    COMMETHOD([helpstring(u'Resets the current position back to the beginning of the array.')], HRESULT, 'Reset'),
    COMMETHOD([helpstring(u'Obtains the next filename in the array.')], HRESULT, 'Next',
              ( ['retval', 'out'], POINTER(BSTR), 'FileName' )),
    COMMETHOD([helpstring(u'Indicates if the current filename is a directory.')], HRESULT, 'IsDirectory',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsDirectory' )),
]
################################################################
## code template for IFileNames implementation
##class IFileNames_Impl(object):
##    def Reset(self):
##        u'Resets the current position back to the beginning of the array.'
##        #return 
##
##    def Add(self, FileName):
##        u'Adds a filename to the array.'
##        #return 
##
##    def IsDirectory(self):
##        u'Indicates if the current filename is a directory.'
##        #return IsDirectory
##
##    def Remove(self):
##        u'Removes the current filename from the array.'
##        #return 
##
##    def Next(self):
##        u'Obtains the next filename in the array.'
##        #return FileName
##

IAuthorizeLicense._methods_ = [
    COMMETHOD(['propget', helpstring(u'Retrieves the last error message and code from an attempt to process features.')], HRESULT, 'LastError',
              ( ['out'], POINTER(BSTR), 'LastError' ),
              ( ['retval', 'out'], POINTER(c_int), 'lastErrorCode' )),
    COMMETHOD(['propget', helpstring(u'Retrieves the details of the new authorized features.')], HRESULT, 'FeaturesAdded',
              ( ['retval', 'out'], POINTER(BSTR), 'FeaturesAdded' )),
    COMMETHOD([helpstring(u'Authorize new feature(s).')], HRESULT, 'AuthorizeASR',
              ( ['in'], BSTR, 'strAsr' ),
              ( ['in'], BSTR, 'Password' )),
    COMMETHOD([helpstring(u'Authorize new feature(s) from file.')], HRESULT, 'AuthorizeASRFromFile',
              ( ['in'], BSTR, 'FileName' ),
              ( ['in'], BSTR, 'Password' )),
    COMMETHOD([helpstring(u'Deauthorize feature(s).')], HRESULT, 'DeauthorizeASR',
              ( ['in'], BSTR, 'strAsr' ),
              ( ['in'], BSTR, 'Password' )),
    COMMETHOD([helpstring(u'Deauthorize feature(s) from file.')], HRESULT, 'DeauthorizeASRFromFile',
              ( ['in'], BSTR, 'FileName' ),
              ( ['in'], BSTR, 'Password' )),
    COMMETHOD([helpstring(u'Repair feature(s).')], HRESULT, 'RepairASR',
              ( ['in'], BSTR, 'strAsr' ),
              ( ['in'], BSTR, 'Password' )),
    COMMETHOD([helpstring(u'Repair feature(s) from file.')], HRESULT, 'RepairASRFromFile',
              ( ['in'], BSTR, 'FileName' ),
              ( ['in'], BSTR, 'Password' )),
    COMMETHOD([helpstring(u'Check feature(s).')], HRESULT, 'CheckASR',
              ( ['in'], BSTR, 'strAsr' ),
              ( ['in'], BSTR, 'Password' )),
    COMMETHOD([helpstring(u'Check feature(s) from file.')], HRESULT, 'CheckASRFromFile',
              ( ['in'], BSTR, 'FileName' ),
              ( ['in'], BSTR, 'Password' )),
]
################################################################
## code template for IAuthorizeLicense implementation
##class IAuthorizeLicense_Impl(object):
##    def CheckASR(self, strAsr, Password):
##        u'Check feature(s).'
##        #return 
##
##    def AuthorizeASRFromFile(self, FileName, Password):
##        u'Authorize new feature(s) from file.'
##        #return 
##
##    def DeauthorizeASRFromFile(self, FileName, Password):
##        u'Deauthorize feature(s) from file.'
##        #return 
##
##    def AuthorizeASR(self, strAsr, Password):
##        u'Authorize new feature(s).'
##        #return 
##
##    @property
##    def FeaturesAdded(self):
##        u'Retrieves the details of the new authorized features.'
##        #return FeaturesAdded
##
##    def DeauthorizeASR(self, strAsr, Password):
##        u'Deauthorize feature(s).'
##        #return 
##
##    def CheckASRFromFile(self, FileName, Password):
##        u'Check feature(s) from file.'
##        #return 
##
##    def RepairASR(self, strAsr, Password):
##        u'Repair feature(s).'
##        #return 
##
##    def RepairASRFromFile(self, FileName, Password):
##        u'Repair feature(s) from file.'
##        #return 
##
##    @property
##    def LastError(self):
##        u'Retrieves the last error message and code from an attempt to process features.'
##        #return LastError, lastErrorCode
##

IStringArray._methods_ = [
    COMMETHOD(['propget', helpstring(u'The element count.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'An element in the array.')], HRESULT, 'Element',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Element' )),
    COMMETHOD(['propput', helpstring(u'An element in the array.')], HRESULT, 'Element',
              ( ['in'], c_int, 'index' ),
              ( ['in'], BSTR, 'Element' )),
    COMMETHOD([helpstring(u'Removes element at the specified position.')], HRESULT, 'Remove',
              ( ['in'], c_int, 'index' )),
    COMMETHOD([helpstring(u'Removes all elements.')], HRESULT, 'RemoveAll'),
    COMMETHOD([helpstring(u'Add an element.')], HRESULT, 'Add',
              ( ['in'], BSTR, 'Element' )),
    COMMETHOD([helpstring(u'Add an element at the specified posiiton.')], HRESULT, 'Insert',
              ( ['in'], c_int, 'index' ),
              ( ['in'], BSTR, 'Element' )),
]
################################################################
## code template for IStringArray implementation
##class IStringArray_Impl(object):
##    @property
##    def Count(self):
##        u'The element count.'
##        #return Count
##
##    def Insert(self, index, Element):
##        u'Add an element at the specified posiiton.'
##        #return 
##
##    def Remove(self, index):
##        u'Removes element at the specified position.'
##        #return 
##
##    def _get(self, index):
##        u'An element in the array.'
##        #return Element
##    def _set(self, index, Element):
##        u'An element in the array.'
##    Element = property(_get, _set, doc = _set.__doc__)
##
##    def RemoveAll(self):
##        u'Removes all elements.'
##        #return 
##
##    def Add(self, Element):
##        u'Add an element.'
##        #return 
##

class TimeReference(CoClass):
    u'An object that represents a time reference, including a time zone.'
    _reg_clsid_ = GUID('{EFB2E7DB-78F4-4E24-B01F-4F9C7AB800C5}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
TimeReference._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ITimeReference, IXMLSerialize, IXMLVersionSupport, IClone, IPersistStream, IDocumentVersionSupportGEN]

class TimeZoneInfo(CoClass):
    u'An object that represents a time zone information.'
    _reg_clsid_ = GUID('{78FAD5F1-60FA-458A-8D93-630DA920448D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
TimeZoneInfo._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ITimeZoneInfo, IXMLSerialize, IXMLVersionSupport, IClone, IPersistStream, IDocumentVersionSupportGEN]

_WKSEnvelopeZ._fields_ = [
    ('XMin', c_double),
    ('YMin', c_double),
    ('ZMin', c_double),
    ('XMax', c_double),
    ('YMax', c_double),
    ('ZMax', c_double),
]
assert sizeof(_WKSEnvelopeZ) == 48, sizeof(_WKSEnvelopeZ)
assert alignment(_WKSEnvelopeZ) == 8, alignment(_WKSEnvelopeZ)

# values for enumeration 'esriDrawOp'
esriDrawPolyPolyline = 0
esriDrawPolyPolygon = 1
esriDrawPolyline = 2
esriDrawPolygon = 3
esriDrawBeginPath = 4
esriDrawEndPath = 5
esriDrawArcCW = 6
esriDrawArcCCW = 7
esriDrawPolyBezier = 8
esriDrawRectangle = 9
esriDrawCircle = 10
esriDrawMoveTo = 11
esriDrawMultipoint = 12
esriDrawStop = 13
esriDrawTrapezoids = 14
esriDrawPolygonNoBorder = 15
esriDrawPolyPolygonNoBorder = 16
esriDrawOp = c_int # enum

# values for enumeration 'esriByteSwapDataType'
esriBSDTchar = 0
esriBSDTbool = 1
esriBSDTunsignedint = 2
esriBSDTBYTE = 3
esriBSDTBOOLU = 4
esriBSDTUSHORT = 5
esriBSDTSHORT = 6
esriBSDTULONG = 7
esriBSDTLONG = 8
esriBSDTULONGLONG = 9
esriBSDTLONGLONG = 10
esriBSDTFLOAT = 11
esriBSDTDOUBLE = 12
esriBSDTGUID = 13
esriBSDTWCHAR = 14
esriByteSwapDataType = c_int # enum
class LocaleInfo(CoClass):
    u'An object that represents a locale info.'
    _reg_clsid_ = GUID('{1CB5F59D-FD41-4695-9F48-FAE4675DBF3C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
LocaleInfo._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ILocaleInfo, IXMLSerialize, IXMLVersionSupport, IClone, IPersistStream, IDocumentVersionSupportGEN]

IScientificNumberFormat._methods_ = [
    COMMETHOD(['propput', helpstring(u'The number of decimal digits in a scientifically-formatted number.')], HRESULT, 'DecimalPlaces',
              ( ['in'], c_int, 'num' )),
    COMMETHOD(['propget', helpstring(u'The number of decimal digits in a scientifically-formatted number.')], HRESULT, 'DecimalPlaces',
              ( ['retval', 'out'], POINTER(c_int), 'num' )),
]
################################################################
## code template for IScientificNumberFormat implementation
##class IScientificNumberFormat_Impl(object):
##    def _get(self):
##        u'The number of decimal digits in a scientifically-formatted number.'
##        #return num
##    def _set(self, num):
##        u'The number of decimal digits in a scientifically-formatted number.'
##    DecimalPlaces = property(_get, _set, doc = _set.__doc__)
##

IPropertySetArray._methods_ = [
    COMMETHOD(['propget', helpstring(u'The propertyset count.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'The propertyset at the specified position.')], HRESULT, 'Element',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IPropertySet)), 'ppPropertySet' )),
    COMMETHOD([helpstring(u'Removes the propertyset at the specified position.')], HRESULT, 'Remove',
              ( ['in'], c_int, 'index' )),
    COMMETHOD([helpstring(u'Removes all propertysets.')], HRESULT, 'RemoveAll'),
    COMMETHOD([helpstring(u'Adds a propertyset.')], HRESULT, 'Add',
              ( ['in'], POINTER(IPropertySet), 'pPropertySet' )),
    COMMETHOD([helpstring(u'Adds a propertyset at the specified position.')], HRESULT, 'Insert',
              ( ['in'], c_int, 'index' ),
              ( ['in'], POINTER(IPropertySet), 'pPropertySet' )),
]
################################################################
## code template for IPropertySetArray implementation
##class IPropertySetArray_Impl(object):
##    @property
##    def Count(self):
##        u'The propertyset count.'
##        #return Count
##
##    def Insert(self, index, pPropertySet):
##        u'Adds a propertyset at the specified position.'
##        #return 
##
##    def Remove(self, index):
##        u'Removes the propertyset at the specified position.'
##        #return 
##
##    @property
##    def Element(self, index):
##        u'The propertyset at the specified position.'
##        #return ppPropertySet
##
##    def RemoveAll(self):
##        u'Removes all propertysets.'
##        #return 
##
##    def Add(self, pPropertySet):
##        u'Adds a propertyset.'
##        #return 
##

class TimeZoneFactory(CoClass):
    u'An object that creates TimeZoneInfo instances.'
    _reg_clsid_ = GUID('{C559680F-9FAE-4967-938A-33548BC5EBA0}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
TimeZoneFactory._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ITimeZoneFactory, ITimeZoneFactory2]

class IRequestHandler2(IRequestHandler):
    _case_insensitive_ = True
    u'Provides access to members that control handing of request messages.'
    _iid_ = GUID('{8319E7D0-8AD1-48ED-AA99-03F9D0C93BA8}')
    _idlflags_ = ['oleautomation']
IRequestHandler2._methods_ = [
    COMMETHOD([helpstring(u'Handles a binary request with explicit capabilities.')], HRESULT, 'HandleBinaryRequest2',
              ( ['in'], BSTR, 'Capabilities' ),
              ( ['in'], POINTER(_midlSAFEARRAY(c_ubyte)), 'request' ),
              ( ['retval', 'out'], POINTER(_midlSAFEARRAY(c_ubyte)), 'response' )),
]
################################################################
## code template for IRequestHandler2 implementation
##class IRequestHandler2_Impl(object):
##    def HandleBinaryRequest2(self, Capabilities, request):
##        u'Handles a binary request with explicit capabilities.'
##        #return response
##

ILog._methods_ = [
    COMMETHOD([helpstring(u'Adds a message to the log.')], HRESULT, 'AddMessage',
              ( ['in'], c_int, 'msgType' ),
              ( ['in'], c_int, 'msgCode' ),
              ( ['in'], BSTR, 'msg' )),
]
################################################################
## code template for ILog implementation
##class ILog_Impl(object):
##    def AddMessage(self, msgType, msgCode, msg):
##        u'Adds a message to the log.'
##        #return 
##

IComponentCategoryManager._methods_ = [
    COMMETHOD([helpstring(u'Creates a component category.')], HRESULT, 'Create',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], POINTER(IUID), 'category' )),
    COMMETHOD([helpstring(u'Installs or uninstalls the objects that match the object type into the given category.')], HRESULT, 'Setup',
              ( ['in'], BSTR, 'pathname' ),
              ( ['in'], POINTER(IUID), 'objectType' ),
              ( ['in'], POINTER(IUID), 'category' ),
              ( ['in'], VARIANT_BOOL, 'install' )),
    COMMETHOD([helpstring(u'Installs or uninstalls the given object into the given category.')], HRESULT, 'SetupObject',
              ( ['in'], BSTR, 'pathname' ),
              ( ['in'], POINTER(IUID), 'obj' ),
              ( ['in'], POINTER(IUID), 'category' ),
              ( ['in'], VARIANT_BOOL, 'install' )),
]
################################################################
## code template for IComponentCategoryManager implementation
##class IComponentCategoryManager_Impl(object):
##    def Create(self, Name, category):
##        u'Creates a component category.'
##        #return 
##
##    def Setup(self, pathname, objectType, category, install):
##        u'Installs or uninstalls the objects that match the object type into the given category.'
##        #return 
##
##    def SetupObject(self, pathname, obj, category, install):
##        u'Installs or uninstalls the given object into the given category.'
##        #return 
##

tagSTATSTG._fields_ = [
    ('pwcsName', WSTRING),
    ('type', c_ulong),
    ('cbSize', _ULARGE_INTEGER),
    ('mtime', _FILETIME),
    ('ctime', _FILETIME),
    ('atime', _FILETIME),
    ('grfMode', c_ulong),
    ('grfLocksSupported', c_ulong),
    ('clsid', comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID),
    ('grfStateBits', c_ulong),
    ('reserved', c_ulong),
]
assert sizeof(tagSTATSTG) == 72, sizeof(tagSTATSTG)
assert alignment(tagSTATSTG) == 8, alignment(tagSTATSTG)
INumberFormatOperations._methods_ = [
    COMMETHOD([helpstring(u'Increments a value according to the numbers format.')], HRESULT, 'Increment',
              ( ['in'], c_double, 'Value' ),
              ( ['retval', 'out'], POINTER(c_double), 'Result' )),
]
################################################################
## code template for INumberFormatOperations implementation
##class INumberFormatOperations_Impl(object):
##    def Increment(self, Value):
##        u'Increments a value according to the numbers format.'
##        #return Result
##

IClassifyGEN._methods_ = [
    COMMETHOD([helpstring(u'Classifies histogram data (array of values (doubles) and a paired array of frequencies (longs)) into the specified number of classes.')], HRESULT, 'Classify',
              ( ['in'], VARIANT, 'doubleArrayValues' ),
              ( ['in'], VARIANT, 'longArrayFrequencies' ),
              ( ['in', 'out'], POINTER(c_int), 'numClasses' )),
    COMMETHOD(['propget', helpstring(u'The array of class breaks (double).  ClassBreaks(0) is the minimum value in the dataset, and subsequent breaks represent the upper limit of each class.')], HRESULT, 'ClassBreaks',
              ( ['retval', 'out'], POINTER(VARIANT), 'doubleArrayBreaks' )),
    COMMETHOD(['propget', helpstring(u'The name of the classification method (based on choice of classification object).')], HRESULT, 'MethodName',
              ( ['retval', 'out'], POINTER(BSTR), 'txt' )),
    COMMETHOD(['propget', helpstring(u'The CLSID for the classification object.')], HRESULT, 'ClassID',
              ( ['retval', 'out'], POINTER(POINTER(IUID)), 'clsid' )),
]
################################################################
## code template for IClassifyGEN implementation
##class IClassifyGEN_Impl(object):
##    @property
##    def ClassID(self):
##        u'The CLSID for the classification object.'
##        #return clsid
##
##    @property
##    def MethodName(self):
##        u'The name of the classification method (based on choice of classification object).'
##        #return txt
##
##    def Classify(self, doubleArrayValues, longArrayFrequencies):
##        u'Classifies histogram data (array of values (doubles) and a paired array of frequencies (longs)) into the specified number of classes.'
##        #return numClasses
##
##    @property
##    def ClassBreaks(self):
##        u'The array of class breaks (double).  ClassBreaks(0) is the minimum value in the dataset, and subsequent breaks represent the upper limit of each class.'
##        #return doubleArrayBreaks
##

IAngularConverter._methods_ = [
    COMMETHOD([helpstring(u'Writes an angle.')], HRESULT, 'SetAngle',
              ( ['in'], c_double, 'angle' ),
              ( ['in'], esriDirectionType, 'dt' ),
              ( ['in'], esriDirectionUnits, 'du' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'fail' )),
    COMMETHOD([helpstring(u'Reads the angle.')], HRESULT, 'GetAngle',
              ( ['in'], esriDirectionType, 'dt' ),
              ( ['in'], esriDirectionUnits, 'du' ),
              ( ['retval', 'out'], POINTER(c_double), 'angle' )),
    COMMETHOD([helpstring(u'Writes an angle.')], HRESULT, 'SetString',
              ( ['in'], BSTR, 'angle' ),
              ( ['in'], esriDirectionType, 'dt' ),
              ( ['in'], esriDirectionUnits, 'du' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bRet' )),
    COMMETHOD([helpstring(u'Reads the angle.')], HRESULT, 'GetString',
              ( ['in'], esriDirectionType, 'dt' ),
              ( ['in'], esriDirectionUnits, 'du' ),
              ( ['in'], c_int, 'precision' ),
              ( ['retval', 'out'], POINTER(BSTR), 'angle' )),
]
################################################################
## code template for IAngularConverter implementation
##class IAngularConverter_Impl(object):
##    def SetAngle(self, angle, dt, du):
##        u'Writes an angle.'
##        #return fail
##
##    def SetString(self, angle, dt, du):
##        u'Writes an angle.'
##        #return bRet
##
##    def GetAngle(self, dt, du):
##        u'Reads the angle.'
##        #return angle
##
##    def GetString(self, dt, du, precision):
##        u'Reads the angle.'
##        #return angle
##

class NumericFormat(CoClass):
    u'An object for formatting numbers in a variety of numeric formats.'
    _reg_clsid_ = GUID('{7E4F4719-8E54-11D2-AAD8-000000000000}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
NumericFormat._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, INumberFormat, INumericFormat, INumberFormatOperations, IClone, IPersist, IPersistStream, IXMLSerialize]

IXMLFlags._methods_ = [
    COMMETHOD([helpstring(u'Writes a flag value.')], HRESULT, 'SetFlag',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], VARIANT_BOOL, 'FlagValue' )),
    COMMETHOD([helpstring(u'Indicates whether XML flag is set.')], HRESULT, 'GetFlag',
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'FlagValue' )),
    COMMETHOD(['propget', helpstring(u'Number of flags.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Flag name by index.')], HRESULT, 'FlagName',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'Indicates whether the flag has value by index.')], HRESULT, 'FlagValue',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
]
################################################################
## code template for IXMLFlags implementation
##class IXMLFlags_Impl(object):
##    @property
##    def Count(self):
##        u'Number of flags.'
##        #return Count
##
##    def SetFlag(self, Name, FlagValue):
##        u'Writes a flag value.'
##        #return 
##
##    @property
##    def FlagName(self, index):
##        u'Flag name by index.'
##        #return Name
##
##    def GetFlag(self, Name):
##        u'Indicates whether XML flag is set.'
##        #return FlagValue
##
##    @property
##    def FlagValue(self, index):
##        u'Indicates whether the flag has value by index.'
##        #return Value
##

ICategoryFactory._methods_ = [
    COMMETHOD(['propput', helpstring(u'The ID of the category.')], HRESULT, 'CategoryID',
              ( ['in'], POINTER(IUID), 'rhs' )),
    COMMETHOD([helpstring(u'Creates the next component in the category.')], HRESULT, 'CreateNext',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'nextComponent' )),
]
################################################################
## code template for ICategoryFactory implementation
##class ICategoryFactory_Impl(object):
##    def _set(self, rhs):
##        u'The ID of the category.'
##    CategoryID = property(fset = _set, doc = _set.__doc__)
##
##    def CreateNext(self):
##        u'Creates the next component in the category.'
##        #return nextComponent
##

IEnvironmentManager._methods_ = [
    COMMETHOD([helpstring(u'Retrieves an environment.')], HRESULT, 'GetEnvironment',
              ( ['in'], POINTER(IUID), 'pGuid' ),
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'ppUnk' )),
    COMMETHOD([helpstring(u'Adds an environment.')], HRESULT, 'AddEnvironment',
              ( ['in'], POINTER(IUID), 'pGuid' ),
              ( ['in'], POINTER(IUnknown), 'pUnk' )),
]
################################################################
## code template for IEnvironmentManager implementation
##class IEnvironmentManager_Impl(object):
##    def GetEnvironment(self, pGuid):
##        u'Retrieves an environment.'
##        #return ppUnk
##
##    def AddEnvironment(self, pGuid, pUnk):
##        u'Adds an environment.'
##        #return 
##

IComponentCategoryInfo._methods_ = [
    COMMETHOD([helpstring(u'Obtains a collection of component IDs matching the specified component category ID.')], HRESULT, 'GetComponentsInCategory',
              ( ['in'], POINTER(IUID), 'pCategoryID' ),
              ( ['retval', 'out'], POINTER(POINTER(IEnumUID)), 'ppUIDs' )),
]
################################################################
## code template for IComponentCategoryInfo implementation
##class IComponentCategoryInfo_Impl(object):
##    def GetComponentsInCategory(self, pCategoryID):
##        u'Obtains a collection of component IDs matching the specified component category ID.'
##        #return ppUIDs
##

class IObjectConstruct(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods for constructing an object.'
    _iid_ = GUID('{30FA4757-A2F3-4D11-B944-059AAD5C3991}')
    _idlflags_ = ['oleautomation']
IObjectConstruct._methods_ = [
    COMMETHOD([helpstring(u'Two phase object construction.')], HRESULT, 'Construct',
              ( ['in'], POINTER(IPropertySet), 'props' )),
]
################################################################
## code template for IObjectConstruct implementation
##class IObjectConstruct_Impl(object):
##    def Construct(self, props):
##        u'Two phase object construction.'
##        #return 
##

IJITExtensionManager._methods_ = [
    COMMETHOD(['propget', helpstring(u'The number of just in time extensions registered with the application.')], HRESULT, 'JITExtensionCount',
              ( ['retval', 'out'], POINTER(c_int), 'pCount' )),
    COMMETHOD(['propget', helpstring(u'Retrieves the CLSID of the JIT Extension at index.')], HRESULT, 'JITExtensionCLSID',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IUID)), 'ppID' )),
    COMMETHOD([helpstring(u'Indicates whether the extension is currently loaded.')], HRESULT, 'IsLoaded',
              ( ['in'], POINTER(IUID), 'pID' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bLoaded' )),
    COMMETHOD([helpstring(u'Removes a just in time extension from the manager.')], HRESULT, 'RemoveExtension',
              ( ['in'], POINTER(IExtension), 'pExtension' )),
    COMMETHOD([helpstring(u'Adds an extension to the manager without initialization.')], HRESULT, 'InsertExtension',
              ( ['in'], POINTER(IUID), 'pExtCLSID' ),
              ( ['in'], POINTER(IExtension), 'pExtension' )),
    COMMETHOD([helpstring(u'Indicates whether the extension is currently checked on.')], HRESULT, 'IsExtensionEnabled',
              ( ['in'], POINTER(IUID), 'pExtCLSID' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Enabled' )),
]
################################################################
## code template for IJITExtensionManager implementation
##class IJITExtensionManager_Impl(object):
##    def InsertExtension(self, pExtCLSID, pExtension):
##        u'Adds an extension to the manager without initialization.'
##        #return 
##
##    def IsExtensionEnabled(self, pExtCLSID):
##        u'Indicates whether the extension is currently checked on.'
##        #return Enabled
##
##    def IsLoaded(self, pID):
##        u'Indicates whether the extension is currently loaded.'
##        #return bLoaded
##
##    def RemoveExtension(self, pExtension):
##        u'Removes a just in time extension from the manager.'
##        #return 
##
##    @property
##    def JITExtensionCLSID(self, index):
##        u'Retrieves the CLSID of the JIT Extension at index.'
##        #return ppID
##
##    @property
##    def JITExtensionCount(self):
##        u'The number of just in time extensions registered with the application.'
##        #return pCount
##


# values for enumeration 'esriAreaUnits'
esriUnknownAreaUnits = 0
esriSquareInches = 1
esriSquareFeet = 2
esriSquareYards = 3
esriAcres = 4
esriSquareMiles = 5
esriSquareMillimeters = 6
esriSquareCentimeters = 7
esriSquareDecimeters = 8
esriSquareMeters = 9
esriAres = 10
esriHectares = 11
esriSquareKilometers = 12
esriAreaUnitsLast = 13
esriAreaUnits = c_int # enum
class FractionFormat(CoClass):
    u'An object for formatting numbers in a fraction format.'
    _reg_clsid_ = GUID('{7E4F471C-8E54-11D2-AAD8-000000000000}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
FractionFormat._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, INumberFormat, INumberFormatOperations, IFractionFormat, IClone, IPersist, IPersistStream]

class IObjectUpdate(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods for updating an object.'
    _iid_ = GUID('{D641F414-1004-4E73-9386-F6EA543E2D95}')
    _idlflags_ = ['oleautomation']
IObjectUpdate._methods_ = [
    COMMETHOD([helpstring(u"Updates object's properties.")], HRESULT, 'Update',
              ( ['in'], POINTER(IPropertySet), 'props' )),
]
################################################################
## code template for IObjectUpdate implementation
##class IObjectUpdate_Impl(object):
##    def Update(self, props):
##        u"Updates object's properties."
##        #return 
##

IStatisticsResults._methods_ = [
    COMMETHOD(['propget', helpstring(u'The count of the values.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'The minimum value.')], HRESULT, 'Minimum',
              ( ['retval', 'out'], POINTER(c_double), 'min' )),
    COMMETHOD(['propget', helpstring(u'The maximum value.')], HRESULT, 'Maximum',
              ( ['retval', 'out'], POINTER(c_double), 'max' )),
    COMMETHOD(['propget', helpstring(u'The sum of the values.')], HRESULT, 'Sum',
              ( ['retval', 'out'], POINTER(c_double), 'Sum' )),
    COMMETHOD(['propget', helpstring(u'The arithmetic mean.')], HRESULT, 'Mean',
              ( ['retval', 'out'], POINTER(c_double), 'Mean' )),
    COMMETHOD(['propget', helpstring(u'The standard deviation, based on sample flag.')], HRESULT, 'StandardDeviation',
              ( ['retval', 'out'], POINTER(c_double), 'stdDev' )),
]
################################################################
## code template for IStatisticsResults implementation
##class IStatisticsResults_Impl(object):
##    @property
##    def Count(self):
##        u'The count of the values.'
##        #return Count
##
##    @property
##    def Sum(self):
##        u'The sum of the values.'
##        #return Sum
##
##    @property
##    def StandardDeviation(self):
##        u'The standard deviation, based on sample flag.'
##        #return stdDev
##
##    @property
##    def Maximum(self):
##        u'The maximum value.'
##        #return max
##
##    @property
##    def Minimum(self):
##        u'The minimum value.'
##        #return min
##
##    @property
##    def Mean(self):
##        u'The arithmetic mean.'
##        #return Mean
##

class ILog2(ILog):
    _case_insensitive_ = True
    u'Provides access to methods for accessing a log.'
    _iid_ = GUID('{44F1FE1D-CCC4-4A5F-977A-233C25A45625}')
    _idlflags_ = ['oleautomation']
ILog2._methods_ = [
    COMMETHOD([helpstring(u'True if the message type is allowed to be written into the log file.')], HRESULT, 'WillLog',
              ( ['in'], c_int, 'msgType' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'WillLog' )),
    COMMETHOD([helpstring(u'Adds a message to the log.')], HRESULT, 'AddMessageEx',
              ( ['in'], c_int, 'msgType' ),
              ( ['in'], BSTR, 'MethodName' ),
              ( ['in'], c_int, 'msgCode' ),
              ( ['in'], c_double, 'elapsed' ),
              ( ['in'], BSTR, 'msg' )),
]
################################################################
## code template for ILog2 implementation
##class ILog2_Impl(object):
##    def AddMessageEx(self, msgType, MethodName, msgCode, elapsed, msg):
##        u'Adds a message to the log.'
##        #return 
##
##    def WillLog(self, msgType):
##        u'True if the message type is allowed to be written into the log file.'
##        #return WillLog
##


# values for enumeration 'esriCaseAppearance'
esriCaseAppearanceUnchanged = 0
esriCaseAppearanceUpper = 1
esriCaseAppearanceLower = 2
esriCaseAppearance = c_int # enum
IUnitConverter._methods_ = [
    COMMETHOD([helpstring(u'Convert Esri units.')], HRESULT, 'ConvertUnits',
              ( ['in'], c_double, 'dValue' ),
              ( ['in'], esriUnits, 'inUnits' ),
              ( ['in'], esriUnits, 'outUnits' ),
              ( ['retval', 'out'], POINTER(c_double), 'outValue' )),
    COMMETHOD([helpstring(u'Convert Esri unit enumerations to strings.')], HRESULT, 'EsriUnitsAsString',
              ( ['in'], esriUnits, 'units' ),
              ( ['in'], esriCaseAppearance, 'appearance' ),
              ( ['in'], VARIANT_BOOL, 'bPlural' ),
              ( ['retval', 'out'], POINTER(BSTR), 'sUnitString' )),
]
################################################################
## code template for IUnitConverter implementation
##class IUnitConverter_Impl(object):
##    def ConvertUnits(self, dValue, inUnits, outUnits):
##        u'Convert Esri units.'
##        #return outValue
##
##    def EsriUnitsAsString(self, units, appearance, bPlural):
##        u'Convert Esri unit enumerations to strings.'
##        #return sUnitString
##


# values for enumeration 'esriJobMessageType'
esriJobMessageTypeInformative = 0
esriJobMessageTypeWarning = 1
esriJobMessageTypeError = 2
esriJobMessageTypeEmpty = 3
esriJobMessageTypeAbort = 4
esriJobMessageTypeProcessStart = 5
esriJobMessageTypeProcessStop = 6
esriJobMessageTypeProcessDefinition = 7
esriJobMessageType = c_int # enum
IJobMessage._methods_ = [
    COMMETHOD(['propget', helpstring(u'Method to return message type.')], HRESULT, 'MessageType',
              ( ['retval', 'out'], POINTER(esriJobMessageType), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Method to return message type.')], HRESULT, 'MessageType',
              ( ['in'], esriJobMessageType, 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Method to return message description.')], HRESULT, 'Description',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Method to return message description.')], HRESULT, 'Description',
              ( ['in'], BSTR, 'pVal' )),
]
################################################################
## code template for IJobMessage implementation
##class IJobMessage_Impl(object):
##    def _get(self):
##        u'Method to return message description.'
##        #return pVal
##    def _set(self, pVal):
##        u'Method to return message description.'
##    Description = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Method to return message type.'
##        #return pVal
##    def _set(self, pVal):
##        u'Method to return message type.'
##    MessageType = property(_get, _set, doc = _set.__doc__)
##

IJSONArray._methods_ = [
    COMMETHOD([helpstring(u'Parses JSON array from string into memory.')], HRESULT, 'ParseString',
              ( ['in'], BSTR, 'json' )),
    COMMETHOD([helpstring(u'Parses JSON array from IJSONReader into memory. Useful if you want to have random acces to just a part of a JSON.')], HRESULT, 'ParseJSON',
              ( ['in'], POINTER(IJSONReader), 'pReader' )),
    COMMETHOD(['propget', helpstring(u'Returns an array size.')], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'Returns an array value at a given index. Returns E_INVALIDARG if index is out of bounds.')], HRESULT, 'Value',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'Value' )),
    COMMETHOD([helpstring(u'Checks if an array value at a given index is NULL.')], HRESULT, 'IsValueNull',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([helpstring(u"Returns array value at a given index as DATE. If index is out of bounds or type coercion fails, returns VARIANT_FALSE in 'success' parameter.")], HRESULT, 'TryGetValueAsDate',
              ( ['in'], c_int, 'index' ),
              ( ['out'], POINTER(c_double), 'Value' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'success' )),
    COMMETHOD([helpstring(u"Returns array value at a given index as boolean. If index is out of bounds or type coercion fails, returns VARIANT_FALSE in 'success' parameter.")], HRESULT, 'TryGetValueAsBoolean',
              ( ['in'], c_int, 'index' ),
              ( ['out'], POINTER(VARIANT_BOOL), 'Value' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'success' )),
    COMMETHOD([helpstring(u"Returns array value at a given index as long. If index is out of bounds or type coercion fails, returns VARIANT_FALSE in 'success' parameter.")], HRESULT, 'TryGetValueAsLong',
              ( ['in'], c_int, 'index' ),
              ( ['out'], POINTER(c_int), 'Value' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'success' )),
    COMMETHOD([helpstring(u"Returns array value at a given index as double. If index is out of bounds or type coercion fails, returns VARIANT_FALSE in 'success' parameter.")], HRESULT, 'TryGetValueAsDouble',
              ( ['in'], c_int, 'index' ),
              ( ['out'], POINTER(c_double), 'Value' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'success' )),
    COMMETHOD([helpstring(u"Returns array value at a given index as string. If index is out of bounds or type coercion fails, returns VARIANT_FALSE in 'success' parameter.")], HRESULT, 'TryGetValueAsString',
              ( ['in'], c_int, 'index' ),
              ( ['out'], POINTER(BSTR), 'Value' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'success' )),
    COMMETHOD([helpstring(u"Returns array value at a given index as IJSONObject. If index is out of bounds or type coercion fails, returns VARIANT_FALSE in 'success' parameter.")], HRESULT, 'TryGetValueAsObject',
              ( ['in'], c_int, 'index' ),
              ( ['out'], POINTER(POINTER(IJSONObject)), 'Value' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'success' )),
    COMMETHOD([helpstring(u"Returns array value at a given index as IJSONArray. If index is out of bounds or type coercion fails, returns VARIANT_FALSE in 'success' parameter.")], HRESULT, 'TryGetValueAsArray',
              ( ['in'], c_int, 'index' ),
              ( ['out'], POINTER(POINTER(IJSONArray)), 'Value' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'success' )),
    COMMETHOD([helpstring(u'Adds new variant value to the array.')], HRESULT, 'Add',
              ( ['in'], VARIANT, 'Value' )),
    COMMETHOD([helpstring(u'Adds new DATE value to the array.')], HRESULT, 'AddDate',
              ( ['in'], c_double, 'Value' )),
    COMMETHOD([helpstring(u'Adds new boolean value to the array.')], HRESULT, 'AddBoolean',
              ( ['in'], VARIANT_BOOL, 'Value' )),
    COMMETHOD([helpstring(u'Adds new long value to the array.')], HRESULT, 'AddLong',
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([helpstring(u'Adds new double value to the array.')], HRESULT, 'AddDouble',
              ( ['in'], c_double, 'Value' )),
    COMMETHOD([helpstring(u'Adds new string value to the array.')], HRESULT, 'AddString',
              ( ['in'], BSTR, 'Value' )),
    COMMETHOD([helpstring(u'Adds new null value to the array.')], HRESULT, 'AddNull'),
    COMMETHOD([helpstring(u'Adds new nested object to the array.')], HRESULT, 'AddJSONObject',
              ( ['in'], POINTER(IJSONObject), 'Value' )),
    COMMETHOD([helpstring(u'Adds new nested array to the array.')], HRESULT, 'AddJSONArray',
              ( ['in'], POINTER(IJSONArray), 'Value' )),
    COMMETHOD([helpstring(u'Creates and adds new member to the member collection. Returns E_FAIL if creation of the member fails.')], HRESULT, 'CreateMemberObject',
              ( ['out'], POINTER(POINTER(IJSONObject)), 'Value' )),
    COMMETHOD([helpstring(u'Creates and adds new member to the member collection. Returns E_FAIL if creation of the member fails.')], HRESULT, 'CreateMemberArray',
              ( ['out'], POINTER(POINTER(IJSONArray)), 'Value' )),
    COMMETHOD([helpstring(u"Converts IJSONArray to JSON representation using IJSONWriter internally. 'props' parameter is to control IJSONWriter properties. It's safe to set it to NULL. ")], HRESULT, 'ToJSONString',
              ( ['in'], POINTER(IPropertySet), 'props' ),
              ( ['retval', 'out'], POINTER(BSTR), 'outStr' )),
    COMMETHOD([helpstring(u'Converts IJSONArray to JSON representation using provided IJSONWriter. Useful when you have complex JSON response you want to combine from the output of several methods.')], HRESULT, 'ToJSON',
              ( ['in'], BSTR, 'objectName' ),
              ( ['in'], POINTER(IJSONWriter), 'pWriter' )),
    COMMETHOD([helpstring(u'Remove a value from the member collection.')], HRESULT, 'RemoveValue',
              ( ['in'], c_int, 'index' )),
    COMMETHOD([helpstring(u'Removes all values.')], HRESULT, 'ClearAll'),
    COMMETHOD([helpstring(u'Adds new double value to the array. Stores precision for use in ToJSON and ToJSONString')], HRESULT, 'AddDoubleEx',
              ( ['in'], c_double, 'Value' ),
              ( ['in'], c_int, 'precision' )),
]
################################################################
## code template for IJSONArray implementation
##class IJSONArray_Impl(object):
##    def AddDoubleEx(self, Value, precision):
##        u'Adds new double value to the array. Stores precision for use in ToJSON and ToJSONString'
##        #return 
##
##    def TryGetValueAsArray(self, index):
##        u"Returns array value at a given index as IJSONArray. If index is out of bounds or type coercion fails, returns VARIANT_FALSE in 'success' parameter."
##        #return Value, success
##
##    def TryGetValueAsBoolean(self, index):
##        u"Returns array value at a given index as boolean. If index is out of bounds or type coercion fails, returns VARIANT_FALSE in 'success' parameter."
##        #return Value, success
##
##    def AddDate(self, Value):
##        u'Adds new DATE value to the array.'
##        #return 
##
##    def Add(self, Value):
##        u'Adds new variant value to the array.'
##        #return 
##
##    def IsValueNull(self, index):
##        u'Checks if an array value at a given index is NULL.'
##        #return Value
##
##    def CreateMemberArray(self):
##        u'Creates and adds new member to the member collection. Returns E_FAIL if creation of the member fails.'
##        #return Value
##
##    def RemoveValue(self, index):
##        u'Remove a value from the member collection.'
##        #return 
##
##    def ToJSONString(self, props):
##        u"Converts IJSONArray to JSON representation using IJSONWriter internally. 'props' parameter is to control IJSONWriter properties. It's safe to set it to NULL. "
##        #return outStr
##
##    def ClearAll(self):
##        u'Removes all values.'
##        #return 
##
##    def TryGetValueAsDate(self, index):
##        u"Returns array value at a given index as DATE. If index is out of bounds or type coercion fails, returns VARIANT_FALSE in 'success' parameter."
##        #return Value, success
##
##    def AddBoolean(self, Value):
##        u'Adds new boolean value to the array.'
##        #return 
##
##    def TryGetValueAsLong(self, index):
##        u"Returns array value at a given index as long. If index is out of bounds or type coercion fails, returns VARIANT_FALSE in 'success' parameter."
##        #return Value, success
##
##    def ParseJSON(self, pReader):
##        u'Parses JSON array from IJSONReader into memory. Useful if you want to have random acces to just a part of a JSON.'
##        #return 
##
##    @property
##    def Count(self):
##        u'Returns an array size.'
##        #return Count
##
##    def ParseString(self, json):
##        u'Parses JSON array from string into memory.'
##        #return 
##
##    def AddJSONObject(self, Value):
##        u'Adds new nested object to the array.'
##        #return 
##
##    def TryGetValueAsString(self, index):
##        u"Returns array value at a given index as string. If index is out of bounds or type coercion fails, returns VARIANT_FALSE in 'success' parameter."
##        #return Value, success
##
##    @property
##    def Value(self, index):
##        u'Returns an array value at a given index. Returns E_INVALIDARG if index is out of bounds.'
##        #return Value
##
##    def AddDouble(self, Value):
##        u'Adds new double value to the array.'
##        #return 
##
##    def TryGetValueAsDouble(self, index):
##        u"Returns array value at a given index as double. If index is out of bounds or type coercion fails, returns VARIANT_FALSE in 'success' parameter."
##        #return Value, success
##
##    def AddNull(self):
##        u'Adds new null value to the array.'
##        #return 
##
##    def TryGetValueAsObject(self, index):
##        u"Returns array value at a given index as IJSONObject. If index is out of bounds or type coercion fails, returns VARIANT_FALSE in 'success' parameter."
##        #return Value, success
##
##    def AddString(self, Value):
##        u'Adds new string value to the array.'
##        #return 
##
##    def AddJSONArray(self, Value):
##        u'Adds new nested array to the array.'
##        #return 
##
##    def AddLong(self, Value):
##        u'Adds new long value to the array.'
##        #return 
##
##    def CreateMemberObject(self):
##        u'Creates and adds new member to the member collection. Returns E_FAIL if creation of the member fails.'
##        #return Value
##
##    def ToJSON(self, objectName, pWriter):
##        u'Converts IJSONArray to JSON representation using provided IJSONWriter. Useful when you have complex JSON response you want to combine from the output of several methods.'
##        #return 
##

class ISystemBridge(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods usable in all supported languages.'
    _iid_ = GUID('{848E0E84-E280-4883-BA8C-320864C3D42E}')
    _idlflags_ = ['oleautomation']
ISystemBridge._methods_ = [
    COMMETHOD([helpstring(u'Classifies histogram data (array of values (doubles) and a paired array of frequencies (longs)) into the specified number of classes.')], HRESULT, 'Classify',
              ( [], POINTER(IClassifyGEN), 'pClassify' ),
              ( ['in'], POINTER(_midlSAFEARRAY(c_double)), 'doubleArrayValues' ),
              ( ['in'], POINTER(_midlSAFEARRAY(c_int)), 'longArrayFrequencies' ),
              ( ['in', 'out'], POINTER(c_int), 'numClasses' )),
]
################################################################
## code template for ISystemBridge implementation
##class ISystemBridge_Impl(object):
##    def Classify(self, pClassify, doubleArrayValues, longArrayFrequencies):
##        u'Classifies histogram data (array of values (doubles) and a paired array of frequencies (longs)) into the specified number of classes.'
##        #return numClasses
##

class IServerEnvironment(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to Server configuration information.'
    _iid_ = GUID('{32D4C328-E473-4615-922C-63C108F55E60}')
    _idlflags_ = ['oleautomation']
class IJobTracker(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that track and control execution of jobs.'
    _iid_ = GUID('{E95E6C90-0029-47E6-B0EA-5C6AA6642968}')
    _idlflags_ = ['oleautomation']
IServerEnvironment._methods_ = [
    COMMETHOD(['propget', helpstring(u'Retrieves an ILog interface that can be used to add logging messages.')], HRESULT, 'Log',
              ( ['retval', 'out'], POINTER(POINTER(ILog)), 'ppLog' )),
    COMMETHOD(['propget', helpstring(u'Retrieves an IProperySet interface that provides access to the server configuration information.')], HRESULT, 'Properties',
              ( ['retval', 'out'], POINTER(POINTER(IPropertySet)), 'ppProps' )),
    COMMETHOD(['propget', helpstring(u'Retrieves IJobTracker interface that provides access to members that track and control execution of jobs.')], HRESULT, 'JobTracker',
              ( ['retval', 'out'], POINTER(POINTER(IJobTracker)), 'ppJT' )),
    COMMETHOD(['propget', helpstring(u'Retrieves job directory for given job.')], HRESULT, 'JobDirectory',
              ( ['in'], BSTR, 'JobID' ),
              ( ['retval', 'out'], POINTER(BSTR), 'pDirPath' )),
    COMMETHOD(['propget', helpstring(u'Retrieves current job ID.')], HRESULT, 'CurrentJobID',
              ( ['retval', 'out'], POINTER(BSTR), 'pJobID' )),
]
################################################################
## code template for IServerEnvironment implementation
##class IServerEnvironment_Impl(object):
##    @property
##    def JobDirectory(self, JobID):
##        u'Retrieves job directory for given job.'
##        #return pDirPath
##
##    @property
##    def CurrentJobID(self):
##        u'Retrieves current job ID.'
##        #return pJobID
##
##    @property
##    def Log(self):
##        u'Retrieves an ILog interface that can be used to add logging messages.'
##        #return ppLog
##
##    @property
##    def JobTracker(self):
##        u'Retrieves IJobTracker interface that provides access to members that track and control execution of jobs.'
##        #return ppJT
##
##    @property
##    def Properties(self):
##        u'Retrieves an IProperySet interface that provides access to the server configuration information.'
##        #return ppProps
##

class SystemHelper(CoClass):
    u'SystemHelper object. Providing helper methods for System objects.'
    _reg_clsid_ = GUID('{BE49D696-3C46-4B81-960B-F67D1BBD238D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
SystemHelper._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ISystemBridge]

class ITestConnection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to members that test connection for a preset configuration.'
    _iid_ = GUID('{6B61D022-CAE6-41A9-BD13-6DAC82CFFEFD}')
    _idlflags_ = ['oleautomation']
ITestConnection._methods_ = [
    COMMETHOD([helpstring(u'Tests if the connection is successful with the current configuration.')], HRESULT, 'TestConnection',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'successful' )),
]
################################################################
## code template for ITestConnection implementation
##class ITestConnection_Impl(object):
##    def TestConnection(self):
##        u'Tests if the connection is successful with the current configuration.'
##        #return successful
##

esriPointAttributes = _esriPointAttributes
class IRectHolder(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to rectangle methods.'
    _iid_ = GUID('{1074568C-CC5F-48B4-9316-015CAD473359}')
    _idlflags_ = ['oleautomation']
IRectHolder._methods_ = [
    COMMETHOD([helpstring(u'Write a rectangle.')], HRESULT, 'Rect',
              ( ['in'], POINTER(tagRECT), 'pRect' )),
]
################################################################
## code template for IRectHolder implementation
##class IRectHolder_Impl(object):
##    def Rect(self, pRect):
##        u'Write a rectangle.'
##        #return 
##

IJobTracker._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates whether job execution can be continued.')], HRESULT, 'CanContinue',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD(['propput', helpstring(u'Must be called by job processor after it stopped job execution.')], HRESULT, 'IsStopped',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Notifies client about the job execution progress.')], HRESULT, 'Message',
              ( ['in'], esriJobMessageType, 'type' ),
              ( ['in'], BSTR, 'rhs' )),
]
################################################################
## code template for IJobTracker implementation
##class IJobTracker_Impl(object):
##    def _set(self, type, rhs):
##        u'Notifies client about the job execution progress.'
##    Message = property(fset = _set, doc = _set.__doc__)
##
##    @property
##    def CanContinue(self):
##        u'Indicates whether job execution can be continued.'
##        #return pVal
##
##    def _set(self, rhs):
##        u'Must be called by job processor after it stopped job execution.'
##    IsStopped = property(fset = _set, doc = _set.__doc__)
##

INumberFormat._methods_ = [
    COMMETHOD([helpstring(u'Converts a numeric value to a formatted string.')], HRESULT, 'ValueToString',
              ( ['in'], c_double, 'Value' ),
              ( ['retval', 'out'], POINTER(BSTR), 'str' )),
    COMMETHOD([helpstring(u'Converts a formatted string to a numeric value.')], HRESULT, 'StringToValue',
              ( ['in'], BSTR, 'str' ),
              ( ['retval', 'out'], POINTER(c_double), 'Value' )),
]
################################################################
## code template for INumberFormat implementation
##class INumberFormat_Impl(object):
##    def StringToValue(self, str):
##        u'Converts a formatted string to a numeric value.'
##        #return Value
##
##    def ValueToString(self, Value):
##        u'Converts a numeric value to a formatted string.'
##        #return str
##


# values for enumeration 'esriLockMgrType'
esriLockMgrNone = 0
esriLockMgrRead = 1
esriLockMgrWrite = 2
esriLockMgrEdit = 3
esriLockMgrSchemaRead = 4
esriLockMgrSchemaWrite = 5
esriLockMgrType = c_int # enum
IShortcutName._methods_ = [
    COMMETHOD(['propget', helpstring(u'The value of the TargetName property.')], HRESULT, 'TargetName',
              ( ['retval', 'out'], POINTER(POINTER(IName)), 'ppTargetName' )),
    COMMETHOD(['propputref', helpstring(u'The value of the TargetName property.')], HRESULT, 'TargetName',
              ( ['in'], POINTER(IName), 'ppTargetName' )),
]
################################################################
## code template for IShortcutName implementation
##class IShortcutName_Impl(object):
##    def TargetName(self, ppTargetName):
##        u'The value of the TargetName property.'
##        #return 
##

IAngularConverter2._methods_ = [
    COMMETHOD(['propput', helpstring(u'Allow an angle to be converted from one direction unit to another.')], HRESULT, 'NegativeAngles',
              ( ['in'], VARIANT_BOOL, 'negAngles' )),
    COMMETHOD(['propget', helpstring(u'Allow an angle to be converted from one direction unit to another.')], HRESULT, 'NegativeAngles',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'negAngles' )),
]
################################################################
## code template for IAngularConverter2 implementation
##class IAngularConverter2_Impl(object):
##    def _get(self):
##        u'Allow an angle to be converted from one direction unit to another.'
##        #return negAngles
##    def _set(self, negAngles):
##        u'Allow an angle to be converted from one direction unit to another.'
##    NegativeAngles = property(_get, _set, doc = _set.__doc__)
##

class IServerUserInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to the current user information.'
    _iid_ = GUID('{DCEE6BD6-395A-49AB-AE32-0559125C1DAF}')
    _idlflags_ = ['oleautomation']
IServerUserInfo._methods_ = [
    COMMETHOD(['propget', helpstring(u'Obtains user name.')], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propget', helpstring(u'Obtains user roles.')], HRESULT, 'Roles',
              ( ['retval', 'out'], POINTER(POINTER(IEnumBSTR)), 'ppEnum' )),
]
################################################################
## code template for IServerUserInfo implementation
##class IServerUserInfo_Impl(object):
##    @property
##    def Name(self):
##        u'Obtains user name.'
##        #return pVal
##
##    @property
##    def Roles(self):
##        u'Obtains user roles.'
##        #return ppEnum
##

IFrequencyStatistics._methods_ = [
    COMMETHOD(['propget', helpstring(u'The frequency interval count.')], HRESULT, 'FrequencyIntervalCount',
              ( ['retval', 'out'], POINTER(c_int), 'numIntervals' )),
    COMMETHOD(['propput', helpstring(u'The frequency interval count.')], HRESULT, 'FrequencyIntervalCount',
              ( ['in'], c_int, 'numIntervals' )),
    COMMETHOD([helpstring(u'Computes a suitable frequency interval count for the number of values.')], HRESULT, 'ComputeAutoFrequencyIntervals'),
    COMMETHOD(['propget', helpstring(u'The size (range) of each frequency interval.')], HRESULT, 'FrequencyIntervalSize',
              ( ['retval', 'out'], POINTER(c_double), 'intervalSize' )),
    COMMETHOD(['propget', helpstring(u'The frequency class count at a given interval index.')], HRESULT, 'FrequencyClassCount',
              ( ['in'], c_int, 'intervalIndex' ),
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
]
################################################################
## code template for IFrequencyStatistics implementation
##class IFrequencyStatistics_Impl(object):
##    def _get(self):
##        u'The frequency interval count.'
##        #return numIntervals
##    def _set(self, numIntervals):
##        u'The frequency interval count.'
##    FrequencyIntervalCount = property(_get, _set, doc = _set.__doc__)
##
##    def ComputeAutoFrequencyIntervals(self):
##        u'Computes a suitable frequency interval count for the number of values.'
##        #return 
##
##    @property
##    def FrequencyClassCount(self, intervalIndex):
##        u'The frequency class count at a given interval index.'
##        #return Count
##
##    @property
##    def FrequencyIntervalSize(self):
##        u'The size (range) of each frequency interval.'
##        #return intervalSize
##

IArcGISLocale._methods_ = [
    COMMETHOD(['propget', helpstring(u'The value of the language ID from the locale.')], HRESULT, 'LangID',
              ( ['retval', 'out'], POINTER(c_int), 'LangID' )),
    COMMETHOD(['propget', helpstring(u'The value of the country ID from the locale.')], HRESULT, 'CountryID',
              ( ['retval', 'out'], POINTER(c_int), 'CountryID' )),
    COMMETHOD(['propget', helpstring(u'The value of the locale.')], HRESULT, 'Locale',
              ( ['retval', 'out'], POINTER(c_int), 'Locale' )),
    COMMETHOD(['propget', helpstring(u'The value of the language ID from the UI locale.')], HRESULT, 'UILangID',
              ( ['retval', 'out'], POINTER(c_int), 'LangID' )),
    COMMETHOD(['propget', helpstring(u'The value of the country ID from the UI locale.')], HRESULT, 'UICountryID',
              ( ['retval', 'out'], POINTER(c_int), 'CountryID' )),
    COMMETHOD(['propget', helpstring(u'The value of the UI locale.')], HRESULT, 'UILocale',
              ( ['retval', 'out'], POINTER(c_int), 'Locale' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the UI locale is right to left.')], HRESULT, 'RightToLeft',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsRightToLeft' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the UI locale is right to left user interface.')], HRESULT, 'RightToLeftUI',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsRightToLeftUI' )),
    COMMETHOD(['propget', helpstring(u'Indicates if the UI locale is right to left table.')], HRESULT, 'RightToLeftTable',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsRightToLeftTable' )),
    COMMETHOD([helpstring(u'Write the ArcGIS locale for the process.')], HRESULT, 'SetLocale'),
    COMMETHOD([helpstring(u'Write the ArcGIS locale for the thread.')], HRESULT, 'SetThreadLocale'),
    COMMETHOD([helpstring(u'Write the ArcGIS UI locale for the thread.')], HRESULT, 'SetThreadUILocale'),
]
################################################################
## code template for IArcGISLocale implementation
##class IArcGISLocale_Impl(object):
##    def SetThreadLocale(self):
##        u'Write the ArcGIS locale for the thread.'
##        #return 
##
##    @property
##    def CountryID(self):
##        u'The value of the country ID from the locale.'
##        #return CountryID
##
##    def SetLocale(self):
##        u'Write the ArcGIS locale for the process.'
##        #return 
##
##    @property
##    def Locale(self):
##        u'The value of the locale.'
##        #return Locale
##
##    @property
##    def UILangID(self):
##        u'The value of the language ID from the UI locale.'
##        #return LangID
##
##    @property
##    def LangID(self):
##        u'The value of the language ID from the locale.'
##        #return LangID
##
##    @property
##    def RightToLeft(self):
##        u'Indicates if the UI locale is right to left.'
##        #return IsRightToLeft
##
##    @property
##    def RightToLeftUI(self):
##        u'Indicates if the UI locale is right to left user interface.'
##        #return IsRightToLeftUI
##
##    @property
##    def RightToLeftTable(self):
##        u'Indicates if the UI locale is right to left table.'
##        #return IsRightToLeftTable
##
##    @property
##    def UILocale(self):
##        u'The value of the UI locale.'
##        #return Locale
##
##    @property
##    def UICountryID(self):
##        u'The value of the country ID from the UI locale.'
##        #return CountryID
##
##    def SetThreadUILocale(self):
##        u'Write the ArcGIS UI locale for the thread.'
##        #return 
##


# values for enumeration 'esriScaleFormat'
esriAbsoluteScale = 0
esriImperialScale = 1
esriCustomScale = 2
esriScaleFormat = c_int # enum
IScaleFormat._methods_ = [
    COMMETHOD(['propput', helpstring(u'Format used to display scale, i.e., 1:20000 or 1 inch equals 5 miles.')], HRESULT, 'Format',
              ( ['in'], esriScaleFormat, 'Format' )),
    COMMETHOD(['propget', helpstring(u'Format used to display scale, i.e., 1:20000 or 1 inch equals 5 miles.')], HRESULT, 'Format',
              ( ['retval', 'out'], POINTER(esriScaleFormat), 'Format' )),
    COMMETHOD(['propput', helpstring(u'Format used to display scale value, i.e., 20,000.')], HRESULT, 'NumberFormat',
              ( ['in'], POINTER(INumberFormat), 'Format' )),
    COMMETHOD(['propget', helpstring(u'Format used to display scale value, i.e., 20,000.')], HRESULT, 'NumberFormat',
              ( ['retval', 'out'], POINTER(POINTER(INumberFormat)), 'Format' )),
    COMMETHOD(['propput', helpstring(u"Character(s) used to separate '1' from the scale in an absolute scale, i.e., the ':' in 1:20000.")], HRESULT, 'Separator',
              ( ['in'], BSTR, 'Separator' )),
    COMMETHOD(['propget', helpstring(u"Character(s) used to separate '1' from the scale in an absolute scale, i.e., the ':' in 1:20000.")], HRESULT, 'Separator',
              ( ['retval', 'out'], POINTER(BSTR), 'Separator' )),
    COMMETHOD(['propput', helpstring(u"The number preceding the page units in a scale, i.e., the '1' in 1 inch = 5 miles.")], HRESULT, 'PageUnitValue',
              ( ['in'], c_double, 'Value' )),
    COMMETHOD(['propget', helpstring(u"The number preceding the page units in a scale, i.e., the '1' in 1 inch = 5 miles.")], HRESULT, 'PageUnitValue',
              ( ['retval', 'out'], POINTER(c_double), 'Value' )),
    COMMETHOD(['propput', helpstring(u"The page units used to display a scale, i.e., the 'inch' in 1 inch = 5 miles.")], HRESULT, 'PageUnits',
              ( ['in'], esriUnits, 'units' )),
    COMMETHOD(['propget', helpstring(u"The page units used to display a scale, i.e., the 'inch' in 1 inch = 5 miles.")], HRESULT, 'PageUnits',
              ( ['retval', 'out'], POINTER(esriUnits), 'units' )),
    COMMETHOD(['propput', helpstring(u"The text used for 'equals', i.e., ' = ' in 1 inch = 5 miles.")], HRESULT, 'Equals',
              ( ['in'], BSTR, 'Text' )),
    COMMETHOD(['propget', helpstring(u"The text used for 'equals', i.e., ' = ' in 1 inch = 5 miles.")], HRESULT, 'Equals',
              ( ['retval', 'out'], POINTER(BSTR), 'Text' )),
    COMMETHOD(['propput', helpstring(u"The map units used to display a scale, i.e., the 'miles' in 1 inch = 5 miles.")], HRESULT, 'MapUnits',
              ( ['in'], esriUnits, 'units' )),
    COMMETHOD(['propget', helpstring(u"The map units used to display a scale, i.e., the 'miles' in 1 inch = 5 miles.")], HRESULT, 'MapUnits',
              ( ['retval', 'out'], POINTER(esriUnits), 'units' )),
    COMMETHOD(['propput', helpstring(u'Capitolize the units in the scale string.')], HRESULT, 'CapitolizeUnits',
              ( ['in'], VARIANT_BOOL, 'flag' )),
    COMMETHOD(['propget', helpstring(u'Capitolize the units in the scale string.')], HRESULT, 'CapitolizeUnits',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD(['propput', helpstring(u'Abbreviate the units in the scale string.')], HRESULT, 'AbbreviateUnits',
              ( ['in'], VARIANT_BOOL, 'flag' )),
    COMMETHOD(['propget', helpstring(u'Abbreviate the units in the scale string.')], HRESULT, 'AbbreviateUnits',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD(['propput', helpstring(u'Reverse the standard order [1:1000] becomes [1000:1] and [1 in = 10 mi] becomes [10 mi = 1 in].')], HRESULT, 'ReverseOrder',
              ( ['in'], VARIANT_BOOL, 'flag' )),
    COMMETHOD(['propget', helpstring(u'Reverse the standard order [1:1000] becomes [1000:1] and [1 in = 10 mi] becomes [10 mi = 1 in].')], HRESULT, 'ReverseOrder',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'flag' )),
    COMMETHOD(['propput', helpstring(u"A string defining the scale format. Embed XML tokens where scale values should go, i.e., <SCA a=''Attribute''>. Possible attributes: Scale, Separator, PageUnitValue, PageUnits, EqualsText, MapUnits.")], HRESULT, 'CustomFormat',
              ( ['in'], BSTR, 'Format' )),
    COMMETHOD(['propget', helpstring(u"A string defining the scale format. Embed XML tokens where scale values should go, i.e., <SCA a=''Attribute''>. Possible attributes: Scale, Separator, PageUnitValue, PageUnits, EqualsText, MapUnits.")], HRESULT, 'CustomFormat',
              ( ['retval', 'out'], POINTER(BSTR), 'Format' )),
    COMMETHOD([helpstring(u'Calculate the number of map units corresponding to the specified page units at the given absolute scale.')], HRESULT, 'CalcMapUnitValue',
              ( ['in'], c_double, 'absoluteScale' ),
              ( ['retval', 'out'], POINTER(c_double), 'mapUnitValue' )),
    COMMETHOD([helpstring(u'Convert the absolute scale to a string using the current IScaleFormat attributes.')], HRESULT, 'ScaleToString',
              ( ['in'], c_double, 'Scale' ),
              ( ['retval', 'out'], POINTER(BSTR), 'scaleStr' )),
    COMMETHOD([helpstring(u'Convert the string to an absolute scale using the current IScaleFormat attributes.')], HRESULT, 'StringToScale',
              ( ['in'], BSTR, 'scaleStr' ),
              ( ['retval', 'out'], POINTER(c_double), 'Scale' )),
    COMMETHOD([helpstring(u'Store the scale format as the system default.')], HRESULT, 'SaveToRegistry'),
    COMMETHOD([helpstring(u'Obtain the scale format to the system default.')], HRESULT, 'LoadFromRegistry'),
]
################################################################
## code template for IScaleFormat implementation
##class IScaleFormat_Impl(object):
##    def _get(self):
##        u"A string defining the scale format. Embed XML tokens where scale values should go, i.e., <SCA a=''Attribute''>. Possible attributes: Scale, Separator, PageUnitValue, PageUnits, EqualsText, MapUnits."
##        #return Format
##    def _set(self, Format):
##        u"A string defining the scale format. Embed XML tokens where scale values should go, i.e., <SCA a=''Attribute''>. Possible attributes: Scale, Separator, PageUnitValue, PageUnits, EqualsText, MapUnits."
##    CustomFormat = property(_get, _set, doc = _set.__doc__)
##
##    def StringToScale(self, scaleStr):
##        u'Convert the string to an absolute scale using the current IScaleFormat attributes.'
##        #return Scale
##
##    def ScaleToString(self, Scale):
##        u'Convert the absolute scale to a string using the current IScaleFormat attributes.'
##        #return scaleStr
##
##    def SaveToRegistry(self):
##        u'Store the scale format as the system default.'
##        #return 
##
##    def _get(self):
##        u'Format used to display scale value, i.e., 20,000.'
##        #return Format
##    def _set(self, Format):
##        u'Format used to display scale value, i.e., 20,000.'
##    NumberFormat = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Format used to display scale, i.e., 1:20000 or 1 inch equals 5 miles.'
##        #return Format
##    def _set(self, Format):
##        u'Format used to display scale, i.e., 1:20000 or 1 inch equals 5 miles.'
##    Format = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u"The map units used to display a scale, i.e., the 'miles' in 1 inch = 5 miles."
##        #return units
##    def _set(self, units):
##        u"The map units used to display a scale, i.e., the 'miles' in 1 inch = 5 miles."
##    MapUnits = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u"The text used for 'equals', i.e., ' = ' in 1 inch = 5 miles."
##        #return Text
##    def _set(self, Text):
##        u"The text used for 'equals', i.e., ' = ' in 1 inch = 5 miles."
##    Equals = property(_get, _set, doc = _set.__doc__)
##
##    def CalcMapUnitValue(self, absoluteScale):
##        u'Calculate the number of map units corresponding to the specified page units at the given absolute scale.'
##        #return mapUnitValue
##
##    def LoadFromRegistry(self):
##        u'Obtain the scale format to the system default.'
##        #return 
##
##    def _get(self):
##        u'Capitolize the units in the scale string.'
##        #return flag
##    def _set(self, flag):
##        u'Capitolize the units in the scale string.'
##    CapitolizeUnits = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Abbreviate the units in the scale string.'
##        #return flag
##    def _set(self, flag):
##        u'Abbreviate the units in the scale string.'
##    AbbreviateUnits = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u"Character(s) used to separate '1' from the scale in an absolute scale, i.e., the ':' in 1:20000."
##        #return Separator
##    def _set(self, Separator):
##        u"Character(s) used to separate '1' from the scale in an absolute scale, i.e., the ':' in 1:20000."
##    Separator = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Reverse the standard order [1:1000] becomes [1000:1] and [1 in = 10 mi] becomes [10 mi = 1 in].'
##        #return flag
##    def _set(self, flag):
##        u'Reverse the standard order [1:1000] becomes [1000:1] and [1 in = 10 mi] becomes [10 mi = 1 in].'
##    ReverseOrder = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u"The number preceding the page units in a scale, i.e., the '1' in 1 inch = 5 miles."
##        #return Value
##    def _set(self, Value):
##        u"The number preceding the page units in a scale, i.e., the '1' in 1 inch = 5 miles."
##    PageUnitValue = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u"The page units used to display a scale, i.e., the 'inch' in 1 inch = 5 miles."
##        #return units
##    def _set(self, units):
##        u"The page units used to display a scale, i.e., the 'inch' in 1 inch = 5 miles."
##    PageUnits = property(_get, _set, doc = _set.__doc__)
##

IFileName._methods_ = [
    COMMETHOD(['propput', helpstring(u'Pathname to the file.')], HRESULT, 'Path',
              ( ['in'], BSTR, 'Path' )),
    COMMETHOD(['propget', helpstring(u'Pathname to the file.')], HRESULT, 'Path',
              ( ['retval', 'out'], POINTER(BSTR), 'Path' )),
]
################################################################
## code template for IFileName implementation
##class IFileName_Impl(object):
##    def _get(self):
##        u'Pathname to the file.'
##        #return Path
##    def _set(self, Path):
##        u'Pathname to the file.'
##    Path = property(_get, _set, doc = _set.__doc__)
##


# values for enumeration 'esriTransportType'
esriTransportTypeEmbedded = 1
esriTransportTypeUrl = 2
esriTransportType = c_int # enum
class IServerEnvironment2(IServerEnvironment):
    _case_insensitive_ = True
    u'Provides access to Server configuration information.'
    _iid_ = GUID('{8037EE78-6197-4B8E-8F8B-52C744E42A31}')
    _idlflags_ = ['oleautomation']
class IServerEnvironment3(IServerEnvironment2):
    _case_insensitive_ = True
    u'Provides access to Server configuration information.'
    _iid_ = GUID('{9940E0CD-D279-468A-B0EA-C546DA5C3D0C}')
    _idlflags_ = ['oleautomation']
IServerEnvironment2._methods_ = [
    COMMETHOD(['propget', helpstring(u'Retrieves information about current user.')], HRESULT, 'UserInfo',
              ( ['retval', 'out'], POINTER(POINTER(IServerUserInfo)), 'ppInfo' )),
]
################################################################
## code template for IServerEnvironment2 implementation
##class IServerEnvironment2_Impl(object):
##    @property
##    def UserInfo(self):
##        u'Retrieves information about current user.'
##        #return ppInfo
##

IServerEnvironment3._methods_ = [
    COMMETHOD(['propget', helpstring(u'Indicates if server configuration is running as engine.')], HRESULT, 'IsRunningAsEngine',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
]
################################################################
## code template for IServerEnvironment3 implementation
##class IServerEnvironment3_Impl(object):
##    @property
##    def IsRunningAsEngine(self):
##        u'Indicates if server configuration is running as engine.'
##        #return pVal
##


# values for enumeration 'esriFilePermission'
esriReadOnly = 1
esriReadWrite = 2
esriFilePermission = c_int # enum
IFile._methods_ = [
    COMMETHOD([helpstring(u'Opens the specified file.')], HRESULT, 'Open',
              ( ['in'], BSTR, 'FileName' ),
              ( ['in'], esriFilePermission, 'permission' )),
]
################################################################
## code template for IFile implementation
##class IFile_Impl(object):
##    def Open(self, FileName, permission):
##        u'Opens the specified file.'
##        #return 
##

class AngleFormat(CoClass):
    u'An object for formatting numbers in an angle format.'
    _reg_clsid_ = GUID('{7E4F471E-8E54-11D2-AAD8-000000000000}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
AngleFormat._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, INumberFormat, INumericFormat, INumberFormatOperations, IAngleFormat, IClone, IPersist, IPersistStream, IDocumentVersionSupportGEN]

IObjectCopy._methods_ = [
    COMMETHOD([helpstring(u'Obtains a new object which is a copy of the input object.')], HRESULT, 'Copy',
              ( ['in'], POINTER(IUnknown), 'pInObject' ),
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'pResult' )),
    COMMETHOD([helpstring(u'Overwrites the object with the contents of input object.')], HRESULT, 'Overwrite',
              ( ['in'], POINTER(IUnknown), 'pInObject' ),
              ( ['in', 'out'], POINTER(POINTER(IUnknown)), 'pOverwriteObject' )),
]
################################################################
## code template for IObjectCopy implementation
##class IObjectCopy_Impl(object):
##    def Copy(self, pInObject):
##        u'Obtains a new object which is a copy of the input object.'
##        #return pResult
##
##    def Overwrite(self, pInObject):
##        u'Overwrites the object with the contents of input object.'
##        #return pOverwriteObject
##

IName._methods_ = [
    COMMETHOD(['propput', helpstring(u'The name string of the object.')], HRESULT, 'NameString',
              ( ['in'], BSTR, 'NameString' )),
    COMMETHOD(['propget', helpstring(u'The name string of the object.')], HRESULT, 'NameString',
              ( ['retval', 'out'], POINTER(BSTR), 'NameString' )),
    COMMETHOD([helpstring(u'Opens the object referred to by this name.')], HRESULT, 'Open',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'unknown' )),
]
################################################################
## code template for IName implementation
##class IName_Impl(object):
##    def _get(self):
##        u'The name string of the object.'
##        #return NameString
##    def _set(self, NameString):
##        u'The name string of the object.'
##    NameString = property(_get, _set, doc = _set.__doc__)
##
##    def Open(self):
##        u'Opens the object referred to by this name.'
##        #return unknown
##

IInputDeviceManager._methods_ = [
    COMMETHOD([helpstring(u'Creates and starts the devices for Inut Device component category, passing initializationData to each in IInputDevice::Startup.')], HRESULT, 'StartupDevices',
              ( ['in'], POINTER(VARIANT), 'initializationData' )),
    COMMETHOD([helpstring(u'Shuts down and releases the extensions that are loaded and calls IExtension::Shutdown.')], HRESULT, 'ShutdownDevices'),
    COMMETHOD([helpstring(u'Creates a single device given the CLSID, then passes initializationData to IInputDevice::Startup.')], HRESULT, 'AddDevice',
              ( ['in'], POINTER(IUID), 'pDeviceCLSID' ),
              ( ['in'], POINTER(VARIANT), 'initializationData' )),
    COMMETHOD(['propget', helpstring(u'The number of input devices loaded in the application.')], HRESULT, 'DeviceCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'The input device at the specified index.')], HRESULT, 'Device',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IExtension)), 'Extension' )),
    COMMETHOD(['propget', helpstring(u'The CLSID of the input device at the specified index.')], HRESULT, 'DeviceCLSID',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IUID)), 'ClassID' )),
    COMMETHOD([helpstring(u'Finds the input device by CLSID (IUID) or name (String).')], HRESULT, 'FindDevice',
              ( ['in'], VARIANT, 'nameOrID' ),
              ( ['retval', 'out'], POINTER(POINTER(IExtension)), 'Extension' )),
]
################################################################
## code template for IInputDeviceManager implementation
##class IInputDeviceManager_Impl(object):
##    def ShutdownDevices(self):
##        u'Shuts down and releases the extensions that are loaded and calls IExtension::Shutdown.'
##        #return 
##
##    def StartupDevices(self, initializationData):
##        u'Creates and starts the devices for Inut Device component category, passing initializationData to each in IInputDevice::Startup.'
##        #return 
##
##    def AddDevice(self, pDeviceCLSID, initializationData):
##        u'Creates a single device given the CLSID, then passes initializationData to IInputDevice::Startup.'
##        #return 
##
##    @property
##    def DeviceCount(self):
##        u'The number of input devices loaded in the application.'
##        #return Count
##
##    def FindDevice(self, nameOrID):
##        u'Finds the input device by CLSID (IUID) or name (String).'
##        #return Extension
##
##    @property
##    def Device(self, index):
##        u'The input device at the specified index.'
##        #return Extension
##
##    @property
##    def DeviceCLSID(self, index):
##        u'The CLSID of the input device at the specified index.'
##        #return ClassID
##


# values for enumeration 'esriSystemMessageCodeEnum'
esriSystemMessageCode_XMLTypeMappingFailed = 100100
esriSystemMessageCode_HTTPConnectionFailed = 100101
esriSystemMessageCode_CertFailed = 100102
esriSystemMessageCode_AuthFailed = 100103
esriSystemMessageCodeEnum = c_int # enum

# values for enumeration 'esriServerMessageCodeEnum'
esriSystemMessageCode_Debug = 100000
esriSystemMessageCode_StringRequestReceived = 100001
esriSystemMessageCode_StringResponseSent = 100002
esriSystemMessageCode_BinaryRequestReceived = 100003
esriSystemMessageCode_BinaryResponseSent = 100004
esriSystemMessageCode_RequestFailed = 100005
esriSystemMessageCode_ErrorLoadFromString = 100006
esriSystemMessageCode_ErrorReadXml = 100007
esriSystemMessageCode_ErrorWriteXml = 100008
esriSystemMessageCode_ErrorSaveToString = 100009
esriSystemMessageCode_ErrorImportFromMem = 100010
esriSystemMessageCode_ErrorLoadBinaryStream = 100011
esriSystemMessageCode_SetResponseStreamVersion = 100012
esriSystemMessageCode_ErrorWriteBinaryResponse = 100013
esriServerMessageCodeEnum = c_int # enum

# values for enumeration 'esriLicenseStatus'
esriLicenseAvailable = 10
esriLicenseNotLicensed = 20
esriLicenseUnavailable = 30
esriLicenseFailure = 40
esriLicenseAlreadyInitialized = 50
esriLicenseNotInitialized = 60
esriLicenseCheckedOut = 70
esriLicenseCheckedIn = 80
esriLicenseUntrusted = 90
esriLicenseStatus = c_int # enum
class TimeDuration(CoClass):
    u'An object that represents a time duration value.'
    _reg_clsid_ = GUID('{09692C1C-21FA-4FE2-8EFA-6C4ACB59A323}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
TimeDuration._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, ITimeDuration, IXMLSerialize, IXMLVersionSupport, IClone, IPersistStream, IDocumentVersionSupportGEN]

IXMLNamespaces._methods_ = [
    COMMETHOD([helpstring(u'Adds a namespace to the element.')], HRESULT, 'AddNamespace',
              ( ['in'], BSTR, 'Prefix' ),
              ( ['in'], BSTR, 'uri' )),
    COMMETHOD([helpstring(u'Deletes a namespace from the element.')], HRESULT, 'DeleteNamespace',
              ( ['in'], BSTR, 'uri' )),
    COMMETHOD(['propget', helpstring(u'Number of namespaces.')], HRESULT, 'NamespaceCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD(['propget', helpstring(u'The namespace prefix for a namespace.')], HRESULT, 'Prefix',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Prefix' )),
    COMMETHOD(['propget', helpstring(u'The namespace URI for a namespace.')], HRESULT, 'NamespaceURI',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'uri' )),
]
################################################################
## code template for IXMLNamespaces implementation
##class IXMLNamespaces_Impl(object):
##    @property
##    def NamespaceURI(self, index):
##        u'The namespace URI for a namespace.'
##        #return uri
##
##    @property
##    def Prefix(self, index):
##        u'The namespace prefix for a namespace.'
##        #return Prefix
##
##    @property
##    def NamespaceCount(self):
##        u'Number of namespaces.'
##        #return Count
##
##    def DeleteNamespace(self, uri):
##        u'Deletes a namespace from the element.'
##        #return 
##
##    def AddNamespace(self, Prefix, uri):
##        u'Adds a namespace to the element.'
##        #return 
##

class JobMessages(CoClass):
    u'The JobMessages object which defines properties and behaviour of an array of job messages.'
    _reg_clsid_ = GUID('{F3A6825C-9780-4265-89A1-AE35F7A3BB56}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{5E1F7BC3-67C5-4AEE-8EC6-C4B73AAC42ED}', 10, 2)
JobMessages._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IJobMessages, IXMLSerialize, IPersistStream]

ITimeZoneRule._methods_ = [
    COMMETHOD(['propget', helpstring(u'The year this rule is in effect.')], HRESULT, 'Year',
              ( ['retval', 'out'], POINTER(c_int), 'Year' )),
    COMMETHOD(['propput', helpstring(u'The year this rule is in effect.')], HRESULT, 'Year',
              ( ['in'], c_int, 'Year' )),
    COMMETHOD(['propget', helpstring(u'The time zone bias from UTC in minutes. LocalTime = UtcTime + BiasFromUTC.')], HRESULT, 'BiasFromUTC',
              ( ['retval', 'out'], POINTER(c_int), 'BiasFromUTC' )),
    COMMETHOD(['propput', helpstring(u'The time zone bias from UTC in minutes. LocalTime = UtcTime + BiasFromUTC.')], HRESULT, 'BiasFromUTC',
              ( ['in'], c_int, 'BiasFromUTC' )),
    COMMETHOD(['propget', helpstring(u'Date for transition to daylight time.')], HRESULT, 'DaylightTimeTransitionTime',
              ( ['retval', 'out'], POINTER(TimeZoneTransitionTime), 'DaylightTimeTransitionTime' )),
    COMMETHOD(['propput', helpstring(u'Date for transition to daylight time.')], HRESULT, 'DaylightTimeTransitionTime',
              ( ['in'], POINTER(TimeZoneTransitionTime), 'DaylightTimeTransitionTime' )),
    COMMETHOD(['propget', helpstring(u"The bias to be used during daylight time. This bias is relative to the time zone's BiasFromUTC.")], HRESULT, 'DaylightTimeBias',
              ( ['retval', 'out'], POINTER(c_int), 'DaylightTimeBias' )),
    COMMETHOD(['propput', helpstring(u"The bias to be used during daylight time. This bias is relative to the time zone's BiasFromUTC.")], HRESULT, 'DaylightTimeBias',
              ( ['in'], c_int, 'DaylightTimeBias' )),
    COMMETHOD(['propget', helpstring(u'Date for transition to standard time.')], HRESULT, 'StandardTimeTransitionTime',
              ( ['retval', 'out'], POINTER(TimeZoneTransitionTime), 'StandardTimeTransitionTime' )),
    COMMETHOD(['propput', helpstring(u'Date for transition to standard time.')], HRESULT, 'StandardTimeTransitionTime',
              ( ['in'], POINTER(TimeZoneTransitionTime), 'StandardTimeTransitionTime' )),
    COMMETHOD(['propget', helpstring(u"The bias to be used during Standard time. This bias is relative to the time zone's BiasFromUTC.")], HRESULT, 'StandardTimeBias',
              ( ['retval', 'out'], POINTER(c_int), 'StandardTimeBias' )),
    COMMETHOD(['propput', helpstring(u"The bias to be used during Standard time. This bias is relative to the time zone's BiasFromUTC.")], HRESULT, 'StandardTimeBias',
              ( ['in'], c_int, 'StandardTimeBias' )),
]
################################################################
## code template for ITimeZoneRule implementation
##class ITimeZoneRule_Impl(object):
##    def _get(self):
##        u"The bias to be used during Standard time. This bias is relative to the time zone's BiasFromUTC."
##        #return StandardTimeBias
##    def _set(self, StandardTimeBias):
##        u"The bias to be used during Standard time. This bias is relative to the time zone's BiasFromUTC."
##    StandardTimeBias = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The time zone bias from UTC in minutes. LocalTime = UtcTime + BiasFromUTC.'
##        #return BiasFromUTC
##    def _set(self, BiasFromUTC):
##        u'The time zone bias from UTC in minutes. LocalTime = UtcTime + BiasFromUTC.'
##    BiasFromUTC = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Date for transition to standard time.'
##        #return StandardTimeTransitionTime
##    def _set(self, StandardTimeTransitionTime):
##        u'Date for transition to standard time.'
##    StandardTimeTransitionTime = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Date for transition to daylight time.'
##        #return DaylightTimeTransitionTime
##    def _set(self, DaylightTimeTransitionTime):
##        u'Date for transition to daylight time.'
##    DaylightTimeTransitionTime = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The year this rule is in effect.'
##        #return Year
##    def _set(self, Year):
##        u'The year this rule is in effect.'
##    Year = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u"The bias to be used during daylight time. This bias is relative to the time zone's BiasFromUTC."
##        #return DaylightTimeBias
##    def _set(self, DaylightTimeBias):
##        u"The bias to be used during daylight time. This bias is relative to the time zone's BiasFromUTC."
##    DaylightTimeBias = property(_get, _set, doc = _set.__doc__)
##

class IWebRequestHandler(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'Provides access to methods that control handing of web requests.'
    _iid_ = GUID('{D1DA21F3-9EC1-40BC-B8A2-CD29A1EBED8D}')
    _idlflags_ = ['oleautomation']
IWebRequestHandler._methods_ = [
    COMMETHOD([helpstring(u'Handles a request with explicit capabilities.')], HRESULT, 'HandleStringWebRequest',
              ( ['in'], esriHttpMethod, 'httpMethod' ),
              ( ['in'], BSTR, 'requestURL' ),
              ( ['in'], BSTR, 'queryString' ),
              ( ['in'], BSTR, 'Capabilities' ),
              ( ['in'], BSTR, 'requestData' ),
              ( ['out'], POINTER(BSTR), 'responseContentType' ),
              ( ['out'], POINTER(esriWebResponseDataType), 'respDataType' ),
              ( ['retval', 'out'], POINTER(_midlSAFEARRAY(c_ubyte)), 'responseData' )),
]
################################################################
## code template for IWebRequestHandler implementation
##class IWebRequestHandler_Impl(object):
##    def HandleStringWebRequest(self, httpMethod, requestURL, queryString, Capabilities, requestData):
##        u'Handles a request with explicit capabilities.'
##        #return responseContentType, respDataType, responseData
##

IJSONObject._methods_ = [
    COMMETHOD([helpstring(u'Parses JSON object from string into memory.')], HRESULT, 'ParseString',
              ( ['in'], BSTR, 'json' )),
    COMMETHOD([helpstring(u'Parses JSON object from IJSONReader into memory. Useful if you want to have random acces to just a part of a JSON.')], HRESULT, 'ParseJSON',
              ( ['in'], POINTER(IJSONReader), 'pReader' )),
    COMMETHOD(['propget', helpstring(u'Returns true if member name lookups are case-sensitive. Default value is true. Methods affected by this state change: MemberExists, IsValueNull and all TryGet... methods.')], HRESULT, 'CaseSensitiveNames',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'case_sensitive' )),
    COMMETHOD(['propput', helpstring(u'Returns true if member name lookups are case-sensitive. Default value is true. Methods affected by this state change: MemberExists, IsValueNull and all TryGet... methods.')], HRESULT, 'CaseSensitiveNames',
              ( ['in'], VARIANT_BOOL, 'case_sensitive' )),
    COMMETHOD([helpstring(u'Checks if a member with the given name exists.')], HRESULT, 'MemberExists',
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'exists' )),
    COMMETHOD([helpstring(u"Returns VARIANT_TRUE if member is undefined or member's value is null. Returns VARIANT_FALSE if member exists and its value is not null.")], HRESULT, 'IsValueNull',
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsNull' )),
    COMMETHOD(['propget', helpstring(u'Returns size of member collection.')], HRESULT, 'MemberCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD([helpstring(u'Returns member name and value at a given index.')], HRESULT, 'GetMemberAt',
              ( ['in'], c_int, 'index' ),
              ( ['out'], POINTER(BSTR), 'Name' ),
              ( ['out'], POINTER(VARIANT), 'Value' )),
    COMMETHOD([helpstring(u"Returns member value for a given name. If member does not exist, returns VARIANT_FALSE in 'success' parameter.")], HRESULT, 'TryGetValue',
              ( ['in'], BSTR, 'Name' ),
              ( ['out'], POINTER(VARIANT), 'Value' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'success' )),
    COMMETHOD([helpstring(u"Returns member value for a given name as DATE. If member does not exist or type coercion fails, returns VARIANT_FALSE in 'success' parameter.")], HRESULT, 'TryGetValueAsDate',
              ( ['in'], BSTR, 'Name' ),
              ( ['out'], POINTER(c_double), 'Value' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'success' )),
    COMMETHOD([helpstring(u"Returns member value for a given name as boolean. If member does not exist or type coercion fails, returns VARIANT_FALSE in 'success' parameter.")], HRESULT, 'TryGetValueAsBoolean',
              ( ['in'], BSTR, 'Name' ),
              ( ['out'], POINTER(VARIANT_BOOL), 'Value' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'success' )),
    COMMETHOD([helpstring(u"Returns member value for a given name as long. If member does not exist or type coercion fails, returns VARIANT_FALSE in 'success' parameter.")], HRESULT, 'TryGetValueAsLong',
              ( ['in'], BSTR, 'Name' ),
              ( ['out'], POINTER(c_int), 'Value' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'success' )),
    COMMETHOD([helpstring(u"Returns member value for a given name as double. If member does not exist or type coercion fails, returns VARIANT_FALSE in 'success' parameter.")], HRESULT, 'TryGetValueAsDouble',
              ( ['in'], BSTR, 'Name' ),
              ( ['out'], POINTER(c_double), 'Value' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'success' )),
    COMMETHOD([helpstring(u"Returns member value for a given name as string. If member does not exist or type coercion fails, returns VARIANT_FALSE in 'success' parameter.")], HRESULT, 'TryGetValueAsString',
              ( ['in'], BSTR, 'Name' ),
              ( ['out'], POINTER(BSTR), 'Value' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'success' )),
    COMMETHOD([helpstring(u"Returns member value for a given name as IJSONObject. If member does not exist or type coercion fails, returns VARIANT_FALSE in 'success' parameter.")], HRESULT, 'TryGetValueAsObject',
              ( ['in'], BSTR, 'Name' ),
              ( ['out'], POINTER(POINTER(IJSONObject)), 'Value' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'success' )),
    COMMETHOD([helpstring(u"Returns member value for a given name as IJSONArray. If member does not exist or type coercion fails, returns VARIANT_FALSE in 'success' parameter.")], HRESULT, 'TryGetValueAsArray',
              ( ['in'], BSTR, 'Name' ),
              ( ['out'], POINTER(POINTER(IJSONArray)), 'Value' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'success' )),
    COMMETHOD([helpstring(u'Adds new member name-value pair to the member collection. Returns E_FAIL if duplicate member is found.')], HRESULT, 'AddDate',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], c_double, 'Value' )),
    COMMETHOD([helpstring(u'Adds new member name-value pair to the member collection. Returns E_FAIL if duplicate member is found.')], HRESULT, 'AddBoolean',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], VARIANT_BOOL, 'Value' )),
    COMMETHOD([helpstring(u'Adds new member name-value pair to the member collection. Returns E_FAIL if duplicate member is found.')], HRESULT, 'AddLong',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([helpstring(u'Adds new member name-value pair to the member collection. Returns E_FAIL if duplicate member is found.')], HRESULT, 'AddDouble',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], c_double, 'Value' )),
    COMMETHOD([helpstring(u'Adds new member name-value pair to the member collection. Returns E_FAIL if duplicate member is found.')], HRESULT, 'AddString',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], BSTR, 'Value' )),
    COMMETHOD([helpstring(u'Adds new member with the value of null to the member collection. Returns E_FAIL if duplicate member is found.')], HRESULT, 'AddNull',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD([helpstring(u'Adds new member name-value pair to the member collection. Returns E_FAIL if duplicate member is found.')], HRESULT, 'Add',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], VARIANT, 'Value' )),
    COMMETHOD([helpstring(u'Adds new member name-value pair to the member collection. Returns E_FAIL if duplicate member is found.')], HRESULT, 'AddJSONObject',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], POINTER(IJSONObject), 'Value' )),
    COMMETHOD([helpstring(u'Adds new member name-value pair to the member collection. Returns E_FAIL if duplicate member is found.')], HRESULT, 'AddJSONArray',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], POINTER(IJSONArray), 'Value' )),
    COMMETHOD([helpstring(u'Creates and adds new member name-value pair to the member collection. Returns E_FAIL if duplicate member is found.')], HRESULT, 'CreateMemberObject',
              ( ['in'], BSTR, 'Name' ),
              ( ['out'], POINTER(POINTER(IJSONObject)), 'Value' )),
    COMMETHOD([helpstring(u'Creates and adds new member name-value pair to the member collection. Returns E_FAIL if duplicate member is found.')], HRESULT, 'CreateMemberArray',
              ( ['in'], BSTR, 'Name' ),
              ( ['out'], POINTER(POINTER(IJSONArray)), 'Value' )),
    COMMETHOD([helpstring(u'Make a designated member NULL.')], HRESULT, 'MakeValueNull',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD([helpstring(u"Converts IJSONObject to JSON representation using IJSONWriter internally. 'props' parameter is to control IJSONWriter properties. It's safe to set it to NULL. ")], HRESULT, 'ToJSONString',
              ( ['in'], POINTER(IPropertySet), 'props' ),
              ( ['retval', 'out'], POINTER(BSTR), 'outStr' )),
    COMMETHOD([helpstring(u'Converts IJSONObject to JSON representation using provided IJSONWriter. Useful when you have complex JSON response you want to combine from the output of several methods.')], HRESULT, 'ToJSON',
              ( ['in'], BSTR, 'objectName' ),
              ( ['in'], POINTER(IJSONWriter), 'pWriter' )),
    COMMETHOD([helpstring(u'Remove a member from the member collection.')], HRESULT, 'RemoveMember',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD([helpstring(u'Removes all members.')], HRESULT, 'ClearAll'),
    COMMETHOD([helpstring(u'Adds new member name-value pair to the member collection. Stores precision for use in ToJSON and ToJSONString. Returns E_FAIL if duplicate member is found.')], HRESULT, 'AddDoubleEx',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], c_double, 'Value' ),
              ( ['in'], c_int, 'precision' )),
]
################################################################
## code template for IJSONObject implementation
##class IJSONObject_Impl(object):
##    def AddDoubleEx(self, Name, Value, precision):
##        u'Adds new member name-value pair to the member collection. Stores precision for use in ToJSON and ToJSONString. Returns E_FAIL if duplicate member is found.'
##        #return 
##
##    def TryGetValueAsArray(self, Name):
##        u"Returns member value for a given name as IJSONArray. If member does not exist or type coercion fails, returns VARIANT_FALSE in 'success' parameter."
##        #return Value, success
##
##    def TryGetValueAsBoolean(self, Name):
##        u"Returns member value for a given name as boolean. If member does not exist or type coercion fails, returns VARIANT_FALSE in 'success' parameter."
##        #return Value, success
##
##    def AddDate(self, Name, Value):
##        u'Adds new member name-value pair to the member collection. Returns E_FAIL if duplicate member is found.'
##        #return 
##
##    def _get(self):
##        u'Returns true if member name lookups are case-sensitive. Default value is true. Methods affected by this state change: MemberExists, IsValueNull and all TryGet... methods.'
##        #return case_sensitive
##    def _set(self, case_sensitive):
##        u'Returns true if member name lookups are case-sensitive. Default value is true. Methods affected by this state change: MemberExists, IsValueNull and all TryGet... methods.'
##    CaseSensitiveNames = property(_get, _set, doc = _set.__doc__)
##
##    def Add(self, Name, Value):
##        u'Adds new member name-value pair to the member collection. Returns E_FAIL if duplicate member is found.'
##        #return 
##
##    def IsValueNull(self, Name):
##        u"Returns VARIANT_TRUE if member is undefined or member's value is null. Returns VARIANT_FALSE if member exists and its value is not null."
##        #return IsNull
##
##    def CreateMemberArray(self, Name):
##        u'Creates and adds new member name-value pair to the member collection. Returns E_FAIL if duplicate member is found.'
##        #return Value
##
##    def ToJSONString(self, props):
##        u"Converts IJSONObject to JSON representation using IJSONWriter internally. 'props' parameter is to control IJSONWriter properties. It's safe to set it to NULL. "
##        #return outStr
##
##    def ClearAll(self):
##        u'Removes all members.'
##        #return 
##
##    def TryGetValueAsDate(self, Name):
##        u"Returns member value for a given name as DATE. If member does not exist or type coercion fails, returns VARIANT_FALSE in 'success' parameter."
##        #return Value, success
##
##    def AddBoolean(self, Name, Value):
##        u'Adds new member name-value pair to the member collection. Returns E_FAIL if duplicate member is found.'
##        #return 
##
##    def MemberExists(self, Name):
##        u'Checks if a member with the given name exists.'
##        #return exists
##
##    def TryGetValue(self, Name):
##        u"Returns member value for a given name. If member does not exist, returns VARIANT_FALSE in 'success' parameter."
##        #return Value, success
##
##    def ParseJSON(self, pReader):
##        u'Parses JSON object from IJSONReader into memory. Useful if you want to have random acces to just a part of a JSON.'
##        #return 
##
##    def MakeValueNull(self, Name):
##        u'Make a designated member NULL.'
##        #return 
##
##    def TryGetValueAsString(self, Name):
##        u"Returns member value for a given name as string. If member does not exist or type coercion fails, returns VARIANT_FALSE in 'success' parameter."
##        #return Value, success
##
##    def RemoveMember(self, Name):
##        u'Remove a member from the member collection.'
##        #return 
##
##    def ParseString(self, json):
##        u'Parses JSON object from string into memory.'
##        #return 
##
##    def AddJSONObject(self, Name, Value):
##        u'Adds new member name-value pair to the member collection. Returns E_FAIL if duplicate member is found.'
##        #return 
##
##    @property
##    def MemberCount(self):
##        u'Returns size of member collection.'
##        #return Count
##
##    def TryGetValueAsLong(self, Name):
##        u"Returns member value for a given name as long. If member does not exist or type coercion fails, returns VARIANT_FALSE in 'success' parameter."
##        #return Value, success
##
##    def TryGetValueAsDouble(self, Name):
##        u"Returns member value for a given name as double. If member does not exist or type coercion fails, returns VARIANT_FALSE in 'success' parameter."
##        #return Value, success
##
##    def AddNull(self, Name):
##        u'Adds new member with the value of null to the member collection. Returns E_FAIL if duplicate member is found.'
##        #return 
##
##    def TryGetValueAsObject(self, Name):
##        u"Returns member value for a given name as IJSONObject. If member does not exist or type coercion fails, returns VARIANT_FALSE in 'success' parameter."
##        #return Value, success
##
##    def AddString(self, Name, Value):
##        u'Adds new member name-value pair to the member collection. Returns E_FAIL if duplicate member is found.'
##        #return 
##
##    def AddJSONArray(self, Name, Value):
##        u'Adds new member name-value pair to the member collection. Returns E_FAIL if duplicate member is found.'
##        #return 
##
##    def AddLong(self, Name, Value):
##        u'Adds new member name-value pair to the member collection. Returns E_FAIL if duplicate member is found.'
##        #return 
##
##    def GetMemberAt(self, index):
##        u'Returns member name and value at a given index.'
##        #return Name, Value
##
##    def AddDouble(self, Name, Value):
##        u'Adds new member name-value pair to the member collection. Returns E_FAIL if duplicate member is found.'
##        #return 
##
##    def CreateMemberObject(self, Name):
##        u'Creates and adds new member name-value pair to the member collection. Returns E_FAIL if duplicate member is found.'
##        #return Value
##
##    def ToJSON(self, objectName, pWriter):
##        u'Converts IJSONObject to JSON representation using provided IJSONWriter. Useful when you have complex JSON response you want to combine from the output of several methods.'
##        #return 
##


# values for enumeration 'esriTimeRelation'
esriTimeRelationOverlaps = 0
esriTimeRelationOverlapsStartWithinEnd = 1
esriTimeRelationAfterStartOverlapsEnd = 2
esriTimeRelation = c_int # enum
_TimeZoneTransitionTime._fields_ = [
    ('Year', c_short),
    ('Month', c_short),
    ('DayOfWeek', c_short),
    ('DayOccurrence', c_short),
    ('Hour', c_short),
    ('Minute', c_short),
    ('Second', c_short),
    ('Milliseconds', c_short),
]
assert sizeof(_TimeZoneTransitionTime) == 16, sizeof(_TimeZoneTransitionTime)
assert alignment(_TimeZoneTransitionTime) == 2, alignment(_TimeZoneTransitionTime)
IRESTOperation._methods_ = [
    COMMETHOD(['propget', helpstring(u"Operation name. Used in IRESTRequestHandler's schema generation and url parsing.")], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'Operation parameters, separated by comma.')], HRESULT, 'Parameters',
              ( ['retval', 'out'], POINTER(BSTR), 'Parameters' )),
    COMMETHOD(['propget', helpstring(u'Supported output formats, separated by comma.')], HRESULT, 'OutputFormats',
              ( ['retval', 'out'], POINTER(BSTR), 'OutputFormats' )),
    COMMETHOD(['propget', helpstring(u'Required capability for the operation.')], HRESULT, 'RequiredCapability',
              ( ['retval', 'out'], POINTER(BSTR), 'capability' )),
    COMMETHOD(['propget', helpstring(u'Denotes POST-only operations.')], HRESULT, 'PostOnly',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([helpstring(u'Converts operation object to JSON representation.')], HRESULT, 'ToJSONObject',
              ( ['retval', 'out'], POINTER(POINTER(IJSONObject)), 'pObj' )),
    COMMETHOD(['propput', helpstring(u"Operation name. Used in IRESTRequestHandler's schema generation and url parsing.")], HRESULT, 'Name',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD(['propput', helpstring(u'Operation parameters, separated by comma.')], HRESULT, 'Parameters',
              ( ['in'], BSTR, 'Parameters' )),
    COMMETHOD(['propput', helpstring(u'Supported output formats, separated by comma.')], HRESULT, 'OutputFormats',
              ( ['in'], BSTR, 'OutputFormats' )),
    COMMETHOD(['propput', helpstring(u'Required capability for the operation.')], HRESULT, 'RequiredCapability',
              ( ['in'], BSTR, 'capability' )),
    COMMETHOD(['propput', helpstring(u'Denotes POST-only operations.')], HRESULT, 'PostOnly',
              ( ['in'], VARIANT_BOOL, 'Value' )),
]
################################################################
## code template for IRESTOperation implementation
##class IRESTOperation_Impl(object):
##    def ToJSONObject(self):
##        u'Converts operation object to JSON representation.'
##        #return pObj
##
##    def _get(self):
##        u"Operation name. Used in IRESTRequestHandler's schema generation and url parsing."
##        #return Name
##    def _set(self, Name):
##        u"Operation name. Used in IRESTRequestHandler's schema generation and url parsing."
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Operation parameters, separated by comma.'
##        #return Parameters
##    def _set(self, Parameters):
##        u'Operation parameters, separated by comma.'
##    Parameters = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Required capability for the operation.'
##        #return capability
##    def _set(self, capability):
##        u'Required capability for the operation.'
##    RequiredCapability = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Denotes POST-only operations.'
##        #return Value
##    def _set(self, Value):
##        u'Denotes POST-only operations.'
##    PostOnly = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Supported output formats, separated by comma.'
##        #return OutputFormats
##    def _set(self, OutputFormats):
##        u'Supported output formats, separated by comma.'
##    OutputFormats = property(_get, _set, doc = _set.__doc__)
##

IByteSwapStreamIO._methods_ = [
    COMMETHOD(['propputref', helpstring(u'The stream to perform byte swap reads and writes to.')], HRESULT, 'Stream',
              ( ['in'], POINTER(IStream), 'ppStream' )),
    COMMETHOD(['propget', helpstring(u'The stream to perform byte swap reads and writes to.')], HRESULT, 'Stream',
              ( ['retval', 'out'], POINTER(POINTER(IStream)), 'ppStream' )),
    COMMETHOD([helpstring(u'Perform a read byte swapping to the native format.')], HRESULT, 'Read',
              ( ['in'], esriByteSwapDataType, 'dataType' ),
              ( ['out'], c_void_p, 'pv' ),
              ( ['in'], c_ulong, 'cb' ),
              ( ['out'], POINTER(c_ulong), 'pcbRead' )),
    COMMETHOD([helpstring(u'Perform a write byte swapping to the windows format.')], HRESULT, 'Write',
              ( ['in'], esriByteSwapDataType, 'dataType' ),
              ( ['in'], c_void_p, 'pv' ),
              ( ['in'], c_ulong, 'cb' ),
              ( ['out'], POINTER(c_ulong), 'pcbWritten' )),
]
################################################################
## code template for IByteSwapStreamIO implementation
##class IByteSwapStreamIO_Impl(object):
##    def Read(self, dataType, cb):
##        u'Perform a read byte swapping to the native format.'
##        #return pv, pcbRead
##
##    def Write(self, dataType, pv, cb):
##        u'Perform a write byte swapping to the windows format.'
##        #return pcbWritten
##
##    @property
##    def Stream(self, ppStream):
##        u'The stream to perform byte swap reads and writes to.'
##        #return 
##

IXMLReader2._methods_ = [
    COMMETHOD(['propget', helpstring(u'XML representation of the current element.')], HRESULT, 'XML',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([helpstring(u'Reads the current element value as an int64.')], HRESULT, 'ReadInt64',
              ( ['retval', 'out'], POINTER(c_longlong), 'Value' )),
]
################################################################
## code template for IXMLReader2 implementation
##class IXMLReader2_Impl(object):
##    @property
##    def XML(self):
##        u'XML representation of the current element.'
##        #return Value
##
##    def ReadInt64(self):
##        u'Reads the current element value as an int64.'
##        #return Value
##

IXMLWriter._methods_ = [
    COMMETHOD([helpstring(u'Specifies output XML stream.')], HRESULT, 'WriteTo',
              ( ['in'], POINTER(IStream), 'outputStream' )),
    COMMETHOD([helpstring(u'Writes the starting tag of an element.')], HRESULT, 'WriteStartTag',
              ( ['in'], BSTR, 'LocalName' ),
              ( ['in'], BSTR, 'uri' ),
              ( ['in'], POINTER(IXMLAttributes), 'Attributes' ),
              ( ['in'], POINTER(IXMLNamespaces), 'namespaces' ),
              ( ['in'], VARIANT_BOOL, 'isEmpty' )),
    COMMETHOD([helpstring(u'Writes the text value of an element.')], HRESULT, 'WriteText',
              ( ['in'], BSTR, 'Text' )),
    COMMETHOD([helpstring(u'Writes a CDATA section.')], HRESULT, 'WriteCData',
              ( ['in'], BSTR, 'cdata' )),
    COMMETHOD([helpstring(u'Writes the ending tag of an element.')], HRESULT, 'WriteEndTag'),
    COMMETHOD([helpstring(u'Writes an element value as a boolean.')], HRESULT, 'WriteBoolean',
              ( ['in'], VARIANT_BOOL, 'Value' )),
    COMMETHOD([helpstring(u'Writes an element value as a byte.')], HRESULT, 'WriteByte',
              ( ['in'], c_ubyte, 'Value' )),
    COMMETHOD([helpstring(u'Writes an element value as a short.')], HRESULT, 'WriteShort',
              ( ['in'], c_short, 'Value' )),
    COMMETHOD([helpstring(u'Writes an element value as a long.')], HRESULT, 'WriteInteger',
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([helpstring(u'Writes an element value as a float.')], HRESULT, 'WriteFloat',
              ( ['in'], c_float, 'Value' )),
    COMMETHOD([helpstring(u'Writes an element value as a double.')], HRESULT, 'WriteDouble',
              ( ['in'], c_double, 'Value' )),
    COMMETHOD([helpstring(u'Writes an element value as a date.')], HRESULT, 'WriteDate',
              ( ['in'], c_double, 'Value' )),
    COMMETHOD([helpstring(u'Writes an element value as a binary array.')], HRESULT, 'WriteBinary',
              ( ['in'], POINTER(_midlSAFEARRAY(c_ubyte)), 'Value' )),
    COMMETHOD([helpstring(u'Writes an element value as a variant.')], HRESULT, 'WriteVariant',
              ( ['in'], VARIANT, 'Value' )),
    COMMETHOD([helpstring(u'Writes raw XML.')], HRESULT, 'WriteXML',
              ( ['in'], BSTR, 'XML' )),
    COMMETHOD([helpstring(u'Writes the XML document declaration.')], HRESULT, 'WriteXMLDeclaration'),
    COMMETHOD([helpstring(u'Writes a newline.')], HRESULT, 'WriteNewLine'),
    COMMETHOD([helpstring(u'Writes a tab.')], HRESULT, 'WriteTab'),
    COMMETHOD([helpstring(u'Obtains the declared namespace prefix for a namespace.')], HRESULT, 'LookupNamespace',
              ( ['in'], BSTR, 'uri' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Prefix' )),
]
################################################################
## code template for IXMLWriter implementation
##class IXMLWriter_Impl(object):
##    def WriteDate(self, Value):
##        u'Writes an element value as a date.'
##        #return 
##
##    def WriteText(self, Text):
##        u'Writes the text value of an element.'
##        #return 
##
##    def WriteNewLine(self):
##        u'Writes a newline.'
##        #return 
##
##    def WriteBoolean(self, Value):
##        u'Writes an element value as a boolean.'
##        #return 
##
##    def WriteShort(self, Value):
##        u'Writes an element value as a short.'
##        #return 
##
##    def LookupNamespace(self, uri):
##        u'Obtains the declared namespace prefix for a namespace.'
##        #return Prefix
##
##    def WriteTo(self, outputStream):
##        u'Specifies output XML stream.'
##        #return 
##
##    def WriteTab(self):
##        u'Writes a tab.'
##        #return 
##
##    def WriteXMLDeclaration(self):
##        u'Writes the XML document declaration.'
##        #return 
##
##    def WriteXML(self, XML):
##        u'Writes raw XML.'
##        #return 
##
##    def WriteDouble(self, Value):
##        u'Writes an element value as a double.'
##        #return 
##
##    def WriteFloat(self, Value):
##        u'Writes an element value as a float.'
##        #return 
##
##    def WriteVariant(self, Value):
##        u'Writes an element value as a variant.'
##        #return 
##
##    def WriteByte(self, Value):
##        u'Writes an element value as a byte.'
##        #return 
##
##    def WriteEndTag(self):
##        u'Writes the ending tag of an element.'
##        #return 
##
##    def WriteInteger(self, Value):
##        u'Writes an element value as a long.'
##        #return 
##
##    def WriteStartTag(self, LocalName, uri, Attributes, namespaces, isEmpty):
##        u'Writes the starting tag of an element.'
##        #return 
##
##    def WriteBinary(self, Value):
##        u'Writes an element value as a binary array.'
##        #return 
##
##    def WriteCData(self, cdata):
##        u'Writes a CDATA section.'
##        #return 
##

IRESTResource._methods_ = [
    COMMETHOD(['propget', helpstring(u"Resource name. Used in IRESTRequestHandler's schema generation and url parsing.")], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD(['propget', helpstring(u'Specifies collection resource.')], HRESULT, 'IsCollection',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD(['propget', helpstring(u"Specifies 'default' collection resource that can be accessed without explicitly using its name in the URL.")], HRESULT, 'IsDefaultCollection',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD(['propget', helpstring(u'This flag marks resources that do not change over time.')], HRESULT, 'IsStatic',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD(['propget', helpstring(u'This flag is only for a root level resource. If this flag is true, IRRH implementation supports ETag.')], HRESULT, 'SupportsETag',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD(['propget', helpstring(u'Required capability for the resource.')], HRESULT, 'RequiredCapability',
              ( ['retval', 'out'], POINTER(BSTR), 'capability' )),
    COMMETHOD(['propput', helpstring(u"Resource name. Used in IRESTRequestHandler's schema generation and url parsing.")], HRESULT, 'Name',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD(['propput', helpstring(u'Specifies collection resource.')], HRESULT, 'IsCollection',
              ( ['in'], VARIANT_BOOL, 'Value' )),
    COMMETHOD(['propput', helpstring(u"Specifies 'default' collection resource that can be accessed without explicitly using its name in the URL.")], HRESULT, 'IsDefaultCollection',
              ( ['in'], VARIANT_BOOL, 'Value' )),
    COMMETHOD(['propput', helpstring(u'This flag marks resources that do not change over time.')], HRESULT, 'IsStatic',
              ( ['in'], VARIANT_BOOL, 'Value' )),
    COMMETHOD(['propput', helpstring(u'This flag is only for a root level resource. If this flag is true, IRRH implementation supports ETag.')], HRESULT, 'SupportsETag',
              ( ['in'], VARIANT_BOOL, 'Value' )),
    COMMETHOD(['propput', helpstring(u'Required capability for the resource.')], HRESULT, 'RequiredCapability',
              ( ['in'], BSTR, 'capability' )),
    COMMETHOD([helpstring(u'Converts resource object to JSON representation.')], HRESULT, 'ToJSONObject',
              ( ['retval', 'out'], POINTER(POINTER(IJSONObject)), 'pObj' )),
    COMMETHOD([helpstring(u'Adds child resource.')], HRESULT, 'AddResource',
              ( ['in'], POINTER(IRESTResource), 'r' )),
    COMMETHOD([helpstring(u'Adds child operation.')], HRESULT, 'AddOperation',
              ( ['in'], POINTER(IRESTOperation), 'o' )),
    COMMETHOD([helpstring(u'Finds child resource, non-recursive.')], HRESULT, 'FindChildResource',
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(POINTER(IRESTResource)), 'ppObj' )),
    COMMETHOD([helpstring(u'Finds child operation, non-recursive.')], HRESULT, 'FindChildOperation',
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(POINTER(IRESTOperation)), 'ppObj' )),
    COMMETHOD([helpstring(u'Returns enumerator for immediate child resources.')], HRESULT, 'GetResources',
              ( ['retval', 'out'], POINTER(POINTER(IEnumRESTResource)), 'ppEnum' )),
    COMMETHOD([helpstring(u'Returns enumerator for operations.')], HRESULT, 'GetOperations',
              ( ['retval', 'out'], POINTER(POINTER(IEnumRESTOperation)), 'ppEnum' )),
]
################################################################
## code template for IRESTResource implementation
##class IRESTResource_Impl(object):
##    def _get(self):
##        u'Specifies collection resource.'
##        #return Value
##    def _set(self, Value):
##        u'Specifies collection resource.'
##    IsCollection = property(_get, _set, doc = _set.__doc__)
##
##    def ToJSONObject(self):
##        u'Converts resource object to JSON representation.'
##        #return pObj
##
##    def _get(self):
##        u'This flag marks resources that do not change over time.'
##        #return Value
##    def _set(self, Value):
##        u'This flag marks resources that do not change over time.'
##    IsStatic = property(_get, _set, doc = _set.__doc__)
##
##    def GetOperations(self):
##        u'Returns enumerator for operations.'
##        #return ppEnum
##
##    def _get(self):
##        u"Resource name. Used in IRESTRequestHandler's schema generation and url parsing."
##        #return Name
##    def _set(self, Name):
##        u"Resource name. Used in IRESTRequestHandler's schema generation and url parsing."
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Required capability for the resource.'
##        #return capability
##    def _set(self, capability):
##        u'Required capability for the resource.'
##    RequiredCapability = property(_get, _set, doc = _set.__doc__)
##
##    def AddOperation(self, o):
##        u'Adds child operation.'
##        #return 
##
##    def AddResource(self, r):
##        u'Adds child resource.'
##        #return 
##
##    def FindChildOperation(self, Name):
##        u'Finds child operation, non-recursive.'
##        #return ppObj
##
##    def FindChildResource(self, Name):
##        u'Finds child resource, non-recursive.'
##        #return ppObj
##
##    def _get(self):
##        u"Specifies 'default' collection resource that can be accessed without explicitly using its name in the URL."
##        #return Value
##    def _set(self, Value):
##        u"Specifies 'default' collection resource that can be accessed without explicitly using its name in the URL."
##    IsDefaultCollection = property(_get, _set, doc = _set.__doc__)
##
##    def GetResources(self):
##        u'Returns enumerator for immediate child resources.'
##        #return ppEnum
##
##    def _get(self):
##        u'This flag is only for a root level resource. If this flag is true, IRRH implementation supports ETag.'
##        #return Value
##    def _set(self, Value):
##        u'This flag is only for a root level resource. If this flag is true, IRRH implementation supports ETag.'
##    SupportsETag = property(_get, _set, doc = _set.__doc__)
##

ITimeRelationalOperator._methods_ = [
    COMMETHOD([helpstring(u'Indicates whether the two time values are of the same type and define the same time values.')], HRESULT, 'Equals',
              ( ['in'], POINTER(ITimeValue), 'otherTimeValue' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Equals' )),
    COMMETHOD([helpstring(u'Indicates whether the input time value falls fully outside of the time extent.')], HRESULT, 'Disjoint',
              ( ['in'], POINTER(ITimeValue), 'otherTimeValue' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Disjoint' )),
    COMMETHOD([helpstring(u'Indicates whether the boundaries of the time values intersect.')], HRESULT, 'Touches',
              ( ['in'], POINTER(ITimeValue), 'otherTimeValue' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Touches' )),
    COMMETHOD([helpstring(u'Indicates whether this time value is contained (is within) the other time value.')], HRESULT, 'Within',
              ( ['in'], POINTER(ITimeValue), 'otherTimeValue' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Within' )),
    COMMETHOD([helpstring(u'Indicates whether this time value contains the other time value.')], HRESULT, 'Contains',
              ( ['in'], POINTER(ITimeValue), 'otherTimeValue' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Contains' )),
]
################################################################
## code template for ITimeRelationalOperator implementation
##class ITimeRelationalOperator_Impl(object):
##    def Disjoint(self, otherTimeValue):
##        u'Indicates whether the input time value falls fully outside of the time extent.'
##        #return Disjoint
##
##    def Touches(self, otherTimeValue):
##        u'Indicates whether the boundaries of the time values intersect.'
##        #return Touches
##
##    def Within(self, otherTimeValue):
##        u'Indicates whether this time value is contained (is within) the other time value.'
##        #return Within
##
##    def Contains(self, otherTimeValue):
##        u'Indicates whether this time value contains the other time value.'
##        #return Contains
##
##    def Equals(self, otherTimeValue):
##        u'Indicates whether the two time values are of the same type and define the same time values.'
##        #return Equals
##

IAoInitialize._methods_ = [
    COMMETHOD([helpstring(u'Check if the Product Code is available.')], HRESULT, 'IsProductCodeAvailable',
              ( ['in'], esriLicenseProductCode, 'ProductCode' ),
              ( ['retval', 'out'], POINTER(esriLicenseStatus), 'licenseStatus' )),
    COMMETHOD([helpstring(u'Check if the Product Code is available and then the Extension Code for that product.')], HRESULT, 'IsExtensionCodeAvailable',
              ( ['in'], esriLicenseProductCode, 'ProductCode' ),
              ( ['in'], esriLicenseExtensionCode, 'extensionCode' ),
              ( ['retval', 'out'], POINTER(esriLicenseStatus), 'licenseStatus' )),
    COMMETHOD([helpstring(u'This must be called before any other ArcObjects are created to initialize product Code. If called a second time during the life time of an executable with a new product code, it will return esriLicenseAlreadyInitialized.')], HRESULT, 'Initialize',
              ( ['in'], esriLicenseProductCode, 'ProductCode' ),
              ( ['retval', 'out'], POINTER(esriLicenseStatus), 'licenseStatus' )),
    COMMETHOD([helpstring(u'Check out an extension.')], HRESULT, 'CheckOutExtension',
              ( ['in'], esriLicenseExtensionCode, 'extensionCode' ),
              ( ['retval', 'out'], POINTER(esriLicenseStatus), 'licenseStatus' )),
    COMMETHOD([helpstring(u'Check in an extension.')], HRESULT, 'CheckInExtension',
              ( ['in'], esriLicenseExtensionCode, 'extensionCode' ),
              ( ['retval', 'out'], POINTER(esriLicenseStatus), 'licenseStatus' )),
    COMMETHOD([helpstring(u'Shutdown method.  This should be the last call to ArcObjects in an application.')], HRESULT, 'Shutdown'),
    COMMETHOD([helpstring(u"Retrieve's the product code at which the application has been initialized.")], HRESULT, 'InitializedProduct',
              ( ['retval', 'out'], POINTER(esriLicenseProductCode), 'ProductCode' )),
    COMMETHOD([helpstring(u'Is the Extension checked out.')], HRESULT, 'IsExtensionCheckedOut',
              ( ['in'], esriLicenseExtensionCode, 'extensionCode' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'checkedOut' )),
]
################################################################
## code template for IAoInitialize implementation
##class IAoInitialize_Impl(object):
##    def IsExtensionCheckedOut(self, extensionCode):
##        u'Is the Extension checked out.'
##        #return checkedOut
##
##    def CheckInExtension(self, extensionCode):
##        u'Check in an extension.'
##        #return licenseStatus
##
##    def IsExtensionCodeAvailable(self, ProductCode, extensionCode):
##        u'Check if the Product Code is available and then the Extension Code for that product.'
##        #return licenseStatus
##
##    def Shutdown(self):
##        u'Shutdown method.  This should be the last call to ArcObjects in an application.'
##        #return 
##
##    def Initialize(self, ProductCode):
##        u'This must be called before any other ArcObjects are created to initialize product Code. If called a second time during the life time of an executable with a new product code, it will return esriLicenseAlreadyInitialized.'
##        #return licenseStatus
##
##    def IsProductCodeAvailable(self, ProductCode):
##        u'Check if the Product Code is available.'
##        #return licenseStatus
##
##    def CheckOutExtension(self, extensionCode):
##        u'Check out an extension.'
##        #return licenseStatus
##
##    def InitializedProduct(self):
##        u"Retrieve's the product code at which the application has been initialized."
##        #return ProductCode
##

ILicenseInfoEnum._methods_ = [
    COMMETHOD([helpstring(u'Resets the extension code.')], HRESULT, 'Reset'),
    COMMETHOD([helpstring(u'Obtains the next extension code.')], HRESULT, 'Next',
              ( ['retval', 'out'], POINTER(esriLicenseExtensionCode), 'extensionCode' )),
]
################################################################
## code template for ILicenseInfoEnum implementation
##class ILicenseInfoEnum_Impl(object):
##    def Reset(self):
##        u'Resets the extension code.'
##        #return 
##
##    def Next(self):
##        u'Obtains the next extension code.'
##        #return extensionCode
##

IXMLWriter2._methods_ = [
    COMMETHOD(['propget', helpstring(u'Obtains underlying stream. If WriteTo() is not called yet, will return NULL.')], HRESULT, 'Stream',
              ( ['retval', 'out'], POINTER(POINTER(IStream)), 'ppStream' )),
    COMMETHOD([helpstring(u'Writes an element value as an int64.')], HRESULT, 'WriteInt64',
              ( ['in'], c_longlong, 'Value' )),
]
################################################################
## code template for IXMLWriter2 implementation
##class IXMLWriter2_Impl(object):
##    def WriteInt64(self, Value):
##        u'Writes an element value as an int64.'
##        #return 
##
##    @property
##    def Stream(self):
##        u'Obtains underlying stream. If WriteTo() is not called yet, will return NULL.'
##        #return ppStream
##

class IJSONDeserializer(IExternalDeserializer):
    _case_insensitive_ = True
    u'Provides access to high-level JSON deserialization methods.'
    _iid_ = GUID('{1E6DC0EB-5C8A-4401-A8AF-BB5602DDFB7E}')
    _idlflags_ = ['oleautomation']
IJSONDeserializer._methods_ = [
    COMMETHOD(['propget', helpstring(u'Obtains JSON Reader.')], HRESULT, 'Reader',
              ( ['retval', 'out'], POINTER(POINTER(IJSONReader)), 'ppReader' )),
    COMMETHOD([helpstring(u'Write deserialization options.')], HRESULT, 'InitDeserializer',
              ( ['in'], POINTER(IJSONReader), 'pReader' ),
              ( ['in'], POINTER(IPropertySet), 'pProps' )),
]
################################################################
## code template for IJSONDeserializer implementation
##class IJSONDeserializer_Impl(object):
##    def InitDeserializer(self, pReader, pProps):
##        u'Write deserialization options.'
##        #return 
##
##    @property
##    def Reader(self):
##        u'Obtains JSON Reader.'
##        #return ppReader
##

IGenerateStatistics._methods_ = [
    COMMETHOD(['propput', helpstring(u'Indicates if simple statistics are sufficient. These are Count, Minimum, Maximum, Sum, Mean, Standard Deviation.')], HRESULT, 'SimpleStats',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD(['propput', helpstring(u'Indicates if the statistics represent a sample of the data (used for calculating standard deviation).')], HRESULT, 'Sample',
              ( ['in'], VARIANT_BOOL, 'rhs' )),
    COMMETHOD([helpstring(u'Clears out the currently gathered statistics.')], HRESULT, 'Reset',
              ( ['in'], VARIANT_BOOL, 'SimpleStats' )),
    COMMETHOD([helpstring(u'Adds a data value to the collection of values used to derive the statistics.')], HRESULT, 'AddValue',
              ( ['in'], c_double, 'Value' )),
    COMMETHOD([helpstring(u'May be called after all values have been added to establish frequeny table (the function is not required any more).')], HRESULT, 'FinalCompute'),
]
################################################################
## code template for IGenerateStatistics implementation
##class IGenerateStatistics_Impl(object):
##    def _set(self, rhs):
##        u'Indicates if simple statistics are sufficient. These are Count, Minimum, Maximum, Sum, Mean, Standard Deviation.'
##    SimpleStats = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        u'Indicates if the statistics represent a sample of the data (used for calculating standard deviation).'
##    Sample = property(fset = _set, doc = _set.__doc__)
##
##    def Reset(self, SimpleStats):
##        u'Clears out the currently gathered statistics.'
##        #return 
##
##    def FinalCompute(self):
##        u'May be called after all values have been added to establish frequeny table (the function is not required any more).'
##        #return 
##
##    def AddValue(self, Value):
##        u'Adds a data value to the collection of values used to derive the statistics.'
##        #return 
##

__all__ = ['IAngularConverter',
           'esriLicenseExtensionCodeWorkflowManager',
           'esriTSFYearThruDayWithDash',
           'esriLicenseExtensionCodeNautical', 'TimeExtent',
           'esriSystemMessageCode_ErrorReadXml', 'JSONEndOfArray',
           'IXMLFlags', 'IObjectConstruct', 'CoRESTOperation',
           'esriAnimationDrawing', 'esriDTPolar', 'IRectHolder',
           'esriDecimeters',
           'esriSystemMessageCode_XMLTypeMappingFailed',
           'IMemoryBlobStream', 'esriLicenseExtensionCodeBathymetry',
           'esriBSDTWCHAR', 'esriProductCodePublisher',
           'esriJobMessageTypeProcessStart', 'esriLockMgrSchemaRead',
           'esriProductCodeServerAdvancedEdition',
           'esriTSFYearThruMinuteWithDash', 'esriLicenseUnavailable',
           'EnvironmentManager', 'esriSquareMiles', 'esriUnitsLast',
           'esriAGSInternetMessageFormatBin', 'esriSquareYards',
           'IClassifyMinMax2', 'esriTSFYearThruDay', 'esriBSDTULONG',
           'MESSAGESUPPORT_E_FORBIDDEN', 'IVariantArray',
           'IFractionFormat', 'esriProductInstalled',
           'esriTSFYearThruSubSecond', 'esriJobMessageTypeError',
           'esriProductCodeNautical', 'esriJobMessageType',
           'FileName', 'esriProductCodeSchematics',
           'esriSystemMessageCode_ErrorImportFromMem',
           'esriServerMessageCodeEnum', 'esriDrawPolyPolyline',
           'IXMLSerializerAlt', '_esriPointAttributes',
           'esriProductCodeDesigner', 'esriLicenseCheckedIn',
           'esriPointAttributesEx', 'esriITFYearOnly', 'FileNames',
           'IJSONSerializer', 'esriProductCodeRuntimeBasic',
           'esriArcGISVersion92', 'esriJobCancelled',
           'esriArcGISVersion93', 'IEnumBSTR', 'IExtensionManager',
           'JSONStartOfObject', 'IWebRequestHandler', 'IJobResults',
           'esriSystemMessageCode_ErrorSaveToString',
           'XML_SERIALIZE_E_INVALIDENUMVALUE',
           'esriLicenseExtensionCodeCOGO', 'TimeReference',
           'MESSAGESUPPORT_E_SSL_CACERT', 'esriTransportTypeEmbedded',
           'JobMessages', 'esriProductCodeHighways',
           'esriByteSwapDataType',
           'esriLicenseExtensionCodeServerStandardEdition',
           'esriJobCancelling', 'esriBSDTbool',
           'esriLicenseExtensionCodeTIFFLZW', 'esriAres',
           'esriProductsInstalledServerJAVA',
           'esriTextureCompressionJPEG', 'esriPoints',
           'esriLicenseExtensionCodeVirtualEarthEng',
           'esriProductCodeIntelAgency', 'IDeviationInterval',
           'esriProductCodeBusinessStandard', 'esriAlignRight',
           'IArray', 'esriDecimalDegrees', 'esriTimeUnitsCenturies',
           'IXMLStream', 'esriProductCodeCOGO', 'IXMLSerialize',
           'esriProductCodeItaly', 'esriProductCodeBelgium',
           'esriScaleFormat', 'XMLFlags', 'ILatLonFormat',
           'esriTimeLocaleFormat', 'esriLicenseProductCode',
           'IEnvironmentManager', 'esriLicenseNotLicensed',
           'DefinedInterval', 'esriLicenseExtensionCodeSchematics',
           'esriLicenseNotInitialized', 'ITestConnection',
           'ILocaleInfo', 'esriDUGons',
           'MESSAGESUPPORT_E_AUTH_TOKEN_REQUIRED',
           'esriLicenseExtensionCodeHighways', 'DirectionFormat',
           'esriAnimationPrinting', 'ESRIScriptEngine',
           'StandardDeviation', 'IAnimationProgressor',
           'esriProductsInstalledReader', 'esriTimeUnitsMilliseconds',
           'MESSAGESUPPORT_E_UNAUTHORIZED', 'esriTLFLongDate',
           'MESSAGESUPPORT_E_SSL_CONNECT_ERROR', 'ILog2',
           'IPropertySetArray', 'esriTSFYearThruSecondWithDash',
           'CurrencyFormat', 'INumberFormat', 'Time',
           'IPersistVariant', 'IFrequencyStatistics',
           'esriSystemMessageCode_SetResponseStreamVersion',
           'XMLNamespaces', 'ITrackCancel2', 'JSONArray',
           'esriJobDeleted', 'esriArcGISVersion90',
           'esriBSDTULONGLONG', 'esriTimeStringFormat',
           'esriTSFYearThruSecondWithSlash',
           'esriTSFYearThruMonthWithDash', 'XMLStream',
           'esriJobDeleting', 'esriSystemMessageCodeEnum',
           'WKSTimeDuration', 'E_REQUIRES_SERVER_STANDARD_EDITION',
           'IJSONObject', 'esriAGSInternetMessageFormat',
           'ITimeExtent', 'IESRIScriptEngine', 'esriHectares',
           'IMessage', 'esriLicenseExtensionCode3DAnalyst',
           'IStatisticsResults', 'IComponentCategoryManager',
           'esriProductCodeDefenseUS',
           'SCRIPTENGINE_E_CANNOT_COCREATE_VBSCRIPT_CONTROL',
           'IZlibCompression', 'IClassID',
           'MESSAGESUPPORT_E_COULDNT_RESOLVE_HOST', 'IXMLReader',
           'esriProductCodeVBAExtension',
           'MESSAGESUPPORT_E_SSL_PEER_CERTIFICATE', 'ILog',
           'WKSDateTime', 'esriTransportTypeUrl',
           'esriProductCodeVector',
           'esriLicenseExtensionCodeRuntimeStandard', 'IZipArchive',
           'MemoryBlobStream', 'esriLicenseAvailable',
           'esriESDisabled', 'IVariantStream',
           'esriTextureCompressionType', 'esriAcres', 'INameFactory',
           'IRateFormat', 'MESSAGESUPPORT_E_NOT_IMPLEMENTED',
           'esriDFDegreesMinutesSeconds', 'IExtension',
           'esriLicenseExtensionCodeSchematicsSDK',
           'esriDTSouthAzimuth', 'scriptEngineError',
           'esriTSFYearThruMinute',
           'esriSystemMessageCode_ErrorLoadBinaryStream',
           'IJITExtensionManager', 'IJSONWriter2',
           'E_NO_PRODUCT_LICENSE',
           'esriSystemMessageCode_BinaryResponseSent',
           'esriLicenseExtensionCodeServerAdvancedEdition',
           'IExtensionConfig', 'IFileNames', 'esriRoundingOptionEnum',
           'esriSystemMessageCode_CertFailed', 'TimeInstant',
           'esriLicenseExtensionCodePublisher', 'AoAuthorizeLicense',
           'XML_SERIALIZE_E_CONVFAILED', 'esriProductCodeNetwork',
           'esriExtensionState', 'esriLicenseProductCodeBasic',
           'esriLicenseExtensionCodeProductionMapping',
           'XMLSerializerAlt', 'IPercentageFormat', 'IStringArray',
           'esriLicenseExtensionCodeBusiness', 'JSONWriter',
           'IJobInfo', 'IServerEnvironment2', 'IServerEnvironment3',
           'AngularConverter', 'ITimeValue',
           'esriRoundNumberOfDecimals', 'IObjectStream',
           'IAngularConverter2', 'ITimeZoneFactory', 'ITime',
           'esriLicenseExtensionCodeAeronautical', 'esriUnknownUnits',
           'IPersistStream', '_TimeZoneTransitionTime',
           'esriProductCodeArcScan', 'IProductInstalled',
           'esriTSFYearThruHourWithDash', 'WKSEnvelopeZ',
           'IArcGISLocale', 'esriProductCodeArcMapServer',
           'esriDPGeography', 'esriTimeUnitsMinutes',
           'esriLicenseExtensionCodeMrSID', 'IJobFilter',
           'AngleFormat', 'VariantStreamIO', 'esriDrawPhase',
           'esriCaseAppearance', 'LocaleInfo', 'IEnumVariantSimple',
           'esriReadWrite', 'IParseNameString',
           'esriLicenseExtensionCodeArcMapServer', 'CategoryFactory',
           'VarArray', 'ISet', 'esriDrawMoveTo', 'Quantile',
           'esriProductCodeRuntimeStandard',
           'XML_SERIALIZE_E_CANT_MAP_XMLTYPE_TO_CLASS', 'IArray2',
           'esriSquareCentimeters', 'esriAreaUnits',
           'esriTextureCompressionNone', 'IRESTDispatcher',
           'IParentExtension', 'esriDrawPolyBezier',
           'esriDirectionUnits', 'IIntervalRange2', 'LongArray',
           'esriAbsoluteScale', 'esriProductCodeTIFFLZW',
           'esriProductCodeMappingAgency', 'esriProductCodeMLE',
           'ProductInstalled', 'esriWRDTFileToReturn',
           'esriProductCodeUnitedKingdom', 'IServerUserInfo',
           'IObjectCopy', 'esriProductsInstalledDesktop',
           'IParentLicenseExtension', 'esriCaseAppearanceUnchanged',
           'esriLicenseExtensionCodeVideo',
           'esriTSFYearThruHourWithSlash',
           'esriDrawPolyPolygonNoBorder', 'esriBSDTBYTE',
           'ITimeDuration', 'IProgressor', 'ICategoryFactory',
           'esriProductCodeGeoStats', 'IByteSwapStreamIO',
           'MESSAGESUPPORT_E_AUTH_TOKEN_FAILURE',
           'esriITFYearThruMinute',
           'esriProductCodeDataInteroperability',
           'esriLicenseExtensionCodeDataReViewer',
           'esriLicenseCheckedOut', 'ISequentialStream',
           'IJobDefinition', 'esriProductCodeSchematicsSDK',
           'esriLicenseProductCodeAdvanced', 'NameFactory',
           'esriTimeUnitsSeconds',
           'esriLicenseExtensionCodeDefenseUS', 'WKSEnvelope',
           'IJSONDeserializer', 'JSONTokenType',
           'esriJobMessageTypeProcessDefinition', 'IProxyServerInfo2',
           'esriSquareInches', 'esriLicenseExtensionCodeDesigner',
           'IScaleFormat', 'IXMLSerializeData',
           'esriLicenseExtensionCodeBusinessStandard',
           'IRESTCallback', 'esriProductCodeSpain',
           'esriLicenseExtensionCodeStreetMap', 'RateFormat',
           'esriLicenseAlreadyInitialized', 'esriTLFDefaultDateTime',
           'PropertySet', 'esriTimeUnitsHours',
           'esriDrawPolygonNoBorder', 'TimeZoneFactory',
           'esriTSFYearThruHour', 'E_NO_EXTENSION_LICENSE',
           'esriLicenseExtensionCodeArcPress', 'IShortcutName',
           'esriArcGISVersion10', 'JSONReader', 'esriTimeUnitsWeeks',
           'esriImperialScale', 'esriTimeUnits', 'esriLicenseFailure',
           'esriLicenseExtensionCodeIntelAgency',
           'esriITFYearThruDay', 'esriProductCodeTracking',
           'esriAnimationLast', 'MESSAGESUPPORT_E_GET_TOKEN_FAILED',
           'esriWRDTPayload', 'esriProductCodeAdvanced',
           'esriProductsInstalledEngineRuntime',
           'IExtensionManagerAdmin', 'Set', 'esriBSDTunsignedint',
           'esriDrawPolyPolygon', 'esriTSFYearThruDayWithSlash',
           'AoInitialize', 'IUnitConverter', 'ICustomNumberFormat',
           'IChildExtension', 'esriReadOnly',
           'esriLicenseExtensionCodeDefense',
           'esriTextureCompressionNever',
           'esriSystemMessageCode_ErrorWriteXml', 'IBlobStream',
           'esriUnknownAreaUnits', 'ICheckProgressor', 'IJSONReader2',
           'esriDTQuadrantBearing', 'InputDeviceManager',
           'esriDrawBeginPath', 'IXMLVersionSupport',
           'XML_SERIALIZE_E_UNKNOWN', 'IClone', 'JSONNull',
           'XMLSerializer', 'esriSquareDecimeters',
           'esriJobSubmitted', 'ArcGISLocale', 'ESRILicenseInfo',
           'IEnumRESTOperation', 'ILogSupport', 'xmlSerializeError',
           'StrArray', 'IDirectionFormat', 'ZipArchive',
           'esriDPAnnotation', 'esriHttpMethodDelete',
           'IXMLObjectElement', 'esriFeet', 'esriAreaUnitsLast',
           'esriDrawRectangle',
           'MESSAGESUPPORT_E_PROXY_GATEWAY_ERROR',
           'esriProductCodeDenmark', '_WKSEnvelopeZ', 'IZipArchiveEx',
           'esriSystemMessageCode_StringRequestReceived',
           'esriSquareMeters', 'esriCoreErrorReturnCodes',
           'esriPointAttributes', 'ShortcutName',
           'esriLicenseProductCodeEngineGeoDB', 'esriBSDTUSHORT',
           'esriProductCodeBingMaps', 'IAngleFormat',
           'IServerEnvironment', 'esriProductCode', 'esriTLFLongTime',
           'esriProductCodePortugal', 'esriInches',
           'esriTLFShortDate', 'esriProductCodeImageExt',
           'esriJobMessageTypeWarning', 'esriAnimations',
           'IInputDeviceManager', 'esriBSDTDOUBLE',
           'IErrorCollection', 'IEnumName', 'esriTimeUnitsYears',
           'IStatusBar', 'esriSegmentModifier',
           'MESSAGESUPPORT_E_MEM_ALLOC_FAILED',
           'INumberFormatOperations', 'EqualInterval', 'tagSTATSTG',
           'esriSystemMessageCode_ErrorWriteBinaryResponse',
           'TimeZoneRule', 'esriProductCodeProductionMapping',
           'IRESTRequestHandler',
           'esriLicenseExtensionCodeDefenseINTL', '_WKSPoint',
           'esriLicenseExtensionCodeRuntimeAdvanced', 'IJobMessage',
           'JSONBoolean', 'esriProductCodeMrSID', 'esriBSDTBOOLU',
           'esriITFYearThruHour', 'esriDrawArcCCW', 'OLE_HANDLE',
           'esriSystemMessageCode_AuthFailed', 'IAuthorizeLicense',
           'IClassify', 'MESSAGESUPPORT_E_NOT_ACCEPTABLE',
           'esriProductCodeAeronautical', 'SSLInfo', '_WKSPointZ',
           'ILatLonFormat2', 'esriDrawCircle',
           'MESSAGESUPPORT_E_REQUEST_TOLARGE', 'ITime2',
           'esriHttpMethodGet', 'esriMeters', 'IClassifyMinMax',
           'IGenerateStatistics', 'IJobRegistry',
           'esriProductCodeTIN', 'IStream', 'esriKilometers',
           'IAMFWriter', 'MESSAGESUPPORT_E_COULDNT_CONNECT',
           'SystemHelper', 'esriHttpMethodOptions',
           'esriProductCodeSwitzerland', 'esriBSDTLONGLONG',
           'esriProductCodeBusiness', 'esriESEnabled',
           'BaseStatistics', 'esriDrawMultipoint',
           'esriSystemMessageCode_BinaryRequestReceived', 'ISSLInfo',
           'IESRILicenseInfo', 'IGlobeCompression',
           'JSONStartOfArray', 'esriLicenseExtensionCodeNetwork',
           'MESSAGESUPPORT_E_URL_MALFORMAT',
           'esriLicenseServerEditionAdvanced',
           'MESSAGESUPPORT_E_BAD_REQUEST', 'esriLockMgrWrite',
           'ComponentCategoryManager',
           'esriLicenseExtensionCodeVBAExtension', 'IJobMessages',
           'esriHttpMethodHead', 'IEnumNameEdit',
           'esriHttpMethodTrace', 'MESSAGESUPPORT_E_NO_CONTENT',
           'CoRESTDispatcher', 'esriJobMessageTypeProcessStop',
           'esriMillimeters', 'esriLicenseExtensionCodeBingMapsEng',
           'XMLAttributes', 'MESSAGESUPPORT_E_INTERNAL_SERVER_ERROR',
           'esriTextureCompressionJPEGPlus', 'esriProductCodeReader',
           'esriLicenseProductCodeArcServer',
           'esriTSFYearThruMinuteWithSlash', 'ILicenseInfoEnum',
           'esriJobMessageTypeEmpty', 'IJobTracker',
           'esriProductCodeBingMapsEng',
           'esriProductCodeServerStandardEdition',
           'esriJobMessageTypeAbort', 'JSONUndefined',
           'esriTimeRelationOverlapsStartWithinEnd', 'esriBSDTFLOAT',
           'esriLicenseProductCodeStandard', 'esriYards',
           'ObjectCopy', 'IStepProgressor', 'esriLockMgrType',
           'esriAlignLeft', 'IFileNames2', 'IMemoryBlobStream2',
           'FileStream', 'IPropertySupport', 'ITimeOffsetOperator',
           'MESSAGESUPPORT_E_SERVICE_NOT_AVAILABLE',
           'esriLicenseExtensionCode', 'AMFWriter', 'INumericFormat',
           'esriDrawPolyline', 'esriDPSelection', 'ISupportErrorInfo',
           'esriTimeUnitsUnknown', 'IComponentCategoryInfo',
           'esriHttpMethodPut',
           'esriSystemMessageCode_ErrorLoadFromString',
           'IXMLPersistedObject', 'esriProductCodeLuxembourg',
           'esriLicenseExtensionCodeMLE', 'IMemoryBlobStreamVariant',
           'NumericFormat', 'esriITFYearThruMonth',
           'esriLicenseExtensionCodeBingMaps',
           'esriLicenseExtensionCodeVector', 'CustomNumberFormat',
           'esriProductCodeNetherlands', 'ILongArray',
           'XMLTypeMapper', 'ProxyServerInfo',
           'MESSAGESUPPORT_E_COULDNT_RESOLVE_PROXY', 'IFile',
           'esriMiles', 'esriProductCodeDefense',
           'esriLicenseExtensionCodeAGINSPIRE', 'ITextureCompression',
           'esriProductCodeStreetMap', 'IUID',
           'esriTSFYearThruSecond', 'esriJobTimedOut', 'IXMLWriter',
           'esriLicenseExtensionCodeDataInteroperability',
           'esriTSFYearThruSubSecondWithSlash',
           'esriWebResponseDataType', 'IVariantStreamIO',
           'esriTSFYearThruMonth',
           'MESSAGESUPPORT_E_OPERATION_TIMEDOUT', 'esriDrawPolygon',
           'IXMLSerializeData2', 'IXMLNamespaces',
           'esriNumericAlignmentEnum', 'IEnumRESTResource',
           'esriBSDTchar', 'FractionFormat',
           'esriDUDegreesMinutesSeconds',
           'esriProductCodeWorkflowManager',
           'esriSpecifyFractionDenominator', 'esriDrawEndPath',
           'IRequestHandler2', 'esriCentimeters', 'esriCustomScale',
           'esriSquareKilometers', 'esriJobExecuting',
           'ITimeRelationalOperator', 'esriLockMgrEdit',
           'esriJobSucceeded', 'JSONValueDelimiter',
           'ScientificFormat',
           'esriLicenseExtensionCodeMappingAgency', 'ITimeReference',
           'LatLonFormat', 'esriProductCodeFrance', 'IXMLWriter2',
           'esriArcGISVersion101', 'esriProductCodeVirtualEarthEng',
           'JSONString', 'esriLockMgrSchemaWrite', 'LicenseInfoEnum',
           'IEnumUID', 'JSONObject', 'esriProductCodeDefenseINTL',
           'IErrorInfo', 'ExtensionManager', 'ITimeZoneInfo',
           'ScaleFormat', 'E_NOTLICENSED',
           'esriLicenseServerEditionStandard',
           'TimeZoneTransitionTime',
           'esriLicenseExtensionCodeAirports',
           'esriLicenseServerEditionBasic', 'IScientificNumberFormat',
           'esriDrawArcCW', 'IAoInitialize',
           'esriSpecifyFractionDigits', 'esriHttpMethodPost',
           'esriProductCodeSweden', 'JSONEndOfObject',
           'XMLPersistedObject', 'IDocumentVersionSupportGEN',
           'esriDrawStop', 'esriProductCodeDataReViewer',
           'esriTSFYearThruMonthWithSlash', 'OLE_COLOR',
           'esriProductCodeGermany', 'esriFractionOptionEnum', 'UID',
           'IExtensionAccelerators', 'ITimeZoneFactory2',
           'IPropertySet', 'esriProductCodeAGINSPIRE',
           'messageSupportError', 'esriJobStatus', 'IObjectUpdate',
           'esriSquareFeet', 'IAutoExtension',
           'esriTimeRelationAfterStartOverlapsEnd', 'esriDUGradians',
           'esriLicenseStatus', 'esriJobWaiting',
           'esriProductCodeServerEnterprise', 'esriNauticalMiles',
           'PropertySetArray', 'esriProductCodeBasic',
           'esriProductCodeArcPress', 'esriLockMgrRead', 'JobMessage',
           'MESSAGESUPPORT_E_BAD_GATEWAY',
           'esriLicenseExtensionCodeTracking',
           'esriLicenseExtensionCodeGeoStats', 'esriUnits',
           'esriProductPostCodesMajorRoads', 'esriTransportType',
           'MESSAGESUPPORT_E_METHOD_NOT_ALLOWED', 'IIntervalRange',
           'GeometricalInterval', 'JSONNumber',
           'esriITFYearThruSecond', 'ILicenseInformation',
           'esriTimeUnitsDays', 'esriDFQuadrantBearing',
           'esriTimeRelationOverlaps', 'esriJobNew',
           'esriDrawTrapezoids', 'IClassifyGEN',
           '_esriPointAttributesEx', 'IFileName', 'IProxyServerInfo',
           'NaturalBreaks', 'esriProductCodeAirports',
           'esriLockMgrNone', 'XMLWriter',
           'esriTSFYearThruSubSecondWithDash', 'esriDURadians',
           'UnitConverter', 'esriCaseAppearanceLower',
           'esriLicenseExtensionCodeRuntimeBasic',
           'esriProductCodeStandard', 'esriProductCodeVirtualEarth',
           'MESSAGESUPPORT_E_REQUEST_TIMEOUT', 'IDocumentVersion',
           'MESSAGESUPPORT_E_PROXY_AUTHENTICATION_REQUIRED',
           'IXMLReader2', 'esriLicenseExtensionCodeServerEnterprise',
           'IExternalSerializer', 'IXMLTypeMapper2',
           'esriSystemMessageCode_HTTPConnectionFailed',
           'esriLicenseExtensionCodeVirtualEarth',
           'esriSystemMessageCode_RequestFailed',
           'esriProductsInstalledServerNET', 'IEnumNamedID',
           'ITimeInstant', 'esriLicenseExtensionCodeSpatialAnalyst',
           'IDoubleArray', 'XMLReader', 'IJob',
           '_esriSegmentModifier', 'Message',
           'JSONPropertyValueDelimiter', 'IXMLTypeMapper',
           'esriTLFShortTime', 'esriArcGISVersion', 'DoubleArray',
           'IExternalDeserializer', 'esriProductCodeBathymetry',
           'esriProductCodeRuntimeAdvanced', 'esriDrawOp',
           'PercentageFormat', 'esriProductCodeGrid', 'IJSONWriter',
           'IRequestHandler', 'esriArcGISVersion83',
           'MESSAGESUPPORT_E_INVALID_GET_FILE',
           'esriSquareMillimeters', 'esriDirectionType',
           'esriAGSInternetMessageFormatSoap',
           'SCRIPTENGINE_E_CANNOT_COCREATE_JSCRIPT_CONTROL',
           'esriBSDTGUID', 'esriTimeRelation', 'IName',
           'esriProductCodeAustria', 'ITimeZoneRule', 'TimeDuration',
           'esriLicenseExtensionCodeArcScan',
           'esriLicenseServerEdition', 'ByteSwapStreamIO',
           'IXMLSerializer', 'IXMLAttributes', 'CoRESTResource',
           'esriSystemMessageCode_Debug',
           'esriSystemMessageCode_StringResponseSent',
           'esriESUnavailable', 'esriProductCodeReaderPro',
           'IJSONReader', '_WKSTimeDuration', 'IRESTOperation',
           'esriBSDTLONG', 'esriTimeUnitsMonths', 'IJSONArray',
           '_WKSDateTime', 'esriJobFailed',
           'esriArcGISVersionCurrent', 'esriTSFYearOnly',
           'esriFilePermission', 'E_REQUIRES_SERVER_ADVANCED_EDITION',
           'TimeZoneInfo', '_WKSEnvelope', 'esriProductCodeMPSAtlas',
           'esriProductCodeAllEurope', 'esriAnimationOther',
           'esriJobMessageTypeInformative',
           'esriLicenseExtensionCodeImageExt', 'ISystemBridge',
           'IRESTResource', 'IJobCatalog', 'ObjectStream',
           'esriHttpMethod', 'esriCaseAppearanceUpper',
           'IAMFSerializer', 'esriLicenseUntrusted',
           'IObjectValidate', 'ITrackCancel',
           'esriDirectionFormatEnum', 'esriIntegerTimeFormat',
           'IPropertySet2', 'esriLicenseProductCodeEngine',
           'esriBSDTSHORT', 'esriDUDecimalDegrees', 'WKSPoint',
           'esriRoundNumberOfSignificantDigits', 'IObjectActivate',
           'esriLicenseExtensionCodeMPSAtlas', 'esriTimeUnitsDecades',
           'MESSAGESUPPORT_E_NOT_FOUND', 'esriProductCodeVideo',
           'esriDTNorthAzimuth',
           'MESSAGESUPPORT_E_UNSUPPORTED_PROTOCOL', 'WKSPointZ']
from comtypes import _check_version; _check_version('501')

import arcpy
import pythonaddins
import webbrowser
import functools
import threading
import os

def run_in_other_thread(function):
    # functool.wraps will copy over the docstring and some other metadata
    # from the original function
    @functools.wraps(function)
    def fn_(*args, **kwargs):
        thread = threading.Thread(target=function, args=args, kwargs=kwargs)
        thread.start()
        thread.join()
    return fn_

startfile = run_in_other_thread(os.startfile)
openbrowser = run_in_other_thread(webbrowser.open)

class ButtonClass6(object):
    """Implementation for RemoveData_addin.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        openbrowser(r"http://arcgis.com")

class ComboBoxClass5(object):
    """Implementation for RemoveData_addin.combobox (ComboBox)"""
    def __init__(self):
        self.items = ["item1", "item2", "item3"]
        self.editable = True
        self.enabled = True
        self.dropdownWidth = 'WWWWWW'
        self.width = 'WWWWWW'
    def onSelChange(self, selection):
        pass
    def onEditChange(self, text):
        pass
    def onFocus(self, focused):
        pass
    def onEnter(self):
        pass
    def refresh(self):
        self.items = []

class DataDelete(object):
    """Implementation for RemoveData_addin.extension2 (Extension)"""
    def __init__(self):
        # For performance considerations, please remove all unused methods in this class.
        self.enabled = True

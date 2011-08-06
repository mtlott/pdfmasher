# Created By: Virgil Dupras
# Created On: 2011-08-04
# Copyright 2011 Hardcoded Software (http://www.hardcoded.net)
# 
# This software is licensed under the "BSD" License as described in the "LICENSE" file, 
# which should be included with this package. The terms are also available at 
# http://www.hardcoded.net/licenses/bsd_license

from hscommon.cocoa.inter import PyGUIObject, signature

from core.gui.page_controller import PageController

class PyPageController(PyGUIObject):
    py_class = PageController
    
    def setChildren_(self, children):
        self.py.set_children([child.py for child in children])
    
    def prevPage(self):
        self.py.prev_page()
    
    def nextPage(self):
        self.py.next_page()
    
    def pageLabel(self):
        return self.py.page_label
    
    @signature('v@:c')
    def setReorderMode_(self, flag):
        self.py.page_repr.reorder_mode = flag
    
    #--- model -> view calls:
    def refresh_page_label(self):
        self.cocoa.refreshPageLabel()
    
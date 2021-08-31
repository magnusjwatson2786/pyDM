from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from ui.custom_pb import CustomPb
import requests, sys, concurrent.futures,time, os, re, platform
import res_rc
from ui.ui_dlitem_g import Ui_Form
verbose=False
class GUISignal(QObject):
    signal_val = Signal(int)

class Ui_Dlitem(QWidget):
    def __init__ (self, link:str,lidx:int,myparent = None):
        # super(Ui_Dlitem, self).__init__(parent)
        QWidget.__init__(self)
        self.itemUI = Ui_Form()
        self.itemUI.setupUi(self)
        if verbose: print("setup")
        self.link = link
        self.lidx=lidx
        self.flen=0
        self.csize=512*1024
        self.dlen=0
        self.strt=0
        self.br=False
        self.filename="dlitem"
        self.checkurl(self.link)
        self.setfilename()
        self.gui_connection = GUISignal()

        self.itemUI.progressBar.setValue(0)
        self.gui_connection.signal_val.connect(self.itemUI.progressBar.setValue)
        self.itemUI.label_2.setText(QCoreApplication.translate("Form", self.filename, None))
        self.itemUI.pushButton.clicked.connect(self.pause)
        self.itemUI.label.setScaledContents(True)
        self.itemUI.pushButton_3.clicked.connect(lambda: print("delete"))
        if verbose: print("ready")
        # self.myparent=myparent
    def checkurl(self,url):
        try:
            r=requests.head(url)
        except:
            print("Oops!", sys.exc_info()[0], "occurred.")
        else:
            # print(r.headers)
            if 'Location' in r.headers.keys():
                self.checkurl(r.headers['Location'])
            # print(r.headers['Location'])
            else:
                # print(r.url,r.headers['content-length'])
                self.link=str(r.url)
                self.flen=r.headers['content-length']

    def setfilename(self):
        temp=self.link.split("/")[-1]
        if len(temp)>100:
            temp=temp[:100]
        temp=temp.split("?")[0]
        self.filename=temp
    
    def pause(self):
        if self.br:
            self.br=False
        else:
            self.br=True
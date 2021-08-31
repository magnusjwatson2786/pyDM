
# from GUI.ui.dladdfxns import Addfxns
import requests, sys, concurrent.futures,time, os, re, platform
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from dlic import Dlitem

from ui import *

widgets = None
verbose= False

import res_rc

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        widgets.pushButton_5.clicked.connect(lambda: Fxns.toggleMenu(self, True))
        Fxns.toggleMenu(self, True)
        Fxns.fxnsdef(self)
        
        widgets.pushButton_6.clicked.connect(self.buttonClick)
        widgets.pushButton_7.clicked.connect(self.buttonClick)
        widgets.pushButton_8.clicked.connect(self.buttonClick)
        widgets.pushButton_9.clicked.connect(self.buttonClick)
        widgets.pushButton_10.clicked.connect(self.buttonClick)

        self.show()

        themeFile = "themes\deep_ocean.qss"
        Fxns.theme(self, themeFile, True)

        widgets.stackedWidget.setCurrentWidget(widgets.page_3)
        widgets.label.setText("Tasks - YTD")
        widgets.tabWidget.setCurrentWidget(widgets.tab)
        widgets.pushButton_7.setStyleSheet(Fxns.selectMenu(widgets.pushButton_7.styleSheet()))

        self.q=[]
        self.h=[]
        self.l=[]
        self.c=0
        self.br=False
        self.executor=concurrent.futures.ThreadPoolExecutor()
        self.videofiles=[".mp4",".mkv",".avi","webm",".flv",".wmv"]
        self.audiofiles=[".mp3",".wav",".aac",".opus",".flac"]
        self.imagefiles=[".png","jpg",".jpeg",".gif",".bmp",".ico"]
        self.appfiles=[".exe",".msi"]

        # self.ui.listWidget.setStyleSheet("QListWidget::item, QListWidget::item:hover, QListWidget::item:selected"
        #                                 "{background-color:#0B0D16;"
        #                                 "border: 3px solid #0A0C15;}")
        


    def buttonClick(self):
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "pushButton_6":
            self.openAddDialog()

        if btnName == "pushButton_7":
            widgets.stackedWidget.setCurrentWidget(widgets.page_3)
            Fxns.resetStyle(self, btnName)
            btn.setStyleSheet(Fxns.selectMenu(btn.styleSheet()))
            widgets.label.setText("Tasks - YTD")

        if btnName == "pushButton_8":
            widgets.stackedWidget.setCurrentWidget(widgets.page) 
            Fxns.resetStyle(self, btnName) 
            btn.setStyleSheet(Fxns.selectMenu(btn.styleSheet()))
            widgets.label.setText("History - YTD")

        if btnName == "pushButton_9":
            self.close()

        if btnName == "pushButton_10":
            widgets.stackedWidget.setCurrentWidget(widgets.page_2)
            Fxns.resetStyle(self, btnName, True)
            widgets.label.setText("Settings - YTD")

    
    def mousePressEvent(self, event):
        # self.dragPos = event.globalPos() # Deprecated function
        p = event.globalPosition()
        self.dragPos = p.toPoint()

    def openAddDialog(self):
        # self.addDialog = QDialog()
        # self.dialogUI = Ui_Addbox()
        # self.dialogUI.setupUi(self.addDialog)
        # self.addDialog.setWindowModality(Qt.ApplicationModal)
        # Addfxns.setfxns(self.addDialog, self.dialogUI)
        # self.addDialog.show()
        # self.dialogUI.cancelbtn.clicked.connect(self.addDialog.close)
        # self.dialogUI.addbtn.clicked.connect(lambda: self.add(self.dialogUI.urlbox.toPlainText()))
        addnew=Addfxns(myparent=self)


    # def urlAdd(self, goturl):
    #     if self.validateUrl(goturl):
    #         self.add(goturl)
    #         self.addDialog.close()
    #     else:
    #         if verbose: print("Invalid URL")

    def validateUrl(self, url):
        regex = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return re.match(regex, str(url))

    def pause(self,x):
        if x.br:
            x.br=False
        else:
            x.br=True

    def add(self, goturl):
        # def submitex(x):
        #     self.q[x]=Ui_Dlitem(link=goturl,lidx=x)
        # if self.validateUrl(goturl):
        x=self.executor.submit(self.q.append,Ui_Dlitem(link=goturl,lidx=self.c))
        # x=self.executor.submit(submitex,self.c)
        # self.q.append(Ui_Dlitem(link=goturl,lidx=self.c))
        # if verbose: print("submitted")
        # self.addDialog.close()
        # x.result()
        # self.q[-1].pushButton.clicked.connect(lambda: self.pause(self.q[-1]))
        myQListWidgetItem = QListWidgetItem(self.ui.listWidget)
        x.result()
        ''' get results'''
        myQListWidgetItem.setSizeHint(self.q[self.c].sizeHint())
        self.ui.listWidget.addItem(myQListWidgetItem)
        
        self.ui.listWidget.setItemWidget(myQListWidgetItem, self.q[self.c])
        self.h.append(self.executor.submit(self.downld, self.q[self.c]))
        
        self.c+=1
        if verbose: print("added")
        self.ui.label_8.setText("")
        # self.ui.plainTextEdit.clear()
    
    # def updateBar(self, obj, val):
    #     QTimer.singleShot(250, lambda: obj.progressBar.setValue(val))
        # obj.progressBar.setValue(val)

    def downld(self,dlclass):
        if verbose: print(dlclass.br)
        headers={}
        loop=1
        if os.path.exists(str(dlclass.filename)):
            if verbose: print("existing instance")
            otf = open(str(dlclass.filename),"ab")
            existSize = os.path.getsize(str(dlclass.filename))
            sizeper=(int(existSize)/int(dlclass.flen))*100
            if verbose: print(sizeper)
            dlclass.gui_connection.signal_val.emit(sizeper)
            # self.updateBar(dlclass,(int(existSize)/int(dlclass.flen))*100) '''signal slot needed'''
            # dlclass.progressBar.setValue((int(existSize)/int(dlclass.flen))*100)
            if verbose: print(existSize)
            if int(existSize) == int(dlclass.flen):
                loop = 0
                if verbose: print("Already Downloaded")
            else:
                headers = {'Range': 'bytes=%d-' % (existSize)}
                dlclass.dlen=int(existSize)
                if verbose: print("Appending")

        # headers = {'Range': 'bytes=%d-%d' % (0, 4197044)}
        else:
            otf = open(str(dlclass.filename),"wb")
            if verbose: print("New Download")
        self.setdlIcon(dlclass)
        if loop:
            try:
                r = requests.get(dlclass.link, headers=headers, stream = True)
                # r = requests.get(dlclass.link, stream = True)
            except:
                print("Oops!", sys.exc_info()[0], "Cant download")
            else:
                a=0
                if verbose: print(str(dlclass.filename))
                # with open(str(dlclass.filename),"ab") as otf:
                for chunk in r.iter_content(chunk_size=dlclass.csize):
                    # global BREAK
                    if dlclass.br:
                        if verbose: print("break")
                        break
                    if chunk:
                        otf.write(chunk)
                        dlclass.dlen+=dlclass.csize
                        if verbose: print((dlclass.dlen/int(dlclass.flen))*100)
                        if round((dlclass.dlen/int(dlclass.flen)*100),1)>a:
                            a=round((dlclass.dlen/int(dlclass.flen)*100),1)
                            # dlclass.progressBar.setValue(a)
                            # self.updateBar(dlclass, a)
                            if a>100:
                                a=100
                            dlclass.gui_connection.signal_val.emit(a)
                            # self.l[dlclass.lidx].setText(QCoreApplication.translate("MainWindow",str(a),None))
                        # self.l[dlclass.lidx].setText(QCoreApplication.translate("MainWindow",str(round((dlclass.dlen/int(dlclass.flen)*100),2)),None))
                # self.l[dlclass.lidx].setText(QCoreApplication.translate("MainWindow", u"Done", None))
        # BREAK=False
        dlclass.br=False
        otf.close()
        if verbose: print(f"download thread for {dlclass.filename} has been terminated")

    def setdlIcon(self, dlclass):
        if dlclass.filename.endswith(tuple(self.videofiles)):
            dlclass.itemUI.label.setPixmap(u":/icons/icons/cil-movie.png")
            # dlclass.itemUI.label.setScaledContents(True)
        elif dlclass.filename.endswith(tuple(self.appfiles)):
            dlclass.itemUI.label.setPixmap(u":/icons/icons/cil-browser.png")
        elif dlclass.filename.endswith(tuple(self.imagefiles)):
            dlclass.itemUI.label.setPixmap(u":/icons/icons/cil-image1.png")
        elif dlclass.filename.endswith(tuple(self.audiofiles)):
            dlclass.itemUI.label.setPixmap(u":/icons/icons/cil-headphones.png")
        else:
            dlclass.itemUI.label.setPixmap(u":/icons/icons/cil-file.png")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
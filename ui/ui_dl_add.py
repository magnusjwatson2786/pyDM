# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dl_addORzXII.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import res_rc

class Ui_Addbox(object):
    def setupUi(self, Addbox):
        if not Addbox.objectName():
            Addbox.setObjectName(u"Addbox")
        Addbox.setWindowModality(Qt.ApplicationModal)
        Addbox.resize(355, 300)
        Addbox.setMinimumSize(QSize(300, 300))
        Addbox.setMaximumSize(QSize(16777215, 300))
        Addbox.setStyleSheet(u"QWidget{\n"
"background-color: #0F111A;\n"
"color:#8590C8;\n"
"font: 10pt \"Segoe UI\";}\n"
"\n"
"QLineEdit {\n"
"	border-color: rgb(12, 86, 156);\n"
"}\n"
"#contentframe .QPushButton {	\n"
"	/*border: 1px solid rgb(52, 59, 72);\n"
"	border-radius:2px;\n"
"	background-color: #27496D;0E161F;*/\n"
"	background-color: rgb(20, 40, 80);\n"
"}\n"
"#contentframe .QPushButton:hover {\n"
"	background-color:#1F2233;\n"
"	color:#DDDDDD;\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#contentframe .QPushButton:pressed {	\n"
"	background-color: #1E3250;\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(22,160,255);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icons/icons/cil-media-stop.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icons/icons/cil-task.png);\n"
"}\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    image:url(:/icons/icons/cil-flip-to-back.png);\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	background: rgb(52, 59, 72);\n"
"	width: 7px;\n"
"	m"
                        "argin: 11px 0 11px 0;\n"
"	/*border-radius: 0px;*/\n"
"}\n"
"QScrollBar::handle:vertical {	\n"
"	background: rgb(22,160,255);\n"
"	min-height: 25px;\n"
"	/*border-radius: 4px*/\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background: rgb(55, 63, 77);	\n"
"	height: 10px;\n"
"	/*border-bottom-left-radius: 4px;\n"
"	border-bottom-right-radius: 4px;*/\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background: rgb(55, 63, 77);\n"
"	height: 10px;\n"
"	/*border-top-left-radius: 4px;\n"
"	border-top-right-radius: 4px;*/\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}")
        Addbox.setSizeGripEnabled(False)
        self.verticalLayout_3 = QVBoxLayout(Addbox)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(Addbox)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"/*background-color: rgb(22, 160, 255)\n"
"background-color: rgb(52, 59, 72);;*/\n"
"background-color: rgb(15, 52, 96);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.titleframe = QFrame(self.frame_2)
        self.titleframe.setObjectName(u"titleframe")
        self.titleframe.setMinimumSize(QSize(0, 29))
        self.titleframe.setMaximumSize(QSize(16777215, 29))
        self.titleframe.setStyleSheet(u"QWidget{\n"
"background-color: #0F111A;\n"
"color:#8590C8;\n"
"font: 10pt \"Segoe UI\";}")
        self.titleframe.setFrameShape(QFrame.StyledPanel)
        self.titleframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.titleframe)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 0, 0, 0)
        self.titlebar = QHBoxLayout()
        self.titlebar.setObjectName(u"titlebar")
        self.titlebar.setContentsMargins(0, -1, 0, -1)
        self.label_2 = QLabel(self.titleframe)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.titlebar.addWidget(self.label_2)

        self.pushButton = QPushButton(self.titleframe)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(24, 24))
        self.pushButton.setMaximumSize(QSize(24, 24))
        self.pushButton.setFocusPolicy(Qt.NoFocus)
        self.pushButton.setStyleSheet(u"QPushButton:hover {\n"
"	background-color:#962128; border-style: solid; border-radius: 4px; \n"
"}\n"
"QPushButton:pressed {\n"
"	 background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; \n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)

        self.titlebar.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.titlebar)


        self.verticalLayout_4.addWidget(self.titleframe)

        self.contentframe = QFrame(self.frame_2)
        self.contentframe.setObjectName(u"contentframe")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.contentframe.sizePolicy().hasHeightForWidth())
        self.contentframe.setSizePolicy(sizePolicy1)
        self.contentframe.setMinimumSize(QSize(0, 181))
        self.contentframe.setMaximumSize(QSize(16777215, 16777215))
        self.contentframe.setStyleSheet(u"QWidget{\n"
"background-color: #0F111A;\n"
"color:#8590C8;\n"
"font: 10pt \"Segoe UI\";}\n"
"\n"
"#contentframe .QPushButton {	\n"
"	/*border: 1px solid rgb(52, 59, 72);\n"
"	border-radius:2px;\n"
"	color: rgb(0, 168, 204);\n"
"	background-color: #27496D;0E161F;*/\n"
"	background-color: rgb(26, 26, 46);\n"
"}\n"
"#contentframe .QPushButton:hover {\n"
"	background-color:rgb(20, 40, 80);\n"
"	color: rgb(0, 168, 204);\n"
"	/*border: 2px solid rgb(61, 70, 86);*/\n"
"	border: 1px solid #00A8CC;\n"
"}\n"
"#contentframe .QPushButton:pressed {	\n"
"	background-color: #1E3250;\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(22,160,255);\n"
"}")
        self.contentframe.setFrameShape(QFrame.StyledPanel)
        self.contentframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.contentframe)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.instructions = QHBoxLayout()
        self.instructions.setObjectName(u"instructions")
        self.label = QLabel(self.contentframe)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.instructions.addWidget(self.label)

        self.analysebtn = QPushButton(self.contentframe)
        self.analysebtn.setObjectName(u"analysebtn")
        self.analysebtn.setMinimumSize(QSize(55, 0))
        self.analysebtn.setFocusPolicy(Qt.TabFocus)
        self.analysebtn.setStyleSheet(u"")

        self.instructions.addWidget(self.analysebtn)


        self.verticalLayout.addLayout(self.instructions)

        self.urlbox = QPlainTextEdit(self.contentframe)
        self.urlbox.setObjectName(u"urlbox")
        self.urlbox.setStyleSheet(u"\n"
"QPlainTextEdit {\n"
"	background-color: rgb(26, 26, 46);\n"
"	padding:3px;\n"
"	border:none;\n"
"	selection-background-color: rgb(22, 160, 255);\n"
"}\n"
"QPlainTextEdit:hover {\n"
"	border: 1px solid #0264AF ;\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 1px solid #0264AF;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.urlbox)

        self.results = QHBoxLayout()
        self.results.setObjectName(u"results")
        self.filename = QLabel(self.contentframe)
        self.filename.setObjectName(u"filename")
        sizePolicy.setHeightForWidth(self.filename.sizePolicy().hasHeightForWidth())
        self.filename.setSizePolicy(sizePolicy)

        self.results.addWidget(self.filename)

        self.flenlabel = QLabel(self.contentframe)
        self.flenlabel.setObjectName(u"flenlabel")
        self.flenlabel.setWordWrap(True)

        self.results.addWidget(self.flenlabel)


        self.verticalLayout.addLayout(self.results)

        self.options = QHBoxLayout()
        self.options.setObjectName(u"options")
        self.label_3 = QLabel(self.contentframe)
        self.label_3.setObjectName(u"label_3")

        self.options.addWidget(self.label_3)

        self.savdirec = QLineEdit(self.contentframe)
        self.savdirec.setObjectName(u"savdirec")
        self.savdirec.setStyleSheet(u"\n"
"/*background-color:#090B10;*/\n"
"QLineEdit {\n"
"	background-color: rgb(26, 26, 46);\n"
"	border:none;\n"
"	selection-background-color: rgb(22, 160, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 1px solid #0264AF ;\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 1px solid #0264AF ;\n"
"}\n"
"")

        self.options.addWidget(self.savdirec)

        self.browsebtn = QPushButton(self.contentframe)
        self.browsebtn.setObjectName(u"browsebtn")
        self.browsebtn.setMinimumSize(QSize(55, 0))
        self.browsebtn.setFocusPolicy(Qt.TabFocus)

        self.options.addWidget(self.browsebtn)


        self.verticalLayout.addLayout(self.options)

        self.dwnldlater = QCheckBox(self.contentframe)
        self.dwnldlater.setObjectName(u"dwnldlater")
        self.dwnldlater.setAutoFillBackground(False)
        self.dwnldlater.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.dwnldlater)

        self.actions = QHBoxLayout()
        self.actions.setObjectName(u"actions")
        self.warning = QLabel(self.contentframe)
        self.warning.setObjectName(u"warning")
        sizePolicy.setHeightForWidth(self.warning.sizePolicy().hasHeightForWidth())
        self.warning.setSizePolicy(sizePolicy)

        self.actions.addWidget(self.warning)

        self.addbtn = QPushButton(self.contentframe)
        self.addbtn.setObjectName(u"addbtn")
        self.addbtn.setMinimumSize(QSize(32, 0))

        self.actions.addWidget(self.addbtn)

        self.cancelbtn = QPushButton(self.contentframe)
        self.cancelbtn.setObjectName(u"cancelbtn")
        self.cancelbtn.setMinimumSize(QSize(47, 0))
        self.cancelbtn.setFocusPolicy(Qt.TabFocus)

        self.actions.addWidget(self.cancelbtn)


        self.verticalLayout.addLayout(self.actions)


        self.verticalLayout_4.addWidget(self.contentframe)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.retranslateUi(Addbox)

        QMetaObject.connectSlotsByName(Addbox)
    # setupUi

    def retranslateUi(self, Addbox):
        Addbox.setWindowTitle(QCoreApplication.translate("Addbox", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Addbox", u"Add Download", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("Addbox", u"Enter Url :", None))
        self.analysebtn.setText(QCoreApplication.translate("Addbox", u"Analyse", None))
        self.filename.setText("")
        self.flenlabel.setText("")
        self.label_3.setText(QCoreApplication.translate("Addbox", u"Save at : ", None))
        self.browsebtn.setText(QCoreApplication.translate("Addbox", u"Browse", None))
        self.dwnldlater.setText(QCoreApplication.translate("Addbox", u"Download Later", None))
        self.warning.setText("")
        self.addbtn.setText(QCoreApplication.translate("Addbox", u"Add", None))
        self.cancelbtn.setText(QCoreApplication.translate("Addbox", u"Cancel", None))
    # retranslateUi


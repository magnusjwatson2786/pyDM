# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlitem_gzsWgZO.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from ui.custom_pb import CustomPb

import res_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(471, 122)
        Form.setMaximumSize(QSize(16777215, 122))
        Form.setStyleSheet(u"QPushButton:hover{\n"
"    background-color: rgb(30,30,45);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgba(22,160,255,147);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#pushButton_3 .QPushButton:hover {\n"
"	background-color: rgba(150,33,40,147);\n"
"	 /*border-style: solid;\n"
"	 border-radius: 4px; */\n"
"}")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(60, 60))
        self.label.setMaximumSize(QSize(60, 60))

        self.horizontalLayout.addWidget(self.label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 30))
        self.label_2.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.progressBar = CustomPb(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(40, 40))
        self.pushButton.setMaximumSize(QSize(40, 40))
        self.pushButton.setFocusPolicy(Qt.NoFocus)
        self.pushButton.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/cil-media-pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(40, 40))
        self.pushButton_2.setMaximumSize(QSize(40, 40))
        self.pushButton_2.setFocusPolicy(Qt.NoFocus)
        self.pushButton_2.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(40, 40))
        self.pushButton_3.setMaximumSize(QSize(40, 40))
        self.pushButton_3.setFocusPolicy(Qt.NoFocus)
        self.pushButton_3.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgba(210,53,60,147);\n"
"	/*border-style: solid;\n"
"	border-radius: 4px; */\n"
"}"
"#pushButton_3 .QPushButton:pressed {\n"
"	background-color: rgb(150,33,40);\n"
"	 /*border-style: solid;\n"
"	 border-radius: 4px; */\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)

        self.verticalLayout_2.addWidget(self.pushButton_3)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
    # retranslateUi


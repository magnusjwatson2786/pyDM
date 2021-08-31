# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'q3yoZBYSE.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(844, 580)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget{\n"
"	color:#8590C8;\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"#frame_12{\n"
"    background-color: #0F111A;\n"
"	border: 1px solid rgb(44,49,58);\n"
"}\n"
"#frame_11{\n"
"	background-color: transparent;\n"
"	image: url(:/images/images/terminal.ico);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"	margin-top:0px;\n"
"}\n"
"#frame {\n"
"    background-color: #0E161F;\n"
"	border:0px;\n"
" 	margin:0px;\n"
"}\n"
"#pushButton_4 {\n"
"    background-color: transparent;\n"
"}\n"
"#frame_3 {\n"
"    background-color: #0F111A;\n"
"	padding-top:0px;\n"
"	padding-right:3px;\n"
"	padding-bottom: 5px; \n"
"}\n"
"\n"
"#frame_3 .QPushButton { \n"
"	background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px;\n"
"}\n"
"#frame_3 .QPushButton:hover {\n"
"	background-color:#1F2233; border-style: solid; border-radius: 4px; \n"
"}\n"
"#frame_3 .QPushButton:pressed {\n"
"	 background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; \n"
"}\n"
"#frame_2 {\n"
"    back"
                        "ground-color: transparent;\n"
"	border:0px;\n"
"}\n"
"#label{\n"
"	color:#82aaff;\n"
"	font: 11pt \"Segoe UI\";\n"
"    \n"
"    margin: 10px;\n"
"}\n"
"#frame_4 .QPushButton{\n"
"    font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249);\n"
"}\n"
"#frame_4 .QPushButton:hover{\n"
"    background-color: rgb(30,30,45);\n"
"}\n"
"#frame_4 .QPushButton:pressed{\n"
"    background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#frame_7{\n"
"	margin-right:0px;\n"
"	border:0px;\n"
"	padding-right:0px;\n"
"}\n"
"#frame_7 .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 15px solid transparent;\n"
"	border-right: 0px;\n"
"	margin-right:0px;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#frame_7 .QPushButton:hover {\n"
"	background-color:#1F2233;\n"
"	color:#DDDDDD;\n"
"}\n"
"#frame_7 .QPushButton:pressed {	\n"
"	background-color: #1E3250;\n"
"	color: rgb(255, 255, 255);\n"
"}"
                        "\n"
"#frame_6 {\n"
"	 background-color: transparent;\n"
"	 padding-top:10px;\n"
"} \n"
"#label_3{\n"
"	color:#82aaff;\n"
"	 font: 63 12pt \"Segoe UI Semibold\"; \n"
"}\n"
"#label_4{\n"
"	font: 8pt \"Segoe UI\";\n"
"	color: rgb(189, 147, 249);\n"
"}\n"
"#frame_5 {\n"
"	 background-color: #1D222B; \n"
"}\n"
"#frame_5 QLabel { \n"
"	font-size: 11px; color: \n"
"	rgb(113, 126, 149);\n"
"	padding-left: 10px; \n"
"	padding-right: 10px; \n"
"	padding-bottom: 2px; \n"
"}\n"
"#frame_15 QLabel { \n"
"	font-size: 11px; color: \n"
"	rgb(113, 126, 149);\n"
"	padding-left: 10px; \n"
"	padding-right: 10px; \n"
"	padding-bottom: 2px; \n"
"}\n"
"QPushButton#pushButton_6:hover {\n"
"	background-color:rgb(22,160,255); color:#DDDDDD;\n"
"}\n"
"QPushButton#pushButton_6:pressed {\n"
"	 background-color:rgb(22,160,255); color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#pushButton .QPushButton:hover {\n"
"	background-color:#962128; border-style: solid; border-radius: 4px; \n"
"}\n"
"#pushButton .QPushButton:pressed {\n"
"	 background-color:"
                        " rgb(23, 26, 30); border-style: solid; border-radius: 4px; \n"
"}\n"
"\n"
"#frame_14 .QListWidget::item, QListWidget::item:hover, QListWidget::item:selected {\n"
"	background-color:#0B0D16;\n"
"	border: 3px solid #0A0C15;}\n"
"/*	\n"
"#frame_14 .QScrollBar:vertical {\n"
"	border: none;\n"
"	background-color: rgb(242, 47, 130);\n"
"	width:7px;\n"
"	margin: 0px 0px 0px 0px;\n"
"}\n"
"#frame_14 .QScrollBar::handle:vertical {\n"
"	background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"	stop: 0 rgb(133,144,200), stop: 0.5 rgb(133,144,200), stop:1 rgb(133,144,200));\n"
"	min-height: 0px;\n"
"}\n"
"#frame_14 .QScrollBar::add-line:vertical {\n"
"	background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"	stop: 0 rgb(242, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 250));\n"
"	height: 0px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"#frame_14 .QScrollBar::sub-line:vertical {\n"
"	background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"	stop: 0  rgb(32, 47, 130), stop: 0.5 rg"
                        "b(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"	height: 0 px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"*/\n"
"#tabWidget::pane{\n"
"	background: transparent;\n"
"	border:0;\n"
"}\n"
"#frame_4 .QTabBar::tab {\n"
"    background: transparent;\n"
"	border: 1px solid rgb(44,49,58);\n"
"}\n"
"\n"
"#frame_14 .QScrollBar:vertical {\n"
"	border: none;\n"
"	background: rgb(52, 59, 72);\n"
"	width: 7px;\n"
"	margin: 11px 0 11px 0;\n"
"	/*border-radius: 0px;*/\n"
"}\n"
"#frame_14 .QScrollBar::handle:vertical {	\n"
"	background: rgb(22,160,255);\n"
"	min-height: 25px;\n"
"	/*border-radius: 4px*/\n"
"}\n"
"#frame_14 .QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background: rgb(55, 63, 77);	\n"
"	height: 10px;\n"
"	/*border-bottom-left-radius: 4px;\n"
"	border-bottom-right-radius: 4px;*/\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"#frame_14 .QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background: rgb(55, 63, 77);\n"
"	height: 10px;\n"
"	/"
                        "*border-top-left-radius: 4px;\n"
"	border-top-right-radius: 4px;*/\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"#frame_14 .QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"#frame_14 .QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"#frame_14 .QScrollBar:horizontal {\n"
"	border: none;\n"
"	background: rgb(52, 59, 72);\n"
"	height: 7px;\n"
"	margin:0 11px 0 11px;\n"
"	/*border-radius: 0px;*/\n"
"}\n"
"#frame_14 .QScrollBar::handle:horizontal {	\n"
"	background: rgb(22,160,255);\n"
"	min-width: 25px;\n"
"	/*border-radius: 4px*/\n"
"}\n"
"#frame_14 .QScrollBar::add-line:horizontal {\n"
"	border: none;\n"
"	background: rgb(55, 63, 77);	\n"
"	width: 10px;\n"
"	/*border-top-right-radius: 4px;\n"
"	border-bottom-right-radius: 4px;*/\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"#frame_14 .QScrollBar::sub-line:horizontal {\n"
"	border: none;\n"
"	background:"
                        " rgb(55, 63, 77);\n"
"	width: 10px;\n"
"	/*border-top-left-radius: 4px;\n"
"	border-bottom-left-radius: 4px;*/\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"#frame_14 .QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {\n"
"	background: none;\n"
"}\n"
"\n"
"#frame_14 .QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"	background: none;\n"
"}\n"
"#frame_15 .QPushButton:hover {\n"
"	background-color:#1F2233;\n"
"	color:#DDDDDD;\n"
"}\n"
"#frame_15 .QPushButton:pressed {	\n"
"	background-color: #1E3250;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#label_6, #label_9{\n"
"	font: 26pt \"Segoe UI\";\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.centralwidget)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_12)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_12)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(230, 0))
        self.frame.setMaximumSize(QSize(50, 16777215))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 50))
        self.frame_6.setMaximumSize(QSize(16777215, 50))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_11 = QFrame(self.frame_6)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(0, 0, 50, 45))
        self.frame_11.setMinimumSize(QSize(50, 45))
        self.frame_11.setMaximumSize(QSize(50, 45))
        self.frame_11.setStyleSheet(u"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.frame_11.setLineWidth(0)
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 10, 151, 21))
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 30, 111, 14))
        self.label_4.setMaximumSize(QSize(16777215, 16))

        self.verticalLayout_2.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 45))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.frame_8)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 45))
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setFocusPolicy(Qt.NoFocus)
        self.pushButton_5.setStyleSheet(u"background-image: url(:/icons/icons/cil-menu.png);")

        self.verticalLayout_4.addWidget(self.pushButton_5)


        self.verticalLayout_3.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFocusPolicy(Qt.NoFocus)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_6 = QPushButton(self.frame_9)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy1)
        self.pushButton_6.setMinimumSize(QSize(0, 45))
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setFocusPolicy(Qt.NoFocus)
        self.pushButton_6.setStyleSheet(u"background-image: url(:/icons/icons/cil-plus.png);")

        self.verticalLayout_5.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.frame_9)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy1.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy1)
        self.pushButton_7.setMinimumSize(QSize(0, 45))
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_7.setFocusPolicy(Qt.NoFocus)
        self.pushButton_7.setStyleSheet(u"background-image: url(:/icons/icons/cil-data-transfer-down.png);")

        self.verticalLayout_5.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.frame_9)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy1.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy1)
        self.pushButton_8.setMinimumSize(QSize(0, 45))
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_8.setFocusPolicy(Qt.NoFocus)
        self.pushButton_8.setStyleSheet(u"background-image: url(:/icons/icons/cil-history.png);")

        self.verticalLayout_5.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.frame_9)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy1.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy1)
        self.pushButton_9.setMinimumSize(QSize(0, 45))
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_9.setFocusPolicy(Qt.NoFocus)
        self.pushButton_9.setStyleSheet(u"background-image: url(:/icons/icons/cil-x.png);")

        self.verticalLayout_5.addWidget(self.pushButton_9)


        self.verticalLayout_3.addWidget(self.frame_9, 0, Qt.AlignTop)

        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setMinimumSize(QSize(0, 0))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_10)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton_10 = QPushButton(self.frame_10)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(0, 45))
        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_10.setFocusPolicy(Qt.NoFocus)
        self.pushButton_10.setStyleSheet(u"background-image: url(:/icons/icons/cil-settings.png);")

        self.verticalLayout_6.addWidget(self.pushButton_10)


        self.verticalLayout_3.addWidget(self.frame_10, 0, Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.frame_7)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_12)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"border:0px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 45))
        self.frame_3.setMaximumSize(QSize(16777215, 45))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(False)
        self.label.setFont(font1)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.label)

        self.pushButton_11 = QPushButton(self.frame_3)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(36, 36))
        self.pushButton_11.setMaximumSize(QSize(28, 28))
        self.pushButton_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon)
        self.pushButton_11.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.pushButton_11)

        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(36, 36))
        self.pushButton_3.setMaximumSize(QSize(28, 28))
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(36, 36))
        self.pushButton_2.setMaximumSize(QSize(28, 28))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(36, 36))
        self.pushButton.setMaximumSize(QSize(28, 28))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton:hover {\n"
"	background-color:#962128; border-style: solid; border-radius: 4px; \n"
"}\n"
"QPushButton:pressed {\n"
"	 background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; \n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_3.raise_()
        self.pushButton_2.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.pushButton_11.raise_()

        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_4)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: transparent;")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_6 = QLabel(self.page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(180, 180, 441, 101))
        font2 = QFont()
        font2.setPointSize(26)
        font2.setBold(False)
        font2.setItalic(False)
        self.label_6.setFont(font2)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_9 = QVBoxLayout(self.page_2)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(9, 5, 9, 5)
        self.tabWidget = QTabWidget(self.page_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setAutoFillBackground(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(170, 180, 431, 91))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setAutoFillBackground(False)
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_9.addWidget(self.tabWidget)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_8 = QVBoxLayout(self.page_3)
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.page_3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 0, 5, 0)
        self.label_7 = QLabel(self.frame_13)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)


        self.verticalLayout_8.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.page_3)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 0, 5, 0)
        self.listWidget = QListWidget(self.frame_14)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMouseTracking(False)
        self.listWidget.setFocusPolicy(Qt.NoFocus)
        self.listWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listWidget.setFlow(QListView.TopToBottom)
        self.listWidget.setSpacing(2)

        self.horizontalLayout_6.addWidget(self.listWidget)


        self.verticalLayout_8.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.page_3)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 0, 5, 0)
        self.label_8 = QLabel(self.frame_15)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)
        self.label_8.setStyleSheet(u"background-color:transparent;")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_8)

        self.pushButton_12 = QPushButton(self.frame_15)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setEnabled(True)
        self.pushButton_12.setMinimumSize(QSize(0, 0))
        self.pushButton_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_12.setFocusPolicy(Qt.NoFocus)
        self.pushButton_12.setStyleSheet(u"")
        self.pushButton_12.setIconSize(QSize(28, 28))

        self.horizontalLayout_7.addWidget(self.pushButton_12)


        self.verticalLayout_8.addWidget(self.frame_15)

        self.stackedWidget.addWidget(self.page_3)

        self.horizontalLayout_3.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 22))
        self.frame_5.setMaximumSize(QSize(16777215, 22))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.frame_rs = QFrame(self.frame_5)
        self.frame_rs.setObjectName(u"frame_rs")
        self.frame_rs.setMinimumSize(QSize(20, 10))
        self.frame_rs.setMaximumSize(QSize(20, 15))
        self.frame_rs.setStyleSheet(u"background-color: transparent;\n"
"image: url(:/icons/icons/cil-size-grip.png);\n"
"background-position: centered;\n"
"background-repeat: no-repeat;")
        self.frame_rs.setFrameShape(QFrame.StyledPanel)
        self.frame_rs.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_rs)


        self.verticalLayout.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout_7.addWidget(self.frame_12)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Download Manager", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Created using Python", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Tasks", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Window", None))
        self.pushButton_11.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_3.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Minimize</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_3.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Maximize</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_2.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Close</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"History Tab coming soon :)", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Settings Tab coming soon!", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"General", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"More", None))
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Downloads will appear here.", None))
        self.pushButton_12.setText("")
        self.label_2.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Version: 1.0.0", None))
    # retranslateUi


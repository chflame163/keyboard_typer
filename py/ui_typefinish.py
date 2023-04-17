# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_typefinish.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(460, 380)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(45)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(460, 380))
        Form.setMaximumSize(QSize(460, 380))
        self.frame_finish = QFrame(Form)
        self.frame_finish.setObjectName(u"frame_finish")
        self.frame_finish.setGeometry(QRect(20, 20, 420, 340))
        self.frame_finish.setMinimumSize(QSize(420, 340))
        self.frame_finish.setMaximumSize(QSize(420, 340))
        self.frame_finish.setStyleSheet(u"QFrame#frame_finish{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 18px;\n"
"background-color: qradialgradient(cx:0, cy:0, radius:2, fx:0.1, fy:0.1, stop:0 rgb(222, 222, 222),  stop:1 rgb(208, 208, 208));\n"
"border: 1px outset rgba(199, 199, 199, 0)\n"
"}")
        self.frame_finish.setFrameShape(QFrame.StyledPanel)
        self.frame_finish.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_finish)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 6, 0, 0)
        self.frame_1 = QFrame(self.frame_finish)
        self.frame_1.setObjectName(u"frame_1")
        self.frame_1.setFrameShape(QFrame.NoFrame)
        self.frame_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.horizontalSpacer = QSpacerItem(387, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_close = QPushButton(self.frame_1)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(14, 14))
        self.btn_close.setMaximumSize(QSize(12, 12))
        self.btn_close.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(240, 108, 96);\n"
"border:1px solid rgba(113, 17, 15,50);\n"
"border-radius:7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(139, 29, 31)\n"
"	\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(232, 59, 35);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btn_close)


        self.verticalLayout.addWidget(self.frame_1)

        self.frame_2 = QFrame(self.frame_finish)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 41))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_title = QLabel(self.frame_2)
        self.label_title.setObjectName(u"label_title")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy1)
        self.label_title.setMinimumSize(QSize(0, 39))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(10)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgba(0, 0, 0, 111);")
        self.label_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_title)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame_finish)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 74))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_info = QLabel(self.frame_3)
        self.label_info.setObjectName(u"label_info")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        self.label_info.setFont(font1)
        self.label_info.setAlignment(Qt.AlignCenter)
        self.label_info.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_info)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_finish)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(66)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(88, 0, 88, 0)
        self.btn_next = QPushButton(self.frame_4)
        self.btn_next.setObjectName(u"btn_next")
        self.btn_next.setMinimumSize(QSize(88, 38))
        self.btn_next.setMaximumSize(QSize(16777215, 38))
        palette = QPalette()
        brush = QBrush(QColor(177, 177, 177, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        brush2 = QBrush(QColor(31, 31, 31, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.btn_next.setPalette(palette)
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei"])
        font2.setPointSize(10)
        self.btn_next.setFont(font2)
        self.btn_next.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(144, 144, 144)\n"
"	\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(111, 111, 111);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.btn_next)

        self.btn_quit = QPushButton(self.frame_4)
        self.btn_quit.setObjectName(u"btn_quit")
        self.btn_quit.setMinimumSize(QSize(88, 38))
        self.btn_quit.setMaximumSize(QSize(16777215, 38))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Button, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.btn_quit.setPalette(palette1)
        self.btn_quit.setFont(font2)
        self.btn_quit.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(144, 144, 144)\n"
"	\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(111, 111, 111);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.btn_quit)


        self.verticalLayout.addWidget(self.frame_4)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(2, 12)
        self.verticalLayout.setStretch(3, 5)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_close.setText("")
        self.label_title.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_info.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.btn_next.setText(QCoreApplication.translate("Form", u"Next", None))
        self.btn_quit.setText(QCoreApplication.translate("Form", u"Quit", None))
    # retranslateUi


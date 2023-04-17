# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_typer_win.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import ui_resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(888, 612)
        Form.setMinimumSize(QSize(888, 612))
        Form.setMaximumSize(QSize(888, 612))
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(16, 16, 16, 16)
        self.frame_typer = QFrame(Form)
        self.frame_typer.setObjectName(u"frame_typer")
        self.frame_typer.setMaximumSize(QSize(16777215, 260))
        self.frame_typer.setStyleSheet(u"QFrame#frame_typer{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 18px;\n"
"background-color: qradialgradient(cx:0, cy:0, radius:2, fx:0.1, fy:0.1, stop:0 rgb(222, 222, 222),  stop:1 rgb(208, 208, 208));\n"
"border: 1px outset rgba(199, 199, 199, 0)\n"
"}")
        self.frame_typer.setFrameShape(QFrame.StyledPanel)
        self.frame_typer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_typer)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(16, 0, 6, 16)
        self.frame_1 = QFrame(self.frame_typer)
        self.frame_1.setObjectName(u"frame_1")
        self.frame_1.setMinimumSize(QSize(0, 36))
        self.frame_1.setFrameShape(QFrame.NoFrame)
        self.frame_1.setFrameShadow(QFrame.Raised)
        self.frame_1.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_left = QFrame(self.frame_1)
        self.frame_top_left.setObjectName(u"frame_top_left")
        self.frame_top_left.setFrameShape(QFrame.NoFrame)
        self.frame_top_left.setFrameShadow(QFrame.Raised)
        self.frame_top_left.setLineWidth(0)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_top_left)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(10, 11, 0, 6)
        self.widget = QWidget(self.frame_top_left)
        self.widget.setObjectName(u"widget")
        self.widget.setContextMenuPolicy(Qt.NoContextMenu)
        self.widget.setStyleSheet(u"QWidget{\n"
"	image:url(:/image/res/image/essay.png)\n"
"}")

        self.horizontalLayout_16.addWidget(self.widget)


        self.horizontalLayout_3.addWidget(self.frame_top_left)

        self.frame_status = QFrame(self.frame_1)
        self.frame_status.setObjectName(u"frame_status")
        self.frame_status.setFrameShape(QFrame.NoFrame)
        self.frame_status.setFrameShadow(QFrame.Raised)
        self.frame_status.setLineWidth(0)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_status)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 4, 0, 0)
        self.frame_3 = QFrame(self.frame_status)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setLineWidth(0)
        self.verticalLayout_9 = QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_essay_title = QLabel(self.frame_3)
        self.label_essay_title.setObjectName(u"label_essay_title")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_essay_title.sizePolicy().hasHeightForWidth())
        self.label_essay_title.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setBold(False)
        self.label_essay_title.setFont(font)
        self.label_essay_title.setContextMenuPolicy(Qt.NoContextMenu)
        self.label_essay_title.setStyleSheet(u"color: rgba(0, 0, 0, 66);")

        self.verticalLayout_9.addWidget(self.label_essay_title)


        self.horizontalLayout_15.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_status)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setLineWidth(0)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(0)
        self.horizontalLayout_21 = QHBoxLayout(self.frame)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setContextMenuPolicy(Qt.NoContextMenu)
        self.widget_2.setStyleSheet(u"QWidget{\n"
"	image:url(:/image/res/image/timer.png)\n"
"}")

        self.horizontalLayout_21.addWidget(self.widget_2)

        self.label_time = QLabel(self.frame)
        self.label_time.setObjectName(u"label_time")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(10)
        self.label_time.setFont(font1)
        self.label_time.setContextMenuPolicy(Qt.NoContextMenu)
        self.label_time.setStyleSheet(u"color: rgba(0, 0, 0, 66);")

        self.horizontalLayout_21.addWidget(self.label_time)

        self.horizontalLayout_21.setStretch(0, 1)
        self.horizontalLayout_21.setStretch(1, 3)

        self.horizontalLayout_17.addWidget(self.frame)

        self.label_speed = QLabel(self.frame_4)
        self.label_speed.setObjectName(u"label_speed")
        self.label_speed.setFont(font1)
        self.label_speed.setContextMenuPolicy(Qt.NoContextMenu)
        self.label_speed.setStyleSheet(u"color: rgba(0, 0, 0, 66);")

        self.horizontalLayout_17.addWidget(self.label_speed)

        self.label_accuracy = QLabel(self.frame_4)
        self.label_accuracy.setObjectName(u"label_accuracy")
        self.label_accuracy.setFont(font1)
        self.label_accuracy.setContextMenuPolicy(Qt.NoContextMenu)
        self.label_accuracy.setStyleSheet(u"color: rgba(0, 0, 0, 66);")

        self.horizontalLayout_17.addWidget(self.label_accuracy)

        self.horizontalLayout_17.setStretch(0, 1)
        self.horizontalLayout_17.setStretch(1, 2)
        self.horizontalLayout_17.setStretch(2, 1)

        self.horizontalLayout_15.addWidget(self.frame_4)

        self.horizontalLayout_15.setStretch(0, 1)
        self.horizontalLayout_15.setStretch(1, 1)

        self.horizontalLayout_3.addWidget(self.frame_status)

        self.frame_top_right = QFrame(self.frame_1)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.frame_top_right.setLineWidth(0)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_top_right)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(18, 4, 0, 14)
        self.btn_close = QPushButton(self.frame_top_right)
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

        self.horizontalLayout_14.addWidget(self.btn_close)


        self.horizontalLayout_3.addWidget(self.frame_top_right)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 20)
        self.horizontalLayout_3.setStretch(2, 1)

        self.verticalLayout_8.addWidget(self.frame_1)

        self.frame_2 = QFrame(self.frame_typer)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 10, 0)
        self.frame_labels = QFrame(self.frame_2)
        self.frame_labels.setObjectName(u"frame_labels")
        self.frame_labels.setFrameShape(QFrame.NoFrame)
        self.frame_labels.setFrameShadow(QFrame.Raised)
        self.frame_labels.setLineWidth(0)
        self.verticalLayout_6 = QVBoxLayout(self.frame_labels)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(12, -1, 12, -1)
        self.label_line1 = QLabel(self.frame_labels)
        self.label_line1.setObjectName(u"label_line1")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(20)
        self.label_line1.setFont(font2)
        self.label_line1.setMouseTracking(True)
        self.label_line1.setContextMenuPolicy(Qt.NoContextMenu)
        self.label_line1.setStyleSheet(u"color: rgba(0, 0, 0, 66);")
        self.label_line1.setTextFormat(Qt.RichText)

        self.verticalLayout_6.addWidget(self.label_line1)

        self.label_line2 = QLabel(self.frame_labels)
        self.label_line2.setObjectName(u"label_line2")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(24)
        self.label_line2.setFont(font3)
        self.label_line2.setMouseTracking(True)
        self.label_line2.setContextMenuPolicy(Qt.NoContextMenu)
        self.label_line2.setStyleSheet(u"color: rgb(1, 1, 1);")
        self.label_line2.setTextFormat(Qt.RichText)

        self.verticalLayout_6.addWidget(self.label_line2)

        self.label_line3 = QLabel(self.frame_labels)
        self.label_line3.setObjectName(u"label_line3")
        self.label_line3.setFont(font2)
        self.label_line3.setMouseTracking(True)
        self.label_line3.setContextMenuPolicy(Qt.NoContextMenu)
        self.label_line3.setStyleSheet(u"color: rgb(155, 155, 155);")
        self.label_line3.setTextFormat(Qt.RichText)

        self.verticalLayout_6.addWidget(self.label_line3)


        self.verticalLayout_7.addWidget(self.frame_labels)

        self.frame_input = QFrame(self.frame_2)
        self.frame_input.setObjectName(u"frame_input")
        self.frame_input.setMinimumSize(QSize(0, 42))
        self.frame_input.setMaximumSize(QSize(16777215, 42))
        self.frame_input.setStyleSheet(u"QFrame#frame_input{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"background-color: rgb(244, 244, 244);\n"
"border: 1px outset rgba(199, 199, 199, 0)\n"
"}")
        self.frame_input.setFrameShape(QFrame.NoFrame)
        self.frame_input.setFrameShadow(QFrame.Raised)
        self.frame_input.setLineWidth(0)
        self.verticalLayout_5 = QVBoxLayout(self.frame_input)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, 4)
        self.lineEdit_input = QLineEdit(self.frame_input)
        self.lineEdit_input.setObjectName(u"lineEdit_input")
        self.lineEdit_input.setEnabled(True)
        font4 = QFont()
        font4.setFamilies([u"Alibaba Sans"])
        font4.setPointSize(14)
        self.lineEdit_input.setFont(font4)
        self.lineEdit_input.setMouseTracking(False)
        self.lineEdit_input.setFocusPolicy(Qt.StrongFocus)
        self.lineEdit_input.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit_input.setAcceptDrops(False)
        self.lineEdit_input.setStyleSheet(u"border:none;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"selection-color: rgba(193, 193, 193,150);\n"
"border-bottom:1px solid rgba(0, 0, 0,40);\n"
"padding:1px")
        self.lineEdit_input.setMaxLength(79)
        self.lineEdit_input.setFrame(True)

        self.verticalLayout_5.addWidget(self.lineEdit_input)


        self.verticalLayout_7.addWidget(self.frame_input)

        self.verticalLayout_7.setStretch(1, 1)

        self.verticalLayout_8.addWidget(self.frame_2)

        self.verticalLayout_8.setStretch(1, 4)

        self.verticalLayout_3.addWidget(self.frame_typer)

        self.frame_keyboard = QFrame(Form)
        self.frame_keyboard.setObjectName(u"frame_keyboard")
        self.frame_keyboard.setMinimumSize(QSize(856, 316))
        self.frame_keyboard.setMaximumSize(QSize(856, 316))
        self.frame_keyboard.setContextMenuPolicy(Qt.CustomContextMenu)
        self.frame_keyboard.setStyleSheet(u"QFrame#frame_keyboard{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 18px;\n"
"background-color: qradialgradient(cx:0, cy:0, radius:2, fx:0.1, fy:0.1, stop:0 rgb(222, 222, 222),  stop:1 rgb(208, 208, 208));\n"
"border: 1px outset rgba(199, 199, 199, 0)\n"
"}")
        self.frame_keyboard.setFrameShape(QFrame.StyledPanel)
        self.frame_keyboard.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_keyboard)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(12, 0, 4, 4)
        self.Main_Area = QFrame(self.frame_keyboard)
        self.Main_Area.setObjectName(u"Main_Area")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Main_Area.sizePolicy().hasHeightForWidth())
        self.Main_Area.setSizePolicy(sizePolicy1)
        self.Main_Area.setMinimumSize(QSize(666, 300))
        self.Main_Area.setMaximumSize(QSize(666, 300))
        self.Main_Area.setFrameShape(QFrame.NoFrame)
        self.Main_Area.setFrameShadow(QFrame.Plain)
        self.Main_Area.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.Main_Area)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 8, 0, 8)
        self.M_line_1 = QFrame(self.Main_Area)
        self.M_line_1.setObjectName(u"M_line_1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.M_line_1.sizePolicy().hasHeightForWidth())
        self.M_line_1.setSizePolicy(sizePolicy2)
        self.M_line_1.setMinimumSize(QSize(666, 0))
        self.M_line_1.setMaximumSize(QSize(666, 16777215))
        self.M_line_1.setFrameShape(QFrame.NoFrame)
        self.M_line_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.M_line_1)
        self.horizontalLayout_10.setSpacing(14)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 2, 0)
        self.frame_esc = QFrame(self.M_line_1)
        self.frame_esc.setObjectName(u"frame_esc")
        self.frame_esc.setMinimumSize(QSize(61, 0))
        self.frame_esc.setFrameShape(QFrame.NoFrame)
        self.frame_esc.setFrameShadow(QFrame.Raised)
        self.frame_esc.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.frame_esc)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.key_esc = QPushButton(self.frame_esc)
        self.key_esc.setObjectName(u"key_esc")
        sizePolicy1.setHeightForWidth(self.key_esc.sizePolicy().hasHeightForWidth())
        self.key_esc.setSizePolicy(sizePolicy1)
        self.key_esc.setMinimumSize(QSize(42, 42))
        self.key_esc.setMaximumSize(QSize(42, 42))
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
        self.key_esc.setPalette(palette)
        font5 = QFont()
        font5.setFamilies([u"Microsoft YaHei"])
        font5.setPointSize(8)
        self.key_esc.setFont(font5)
        self.key_esc.setFocusPolicy(Qt.NoFocus)
        self.key_esc.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_esc.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.verticalLayout_4.addWidget(self.key_esc)


        self.horizontalLayout_10.addWidget(self.frame_esc)

        self.frame_f1_f4 = QFrame(self.M_line_1)
        self.frame_f1_f4.setObjectName(u"frame_f1_f4")
        self.frame_f1_f4.setFrameShape(QFrame.NoFrame)
        self.frame_f1_f4.setFrameShadow(QFrame.Raised)
        self.frame_f1_f4.setLineWidth(0)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_f1_f4)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.key_F1 = QPushButton(self.frame_f1_f4)
        self.key_F1.setObjectName(u"key_F1")
        sizePolicy1.setHeightForWidth(self.key_F1.sizePolicy().hasHeightForWidth())
        self.key_F1.setSizePolicy(sizePolicy1)
        self.key_F1.setMinimumSize(QSize(42, 42))
        self.key_F1.setMaximumSize(QSize(42, 42))
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
        self.key_F1.setPalette(palette1)
        self.key_F1.setFont(font5)
        self.key_F1.setFocusPolicy(Qt.NoFocus)
        self.key_F1.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_F1.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_18.addWidget(self.key_F1)

        self.key_F2 = QPushButton(self.frame_f1_f4)
        self.key_F2.setObjectName(u"key_F2")
        sizePolicy1.setHeightForWidth(self.key_F2.sizePolicy().hasHeightForWidth())
        self.key_F2.setSizePolicy(sizePolicy1)
        self.key_F2.setMinimumSize(QSize(42, 42))
        self.key_F2.setMaximumSize(QSize(42, 42))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Button, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_F2.setPalette(palette2)
        self.key_F2.setFont(font5)
        self.key_F2.setFocusPolicy(Qt.NoFocus)
        self.key_F2.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_F2.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_18.addWidget(self.key_F2)

        self.key_F3 = QPushButton(self.frame_f1_f4)
        self.key_F3.setObjectName(u"key_F3")
        sizePolicy1.setHeightForWidth(self.key_F3.sizePolicy().hasHeightForWidth())
        self.key_F3.setSizePolicy(sizePolicy1)
        self.key_F3.setMinimumSize(QSize(42, 42))
        self.key_F3.setMaximumSize(QSize(42, 42))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Button, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_F3.setPalette(palette3)
        self.key_F3.setFont(font5)
        self.key_F3.setFocusPolicy(Qt.NoFocus)
        self.key_F3.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_F3.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_18.addWidget(self.key_F3)

        self.key_F4 = QPushButton(self.frame_f1_f4)
        self.key_F4.setObjectName(u"key_F4")
        sizePolicy1.setHeightForWidth(self.key_F4.sizePolicy().hasHeightForWidth())
        self.key_F4.setSizePolicy(sizePolicy1)
        self.key_F4.setMinimumSize(QSize(42, 42))
        self.key_F4.setMaximumSize(QSize(42, 42))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.Button, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_F4.setPalette(palette4)
        self.key_F4.setFont(font5)
        self.key_F4.setFocusPolicy(Qt.NoFocus)
        self.key_F4.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_F4.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_18.addWidget(self.key_F4)


        self.horizontalLayout_10.addWidget(self.frame_f1_f4)

        self.frame_f5_f8 = QFrame(self.M_line_1)
        self.frame_f5_f8.setObjectName(u"frame_f5_f8")
        self.frame_f5_f8.setFrameShape(QFrame.NoFrame)
        self.frame_f5_f8.setFrameShadow(QFrame.Raised)
        self.frame_f5_f8.setLineWidth(0)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_f5_f8)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.key_F5 = QPushButton(self.frame_f5_f8)
        self.key_F5.setObjectName(u"key_F5")
        sizePolicy1.setHeightForWidth(self.key_F5.sizePolicy().hasHeightForWidth())
        self.key_F5.setSizePolicy(sizePolicy1)
        self.key_F5.setMinimumSize(QSize(42, 42))
        self.key_F5.setMaximumSize(QSize(42, 42))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.Button, brush)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_F5.setPalette(palette5)
        self.key_F5.setFont(font5)
        self.key_F5.setFocusPolicy(Qt.NoFocus)
        self.key_F5.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_F5.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_19.addWidget(self.key_F5)

        self.key_F6 = QPushButton(self.frame_f5_f8)
        self.key_F6.setObjectName(u"key_F6")
        sizePolicy1.setHeightForWidth(self.key_F6.sizePolicy().hasHeightForWidth())
        self.key_F6.setSizePolicy(sizePolicy1)
        self.key_F6.setMinimumSize(QSize(42, 42))
        self.key_F6.setMaximumSize(QSize(42, 42))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.Button, brush)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_F6.setPalette(palette6)
        self.key_F6.setFont(font5)
        self.key_F6.setFocusPolicy(Qt.NoFocus)
        self.key_F6.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_F6.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_19.addWidget(self.key_F6)

        self.key_F7 = QPushButton(self.frame_f5_f8)
        self.key_F7.setObjectName(u"key_F7")
        sizePolicy1.setHeightForWidth(self.key_F7.sizePolicy().hasHeightForWidth())
        self.key_F7.setSizePolicy(sizePolicy1)
        self.key_F7.setMinimumSize(QSize(42, 42))
        self.key_F7.setMaximumSize(QSize(42, 42))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.Button, brush)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_F7.setPalette(palette7)
        self.key_F7.setFont(font5)
        self.key_F7.setFocusPolicy(Qt.NoFocus)
        self.key_F7.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_F7.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_19.addWidget(self.key_F7)

        self.key_F8 = QPushButton(self.frame_f5_f8)
        self.key_F8.setObjectName(u"key_F8")
        sizePolicy1.setHeightForWidth(self.key_F8.sizePolicy().hasHeightForWidth())
        self.key_F8.setSizePolicy(sizePolicy1)
        self.key_F8.setMinimumSize(QSize(42, 42))
        self.key_F8.setMaximumSize(QSize(42, 42))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.Button, brush)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_F8.setPalette(palette8)
        self.key_F8.setFont(font5)
        self.key_F8.setFocusPolicy(Qt.NoFocus)
        self.key_F8.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_F8.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_19.addWidget(self.key_F8)


        self.horizontalLayout_10.addWidget(self.frame_f5_f8)

        self.frame_f9_f12 = QFrame(self.M_line_1)
        self.frame_f9_f12.setObjectName(u"frame_f9_f12")
        self.frame_f9_f12.setFrameShape(QFrame.NoFrame)
        self.frame_f9_f12.setFrameShadow(QFrame.Raised)
        self.frame_f9_f12.setLineWidth(0)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_f9_f12)
        self.horizontalLayout_20.setSpacing(4)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.key_F9 = QPushButton(self.frame_f9_f12)
        self.key_F9.setObjectName(u"key_F9")
        sizePolicy1.setHeightForWidth(self.key_F9.sizePolicy().hasHeightForWidth())
        self.key_F9.setSizePolicy(sizePolicy1)
        self.key_F9.setMinimumSize(QSize(42, 42))
        self.key_F9.setMaximumSize(QSize(42, 42))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.Button, brush)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_F9.setPalette(palette9)
        self.key_F9.setFont(font5)
        self.key_F9.setFocusPolicy(Qt.NoFocus)
        self.key_F9.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_F9.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_20.addWidget(self.key_F9)

        self.key_F10 = QPushButton(self.frame_f9_f12)
        self.key_F10.setObjectName(u"key_F10")
        sizePolicy1.setHeightForWidth(self.key_F10.sizePolicy().hasHeightForWidth())
        self.key_F10.setSizePolicy(sizePolicy1)
        self.key_F10.setMinimumSize(QSize(42, 42))
        self.key_F10.setMaximumSize(QSize(42, 42))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.Button, brush)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_F10.setPalette(palette10)
        self.key_F10.setFont(font5)
        self.key_F10.setFocusPolicy(Qt.NoFocus)
        self.key_F10.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_F10.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_20.addWidget(self.key_F10)

        self.key_F11 = QPushButton(self.frame_f9_f12)
        self.key_F11.setObjectName(u"key_F11")
        sizePolicy1.setHeightForWidth(self.key_F11.sizePolicy().hasHeightForWidth())
        self.key_F11.setSizePolicy(sizePolicy1)
        self.key_F11.setMinimumSize(QSize(42, 42))
        self.key_F11.setMaximumSize(QSize(42, 42))
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.Button, brush)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_F11.setPalette(palette11)
        self.key_F11.setFont(font5)
        self.key_F11.setFocusPolicy(Qt.NoFocus)
        self.key_F11.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_F11.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_20.addWidget(self.key_F11)

        self.key_F12 = QPushButton(self.frame_f9_f12)
        self.key_F12.setObjectName(u"key_F12")
        sizePolicy1.setHeightForWidth(self.key_F12.sizePolicy().hasHeightForWidth())
        self.key_F12.setSizePolicy(sizePolicy1)
        self.key_F12.setMinimumSize(QSize(42, 42))
        self.key_F12.setMaximumSize(QSize(42, 42))
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.Button, brush)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_F12.setPalette(palette12)
        self.key_F12.setFont(font5)
        self.key_F12.setFocusPolicy(Qt.NoFocus)
        self.key_F12.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_F12.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_20.addWidget(self.key_F12)


        self.horizontalLayout_10.addWidget(self.frame_f9_f12)

        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 4)
        self.horizontalLayout_10.setStretch(2, 4)
        self.horizontalLayout_10.setStretch(3, 4)

        self.verticalLayout.addWidget(self.M_line_1)

        self.M_line_2 = QFrame(self.Main_Area)
        self.M_line_2.setObjectName(u"M_line_2")
        sizePolicy2.setHeightForWidth(self.M_line_2.sizePolicy().hasHeightForWidth())
        self.M_line_2.setSizePolicy(sizePolicy2)
        self.M_line_2.setMinimumSize(QSize(666, 0))
        self.M_line_2.setMaximumSize(QSize(666, 16777215))
        self.M_line_2.setFrameShape(QFrame.NoFrame)
        self.M_line_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.M_line_2)
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(1, 1, 6, 1)
        self.key_backquote = QPushButton(self.M_line_2)
        self.key_backquote.setObjectName(u"key_backquote")
        sizePolicy1.setHeightForWidth(self.key_backquote.sizePolicy().hasHeightForWidth())
        self.key_backquote.setSizePolicy(sizePolicy1)
        self.key_backquote.setMinimumSize(QSize(42, 42))
        self.key_backquote.setMaximumSize(QSize(42, 42))
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.Button, brush)
        palette13.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_backquote.setPalette(palette13)
        self.key_backquote.setFont(font5)
        self.key_backquote.setFocusPolicy(Qt.NoFocus)
        self.key_backquote.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_backquote.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_4.addWidget(self.key_backquote)

        self.key_1 = QPushButton(self.M_line_2)
        self.key_1.setObjectName(u"key_1")
        sizePolicy1.setHeightForWidth(self.key_1.sizePolicy().hasHeightForWidth())
        self.key_1.setSizePolicy(sizePolicy1)
        self.key_1.setMinimumSize(QSize(42, 42))
        self.key_1.setMaximumSize(QSize(42, 42))
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.Button, brush)
        palette14.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_1.setPalette(palette14)
        self.key_1.setFont(font5)
        self.key_1.setFocusPolicy(Qt.NoFocus)
        self.key_1.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_1.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_4.addWidget(self.key_1)

        self.key_2 = QPushButton(self.M_line_2)
        self.key_2.setObjectName(u"key_2")
        sizePolicy1.setHeightForWidth(self.key_2.sizePolicy().hasHeightForWidth())
        self.key_2.setSizePolicy(sizePolicy1)
        self.key_2.setMinimumSize(QSize(42, 42))
        self.key_2.setMaximumSize(QSize(42, 42))
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.Button, brush)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_2.setPalette(palette15)
        self.key_2.setFont(font5)
        self.key_2.setFocusPolicy(Qt.NoFocus)
        self.key_2.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_2.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_4.addWidget(self.key_2)

        self.key_3 = QPushButton(self.M_line_2)
        self.key_3.setObjectName(u"key_3")
        sizePolicy1.setHeightForWidth(self.key_3.sizePolicy().hasHeightForWidth())
        self.key_3.setSizePolicy(sizePolicy1)
        self.key_3.setMinimumSize(QSize(42, 42))
        self.key_3.setMaximumSize(QSize(42, 42))
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.Button, brush)
        palette16.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_3.setPalette(palette16)
        self.key_3.setFont(font5)
        self.key_3.setFocusPolicy(Qt.NoFocus)
        self.key_3.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_3.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_4.addWidget(self.key_3)

        self.key_4 = QPushButton(self.M_line_2)
        self.key_4.setObjectName(u"key_4")
        sizePolicy1.setHeightForWidth(self.key_4.sizePolicy().hasHeightForWidth())
        self.key_4.setSizePolicy(sizePolicy1)
        self.key_4.setMinimumSize(QSize(42, 42))
        self.key_4.setMaximumSize(QSize(42, 42))
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.Button, brush)
        palette17.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_4.setPalette(palette17)
        self.key_4.setFont(font5)
        self.key_4.setFocusPolicy(Qt.NoFocus)
        self.key_4.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_4.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_4.addWidget(self.key_4)

        self.key_5 = QPushButton(self.M_line_2)
        self.key_5.setObjectName(u"key_5")
        sizePolicy1.setHeightForWidth(self.key_5.sizePolicy().hasHeightForWidth())
        self.key_5.setSizePolicy(sizePolicy1)
        self.key_5.setMinimumSize(QSize(42, 42))
        self.key_5.setMaximumSize(QSize(42, 42))
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.Button, brush)
        palette18.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_5.setPalette(palette18)
        self.key_5.setFont(font5)
        self.key_5.setFocusPolicy(Qt.NoFocus)
        self.key_5.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_5.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_4.addWidget(self.key_5)

        self.key_6 = QPushButton(self.M_line_2)
        self.key_6.setObjectName(u"key_6")
        sizePolicy1.setHeightForWidth(self.key_6.sizePolicy().hasHeightForWidth())
        self.key_6.setSizePolicy(sizePolicy1)
        self.key_6.setMinimumSize(QSize(42, 42))
        self.key_6.setMaximumSize(QSize(42, 42))
        palette19 = QPalette()
        palette19.setBrush(QPalette.Active, QPalette.Button, brush)
        palette19.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette19.setBrush(QPalette.Active, QPalette.Base, brush)
        palette19.setBrush(QPalette.Active, QPalette.Window, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette19.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette19.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_6.setPalette(palette19)
        self.key_6.setFont(font5)
        self.key_6.setFocusPolicy(Qt.NoFocus)
        self.key_6.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_6.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_4.addWidget(self.key_6)

        self.key_7 = QPushButton(self.M_line_2)
        self.key_7.setObjectName(u"key_7")
        sizePolicy1.setHeightForWidth(self.key_7.sizePolicy().hasHeightForWidth())
        self.key_7.setSizePolicy(sizePolicy1)
        self.key_7.setMinimumSize(QSize(42, 42))
        self.key_7.setMaximumSize(QSize(42, 42))
        palette20 = QPalette()
        palette20.setBrush(QPalette.Active, QPalette.Button, brush)
        palette20.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette20.setBrush(QPalette.Active, QPalette.Base, brush)
        palette20.setBrush(QPalette.Active, QPalette.Window, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette20.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette20.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_7.setPalette(palette20)
        self.key_7.setFont(font5)
        self.key_7.setFocusPolicy(Qt.NoFocus)
        self.key_7.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_7.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_4.addWidget(self.key_7)

        self.key_8 = QPushButton(self.M_line_2)
        self.key_8.setObjectName(u"key_8")
        sizePolicy1.setHeightForWidth(self.key_8.sizePolicy().hasHeightForWidth())
        self.key_8.setSizePolicy(sizePolicy1)
        self.key_8.setMinimumSize(QSize(42, 42))
        self.key_8.setMaximumSize(QSize(42, 42))
        palette21 = QPalette()
        palette21.setBrush(QPalette.Active, QPalette.Button, brush)
        palette21.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette21.setBrush(QPalette.Active, QPalette.Base, brush)
        palette21.setBrush(QPalette.Active, QPalette.Window, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette21.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette21.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_8.setPalette(palette21)
        self.key_8.setFont(font5)
        self.key_8.setFocusPolicy(Qt.NoFocus)
        self.key_8.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_8.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_4.addWidget(self.key_8)

        self.key_9 = QPushButton(self.M_line_2)
        self.key_9.setObjectName(u"key_9")
        sizePolicy1.setHeightForWidth(self.key_9.sizePolicy().hasHeightForWidth())
        self.key_9.setSizePolicy(sizePolicy1)
        self.key_9.setMinimumSize(QSize(42, 42))
        self.key_9.setMaximumSize(QSize(42, 42))
        palette22 = QPalette()
        palette22.setBrush(QPalette.Active, QPalette.Button, brush)
        palette22.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette22.setBrush(QPalette.Active, QPalette.Base, brush)
        palette22.setBrush(QPalette.Active, QPalette.Window, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette22.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette22.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_9.setPalette(palette22)
        self.key_9.setFont(font5)
        self.key_9.setFocusPolicy(Qt.NoFocus)
        self.key_9.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_9.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_4.addWidget(self.key_9)

        self.key_0 = QPushButton(self.M_line_2)
        self.key_0.setObjectName(u"key_0")
        sizePolicy1.setHeightForWidth(self.key_0.sizePolicy().hasHeightForWidth())
        self.key_0.setSizePolicy(sizePolicy1)
        self.key_0.setMinimumSize(QSize(42, 42))
        self.key_0.setMaximumSize(QSize(42, 42))
        palette23 = QPalette()
        palette23.setBrush(QPalette.Active, QPalette.Button, brush)
        palette23.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette23.setBrush(QPalette.Active, QPalette.Base, brush)
        palette23.setBrush(QPalette.Active, QPalette.Window, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette23.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette23.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_0.setPalette(palette23)
        self.key_0.setFont(font5)
        self.key_0.setFocusPolicy(Qt.NoFocus)
        self.key_0.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_0.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_4.addWidget(self.key_0)

        self.key_minus = QPushButton(self.M_line_2)
        self.key_minus.setObjectName(u"key_minus")
        sizePolicy1.setHeightForWidth(self.key_minus.sizePolicy().hasHeightForWidth())
        self.key_minus.setSizePolicy(sizePolicy1)
        self.key_minus.setMinimumSize(QSize(42, 42))
        self.key_minus.setMaximumSize(QSize(42, 42))
        palette24 = QPalette()
        palette24.setBrush(QPalette.Active, QPalette.Button, brush)
        palette24.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette24.setBrush(QPalette.Active, QPalette.Base, brush)
        palette24.setBrush(QPalette.Active, QPalette.Window, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette24.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette24.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_minus.setPalette(palette24)
        self.key_minus.setFont(font5)
        self.key_minus.setFocusPolicy(Qt.NoFocus)
        self.key_minus.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_minus.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_4.addWidget(self.key_minus)

        self.key_equal = QPushButton(self.M_line_2)
        self.key_equal.setObjectName(u"key_equal")
        sizePolicy1.setHeightForWidth(self.key_equal.sizePolicy().hasHeightForWidth())
        self.key_equal.setSizePolicy(sizePolicy1)
        self.key_equal.setMinimumSize(QSize(42, 42))
        self.key_equal.setMaximumSize(QSize(42, 42))
        palette25 = QPalette()
        palette25.setBrush(QPalette.Active, QPalette.Button, brush)
        palette25.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette25.setBrush(QPalette.Active, QPalette.Base, brush)
        palette25.setBrush(QPalette.Active, QPalette.Window, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette25.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette25.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_equal.setPalette(palette25)
        self.key_equal.setFont(font5)
        self.key_equal.setFocusPolicy(Qt.NoFocus)
        self.key_equal.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_equal.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_4.addWidget(self.key_equal)

        self.key_backspace = QPushButton(self.M_line_2)
        self.key_backspace.setObjectName(u"key_backspace")
        sizePolicy1.setHeightForWidth(self.key_backspace.sizePolicy().hasHeightForWidth())
        self.key_backspace.setSizePolicy(sizePolicy1)
        self.key_backspace.setMinimumSize(QSize(90, 42))
        self.key_backspace.setMaximumSize(QSize(90, 42))
        palette26 = QPalette()
        palette26.setBrush(QPalette.Active, QPalette.Button, brush)
        palette26.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette26.setBrush(QPalette.Active, QPalette.Base, brush)
        palette26.setBrush(QPalette.Active, QPalette.Window, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette26.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette26.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_backspace.setPalette(palette26)
        self.key_backspace.setFont(font5)
        self.key_backspace.setFocusPolicy(Qt.NoFocus)
        self.key_backspace.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_backspace.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_4.addWidget(self.key_backspace)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 1)
        self.horizontalLayout_4.setStretch(3, 1)
        self.horizontalLayout_4.setStretch(4, 1)
        self.horizontalLayout_4.setStretch(5, 1)
        self.horizontalLayout_4.setStretch(6, 1)
        self.horizontalLayout_4.setStretch(7, 1)
        self.horizontalLayout_4.setStretch(8, 1)
        self.horizontalLayout_4.setStretch(9, 1)
        self.horizontalLayout_4.setStretch(10, 1)
        self.horizontalLayout_4.setStretch(11, 1)
        self.horizontalLayout_4.setStretch(12, 1)
        self.horizontalLayout_4.setStretch(13, 2)

        self.verticalLayout.addWidget(self.M_line_2)

        self.M_line_3 = QFrame(self.Main_Area)
        self.M_line_3.setObjectName(u"M_line_3")
        sizePolicy2.setHeightForWidth(self.M_line_3.sizePolicy().hasHeightForWidth())
        self.M_line_3.setSizePolicy(sizePolicy2)
        self.M_line_3.setMinimumSize(QSize(666, 0))
        self.M_line_3.setMaximumSize(QSize(666, 16777215))
        self.M_line_3.setFrameShape(QFrame.NoFrame)
        self.M_line_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.M_line_3)
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(1, 1, 6, 1)
        self.key_tab = QPushButton(self.M_line_3)
        self.key_tab.setObjectName(u"key_tab")
        sizePolicy1.setHeightForWidth(self.key_tab.sizePolicy().hasHeightForWidth())
        self.key_tab.setSizePolicy(sizePolicy1)
        self.key_tab.setMinimumSize(QSize(60, 42))
        self.key_tab.setMaximumSize(QSize(60, 42))
        palette27 = QPalette()
        palette27.setBrush(QPalette.Active, QPalette.Button, brush)
        palette27.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette27.setBrush(QPalette.Active, QPalette.Base, brush)
        palette27.setBrush(QPalette.Active, QPalette.Window, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette27.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette27.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_tab.setPalette(palette27)
        self.key_tab.setFont(font5)
        self.key_tab.setFocusPolicy(Qt.NoFocus)
        self.key_tab.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_tab.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_5.addWidget(self.key_tab)

        self.key_q = QPushButton(self.M_line_3)
        self.key_q.setObjectName(u"key_q")
        sizePolicy1.setHeightForWidth(self.key_q.sizePolicy().hasHeightForWidth())
        self.key_q.setSizePolicy(sizePolicy1)
        self.key_q.setMinimumSize(QSize(42, 42))
        self.key_q.setMaximumSize(QSize(42, 42))
        palette28 = QPalette()
        palette28.setBrush(QPalette.Active, QPalette.Button, brush)
        palette28.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette28.setBrush(QPalette.Active, QPalette.Base, brush)
        palette28.setBrush(QPalette.Active, QPalette.Window, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette28.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette28.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_q.setPalette(palette28)
        self.key_q.setFont(font5)
        self.key_q.setFocusPolicy(Qt.NoFocus)
        self.key_q.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_q.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_5.addWidget(self.key_q)

        self.key_w = QPushButton(self.M_line_3)
        self.key_w.setObjectName(u"key_w")
        sizePolicy1.setHeightForWidth(self.key_w.sizePolicy().hasHeightForWidth())
        self.key_w.setSizePolicy(sizePolicy1)
        self.key_w.setMinimumSize(QSize(42, 42))
        self.key_w.setMaximumSize(QSize(42, 42))
        palette29 = QPalette()
        palette29.setBrush(QPalette.Active, QPalette.Button, brush)
        palette29.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette29.setBrush(QPalette.Active, QPalette.Base, brush)
        palette29.setBrush(QPalette.Active, QPalette.Window, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette29.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette29.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_w.setPalette(palette29)
        self.key_w.setFont(font5)
        self.key_w.setFocusPolicy(Qt.NoFocus)
        self.key_w.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_w.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_5.addWidget(self.key_w)

        self.key_e = QPushButton(self.M_line_3)
        self.key_e.setObjectName(u"key_e")
        sizePolicy1.setHeightForWidth(self.key_e.sizePolicy().hasHeightForWidth())
        self.key_e.setSizePolicy(sizePolicy1)
        self.key_e.setMinimumSize(QSize(42, 42))
        self.key_e.setMaximumSize(QSize(42, 42))
        palette30 = QPalette()
        palette30.setBrush(QPalette.Active, QPalette.Button, brush)
        palette30.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette30.setBrush(QPalette.Active, QPalette.Base, brush)
        palette30.setBrush(QPalette.Active, QPalette.Window, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette30.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette30.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_e.setPalette(palette30)
        self.key_e.setFont(font5)
        self.key_e.setFocusPolicy(Qt.NoFocus)
        self.key_e.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_e.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_5.addWidget(self.key_e)

        self.key_r = QPushButton(self.M_line_3)
        self.key_r.setObjectName(u"key_r")
        sizePolicy1.setHeightForWidth(self.key_r.sizePolicy().hasHeightForWidth())
        self.key_r.setSizePolicy(sizePolicy1)
        self.key_r.setMinimumSize(QSize(42, 42))
        self.key_r.setMaximumSize(QSize(42, 42))
        palette31 = QPalette()
        palette31.setBrush(QPalette.Active, QPalette.Button, brush)
        palette31.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette31.setBrush(QPalette.Active, QPalette.Base, brush)
        palette31.setBrush(QPalette.Active, QPalette.Window, brush)
        palette31.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette31.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette31.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette31.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette31.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette31.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette31.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette31.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_r.setPalette(palette31)
        self.key_r.setFont(font5)
        self.key_r.setFocusPolicy(Qt.NoFocus)
        self.key_r.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_r.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_5.addWidget(self.key_r)

        self.key_t = QPushButton(self.M_line_3)
        self.key_t.setObjectName(u"key_t")
        sizePolicy1.setHeightForWidth(self.key_t.sizePolicy().hasHeightForWidth())
        self.key_t.setSizePolicy(sizePolicy1)
        self.key_t.setMinimumSize(QSize(42, 42))
        self.key_t.setMaximumSize(QSize(42, 42))
        palette32 = QPalette()
        palette32.setBrush(QPalette.Active, QPalette.Button, brush)
        palette32.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette32.setBrush(QPalette.Active, QPalette.Base, brush)
        palette32.setBrush(QPalette.Active, QPalette.Window, brush)
        palette32.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette32.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette32.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette32.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette32.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette32.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette32.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette32.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_t.setPalette(palette32)
        self.key_t.setFont(font5)
        self.key_t.setFocusPolicy(Qt.NoFocus)
        self.key_t.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_t.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_5.addWidget(self.key_t)

        self.key_y = QPushButton(self.M_line_3)
        self.key_y.setObjectName(u"key_y")
        sizePolicy1.setHeightForWidth(self.key_y.sizePolicy().hasHeightForWidth())
        self.key_y.setSizePolicy(sizePolicy1)
        self.key_y.setMinimumSize(QSize(42, 42))
        self.key_y.setMaximumSize(QSize(42, 42))
        palette33 = QPalette()
        palette33.setBrush(QPalette.Active, QPalette.Button, brush)
        palette33.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette33.setBrush(QPalette.Active, QPalette.Base, brush)
        palette33.setBrush(QPalette.Active, QPalette.Window, brush)
        palette33.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette33.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette33.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette33.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette33.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette33.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette33.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette33.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_y.setPalette(palette33)
        self.key_y.setFont(font5)
        self.key_y.setFocusPolicy(Qt.NoFocus)
        self.key_y.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_y.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_5.addWidget(self.key_y)

        self.key_u = QPushButton(self.M_line_3)
        self.key_u.setObjectName(u"key_u")
        sizePolicy1.setHeightForWidth(self.key_u.sizePolicy().hasHeightForWidth())
        self.key_u.setSizePolicy(sizePolicy1)
        self.key_u.setMinimumSize(QSize(42, 42))
        self.key_u.setMaximumSize(QSize(42, 42))
        palette34 = QPalette()
        palette34.setBrush(QPalette.Active, QPalette.Button, brush)
        palette34.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette34.setBrush(QPalette.Active, QPalette.Base, brush)
        palette34.setBrush(QPalette.Active, QPalette.Window, brush)
        palette34.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette34.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette34.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette34.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette34.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette34.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette34.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette34.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_u.setPalette(palette34)
        self.key_u.setFont(font5)
        self.key_u.setFocusPolicy(Qt.NoFocus)
        self.key_u.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_u.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_5.addWidget(self.key_u)

        self.key_i = QPushButton(self.M_line_3)
        self.key_i.setObjectName(u"key_i")
        sizePolicy1.setHeightForWidth(self.key_i.sizePolicy().hasHeightForWidth())
        self.key_i.setSizePolicy(sizePolicy1)
        self.key_i.setMinimumSize(QSize(42, 42))
        self.key_i.setMaximumSize(QSize(42, 42))
        palette35 = QPalette()
        palette35.setBrush(QPalette.Active, QPalette.Button, brush)
        palette35.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette35.setBrush(QPalette.Active, QPalette.Base, brush)
        palette35.setBrush(QPalette.Active, QPalette.Window, brush)
        palette35.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette35.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette35.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette35.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette35.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette35.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette35.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette35.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_i.setPalette(palette35)
        self.key_i.setFont(font5)
        self.key_i.setFocusPolicy(Qt.NoFocus)
        self.key_i.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_i.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_5.addWidget(self.key_i)

        self.key_o = QPushButton(self.M_line_3)
        self.key_o.setObjectName(u"key_o")
        sizePolicy1.setHeightForWidth(self.key_o.sizePolicy().hasHeightForWidth())
        self.key_o.setSizePolicy(sizePolicy1)
        self.key_o.setMinimumSize(QSize(42, 42))
        self.key_o.setMaximumSize(QSize(42, 42))
        palette36 = QPalette()
        palette36.setBrush(QPalette.Active, QPalette.Button, brush)
        palette36.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette36.setBrush(QPalette.Active, QPalette.Base, brush)
        palette36.setBrush(QPalette.Active, QPalette.Window, brush)
        palette36.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette36.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette36.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette36.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette36.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette36.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette36.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette36.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_o.setPalette(palette36)
        self.key_o.setFont(font5)
        self.key_o.setFocusPolicy(Qt.NoFocus)
        self.key_o.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_o.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_5.addWidget(self.key_o)

        self.key_p = QPushButton(self.M_line_3)
        self.key_p.setObjectName(u"key_p")
        sizePolicy1.setHeightForWidth(self.key_p.sizePolicy().hasHeightForWidth())
        self.key_p.setSizePolicy(sizePolicy1)
        self.key_p.setMinimumSize(QSize(42, 42))
        self.key_p.setMaximumSize(QSize(42, 42))
        palette37 = QPalette()
        palette37.setBrush(QPalette.Active, QPalette.Button, brush)
        palette37.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette37.setBrush(QPalette.Active, QPalette.Base, brush)
        palette37.setBrush(QPalette.Active, QPalette.Window, brush)
        palette37.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette37.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette37.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette37.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette37.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette37.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette37.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette37.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_p.setPalette(palette37)
        self.key_p.setFont(font5)
        self.key_p.setFocusPolicy(Qt.NoFocus)
        self.key_p.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_p.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_5.addWidget(self.key_p)

        self.key_bracketleft = QPushButton(self.M_line_3)
        self.key_bracketleft.setObjectName(u"key_bracketleft")
        sizePolicy1.setHeightForWidth(self.key_bracketleft.sizePolicy().hasHeightForWidth())
        self.key_bracketleft.setSizePolicy(sizePolicy1)
        self.key_bracketleft.setMinimumSize(QSize(42, 42))
        self.key_bracketleft.setMaximumSize(QSize(42, 42))
        palette38 = QPalette()
        palette38.setBrush(QPalette.Active, QPalette.Button, brush)
        palette38.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette38.setBrush(QPalette.Active, QPalette.Base, brush)
        palette38.setBrush(QPalette.Active, QPalette.Window, brush)
        palette38.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette38.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette38.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette38.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette38.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette38.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette38.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette38.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_bracketleft.setPalette(palette38)
        self.key_bracketleft.setFont(font5)
        self.key_bracketleft.setFocusPolicy(Qt.NoFocus)
        self.key_bracketleft.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_bracketleft.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_5.addWidget(self.key_bracketleft)

        self.key_bracketright = QPushButton(self.M_line_3)
        self.key_bracketright.setObjectName(u"key_bracketright")
        sizePolicy1.setHeightForWidth(self.key_bracketright.sizePolicy().hasHeightForWidth())
        self.key_bracketright.setSizePolicy(sizePolicy1)
        self.key_bracketright.setMinimumSize(QSize(42, 42))
        self.key_bracketright.setMaximumSize(QSize(42, 42))
        palette39 = QPalette()
        palette39.setBrush(QPalette.Active, QPalette.Button, brush)
        palette39.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette39.setBrush(QPalette.Active, QPalette.Base, brush)
        palette39.setBrush(QPalette.Active, QPalette.Window, brush)
        palette39.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette39.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette39.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette39.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette39.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette39.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette39.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette39.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_bracketright.setPalette(palette39)
        self.key_bracketright.setFont(font5)
        self.key_bracketright.setFocusPolicy(Qt.NoFocus)
        self.key_bracketright.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_bracketright.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_5.addWidget(self.key_bracketright)

        self.key_backslash = QPushButton(self.M_line_3)
        self.key_backslash.setObjectName(u"key_backslash")
        sizePolicy1.setHeightForWidth(self.key_backslash.sizePolicy().hasHeightForWidth())
        self.key_backslash.setSizePolicy(sizePolicy1)
        self.key_backslash.setMinimumSize(QSize(60, 42))
        self.key_backslash.setMaximumSize(QSize(60, 42))
        palette40 = QPalette()
        palette40.setBrush(QPalette.Active, QPalette.Button, brush)
        palette40.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette40.setBrush(QPalette.Active, QPalette.Base, brush)
        palette40.setBrush(QPalette.Active, QPalette.Window, brush)
        palette40.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette40.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette40.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette40.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette40.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette40.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette40.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette40.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_backslash.setPalette(palette40)
        self.key_backslash.setFont(font5)
        self.key_backslash.setFocusPolicy(Qt.NoFocus)
        self.key_backslash.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_backslash.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_5.addWidget(self.key_backslash)

        self.horizontalLayout_5.setStretch(0, 4)
        self.horizontalLayout_5.setStretch(1, 3)
        self.horizontalLayout_5.setStretch(2, 3)
        self.horizontalLayout_5.setStretch(3, 3)
        self.horizontalLayout_5.setStretch(4, 3)
        self.horizontalLayout_5.setStretch(5, 3)
        self.horizontalLayout_5.setStretch(6, 3)
        self.horizontalLayout_5.setStretch(7, 3)
        self.horizontalLayout_5.setStretch(8, 3)
        self.horizontalLayout_5.setStretch(9, 3)
        self.horizontalLayout_5.setStretch(10, 3)
        self.horizontalLayout_5.setStretch(11, 3)
        self.horizontalLayout_5.setStretch(12, 3)
        self.horizontalLayout_5.setStretch(13, 4)

        self.verticalLayout.addWidget(self.M_line_3)

        self.M_line_4 = QFrame(self.Main_Area)
        self.M_line_4.setObjectName(u"M_line_4")
        sizePolicy2.setHeightForWidth(self.M_line_4.sizePolicy().hasHeightForWidth())
        self.M_line_4.setSizePolicy(sizePolicy2)
        self.M_line_4.setMinimumSize(QSize(666, 0))
        self.M_line_4.setMaximumSize(QSize(666, 16777215))
        self.M_line_4.setFrameShape(QFrame.NoFrame)
        self.M_line_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.M_line_4)
        self.horizontalLayout_6.setSpacing(3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(1, 1, 6, 1)
        self.key_capslock = QPushButton(self.M_line_4)
        self.key_capslock.setObjectName(u"key_capslock")
        sizePolicy1.setHeightForWidth(self.key_capslock.sizePolicy().hasHeightForWidth())
        self.key_capslock.setSizePolicy(sizePolicy1)
        self.key_capslock.setMinimumSize(QSize(68, 42))
        self.key_capslock.setMaximumSize(QSize(68, 42))
        palette41 = QPalette()
        palette41.setBrush(QPalette.Active, QPalette.Button, brush)
        palette41.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette41.setBrush(QPalette.Active, QPalette.Base, brush)
        palette41.setBrush(QPalette.Active, QPalette.Window, brush)
        palette41.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette41.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette41.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette41.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette41.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette41.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette41.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette41.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_capslock.setPalette(palette41)
        self.key_capslock.setFont(font5)
        self.key_capslock.setFocusPolicy(Qt.NoFocus)
        self.key_capslock.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_capslock.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_6.addWidget(self.key_capslock)

        self.key_a = QPushButton(self.M_line_4)
        self.key_a.setObjectName(u"key_a")
        sizePolicy1.setHeightForWidth(self.key_a.sizePolicy().hasHeightForWidth())
        self.key_a.setSizePolicy(sizePolicy1)
        self.key_a.setMinimumSize(QSize(42, 42))
        self.key_a.setMaximumSize(QSize(42, 42))
        palette42 = QPalette()
        palette42.setBrush(QPalette.Active, QPalette.Button, brush)
        palette42.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette42.setBrush(QPalette.Active, QPalette.Base, brush)
        palette42.setBrush(QPalette.Active, QPalette.Window, brush)
        palette42.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette42.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette42.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette42.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette42.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette42.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette42.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette42.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_a.setPalette(palette42)
        self.key_a.setFont(font5)
        self.key_a.setFocusPolicy(Qt.NoFocus)
        self.key_a.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_a.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_6.addWidget(self.key_a)

        self.key_s = QPushButton(self.M_line_4)
        self.key_s.setObjectName(u"key_s")
        sizePolicy1.setHeightForWidth(self.key_s.sizePolicy().hasHeightForWidth())
        self.key_s.setSizePolicy(sizePolicy1)
        self.key_s.setMinimumSize(QSize(42, 42))
        self.key_s.setMaximumSize(QSize(42, 42))
        palette43 = QPalette()
        palette43.setBrush(QPalette.Active, QPalette.Button, brush)
        palette43.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette43.setBrush(QPalette.Active, QPalette.Base, brush)
        palette43.setBrush(QPalette.Active, QPalette.Window, brush)
        palette43.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette43.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette43.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette43.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette43.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette43.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette43.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette43.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_s.setPalette(palette43)
        self.key_s.setFont(font5)
        self.key_s.setFocusPolicy(Qt.NoFocus)
        self.key_s.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_s.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_6.addWidget(self.key_s)

        self.key_d = QPushButton(self.M_line_4)
        self.key_d.setObjectName(u"key_d")
        sizePolicy1.setHeightForWidth(self.key_d.sizePolicy().hasHeightForWidth())
        self.key_d.setSizePolicy(sizePolicy1)
        self.key_d.setMinimumSize(QSize(42, 42))
        self.key_d.setMaximumSize(QSize(42, 42))
        palette44 = QPalette()
        palette44.setBrush(QPalette.Active, QPalette.Button, brush)
        palette44.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette44.setBrush(QPalette.Active, QPalette.Base, brush)
        palette44.setBrush(QPalette.Active, QPalette.Window, brush)
        palette44.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette44.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette44.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette44.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette44.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette44.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette44.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette44.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_d.setPalette(palette44)
        self.key_d.setFont(font5)
        self.key_d.setFocusPolicy(Qt.NoFocus)
        self.key_d.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_d.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_6.addWidget(self.key_d)

        self.key_f = QPushButton(self.M_line_4)
        self.key_f.setObjectName(u"key_f")
        sizePolicy1.setHeightForWidth(self.key_f.sizePolicy().hasHeightForWidth())
        self.key_f.setSizePolicy(sizePolicy1)
        self.key_f.setMinimumSize(QSize(42, 42))
        self.key_f.setMaximumSize(QSize(42, 42))
        palette45 = QPalette()
        palette45.setBrush(QPalette.Active, QPalette.Button, brush)
        palette45.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette45.setBrush(QPalette.Active, QPalette.Base, brush)
        palette45.setBrush(QPalette.Active, QPalette.Window, brush)
        palette45.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette45.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette45.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette45.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette45.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette45.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette45.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette45.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_f.setPalette(palette45)
        self.key_f.setFont(font5)
        self.key_f.setFocusPolicy(Qt.NoFocus)
        self.key_f.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_f.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_6.addWidget(self.key_f)

        self.key_g = QPushButton(self.M_line_4)
        self.key_g.setObjectName(u"key_g")
        sizePolicy1.setHeightForWidth(self.key_g.sizePolicy().hasHeightForWidth())
        self.key_g.setSizePolicy(sizePolicy1)
        self.key_g.setMinimumSize(QSize(42, 42))
        self.key_g.setMaximumSize(QSize(42, 42))
        palette46 = QPalette()
        palette46.setBrush(QPalette.Active, QPalette.Button, brush)
        palette46.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette46.setBrush(QPalette.Active, QPalette.Base, brush)
        palette46.setBrush(QPalette.Active, QPalette.Window, brush)
        palette46.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette46.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette46.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette46.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette46.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette46.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette46.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette46.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_g.setPalette(palette46)
        self.key_g.setFont(font5)
        self.key_g.setFocusPolicy(Qt.NoFocus)
        self.key_g.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_g.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_6.addWidget(self.key_g)

        self.key_h = QPushButton(self.M_line_4)
        self.key_h.setObjectName(u"key_h")
        sizePolicy1.setHeightForWidth(self.key_h.sizePolicy().hasHeightForWidth())
        self.key_h.setSizePolicy(sizePolicy1)
        self.key_h.setMinimumSize(QSize(42, 42))
        self.key_h.setMaximumSize(QSize(42, 42))
        palette47 = QPalette()
        palette47.setBrush(QPalette.Active, QPalette.Button, brush)
        palette47.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette47.setBrush(QPalette.Active, QPalette.Base, brush)
        palette47.setBrush(QPalette.Active, QPalette.Window, brush)
        palette47.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette47.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette47.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette47.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette47.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette47.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette47.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette47.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_h.setPalette(palette47)
        self.key_h.setFont(font5)
        self.key_h.setFocusPolicy(Qt.NoFocus)
        self.key_h.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_h.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_6.addWidget(self.key_h)

        self.key_j = QPushButton(self.M_line_4)
        self.key_j.setObjectName(u"key_j")
        sizePolicy1.setHeightForWidth(self.key_j.sizePolicy().hasHeightForWidth())
        self.key_j.setSizePolicy(sizePolicy1)
        self.key_j.setMinimumSize(QSize(42, 42))
        self.key_j.setMaximumSize(QSize(42, 42))
        palette48 = QPalette()
        palette48.setBrush(QPalette.Active, QPalette.Button, brush)
        palette48.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette48.setBrush(QPalette.Active, QPalette.Base, brush)
        palette48.setBrush(QPalette.Active, QPalette.Window, brush)
        palette48.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette48.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette48.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette48.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette48.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette48.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette48.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette48.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_j.setPalette(palette48)
        self.key_j.setFont(font5)
        self.key_j.setFocusPolicy(Qt.NoFocus)
        self.key_j.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_j.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_6.addWidget(self.key_j)

        self.key_k = QPushButton(self.M_line_4)
        self.key_k.setObjectName(u"key_k")
        sizePolicy1.setHeightForWidth(self.key_k.sizePolicy().hasHeightForWidth())
        self.key_k.setSizePolicy(sizePolicy1)
        self.key_k.setMinimumSize(QSize(42, 42))
        self.key_k.setMaximumSize(QSize(42, 42))
        palette49 = QPalette()
        palette49.setBrush(QPalette.Active, QPalette.Button, brush)
        palette49.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette49.setBrush(QPalette.Active, QPalette.Base, brush)
        palette49.setBrush(QPalette.Active, QPalette.Window, brush)
        palette49.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette49.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette49.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette49.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette49.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette49.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette49.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette49.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_k.setPalette(palette49)
        self.key_k.setFont(font5)
        self.key_k.setFocusPolicy(Qt.NoFocus)
        self.key_k.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_k.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_6.addWidget(self.key_k)

        self.key_l = QPushButton(self.M_line_4)
        self.key_l.setObjectName(u"key_l")
        sizePolicy1.setHeightForWidth(self.key_l.sizePolicy().hasHeightForWidth())
        self.key_l.setSizePolicy(sizePolicy1)
        self.key_l.setMinimumSize(QSize(42, 42))
        self.key_l.setMaximumSize(QSize(42, 42))
        palette50 = QPalette()
        palette50.setBrush(QPalette.Active, QPalette.Button, brush)
        palette50.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette50.setBrush(QPalette.Active, QPalette.Base, brush)
        palette50.setBrush(QPalette.Active, QPalette.Window, brush)
        palette50.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette50.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette50.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette50.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette50.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette50.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette50.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette50.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_l.setPalette(palette50)
        self.key_l.setFont(font5)
        self.key_l.setFocusPolicy(Qt.NoFocus)
        self.key_l.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_l.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_6.addWidget(self.key_l)

        self.key_semicolon = QPushButton(self.M_line_4)
        self.key_semicolon.setObjectName(u"key_semicolon")
        sizePolicy1.setHeightForWidth(self.key_semicolon.sizePolicy().hasHeightForWidth())
        self.key_semicolon.setSizePolicy(sizePolicy1)
        self.key_semicolon.setMinimumSize(QSize(42, 42))
        self.key_semicolon.setMaximumSize(QSize(42, 42))
        palette51 = QPalette()
        palette51.setBrush(QPalette.Active, QPalette.Button, brush)
        palette51.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette51.setBrush(QPalette.Active, QPalette.Base, brush)
        palette51.setBrush(QPalette.Active, QPalette.Window, brush)
        palette51.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette51.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette51.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette51.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette51.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette51.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette51.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette51.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_semicolon.setPalette(palette51)
        self.key_semicolon.setFont(font5)
        self.key_semicolon.setFocusPolicy(Qt.NoFocus)
        self.key_semicolon.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_semicolon.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_6.addWidget(self.key_semicolon)

        self.key_quote = QPushButton(self.M_line_4)
        self.key_quote.setObjectName(u"key_quote")
        sizePolicy1.setHeightForWidth(self.key_quote.sizePolicy().hasHeightForWidth())
        self.key_quote.setSizePolicy(sizePolicy1)
        self.key_quote.setMinimumSize(QSize(42, 42))
        self.key_quote.setMaximumSize(QSize(42, 42))
        palette52 = QPalette()
        palette52.setBrush(QPalette.Active, QPalette.Button, brush)
        palette52.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette52.setBrush(QPalette.Active, QPalette.Base, brush)
        palette52.setBrush(QPalette.Active, QPalette.Window, brush)
        palette52.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette52.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette52.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette52.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette52.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette52.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette52.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette52.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_quote.setPalette(palette52)
        self.key_quote.setFont(font5)
        self.key_quote.setFocusPolicy(Qt.NoFocus)
        self.key_quote.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_quote.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_6.addWidget(self.key_quote)

        self.key_enter = QPushButton(self.M_line_4)
        self.key_enter.setObjectName(u"key_enter")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.key_enter.sizePolicy().hasHeightForWidth())
        self.key_enter.setSizePolicy(sizePolicy3)
        self.key_enter.setMinimumSize(QSize(94, 42))
        self.key_enter.setMaximumSize(QSize(94, 42))
        palette53 = QPalette()
        palette53.setBrush(QPalette.Active, QPalette.Button, brush)
        palette53.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette53.setBrush(QPalette.Active, QPalette.Base, brush)
        palette53.setBrush(QPalette.Active, QPalette.Window, brush)
        palette53.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette53.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette53.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette53.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette53.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette53.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette53.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette53.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_enter.setPalette(palette53)
        self.key_enter.setFont(font5)
        self.key_enter.setFocusPolicy(Qt.NoFocus)
        self.key_enter.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_enter.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_6.addWidget(self.key_enter)


        self.verticalLayout.addWidget(self.M_line_4)

        self.M_line_5 = QFrame(self.Main_Area)
        self.M_line_5.setObjectName(u"M_line_5")
        sizePolicy2.setHeightForWidth(self.M_line_5.sizePolicy().hasHeightForWidth())
        self.M_line_5.setSizePolicy(sizePolicy2)
        self.M_line_5.setMinimumSize(QSize(666, 0))
        self.M_line_5.setMaximumSize(QSize(666, 16777215))
        self.M_line_5.setFrameShape(QFrame.NoFrame)
        self.M_line_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.M_line_5)
        self.horizontalLayout_7.setSpacing(3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(1, 1, 6, 1)
        self.key_shift_l = QPushButton(self.M_line_5)
        self.key_shift_l.setObjectName(u"key_shift_l")
        sizePolicy1.setHeightForWidth(self.key_shift_l.sizePolicy().hasHeightForWidth())
        self.key_shift_l.setSizePolicy(sizePolicy1)
        self.key_shift_l.setMinimumSize(QSize(104, 42))
        self.key_shift_l.setMaximumSize(QSize(104, 42))
        palette54 = QPalette()
        palette54.setBrush(QPalette.Active, QPalette.Button, brush)
        palette54.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette54.setBrush(QPalette.Active, QPalette.Base, brush)
        palette54.setBrush(QPalette.Active, QPalette.Window, brush)
        palette54.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette54.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette54.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette54.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette54.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette54.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette54.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette54.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_shift_l.setPalette(palette54)
        self.key_shift_l.setFont(font5)
        self.key_shift_l.setFocusPolicy(Qt.NoFocus)
        self.key_shift_l.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_shift_l.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_7.addWidget(self.key_shift_l)

        self.key_z = QPushButton(self.M_line_5)
        self.key_z.setObjectName(u"key_z")
        sizePolicy1.setHeightForWidth(self.key_z.sizePolicy().hasHeightForWidth())
        self.key_z.setSizePolicy(sizePolicy1)
        self.key_z.setMinimumSize(QSize(42, 42))
        self.key_z.setMaximumSize(QSize(42, 42))
        palette55 = QPalette()
        palette55.setBrush(QPalette.Active, QPalette.Button, brush)
        palette55.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette55.setBrush(QPalette.Active, QPalette.Base, brush)
        palette55.setBrush(QPalette.Active, QPalette.Window, brush)
        palette55.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette55.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette55.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette55.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette55.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette55.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette55.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette55.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_z.setPalette(palette55)
        self.key_z.setFont(font5)
        self.key_z.setFocusPolicy(Qt.NoFocus)
        self.key_z.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_z.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_7.addWidget(self.key_z)

        self.key_x = QPushButton(self.M_line_5)
        self.key_x.setObjectName(u"key_x")
        sizePolicy1.setHeightForWidth(self.key_x.sizePolicy().hasHeightForWidth())
        self.key_x.setSizePolicy(sizePolicy1)
        self.key_x.setMinimumSize(QSize(42, 42))
        self.key_x.setMaximumSize(QSize(42, 42))
        palette56 = QPalette()
        palette56.setBrush(QPalette.Active, QPalette.Button, brush)
        palette56.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette56.setBrush(QPalette.Active, QPalette.Base, brush)
        palette56.setBrush(QPalette.Active, QPalette.Window, brush)
        palette56.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette56.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette56.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette56.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette56.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette56.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette56.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette56.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_x.setPalette(palette56)
        self.key_x.setFont(font5)
        self.key_x.setFocusPolicy(Qt.NoFocus)
        self.key_x.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_x.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_7.addWidget(self.key_x)

        self.key_c = QPushButton(self.M_line_5)
        self.key_c.setObjectName(u"key_c")
        sizePolicy1.setHeightForWidth(self.key_c.sizePolicy().hasHeightForWidth())
        self.key_c.setSizePolicy(sizePolicy1)
        self.key_c.setMinimumSize(QSize(42, 42))
        self.key_c.setMaximumSize(QSize(42, 42))
        palette57 = QPalette()
        palette57.setBrush(QPalette.Active, QPalette.Button, brush)
        palette57.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette57.setBrush(QPalette.Active, QPalette.Base, brush)
        palette57.setBrush(QPalette.Active, QPalette.Window, brush)
        palette57.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette57.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette57.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette57.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette57.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette57.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette57.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette57.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_c.setPalette(palette57)
        self.key_c.setFont(font5)
        self.key_c.setFocusPolicy(Qt.NoFocus)
        self.key_c.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_c.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_7.addWidget(self.key_c)

        self.key_v = QPushButton(self.M_line_5)
        self.key_v.setObjectName(u"key_v")
        sizePolicy1.setHeightForWidth(self.key_v.sizePolicy().hasHeightForWidth())
        self.key_v.setSizePolicy(sizePolicy1)
        self.key_v.setMinimumSize(QSize(42, 42))
        self.key_v.setMaximumSize(QSize(42, 42))
        palette58 = QPalette()
        palette58.setBrush(QPalette.Active, QPalette.Button, brush)
        palette58.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette58.setBrush(QPalette.Active, QPalette.Base, brush)
        palette58.setBrush(QPalette.Active, QPalette.Window, brush)
        palette58.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette58.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette58.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette58.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette58.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette58.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette58.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette58.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_v.setPalette(palette58)
        self.key_v.setFont(font5)
        self.key_v.setFocusPolicy(Qt.NoFocus)
        self.key_v.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_v.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_7.addWidget(self.key_v)

        self.key_b = QPushButton(self.M_line_5)
        self.key_b.setObjectName(u"key_b")
        sizePolicy1.setHeightForWidth(self.key_b.sizePolicy().hasHeightForWidth())
        self.key_b.setSizePolicy(sizePolicy1)
        self.key_b.setMinimumSize(QSize(42, 42))
        self.key_b.setMaximumSize(QSize(42, 42))
        palette59 = QPalette()
        palette59.setBrush(QPalette.Active, QPalette.Button, brush)
        palette59.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette59.setBrush(QPalette.Active, QPalette.Base, brush)
        palette59.setBrush(QPalette.Active, QPalette.Window, brush)
        palette59.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette59.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette59.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette59.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette59.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette59.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette59.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette59.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_b.setPalette(palette59)
        self.key_b.setFont(font5)
        self.key_b.setFocusPolicy(Qt.NoFocus)
        self.key_b.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_b.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_7.addWidget(self.key_b)

        self.key_n = QPushButton(self.M_line_5)
        self.key_n.setObjectName(u"key_n")
        sizePolicy1.setHeightForWidth(self.key_n.sizePolicy().hasHeightForWidth())
        self.key_n.setSizePolicy(sizePolicy1)
        self.key_n.setMinimumSize(QSize(42, 42))
        self.key_n.setMaximumSize(QSize(42, 42))
        palette60 = QPalette()
        palette60.setBrush(QPalette.Active, QPalette.Button, brush)
        palette60.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette60.setBrush(QPalette.Active, QPalette.Base, brush)
        palette60.setBrush(QPalette.Active, QPalette.Window, brush)
        palette60.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette60.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette60.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette60.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette60.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette60.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette60.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette60.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_n.setPalette(palette60)
        self.key_n.setFont(font5)
        self.key_n.setFocusPolicy(Qt.NoFocus)
        self.key_n.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_n.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_7.addWidget(self.key_n)

        self.key_m = QPushButton(self.M_line_5)
        self.key_m.setObjectName(u"key_m")
        sizePolicy1.setHeightForWidth(self.key_m.sizePolicy().hasHeightForWidth())
        self.key_m.setSizePolicy(sizePolicy1)
        self.key_m.setMinimumSize(QSize(42, 42))
        self.key_m.setMaximumSize(QSize(42, 42))
        palette61 = QPalette()
        palette61.setBrush(QPalette.Active, QPalette.Button, brush)
        palette61.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette61.setBrush(QPalette.Active, QPalette.Base, brush)
        palette61.setBrush(QPalette.Active, QPalette.Window, brush)
        palette61.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette61.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette61.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette61.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette61.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette61.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette61.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette61.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_m.setPalette(palette61)
        self.key_m.setFont(font5)
        self.key_m.setFocusPolicy(Qt.NoFocus)
        self.key_m.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_m.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_7.addWidget(self.key_m)

        self.key_comma = QPushButton(self.M_line_5)
        self.key_comma.setObjectName(u"key_comma")
        sizePolicy1.setHeightForWidth(self.key_comma.sizePolicy().hasHeightForWidth())
        self.key_comma.setSizePolicy(sizePolicy1)
        self.key_comma.setMinimumSize(QSize(42, 42))
        self.key_comma.setMaximumSize(QSize(42, 42))
        palette62 = QPalette()
        palette62.setBrush(QPalette.Active, QPalette.Button, brush)
        palette62.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette62.setBrush(QPalette.Active, QPalette.Base, brush)
        palette62.setBrush(QPalette.Active, QPalette.Window, brush)
        palette62.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette62.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette62.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette62.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette62.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette62.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette62.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette62.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_comma.setPalette(palette62)
        self.key_comma.setFont(font5)
        self.key_comma.setFocusPolicy(Qt.NoFocus)
        self.key_comma.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_comma.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_7.addWidget(self.key_comma)

        self.key_period = QPushButton(self.M_line_5)
        self.key_period.setObjectName(u"key_period")
        sizePolicy1.setHeightForWidth(self.key_period.sizePolicy().hasHeightForWidth())
        self.key_period.setSizePolicy(sizePolicy1)
        self.key_period.setMinimumSize(QSize(42, 42))
        self.key_period.setMaximumSize(QSize(42, 42))
        palette63 = QPalette()
        palette63.setBrush(QPalette.Active, QPalette.Button, brush)
        palette63.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette63.setBrush(QPalette.Active, QPalette.Base, brush)
        palette63.setBrush(QPalette.Active, QPalette.Window, brush)
        palette63.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette63.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette63.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette63.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette63.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette63.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette63.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette63.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_period.setPalette(palette63)
        self.key_period.setFont(font5)
        self.key_period.setFocusPolicy(Qt.NoFocus)
        self.key_period.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_period.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_7.addWidget(self.key_period)

        self.key_slash = QPushButton(self.M_line_5)
        self.key_slash.setObjectName(u"key_slash")
        sizePolicy1.setHeightForWidth(self.key_slash.sizePolicy().hasHeightForWidth())
        self.key_slash.setSizePolicy(sizePolicy1)
        self.key_slash.setMinimumSize(QSize(42, 42))
        self.key_slash.setMaximumSize(QSize(42, 42))
        palette64 = QPalette()
        palette64.setBrush(QPalette.Active, QPalette.Button, brush)
        palette64.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette64.setBrush(QPalette.Active, QPalette.Base, brush)
        palette64.setBrush(QPalette.Active, QPalette.Window, brush)
        palette64.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette64.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette64.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette64.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette64.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette64.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette64.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette64.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_slash.setPalette(palette64)
        self.key_slash.setFont(font5)
        self.key_slash.setFocusPolicy(Qt.NoFocus)
        self.key_slash.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_slash.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_7.addWidget(self.key_slash)

        self.key_shift_r = QPushButton(self.M_line_5)
        self.key_shift_r.setObjectName(u"key_shift_r")
        sizePolicy1.setHeightForWidth(self.key_shift_r.sizePolicy().hasHeightForWidth())
        self.key_shift_r.setSizePolicy(sizePolicy1)
        self.key_shift_r.setMinimumSize(QSize(104, 42))
        self.key_shift_r.setMaximumSize(QSize(104, 42))
        palette65 = QPalette()
        palette65.setBrush(QPalette.Active, QPalette.Button, brush)
        palette65.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette65.setBrush(QPalette.Active, QPalette.Base, brush)
        palette65.setBrush(QPalette.Active, QPalette.Window, brush)
        palette65.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette65.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette65.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette65.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette65.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette65.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette65.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette65.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_shift_r.setPalette(palette65)
        self.key_shift_r.setFont(font5)
        self.key_shift_r.setFocusPolicy(Qt.NoFocus)
        self.key_shift_r.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_shift_r.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_7.addWidget(self.key_shift_r)

        self.horizontalLayout_7.setStretch(0, 5)
        self.horizontalLayout_7.setStretch(1, 2)
        self.horizontalLayout_7.setStretch(2, 2)
        self.horizontalLayout_7.setStretch(3, 2)
        self.horizontalLayout_7.setStretch(4, 2)
        self.horizontalLayout_7.setStretch(5, 2)
        self.horizontalLayout_7.setStretch(6, 2)
        self.horizontalLayout_7.setStretch(7, 2)
        self.horizontalLayout_7.setStretch(8, 2)
        self.horizontalLayout_7.setStretch(9, 2)
        self.horizontalLayout_7.setStretch(10, 2)
        self.horizontalLayout_7.setStretch(11, 5)

        self.verticalLayout.addWidget(self.M_line_5)

        self.M_line_6 = QFrame(self.Main_Area)
        self.M_line_6.setObjectName(u"M_line_6")
        sizePolicy2.setHeightForWidth(self.M_line_6.sizePolicy().hasHeightForWidth())
        self.M_line_6.setSizePolicy(sizePolicy2)
        self.M_line_6.setMinimumSize(QSize(666, 0))
        self.M_line_6.setMaximumSize(QSize(666, 16777215))
        self.M_line_6.setFrameShape(QFrame.NoFrame)
        self.M_line_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.M_line_6)
        self.horizontalLayout_8.setSpacing(3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 1, 6, 1)
        self.key_ctrl_l = QPushButton(self.M_line_6)
        self.key_ctrl_l.setObjectName(u"key_ctrl_l")
        sizePolicy1.setHeightForWidth(self.key_ctrl_l.sizePolicy().hasHeightForWidth())
        self.key_ctrl_l.setSizePolicy(sizePolicy1)
        self.key_ctrl_l.setMinimumSize(QSize(64, 42))
        self.key_ctrl_l.setMaximumSize(QSize(64, 42))
        palette66 = QPalette()
        palette66.setBrush(QPalette.Active, QPalette.Button, brush)
        palette66.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette66.setBrush(QPalette.Active, QPalette.Base, brush)
        palette66.setBrush(QPalette.Active, QPalette.Window, brush)
        palette66.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette66.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette66.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette66.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette66.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette66.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette66.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette66.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_ctrl_l.setPalette(palette66)
        self.key_ctrl_l.setFont(font5)
        self.key_ctrl_l.setFocusPolicy(Qt.NoFocus)
        self.key_ctrl_l.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_ctrl_l.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_8.addWidget(self.key_ctrl_l)

        self.key_win = QPushButton(self.M_line_6)
        self.key_win.setObjectName(u"key_win")
        sizePolicy1.setHeightForWidth(self.key_win.sizePolicy().hasHeightForWidth())
        self.key_win.setSizePolicy(sizePolicy1)
        self.key_win.setMinimumSize(QSize(56, 42))
        self.key_win.setMaximumSize(QSize(56, 42))
        palette67 = QPalette()
        palette67.setBrush(QPalette.Active, QPalette.Button, brush)
        palette67.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette67.setBrush(QPalette.Active, QPalette.Base, brush)
        palette67.setBrush(QPalette.Active, QPalette.Window, brush)
        palette67.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette67.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette67.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette67.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette67.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette67.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette67.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette67.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_win.setPalette(palette67)
        self.key_win.setFont(font5)
        self.key_win.setFocusPolicy(Qt.NoFocus)
        self.key_win.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_win.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_8.addWidget(self.key_win)

        self.key_alt_l = QPushButton(self.M_line_6)
        self.key_alt_l.setObjectName(u"key_alt_l")
        sizePolicy1.setHeightForWidth(self.key_alt_l.sizePolicy().hasHeightForWidth())
        self.key_alt_l.setSizePolicy(sizePolicy1)
        self.key_alt_l.setMinimumSize(QSize(64, 42))
        self.key_alt_l.setMaximumSize(QSize(64, 42))
        palette68 = QPalette()
        palette68.setBrush(QPalette.Active, QPalette.Button, brush)
        palette68.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette68.setBrush(QPalette.Active, QPalette.Base, brush)
        palette68.setBrush(QPalette.Active, QPalette.Window, brush)
        palette68.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette68.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette68.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette68.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette68.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette68.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette68.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette68.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_alt_l.setPalette(palette68)
        self.key_alt_l.setFont(font5)
        self.key_alt_l.setFocusPolicy(Qt.NoFocus)
        self.key_alt_l.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_alt_l.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_8.addWidget(self.key_alt_l)

        self.key_space = QPushButton(self.M_line_6)
        self.key_space.setObjectName(u"key_space")
        sizePolicy1.setHeightForWidth(self.key_space.sizePolicy().hasHeightForWidth())
        self.key_space.setSizePolicy(sizePolicy1)
        self.key_space.setMinimumSize(QSize(276, 42))
        self.key_space.setMaximumSize(QSize(276, 42))
        palette69 = QPalette()
        palette69.setBrush(QPalette.Active, QPalette.Button, brush)
        palette69.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette69.setBrush(QPalette.Active, QPalette.Base, brush)
        palette69.setBrush(QPalette.Active, QPalette.Window, brush)
        palette69.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette69.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette69.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette69.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette69.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette69.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette69.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette69.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_space.setPalette(palette69)
        self.key_space.setFont(font5)
        self.key_space.setFocusPolicy(Qt.NoFocus)
        self.key_space.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_space.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_8.addWidget(self.key_space)

        self.key_alt_r = QPushButton(self.M_line_6)
        self.key_alt_r.setObjectName(u"key_alt_r")
        sizePolicy1.setHeightForWidth(self.key_alt_r.sizePolicy().hasHeightForWidth())
        self.key_alt_r.setSizePolicy(sizePolicy1)
        self.key_alt_r.setMinimumSize(QSize(64, 42))
        self.key_alt_r.setMaximumSize(QSize(64, 42))
        palette70 = QPalette()
        palette70.setBrush(QPalette.Active, QPalette.Button, brush)
        palette70.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette70.setBrush(QPalette.Active, QPalette.Base, brush)
        palette70.setBrush(QPalette.Active, QPalette.Window, brush)
        palette70.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette70.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette70.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette70.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette70.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette70.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette70.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette70.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_alt_r.setPalette(palette70)
        self.key_alt_r.setFont(font5)
        self.key_alt_r.setFocusPolicy(Qt.NoFocus)
        self.key_alt_r.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_alt_r.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_8.addWidget(self.key_alt_r)

        self.key_menu = QPushButton(self.M_line_6)
        self.key_menu.setObjectName(u"key_menu")
        sizePolicy1.setHeightForWidth(self.key_menu.sizePolicy().hasHeightForWidth())
        self.key_menu.setSizePolicy(sizePolicy1)
        self.key_menu.setMinimumSize(QSize(56, 42))
        self.key_menu.setMaximumSize(QSize(48, 42))
        palette71 = QPalette()
        palette71.setBrush(QPalette.Active, QPalette.Button, brush)
        palette71.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette71.setBrush(QPalette.Active, QPalette.Base, brush)
        palette71.setBrush(QPalette.Active, QPalette.Window, brush)
        palette71.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette71.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette71.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette71.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette71.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette71.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette71.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette71.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_menu.setPalette(palette71)
        self.key_menu.setFont(font5)
        self.key_menu.setFocusPolicy(Qt.NoFocus)
        self.key_menu.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_menu.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_8.addWidget(self.key_menu)

        self.key_ctrl_r = QPushButton(self.M_line_6)
        self.key_ctrl_r.setObjectName(u"key_ctrl_r")
        sizePolicy1.setHeightForWidth(self.key_ctrl_r.sizePolicy().hasHeightForWidth())
        self.key_ctrl_r.setSizePolicy(sizePolicy1)
        self.key_ctrl_r.setMinimumSize(QSize(64, 42))
        self.key_ctrl_r.setMaximumSize(QSize(64, 42))
        palette72 = QPalette()
        palette72.setBrush(QPalette.Active, QPalette.Button, brush)
        palette72.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette72.setBrush(QPalette.Active, QPalette.Base, brush)
        palette72.setBrush(QPalette.Active, QPalette.Window, brush)
        palette72.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette72.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette72.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette72.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette72.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette72.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette72.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette72.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_ctrl_r.setPalette(palette72)
        self.key_ctrl_r.setFont(font5)
        self.key_ctrl_r.setFocusPolicy(Qt.NoFocus)
        self.key_ctrl_r.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_ctrl_r.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_8.addWidget(self.key_ctrl_r)

        self.horizontalLayout_8.setStretch(0, 4)
        self.horizontalLayout_8.setStretch(1, 3)
        self.horizontalLayout_8.setStretch(2, 4)
        self.horizontalLayout_8.setStretch(3, 15)
        self.horizontalLayout_8.setStretch(4, 4)
        self.horizontalLayout_8.setStretch(5, 3)
        self.horizontalLayout_8.setStretch(6, 4)

        self.verticalLayout.addWidget(self.M_line_6)

        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(1, 4)
        self.verticalLayout.setStretch(2, 4)
        self.verticalLayout.setStretch(3, 4)
        self.verticalLayout.setStretch(4, 4)
        self.verticalLayout.setStretch(5, 4)

        self.horizontalLayout.addWidget(self.Main_Area)

        self.Middle_Area = QFrame(self.frame_keyboard)
        self.Middle_Area.setObjectName(u"Middle_Area")
        sizePolicy2.setHeightForWidth(self.Middle_Area.sizePolicy().hasHeightForWidth())
        self.Middle_Area.setSizePolicy(sizePolicy2)
        self.Middle_Area.setMinimumSize(QSize(150, 300))
        self.Middle_Area.setMaximumSize(QSize(150, 300))
        self.Middle_Area.setFrameShape(QFrame.NoFrame)
        self.Middle_Area.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Middle_Area)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 8, 0, 8)
        self.Mid_line_1 = QFrame(self.Middle_Area)
        self.Mid_line_1.setObjectName(u"Mid_line_1")
        self.Mid_line_1.setFrameShape(QFrame.NoFrame)
        self.Mid_line_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Mid_line_1)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.key_prtsc = QPushButton(self.Mid_line_1)
        self.key_prtsc.setObjectName(u"key_prtsc")
        sizePolicy1.setHeightForWidth(self.key_prtsc.sizePolicy().hasHeightForWidth())
        self.key_prtsc.setSizePolicy(sizePolicy1)
        self.key_prtsc.setMinimumSize(QSize(42, 42))
        self.key_prtsc.setMaximumSize(QSize(42, 42))
        palette73 = QPalette()
        palette73.setBrush(QPalette.Active, QPalette.Button, brush)
        palette73.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette73.setBrush(QPalette.Active, QPalette.Base, brush)
        palette73.setBrush(QPalette.Active, QPalette.Window, brush)
        palette73.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette73.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette73.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette73.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette73.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette73.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette73.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette73.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_prtsc.setPalette(palette73)
        self.key_prtsc.setFont(font5)
        self.key_prtsc.setFocusPolicy(Qt.NoFocus)
        self.key_prtsc.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_prtsc.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_2.addWidget(self.key_prtsc)

        self.key_scrlk = QPushButton(self.Mid_line_1)
        self.key_scrlk.setObjectName(u"key_scrlk")
        sizePolicy1.setHeightForWidth(self.key_scrlk.sizePolicy().hasHeightForWidth())
        self.key_scrlk.setSizePolicy(sizePolicy1)
        self.key_scrlk.setMinimumSize(QSize(42, 42))
        self.key_scrlk.setMaximumSize(QSize(42, 42))
        palette74 = QPalette()
        palette74.setBrush(QPalette.Active, QPalette.Button, brush)
        palette74.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette74.setBrush(QPalette.Active, QPalette.Base, brush)
        palette74.setBrush(QPalette.Active, QPalette.Window, brush)
        palette74.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette74.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette74.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette74.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette74.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette74.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette74.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette74.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_scrlk.setPalette(palette74)
        self.key_scrlk.setFont(font5)
        self.key_scrlk.setFocusPolicy(Qt.NoFocus)
        self.key_scrlk.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_scrlk.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_2.addWidget(self.key_scrlk)

        self.key_pause = QPushButton(self.Mid_line_1)
        self.key_pause.setObjectName(u"key_pause")
        sizePolicy1.setHeightForWidth(self.key_pause.sizePolicy().hasHeightForWidth())
        self.key_pause.setSizePolicy(sizePolicy1)
        self.key_pause.setMinimumSize(QSize(42, 42))
        self.key_pause.setMaximumSize(QSize(42, 42))
        palette75 = QPalette()
        palette75.setBrush(QPalette.Active, QPalette.Button, brush)
        palette75.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette75.setBrush(QPalette.Active, QPalette.Base, brush)
        palette75.setBrush(QPalette.Active, QPalette.Window, brush)
        palette75.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette75.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette75.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette75.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette75.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette75.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette75.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette75.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_pause.setPalette(palette75)
        self.key_pause.setFont(font5)
        self.key_pause.setFocusPolicy(Qt.NoFocus)
        self.key_pause.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_pause.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_2.addWidget(self.key_pause)


        self.verticalLayout_2.addWidget(self.Mid_line_1)

        self.Mid_line_2 = QFrame(self.Middle_Area)
        self.Mid_line_2.setObjectName(u"Mid_line_2")
        self.Mid_line_2.setFrameShape(QFrame.NoFrame)
        self.Mid_line_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.Mid_line_2)
        self.horizontalLayout_9.setSpacing(3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(1, 1, 1, 1)
        self.key_insert = QPushButton(self.Mid_line_2)
        self.key_insert.setObjectName(u"key_insert")
        sizePolicy1.setHeightForWidth(self.key_insert.sizePolicy().hasHeightForWidth())
        self.key_insert.setSizePolicy(sizePolicy1)
        self.key_insert.setMinimumSize(QSize(42, 42))
        self.key_insert.setMaximumSize(QSize(42, 42))
        palette76 = QPalette()
        palette76.setBrush(QPalette.Active, QPalette.Button, brush)
        palette76.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette76.setBrush(QPalette.Active, QPalette.Base, brush)
        palette76.setBrush(QPalette.Active, QPalette.Window, brush)
        palette76.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette76.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette76.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette76.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette76.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette76.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette76.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette76.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_insert.setPalette(palette76)
        self.key_insert.setFont(font5)
        self.key_insert.setFocusPolicy(Qt.NoFocus)
        self.key_insert.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_insert.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_9.addWidget(self.key_insert)

        self.key_home = QPushButton(self.Mid_line_2)
        self.key_home.setObjectName(u"key_home")
        sizePolicy1.setHeightForWidth(self.key_home.sizePolicy().hasHeightForWidth())
        self.key_home.setSizePolicy(sizePolicy1)
        self.key_home.setMinimumSize(QSize(42, 42))
        self.key_home.setMaximumSize(QSize(42, 42))
        palette77 = QPalette()
        palette77.setBrush(QPalette.Active, QPalette.Button, brush)
        palette77.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette77.setBrush(QPalette.Active, QPalette.Base, brush)
        palette77.setBrush(QPalette.Active, QPalette.Window, brush)
        palette77.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette77.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette77.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette77.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette77.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette77.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette77.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette77.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_home.setPalette(palette77)
        self.key_home.setFont(font5)
        self.key_home.setFocusPolicy(Qt.NoFocus)
        self.key_home.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_home.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_9.addWidget(self.key_home)

        self.key_pageup = QPushButton(self.Mid_line_2)
        self.key_pageup.setObjectName(u"key_pageup")
        sizePolicy1.setHeightForWidth(self.key_pageup.sizePolicy().hasHeightForWidth())
        self.key_pageup.setSizePolicy(sizePolicy1)
        self.key_pageup.setMinimumSize(QSize(42, 42))
        self.key_pageup.setMaximumSize(QSize(42, 42))
        palette78 = QPalette()
        palette78.setBrush(QPalette.Active, QPalette.Button, brush)
        palette78.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette78.setBrush(QPalette.Active, QPalette.Base, brush)
        palette78.setBrush(QPalette.Active, QPalette.Window, brush)
        palette78.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette78.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette78.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette78.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette78.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette78.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette78.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette78.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_pageup.setPalette(palette78)
        self.key_pageup.setFont(font5)
        self.key_pageup.setFocusPolicy(Qt.NoFocus)
        self.key_pageup.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_pageup.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_9.addWidget(self.key_pageup)


        self.verticalLayout_2.addWidget(self.Mid_line_2)

        self.Mid_line_3 = QFrame(self.Middle_Area)
        self.Mid_line_3.setObjectName(u"Mid_line_3")
        self.Mid_line_3.setFrameShape(QFrame.NoFrame)
        self.Mid_line_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.Mid_line_3)
        self.horizontalLayout_11.setSpacing(3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(1, 1, 1, 1)
        self.key_delete = QPushButton(self.Mid_line_3)
        self.key_delete.setObjectName(u"key_delete")
        sizePolicy1.setHeightForWidth(self.key_delete.sizePolicy().hasHeightForWidth())
        self.key_delete.setSizePolicy(sizePolicy1)
        self.key_delete.setMinimumSize(QSize(42, 42))
        self.key_delete.setMaximumSize(QSize(42, 42))
        palette79 = QPalette()
        palette79.setBrush(QPalette.Active, QPalette.Button, brush)
        palette79.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette79.setBrush(QPalette.Active, QPalette.Base, brush)
        palette79.setBrush(QPalette.Active, QPalette.Window, brush)
        palette79.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette79.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette79.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette79.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette79.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette79.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette79.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette79.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_delete.setPalette(palette79)
        self.key_delete.setFont(font5)
        self.key_delete.setFocusPolicy(Qt.NoFocus)
        self.key_delete.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_delete.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_11.addWidget(self.key_delete)

        self.key_end = QPushButton(self.Mid_line_3)
        self.key_end.setObjectName(u"key_end")
        sizePolicy1.setHeightForWidth(self.key_end.sizePolicy().hasHeightForWidth())
        self.key_end.setSizePolicy(sizePolicy1)
        self.key_end.setMinimumSize(QSize(42, 42))
        self.key_end.setMaximumSize(QSize(42, 42))
        palette80 = QPalette()
        palette80.setBrush(QPalette.Active, QPalette.Button, brush)
        palette80.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette80.setBrush(QPalette.Active, QPalette.Base, brush)
        palette80.setBrush(QPalette.Active, QPalette.Window, brush)
        palette80.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette80.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette80.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette80.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette80.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette80.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette80.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette80.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_end.setPalette(palette80)
        self.key_end.setFont(font5)
        self.key_end.setFocusPolicy(Qt.NoFocus)
        self.key_end.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_end.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_11.addWidget(self.key_end)

        self.key_pagedown = QPushButton(self.Mid_line_3)
        self.key_pagedown.setObjectName(u"key_pagedown")
        sizePolicy1.setHeightForWidth(self.key_pagedown.sizePolicy().hasHeightForWidth())
        self.key_pagedown.setSizePolicy(sizePolicy1)
        self.key_pagedown.setMinimumSize(QSize(42, 42))
        self.key_pagedown.setMaximumSize(QSize(42, 42))
        palette81 = QPalette()
        palette81.setBrush(QPalette.Active, QPalette.Button, brush)
        palette81.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette81.setBrush(QPalette.Active, QPalette.Base, brush)
        palette81.setBrush(QPalette.Active, QPalette.Window, brush)
        palette81.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette81.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette81.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette81.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette81.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette81.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette81.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette81.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_pagedown.setPalette(palette81)
        self.key_pagedown.setFont(font5)
        self.key_pagedown.setFocusPolicy(Qt.NoFocus)
        self.key_pagedown.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_pagedown.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_11.addWidget(self.key_pagedown)


        self.verticalLayout_2.addWidget(self.Mid_line_3)

        self.Mid_line_4 = QFrame(self.Middle_Area)
        self.Mid_line_4.setObjectName(u"Mid_line_4")
        self.Mid_line_4.setFrameShape(QFrame.NoFrame)
        self.Mid_line_4.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.Mid_line_4)

        self.Mid_line_5 = QFrame(self.Middle_Area)
        self.Mid_line_5.setObjectName(u"Mid_line_5")
        self.Mid_line_5.setFrameShape(QFrame.NoFrame)
        self.Mid_line_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.Mid_line_5)
        self.horizontalLayout_12.setSpacing(3)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(1, 1, 1, 1)
        self.key_up = QPushButton(self.Mid_line_5)
        self.key_up.setObjectName(u"key_up")
        sizePolicy1.setHeightForWidth(self.key_up.sizePolicy().hasHeightForWidth())
        self.key_up.setSizePolicy(sizePolicy1)
        self.key_up.setMinimumSize(QSize(42, 42))
        self.key_up.setMaximumSize(QSize(42, 42))
        palette82 = QPalette()
        palette82.setBrush(QPalette.Active, QPalette.Button, brush)
        palette82.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette82.setBrush(QPalette.Active, QPalette.Base, brush)
        palette82.setBrush(QPalette.Active, QPalette.Window, brush)
        palette82.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette82.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette82.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette82.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette82.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette82.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette82.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette82.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_up.setPalette(palette82)
        self.key_up.setFont(font5)
        self.key_up.setFocusPolicy(Qt.NoFocus)
        self.key_up.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_up.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_12.addWidget(self.key_up)


        self.verticalLayout_2.addWidget(self.Mid_line_5)

        self.Mid_line_6 = QFrame(self.Middle_Area)
        self.Mid_line_6.setObjectName(u"Mid_line_6")
        self.Mid_line_6.setFrameShape(QFrame.NoFrame)
        self.Mid_line_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.Mid_line_6)
        self.horizontalLayout_13.setSpacing(3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(1, 1, 1, 1)
        self.key_left = QPushButton(self.Mid_line_6)
        self.key_left.setObjectName(u"key_left")
        sizePolicy1.setHeightForWidth(self.key_left.sizePolicy().hasHeightForWidth())
        self.key_left.setSizePolicy(sizePolicy1)
        self.key_left.setMinimumSize(QSize(42, 42))
        self.key_left.setMaximumSize(QSize(42, 42))
        palette83 = QPalette()
        palette83.setBrush(QPalette.Active, QPalette.Button, brush)
        palette83.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette83.setBrush(QPalette.Active, QPalette.Base, brush)
        palette83.setBrush(QPalette.Active, QPalette.Window, brush)
        palette83.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette83.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette83.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette83.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette83.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette83.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette83.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette83.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_left.setPalette(palette83)
        self.key_left.setFont(font5)
        self.key_left.setFocusPolicy(Qt.NoFocus)
        self.key_left.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_left.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_13.addWidget(self.key_left)

        self.key_down = QPushButton(self.Mid_line_6)
        self.key_down.setObjectName(u"key_down")
        sizePolicy1.setHeightForWidth(self.key_down.sizePolicy().hasHeightForWidth())
        self.key_down.setSizePolicy(sizePolicy1)
        self.key_down.setMinimumSize(QSize(42, 42))
        self.key_down.setMaximumSize(QSize(42, 42))
        palette84 = QPalette()
        palette84.setBrush(QPalette.Active, QPalette.Button, brush)
        palette84.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette84.setBrush(QPalette.Active, QPalette.Base, brush)
        palette84.setBrush(QPalette.Active, QPalette.Window, brush)
        palette84.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette84.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette84.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette84.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette84.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette84.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette84.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette84.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_down.setPalette(palette84)
        self.key_down.setFont(font5)
        self.key_down.setFocusPolicy(Qt.NoFocus)
        self.key_down.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_down.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_13.addWidget(self.key_down)

        self.key_right = QPushButton(self.Mid_line_6)
        self.key_right.setObjectName(u"key_right")
        sizePolicy1.setHeightForWidth(self.key_right.sizePolicy().hasHeightForWidth())
        self.key_right.setSizePolicy(sizePolicy1)
        self.key_right.setMinimumSize(QSize(42, 42))
        self.key_right.setMaximumSize(QSize(42, 42))
        palette85 = QPalette()
        palette85.setBrush(QPalette.Active, QPalette.Button, brush)
        palette85.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette85.setBrush(QPalette.Active, QPalette.Base, brush)
        palette85.setBrush(QPalette.Active, QPalette.Window, brush)
        palette85.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette85.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette85.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette85.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette85.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette85.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette85.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette85.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.key_right.setPalette(palette85)
        self.key_right.setFont(font5)
        self.key_right.setFocusPolicy(Qt.NoFocus)
        self.key_right.setContextMenuPolicy(Qt.CustomContextMenu)
        self.key_right.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_13.addWidget(self.key_right)


        self.verticalLayout_2.addWidget(self.Mid_line_6)

        self.verticalLayout_2.setStretch(0, 5)
        self.verticalLayout_2.setStretch(1, 4)
        self.verticalLayout_2.setStretch(2, 4)
        self.verticalLayout_2.setStretch(3, 4)
        self.verticalLayout_2.setStretch(4, 4)
        self.verticalLayout_2.setStretch(5, 4)

        self.horizontalLayout.addWidget(self.Middle_Area)

        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_3.addWidget(self.frame_keyboard)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_essay_title.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_time.setText(QCoreApplication.translate("Form", u"00:00:00", None))
        self.label_speed.setText(QCoreApplication.translate("Form", u"Speed:", None))
        self.label_accuracy.setText(QCoreApplication.translate("Form", u"Accuracy:", None))
        self.btn_close.setText("")
        self.label_line1.setText(QCoreApplication.translate("Form", u"Label1", None))
        self.label_line2.setText(QCoreApplication.translate("Form", u"Label3", None))
        self.label_line3.setText(QCoreApplication.translate("Form", u"Label5", None))
        self.lineEdit_input.setPlaceholderText("")
        self.key_esc.setText(QCoreApplication.translate("Form", u"Esc", None))
        self.key_F1.setText(QCoreApplication.translate("Form", u"F1", None))
        self.key_F2.setText(QCoreApplication.translate("Form", u"F2", None))
        self.key_F3.setText(QCoreApplication.translate("Form", u"F3", None))
        self.key_F4.setText(QCoreApplication.translate("Form", u"F4", None))
        self.key_F5.setText(QCoreApplication.translate("Form", u"F5", None))
        self.key_F6.setText(QCoreApplication.translate("Form", u"F6", None))
        self.key_F7.setText(QCoreApplication.translate("Form", u"F7", None))
        self.key_F8.setText(QCoreApplication.translate("Form", u"F8", None))
        self.key_F9.setText(QCoreApplication.translate("Form", u"F9", None))
        self.key_F10.setText(QCoreApplication.translate("Form", u"F10", None))
        self.key_F11.setText(QCoreApplication.translate("Form", u"F11", None))
        self.key_F12.setText(QCoreApplication.translate("Form", u"F12", None))
        self.key_backquote.setText(QCoreApplication.translate("Form", u"` ~", None))
        self.key_1.setText(QCoreApplication.translate("Form", u"1 !", None))
        self.key_2.setText(QCoreApplication.translate("Form", u"2 @", None))
        self.key_3.setText(QCoreApplication.translate("Form", u"3 #", None))
        self.key_4.setText(QCoreApplication.translate("Form", u"4 $", None))
        self.key_5.setText(QCoreApplication.translate("Form", u"5 %", None))
        self.key_6.setText(QCoreApplication.translate("Form", u"6 ^", None))
        self.key_7.setText(QCoreApplication.translate("Form", u"7 &&", None))
        self.key_8.setText(QCoreApplication.translate("Form", u"8 *", None))
        self.key_9.setText(QCoreApplication.translate("Form", u"9 (", None))
        self.key_0.setText(QCoreApplication.translate("Form", u"0 )", None))
        self.key_minus.setText(QCoreApplication.translate("Form", u"- _", None))
        self.key_equal.setText(QCoreApplication.translate("Form", u"= +", None))
        self.key_backspace.setText(QCoreApplication.translate("Form", u"Back\n"
"Space", None))
        self.key_tab.setText(QCoreApplication.translate("Form", u"Tab", None))
        self.key_q.setText(QCoreApplication.translate("Form", u"Q", None))
        self.key_w.setText(QCoreApplication.translate("Form", u"W", None))
        self.key_e.setText(QCoreApplication.translate("Form", u"E", None))
        self.key_r.setText(QCoreApplication.translate("Form", u"R", None))
        self.key_t.setText(QCoreApplication.translate("Form", u"T", None))
        self.key_y.setText(QCoreApplication.translate("Form", u"Y", None))
        self.key_u.setText(QCoreApplication.translate("Form", u"U", None))
        self.key_i.setText(QCoreApplication.translate("Form", u"I", None))
        self.key_o.setText(QCoreApplication.translate("Form", u"O", None))
        self.key_p.setText(QCoreApplication.translate("Form", u"P", None))
        self.key_bracketleft.setText(QCoreApplication.translate("Form", u"[ {", None))
        self.key_bracketright.setText(QCoreApplication.translate("Form", u"] }", None))
        self.key_backslash.setText(QCoreApplication.translate("Form", u"\\ |", None))
        self.key_capslock.setText(QCoreApplication.translate("Form", u"Caps\n"
"Lodk", None))
        self.key_a.setText(QCoreApplication.translate("Form", u"A", None))
        self.key_s.setText(QCoreApplication.translate("Form", u"S", None))
        self.key_d.setText(QCoreApplication.translate("Form", u"D", None))
        self.key_f.setText(QCoreApplication.translate("Form", u"F", None))
        self.key_g.setText(QCoreApplication.translate("Form", u"G", None))
        self.key_h.setText(QCoreApplication.translate("Form", u"H", None))
        self.key_j.setText(QCoreApplication.translate("Form", u"J", None))
        self.key_k.setText(QCoreApplication.translate("Form", u"K", None))
        self.key_l.setText(QCoreApplication.translate("Form", u"L", None))
        self.key_semicolon.setText(QCoreApplication.translate("Form", u"; :", None))
        self.key_quote.setText(QCoreApplication.translate("Form", u"' \"", None))
        self.key_enter.setText(QCoreApplication.translate("Form", u"Enter", None))
        self.key_shift_l.setText(QCoreApplication.translate("Form", u"Shift", None))
        self.key_z.setText(QCoreApplication.translate("Form", u"Z", None))
        self.key_x.setText(QCoreApplication.translate("Form", u"X", None))
        self.key_c.setText(QCoreApplication.translate("Form", u"C", None))
        self.key_v.setText(QCoreApplication.translate("Form", u"V", None))
        self.key_b.setText(QCoreApplication.translate("Form", u"B", None))
        self.key_n.setText(QCoreApplication.translate("Form", u"N", None))
        self.key_m.setText(QCoreApplication.translate("Form", u"M", None))
        self.key_comma.setText(QCoreApplication.translate("Form", u", <", None))
        self.key_period.setText(QCoreApplication.translate("Form", u". >", None))
        self.key_slash.setText(QCoreApplication.translate("Form", u"/ ?", None))
        self.key_shift_r.setText(QCoreApplication.translate("Form", u"Shift", None))
        self.key_ctrl_l.setText(QCoreApplication.translate("Form", u"Ctrl", None))
        self.key_win.setText(QCoreApplication.translate("Form", u"Win", None))
        self.key_alt_l.setText(QCoreApplication.translate("Form", u"Alt", None))
        self.key_space.setText(QCoreApplication.translate("Form", u"Space", None))
        self.key_alt_r.setText(QCoreApplication.translate("Form", u"Alt", None))
        self.key_menu.setText(QCoreApplication.translate("Form", u"Menu", None))
        self.key_ctrl_r.setText(QCoreApplication.translate("Form", u"Ctrl", None))
        self.key_prtsc.setText(QCoreApplication.translate("Form", u"PrtSc", None))
        self.key_scrlk.setText(QCoreApplication.translate("Form", u"ScrLk", None))
        self.key_pause.setText(QCoreApplication.translate("Form", u"Pause", None))
        self.key_insert.setText(QCoreApplication.translate("Form", u"Ins", None))
        self.key_home.setText(QCoreApplication.translate("Form", u"Home", None))
        self.key_pageup.setText(QCoreApplication.translate("Form", u"PgUp", None))
        self.key_delete.setText(QCoreApplication.translate("Form", u"Del", None))
        self.key_end.setText(QCoreApplication.translate("Form", u"End", None))
        self.key_pagedown.setText(QCoreApplication.translate("Form", u"PgDn", None))
        self.key_up.setText(QCoreApplication.translate("Form", u"\u2191", None))
        self.key_left.setText(QCoreApplication.translate("Form", u"\u2190", None))
        self.key_down.setText(QCoreApplication.translate("Form", u"\u2193", None))
        self.key_right.setText(QCoreApplication.translate("Form", u"\u2192", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_create.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(350, 441)
        Form.setMinimumSize(QSize(350, 400))
        Form.setMaximumSize(QSize(350000, 40000))
        Form.setStyleSheet(u"QWidget {\n"
"    background-color: #2C2F33;\n"
"    color: #FFFFFF;\n"
"}\n"
"QPushButton {\n"
"    border: 2px solid white;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px; \n"
"}\n"
"QPushButton:hover {\n"
"    background-color:#3A3D42; \n"
"}")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 351, 81))
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 180, 301, 21))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 300, 161, 61))
        font1 = QFont()
        font1.setPointSize(15)
        self.label_3.setFont(font1)
        self.start_date_2 = QDateEdit(Form)
        self.start_date_2.setObjectName(u"start_date_2")
        self.start_date_2.setGeometry(QRect(220, 320, 113, 24))
        self.start_date_2.setDateTime(QDateTime(QDate(2024, 12, 31), QTime(0, 0, 0)))
        self.start_date_2.setCalendarPopup(True)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(120, 390, 111, 31))
        self.error_label = QLabel(Form)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setGeometry(QRect(40, 360, 281, 21))
        self.error_label.setStyleSheet(u"color: red")
        self.error_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(30, 140, 301, 21))
        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(30, 100, 301, 21))
        self.lineEdit_4 = QLineEdit(Form)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(30, 220, 301, 21))
        self.lineEdit_5 = QLineEdit(Form)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(30, 260, 301, 21))
        self.lineEdit_5.setEchoMode(QLineEdit.EchoMode.Password)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0414\u0435\u043d\u044c \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.start_date_2.setDisplayFormat(QCoreApplication.translate("Form", u"d/M/yyyy", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.error_label.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Form", u"\u041f\u043e\u0447\u0442\u0430", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Form", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("Form", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
    # retranslateUi


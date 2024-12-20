# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'secrion_create.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(350, 240)
        Form.setMinimumSize(QSize(350, 240))
        Form.setMaximumSize(QSize(350, 240))
        Form.setStyleSheet(u"QWidget {\n"
"    background-color: #2C2F33;\n"
"    color: #FFFFFF;\n"
"}\n"
"QPushButton {\n"
"    border: 2px solid white;\n"
"    border-radius: 5px; \n"
"    padding: 5px 10px; \n"
"}\n"
"QPushButton:hover {\n"
"    background-color:#3A3D42;\n"
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
        self.lineEdit.setGeometry(QRect(30, 90, 301, 21))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(120, 170, 111, 31))
        self.error_label = QLabel(Form)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setGeometry(QRect(40, 210, 281, 21))
        self.error_label.setStyleSheet(u"color: red")
        self.error_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(30, 120, 301, 21))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u044b\u0439 \u043e\u0442\u0434\u0435\u043b", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043e\u0442\u0434\u0435\u043b\u0430", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.error_label.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Form", u"\u0413\u043b\u0430\u0432\u0430 \u043e\u0442\u0434\u0435\u043b\u0430", None))
    # retranslateUi


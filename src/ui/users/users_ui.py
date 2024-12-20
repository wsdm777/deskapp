# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'users.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1080, 560)
        Dialog.setMinimumSize(QSize(1080, 560))
        Dialog.setMaximumSize(QSize(1080, 560))
        Dialog.setStyleSheet(u"QWidget {\n"
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
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 60, 311, 71))
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(18)
        self.label.setFont(font)
        self.countler = QLabel(Dialog)
        self.countler.setObjectName(u"countler")
        self.countler.setGeometry(QRect(350, 60, 121, 71))
        font1 = QFont()
        font1.setFamilies([u"Verdana"])
        font1.setPointSize(20)
        self.countler.setFont(font1)
        self.tableWidget = QTableWidget(Dialog)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 160, 1041, 391))
        self.main_window_button = QPushButton(Dialog)
        self.main_window_button.setObjectName(u"main_window_button")
        self.main_window_button.setGeometry(QRect(20, 10, 111, 51))
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        self.main_window_button.setFont(font2)
        self.main_window_button.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    color: darkblue;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:#2C2F33; \n"
"}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432", None))
        self.countler.setText("")
        self.main_window_button.setText(QCoreApplication.translate("Dialog", u"\u0413\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
    # retranslateUi


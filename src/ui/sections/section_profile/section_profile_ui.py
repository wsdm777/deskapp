# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'section_profile.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(900, 560)
        Dialog.setMinimumSize(QSize(900, 560))
        Dialog.setMaximumSize(QSize(900, 560))
        Dialog.setStyleSheet(u"QWidget {\n"
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
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 170, 321, 31))
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(18)
        self.label.setFont(font)
        self.countler = QLabel(Dialog)
        self.countler.setObjectName(u"countler")
        self.countler.setGeometry(QRect(350, 150, 61, 71))
        font1 = QFont()
        font1.setFamilies([u"Verdana"])
        font1.setPointSize(20)
        self.countler.setFont(font1)
        self.remove_section = QPushButton(Dialog)
        self.remove_section.setObjectName(u"remove_section")
        self.remove_section.setGeometry(QRect(750, 90, 141, 41))
        self.tableWidget = QTableWidget(Dialog)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 220, 861, 331))
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
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 110, 171, 41))
        self.label_3.setFont(font)
        self.new_head = QLineEdit(Dialog)
        self.new_head.setObjectName(u"new_head")
        self.new_head.setGeometry(QRect(510, 180, 231, 21))
        self.change_head = QPushButton(Dialog)
        self.change_head.setObjectName(u"change_head")
        self.change_head.setGeometry(QRect(750, 170, 141, 41))
        self.error_label = QLabel(Dialog)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setGeometry(QRect(510, 150, 231, 20))
        self.error_label.setStyleSheet(u"color: red")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(220, 110, 521, 41))
        self.label_2.setFont(font)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 60, 81, 41))
        self.label_4.setFont(font)
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(130, 60, 521, 41))
        self.label_5.setFont(font)
        self.add_position = QPushButton(Dialog)
        self.add_position.setObjectName(u"add_position")
        self.add_position.setGeometry(QRect(750, 20, 141, 41))
        self.new_position = QLineEdit(Dialog)
        self.new_position.setObjectName(u"new_position")
        self.new_position.setGeometry(QRect(510, 30, 231, 21))
        self.error_label_2 = QLabel(Dialog)
        self.error_label_2.setObjectName(u"error_label_2")
        self.error_label_2.setGeometry(QRect(540, 10, 191, 20))
        self.error_label_2.setStyleSheet(u"color: red")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0434\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u0435\u0439", None))
        self.countler.setText("")
        self.remove_section.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043e\u0442\u0434\u0435\u043b", None))
        self.main_window_button.setText(QCoreApplication.translate("Dialog", u"\u0413\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0413\u043b\u0430\u0432\u0430 \u043e\u0442\u0434\u0435\u043b\u0430", None))
        self.new_head.setText("")
        self.new_head.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0447\u0442\u0430 \u043d\u043e\u0432\u043e\u0433\u043e \u0433\u043b\u0430\u0432\u044b", None))
        self.change_head.setText(QCoreApplication.translate("Dialog", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0433\u043b\u0430\u0432\u0443", None))
        self.error_label.setText("")
        self.label_2.setText("")
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u0434\u0435\u043b", None))
        self.label_5.setText("")
        self.add_position.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0434\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.new_position.setText("")
        self.new_position.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0434\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u0438", None))
        self.error_label_2.setText("")
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_rew.ui'
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
        Form.resize(700, 350)
        Form.setMinimumSize(QSize(700, 350))
        Form.setMaximumSize(QSize(700, 350))
        Form.setStyleSheet(u"QWidget {\n"
"    background-color: #2C2F33;\n"
"    color: #FFFFFF;\n"
"}\n"
"QPushButton {\n"
"    border: 2px solid white;\n"
"	border-radius: 5px; /* \u0411\u0435\u043b\u0430\u044f \u043e\u0431\u0432\u043e\u0434\u043a\u0430 \u0448\u0438\u0440\u0438\u043d\u043e\u0439 2px */\n"
"    padding: 5px 10px;      /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:#3A3D42; /* \u0426\u0432\u0435\u0442 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}")
        self.sections = QPushButton(Form)
        self.sections.setObjectName(u"sections")
        self.sections.setGeometry(QRect(20, 210, 190, 81))
        self.vacations = QPushButton(Form)
        self.vacations.setObjectName(u"vacations")
        self.vacations.setGeometry(QRect(490, 210, 190, 81))
        self.users = QPushButton(Form)
        self.users.setObjectName(u"users")
        self.users.setGeometry(QRect(260, 210, 190, 81))
        self.userinfo = QLabel(Form)
        self.userinfo.setObjectName(u"userinfo")
        self.userinfo.setGeometry(QRect(30, 10, 511, 91))
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(20)
        self.userinfo.setFont(font)
        self.access_info = QLabel(Form)
        self.access_info.setObjectName(u"access_info")
        self.access_info.setGeometry(QRect(30, 70, 161, 61))
        font1 = QFont()
        font1.setFamilies([u"Verdana"])
        self.access_info.setFont(font1)
        self.profile_button = QPushButton(Form)
        self.profile_button.setObjectName(u"profile_button")
        self.profile_button.setGeometry(QRect(540, 310, 141, 31))
        self.user_find_line = QLineEdit(Form)
        self.user_find_line.setObjectName(u"user_find_line")
        self.user_find_line.setGeometry(QRect(420, 10, 181, 22))
        self.user_find_line.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(620, 10, 75, 24))
        self.error_found_user = QLabel(Form)
        self.error_found_user.setObjectName(u"error_found_user")
        self.error_found_user.setGeometry(QRect(420, 40, 231, 20))
        self.error_found_user.setStyleSheet(u"color: red;")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 10, 141, 21))
        self.label.setFont(font1)
        self.adduser = QPushButton(Form)
        self.adduser.setObjectName(u"adduser")
        self.adduser.setGeometry(QRect(20, 310, 161, 31))
        self.adduser_2 = QPushButton(Form)
        self.adduser_2.setObjectName(u"adduser_2")
        self.adduser_2.setGeometry(QRect(280, 310, 161, 31))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.sections.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u0434\u0435\u043b\u044b", None))
        self.vacations.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043f\u0443\u0441\u043a\u0430", None))
        self.users.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0438", None))
        self.userinfo.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.access_info.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.profile_button.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.user_find_line.setText("")
        self.user_find_line.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u043e\u0447\u0442\u0443 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.error_found_user.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0438\u0441\u043a \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430", None))
        self.adduser.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u043b\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.adduser_2.setText(QCoreApplication.translate("Form", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442 \u0431\u0430\u0437\u044b \u0434\u0430\u043d\u043d\u044b\u0445", None))
    # retranslateUi


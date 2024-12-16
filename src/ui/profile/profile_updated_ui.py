# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile_updated.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(700, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(500, 400))
        Dialog.setMaximumSize(QSize(700, 600))
        Dialog.setStyleSheet(u"QWidget {\n"
"    background-color: #2C2F33;\n"
"    color: #FFFFFF;\n"
"	font-family: \"Segoe UI\", Arial, sans-serif;\n"
"}\n"
"QLabel#label_3 {\n"
"    color: red;\n"
"    font-size: 10pt; /* \u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u043e: \u0437\u0430\u0434\u0430\u0451\u0442 \u0440\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    font-weight: bold; /* \u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u043e: \u0434\u0435\u043b\u0430\u0435\u0442 \u0442\u0435\u043a\u0441\u0442 \u0436\u0438\u0440\u043d\u044b\u043c */\n"
"}\n"
"\n"
"QLabel#profile_id {\n"
"    color: #ffffff;\n"
"    font-size: 24pt;\n"
"    font-weight: bold;\n"
"    margin-bottom: 10px;\n"
"}\n"
"QLabel {\n"
"    font-family: \"Vardana\";\n"
"    color: #e0e0e0;\n"
"    font-weight: normal;\n"
"}\n"
"\n"
"\n"
"QPushButton#pwd{\n"
"    background-color: #7289DA;\n"
"    color: #FFFFFF\n"
"    border-radius: 5px\n"
"    padding: 10px 20px;       \n"
"    font-si"
                        "ze: 16px;         \n"
"    font-weight: bold;       \n"
"}\n"
"\n"
"QPushButton#pwd:hover {\n"
"    background-color: #5B6EAE; \n"
"}\n"
"\n"
"QPushButton#pwd:pressed {\n"
"    background-color: #4E5E92; \n"
"}\n"
"")
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(90)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setContentsMargins(15, -1, -1, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    color: darkblue;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.pushButton, 0, Qt.AlignHCenter)


        self.formLayout.setLayout(1, QFormLayout.LabelRole, self.verticalLayout)

        self.profile_id = QLabel(Dialog)
        self.profile_id.setObjectName(u"profile_id")
        font1 = QFont()
        font1.setFamilies([u"Vardana"])
        font1.setPointSize(24)
        font1.setBold(True)
        self.profile_id.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.profile_id)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(3, QFormLayout.LabelRole, self.verticalSpacer)

        self.email = QLabel(Dialog)
        self.email.setObjectName(u"email")
        font2 = QFont()
        font2.setFamilies([u"Vardana"])
        font2.setPointSize(16)
        font2.setBold(False)
        self.email.setFont(font2)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.email)

        self.email_value = QLabel(Dialog)
        self.email_value.setObjectName(u"email_value")
        self.email_value.setFont(font2)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.email_value)

        self.surname = QLabel(Dialog)
        self.surname.setObjectName(u"surname")
        self.surname.setFont(font2)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.surname)

        self.surname_value = QLabel(Dialog)
        self.surname_value.setObjectName(u"surname_value")
        self.surname_value.setFont(font2)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.surname_value)

        self.name = QLabel(Dialog)
        self.name.setObjectName(u"name")
        self.name.setFont(font2)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.name)

        self.name_value = QLabel(Dialog)
        self.name_value.setObjectName(u"name_value")
        self.name_value.setFont(font2)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.name_value)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.label)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_3)


        self.verticalLayout_3.addLayout(self.formLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(50)
        self.formLayout_2.setVerticalSpacing(10)
        self.formLayout_2.setContentsMargins(15, 30, -1, 0)
        self.pos = QLabel(Dialog)
        self.pos.setObjectName(u"pos")
        font3 = QFont()
        font3.setFamilies([u"Vardana"])
        font3.setPointSize(14)
        font3.setBold(False)
        self.pos.setFont(font3)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.pos)

        self.button_section = QPushButton(Dialog)
        self.button_section.setObjectName(u"button_section")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.button_section.sizePolicy().hasHeightForWidth())
        self.button_section.setSizePolicy(sizePolicy1)
        self.button_section.setFont(font)
        self.button_section.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    color: darkblue;\n"
"}\n"
"")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.button_section)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.button_position = QPushButton(Dialog)
        self.button_position.setObjectName(u"button_position")
        sizePolicy1.setHeightForWidth(self.button_position.sizePolicy().hasHeightForWidth())
        self.button_position.setSizePolicy(sizePolicy1)
        self.button_position.setFont(font)
        self.button_position.setToolTipDuration(0)
        self.button_position.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    color: darkblue;\n"
"}\n"
"")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.button_position)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.bitrhday_value = QLabel(Dialog)
        self.bitrhday_value.setObjectName(u"bitrhday_value")
        self.bitrhday_value.setFont(font3)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.bitrhday_value)

        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_7)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.label_2)

        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_9)

        self.joined_at_value = QLabel(Dialog)
        self.joined_at_value.setObjectName(u"joined_at_value")
        self.joined_at_value.setFont(font3)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.joined_at_value)


        self.verticalLayout_3.addLayout(self.formLayout_2)

        self.verticalLayout_3.setStretch(0, 10)
        self.verticalLayout_3.setStretch(2, 15)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0413\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
        self.profile_id.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.email.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0447\u0442\u0430", None))
        self.email_value.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.surname.setText(QCoreApplication.translate("Dialog", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.surname_value.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.name.setText(QCoreApplication.translate("Dialog", u"\u0418\u043c\u044f", None))
        self.name_value.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label.setText("")
        self.label_3.setText("")
        self.pos.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u0434\u0435\u043b", None))
        self.button_section.setText(QCoreApplication.translate("Dialog", u"PushButton", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.button_position.setText(QCoreApplication.translate("Dialog", u"PushButton", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.bitrhday_value.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u0412 \u043e\u0442\u043f\u0443\u0441\u043a\u0435", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u0412 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438 \u0441", None))
        self.joined_at_value.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
    # retranslateUi


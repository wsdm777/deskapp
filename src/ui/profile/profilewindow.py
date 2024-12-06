# Form implementation generated from reading ui file 'profile.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 700)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(700, 600))
        Dialog.setMaximumSize(QtCore.QSize(1000, 700))
        Dialog.setStyleSheet(
            "QWidget {\n"
            "    background-color: #2C2F33;\n"
            "    color: #FFFFFF;\n"
            "}\n"
            "\n"
            "QLabel {\n"
            '    font-family: "Vardana";\n'
            "    color: #FFFFFF;\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton#pwd{\n"
            "    background-color: #7289DA;\n"
            "    color: #FFFFFF\n"
            "    border-radius: 5px\n"
            "    padding: 10px 20px;       \n"
            "    font-size: 16px;         \n"
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
            "\n"
            ""
        )
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(15, -1, -1, 0)
        self.formLayout.setHorizontalSpacing(90)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    color: white;\n"
            "}\n"
            "QPushButton:hover {\n"
            "    color: darkblue;\n"
            "}\n"
            ""
        )
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(
            self.pushButton,
            0,
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter,
        )
        self.formLayout.setLayout(
            1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.verticalLayout
        )
        self.profile_id = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setFamily("Vardana")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.profile_id.setFont(font)
        self.profile_id.setObjectName("profile_id")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.profile_id
        )
        spacerItem = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.formLayout.setItem(2, QtWidgets.QFormLayout.ItemRole.LabelRole, spacerItem)
        self.email = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setFamily("Vardana")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.email.setFont(font)
        self.email.setObjectName("email")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.email
        )
        self.email_value = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setFamily("Vardana")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.email_value.setFont(font)
        self.email_value.setObjectName("email_value")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.email_value
        )
        self.surname = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setFamily("Vardana")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.surname.setFont(font)
        self.surname.setObjectName("surname")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.surname
        )
        self.surname_value = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setFamily("Vardana")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.surname_value.setFont(font)
        self.surname_value.setObjectName("surname_value")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.surname_value
        )
        self.name = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setFamily("Vardana")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.formLayout.setWidget(
            5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.name
        )
        self.name_value = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setFamily("Vardana")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.name_value.setFont(font)
        self.name_value.setObjectName("name_value")
        self.formLayout.setWidget(
            5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.name_value
        )
        self.verticalLayout_3.addLayout(self.formLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setFamily("Vardana")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setContentsMargins(15, 30, -1, 0)
        self.formLayout_2.setHorizontalSpacing(50)
        self.formLayout_2.setVerticalSpacing(10)
        self.formLayout_2.setObjectName("formLayout_2")
        self.pos = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setFamily("Vardana")
        font.setPointSize(14)
        self.pos.setFont(font)
        self.pos.setObjectName("pos")
        self.formLayout_2.setWidget(
            0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.pos
        )
        self.button_section = QtWidgets.QPushButton(parent=Dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.button_section.sizePolicy().hasHeightForWidth()
        )
        self.button_section.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_section.setFont(font)
        self.button_section.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    color: white;\n"
            "}\n"
            "QPushButton:hover {\n"
            "    color: darkblue;\n"
            "}\n"
            ""
        )
        self.button_section.setObjectName("button_section")
        self.formLayout_2.setWidget(
            0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.button_section
        )
        self.label_5 = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setFamily("Vardana")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(
            1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5
        )
        self.button_position = QtWidgets.QPushButton(parent=Dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.button_position.sizePolicy().hasHeightForWidth()
        )
        self.button_position.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_position.setFont(font)
        self.button_position.setToolTipDuration(0)
        self.button_position.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    color: white;\n"
            "}\n"
            "QPushButton:hover {\n"
            "    color: darkblue;\n"
            "}\n"
            ""
        )
        self.button_position.setObjectName("button_position")
        self.formLayout_2.setWidget(
            1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.button_position
        )
        self.label_6 = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setFamily("Vardana")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(
            2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6
        )
        self.bitrhday_value = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setFamily("Vardana")
        font.setPointSize(14)
        self.bitrhday_value.setFont(font)
        self.bitrhday_value.setObjectName("bitrhday_value")
        self.formLayout_2.setWidget(
            2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.bitrhday_value
        )
        self.label_7 = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setFamily("Vardana")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(
            3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7
        )
        self.label_8 = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setFamily("Vardana")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(
            4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_8
        )
        self.last_payment_value = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setFamily("Vardana")
        font.setPointSize(14)
        self.last_payment_value.setFont(font)
        self.last_payment_value.setObjectName("last_payment_value")
        self.formLayout_2.setWidget(
            4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.last_payment_value
        )
        self.label_9 = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setFamily("Vardana")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(
            5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_9
        )
        self.joined_at_value = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setFamily("Vardana")
        font.setPointSize(14)
        self.joined_at_value.setFont(font)
        self.joined_at_value.setObjectName("joined_at_value")
        self.formLayout_2.setWidget(
            5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.joined_at_value
        )
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setFamily("Vardana")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(
            3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_2
        )
        self.verticalLayout_3.addLayout(self.formLayout_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pwd = QtWidgets.QPushButton(parent=Dialog)
        self.pwd.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pwd.sizePolicy().hasHeightForWidth())
        self.pwd.setSizePolicy(sizePolicy)
        self.pwd.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.pwd.setCheckable(False)
        self.pwd.setDefault(False)
        self.pwd.setFlat(False)
        self.pwd.setObjectName("pwd")
        self.verticalLayout_5.addWidget(self.pwd)
        self.verticalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_3.setStretch(0, 10)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 15)
        self.verticalLayout_3.setStretch(3, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Главное меню"))
        self.profile_id.setText(_translate("Dialog", "TextLabel"))
        self.email.setText(_translate("Dialog", "Почта"))
        self.email_value.setText(_translate("Dialog", "TextLabel"))
        self.surname.setText(_translate("Dialog", "Фамилия"))
        self.surname_value.setText(_translate("Dialog", "TextLabel"))
        self.name.setText(_translate("Dialog", "Имя"))
        self.name_value.setText(_translate("Dialog", "TextLabel"))
        self.label.setText(_translate("Dialog", "Дополнительная информация"))
        self.pos.setText(_translate("Dialog", "Отдел"))
        self.button_section.setText(_translate("Dialog", "PushButton"))
        self.label_5.setText(_translate("Dialog", "Должность"))
        self.button_position.setText(_translate("Dialog", "PushButton"))
        self.label_6.setText(_translate("Dialog", "Дата рождения"))
        self.bitrhday_value.setText(_translate("Dialog", "TextLabel"))
        self.label_7.setText(_translate("Dialog", "В отпуске"))
        self.label_8.setText(_translate("Dialog", "Последняя премия"))
        self.last_payment_value.setText(_translate("Dialog", "TextLabel"))
        self.label_9.setText(_translate("Dialog", "В компании с"))
        self.joined_at_value.setText(_translate("Dialog", "TextLabel"))
        self.label_2.setText(_translate("Dialog", "TextLabel"))
        self.pwd.setText(_translate("Dialog", "Смена пароля"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())

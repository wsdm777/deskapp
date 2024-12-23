# Form implementation generated from reading ui file 'user_create.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(350, 441)
        Form.setMinimumSize(QtCore.QSize(350, 400))
        Form.setMaximumSize(QtCore.QSize(350000, 40000))
        Form.setStyleSheet("QWidget {\n"
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
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 351, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(30, 180, 301, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(30, 300, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.start_date_2 = QtWidgets.QDateEdit(parent=Form)
        self.start_date_2.setGeometry(QtCore.QRect(220, 320, 113, 24))
        self.start_date_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2024, 12, 31), QtCore.QTime(0, 0, 0)))
        self.start_date_2.setCalendarPopup(True)
        self.start_date_2.setObjectName("start_date_2")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 390, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.error_label = QtWidgets.QLabel(parent=Form)
        self.error_label.setGeometry(QtCore.QRect(40, 360, 281, 21))
        self.error_label.setStyleSheet("color: red")
        self.error_label.setText("")
        self.error_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.error_label.setObjectName("error_label")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 140, 301, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 100, 301, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(30, 220, 301, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(30, 260, 301, 21))
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Создание пользователя"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Фамилия"))
        self.label_3.setText(_translate("Form", "День рождения"))
        self.start_date_2.setDisplayFormat(_translate("Form", "d/M/yyyy"))
        self.pushButton.setText(_translate("Form", "Создать"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Имя"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Почта"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "Должность"))
        self.lineEdit_5.setPlaceholderText(_translate("Form", "Пароль"))

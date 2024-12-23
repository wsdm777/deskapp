# Form implementation generated from reading ui file 'vacation_create_rew.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(350, 400)
        Form.setMinimumSize(QtCore.QSize(350, 400))
        Form.setMaximumSize(QtCore.QSize(350, 400))
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
        self.lineEdit.setGeometry(QtCore.QRect(30, 90, 301, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.start_date = QtWidgets.QDateEdit(parent=Form)
        self.start_date.setGeometry(QtCore.QRect(220, 130, 113, 24))
        self.start_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2025, 1, 1), QtCore.QTime(0, 0, 0)))
        self.start_date.setCalendarPopup(True)
        self.start_date.setObjectName("start_date")
        self.start_date_2 = QtWidgets.QDateEdit(parent=Form)
        self.start_date_2.setGeometry(QtCore.QRect(220, 170, 113, 24))
        self.start_date_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2025, 1, 1), QtCore.QTime(0, 0, 0)))
        self.start_date_2.setObjectName("start_date_2")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 320, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 210, 301, 101))
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.error_label = QtWidgets.QLabel(parent=Form)
        self.error_label.setGeometry(QtCore.QRect(40, 360, 281, 21))
        self.error_label.setStyleSheet("color: red")
        self.error_label.setText("")
        self.error_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.error_label.setObjectName("error_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Выдача отпуска"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Почта получателя"))
        self.label_2.setText(_translate("Form", "Дата начала"))
        self.label_3.setText(_translate("Form", "Дата окончания"))
        self.start_date.setDisplayFormat(_translate("Form", "d/M/yyyy"))
        self.start_date_2.setDisplayFormat(_translate("Form", "d/M/yyyy"))
        self.pushButton.setText(_translate("Form", "Создать"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Описание(необязательно)"))

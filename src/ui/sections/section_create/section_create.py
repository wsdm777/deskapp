# Form implementation generated from reading ui file 'secrion_create.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(350, 240)
        Form.setMinimumSize(QtCore.QSize(350, 240))
        Form.setMaximumSize(QtCore.QSize(350, 240))
        Form.setStyleSheet("QWidget {\n"
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
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 351, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(30, 90, 301, 21))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 170, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.error_label = QtWidgets.QLabel(parent=Form)
        self.error_label.setGeometry(QtCore.QRect(40, 210, 281, 21))
        self.error_label.setStyleSheet("color: red")
        self.error_label.setText("")
        self.error_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.error_label.setObjectName("error_label")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 120, 301, 21))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Новый отдел"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Название отдела"))
        self.pushButton.setText(_translate("Form", "Создать"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Глава отдела"))
# Form implementation generated from reading ui file 'vacations.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 450)
        Dialog.setMinimumSize(QtCore.QSize(600, 450))
        Dialog.setMaximumSize(QtCore.QSize(600, 450))
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(20, 0, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.countler = QtWidgets.QLabel(parent=Dialog)
        self.countler.setGeometry(QtCore.QRect(340, 0, 141, 71))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        self.countler.setFont(font)
        self.countler.setText("")
        self.countler.setObjectName("countler")
        self.vacations = QtWidgets.QListWidget(parent=Dialog)
        self.vacations.setGeometry(QtCore.QRect(20, 70, 561, 361))
        self.vacations.setObjectName("vacations")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Количество отпусков "))
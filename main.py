import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
from authwindow import Ui_Form as authForm
from repository import (
    APIClient,
)


class LoginForm(QWidget, authForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.api = APIClient("http://127.0.0.1:8000")
        self.pushButton.clicked.connect(self.on_login_clicked)

    def on_login_clicked(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        self.login(username, password)

    def login(self, username, password):
        try:
            self.api.login(username, password)
            res = self.api.me()
            print(res)
        except ValueError:
            self.show_error()

    def show_error(self):
        self.errorLabel.setText("Логин или пароль неверный")

    def closeEvent(self, event):
        self.api.close_session()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.jpg"))
    login_form = LoginForm()
    login_form.show()
    sys.exit(app.exec())

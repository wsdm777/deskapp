import sys
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QLabel,
)

from repository import (
    APIClient,
)


class LoginForm(QWidget):
    def __init__(self):
        super().__init__()

        self.api = APIClient("http://127.0.0.1:8000")

        self.setWindowTitle("Авторизация")
        self.setGeometry(100, 100, 300, 150)

        self.username_label = QLabel("Почта:")
        self.password_label = QLabel("Пароль:")

        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button = QPushButton("Войти")
        self.login_button.clicked.connect(self.on_login_clicked)

        form_layout = QVBoxLayout()
        form_layout.addWidget(self.username_label)
        form_layout.addWidget(self.username_input)
        form_layout.addWidget(self.password_label)
        form_layout.addWidget(self.password_input)
        form_layout.addWidget(self.login_button)

        self.setLayout(form_layout)

    def on_login_clicked(self):
        username = self.username_input.text()
        password = self.password_input.text()
        self.login(username, password)

    def login(self, username, password):
        self.api.login(username, password)
        res = self.api.me()
        print(res)

    def closeEvent(self, event):
        self.api.close_session()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.jpg"))
    login_form = LoginForm()
    login_form.show()
    sys.exit(app.exec())

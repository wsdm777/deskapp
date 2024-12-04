import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QStackedWidget,
    QMainWindow,
    QVBoxLayout,
)
from PyQt6.QtGui import QIcon
from ui.auth.authwindow import Ui_Form as authForm
from ui.profile.profilewindow import Ui_Dialog as profileForm
from repository import APIClient


class BaseWindow(QWidget):
    def __init__(self):
        self.id = None
        super().__init__()
        self.api = APIClient("http://127.0.0.1:8000")

    def closeEvent(self, event):
        print("Закрытие окна, завершение сессии API")
        self.api.close_session()
        event.accept()


class LoginForm(BaseWindow, authForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_login_clicked)

    def on_login_clicked(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        self.login(username, password)

    def login(self, username, password):
        try:
            self.api.login(username, password)
            self.hide()
            self.id = self.api.my_id()["id"]
            self.open_profile_window()
        except ValueError:
            self.show_error()

    def show_error(self):
        self.errorLabel.setText("Логин или пароль неверный")

    def open_profile_window(self):
        self.window = ProfileWindow(self.api, self.id)
        self.window.show()


class ProfileWindow(BaseWindow, profileForm):
    def __init__(self, api: APIClient, id):
        super().__init__()
        self.setupUi(self)
        data = api.get_info_by_id(id)
        self.email_value.setText(str(data["email"]))
        self.profile_id.setText(f"Пользователь {data["id"]}")
        self.name_value.setText(str(data["name"]))
        self.surname_value.setText(str(data["surname"]))
        self.bitrhday_value.setText(str(data["birthday"]))
        self.joined_at_value.setText(str(data["joined_at"]))
        self.last_payment_value.setText(str(data["last_bonus_payment"]))
        self.button_position.setText(str(data["position_name"]))
        self.button_section.setText(str(data["section_name"]))
        self.label_2.setText("Да" if data["is_on_vacation"] is True else "Нет")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.jpg"))
    login_form = LoginForm()
    login_form.show()
    sys.exit(app.exec())

# TODO button section in api
# TODO create is superuser
# TODO create upgrade user

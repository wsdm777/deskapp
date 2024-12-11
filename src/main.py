import asyncio
from multiprocessing import Value
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QStackedWidget,
    QMainWindow,
    QVBoxLayout,
)
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QIcon
from src.repository_file import Client
from src.ui.auth.authwindow import Ui_Form as authForm
from src.ui.profile.profilewindow import Ui_Dialog as profileForm
from qasync import QEventLoop, asyncSlot


class BaseWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.client = Client()

    def closeEvent(self, event):
        print("Закрытие окна, завершение сессии API")
        self.api.close_session()
        event.accept()


class LoginForm(BaseWindow, authForm):
    def __init__(self, loop=None):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_login_clicked)
        self.loop = loop or asyncio.get_event_loop()

    def on_login_clicked(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        asyncio.ensure_future(self.run_async_login(username, password))

    @asyncSlot()
    async def run_async_login(self, username, password):
        # Получаем или создаем цикл событий для асинхронной задачи
        loop = asyncio.get_event_loop()

        if loop.is_running():
            # Если цикл событий уже запущен, создаем задачу
            asyncio.create_task(self.login(username, password))
        else:
            # Если цикла нет, создаем новый
            loop.run_until_complete(self.login(username, password))

    async def login(self, username, password):
        try:
            res = await self.client.login(username, password)
            # self.hide()
        except ValueError:
            self.show_error()

    def show_error(self):
        self.errorLabel.setText("Логин или пароль неверный")

    # def open_profile_window(self):
    #     self.window = ProfileWindow(self.api, self.id)
    #     self.window.show()


# class ProfileWindow(BaseWindow, profileForm):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#         data = api.get_info_by_id(id)
#         self.email_value.setText(str(data["email"]))
#         self.profile_id.setText(f"Пользователь {data["id"]}")
#         self.name_value.setText(str(data["name"]))
#         self.surname_value.setText(str(data["surname"]))
#         self.bitrhday_value.setText(str(data["birthday"]))
#         self.joined_at_value.setText(str(data["joined_at"]))
#         self.last_payment_value.setText(str(data["last_bonus_payment"]))
#         self.button_position.setText(str(data["position_name"]))
#         self.button_section.setText(str(data["section_name"]))
#         self.label_2.setText("Да" if data["is_on_vacation"] is True else "Нет")


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     app.setWindowIcon(QIcon("icon.jpg"))
#     login_form = LoginForm()
#     login_form.show()
#     sys.exit(app.exec())

# TODO button section in api
# TODO create is superuser
# TODO create upgrade user


def main():
    app = QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    window = LoginForm(loop)
    window.show()

    with loop:
        loop.run_forever()


if __name__ == "__main__":
    main()

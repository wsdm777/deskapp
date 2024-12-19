import asyncio
from multiprocessing import Value
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QStackedWidget,
    QMainWindow,
    QVBoxLayout,
    QTableWidgetItem,
    QHeaderView,
)
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QIcon
from src.repository.crud.section.schemas import SectionCreate
from src.repository.crud.section.section import add_section, get_all_sections
from src.repository.crud.vacation.schemas import VacationCreate
from src.repository.crud.vacation.vacation import add_vacation, get_all_vacations
from src.repository_file import Client
from src.ui.auth.authwindow import Ui_Form as authForm
from src.ui.profile.profile_window_rew import Ui_Dialog as profileForm
from src.ui.main.main_window_rew import Ui_Form as mainForm
from src.ui.vacations.vacations_window_rew_upd import Ui_Dialog as vacationForm
from src.ui.sections.sections import Ui_Dialog as sectionForm
from src.ui.sections.section_create.section_create import Ui_Form as sectionCreateForm
from src.ui.vacations.vacation_create.vacation_create_rew import (
    Ui_Form as vacationCreateForm,
)
from qasync import QEventLoop, asyncSlot


class BaseWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.client = Client()


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

    async def run_async_login(self, username, password):
        loop = asyncio.get_event_loop()

        if loop.is_running():
            asyncio.create_task(self.login(username, password))
        else:
            loop.run_until_complete(self.login(username, password))

    async def login(self, username, password):
        try:
            await self.client.login(username, password)
            self.hide()
            self.open_profile_window(username)
        except ValueError:
            self.show_error()

    def show_error(self):
        self.errorLabel.setText("Логин или пароль неверный")

    def open_profile_window(self, username):
        self.window = ProfileWindow(self.client, username)
        self.window.show()


class ProfileWindow(BaseWindow, profileForm):
    def __init__(self, client, username, profile_username=None):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_main_clicked)
        self.client = client
        self.username = username
        asyncio.create_task(self.load_profile_data(profile_username))

    async def load_profile_data(self, user):
        # Получаем данные с сервера
        data, is_root = await self.client.get_page(user)
        if data == 0:
            raise ValueError
        if data.is_superuser is True:
            self.label_3.setText("Администратор")
        self.email_value.setText(str(data.email))
        self.profile_id.setText(f"Пользователь {data.id}")
        self.name_value.setText(str(data.name))
        self.surname_value.setText(str(data.surname))
        self.bitrhday_value.setText(str(data.birthday))
        self.joined_at_value.setText(str(data.joined_at))
        self.button_position.setText(str(data.position_name))
        self.button_section.setText(str(data.section_name))
        self.label_2.setText("Да" if data.is_on_vacation else "Нет")

        if is_root == False or data.email == self.username:
            self.pushButton_2.setVisible(False)
            self.pushButton_3.setVisible(False)
        elif data.is_superuser is True:
            self.pushButton_3.setVisible(False)

    def on_main_clicked(self):
        self.hide()
        self.window = MainWindow(self.client, self.username)
        self.window.show()


class MainWindow(BaseWindow, mainForm):
    def __init__(self, client, username):
        super().__init__()
        self.setupUi(self)
        self.client = client
        self.username = username
        self.sections.clicked.connect(self.on_sections_clicked)
        self.vacations.clicked.connect(self.on_vacation_clicked)
        self.pushButton.clicked.connect(self.on_find_clicked)
        self.profile_button.clicked.connect(self.on_profile_clicked)
        asyncio.create_task(self.load_main_window())

    async def load_main_window(self):
        data = await self.client.get_info_by_email()
        self.userinfo.setText(str(f"{data.name} {data.surname}"))
        if data.is_superuser == True:
            self.access_info.setText("Администратор")
            self.access_info.setStyleSheet("color: red;")
        else:
            self.access_info.setText("Пользователь")

    def on_sections_clicked(self):
        self.hide()
        self.window = SectionWindow(self.client, self.username)
        self.window.show()

    def on_profile_clicked(self):
        self.hide()
        self.window = ProfileWindow(self.client, self.username)
        self.window.show()

    def on_vacation_clicked(self):
        self.hide()
        self.window = VacationWindow(self.client, self.username)
        self.window.show()

    def on_find_clicked(self):
        asyncio.create_task(self.open_profile_user(self.user_find_line.text()))

    async def open_profile_user(self, username):
        result = await self.client.get_info_by_email(username)
        if result == 0:
            self.error_found_user.setText("Пользователь не найден")
        else:
            self.hide()
            self.window = ProfileWindow(self.client, self.username, username)
            self.window.show()


class VacationWindow(BaseWindow, vacationForm):
    def __init__(self, client, username):
        super().__init__()
        self.setupUi(self)
        self.client = client
        self.username = username
        self.vacation_button.clicked.connect(self.open_vacation_create)
        self.main_window_button.clicked.connect(self.open_main)
        asyncio.create_task(self.load_vacations())

    def open_vacation_create(self):
        self.window = VacationCreateForm(self.client, self.username)
        self.window.show()

    def open_main(self):
        self.hide()
        self.window = MainWindow(self.client, self.username)
        self.window.show()

    async def load_vacations(self):
        result = await get_all_vacations()
        if result != 0:
            self.countler.setText(str(len(result)))
            self.tableWidget.setRowCount(len(result))
            self.tableWidget.setColumnCount(8)
            self.tableWidget.setHorizontalHeaderLabels(
                [
                    "ID",
                    "Выдал",
                    "Получил",
                    "Дата выдачи",
                    "Дата начала",
                    "Дата окончания",
                    "Активно",
                    "Описание",
                ]
            )

            for i in range(len(result)):
                self.tableWidget.setItem(i, 0, QTableWidgetItem(str(result[i].id)))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(result[i].giver_email))
                self.tableWidget.setItem(
                    i, 2, QTableWidgetItem(result[i].receiver_email)
                )
                self.tableWidget.setItem(
                    i, 3, QTableWidgetItem(result[i].created_date.strftime("%d-%m-%Y"))
                )
                self.tableWidget.setItem(
                    i, 4, QTableWidgetItem(result[i].start_date.strftime("%d-%m-%Y"))
                )
                self.tableWidget.setItem(
                    i, 5, QTableWidgetItem(result[i].end_date.strftime("%d-%m-%Y"))
                )
                self.tableWidget.setItem(
                    i,
                    6,
                    QTableWidgetItem("Да" if result[i].is_active == True else "Нет"),
                )
                self.tableWidget.setItem(i, 7, QTableWidgetItem(result[i].description))


class VacationCreateForm(BaseWindow, vacationCreateForm):
    def __init__(self, client, username):
        super().__init__()
        self.setupUi(self)
        self.client = client
        self.username = username
        self.pushButton.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        asyncio.create_task(self.add_vacation())

    async def add_vacation(self):
        try:
            await add_vacation(
                VacationCreate(
                    giver_email=self.username,
                    receiver_email=self.lineEdit.text(),
                    start_date=self.start_date.date().toPyDate(),
                    end_date=self.start_date_2.date().toPyDate(),
                    description=self.lineEdit_2.text(),
                )
            )
            self.hide()
        except:
            self.error_label.setText("Введенные данные не корректны")


class SectionWindow(BaseWindow, sectionForm):
    def __init__(self, client, username):
        super().__init__()
        self.setupUi(self)
        self.client = client
        self.username = username
        self.tableWidget.itemClicked.connect(self.handle_item_click)
        self.vacation_button.clicked.connect(self.open_section_create)
        self.main_window_button.clicked.connect(self.open_main)
        asyncio.create_task(self.load_sections())

    def handle_item_click(self, item):
        column = item.column()
        if column == 1:
            section = item.text()
            self.on_department_name_clicked(section)

    def on_department_name_clicked(self, section_name): ...

    def open_section_create(self):
        ...
        self.window = SectionCreateForm(self.client, self.username)
        self.window.show()

    def open_main(self):
        self.hide()
        self.window = MainWindow(self.client, self.username)
        self.window.show()

    async def load_sections(self):
        result = await get_all_sections()
        if result != 0:
            self.countler.setText(str(len(result)))
            self.tableWidget.setRowCount(len(result))
            self.tableWidget.setColumnCount(3)
            self.tableWidget.setHorizontalHeaderLabels(
                ["ID", "Название", "Глава отдела"]
            )

            for i in range(len(result)):
                self.tableWidget.setItem(i, 0, QTableWidgetItem(str(result[i].id)))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(result[i].name))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(result[i].head_email))

            header = self.tableWidget.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            vertical_header = self.tableWidget.verticalHeader()
            vertical_header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)


class SectionCreateForm(BaseWindow, sectionCreateForm):
    def __init__(self, client, username):
        super().__init__()
        self.setupUi(self)
        self.client = client
        self.username = username
        self.pushButton.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        asyncio.create_task(self.add_section())

    async def add_section(self):
        print("dfwdfsdf")
        try:
            print(self.lineEdit.text())
            print()
            await add_section(
                SectionCreate(
                    name=self.lineEdit.text(), head_email=self.lineEdit_3.text()
                )
            )
            self.hide()
        except:
            self.error_label.setText("Введенные данные не корректны")


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

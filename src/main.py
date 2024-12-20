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
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from attr import has
from src.repository.crud.position.position import (
    add_position,
    delete_position,
    get_position,
    get_positions,
)
from src.repository.crud.position.schemas import PositionCreate
from src.repository.crud.section.schemas import SectionCreate
from src.repository.crud.section.section import (
    add_section,
    delete_section,
    get_all_sections,
    get_section_by_name,
    update_section_head,
)
from src.repository.crud.user.schemas import UserCreate, UserSearchParametrs
from src.repository.crud.user.user import (
    change_user_position,
    delete_user,
    get_users,
    register_user,
    update_user,
)
from src.repository.crud.vacation.schemas import VacationCreate
from src.repository.crud.vacation.vacation import add_vacation, get_all_vacations
from src.repository_file import Client
from src.ui.auth.authwindow import Ui_Form as authForm
from src.ui.profile.profile_window_rew import Ui_Dialog as profileForm
from src.ui.main.main_window_rew import Ui_Form as mainForm
from src.ui.vacations.vacations_window_rew_upd import Ui_Dialog as vacationForm
from src.ui.sections.sections import Ui_Dialog as sectionForm
from src.ui.sections.section_profile.section_profile import (
    Ui_Dialog as sectionProfileForm,
)
from src.ui.users.user_create.user_create import Ui_Form as userCreateForm
from src.ui.position.position_profile import Ui_Dialog as positionForm
from src.ui.sections.section_create.section_create import Ui_Form as sectionCreateForm
from src.ui.vacations.vacation_create.vacation_create_rew import (
    Ui_Form as vacationCreateForm,
)
from src.ui.users.users import Ui_Dialog as usersForm
from qasync import QEventLoop, asyncSlot

from src.utils.conver_to_excel import export_all_tables_to_excel


class BaseWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.client = Client()


class LoginForm(BaseWindow, authForm):
    def __init__(self, loop=None):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Авторизация")
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
        self.setWindowTitle("Профиль")
        self.pushButton.clicked.connect(self.on_main_clicked)
        self.client = client
        self.username = username
        self.profile = profile_username
        self.pushButton_3.clicked.connect(self.give_admin)
        self.pushButton_2.clicked.connect(self.delete_user)
        self.pushButton_4.clicked.connect(self.update_user)
        self.button_position.clicked.connect(self.on_position)
        self.button_section.clicked.connect(self.on_section)
        asyncio.create_task(self.load_profile_data(profile_username))

    def on_section(self):
        if self.button_section.text() != "None":
            self.hide()
            self.window = SectionProfileForm(
                self.client, self.username, self.button_section.text()
            )
            self.window.show()

    def on_position(self):
        if self.button_position.text() != "None":
            self.hide()
            self.window = PositionForm(
                self.client,
                self.username,
                self.button_position.text(),
                self.button_section.text(),
            )
            self.window.show()

    def update_user(self):
        asyncio.create_task(self.update_position())

    async def update_position(self):
        try:
            await change_user_position(
                email=self.profile, new_position_name=self.lineEdit.text()
            )
        except:
            self.error_label.setText("Введенные данные не корректны")

    def give_admin(self):
        asyncio.create_task(self.give_admin_to_user())

    async def give_admin_to_user(self):
        await update_user(self.profile)

    def delete_user(self):
        asyncio.create_task(self.delete_user_finally())

    async def delete_user_finally(self):
        await delete_user(self.profile)

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
            self.pushButton_4.setVisible(False)
            self.lineEdit.setVisible(False)
        elif data.is_superuser is True:
            self.pushButton_3.setVisible(False)

    def on_main_clicked(self):
        self.hide()
        self.window = MainWindow(self.client, self.username)
        self.window.show()


class UserCreateWindow(BaseWindow, userCreateForm):
    def __init__(self, client, username):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Создание пользователя")
        self.client = client
        self.username = username
        self.pushButton.clicked.connect(self.register)

    def register(self):
        asyncio.create_task(self.add_user())

    async def add_user(self):
        try:
            await register_user(
                UserCreate(
                    email=self.lineEdit_3.text(),
                    name=self.lineEdit_2.text(),
                    surname=self.lineEdit.text(),
                    position_name=self.lineEdit_4.text(),
                    hashed_password=self.lineEdit_5.text(),
                    is_superuser=False,
                    birthday=self.start_date_2.date().toPyDate(),
                )
            )
            self.hide()
        except:
            self.error_label.setText("Введенные данные не корректны")


class MainWindow(BaseWindow, mainForm):
    def __init__(self, client, username):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Главное меню")
        self.client = client
        self.username = username
        if self.client.is_root is False:
            self.adduser.setVisible(False)
        self.adduser_2.clicked.connect(self.database)
        self.adduser.clicked.connect(self.register_user)
        self.users.clicked.connect(self.on_users_clicked)
        self.sections.clicked.connect(self.on_sections_clicked)
        self.vacations.clicked.connect(self.on_vacation_clicked)
        self.pushButton.clicked.connect(self.on_find_clicked)
        self.profile_button.clicked.connect(self.on_profile_clicked)
        asyncio.create_task(self.load_main_window())

    def database(self):
        asyncio.create_task(export_all_tables_to_excel())

    def register_user(self):
        self.window = UserCreateWindow(self.client, self.username)
        self.window.show()

    async def load_main_window(self):
        data = await self.client.get_info_by_email()
        self.userinfo.setText(str(f"{data.name} {data.surname}"))
        if data.is_superuser == True:
            self.access_info.setText("Администратор")
            self.access_info.setStyleSheet("color: red;")
        else:
            self.access_info.setText("Пользователь")

    def on_users_clicked(self):
        self.hide()
        self.window = UsersForm(self.client, self.username)
        self.window.show()

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
        self.setWindowTitle("Отпуска")
        self.client = client
        self.username = username
        if self.client.is_root is False:
            self.vacation_button.setVisible(False)
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
        self.setWindowTitle("Создание отпуска")
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
        self.setWindowTitle("Отделы")
        self.client = client
        self.username = username
        if self.client.is_root is False:
            self.vacation_button.setVisible(False)
        self.tableWidget.itemClicked.connect(self.handle_item_click)
        self.vacation_button.clicked.connect(self.open_section_create)
        self.main_window_button.clicked.connect(self.open_main)
        asyncio.create_task(self.load_sections())

    def handle_item_click(self, item):
        column = item.column()
        if column == 1:
            section = item.text()
            self.on_department_name_clicked(section)

    def on_department_name_clicked(self, section_name):
        self.hide()
        self.window = SectionProfileForm(self.client, self.username, section_name)
        self.window.show()

    def open_section_create(self):
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
        self.setWindowTitle("Создание отдела")
        self.client = client
        self.username = username
        self.pushButton.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        asyncio.create_task(self.add_section())

    async def add_section(self):
        try:
            await add_section(
                SectionCreate(
                    name=self.lineEdit.text(), head_email=self.lineEdit_3.text()
                )
            )
            self.hide()
        except:
            self.error_label.setText("Введенные данные не корректны")


class SectionProfileForm(BaseWindow, sectionProfileForm):
    def __init__(self, client, username, section_name):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Отдел")
        self.client = client
        self.username = username
        self.section_name = section_name
        if self.client.is_root is False:
            self.add_position.setVisible(False)
            self.change_head.setVisible(False)
            self.remove_section.setVisible(False)
            self.new_position.setVisible(False)
            self.new_head.setVisible(False)
        self.tableWidget.itemClicked.connect(self.handle_item_click)
        self.add_position.clicked.connect(self.on_add_position)
        self.remove_section.clicked.connect(self.on_delete_clicked)
        self.change_head.clicked.connect(self.on_change_head)
        self.main_window_button.clicked.connect(self.open_main)
        asyncio.create_task(self.load_section(section_name))
        asyncio.create_task(self.load_positions(section_name))

    def handle_item_click(self, item):
        column = item.column()
        if column == 1:
            position = item.text()
            self.on_position_name_clicked(position)

    def on_position_name_clicked(self, position):
        self.hide()
        self.window = PositionForm(
            self.client, self.username, position, self.section_name
        )
        self.window.show()

    def open_main(self):
        self.hide()
        self.window = MainWindow(self.client, self.username)
        self.window.show()

    def on_add_position(self):
        asyncio.create_task(self.add_new_position())

    def on_delete_clicked(self):
        asyncio.create_task(self.delete_section())

    def on_change_head(self):
        asyncio.create_task(self.update_head())

    async def add_new_position(self):
        try:
            if self.new_position.text() == "":
                raise ValueError
            await add_position(
                PositionCreate(
                    section_name=self.section_name, name=self.new_position.text()
                )
            )
        except:
            self.error_label_2.setText("Введенные данные не корректны")

    async def delete_section(self):
        await delete_section(self.section_name)

    async def update_head(self):
        try:
            await update_section_head(str(self.section_name), str(self.new_head.text()))
        except:
            self.error_label.setText("Введенные данные не корректны")

    async def load_section(self, section_name):
        result = await get_section_by_name(section_name)
        if result != 0:
            if str(result.head_email) != "None":
                self.label_2.setText(str(result.head_email))
            else:
                self.label_2.setText("Нет")
            self.label_5.setText(str(section_name))

    async def load_positions(self, section_name):
        result = await get_positions(section_name)
        if result != 0:
            self.countler.setText(str(len(result)))
            self.tableWidget.setRowCount(len(result))
            self.tableWidget.setColumnCount(3)
            self.tableWidget.setHorizontalHeaderLabels(
                ["ID", "Должность", "Кол-во человек"]
            )
            for i in range(len(result)):
                self.tableWidget.setItem(i, 0, QTableWidgetItem(str(result[i].id)))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(result[i].name))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(str(result[i].users)))

            header = self.tableWidget.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)


class PositionForm(BaseWindow, positionForm):
    def __init__(self, client, username, position_name, section_name):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Должность")
        self.client = client
        self.username = username
        self.section_name = section_name
        self.position_name = position_name
        self.label_2.setText(position_name)
        self.label_5.setText(section_name)

        if self.client.is_root is False:
            self.remove_section.setVisible(False)

        self.main_window_button.clicked.connect(self.open_main)
        self.remove_section.clicked.connect(self.on_remove_clicked)
        asyncio.create_task(self.load_users())

    def open_main(self):
        self.hide()
        self.window = MainWindow(self.client, self.username)
        self.window.show()

    def on_remove_clicked(self):
        asyncio.create_task(self.delete_position())

    async def delete_position(self):
        await delete_position(self.position_name)

    async def load_users(self):
        result = await get_users(
            UserSearchParametrs(
                filter_on_vacation=None, filter_position=self.position_name
            )
        )
        if result != 0:
            self.countler.setText(str(len(result)))
            self.tableWidget.setRowCount(len(result))
            self.tableWidget.setColumnCount(8)
            self.tableWidget.setHorizontalHeaderLabels(
                [
                    "ID",
                    "Имя",
                    "Фамилия",
                    "Почта",
                    "Дата прихода",
                    "День рождения",
                    "Отпуск",
                    "Администратор",
                ]
            )
            for i in range(len(result)):
                self.tableWidget.setItem(i, 0, QTableWidgetItem(str(result[i].id)))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(result[i].name))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(result[i].surname))
                self.tableWidget.setItem(i, 3, QTableWidgetItem(result[i].email))
                self.tableWidget.setItem(
                    i, 4, QTableWidgetItem(result[i].joined_at.strftime("%d-%m-%Y"))
                )
                self.tableWidget.setItem(
                    i, 5, QTableWidgetItem(result[i].birthday.strftime("%d-%m-%Y"))
                )
                self.tableWidget.setItem(
                    i,
                    6,
                    QTableWidgetItem(
                        "Да" if result[i].is_on_vacation == True else "Нет"
                    ),
                )
                self.tableWidget.setItem(
                    i,
                    7,
                    QTableWidgetItem("Да" if result[i].is_superuser == True else "Нет"),
                )

            header = self.tableWidget.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)


class UsersForm(BaseWindow, usersForm):
    def __init__(self, client, username):
        super().__init__()
        self.setupUi(self)
        self.client = client
        self.username = username
        self.setWindowTitle("Пользователи")
        self.main_window_button.clicked.connect(self.open_main)
        asyncio.create_task(self.load_users())

    def open_main(self):
        self.hide()
        self.window = MainWindow(self.client, self.username)
        self.window.show()

    async def load_users(self):
        result = await get_users(
            UserSearchParametrs(filter_on_vacation=None, filter_position=None)
        )
        if result != 0:
            self.countler.setText(str(len(result)))
            self.tableWidget.setRowCount(len(result))
            self.tableWidget.setColumnCount(10)
            self.tableWidget.setHorizontalHeaderLabels(
                [
                    "ID",
                    "Имя",
                    "Фамилия",
                    "Должность",
                    "Отдел",
                    "Почта",
                    "Дата прихода",
                    "День рождения",
                    "Отпуск",
                    "Админ",
                ]
            )
            for i in range(len(result)):
                self.tableWidget.setItem(i, 0, QTableWidgetItem(str(result[i].id)))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(result[i].name))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(result[i].surname))
                self.tableWidget.setItem(
                    i, 3, QTableWidgetItem(result[i].position_name)
                )
                self.tableWidget.setItem(i, 4, QTableWidgetItem(result[i].section_name))
                self.tableWidget.setItem(i, 5, QTableWidgetItem(result[i].email))
                self.tableWidget.setItem(
                    i, 6, QTableWidgetItem(result[i].joined_at.strftime("%d-%m-%Y"))
                )
                self.tableWidget.setItem(
                    i, 7, QTableWidgetItem(result[i].birthday.strftime("%d-%m-%Y"))
                )
                self.tableWidget.setItem(
                    i,
                    8,
                    QTableWidgetItem(
                        "Да" if result[i].is_on_vacation == True else "Нет"
                    ),
                )
                self.tableWidget.setItem(
                    i,
                    9,
                    QTableWidgetItem("Да" if result[i].is_superuser == True else "Нет"),
                )

            header = self.tableWidget.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)


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

from src.repository.crud.user.schemas import UserLogin
from src.repository.crud.user.user import get_user_by_email, login_user, update_user
from src.utils.logger import logger


class Client:
    def __init__(self) -> None:
        self.email = None
        self.is_root = None

    async def login(self, login, password):
        res = await login_user(UserLogin(email=login, password=password))
        if res == 0:
            raise ValueError
        self.email = login

    async def get_home_page(self):
        try:
            data = await get_user_by_email(self.email)
            if self.is_root is None:
                self.is_root = data.is_superuser
            return data
        except Exception:
            logger.critical(f"Home page error {self.email}")

    async def get_info_by_email(self, email):
        try:
            return await get_user_by_email(email)
        except Exception:
            logger.critical(f"Get info error {self.email}")

    async def update_user_by_email(self, email):
        try:
            return await update_user(email)
        except Exception:
            logger.critical(f"Update user error {self.email}")

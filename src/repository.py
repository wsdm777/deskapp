from src.repository.crud.user.user import get_user_by_email, login_user


class Client:
    def __init__(self) -> None:
        self.email = None
        self.is_root = None

    async def login(self, login, password):
        try:
            await login_user(login, password)
            self.email = login
        except Exception:
            return "ERROR"

    async def get_home_page(self):
        try:
            data = await get_user_by_email(self.email)
            if self.is_root is None:
                self.is_root = data.is_superuser
            return data
        except Exception:
            return "ERROR"

    async def get_info_by_email(self, email):
        try:
            return await get_user_by_email(email)
        except Exception:
            return "ERROR"

    async def update_user_by_email(self, email):
        try:
            return await get_user_by_email(email)
        except Exception:
            return "ERROR"

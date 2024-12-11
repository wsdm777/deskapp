from src.repository.crud.user.user import login_user


class Client:
    def __init__(self) -> None:
        self.email = None
        self.is_root = None

    async def login(self, login, password):
        try:
            data = await login_user(login, password)
            self.email = data
            self.is_root = data.is_superuser
            return data
        except Exception:
            return "ERROR"

    def my_id(self):
        endpoint = "/user/me"
        url = f"{self.baseurl}{endpoint}"

        headers = {
            "accept": "application/json",
        }

        response = self.session.get(url, headers=headers, cookies=self.cookies)
        return response.json()

    def get_info_by_id(self, id):
        endpoint = f"/user/{id}"
        url = f"{self.baseurl}{endpoint}"
        headers = {
            "accept": "application/json",
        }
        response = self.session.get(url, headers=headers, cookies=self.cookies)
        return response.json()

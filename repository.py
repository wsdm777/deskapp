import requests


class APIClient:
    def __init__(self, url) -> None:
        self.baseurl = url
        self.session = requests.Session()
        self.cookies = None

    def close_session(self):
        if self.session:
            self.session.close()

    def login(self, login, password):

        endpoint = "/auth/login"
        url = f"{self.baseurl}{endpoint}"
        headers = {
            "accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {"grant_type": "password", "username": login, "password": password}

        response = self.session.post(url, headers=headers, data=data)
        if response.status_code == 400:
            raise ValueError
        self.cookies = response.cookies.get_dict()

    def me(self):
        endpoint = "/user/me"
        url = f"{self.baseurl}{endpoint}"

        headers = {
            "accept": "application/json",
        }

        response = self.session.get(url, headers=headers, cookies=self.cookies)
        return response.json()

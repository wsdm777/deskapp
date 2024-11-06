import requests

url = "http://127.0.0.1:8000/auth/login"
headers = {
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded",
}
data = {"grant_type": "password", "username": "user@example.com", "password": "1"}

with requests.session() as s:
    response = s.post(url, headers=headers, data=data)
    print(response)
    cook = s.cookies.get_dict()
    response = s.get("http://127.0.0.1:8000/user/me", cookies=cook)
    print(response.content)
    print(response)

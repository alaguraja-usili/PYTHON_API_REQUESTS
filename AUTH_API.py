import requests

auth_resp=requests.get("https://the-internet.herokuapp.com/basic_auth", auth=('admin','admin'))

print(auth_resp)
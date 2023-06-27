import json
import requests

""" payload = {
    "name": "Raja",
    "job": "leader"
} """

# read json file

mydata=open("data.json","r").read()

post_resp = requests.post("https://reqres.in/api/users", data=json.loads(mydata))

print(post_resp)

print(post_resp.json())


assert post_resp.json()['job']=='leader','Wrong Job name'

print(post_resp.headers.get("Content-Type"))
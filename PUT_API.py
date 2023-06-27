import json
import requests

payload = {
    "name": "morpheus",
    "job": "resident"
} 

put_resp = requests.put("https://reqres.in/api/users/2", data=payload)

print(put_resp)

print(put_resp.headers.get("Content-Type"))

assert put_resp.json()['job']=='resident','Wrong Job name'
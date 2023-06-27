import requests

#resp = requests.get("https://reqres.in/api/users?page=2")

# using params

p = {"page":2}

resp = requests.get("https://reqres.in/api/users", params=p) 

print(resp.url)


#print(resp)
#print(type(resp))
#print(dir(resp))

sta_code = resp.status_code

#Assert
assert sta_code==200, "sta_code doesn't match"
#assert sta_code==201, "sta_code doesn't match"

#JSON resp

#print(resp.json())
print(resp.headers)

print(resp.encoding)

print(resp.cookies)

print(resp.url)

print(resp.content)

resp_json = resp.json()
print(resp_json)

print(resp_json['total_pages'])

assert resp_json['total_pages'] ==2,"wrong total_pages"

#validate JSON file

assert (resp_json["data"][0]["email"]).endswith("reqres.in"), "email format is not matching"
# import requests
# import json
# import os

# headers = {
#     "developerkey": os.environ["REMOTEIT_DEVELOPER_KEY"]
# }
# body = {
#     "password": os.environ["REMOTEIT_PASSWORD"],
#     "username": os.environ["REMOTEIT_USERNAME"]
# }

# url = "https://api.remot3.it/apv/v27/user/login"

# response = requests.post(url, data=json.dumps(body), headers=headers)
# response_body = response.json()

# print("Status Code: %s" % response.status_code)
# print("Raw Response: %s" % response.raw)
# print("Body: %s" % response_body)
	

# import requests
# import os

# headers = {
#     "developerkey": os.environ["REMOTEIT_DEVELOPER_KEY"],
#     # Created using the login API
#     "token": os.environ["REMOTEIT_TOKEN"]
# }

# url = "https://api.remot3.it/apv/v27/device/list/all"

# response = requests.get(url, headers=headers)
# response_body = response.json()

# print("Status Code: %s" % response.status_code)
# print("Raw Response: %s" % response.raw)
# print("Body: %s" % response_body)


import requests
import json
import os

headers = {
    "developerkey": os.environ["REMOTEIT_DEVELOPER_KEY"],
    # Created using the login API
    "token": os.environ["REMOTEIT_TOKEN"]
}
body = {
    "deviceaddress": "DEVICE_ADDRESS",
    "wait":"true",
    "hostip":os.environ["MY_PUBLIC_IP"]
}

url = "https://api.remot3.it/apv/v27/device/connect"

response = requests.post(url, data=json.dumps(body), headers=headers)
response_body = response.json()

print("Status Code: %s" % response.status_code)
print("Raw Response: %s" % response.raw)
print("Body: %s" % response_body)


# import requests
# import json
# import os

# headers = {
#     "developerkey": os.environ["REMOTEIT_DEVELOPER_KEY"],
#     # Created using the login API
#     "token": os.environ["REMOTEIT_TOKEN"]
# }
# body = {
#     "deviceaddress": "DEVICE_ID",
#     "connectionid": "CONNECTION_ID"
# }

# url = "https://api.remot3.it/apv/v27/device/connect/stop"

# response = requests.post(url, data=json.dumps(body), headers=headers)
# response_body = response.json()

# print("Status Code: %s" % response.status_code)
# print("Raw Response: %s" % response.raw)
# print("Body: %s" % response_body)
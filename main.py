import requests
import datetime

USERNAME = "marcinqwerty"
TOKEN = "abcdefghijklm"

pixela_endpoint = "https://pixe.la/v1/users"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint,json=user_params)
print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "graph1",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
response = requests.post(url=graph_endpoint,json=graph_config, headers=headers)

# headers = {
#     "X-USER-TOKEN": TOKEN
# }
#
# body = {
#     "date":"20230727",
#     #"quantity":"100"
# }
#
#
# now = datetime.datetime.now()
# print(now.strftime("%Y%m%d"))
#
# post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
#
# response = requests.delete(url=post_endpoint,json=body, headers=headers)
#
# print(response.text)

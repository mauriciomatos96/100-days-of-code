import requests
import datetime as dt

USERNAME = "punisher96"
TOKEN = "huviofydt87aokhviufv87d98a7gyfvgy67"
GRAPH_ID = "graph1"

today = dt.datetime.today().strftime('%Y%m%d')

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Python Graph",
    "unit": "minutes",
    "type": "int",
    "color": "kuro"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

add_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

pixel_data = {
    "date": today,
    "quantity": input("How many minutes do you expend on python today? ")
}

response = requests.post(url=add_pixel_endpoint, json=pixel_data, headers=headers)
print(response.text)

# update_pixel_endpoint = f"{add_pixel_endpoint}/{today}"

# update_pixel_data = {
#     "quantity": "130"
# }

# response = requests.put(url=update_pixel_endpoint, json=update_pixel_data, headers=headers)
# print(response.text)
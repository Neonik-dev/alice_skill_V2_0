import urllib.request

import requests

header = {
    "Authorization": "AQAAAABbZGCdAAT7o-zwBdbrR0aLnPJ_3DKu1p4",
    'Content-Type': 'multipart/form-data'
}

urllib.request.urlretrieve("https://tel-hackathon.ru/assets/sounds/171.mp3", '171.mp3')
with open('171.mp3', 'rb') as f:
    response = requests.post("https://dialogs.yandex.net/api/v1/skills/4b81da5e-f2e6-4fb2-a5a8-33bc7d7bf7d8/sounds", files={'171.mp3': f}, headers=header)

print(response)
import sys
from io import BytesIO
import requests
from PIL import Image
import selection_param

toponym_to_find = " ".join(sys.argv[1:])  # 'Москва, ул. Ак. Королева, 12'
geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
# py main.py Москва, ул. Ак. Королева, 12
geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}
response = requests.get(geocoder_api_server, params=geocoder_params)
if not response:
    print(response.json())
    sys.exit()
    pass
map_params = selection_param.selection_of_parameters(response.json())
map_api_server = f"http://static-maps.yandex.ru/1.x/?pt={map_params['ll']},pm2dol1"
response = requests.get(map_api_server, params=map_params)
Image.open(BytesIO(response.content)).show()

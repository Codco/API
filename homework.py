import requests
import json

heroes_list = ['Hulk', 'Captain america', 'Thanos']
intelligence_dict = {'Hulk': 0, 'Captain america': 0, 'Thanos': 0}
url = 'https://www.superheroapi.com/api.php/2619421814940190/search/'

for hero in heroes_list:
    hero_dict = json.loads(requests.get(url + hero).content)
    intelligence_dict[hero] = int(hero_dict['results'][0]['powerstats']['intelligence'])


from urllib.parse import urlencode

base_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?'
public_key = 'https://cloud-api.yandex.net:443'

final_url = base_url + urlencode(dict(public_key=public_key))
response = requests.get(final_url)
download_url = response.json()['href']

download_response = requests.get(download_url)
with open('downloaded_file.txt', 'wb') as f:   # Здесь укажите нужный путь к файлу
    f.write(download_response.content)


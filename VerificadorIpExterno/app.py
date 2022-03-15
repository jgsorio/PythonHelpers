import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

response = urlopen(url)
dados = json.load(response)

ip = dados['ip']
cidade = dados['city']

print(f'IP Externo: {ip}, cidade: {cidade}')
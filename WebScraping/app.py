from bs4 import BeautifulSoup
import requests

url = 'https://climatempo.com.br'
response = requests.get(url).content

soup = BeautifulSoup(response, 'html.parser')

temperatura_minima = soup.find("img", alt="Temperatura mínima Hoje")
print(temperatura_minima)
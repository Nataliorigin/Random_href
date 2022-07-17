import requests


print('че я хочу')
URL = 'https://api.thecatapi.com/v1/images/search'
response = requests.get(URL).json()
random_cat = response[0].get('url')
print(random_cat)

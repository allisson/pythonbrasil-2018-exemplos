import requests


url = 'https://swapi.co/api/people/'
response = requests.get(url)
for person in response.json()['results']:
    print(person['name'])

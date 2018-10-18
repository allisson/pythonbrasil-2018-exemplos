import requests


url = 'https://swapi.co/api/people/'
people = requests.get(url)
for person in people.json()['results']:
    print(person['name'])

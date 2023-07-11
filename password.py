import json
import requests
import pprint

DRINK = 'margarita'
ID_KEY= 1
#search cocktail by name request
response = requests.get(f'http://www.thecocktaildb.com/api/json/v1/{ID_KEY}/search.php?s={DRINK}')

pprint.pprint(response.text)
print(response.status_code)
#already in json format so this is wrong: print(reponse.json())


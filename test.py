import requests
#import json
import pprint
from api import get_drink_data, get_ingredients, get_search_results





url = 'https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita'

response = requests.get(url)
data = response.json()  # Convert response content to a dictionary
#pprint.pprint(data)

all_dicts = data["drinks"]  # Access the "drinks" key in the dictionary
#for drink_dict in all_dicts:
    #print("**NEW DRINK**")
    #print(drink_dict['strDrink'])

#print(len(all_dicts))


#for i in range(len(data)):
 #   print("**NEW DRINK**")
 #   print(drinks['idDrink'])
    #for j in marg[i]:
        #print(j)


"""

What I need while using dynamic routes
'strDrink' - 
'strIngredient' + {num}' - strIngredient15
'strInstructions' - complete sentences

"""


#TESTING:
#print(get_ingredients('margarita'))#just picking the first of list: Watermelon Marg
print(" ")
print(get_drink_data('margarita', 'Blue Margarita')) # all data on margs
print(" ")
print(get_search_results('margarita')) #the whole list of margs
#print(get_single_drink_data('Blue Margarita', 'margarita')) # gets the recipe info of ONE drink result

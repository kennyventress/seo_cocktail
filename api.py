import requests

API_KEY = 1


#def get_single_drink_data(recipe_info):
"""
def get_single_drink_data(drink_name, recipe_name):

     gives us data to be used in drink.html 
    so we can display it for us to grab later
    #DRINK = input("Enter a drink: ")  # Prompt the user for input
    url = f'https://www.thecocktaildb.com/api/json/v1/{API_KEY}/search.php?s={drink_name}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        all_dicts = data['drinks']
        if all_dicts:
            for drink_dict in all_dicts:
                #print(drink_dict['strDrink'])
                #makes a small dict of ONLY the data we want to display from the API
                if drink_dict['strDrink'] == recipe_name:
                    recipe_dict = {
                        'name': drink_dict['strDrink'],
                        'instructions': drink_dict['strInstructions'],
                        'ingredients': get_ingredients(drink_dict),
                        'image_url': drink_dict['strDrinkThumb']
                    }
            return recipe_dict
    return None 
"""

def get_every_drink_data(drink_name):
    """ gives us data to be used in drink.html 
    so we can display it for us to grab later"""
    url = f'https://www.thecocktaildb.com/api/json/v1/{API_KEY}/search.php?s={drink_name}'
    response = requests.get(url)
    every_drink_dict = []
    if response.status_code == 200:
        data = response.json()
        all_dicts = data['drinks']
        if all_dicts:
            for drink_dict in all_dicts:
                drink_dict = {
                    'name': drink_dict['strDrink'],
                    'instructions': drink_dict['strInstructions'],
                    'ingredients': get_ingredients(drink_dict),
                    'image_url': drink_dict['strDrinkThumb']
                }
                every_drink_dict.append(drink_dict)
            return every_drink_dict
    return None 
    # TODO: in corresponding html... if this is NONE we need to disply that there was nothing there

def get_ingredients(drink_dict):
    """
    helper function to make it easier to display ingrediants from API (stored in a list)
    """
    ingredients = []
    for i in range(1, 16):
        item = f'strIngredient{i}'
        amount = f'strMeasure{i}'
        ingredient = f'{drink_dict[item]}'
        measurement = f'{drink_dict[amount]}'
        ingredients.append(f'{measurement} of {ingredient}')
    return ingredients

def get_search_results(drink_name):
    """ completely SEPERATE from above functions and used to 
    to return a full list of all available drinks for out hyperlinks"""
    
    url = f'https://www.thecocktaildb.com/api/json/v1/{API_KEY}/search.php?s={drink_name}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        all_dicts = data['drinks']
        drink_info = []
        for drink_dict in all_dicts:
                drink_info.append(drink_dict['strDrink'])
        return drink_info
    return None

def all_drink_recipes():
    all_recipes = []
    url_alc = f'https://www.thecocktaildb.com/api/json/v1/{API_KEY}/filter.php?a=Alcoholic'
    url_non_alc = f'https://www.thecocktaildb.com/api/json/v1/{API_KEY}/filter.php?a=Non_Alcoholic'
    
    response_1 = requests.get(url_alc)
    response_2 = requests.get(url_non_alc)

    if response_1.status_code == 200:
        data = response_1.json()
        all_dicts = data['drinks']
        if all_dicts:
            for drink_dict in all_dicts:
                all_recipes.append(drink_dict['strDrink'])
    
    if response_2.status_code == 200:
        data = response_2.json()
        all_dicts = data['drinks']
        
        if all_dicts:
            for drink_dict in all_dicts:
                all_recipes.append(drink_dict['strDrink'])
                #print("one non-alc drink")
        return all_recipes
            
    return None

def perform_search(search_query):
    all_drinks = all_drink_recipes()
    search_results = []
    for drink in all_drinks:
        if search_query.lower() in drink.lower():
            search_results.append(drink)
    return search_results

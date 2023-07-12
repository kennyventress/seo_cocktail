import requests

API_KEY = 1

def get_drink_data(drink_name, recipe_name):
    """ gives us data to be used in drink.html 
    so we can display it for us to grab later"""
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
    # TODO: in corresponding html... if this is NONE we need to disply that there was nothing there

def get_ingredients(drink_dict):
    """
    helper function to make it easier to display ingrediants from API (stored in a list)
    """
    ingredients = []
    for i in range(1, 16):
        ingredient = f'strIngredient{i}'
        measurement = f'strMeasure{i}'
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


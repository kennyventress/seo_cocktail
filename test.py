import requests
#import json
import pprint
from api import get_ingredients, get_search_results, get_every_drink_data, get_single_drink_data, perform_search, all_drink_recipes

url = 'https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita'
response = requests.get(url)
data = response.json()  # Convert response content to a dictionary
#pprint.pprint(data)

all_dicts = data["drinks"]  # Access the "drinks" key in the dictionary

#TESTING:
print(get_every_drink_data('vodka'))
print(" ")
print(get_single_drink_data('margarita', 'Blue Margarita')) # all data on margs
print(" ")
print(get_search_results('margarita')) #the whole list of margs
#print(get_single_drink_data('Blue Margarita', 'margarita')) # gets the recipe info of ONE drink result
print(" ")
print(all_drink_recipes())
#print(" ")
#print(perform_search('margarita'))




#@app.route('/search', methods=['GET', 'POST'])
 #   if request.method == 'POST':
 #       search_query = request.form.get('search_query')
  #      if search_query:
  #          return redirect(url_for('search_results', drink_name=search_query))
  # return render_template('search.html')
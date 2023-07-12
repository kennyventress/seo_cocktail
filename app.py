from flask import Flask, render_template, redirect, url_for, flash, request
#from form import RegistrationForm 
#TODO^^ make my own search form!!!!
from api import get_every_drink_data
from flask_behind_proxy import FlaskBehindProxy

# Create the App
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    """ Home Page """
    return render_template('home.html')

@app.route('/search', methods=['GET', 'POST']) #look up if GET is needed
def search(): #works here
    print("SEARCH ROUTE")
    if request.method == 'POST':
        print("This is a POST request")
        print(request.form)
        search_query = request.form.get('drink_name')
        print(f'We have a search query: {search_query}')
        print(" ")
        print(" ")
        #print(type(search_query))
        if search_query:
            # Perform search based on search_query
            #list_all_drink_info = get_every_drink_data(search_query)
            #print(f'this is my list of all drink info: {list_all_drink_info }')
            return redirect(url_for('search_results', search_query=search_query ))
    return render_template('search.html') #search template but edited to have "no search results found"

@app.route('/search_results/<search_query>', methods=['GET', 'POST'])
def search_results(search_query):
    print(f'Search_results route works')
    print(" ")
    print(" ")
    print(" ")
    drink_list = get_every_drink_data(search_query)
    
    print(f'This is drink list: {drink_list}')
    return render_template('search_results.html', drink_list=drink_list)

@app.route('/search_results/drink_info/<recipe_name>')
def drink_info(recipe_name):
    # pass the drink name in here into rout and then take it
    # call a function that gives all the info for that particular drink
    # return it to drink_info page

    print(f'We want this EXACT DRINK: {recipe_name}')
    drink_list = get_every_drink_data(recipe_name)
    our_drink = drink_list[0]
    print(our_drink)
    
    #recipe_dict = request.args.get('recipe_dict')

    return render_template('drink_info.html', recipe_dict=our_drink)

@app.route('/about')
def about():
    """ about page linked """
    return render_template('about.html')

# make own database and add it to API's as another option...
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """ contact page linked """
    if request.method == 'POST':
        # Process the form submission
        flash('Form submitted successfully!')
        return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

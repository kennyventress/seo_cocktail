from flask import Flask, render_template, redirect, url_for, flash, request
#from form import RegistrationForm 
#TODO^^ make my own search form!!!!
from api import get_drink_data
from flask_behind_proxy import FlaskBehindProxy

# Create the App
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    """ Home Page """
    return render_template('home.html')

#@app.route('/search', methods=['GET', 'POST'])
 #   if request.method == 'POST':
 #       search_query = request.form.get('search_query')
  #      if search_query:
  #          return redirect(url_for('search_results', drink_name=search_query))
  # return render_template('search.html')

@app.route('/search_results', methods=['GET', 'POST'])
def search_results():
    if request.method == 'POST':
        search_query = request.form.get('search_query')
        if search_query:
            # Perform search based on search_query
            results = perform_search(search_query)
            return render_template('search_results.html', results=results)
    return render_template('search_results.html')

@app.route('/search_results/drink_info')
def drink_info(drink_name, recipe_name):
    ''' This is only triggered within the search_result.html and creates
    a usable, unique hyperlink specifique to a certain recipe name'''
    #TODO is the 'name' a string type when passed to get_drink_data?
    recipe_dict = get_drink_data(drink_name, recipe_name)
    return render_template('drink_info.html', recipe_dict=recipe_dict)

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

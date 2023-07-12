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

@app.route('/search_results', methods=['GET', 'POST'])
def search_results():
    if request.method == 'POST':
        search_query = request.form.get('search_query')
        if search_query:
            # Perform search based on search_query
            every_drink = get_every_drink_data(search_query)
            return render_template('search_results.html', every_drink = every_drink)
    return render_template('search_results.html')

@app.route('/search_results/drink_info/<recipe_dict>')
def drink_info(recipe_dict):
    #recipe_dict = request.args.get('recipe_dict')
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

from flask import Flask, render_template, redirect, url_for, flash, request
#from forms import RegistrationForm
from flask_behind_proxy import FlaskBehindProxy

# Create the App
app = Flask(__name__)

@app.route('/')
def default():
    """ main page """
    return render_template('home.html')

@app.route('/home')
def home():
    """ home page linked """
    return render_template('home.html')

@app.route('/find')
def find():
    """ goes to find cocktail page """
    return render_template('find.html')

@app.route('/about')
def about():
    """ about page linked """
    return render_template('about.html')

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

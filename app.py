"""
app.py 
"""
from flask import Flask, render_template
from flask import redirect, url_for

app = Flask(__name__)

@app.route('/home')
def home():
    """
    Route to home page using flask
    """
    return render_template("index.html")

@app.route('/')
def old_page():
    """
    Redirects '/' to '/home'
    """
    return redirect(url_for('home'))

@app.route('/professionals')
def professionals():
    """
    Route to Professionals page
    """
    return render_template('professionals.html')

@app.route('/services')
def services():
    """
    Route to Services page
    """
    return render_template('services.html')

@app.route('/contact')
def contact():
    """
    Route to Contact page
    """
    return render_template('contact.html')

@app.route('/login')
def login():
    """
    Route to Login page
    """
    return render_template('login.html')

@app.route('/register')
def register():
    """
    Route to Register page
    """
    return render_template('register.html')

@app.route('/pay')
def pay():
    """
    Route to Pay page
    """
    return render_template('pay.html')

@app.route('/common/<path:pathname>')
def common_things(pathname):
    """
    Route to Nav and Footer pages in common folder
    """
    return render_template(f'/common/{pathname}')

# @app.route('/static/css/<path:pathname>')
# def css(pathname):
#     """
#     Route to CSS file 
#     """
#     return render_template(f'/static/css/{pathname}')

# @app.route('/static/js/<path:pathname>')
# def js(pathname):
#     """
#     Route to JS file 
#     """
#     return render_template(f'/static/js/{pathname}')

# @app.route('/static/images/<path:pathname>')
# def images(pathname):
#     """
#     Route to Images file 
#     """
#     return render_template(f'/static/images/{pathname}')

if __name__ == '__main__':
    app.run(debug=True)

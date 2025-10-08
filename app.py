"""
app.py 
"""
from flask import Flask, render_template
from flask import redirect
from flask import send_file
from model import get_professionals, get_services

app = Flask(__name__)

@app.route('/home')
def home():
    """
    Route to home page using flask
    """
    return render_template("index.html")

@app.route('/')
def root():
    """
    Redirects '/' to '/home'
    """
    return redirect('home')

@app.route('/professionals')
def professionals():
    """
    Route to Professionals page
    """
    professionals_data = get_professionals()
    return render_template('professionals.html', professionals_data=professionals_data)

@app.route('/services')
def services():
    """
    Route to Services page
    """
    categories = get_services()
    return render_template('services.html', categories=categories)

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

# Common Routes
@app.route('/common/nav.html')
def nav():
    """
    Route to Nav
    """
    return render_template('common/nav.html')

@app.route('/common/footer.html')
def footer():
    """
    Route to Footer
    """
    return render_template('common/footer.html')

# Other Templates
@app.route('/css/styles.css')
def css():
    """
    Route to CSS file 
    """
    return send_file('static/css/styles.css')

@app.route('/images/<path:pathname>')
def images(pathname):
    """
    Route to Images file 
    """
    return send_file(f'static/images/{pathname}')

if __name__ == '__main__':
    app.run(debug=True)

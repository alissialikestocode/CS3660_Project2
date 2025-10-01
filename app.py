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

@app.route('/common/footer')
def common_footer():
    """
    Route to Footer page in common folder
    """
    return render_template('/common/footer.html')

@app.route('/common/nav')
def common_nav():
    """
    Route to Header page in common folder
    """
    return render_template('/common/nav.html')

# @app.route('/static/css/styles')
# def css_styles():
#     """
#     Route to css stylesheet
#     """
#     return render_template("/static/css/styles.css")

# @app.route('/static/js/index')
# def js():
#     """
#     Route to javascript file
#     """
#     return render_template("/static/js/index.js")


if __name__ == '__main__':
    app.run(debug=True)

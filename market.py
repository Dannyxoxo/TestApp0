from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html', item='Laptop')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/shop')
def shop_page():
    return render_template('shop.html')

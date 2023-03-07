from flask import Flask, render_template
from web_app.variables import data

app = Flask(__name__)


@app.route('/')
def front_page():
    return render_template("main.html")

@app.route('/list')
def list():
    return render_template("pc.html", pcs=data)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)
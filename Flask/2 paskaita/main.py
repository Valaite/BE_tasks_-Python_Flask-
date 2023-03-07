from flask import Flask, render_template, url_for, redirect, request
from dictionary import data
from forms import ContactForm
import os

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        date = request.form['date']
        autorius = request.form['autorius']
        tekstas = request.form['tekstas']
        pavadinimas = request.form['pavadinimas']
        data.append({
            'data': date,
            'autorius': autorius,
            'pavadinimas': pavadinimas,
            'tekstas': tekstas,
            'status': 'Aktyvus'
        })
    return render_template('adv.html', data=data)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        name = request.form['name']
        return render_template("name.html", name=name)
    else:
        return render_template("login.html")

@app.route('/adv')
def adv():
    return render_template('adv.html', data=data)

#/admin - grąžina į home page naudodamas admin vietoje vardo:
@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin!"))

@app.route('/<string:title>') # parametruose nurodomas kintamasis (title) ir jo tipas (string)
def article(title): # kintam1jį būtinai nurodykite ir funkcijos parametruose
    return render_template('fullAdv.html', title=title, data=data) # taip pat ir čia reikia jį perduoti

@app.route('/add_adv')
def add_adv():
    return render_template('add_adv.html')
    
@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = ContactForm()
    if form.validate_on_submit():
        return render_template('greetings.html', form=form)
    return render_template('registration.html', form=form)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
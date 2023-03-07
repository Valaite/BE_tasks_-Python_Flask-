from flask import Flask, render_template, request, redirect, url_for
from web_app.data import data
from forms import ContactForm
import os

SECRET_KEY = os.urandom(32)
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/autorius_sarasas/listas')
def list():
    return render_template('list.html', data=data)

@app.route('/<string:title>')
def article(title):
     return render_template('article.html', title=title, data=data)

@app.route('/add_article', methods=['GET', 'POST'])
def add_article():
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
            'status': 'published'
        })
        return redirect(url_for('list'))
    return render_template('add_article.html')

@app.route('/contact_us', methods=['GET', 'POST'])
def contact_us():
    ContantForm = ContactForm()
    if ContantForm.validate_on_submit():
        return "Form.Validate"
    return render_template('contact_us.html', form=ContantForm)

if __name__ == '__main__':
  app.run(debug=True)

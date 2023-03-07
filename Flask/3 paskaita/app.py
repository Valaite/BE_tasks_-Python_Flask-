import os
from datetime import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from form import PersonForm

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.app_context().push()

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir, 'data.sqlite')
# nustatėme, kad mūsų duomenų bazė bus šalia šio failo esants data.sqlite failas
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# neseksime kiekvienos modifikacijos
db = SQLAlchemy(app)
# sukuriame duomenų bazės objektą
# sukurkime modelį užklausos formai, kuris sukurs duomenų bazėje lentelę


class Signature(db.Model):
    # DB lentelei priskiria pavadinimą, jei nenurodysite, priskirs automatiškai pagal klasės pavadinimą.
    __tablename__ = 'signatures'
    id = db.Column(db.Integer, primary_key=True)  # stulpelis, kurio reikšmės integer. Taip pat jis bus primary_key.
    name = db.Column(db.String(80), nullable=False)
    l_name = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(80))
    comment = db.Column(db.Text, nullable=False)

    def __init__(self, name, l_name, comment, date):
        self.name = name
        self.l_name = l_name
        self.comment = comment
        self.date = date

    def __repr__(self):
        return f'{self.name} - {self.l_name}'


@app.route('/', methods=['GET', 'POST'])
def sign():
    data = Signature.query.all()[::-1]
    form = PersonForm()
    if form.validate_on_submit():
        name = form.name.data
        l_name = form.l_name.data
        comment = form.comment.data
        now = datetime.now()
        date = now.strftime("%d/%m/%Y %H:%M:%S")
        entry = Signature(name=name, l_name=l_name, comment=comment, date=date)
        db.session.add(entry)
        db.session.commit()
        data = Signature.query.all()[::-1]
        return render_template('petition.html', form=False, data=data)
    return render_template('petition.html', form=form, data=data)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
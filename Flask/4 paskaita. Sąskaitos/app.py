import os
from flask import Flask, render_template,  redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import forms

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir, 'biudzetas.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column("Vardas", db.String(50), nullable=False)
    l_name = db.Column("Pavardė", db.String(50), nullable=False)
    code = db.Column("Asmens kodas", db.String(50), nullable=False)
    phone_number = db.Column("Telefono numeris", db.String(50), nullable=False)
    accounts = db.relationship('Account')
    
class Bank(db.Model):
    __tablename__ = "bank"
    id = db.Column(db.Integer, primary_key=True)
    bank_name = db.Column('Pavadinimas', db.String(50), nullable=False)
    address = db.Column("Adresas", db.String(50), nullable=False)
    bank_code = db.Column("Banko kodas", db.String(50), nullable=False)
    swift = db.Column("SWIFT kodas", db.String(50), nullable=False)
    accounts = db.relationship('Account')
    
class Account(db.Model):
    __tablename__ = "account"
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column("Sąskaitos numeris", db.String(50), nullable=False)
    balanse = db.Column("Balansas", db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User", cascade="all, delete", passive_deletes=True)
    bank_id = db.Column(db.Integer, db.ForeignKey("bank.id"))
    bank = db.relationship("Bank", cascade="all, delete", passive_deletes=True)

@app.route("/form_banks", methods=["GET", "POST"])
def new_bank():
    db.create_all()
    form = forms.BankForm()
    if form.validate_on_submit():
        new_bank = Bank(bank_name=form.bank_name.data, address=form.address.data, bank_code=form.bank_code.data, swift=form.swift.data)
        db.session.add(new_bank)
        db.session.commit()
        return render_template("form_banks.html", form=False)
    return render_template("form_banks.html", form=form)

@app.route("/form_users", methods=["GET", "POST"])
def new_user():
    db.create_all()
    form = forms.UserForm()
    if form.validate_on_submit():
        new_user = User(name=form.name.data, l_name=form.l_name.data, code=form.code.data, phone_number=form.phone_number.data)
        db.session.add(new_user)
        db.session.commit()
        return render_template("form_users.html", form=False)
    return render_template("form_users.html", form=form)

@app.route("/form_accounts", methods=["GET", "POST"])
def new_account():
    db.create_all()
    form = forms.AccountForm()
    if form.validate_on_submit():
        new_account = Account(number=form.number.data, balanse=form.balanse.data, bank_id=form.bank.data.id, user_id=form.user.data.id)
        db.session.add(new_account)
        db.session.commit()
        return render_template("form_accounts.html", form=False)
    return render_template("form_accounts.html", form=form)

@app.route("/account_delete/<int:id>")
def account_delete(id):
    uzklausa = Account.query.get(id)
    db.session.delete(uzklausa)
    db.session.commit()
    return redirect(url_for('accounts'))

@app.route("/bank_delete/<int:id>")
def bank_delete(id):
    uzklausa = Bank.query.get(id)
    db.session.delete(uzklausa)
    db.session.commit()
    return redirect(url_for('banks'))

@app.route("/user_delete/<int:id>")
def user_delete(id):
    uzklausa = User.query.get(id)
    db.session.delete(uzklausa)
    db.session.commit()
    return redirect(url_for('users'))


@app.route("/banks")
def banks():
    try:
        all_banks = Bank.query.all()
    except:
        all_banks = []
    return render_template("banks.html", all_banks=all_banks)

@app.route("/users")
def users():
    try:
        all_users = User.query.all()
    except:
        all_users = []
    return render_template("users.html", all_users=all_users)

@app.route("/accounts")
def accounts():
    try:
        all_accounts = Account.query.all()
    except:
        all_accounts = []
    return render_template("accounts.html", all_accounts=all_accounts)

@app.route('/')
def about():
    return render_template('base.html')

if __name__ == "__main__":
    db.create_all()
    app.run(host='127.0.0.1', port=8000, debug=True)
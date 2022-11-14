from app import *
from flask import render_template, request
from .form import LoginForm


@app.route("/")
def index():
    return render_template('index.html', title="Main")


@app.route("/login", methods=["GET", "POST"])
def login():
    message = ''
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('psw')
        # simple checking a sending of form
        if email == 'e@mail.ru' and password == 'pass':
            message = "Correct username and password"
        else:
            message = "Wrong username or password"
        print("Custom Form - is ok")
    return render_template('login.html', message=message, title="Using Custom html forms")


@app.route("/login_quick_form", methods=["GET", "POST"])
def login_quick_form():
    form = LoginForm()

    if form.validate_on_submit():
        print("QuickForm - is ok")
    return render_template('login_quick_form.html', form=form, title="Using Quick_form()")


@app.route('/login_custom_wtforms', methods=["POST", "GET"])
def login_custom_wtforms():
    form = LoginForm()
    if form.validate_on_submit():
        print("Custom WTForms - is ok")
    return render_template('login_custom_wtforms.html', form=form, title="Using WTForms with custom styles")

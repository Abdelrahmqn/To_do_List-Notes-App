from flask import render_template, url_for, flash, redirect, request
from Application import app
from Application.forms import SignUp, LogIn
from Application.models import User, Notes
from flask_login import login_required, logout_user, login_user
from Application import db
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', strict_slashes=False)



@app.route("/sign-up", methods=['GET', 'POST'], strict_slashes=False)
def sign_up():
    form = SignUp()
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        if User.query.filter_by(username=username).first():
            flash("Username already exists, please choose another one.")
            return redirect(url_for('sign_up'))
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        flash("Sign Up successful")
        return redirect(url_for('login'))
    return render_template('sign_up.html', title='Sign Up', form=form)

@app.route("/login/", methods=['GET', 'POST'])
def login():
    form = LogIn()
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for("home"))
        flash("Invalid email or password")
    return render_template('login.html', title='Login', form=form)


@app.route('/logout', strict_slashes=False)
@login_required
def logout():
    logout_user()
    flash('you are out')
    return redirect(url_for('home'))

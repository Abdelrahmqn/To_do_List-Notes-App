from flask import render_template, url_for, flash, redirect
from Application import app
from Application.forms import SignUp, LogIn
from Application.models import User, Notes


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')



@app.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    form = SignUp()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('sign_up.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'], strict_slashes=False)
def login():
    form = LogIn()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
from flask import render_template, url_for, flash, redirect
from blog_chuhan import app
from blog_chuhan.forms import RegistrationForm, LoginForm
from blog_chuhan.models import User,Post


posts = [{
    "author": "Chuhan",
    "title": "blog1",
    "content": "first_blog",
    "date_posted": "Jun 22"
}, {
    "author": "Xiaoyu",
    "title": "blog2",
    "content": "second_blog",
    "date_posted": "Jun 22"
}]
# decorator @app


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', blog_list=posts, title="Chuhan")


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
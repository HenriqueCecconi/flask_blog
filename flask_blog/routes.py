from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_user, logout_user

from flask_blog import app, bcrypt, db
from flask_blog.forms import LoginForm, RegistrationForm
from flask_blog.models import Post, User

posts = [
    {
        "author": "Henrique Cecconi",
        "title": "Blog Post 1",
        "content": "My first blog post!",
        "date_posted": "2023-01-10",
    },
    {
        "author": "Henrique Cecconi",
        "title": "Blog Post 2",
        "content": "My second blog post!",
        "date_posted": "2023-01-11",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for("home"))
        else:
            flash(
                "Login failed. Please check your email and password", category="danger"
            )
    return render_template("login.html", title="Login", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        user = User(
            username=form.username.data, email=form.email.data, password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created. You are now able to login!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

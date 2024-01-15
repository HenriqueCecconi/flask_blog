from flask import Flask, flash, redirect, render_template, url_for
from forms import LoginForm, RegistrationForm

app = Flask(__name__)

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
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You have been logged in!", category="success")
            return redirect(url_for("home"))
        else:
            flash(
                "Login failed. Please check your email and password",
                category="danger",
            )

    return render_template("login.html", title="Login", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", category="success")
        return redirect(url_for("home"))

    return render_template("register.html", title="Register", form=form)


if __name__ == "__main__":
    app.run(debug=True)

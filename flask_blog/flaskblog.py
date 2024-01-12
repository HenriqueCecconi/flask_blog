from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Henrique Cecconi',
        'title': 'Blog Post 1',
        'content': 'My first blog post!',
        'date_posted': '2023-01-10'
    },
    {
        'author': 'Henrique Cecconi',
        'title': 'Blog Post 2',
        'content': 'My second blog post!',
        'date_posted': '2023-01-11'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')
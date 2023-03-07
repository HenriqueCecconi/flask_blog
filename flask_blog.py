from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Henrique Cecconi',
        'title': 'First Blog Post',
        'content': 'Fisrt post content',
        'date_posted': '07/03/2023'
    },
    {
        'author': 'Caio Castro',
        'title': 'Second Blog Post',
        'content': 'Second post content',
        'date_posted': '07/03/2023'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)
    
@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)
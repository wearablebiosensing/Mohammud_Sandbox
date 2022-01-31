from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog post 1',
        'content': 'First post content',
        'data_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'data_posted': 'April 21, 2018'
    },
]

@app.route('/')
@app.route('/home')
def home():
    #render the template
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')





#-------------------------
if __name__ == '__main__':
    app.run(debug=True)
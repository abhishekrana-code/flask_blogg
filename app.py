from flask import Flask,render_template
app = Flask(__name__)

posts=[
    {
        'author':'ABHISHEK',
        'title':'Blog Post 1',
        'content':'First post',
        'date_posted':'March 10, 2026'
    },
    {
        'author':'John',
        'title':'Blog Post 2',
        'content':'Second post',
        'date_posted':'March 11, 2026'
    },
    {
        'author':'Sonu',
        'title':'Blog Post 3',
        'content':'Third post',
        'date_posted':'March 12, 2026'
    }
    

]


@app.route('/')
def home():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',title='Aboutme')

if __name__ == '__main__':
    app.run(debug=True)
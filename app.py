from flask import Flask, flash, url_for, redirect, render_template
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'ecf0e9fc94ea05601651791c2727fca1'

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

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account crated for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com' and form.password.data == '1234':
            flash('you have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('login unsuccessful. Please check email and password', 'danger')
    return render_template('login.html',title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
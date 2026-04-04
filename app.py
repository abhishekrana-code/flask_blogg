from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask import Flask, flash, url_for, redirect, render_template
from forms import RegistrationForm, LoginForm 
from models import User, Post

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['SECRET_KEY'] = 'ecf0e9fc94ea05601651791c2727fca1'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

db = SQLAlchemy(app);

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
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        )

        db.session.add(user)
        db.session.commit()

        flash('Account created successfully!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html',title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # if form.validate_on_submit():
    #     if form.email.data == 'admin@gmail.com' and form.password.data == '1234':
    #         flash('you have been logged in!', 'success')
    #         return redirect(url_for('home'))
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('login unsuccessful. Please check email and password', 'danger')
    return render_template('login.html',title='Login', form=form)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
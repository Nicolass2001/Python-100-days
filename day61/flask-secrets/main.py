from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap4

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

WTF_CSRF_ENABLED = False
EMAIL = "admin@email.com"
PASSWORD = "12345678"

class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    pwd = PasswordField(label='Password', validators=[DataRequired(), Length(8)])
    submit = SubmitField(label='Login')


app = Flask(__name__)
app.secret_key = "qweklajjaklewkla"
bootstrap = Bootstrap4(app)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        email = form.email.data
        pwd = form.pwd.data
        if email == EMAIL and pwd == PASSWORD:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)

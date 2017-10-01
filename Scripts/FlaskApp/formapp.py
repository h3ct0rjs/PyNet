# Core Flask
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

# Time
from flask_moment import Moment
from datetime import datetime
# Forms
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


app = Flask(__name__)
Bootstrap(app)  # Implement bootstrap in the app instance
moment = Moment(app)  # Use moment.js to handle the time in client-side
app.config['SECRET_KEY'] = 'hector'

# Playing with Forms


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    name2 = StringField('Grade')
    submit = SubmitField('Submit')
    print(name,name2,submit,'Clase\n')

# Routes

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    name2 = None 
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        name2 = form.name2.data
        print(name,name2,'dasd')
        form.name.data = ''
        form.name2.data = ''
    return render_template('forms.html', form=form, name=name, name2=name2)

if __name__ == '__main__':
    app.run(debug=True)

from flask import request, Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment 
from datetime import datetime

#Forms
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

#My progressive app to learn flask. 
app = Flask(__name__)
Bootstrap(app)  #Implement bootstrap in the app instance
moment = Moment(app) #Use moment.js to handle the time in client-side

#Routes
@app.route('/')
def index():
    x = "Yupiii Yay!"
    return render_template('index.html',val=x,current_time=datetime.utcnow())

@app.route('/contact')
def contact():
    return render_template('index.html',val ='Contacto! ',\
        current_time=datetime.utcnow())

@app.route('/about')
def about():
    return render_template('index.html',val ='Acerca de ',\
        current_time=datetime.utcnow())

#Error Handlers for common http problems 
@app.errorhandler(404)
def page_not_found(e):
    return render_template('failure.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('failure.html'), 500
 
if __name__ == '__main__':
    app.run(debug=True)

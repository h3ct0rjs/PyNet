from flask import request, Flask, redirect
app = Flask(__name__)

@app.route('/')
def index():
    '''
    Request Context
    '''
    user_agent = request.headers.get('User-Agent')
    print('The Header sent by the user is :\n {}'.format(request.headers))
    return '<h1>Hello!</h1> \n <p>Your browser is {}</p> to {} '.format(user_agent, request.headers.get('Host'))

@app.route('/fooredirect')  
def red():
    '''
    Creates a basic redirection 
    '''
    return redirect('http://www.hectorfjimenez.co')
@app.route('/foo')
def red2():
    abort(404)  

if __name__ == '__main__':
    app.run(debug=True)
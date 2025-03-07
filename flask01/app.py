from flask import Flask

app = Flask(__name__)

@app.route('/')

def hola_aaron():
    return 'Hola Aaron!'

@app.route('/alex')
def hola_alex():
    return 'Hola Alex!'

@app.route('/jorge')
def hola_jorge():
    return '<h1 style="color:red;">Hola jorge!</h1>'

@app.route('/json')
def algo():
    return '{"nombre":"John"}'

@app.route('/xml')
def algo2():
    return '<nombre>Jonh</nombre>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True) 
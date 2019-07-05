from flask import Flask,jsonify

import dbmodle as db
app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello proxy !\n power by redis '

@app.route('/http')
def http():
    _http = db.getkey()
    return jsonify({'http':_http.decode('utf-8')})

@app.route('/https')
def https():
    _https = db.getkey(protocol='https')
    return jsonify({'https':_https.decode('utf-8')})

@app.route('/list')
def listindex():
    return jsonify(db.getkeys())

if __name__ == '__main__':
    app.run(debug=True)
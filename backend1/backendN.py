from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

@app.route('/')
def content():
    return ''

@app.route('/healthz')
def healthz():
    return 'HTTP 200 OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
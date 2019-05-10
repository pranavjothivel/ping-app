from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'hello'

@app.route('/api/ping')
def ping():
    return jsonify({'ping': 'pong'})
    
if __name__ == "__main__":
    app.run()
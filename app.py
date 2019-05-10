from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return 'hello'

@app.route('/api/ping')
def ping():
    return jsonify({'ping': 'pong'})
    
if __name__ == "__main__":
    app.run()
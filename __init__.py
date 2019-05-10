from Flask import flask, jsonify

app = flask(__name__)

@app.route('/api/ping')
def ping():
    return jsonify({'ping': 'pong'})
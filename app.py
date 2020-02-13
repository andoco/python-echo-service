import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/hello', methods=['GET'])
def api_hello():
    if 'name' in request.args:
        msg = 'Hello ' + request.args['name']
    else:
        msg = 'Hello world'

    return jsonify({'response': msg})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

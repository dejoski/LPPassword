#%%

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods = ['GET', 'POST'])
def hello():
    return jsonify("hello")

@app.route('/test', methods = ['GET', 'POST'])
def hello():
    return jsonify("hello")


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
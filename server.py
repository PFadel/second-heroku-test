import os

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

port = int(os.environ.get("PORT", 5000))


@app.route('/hello')
def hello():
    if not request.headers.get("cooler_token"):
        return jsonify({
            "message": "You need to send me a cooler token!"
        }), 401

    return jsonify({"message": "I'm even cooler"})


app.run(host='0.0.0.0', threaded=True, port=port)

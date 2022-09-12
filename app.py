from flask import Flask, jsonify

from db import Drivers as drivers

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_index():
    return jsonify({'Drivers': drivers})


if __name__ == '__main__':
    app.run(debug=True)  
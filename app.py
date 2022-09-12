from flask import Flask, jsonify

from db import Drivers as drivers

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_index():
    return jsonify({'Drivers': drivers})

@app.route('/<string:driverId>/')
def get_driver(driverId):
    for driver in drivers:
        if driver['driverId'] == driverId:
            return jsonify(driver)
    return '<h1>No driver with that id</h1>'
    
@app.route('/<string:driverId>/short/')
def get_driver_short(driverId):
    for driver in drivers:
        if driver['driverId'] == driverId:
            return (
                f"<h1>{driver['givenName']} {driver['familyName']}</h1><hr><h4>Number: {driver['permanentNumber']}</h4><h4>Nationality: {driver['nationality']}</h4>"
            )
    return '<h1>No driver with that id</h1>'

if __name__ == '__main__':
    app.run(debug=True)  
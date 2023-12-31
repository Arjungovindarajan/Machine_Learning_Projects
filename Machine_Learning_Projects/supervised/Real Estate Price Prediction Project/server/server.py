from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    responce = jsonify({
        'locations' : util.get_location_names()
    })
    responce.headers.add('Access-Control-Allow-origin', '*')

    return responce

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    responce = jsonify({'estimated_price' : util.get_estimated_price(location,total_sqft,bhk,bath)})
    responce.headers.add('Access-Control-Allow-origin', '*')

    return responce

if __name__ == "__main__":
    print("Starting Python Flask Server for Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()
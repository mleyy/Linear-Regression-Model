import numpy as np
from flask import Flask, render_template, request
import joblib
from src.forms import CarForm
from src.config import Config

# Initialize the Flask app
app = Flask(
    'Car Price Prediction',
    template_folder='templates',  # Simplified folder structure
    static_folder='static'
)
app.config.from_object(Config)  # Load configuration, including SECRET_KEY

# Load the scaler and the model
scaler = joblib.load('src/mlmodel/scaling.pkl')
model = joblib.load('src/mlmodel/car_price_prediction.pkl')

@app.route('/', methods=['GET', 'POST'])
def home():
    car_form = CarForm()
    if car_form.validate_on_submit():
        # Retrieve and preprocess form data
        fuel = 1 if int(car_form.car_fuel.data) == 1 else 0
        transmission = 1 if int(car_form.car_transmission.data) == 1 else 0
        color = 1 if int(car_form.car_color.data) == 1 else 0

        # Prepare input data for prediction
        new_car = np.array([
            car_form.car_odometer.data,
            fuel,
            car_form.car_doors.data,
            transmission,
            car_form.car_horsepower.data,
            color,
            car_form.car_cc.data,
            car_form.car_weight.data,
            car_form.car_age.data
        ]).reshape(1, -1)

        # Scale and predict
        new_car_scaled = scaler.transform(new_car)
        predicted_price = model.predict(new_car_scaled)
        predicted_price = max(0, int(predicted_price))  # Ensure non-negative price

        # Render the result template with the prediction
        return render_template('result.html', price=predicted_price)

    # Render the form if not submitted or invalid
    return render_template('car.html', form=car_form)

# Error handling route (optional, in case of manual errors)
@app.errorhandler(ValueError)
def handle_value_error(e):
    return render_template('error.html'), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=app.config.get('PORT', 9090), debug=True)

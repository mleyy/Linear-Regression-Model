from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, NumberRange

class CarForm(FlaskForm):
    FUEL_TYPE = {'Petrol': 1, 'Diesel': 0}
    TRANSMISSION_TYPE = {'Automatic': 1, 'Manual': 0}
    FUEL_SELECTION = [('1', 'Petrol'), ('0', 'Diesel')]
    TRANSMISSION_SELECTION = [('1', 'Automatic'), ('0', 'Manual')]
    COLOR_SELECTION = [('1', 'Regular'), ('2', 'Metallic')]

    car_age = IntegerField(
        'Car Age (In Years)', 
        validators=[DataRequired(message="Car age is required"), NumberRange(min=0, max=100, message="Car age must be between 0 and 100")]
    )
    car_fuel = SelectField(
        label='Fuel Type', 
        choices=FUEL_SELECTION, 
        validators=[DataRequired(message="Fuel type is required")]
    )
    car_doors = IntegerField(
        'Number of Doors', 
        validators=[DataRequired(message="Number of doors is required"), NumberRange(min=0, max=6, message="Doors must be between 0 and 6")]
    )
    car_cc = IntegerField(
        'Car CC', 
        validators=[DataRequired(message="Car CC is required"), NumberRange(min=1, max=3000, message="Car CC must be between 1 and 3000")]
    )
    car_horsepower = IntegerField(
        'Car HP', 
        validators=[DataRequired(message="Car horsepower is required"), NumberRange(min=1, max=1000, message="Horsepower must be between 1 and 1000")]
    )
    car_transmission = SelectField(
        label='Transmission Type', 
        choices=TRANSMISSION_SELECTION, 
        validators=[DataRequired(message="Transmission type is required")]
    )
    car_odometer = IntegerField(
        'Odometer (in Kilometers)', 
        validators=[DataRequired(message="Odometer reading is required"), NumberRange(min=1, max=10000000, message="Odometer must be between 1 and 10,000,000")]
    )
    car_weight = IntegerField(
        'Car Weight (in Kilograms)', 
        validators=[DataRequired(message="Car weight is required"), NumberRange(min=1, max=10000, message="Weight must be between 1 and 10,000 kg")]
    )
    car_color = SelectField(
        label='Color Type', 
        choices=COLOR_SELECTION, 
        validators=[DataRequired(message="Color type is required")]
    )
    predict = SubmitField('Predict')

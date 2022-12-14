import flask
from flask import render_template
from flask import request
from app.calculator import *
from app.calculator_form import *
import os

SECRET_KEY = os.urandom(32)

ev_calculator_app = flask.Flask(__name__)
ev_calculator_app.config['SECRET_KEY'] = SECRET_KEY


@ev_calculator_app.route('/', methods=['GET', 'POST'])
def operation_result():
    # request.form looks for:
    # html tags with matching "name="

    calculator_form = Calculator_Form(request.form)

    # validation of the form
    if request.method == "POST" and calculator_form.validate():
        # if valid, create calculator to calculate the time and cost
        calculator = Calculator()

        # extract information from the form
        battery_capacity = request.form['BatteryPackCapacity']
        initial_charge = request.form['InitialCharge']
        final_charge = request.form['FinalCharge']
        start_date = request.form['StartDate']
        start_time = request.form['StartTime']
        charger_configuration = request.form['ChargerConfiguration']

        # you may change the logic as your like


        is_peak = calculator.is_peak()

        if is_peak:
            peak_period = calculator.peak_period(start_date)

        is_holiday = calculator.is_holiday(start_date)

        # cost = calculator.cost_calculation(initial_charge, final_charge, battery_capacity, is_peak, is_holiday)

        # time = calculator.time_calculation(initial_charge, final_charge, battery_capacity, power)

        # you may change the return statement also
        
        # values of variables can be sent to the template for rendering the webpage that users will see
        # return render_template('calculator.html', cost = cost, time = time, calculation_success = True, form = calculator_form)
        return render_template('calculator.html', calculation_success=True, form=calculator_form)

    else:
        # battery_capacity = request.form['BatteryPackCapacity']
        # flash(battery_capacity)
        # flash("something went wrong")
        flash_errors(calculator_form)
        return render_template('calculator.html', calculation_success = False, form = calculator_form)

# method to display all errors
def flash_errors(form):
    """Flashes form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            flask.flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'error')

class  Charge_configruation():

    def __init__(self, power, baseprice):
        self.power = power
        self.baseprice = baseprice

configuration1 = Charge_configruation(2, 5)
configuration2 = Charge_configruation(3.6, 7.5)
configuration3 = Charge_configruation(7.2, 10)
configuration4 = Charge_configruation(11, 12.5)
configuration5 = Charge_configruation(22, 15)
configuration6 = Charge_configruation(36, 20)
configuration7 = Charge_configruation(90, 30)
configuration8 = Charge_configruation(350, 50)

if __name__ == '__main__':
    ev_calculator_app.run()

from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TimeField
from wtforms.validators import DataRequired, ValidationError, Optional

# validation for form inputs
class Calculator_Form(FlaskForm):
    # this variable name needs to match with the input attribute name in the html file
    # you are NOT ALLOWED to change the field type, however, you can add more built-in validators and custom messages
    BatteryPackCapacity = StringField("Battery Pack Capacity", [DataRequired()])
    InitialCharge = StringField("Initial Charge", [DataRequired()])
    FinalCharge = StringField("Final Charge", [DataRequired()])
    StartDate = DateField("Start Date", [DataRequired("Data is missing or format is incorrect")], format='%d/%m/%Y')
    StartTime = TimeField("Start Time", [DataRequired("Data is missing or format is incorrect")], format='%H:%M')
    ChargerConfiguration = StringField("Charger Configuration", [DataRequired()])
    PostCode = StringField("Post Code", [DataRequired()])

    # use validate_ + field_name to activate the flask-wtforms built-in validator
    # this is an example for you
    def validate_BatteryPackCapacity(self, field):
        if field.data is None:
            raise ValidationError('Field data is none')
        elif field.data == '':
            raise ValueError("cannot fetch data")
        if float(field.data) < 0:
            raise ValidationError('The Battery Pack Capacity is an Invalid data!!')

    # validate initial charge here
    def validate_InitialCharge(self, field):
        # another example of how to compare initial charge with final charge
        # you may modify this part of the code
        if field.data > self.FinalCharge.data:
            raise ValueError("Initial charge data error")
        if float(field.data)> float(self.FinalCharge.data):
            raise ValueError("The Final charge must larger than the Initial charge!!")
        if float(field.data)>100 or float(field.data)<0:
            raise ValueError("The Initial charge is an invalid data!!")
    # validate final charge here
    def validate_FinalCharge(self, field):
        # two ways
        if field.data == '':
            raise ValidationError('The Final charge can not be empty!!')
        if float(field.data) > 100 or float(field.data) < 0:
            raise ValueError("The Final charge is an invalid data!!")

    # validate start date here
    def validate_StartDate(self, field):
        if field.data =='':
            raise ValidationError('The Start date can not be empty!!')

    # validate start time here
    def validate_StartTime(self, field):
        if field.data =='':
            raise ValidationError('The Start time can not be empty!!')

        hours = field.data.hour
        minutes = field.data.minute
        # The range of time
        if hours <= 0 or hours >24:
            raise ValueError("The time is an invalid data!!")
        if minutes <=0 or minutes > 60:
            raise ValueError("The time is an invalid data!!")

    # validate charger configuration here
    def validate_ChargerConfiguration(self, field):
        if field.data == '':
            raise ValidationError('The Charger configuration can not be empty!!')
        if field.data<1 or field.data>8:
            raise ValueError("The charger configuration is an invalid data!!")

    # validate postcode here
    def validate_PostCode(self, field):
        if field.data == '':
            raise ValidationError('The postcode can not be empty!!')
        if field.data<1000 or field.data>9999:
            raise ValueError("The postcode is an invalid data!!")
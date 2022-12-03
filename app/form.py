from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField
from wtforms.validators import DataRequired, Length, Email

class RegisterPoetForm(FlaskForm):
    username = StringField(label = 'Username', validators=[DataRequired(), Length(1,64)])
    carnet = StringField(label = 'Carnet', validators=[DataRequired(), Length(1,6)])
    career = StringField(label = 'Career', validators=[DataRequired()])
    date_birth = DateField(label='Birthday',validators=[DataRequired()])
    address = StringField(label = 'Address', validators=[DataRequired()])
    email= StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    gender = StringField(label = 'Gender', validators=[DataRequired()])
    poetry_gen = StringField(label = 'Poetry Gender', validators=[DataRequired()])
    phone = StringField(label = 'Phone Number', validators=[DataRequired()])
    phone_country_code = StringField(label = 'Phone Country Code', validators=[DataRequired()])
    submit = SubmitField(label='Submit')
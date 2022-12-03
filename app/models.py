from werkzeug.security import generate_password_hash, check_password_hash
from app.utils.validators import presentation_date_def, presentation_date_epic, presentation_date_dramatic
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy.types import Text

db = SQLAlchemy()

class Poet(db.Model):
    __tablename__ = 'poets'

    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    username = db.Column(db.String(64), nullable = False)
    carnet = db.Column(db.String(6), nullable = False)
    career = db.Column(db.String(64), nullable = False)
    address = db.Column(db.String(64), nullable = False)
    password = db.Column(db.String(256), nullable = False)
    email = db.Column(db.String(128), nullable = False)
    date_birth = db.Column(db.Date)
    presentation_day = db.Column(db.Date, nullable=True)
    phone = db.Column(db.Unicode(255))
    phone_country_code = db.Column(db.Unicode(8))
    gender = db.Column(db.String(256), nullable = False)
    poetry_gen = db.Column(db.String(256), nullable = False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __init__(
        self, username, carnet, career,
        address, password, email, date_birth, 
        phone, phone_country_code, gender,
        poetry_gen
        ):
        self.username = username
        self.career=career
        self.date_birth=date_birth
        self.carnet = carnet
        self.address = address
        self.password = password
        self.email = email
        self.phone = phone
        self.phone_country_code = phone_country_code
        self.gender = gender
        self.poetry_gen = poetry_gen

    def __str__(self):
        return f'Poet {self.id}'

    def set_presentation_day(self):
        if self.carnet[-1] == '1':
            self.presentation_day = presentation_date_dramatic(5, self.created_at)
        elif self.carnet[-1] == '3':
            self.presentation_day = presentation_date_epic(self.created_at)
        else:
            self.presentation_day = presentation_date_def(self.created_at)
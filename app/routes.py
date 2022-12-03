from flask import Flask, render_template, escape, redirect, url_for, jsonify
from .models import db, Poet
import datetime
from .utils import validators
from .form import RegisterPoetForm
from app.utils.dicts import get_dict_all_students, get_dict_students_career, get_dict_students_age, get_dict_students_gender, get_dict_students_presentation_day

app = Flask(__name__, template_folder='res/templates', static_folder='res/static')

@app.route('/', methods=['GET', 'POST'])
def register_form():
    form = RegisterPoetForm()

    if not form.validate_on_submit():
        return render_template('form.html', form=form)

    username = form.username.data
    carnet = form.carnet.data
    career = form.career.data
    date_birth = form.date_birth.data
    address = form.address.data
    email = form.email.data
    password = form.password.data
    gender = form.gender.data
    poetry_gen = form.poetry_gen.data
    phone = form.phone.data
    phone_country_code = form.phone_country_code.data

    if not validators.carnet(carnet):
        return render_template('form.html', form=form)
    if not validators.age(date_birth):
        return render_template('form.html', form=form)
    if not validators.gender(gender):
        return render_template('form.html', form=form)
    if not validators.poetry_gen(poetry_gen):
        return render_template('form.html', form=form)

    poet = Poet(
        username, carnet, career,
        address, password, email, date_birth, 
        phone, phone_country_code, gender,
        poetry_gen
    )
    
    db.session.add(poet)
    db.session.commit()
    
    poet.set_presentation_day()
    db.session.commit()
    return redirect(url_for('register_form'))

@app.route('/students/', methods=['GET'])
def students():
    return jsonify(get_dict_all_students())

@app.route('/students/career/<string:career>/', methods=['GET'])
def students_career(career):
    return jsonify(get_dict_students_career(career))

@app.route('/students/date_birth/<string:date_birth>/', methods=['GET'])
def students_date_birth(date_birth):
    date = datetime.strptime(date_birth)
    return jsonify(get_dict_students_age(date))

@app.route('/students/declamation_date/<string:declamation_date>/', methods=['GET'])
def students_declamation_date(declamation_date):
    date = datetime.strptime(declamation_date)
    return jsonify(get_dict_students_presentation_day(declamation_date))

@app.route('/students/gender/<string:gender>/', methods=['GET'])
def students_gender(gender):
    return jsonify(get_dict_students_gender(gender))
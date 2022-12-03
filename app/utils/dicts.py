from app.models import Poet

def get_dict_all_students(): 
    ret = {
        'students' : [
            {
                'id' : p.id,
                'username' : p.username,
                'carnet' : p.carnet,
                'career' : p.career,
                'address' : p.address,
                'password' : p.password,
                'email' : p.email,
                'date_birth' : p.date_birth,
                'presentation_day' : p.presentation_day,
                'phone' : p.phone,
                'phone_country_code' : p.phone_country_code,
                'gender' : p.gender,
                'poetry_gen' : p.poetry_gen,
                'created_at' : p.created_at
            }
            for p in Poet.query.all()
        ]
    }
    return ret

def get_dict_students_career(career): 
    ret = {
        'students' : [
            {
                'id' : p.id,
                'username' : p.username,
                'carnet' : p.carnet,
                'career' : p.career,
                'address' : p.address,
                'password' : p.password,
                'email' : p.email,
                'date_birth' : p.date_birth,
                'presentation_day' : p.presentation_day,
                'phone' : p.phone,
                'phone_country_code' : p.phone_country_code,
                'gender' : p.gender,
                'poetry_gen' : p.poetry_gen,
                'created_at' : p.created_at
            }
            for p in Poet.query.filter_by(career=career).all()
        ]
    }
    return ret

def get_dict_students_age(date_bird): 
    ret = {
        'students' : [
            {
                'id' : p.id,
                'username' : p.username,
                'carnet' : p.carnet,
                'career' : p.career,
                'address' : p.address,
                'password' : p.password,
                'email' : p.email,
                'date_birth' : p.date_birth,
                'presentation_day' : p.presentation_day,
                'phone' : p.phone,
                'phone_country_code' : p.phone_country_code,
                'gender' : p.gender,
                'poetry_gen' : p.poetry_gen,
                'created_at' : p.created_at
            }
            for p in Poet.query.filter_by(date_birth=date_bird).all()
        ]
    }
    return ret

def get_dict_students_presentation_day(presentation_day): 
    ret = {
        'students' : [
            {
                'id' : p.id,
                'username' : p.username,
                'carnet' : p.carnet,
                'career' : p.career,
                'address' : p.address,
                'password' : p.password,
                'email' : p.email,
                'date_birth' : p.date_birth,
                'presentation_day' : p.presentation_day,
                'phone' : p.phone,
                'phone_country_code' : p.phone_country_code,
                'gender' : p.gender,
                'poetry_gen' : p.poetry_gen,
                'created_at' : p.created_at
            }
            for p in Poet.query.filter_by(presentation_day=presentation_day).all()
        ]
    }
    return ret

def get_dict_students_gender(gender_str): 
    ret = {
        'students' : [
            {
                'id' : p.id,
                'username' : p.username,
                'carnet' : p.carnet,
                'career' : p.career,
                'address' : p.address,
                'password' : p.password,
                'email' : p.email,
                'date_birth' : p.date_birth,
                'presentation_day' : p.presentation_day,
                'phone' : p.phone,
                'phone_country_code' : p.phone_country_code,
                'gender' : p.gender,
                'poetry_gen' : p.poetry_gen,
                'created_at' : p.created_at
            }
            for p in Poet.query.filter_by(gender=gender_str).all()
        ]
    }
    return ret
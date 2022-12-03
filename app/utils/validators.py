import datetime
import calendar

def carnet(carnet_str):
    if len(carnet_str) != 6:
        return False
    
    if not (
        carnet_str[0] == 'A' and 
        carnet_str[2] == '5' and 
        carnet_str[-1] in ['1', '3', '9']):
        return False
    return True

def gender(gender_str):
    if gender_str in ['male', 'female', 'other']:
        return True
    return False 

def age(date):
    today = datetime.date.today()
    if today < date:
        return False

    age=today.year-date.year

    if age < 18:
        print(age)
        return False
    return True

def poetry_gen(poetry_str):
    if poetry_str in ['lyrical', 'epic', 'dramatic']:
        return True
    return False 

def presentation_date_dramatic(next_days, date):
    try: 
        d = datetime.date(date.year, date.month, date.day+next_days)
    except:
        maxday = calendar.monthrange(date.year, date.month)[1]
        complete = maxday-date.day
        subtract = next_days-complete
        d = datetime.date(date.year, date.month+1, subtract)
    while d.weekday() in [7, 8]:
        subtract += 1
        d = datetime.date(date.year, date.month+1, subtract)
    return d


def presentation_date_epic(date):
    maxday = calendar.monthrange(date.year, date.month)[1]
    d = datetime.date(date.year, date.month, maxday)
    while d.weekday() in [7, 8]:
        maxday -= 1
        d = datetime.date(date.year, date.month, maxday)
    return d

def presentation_date_def(date):
    maxday = calendar.monthrange(date.year, date.month)[1]
    if maxday == date.day:
        date = datetime.date(date.year, date.month+1, 1)
    day = date.day
    while date.weekday() != 6:
        day += 1
        date = datetime.date(date.year, date.month, day)
    return date
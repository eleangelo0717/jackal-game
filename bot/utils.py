import datetime

def checkDate(text):
    try:
        d = datetime.datetime.strptime(text, '%Y-%m-%d').date()
    except ValueError:
        return None, 'Неправильный формат даты' 

    delta = (d - datetime.date.today()).days
    if delta <= 0:
        return None, 'Дата уже прошла' 

    if delta > 365:
        return None, 'Введите дату не более чем год от сегодняшней' 

    return d.isoformat(), None

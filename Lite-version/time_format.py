"""
    МОДУЛЬ ДЛЯ ФОРМАТИРОВАНИЯ ВРЕМЕНИ И ДАТЫ
"""

from datetime import datetime, timedelta
import time

def day_translite():
    # перевод дня недели

    # Sun Jan 19 01:59:38 2020
    day = time.ctime(time.time()).split(' ')[0]

    day_dict = {
        'Mon': 'Понедельник',
        'Tue': 'Вторник',
        'Wed': 'Среда',
        'Thu': 'Четверг',
        'Fri': 'Пятница',
        'Sat': 'Суббота',
        'Sun': 'Воскресенье'}
    
    for i in day_dict:
        if day == i:
            day = day_dict[i]

    return day

def time_edit_1():
    """ Форматирование даты """

    data = datetime.now().strftime('%x')
    data = str(data)[3:5]+'.'+str(data)[0:2]+'.'+str(data)[6:8]

    return str(data+' '+day_translite())

def time_edit_2():
    """ Форматирование времени """

    hms = time.ctime(time.time()).split(' ')[3]

    return str('\n'+hms)

def time_edit_3():
        """ время замены """

        return (str((datetime.now()+timedelta(minutes=50))).split(' ')[1])[:-10]

def time_edit_4():
        """ время конца покура """

        return (str((datetime.now()+timedelta(hours=2))).split(' ')[1])[:-10]

def data_period(start_data, end_data):
    """ получаем список дат из периода """
    # start_data and end_data - <class 'datetime.date'>

    period = []
    period.append(start_data)

    if start_data < end_data:

        while period[-1] != end_data:
            future_day = period[-1] + timedelta(days=1)
            period.append(future_day)

        for i in range(len(period)):
            period[i] = str(period[i]).split('-')[2]+'.'+str(period[i]).split('-')[1]+'.'+str(period[i]).split('-')[0][2:]

    else:

        from kivymd.toast import toast
        toast('ОШИБКА: Конечная дата младше начальной!')

    return period
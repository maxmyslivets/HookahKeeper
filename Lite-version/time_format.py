"""
    МОДУЛЬ ДЛЯ ФОРМАТИРОВАНИЯ ВРЕМЕНИ И ДАТЫ
"""

from datetime import datetime
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

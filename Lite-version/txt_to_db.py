import sqlite3 as sql
from uuid import uuid4

with open('hookah_data.txt', 'r') as txt_data:
    
    data_read = txt_data.read().split('\n')
    new_data = []
    key_data = {}
    realtime_key = None
    for i in range(len(data_read)):
        if (data_read[i] == '') or (data_read[i][0] == 'с'):
            continue
        if (data_read[i][2] == '.') or (data_read[i][2] == ','):
            print(data_read[i])
            # разбиваем на дату и день
            data_day = data_read[i].split(' ')
            # в дате убираем с конца 20
            data = data_day[0][:-2]
            # заменяем запятые на точки
            data = list(data)
            for simbol in range(len(data)):
                if data[simbol] == ',':
                    data[simbol] = '.'
            # собираем в дату и день
            data2 = ''
            for f in data:
                data2 += f
            if data_day[1] == '2':
                data_day[1] = 'суббота'
            data_day = str(data2)+' '+str(data_day[1])
            key_data[data_day] = []
            realtime_key = data_day
            continue
        key_data[realtime_key].append(data_read[i])

    for i,j in key_data.items():
        print(i)
        for k in j:
            print(k)

orders = []      
for i,j in key_data.items():
    #print(i, j)
    for k in j:
        orders.append(str(i)+' '+str(k))
orders2 = []
for i in range(len(orders)):
    orders2.append(orders[i].split('\t')[0].split(' ')+orders[i].split('\t')[1:])
    orders2[-1][-2] = int(orders2[-1][-2][:-3])
    if orders2[-1][-1] != 'перезабивка':
        orders2[-1].append(5)
    else:
        orders2[-1].append(0)
    if orders2[-1][-2] == 'вода':
        orders2[-1][-2] = 'Классический'
    if orders2[-1][-2] == 'перезабивка':
        orders2[-1][-2] = 'Замена'




def db_connect(id_order, data, day, time1, tablet, class_hookah, time2, time3, price, share):
    con = sql.connect('test2.db')    # подключиться к БД по адресу или создать, если не существует
    with con:
        cur = con.cursor()  # создание курсора
        cur.execute('CREATE TABLE IF NOT EXISTS HookahOrders ('     # создать таблицу, если не существует
            'id_order TEXT, '   # уникальный 128-битный ID
            'data TEXT, '   # дата добавления заказа
            'day TEXT, '    # день
            'time1 TEXT, '  # время выноса
            'tablet TEXT, ' # стол
            'class_hookah TEXT, '   # вид кальяна
            'time2 TEXT, '  # время смены угля
            'time3 TEXT, '  # время конца покура
            'price INTEGER, '   # цена кальяна
            'share INTEGER)'    # доля кальянного мастера
            )
        
        datafordb = [id_order, data, day, time1, tablet, class_hookah, time2, time3, price, share]        # создание набора данных
        cur.execute(f"INSERT INTO HookahOrders VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", datafordb)  # запись в таблицу
        
        con.commit()
        cur.close()

#for i in orders2:
    #Запись в БД
    #db_connect(str(uuid4()), i[0], i[1], i[3], i[2], i[-2], i[-5], i[-4], i[-3], i[-1])

""" Чтение данных из БД за выбранный период и передача в MDList"""

#self.ids.scrollForDatalist.remove_widget(self.MDL)
#self.ids.scrollForDatalist.add_widget(self.MDL)

con = sql.connect('test.2db')

with con:

    cur = con.cursor()

    cur.execute("SELECT * FROM HookahOrders ORDER BY data")      # чтение с таблицы с сортировкой по колонке даты
    rows = cur.fetchall()   # запись в переменную всего, что пришло из БД
    for row in rows:
        print(row)
    cur.close()

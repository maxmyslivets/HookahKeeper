from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from datetime import datetime
from time_format import time_edit_1, time_edit_2, time_edit_3, time_edit_4
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.picker import MDDatePicker
import sqlite3 as sql


class OrderListItem(OneLineAvatarIconListItem):
    '''Custom list item.'''


class Container(IRightBodyTouch, MDBoxLayout):
    adaptive_width = True


class Home(Screen):

    with open("home.kv", encoding='utf8') as HomeKV:
        Builder.load_string(HomeKV.read())
    
    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs) 

        # Вызов функции time_update() с интервалом в 1 секунду
        Clock.schedule_interval(lambda dt: self.time_update(), .1)
    
    def time_update(self):
        """ Функция обновления времени в time_label """

        self.time_label_1.text = time_edit_1() # дата, день
        self.time_label_2.text = time_edit_2() # время
    
    def add_order(self, table, class_hookah, additive):
        """ Добавление заказа в MDList """

        order = OrderListItem()
        time1, time2, time3 = time_edit_2()[:-3], time_edit_3(), time_edit_4()

        # price class_hookah
        if class_hookah == 'Классический': price = 20
        elif class_hookah == 'С добавками': price = 25
        elif class_hookah == 'На фрукте': price = 35
        elif class_hookah == 'Микс': price = 35
        elif class_hookah == 'Замена': price = 10

        if not additive:
            order.text = table + ' ' + class_hookah + '    ' + time1 + '    ' + time2 + '    ' + time3
            self.add_order_in_database(
                time_edit_1().split(' ')[0],
                time_edit_1().split(' ')[1],
                time1[1:],
                table,
                class_hookah,
                time2,
                time3,
                price,
                5
                )
            
        else:
            order.text = table + ' ' + additive + '    ' + time1 + '    ' + time2 + '    ' + time3
            self.add_order_in_database(
                time_edit_1().split(' ')[0],
                time_edit_1().split(' ')[1],
                time1[1:],
                table,
                additive,
                time2,
                time3,
                price,
                0
                )

        self.ids.mdlist.add_widget(order)
    
    def add_order_in_database(self, data, day, time1, tablet, class_hookah, time2, time3, price, share):
        """ Запись в БД """

        con = sql.connect('test.db')    # подключиться к БД по адресу или создать, если не существует
        with con:
            cur = con.cursor()  # создание курсора
            cur.execute('CREATE TABLE IF NOT EXISTS HookahOrders ('     # создать таблицу, если не существует
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
            datafordb = [data, day, time1, tablet, class_hookah, time2, time3, price, share]        # создание набора данных
            cur.execute(f"INSERT INTO HookahOrders VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", datafordb)  # запись в таблицу

            cur.execute("SELECT * FROM HookahOrders")      # чтение с таблицы
            rows = cur.fetchall()   # запись в переменную всего, что пришло из БД
            for row in rows:
                print(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            
            con.commit()
            cur.close()


class Data(Screen):

    with open("data.kv", encoding='utf8') as DataKV:
        Builder.load_string(DataKV.read())

    min_data = None

    def show_date_picker_1(self):
        MDDatePicker(self.set_previous_date_1).open()

    def set_previous_date_1(self, date_obj):
        date_obj = str(date_obj).split('-')
        self.ids.date_picker_label_1.text = str(date_obj[2])+'.'+str(date_obj[1])+'.'+str(date_obj[0])[2:]
    
    def show_date_picker_2(self):
        MDDatePicker(self.set_previous_date_2).open()

    def set_previous_date_2(self, date_obj):
        date_obj = str(date_obj).split('-')
        self.ids.date_picker_label_2.text = str(date_obj[2])+'.'+str(date_obj[1])+'.'+str(date_obj[0])[2:]


class HookahKeeperApp(MDApp):

    def build(self):

        self.theme_cls.theme_style = "Light"

        sm = ScreenManager()
        sm.add_widget(Home(name='HomeScreen'))
        sm.add_widget(Data(name='DataScreen'))

        return sm


if __name__ == "__main__":
    HookahKeeperApp().run()
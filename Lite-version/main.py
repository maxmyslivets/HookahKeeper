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

        if not additive:
            order.text = table + ' ' + class_hookah + '    ' + time_edit_2()[:-3] + '    ' + time_edit_3() + '    ' + time_edit_4()
            with open('statistic.txt', 'a', encoding='utf8') as stat:
                stat.write(time_edit_1()+' '+time_edit_2()[1:-3]+' '+table+' '+class_hookah+'\n')
        else:
            order.text = table + ' ' + additive + '    ' + time_edit_2()[:-3] + '    ' + time_edit_3() + '    ' + time_edit_4()
            with open('statistic.txt', 'a', encoding='utf8') as stat:
                stat.write(time_edit_1()+' '+time_edit_2()[1:-3]+' '+table+' '+additive+'\n')

        self.ids.mdlist.add_widget(order)
    

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
        print(date_obj)
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
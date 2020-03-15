from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from time_format import time_edit_1, time_edit_2
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox


class OrderListItem(OneLineAvatarIconListItem):
    pass


class ListItemWithCheckbox(OneLineAvatarIconListItem):
    '''Custom list item.'''


class RightCheckbox(IRightBodyTouch, MDCheckbox):
    '''Custom right container.'''


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
    
    def add_order(self, table, cls, additive):
        """ Добавление заказа в MDList """

        order = ListItemWithCheckbox()

        if not additive:
            order.text = table + '    ' + cls + '    ' + time_edit_2()
        else:
            order.text = table + '    ' + additive + '    ' + time_edit_2()

        self.ids.mdlist.add_widget(order)


class HookahKeeperApp(MDApp):

    def build(self):

        #self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"

        sm = ScreenManager()
        sm.add_widget(Home(name='HomeScreen'))

        return sm


if __name__ == "__main__":
    HookahKeeperApp().run()
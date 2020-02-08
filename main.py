from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from libs.time_format import time_edit_1, time_edit_2
from kivy.uix.button import Button


class RootScreen(Screen):

    with open("kv/RootScreen.kv", encoding='utf8') as RootScreenKV:
        Builder.load_string(RootScreenKV.read())
    
    time_label_1 = ObjectProperty()
    time_label_2 = ObjectProperty()
    
    def __init__(self, **kwargs):
        super(RootScreen, self).__init__(**kwargs) 

        # Вызов функции time_update() с интервалом в 1 секунду
        Clock.schedule_interval(lambda dt: self.time_update(), .1)
    
    def time_update(self):
        """ Функция обновления времени в time_label """

        self.time_label_1.text = time_edit_1() # дата, день
        self.time_label_2.text = time_edit_2() # время


    def func(self, txt):
        print(txt)


class AddHookahScreen(Screen):

    with open("kv/AddHookahScreen.kv", encoding='utf8') as AddHookahScreenKV:
        Builder.load_string(AddHookahScreenKV.read())


class HookahSferaClubApp(MDApp):

    def build(self):

        sm = ScreenManager()
        sm.add_widget(RootScreen(name='Root Screen'))
        sm.add_widget(AddHookahScreen(name='Add Hookah Screen'))
        
        return sm


if __name__ == '__main__':

    HookahSferaClubApp().run()

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.uix.button import Button
from libs.time_format import time_edit_1, time_edit_2


class RootScreen(Screen):

    with open("RootScreen.kv", encoding='utf8') as RootScreenKV:
        Builder.load_string(RootScreenKV.read())

    def func(self, txt):
        print(txt)
        self.manager.current = 'Add Hookah Screen'
    
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


class AddHookahScreen(Screen):

    with open("AddHookahScreen.kv", encoding='utf8') as AddHookahScreenKV:
        Builder.load_string(AddHookahScreenKV.read())

    def functwo(self):
        self.manager.current = 'Root Screen'


class HookahSferaClubApp(MDApp):

    def build(self):

        #self.root = Builder.load_string(kv_code)

        sm = ScreenManager()
        sm.add_widget(RootScreen(name='Root Screen'))
        sm.add_widget(AddHookahScreen(name='Add Hookah Screen'))
        
        return sm


if __name__ == '__main__':

    HookahSferaClubApp().run()

# -*- coding: utf-8 -*-


from kivymd.app import MDApp
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import time
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivy.uix.modalview import ModalView


Config.set('graphics', 'fullscreen', 'auto')


with open("myHookah.kv", encoding='utf8') as f:
    drunk = Builder.load_string(f.read())


class RootLayout(BoxLayout):

    time_label = ObjectProperty()

    def __init__(self, **kwargs):  
        super(RootLayout, self).__init__(**kwargs) 

        # функция вызова функции time_update() с интервалом в 1 секунду
        Clock.schedule_interval(lambda dt: self.time_update(), .1)
    
    """
    функция обновления времени в time_label
    """
    def time_update(self):

        # забираем из модуля time значение времени "Wed Jan  8 13:27:34 2020"
        # в time_label.text выводим [11:19] => "13:27:34"
        self.time_label.text = time.ctime(time.time())[0:11] + '\n' + time.ctime(time.time())[11:19]


class AddHokahWindow(BoxLayout):
    pass


class ClassicHookah(BoxLayout):
    
    classic_time = ObjectProperty()

    def __init__(self, **kwargs):  
        super(ClassicHookah, self).__init__(**kwargs)

        self.classic_time.text = time.ctime(time.time())[11:16]
        self.classic_stol_number.text = stol_number


class AdditiveHookah(BoxLayout):
    pass


class FruitHookah(BoxLayout):
    pass


class MixHookah(BoxLayout):
    pass


class ReplacementHookah(BoxLayout):
    pass


class HookahSferaClubApp(MDApp):

    def build(self):
        
        return RootLayout()
    
    def win_min(self):
        Config.set('graphics', 'window_state', 'minimized')

    def add_hookah_window(self):
        add_win = ModalView(size_hint=(None, None), size=(340, 400))
        add_win.add_widget(AddHokahWindow())
        add_win.open()
    
    def classic_hookah(self):
        add_1 = ModalView(size_hint=(None, None), size=(340, 400))
        add_1.add_widget(ClassicHookah())
        add_1.open()
    
    def additive_hookah(self):
        add_2 = ModalView(size_hint=(None, None), size=(340, 400))
        add_2.add_widget(AdditiveHookah())
        add_2.open()
    
    def fruit_hookah(self):
        add_3 = ModalView(size_hint=(None, None), size=(340, 400))
        add_3.add_widget(FruitHookah())
        add_3.open()
    
    def mix_hookah(self):
        add_4 = ModalView(size_hint=(None, None), size=(340, 400))
        add_4.add_widget(MixHookah())
        add_4.open()
    
    def replacement_hookah(self):
        add_5 = ModalView(size_hint=(None, None), size=(340, 400))
        add_5.add_widget(ReplacementHookah())
        add_5.open()
    
    def global_value_number_stol(self, data):
        global stol_number 
        stol_number = data


if __name__ == '__main__':
    HookahSferaClubApp().run()

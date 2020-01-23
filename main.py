# -*- coding: utf-8 -*-


from kivymd.app import MDApp
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivy.uix.modalview import ModalView
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.list import IRightBodyTouch
from datetime import datetime
import time


Config.set('graphics', 'fullscreen', 'auto')


with open("myHookah.kv", encoding='utf8') as f:
    """ Данный метод прочтения файла .kv выбран для
    возможности прочтения Кириллицы в кодировке utf8 """

    drunk = Builder.load_string(f.read())


class RootLayout(BoxLayout):
    """ Главное окно """

    time_label_1 = ObjectProperty()
    time_label_2 = ObjectProperty()

    type_1 = ObjectProperty()

    """
    type_2 = ObjectProperty()
    type_3 = ObjectProperty()
    type_4 = ObjectProperty()
    type_5 = ObjectProperty()
    type_6 = ObjectProperty()
    type_7 = ObjectProperty()
    type_8 = ObjectProperty()
    type_9 = ObjectProperty()
    """

    time_1 = ObjectProperty()
    """
    time_2 = ObjectProperty()
    time_3 = ObjectProperty()
    """

    def __init__(self, **kwargs):
        super(RootLayout, self).__init__(**kwargs) 

        # Вызов функции time_update() с интервалом в 1 секунду
        Clock.schedule_interval(lambda dt: self.time_update(), .1)
    
    
    def time_update(self):
        """ Функция обновления времени в time_label """

        # в time_label.text из time_edit выводим дату и время
        self.time_label_1.text = self.time_edit_1()
        self.time_label_2.text = self.time_edit_2()


    def day_translite(self):
        # перевод дня недели

        # Sun Jan 19 01:59:38 2020
        day = time.ctime(time.time()).split(' ')[0]

        day_dict = {
            'Thu': 'Четверг',
            'Sun': 'Воскресенье'}
        
        for i in day_dict:
            if day == i:
                day = day_dict[i]

        return day

    def time_edit_1(self):
        """ Форматирование даты """

        data = datetime.now().strftime('%x')
        data = str(data)[0:2]+'.'+str(data)[3:5]+'.'+str(data)[6:8]

        return str(data+' '+self.day_translite())

    def time_edit_2(self):
        """ Форматирование времени """

        hms = time.ctime(time.time()).split(' ')[3]

        return str('\n'+hms)

    hookah_list = ObjectProperty()
    text_hookah = ObjectProperty()
    
    def stol_add_data(self, stol_number_add_hookah, type_add_hookah, time_add_hookah):
        """ Передача указанного типа кальяна и времени подачи
        в label указанного стола """

        # Add hookah data in hookah_list
        # XXX hookah_list.add_widget(DataForHookahList(self.text_hookah.text = type_add_hookah))

        # FIXME: Не добавляется в label стола.
        # P.S. Если прописать код в time_update, то все работает

        if stol_number_add_hookah == '1':
            self.type_1.text = type_add_hookah
            self.time_1.text = time_add_hookah
            
            print (stol_number_add_hookah,
            type_add_hookah,
            time_add_hookah)


class IconRightSampleWidget(IRightBodyTouch, MDCheckbox):
    pass


class DataForHookahList():
    pass


class AddHokahWindow(BoxLayout):
    """ Модальное окно выбора вида кальяна """

    pass


class ClassicHookah(BoxLayout):
    """ Модальное окно с информацией и кнопкой для
    подтверждения добавления заказа 'Классический' """
    
    time_add = ObjectProperty()
    stol_number = ObjectProperty()


    def __init__(self, **kwargs):  
        super(ClassicHookah, self).__init__(**kwargs)

        self.time_add.text = time.ctime(time.time())[11:16]
        self.stol_number.text = stol_number


class AdditiveHookah(BoxLayout):
    """ Модальное окно с информацией и кнопкой для
    подтверждения добавления заказа 'С добавками' """

    pass


class FruitHookah(BoxLayout):
    """ Модальное окно с информацией и кнопкой для
    подтверждения добавления заказа 'На фрукте' """

    pass


class MixHookah(BoxLayout):
    """ Модальное окно с информацией и кнопкой для
    подтверждения добавления заказа 'Микс' """

    pass


class ReplacementHookah(BoxLayout):
    """ Модальное окно с информацией и кнопкой для
    подтверждения добавления заказа 'Замена чаши' """

    pass


class HookahSferaClubApp(MDApp):


    def build(self):
        
        return RootLayout()


    def win_min(self):
        """" При нажатии кнопки сворачивания окна """
        # FIXME: Не сворачивается окно

        Config.set('graphics', 'window_state', 'minimized')


    def add_hookah_window(self):
        """ При нажатии на стол появляется это модальное окно
        в котором указаны виды кальяна для выбора """

        global add_win
        add_win = ModalView(size_hint=(None, None), size=(340, 400))
        add_win.add_widget(AddHokahWindow())
        add_win.open()
    

    def stol_data(self, stol_number_add_hookah, time_add_hookah, type_add_hookah):

        """ Функция, которая передает на label стола
        вид кальяна, время замены угля, время конца покура """
        RootLayout().stol_add_data(stol_number_add_hookah, type_add_hookah, time_add_hookah)

        add_1.dismiss()

    """ При нажатии на вид кальяна появляется одно из этих модальных окон,
    в которых указаны: вид кальяна, время подачи, цена, стол """
    
    def classic_hookah(self):

        global add_1

        add_1 = ModalView(size_hint=(None, None), size=(340, 400))
        add_1.add_widget(ClassicHookah())

        add_1.open()
        add_win.dismiss()
        
    
    def additive_hookah(self):

        add_2 = ModalView(size_hint=(None, None), size=(340, 400))
        add_2.add_widget(AdditiveHookah())

        add_2.open()
        add_win.dismiss()
    

    def fruit_hookah(self):

        add_3 = ModalView(size_hint=(None, None), size=(340, 400))
        add_3.add_widget(FruitHookah())

        add_3.open()
        add_win.dismiss()
    

    def mix_hookah(self):

        add_4 = ModalView(size_hint=(None, None), size=(340, 400))
        add_4.add_widget(MixHookah())

        add_4.open()
        add_win.dismiss()
    

    def replacement_hookah(self):

        add_5 = ModalView(size_hint=(None, None), size=(340, 400))
        add_5.add_widget(ReplacementHookah())

        add_5.open()
        add_win.dismiss()
    

    def global_value_number_stol(self, data):

        global stol_number 
        stol_number = data


if __name__ == '__main__':

    HookahSferaClubApp().run()

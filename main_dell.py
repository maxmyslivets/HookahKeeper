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
from kivymd.uix.list import OneLineAvatarIconListItem
from datetime import datetime
import time


Config.set('graphics', 'fullscreen', 'auto')


with open("myHookah_dell.kv", encoding='utf8') as f:
    """ Данный метод прочтения файла .kv выбран для
    возможности прочтения Кириллицы в кодировке utf8 """

    kv_txt = f.read()


class RootLayout(BoxLayout):
    """ Главное окно """

    time_label_1 = ObjectProperty()
    time_label_2 = ObjectProperty()

    type_1 = ObjectProperty()
    type_2 = ObjectProperty()
    type_3 = ObjectProperty()
    type_4 = ObjectProperty()
    type_5 = ObjectProperty()
    type_6 = ObjectProperty()
    type_7 = ObjectProperty()
    type_8 = ObjectProperty()
    type_9 = ObjectProperty()
    type_10 = ObjectProperty()
    type_11 = ObjectProperty()
    type_12 = ObjectProperty()
    type_13 = ObjectProperty()
    type_14 = ObjectProperty()
    type_15 = ObjectProperty()
    type_16 = ObjectProperty()
    type_17 = ObjectProperty()
    type_18 = ObjectProperty()
    type_19 = ObjectProperty()
    type_20 = ObjectProperty()
    type_21 = ObjectProperty()
    type_22 = ObjectProperty()
    type_23 = ObjectProperty()
    type_24 = ObjectProperty()
    type_25 = ObjectProperty()
    type_B = ObjectProperty()
    type_K = ObjectProperty()

    time_1 = ObjectProperty()
    time_2 = ObjectProperty()
    time_3 = ObjectProperty()
    time_4 = ObjectProperty()
    time_5 = ObjectProperty()
    time_6 = ObjectProperty()
    time_7 = ObjectProperty()
    time_8 = ObjectProperty()
    time_9 = ObjectProperty()
    time_10 = ObjectProperty()
    time_11 = ObjectProperty()
    time_12 = ObjectProperty()
    time_13 = ObjectProperty()
    time_14 = ObjectProperty()
    time_15 = ObjectProperty()
    time_16 = ObjectProperty()
    time_17 = ObjectProperty()
    time_18 = ObjectProperty()
    time_19 = ObjectProperty()
    time_20 = ObjectProperty()
    time_21 = ObjectProperty()
    time_22 = ObjectProperty()
    time_23 = ObjectProperty()
    time_24 = ObjectProperty()
    time_25 = ObjectProperty()
    time_B = ObjectProperty()
    time_K = ObjectProperty()

    hookah_list = ObjectProperty()

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

    def time_edit_1(self):
        """ Форматирование даты """

        data = datetime.now().strftime('%x')
        data = str(data)[0:2]+'.'+str(data)[3:5]+'.'+str(data)[6:8]

        return str(data+' '+self.day_translite())

    def time_edit_2(self):
        """ Форматирование времени """

        hms = time.ctime(time.time()).split(' ')[3]

        return str('\n'+hms)

    text_hookah = ObjectProperty()

    #from kivy.factory import Factory
    
    def stol_add_data(self, hookah_list, stol_number_add_hookah, type_add_hookah, time_add_hookah):
        """ Передача указанного типа кальяна и времени подачи
        в label указанного стола """

        print('работает stol_add_data')
        # Создание списка столов
        list_stol = list()
        for i in range(25):
            list_stol.append(str(i+1))
        list_stol.append('Б')
        list_stol.append('К')

        for i in list_stol:
            if stol_number_add_hookah == i:
                self.type_1.text = type_add_hookah
                self.time_1.text = time_add_hookah
                
                print (stol_number_add_hookah,
                type_add_hookah,
                time_add_hookah, '+00:50 +02:00')

        # Add hookah data in hookah_list
        #hookah_list.add_widget(DataForHookahList())
        hookah_list.add_widget(OneLineAvatarIconListItem(text='add ...')) # add add_widget
        # FIXME: Не добавляется в label стола.
        # P.S. Если прописать код в time_update, то все работает


class IconRightSampleWidget(IRightBodyTouch, MDCheckbox):
    pass

#from kivymd.list.OneLineAvatarIconListItem import OneLineAvatarIconListItem

class DataForHookahList(BoxLayout):
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

    time_add = ObjectProperty()
    stol_number = ObjectProperty()


    def __init__(self, **kwargs):  
        super(AdditiveHookah, self).__init__(**kwargs)

        self.time_add.text = time.ctime(time.time())[11:16]
        self.stol_number.text = stol_number


class FruitHookah(BoxLayout):
    """ Модальное окно с информацией и кнопкой для
    подтверждения добавления заказа 'На фрукте' """

    time_add = ObjectProperty()
    stol_number = ObjectProperty()


    def __init__(self, **kwargs):  
        super(FruitHookah, self).__init__(**kwargs)

        self.time_add.text = time.ctime(time.time())[11:16]
        self.stol_number.text = stol_number


class MixHookah(BoxLayout):
    """ Модальное окно с информацией и кнопкой для
    подтверждения добавления заказа 'Микс' """

    time_add = ObjectProperty()
    stol_number = ObjectProperty()


    def __init__(self, **kwargs):  
        super(MixHookah, self).__init__(**kwargs)

        self.time_add.text = time.ctime(time.time())[11:16]
        self.stol_number.text = stol_number


class ReplacementHookah(BoxLayout):
    """ Модальное окно с информацией и кнопкой для
    подтверждения добавления заказа 'Замена чаши' """

    time_add = ObjectProperty()
    stol_number = ObjectProperty()


    def __init__(self, **kwargs):  
        super(ReplacementHookah, self).__init__(**kwargs)

        self.time_add.text = time.ctime(time.time())[11:16]
        self.stol_number.text = stol_number


class HookahSferaClubApp(MDApp):


    def build(self):
        Builder.load_string(kv_txt)
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
    

    def stol_data(self, hookah_list, stol_number_add_hookah, time_add_hookah, type_add_hookah):

        """ Функция, которая передает на label стола
        вид кальяна, время замены угля, время конца покура """
        print('работает stol_data')
        RootLayout().stol_add_data(hookah_list, stol_number_add_hookah, type_add_hookah, time_add_hookah)

        if type_add_hookah == 'Классический':
            add_1.dismiss()
        if type_add_hookah == 'С добавками':
            add_2.dismiss()
        if type_add_hookah == 'На фрукте':
            add_3.dismiss()
        if type_add_hookah == 'Микс':
            add_4.dismiss()
        if type_add_hookah == 'Замена чаши':
            add_5.dismiss()

    """ При нажатии на вид кальяна появляется одно из этих модальных окон,
    в которых указаны: вид кальяна, время подачи, цена, стол """
    
    def classic_hookah(self):

        global add_1

        add_1 = ModalView(size_hint=(None, None), size=(340, 400))
        add_1.add_widget(ClassicHookah())

        add_1.open()
        add_win.dismiss()
        
    
    def additive_hookah(self):

        global add_2

        add_2 = ModalView(size_hint=(None, None), size=(340, 400))
        add_2.add_widget(AdditiveHookah())

        add_2.open()
        add_win.dismiss()
    

    def fruit_hookah(self):

        global add_3

        add_3 = ModalView(size_hint=(None, None), size=(340, 400))
        add_3.add_widget(FruitHookah())

        add_3.open()
        add_win.dismiss()
    

    def mix_hookah(self):

        global add_4

        add_4 = ModalView(size_hint=(None, None), size=(340, 400))
        add_4.add_widget(MixHookah())

        add_4.open()
        add_win.dismiss()
    

    def replacement_hookah(self):

        global add_5

        add_5 = ModalView(size_hint=(None, None), size=(340, 400))
        add_5.add_widget(ReplacementHookah())

        add_5.open()
        add_win.dismiss()
    

    def global_value_number_stol(self, data):

        global stol_number 
        stol_number = data


if __name__ == '__main__':

    HookahSferaClubApp().run()

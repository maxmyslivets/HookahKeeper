from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button


with open("myHookah.kv", encoding='utf8') as kv:
    """ Данный метод прочтения файла .kv выбран для
    возможности прочтения Кириллицы """

    kv_code = kv.read()


class RootScreen(Screen):

    def func(self, txt):
        
        print(txt)
        self.manager.current = 'Add Hookah Screen'

class AddHookahScreen(Screen):

    def functwo(self):
        print('+++', txt)
        self.manager.current = 'Root Screen'


class HookahSferaClubApp(MDApp):

    def build(self):

        self.root = Builder.load_string(kv_code)

        sm = ScreenManager()
        sm.add_widget(RootScreen(name='Root Screen'))
        sm.add_widget(AddHookahScreen(name='Add Hookah Screen'))
        
        return sm


if __name__ == '__main__':

    HookahSferaClubApp().run()

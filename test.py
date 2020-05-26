from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.properties import ObjectProperty


class ButCats(Button):
    pass

class Home(Screen):

    with open("test.kv", 'r') as DataKV:
        Builder.load_string(DataKV.read())
    
    def add_func(self):
        Button_a2 = ButCats()
        Button_a2.id = 'a2'
        self.ids.list_a2.add_widget(Button_a2)
        #pass
    
    def remove_func(self):
        self.ids.list_a2.remove_widget(self.ids.a2)

class TestApp(MDApp):

    def build(self):

        sm = ScreenManager()
        sm.add_widget(Home(name='HomeScreen'))

        return sm


if __name__ == "__main__":
    TestApp().run()
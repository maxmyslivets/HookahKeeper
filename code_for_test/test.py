from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button


Builder.load_string("""
<HomeScreen>:

    grid_layout: grid_layout
    bl: bl

    BoxLayout:
        orientation: 'vertical'

        AnchorLayout:
            size_hint_y: .2

            Button:

        GridLayout:
            id: grid_layout

            # Здесь нужно много кнопок (например 4)

            rows: 2
            cols: 2
            spacing: 10
        
        BoxLayout:
            id: bl


""")


class HomeScreen(Screen):

    grid_layout = ObjectProperty()

    def func(self):
        
        for i in range(4):
            table_button = Button(text=str(i+1))
            self.grid_layout.add_widget(table_button)
    
    bl = ObjectProperty()

    def on_kv_post(self):
        self.bl.add_widget(Button)


class RootApp(MDApp):

    def build(self):
        
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='Home Screen'))

        return sm


if __name__ == "__main__":
    RootApp().run()
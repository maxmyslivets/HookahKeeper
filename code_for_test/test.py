from kivymd.app import MDApp
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

def crya(instance):
    print(instance.text)

class RootApp(MDApp):
    def build(self):

        bx = GridLayout(
            rows=9,
            cols=3,
            spacing=10,
            padding=40)
        
        for table_number in range(27):
            
            table_button = Button(text=str(table_number+1))
            table_button.bind(on_release=crya)

            bx.add_widget(table_button)

        return bx

if __name__ == "__main__":
    RootApp().run()
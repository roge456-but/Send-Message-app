from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from utils.uix import U_button
name = "Userinfo1"
class View(Screen):
    def __init__(self, **kwargs):
        super(View, self).__init__(**kwargs)
        self.name = name
        self.add_widget(U_button(text="菜单栏"))

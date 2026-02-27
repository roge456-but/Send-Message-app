from kivy.config import Config
Config.set("graphics", "width", "400")
Config.set("graphics", "height", "773")
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivy.core.text import LabelBase
from index import Index_veiw
from index import Userinfo1




from kivy.core.window import Window
from kivy.utils import get_color_from_hex

route_view = {
    Index_veiw.name: Index_veiw.View(),
    Userinfo1.name: Userinfo1.View(),

}

LabelBase.register(name="Roboto", fn_regular="font/simkai.ttf", fn_bold="font/simsun.ttc")
class Message_Client_App(App):
    def __init__(self):
        super().__init__()
        self.body = ScreenManager(transition=NoTransition())
        Window.clearcolor = get_color_from_hex('FFFFFF')

    def build(self):
        return self.body

    def on_start(self):
        for screen_name, screen_view in route_view.items():
            self.body.add_widget(screen_view)
        self.body.current = Userinfo1.name

Main = Message_Client_App()
Main.run()
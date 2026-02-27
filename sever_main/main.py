from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

# 定义两个屏幕，一个作为首页，一个作为用户页
class LoginScreen(Screen):
    pass

class UserScreen(Screen):
    pass

class Message_Client_App(App):
    def __init__(self):
        super().__init__()
        self.body = ScreenManager()
        # 注册两个屏幕到 ScreenManager，并分配名字
        self.body.add_widget(LoginScreen(name='login'))
        self.body.add_widget(UserScreen(name='user'))

    def build(self):
        return self.body

    def on_start(self):
        # 启动时自动切换到登录页
        self.body.current = 'login'

Main = Message_Client_App()
Main.run()
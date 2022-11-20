from kivy import Config
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '500')

class Signin(BoxLayout):
        pass

class Login(App):
    pass
Login().run()
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from dashboard import DashBoard
from settingscreen import SettingScreen

Window.size = (300, 500)


class DemoApp(MDApp):

    def build(self):
        self.title = "my primary app"
        self.theme_cls.primary_palette = "Green"
        return Builder.load_file("main.kv")


DemoApp().run()

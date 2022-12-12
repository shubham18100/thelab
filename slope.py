from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
Window.size = (310, 500)


class Slope(MDApp):

    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add.widget(Builder.load_file("main.kv"))
        screen_manager.add_widget(Builder.load.file("login1.kv"))
        screen_manager.add_widget(Builder.load_file("signup.kv"))
        return screen_manager


if __name__ == "__main__":
    LabelBase.register(name="MPoppins",fn_regular ="")
    LabelBase.register(name="BPoppins",fn_regular ="")

    Slope().run()
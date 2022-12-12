from kivy.app import App 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import AsyncImage


class shubham(GridLayout):
    pass

class LabApp(App):
    def build(self):
        return AsyncImage(source ='C:\Users\Subham\OneDrive\Pictures\2021-07\IMG_20211018_200545.jpg' )
LabApp().run()
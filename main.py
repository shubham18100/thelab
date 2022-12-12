from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button  
from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(100):
            b = Button(text=str(i+1), size_hint = (.2,.2))
            self.add_widget(b)

#class GridLayoutExample(GridLayout):
#    pass
class AnchorlayoutExample(AnchorLayout):
    pass 

class Box1(BoxLayout):
    pass
'''    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "horizontal"
        b1= Button(text="shubham")
        b2= Button(text="success")
        b3= Button(text="success")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
'''
class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()
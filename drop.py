import kivy
from kivy.app import App

kivy.require("1.9.0")
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp

dropdown = DropDown()
for index in range(7): 
    btn = Button(
        text="Help %d" % index,
        background_color=(1, 0.5, 255),
        size_hint_y=None,
        height=50,
    )
    btn.bind(on_release=lambda btn: dropdown.select(btn.text))
    dropdown.add_widget(btn)
mainbutton = Button(
    text="Menu",
    font_size=30,
    background_color=(1, 0, 255),
    size_hint=(None, None),
    height=60,
    width=150,
    pos=(15, 500),)
mainbutton.bind(on_release=dropdown.open)
dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, "text", x))
runTouchApp(mainbutton)
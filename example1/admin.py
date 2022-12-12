from kivy.lang import Builder 
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp


class MainApp(MDApp):
    def build(self):

        screen = Screen()
        table = MDDataTable(
            pos_hint = {'center_x': 0.5,'center_y':0.5},          
            size_hint =(0.9,0.6),

            check = True,
            column_data = [
                ("First Name",dp(30)),
                ("Last Name",dp(30)),
                ("Email Address",dp(30)),
                ("Phone Numbers",dp(30))
            ],
            row_data = [
                ("ram", "yadav", "yadav@gamil.com", "623869362"),
                ("syam", "singh", "singh@gamil.com", "623379892"),
                ("raju", "sahu", "sahu@gamil.com", "639846868"),
            ]

            )

        table.bind(on_check_press=self.checked)
        table.bind(on_row_press=self.row_checked)


        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        #return Builder.load_file('table.kv')
        screen.add_widget(table)
        return screen

    def checked(self, instance_table , current_row):
        print(instance_table, current_row)

    def row_checked(self, instance_table, instance_row):
        print(instance_table, instance_row)

MainApp().run()
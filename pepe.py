# Листинг 2.13
from kivy.app import App

class Basic_Class(App):
    pass

My_App = Basic_Class()
My_App.run()

# # Листинг 2.14
# Label:
#     text: 'Метка из файла basic_class.kv'
#     font_size: '16pt'

# Листинг 2.15
from kivy.app import App
from kivy.lang import Builder

kv_file = Builder.load_file("./basic_class.kv")

class Basic_Class(App):
    def build(self):
        return kv_file

# Листинг 2.16
from kivy.app import App
from kivy.lang import Builder

kv_file = Builder.load_file("./KV_file/main_screen.kv")

class Basic_Class(App):
    def build(self):
        return kv_file

My_App = Basic_Class()
My_App.run()

# # Листинг 2.17
# Label:
#     text: 'Метка из файла ./KV_file/main_screen.kv'
#     font_size: '16pt'

# Листинг 2.18
from kivy.app import App
from kivy.lang import Builder

my_str = """
Label:
    text: 'Загрузка метки из текстовой строки'
    font_size: '16pt'
"""

kv_str = Builder.load_string(my_str)

class Basic_Class(App):
    def build(self):
        return kv_str

My_App = Basic_Class()
My_App.run()


# Листинг 2.19
from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        L = Label(text='Это текст', font_size=50)
        return L

MainApp().run()

# Листинг 2.20
from kivy.app import App
from kivy.lang import Builder

KV = """
Label:
    text: 'Это текст'
    font_size: 50
"""

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()

# Листинг 2.21
from kivy.app import App
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        btn = Button(text='Это кнопка', font_size=50)
        return btn

MainApp().run()

# Листинг 2.22
from kivy.app import App
from kivy.lang import Builder

KV = """
Button:
    text: 'Это кнопка'
    font_size: 50
"""

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()

# Листинг 2.23
from kivy.app import App
from kivy.uix.checkbox import CheckBox

class MainApp(App):
    def build(self):
        checkbox = CheckBox()
        return checkbox

MainApp().run()

# Листинг 2.24
from kivy.app import App
from kivy.lang import Builder

KV = """
CheckBox:
"""

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()
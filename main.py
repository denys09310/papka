import kivy

kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class MyApp(App):

    def build(self):
        text = Label(text='Hello world')
        btn = Button(text ='fjgsfbcdvyugzjbutydjybryzejr', size_hint = (1, None), height = '30sp')
        btn.on_press = self.click
        col = BoxLayout(orientation = "vertical", size_hint = (0.8,0.8), pos_hint = {'center_x': 0.5, 'center_y' : 0.5})
        col.add_widget(text)
        col.add_widget(btn)
        return col
    def click(self):
        print("klick")

if __name__ == '__main__':
    MyApp().run() 
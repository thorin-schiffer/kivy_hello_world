from kivy.app import App
from kivy.uix.screenmanager import ScreenManager


class HelloWidget(ScreenManager):
    pass


class HelloWorldApp(App):
    def build(self):
        return HelloWidget()


from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)



app = HelloWorldApp()
app.run()

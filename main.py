from kivy.app import App
from kivy.uix.screenmanager import ScreenManager


class HelloWidget(ScreenManager):
    pass


class HelloWorldApp(App):
    def build(self):
        return HelloWidget()


app = HelloWorldApp()
app.run()

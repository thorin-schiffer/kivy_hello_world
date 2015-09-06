from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout


class HelloWidget(AnchorLayout):
    pass


class HelloWorldApp(App):
    def build(self):
        return HelloWidget()


app = HelloWorldApp()
app.run()

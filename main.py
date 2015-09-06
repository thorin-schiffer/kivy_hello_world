from kivy.app import App


class HelloWorldApp(App):
    def build(self):
        from kivy.uix.label import Label
        return Label(text="Hello world!")

app = HelloWorldApp()
app.run()

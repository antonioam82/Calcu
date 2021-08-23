from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.size = (350, 550)

class CalculatorWidget(Widget):
    pass

class CalculatorApp(App):
    def built(self):
        return CalculatorWidget()

if __name__=="__main__":
    CalculatorApp().run()

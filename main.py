from kivy.app import App
from kivy.uix.label import Label

class DieAgainApp(App):
    def build(self):
        return Label(text='ARZUM DIE AGAIN - SIFRE: HILALIYE')

if __name__ == '__main__':
    DieAgainApp().run()
  

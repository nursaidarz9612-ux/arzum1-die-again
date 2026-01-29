from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget

Builder.load_string('''
<LoginScreen>:
    canvas.before:
        Color:
            rgba: 0.1, 0.1, 0.2, 1
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation: 'vertical'
        padding: 50
        spacing: 20
        Label:
            text: "ARZUM DIE AGAIN"
            font_size: '30sp'
            bold: True
        TextInput:
            id: pass_input
            hint_text: "SIFREYI GIRIN"
            password: True
            size_hint_y: None
            height: '50dp'
            multiline: False
        Button:
            text: "OYUNA GIR"
            background_color: 0, 0.8, 0, 1
            on_press: root.check_password()
            size_hint_y: None
            height: '60dp'

<GameScreen>:
    DieAgainGame:
        id: game_widget

<DieAgainGame>:
    canvas:
        Color:
            rgba: 0.7, 0.8, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
        Color:
            rgba: 1, 0, 0, 1
        Rectangle:
            pos: self.player_x, self.player_y
            size: 40, 40
        Color:
            rgba: 0, 0, 0, 1
        Rectangle:
            pos: 0, 100
            size: 2000, 20
''')

class LoginScreen(Screen):
    def check_password(self):
        if self.ids.pass_input.text == "HİLALİYE":
            self.manager.current = 'game'

class GameScreen(Screen):
    def on_enter(self):
        self.ids.game_widget.start()

class DieAgainGame(Widget):
    player_x = NumericProperty(100)
    player_y = NumericProperty(120)
    def start(self, *args):
        Clock.schedule_interval(self.update, 1.0/60.0)
    def update(self, dt):
        self.player_x += 3

class DieAgainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(GameScreen(name='game'))
        return sm

if __name__ == '__main__':
    DieAgainApp().run()
  

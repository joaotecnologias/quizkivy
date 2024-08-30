from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDButton
from kivy.uix.popup import Popup


KV = '''
ScreenManager:
    HomeScreen:
    QuizScreen:
    
    
<HomeScreen>:
    name: 'login'
    MDFloatLayout:
    
        md_bg_color: self.theme_cls.backgroundColor

    Label:
        text: 'Bem Vindo!'
        pos_hint: {'center_y': .7}
        halign: 'center'
        font_size: '28sp'
        bold: True
        color: rgba(255, 65, 46, 255)

    MDButton:
        style: 'elevated'
        pos_hint: {'center_x': .34, 'center_y': .4}
        on_release: app.tela_quiz()

        MDButtonIcon:
            icon: 'play'

        MDButtonText:
            text: 'Começar'

    MDButton:
        style: "elevated"
        pos_hint: {'center_x': .69, 'center_y': .4}
        on_release: app.stop()
        MDButtonIcon:
            icon: 'close'
        MDButtonText:
            text:'Sair'


<QuizScreen>:
    name: 'quiz'
    MDFloatLayout:
        md_bg_color: [108/255, 255/255, 133/255, 1]
        MDBoxLayout:
            orientation: 'horizontal'
            spacing: 10
            padding: 10
            size_hint: (None, None)  
            size: (490, 250)  
            pos_hint: {'center_x': 0.5, 'center_y': 0.64}

            canvas.before:
                Color:
                    rgba: 179/255, 229/255, 252/255, 1
                Rectangle:
                    pos: self.pos
                    size: self.size

        MDLabel:
            text:  "Qual artista é conhecido como 'O Síndico'?"
            halign: 'center'
            pos_hint: {'center_x': 0.5, 'center_y': 0.7}


                
        MDButton:
            style: 'elevated'
            pos_hint: {'center_x': .23, 'center_y': .32}
            on_release: app.checar_resposta('Caetano Veloso')
            MDButtonText:
                text: "Caetano Veloso"
                text_color: rgba( 0/255, 0/255, 0/255, 1)


        MDButton:
            style: 'elevated'
            pos_hint: {'center_x': .41, 'center_y': .32}
            on_release: app.checar_resposta('Belchior')
            MDButtonText:
                text: "Belchior"
                text_color: rgba( 0/255, 0/255, 0/255, 1)

        MDButton:
            style: 'elevated'
            pos_hint: {'center_x': .59, 'center_y': .32}
            on_release: app.checar_resposta('Jorge Ben Jor')
            MDButtonText:
                text: "Jorge Ben Jor"
                text_color: rgba( 0/255, 0/255, 0/255, 1)

        MDButton:
            style: 'elevated'
            pos_hint: {'center_x': .76, 'center_y': .32}
            on_release: app.checar_resposta('Tim Maia')
            MDButtonText:
                text: "Tim Maia"
                text_color: rgba( 0/255, 0/255, 0/255, 1)       
            '''


class Botão(MDButton):
    pass

class HomeScreen(MDScreen):
    pass

class QuizScreen(MDScreen):
   pass


class QuizApp(MDApp):
    def build(self):
        return Builder.load_string(KV)
    def tela_quiz(self):
        self.root.current = 'quiz'

    def checar_resposta(self, answer):
        if answer == 'Tim Maia':
            self.show_popup("Resposta Correta!")
        else:
            self.show_popup("Resposta Errada!")

    def show_popup(self, message):
        popup = Popup(title='Resultado',
                      content=Label(text=message),
                      size_hint=(0.6, 0.4))
        popup.open()

        
    

if __name__== '__main__':

    QuizApp().run()

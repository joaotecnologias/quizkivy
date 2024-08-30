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

perguntas = [
    {
        "pergunta": "Qual artista é conhecido como 'O Síndico'?",
        "opcoes": ["Caetano Veloso", "Belchior", "Tim Maia", "Jorge Ben Jor"],
        "resposta": "Tim Maia"
    },
    {
        'pergunta': "Quem compôs a música 'Águas de Março'?",
        'opcoes': ["Adoniran Barbosa", "Gilberto Gil", "Tom Jobim", "Chico Buarque"],
        'resposta': "Tom Jobim"
    },
]


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
        on_release: app.go_to_quiz()

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
            size: (550, 250)  
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
    def go_to_quiz(self):
        self.root.current = 'quiz'
    

        
    

if __name__== '__main__':

    QuizApp().run()

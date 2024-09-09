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
from kivy.clock import Clock

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
        font_size: '40sp'
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
            id: pergunta
            text:  "Pergunta"
            halign: 'center'
            valign: 'middle'
            text_size: self.width, None
            size_hint_x: None
            width: 400
            pos_hint: {'center_x': 0.5, 'center_y': 0.7}

        MDButton:
            id: opcao1
            style: 'elevated'
            pos_hint: {'center_x': .23, 'center_y': .32}
            on_release: app.checar_resposta('opcao1')
            MDButtonText:
                text: "Opção 1"
                text_color: rgba( 0/255, 0/255, 0/255, 1)

        MDButton:
            id: opcao2
            style: 'elevated'
            pos_hint: {'center_x': .41, 'center_y': .32}
            on_release: app.checar_resposta('opcao2')
            MDButtonText:
                text: "Opção 2"
                text_color: rgba( 0/255, 0/255, 0/255, 1)

        MDButton:
            id: opcao3
            style: 'elevated'
            pos_hint: {'center_x': .59, 'center_y': .32}
            on_release: app.checar_resposta('opcao3')
            MDButtonText:
                text: "Opção 3"
                text_color: rgba( 0/255, 0/255, 0/255, 1)

        MDButton:
            id: opcao4
            style: 'elevated'
            pos_hint: {'center_x': .76, 'center_y': .32}
            on_release: app.checar_resposta('opcao4')
            MDButtonText:
                text: "Opção 4"
                text_color: rgba( 0/255, 0/255, 0/255, 1)       
'''

class Botao(MDButton):
    pass

class HomeScreen(MDScreen):
    pass

class QuizScreen(MDScreen):
    pass

class QuizApp(MDApp):
    def build(self):
        self.perguntas = [
            {"pergunta": "Qual artista é conhecido como 'O Síndico'?",
             "opcoes": ["Caetano Veloso", "Belchior", "Jorge Ben Jor", "Tim Maia"],
             "resposta": "Tim Maia"},
            {"pergunta": "Quem é conhecido como o 'Pai da Bossa Nova'?",
             "opcoes": ["Tom Jobim", "Vinícius de Moraes", "João Gilberto", "Gilberto Gil"],
             "resposta": "João Gilberto"},
            {"pergunta": "Qual dessas músicas é um dos maiores sucessos de Chico Buarque?",
             "opcoes": ["Aquele Abraço", "Construção", "Águas de Março", "Mas Que Nada"],
             "resposta": "Construção"},
            {"pergunta": "Quem é o compositor de 'O Que É, O Que É?'?",
             "opcoes": ["Djavan", "Gonzaguinha", "Milton Nascimento", "Elis Regina"],
             "resposta": "Gonzaguinha"},
        ]
        self.indice_pergunta = 0
        self.popup = None
        return Builder.load_string(KV)
   
    def tela_quiz(self):
        self.root.current = 'quiz'
        self.carregar_pergunta()
        

    def checar_resposta(self, answer_id):
        answer = self.root.get_screen('quiz').ids[answer_id].text
        resposta_correta = self.perguntas[self.indice_pergunta]['resposta']
        if answer == resposta_correta:
            self.show_popup('Resposta correta!!')
            Clock.schedule_once(self.proxima_pergunta, 1)
        else:
            self.show_popup('Resposta errada!!')
            Clock.schedule_once(self.fechar_popup, 1)
        

    def show_popup(self, message):
        if self.popup:
            self.popup.dismiss()
        self.popup = Popup(title='Resultado',
                           content=Label(text=message),
                           size_hint=(0.6, 0.4))
        self.popup.open()
       
    def fechar_popup(self, dt):
        if self.popup:
            self.popup.dismiss()
    
    def proxima_pergunta(self, dt):
        if self.popup:
            self.popup.dismiss()
        self.indice_pergunta += 1
        if self.indice_pergunta < len(self.perguntas):
            self.carregar_pergunta()
        #if self.indice_pergunta == len(self.perguntas):

    def carregar_pergunta(self):
        tela_quiz = self.root.get_screen('quiz')
        info_pergunta = self.perguntas[self.indice_pergunta]
        
        
        tela_quiz.ids.pergunta.text = info_pergunta['pergunta']
        
        
        opcoes = info_pergunta['opcoes']
        tela_quiz.ids.opcao1.text = opcoes[0]
        tela_quiz.ids.opcao2.text = opcoes[1]
        tela_quiz.ids.opcao3.text = opcoes[2]
        tela_quiz.ids.opcao4.text = opcoes[3]

if __name__ == '__main__':
    QuizApp().run()

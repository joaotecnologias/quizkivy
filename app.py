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
from random import shuffle


KV = '''
ScreenManager:
    HomeScreen:
    QuizScreen:
    
<HomeScreen>:
    name: 'login'
    MDFloatLayout:
        md_bg_color: rgba(173, 216, 230, 255)
    
      #  Image:
       #     source: "C:/Users/joao_/OneDrive/Área de Trabalho/fundo2.jpeg"
        #    allow_stretch: True
         #   keep_ratio: False
          #  size_hint: 1, 1
           # pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
    Label:
        text: 'Bem Vindo, fã de MPB! Vamos testar seus conhecimentos?'
        pos_hint: {'center_y': .7}
        halign: 'center'
        font_size: '24sp'
        bold: True
        color: rgba(32, 0, 66, 255)

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
            text: 'Sair'
            

<QuizScreen>:
    name: 'quiz'
    MDFloatLayout:
        md_bg_color: [255/255, 214/255, 102/255, 1]
        MDBoxLayout:
            orientation: 'horizontal'
            spacing: 10
            padding: 10
            size_hint: (None, None)  
            size: (550, 330)  
            pos_hint: {'center_x': 0.5, 'center_y': 0.64}

            canvas.before:
                Color:
                    rgba: 165/255, 255/255, 184/255, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [30]

        MDLabel:
            id: pergunta
            text:  "Pergunta"
            halign: 'center'
            valign: 'middle'
            text_size: self.width, None
            size_hint_x: None
            width: 350
            pos_hint: {'center_x': 0.5, 'center_y': 0.65}
            font_size: '19sp'

        MDButton:
            id: opcao1
            style: 'elevated'
            pos_hint: {'center_x': .23, 'center_y': .32}
            on_release: app.checar_resposta('opcao1')
            MDButtonText:
                text: "Alternativa A"
                text_color: rgba(0/255, 0/255, 0/255, 1)

        MDButton:
            id: opcao2
            style: 'elevated'
            pos_hint: {'center_x': .41, 'center_y': .32}
            on_release: app.checar_resposta('opcao2')
            MDButtonText:
                text: "Alternativa B"
                text_color: rgba(0/255, 0/255, 0/255, 1)

        MDButton:
            id: opcao3
            style: 'elevated'
            pos_hint: {'center_x': .59, 'center_y': .32}
            on_release: app.checar_resposta('opcao3')
            MDButtonText:
                text: "Alternativa C"
                text_color: rgba(0/255, 0/255, 0/255, 1)

        MDButton:
            id: opcao4
            style: 'elevated'
            pos_hint: {'center_x': .76, 'center_y': .32}
            on_release: app.checar_resposta('opcao4')
            MDButtonText:
                text: "Alternativa D"
                text_color: rgba(0/255, 0/255, 0/255, 1)       
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
             "resposta": "Alternativa D"},

            {"pergunta": "Quem é conhecido como o 'Pai da Bossa Nova'?",
             "opcoes": ["Tom Jobim", "Vinícius de Moraes", "João Gilberto", "Gilberto Gil"],
             "resposta": "Alternativa C"},

            {"pergunta": "Qual dessas músicas é um dos maiores sucessos de Chico Buarque?",
             "opcoes": ["Aquele Abraço", "Construção", "Águas de Março", "Mas Que Nada"],
             "resposta": "Alternativa B"},

            {"pergunta": "Quem é o compositor de 'O Que É, O Que É?'?",
             "opcoes": ["Djavan", "Gonzaguinha", "Milton Nascimento", "Elis Regina"],
             "resposta": "Alternativa B"},

            {"pergunta": "A música Aquarela reúne dois grandes nomes do MPB. Quem são eles?",
             "opcoes": ["Toquinho e Gal Costa", "Vinícius de Moraes e Tom Jobim", "Vinícius de Moraes e Toquinho", "João Gilberto e Caetano Veloso"],
             "resposta": "Alternativa C"},
            
            {"pergunta": "Quem é a Rainha do Rock Brasileiro?",
             "opcoes": ["Pitty", "Rita Lee", "Cássia Eler", "Gal Costa"],
             "resposta": "Alternativa B"},

            {"pergunta": "Quem é o VERDADEIRO 'Rei da música brasileira'?",
             "opcoes": ["Erasmo Carlos", "Tim Maia", "Belchior", "Luiz Gonzaga"],
             "resposta": "Alternativa B"},
            
            {"pergunta": "Quem foi o músico brasileiro dono do pseudônimo 'Julinho da Adelaide'?",
             "opcoes": ["Chico Buarque", "Erasmo Carlos", "Milton Nascimento", "Adoniran Barbosa"],
             "resposta": "Alternativa A"},
            
            {"pergunta": "Qual é o álbum mais famoso da Nação Zumbi, lançado em 1994?",
             "opcoes": ["Afrociberdelia", "Samba Esquema Noise", "Cabeça Dinossauro", "Da Lama ao Caos"],
             "resposta": "Alternativa D"},

            {"pergunta": "O álbum 'Clube da Esquina' foi composto por quais cantores brasileiros?",
             "opcoes": ["Jorge Ben e Marisa Monte", "Djavan e Zé Ramalho", "Lô Borges e Milton Nascimento", "Lô Borges e Djavan"],
             "resposta": "Alternativa C"},

             


        ]
        shuffle(self.perguntas)
        self.indice_pergunta = 0
        self.popup = None
        self.pontuacao = 0
        self.tentativas = 0
        self.maxtentativas = 2
        return Builder.load_string(KV)
   
    def tela_quiz(self):
        self.root.current = 'quiz'
        self.carregar_pergunta()
        
    def carregar_pergunta(self):
        if self.indice_pergunta >= len(self.perguntas):
            return

        tela_quiz = self.root.get_screen('quiz')
        info_pergunta = self.perguntas[self.indice_pergunta]
        
        pergunta_formatada = f"{info_pergunta['pergunta']}\n\nA) {info_pergunta['opcoes'][0]}   B) {info_pergunta['opcoes'][1]}   C) {info_pergunta['opcoes'][2]}   D) {info_pergunta['opcoes'][3]}"
        
        tela_quiz.ids.pergunta.text = pergunta_formatada    

    def checar_resposta(self, answer_id):
        if self.indice_pergunta >= len(self.perguntas):
            return
        answer = self.root.get_screen('quiz').ids[answer_id].children[0].text
        
        resposta_correta = self.perguntas[self.indice_pergunta]['resposta']
        
        if answer == resposta_correta:
           
            self.show_popup('Resposta correta!!')
            self.pontuacao += 1
            Clock.schedule_once(self.proxima_pergunta, 1)
            self.tentativas = 0
       
        else:
            self.tentativas += 1
            
            if self.tentativas == self.maxtentativas:
                
                self.show_popup('Você excedeu o limite de tentativas, passando para a próxima pergunta!')
                
                Clock.schedule_once(self.proxima_pergunta, 1)
            else:
                self.show_popup('Resposta errada, você tem mais uma chance!')
                Clock.schedule_once(self.fechar_popup, 1)

    def proxima_pergunta(self, *args):
        if self.popup:
            self.popup.dismiss()
        self.indice_pergunta += 1

        if self.indice_pergunta < len(self.perguntas):
            self.carregar_pergunta()
        else:
            self.mostrar_pontuacao_final()
        

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
    
    def mostrar_pontuacao_final(self):
        total_perguntas = len(self.perguntas)
        pontuacao_texto = f'Você acertou {self.pontuacao} de {total_perguntas} perguntas.\n\n'
        
        if self.pontuacao <= 2:
            resultado = 'Parece que você não sabe nada de MPB...'
        elif self.pontuacao <= 5:
            resultado = 'Você sabe um pouco sobre MPB, mas pode melhorar!'
        elif self.pontuacao >= 6:
            resultado = 'Você acertou a maioria! Com certeza é fã de MPB!'
        if self.pontuacao == len(self.perguntas):
            resultado = 'Você é o maior fã de MPB de todos!! Parabéns!!'
        
        texto_popup = pontuacao_texto + resultado

        self.pontuacao_final = Popup(
        title='Fim do Quiz!! Parabéns por chegar até aqui!',
        content=Label(text=texto_popup, halign='center', valign='middle'),
        size_hint=(None, None),
        size=(500, 200))

        self.pontuacao_final.open()

    
if __name__ == '__main__':
    QuizApp().run()

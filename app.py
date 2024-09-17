from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFillRoundFlatButton, MDFillRoundFlatIconButton, MDFlatButton
from kivy.uix.popup import Popup
from kivy.clock import Clock
from random import shuffle
from kivymd.uix.dialog import MDDialog
from kivy.animation import Animation




KV = '''
ScreenManager:
    HomeScreen:
    QuizScreen:
    RockScreen:
    RapScreen:

<HomeScreen>:
    name: 'login'
    MDFloatLayout:
        Image:
            source: 'C:/Users/joao_/.vscode/fundoinicio.png'
            allow_stretch: True
            keep_ratio: False
    MDFloatLayout:
    MDCard:
        size_hint: None, None
        size: "650dp", "80dp"
        pos_hint: {"center_x": .5, "center_y": .75}
        elevation: 0
        md_bg_color: [1, 1, 1, 1]

        MDBoxLayout:
            orientation: 'vertical'
            padding: "16dp"
            spacing: "8dp"    
            pos_hint: {'center_x': .5, 'center_y': .5}
            Label:
                text: 'Bem vindo, amante da música!'
                pos_hint: {'center_y': .75}
                halign: 'center'
                font_size: '28sp'
                bold: True
                color: [0.2, 0.2, 0.6, 1]
                font_name: 'C:/Users/joao_/OneDrive/Área de Trabalho/coisas/Poppins-SemiBoldItalic.ttf'

    MDCard:
        size_hint: None, None
        size: "650dp", "80dp"
        pos_hint: {"center_x": .5, "center_y": .66}
        elevation: 0
        md_bg_color: [1, 1, 1, 1]

        MDBoxLayout:
            orientation: 'vertical'
            padding: "16dp"
            spacing: "8dp"
            pos_hint: {'center_x': .5, 'center_y': .5}

            Label:
                text: 'Escolha um quiz para jogar:'
                pos_hint: {'center_y': .67}
                halign: 'center'
                font_size: '28sp'
                bold: True
                color: [0.2, 0.2, 0.6, 1] 
                font_name: 'C:/Users/joao_/OneDrive/Área de Trabalho/coisas/Poppins-SemiBoldItalic.ttf'
       
        
           

    MDRectangleFlatIconButton:
        pos_hint: {'center_x': .29, 'center_y': .45}
        size_hint: (0.40, 0.1)
        on_release: app.tela_quiz()
        icon: 'music'
        text: 'MPB'
        md_bg_color: [1, 1, 1, 1]
        text_color: [0.2, 0.2, 0.6, 1]
        icon_color: [0, 0, 0, 1]
        font_name: 'C:/Users/joao_/OneDrive/Área de Trabalho/coisas/Poppins-SemiBold.ttf'

    MDRectangleFlatIconButton:
        pos_hint: {'center_x': .29, 'center_y': .33}
        size_hint: (0.40, 0.1)
        on_release: app.tela_rap()
        icon: 'headphones'
        text: 'Rap'
        md_bg_color: [1, 1, 1, 1]
        text_color: [0.2, 0.2, 0.6, 1]
        icon_color: [0, 0, 0, 1]
        font_name: 'C:/Users/joao_/OneDrive/Área de Trabalho/coisas/Poppins-SemiBold.ttf'
    
    MDRectangleFlatIconButton:
        pos_hint: {'center_x': .72, 'center_y': .45}
        size_hint: (0.40, 0.1)
        on_release: app.tela_rock()
        icon: 'guitar-electric'
        text: 'Rock'
        md_bg_color: [1, 1, 1, 1]
        text_color: [0.2, 0.2, 0.6, 1]
        icon_color: [0, 0, 0, 1]
        font_name: 'C:/Users/joao_/OneDrive/Área de Trabalho/coisas/Poppins-SemiBold.ttf'

    MDRectangleFlatIconButton:
        pos_hint: {'center_x': .72, 'center_y': .33}
        size_hint: (0.40, 0.1)
        on_release: app.stop()
        icon: 'close'
        text: 'Sair'
        md_bg_color: [1, 1, 1, 1]
        text_color: [0.2, 0.2, 0.6, 1]
        icon_color: [0, 0, 0, 1]
        font_name: 'C:/Users/joao_/OneDrive/Área de Trabalho/coisas/Poppins-SemiBold.ttf'
        


<QuizScreen>:
    name: 'quiz'
    MDFloatLayout:
        Image:
            source: 'C:/Users/joao_/.vscode/fundompb.png'
            allow_stretch: True
            keep_ratio: False
        MDBoxLayout:
            orientation: 'horizontal'
            spacing: 10
            padding: 10
            size_hint: (None, None)
            size: (500, 280)
            pos_hint: {'center_x': 0.5, 'center_y': 0.64}

            canvas.before:
                Color:
                    rgba: [165/255, 255/255, 184/255, 1]
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
            font_size: '18sp'
            font_name: 'C:/Users/joao_/OneDrive/Área de Trabalho/coisas/Poppins-SemiBold.ttf'

        MDLabel:
            id: contador
            text: "Pergunta 1/10"
            pos_hint: {'right': 1, 'center_y': 0.94}
            size_hint: None, None
            size: dp(150), dp(40)
            padding: [10, 10]
            halign: 'right'
            valign: 'top'
            theme_text_color: "Custom"
            text_color: [0, 0, 0, 1]
            font_name: 'C:/Users/joao_/.vscode/Poppins-Black.ttf'

        MDFillRoundFlatIconButton:
            id: voltar
            pos_hint: {'center_x': 0.08, 'center_y': 0.95}
            size_hint: None, None
            width: 100
            height: 50
            background_color: [0/255, 150/255, 136/255, 1]
            on_release: app.tela_inicio()
            text: "Voltar"
            icon: 'arrow-left'
            md_bg_color: [1, 1, 1, 1]
            text_color: [0, 0, 0, 1]
            icon_color: [0, 0, 0, 1]
            font_name: "C:/Users/joao_/OneDrive/Área de Trabalho/coisas/Poppins-MediumItalic.ttf"

        MDRaisedButton:
            id: opcao1
            pos_hint: {'center_x': .29, 'center_y': .32}
            size_hint: (0.40, 0.1)
            on_release: app.checar_resposta('opcao1')
            text: "Alternativa A"
            text_color: [0, 0.5, 0, 1]
            md_bg_color: [1, 1, 1, 1]
            font_name: 'C:/Users/joao_/OneDrive/Área de Trabalho/coisas/Poppins-SemiBoldItalic.ttf'

        MDRaisedButton:
            id: opcao2
            pos_hint: {'center_x': .29, 'center_y': .20}
            size_hint: (0.40, 0.1)
            on_release: app.checar_resposta('opcao2')
            text: "Alternativa B"
            text_color: [0, 0.5, 0, 1]
            md_bg_color: [1, 1, 1, 1]
            font_name: 'C:/Users/joao_/OneDrive/Área de Trabalho/coisas/Poppins-SemiBoldItalic.ttf'

        MDRaisedButton:
            id: opcao3
            pos_hint: {'center_x': .72, 'center_y': .32}
            size_hint: (0.40, 0.1)
            on_release: app.checar_resposta('opcao3')
            text: "Alternativa C"
            text_color: [0, 0.5, 0, 1]
            md_bg_color: [1, 1, 1, 1]
            font_name: 'C:/Users/joao_/OneDrive/Área de Trabalho/coisas/Poppins-SemiBoldItalic.ttf'

        MDRaisedButton:
            id: opcao4
            pos_hint: {'center_x': .72, 'center_y': .20}
            size_hint: (0.40, 0.1)
            on_release: app.checar_resposta('opcao4')
            text: "Alternativa D"
            text_color: [0, 0.5, 0, 1]
            md_bg_color: [1, 1, 1, 1]
            font_name: 'C:/Users/joao_/OneDrive/Área de Trabalho/coisas/Poppins-SemiBoldItalic.ttf'

<RockScreen>:
    name: 'rock'
    MDFloatLayout:
        Image:
            source: 'C:/Users/joao_/.vscode/telarock.png'
            keep_ratio: False
            allow_stretch: True
       
        MDBoxLayout:
            orientation: 'horizontal'
            spacing: 10
            padding: 10
            size_hint: (None, None)
            size: (500, 280)
            pos_hint: {'center_x': 0.5, 'center_y': 0.64}

            canvas.before:
                Color:
                    rgba: [192/255, 192/255, 192/255, 1]
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [30]

        MDLabel:
            id: perguntarock
            text:  "Pergunta"
            halign: 'center'
            valign: 'middle'
            text_size: self.width, None
            size_hint_x: None
            width: 350
            pos_hint: {'center_x': 0.5, 'center_y': 0.65}
            font_size: '18sp'
            font_name: 'C:/Users/joao_/OneDrive/Área de Trabalho/coisas/Poppins-SemiBold.ttf'

        

        MDLabel:
            id: contadorrock
            text: "Pergunta 1/10"
            pos_hint: {'right': 1, 'center_y': 0.94}
            size_hint: None, None
            size: dp(150), dp(40)
            padding: [10, 10]
            halign: 'right'
            valign: 'top'
            theme_text_color: "Custom"
            text_color: [0, 0, 0, 1]
            font_name: 'C:/Users/joao_/.vscode/Poppins-Black.ttf'
            

        MDFillRoundFlatIconButton:
            id: voltar
            pos_hint: {'center_x': 0.08, 'center_y': 0.95}
            size_hint: None, None
            width: 100
            height: 50
            background_color: [0/255, 150/255, 136/255, 1]
            on_release: app.tela_inicio()
            text: "Voltar"
            bold: True
            icon: 'arrow-left'
            md_bg_color: [1, 1, 1, 1]
            text_color:[0, 0, 0, 1]
            icon_color: [0, 0, 0, 1]

        
        MDRaisedButton:
            id: opcao1rock
            pos_hint: {'center_x': .29, 'center_y': .32}
            size_hint: (0.40, 0.1)
            on_release: app.checar_resposta_rock('opcao1rock')
            text: "Alternativa A"
            md_bg_color: [0.84, 0.84, 0.84, 1]
            text_color: [0, 0, 0, 1]
            font_name: 'C:/Users/joao_/OneDrive/Área de Trabalho/coisas/Poppins-SemiBold.ttf'
           

        MDRaisedButton:
            id: opcao2rock
            pos_hint: {'center_x': .29, 'center_y': .20}
            size_hint: (0.40, 0.1)
            on_release: app.checar_resposta_rock('opcao2rock')
            text: "Alternativa B"
            md_bg_color: [0.84, 0.84, 0.84, 1]
            text_color: [0, 0, 0, 1]
            font_name: 'C:/Users/joao_/OneDrive/Área de Trabalho/coisas/Poppins-SemiBold.ttf'
            

        MDRaisedButton:
            id: opcao3rock
            pos_hint: {'center_x': .72, 'center_y': .32}
            size_hint: (0.40, 0.1)
            on_release: app.checar_resposta_rock('opcao3rock')
            text: "Alternativa C"
            md_bg_color: [0.84, 0.84, 0.84, 1]
            text_color: [0, 0, 0, 1]
            font_name: 'C:/Users/joao_/OneDrive/Área de Trabalho/coisas/Poppins-SemiBold.ttf'

        MDRaisedButton:
            id: opcao4rock
            pos_hint: {'center_x': .72, 'center_y': .20}
            size_hint: (0.40, 0.1)
            on_release: app.checar_resposta_rock('opcao4rock')
            text: "Alternativa D"
            md_bg_color: [0.84, 0.84, 0.84, 1]
            text_color: [0, 0, 0, 1]
            font_name: 'C:/Users/joao_/OneDrive/Área de Trabalho/coisas/Poppins-SemiBold.ttf'

            


<RapScreen>
    name: 'rap'
    MDFloatLayout:
        Image:
            source: 'C:/Users/joao_/.vscode/telarap.png'
            keep_ratio: False
            allow_stretch: True
        MDBoxLayout:
            orientation: 'horizontal'
            spacing: 10
            padding: 10
            size_hint: (None, None)
            size: (500, 280)
            pos_hint: {'center_x': 0.5, 'center_y': 0.64}

            canvas.before:
                Color:
                    rgba: [245/255, 245/255, 245/255, 1]
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [30]
        MDLabel:
            id: perguntarap
            text:  "Pergunta"
            halign: 'center'
            valign: 'middle'
            text_size: self.width, None
            size_hint_x: None
            width: 350
            pos_hint: {'center_x': 0.5, 'center_y': 0.65}
            font_size: '18sp'
            font_name: 'C:/Users/joao_/OneDrive/Área de Trabalho/coisas/Poppins-SemiBold.ttf'

        MDLabel:
            id: contadorrap
            text: "Pergunta 1/10"
            pos_hint: {'right': 1, 'center_y': 0.94}
            size_hint: None, None
            size: dp(150), dp(40)
            padding: [10, 10]
            halign: 'right'
            valign: 'top'
            theme_text_color: "Custom"
            text_color: [0, 0, 0, 1]
            font_name: 'C:/Users/joao_/.vscode/Poppins-Black.ttf'
            

        MDFillRoundFlatIconButton:
            id: voltar
            pos_hint: {'center_x': 0.08, 'center_y': 0.95}
            size_hint: None, None
            width: 100
            height: 50
            background_color: [0/255, 150/255, 136/255, 1]
            on_release: app.tela_inicio()
            text: "Voltar"
            bold: True
            icon: 'arrow-left'
            md_bg_color: [1, 1, 1, 1]
            text_color:[0, 0, 0, 1]
            icon_color: [0, 0, 0, 1]


        MDRaisedButton:
            id: opcao1rap
            pos_hint: {'center_x': .29, 'center_y': .32}
            size_hint: (0.40, 0.1)
            on_release: app.checar_resposta_rap('opcao1rap')
            text: "Alternativa A"
            md_bg_color: [0.84, 0.84, 0.84, 1]
            text_color: [0, 0, 0, 1]
            font_name: 'C:/Users/joao_/OneDrive/Área de Trabalho/coisas/Poppins-SemiBold.ttf'
           

        MDRaisedButton:
            id: opcao2rap
            pos_hint: {'center_x': .29, 'center_y': .20}
            size_hint: (0.40, 0.1)
            on_release: app.checar_resposta_rap('opcao2rap')
            text: "Alternativa B"
            md_bg_color: [0.84, 0.84, 0.84, 1]
            text_color: [0, 0, 0, 1]
            font_name: 'C:/Users/joao_/OneDrive/Área de Trabalho/coisas/Poppins-SemiBold.ttf'
            

        MDRaisedButton:
            id: opcao3rap
            pos_hint: {'center_x': .72, 'center_y': .32}
            size_hint: (0.40, 0.1)
            on_release: app.checar_resposta_rap('opcao3rap')
            text: "Alternativa C"
            md_bg_color: [0.84, 0.84, 0.84, 1]
            text_color: [0, 0, 0, 1]
            font_name: 'C:/Users/joao_/OneDrive/Área de Trabalho/coisas/Poppins-SemiBold.ttf'

        MDRaisedButton:
            id: opcao4rap
            pos_hint: {'center_x': .72, 'center_y': .20}
            size_hint: (0.40, 0.1)
            on_release: app.checar_resposta_rap('opcao4rap')
            text: "Alternativa D"
            md_bg_color: [0.84, 0.84, 0.84, 1]
            text_color: [0, 0, 0, 1]
            font_name: 'C:/Users/joao_/OneDrive/Área de Trabalho/coisas/Poppins-SemiBold.ttf'
'''

class HomeScreen(MDScreen):
    pass

class QuizScreen(MDScreen):
    pass

class RockScreen(MDScreen):
    pass

class RapScreen(MDScreen):
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

            {"pergunta": "A música Aquarela reúne dois grandes nomes do MPB. Quem são eles?",
             "opcoes": ["Toquinho e Gal Costa", "Vinícius de Moraes e Tom Jobim", "Vinícius de Moraes e Toquinho", "João Gilberto e Toquinho"],
             "resposta": "Vinícius de Moraes e Toquinho"}, 

            {"pergunta": "Quem é a Rainha do Rock Brasileiro?",
             "opcoes": ["Pitty", "Rita Lee", "Cássia Eler", "Gal Costa"],
             "resposta": "Rita Lee"}, 

            {"pergunta": "Quem é o VERDADEIRO 'Rei da música brasileira'?",
             "opcoes": ["Erasmo Carlos", "Tim Maia", "Belchior", "Luiz Gonzaga"],
             "resposta": "Tim Maia"}, 

            {"pergunta": "Quem foi o músico brasileiro dono do pseudônimo 'Julinho da Adelaide'?",
             "opcoes": ["Chico Buarque", "Erasmo Carlos", "Milton Nascimento", "Adoniran Barbosa"],
             "resposta": "Chico Buarque"}, 

            {"pergunta": "Qual é o álbum mais famoso da Nação Zumbi, lançado em 1994?",
             "opcoes": ["Afrociberdelia", "Samba Esquema Noise", "Cabeça Dinossauro", "Da Lama ao Caos"],
             "resposta": "Da Lama ao Caos"}, 

            {"pergunta": "O álbum 'Clube da Esquina' foi composto por quais cantores brasileiros?",
             "opcoes": ["Jorge Ben e Marisa Monte", "Djavan e Zé Ramalho", "Lô Borges e Milton Nascimento", "Lô Borges e Djavan"],
             "resposta": "Lô Borges e Milton Nascimento"},
        ]

        self.perguntasrock = [
            {"perguntarock": "Qual grupo de rock britânico lançou o álbum 'The Wall' em 1979?",
             "opcoesrock": ["Pink Floyd", "The Rolling Stones", "The Who", "Rush"],
             "respostarock": "Pink Floyd"},
            
            {"perguntarock": "Qual banda britânica lançou o álbum 'Sgt. Peppers Lonely Hearts Club Band', em 1967?",
             "opcoesrock": ["Led Zeppelin", "Queen", "The Beatles", "The Doors"],
             "respostarock": "The Beatles"},

            {"perguntarock": "Qual é o nome do álbum clássico do Nirvana que ajudou a popularizar o grunge em 1991?",
             "opcoesrock": ["Abbey Road", "Back in Black", "Ten", "Nevermind"],
             "respostarock": "Nevermind"},

            {"perguntarock": "Qual banda é famosa pelo hit 'Stairway to Heaven'?",
             "opcoesrock": ["Pearl Jam", "U2", "Led Zeppelin", "Guns N' Roses"],
             "respostarock": "Led Zeppelin"},

            {"perguntarock": "Qual banda de rock dos anos 80 é famosa pelo álbum 'Thriller' e a canção 'Billie Jean'",
             "opcoesrock": ["America", "Supertramp", "The Police", "Não é uma banda, é o Michael Jackson"],
             "respostarock": "Não é uma banda, é o Michael Jackson"},

            {"perguntarock": "Qual banda lançou o clássico álbum 'Hotel California' em 1976?",
             "opcoesrock": ["Fleetwood Mac", "The Beach Boys", "Lynyrd Skynyrd", "Eagles"],
             "respostarock": "Eagles"},
            
            {"perguntarock": "Qual música de David Bowie ajudou a consolidar sua persona de Ziggy Stardust?",
             "opcoesrock": ["Life on Mars?", "Space Oddity", "Starman", "Heroes"],
             "respostarock": "Starman"},

            {"perguntarock": "Qual banda lançou o álbum 'A Night at the Opera' em 1975?",
             "opcoesrock": ["Queen", "The Rolling Stones", "The Beatles", "Yes"],
             "respostarock": "Queen"},

            {"perguntarock": "Qual banda é conhecida pelo álbum 'Rumours', lançado em 1977?",
             "opcoesrock": ["The Police", "ABBA", "Fleetwood Mac", "Black Sabbath"],
             "respostarock": "Fleetwood Mac"},
            
            {"perguntarock": "Qual artista é conhecido pelo álbum 'Purple Rain'?",
             "opcoesrock": ["Prince", "Michael Jackson", "Stevie Wonder", "George Michael"],
             "respostarock": "Prince"},
            

            
        ]

        self.perguntasrap = [
            {"perguntarap": "Qual álbum de Tyler, The Creator foi nomeado para um Grammy em 2019?",
             "opcoesrap": ["Goblin", "Wolf", "Flower Boy", "Igor"],
             "respostarap": "Igor"},
            
            {"perguntarap": "Qual rapper americano lançou o álbum Astroworld em 2018?",
             "opcoesrap": ["Lil Uzi Vert", "Lil Yachty", "Travis Scott", "Post Malone"],
             "respostarap": "Travis Scott"},
            
            {"perguntarap": "Qual rapper lançou o álbum DAMN. em 2017, que ganhou o Pulitzer Prize de Música?",
             "opcoesrap": ["J. Cole", "Drake", "Kendrick Lamar", "Chance the Rapper"],
             "respostarap": "Kendrick Lamar"},
            
            {"perguntarap": "Qual rapper lançou o álbum Life of Pablo em 2016?",
             "opcoesrap": ["Jay Z", "Playboi Carti", "Pusha T", "Kanye West"],
             "respostarap": "Kanye West"},
             
            {"perguntarap": "Qual rapper é conhecido pelo álbum The Slim Shady LP e pelo sucesso de Lose Yourself?",
             "opcoesrap": ["Eminem", "Nas", "Ice Cube", "Jay-Z"],
             "respostarap": "Eminem"},

            {"perguntarap": "Qual é o nome verdadeiro de Eminem?",
             "opcoesrap": ["Marshall Mathers", "Curtis Jackson", "Shawn Carter", "Calvin Broadus"],
             "respostarap": "Marshall Mathers"},
        
            {"perguntarap": "Qual rapper é conhecido pelo seu alter ego 'Yeezy'?",
             "opcoesrap": ["50 Cent", "Kanye West", "Lil Wayne", "MF Doom"],
             "respostarap": "Kanye West"},

            {"perguntarap": "Quem é o rapper famoso pelo álbum 'Awaken, My Love!'?",
             "opcoesrap": ["Snoop Dog", "Donald Glover (Childish Gambino)", "Dr. Dre", "Tupac"],
             "respostarap": "Donald Glover (Childish Gambino)"},

            {"perguntarap": "Qual artista colaborou com Rihanna no hit 'Umbrella'?",
             "opcoesrap": ["Eminem", "The Notorious B.I.G.", "Kanye West", "Jay-Z"],
             "respostarap": "Jay-Z"},

            {"perguntarap": "Qual rapper lançou o álbum 'Graduation' em 2007?",
             "opcoesrap": ["T.I.", "50 Cent", "Kanye West", "Lil Wayne"],
             "respostarap": "Kanye West"},
            
            

        ]

        shuffle(self.perguntas)
        shuffle(self.perguntasrock)
        shuffle(self.perguntasrap)
        self.indice_pergunta = 0
        self.indice_pergunta_rock = 0
        self.indice_pergunta_rap = 0
        self.dialog = None
        self.pontuacao = 0
        self.pontuacao_rock = 0
        self.pontuacao_rap = 0
        self.tentativas = 0
        self.maxtentativas = 2
        return Builder.load_string(KV)

    def carregar_pergunta(self):
        if self.indice_pergunta >= len(self.perguntas):
            return

        tela_quiz = self.root.get_screen('quiz')
        info_pergunta = self.perguntas[self.indice_pergunta]

        pergunta_formatada = f"{info_pergunta['pergunta']}"
        tela_quiz.ids.pergunta.text = pergunta_formatada
        tela_quiz.ids.contador.text = f"Pergunta {self.indice_pergunta + 1}/{len(self.perguntas)}"

        opcoes = info_pergunta['opcoes']
        botoes = [tela_quiz.ids.opcao1, tela_quiz.ids.opcao2, tela_quiz.ids.opcao3, tela_quiz.ids.opcao4]

        for i, opcao in enumerate(opcoes):
            botoes[i].text = opcao
            

    def checar_resposta(self, answer_id):
        if self.indice_pergunta >= len(self.perguntas):
            return
        tela_quiz = self.root.get_screen('quiz')
        resposta_botao = tela_quiz.ids[answer_id]
        answer = resposta_botao.text
        resposta_correta = self.perguntas[self.indice_pergunta]['resposta']

        if answer == resposta_correta:
            self.animar_botao(resposta_botao, True)
            self.mostrar_dialog('Resposta correta!!')
            self.pontuacao += 1
            Clock.schedule_once(self.proxima_pergunta, 1.6)
            self.tentativas = 0
        else:
            self.animar_botao(resposta_botao, False)
            self.tentativas += 1
            if self.tentativas >= self.maxtentativas:
                self.mostrar_dialog('Você excedeu o limite de tentativas, passando para a próxima pergunta!')
                self.tentativas = 0
                Clock.schedule_once(self.proxima_pergunta, 1.6)
            else:
                self.mostrar_dialog('Resposta errada, você tem mais uma chance!')
                Clock.schedule_once(self.fechar_dialog, 1.6)

    def proxima_pergunta(self, *args):
        if self.dialog:
            self.dialog.dismiss()
        tela_quiz = self.root.get_screen('quiz')
        botoes = [tela_quiz.ids.opcao1, tela_quiz.ids.opcao2, tela_quiz.ids.opcao3, tela_quiz.ids.opcao4]
        for botao in botoes:
            botao.md_bg_color = [1, 1, 1, 1]
        self.indice_pergunta += 1

        if self.indice_pergunta < len(self.perguntas):
            self.carregar_pergunta()
        else:
            self.mostrar_pontuacao_final()


    def mostrar_pontuacao_final(self):
        total_perguntas = len(self.perguntas)
        pontuacao_texto = f'Você acertou {self.pontuacao} de {total_perguntas} perguntas.\n\n'

        if self.pontuacao <= 2:
            resultado = 'Parece que você não sabe nada sobre MPB...'
        elif self.pontuacao <= 5:
            resultado = 'Você sabe um pouco sobre MPB, mas pode melhorar!'
        elif self.pontuacao >= 6:
            resultado = 'Você acertou a maioria! Com certeza é fã de MPB!'
        elif self.pontuacao == len(self.perguntas):
            resultado = 'Você é o maior fã de MPB de todos!! Parabéns!!'

        texto_dialog = pontuacao_texto + resultado

        self.dialog = MDDialog(
            title='Fim do Quiz!! Parabéns por chegar até aqui!',
            text=texto_dialog,
            buttons =[MDFlatButton(text='Início', on_release = lambda x: self.tela_inicio())],
            auto_dismiss=True
        )

        self.dialog.open()


    def carregar_pergunta_rock(self):
        if self.indice_pergunta_rock >= len(self.perguntasrock):
            return

        tela_rock = self.root.get_screen('rock')
        info_pergunta_rock = self.perguntasrock[self.indice_pergunta_rock]

        pergunta_formatada = f"{info_pergunta_rock['perguntarock']}"
        tela_rock.ids.perguntarock.text = pergunta_formatada
        tela_rock.ids.contadorrock.text = f"Pergunta {self.indice_pergunta_rock + 1}/{len(self.perguntasrock)}"

        opcoes_rock = info_pergunta_rock['opcoesrock']
        botoes_rock = [tela_rock.ids.opcao1rock, tela_rock.ids.opcao2rock, tela_rock.ids.opcao3rock, tela_rock.ids.opcao4rock]

        for i, opcaorock in enumerate(opcoes_rock):
            botoes_rock[i].text = opcaorock
            


    def checar_resposta_rock(self, answer_id):
        if self.indice_pergunta_rock >= len(self.perguntasrock):
            return
    
        tela_rock = self.root.get_screen('rock')
        resposta_botao_rock = tela_rock.ids[answer_id]
        answer = resposta_botao_rock.text
        resposta_correta = self.perguntasrock[self.indice_pergunta_rock]['respostarock']

        if answer == resposta_correta:
            self.animar_botao_rock(resposta_botao_rock, True)
            self.mostrar_dialog('Resposta correta!!')
            self.pontuacao_rock += 1
            Clock.schedule_once(self.proxima_pergunta_rock, 1.6)
            self.tentativas = 0
        else:
            self.animar_botao_rock(resposta_botao_rock, False)
            self.tentativas += 1
            if self.tentativas >= self.maxtentativas:
                self.mostrar_dialog('Você excedeu o limite de tentativas, passando para a próxima pergunta!')
                self.tentativas = 0
                Clock.schedule_once(self.proxima_pergunta_rock, 1.6)
            else:
                self.mostrar_dialog('Resposta errada, você tem mais uma chance!')
                Clock.schedule_once(self.fechar_dialog, 1.6)


    def proxima_pergunta_rock(self, *args):
        if self.dialog:
            self.dialog.dismiss()
    
        tela_rock = self.root.get_screen('rock')
        botoes_rock = [tela_rock.ids.opcao1rock, tela_rock.ids.opcao2rock, tela_rock.ids.opcao3rock, tela_rock.ids.opcao4rock]
        for botao in botoes_rock:
            botao.md_bg_color = [0.84, 0.84, 0.84, 1]  

        self.indice_pergunta_rock += 1

        if self.indice_pergunta_rock < len(self.perguntasrock):
            self.carregar_pergunta_rock()
        else:
            self.mostrar_pontuacao_final_rock()



    def mostrar_pontuacao_final_rock(self):
        total_perguntas_rock = len(self.perguntasrock)
        pontuacao_texto = f'Você acertou {self.pontuacao_rock} de {total_perguntas_rock} perguntas.\n\n'

        if self.pontuacao_rock <= 2:
            resultado = 'Infelizmente você não sabe nada sobre rock...'
        elif self.pontuacao_rock <= 5:
            resultado = 'Está na média, mas pode melhorar...'
        elif self.pontuacao_rock >= 6:
            resultado = 'Uau! Você sabe mesmo sobre rock!!'
        elif self.pontuacao_rock == len(self.perguntasrock):
            resultado = 'Você não sabe sobre rock. Você É O ROCK!!!'

        texto_dialog = pontuacao_texto + resultado

        self.dialog = MDDialog(
            title='Fim do Quiz!! Parabéns por chegar até aqui!',
            text=texto_dialog,
            buttons =[MDFlatButton(text='Início', on_release = lambda x: self.tela_inicio())],
            auto_dismiss=True
        )

        self.dialog.open()


    def carregar_pergunta_rap(self):
        if self.indice_pergunta_rap >= len(self.perguntasrap):
            return

        tela_rap = self.root.get_screen('rap')
        info_pergunta_rap = self.perguntasrap[self.indice_pergunta_rap]

        pergunta_formatada = f"{info_pergunta_rap['perguntarap']}"
        tela_rap.ids.perguntarap.text = pergunta_formatada
        tela_rap.ids.contadorrap.text = f"Pergunta {self.indice_pergunta_rap + 1}/{len(self.perguntasrap)}"

        opcoes_rap = info_pergunta_rap['opcoesrap']
        botoes_rap = [tela_rap.ids.opcao1rap, tela_rap.ids.opcao2rap, tela_rap.ids.opcao3rap, tela_rap.ids.opcao4rap]

        for i, opcaorap in enumerate(opcoes_rap):
            botoes_rap[i].text = opcaorap


    def checar_resposta_rap(self, answer_id):
        if self.indice_pergunta_rap >= len(self.perguntasrap):
            return
    
        tela_rap = self.root.get_screen('rap')
        resposta_botao_rap = tela_rap.ids[answer_id]
        answer = resposta_botao_rap.text
        resposta_correta = self.perguntasrap[self.indice_pergunta_rap]['respostarap']

        if answer == resposta_correta:
            self.animar_botao_rap(resposta_botao_rap, True)
            self.mostrar_dialog('Resposta correta!!')
            self.pontuacao_rap += 1
            Clock.schedule_once(self.proxima_pergunta_rap, 1.6)
            self.tentativas = 0
        else:
            self.animar_botao_rap(resposta_botao_rap, False)
            self.tentativas += 1
            if self.tentativas >= self.maxtentativas:
                self.mostrar_dialog('Você excedeu o limite de tentativas, passando para a próxima pergunta!')
                self.tentativas = 0
                Clock.schedule_once(self.proxima_pergunta_rap, 1.6)
            else:
                self.mostrar_dialog('Resposta errada, você tem mais uma chance!')
                Clock.schedule_once(self.fechar_dialog, 1.6)


    def proxima_pergunta_rap(self, *args):
        if self.dialog:
            self.dialog.dismiss()
    
        tela_rap = self.root.get_screen('rap')
        botoes_rap = [tela_rap.ids.opcao1rap, tela_rap.ids.opcao2rap, tela_rap.ids.opcao3rap, tela_rap.ids.opcao4rap]
        for botao in botoes_rap:
            botao.md_bg_color = [0.84, 0.84, 0.84, 1]  

        self.indice_pergunta_rap += 1

        if self.indice_pergunta_rap < len(self.perguntasrap):
            self.carregar_pergunta_rap()
        else:
            self.mostrar_pontuacao_final_rap()


    def mostrar_pontuacao_final_rap(self):
        total_perguntas_rap = len(self.perguntasrap)
        pontuacao_texto = f'Você acertou {self.pontuacao_rap} de {total_perguntas_rap} perguntas.\n\n'

        if self.pontuacao_rap <= 2:
            resultado = 'Parece que tu não manja nada de rap, parça...'
        elif self.pontuacao_rap <= 5:
            resultado = 'Tá suave, mas dá pra dar um grau...'
        elif self.pontuacao_rap >= 6:
            resultado = 'Po, tu sabe mesmo, ein!!'
        elif self.pontuacao_rap == len(self.perguntasrock):
            resultado = 'Você é BRABO. Sabe muito sobre rap!!!'

        texto_dialog = pontuacao_texto + resultado

        self.dialog = MDDialog(
            title='Fim do Quiz!! Parabéns por chegar até aqui!',
            text=texto_dialog,
            buttons =[MDFlatButton(text='Início', on_release = lambda x: self.tela_inicio())],
            auto_dismiss=True
        )

        self.dialog.open()

    



    def tela_inicio(self, *args):
        if self.dialog:
            self.dialog.dismiss()
        self.root.transition.direction = 'right'
        self.root.current = 'login'
        self.indice_pergunta = 0
        self.indice_pergunta_rock = 0
        self.indice_pergunta_rap = 0
        self.pontuacao = 0
        self.pontuacao_rock = 0
        self.pontuacao_rap = 0
        self.tentativas = 0
        shuffle(self.perguntas)
        shuffle(self.perguntasrock)
        shuffle(self.perguntasrap)

    def tela_rock(self):
        self.root.transition.direction = 'left'
        self.root.current = 'rock'
        self.carregar_pergunta_rock()

    def tela_quiz(self):
        self.root.transition.direction = 'left'
        self.root.current = 'quiz'
        self.carregar_pergunta()
    
    def tela_rap(self):
        self.root.transition.direction = 'left'
        self.root.current = 'rap'
        self.carregar_pergunta_rap()

    def animar_botao(self, botao, correto):
        cor_resposta = [0, 1, 0, 1] if correto else [1, 0, 0, 1]
        cor_padrao = [1, 1, 1, 1]
        anim = Animation(md_bg_color=cor_resposta, duration=1)
        anim.bind(on_complete=lambda *args: Animation(md_bg_color=cor_padrao, duration=1).start(botao))
        anim.start(botao)

    def animar_botao_rock(self, botao, correto):
        cor_resposta = [0, 1, 0, 1] if correto else [1, 0, 0, 1]
        cor_padrao = [0.84, 0.84, 0.84, 1]
        anim = Animation(md_bg_color=cor_resposta, duration=1)
        anim.bind(on_complete=lambda *args: Animation(md_bg_color=cor_padrao, duration=1).start(botao))
        anim.start(botao)

    def animar_botao_rap(self, botao, correto):
        cor_resposta = [0, 1, 0, 1] if correto else [1, 0, 0, 1]
        cor_padrao = [0.84, 0.84, 0.84, 1]
        anim = Animation(md_bg_color=cor_resposta, duration=1)
        anim.bind(on_complete=lambda *args: Animation(md_bg_color=cor_padrao, duration=1).start(botao))
        anim.start(botao)

    def mostrar_dialog(self, message):
        if self.dialog:
            self.dialog.dismiss()
        self.dialog = MDDialog(
            title='Resultado',text = message,
            auto_dismiss=False, 
        )
        self.dialog.open()
        

    def fechar_dialog(self, dt):
        if self.dialog:
            self.dialog.dismiss()

    


if __name__ == '__main__':
    QuizApp().run()

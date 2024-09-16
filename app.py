from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFillRoundFlatButton, MDFillRoundFlatIconButton, MDFlatButton, MDRectangleFlatButton, MDRectangleFlatIconButton
from kivy.uix.popup import Popup
from kivy.clock import Clock
from random import shuffle
from kivymd.uix.dialog import MDDialog
from kivy.animation import Animation



KV = '''
ScreenManager:
    HomeScreen:
    

<HomeScreen>:
    name: 'login'
    MDFloatLayout:
        md_bg_color: [173/255, 216/255, 230/255, 1]

    Label:
        text: 'Bem vindo! Selecione o quiz que você deseja jogar:'
        pos_hint: {'center_y': .8}
        halign: 'center'
        font_size: '24sp'
        bold: True
        color: [32/255, 0/255, 66/255, 1]

    MDRaisedButton:
        pos_hint: {'center_x': .5, 'center_y': .5}
        halign: 'center'
        
        icon: 'music'
        text: 'MPB'
        md_bg_color: [1, 1, 1, 1]
        text_color: [0.2, 0.2, 0.6, 1]
        icon_color: [0, 0, 0, 1]
        font_name: 'C:/Users/joao_/OneDrive/Área de Trabalho/coisas/Poppins-SemiBold.ttf'

    MDRectangleFlatIconButton:
        pos_hint: {'center_x': .5, 'center_y': .4}
        halign: 'center'
       
        icon: 'earth'
        text: 'Geografia'
        md_bg_color: [1, 1, 1, 1]
        text_color: [0.2, 0.2, 0.6, 1]
        icon_color: [0, 0, 0, 1]
        font_name: 'C:/Users/joao_/OneDrive/Área de Trabalho/coisas/Poppins-SemiBold.ttf'

    MDFillRoundFlatIconButton:
        pos_hint: {'center_x': .5, 'center_y': .2}
        halign: 'center'
        
        icon: 'close'
        text: 'Sair'
        md_bg_color: [1, 1, 1, 1]
        text_color: [0.2, 0.2, 0.6, 1]
        icon_color: [0, 0, 0, 1]
        font_name: 'C:/Users/joao_/OneDrive/Área de Trabalho/coisas/Poppins-SemiBold.ttf'
'''

class HomeScreen(MDScreen):
    pass

class QuizApp(MDApp):
    def build(self):
        return Builder.load_string(KV)
    
if __name__ == '__main__':
    QuizApp().run()

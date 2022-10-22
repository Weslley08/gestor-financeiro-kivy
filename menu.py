import requests
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
kivy.require('1.10.0')

class Main(App):
    def build(self):
        return Gerenciador()

class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    pass

class Listagem(Screen):
    pass

class Conversor(Screen):
    def converter_moeda(self):
        moeda_origem = self.ids.moeda_origem.text
        moeda_destino = self.ids.moeda_destino.text
        url = f"https://gestor-financeiro.herokuapp.com/converter-moedas/{moeda_origem}/{moeda_destino}"

        cotacao = requests.get(url)
        json_cotacao = cotacao.json()
        data = json_cotacao["data"]
        print(data["valor_atual"])
    pass

Main().run()
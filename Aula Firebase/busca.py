import requests
import json

#request

link = "https://aulafirebase-9e6c5-default-rtdb.firebaseio.com/"

class Busca():
    def __init__(self) -> None:
        requisicao = requests.get(f'{link}/.json')
        print(requisicao)
        print(requisicao.text)
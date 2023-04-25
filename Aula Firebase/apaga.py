import requests
import json

#DELETE

link = "https://aulafirebase-9e6c5-default-rtdb.firebaseio.com/"

class Apaga():
    def __init__(self) -> None:
        id = input('Qual Id do usuario que deseja APAGAR :')
        requisicao = requests.delete(f'{link}/Users/{id}/.json')
        print(requisicao)
        print(requisicao.text)
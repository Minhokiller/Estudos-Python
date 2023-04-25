import requests
import json

#Patch

link = "https://aulafirebase-9e6c5-default-rtdb.firebaseio.com/"

class Patch():
    def __init__(self) -> None:
        
        id = input('Qual Id do usuario que deseja alterar')
        nome = input('qual o novo nome')
        dados = {'nome': nome}
        
        requisicao = requests.patch(f'{link}/Users/{id}/.json', data=json.dumps(dados))
        print(requisicao)
        print(requisicao.text)
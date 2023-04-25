import requests
import json

#post

link = "https://aulafirebase-9e6c5-default-rtdb.firebaseio.com/"

class Create_User():
    def __init__(self) -> None:
        id = input('ID do cliente: ')  # Solicitar o ID desejado do usuário
        nome = input('Nome do cliente: ')
        idade = int(input('Idade do cliente: '))
        cidade = input('Cidade onde mora: ')
        self.Verfica_idade(idade)

        dados = {'nome': nome, 'idade': idade, 'cidade': cidade, 'maior': self.maior}
        requisicao = requests.put(f'{link}/Users/{id}.json', data=json.dumps(dados))  # Usar o ID personalizado na URL da requisição
        print(requisicao)
        print(requisicao.text)
        print(self.maior)

    def Verfica_idade(self, idade):
        self.maior = "não"
        if idade >= 18:
            self.maior = "sim"

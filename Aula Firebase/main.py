import requests
import json

link = "https://aulafirebase-9e6c5-default-rtdb.firebaseio.com/"

#venda
#dados = {'cliente': 'andre', 'preco': '200', 'produto' : 'fone ouvido'}
#requisicao = requests.post(f'{link}/Vendas/.json', data=json.dumps(dados))
#print(requisicao)
#print(requisicao.text)

#editar

#dados = {'cliente': 'Craudio'}
#requisicao = requests.patch(f'{link}/Vendas/-NTskUESSNsQZH0aA5Ft.json', data=json.dumps(dados))
#print(requisicao)
#print(requisicao.text)

#request

requisicao = requests.get(f'{link}/Vendas/.json')
print(requisicao)
dic_requisicao = requisicao.json()
print(dic_requisicao['ID'])
for id_venda in dic_requisicao:
    cliente = dic_requisicao[id_venda]['cliente']
    if cliente == "Craudio":
        print(id_venda)
        id_andre = id_venda

#request

requisicao = requests.delete(f'{link}/Vendas/{id_andre}/.json')
print(requisicao)
print(requisicao.text)
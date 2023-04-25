import requests
import json
from auth import Auth
from post import Create_User
from patch import Patch
from busca import Busca
from apaga import Apaga

link = "https://aulafirebase-9e6c5-default-rtdb.firebaseio.com/"

auth = Auth()

while True:
    print("MENU:")
    print("1. Cadastra")
    print("2. Atualiza")
    print("3. Busca")
    print("4. Apaga")
    print("5. Sair")
    escolha = input("Escolha uma opção (1-5): ")

    if escolha == "1":
        print("Você escolheu a Opção 1.")
        Create_User()
    elif escolha == "2":
        print("Você escolheu a Opção 2.")
        Patch()
    elif escolha == "3":
        print("Você escolheu a Opção 3.")
        Busca()
    elif escolha == "4":
        print("Você escolheu a Opção 4.")
        Apaga()
    elif escolha == "5":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha novamente.")
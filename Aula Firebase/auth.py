import requests

# Dados de autenticação do usuário


email = input('Insira o Usuario: ')
senha = input('Insira a Senha: ')

# Endpoint de login por e-mail e senha
url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=XXX"

# Corpo da requisição
data = {
    "email": email,
    "password": senha,
    "returnSecureToken": True
}

class Auth():
    def __init__(self):
        # Faz a chamada HTTP POST
        response = requests.post(url, json=data)

        # Obtém a resposta em formato JSON
        response_json = response.json()

        # Verifica se a autenticação foi bem-sucedida
        if "idToken" in response_json:
            id_token = response_json["idToken"]
            print("Usuário autenticado com sucesso. ID do token:", id_token)
        else:
            print("Erro na autenticação:", response_json)
            exit()

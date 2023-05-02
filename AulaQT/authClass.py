import requests

# Endpoint de login por e-mail e senha
url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=xxx"

# Corpo da requisição
class Autentica():
    def __init__(self,email, senha):
        
        data = {
                "email": email,
                "password": senha,
                "returnSecureToken": True
                }
        # Faz a chamada HTTP POST
        response = requests.post(url, json=data)

        # Obtém a resposta em formato JSON
        response_json = response.json()

        # Verifica se a autenticação foi bem-sucedida
        if "idToken" in response_json:
            id_token = response_json["idToken"]
            print("Usuário autenticado com sucesso. ID do token:", id_token)
            self.stat1 = True
        else:
            print("Erro na autenticação:", response_json)
            self.stat1 = False
    def esta_autenticado(self):
        return self.stat1
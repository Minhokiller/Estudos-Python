import tkinter as tk
import boto3
from PIL import Image, ImageTk

# Configure o acesso ao S3
s3 = boto3.client('s3')

# Crie uma janela Tkinter
root = tk.Tk()
root.geometry('400x400')
root.title('Exibir Imagem do S3')

# Crie uma função para exibir a imagem
def exibir_imagem():
    # Obtenha o nome do arquivo da caixa de entrada
    nome_arquivo = nome_imagem.get()
    # Obtenha o objeto S3 da imagem
    objeto_imagem = s3.get_object(Bucket='teste-jadlog', Key=nome_arquivo)
    # Leia o conteúdo do objeto como uma imagem
    imagem = Image.open(objeto_imagem['Body'])
    # Exiba a imagem na janela Tkinter
    imagem_tk = ImageTk.PhotoImage(imagem)
    label_imagem.configure(image=imagem_tk)
    label_imagem.image = imagem_tk

# Crie uma entrada de texto e um botão na janela
nome_imagem = tk.Entry(root, width=30)
nome_imagem.pack(pady=10)
btn_exibir = tk.Button(root, text='Exibir Imagem', command=exibir_imagem)
btn_exibir.pack(pady=10)

# Crie um rótulo para exibir a imagem
label_imagem = tk.Label(root)
label_imagem.pack()

# Execute a janela Tkinter
root.mainloop()

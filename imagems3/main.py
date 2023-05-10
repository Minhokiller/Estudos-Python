import tkinter as tk
import boto3
from PIL import Image, ImageTk


s3 = boto3.client('s3')


root = tk.Tk()
root.geometry('400x400')
root.title('Exibir Imagem do S3')


def exibir_imagem():
    
    nome_arquivo = nome_imagem.get()
    
    objeto_imagem = s3.get_object(Bucket='teste-jadlog', Key=nome_arquivo)
    
    imagem = Image.open(objeto_imagem['Body'])
    
    imagem_tk = ImageTk.PhotoImage(imagem)
    label_imagem.configure(image=imagem_tk)
    label_imagem.image = imagem_tk

nome_imagem = tk.Entry(root, width=30)
nome_imagem.pack(pady=10)
btn_exibir = tk.Button(root, text='Exibir Imagem', command=exibir_imagem)
btn_exibir.pack(pady=10)

label_imagem = tk.Label(root)
label_imagem.pack()


root.mainloop()

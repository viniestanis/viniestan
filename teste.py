import customtkinter
from customtkinter import *

janela= customtkinter.CTk()
janela.geometry("500x300")

def clique():
    print("Fazer Login")


texto = customtkinter.CTkLabel(janela, text="Fazer Login")
texto.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text="Login",command=clique)
botao.pack(padx=10, pady=10)
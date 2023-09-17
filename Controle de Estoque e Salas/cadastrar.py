import customtkinter as ctk

janela = ctk.CTk()
janela.title("Cadastro de ITEM")

labelInicio = ctk.CTkLabel(janela, text="Cadastre o ITEM: ")

labelId = ctk.CTkLabel(janela, text="ID: ")
caixaId = ctk.CTkEntry(janela, placeholder_text="Digite o ID")

labelNome = ctk.CTkLabel(janela, text="NOME: ")
caixaNome = ctk.CTkEntry(janela, placeholder_text="Digite o Nome")

labelEspecificacao = ctk.CTkLabel(janela, text="ESPECIFICAÇÃO: ")
caixaEspecificacao = ctk.CTkEntry(janela, placeholder_text="Digite a Especificação")

janela.geometry("300x500")
janela.resizable(0,0)
janela.mainloop()
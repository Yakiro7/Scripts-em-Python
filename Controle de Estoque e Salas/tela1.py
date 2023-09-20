import customtkinter as ctk


#FUNÇÕES
def cadastrar_item():
    import cadastrar
    return cadastrar




#INTERFACE GRÁFICA
janela = ctk.CTk()
janela.title("Opções do controle de Estoque")

labelInicio = ctk.CTkLabel(janela, text="Escolha uma das opções: ")

labelEstoque = ctk.CTkLabel(janela, text="Controle de Estoque")
labelSalas = ctk.CTkLabel(janela, text="Controle de Salas")


botaoCadastro = ctk.CTkButton(janela, text="Cadastrar", command=cadastrar_item)
botaoAtualizar = ctk.CTkButton(janela, text="Atualizar")
botaoVizualizar = ctk.CTkButton(janela, text="Vizualizar")

botao1Cadastro = ctk.CTkButton(janela, text="Cadastrar", command=cadastrar_item)
botao1Atualizar = ctk.CTkButton(janela, text="Atualizar")
botao1Vizualizar = ctk.CTkButton(janela, text="Vizualizar")


labelInicio.place(x=120, y=10)

labelEstoque.place(x=20, y=70)
botaoCadastro.place(x=10, y=120)
botaoAtualizar.place(x=10, y=160)
botaoVizualizar.place(x=10, y=200)

labelSalas.place(x=210, y=70)
botao1Cadastro.place(x=200, y=120)
botao1Atualizar.place(x=200, y=160)
botao1Vizualizar.place(x=200, y=200)




janela.geometry("350x300")
janela.resizable(0,0)
janela.mainloop()
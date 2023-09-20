import customtkinter as ctk
import mysql.connector as my #pip install mysql-connector-python
from mysql.connector import errorcode
from datetime import date

#BANCO DE DADOS
try:
	db_connection = my.connect(host='localhost', user='root', password='13579', database='bd')
	conexao = "Conexão estabelecida!"
except my.Error as error:
	if error.errno == errorcode.ER_BAD_DB_ERROR:
		conexao = "O Banco de Dados não existe!"
	elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		conexao = "Usário ou Senha está errada!"
	else:
		conexao = error
		
cursor = db_connection.cursor()


def cadastrar():
            sql = "INSERT INTO ESTOQUE VALUES (%s, %s, %s, %s)"
            valores = caixaId.get(),caixaNome.get(),caixaEspecificacao.get(),caixaQuantidade.get()
            cursor.execute(sql, valores)
            db_connection.commit()


def mostrar_banco():
    sql_select_query = '''SELECT * FROM ESTOQUE'''
    cursor.execute(sql_select_query)
    registros = cursor.fetchall()
    print(registros)
    janela.destroy()

#INTERFACE GRÁFICA
janela = ctk.CTk()
janela.title("Cadastro de ITEM")

labelInicio = ctk.CTkLabel(janela, text="Cadastre o ITEM: ").grid(row=0, column=1, pady=20, padx=20)
labelConexao = ctk.CTkLabel(janela, text=conexao).grid(row=0, column=2, pady=20, padx=20)

labelId = ctk.CTkLabel(janela, text="ID: ").grid(row=1, column=1,padx=10, pady=10)
caixaId = ctk.CTkEntry(janela, placeholder_text="Digite o ID")
caixaId.grid(row=1, column=2,padx=10, pady=10)

labelNome = ctk.CTkLabel(janela, text="NOME: ").grid(row=2, column=1,padx=10, pady=10)
caixaNome = ctk.CTkEntry(janela, placeholder_text="Digite o Nome")
caixaNome.grid(row=2, column=2,padx=10, pady=10)

labelEspecificacao = ctk.CTkLabel(janela, text="ESPECIFICAÇÃO: ").grid(row=3, column=1,padx=10, pady=10)
caixaEspecificacao = ctk.CTkEntry(janela, placeholder_text="Digite a Especificação")
caixaEspecificacao.grid(row=3, column=2,padx=10, pady=10)

labelQuantidade = ctk.CTkLabel(janela, text="QUANTIDADE: ").grid(row=4, column=1,padx=10, pady=10)
caixaQuantidade = ctk.CTkEntry(janela, placeholder_text="Digite a Quatidade")
caixaQuantidade.grid(row=4, column=2,padx=10, pady=10)

botaoCadastrar = ctk.CTkButton(janela, text="Cadastrar", command=cadastrar).grid(row=5, column=2,padx=10, pady=10)
botaoSair = ctk.CTkButton(janela, text="Sair",command=mostrar_banco).grid(row=5, column=1,padx=10, pady=10)


janela.geometry("320x320")
janela.resizable(0,0)
janela.mainloop()
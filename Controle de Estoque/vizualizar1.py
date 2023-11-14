import customtkinter as ctk
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo
import mysql.connector as my #pip install mysql-connector-python
from mysql.connector import errorcode



def vizualizar():

    
    try:
        db_connection = my.connect(host='localhost', user='YURI',password='123456', database='bd',)
        conexao = "Conexão estabelecida!"
        cursor = db_connection.cursor()

    except my.Error as error:
        if error.errno == errorcode.ER_BAD_DB_ERROR:
            conexao = "O Banco de Dados não existe!"
        elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            conexao = "Usário ou Senha está errada!"
        else:
            conexao = error
        
    print('TODOS OS ITENS DA TABELA: ')
    sql_select_query = '''SELECT * FROM ESTOQUE'''
    cursor.execute(sql_select_query)
    registros = cursor.fetchall()

        
    janela = ctk.CTk()

    colunas = ("ID", "NOME", "MARCA", "ESPECIFICACAO", "QUANTIDADE")

    tree = ttk.Treeview(janela, columns=colunas,show = "headings")


    tree.heading("ID", text="ID")
    tree.heading("NOME", text="NOME")
    tree.heading("MARCA", text="MARCA")
    tree.heading("ESPECIFICACAO", text="ESPECIFICACAO")
    tree.heading("QUANTIDADE", text="QUANTIDADE")


    contacts = registros
    

    for contact in contacts:
        tree.insert('', tk.END, values=contact)

    def item_selected(event):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']
            # show a message
            showinfo(title='Information', message=','.join(record))


    tree.bind('<<TreeviewSelect>>', item_selected)

    tree.grid(row=0, column=0, sticky='nsew')

    # add a scrollbar
    scrollbar = ttk.Scrollbar(janela, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)


    scrollbar.grid(row=0, column=1, sticky='ns')



    janela.title("Vizualizar e Editar o Estoque")
    janela.geometry("820x350")
    janela.mainloop()

vizualizar()
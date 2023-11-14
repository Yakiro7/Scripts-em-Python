import customtkinter as ctk
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo
import mysql.connector as my #pip install mysql-connector-python
from mysql.connector import errorcode



def vizualizar():

    def item_selected(event):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']


    def deletar():
        sql_delete = 'DELETE FROM ESTOQUE WHERE ID = %s'
        valor_para_deletar = deletar_entry.get()
        valor_para_deletar = int(valor_para_deletar)
        cursor.execute(sql_delete, valor_para_deletar)
        db_connection.commit()
        print(f'Registro com o ID {sql_delete} foi deletado com sucesso!')

    #alterar dados do registro
    def item_selected(event):
        janela2 = ctk.CTk()

        janela2.title('Alterar dados do registro')
        janela2.geometry("300x200")
        janela2.mainloop()   


    #conexão com banco de dados
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

    


    tree.bind('<<TreeviewSelect>>', item_selected)

    

    # add a scrollbar
    scrollbar = ttk.Scrollbar(janela, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)


    

    deletar_por_id = ctk.CTkButton(janela, text='DELETAR', command=deletar)
    deletar_entry = ctk.CTkEntry(janela, placeholder_text='DIGITE O ID')

    tree.grid(row=0, column=0, sticky='nsew')
    scrollbar.grid(row=0, column=1, sticky='ns')
    deletar_por_id.place(x=150,y=230)
    deletar_entry.place(x=0,y=230)

    janela.title("Vizualizar e Editar o Estoque")
    janela.geometry("1020x350")
    janela.resizable(0,0)
    janela.mainloop()

vizualizar()
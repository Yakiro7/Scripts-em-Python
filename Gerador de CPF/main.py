import random
import tkinter
from tkinter import messagebox
import webbrowser

cpf = ''
def gerar():
    global cpf
    cpf_gerado = ''
    for i in range(9):
        cpf_gerado += str(random.randint(0,9))

    cpf = cpf_gerado

    indice = 10
    primeiro_numero = 0
    for numeros in cpf:
        novo_cpf = int(numeros) * indice
        indice -= 1
        primeiro_numero += novo_cpf

    primeiro_numero = (primeiro_numero * 10) % 11
    primeiro_numero = primeiro_numero if primeiro_numero <= 9 else 0

    cpf = str(cpf) + str(primeiro_numero)

    indice = 11
    segundo_numero = 0
    for numeros_2 in cpf:
        novo_cpf2 = int(numeros_2) * indice
        indice -= 1
        segundo_numero += novo_cpf2

    segundo_numero = (segundo_numero * 10) % 11
    segundo_numero = segundo_numero if segundo_numero <= 9 else 0
    
    cpf = str(cpf) + str(segundo_numero)

    
    cpf = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}'
    textocpf.delete(0, 'end')
    textocpf.insert(0, cpf)

def info():
    messagebox.showinfo('Apenas um teste', 'Programa criado apenas para fins didáticos')
    print("Desenvolvido por: Yuri Leal da Cruz")
    webbrowser.open("https://yurilealdacruz.github.io/")


janela = tkinter.Tk()
v = tkinter.IntVar()
texto = tkinter.StringVar()
janela.title('GERADOR DE CPF')

labeltitulo = tkinter.Label(janela, text='GERADOR DE CPF')
botarogerar = tkinter.Button(janela, text='GERAR NOVO CPF',command=gerar)
textocpf = tkinter.Entry(janela)
botaoinfo = tkinter.Button(janela, text='Clique para mais informações',command=info)




labeltitulo.place(x=100,y=0)
textocpf.place(x=100,y=30,width=110)
botarogerar.place(x=100,y=60)
botaoinfo.place(x=70,y=90)
janela.geometry('300x120')
janela.mainloop()
from time import sleep
from pytube import YouTube #pip install pytube
import tkinter as tk
import os
import moviepy.editor as mp #pip install moviepy
from tkinter import filedialog #Pretendo aadicionar uma aseleção de pasta para salvar o arquivo
import webbrowser
#Criando a opção de escolha entre vídeo e música
opcao = 0
def opcao1():
    global opcao
    texto.set('Selecionado Vídeo')
    opcao = 1
def opcao2():
    global opcao
    texto.set('Selecionado Música')
    opcao = 2


def teste():
    if opcao == 1:
        print(f"Opção vídeo {video_url.get()} {opcao}")
    else:
        print(f"Opção Música {video_url.get()} {opcao}")

def Donwload():
    #Função para pegar a URL que foi colocada no "Entry"
    link = video_url.get()
    yt = YouTube(link)
    
    if opcao == 1:
        #Download do Vídeo
        print('Você escolheu vídeo')
        video = yt.streams.get_highest_resolution()
        titulo = yt.title
        print(titulo)
        video.download()
    else:
        #Download o Audio
        print('Você escolheu música')
        musica = yt.streams.get_highest_resolution()
        titulo = yt.title
        print(titulo)
        musica.download()
        #Correção de Titulo
        chars = "'.,!{「」|}'|-|/"
        titulo = titulo.translate(str.maketrans('', '', chars))
        #Conversor para MP3
        mp4 = f'{titulo}.mp4'
        mp3 = f'{titulo}.mp3'
        clip = mp.VideoFileClip(mp4).subclip()
        clip.audio.write_audiofile(mp3)
        
    texto.set('Conclúido com Sucesso!')
    #os.remove(mp4) Ainda com problemas
    
def info():
    webbrowser.open('https://yurilealdacruz.github.io')

#Criação da interface Gráfica
janela = tk.Tk()
v = tk.IntVar()
texto = tk.StringVar()
texto.set('Escolha uma opção')

janela.title("Baixar Vídeos e Músicas do Youtube")
lblTitile = tk.Label(janela, text='Baixar vídeos e Músicas do Youtube')
lblLink = tk.Label(janela, text='Insira a URL do vídeo: ')
video_url = tk.Entry(janela)
baixar = tk.Button(janela, text='Baixar', command= Donwload)
btnDownloadV = tk.Radiobutton(janela, text='Vídeo', padx=20, variable=v, value=1, command= opcao1)
btnDownloadM = tk.Radiobutton(janela, text='Música',padx=30, variable=v, value=2, command= opcao2)
btnSair = tk.Button(janela, text='Sair', command= janela.destroy)
escolha1 = tk.Checkbutton(janela, text='Vídeo')
escolha2 = tk.Checkbutton(janela, text="Música")
lblDownload = tk.Label(janela, textvariable=texto)
btninfo = tk.Button(janela, text='Info', command=info)


lblTitile.grid()
lblLink.grid(row=1, column=0)
video_url.grid(row=1, column=1, ipadx= 200)
btnDownloadV.grid(row=2, column=0)
btnDownloadM.grid(row=3, column=0)
baixar.grid(row=3, column=1)
lblDownload.grid(row=3, columns=3)
btnSair.grid(row=4, column=0)
btninfo.grid(row=4, column=3)


janela.mainloop()


#Adicionar escolha entre resoluções
#verificar velocidade da rede e recomendar uma determinada resolução
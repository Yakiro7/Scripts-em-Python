#Conversor de arquivo em MP4 apra MP3
import tkinter as tk
import os
import moviepy.editor as mp #pip install moviepy
from tqdm import tqdm
import re
from tkinter import filedialog 

def conversor():
    arquivo2 = arquivo
    mp4 = arquivo
    mp3 = f'{arquivo}.mp3'
    clip = mp.VideoFileClip(mp4).subclip()
    clip.audio.write_audiofile(mp3)

def browseFiles(): 
    global arquivo
    arquivo = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Selecione o Arquivo em MP4: ", 
                                          filetypes = (("", 
                                                        "*.mp4*"), 
                                                       ("Todos os Arquivos (Só funciona em MP4)", 
                                                        "*.*"))) 
    label_file_explorer.configure(text='Arquivo Selecionado') 

janela = tk.Tk()
janela.title('Conversor de MP4 para MP3')
v = tk.IntVar()
texto = tk.StringVar()
texto.set('...')

labelcaminho = tk.Label(janela, text='Selecione o arquivo: ')
button_explore = tk.Button(janela, text = "Browse Files", command = browseFiles)  
label_file_explorer = tk.Label(janela, text = "Arguadando o Arquivo!",  fg = "blue")
converter = tk.Button(janela, text='Clique aqui para converter', command=conversor)

labelcaminho.place(x=120, y=20)
label_file_explorer.place(x=120, y=60)
button_explore.place(x=140, y=100)
converter.place(x=100, y=150)

janela.geometry('350x300')
janela.mainloop()

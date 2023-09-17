import customtkinter as ctk
import webbrowser


#FUNÇÕES
def abrir_tela1():
    if caixaLogin.get() == "Yuri" and caixaSenha.get() == "123":
        import tela1
        return tela1

def info():
    webbrowser.open("https://yurilealdacruz.github.io/")


#INTERFACE GRÁFICA
janela = ctk.CTk()
janela.title("Controle de Estoque e Salas")

ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")


textoPrincipal = ctk.CTkLabel(janela, text="Realizar o Login: ")
botaoLogin = ctk.CTkButton(janela, text="Entrar", corner_radius=10, command=abrir_tela1)
caixaLogin = ctk.CTkEntry(janela, placeholder_text="Digite seu Login")
caixaSenha = ctk.CTkEntry(janela, placeholder_text="Digite sua Senha", show="*")
botaoInfo = ctk.CTkButton(janela, text="Info", corner_radius=10,width=100, height=25 ,command=info)



textoPrincipal.pack(padx=10, pady=10)
caixaLogin.pack(padx=10, pady=10)
caixaSenha.pack(padx=10, pady=10)
botaoLogin.pack(padx=10, pady=10)

botaoInfo.place(relx=0.76, rely=0.87)


janela.geometry("500x260")
janela.resizable(0,0)
janela.mainloop()
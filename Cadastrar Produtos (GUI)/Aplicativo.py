import tkinter as tk
from tkinter import ttk
import ClassesBD as crud
import webbrowser

class principalBD:
  def __init__(self, win):
    self.objBD = crud.AppBD()

    self.lblCodigo = tk.Label(win, text='Código do Produto: ')
    self.lblNome = tk.Label(win, text='Nome do Produto: ')
    self.lblQuantidade = tk.Label(win, text='Quantidade de Produtos: ')
    self.lblPreco = tk.Label(win, text='Preço do Produto: ')

    self.txtCodigo = tk.Entry(bd=3)
    self.txtNome = tk.Entry()
    self.txtQuantidade = tk.Entry()
    self.txtPreco =tk.Entry()

    self.botaoCadastrar = tk.Button(win, text='Cadastrar', 
    command = self.fCadastrarProduto)
    self.botaoAtualizar = tk.Button(win, text='Atualizar',
    command = self.fAtualizarProduto)
    self.botaoExcluir = tk.Button(win, text='Excluir',
    command = self.fExcluirProduto)
    self.botaoLimpar = tk.Button(win, text='Limpar',
    command = self.fLimparTela)
    self.botaoInfo = tk.Button(win, text='Informações', 
    command= self.fInformacoes)

    self.dadosColunas = ('Código', 'Nome', 'Quantidade', 'Preço')

    self.treeProdutos = ttk.Treeview(win, 
    columns = self.dadosColunas,
    selectmode = 'browse')

    self.verscrlbar = ttk.Scrollbar(win, orient = 'vertical',
    command = self.treeProdutos.yview)

    self.verscrlbar.pack(side = 'right', fill = 'x')

    self.treeProdutos.configure(yscrollcommand=self.verscrlbar.set)

    self.treeProdutos.heading('Código', text='Código')
    self.treeProdutos.heading('Nome', text='Nome')
    self.treeProdutos.heading('Quantidade', text='Quantidade')
    self.treeProdutos.heading('Preço', text='Preço')

    self.treeProdutos.column('Código', minwidth=0, width=50)
    self.treeProdutos.column('Nome', minwidth=0, width=50)
    self.treeProdutos.column('Quantidade', minwidth=0, width=50)
    self.treeProdutos.column('Preço', minwidth=0, width=50)

    self.treeProdutos.pack(padx=10, pady=10)
    self.treeProdutos.bind('<<TreeviwerSelect>>',
    self.apresentarRegistrosSelecionados)

    self.lblCodigo.place(x=100, y=10)
    self.txtCodigo.place(x=250, y=10)

    self.lblNome.place(x=100, y=60)
    self.txtNome.place(x=250, y=60)

    self.lblQuantidade.place(x=100, y=110)
    self.txtQuantidade.place(x=250, y=110)

    self.lblPreco.place(x=100, y=160)
    self.txtPreco.place(x=250, y=160)

    self.botaoCadastrar.place(x=100, y=200)
    self.botaoAtualizar.place(x=200, y=200)
    self.botaoExcluir.place(x=300, y=200)
    self.botaoLimpar.place(x=400, y=200)
    self.botaoInfo.place(x=470, y=500)

    self.treeProdutos.place(x=25, y=250, width=550)
    self.verscrlbar.place(x=560, y=250, height=225)
    self.carregarDadosIniciais()

  def apresentarRegistrosSelecionados(self, event):
    self.fLimparTela()
    for selection in self.treeProdutos.selection():
      item = self.treeProdutos.item(selection)
      codigo, nome, quantidade, preco = item['values'][0:4]
      self.txtCodigo.insert(0, codigo)
      self.txtNome.insert(0, nome)
      self.txtQuantidade.insert(0, quantidade)
      self.txtPreco.insert(0, preco)

  def carregarDadosIniciais(self):
    try:
      self.id = 0
      self.iid = 0
      registros = self.objBD.selecionar_dados()
      print('Dados disponiveis no Banco de Dados')
      for item in registros:
        codigo = item[0]
        nome = item[1]
        quantidade = item[2]
        preco = item[3]
        
        print('Codigo = ', codigo )
        print('Nome = ', nome)
        print('Quantidade = ', quantidade)
        print('Preço = ', preco, '\n')

        self.treeProdutos.insert('', 'end',
        iid = self.iid,
        values = (codigo, nome, quantidade, preco))

        self.iid = self.iid + 1
        self.id = self.id + 1

      print('Dados da Base')
    except:
      print('Ainda não existem dados para carregar')

  def fLerCampos(self):
    try:
      print('Dados Disponíveis')

      codigo = int(self.txtCodigo.get())
      print('codigo', codigo)

      nome = self.txtNome.get()
      print('nome', nome)

      quantidade = int(self.txtQuantidade.get())
      print('quantidade', quantidade)

      preco = float(self.txtPreco.get())
      print('preco', preco)

      print('Leitura dos dados com suceso!')
    except:
      print('Não foi possível ler os dados')
    
    return codigo, nome, quantidade, preco

  def fCadastrarProduto(self):
    try:
      print('Dados disponiveis')

      codigo, nome, quantidade, preco = self.fLerCampos()
      self.objBD.inserir_dados(codigo, nome, quantidade, preco)
      self.treeProdutos.insert('', 'end',
      iid = self.iid,
      values = (codigo, nome, quantidade, preco))

      self.iid = self.iid + 1
      self.id = self.id + 1
      self.fLimparTela()
      print('Produto Cadastrado com sucesso!')
    except:
      print('Não foi possível cadastrar o produto')

  def fAtualizarProduto(self):
    try:
      print('Dados disponíveis')
      codigo, nome, quantidade, preco = self.fLerCampos()
      self.objBD.atualizar_dados(codigo, nome, quantidade, preco)
      
      self.treeProdutos.delete(*self.treeProdutos.get_children())
      self.carregarDadosIniciais()
      self.fLimparTela()
      print('Produto atualizado com sucesso')
    except:
      print('Não foi possível atualizar o produto')

  def fExcluirProduto(self):
    try:
      print('Dados disponiveis')
      codigo, nome, quantidade, preco = self.fLerCampos()
      self.objBD.excluir_dados(codigo)

      self.treeProdutos.delete(*self.treeProdutos.get_children())
      self.carregarDadosIniciais()
      self.fLimparTela()
      print('Produto excluido com sucesso!')
    
    except:
      print('Não foi possível excluir o produto')

  def fLimparTela(self):
    try:
      print('Dados disponiveis')

      self.txtCodigo.delete(0, tk.END)
      self.txtNome.delete(0, tk.END)
      self.txtQuantidade.delete(0, tk.END)
      self.txtPreco.delete(0, tk.END)

      print('Campos limpos!')
    except:
      print('Não foi possível limpar os campos')
  
  def fInformacoes(self):
    print("Desenvolvido por: Yuri Leal da Cruz")
    webbrowser.open("https://yurilealdacruz.github.io/")


janela = tk.Tk()
principal = principalBD(janela)
janela.title('Bem vindo ao Aplicativo: Cadastrar produtos usando o Banco de Dados')
janela.geometry('600x550+10+10')
janela.mainloop()















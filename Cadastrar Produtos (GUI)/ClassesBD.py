
import psycopg2 as pg

class AppBD:
  def __init__(self):
    print('Método construtor')

  def abrir_conexao(self):
    try:
      self.conexao = pg.connect(host='127.0.0.1',
      port='5432',
      user='postgres',
      password='1234',
      database='dbestudo')
      
      print('Conexão realizada com sucesso!')
    except (Exception, pg.Error) as erro:
      if (self.conexao):
        print('Ocorreu um erro ao conectar ao banco de dados, erro: ',erro)
      
  def selecionar_dados(self):
    try:
      self.abrir_conexao()
      cursor = self.conexao.cursor()
      print('Selecionando todos os produtos')
      sql_select_query = '''SELECT * FROM PRODUTO'''
      cursor.execute(sql_select_query)
      registros = cursor.fetchall()
      print(registros)

    except (Exception, pg.Error) as erro:
      print('Ocorreu um erro e não foi possível selecionar a tabela, erro: ',erro)

    finally:
      if (self.conexao):
        cursor.close()
        self.conexao.close()
        print('A conexão com o PostgreSQL foi encerrada')
    
    return registros

  def inserir_dados(self, codigo, nome, preco):
    try:
      self.abrir_conexao()
      cursor = self.conexao.cursor()
      inserir_query = '''INSERT INTO PRODUTO VALUES (%s, %s, %s);'''
      inserir_registro = (codigo, nome, preco)
      cursor.execute(inserir_query,inserir_registro)
      self.conexao.commit()
      contagem = cursor.rowcount()
      print(contagem, ' Registro(s) inserido(s) com sucesso na tabela')
    except (Exception, pg.Error) as erro:
      print('Falha ao inserir registro da tabela, erro: ', erro)

    finally:
      if (self.conexao):
        cursor.close()
        self.conexao.close()
        print('A conexao com o PostgreSQL foi encerrada')

  def atualizar_dados(self, codigo, nome, preco):
    try:
      self.abrir_conexao()
      cursor = self.conexao.cursor()

      print('Registro antes da atualização')
      sql_select_query = '''SELECT * FROM PRODUTO WHERE CODIGO = %s'''
      cursor.execute(sql_select_query, (codigo,))
      registro = cursor.fetchone()
      print(registro)

      sql_update_query = '''UPDATE PRODUTO SET NOME = %s, PRECO = %s 
      WHERE CODIGO = %s'''

      cursor.execute(sql_update_query, (nome, preco, codigo))

      registro = cursor.fetchone()
      print(registro)

    except (Exception, pg.Error) as erro:
      print('Erro ao atualizar erro: ', erro)
    
    finally:
      if (self.conexao):
        cursor.close()
        self.conexao.close()
        print('A conexao com o PostgreSQL foi encerrada')
    
  def excluir_dados(self, codigo):
    try:
      self.abrir_conexao()
      cursor = self.conexao.cursor()
      sql_delete_query = '''DELETE FROM PRODUTO WHERE CODIGO = %s'''
      cursor.execute(sql_delete_query, (codigo,))
      self.conexao.commit()
      contagem = cursor.rowcount()
      print(contagem, ' Registro foi excluido da tabela')
    except (Exception, pg.Error) as erro:
      print('Ocorreu um erro e não foi possível excluir, erro: ', erro)
    finally:
      if (self.conexao):
        cursor.close()
        self.conexao.close()
        print('A conexao com o PostgreSQL foi encerrada')





    



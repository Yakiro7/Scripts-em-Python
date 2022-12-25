import psycopg2 as pg

try:
  conexao = pg.connect(host='127.0.0.1',port='5432',database='produtos',user='postgres',password='123')
  print('Conexão realizada com sucesso!')
except pg.DatabaseError as erro:
  print('Ocorreu um erro e não foi possível conectar ao banco de dados: ',erro)

cursor = conexao.cursor()

cursor.execute('''
  CREATE TABLE PRODUTO (
    CODIGO INT PRIMARY KEY NOT NULL,
    NOME TEXT NOT NULL,
    QUANTIDADE INT NOT NULL,
    PRECO REAL NOT NULL
  );
''')
print('Tabela criada com sucesso!')
conexao.commit()
conexao.close()
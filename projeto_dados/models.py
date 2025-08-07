from database import get_connection # Importa a função get_connection do módulo database

def criar_tabela():
    """Cria a tabela de usuários se não existir."""
    conn = get_connection() # Obtém a conexão com o banco de dados
    cursor = conn.cursor() # Cria um cursor para executar comandos SQL
    #                       # Cursor é um objeto que permite executar comandos SQL e manipular os resultados
    cursor.execute('''
                   CREATE TABLE  IF NOT EXISTS usuarios (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome TEXT NOT NULL,
                       idade INTEGER NOT NULL,
                       email TEXT NOT NULL UNIQUE
                   )
                   ''') # Cria a tabela 'usuarios' com colunas 'id', 'nome', 'idade' e 'email'
    conn.commit() # Salva as alterações no banco de dados
    conn.close() # Fecha a conexão com o banco de dados
    
def inserir_usuario(nome, idade, email):
    """Insere um novo usuário na tabela.""" # As aspas triplas são usadas para criar uma string de várias linhas
    conn = get_connection() # Obtém a conexão com o banco de dados
    cursor = conn.cursor() # Cria um cursor para executar comandos SQL
    cursor.execute('''
                   INSERT INTO usuarios (nome, idade, email)
                   VALUES (?, ?, ?)
                   ''', (nome, idade, email)) # Insere um novo usuário com os valores fornecidos
    conn.commit()
    conn.close()
    
def listar_usuários():
    """Retorna uma lista de todos os usuários na tabela."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.ececute('''
                   SELECT * FROM usuarios
                   ''') # Seleciona todos os usuários da tabela
    usuarios = cursor.fetchall() # Obtém todos os resultados da consulta
    conn.close() # Fecha a conexão com o banco de dados
    return usuarios # Retorna a lista de usuários
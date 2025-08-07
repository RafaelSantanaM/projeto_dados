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
    # Comandos SQL são representados com letras maiúsculas.
    # IF NOT EXISTS garante que a tabela só será criada se ela não existir
    # AUTOINCREMENT faz com que o ID seja incrementado automaticamente
    # NOT NULL garante que os campos não podem ser nulos
    # UNIQUE garante que o email não pode ser duplicado
    
    conn.commit() # Salva as alterações no banco de dados
    conn.close() # Fecha a conexão com o banco de dados
    
def inserir_usuario(nome, idade, email):
    """Insere um novo usuário na tabela.""" # As aspas triplas são usadas para criar uma string de várias linhas
                                            # Esta é uma boa prática para documentar funções
                                            # Isso é conhecido como docstring
                                            # A docstring deve descrever o que a função faz, seus parâmetros e o que retorna
                                            # As docstrings são úteis para gerar documentação automática e para ajudar outros desenvolvedores a entenderem o código
                                            # As docstrings são escritas entre aspas triplas e podem ser acessadas através do atributo __doc__ da função
                                            # Não afetam a execução do código, mas são uma boa prática de programação
                                            
    conn = get_connection() # Obtém a conexão com o banco de dados
    cursor = conn.cursor() # Cria um cursor para executar comandos SQL
    cursor.execute('''
                   INSERT INTO usuarios (nome, idade, email)
                   VALUES (?, ?, ?)
                   ''', (nome, idade, email)) # Insere um novo usuário com os valores fornecidos
    conn.commit()
    conn.close()
    
def listar_usuarios():
    """Retorna uma lista de todos os usuários na tabela."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
                   SELECT * FROM usuarios
                   ''') # Seleciona todos os usuários da tabela
    # O asterisco (*) indica que queremos selecionar todas as colunas
    # O SELECT é usado para consultar dados no banco de dados
    # O FROM indica de qual tabela queremos selecionar os dados
    # O WHERE é usado para filtrar os resultados, mas não é necessário aqui porque queremos
    
    usuarios = cursor.fetchall() # Obtém todos os resultados da consulta
    conn.close() # Fecha a conexão com o banco de dados
    return usuarios # Retorna a lista de usuários
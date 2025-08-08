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
    return True
    
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
    return True
    
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

def atualizar_usuario(id, nome, idade, email):
    """Atualiza os dados de um usuário existente na tabela."""
    conn = get_connection()
    cursor = conn.cursor()
    conn.execute('''
                   UPDATE usuarios
                     SET nome = ?, idade = ?, email = ?
                     WHERE id = ?
                     ''', (nome, idade, email, id)) # Atualiza os dados do usuário com o ID fornecido
    # O UPDATE é usado para atualizar dados no banco de dados
    # O SET indica quais colunas queremos atualizar e com quais valores
    # O WHERE é usado para especificar qual registro queremos atualizar
    
    conn.commit() # Salva as alterações no banco de dados
    conn.close() # Fecha a conexão com o banco de dados
    return True # Retorna True para indicar que a atualização foi bem-sucedida
    # Retornar True é uma boa prática para indicar que a operação foi bem-sucedida
    # Isso pode ser útil para verificar se a operação foi bem-sucedida em outras partes
    # do código, como em testes ou em outras funções que chamam esta função
    
def deletar_usuario(id):
    """Deleta um usuário da tabela pelo ID."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
                   DELETE FROM usuarios
                   WHERE id = ?
                   ''', (id,)) # Deleta o usuário com o ID fornecido
    # Sintaxe: DELETE FROM tabela WHERE condição
    # É como se fosse uma pergunta: Deletar da tabela `tabela`. Onde? `condição(resposta)` 
    # A vírgula após (id,) é necessária para passar uma tupla com um único elemento
    # Isso é necessário porque o método execute espera uma tupla como segundo argumento
    
    conn.commit()
    conn.close()
    return True

def usuario_existe(id):
    """Verifica se existe um usuário com o ID fornecido."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT 1 FROM usuarios WHERE id = ?', (id,)) # Aqui não usamos aspas triplas porque a query é curta
    # O SELECT 1 é uma prática comum para verificar a existência de um registro
    # Ele retorna 1 se o registro existir, o que é suficiente para nossa verificação
    
    resultado = cursor.fetchone() # Obtém o primeiro resultado da consulta
     # O fetchone retorna uma tupla com os dados do registro ou None se não houver resultados
    conn.close()
    return resultado is not None # Retorna True se o usuário existir, caso contrário False
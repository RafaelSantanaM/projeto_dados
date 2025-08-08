import sqlite3

def get_connection(): #função que retorna a conexão para ser usada em outros módulos
    """Cria e retorna uma conexão com o banco de dados SQLite.""" 
    conn = sqlite3.connect('dados.db') #Cria ou conecta ao banco de dados 'dados.db'
    return conn
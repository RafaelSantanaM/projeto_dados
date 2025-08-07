from models import criar_tabela, inserir_usuario, listar_usuarios
# O import pode ser feito de múltiplas funções, usando a vírgula para separar os nomes

def menu(): # Cria um menu interativo para o usuário
    print("1. Inserir Usuário")
    print("2. Listar Usuários")
    print("3. Sair")
    
def main(): #Cria a função principal do programa
    criar_tabela() # Chama a função para criar a tabela de usuários
    while True: # Inicia um loop infinito par o menu
        menu()
        escolha = int(input('Escolha uma opção: '))
        if escolha == 1:
            nome = input('Nome: ')
            idade = int(input('Idade: '))
            email = input('Email: ')
            inserir_usuario(nome, idade, email)
            print('Usuário inserido com sucesso!')
        elif escolha == 2:
            usuarios = listar_usuarios()
            for usuario in usuarios: # Faz um loop para imprimir cada usuário
                print(f'ID: {usuario[0]} - Nome: {usuario[1]} - Idade: {usuario[2]} - Email: {usuario[3]}')
                # Nesta parte, a variável usuario é uma tupla com os dados do usuário
        elif escolha == 3:
            print('Saindo...')
            break
        else: 
            print('Opção inválida!\n')
            
if __name__ == '__main__': # Verifica se o script está sendo executado diretamente
    main() # Chama a função principal do programa
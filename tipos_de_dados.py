# Nome, idade, altura

pessoas = []

pessoa = {}


def exibirOpcoes():
    print('\n\nEscolha uma das opções:')
    print("Inserir (I)")
    print("Remover (R)")
    print("Exibir Cadastros (E)")
    print("Sair (S)")


def inserirPessoa():
    pessoa = {}
    pessoa['nome'] = input('Nome: ')
    pessoa['idade'] = input('Idade: ')
    pessoa['altura'] = input('Altura: ')
    pessoas.append(pessoa)


opcao = 'E'

while opcao != 'S':

    exibirOpcoes()
    opcao = input('Digite a opção: ')

    if opcao == 'I':
        inserirPessoa()

    elif opcao == 'E':
        print(pessoas)
        print('{0} pessoas cadastradas.'.format(len(pessoas)))

    elif opcao == 'R':
        nome = input('Nome para remover: ')
        temp = []
        for item in pessoas:
            if nome != item['nome']:
                temp.append(item)
        if len(pessoas) == len(temp):
            print('O nome não foi encontrado!')
        else:
            pessoas = temp

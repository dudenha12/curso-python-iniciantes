import os
# Adicionar itens
# Remover itens
# Exibir itens e total
# Limpar

produtos = (
    {'id': 1, 'nome': 'Notebook', 'preco': 2800},
    {'id': 2, 'nome': 'Mouse', 'preco': 38.55},
    {'id': 3, 'nome': 'Teclado', 'preco': 85.48},
    {'id': 4, 'nome': 'Monitor', 'preco': 850.89}
)

carrinho = []


def exibirOpcoes():
    print('\n\n')
    print('1 - Adicionar Item')
    print('2 - Remover Item')
    print('3 - Exibir itens e o valor total')
    print('4 - Limpar Carrinho de compras')
    print('5 - Sair')


def exibirProdutos():
    for p in produtos:
        print(
            'Id: {0} - Nome: {1} - Preço: {2}\n'.format(p['id'], p['nome'], p['preco']))


opcao = '1'

os.system('clear')
print('Carrinho de Compras \n')


def obterNomeProduto(id):
    for p in produtos:
        if p['id'] == id:
            return p['nome']


while opcao != '5':
    exibirOpcoes()
    opcao = input('Digite a opção: ')

    if opcao == '1':
        exibirProdutos()
        id = int(input('Digite o identificador do produto: '))
        quantidade = int(input('Digite quantidade: '))
        carrinho.append({'id': id, 'quantidade': quantidade})

    if opcao == '2':
        id = int(input('Digite o identificador do produto: '))
        temp = []
        for item in carrinho:
            if item['id'] != id:
                temp.append(item)

    if opcao == '3':
        print('\n\n')
        somatorio = 0
        for item in carrinho:
            for produto in produtos:
                if produto['id'] == item['id']:
                    somatorio = somatorio + \
                        (produto['preco'] * item['quantidade'])
                    break

            print(
                'Nome: {0} - Quantidade: {1}'.format(obterNomeProduto(item['id']), item['quantidade']))
        print('Preço total: {0}'.format(somatorio))

    if opcao == '4':
        carrinho = []

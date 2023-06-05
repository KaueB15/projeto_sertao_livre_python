def verificarLogin_duplicado(lista, dicionario):
    while(True):
        parar = True
        cadastroLogin = input('Digite o Login - ')
        for cadastroNovo in lista:
            if(cadastroLogin == cadastroNovo['Login']):
                print(40*'=')
                print('Login já existente')
                print('Cadastro invalido, tente novamente.')
                print(40*'=')
                parar = False
                break
            else:
                parar = True
        if(parar == True):
            dicionario['Login'] = cadastroLogin
            break
        
def verificar_CPF(lista, dicionario):
    while(True):
        parar = True
        cpf = int(input('Digite seu CPF (sem . e -) - '))
        if(len(str(cpf)) == 11):
            for cadastroNovo in lista:
                if(cpf == cadastroNovo['CPF']):
                    print(40*'=')
                    print('CPF já existente')
                    print('Cadastro invalido, tente novamente.')
                    print(40*'=')
                    parar = False
                    break
                else:
                    parar = True
            if(parar == True):
                dicionario['CPF'] = cpf
                break
        else:
            print(40*'=')
            print('CPF invalido, digite novamente.')
            print(40*'=')

def verificar_idade(dicionario):
    while(True):
        anoNascimento = int(input('Digite seu ano de nascimento - '))
        if(len(str(anoNascimento)) == 4):
            if(2023 - anoNascimento >= 18):
                dicionario['Ano de Nascimento'] = anoNascimento
                break
            else:
                print(40*'=')
                print('Menor de 18 anos não pode se cadastrar')
                print(40*'=')
        else:
            print(40*'=')
            print('Ano invalido, digite os 4 numeros')
            print(40*'=')

def verificar_CEP(dicionario):
    while(True):
        cep = int(input('Digite seu CEP (sem o -) - '))
        if(len(str(cep)) == 8):
            dicionario['CEP'] = cep
            break
        else:
            print(40*'=')
            print('CEP digitado é invalido')
            print(40*'=')

def verificar_celular(dicionario):
    while(True):
        celular = int(input('Digite o numero do seu celular parar contato (com ddd) - '))
        if(len(str(celular)) == 11):
            dicionario['Celular'] = celular
            break
        else:
            print(40*'=')
            print('O numero digitado é inválido')
            print(40*'=')

def cadastrarUsuario_cliente(lista):
    cadastro = {}
    verificarLogin_duplicado(lista, cadastro)
    cadastro['Senha'] = input('Digite a Senha - ')
    cadastro['Nome'] = input('Digite seu Nome - ')
    verificar_CPF(lista, cadastro)
    verificar_idade(cadastro)
    verificar_CEP(cadastro)
    cadastro['Bairro'] = input('Digite o seu bairro - ')
    cadastro['Numero'] = int(input('Digite o numero de sua residencia - '))
    verificar_celular(cadastro)
    lista.append(cadastro)
    print(40*'=')
    print('Usuario cadastrado com sucesso')
    
def buscarProdutos_cliente(lista):
    achei = False
    busca = input('O que está procurando - ')
    for produto in lista:
        if(produto['Tipo'].find(busca) >= 0 or produto['Marca'].find(busca) >= 0 or produto['Modelo'].find(busca) >= 0):
                print(40*'=')
                print(f'Tipo - ' + produto['Tipo'])
                print(f'Modelo - ' + produto['Modelo'])
                print(f'Ficha Tecnica - ' + produto['Especificacao'])
                print(f'Quantidade - ' + str(produto['Quantidade']))
                print(f'Valor - ' + str(produto['Valor']))
                print(f'Codigo - ' + str(produto['Codigo']))
                print(f'Vendedor - ' + produto['Vendedor'])
                achei = True
    if(achei == False):
        print(40*'=')
        print('Nada encontrado.')
    return achei    

def comprarProdutos(lista1, login, lista2):
    if(buscarProdutos_cliente(lista1)):
        print(40*'=')
        comprados = {}
        codigoProduto_compra = int(input('Digite o codigo do produto que deseja comprar - '))
        quantidadeCompra = int(input('Digite quantos produtos quer comprar - '))
        for produto in lista1:
            if(produto['Codigo'] == codigoProduto_compra):
                if(produto['Quantidade'] == 0):
                    print(40*'=')
                    print('Produto sem estoque')
                else:
                    novaQuantidade = produto['Quantidade'] - quantidadeCompra
                    produto['Quantidade'] = novaQuantidade
                    comprados['Nome_Produto'] = produto['Modelo']
                    comprados['Quantidade_Compra'] = quantidadeCompra
                    comprados['Valor_Unitario'] = produto['Valor']
                    comprados['Usuario_Comprou'] = login
                    lista2.append(comprados)
                    print(40*'=')
                    print('Produto comprado com sucesso')
                    
def listarCompras(lista, login):
    for produto in lista:
        if(produto['Usuario_Comprou'] == login):
            print(40*'=')
            print(f'Produto - ' + produto['Nome_Produto'])
            print(f'Quantidade - ' + str(produto['Quantidade_Compra']))
            print(f'Valor - ' + str(produto['Valor_Unitario']))
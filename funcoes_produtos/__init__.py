import openai
import matplotlib.pyplot as plt

def cadastrarProdutos(lista, login):
    produto = {}
    while(True):
        produto['Tipo'] = input('Digite o tipo de produto a ser vendido - ')
        produto['Modelo'] = input('Digite o modelo do produto - ')
        produto['Marca'] = input('Digite a marca do produto - ')
        produto['Especificacao'] = input('Digite as especificações do produto - ')
        produto['Valor'] = float(input('Digite o valor do produto - '))
        produto['Quantidade'] = int(input('Digite quantos produtos estarão a venda - '))
        produto['Vendedor'] = login
        codigoProduto = int(input('Digite o codigo do produto - '))
        colocado = True
        for produtoCodigo in lista:
            if(produtoCodigo['Codigo'] == codigoProduto):
                print(40*'=')
                print('Codigo invalido, produto não cadastrado.')
                colocado = False
                break
            else:
                colocado = True
        if(colocado == False):
            break
        else:
            produto['Codigo'] = codigoProduto
        lista.append(produto)
        print(40*'=')
        print('Produto Cadatrado')
        break
    
def buscarProdutos_vendedor(lista, login):
    achei = False
    busca = input('O que está procurando - ')
    for produto in lista:
        if(produto['Tipo'].find(busca) >= 0 or produto['Marca'].find(busca) >= 0 or produto['Modelo'].find(busca) >= 0):
            if(produto['Vendedor'] == login):
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
        
def removerProdutos(lista, login):
    if(buscarProdutos_vendedor(lista, login)):
        removerProduto = False
        print(40*'=')
        codigoSelecionado = int(input('Digite o codigo o produto que quer remover - '))
        for remover in lista:
            if(remover['Codigo'] == codigoSelecionado):
                indexProduto = lista.index(remover)
                if(lista[indexProduto]['Vendedor'] == login):
                    produtoRemover = lista.index(remover)
                    removerProduto = True
        
        if(removerProduto == False):
            print(40*'=')
            print('Vendedor não confirmado')
            print('Produto não Removido')
            print(40*'=')
    
        if(removerProduto == True):
            if(lista[indexProduto]['Vendedor'] == login):
                lista.pop(produtoRemover)
                print(40*'=')
                print('Produto Removido')
            
def atualizarProdutos(lista, login):
    if(buscarProdutos_vendedor(lista, login)):
        atualizarProduto = False
        codigoSelecionado = int(input('Digite o codigo o produto que quer atualizar - '))
        for produto in lista:
            if(produto['Codigo'] == codigoSelecionado):
                indexProduto = lista.index(produto)
                if(lista[indexProduto]['Vendedor'] == login):
                    produtoAtualizar = lista.index(produto) 
                    atualizarProduto = True
        
        if(atualizarProduto == False):
            print(40*'=')
            print('Vendedor invalido')
            print('Esse produto não é seu')
            
        if(atualizarProduto == True):        
                print(40*'=')
                print('O QUE QUER ATUALIZAR?')
                print('1 - Valor')
                print('2 - Modelo')
                print('3 - Especificacao')
                print(40*'=')
                
                opcaoAtualizar = int(input('O que quer atualizar - '))
                
                if(opcaoAtualizar == 1):
                    valorNovo = float(input('Digite o novo valor - '))
                    produto['Valor'] = valorNovo
                    print(40*'=')
                    print('Valor atualizado.')
                elif(opcaoAtualizar == 2):
                    modeloNovo = input('Digite o novo modelo - ')
                    produto['Modelo'] = modeloNovo
                    print(40*'=')
                    print('Modelo atualizado.')
                elif(opcaoAtualizar == 3):
                    especificacaoNova = input('Digite a nova especificacao - ')
                    produto['Especificacao'] = especificacaoNova
                    print(40*'=')
                    print('Especificação atualizado.')    
                else:
                    print(40*'=')
                    print('Opção invalida')
                    
def consultarCHATGPT(produto):
    openai.api_key = 'sua chave'
    
    # Set the model and prompt
    model_engine = "text-davinci-003"
    prompt = 'Me diga resumidamente o que você acha sobre o produto ' + produto + ' ?'
    # Set the maximum number of tokens to generate in the response
    max_tokens = 1024

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Print the response
    return completion.choices[0].text

def gerarGrafico(lista, login):
    # creating the dataset
    for produto in lista:
        if(produto['Vendedor'] == login):
            modeloProduto = produto['Modelo']
            quantidadeProduto =  produto['Quantidade'] 
    courses = list(modeloProduto)
    values = list(quantidadeProduto)

    fig = plt.figure(figsize=(10, 5))

    # creating the bar plot
    plt.bar(courses, values, color='red',
            width=0.4)

    plt.xlabel("Produtos")
    plt.ylabel("Quantidade")
    plt.title("Sertao Livre")
    plt.show()
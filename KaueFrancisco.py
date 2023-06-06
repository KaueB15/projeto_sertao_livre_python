from funcoes_produtos import *
from funcoes_clientes import *
from funcoes_vendedor import *
from funcoes_menus import *

cadastros_vendedor = [{'Login': 'KaueCardz', 'Senha': 'senha', 'Nome': 'Kaue', 'Sobrenome': 'Batista', 'CPF': '02030202133', 'Ano de Nascimento': 2003}]
cadastros_clientes = [{'Login': 'KaueCardz', 'Senha': 'senha', 'Nome': 'Kaue', 'Sobrenome': 'Batista', 'CPF': '02030202133', 'Ano de Nascimento': 2003}]
produtos = [{'Tipo': 'Moto', 'Modelo': 'F800', 'Marca': 'BMW', 'Especificacao': 'Preta', 'Valor': 90000.0, 'Quantidade': 10, 'Vendedor': 'KaueCardz', 'Codigo': 1}]
produtosComprados = []

valor = True

while(valor != False):
    menuInicial()
    opcaoInicial = int(input('Digite a opção desejada - '))
    
    if(opcaoInicial == 1):
        while(True):
            menuVendedor()
            opcaoVendedor = int(input('Digite a opção desejada - '))
            
            if(opcaoVendedor == 1):
                cadastrarUsuario_vendedor(cadastros_vendedor)

            elif(opcaoVendedor == 2):
                login = input('Digite seu Login - ')
                senha = input('Digite sua Senha - ')
                if(validarLogin(cadastros_vendedor, login, senha)):
                    usuarioLogado = login
                    logado = True

                    while(logado):
                        menuPrincipal_vendedor()
                        opcaoPrincipal_vendedor = int(input('Digite a opção desejada - '))

                        if(opcaoPrincipal_vendedor == 1): 
                            atualizarDados(cadastros_vendedor, usuarioLogado)
                            
                        elif(opcaoPrincipal_vendedor == 2):
                            cadastrarProdutos(produtos, usuarioLogado)
                            print(produtos)
                                                            
                        elif(opcaoPrincipal_vendedor == 3):
                            buscarProdutos_vendedor(produtos, usuarioLogado)
                        
                        elif(opcaoPrincipal_vendedor == 4):
                            removerProdutos(produtos, usuarioLogado)

                        elif(opcaoPrincipal_vendedor == 5): 
                            atualizarProdutos(produtos, usuarioLogado)
                        
                        elif(opcaoPrincipal_vendedor == 6):
                            gerarGrafico(produtos, usuarioLogado)
                            
                        elif(opcaoPrincipal_vendedor == 0): 
                            logado = False
                            
                        else:
                            print('Opção Invalida')
                                        
                        if(logado == False):
                            print(40*'=')
                            print('Deslogado com sucesso.')
                            break
                        
            elif(opcaoVendedor == 0):
                break
    
    elif(opcaoInicial == 2):
        while(True):
            menuCliente()
            opcaoCliente = int(input('Digite a opção desejada - '))
            
            if(opcaoCliente == 1):
                cadastrarUsuario_cliente(cadastros_clientes)
                
            elif(opcaoCliente == 2):
                login = input('Digite seu Login - ')
                senha = input('Digite sua Senha - ')
                if(validarLogin(cadastros_clientes, login, senha)):
                    usuarioLogado = login
                    logado = True
                    while(logado):
                        menuPrincipal_cliente()
                        opcaoPrincipal_cliente = int(input('Digite a opção desejada - '))
                        
                        if(opcaoPrincipal_cliente == 1):
                            'a'
                            
                        elif(opcaoPrincipal_cliente == 2):
                            buscarProdutos_cliente(produtos)
                            
                        elif(opcaoPrincipal_cliente == 3):
                            comprarProdutos(produtos, usuarioLogado, produtosComprados)
                            
                        elif(opcaoPrincipal_cliente == 4):
                            listarCompras(produtosComprados, usuarioLogado)
                            
                        elif(opcaoPrincipal_cliente == 5):
                            produto_consulta = input('Digite o produto que quer uma opnião - ')
                            resposta = consultarCHATGPT(produto_consulta)
                            print(resposta)
                            
                        elif(opcaoPrincipal_cliente == 0):
                            print(40*'=')
                            print('Deslogado com sucesso.')
                            break
                                     
            elif(opcaoCliente == 0):
                break
                    
    elif(opcaoInicial == 0):
        valor = False
        
    else:
        print(40*'=')
        print('Opção Invalida.')
        print(40*'=')
        
print(40*'=')
print('PROGRAMA FINALIZADO!!!')
print(40*'=')
from funcoes_produtos import *
from funcoes_clientes import *
from funcoes_vendedor import *
from funcoes_menus import *

cadastros_vendedor = [{'Login': 'KaueCardz', 'Senha': 'senha', 'Nome': 'Kaue', 'Sobrenome': 'Batista', 'CPF': '02030202133', 'Ano de Nascimento': 2003}]
cadastros_clientes = []
produtos = []

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
                        opcaoPrincipal = int(input('Digite a opção desejada - '))

                        if(opcaoPrincipal == 1): 
                            atualizarDados(cadastros_vendedor, usuarioLogado)
                            
                        elif(opcaoPrincipal == 2):
                            cadastrarProdutos(produtos, usuarioLogado)
                                                            
                        elif(opcaoPrincipal == 3):
                            buscarProdutos_vendedor(produtos, usuarioLogado)
                        
                        elif(opcaoPrincipal == 4):
                            removerProdutos(produtos, usuarioLogado)

                        elif(opcaoPrincipal == 5): 
                            atualizarProdutos(produtos, usuarioLogado)
                            
                        elif(opcaoPrincipal == 0): 
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
                        'a'
                
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
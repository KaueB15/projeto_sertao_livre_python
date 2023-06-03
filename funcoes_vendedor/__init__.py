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

def cadastrarUsuario_vendedor(lista):
    cadastro = {}
    verificarLogin_duplicado(lista, cadastro)
    cadastro['Senha'] = input('Digite a Senha - ')
    cadastro['Nome'] = input('Digite seu Nome - ')
    verificar_CPF(lista, cadastro)
    verificar_idade(cadastro)
    lista.append(cadastro)
    print(40*'=')
    print('Usuario cadastrado com sucesso')
    
def validarLogin(lista, login, senha):
    logado = False
    for cadastrado in lista:
        if(cadastrado['Login'] == login):
            index = lista.index(cadastrado)
            if(senha == lista[index]['Senha']):
                print(40*'=')
                print('Autenticado com sucesso.')       
                logado = True
    if(logado == False):
        logado = False
        print(40*'=')
        print('Login ou senha incorretos')
    return logado

def atualizarDados(lista, login):
    print(40*'=')
    print('O QUE DESEJA ATUALIZAR?')
    print('1 - Senha')
    print(40*'=')
    opcaoAtualizacao = int(input('Digite a opção desejada - '))
    
    if(opcaoAtualizacao == 1):
        for cadastrado in lista:
            if(cadastrado['Login'] == login):
                index = lista.index(cadastrado)
        confirmacao = False
        senhaAtual = input('Digite sua senha atual - ')
        if(senhaAtual == lista[index]['Senha']):
            print(40*'=')
            print('Senha correta.')
            print(40*'=')
            while(confirmacao != True):
                novaSenha = input('Digite sua nova senha - ')
                confirmarSenha = input('Confirme a senha - ')
                if(novaSenha == confirmarSenha):
                    lista[index]['Senha'] = novaSenha
                    print(40*'=')
                    print('Senha atualizado com sucesso.')
                    confirmacao = True
                else:
                    print(40*'=')
                    print('Confirmação incorreta.')
        else:
            print(40*'=')
            print('Senha incorreta')
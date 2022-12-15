# ENTRADAS:

cadastro_atributos = {}                                                       # Cria um dicionário vazio para atributos dos produtos
cadastro_produtos = {}                                                        # Cria um dicionário vazio para os nomes dos produtos
lista_opcoes = ["Cadastrar?", "Consultar?", "Remover?", "Fechar programa?"]   # Cria uma lista contendo as possíveis opções


def exibir_menu():

    for i, v in enumerate(lista_opcoes):                                      # Varre a lista_opcoes atribuindo em I e V, o indice e valor
        print(f"[{i}] {v}")                                                   # Imprime o menu para escolha do usuario


def cadastrar_produto():                                                      # Define a função cadastrar produto

    atributos = []                                                            # Cria uma lista vazia para os atributos de um produto
    global cadastro_atributos                                                 # Define este atributo como global
    global cadastro_produtos                                                  # Define este atributo como global
    chave = int(input("Informe o código do produto a ser cadastrado: "))      # Recebe a chave passada pelo usuário para fazer o cadastro do produto
    cadastro_produtos[chave] = input("Didite o nome do produto: ")            # Adiciona no cadastro, na posicao da chave, o nome do produto fornecido
    atributos.append(input("Didite a cor do produto: "))                      # Adiciona na lista de atributos a cor do produto
    atributos.append(int(input("Didite a quantidade do produto: ")))          # Adiciona na lista de atributos a quantidade do produto após um cast para int
    atributos.append(float(input("Digite o valor do produto: ")))             # Adiciona na lista de atributos o valor do produto após um cast para float
    cadastro_atributos[chave] = atributos                                     # Adiciona no cadastro, na posicao da chave, a lista com os atributos fornecidos
    print(f"O produto cadastrado foi: {cadastro_produtos.get(chave)}")        # Imprime a mensagem especificada mostrando o nome do produto cadastrado


def consultar_produto():                                                      # Define a função consultar produto

    if len(cadastro_produtos) == 0:                                           # verifica se o dicionário está vazio
        print("Não existem produtos cadastrados")                             # Imprime a mensagem especificada
    else:                                                                     # Executa este bloco se a codição do IF seja falsa
        listar_produtos()                                                     # Chama função para listar os produtos
        print("")                                                             # Pula uma linha para melhor visualização na execuçãor do programa
        chave = int(input("Informe o código do produto a ser consultado: "))  # Recebe a chave passada pelo usuário para fazer a consulta do produto
        if chave in cadastro_produtos:                                        # Verifica se a chave fornecida está cadastrada no dicionario de produtos
            print(f"O nome do produto é {cadastro_produtos.get(chave)}")      # Imprime a mensagem especificada mostrando o nome do produto cadastrado
            atributos = cadastro_atributos.get(chave)                         # A lista de atributos recebe a lista contida no dicionario cuja chave foi passada
            print(f"A cor do produto é {atributos[0]}")                       # Imprime a mensagem especificada mostrando a cor do produto cadastrado
            print(f"A quantidade do produto é {atributos[1]}")                # Imprime a mensagem especificada mostrando a quantidade do produto cadastrado
            print(f"O valor do produto é R$ {atributos[2]}")                  # Imprime a mensagem especificada mostrando o valor do produto cadastrado
        else:                                                                 # Caso a chave nao esteja no dicionario, serão executados esses comandos
            print("Chave não existente!")                                     # Imprime a mensagem de que a chave não existe


def remover_produto():                                                        # Define a função remover produto

    global cadastro_atributos                                                 # Define este atributo como global
    global cadastro_produtos                                                  # Define este atributo como global
    if len(cadastro_produtos) == 0:                                           # verifica se o dicionário está vazio
        print("Não existem produtos cadastrados")                             # Imprime a mensagem especificada
    else:                                                                     # Executa este bloco se a codição do IF seja falsa
        listar_produtos()                                                     # Chama função para listar os produtos
        print("")                                                             # Pula uma linha para melhor visualização na execuçãor do programa
        chave = int(input("Informe o código do produto a ser removido: "))    # Recebe a chave passada pelo usuário para fazer a remossão do produto
        if chave in cadastro_produtos:                                        # Verifica se a chave fornecida está cadastrada no dicionario de produtos
            cadastro_atributos.pop(chave)                                     # Remove do cadastro o rigistro para a chave que foi fornecida
            print(f"O produto removido foi {cadastro_produtos.pop(chave)}")   # Imprime a mensagem especificada mostrando o nome do produto removido
        else:                                                                 # Caso a chave nao esteja no dicionario, serão executados esses comandos
            print("Chave não existente!")                                     # Imprime a mensagem de que a chave não existe


def listar_produtos():                                                        # Define a função lista produtos como menu

    print(cadastro_produtos)                                                  # Imprime os produtos para facilitar a escolha do usuário


def menu_opcoes():

    print("")                                                                 # Pula uma linha para melhor visualização na execuçãor do programa
    print("O que deseja fazer?")                                              # Imprime a mensagem especificada
    exibir_menu()                                                             # Chama a função exibir_menu definida na biblioteca
    opcao = int(input("Escolha uma opção: "))                                 # Recebe a entrada do usuário após o cast para inteiro
    print("")                                                                 # Pula uma linha para melhor visualização na execuçãor do programa
    if opcao == 0:                                                            # Verifica se a opção foi a zero

        cadastrar_produto()                                                   # Chama função para cadastrar produtos

    elif opcao == 1:                                                          # Verifica se a opção foi a um

        consultar_produto()                                                   # Chama função para consultar produtos

    elif opcao == 2:                                                          # Verifica se a opção foi a dois

        remover_produto()                                                     # Chama função para remover produtos

    elif opcao == 3:                                                          # Verifica se a opção foi a tres

        print("Finalizando...")                                               # Imprime a mensagem especificada
        return                                                                # Chama função para sair do sistema

    else:                                                                     # Executa caso nenhuma opção válida tenha sido escolhida
        print("")                                                             # Pula uma linha para melhor visualização na execuçãor do programa
        print("Opção inválida, escolha outra opção")                          # Imprime a mensagem especificada

    menu_opcoes()                                                             # Chama a função que exibirá o menu novamente
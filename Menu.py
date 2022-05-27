# Aqui temos um menu com algumas funções
# Podemos inserir, remover, consultar, atualizar, imprimir a lista e sair do programa
# Logo logo trago mais implementações e melhorias, sujestões chamar no LinkedIn

import time

lista = []
escolha = 0
while escolha != 9:

    
    print("\nBem vindo ")
    print("-------------------------------------")
    print("1 - Inserir Usuario")
    print("2 - Remover Usuario")
    print("3 - Consultar Usuario")
    print("4 - Atualizar Usuario")
    print("5 - Imprimir Lista")
    print("9 - Sair")

    print("Escolha o que deseja")
    opçao = int(input())
 
    if opçao == 1:
        
        print("Vamos inserir seu usuario")
        print("Digite seu nome")
        nomel = str(input())
        lista.append(nomel)
        print("Usuario Adicionado")
        time.sleep(3)
        

    elif opçao == 2:
        print("Vamos remover seu usuario")
        print("Digite o nome do usuario a ser removido")
        nome2 = str(input())
        if nome2 in lista:
            lista.remove(nome2)
            print("Usuario Removido")
        else:
            print("Usuario não encontrado para remoção")    
        time.sleep(3)


    elif opçao == 3:
        print("Vamos consultar seu usuario")
        print("Digite o nome do Usuario para verificar se existe")
        nome3 = str(input())
        if nome3 in lista:
            print("Usuario Existente")
        else:
            print("Usuario não encontrado")
        time.sleep(3)

    elif opçao == 4:
        print("Vamos atualizar seu usuario")
        print("Digite o nome do usuario a ser alterado")
        nome4 = str(input())
        if nome4 in lista:
            lista.remove(nome4)
            print("Digite um novo nome de usuario")
            nome5 = str(input())
            lista.append(nome5)
            print("Usuario Atualizado")
            time.sleep(3)
        else:
            print("Usuario não cadastrado")
            
        time.sleep(3)

    elif opçao == 5:
        print("Vamos imprimir sua lista")
        if lista == []:
            print("Não existem usuarios nessa lista")
        else:
            print(lista)        
            print("Aqui está")
        time.sleep(3)

    elif opçao == 9:
        print("Tchauzinho")
        break
    else:
        print("Não encontrei o que vc deseja, por favor repetir ")
        time.sleep(3)
    
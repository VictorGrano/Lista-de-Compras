import os

lista = []
while True:
    print('Selecione uma opção: ')
    opc = input('[i]nserir [a]pagar [l]istar [s]air: ')
    opcao = opc.upper()
    if opcao.startswith('I'):
        valor = input('Item: ')
        lista.append(valor)
        continue
    elif opcao.startswith('A'):
        valor = input('Item para apagar: ')
        try:
            valor = int(valor)
        except:
            print('Digite um índice válido!')
            continue
        lista.pop(valor)
        continue
    elif opcao.startswith('L'):
        if lista == []:
            print('Lista vazia!')
            continue
        lista_enumerada = enumerate(lista)
        for indice, item in lista_enumerada:
            print(indice, item)
            continue
    elif opcao.startswith('S'):
        os.system('cls')
        break
    else:
        print('Digite uma opção correta!')
        continue
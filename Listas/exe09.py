'''
Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
'''
valores = (0)
print(50*'#')
while True:
    num = int(input("Insira um número: \n"))
    for c, v in enumerate(valores):
        if num < valores[v-1]:
            valores.insert(num, c)
            print(f"Valor inserido na posição {c}")
        else:
            valores.append(num)
    c = str(input("Deseja Inserir outro número? [S] para sim, [N] para não\n"))
    if c in 'Nn':
        break
print(50*'=-')
print(valores)

    #if  num not in valores:
     #   valores.append(num)
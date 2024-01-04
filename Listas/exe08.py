'''
Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''
valores = list()
print(50*'#')
while True:
    num = int(input("Insira um número: \n"))
    if  num not in valores:
        valores.append(num)
        print("Valor adicionado\n")
    else:
        print("Número já inserido\n")
    c = str(input("Deseja Inserir outro número? [S] para sim, [N] para não\n"))
    if c in 'Nn':
        break
        




'''num = int(input("Quantos números você deseja adicionar?\n"))
for cont in range(0,num):
    num1= int(input("Insira o número que você deseja ser adicionado"))
    valores.append(num1)
    if num1 in valores:
        print("valor já adicionado\n")
        valores.pop(num1)

#valores.append(int(input('Digite o valor para ser adicionado: \n')))
'''
'''
Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas.
'''
valores = list()
impar = list()
par = list()

while True:
    num = int(input("Insira um número: \n"))
    valores.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    print("Valor adicionado\n")
    c = str(input("Deseja Inserir outro número? [S] para sim, [N] para não\n"))
    if c in 'Nn':
        break
print(f"Os números totais adicionados na lista foram {valores}\n")
print(f"A lista com os valores ímpar contém {impar}\n")
print(f"A lista com os valores pares contem {par}\n")
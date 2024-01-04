'''
Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''
valores = list()

while True:
    num = int(input("Insira um número: \n"))
    valores.append(num)
    print("Valor adicionado\n")
    c = str(input("Deseja Inserir outro número? [S] para sim, [N] para não\n"))
    if c in 'Nn':
        break
valores.sort(reverse=True)
print(f"A lista tem {len(valores)} elementos\n")
if 5 in valores:
    print("O valor 5 esta na lista\n")
else:
    print("O valor 5 não esta na lista\n")
print(f"{valores}")
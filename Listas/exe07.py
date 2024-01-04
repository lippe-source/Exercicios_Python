'''
Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 
'''
valores = list()
print(50*'#')
num = int(input("Quantos números você deseja adicionar?\n"))
for cont in range(0,num):
    valores.append(int(input('Digite o valor para ser adicionado: \n')))
valores.sort()
print(f'O menor número digitado é: {valores[0]}\n')
print(f'O maior número digitado é: {valores[num-1]}\n')
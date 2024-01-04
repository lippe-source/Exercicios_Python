'''
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, 
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''
cont=0
dado = list()
pessoa = list()
w = 0

while True:
    name = str(input("Qual o nome da pessoa?\n"))
    dado.append(name)
    peso = int(input("Qual o peso da pessoa?\n"))
    dado.append(peso)
    pessoa.append(dado[:])
    dado.clear()
    cont = cont+1
    c = (input("Deseja inserir outra pessoa? [S]/[N]"))
    if c in 'Nn':
        break
for p in pessoa:
    if p[1] >= w:
        w = p[1]
print(50*'-=')
print(f"{w}")
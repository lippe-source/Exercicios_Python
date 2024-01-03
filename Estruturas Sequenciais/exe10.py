'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e
mostre:
● o produto do dobro do primeiro com metade do segundo .
● a soma do triplo do primeiro com o terceiro.
● o terceiro elevado ao cubo.

'''
int1 = int(input("Digite o primeiro número inteiro\n"))
int2 = int(input("Digite o segundo número inteiro\n"))
fl1 = float(input("Agora digite o número real\n"))
prod= (2*int1)*(int2/2)
som= (3*int1)+fl1
cub= fl1*fl1*fl1
print(f"O produto do dobro do primeiro com metade do segundo é igual: {prod:.1f}\n")
print(f"A soma do triplo do primeiro com o terceiro é igual: {som:.1f}\n")
print(f"O terceiro elevado ao cubo: {cub:.1f}\n")

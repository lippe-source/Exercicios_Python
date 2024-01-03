'''

Faça um programa que receba a idade, altura e o peso de 25 pessoas, Calcule e mostre:

A quantidade de pessoas com idade superior a 50 anos;
A média das Alturas das pessoas com idade entre 10 e 20 anos
A porcentagem das pessoas com peso inferior a 40 quilos entre todas as pessoas analisadas.
'''




print("########################################################################\n")
cont = 0
cont2 = 0
cont3 = 0
cont4 = 0
pessoas = int(input("Insira a quantidade de pessoas para o calculo\n"))
while (cont < pessoas):
    idade = int(input(f"Insira a idade da pessoa número {cont+1}\n"))
    cont = cont+1
    if idade >= 18:
        cont2 = cont2 +1
    if idade == 18:
        cont3 = cont3+1
    if idade <= 18:
        cont4 = cont4+1
print(f"O número de pessoas maiores que 18 é: {cont2}\n")
print(f"O número de pessoas com 18 anos é: {cont3}\n")
print(f"O número de pessoas menores que 18 é: {cont4}")
print("\n########################################################################")


'''
 Faça um programa que receba a idade e o peso de sete pessoas. Calcule e mostre:

A quantidade de pessoas com mais de 90 quilos;
A média das idades das sete pessoas;

'''


print("########################################################################\n")
cont = 0
cont2 = 0
cont3 = 0
cont4 = 0
cont5 = 0
pessoas = int(input("Insira a quantidade de pessoas para o calculo\n"))
while (cont < pessoas):
    idade = int(input(f"Insira a idade da pessoa número {cont+1}\n"))
    altura = float(input("Agora ensira a altura\n"))
    peso = int(input("por ultimo, insira o peso\n"))
    cont = cont+1
    if idade >= 50:
        cont2 = cont2 +1
    if idade >= 10 and idade <= 20:
        cont5 = cont5+1
        cont3 = cont3+altura
    if peso < 40:
        cont4 = cont4+1
media = cont3/cont5
perc = (100*cont4)/pessoas
print(f"O número de pessoas maiores que 50 é: {cont2}\n")
print(f"A media da altura de pessoas com idade entre 10 e 20 é: {media:.2f}\n")
print(f"A porcentagem das pessoas com peso inferior a 40 quilos entre todas as pessoas analisadas é: {perc:.2f}% porcento")
print("\n########################################################################")

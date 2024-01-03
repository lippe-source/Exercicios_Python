'''
Faça um Programa que pergunta quanto você ganha por hora e o número de
horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês
'''
horas = int(input("Digite o numero de horas trabalhadas\n"))
valor = float(input("Digite o valor das horas\n"))
total = horas*valor
print("O salário final é de:", total)

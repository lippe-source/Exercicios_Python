'''
Faça um Programa que pergunte quanto você ganha por hora e o número de
horas trabalhadas no mês. Calcule e mostre o total do seu salário no mês
específico, sabendo-se que são descontados 11% para o Imposto de Renda, 8%
para o INSS e 5% para o sindicato, faça um programa que nos dê:
● salário bruto.
● quanto pagou ao INSS.
● quanto pagou ao sindicato.
● o salário líquido.
calcule os descontos e o salário líquido, conforme tabela abaixo:
● Salário Bruto: R$
● IR (11%): R$
● INSS (8%): R$
● Sindicato (5%): R$
● Salário Líquido: R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
'''
hrst = int(input("Digite o numero de horas trabalhadas no mês\n"))
valor = float(input("Digite o valor que você ganha por hora\n"))
saltotal = hrst*valor
ir = saltotal*0.11
inss = saltotal*0.08
sind = saltotal*0.05
salliq = saltotal-ir-inss-sind
print(f"O valor do salário bruto é de: R${saltotal:.2f} e valor do salário líquido é de: R${salliq:.2f}")
print("Foram feitos os seguintes descontos:")
print(f"IMPOSTO DE RENDA: -R${ir:.2f}")
print(f"SINDICATO: -R${sind:.2f}")
print(f"INSS: -R${inss:.2f}")

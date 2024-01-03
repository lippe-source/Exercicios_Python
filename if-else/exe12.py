'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos
são do imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o
Sindicato e que o FGTS corresponde a 11% do salário bruto, mas não é descontado (é a
empresa que deposita.) O salário líquido corresponde ao salário bruto menos os descontos O
programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no
mês.
● Desconto do IR;
● Salário Bruto ate RS900,00 (inclusive) – Isento;
● Salário Bruto de RS 1500, 00 (inclusive) – desconto de 5%;
● Salario bruto até RS 2500,00 (Inclusive) – desconto de 10%;
● Salário bruto acima de 2500 – Desconto de 20%.
Imprima na tela as informações, dispostas conforme o exemplo abaixo, no exemplo valor da
hora é 5 e a quantidade de horas é 220.
plaintext
Salário bruto (5 * 220) : RS 1100,00
( - ) IR (5%) : RS 55,00
( - ) INSS ( 10% ) : RS 110,00
FGTS ( 11%) : RS 121,00
Total de descontos : RS 165,00
Salário Líquido : RS 935,00

'''





print("---------------------------------------------------------\n")
vl = float(input("Qual o valor da hora trabalhada\n"))
hrs = int(input("Quantas horas foram trabalhadas\n"))
slb = vl*hrs
slsind = slb*0.03
slfgts = slb*0.11
if slb < 900 :
    sll = slb-slsind-slfgts
    total =slsind+slfgts
    print (f"Salário bruto ({vl:,.2f}*{hrs}): R${slb:,.2f}\n(-) IR (ISENTO): R$00,00\n(-) SINDICATO (3%): R${slsind:,.2f}\nFGTS (11%): R${slfgts:,.2f}\nTotal de descontos: R${total:,.2f}\nSalário líquido: R${sll:,.2f}")
elif slb > 900 and slb < 1500:
    slir = slb*0.05
    sll = slb-slsind-slfgts-slir
    total =slsind+slfgts+slir
    print (f"Salário bruto ({vl:,.2f}*{hrs}): R${slb:,.2f}\n(-) IR (5%): R${slir:,.2f}\n(-) SINDICATO (3%): R${slsind:,.2f}\nFGTS (11%): R${slfgts:,.2f}\nTotal de descontos: R${total:,.2f}\nSalário líquido: R${sll:,.2f}")
elif slb > 1500 and slb < 2500:
    slir = slb*0.10
    sll = slb-slsind-slfgts-slir
    total =slsind+slfgts+slir
    print (f"Salário bruto ({vl:,.2f}*{hrs}): R${slb:,.2f}\n(-) IR (10%): R${slir:,.2f}\n(-) SINDICATO (3%): R${slsind:,.2f}\nFGTS (11%): R${slfgts:,.2f}\nTotal de descontos: R${total:,.2f}\nSalário líquido: R${sll:,.2f}")
else:
    slir = slb*0.20
    sll = slb-slsind-slfgts-slir
    total =slsind+slfgts+slir
    print (f"Salário bruto ({vl:,.2f}*{hrs}): R${slb:,.2f}\n(-) IR (20%): R${slir:,.2f}\n(-) SINDICATO (3%): R${slsind:,.2f}\nFGTS (11%): R${slfgts:,.2f}\nTotal de descontos: R${total:,.2f}\nSalário líquido: R${sll:,.2f}\n")
print("----------------- Fim do programa -----------------------")

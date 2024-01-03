'''

As organizações CSM resolveram dar um aumento de salário aos seus colaboradores e lhe
contrataram para desenvolver o programa que calculará os reajustes.
● Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
seguinte critério, baseado no salário atual;
● Salários até RS 280,00 (incluindo): aumento de 20%;
● Salários entre RS 280,00 e RS 700,00: aumento de 15%;
● Salários entre RS 700,00 e RS 1500,00: aumento de 10%;
● Salários de RS 1500,00 em diante: aumento de 5% Após o aumento ser realizado;
Informe na tela os seguintes dados;
● O salário antes do reajuste;
● O percentual de aumento aplicado;
● O valor do aumento;
● O novo salário, após o aumento.

'''



print("---------------------------------------------------------\n")
slb = float(input("Qual o salário do colaborador\n"))
if slb <= 280:
    slperc = slb *0.20
    slbt = slb+slperc
    print (f"O salário inicial era de: R${slb:.2f}, após o reajuste de 20%, foi adicionado: R${slperc:.2f}, e o valor final do salário foi de: R${slbt:.2f}")
elif slb > 280 and slb < 700:
    slperc = slb *0.15
    slbt = slb+slperc
    print (f"O salário inicial era de: R${slb:.2f}, após o reajuste de 15%, foi adicionado: R${slperc:.2f}, e o valor final do salário foi de: R${slbt:.2f}")
elif slb > 700 and slb < 1500:
    slperc = slb *0.10
    slbt = slb+slperc
    print (f"O salário inicial era de: R${slb:.2f}, após o reajuste de 10%, foi adicionado: R${slperc:.2f}, e o valor final do salário foi de: R${slbt:.2f}")
else:
    slperc = slb *0.05
    slbt = slb+slperc
    print (f"O salário inicial era de: R${slb:.2f}, após o reajuste de 5%, foi adicionado: R${slperc:.2f}, e o valor final do salário foi de: R${slbt:.2f}\n")
print("----------------- Fim do programa -----------------------")


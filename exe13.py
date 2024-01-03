'''
. João Papo-de-Pescador, homem de bem, comprou um microcomputador para
controlar o rendimento diário de seu trabalho. Toda vez que ele trouxer um peso de
peixes maior que o previsto pelo regulamento de pesca do estado de São Paulo (50
quilos) deverá pagar uma multa de R$ 4,00 por quilo excedente. João precisa que
você faça um programa que leia a variável peso (peso de peixes) e calcule o
excesso. Gravar na variável excesso a quantidade de quilos além do limite e na
multa variável o valor da multa que João deverá pagar. Imprima os dados do
programa com as mensagens apropriadas.
'''
peso = float(input("Digite o peso do peixe em quilos\n"))
if peso > 50:
        exe = peso - 50
        mult = exe*4
        print(f"O peixe teve um excesso de {exe:.1f} quilos e a multa será de: R${mult:.2f}\n")

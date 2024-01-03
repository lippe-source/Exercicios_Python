'''
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-
Domingo , 2- Segunda, etc.) se digitar outro valor deve aparecer “valor inválido)
'''
cont = int(input("Digite o número correspondente ao dia da semana\n"))
if cont > 31:
    print("Dia da semana é inválido")
elif cont == 1 or cont%7-1 == 0:
    print("O dia da semana é domingo")
elif cont == 2 or cont%7-2 == 0:
    print("O dia da semana é segunda")
elif cont == 3 or cont%7-3 == 0:
    print("O dia da semana é terça")
elif cont == 4 or cont%7-4 == 0:
    print("O dia da semana é quarta")
elif cont == 5 or cont%7-5 == 0:
    print("O dia da semana é quinta")
elif cont == 6 or cont%7-6 == 0:
    print("O dia da semana é sexta")
elif cont == 7 or cont%7 == 0:
    print("O dia da semana é sábado")


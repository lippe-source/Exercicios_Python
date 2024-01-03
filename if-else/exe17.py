'''
- Faça um Programa que peça um número correspondente a um determinado ano e em
seguida informe se este ano e ou não bissexto.

'''



ano = int (input("Digite o ano\n"))
if ano%4 != 0 or ano%100 == 0:
    print("O ano digitado não é bissexto")
    quit()
else:
    print("O ano é bissexto")
    quit()

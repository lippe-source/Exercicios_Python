'''
Façaumprogramaqueleiatrêsnúmerosemostreomaiordeles
'''


n1 = float(input("Insira o primeiro número\n"))
n2 = float(input("Insira o segundo número\n"))
n3 = float(input("Insira o terceiro número\n"))

if n1 > n2 and n1 > n3:
        print("O primeiro número é o maior\n")
elif n2 > n1 and n2 > n3:
        print("O segundo número é o maior\n")
else:
        print("O terceiro número é o maior")

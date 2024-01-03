'''
 Faça um programa que calcule as raízes de uma equação do segundo grau, na forma
ax2 + bx + c.
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário
nas seguintes situações:
● Se o usuário informar o valor de A igual a zero. a equação não e do segundo grau e o
programa não deve fazer
pedir os demais valores, sendo encerrado;
● Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao usuário
e encerre o programa;
● Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe ao
usuário;
● Se o delta for positivo, a equação possui duas raízes reais; informe-as ao usuário;

'''




a = float(input("Digite o valor de 'A'\n"))
b = float(input("Digite o valor de 'B'\n"))
c2 = float(input("Digite o valor de 'C'\n"))

if a == 0:
    print("A equação não é do segundo grau")
    quit()
delta = (b*b)-4*a*c2
if delta < 0:
    print("ele não possui raizes reais")
    quit()
if delta == 0:
    x = (-b)/2*a
    print(f"A equação só possui uma raiz, o valor dela é {x}")
else:
    print(f"{delta}")
    x1 = (-b+delta ** 0.5)/2*a
    x2 = (-b-delta ** 0.5)/2*a
print(f"O valor da primeira raiz é: {x1}\nO valor da segunda raiz é: {x2}")

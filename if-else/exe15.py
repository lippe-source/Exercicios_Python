'''
Faça um programa que peça os 3 lados de um triângulo. O programa deverá informar se os
valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é:
equilátero, isósceles ou escaleno.
Dicas:
● Três lados formam um triangulo quando a soma de quaisquer dos dois lados é menor
que o terceiro.
● Triângulo Equilátero: três lados iguais;
● Triângulo isósceles: quaisquer dois lados iguais;
● Triângulo Escaleno: três lados diferentes;
a = int(input("primeiro lado"))
b = int(input("segundo lado"))
c = int(input ("terceiro lado"))

'''



l1 = int(input("Digite a primeira medida\n"))
l2 = int(input("Digite a segunda medida\n"))
l3 = int(input("Digite a terceira medida\n"))
if (l1+l2) <= l3 or (l1+l3) <= l2 or (l2+l3) <= l1:
    print("Devido as medidas, isso não corresponde a umm triangulo")
    quit()
elif l1==l2 and l2==l3:
    print("Este é um triangulo equilatero")
elif l1==l2 or l1==l3 or l2==l3:
    print("Este triangulo é isosceles")
else:
    print("Este triangulo é escaleno")

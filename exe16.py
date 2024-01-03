'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho
em metros quadrados da área a ser pintada. Considere que a cobertura de tinta é
de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18
litros, que custa R$ 80,00 ou em galões de 3,6 litros, que custa R$ 25,00 .
● Informe ao usuário as quantidades de tinta a serem compradas e os preços
relevantes em 3 situações:
● comprar apenas latas de 18 litros;
● comprar apenas galões de 3,6 litros;
● Ajuste latas e galões, de forma que o preço seja o menor. Adicione 10% de
folga e sempre arredonde os valores para cima, isto é, considere latas
cheias.
'''
mtrs = float(input("Digite os metros quadrados do ambiente\n"))
litros = mtrs/6
totlat = litros/18
totgal = litros/3.6
totgalarre = round(totgal+0.5)
totalarredondado = round(totlat+0.5)
if totlat < 1:
    if totgal < 2:
        print(f"Será necessário um galão e o total ficará R$25,00")
    else:
        print(f"Serão necessários {totgalarre} galões e o total ficará R${totgalarre*25}")
else:
    print(f"Serão necessárias: {totalarredondado} de latas e o custo ficará: R${totalarredondado*80}")
    print(f"Ou Serão necessárias: {totgalarre} de galões e o custo ficará: R${totgalarre*25}")


'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho
em metros quadrados da área a ser pintada. Considere que a cobertura de tinta é
de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18
litros, que custa R$ 80,00. Informe ao usuário as quantidades de latas de tinta que
serão compradas e o preço total.
'''
mtrs = float(input("Digite os metros quadrados do ambiente\n"))
litros = mtrs/3
totlat = litros/18
totalarredondado = round(totlat+0.5)
if totlat < 1:
    print(f"Será necessária uma lata e o custo ficará: R$80,00")
else:
    print(f"Serão necessárias: {totalarredondado} de latas e o custo ficará: R${totalarredondado*80}")

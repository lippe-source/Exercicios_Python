'''
Declare uma lista de 16 posições e troque os 8 primeiros valores pelos 8 últimos e vice-e-versa.
Escreva ao final o vetor obtido.
'''
print("=-"*30)
valores = list()
for x in range (0, 16):
    val = int(input("Insira um valor á lista "))
    valores.append(val)
print(valores)
for pos in range (0, 16):
    valores.insert(pos, valores[15])
    valores.pop(16)
print("A lista com valores invertidos é igual a:")
print(valores)
print("=-"*30)
print(f'{"FIM DO PROGRAMA":^40}')
'''
Declare uma lista de 40 posições e atribua valor 0 para todos os elementos que possuírem valores negativos.
'''
print("=-"*45)
valores = list()
for x in range (0, 40):
    val = int(input("Insira um valor á lista "))
    if val < 0:
        valores.append(0)
    else:
        valores.append(val)
print("A lista final é:")
print(valores)
print("=-"*45)
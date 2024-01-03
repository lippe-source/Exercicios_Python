'''
Faça ump rograma que leia três números mostre-os em ordem decrescente.'''



print("---------------------------------------------------------")
p1 = float(input("Insira o primeiro número\n"))
p2 = float(input("O segundo número\n"))
p3 = float(input("Agora terceiro número\n"))

if p1 > p2 and p1 > p3:
         maior = p1
elif p2 > p1 and p2 > p3:
         maior = p2
else:
         maior = p3
if p1 < p2 and p1 < p3:
         menor = p1
elif p2 < p1 and p2 < p3:
         menor = p2
else:
         menor = p3
if p1 < maior and p1 > menor:
         meio = p1
elif p2 < maior and p2 > menor:
         meio = p2
else:
         meio = p3
print(f"A ordem decrescente dos número é:{maior},{meio},{menor}")
print("----------------- Fim do programa -----------------------")

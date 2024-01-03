'''
Façaumprogramaquepergunteopreçodetrêsprodutoseinformequalprodutovocêdevecomprar,sabendoqueadecisãoésempreomaisbarato.
'''


print("---------------------------------------------------------")
p1 = float(input("Insira o preço do primeiro produto\n"))
p2 = float(input("O preço do segundo produto\n"))
p3 = float(input("Agora o preço do terceiro produto\n"))

if p1 < p2 and p1 < p3:
        print("O primeiro produto é o mais indicado\n")
elif p2 < p1 and p2 < p3:
        print("O segundo produto é o mais indicado\n")
else:
        print("O terceiro produto é o mais indicado\n")
print("----------------- Fim do programa -----------------------")

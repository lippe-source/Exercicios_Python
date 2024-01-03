'''
Faça um programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou
V-vespertino ou N-noturno. Imprima a mensagem “Bom dia!” ou “Boa Noite” ou “Valor inválido”,
conforme o caso
'''
print("---------------------------------------------------------")
t1 = (input("Qual é o seu turno? Digite 'M' para manhã, 'V' para vespertino ou 'N' para noturno\n"))
if t1 == 'M' or t1 == 'm':
         print("Bom dia")
elif t1 == 'V' or t1 == 'v':
         print("Boa tarde")
elif t1 == 'N' or 'n':
         print("Boa noite")
else:
         print("Valor invalido")
print("----------------- Fim do programa -----------------------")


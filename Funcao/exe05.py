'''
Escreva um procedimento que recebe as 3 notas de um aluno por parâmetro e uma letra. Se a letra for A o procedimento calcula a média aritmética das notas do aluno, se for P, a sua média ponderada (pesos: 5, 3 e 2) e se for H, a sua média harmônica. A média calculada também deve retornar por parâmetro.
'''

def fun(n1, n2, n3, l):
if l == 'a' or 'A':
media = (n1+n2+n3)/3
return media
elif l == 'p' or 'P':
mediap = (n1+n2+n3)/5+3+2
return mediap
elif l == 'h' or 'H':
mediah = 3/(1/n1 + 1/n2 + 1/n3)
return mediah
else:
print("Opção inválida")
quit()
print("#######################################################################\n")
nota1 = float(input("Insira a primeira nota\n"))
nota2 = float(input("Insira a segunda nota\n"))
nota3 = float(input("Insira a terceira nota\n"))
calc = input("Agora insira a opção para fazer o cálculo da média desejado\n[A]
Para a média aritimética\n[P] Para a média ponderada\n[H] Para a média
harmônica\n")
print("A média do aluno é:", fun(nota1, nota2, nota3, calc))
print("\n########################################################")




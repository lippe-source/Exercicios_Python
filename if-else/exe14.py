'''
– Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao
longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela
abaixo:
plaintext
Média de aproveitamento Conceito
Entre 9.0 e 10.0 A
Entre 7.5 e 9.0 B
Entre 6.0 e 7.5 C
Entre 4.0 e 6.0 D
Entre 4.0 e zero E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem
“APROVADO” se o conceito for A, B ou C “REPROVADO” se o conceito for D ou E.
'''



nom = (input("Insira o nome do aluno\n"))
n1 = float(input("Insira a primeira nota do aluno\n"))
if n1 > 10:
    print("Nota inválida.")
    quit()
n2 = float(input("Insira a segunda nota do aluno\n"))
if n2 > 10:
    print("Nota inválida.")
    quit()
media = (n1+n2)/2
conceito = 'd'
if media <= 4:
    conceito = 'E'
    print(f"O aluno {nom} teve uma média de {media} e um conceito E. {nom} esta reprovado.")
elif media >= 4 and media <= 6:
    conceito = 'D'
    print(f"O aluno {nom} teve uma média de {media} e um conceito D. {nom} esta reprovado.")
elif media >= 6 and media <= 7.5:
    conceito = 'C'
    print(f"O aluno {nom} teve uma média de {media} e um conceito C. {nom} esta reprovado.")
elif media >= 7.5 and media <= 9:
    conceito = 'B'
    print(f"O aluno {nom} teve uma média de {media} e um conceito B. {nom} esta aprovado.")
elif media >= 9 and media <= 10:
    conceito = 'A'
    print(f"O aluno {nom} teve uma média de {media} e um conceito A. {nom} esta aprovado.")

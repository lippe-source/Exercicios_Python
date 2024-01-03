'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo
que calcule seu peso ideal, utilizando as seguintes fórmulas:
● Para homens: (72,7*h) - 58
● Para mulheres: (62,1*h) - 44,7
'''
alt = float(input("Digite a altura da pessoa em metros\n"))
sexo = int(input("insira o sexo da pessoa: '1' para feminino, ou '2' para masculino\n"))
if sexo == 2:
        peso = (72.7*alt)-58
        print(f"O peso ideal é igual: {peso:.1f}\n")
else:
        peso = (62,1*alt)-44.7
        print(f"O peso ideal é igual: {peso:.1f}\n")

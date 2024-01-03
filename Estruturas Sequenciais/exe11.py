'''
 Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo
que calcula seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
'''
alt = float(input("Digite a altura da pessoa em metros\n"))
peso = (72.7*alt)-58
print(f"O peso ideal é igual: {peso:.1f}\n")

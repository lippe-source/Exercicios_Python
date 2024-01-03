'''
 Faça um Programa que parte a temperatura em graus Farenheit, transforma e
mostra a temperatura em graus Celsius. C=(5*(F-32)/9).
'''
faren = int(input("Digite a temperatura em fahrenheit\n"))
c=(5*(faren-32)/9)
print(f"A temperatura em Celcius é de: {c:.1f}")

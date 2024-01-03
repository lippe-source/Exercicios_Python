'''
Faça uma função que recebe um valor inteiro e verifica se o valor é par ou ímpar. A função deve retornar uma string com "par" ou "impar"
'''



print("########################################################\n")
def funcao(num):
    if num % 2 == 0:
        return('O número é par')
    else:
        return('O número é ímpar')
x = float(input("Insira o número para a verificação\n"))
print(funcao(x))
print("\n########################################################\n")

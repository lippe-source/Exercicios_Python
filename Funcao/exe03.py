'''
Faça uma função que recebe um valor inteiro e verifica se o valor é positivo ou negativo. A função deve voltar uma string escrito "positivo" ou "negativo“
'''


print("########################################################\n")
def funcao(num):
    if num > 0:
        return('O número é positivo')
    else:
        return('O número é negativo')
x = float(input("Insira o número para a verificação\n"))
print(funcao(x))
print("########################################################\n")

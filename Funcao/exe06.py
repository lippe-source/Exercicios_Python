'''
Faça um procedimento que recebe, por parâmetro, um valor N e calcula e escreve a tabuada de 1 até N.
Mostre a tabuada na forma:
1 x N = N
2 x N = 2N ...
​ N x N = N2 ​
'''



print("#######################################################################\n")
mult = 0
def tab(v, n):
for x in range (1, n+1, 1):
mult = v*x
print(f"{v}x{x} = {mult}")
num1 = int(input("Insira o número que você deseja ver a tabuada\n"))
num2 = int(input(f"Você deseja ver a tabuada de {num1} multiplicado até qual
número?\n"))
tab(num1, num2)
print("\n#######################################################################")
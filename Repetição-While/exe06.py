'''
3) Uma empresa precisa de um programa que realiza o cadastro de seus produtos, 
com os seguintes valores: nome, preço, quantidade.
A cada iteração deve perguntar se o usuário deseja continuar, a resposta for igual a 'n', 
o programa encerrará a execução. No final, deverá ser apresentado o valor total do estoque 
e a quantidade de produtos cadastrados.
'''

print(50*'#')
x = True
precototal = 0
quantotal = 0
while True:
    nome = input("Qual o nome do produto?\n")
    preco = float(input("Valor do produto?\n"))
    precototal = precototal+preco
    quant = int(input("Qual a quantidade do produto?\n"))
    quantotal = quantotal+quant
    x = input("Deseja continuar?\n")
    if x == 'n':
        break
print(f"O preço total dos produtos é de {preco:.2} e a quantidade total é de {quantotal}")
                  

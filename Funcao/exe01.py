'''
Faça uma função que recebe por parâmetro o raio de uma esfera e calcula o seu volume (v = 4/3 * Pi * R^3) .
'''




def volume(raio):
    v = 4/3*(3.14*raio*raio*raio)
    return v
print("########################################################\n")
x = float(input("Insira o raio da esfera\n"))
print(volume(x))

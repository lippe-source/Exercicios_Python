'''
Faça uma função que recebe a idade de uma pessoa em anos, meses e dias e retorna essa idade expressa em dias.
'''
def dias(anos):
    meses = 0
    dias = 0
    meses = anos*12
    dias = meses*30
    return dias
print("########################################################\n")
x = int(input("Insira a idade em anos\n"))
print("O resultado convertidade é:", dias(x), "dias")
print("\n########################################################\n")

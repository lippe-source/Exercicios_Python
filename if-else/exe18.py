'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas
são:
● "Telefonou para a vítima?"
● "Esteve no local do crime?"
● "Mora perto da vítima?"
● "Devia para a vítima?"
● "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se
a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre
3 e 4 como "Cúmplice" e 5 como “Assassino“. Caso contrário, ele será classificado como
"Inocente“.


'''



p1 = (input("Telefonou para a vítima\n"))
cont = 0
if p1 == 'sim' or p1 == 'Sim':
    cont = cont +1
p2 = (input("Esteve no local do crime?\n"))
if p2 == 'sim' or p2 == 'Sim':
    cont = cont +1
p3 = (input("Mora perto da vítima?\n"))
if p2 == 'sim' or p3 == 'Sim':
    cont = cont +1
p4 = (input("Devia para a vítima?\n"))
if p4 == 'sim' or p4 == 'Sim':
    cont = cont +1
p5 = (input("Já trabalhou com a vítima?\n"))
if p5 == 'sim' or p5 == 'Sim':
    cont = cont +1
if cont == 2:
    print("A pessoa é suspeita")
elif cont == 3 or cont == 4:
    print("A pessoa é cúmplice")
elif cont == 5:
    print("A pessoa é o assassino")
else:
    print("A pessoa é inocente")

'''
Faça um Quiz lógico de perguntas e respostas. No final mostre a pontuação total do participante.
'''
print("########################################################################\n")
print("                        Q U I Z  L Ó G I C O                            \n")
print("########################################################################\n")
print("\n")
print("Bem vindo ao quiz lógico em Python, aqui você testa os seus conhecimentos\nem 3 categorias diferentes.\n")
print("\n")
print("Escolha a categoria das perguntas do Quiz\n")
cont = 0
cat = int(input("1 - Primeira categoria: Conhecimentos Gerais\n2 - Primeira categoria: Fatos Históricos\n3 - Primeira categoria: Geografia\n\n\n0 - Você também pode finalizar o Quiz digitando '0' a qualquer momento ou digitar '9' para ver o gabarito\n\n\nDigite o número correspondente a categoria desejada:\n"))
if cat == 0:
    quit()
if cat == 1:
    print("\nCATEGORIA ESCOLHIDA: FATOS GERAIS. BOA SORTE!\n")
    print("\nPERGUNTA 1 - Normalmente, quantos litros de sangue uma pessoa tem? Em média, quantos são retirados numa doação de sangue?\n")
    cg1 = int(input("1 - Tem entre 2 a 4 litros. São retirados 450 mililitros\n2 - Tem entre 4 a 6 litros. São retirados 450 mililitros\n3 - Tem 10 litros. São retirados 2 litros\n4 - Tem 7 litros. São retirados 1,5 litros\n5 - Tem 0,5 litros. São retirados 0,5 litros\n"))
    if cg1 == 2:
        cont = cont + 1
    if cg1 == 0:
        quit()
    print("\nPERGUNTA 2 - As pessoas de qual tipo sanguíneo são consideradas doadores universais?\n")
    cg2 = int(input("1 - Tipo A\n2 - Tipo B\n3 - Tipo O\n4 - Tipo AB\n5 - Tipo ABO\n"))
    if cg2 == 3:
        cont = cont+1
    if cg2 == 0:
        quit()
    print("\nPERGUNTA 3 - Qual a altura da rede de vôlei nos jogos masculino e feminino?\n")
    cg3 = int(input("1 - 2,4 para ambos\n2 - 2,5 m e 2,0 m\n3 - 1,8 m e 1,5 m\n4 - 2,45 m e 2,15 m\n5 - 2,43 m e 2,24 m\n"))
    if cg3 == 4:
        cont = cont+1
    if cg3 == 0:
        quit()
    print("\nPERGUNTA 4 - Qual o livro mais vendido no mundo a seguir à Bíblia?\n")
    cg4 = int(input("1 - O Senhor dos Anéis\n2 - Dom Quixote\n3 - O Pequeno Príncipe\n4 - Ela, a Feiticeira\n5 - Um Conto de Duas Cidades\n"))
    if cg4 == 2:
        cont = cont+1
    if cg4 == 0:
        quit()
    print("\nPERGUNTA 5 - Quantas casas decimais tem o número pi?\n")
    cg5 = int(input("1 - Duas\n2 - Centenas\n3 - Infinitas\n4 - Vinte\n5 - Milhares\n"))
    if cg5 == 3:
        cont = cont+1
    if cg5 == 0:
        quit()
    print(f"A sua pontuação do Quiz de conhecimentos gerais foi de {cont} respostas corretas\n")
    if cont == 5 or cont == 4:
        print("Parabéns!Òtima pontuação!")
if cat == 2:
    print("\nCATEGORIA ESCOLHIDA: HISTÓRIA. BOA SORTE!\n")
    print("\nPERGUNTA 1 - Quais destes acontecimentos completa 10 anos em 2022 e em 2023?\n")
    fh1 = int(input("1 - Primavera árabe e Atentados de 11 de setembro\n2 - Massacre do Carandiru e RIO+20\n3 - Massacre do Carandiru e Impeachment de Fernando Collor\n4 - RIO+20 e eleição do Papa Francisco\n5 - Fim da Guerra no Golfo e Coroação de Dom Pedro II no Brasil\n"))
    if fh1 == 4:
        cont = cont + 1
    if fh1 == 0:
        quit()
    print("\nPERGUNTA 2 - Quantos anos a Rainha Elizabeth II tinha quando assumiu o trono e durante quantos anos governou?“\n")
    fh2 = int(input("1 -  21 e 96 anos\n2 - 25 e 75 anos\n3 - 26 e 95 anos\n4 - 20 e 75 anos\n5 - 25 e 70 anos\n"))
    if fh2 == 5:
        cont = cont+1
    if fh2 == 0:
        quit()
    print("\nPERGUNTA 3 - Quanto tempo durou a monarquia no Brasil?\n")
    cg3 = int(input("1 - 65 anos\n2 - 75 anos\n3 - 67 anos\n4 - 37 anos\n5 - 97 anos\n"))
    if fh3 == 3:
        cont = cont+1
    if fh3 == 0:
        quit()
    print("\nPERGUNTA 4 - Na mitologia grega, Ares é considerado o deus da:\n")
    cg4 = int(input("1 - Morte\n2 - Guerra\n3 - Agricultura\n4 - Mar\n5 - Conquista\n"))
    if fh4 == 2:
        cont = cont+1
    if fh4 == 0:
        quit()
    print("\nPERGUNTA 5 - Nome de nossa terra atribuído por algumas tribos indígenas, no período anterior à chegada dos portugueses ao Brasil:\n")
    cg5 = int(input("1 - Terra do Pau Brasil\n2 - Terra dos Papagaios\n3 - Pindorama\n4 - Terra de Santa Cruz\n5 - Terra de Vera Cruz\n"))
    if fh5 == 3:
        cont = cont+1
    if fh5 == 0:
        quit()
    print(f"A sua pontuação do Quiz de História foi de {cont} respostas corretas\n")
    if cont == 5 or cont == 4:
        print("Parabéns!Òtima pontuação!")
if cat == 3:
    print("\nCATEGORIA ESCOLHIDA: GEOGRAFIA. BOA SORTE!\n")
    print("\nPERGUNTA 1 - Quais o menor e o maior país do mundo?\n")
    geo1 = int(input("1 - Vaticano e Rússia\n2 - Nauru e China\n3 - Mônaco e Canadá\n4 - Malta e Estados Unidos\n5 - São Marino e Índia\n"))
    if geo1 == 1:
        cont = cont + 1
    if geo1 == 0:
        quit()
    print("\nPERGUNTA 2 - Quais os países que têm a maior e a menor expectativa de vida do mundo?\n")
    geo2 = int(input("1 -  Japão e Serra Leoa\n2 - Austrália e Afeganistãos\n3 - Itália e Chade\n4 - Brasil e Congo\n5 - Estados Unidos e Angola\n"))
    if geo2 == 1:
        cont = cont+1
    if geo2 == 0:
        quit()
    print("\nPERGUNTA 3 - Qual a montanha mais alta do Brasil?\n")
    geo3 = int(input("1 - Pico da Neblina\n2 - Pico Paraná\n3 - Monte Roraima\n4 - Pico Maior de Friburgo\n5 - Pico da Bandeira\n"))
    if geo3 == 1:
        cont = cont+1
    if geo3 == 0:
        quit()
    print("\nPERGUNTA 4 - Qual destes países é transcontinental?\n")
    geo4 = int(input("1 - Rússia\n2 - Filipinas\n3 - Marrocos\n4 - Groelândia\n5 - Tanzânia\n"))
    if geo4 == 1:
        cont = cont+1
    if geo4 == 0:
        quit()
    print("\nPERGUNTA 5 - Em que estado australiano fica situada a cidade de Sydney?\n")
    geo5 = int(input("1 - Nova Gales do Sul\n2 - Victoria\n3 - Tasmânia\n4 - Queensland\n5 - Norfolk\n"))
    if geo5 == 1:
        cont = cont+1
    if geo5 == 0:
        quit()
    print(f"A sua pontuação do Quiz de Geografia foi de {cont} respostas corretas\n")
    if cont == 5 or cont == 4:
        print("Parabéns!Òtima pontuação!")
if cat == 9:
    print("\nGABARITO\n")
    print("\nGABARITO FATOS GERAIS\n")
    print("Pergunta 1 - 2\nPergunta 2 - 3\nPergunta 3 - 4\nPergunta 4 - 2\nPergunta 5 - 3\n")
    print("\nGABARITO HISTÓRIA\n")
    print("Pergunta 1 - 4\nPergunta 2 - 5\nPergunta 3 - 3\nPergunta 4 - 2\nPergunta 5 - 3\n")
    print("\nGABARITO GEOGRAFIA\n")
    print("Pergunta 1 - 1\nPergunta 2 - 1\nPergunta 3 - 1\nPergunta 4 - 1\nPergunta 5 - 1\n")



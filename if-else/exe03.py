'''
Façaumprogramaqueverifiqueseumaletradigitadaé“F”ou“M”.Conformealetraescrever:F–Feminino,M-Masculino,Sexoinválido.
'''


sexo = (input("insira o sexo da pessoa: 'f' para feminino, ou 'm' para masculino\n"))
if sexo == 'f':
        print("A pessoa é do sexo feminino\n")
elif sexo =='m':
        print("A pessoa é do sexo masculino\n")
else:
        print("sexo inválido\n")

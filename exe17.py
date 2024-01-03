'''
 Faça um programa que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo
aproximado de download do arquivo usando este link (em minutos).
'''
mbs = float(input("Digite tamanho do arquivo\n"))
vel = float(input("insira a velocidade da internet (Mbps)"))
seg = mbs/vel
segr = round (seg+0.5)
minu = (segr/60)
minur = round (minu+0.5)
hora = (minu/60)
horar = round (hora+0.5)
print("segundo, minuto, hora", segr, minur, horar)
if horar == 0 & minur == 0:
    print(f"{segr}segundos para a conclusão do download ")
elif horar == 0 & minur > 0:
    print(f"{minur}minutos e {segr} segundos para a conclusão do download ")
elif horar >= 1:
    print(f"{horar}Horas e {minur} minutos e {segr} segundos para a conclusão do download ")

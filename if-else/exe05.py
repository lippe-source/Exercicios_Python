'''
Façaumprogramaparaaleituradeduasnotasparciaisdeumaluno.●Amensagem“Aprovado”,seamédiaalcançadaformaiorouigualasete;●Amensagem“AprovadocomDistinção”,seamédiaforigualadez;●Amensagem“Reprovado”seamédiaformenordedoquesete;
'''

n1 = float(input("Insira a primeira nota\n"))
n2 = float(input("Insira a segunda nota\n"))
m = (n1+n2)/2

if m >= 7 and m<10:
        print("Aluno aprovado\n")
elif m == 10:
        print("Aluno aprovado com Distinção\n")
else:
        print("Alino reprovado")

'''
Uma companhia de teatro deseja dar uma série de espetáculos. Fatos:

A direção calcula que praticando o preço de R$5,00 serão vendidos 120 ingressos
As despesas são fixas em R$ 200,00.
Ao diminuir R$ 0,50 o preço dos ingressos espera-se que as vendas aumentem em 26 ingressos.
'''


preco = 5
ingressosVendidos = 120

while preco >1:
    print ("Lucro máximo: ", ingressosVendidos * preco - 200, "preço do ingresso:", preco, "Quantidade de ingressos vendidos", ingressosVendidos)
    preco = preco - 0.5
    ingressosVendidos = ingressosVendidos + 26

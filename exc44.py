preço_total = 0
preço_1000 = 0
produto_barato = 0
menor = 0
menor_produto = 0
while True:
    produto = str(input('Nome do Produto: '))
    preço = int(input('Preço: R$'))
    preço_total += preço
    resposta = ' '
    menor = preço
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print('-' * 30)
    if resposta == 'N':
        break
    if preço > 1000:
        preço_1000 += 1
    if menor < preço:
        menor = preço
        produto = menor_produto
print(f'O total da compra foi R${preço_total:.2f}') 
print(f'Temos {preço_1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi a {produto} que custa R${menor:.2f}')
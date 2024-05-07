lista = []
elementos = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    elementos += 1
    perg = str(input('Quer continuar? [S/N] '))
    if perg not in 'Ss':
        break
lista.sort(reverse=True)
print(f'Você digitou um total de {elementos} elementos')
print(f'Os valores em ordem decrescente {lista}')
if 5 in lista:
    print('O valor 5 está na lista! ')
else:
    print('O valor 5 não foi encontrado na lista!')

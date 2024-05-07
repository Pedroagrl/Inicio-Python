lista = []
while True:
    temp = (int(input('Digite um valor: ')))
    if temp in lista:
        print('Este valor já está na lista')
    else:
        lista.append(temp)
        print('Valor adicionado com sucesso...')
    continuar = str(input('Quer continuar? [S/N] '))
    if continuar not in 'Ss':
        break
lista.sort()
print(f'Você digitou os valores {lista}')
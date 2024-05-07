lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    perg = str(input('Quer continuar? [S/N] ')).strip().lower()
    if perg not in 's':
        break
print(f'A lista completa é {lista}')
pares = []
impares = []
for num in lista:
    if num % 2 == 0 or 0:
        pares.append(num)
    else:
        impares.append(num)
if pares:
    print('Os numeros pares da lista são: ', end='')
    print(f'{pares}')
else:
    print('Não há numeros pares nessa lista')
if impares:
    print('Os numeros impares da lista são: ', end='')
    print(f'{impares}')
else:
    print('Não há numeros impares nessa lista') 
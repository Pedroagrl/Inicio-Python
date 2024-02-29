numero_divisivel = int(input('Digite um numero: '))
total_dividido = 0
for c in range(1, numero_divisivel + 1):
    if numero_divisivel % c == 0:
        print('\033[33m', end=' ')
        total_dividido += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end='')
print(f'\n\033[mO numero {numero_divisivel} foi divisivel {total_dividido} vezes')
if total_dividido == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele não é PRIMO!')
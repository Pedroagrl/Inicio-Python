numero = int(input('Digite um numero: '))
calculo = numero
fatorial = 1
print(f'Calculando {numero}! = ', end='')
while calculo > 0:
    print(f'{calculo}', end='')
    print(' x ' if calculo > 1 else ' = ', end ='')
    calculo -= 1
    fatorial *= calculo
print(f'{fatorial}')
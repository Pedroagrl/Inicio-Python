contagem = ('zero', 'um', 'dois', 'três', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove',
            'dez', 'onze', 'doze', 'treze', 'catorze',
            'quinze', 'dezesseis', 'dezessetee', 'dezoito',
            'dezenove', 'vinte')
while True:
    numero = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= numero <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o numero {contagem[numero]}')
print('-'*30)
print('Sequência Fibonacci')
print('-'*30)
termos = int(input('Quantos termos você quer mostrar? '))
termo1 = 0
termo2 = 1
print(f'{termo1} > {termo2}', end='')
contador = 3
while contador <= termos:
    termo3 = termo1 + termo2
    print(f' > {termo3}', end='')
    contador += 1
    termo1 = termo2
    termo2 = termo3
print(' > FIM')
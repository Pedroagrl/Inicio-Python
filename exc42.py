from random import randint

print('-' * 30)
print('VAMOS JOGAR IMPAR OU PAR')
print('-' * 30)

vezes = 0

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ''
    
    while tipo not in ['P', 'I']: 
        tipo = str(input('Par ou Impar [P/I] ')).strip().upper()[0]
        if tipo not in ['P', 'I']:
            print('Entrada inválida. Por favor, escolha P para Par ou I para Ímpar.')
        
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end='')
    print(' DEU PAR' if total % 2 == 0 else ' DEU IMPAR')
    
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU! ')
            vezes += 1
        else: 
            print('Você PERDEU! ')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU! ')
            vezes += 1
        else:
            print('Você PERDEU! ')
            break

    print('Vamos jogar novamente...')
    print('-' * 30)
from random import randint

def sorteio(sort):
    par = 0
    print(f'Sorteando 6 valores da lista {sort} PRONTO!')
    for num in sort:
        if num % 2 == 0:
            par += num
    print(f'Somandos o valores pares de {sort}, temos {par}')

sorteio([randint(1, 30) for c in range(6)]) 
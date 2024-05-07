from time import sleep

def contador(i, f, p): 
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    print('-=' * 20)

    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    if i < f:
        contador = i
        while contador <= f:
            print(f'{contador}', end=' ',flush=True)
            sleep(0.5)
            contador += p
        print('FIM!')
    else:
        contador =  i
        while contador >= f:
            print(f'{contador}', end=' ', flush=True)
            sleep(0.5)
            contador -= p
        print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2) 
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
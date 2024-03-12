while True:
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if tabuada < 0:
        break
    for c in range(1, 11):
        print(f'{tabuada} x {c} = {tabuada*c}')
    print('-' * 30)
print('PROGRAMA DA TABUADA ENCERRADO. Volte sempre!')
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2)/2
print(f'A sua media foi {media:.1f}')
if media >= 7.0:
    print('Você está na media, PARABÉNS!!')
else:
    print('Você está abaixo da media, estude mais! ')
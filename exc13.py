Oposto = int(input('Comprimento cateto oposto: '))
Adjacente = int(input('Comprimento cateto adjacente: '))
Hipotenusa =  (Oposto ** 2 + Adjacente ** 2) ** (1/2)
print(f'A hipotenusa vai medir {Hipotenusa:.1f}')
x = str(input('Digite seu nome completo?? ')).strip()
y = x.split()
print(f'Seu primeiro nome é {y[0]}')
print(f'Seu ultimo nome é {y[-1]}')
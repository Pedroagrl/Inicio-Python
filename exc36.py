primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro_termo
contador = 1
total = 0
mais_termos = 10
while mais_termos != 0:
    total = total + mais_termos
    while contador <= total:
        print(f'{termo}', end=' > ')
        contador += 1
        termo += razao
    print('PAUSA')
    mais_termos = int(input('Quantos termo você quer mostrar a mais? '))
print('FIM')
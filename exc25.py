primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
calculo_decimo = primeiro_termo + (10 - 1) * razao
for c in range(primeiro_termo, calculo_decimo + razao, razao):
    print(f'{c}', end=' > ')
print('ACABOU!')

numero = (int(input('Digite um numero: ')),
        int(input('Digite outro numero: ')),
        int(input('Digite mais um numero: ')),
        int(input('O ultimo numero: ')))
print(f'Você digitou os valores {numero}')
print(f'O valor 9 apareceu {numero.count(9)} vezes')
if 3 in numero:
    print(f'O numero 3 aparaceu na {numero.index(3)+1}º posição')
else:
    print('O valor 3 não foi digitado')
print(f'Os numeros pares digitados foram', end=' ')
for n in numero:
    if n % 2 == 0:
        print(n, end=' ')
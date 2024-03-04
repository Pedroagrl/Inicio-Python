continuar = 'Ss'
contador = 0
soma = 0
media = 0
menor = maior = 0
while continuar in 'Ss':
    numero = int(input('Digite um numero: '))
    soma += numero
    contador += 1
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
    continuar = str(input('Quer continuar? [S/N] '))
media = soma / contador
print(f'Você digitou {contador} números e a média foi {media:.2f}')
print(f'O maior valor digitado foi {maior} e o menor {menor}')
print('FIM')

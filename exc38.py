numero =  int(input('Digite um numero [999 para parar]: '))
contador = 0
soma = 0
while numero != 999:
    contador += 1
    soma += numero
    numero =  int(input('Digite um numero [999 para parar]: '))
print(f'Você digitou {contador} números e a soma entre eles é {soma}')
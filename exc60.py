from random import randint
lista = list()
jogos = list()
print('-' * 30)
print('       JOGA NA MEGA SENA     ')
print('-' * 30)
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
total = 0
while total <= quantidade:
    contagem = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            contagem += 1
        if contagem >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear() 
    total += 1  
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
from random import randint
menor = maior = 0
computador = menor = maior
computador = (randint(0, 10), randint(0, 10) , randint(0, 10),
              randint(0, 10), randint(0, 10)) 
print(f'Os valores sorteados foram {computador}')
print(f'O maior valor é {max(computador)}')
print(f'O menor valor é {min(computador)}')
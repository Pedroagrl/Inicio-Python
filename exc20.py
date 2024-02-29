import random

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogada = int(input('Qual é a sua jogada? '))

if jogada == 0:
    print('O jogador escolheu PEDRA')
elif jogada == 1:
    print('O jogador escolheu PAPEL')
elif jogada == 2:
    print('O jogador escolheu TESOURA')

escolha_computador = random.randint(0, 2)

if escolha_computador == 0:
    print('O computador escolheu PEDRA')
elif escolha_computador == 1:
    print('O computador escolheu PAPEL')
elif escolha_computador == 2:
    print('O computador escolheu TESOURA')

if jogada == escolha_computador:
    print('EMPATE!')
elif (jogada == 0 and escolha_computador == 2) or \
     (jogada == 1 and escolha_computador == 0) or \
     (jogada == 2 and escolha_computador == 1):
    print('O jogador GANHOU!')
else:
    print('O computador GANHOU!')
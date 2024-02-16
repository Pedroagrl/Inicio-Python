import random
import time
from datetime import date

nome = str(input('Qual seu nome? '))
if nome == 'Pedro':
    print('Que nome lindo você tem!')
else:
    print('Que nome comum esse seu né!?')
print(f'Bom dia, {nome}')


n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2)/2
print(f'A sua media foi {media:.1f}')
if media >= 7.0:
    print('Você está na media, PARABÉNS!!')
else:
    print('Você está abaixo da media, estude mais! ')


print('\033[93m-=-\033[0m' * 20)
numero = print('\033[34mVou pensar em um numero entre 0 e 5. Tente adivinhar... \033[0m')
print('\033[93m-=-\033[0m' * 20)
pergunta = int(input('Em que número pensei? '))
print('\033[95mPROCESSANDO...\033[0m')
time.sleep (2)
escolhido = random.choice([0, 1, 2, 3, 4, 5])
if pergunta == escolhido:
    print('\033[92mParabéns, você acertou!\033[0m]')
else:
    print(f'\033[91mVocê errou!, o número era {escolhido}\033[0m')


velocidade = float(input('Qual a velocidade do seu carro? '))
if velocidade > 80:
    print('\033[91mMUTADO! Você excedeu a velocidade de 80Km/h!\033[0m ')
    multa = (velocidade-80) * 7
    print(f'\033[91mE o valor da multa é de {multa:.0f}R$\033[0m')
print('\033[93mTenha um bom dia, dirija com segurança!\033[0m')
n = int(input('Digite um numero qualquer: '))
resultado = n % 2
if resultado == 0:
    print(f'O número {n} é PAR')
else:
    print(f'O número {n} é IMPAR')

ano = int(input('Que ano você quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} NÃO É BISSEXTO')
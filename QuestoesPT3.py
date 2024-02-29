from datetime import date
import random

casa = float(input('Qual valor da casa: '))
salario = float(input('Qual salario do comprador: '))
financiamento = int(input('Quantos anos de financiamente: '))
ano = financiamento * 12
prestacao = casa/ano
print(f'Para pagar uma casa de R${casa:.2f} em {financiamento} anos a prestação será de R${prestacao:.2f} por mes')
if prestacao >= salario * 30/100:
    print('Emprestimo não pode ser CONCEDIDO')
else:
    print('Emprestimo pode ser CONCEDIDO')

v1 = float(input('Primeiro valor: '))
v2 = float(input('Segundo valor: '))
if v1 > v2:
    print(f'O PRIMEIRO valor é maior')
elif v1 == v2:
    print('Os dois valores são iguais')
else:
    print(f'O SEGUNDO valor é maior')
    
atual = date.today()
nasc = int(input('Ano de nascimento: '))
idade = atual.year - nasc 
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para você se alistar')
    ano2 = atual.year + saldo
    print(f'Você irá se alistar em {ano2}')
else:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos')
    ano2 = atual.year - saldo
    print(f'Você se alistou em {ano2}')

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triangulo ', end= '')
    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('Os segmeentos acima NÃO PODEM FORMAR um triangulo')


peso = float(input('Qual seu peso? (Kg) '))
altura = float(input('Qual sua altura? (m) '))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {imc:.1f} ')
if imc < 18.5:
    print('Você está abaixo do peso')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal ')
elif 25 <= imc < 30:
    print('Você está entrando no sobrepeso')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE! ')
elif imc >= 40:
    print('Você está em OBESIDADE MORBIDA, cuidado!')

print('''Sua opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogada = int(input('Qual sua jogada? '))

if jogada == 0:
    print('O jogador escolheu PEDRA')
elif jogada == 1:
    print('O jogador escolheu PAPEL')
elif jogada == 2:
    print('O jogador escolheu TESOURA')

escolhido = random.choice(['PEDRA', 'TESOURA', 'PAPEL'])

if escolhido == 0:
    print('PEDRA')
elif escolhido == 1:
    print('PAPEL')
elif escolhido == 2:
    print('TESOURA')
print(f'O computador escolheu {escolhido}')

if escolhido == 'PEDRA' and jogada == 2:
    print('\033[91mO computador GANHOU!\033[m')
elif escolhido == 'TESOURA' and jogada == 1:
    print('\033[91mO computador GANHOU!\033[m')
elif escolhido == 'PAPEL' and jogada == 0:
    print('\033[91mO computador GANHOU!\033[m')

if jogada == 0 and escolhido == 'TESOURA\033[m':
   print('\033[91mO jogador GANHOU!')
elif jogada == 1 and escolhido == 'PEDRA\033[m':
    print('\033[91mO jogador GANHOU!')
elif jogada == 2 and escolhido == 'PAPEL\033[m':
    print('\033[91mO jogador GANHOU!\033[m')
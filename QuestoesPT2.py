import math
import random

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome..')
print(f'Seu nome em maiusculo é {nome.upper()}')
print(f'Seu nome em minusculo é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(' ')} letras')
num = int(input('Informe um número de quatro digitos: '))
n = str(num)
print(f'Unidade: {n[3]}')
print(f'Dezena: {n[2]}')
print(f'Centena: {n[1]}')
print(f'Milhar: {n[0]}')
x = str(input('Digite seu nome completo?? ')).strip()
y = x.split()
print(f'Seu primeiro nome é {y[0]}')
print(f'Seu ultimo nome é {y[-1]}')

Largura = float(input('Largura da parede: '))
Altura = float(input('Altura da parede: '))
Resultado = Largura*Altura
print(f'Sua parede tem a dimensão de {Largura}x{Altura} e área de {Resultado:.2f}m²')
Valor = float(input('Digite um valor: '))
print(f'O valor digitado foi {Valor} e a sua porção inteira é {int(Valor)}')
Oposto = int(input('Comprimento cateto oposto: '))
Adjacente = int(input('Comprimento cateto adjacente: '))
Hipotenusa =  (Oposto ** 2 + Adjacente ** 2) ** (1/2)
print(f'A hipotenusa vai medir {Hipotenusa:.1f}')
n1= str(input('Primeiro Aluno: '))
n2= str(input('Segundo Aluno: '))
n3= str(input('Terceiro Aluno: '))
lista = [n1, n2, n3]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')


import random

n1= str(input('Primeiro Aluno: '))
n2= str(input('Segundo Aluno: '))
n3= str(input('Terceiro Aluno: '))
lista = [n1, n2, n3]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')

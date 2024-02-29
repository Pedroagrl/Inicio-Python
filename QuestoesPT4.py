from datetime import date
from time import sleep

for cont in range(10, -1, -1):
    print(cont)
    sleep(1.0)
print('BUM! BUM! POOW!')

numero_par = int(input('Digite um número: '))
for cont in range(0, numero_par+2, 2):
    print(f'{cont}')
    
soma = 0
contagem = 0
for c in range(1, 7):
    valor_par = int(input(f'Digite o {c}º valor: '))
    if valor_par % 2 == 0: 
        soma += valor_par       
        contagem += 1
print(f'Você informou {contagem} numeros PARES e a soma foi {soma}')

numero_tabuada = int(input('Digite numero para ver sua tabuada: '))
for c in range(1, 11):
    print(f'{numero_tabuada} x {c:.0f} = {numero_tabuada * c}')

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
calculo_decimo = primeiro_termo + (10 - 1) * razao
for c in range(primeiro_termo, calculo_decimo + razao, razao):
    print(f'{c}', end=' > ')
print('ACABOU!')

numero_divisivel = int(input('Digite um numero: '))
total_dividido = 0
for c in range(1, numero_divisivel + 1):
    if numero_divisivel % c == 0:
        print('\033[33m', end=' ')
        total_dividido += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end='')
print(f'\n\033[mO numero {numero_divisivel} foi divisivel {total_dividido} vezes')
if total_dividido == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele não é PRIMO!')


frase_invertida = str(input('Digite uma frase: ')).strip().upper()
palavras = frase_invertida.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('Não temos um PALÍNDROMO!')

menor_idade = 0
maior_idade = 0
atual = date.today()
for ano in range(1,8):
    ano_nascido = int(input(f'Em que ano a {ano}º nasceu? '))
    idade = atual.year - ano_nascido
    if idade >= 18:
        maior_idade += 1
    elif idade < 18:
        menor_idade += 1
print(f'Ao todo tivemos {maior_idade} pessoas maior de idade')
print(f'E tambem tivemos {menor_idade} pessoas menor de idade')

maior_peso = 0
menor_peso = 0
for peso in range(1,6):
    peso_pessoa = float(input(f'Peso da {peso}º pessoa: '))    
    if peso ==1:
        maior_peso = peso_pessoa
        menor_peso = peso_pessoa
    else:
        if peso_pessoa > maior_peso:
             maior_peso = peso_pessoa
        if peso_pessoa < menor_peso:
            menor_peso = peso_pessoa
print(f'O maior peso é {maior_peso}Kg ')
print(f'E o menor peso {menor_peso}Kg')

soma_idade = 0
media_idade = 0
maior_idade_homem = 0
total_mulher = 0
nome_velho = ''
for completo in range(1,5):
    print(f'------{completo}º PESSOA------')
    nome_completo = str(input('Nome: ')).strip()
    idade_completo = int(input('Idade: '))
    sexo_completo = str(input('Sexo [M/F]:')).strip()
    soma_idade += idade_completo
    if completo == 1 and sexo_completo in 'Mm':
        maior_idade_homem = idade_completo
        nome_velho = nome_completo
    if sexo_completo in 'Mm' and idade_completo > maior_idade_homem:
        maior_idade_homem = idade_completo
        nome_velho = nome_completo
    if sexo_completo in 'Ff' and idade_completo < 20:
        total_mulher += 1
    media_idade += idade_completo / 4
print(f'A media de idade do grupo é de {media_idade} anos ')
print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_velho}')
print(f'Ao todo são {total_mulher} mulheres com menos de 20 anos')
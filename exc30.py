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
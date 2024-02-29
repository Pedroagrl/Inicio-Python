from datetime import date

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

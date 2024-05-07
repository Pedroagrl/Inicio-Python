galera = list()
dados = dict()
media = total = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F. ')
    dados['idade'] = int(input('Idade: '))
    total += dados['idade']
    galera.append(dados.copy())
    while True: 
        continuar = str(input('Quer continuar? [S/N] ')).upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N. ')
    if continuar == 'N':
        break
print('=-' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas. ')
media = total / len(galera)
print(f'A media de idade é de {media:5.2f} anos')
print('As mulheres cadastradas foram' , end=' ')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p['nome']}', end='')
print()
print('Lista das pessoas que estão acima da media', end='')
for p in galera:
    if p['idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<ENCERRADO>>')
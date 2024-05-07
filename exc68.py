time = list()
dados = dict()
partidas = list()
while True:
    dados.clear()
    dados['Nome'] = str(input('Nome do jogador: '))
    dados['Partidas'] = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
    partidas.clear()
    for g in range(0, dados['Partidas']):
        partidas.append(int(input(f'Quantos gols na partida {g+1}? ')))
    dados['Gols'] = partidas[:]
    dados['Total'] = sum(partidas)
    time.append(dados.copy())
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
print('-=' * 30)
print('Cod', end='  ')
for i in dados.keys():
    print(f'{i:<14}', end='')
print()
print('-=' * 40)
for k, v in enumerate(time): 
    print(f'{k:>3} ', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print()
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com codigo {busca}')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
dados = dict()
partidas = list()
dados['Nome'] = str(input('Nome do jogador: '))
dados['Partidas'] = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
for g in range(0, dados['Partidas']):
    partidas.append(int(input(f'Quantos gols na partida {g}? ')))
dados['gols'] = partidas[:]
dados['total'] = sum(partidas)
print('-=' * 30)
print(dados)
print('-=' * 30)
for k,v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {dados["Nome"]} jogou {dados["Partidas"]} partidas. ')
for i, v in enumerate(dados['gols']):
    print(f'  => Na partida {i}, fez {v} gols. ')
print(f'Foi um total de {dados['total']} gols. ')
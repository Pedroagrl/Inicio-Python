def ficha(jog='<desconhecido>', g=0):
    print(f'O jogador {jog} fez {g} gol(s) no campeonato!')

    
nome = str(input('Nome do jogador: '))
gol = str(input('Numero de gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    g = 0
if nome.strip() == '':
    ficha(gol=g)
else:
    ficha(nome, gol)
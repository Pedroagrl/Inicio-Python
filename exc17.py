from datetime import date

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
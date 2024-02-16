n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))
resultado = (n1 + n2 + n3 + n4)/4
print(f'A média das notas ({n1:.0f}, {n2:.0f}, {n3:.0f}, {n4:.0f}) é {resultado}')

if resultado >= 7:
    print('\033[92mParabéns! Você foi aprovado\033[0m ')
elif resultado >=4:
    print('\033[91mVocê vai para a recuperação!!\033[0m ')
else:
    print('\033[91mVocê foi reprovado!\033[0m ')

numero = resultado % 2
if numero == 0:
    print(f'\033[34mA media {resultado} é um número PAR\033[0m')
else:
    print(f'\033[34mA média {resultado} é um número IMPAR\033[0m')
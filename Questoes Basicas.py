
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))
resultado = (n1 + n2 + n3 + n4)/4
print(f'A média das notas ({n1:.0f}, {n2:.0f}, {n3:.0f}, {n4:.0f}) é {resultado:.2f}')

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

preco = float(input('Preço das compras: R$'))
print('''Formas de pagamento: 
[1] à vista dinheiro/chque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão ''')
opcao = int(input('Qual sua opção de pagamento? '))
if opcao == 1:
    total = preco - (preco * 10/100)
elif opcao == 2:
    total = preco - (preco * 5/100)
elif opcao == 3:
    total = preco * 1
    juros = preco / 2
    print(f'Sua compra será parcelada em 2x de R${juros} SEM JUROS')
elif opcao == 4:
    parcelas = int(input('Quantas vezes parcelada? '))
    parcelado = preco / parcelas
    total = preco + (preco * 20/100)
    print(f'Sua compra será parcelada em {parcelas}x de R${parcelado}')
print(f'Sua compra de R${preco} vai custar R${total}')
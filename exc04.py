velocidade = float(input('Qual a velocidade do seu carro? '))
if velocidade > 80:
    print('\033[91mMUTADO! Você excedeu a velocidade de 80Km/h!\033[0m ')
    multa = (velocidade-80) * 7
    print(f'\033[91mE o valor da multa é de {multa:.0f}R$\033[0m')
print('\033[93mTenha um bom dia, dirija com segurança!\033[0m')
n = int(input('Digite um numero qualquer: '))
resultado = n % 2
if resultado == 0:
    print(f'O número {n} é PAR')
else:
    print(f'O número {n} é IMPAR')
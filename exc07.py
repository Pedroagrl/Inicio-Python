salario = float(input('Qual o salario do funcionario? '))
if salario <= 5000:
    salario2 = (salario * 3/20) + salario
if salario >= 5000:
    salario2 = (salario * 1/10) + salario
print(f'Quem ganhava {salario:.2f} passa a ganhar {salario2:.2f}')
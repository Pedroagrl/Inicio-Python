casa = float(input('Qual valor da casa: '))
salario = float(input('Qual salario do comprador: '))
financiamento = int(input('Quantos anos de financiamente: '))
ano = financiamento * 12
prestacao = casa/ano
print(f'Para pagar uma casa de R${casa:.2f} em {financiamento} anos a prestação será de R${prestacao:.2f} por mes')
if prestacao >= salario * 30/100:
    print('Emprestimo não pode ser CONCEDIDO')
else:
    print('Emprestimo pode ser CONCEDIDO')
soma = 0
contagem = 0
for c in range(1, 7):
    valor_par = int(input(f'Digite o {c}º valor: '))
    if valor_par % 2 == 0: 
        soma += valor_par       
        contagem += 1
print(f'Você informou {contagem} numeros PARES e a soma foi {soma}')
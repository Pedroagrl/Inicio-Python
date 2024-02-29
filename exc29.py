maior_peso = 0
menor_peso = 0
for peso in range(1,6):
    peso_pessoa = float(input(f'Peso da {peso}º pessoa: '))    
    if peso ==1:
        maior_peso = peso_pessoa
        menor_peso = peso_pessoa
    else:
        if peso_pessoa > maior_peso:
             maior_peso = peso_pessoa
        if peso_pessoa < menor_peso:
            menor_peso = peso_pessoa
print(f'O maior peso é {maior_peso}Kg ')
print(f'E o menor peso {menor_peso}Kg')
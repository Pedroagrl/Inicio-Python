sexo = str(input('Informe seu sexo[M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Porfavor, dados invalidos, informe seu sexo[M/F]: '))
print(f'Sexo {sexo.upper()} valido com sucesso!')
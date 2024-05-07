def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [6, 3, 4, 5, 9, 0]
dobra(valores)
print(valores)
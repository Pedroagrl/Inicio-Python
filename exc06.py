a = int(input('Primeiro valor: '))
b = int(input('Primeiro valor: '))
c = int(input('Primeiro valor: '))
if a<b and a<c:
    menor = a
if b<c and b<a:
    menor = b
if c<a and c<b:
    menor = c
if a>b and a>c:
    maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(f'O menor valor digitado foi {menor} e o maior foi {maior}')

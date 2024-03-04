Primeiro_Valor = int(input('Digite o primeiro valor: '))
Segundo_Valor = int(input('Digite o segundo valor: '))
Pergunta_Opcao = 0
while Pergunta_Opcao != 5:  
    print('''Suas opções:
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos numeros
    [ 5 ] Sair do programa
    ''')
    Pergunta_Opcao = int(input('Qual sua opcao? '))
    if Pergunta_Opcao == 1:
        Soma = Primeiro_Valor + Segundo_Valor
        print(f'A soma de {Primeiro_Valor} + {Segundo_Valor} é {Soma}')
    elif Pergunta_Opcao == 2:
        Multiplicacao = Primeiro_Valor * Segundo_Valor
        print(f'A multiplicacao de {Primeiro_Valor} x {Segundo_Valor} é {Multiplicacao}')
    elif Pergunta_Opcao == 3:
        if Primeiro_Valor == Segundo_Valor:
            print('Nenhum é maior que o outro, os valores são iguais.')
        elif Primeiro_Valor > Segundo_Valor:
            print(f'O maior valor entre {Primeiro_Valor} e {Segundo_Valor} é o {Primeiro_Valor}')
        else:
            print(f'O maior valor entre {Primeiro_Valor} e {Segundo_Valor} é o {Segundo_Valor} ')
    elif Pergunta_Opcao == 4:
        print('Informe os numeros novamente')
        Primeiro_Valor = int(input('Digite o primeiro valor: '))
        Segundo_Valor = int(input('Digite o segundo valor: '))
    elif Pergunta_Opcao == 5:
        print('Finalizando...')
    else:
        print('Opção invalida! Tente novamente.')
print('Fim do programa, volte sempre!')
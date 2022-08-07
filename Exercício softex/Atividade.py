def calculadora():
 from time import sleep
 n1 = int(input('Digite o primeiro valor: '))
 n2 = int(input('Digite o segundo valor: '))

 opção = 1

 while opção != 0: 
    
    print('''    {1} somar
    {2} subtrair
    {3} multiplicação
    {4} divisão
    {5} novos números
    {0} sair ''')

    opção= int(input('Qual é a sua opção? '))
    if opção == 1:
         soma = n1 + n2
         print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        Subtração = n1 - n2
        print('A Subtração de {} e {} é {}'.format(n1, n2, Subtração))
    elif opção == 3:
        multiplicação = n1 * n2
        print(' A multiplicação entre {} e {} é {}'.format(n1, n2, multiplicação))   
    elif opção == 4:   
        divisão = n1 / n2
        print('A divisão entre {} e {} é {}'.format(n1, n2, divisão)) 
    elif opção == 5:
        print('Informe os números novamente: ') 
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
         
    elif opção == 0:
        print('Finalizando...')
    else:
        print('Opção inválida. tente novamente ') 
    print('=-=' * 10)
    sleep(2)     
 print('Fim do programa! volte sempre! ')
 
calculadora()
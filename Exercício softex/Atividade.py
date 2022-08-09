import sys
def adicao(a, b):
  return (n1 + n2)

def subtracao(a, b):
  return (n1 - n2)

def multiplicacao(a, b):
  return (n1 * n2)

def divisao(a, b):
  return (n1 / n2)

def cabecalho():
    print('-'*25)
    print('CALCULADORA BÁSICA')
    print('.'*25)
    print('''    1. Soma
    2. Substração
    3. Multiplicacão
    4. Divisão
    ©. Sair''')
    print('.' *25)
x = 1
while x != 0:
   print(' ')
   cabecalho()
   
   x = int (input ("\nEscolha uma das Operações citadas acima: "))
   if x == 1:
        print("\nopção escolhida => SOMA: ")
   elif x == 2:
        print ("\nopção escolhida =› SUBTRAÇÃO: ")
   elif x == 3:
        print ("\nopção escolhida =› MULTIPLICAÇÃO: ")
   elif x == 4:
        print ("\nopção escolhida =› DIVISÃO: ")
   elif x > 4:
        print(' ')
        print("\nOpção invalida: ")
        print('')
        cabecalho()
        x = int (input ("\nEscolha uma das Operações citadas acima: "))
   else: 
        X = 0
        print("\nProcesso encerrado. \n")
        exit(0)
        
   n1 = float(input("\ninsirao primeiro numero: \n") )
   n2 = float(input("\ninsira o segundo numero: \n"))
   
   
   if x == 1:
     print(' ')
     print ('\n\nResultado da soma entre ', '(',str(n1), ') e (', str(n2),')', ' é igual a (', float(adicao(n1, n2)),') ')
    
   elif x == 2:
     print(' ')
     print('\n\nResultado da Subtração entre ', '(',str(n1), ') e (', str(n2),')' , ' é igual a ( ', float(subtracao(n1, n2)),') ')
       
   elif x == 3:
     print(' ')
     print('\n\nResultado da Operação entre ', ' (',str(n1), ') Multiplicado por (', str(n2),')' , ' é igual a (', float(multiplicacao(n1, n2)),') ')
   elif x == 4:
     print(' ')
     print('\n\nResultado da Operação entre ', '(',str(n1), ') Dividido por (', str(n2),')' , ' é igual a (', float(divisao(n1, n2)),') ')
     
       
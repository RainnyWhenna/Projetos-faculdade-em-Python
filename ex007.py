#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
#O usuário deve informar de qual número ele deseja ver a tabuada.
#A saída deve ser conforme o exemplo abaixo:
#Tabuada de 5:
#5 X 1 = 5
#5 X 2 = 10
#...
#5 X 10 = 50

num = int(input('Digite um número entre 1 a 10 para saber a tabuada: '))

if num < 1: print('Número inválido, por favor digite um número de 1 a 10')
elif num > 10: print('Número inválido, por favor digite um número de 1 a 10')
else:
    for cont in range (11): print('{} X {} = {}'.format(num, cont, (num * cont)))
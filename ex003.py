#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#- Para homens: (72.7*h) - 58
#- Para mulheres: (62.1*h) - 44.7

h = float(input('Digite a sua altura: '))
pesoIdealFeminino = (62.1 * h)-44.7
pesoIdealMasculino = (72.7 * h)-58

print('Para uma mulher com {} de altura, o peso ideal é {:.1f}'.format(h, pesoIdealFeminino))
print('Para um homem com {} de altura, o peso ideal é {:.1f}'.format(h, pesoIdealMasculino))
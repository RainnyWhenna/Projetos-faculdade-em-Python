#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8%
#para o INSS e 5% para o sindicato, faça um programa que nos dê:
#- salário bruto.
#- quanto pagou ao INSS.
#- quanto pagou ao sindicato.
#- o salário líquido.
#- calcule os descontos e o salário líquido, conforme a tabela abaixo:
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#- Salário Líquido : R$
#Obs: Salário Bruto - Descontos = Salário Líquido.

salHora = float(input('Quanto você ganha por hora? '))
horasTrabalhadas = int(input('Quantas horas você trabalhou este mês? '))
salBruto = salHora * horasTrabalhadas
imposto = (11*salBruto)/100
inss = (8*salBruto)/100
sindicato = (5*salBruto)/100
totalDescontos = imposto + inss + sindicato
salLiquido = salBruto - totalDescontos
print('Seu salario bruto é R$ {:.2f}'.format(salBruto))
print('Seu desconto do INSS foi de R$ {:.2f}'.format(inss))
print('O valor pago ao Sindicato foi de R$ {:.2f}'.format(sindicato))
print('Seu desconto do Imposto de Renda foi de R$ {:.2f}'.format(imposto))
print('Seu salário líquido este mês é R$ {:.2f}'.format(salLiquido))
#Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado
#um valor igual a -1 (que não deve ser armazenado).
#Após esta entrada de dados, faça:
#- Mostre a quantidade de valores que foram lidos;
#- Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#- Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#- Calcule e mostre a soma dos valores;
#- Calcule e mostre a média dos valores;
#- Calcule e mostre a quantidade de valores acima da média calculada;
#- Calcule e mostre a quantidade de valores abaixo de sete;
#- Encerre o programa com uma mensagem;

def principal():
    num = int(input('Digite um número: '))
    val = list()
    cont = 0
    soma = 0
    media = 0
    maior = 0
    menor = 0

    while num != -1:
        cont = cont + 1
        soma = soma + num
        val.append(num)
        if num < 7: menor = menor +1

        num = int(input('Digite um número: '))

    media = soma / cont

    for i in val:
        if i > media:
            maior = maior +1

    print('Foram lidos {} valores.'.format(cont))
    print('Os valores lidos foram: {}'.format(val))
    val.reverse()
    print('Os valores lidos de trás para frente são:') #Um embaixo do outro
    print(*val,sep='\n')
    print('A soma dos valores lidos é {}'.format(soma))
    print('A média dos valores lidos é {:.1f}'.format(media))
    print('Foram digitados {} valores acima da média dos números digitados.'.format(maior))
    print('Foram digitados {} números menores que sete.'.format(menor))

    print('Obrigada por participar!')

principal()
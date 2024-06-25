#script em python para calcular a sequencia de fibonacci pelo numero de termos providos pelo usuario
#numero de termos desejados pelo usuario
nTermos = int(input('Quantos termos você deseja exibir: '))
print('-'*20)

if nTermos <= 0:
    print("Por favor, insira um número positivo.")
else:
    termo1, termo2 = 0, 1
    count = 1

    if nTermos == 1:
        print(termo1)
    else:
        print('{} -- {}'.format(termo1, termo2), end='')

        #faz um counter para o numero de termos
        while count < nTermos - 1:
            #o terceiro termo sempre será a soma dos termos 1 e 2
            termo3 = termo1 + termo2
            print(' -- {} '.format(termo3), end='')
            #termo 1 vai ser = ao termo 2
            #termo 2 vai ser = ao termo 3
            termo1, termo2 = termo2, termo3
            #adiciona mais um numero ao contador
            count += 1
    print(' -- esses são os {} primeiros termos da sequencia de fibonacci'.format(nTermos))
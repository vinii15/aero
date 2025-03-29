total = 0
dinheiro = 0



while True:
    idade = (input('Digite sua idade:'))
    if idade == 'sair':
        break
    idade = int(idade)

    if idade<3 :
        ingresso= 0
    else:
       if idade>12 :
            ingresso=30
       else:
            ingresso=15

    dinheiro += ingresso
    media= dinheiro/total

    print('Total de pessoas{}'.format(total))
    print('total de dinheiro{}'.format(total))
    print('media arrecadada{}'.format(media))

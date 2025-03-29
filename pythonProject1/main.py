print( 'olá,mundo !')
x = int (input ('digite um numero inteiro : '))
y = int (input(' digite outro numero inteiro : '))
#maneira classica
res = ' o resultado da soma de %i com %i e %i .' % ( x , y , x + y)
print (res)

#maneira mderna
res = ' o resultado da soma de {} com {} e {}.'.format( x , y , x + y)
print(res)

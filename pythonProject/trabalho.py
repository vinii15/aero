print('Bem-vindo a loja do Vinícius Pereira dos Santos')

ValorProduto = float( input('Informe o valor do produto: R$ ') )

Quant = int(input('Informe a quantidade do produto:'))

if 0 <= Quant < 200:

   desconto = 0

elif 200 >= Quant <1000:

   desconto = 0.5

elif 1000 <= Quant < 2000:

    desconto = 0.10

else:

  desconto = 0.15

Semdesconto =  ValorProduto * Quant

Comdesconto = Semdesconto - Semdesconto * desconto

print('O valor Sem desconto foi R${:.2f}'. format(Semdesconto))

print('O valor Com desconto foi R${:.2f}' . format(Comdesconto, desconto))

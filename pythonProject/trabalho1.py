print('------------------------ Bem-Vindo a loja do Vinícius Pereira dos Santos ------------------------')
valor_produto = float(input('Entre com o valor do produto:'))
qtd_produto = int(input('Digite a quantidade desejada: '))
desconto_poduto = 0
#teste da variável quantidade
if qtd_produto < 200:
    desconto_poduto = 0.00
elif  (qtd_produto >=200) and (qtd_produto<=1000):
    desconto_poduto = 0.05 #5% = 0.05 || 100% = 1.00
elif  (qtd_produto >=1000) and (qtd_produto<=200):
    desconto_poduto = 0.10 #10% = 0.10 || 100% = 1.00
elif  (qtd_produto >=2000) :
    desconto_poduto = 0.15 #15% = 0.15 || 100% = 1.00

total_sem_desconto = valor_produto * qtd_produto
print('O valor total sem desconto é de: R$ {:.2f}' .format(total_sem_desconto))
total_com_desconto = total_sem_desconto - total_sem_desconto * desconto_poduto
print('O valor total com desconto é de: R$ {:.2f}' .format(total_com_desconto))

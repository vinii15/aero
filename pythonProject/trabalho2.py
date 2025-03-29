#Exercicio 2 da atividade prática
print('Bem-Vindo a sorveteria do Vinícius Pereira dos Santos')
print('------------------------------------ Cardápio ------------------------------------')
print('| N° De Bolas | Sabor tradicional (tr) | Sabor Premium (pr)| Sabor Especial (es) | ')
print('|      1      |      R$ 6,00           |     R$ 7,00       |      R$ 8,00        | ')
print('|      2      |      R$10,00           |     R$ 12,00      |      R$ 14,00       | ')
print('|      3      |      R$14,00           |     R$ 17,00      |      R$ 20,00       | ')
print('----------------------------------------------------------------------------------')
acumulador = 0
while True:
    sabor = input('Entre com o sabor desejado (tr/es/pr):')
    if sabor != 'tr' and sabor != 'es' and sabor != 'pr' :
      print('Opção Inválida. Esse sabor não existe!')
      continue # Se o usuário digitar algo inválido volta para o inicio do while

    n_bolas = input('Entre com o número de bolas de sorvete desejado (/1/2/3):')
    if n_bolas != '1' and n_bolas != '2' and n_bolas != '3' :
      print('Opção Inválida. Digite numero de bolas de sorvete que existem (/1/2/3)!')
      continue # Se o usuário digitar algo inválido volta para o inicio do while

    if n_bolas == '1' and sabor == 'tr' :
      print('Você escolheu uma bola de sorvete sabor tradicional')
      acumulador = acumulador + 6 # pega o valor que tinha no acumulador e some com 6

    elif n_bolas == '1' and sabor == 'pr':
       print('Você escolheu uma bola de sorvete sabor premium')
       acumulador = acumulador + 7 # pega o valor que tinha no acumulador e some com 7

    elif n_bolas == '1' and sabor == 'es':
       print('Você escolheu uma bola de sorvete sabor especial')
       acumulador = acumulador + 8 # pega o valor que tinha no acumulador e some com 8

    elif n_bolas == '2' and sabor == 'tr':
       print('Você escolheu duas bolas de sorvete sabor tradicional')
       acumulador = acumulador + 10 # pega o valor que tinha no acumulador e some com 10

    elif n_bolas == '2' and sabor == 'pr':
       print('Você escolheu duas bolas de sorvete sabor premium')
       acumulador = acumulador + 12 # pega o valor que tinha no acumulador e some com 12

    elif n_bolas == '2' and sabor == 'es':
       print('Você escolheu duas bolas de sorvete sabor especial')
       acumulador = acumulador + 14 # pega o valor que tinha no acumulador e some com 14

    elif n_bolas == '3' and sabor == 'tr':
       print('Você escolheu três bolas de sorvete sabor tradicional')
       acumulador = acumulador + 14 # pega o valor que tinha no acumulador e some com 14

    elif n_bolas == '3' and sabor == 'pr':
       print('Você escolheu três bolas de sorvete sabor premium')
       acumulador = acumulador + 17 # pega o valor que tinha no acumulador e some com 17

    elif n_bolas == '3' and sabor == 'es':
       print('Você escolheu três bolas de sorvete sabor especial')
       acumulador = acumulador + 20 # pegue o valor que tinha no acumulador e some com 30


    pedir_mais = input('Deseja pedir mais algum sorvete? Digite S para (sim) ou outra tecla para sair:')
    pedir_mais = pedir_mais.upper() # O usuário pode digitar letras maiusculas e minusculas de 'S' e 's'
    if pedir_mais == 'S':
        continue
    else:
        print('O valor total a ser pago: R${:.2f}' .format(acumulador))
        break

#Exercicio 3
#Início da função cachorro_peso()
def cachorro_peso():
  print('------------------------------------ Menu Pet Shop ------------------------------------')
  while True:
   try:
       cachorro_p = int(input('Digite o peso do seu animal (KG):'))
       valor = 0
       if (cachorro_p <3):
            valor =40
            return valor
       elif (cachorro_p >=3) and (cachorro_p <10):
            valor = 50
            return valor
       elif (cachorro_p >=10) and (cachorro_p <30):
           valor = 60
           return valor
       elif (cachorro_p >=30) and (cachorro_p <50):
           valor = 70
           return valor

       else:
           print('Peso inválido! Digite novamente')
           continue #retorna para a pergunta
   except ValueError:# caso o usuario digite um numero com casas decimais
       print('Pare de digitar valores não numéricos')
#fim da função peso_cachorro()

#Início da função cachorro_pelo()
def cachorro_pelo():
    print('-------------------------------------- Menu Pelagem --------------------------------------')
    while True:
      pelo_c = input('Entre com o tamanho do pelo do seu animal \n'+
                      'c - Pelo curto \n'+
                      'm - Pelo medio \n'+
                      'l - Pelo longo \n'+
                      '>> ')
      pelo_c = pelo_c.lower()# O programa reconhecera letras maiúsculas e minúsculas
      pelo_c = pelo_c.strip()
      if pelo_c == 'c':
         return  1.00
      elif pelo_c == 'm':
         return  1.5
      elif pelo_c == 'l':
         return 2.0
      else:
          print('Pare de digitar opções diferentes de (c/m/l)')
          continue #volta para o inicio do laço
#Fim da função cachorro_pelo()

#Início da função cachorro_extra()
def cachorro_extra():
    print('----------------------------------- Menu Adicionais -----------------------------------')
    acumulador = 0
    while True:
      extra_c = input('Deseja mais algum adicional?: \n'+
                      '0- Não desejo adicionais (encerrar pedido)\n'+
                      '1- Cortar as unhas do cachorro\n'+
                      '2- Escovar os dentes do cachorro\n'+
                      '3- Limpar as orelhas do cachorro\n'+
                      '>>')
      if extra_c == '0':
          return acumulador
      elif extra_c == '1':
          acumulador = acumulador + 10
          continue #volta para o inicio do laço
      elif extra_c == '2':
          acumulador = acumulador + 12
          continue
      elif extra_c == '3':
          acumulador = acumulador + 15
          continue
      else:
          print('Pare de digitar opções diferentes de 0/1/2/3:')
#Fim da função cachorro_extra()

#Início main
print('----------------- Bem-vindo ao Pet Shop do Vinícius Pereira dos Santos ----------------')
peso = cachorro_peso()

pelo = cachorro_pelo()

extra = cachorro_extra()

total =(peso * pelo)+ extra
print('O total Ficou: R${:.2f} (Peso: R${:.2f} * Pelo: R${:.2f} + Extra: R${:.2f})' .format(total,peso,pelo,extra))
#Fim do main

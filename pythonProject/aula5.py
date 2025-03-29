def valida_int(pergunta,min,max):
    x =int(input(pergunta))
    while((x<min)or(x>max)):
        x=int(input(pergunta))
    return x

def fatorial(num):
      """
      calcula o fatorial
      :param num: Numero escolhido para calcular o fatorial
      :return:caso o numero fatorial escolhido seja zero vai voltar para o valor 1
      """
      fat=1
      if num ==0:
         return fat
      for i in range(1,num+1,1):
          fat *=i #fat=fat*i
      return fat
#programa principal
x = valida_int('Digite um valor inteiro para cacucalar o fatorial:',0,9999)
print('{}!={}'.format(x,fatorial(x)))




#---------- Início das variáveis Globais ---------
lista_colaboradores = []
id_global = 0
#---------- Fim das variáveis Globais ----------


#---------- Início de cadastrar_colaboradores() ----------
def cadastrar_colaborador(id):
    print('Bem-Vindo ao menu de cadastrar Colaboradores')
    print('---------------------------------------------------')
    print('id do colaborador: {}' .format(id))
    nome = input('Entre com o NOME do colaborador:')
    setor = input('Entre com o SETOR do colaborador:')
    salario = int(input('Entre com o SALÁRIO(R$) do colaborador:'))
    dicionario_colaborador = { 'id'     : id,
                               'nome'   : nome,
                               'setor'  : setor,
                               'salario': salario }
    lista_colaboradores.append(dicionario_colaborador.copy())
#---------- Fim de cadastrar_colaborador() ----------


#---------- Início de consultar_colaborador() ----------
def consultar_colaborador():
    print('Bem-Vindo ao menu de consultar colaboradores')
    print('---------------------------------------------------')
    while True:
        opcao_consultar = input('\nEscolha a opção desejada:\n'+
                                '1-Consultar todos os colaboradores\n'+
                                '2-Consultar colaborador por (id)\n'+
                                '3-Consultar colaborador por setor\n'+
                                '4-Retornar ao Menu\n'+
                                '>>')
        if opcao_consultar == '1':
            print('Você escolheu a opção Consultar Todos os colaboradores')
            for colaborador in lista_colaboradores: #Produto vai varrer toda a lista de produtos
               print('----------------------------')
               for key, value in colaborador.items(): # varrer todos os conjuntos chave e valor do dicionario produto
                   print('{}: {}'.format(key,value))
               print('----------------------------')
        elif opcao_consultar == '2':
          print('Você escolheu a opção Consultar colaborador por (id)')
          colaborador_desejado = int(input('Entre com o (id) desejado:'))
          for colaborador in lista_colaboradores:
            if colaborador['id'] == colaborador_desejado:# O valor do campo id desse dicionario é igual o valor desejado
              print('----------------------------')
              for key, value in colaborador.items(): # varrer todos os conjuntos chave e valor do dicionario produto
                print('{}: {}'.format(key,value))
            print('----------------------------')
        elif opcao_consultar == '3':
            print('Você escolheu a opção Consultar colaborador por Setor')
            colaborador_desejado = input('Entre com o Setor desejado:')
            for colaborador in lista_colaboradores:
                if colaborador['setor'] == colaborador_desejado:# O valor do campo codigo desse dicionario é igual o valor desejado
                    print('----------------------------')
                    for key, value in colaborador.items(): # varrer todos os conjuntos chave e valor do dicionario produto
                       print('{}: {}'.format(key, value))
                print('----------------------------')

        elif opcao_consultar == '4':
            return #Sai da função consultar_colaborador de volta para  main
        else:
            print('Opção Inválida. Tente novamente')
            continue #Volta para o início do laço
#---------- Fim de consultar_colaborador() ----------


#---------- Início de remover_colaborador() ----------
def remover_colaborador():
    print('Bem-Vindo ao menu de remover colaorador')
    print('---------------------------------------------------')

    colaborador_desejado =int(input('Entre com o (id) do colaborador que deseja remover'))
    for colaborador in lista_colaboradores:
        if colaborador['id'] == colaborador_desejado:
            lista_colaboradores.remove(colaborador)
            print('Colaborador Removido')


#---------- Fim de remover_produto() ----------


#---------- Início de main() ----------
print('Bem-Vindo a Empresa do Vinícius Pereira dos Santos')
print('---------------------------------------------------')
while True:
    opcao_principal = input('\nEscolha a opção desejada:\n'+
                            '1-Cadastrar colaborador\n'+
                            '2-Consultar colaborador\n'+
                            '3-Remover colaborador\n'+
                            '4-Encerrar Programa\n'+
                            '>>')
    if opcao_principal == '1':
        id_global = id_global + 1
        cadastrar_colaborador(id_global)
    elif opcao_principal == '2':
        consultar_colaborador()
    elif opcao_principal == '3':
        remover_colaborador()
    elif opcao_principal == '4':
        break #Encerra o laço principal e o programa acaba
    else:
        print('Opção Inválida! Tente novamente')
        continue #Volta para o início do laço
#---------- Fim de main() ----------



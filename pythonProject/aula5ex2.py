def valida_int(pergunta,min,max):
    x =int(input(pergunta))
    while((x<min)or(x>max)):
        x=int(input(pergunta))
    return x
def criaArquivo(nomeArquivo):
    try:
      a=open(nomeArquivo,'wt+')
      a.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print('Arquivo {} foi criado com sucesso\n'.format(nomeArquivo))
def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo,'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        print(a.read())
    finally:
        a.close()

def cadastrarJogo(nomeArquivo,nomeJogo,nomeVideoGame):
    try:
        a =open(nomeArquivo,'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        a.write('{};{}\n'.format(nomeJogo,nomeVideoGame))
    finally:
        a.close()
#programa principal
arquivo = ' games.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado no computador')
else:
    print('Arquivo inexistente')
    criaArquivo(arquivo)
while True:
    print('MENU')
    print('1 - cadastrar novo intem')
    print('2 - Listar cadastrdos')
    print('3 - sair')

    op = valida_int('Escolha a opção desejada:',1,3)
    if op ==1:
        print('Opção de cadastrar novo item selecionado...\n')
        nomeJogo =input('nome do jogo:')
        nomeVideoGame =input('nome do videogame:')
        cadastrarJogo(arquivo,nomeJogo,nomeVideoGame)
    elif op == 2:
        print('Opção de listar selecionados...\n')
        listarArquivo(arquivo)
    elif op == 3:
        print('Encerrando o programa...')
        break



######## Exercícios Gerais #########

### Programa de gerenciamento de estoque com sistema de Login

def menu():
    titulo = 'Programa de Gerenciamento'
    cor = '\033[46m'
    print('-' * len(titulo))
    print(f'{cor}{titulo}\033[0m')
    print('-' * len(titulo))

    print('1 - Cadastre uma caixa na pilha')
    print('2 - Consultar caixas na pilha')
    print('3 - Retirar caixa da pilha')
    print('4 - Encerrar o programa')

def login(lista):
    usuario = input("Entre com seu nome de usuário: ")
    senha = input("Entre com sua senha: ")

    usuario_na_lista = False
    usuario_atual ={}

    for funcionario in lista:
        if funcionario['usuario'] == usuario:
            print('usuario cadastrado')
            usuario_na_lista = True
            usuario_atual = funcionario
            break

    if not usuario_na_lista:
        print('Não está cadastrado.')
    else:
        if senha == usuario_atual['senha']:
            print('Login efetuado com sucesso!')
        else:
            print('Senha incorreta!')









lista_usuarios = [{'usuario':'marcos','senha':'1234'}
    , {'usuario':'ana clara','senha':'567'},
                  {'usuario':'joao','senha':'2004'}]

pilha = []
#Cadastra caixas  com códigos de uma letra e 3 número

login(lista_usuarios)
'''
while True:
    menu()
    opcao = input("Digite a opção desejada: ")

    if opcao == '1':
        codigo = input('Digite o código da caixa: ')
        pilha.append(codigo)

    elif opcao == '2':
        print(pilha)
    elif opcao == '3':
        pilha.pop()
    elif opcao == '4':
        break
    else:
        print("\033[031mOpção inválida, tente novamente!\033[0m")

print("FIM DO PROGRAMA")'''









'''lista = [{'nome':'zé', 'idade':31}, {'nome':'maria', 'idade':30}]

nome = 'pedro'
esta_na_lista = False

for pessoa in lista:
    if pessoa['nome'] == nome:
        print("Pessoa está na lista")
        esta_na_lista = True

if not esta_na_lista:
    print("Pessoa não está na lista")




numeros = [1,2,3,4,5]
num = 7
esta_na_lista = False
for c in numeros:
    if c == num:
        print('Número está na lista')
        esta_na_lista = True

if esta_na_lista == False:
    print('O número não está na lista')


dicionario = {'nome':'zé', 'idade':31}

#print(dicionario['nome'])'''




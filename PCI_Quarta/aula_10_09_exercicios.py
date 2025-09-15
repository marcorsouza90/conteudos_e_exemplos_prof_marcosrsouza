################ EXERCÍCIOS ##########

##### Calculdora Simples

'''expressao = '7 / 2'

# separa os termos da expressão e converte os números
termos = expressao.split()
termos[0] = float(termos[0])
termos[-1] = float(termos[-1])

# implementação das operações

resultado = 0
a = termos[0]
b = termos[2]
validade = True

if termos[1] == '+':
    resultado = a + b
elif termos[1] == '-':
    resultado = a - b
elif termos[1] == '*':
    resultado = a * b
elif termos[1] == '/':
    resultado = a / b
elif termos[1] == '//':
    resultado = a//b
else:
    print('\033[31mOperação inválida!\033[0m')
    #validade = False


if validade == True:
    print(resultado)'''

####### Sistema de Login

'''lista = [1,2,3,4,5,6,7,8,49,6,3]
num = 6

for numero in lista:
    if numero == num:
        print('O número está na lista')
        break'''

lista = [{'nome_usuario':'marcos','senha':'1234'},
         {'nome_usuario':'joana','senha':'5678'},
         {'nome_usuario':'pedro','senha':'987'}]

usuario = input("Digite seu nome de usuário: ")
senha = input('Digite sua senha: ')

cadastrado = False

for item in lista:
    if item['nome_usuario'] == usuario:
        if item['senha'] == senha:
            print('Login efetuado com sucesso!')
            cadastrado = True
        break

if cadastrado == False:
    print("Usuário ou senha incorretos")








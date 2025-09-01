###### ESTRUTURAS DE DADOS ########

### LISTAS

'''lista_exemplo = [1, 2, 3, 4]
print(lista_exemplo)
lista_vazia = []
print(lista_vazia)'''

# referência a um elemento da lista: lista[<índice>]

''''lista_nomes = ["José", 'Maria', "Pedro"]
print(lista_nomes[2])'''

# listas são heterogêneas

'''lista_misturada = [5, 6.8, "Marcos", True]
print(lista_misturada)'''

#Listas são mutáveis
'''pessoas = ['Marcelo', 'César', 'Eline', 'Fernanda']
print(pessoas)

pessoas[2] = 'Elaine'

print(pessoas)'''

# Método .append(): insere um elemento no final da lista.

'''pessoas = ['Marcelo', 'César', 'Elaine', 'Fernanda']

pessoas.append("Vivian")

print(pessoas)

# Método .pop(índice): retira o elemento indicado
# da lista

pessoas.pop(1)
print(pessoas)

pessoas.pop() # --> retira o último item da lista.
print(pessoas)'''

### TUPLAS

'''numeros = (1, 2, 3, 4)
print(numeros)

letras = 'a', 'b', 'c'
print(letras)

print(letras[1])

tupla_misturada = "Olá", 2.5, True

print(tupla_misturada)

numeros[1] = 7'''

### DICIONÁRIOS

'''aluno ={'Nome': 'André', 'Idade': 24,
        'Curso': 'Mecânica'}
print(aluno)

# Acessar um elemento do dicionário:

print(aluno['Idade'])

# Mudar o valor de uma chave

aluno['Curso'] = 'Materiais'

print(aluno)

# Acrescentar chaves/valores ao dicionário

aluno['Cidade natal'] = 'Campinas'
print(aluno)

# Apagar elementos do dicionário

aluno.pop('Cidade natal')
print(aluno)'''

######## EXEMPLO DE FILA

## Programa que dê ao usuário as opções de:
# cadastar um nome em uma fila, consultar os nomes
# na fila, retirar (atender) alguém da fila e encerrar
# o programa.

fila = []

while True:
        print("PROGRAMA DE GERENCIAMENTO DE FILA")
        print('1 - Cadastrar um novo nome')
        print('2 - Consultar pessoas na fila ')
        print('3 - Retirar o próximo da fila (atendido)')
        print('4 - Encerrar programa')

        opcao = input("Digite uma opção: ")

        if opcao == '1':
                novo_nome = input('Digite o nome: ')
                fila.append(novo_nome)
        elif opcao == '2':
                print(fila)
        elif opcao == '3':
                fila.pop(0)
        elif opcao == '4':
                print('Programa Encerrado.')
                break













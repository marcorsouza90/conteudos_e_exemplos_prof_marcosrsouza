################ ESTRUTURA DE DADOS #############

### LISTAS

'''lista1 = [1,2,3]
print(lista1)
lista_heterogenea = [2, 'Olá', 2.5, False]
print(lista_heterogenea)
lista_vazia = []
print(lista_vazia)'''

'''nomes = ['Ana Clara', 'João Lucas', 'Carlos']

nomes[2] = 'Kauan'

print(nomes)
print(nomes[-1])

# len() retorna o tamanho de uma lista:
print(len(nomes))'''

##### Inserção e remoção de itens de uma lista

# .append(): método que
# insere elementos no final da lista

'''nomes = ['Ana Clara', 'João Lucas', 'kauan']

nomes.append('Mariana')
nomes.append("Carlos")
print(nomes)

# método .pop(indice) retira elementos da lista

nomes.pop(3)
print(nomes)

nomes.pop()

print(nomes)'''

### TUPLAS

'''nomes = ('João', 'Ana Clara', 'Kauan')
numeros = 1, 2, 3

print(nomes)
print(numeros)

# nomes[1] = "Mariana" --> Dá erro!

print(nomes[1])'''

### DICIONÁRIOS

'''aluno = {"Nome": 'João','Idade': 20, "Curso": 'Mecânica',
         'Cidade': 'Sanja'}

print(aluno['Cidade'])

aluno["Idade"] = 75
print(aluno)

aluno["Universidade"] = 'Unesp'

print(aluno)

aluno.pop("Universidade")

print(aluno)'''

### FILAS (FIFO)
# São estruturas onde o primeiro elemento a
# ser inserido é o primeiro a ser retirado.


#EXEMPLO: Programa que permita usuário cadastar
# nomes em uma fila,consultar nomes presentes na fila,
# retirar alguém da fila e ver quantas pessoas há na
# fila. O programa deve também dar uma opção de
# encerrar.

fila = []

while True:
    print('PROGRAMA DE GERENCIAMENTO DE FILA')
    print("1 - Cadastrar usuário na fila")
    print('2 - Consultar nomes da fila')
    print('3 - Retirar da fila (atendimento realizado)')
    print('4 - Encerrar programa')

    opcao = input('Digite a opção desejada: ')

    if opcao == '1':
        novo_nome = input('Digite o nome: ')
        fila.append(novo_nome)
    elif opcao == '2':
        #print(fila)
        for item in fila:
            print(item)

        print(f'Há {len(fila)} pessoas na fila.')
    elif opcao == '3':
        fila.pop(0)
    elif opcao == '4':
        print('FIM DO PROGRAMA')
        break
    else:
        print('Opçao inválida. Tente novamente!')












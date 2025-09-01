################### ESTRUTURAS DE DADOS ###################

###### VETORES ######

### Listas
# Listas são criadas usando colchetes
'''lista = [1,2,3]
print(lista)

lista_vazia = []
print(lista_vazia)'''

# É possível misturar variáveis diferentes na lista
'''lista_heterogenea = [2, 7, "Olá", 4.8, True]
print(lista_heterogenea)'''

# Para acessar um elemento da lista, usamos var[<índice]
'''print(lista_heterogenea[2])
print(lista_heterogenea[0])
print(lista_heterogenea[4])
print(lista_heterogenea[-1])'''

# Listas são mutáveis:

'''nomes = ['João', 'Maria', 'Pedro', 'Ana']
print(nomes)
nomes[1] = "Mariana"
print(nomes)'''

#Podemos obter o tamanho da lista utilizando len(lista)

'''print(len(nomes))'''

### Tuplas

'''tupla1 = (1,2,3)
tupla2 = "Olá", "Bom dia", 5

print(tupla1)
print(tupla2)
#print(type(tupla2))
print(tupla2[1])'''

#Tuplas são imutáveis
'''
tupla1[0] = 4  #---->  Dá erro!!!
'''
#### Dicionários

'''aluno = {"Nome": 'Guilherme', "Idade": 21, "RA": 2213087}

print(aluno['Idade'])

aluno['Idade'] = 47

print(aluno['Idade'])'''

# Acrescentendo informações no dicionário:
# var["nova chave"] = valor

'''aluno['Cidade'] = "Capivarlândia"

print(aluno)'''

### Filas (FIFO)

#fila inicial
'''fila = ['Alexandro', 'Ana Júlia','Diego']'''

# Adicionar elementos à fila com .append():

'''fila.append("Pedro")
fila.append('Marília')
print(fila)'''

# Retirar elementos da fila com .pop(0)

'''fila.pop(0)
fila.pop(0)

print(fila)'''

### Pilhas (LIFO)

pilha = ["O Alienista", "O Grande Sertão Veredas",
         "1984", "Cálculo Stewart"]
print(pilha)
# Inserindo elementos na pilha com .append()

pilha.append("Neuromancer")

print(pilha)

# Retirar elementos usando pop()

pilha.pop()
print(pilha)


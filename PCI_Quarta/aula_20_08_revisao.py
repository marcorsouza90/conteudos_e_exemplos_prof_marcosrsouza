######### ESTRUTURAS DE SELEÇÃO/CONTROLE/DECISÃO

### if, elif, else

# Programa que pega um valor de idade e avisa se
# a pessoa for maior de idade.

'''idade = 35
print(f'Sua idade é {idade}')

if idade >= 18:
    print("Você é maior de idade!")

print("Adeus")'''

# Dica: Use três aspas (simples ou duplas) para
# comentar um trecho inteiro de código.

### Programa que recebe a idade de um usuário
### e informa se ele é maior ou menor de idade.

"""idade = int(input("Digite sua idade: "))

print(f"Sua idade é {idade}")

if idade >= 18:
    print("Você é maior de idade!")
else:
    print("Você é menor de idade!")

print("Adeus!")"""

### Programa que lê a idade do usuário, informa se
### é maior ou menor de idade e acusa erro caso
### digite valor negativo.

"""idade = int(input("Digite um número: "))
print(f'Sua idade é {idade}.')

if idade >= 18:
    print("Você é maior de idade!")
elif idade >= 0 and idade < 18:
    print("Você é menor de idade!")
else:
    print("Você digitou uma idade inválida!")

print("Adeus!")"""

### Verificar se um número é divisível por 2 e por 3.

"""numero = 6

print(f'O número é {numero}')

if numero%2 == 0:
    print(f'{numero} é divisivel por 2.')
if numero%3 == 0:
    print(f'{numero} é divisível por 3.')"""

########################################

########## ESTRUTURAS DE REPETIÇÃO

### for

#Programa que imprime os números de 1 a 10.

"""for contador in range(1, 11):
    print('Olá')"""

###Programa que imprime os números desejados entre
### um valor inicial e um final, pulando de acordo
### com um passo escolhido.

"""inicial = 30
final = 10
passo = -2

for numero in range(inicial, final+1, -2):
    print(numero)"""

##### while

#Programa que imprime os números de 1 a 10.

"""contador = 1

while contador <= 10:
    print(contador)
    contador += 1"""

# Programa que recebe um número e só para quando
# o usuário digitar 0.

"""numero = 1

while numero != 0:
    numero = int(input("Digite um número: "))"""

# Programa que recebe um número e só para quando
# o usuário digitar 0, usando while True.

while True:
    numero = int(input("Digite um número: "))
    if numero == 0:
        break



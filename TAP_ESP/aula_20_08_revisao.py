#######  Revisão   ########

##### ESTRUTURAS DE SELEÇÃO

### Programa que informa se o usuário é maior de idade.

"""idade = 19

print(f'Sua idade é {idade} anos.')

#Se o if of utilizado sozinho (sem elif ou else), pode ser que toda
# a estrutura de seleção seja ignorada se a condição não for satisfeita.

if idade >= 18:
    print('Você é maior de idade.')


print("Até logo!")"""

### Programa que lê a idade do usuário e informa se ele é
### maior ou menor de idade.

"""idade = int(input("Digite sua idade: "))
print(f'Sua idade é {idade} anos.')

if idade >= 18:
    print('Você é maior de idade.')
else:
    print('Você é menor de idade.')

print("Até logo!")"""

### Programa que lê a idade de um usuário e informe
### se ele é maior ou menor de idade e se a idade
### é válida.

"""idade = int(input('Digite sua idade:'))
print(f'Você tem {idade} anos.')

if idade >= 18:
    print('Você é maior de idade.')
elif idade < 18 and 18 > 0:
    print('Você é menor de idade.')
else:
    print('Você digitou uma idade inválida.')

print("Até mais!")"""

### Programa que lê a idade e informa se o usuário
### é idoso

"""idade = int(input('Digite sua idade: '))

if idade >= 18:
    print('Você é maior de idade.')
if idade >= 60:
    print('Você é idoso.')

print('Adeus!')"""

##### ESTRUTURAS DE REPETIÇÃO

### for

## Programa que imprime todos os números de 1 a 10.

"""for numero in range(1, 11):
    print(numero, end=" ")"""

### Programa que imprime todos os números entre um
### valor inicial e um final escolhidos, e também o
### passo dessa repetição.

"""inicio = 50
fim = 30
passo = -1

for numero in range(inicio, fim+1,passo):
    print(numero, end=" ")"""

### while

# Programa que imprime os números de 1 a 10

"""numero = 1

while numero <= 10:
    print(numero)
    numero += 1"""

### Programa que lê um valor digitado
### e só para se o valor digitado for 0.

"""num = int(input('Digite um número: '))
while num != 0:
    num = int(input('Digite um número: '))

print("Adeus")"""

### Programa que lê um valor digitado
### e só para se o valor digitado for 0, usando
# while true.

while True:
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    print(numero * 2)

# O comando "break" quebra o laço mais interno
# que ele encontrar.









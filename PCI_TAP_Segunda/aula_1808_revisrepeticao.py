####### Laço for
###Programa que imprime os números de 1 até 10.

"""for num in range(1,11):
    print(2*num)"""

#programa que imprime o dobro dos números entre
# um valor inicial e um valor final fornecidos

"""inicial = 13
final = 27

for num in range(inicial,final + 1):
    print(2*num)"""

## programa que imprime os números entre um valor
# inicial e um final com um passo determinado.

"""inicial = 40
final = 10
passo = -2

for num in range(inicial, final, passo):
    print(num)"""

##### Laço While

## Programa que imprime os números de 1 à 10.

"""contador = 1

while contador <= 10:
    print(contador)
    contador += 1"""

### Programa que peça para o usuário digitar um
# Número inteiro e só pare quando ele digitar 0.

"""numero = int(input("Digite um número: "))

while numero != 0:
    numero = int(input("Digite outro número: "))"""

### Programa que peça para o usuário digitar um
# Número inteiro e só pare quando ele digitar 0. Porém,
# O programa também para se ele digitar 12.

numero = int(input("Digite número: "))

while numero != 0:
    if numero==12:
        print("Você digitou o número proibido!!!")
    numero = int(input("Digite outro valor:"))
    dobro = 2 * numero
    print(f'O dobro de {numero} é {dobro}')





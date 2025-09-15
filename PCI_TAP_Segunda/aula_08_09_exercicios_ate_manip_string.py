############ EXERCÍCIOS #######

### Programa que recebe valores digitados em ordem pelo usuário
# (em uma única entrada) e retorna a soma dos números pares.


'''numeros = '1 2 3 4 5 6 7 8 9 10'
#numeros = input("Digite dez números separados por espaços: ")

lista_numeros = numeros.split()
print(lista_numeros)

for numero in lista_numeros:
    numero = int(numero)
    if numero % 2 == 0:
        print(numero)'''


numeros = '1 2 3 4 5 6 7 8 9 10'
#numeros = input("Digite dez números separados por espaços: ")

lista_numeros = numeros.split()

lista_convertida = []

cor = '\033[35m'

for numero in lista_numeros:
    numero = int(numero)
    lista_convertida.append(numero)

print(f"{cor}OS NÚMEROS PARES SÃO:\033[0m")
for num in lista_convertida:
    if num % 2 == 0:
        print(num, end=' ')

print(f'\n{cor}OS NÚMEROS ÍMPARES SÃO:\033[0m')
for num in lista_convertida:
    if num % 2 != 0:
        print(num, end=' ')








### Exemplos do uso do if elif else

##Verificar se o usuário é maior de idade
# Um programa que pergunte ao usuário a idade e retorne
# como resultado um texto dizendo se ele é maior ou
# menor de idade e informando a idade.

"""idade = int(input('Digite sua idade: '))

if idade < 18:
    print(f'Sua idade é {idade}, portanto você é menor de idade!')
else:
    print(f'Sua idade é {idade}, portanto você é maior de idade!')"""

## programa que recebe um valor e identifica se
#ele é par ou ímpar.

"""numero = int(input('Digite um número: '))

#identificando se o numero é par ou ímpar

resto = numero % 2

if resto == 0:
    print(f'O número {numero} é par.')
else:
    print(f'O número {numero} é ímpar.')"""

#Programa que identifica se um aluno foi
# reprovado,aprovado ou ficou de exame.
# Critério: aluno é aprovado se tirar mais que 5,
# fica de exame se tirar entre 3 e 5 e é
# reprovado se tirar menos que 3.

"""nota = float(input("Digite sua nota: "))

if nota >= 5:
    print('Você foi aprovado!')
elif (nota < 5) and (nota >=3):
    print('Você ficou de exame!')
else:
    print("Você foi reprovado!")"""

# Utilizando o comando pass

#projeto de calculadora

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

operacao = input('Digite a operação desejada: ')

if operacao == "soma":
    print(num1 + num2)
if operacao == "subtração":
    pass
if operacao == "produto":
    print(num1 * num2)
print('Fim do programa')







#####   MANIPULAÇÃO DE STRINGS

### Indexação

frase = 'vejo Xuxa gritando que faz show sem playback'

#print(frase[5])

###  Fatiamento
# var[<início>:<final(excludente)>:passo]

'''print(frase[5:25])
print(frase[5:25:2])
print(frase[:24])
print(frase[7:])
print(frase[8::2])
print(frase[::3])
print(frase[::-1])
print(frase[25:2:-1])

registro_academico = 'RA221322965'
print(registro_academico[2:])
cpf ='123456789'
print(f'****{cpf[5:]}')'''

##### Métodos para strings
#vejo Xuxa gritando que faz show sem playback
print(frase)
#.upper() - passa todas as letras para maiúsculas
print(frase.upper())

#.lower() - passa todas as letras para minúsculas
print(frase.lower())

#.capitalize() - torna a primera letra maiúscula e o resto minúscula
print(frase.capitalize())

#.title() - coloca a primeira letra de cada palavra como maiúscula

print(frase.title())

# .strip() - retira espaços do início e
# final da string. Se passarmos uma string como
# argumento, ele retira todos os caracteres contidos
# nesse argumento da string desejada.

frase_espacada = "     Olá, tudo bem?    "
#print(frase_espacada.strip())

frase_maluca = '....,,,,***Olá, tudo bem?****,,,,....'
print(frase_maluca.strip(',*'))

# .lstrip() e r.strip()

print(frase_maluca.lstrip('.,*'))
print(frase_maluca.rstrip('.,*'))

# .find(sub) - retorna o índice da primeira ocorrência
# da substring "sub" na string desejada. Caso não exista,
# retorna -1.

print(frase.find('Xuxa'))
print(frase.find('f'))
print(frase.find('8'))

#.count(sub) - conta o número de ocorrências da
# substring "sub" na string desejada.

print(frase.count('a'))
print(frase.count('Xuxa'))
print(frase.count('2'))

frase_ola = "Bom dia,olá a todos! Espero que todos tenham um bom dia hoje."

print(frase_ola.count("bom"))
print(frase_ola.lower().count("bom"))

# .replace(velha,nova) - em uma string, troca as ocorrências
# da substring "velha" pela "nova"

print(frase.replace('Xuxa','Eliana'))
print(frase.replace('a','*'))
print(frase.replace('gritando','#*$&#'))

# .split(separador) - separa as partes de uma string
# de acordo com o separador e coloca em uma lista.
# por padrão, o separados são espaços

print(frase.split())
print(frase.split("Xuxa"))

#'separador'.join(iteravel) - junta os elementos de um iterável
#(lista, tupla) em uma única string, usando a string
#que chama o método como separador

lista = ['Olá', 'bom', 'dia','como', 'vai']
frase_junta =' '.join(lista)
print(frase_junta)
frase_junta ='/'.join(lista)
print(frase_junta)

######## Operações com strings

# Concatenação - justapõe strings usando +
palavra_concatenada = 'Olá'+ ' ' + "Bom dia"
print(palavra_concatenada)

# Repetição - repete uma string usando
# <quantidade> * string


print(10*'Olá')
titulo = 'PROGRAMA DE GERENCIAMENTO DE FILA'


print('='*len(titulo))
print(titulo)
print('='*len(titulo))


######## COR DA STRING (ANSI)

# Para mudarmos as cores de uma string usando o esquema
# das cores ANSI, utilizamos, antes da string
# o código '\033[<código>m'. A cor padrão (e que pode
# ser utilizada para interromper a mudança de cor)
# '\033[0m'

frase_colorida = '\033[31mOlá, boa noite!\033[0m'

print(frase_colorida)

print(f'Olha só que doidera! \033[36m{frase}\033[0m')



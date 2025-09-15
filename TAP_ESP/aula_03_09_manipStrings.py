####### Manipulação de Strings #######

### Indexação e Fatiamento

frase = "vejo Xuxa gritando que fez show sem playback"

#print(frase[5])

# Fatiamento
# string[início:fim (excludente):passo]

'''print(frase[6:30])
print(frase[2:35:2])
print(frase[:25])
print(frase[5::2])
print(frase[::3])
print(frase[25:3:-1])
print(frase[::-1])

numero = '0,3759'
print(numero[:3])'''

#### Principais Métodos para Strings
#vejo Xuxa gritando que fez show sem playback
'''
# .upper() - passa as letras para maiúsculas
print(frase.upper())

# .lower() - passa as letras para minúsculas
print(frase.lower())

# .capitalize() - deixa a primeira letra maiúscula
print(frase.capitalize())

# .title() - coloca todas as palavras com inicial maiúscula
print(frase.title())

# .strip() - retira espaços no início e final da string.
# pode retirar outros caracteres se passarmos estes caracteres
# como parâmetro opcional.

texto_espacos = "    Olá, bom dia a todos!    "
print(texto_espacos)

string_maluca =',,,,,....;;;;Olá bom dia;;;;...,,,,'
print(string_maluca.strip(',;'))

# .lstrip() e .rstrip()- semelhante ao .strip(), mas
# lstrip() só retira o que está no início e rstrip() só
#retira o que está no final.

print(string_maluca.lstrip(',.;'))
print(string_maluca.rstrip(',.;'))

#.find(sub) - indica a posição da substring sub na
# string desejada. Se não houver, retorna -1.

print(frase.find("Xuxa"))
print(frase.find("5"))

# .count(sub) - conta o número de ocorrências da substring
# sub dentro da string desejada.

print(frase.lower().count('x'))

# replace(velho, novo) - substitui, na string desejada,
# a substring velho por novo

print(frase.replace("Xuxa","Eliana"))
print(frase.replace('a','#'))
print(frase.replace('gritando', '$%#$'))

# .split(string)

print(frase.split())
endereco = 'www.essesite.com.br'
print(endereco.split('.'))

#separador.join(iteravel) - junta os elementos de um iterável
# (tupla, lista, etc...) em uma única string, usando
# a string que chama o método como separador.

lista_frase = ['Bom dia','João',"como", 'está']
frase_junta = ' '.join(lista_frase)
print(frase_junta)
endereco_pasta = ['C:','Meus Documentos','Downloads']
endereco_pasta_junto = '/'.join(endereco_pasta)
print(endereco_pasta_junto)'''

### Operações com Strings

#Concatenação - justapor substrings usando +

frase_completa = 'Olá' + ' ' + 'bom dia' + '!'
print(frase_completa)

# Repetição - repete uma string usando quantidade*string

'''frase_repetida = 5*'Olá '
print(frase_repetida)
titulo= 'PROGRAMA'
print(len(titulo)*'=')
print(titulo)
print(len(titulo)*'=')'''

#### Cores usando ANSI
# é possível alterar cores das letras usando a formula
# '\033[<código>m' antes da string,e para  voltar à cor padrão,
# coloca-se '\033[0m'

print("\033[31mPalavra")
print("\033[32mPalavra")
print("\033[41mPalavra\033[0m")
print("\033[37m\033[46mPalavra\033[0m")

vermelho = '\033[31m'
print(f'{vermelho}Palavra')













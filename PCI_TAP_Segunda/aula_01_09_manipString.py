######## MANIPULAÇÃO DE STRING

#Observação sobre strings - são imutáveis

####### INDEXÇÃO E FATIAMENTO

### String são indexadas com índices inteiros de 0 até
# o tamanho da string (menos 1). Por tamanho nos referimos
# à quantidade de caracteres.

'''palavra_um = 'Pássaro'
print(palavra_um[2])
palavra_dois = "74938$%$83"
print(palavra_dois[-2])'''

#### Fatiamento
# string[início, fim, passo]

frase = 'vejo xuxa gritando que fez show sem playback'

'''print(frase)
print(frase[15])
print(frase[5:20])
print(frase[:25])
print(frase[12:])
print(frase[2:25:2])
print(frase[::3])
print(frase[28:5:-1])
print(frase[::-1])'''

#### PRINCIPAIS MÉTODOS DE STRING

# .upper() - converte tudo para maísculas
#print(frase.upper())

# .lower() - converte tudo para minúscalas
#print(frase.lower())

# .capitalize() - coloca a primeira letra como maiúscula
#print(frase.capitalize())

#.title() - coloca a primeira letra de cada palavra como maiúscula.
#print(frase.title())

# .strip() - remove espaços no início/fim
# ou remove as strings passadas como parâmetro
# do início e fim da string

'''frase_espacada = "     Olá mundo!     "
print(frase_espacada)
print(frase_espacada.strip())

string_doida = ',,,,,....bbbbrrrrwwwt....,,,,,'
print(string_doida.strip(',.br'))'''

#.lstrip() e .rstrip() funcionam com o strip(), mas
# só para um lado

'''print(string_doida.lstrip(',.'))
print(string_doida.rstrip(',.'))'''

# .find(sub) retorna a posição da primeira
# ocorrência da substring sub na string desejada. Se
# não houver, retorna -1
'''print(frase)
print(frase.find('xuxa'))
print(frase.find('2'))'''

# .count(sub) - conta quantas vezes a substring sub
# aparece na string desejada.

'''print(frase)
print(frase.count('x'))
print(frase.count('w'))
print(frase.count('xuxa'))'''

# .replace(velha, nova) - substitui todas as ocorrências
# da substring <velha> pela substring <nova> na
# string desejada.
'''print(frase)
print(frase.replace('xuxa', 'Eliana'))

frase_hashtag = frase.replace('a','#')
print(frase_hashtag)

frase_censurada = frase.replace('gritando','****')

print(frase_censurada)'''

#.split(separador) - separa as substrings da string desejada
# inserindo-as em elementos de uma lista, usando o
# <separador>. Por padrão, os separadores são espaços
# vazios.

'''print(frase.split())
print(frase.split('xuxa'))

lista_aprovados = "Marcos - José - Pedro - Maria"
lista_aprovados = lista_aprovados.split(' - ')
print(lista_aprovados)'''

# separador.join(iteravel) - junta os elementos de um iterável
# (como uma lista ou tupla) em uma única string, usando
# <separador> como separador.

'''lista_aprovados = ["Cecília", 'Elizandra', 'Patrícia', 'Ricardo']

texto_edital = ' - '.join(lista_aprovados)
print(texto_edital)'''

##### OPERAÇÕES COM STRINGS

# (+) Concatenação - junta strings em uma só.

'''frase_concatenada = 'Olá' +' ' + 'tudo' + 'bem' + 'como' + 'está'
print(frase_concatenada)'''

# (*) Repetição - repete a string o número de vezes
# indicado na 'multiplicação'

'''palavra = 20*'OLá'
print(palavra)'''

####### COR DA STRING

# É possível mudar as cores das letras para um esquema
# simples de cores da codificação ANSI. Fazemos isso
# utilizando '\033[<código>m'. para restaurar a cor
# padrão, utilizamos '\033[0m'.

'''print(frase)
print(f'\033[31m{frase}')
print('\033[32mOlá, bom dia!')
print('\033[45mOlá, tudo bem?')
print('\033[45mOlá, tudo bem?\033[0m')
print('\033[44m\033[37mOlá, boa tarde.\033[0m Como vai?')'''


















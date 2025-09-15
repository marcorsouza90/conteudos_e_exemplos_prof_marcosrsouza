#### Programa que permite ao usuário
# cadastrar pessoas em uma fila, retirá-las,
# consultar quem ainda está na fila e encerrar
# o programa.

### Melhorias: criar filas separadas para
# cada profissional

####### PROGRAMA DE ATENDIMENTO CLÍNICA FEG

pessoas = []

while True:
    print("Programa de Gerenciamento de Fila Clínica FEG")

    print('1 - Cadastrar nova pessoa na fila')
    print('2 - Retirar próximo usuário da fila (atendido)')
    print('3 - Consultar pessoas presentes na fila')
    print('4 - Encerrar programa')

    opcao = input("Digite a opção desejada: ")

    if opcao == '1':
        nome = input("Digite o nome do paciente: ")
        pessoas.append(nome)
    elif opcao == '2':
        print(f'Paciente {pessoas[0]} concluiu o atendimento.')
        pessoas.pop(0)
    elif opcao == '3':
        print("Os seguintes pacientes ainda não foram atendidos:")
        for paciente in pessoas:
            print(paciente)
        #print(pessoas)
    elif opcao == '4':
        print("PROGRAMA ENCERRADO.")
        break
    else:
        print("Opção Inválida. Tente novamente.")











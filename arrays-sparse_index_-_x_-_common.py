#!/usr/bin/python3
# -*- coding: utf-8 -*-

# - - - - - - - - - - - - - - [ Bloco de Importar Bibliotecas (libs) ] - - - - - - - - - - - - - - #

try:
    import os
    from datetime import datetime, timedelta
    import sys
    import time
    import random

except Exception as E:
    print('Erro ao Importar Bibliotecas: ' + E)


# - - - - - - - - - - - - - - [ Bloco de Definicao de Variaveis (1o) ] - - - - - - - - - - - - - - #

# [ Define as Variaveis ]
try:
    # Cria os arrays 1 e 2 com numeros aleatorios
    array1 = [random.randint(100000, 1000000) for p in range(0, 1000000)]
    array2 = [random.randint(100000, 1000000) for p in range(0, 100000)]

    # Cria o array 3 que guardara os Indices dos numeros do array 2
    array3 = {}

except Exception as E:
    print('Erro ao Definir as Variaveis: ' + E)


# - - - - - - - - - - - - - - [ Bloco de Execucao (2o) ] - - - - - - - - - - - - - - #

# [ Conta os numeros em comum entre os arrays 1 e 2 utilizando o metodo Comum ]
try:
    count = 0

    print(str(datetime.now()) + ' Tempo Inicial metodo Comum')  # Inicio Comum

    # Efetua a contagem
    for i in range(0, len(array1)):
        if array1[i] in array2:
            count += 1

    print(str(datetime.now()) + ' Tempo Final metodo Comum')  # Fim Comum
    print('Count Metodo Comum: ' + str(count))

except Exception as E:
    print('Erro ao Executar a contagem utilizando o metodo Comum: ' + E)



print('\n\n\n')



# [ Conta os numeros em comum entre os arrays 1 e 2 utilizando o metodo Indexado ]
try:
    # Cria os indices dos numeros do Array 2 no Array 3 para utilizar o metodo Indexado
    print(str(datetime.now()) + ' Tempo Inicial Indexacao previa')  # Inicio Indexacao

    for ncontrato in array2:
        array3[str(ncontrato)] = '0'

    print(str(datetime.now()) + ' Tempo Final Indexacao previa')  # Fim Indexacao
    print('Len Array3: ' + str(len(array3)))


    print('\n')

    count = 0

    print(str(datetime.now()) + ' Tempo Inicial metodo Indexado')  # Inicio Indexado

    # Efetua a contagem
    for contrato in array1:
        if array3.get(str(contrato)) == '0':
            count += 1

    print(str(datetime.now()) + ' Tempo Final metodo Indexado')  # Fim Indexado
    print('Count Metodo Indexado: ' + str(count))

except Exception as E:
    print('Erro ao Executar a contagem utilizando o metodo Indexado: ' + E)

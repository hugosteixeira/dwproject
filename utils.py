import os
import sys
from traceback import print_tb, extract_tb, format_list
import unicodedata
import re

def printError():
    error = sys.exc_info()
    typeError = error[0]#tipo do erro
    print('\n'+'Type: \n'+str(typeError)+'\n')
    value = error[1] # valor do erro
    print('Value: \n'+str(error[1])+'\n')
    tb=error[2]
    print('Traceback:')
    e_tb=extract_tb(tb)
    f_l=format_list(e_tb)#traceback em forma de lista para futuro usos
    print_tb(tb)
    return typeError, value, tb, f_l

def tratarValuesDao(lista):
    resultado = ''
    for x in range(len(lista)):
        if x == len(lista)-1:
            resultado = resultado + str(lista[x]) + ''
        else:
            resultado = resultado + str(lista[x]) + "', '"
    return resultado

def tratarColumnsDao(lista):
    resultado = ''
    for x in lista:
        if x == lista[-1]:
            resultado = resultado + x + ''
        else:
            resultado = resultado + x + ","
    return resultado


def limparTexto(palavra):

    # Unicode normalize transforma um caracter em seu equivalente em latin.
    nfkd = unicodedata.normalize('NFKD', palavra)
    palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])

    # Usa expressão regular para retornar a palavra apenas com números, letras e espaço
    return re.sub('[^a-zA-Z0-9 \\\]', '', palavraSemAcento)
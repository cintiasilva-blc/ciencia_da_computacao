from TADLista_D import *

'''Escreva uma fun ̧c ̃ao que receba, como parˆametros, um arranjo A com n elementos e construa
uma lista encadeada com os n elementos do vetor. Se n=0 a fun ̧c ̃ao deve retornar uma lista
vazia. Exemplo: Se o vetor dado for A=[5, 9, 4, 6, 2, 7] a fun ̧c ̃ao deve retornar uma lista onde
o primeiro elemento  ́e 5, o segundo  ́e 9 ... e o  ́ultimo  ́e 7.
'''

def constroi_lista(array: list) -> lista:
    '''
    Exemplos:
    >>> A=[5, 9, 4, 6, 2, 7]
    >>> constroi_lista(A)
    [item(5), item(9), item(4), item(6), item(2), item(7)]
    '''

    n = len(array)

    if n == 0:
        return lista.vazia()
    else:
        novo = no(array[0])
        


        
            





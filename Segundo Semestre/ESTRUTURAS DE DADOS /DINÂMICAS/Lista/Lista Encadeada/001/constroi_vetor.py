from TADLista_encadeada import *

'''Escreva uma fun ̧c ̃ao que receba, como parˆametros, um arranjo A com n elementos e construa
uma lista encadeada com os n elementos do vetor. Se n=0 a fun ̧c ̃ao deve retornar uma lista
vazia. Exemplo: Se o vetor dado for A=[5, 9, 4, 6, 2, 7] a fun ̧c ̃ao deve retornar uma lista onde
o primeiro elemento  ́e 5, o segundo  ́e 9 ... e o  ́ultimo  ́e 7.'''

def constroi_lista(array: list[int]) -> Lista:
    '''Recebe como parâmetro um arranjo e retorna uma lista encadeada comseus elementos
    
    Exemplos:
    >>> A=[5, 9, 4, 6, 2, 7]
    >>> constroi_lista(A)

    '''

    if len(array) == 0:
        return None
    else:
        novo = no(array[0])
        

if __name__ == '__main__':
    import doctest
    doctest.testmod()
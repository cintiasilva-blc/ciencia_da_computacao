''' Considere uma fila com v ́arios elementos num ́ericos. Liste apenas os elementos pares desta fila.'''

from TADFila_circ import *

def pares(f: fila):
    '''Mostra apenas os elementos pares da fila *f*
    
    Exemplos:
    >>> f = fila(3)
    >>> f.enfileira(item(1))
    >>> f.enfileira(item(2))
    >>> f.enfileira(item(3))
    >>> pares(f)
    Elemento:  2
    '''

    aux = fila(f.tamanho)

    while not f.vazia():
        elemento = f.obtem_primeiro()
        f.desenfileira()
        if elemento.valor % 2 == 0:
            aux.enfileira(elemento)

    while not aux.vazia():
        elemento = aux.obtem_primeiro()
        aux.desenfileira()
        print('Elemento: ', elemento.valor)

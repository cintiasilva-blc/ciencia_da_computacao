'''A paritr de uma lista encadeada l1 gere uma segunda lista l2 com os elementos na ordem inversa(a l1 permanesce com seus elementos originais)'''
from TADLista_encadeada import *

def mostra_lista(l: lista) -> str:
    '''
    Exemplos:
    >>> l = lista()
    >>> A = [1, 5, 4, 3]
    >>> for i in A:
    ...     l.insere_fim(item(i))
    True
    True
    True
    True
    >>> mostra_lista(l)
    '[1, 5, 4, 3]'
    '''
    
    ptr = l.primeiro
    result = '['

    while ptr != None:
        result += str(ptr.dado.valor)
        if ptr.prox != None:
            result += ', '
        ptr = ptr.prox
    result += ']'
    return result

def lista_inversa(l1: lista) -> lista:
    ''' A paritr de uma lista encadeada l1 gere uma segunda lista l2 com os elementos na ordem inversa(a l1 permanesce com seus elementos originais)

    Exemplos:
    >>> l1 = lista()
    >>> A = [1, 5, 4, 3]
    >>> for i in A:
    ...     l1.insere_ini(item(i))
    True
    True
    True
    True
    >>> x = lista_inversa(l1)
    >>> mostra_lista(x)
    '[3, 4, 5, 1]'
    '''

    l2 = lista()
    ptr = l1.primeiro
    while ptr != None:
        x = deepcopy(ptr)
        l2.insere_ini(x)
        ptr = ptr.prox
    return l2

if __name__ == "__main__":
    import doctest
    doctest.testmod()
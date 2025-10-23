from TADLista_D import *



def conta_celulas(l: lista) -> int:
    '''Conta o numero de celulas da lista encadeada.
    
    Exemplos:
    >>> l = lista()
    >>> conta_celulas(l)
    0
    >>> l.insere_ini(item(2))
    >>> l.insere_ini(item(1))
    >>> l.insere_ini(item(3))
    >>> l.insere_ini(item(6))
    >>> conta_celulas(l)
    4
    '''

    if l.vazia():
        return 0
    ''
    
    





if __name__ == '__main__':
    import doctest
    doctest.testmod()





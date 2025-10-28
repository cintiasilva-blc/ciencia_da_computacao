from TADPilha import *

def inverte_pilha(p: pilha):
    '''Recebe como parâmetro uma pilha e modifica a pilha invertendo a ordem dos
    seus elementos. 

    Exemplos:
    >>> p = pilha(4)
    >>> p.empilha(item(1))
    >>> p.empilha(item(9))
    >>> p.empilha(item(2))
    >>> p.empilha(item(7))
    >>> inverte_pilha(p)
    >>> p.desempilha()
    1
    >>> p.desempilha()
    9
    >>> p.desempilha()
    2
    '''
    aux = pilha(p.tam_max)
    aux2 = pilha(p.tam_max)

    while not p.vazia():
        elemento: item = p.consulta_topo()
        aux.empilha(elemento)
        p.desempilha()

    while not aux.vazia():
        elemento: item = aux.consulta_topo()
        aux2.empilha(elemento)
        aux.desempilha()
    
    while not aux2.vazia():
        elemento: item = aux2.consulta_topo()
        p.empilha(elemento)
        aux2.desempilha()

if __name__ == '__main__':
    import doctest
    doctest.testmod()
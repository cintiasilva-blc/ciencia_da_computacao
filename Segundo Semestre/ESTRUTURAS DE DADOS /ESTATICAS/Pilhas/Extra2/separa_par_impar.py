from TADPilha import *

def imprime_pilha(p1: pilha):
    '''Imprime os elementos de uma pilha na mesma ordem em que eles foram empilhados.
    
    Exemplos:
    >>> p1 = pilha(5)
    >>> p1.empilha(5)
    >>> p1.empilha(2)
    >>> p1.empilha(1)
    >>> imprime_pilha(p1)
    Elemento:  5
    Elemento:  2
    Elemento:  1
    '''

    p_aux = pilha(p1.tam_max)

    while not p1.vazia():
        elemento: item = p1.consulta_topo()
        p1.desempilha()
        p_aux.empilha(elemento)
        
    while not p_aux.vazia():
        elemento: item = p_aux.consulta_topo()
        p_aux.desempilha()
        print("Elemento: ", elemento.valor)
        p1.empilha(elemento)

def separa_impar(p1: pilha):
    '''
    
    Exemplos:
    >>> p1 = pilha(10)
    >>> for i in range(1, 11):
    ...     p1.empilha(item(i))
    >>> imprime_pilha(p1)
    Elemento:  1
    Elemento:  2
    Elemento:  3
    Elemento:  4
    Elemento:  5
    Elemento:  6
    Elemento:  7
    Elemento:  8
    Elemento:  9
    Elemento:  10
    >>> separa_impar(p1)
    >>> imprime_pilha(p1)
    Elemento:  1
    Elemento:  3
    Elemento:  5
    Elemento:  7
    Elemento:  9
    '''

    impares = pilha(p1.tam_max)
    while not p1.vazia():
        elemento = p1.consulta_topo()
        if elemento.valor % 2 != 0:
            impares.empilha(elemento)
        p1.desempilha()

    while not impares.vazia():
        elemento = impares.consulta_topo()
        p1.empilha(elemento)
        impares.desempilha()



if __name__ == '__main__':
    import doctest
    doctest.testmod()
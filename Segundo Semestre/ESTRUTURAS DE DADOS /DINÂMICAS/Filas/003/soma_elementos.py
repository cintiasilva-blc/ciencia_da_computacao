from TADFila_D import *
from TADPilha_D import *

def soma_elementos(f: fila) -> int:
    '''Recebe uma fila e soma todos os seus elementos
    
    Exemplos:
    >>> f = fila()
    >>> f.enfileira(item(1))
    >>> f.enfileira(item(2))
    >>> f.enfileira(item(3))
    >>> soma_elementos(f)
    6
    >>> f.desenfileira()
    >>> f.desenfileira()
    >>> soma_elementos(f)
    1
    '''
    soma = 0
    aux = pilha()
    while not f.vazia():
        elemento = f.obtem_primeiro()
        aux.empilha(item(elemento))
        f.desenfileira()
        soma += elemento

    while not aux.vazia():
        elemento = aux.elemento_topo()
        aux.desempilha()
        f.enfileira(item(elemento))

    return soma
    

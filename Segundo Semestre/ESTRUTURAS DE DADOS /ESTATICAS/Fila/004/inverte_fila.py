'''Escreva uma funcao em Python que inverta os elementos de uma fila, usando uma pilha como
estrutura auxiliar.'''

from TADFila_circ import *
from TADPilha import *

def inverte_fila(f: fila):
    '''Inverte os elementos da fila
    
    Exemplos:
    >>> f = fila(10)
    >>> f.enfileira(item(2))
    >>> f.enfileira(item(1))
    >>> f.enfileira(item(0))
    >>> f.enfileira(item(6))
    >>> inverte_fila(f)
    >>> mostra_fila(f)
    Elemento:  6
    Elemento:  0
    Elemento:  1
    Elemento:  2
    '''

    aux = pilha(f.tamanho)

    while not f.vazia():
        elemento = f.obtem_primeiro()
        f.desenfileira()
        aux.empilha(elemento)

    while not aux.vazia():
        elemento = aux.consulta_topo()
        aux.desempilha()
        f.enfileira(elemento)

def mostra_fila(f: fila):
    while not f.vazia():
        elemento = f.obtem_primeiro()
        f.desenfileira()
        print("Elemento: ", elemento.valor)



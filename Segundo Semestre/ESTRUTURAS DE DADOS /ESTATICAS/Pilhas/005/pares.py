'''5. Considere uma pilha com v ́arios elementos num ́ericos. Liste apenas os elementos pares desta
pilha.'''

from TADPilha import *

def lista_pares(p: pilha):
    '''Recebe uma pilha e mostra os numeros pares presentes nela.
    
    Exemplos:
    >>> p = pilha(4)
    >>> p.empilha(1)
    >>> p.empilha(2)
    >>> p.empilha(4)
    >>> p.empilha(5)
    >>> lista_pares(p)
    Elemento:  2
    Elemento:  4
    '''

    aux = pilha(p.tam_max)

    while not p.vazia():
        elemento = p.consulta_topo()
        p.desempilha()
        if elemento % 2 == 0:
            aux.empilha(elemento)
            
    while not aux.vazia():
        elemento = aux.consulta_topo()
        aux.desempilha()
        print('Elemento: ', elemento)



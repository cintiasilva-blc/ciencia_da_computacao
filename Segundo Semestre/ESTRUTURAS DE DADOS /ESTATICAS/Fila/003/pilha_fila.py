'''Considere a estrutura de uma fila e uma pilha. Fa ̧ca uma fun ̧c ̃ao que receba um valor. Se o
valor for positivo, insira na pilha. Caso contr ́ario, insira na fila.'''

from TADPilha import *
from TADFila_circ import *

p = pilha(20)
f = fila(20)

def preenche():
    valores = [1, 9, -3, 4, -2]
    for i in valores:
        separa_pos_neg(i)

def mostra_pilha(p1: pilha):
    while not p.vazia():
        elemento = p.consulta_topo()
        p.desempilha()
        print('Elemento: ', elemento.valor)

def mostra_fila(f: fila):
    while not f.vazia():
        elemento = f.obtem_primeiro()
        f.desenfileira()
        print("Elemento: ", elemento.valor)

def separa_pos_neg(num: int):
    '''Recebe um numero *num*, se esse valor for positivo é alocado em uma pilha, caso contrario em uma fila
    
    Exemplos:
    >>> preenche()
    >>> mostra_pilha(p)
    Elemento:  4
    Elemento:  9
    Elemento:  1
    >>> mostra_fila(f)
    Elemento:  -3
    Elemento:  -2
    '''

    if num >= 0:
        p.empilha(item(num))
    else:
        f.enfileira(item(num))

if __name__ == '__main__':
    import doctest
    doctest.testmod()


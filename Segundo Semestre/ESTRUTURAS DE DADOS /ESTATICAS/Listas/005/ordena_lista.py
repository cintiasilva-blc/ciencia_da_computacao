from TADLista import *

def ordena_lista(l1: lista, l2: lista) -> lista:
    '''Recebe duas listas ordenadas e retorna uma terceira lista gerada a partir da intercalação das outras duas, também ordenada.
    
    Exemplos:
    >>> l1 = lista(5)
    >>> l2 = lista(5)
    >>> l1.insere_ord(item(1))
    True
    >>> l1.insere_ord(item(3))
    True
    >>> l1.insere_ord(item(5))
    True
    >>> l2.insere_ord(item(2))
    True
    >>> l2.insere_ord(item(4))
    True
    >>> l2.insere_ord(item(6))
    True
    >>> ordena_lista(l1, l2)
    [item(valor=1), item(valor=2), item(valor=3), item(valor=4), item(valor=5), item(valor=6)]
    '''

    l3 = lista(l1.tam_max + l2.tam_max)
    for i in range(l1.fim):
        l3.insere_ord(l1.elementos[i])
    for i in range(l2.fim):
        l3.insere_ord(l2.elementos[i])

    return l3.elementos[:l3.fim]



    

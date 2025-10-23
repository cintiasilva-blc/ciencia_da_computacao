from TADPilha import *

def preenche(p: pilha):
    valores = [9, 8, 3, 1, 7, 4]
    for v in valores:
        p.empilha(item(v))

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

def main():
    p = pilha(10)
    preenche(p)
    imprime_pilha(p)



if __name__ == "__main__":
    main()


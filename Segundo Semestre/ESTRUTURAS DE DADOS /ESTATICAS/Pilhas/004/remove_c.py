'''Utilizando somente opera ̧c ̃oes de empilhar e desempilhar, escreva uma fun ̧c ̃ao que remove um
item com chave c fornecida pelo usu ́ario da pilha. Ao final da execu ̧c ̃ao da fun ̧c ̃ao, a pilha deve
ser igual `a original, exceto pela ausˆencia do item removido.'''

from TADPilha import *

def remove_itemC(p: pilha, c: int):

    p2 = pilha(p.tam_max)
    removido = False

    while not p.vazia():
        n = p.desempilha()
        if n == c and not removido:
            removido = True     
        else:
            p2.empilha(n)
 
    while not p2.vazia():
        m = p2.desempilha()
        p.empilha(m)





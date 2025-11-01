'''4. Fa ̧ca uma fun ̧c ̃ao que fa ̧ca a troca de posi ̧c ̃ao de dois elementos de uma lista. O retorno da
fun ̧c ̃ao deve ser se a troca foi realizada com sucesso ou n ̃ao. Considere que exista uma  ́unica
ocorrˆencia dos dois elementos informados para a troca.'''

from TADLista import *

def troca_pos(l: lista, x1: item, x2: item) -> bool:
    '''Recebe uma lista, troca a posição de dois elementos entre si, se a troca for realizada retorna True, caso contrário retorna False.
    
    Exemplos:
    >>> l = lista(4)
    >>> l.insere_fim(item(8))
    True
    >>> l.insere_fim(item(5))
    True
    >>> l.insere_fim(item(7))
    True
    >>> l.insere_fim(item(9))
    True
    >>> troca_pos(l, item(8), item(5))
    True
    >>> troca_pos(l, item(8), item(4))
    False
    '''

    pos1 = l.busca(x1.valor)
    pos2 = l.busca(x2.valor)

    if pos1 != -1 and pos2 != -1:
        aux = l.elementos[pos1]
        l.elementos[pos1] = l.elementos[pos2]
        l.elementos[pos2] = aux
        return True
    return False



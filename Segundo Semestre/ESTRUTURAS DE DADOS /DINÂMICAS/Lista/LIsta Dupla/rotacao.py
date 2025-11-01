from TADLista_duplaD import *

'''Escreva uma função que receba uma lista duplamente encadeada e rotacione a lista para a direita e esquerda, tantas vezes quanto for o valor de um inteiro n passado como parâmetro. Se o inteiro n for positivo a lista deve ser rotacionada n vezes para a direita e se for negativompara a esquerda.'''

def rotacao(self, n: int) -> None:
    '''Move todos os elementos *n* posições para a direita (se *n* positivo) ou
    para a esquerda (se *n* negativo).

    Exemplo:
    >>> l1 = ListaDupla()
    >>> l1.insere_fim(1)
    >>> l1.insere_fim(2)
    >>> l1.insere_fim(3)
    >>> l1.insere_fim(4)
    >>> l1.insere_fim(5)
    >>> mostra(l1)
    [1, 2, 3, 4, 5]
    >>> l1.rotacao(2)
    >>> mostra(l1)
    [4, 5, 1, 2, 3]
    >>> l1.rotacao(-1)
    >>> mostra(l1)
    [5, 1, 2, 3, 4]
    '''




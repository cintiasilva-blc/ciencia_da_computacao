from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class item:
    valor: int | None

class pilha:
    def __init__(self, tam_max: int):
        self.elementos: list[item] = [item(None)] * tam_max
        self.tam_max = tam_max
        self.topo = 0

    def vazia(self) -> bool:
        '''Veririca se uma pilha está vazia e retorna True ou False
        Exemplo:
        >>> p1 = pilha(5)
        >>> p1.vazia()
        True
        >>> p1.empilha(item(2))
        >>> p1.vazia()
        False'''
        return self.topo == 0
    
    def cheia(self) -> bool:
        '''Verifica se uma pilha está cheia, ou seja se atingiu
        o tam_max definido na sua criação e retorna
        True ou False
        Exemplo:
        >>> p1 = pilha(2)
        >>> p1.cheia()
        False
        >>> p1.empilha(item(3))
        >>> p1.empilha(item(1))
        >>> p1.cheia()
        True'''
        return self.topo == self.tam_max

    def empilha(self, x: item):
        '''Insere item *x* no topo da pilha
        Exemplos:
        >>> p1 = pilha(5)
        >>> p1.empilha(item(4))
        >>> x: int = p1.consulta_topo().valor
        >>> x
        4
        '''
        if self.cheia():
            raise ValueError('Pilha Cheia')
        else:
            self.elementos[self.topo] = deepcopy(x)
            self.topo += 1
    
    def desempilha(self):
        '''Remove o item que estiver no topo da pilha
        Exemplos:
        >>> p1 = pilha(5)
        >>> p1.empilha(item(2))
        >>> p1.empilha(item(7))
        >>> p1.desempilha()
        >>> x: int = p1.consulta_topo().valor
        >>> x
        2
        '''
        if self.vazia():
            raise ValueError('Pilha Vazia')
        else:
            self.topo -= 1
            
    def consulta_topo(self) -> item:
        '''Retorna qual o item que está no topo da pilha
        OBS: o item não é desempilhado, apenas consultado
        Exemplos:
        >>> p1 = pilha(5)
        >>> p1.empilha(item(2))
        >>> p1.empilha(item(7))
        >>> n: int = p1.consulta_topo().valor
        >>> n
        7'''
        if self.vazia():
            raise ValueError('Pilha Vazia')
        else:
            return deepcopy(self.elementos[self.topo-1])
            
'''Modifique a fun ̧c ̃ao “desempilha” para que ela retorne o elemento que foi desempilhado.'''

from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class item:
    valor: int

class no:
    def __init__(self, x: item):
        self.dado: item = x
        self.prox: no | None = None

class pilha:
    def __init__(self):
        self.topo: no | None = None
  
    def vazia(self) -> bool:
        '''Verifica se uma pilha está vazia e retorna True ou False
        Exemplo:
        >>> p1 = pilha()
        >>> p1.vazia()
        True
        >>> p1.empilha(item(2))
        >>> p1.vazia()
        False'''

        return self.topo == None

    def empilha(self, x: item):
        '''Insere item *x* no topo da pilha
        Exemplos:
        >>> p1 = pilha()
        >>> p1.empilha(item(4))
        >>> x: int = p1.elemento_topo()
        >>> x
        4'''

        novo = no(x)
        novo.prox = self.topo
        self.topo = novo

    def desempilha(self):
        '''Remove o item que estiver no topo da pilha
        Exemplos:
        >>> p1 = pilha()
        >>> p1.empilha(item(2))
        >>> p1.empilha(item(7))
        >>> p1.desempilha()
        >>> x: int = p1.elemento_topo()
        >>> x
        2
        '''
        if self.vazia():
            raise ValueError('Pilha Vazia!')
        else:
            rem = self.topo
            self.topo = self.topo.prox
            rem.prox = None

    def elemento_topo(self) -> int:
        '''Retorna qual o item que está no topo da pilha
        OBS: o item não é desempilhado, apenas consultado
        Exemplos:
        >>> p1 = pilha()
        >>> p1.empilha(item(2))
        >>> p1.empilha(item(7))
        >>> n: int = p1.elemento_topo()
        >>> n
        7'''

        if self.vazia():
            raise ValueError('Pilha Vazia!')
        else:
            return deepcopy(self.topo.dado.valor)
        

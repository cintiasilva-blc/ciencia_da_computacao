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

class fila:
    def __init__(self):
        self.inicio: no | None = None
        self.fim: no | None = None
  
    def vazia(self):
        '''Verifica se uma fila está vazia e retorna True ou False
        Exemplo:
        >>> f = fila()
        >>> f.vazia()
        True
        >>> f.enfileira(item(2))
        >>> f.vazia()
        False'''
        return self.inicio == None

    def enfileira(self, x:item):
        '''Insere item *x* no final da fila
        Exemplos:
        >>> f = fila()
        >>> f.enfileira(item(4))
        >>> f.enfileira(item(2))
        >>> x: int = f.obtem_primeiro()
        >>> x
        4
        '''
        novo = no(x)
        if self.fim != None:
            self.fim.prox = novo
        else:
            self.inicio = novo   
        self.fim = novo
        
        
    def desenfileira(self):
        '''Remove o item que estiver no topo da pilha
        Exemplos:
        >>> f = fila()
        >>> f.enfileira(item(2))
        >>> f.enfileira(item(7))
        >>> f.desenfileira()
        >>> x: int = f.obtem_primeiro()
        >>> x
        7
        '''
        if self.vazia():
            raise ValueError('Fila vazia')
        else:
            rem = self.inicio
            self.inicio = rem.prox
            if self.vazia():
                self.fim = self.inicio
            rem.prox = None

    def obtem_primeiro(self) -> int:
        '''Retorna qual o item que está no inicio da pilha
        OBS: o item não é desenfileirado, apenas consultado
        Exemplos:
        >>> f = fila()
        >>> f.enfileira(item(2))  
        >>> f.enfileira(item(7))    
        >>> n: int = f.obtem_primeiro()
        >>> n
        2'''

        if self.vazia():
            raise ValueError('Fila vazia')
        else:
            return deepcopy(self.inicio.dado.valor)
        


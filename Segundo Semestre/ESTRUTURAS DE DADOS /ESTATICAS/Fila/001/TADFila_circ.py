'''Reescreva a fun ̧c ̃ao “Desenfileira” para que ela, al ́em de remover o primeiro elemento da fila,
retorne este elemento para ser mostrado na tela.'''

from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy, copy

@dataclass
class item:
    valor: int | None

class fila:
    def __init__(self, tam_max: int):
        self.elementos: list[item] = [item(None) for i in range(tam_max)]
        self.tamanho = tam_max
        self.inicio = 0
        self.fim = 0

    def vazia(self) -> bool:
        '''Verifica se a fila está vazia e retorna True ou False
        
        Exemplos:
        >>> f = fila(5)
        >>> f.vazia()
        True
        >>> f.enfileira(item(2))
        >>> f.vazia()
        False
        '''
        return self.inicio == self.fim
    
    def cheia(self) -> bool:
        '''Verifica se a fila esta cheia e retorna True ou False

        Exemplos:
        >>> f = fila(4)
        >>> f.cheia()
        False
        >>> f.enfileira(item(2))
        >>> f.enfileira(item(1))
        >>> f.enfileira(item(8))
        >>> f.cheia()
        False
        >>> f.enfileira(item(3))
        >>> f.cheia()
        True
        '''
        return self.proximo_indice(self.fim) == self.inicio
    
    def proximo_indice(self, i: int) -> int:
        '''Calcula qual o proximo indice da fila
        
        Exemplos:
        >>> f = fila(3)
        >>> f.proximo_indice(0)
        1
        '''
        return (i+1) % self.tamanho
    
    def enfileira(self, x: item):
        '''Insere o item *x* no final da fila
        
        Exemplos:
        >>> f = fila(3)
        >>> f.enfileira(item(3))
        >>> f.enfileira(item(2))
        >>> x: int = f.obtem_primeiro().valor
        >>> x
        3
        '''
        if self.cheia():
            raise ValueError('Fila cheia')
        else:
            self.elementos[self.fim] = deepcopy(x)   
            self.fim = self.proximo_indice(self.fim)   
    
    def desenfileira(self):
        '''Remove o item no inicio da fila
        
        Exemplos:
        >>> f = fila(3)
        >>> f.enfileira(item(1))
        >>> f.enfileira(item(2))
        >>> f.enfileira(item(3))
        >>> f.desenfileira()
        Elemento Desenfileirado:  1
        ''' 
        if self.vazia():
            raise ValueError('Fila vazia')
        else:
            print("Elemento Desenfileirado: ", self.obtem_primeiro().valor)
            self.inicio = self.proximo_indice(self.inicio)
    
    def obtem_primeiro(self) -> item:
        '''Retorna o item que esta no inicio da fila
        OBS: o item não é desenfileirado, apenas consultado
        Exemplos:
        >>> f1 = fila(5)
        >>> f1.enfileira(item(2))
        >>> f1.enfileira(item(7))
        >>> n: int = f1.obtem_primeiro().valor
        >>> n
        2
        '''
        if self.vazia():
            raise ValueError('Fila vazia')
        else:
            return deepcopy(self.elementos[self.inicio])
        

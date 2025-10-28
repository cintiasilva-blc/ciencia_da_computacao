'''Supondo que o campo chave dos itens estejam em ordem crescente. Adicione ao TAD uma fun ̧c ̃ao “InsereORD” para que ela mantenha os itens ordenados ap ́os a inser ̧c ̃ao do item dese-
jado.'''

from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy


@dataclass
class item:
    valor: int

class lista:
    def __init__(self, tamanho: int):
        self.fim: int = 0
        self.tam_max: int = tamanho
        self.elementos: list[item] = [item(None) for i in range(tamanho)]
    
    def vazia(self) -> bool:
        '''retorna True se a lista estiver vazia
        e False caso contrário
        Exemplos:
        >>> l = lista(5)
        >>> l.vazia()
        True
        >>> l.insere_fim(item(2))
        True
        >>> l.vazia()
        False
        '''
        return self.fim == 0
            
    def cheia(self) -> bool:
        '''retorna True se a lista estiver cheia
        e False caso contrário
        Exemplos:
        >>> l = lista(2)
        >>> l.cheia()
        False
        >>> l.insere_fim(item(2))
        True
        >>> l.cheia()
        False
        >>> l.insere_fim(item(1))
        True
        >>> l.cheia()
        True'''
        return self.fim == self.tam_max
  
    def busca(self, n1: int) -> int:
        '''Procura um item na lista pelo valor.
        Se ele estiver na lista retorna o seu índice,
        caso contrário retorna -1
        Exemplos:
        >>> l = lista(3)
        >>> l.insere_fim(item(8))
        True
        >>> l.insere_fim(item(5))
        True
        >>> l.insere_fim(item(7))
        True
        >>> l.busca(5)
        1
        >>> l.busca(2)
        -1
        '''
        
        for i in range(self.fim):
            if n1 == self.elementos[i].valor:
                return i
        return -1

    def busca_item(self, n1: int) -> item | None:
        '''Retorna um item a partir de uma chave de busca.
        Caso a chave não exista, retorna None
        Exemplo:
        >>> l = lista(3)
        >>> l.insere_fim(item(8))
        True
        >>> l.insere_fim(item(5))
        True
        >>> l.insere_fim(item(7))
        True
        >>> l.busca_item(5)
        item(valor=5)
        >>> l.busca_item(2)
        '''
        
        for i in range(self.fim):
            if self.elementos[i].valor == n1:
                return self.elementos[i]

    def insere_fim(self, x: item) -> bool:
        '''Insere um item no final da lista.
        Se a inserção ocorrer normalmente ela 
        retorna True. Se o item já existir na
        lista, ou a lista já estiver cheia, 
        retorna False
        Exemplo:
        >>> l = lista(4)
        >>> l.insere_fim(item(8))
        True
        >>> l.insere_fim(item(5))
        True
        >>> l.insere_fim(item(7))
        True
        >>> l.busca(5)
        1
        >>> l.busca(8)
        0
        >>> l.insere_fim(5)
        False
        >>> l.insere_fim(1)
        True
        >>> l.insere_fim(3)
        False
        '''

        if (not self.cheia()) and (self.busca(x.valor) == -1):
            self.elementos[self.fim] = deepcopy(x)
            self.fim += 1
            return True
        return False


    def insere_pos(self, x: item, pos: int) -> bool:
        '''Insere um item na lista na posição
         indicada por *pos*. Se a inserção ocorrer 
         normalmente ela retorna True. Se o item já 
         existir na lista, ou a lista já estiver cheia, 
         ou *pos* estiver fora dos limites da lista,
        retorna False
        Exemplo:
        >>> l = lista(4)
        >>> l.insere_fim(item(8))
        True
        >>> l.insere_pos(item(5),0)
        True
        >>> l.insere_pos(item(7),1)
        True
        >>> l.busca(5)
        0
        >>> l.busca(8)
        2
        >>> l.insere_pos(item(5),1)
        False
        >>> l.insere_pos(item(1),1)
        True
        >>> l.insere_pos(item(3),2)
        False
        >>> l.busca(7)
        2
        '''
        if (not self.cheia()) and (pos <= self.fim) and (self.busca(x.valor) == -1):
            for i in range(self.fim, pos, -1):
                self.elementos[i] = self.elementos[i-1]
            self.elementos[pos] = deepcopy(x)
            self.fim += 1
            return True
        return False

    def desloca(self, pos: int):
        '''Função de apoio para remoção
        de itens no meio da lista. Essas
        remoções exigem que os elementos
        após o item removido sejam deslocados
        para a esquerda
        Exemplo:
        >>> l = lista(4)
        >>> l.insere_fim(item(8))
        True
        >>> l.insere_fim(item(5))
        True
        >>> l.insere_fim(item(7))
        True
        >>> l.desloca(0)
        >>> l.busca(8)
        -1
        >>> l.busca(7)
        1
        '''
        for i in range(pos + 1, self.fim):
            self.elementos[i-1] = self.elementos[i]
        
    def remove_fim(self) -> bool:
        '''Remove o último elemento da lista. Se a
        remoção acontecer normalmente a função retorna
        True, se a lista estiver vazia, retorna False
        Exemplos:
         >>> l = lista(4)
        >>> l.insere_fim(item(8))
        True
        >>> l.insere_fim(item(5))
        True
        >>> l.insere_fim(item(7))
        True
        >>> l.remove_fim()
        True
        >>> l.busca(7)
        -1
        '''
        if not self.vazia():
            self.fim -= 1
            return True

    def remove_pos(self, pos: int) -> bool:
        '''Remove o elemento da posição definida por *pos*. 
        Se a remoção acontecer normalmente a função retorna
        True, se a lista estiver vazia, retorna False
        Exemplos:
         >>> l = lista(4)
        >>> l.insere_fim(item(8))
        True
        >>> l.insere_fim(item(5))
        True
        >>> l.insere_fim(item(7))
        True
        >>> l.remove_pos(0)
        True
        >>> l.busca(8)
        -1
        '''
        if not self.vazia():
            self.desloca(pos)
            self.fim -= 1
            return True
    
    def remove_valor(self, valor: int) -> bool:
        '''Remove o elemento definido por *valor*. 
        Se a remoção acontecer normalmente a função retorna
        True, se a lista estiver vazia, retorna False
        Exemplos:
         >>> l = lista(4)
        >>> l.insere_fim(item(8))
        True
        >>> l.insere_fim(item(5))
        True
        >>> l.insere_fim(item(7))
        True
        >>> l.remove_valor(8)
        True
        >>> l.busca(8)
        -1
        '''

        if not self.vazia():
            pos = self.busca(valor)
            self.remove_pos(pos)
            return True
        
    def imprime_lista(self):
        '''Mostra todos os itens armazenados na lista
        
        Exemplos:
        >>> l = lista(3)
        >>> l.insere_fim(item(8))
        True
        >>> l.insere_fim(item(5))
        True
        >>> l.insere_fim(item(7))
        True
        >>> l.imprime_lista()
        Elemento:  8
        Elemento:  5
        Elemento:  7
        '''

        for i in range(self.fim):
            print('Elemento: ', self.elementos[i].valor)

    def insere_ord(self, x: item) -> bool:
        '''Mantém a lista ordenada após a inserção de cada item
        
        Exemplos:
        >>> l = lista(3)
        >>> l.insere_ord(item(3))
        True
        >>> l.insere_ord(item(1))
        True
        >>> l.insere_ord(item(2))
        True
        >>> l.imprime_lista()
        Elemento:  1
        Elemento:  2
        Elemento:  3
        '''

        if (not self.cheia()) and (self.busca(x.valor) == -1):
            pos = 0
            while self.elementos[pos].valor < x.valor and pos < self.fim:
                pos += 1
            return self.insere_pos(x, pos)

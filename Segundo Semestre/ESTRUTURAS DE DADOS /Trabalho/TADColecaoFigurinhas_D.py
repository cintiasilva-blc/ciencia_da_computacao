from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class figurinha:
    valor: int | None

class no:
    def __init__(self, x: figurinha):
        self.dado: figurinha = x
        self.prox: no | None = None
        self.rep: int = 0
    
class coleçao:
    def __init__(self):
        '''Cria uma coleção de figurinhas'''
        self.primeiro: no| None = None
        self.ultimo: no | None = None

    def colecao_vazia(self) -> bool:
        '''Verifica se a coleção esta vazia e retorna True, caso contrário retorna False.
        Exemlos:
        
        '''
        return self.primeiro == None
    
    def busca(self, chave:int) -> no:
        ''''''
        ptr = self.primeiro
        while (ptr != None) and (ptr.dado.valor != chave):
            ptr = ptr.prox
        return ptr
    
    def insere_fig(self, x: figurinha) -> bool:             
        '''Insere uma nova figurinha a coleção, a coleção se mantém ordenada
        
        Exemplos:
        '''
        novo = no(x)
        if self.busca(x.valor) == None:
            novo.rep = 1
            if self.colecao_vazia():
                self.ultimo = novo
            novo.prox = self.primeiro
            self.primeiro = novo
            return True
        else:
            novo.rep += 1

    def remove_fig(self) -> bool:



        



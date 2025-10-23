from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class figurinha:
    valor: int

class no:
    def __init__(self, x: figurinha):
        self.dado: figurinha = x
        self.prox: no | None = None
        self.contador: int = 0

class colecao:
    def __init__(self):
        '''Cria uma colecao vazia de figurinhas'''
        self.primeiro: no | None = None
        self.ultimo: no | None = None

    def colecao_vazia(self):
        '''Verifica se a coleção esta vazia e retorna True, caso contrário retorna False.
        Exemlos:
        '''
        return self.primeiro == None
        
    def insere_fig(self, x:figurinha) -> bool:
        novo = no(x)
        novo.contador = 1
        if self.colecao_vazia():
            self.primeiro = novo
        elif:
    
        else: 
            ptr = self.primeiro
            while ptr.prox != None:
                ptr = ptr.prox
                if ptr.prox.dado.valor == x.valor:
                    novo.contador += 1
            
                    

    def remove_fig(self) -> bool:


        
    def lista_figurinhas():

    def lista_repetidas():

    def calcula_troca_maxima():    

  
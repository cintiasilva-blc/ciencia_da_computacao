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

class Lista:
    def __init__(self):
        self.primeiro: no | None = None
        self.ultimo: no | None = None

    def vazia(self):
        return self.primeiro == None
    
    def busca(self, chave:int) -> no:
        ptr = self.primeiro
        while (ptr != None) and (ptr.dado != chave):
            ptr = ptr.prox
        return ptr
    
    def busca_item(self, chave:int) -> item | None:
        ptr = self.busca(chave)
        if ptr != None:
            return deepcopy(ptr.dado)
        else:
            return None
        
    def insere_ini(self, x:item) -> bool:
        if self.busca(x) == None:
            novo = no(x)
            if self.vazia():
                self.ultimo = novo
            novo.prox = self.primeiro
            self.primeiro = novo
            return True
        else:
            return False
        
    def insere_fim(self, x:item) -> bool:
        if self.busca(x.valor) == None:
            novo = no(x)
            if self.vazia():
                self.primeiro=novo
            else:
                self.ultimo.prox=novo
            self.ultimo=novo
            return True
        else:
            return False
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

class lista:
    def __init__(self):
        self.primeiro: no | None = None
        self.ultimo: no | None = None

    def vazia(self):
        return self.primeiro == None
    
    def busca(self, chave:int) -> no:
        ptr = self.primeiro
        while (ptr != None) and (ptr.dado.valor != chave):
            ptr = ptr.prox
        return ptr
    
    def busca_item(self, chave:int) -> item | None:
        ptr = self.busca(chave)
        if ptr != None:
            return deepcopy(ptr.dado)
        else:
            return None
        
    def insere_ini(self, x:item) -> bool:
        if self.busca(x.valor) == None:
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
        
    def remove_chave(self, chave: int) -> bool:
        ptr=self.primeiro
        if not self.vazia():
            if ptr.dado.valor == chave:
                return self.remove_ini()
            while ptr.prox != None and ptr.prox.dado.valor != chave:
                ptr=ptr.prox
            if ptr.prox != None:
                rem = ptr.prox
                ptr.prox = rem.prox
                if ptr.prox == None:
                    self.ultimo=ptr
                rem.prox=None
                return True
        return False
    
    def remove_ini(self) -> bool:
        if not self.vazia():
            rem = self.primeiro
            self.primeiro = rem.prox
            if self.vazia():
                self.ultimo = None
            rem.prox = None
            return True
        return False
    
    def insere_pos(self, x:item, pos:int) -> bool:
        i=0
        ptr=self.primeiro
        if pos == 0:
            return self.insere_ini(x)
        elif self.busca(x.chave) == None:
            while ptr != None and i < pos-1:
                ptr = ptr.prox
                i+=1
            if ptr != None:
                novo = no(x)
                novo.prox = ptr.prox
                if novo.prox == None:
                    self.ultimo = novo
                ptr.prox = novo
                return True
        return False
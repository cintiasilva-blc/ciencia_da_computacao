from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class item:
    valor: int | None

class no:
    def __init__(self,x: item):
        self.dado: item = x
        self.prox: no | None = None
        self.ant: no | None = None

class lista:
    def __init__(self):
        self.primeiro = no(item(None))
        self.ultimo = self.primeiro
        self.primeiro.prox = None
        self.primeiro.ant = None

    def vazia(self) -> bool:
        return self.primeiro == self.ultimo
    
    def busca(self, chave:int) -> no | None:
        ptr = self.primeiro.prox  
        while (ptr is not None) and (ptr.dado.valor != chave):
            ptr = ptr.prox
        return ptr
    
    def busca_item(self, chave:int) -> item | None:
        ptr = self.busca(chave)
        if ptr is not None:
            return deepcopy(ptr.dado)
        else:
            return None
    
    def insere_ini(self, x: item) -> bool:
        if self.busca(x.valor) == None:
            novo = no(x)
            novo.prox = self.primeiro.prox
            novo.ant = self.primeiro
            if self.primeiro.prox != None:
                self.primeiro.prox.ant = novo
            else:
                self.ultimo = novo
            self.primeiro.prox = novo
            return True
        else:
            return False
        
        
    def remove_ini(self) -> bool:
        if not self.vazia():
            rem = self.primeiro.prox
            self.primeiro.prox = rem.prox
            if rem.prox != None:
                rem.prox.ant = self.primeiro
            else:
                self.ultimo = self.primeiro
            rem.prox = None
            rem.ant = None
            return True
        else:
            return False
        
    ''' rem = self.ultimo
        self.ultimo = rem.ant
        self.ultimo =  None 
        rem.ant = None 
        '''
        
            
        

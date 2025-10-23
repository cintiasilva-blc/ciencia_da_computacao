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
        self.ant: no | None = None
    
class coleçao:
    def __init__(self):
        self.primeiro = no(figurinha(None))
        self.ultimo = self.primeiro
        self.primeiro.prox = None
        self.primeiro.ant = None

    def colecao_vazia(self) -> bool:
        '''Verifica se a coleção esta vazia e retorna True, caso contrário retorna False.
        Exemlos:
        
        '''
        return self.primeiro == self.ultimo
    
    def busca(self, chave:int) -> no | None:
        ptr = self.primeiro.prox  
        while (ptr is not None) and (ptr.dado.valor != chave):
            ptr = ptr.prox
        return ptr
    
    def insere_fig(self, x: figurinha) -> bool:             
        '''Insere uma nova figurinha a coleção, a coleção se mantém ordenada
        
        Exemplos:
        >>> c = colecao()
        >>> c.insere_fig(figurinha(1))
        >>> c.insere_fig(figurinha(3))
        >>> c.insere_fig(figurinha(1))
        >>> c.insere_fig(figurinha(4))

        '''
        
        novo = no(x)
        if self.colecao_vazia():
            novo.prox = self.primeiro 
            novo.ant = self.primeiro       
            self.primeiro.prox = novo
            self.ultimo = novo
        else:
            ptr = self.primeiro.prox
            ptr_ant = self.primeiro
            while ptr != None and ptr.dado.valor < x.valor:
                ptr_ant = ptr
                ptr = ptr.prox
            novo.prox = ptr
            novo.ant = ptr_ant
            ptr_ant.prox = novo
            if ptr == None:
                self.ultimo = novo
            return True
        return False  

    def remove_fig(self, x: figurinha) -> bool:
        '''Remove uma figurinha da coleção
        
        Exemplos:
        '''
        if not self.colecao_vazia():
            rem = self.primeiro.prox
            while rem != None and rem.dado.valor != x.valor:
                rem = rem.prox
            if rem == None:
                return False
            rem.ant.prox = rem.prox
            if rem.prox != None:
                rem.prox.ant = rem.ant
            else:
                self.ultimo = rem.ant
            return True
    
        
    def mostra_colecao(self) -> str:

        if self.colecao_vazia():
            return "[]"
        
        ptr = self.primeiro.prox
        result = "["
        while ptr != None:
            result += str(ptr.dado.valor)
            if ptr.prox != None:
                result += ", "
            ptr = ptr.prox
        result += "]"
        return result

    
    def figurinhas_sem_rep(self) -> str:
        '''Gera uma string com as figurinhas presentes na coleção, nao apresenta as repetições
        
        Exemplos:
        '''
        
        unicas = coleçao()
        ptr = self.primeiro.prox

        while ptr != None:
            atual = ptr.dado
            if not unicas.busca(atual.valor):
                unicas.insere_fig(atual)
            ptr = ptr.prox
        return unicas.mostra_colecao()
    
    
    
    def figurinhas_rep(self) -> str:
        '''Gera uma string com as figurinhas presentes na coleção mostrando a quantidade de repetições
        no formato "[6(3), 9(2), 12(1)]
        
        Exemplos:
        '''

        cont = 0

        ptr = 








        










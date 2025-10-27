from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class fig:
    num_fig: int 

class Colecao:
    def __init__(self,tamanho:int):
        '''Vai criar uma coleção vazia de figurinhas.'''
        self.fim:int = 0
        self.tam_max:int = tamanho
        self.elementos: list[fig] = [None] * tamanho

    def colecao_cheia(self)-> bool:
        '''Retorna true se a coleção estiver cheia e false caso contrário.
        Exemplo:
        >>> c = Colecao(2)
        >>> c.insere_figurinha(fig(1))
        True
        >>> c.insere_figurinha(fig(2))
        True
        >>> c.colecao_cheia()
        True
        >>> p = Colecao(10)
        >>> p.insere_figurinha(fig(1))
        True
        >>> p.colecao_cheia()
        False
        '''
        return self.fim == self.tam_max

    def colecao_vazia(self)-> bool:
        '''Retorna True se a coleção estiver vazia e False caso contrário.
        Exemplo:
        >>> c = Colecao(2)
        >>> c.insere_figurinha(fig(1))
        True
        >>> c.insere_figurinha(fig(2))
        True
        >>> c.colecao_vazia()
        False
        >>> p = Colecao(10)
        >>> p.colecao_vazia()
        True
        '''
        return  self.fim == 0


    def insere_figurinha(self,figurinha:fig)-> bool:
        '''Insere uma figurinha na coleção de forma ordenada.
        Exemplo:
        >>> c = Colecao(10)
        >>> c.insere_figurinha(fig(5))
        True
        >>> c.insere_figurinha(fig(3))
        True
        >>> c.insere_figurinha(fig(7))
        True
        >>> c.lista_figurinhas()
        '[3, 5, 7]'
        >>> p = Colecao(2)
        >>> p.insere_figurinha(fig(1))
        True
        >>> p.insere_figurinha(fig(2))
        True
        >>> p.insere_figurinha(fig(3))
        False
        '''
        
        if self.colecao_cheia():
            return False
        
        i = 0
        while i < self.fim and self.elementos[i].num_fig <= figurinha.num_fig:
            i += 1

        for j in range(self.fim, i, -1):
            self.elementos[j] = self.elementos[j-1]
        self.elementos[i] = deepcopy(figurinha)
        self.fim+=1
        return True
       
        
    def desloca(self,pos:int):
        '''Função auxiliar para remover um elemento. Os elementos são deslocados para a esquerda.'''
        for i in range(pos,self.fim - 1):
            self.elementos[i] = self.elementos[i+1]


    def remove_figurinha(self,pos:int)->bool:
        '''Remove a figurinha  da posição definida. 
        Se a remoção acontecer normalmente a função retorna
        True, se a lista estiver vazia, retorna False
        Exemplo:
        >>> c = Colecao(5)
        >>> c.insere_figurinha(fig(8))
        True
        >>> c.insere_figurinha(fig(5))
        True
        >>> c.insere_figurinha(fig(3))
        True
        >>> c.remove_figurinha(1)
        True
        >>> c.lista_figurinhas()
        '[3, 8]'
        >>> c.remove_figurinha(10)
        False
        >>> v = Colecao(3)
        >>> v.remove_figurinha(1)
        False
        '''

        if self.colecao_vazia() or pos < 0 or pos >= self.fim:
            return False
        
        self.desloca(pos)
        self.fim -= 1
        return True
        
    def remove_valor(self, figurinha_valor: int) -> bool:
        '''Remove o elemento definido por *figurinha_valor*. 
        Se a remoção acontecer normalmente a função retorna
        True, se a lista estiver vazia, retorna False
        Exemplos:
        >>> c = Colecao(5)
        >>> c.insere_figurinha(fig(8))
        True
        >>> c.insere_figurinha(fig(5))
        True
        >>> c.insere_figurinha(fig(3))
        True
        >>> c.remove_valor(5)
        True
        >>> c.lista_figurinhas()
        '[3, 8]'
        >>> c.remove_valor(10)
        False
        >>> v = Colecao(3)
        >>> v.remove_valor(1)
        False
        '''

        if self.colecao_vazia():
           return False
        
        for i in range(self.fim):
            if self.elementos[i].num_fig == figurinha_valor:
                self.desloca(i)
                self.fim -= 1
                return True
        return False

    def lista_figurinhas(self)-> str:
        '''Gera as figurinhas da coleção em formato de string, sem considerar as figurinhas repetidas.
        Exemplo:
        >>> c = Colecao(10)
        >>> c.insere_figurinha(fig(4))
        True
        >>> c.insere_figurinha(fig(10))
        True
        >>> c.insere_figurinha(fig(25))
        True
        >>> c.insere_figurinha(fig(4))  
        True
        >>> c.lista_figurinhas()
        '[4, 10, 25]'
        >>> d = Colecao(5)
        >>> d.insere_figurinha(fig(15))
        True
        >>> d.insere_figurinha(fig(8))
        True
        >>> d.insere_figurinha(fig(20))
        True
        >>> d.lista_figurinhas()
        '[8, 15, 20]'
        >>> v = Colecao(3)
        >>> v.lista_figurinhas()
        '[]'
        '''

        if self.colecao_vazia():
            return '[]'
    

        lista = '['
        lista += str(self.elementos[0].num_fig)

        for i in range(1, self.fim):
            if self.elementos[i].num_fig != self.elementos[i-1].num_fig:
                lista += ', ' + str(self.elementos[i].num_fig)

        lista += ']'
        return lista

        
    def figurinhas_rep(self)->str:
        '''Gera as figurinhas repetidas e sua quantidade( não considera a primeira ocorrÊncia ) em formato de string. Caso não haja figurinhas repetidas retorna *[]*
        Exemplo:
        >>> c = Colecao(10)
        >>> c.insere_figurinha(fig(12))
        True
        >>> c.insere_figurinha(fig(12))
        True
        >>> c.insere_figurinha(fig(60))
        True
        >>> c.insere_figurinha(fig(60))
        True
        >>> c.insere_figurinha(fig(60)) 
        True
        >>> c.figurinhas_rep()
        '[12(1), 60(2)]'
        >>> v = Colecao(3)
        >>> v.figurinhas_rep()
        '[]'
        '''

        if self.colecao_vazia():
            return '[]'
        
        lista = '['
        i = 0
        primeiro = True
        while i < self.fim:
            count = 1
            while i + count < self.fim and self.elementos[i].num_fig == self.elementos[i + count].num_fig:
                count += 1
            if count > 1:
                if not primeiro:
                    lista += ', '
                else:
                    primeiro = False
                lista += str(self.elementos[i].num_fig)+ '('+ str(count - 1) +')'
            i += count
        lista += ']'
        return lista
    

    def identifica_rept_unicas(self,colecaoB:Colecao)->Colecao:
        '''Identifica as figurinhas repetidas desta coleção que não estão na coleção B.
        Exemplo:
        >>> c = Colecao(10)
        >>> c.insere_figurinha(fig(1))
        True
        >>> c.insere_figurinha(fig(1))
        True
        >>> c.insere_figurinha(fig(2))
        True
        >>> c.insere_figurinha(fig(3))
        True
        >>> c.insere_figurinha(fig(3)) 
        True
        >>> c2 = Colecao(10)
        >>> c2.insere_figurinha(fig(2))
        True
        >>> c2.insere_figurinha(fig(4))
        True
        >>> unicas = c.identifica_rept_unicas(c2)
        >>> unicas.lista_figurinhas()
        '[1, 3]'
        >>> x = Colecao(6)
        >>> y = Colecao(6)
        >>> x.insere_figurinha(fig(1))
        True
        >>> x.insere_figurinha(fig(2))
        True
        >>> x.insere_figurinha(fig(3))
        True
        >>> x.insere_figurinha(fig(4))
        True
        >>> y.insere_figurinha(fig(2))
        True
        >>> y.insere_figurinha(fig(3))
        True
        >>> y.insere_figurinha(fig(5))
        True
        >>> y.insere_figurinha(fig(6))
        True
        >>> unicas_x = x.identifica_rept_unicas(y)
        >>> unicas_x.lista_figurinhas()
        '[]'
        '''

        unicas = Colecao(self.tam_max)
        i = 0
        while i < self.fim -1:
            nA = self.elementos[i].num_fig
            if self.elementos[i+1].num_fig == nA:
                existeB = False
                j = 0
                while j < colecaoB.fim:
                    if colecaoB.elementos[j].num_fig == nA:
                        existeB = True
                    j+=1

                if not existeB:
                    unicas.insere_figurinha(fig(nA))

                while i<self.fim and self.elementos[i].num_fig == nA:
                    i+=1
            else:
                i+=1

        return unicas

    
    def encontra_pos(self, n1:int)-> int:
        '''Procura uma figurinha na coleção pelo valor.
        Se ele estiver na lista retorna o seu índice,
        caso contrário retorna -1
        Exemplos:
        >>> c = Colecao(5)
        >>> c.insere_figurinha(fig(8))
        True
        >>> c.insere_figurinha(fig(5))
        True
        >>> c.insere_figurinha(fig(3))
        True
        >>> c.encontra_pos(5)
        1
        >>> c.encontra_pos(2)
        -1
        '''

        for i in range(self.fim):
            if n1 == self.elementos[i].num_fig:
                return i
        return -1
    
    def realiza_troca(self,colecaoB:Colecao,nA:int,nB:int):
        '''Executa uma troca simples entre duas coleções.
        Exemplo:
        >>> a = Colecao(10)
        >>> b = Colecao(10)
        >>> a.insere_figurinha(fig(1))
        True
        >>> a.insere_figurinha(fig(2))
        True
        >>> a.insere_figurinha(fig(3))
        True
        >>> b.insere_figurinha(fig(4))
        True
        >>> b.insere_figurinha(fig(5))
        True
        >>> b.insere_figurinha(fig(6))
        True
        >>> a.realiza_troca(b,1,4)
        >>> a.lista_figurinhas()
        '[2, 3, 4]'
        >>> b.lista_figurinhas()
        '[1, 5, 6]'
        '''

        posA = self.encontra_pos(nA)
        posB = colecaoB.encontra_pos(nB)

        if posA != -1:
            self.remove_figurinha(posA)
        if posB!= -1:
            colecaoB.remove_figurinha(posB)

        self.insere_figurinha(fig(nB))
        colecaoB.insere_figurinha(fig(nA))

     
    def troca_maxima(self,colecaoB:Colecao):
        '''Realiza a troca máxima de figurinhas entre duas coleções.
        A troca considera apenas as figurinhas repetidas de cada coleção que o outro não possui.
        >>> c1 = Colecao(10)
        >>> c2 = Colecao(10)
        >>> c1.insere_figurinha(fig(1))
        True
        >>> c1.insere_figurinha(fig(1))
        True
        >>> c1.insere_figurinha(fig(2))
        True
        >>> c1.insere_figurinha(fig(2))
        True
        >>> c1.insere_figurinha(fig(3)) 
        True
        >>> c1.insere_figurinha(fig(4))
        True
        >>> c2.insere_figurinha(fig(2))
        True
        >>> c2.insere_figurinha(fig(3))
        True
        >>> c2.insere_figurinha(fig(5))
        True
        >>> c2.insere_figurinha(fig(5))
        True
        >>> c2.insere_figurinha(fig(6))
        True
        >>> c2.insere_figurinha(fig(6)) 
        True
        >>> c1.troca_maxima(c2)
        >>> c1.lista_figurinhas()
        '[1, 2, 3, 4, 5]'
        >>> c2.lista_figurinhas()
        '[1, 2, 3, 5, 6]'
        '''

        unicasA = self.identifica_rept_unicas(colecaoB)
        unicasB = colecaoB.identifica_rept_unicas(self)


        if unicasA.fim < unicasB.fim:
            n_trocas = unicasA.fim
        else:
            n_trocas = unicasB.fim

        for i in range(n_trocas):
            numA = unicasA.elementos[i].num_fig
            numB = unicasB.elementos[i].num_fig
            self.realiza_troca(colecaoB, numA, numB)



if __name__ == '__main__':
    import doctest
    doctest.testmod()
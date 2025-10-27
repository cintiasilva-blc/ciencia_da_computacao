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

    
class ColecaoFigurinhas:
    def __init__(self):
        self.primeiro = no(figurinha(None))
        self.ultimo = self.primeiro
        self.primeiro.prox = None
        self.primeiro.ant = None

    def colecao_vazia(self) -> bool:
        '''Verifica se a coleção esta vazia e retorna True, caso contrário retorna False.
        Exemlos:
        >>> c = ColecaoFigurinhas()
        >>> c.colecao_vazia()
        True
        >>> c.insere_fig(figurinha(1))
        True
        >>> c.insere_fig(figurinha(3))
        True
        >>> c.colecao_vazia()
        False
        '''
        return self.primeiro == self.ultimo
    
    def busca(self, num:int) -> no:
        '''Procura uma figurinha na coleção através do seu número e retorna sua posição
        
        Exemplos:
        >>> c = ColecaoFigurinhas()
        >>> c.insere_fig(figurinha(1))
        True
        >>> c.insere_fig(figurinha(3))
        True
        >>> c.insere_fig(figurinha(1))
        True
        >>> c.insere_fig(figurinha(4))
        True
        >>> c.busca(3).dado
        figurinha(valor=3)
        '''
        ptr = self.primeiro.prox  
        while (ptr != None) and (ptr.dado.valor != num):
            ptr = ptr.prox
        return ptr
    
    def insere_fig(self, x: figurinha) -> bool:             
        '''Insere uma nova figurinha a coleção, a coleção se mantém ordenada. Caso a inserção for efetuada, retorna True.
        
        Exemplos:
        >>> c = ColecaoFigurinhas()
        >>> c.insere_fig(figurinha(1))
        True
        >>> c.insere_fig(figurinha(3))
        True
        >>> c.insere_fig(figurinha(1))
        True
        >>> c.insere_fig(figurinha(4))
        True
        >>> c.mostra_colecao()
        '[1, 1, 3, 4]'
        '''
        
        novo = no(x)
        if self.colecao_vazia():
            novo.prox = None 
            novo.ant = self.primeiro       
            self.primeiro.prox = novo
            self.ultimo = novo
            return True
        else:
            ptr = self.primeiro.prox
            while ptr != None and ptr.dado.valor < x.valor:
                ptr = ptr.prox
            if ptr != None:
                novo.prox = ptr
                novo.ant = ptr.ant
                ptr.ant.prox = novo
                ptr.ant = novo
            else:
                novo.prox = None
                novo.ant = self.ultimo
                self.ultimo.prox = novo
                self.ultimo = novo
            return True
 

    def remove_fig(self, x: figurinha) -> bool:
        '''Remove uma figurinha da coleção
        
        Exemplos:
        >>> c = ColecaoFigurinhas()
        >>> c.insere_fig(figurinha(1))
        True
        >>> c.insere_fig(figurinha(3))
        True
        >>> c.insere_fig(figurinha(1))
        True
        >>> c.insere_fig(figurinha(4))
        True
        >>> c.mostra_colecao()
        '[1, 1, 3, 4]'
        >>> c.remove_fig(figurinha(1))
        True
        >>> c.mostra_colecao()
        '[1, 3, 4]'
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
        return False
    
        
    def mostra_colecao(self) -> str:
        '''Mostra a coleção de figurinhas no formato de vetor (Ex: A = [x, y, z]), onde apenas o numero de cada figurinha é mostrado.
        
        Exemplos:
        >>> c = ColecaoFigurinhas()
        >>> c.insere_fig(figurinha(2))
        True
        >>> c.insere_fig(figurinha(4))
        True
        >>> c.insere_fig(figurinha(1))
        True
        >>> c.insere_fig(figurinha(3))
        True
        >>> c.insere_fig(figurinha(3))
        True
        >>> c.mostra_colecao()
        '[1, 2, 3, 3, 4]'
        >>> v = ColecaoFigurinhas()
        >>> v.mostra_colecao()
        '[]'
        '''

        if self.colecao_vazia():
            return '[]'
        
        ptr = self.primeiro.prox
        result = '['
        while ptr != None:
            result += str(ptr.dado.valor)
            if ptr.prox != None:
                result += ', '
            ptr = ptr.prox
        result += ']'
        return result

    def figurinhas_unicas(self) -> str:
        '''Gera uma string com as figurinhas presentes na coleção, nao apresenta as repetições
        
        Exemplos:
        >>> c = ColecaoFigurinhas()
        >>> c.insere_fig(figurinha(2))
        True
        >>> c.insere_fig(figurinha(4))
        True
        >>> c.insere_fig(figurinha(1))
        True
        >>> c.insere_fig(figurinha(1))
        True
        >>> c.insere_fig(figurinha(1))
        True
        >>> c.insere_fig(figurinha(9))
        True
        >>> c.figurinhas_unicas()
        '[1, 2, 4, 9]'
        '''
        
        unicas = ColecaoFigurinhas()
        ptr = self.primeiro.prox

        while ptr != None:
            atual = ptr.dado
            if not unicas.busca(atual.valor):
                unicas.insere_fig(atual)
            ptr = ptr.prox
        return unicas.mostra_colecao()
    
    def figurinhas_rep(self) -> str:
        '''Gera uma string com as figurinhas e a quantidade de repetidas presentes na coleção
        
        Exemplos:
        >>> c = ColecaoFigurinhas()
        >>> c.insere_fig(figurinha(2))
        True
        >>> c.insere_fig(figurinha(4))
        True
        >>> c.insere_fig(figurinha(1))
        True
        >>> c.insere_fig(figurinha(1))
        True
        >>> c.insere_fig(figurinha(1))
        True
        >>> c.insere_fig(figurinha(4))
        True
        >>> c.figurinhas_rep()
        '[1(2), 2(0), 4(1)]'
        '''

        if self.colecao_vazia():
            return '[]'

        ptr = self.primeiro.prox
        att = ptr.dado.valor
        rep = 0
        result = '['
        while ptr != None:
            if ptr.dado.valor == att:
                rep += 1
            else:
                result += str(att) + '(' + str(rep - 1) + '), '
                att = ptr.dado.valor
                rep = 1
            ptr = ptr.prox
        result += str(att) + '(' + str(rep - 1) + ')'
        result += ']'
        return result
    
    def eh_repetida(self, valor: int) -> bool:
        '''Verifica se uma figurinha repete na coleção e retorna True. Caso contrário, retorna False.
        
        Exemplos:
        >>> c = ColecaoFigurinhas()
        >>> c.insere_fig(figurinha(2))
        True
        >>> c.insere_fig(figurinha(4))
        True
        >>> c.insere_fig(figurinha(1))
        True
        >>> c.insere_fig(figurinha(1))
        True
        >>> c.insere_fig(figurinha(1))
        True
        >>> c.insere_fig(figurinha(9))
        True
        >>> c.eh_repetida(1)
        True
        >>> c.eh_repetida(2)
        False
        '''

        cont = 0
        ptr = self.primeiro.prox
        
        while ptr != None and cont < 2:
            if ptr.dado.valor == valor:
                cont += 1
            ptr = ptr.prox
        return cont >= 2

    def fig_trocaveis(self, c2: ColecaoFigurinhas) -> ColecaoFigurinhas:
        '''Encontra e retorna as figurinhas repetidas que podem ser trocadas com outra coleção,

        Exemplos:
        >>> c = ColecaoFigurinhas()
        >>> for i in [4, 4, 5, 5, 5, 6, 7, 7]:
        ...     c.insere_fig(figurinha(i))
        True
        True
        True
        True
        True
        True
        True
        True
        >>> c2 = ColecaoFigurinhas()
        >>> for i in [1, 1, 2, 3, 3, 3]:
        ...     c2.insere_fig(figurinha(i))
        True
        True
        True
        True
        True
        True
        >>> x = c.fig_trocaveis(c2)
        >>> x.mostra_colecao()
        '[4, 5, 7]'
        >>> y = c2.fig_trocaveis(c)
        >>> y.mostra_colecao()
        '[1, 3]'
        '''

        result = ColecaoFigurinhas()
        ptr = self.primeiro.prox
        
        while ptr != None:
            num = ptr.dado.valor
            if (self.eh_repetida(num) and c2.busca(num) == None and result.busca(num) == None):
                result.insere_fig(figurinha(num))
            ptr = ptr.prox
        return result


    def determina_trocas(self, c2: ColecaoFigurinhas) -> int:
        '''Determina quantas figurinhas podem ser trocadas entre as duas coleções, retorna a quantidade
        
        Exemplos:
        >>> c = ColecaoFigurinhas()
        >>> for i in [4, 4, 5, 5, 5, 6, 7, 7]:
        ...     c.insere_fig(figurinha(i))
        True
        True
        True
        True
        True
        True
        True
        True
        >>> c2 = ColecaoFigurinhas()
        >>> for i in [1, 1, 2, 3, 3, 3]:
        ...     c2.insere_fig(figurinha(i))
        True
        True
        True
        True
        True
        True
        >>> c.determina_trocas(c2)
        2
        '''

        minhas_trocaveis = self.fig_trocaveis(c2)
        trocaveis_c2 = c2.fig_trocaveis(self)
        
        qtd_minhas = 0
        ptr = minhas_trocaveis.primeiro.prox
        while ptr != None:
            qtd_minhas += 1
            ptr = ptr.prox
            
        qtd_c2 = 0
        ptr = trocaveis_c2.primeiro.prox
        while ptr is not None:
            qtd_c2 += 1
            ptr = ptr.prox
            
        if qtd_minhas < qtd_c2:
            return qtd_minhas
        else:
            return qtd_c2

    def trocamax_fig(self, c2: ColecaoFigurinhas):
        '''Realiza a troca máxima de figurinhas repetidas entre duas coleções,

        Exemplos:
        >>> c1 = ColecaoFigurinhas()
        >>> c2 = ColecaoFigurinhas()
        >>> c1.insere_fig(figurinha(1))
        True
        >>> c1.insere_fig(figurinha(1))  
        True
        >>> c1.insere_fig(figurinha(2))
        True
        >>> c2.insere_fig(figurinha(3))
        True
        >>> c2.insere_fig(figurinha(3))  
        True
        >>> c2.insere_fig(figurinha(4))
        True
        >>> c1.trocamax_fig(c2)
        >>> c1.mostra_colecao()
        '[1, 2, 3]'
        >>> c2.mostra_colecao()
        '[1, 3, 4]'
        '''
    
        minhas_trocaveis = self.fig_trocaveis(c2)
        c2_trocaveis = c2.fig_trocaveis(self)
        qtd_trocas = self.determina_trocas(c2)

        if qtd_trocas > 0:
            ptr_minhas = minhas_trocaveis.primeiro.prox
            ptr_c2 = c2_trocaveis.primeiro.prox
            
            while ptr_minhas != None and ptr_c2 != None:
                num = ptr_minhas.dado.valor
                self.remove_fig(figurinha(num))
                c2.insere_fig(figurinha(num))
                
                num_c2 = ptr_c2.dado.valor
                c2.remove_fig(figurinha(num_c2))
                self.insere_fig(figurinha(num_c2))
                
                ptr_minhas = ptr_minhas.prox
                ptr_c2 = ptr_c2.prox



    
if __name__ == "__main__":
    import doctest
    doctest.testmod()




        









        










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
        
        if self.colecao_vazia():
            return '[]'
        
        ptr = self.primeiro.prox
        resultado = '['
        primeiro = True

        while ptr != None:
            if ptr.ant == self.primeiro or ptr.dado.valor != ptr.ant.dado.valor:
                if primeiro == False:
                    resultado += ', '
                resultado += str(ptr.dado.valor)
                primeiro = False
            ptr = ptr.prox

        resultado += ']'
        return resultado
    
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
        atual = ptr.dado.valor
        rep = 0
        result = '['
        while ptr != None:
            if ptr.dado.valor == atual:
                rep += 1
            else:
                result += str(atual) + '(' + str(rep - 1) + '), '
                atual = ptr.dado.valor
                rep = 1
            ptr = ptr.prox
        result += str(atual) + '(' + str(rep - 1) + ')'
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

    def fig_trocaveis(self, cB: ColecaoFigurinhas) -> str:
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
        >>> cB = ColecaoFigurinhas()
        >>> for i in [1, 1, 2, 3, 3, 3]:
        ...     cB.insere_fig(figurinha(i))
        True
        True
        True
        True
        True
        True
        >>> x = c.fig_trocaveis(cB)
        >>> x
        '[4, 5, 7]'
        >>> y = cB.fig_trocaveis(c)
        >>> y
        '[1, 3]'
        '''

        if self.colecao_vazia():
            return '[]'
        
        ptr = self.primeiro.prox
        resultado = '['
        primeiro = True

        while ptr != None:
            if ptr.ant == self.primeiro or ptr.dado.valor != ptr.ant.dado.valor:
                num = ptr.dado.valor
                if self.eh_repetida(num) and (cB.busca(num) == None):
                    if not primeiro:
                        resultado += ', '
                    resultado += str(num)
                    primeiro = False
            ptr = ptr.prox

        resultado += ']'
        return resultado

    def determina_trocas(self, cB: ColecaoFigurinhas) -> int:
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
        >>> cB = ColecaoFigurinhas()
        >>> for i in [1, 1, 2, 3, 3, 3]:
        ...     cB.insere_fig(figurinha(i))
        True
        True
        True
        True
        True
        True
        >>> c.determina_trocas(cB)
        2
        '''

        if self.colecao_vazia() or cB.colecao_vazia():
            return 0

        trocaveisA = 0
        ptrA = self.primeiro.prox
        while ptrA != None:
            if (ptrA.ant == self.primeiro) or (ptrA.dado.valor != ptrA.ant.dado.valor):
                num = ptrA.dado.valor
                if (self.eh_repetida(num)) and (cB.busca(num) == None):
                    trocaveisA += 1
            ptrA = ptrA.prox

        trocaveisB = 0
        ptrB = cB.primeiro.prox
        while ptrB is not None:
            if (ptrB.ant == cB.primeiro) or (ptrB.dado.valor != ptrB.ant.dado.valor):
                num = ptrB.dado.valor
                if (cB.eh_repetida(num) )and (self.busca(num) == None):
                    trocaveisB += 1
            ptrB = ptrB.prox

        if trocaveisA < trocaveisB:
            return trocaveisA
        else:
            return trocaveisB

    def trocamax_fig(self, cB: ColecaoFigurinhas):
        '''Realiza a troca máxima de figurinhas repetidas entre duas coleções,
        Exemplos:
        >>> cA = ColecaoFigurinhas()
        >>> cB = ColecaoFigurinhas()
        >>> cA.insere_fig(figurinha(1))
        True
        >>> cA.insere_fig(figurinha(1))  
        True
        >>> cA.insere_fig(figurinha(2))
        True
        >>> cB.insere_fig(figurinha(3))
        True
        >>> cB.insere_fig(figurinha(3))  
        True
        >>> cB.insere_fig(figurinha(4))
        True
        >>> cA.trocamax_fig(cB)
        >>> cA.mostra_colecao()
        '[1, 2, 3]'
        >>> cB.mostra_colecao()
        '[1, 3, 4]'
        '''
    
        
        limite = self.determina_trocas(cB)
        if limite == 0:
            return None

        ptrA = self.primeiro.prox
        trocas = 0

        while ptrA != None and trocas < limite:
            if ptrA.ant == self.primeiro or ptrA.dado.valor != ptrA.ant.dado.valor:
                numA = ptrA.dado.valor
                if self.eh_repetida(numA) and cB.busca(numA) == None:
                    ptrB = cB.primeiro.prox
                    enc_troca = False

                    while ptrB != None and not enc_troca:
                        if ptrB.ant == cB.primeiro or ptrB.dado.valor != ptrB.ant.dado.valor:
                            numB = ptrB.dado.valor
                            if cB.eh_repetida(numB) and self.busca(numB) == None:
                                self.remove_fig(figurinha(numA))
                                cB.insere_fig(figurinha(numA))
                                cB.remove_fig(figurinha(numB))
                                self.insere_fig(figurinha(numB))
                                trocas += 1
                                enc_troca = True
                        ptrB = ptrB.prox
            ptrA = ptrA.prox






        









        










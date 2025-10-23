from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Ponto:
    x: float
    y: float

    def cria_ponto(a: float, b: float) -> Ponto:
        '''Atribui *a* e *b* ao TAD *Ponto*. '''

        p = Ponto(a, b)
        return p
    
    def distancia(p1: Ponto, p2: Ponto) -> Ponto:
        '''calcula a distância entre dois pontos
        '''

        return  ((p1.x - p2.x)**2 + (p1.y - p2.y)**2) ** (1/2)
    
    def imprime(p1: Ponto):
        '''Mostra as coordenadas do ponto
        
        Exemplos:
        >>> p1 = Ponto.cria_ponto(2, 3)
        >>> p1.imprime()
        Coordenada x:  2
        Coordenada y:  3
        '''

        print('Coordenada x: ', p1.x)
        print('Coordenada y: ', p1.y)
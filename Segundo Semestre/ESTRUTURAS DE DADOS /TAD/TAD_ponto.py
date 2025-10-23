from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Ponto:
    x: float
    y: float

    def cria_ponto(a: float, b: float) -> Ponto:
        '''Atribui os valores *a* e *b* a classe Ponto'''
        p = Ponto(a, b)
        return p
    
    def distancia(p1: Ponto, p2: Ponto) -> float:
        '''Calcula a distância entre os pontos *p1* e *p2*'''
        return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2) ** (1/2)
    
    def imprime(p1: Ponto):
        '''Mostra as coordenadas x e y do ponto'''
        print('Coordenada x: ', p1.x)
        print('Coordenada y: ', p1.y)


def main():
    x = 2
    y = 3
    a = 1
    b = 0

    p1 = Ponto.cria_ponto(x, y)
    p2 = Ponto.cria_ponto(a, b)
    print('Distância entre os pontos: ', p1.distancia(p2))

    p1.imprime()
    p2.imprime()

main()

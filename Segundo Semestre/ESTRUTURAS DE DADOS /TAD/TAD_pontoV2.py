from __future__ import annotations
from dataclasses import dataclass

class Ponto:
    x: float
    y: float

    def __init__(self, a: float, b: float):
        self.x = a
        self.y = b
        print('Criado um ponto com as coordenadas x = ', self.x, ' e y = ', self.y)

    def cria_ponto(a: float, b: float) -> Ponto:
        p = Ponto(a, b)
        return p
    
    def distancia(self, p2: Ponto) -> float:
        return ((self.x - p2.x)**2 + (self.y - p2.y)** 2 + (self.y - p2.y)**2) ** (1/2)
    
    def imprime(self):
        print('Coordenada x: ', self.x) 
        print('Coordenada y: ', self.y) 


def main():
    x: float = 2
    y: float = 3
    a: float = 4
    b: float = 5

    p1 = Ponto.cria_ponto(x, y)
    p2 = Ponto.cria_ponto(a, b)
    print("Distancia entre os pontos: ", p1.distancia(p2)) 
    
    p1.imprime()
    p2.imprime()

main()    
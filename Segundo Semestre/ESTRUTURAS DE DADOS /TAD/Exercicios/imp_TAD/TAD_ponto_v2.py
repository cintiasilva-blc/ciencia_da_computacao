from __future__ import annotations
from dataclasses import dataclass

class Ponto:
    x: float
    y: float

    def __init__(self, a: float, b: float):
        self.x = a
        self.y = b
        print('Criado um ponto com as coordenadas ', self.x, ' e ', self.y)

    def cria_ponto(a: float, b: float) -> Ponto:
        p = Ponto(a, b)
        return p
    
    def distancia(self, p2: Ponto) -> float:
        return ((self.x - p2.x)**2 + (self.y - p2.y)**2) ** (1/2)
    
    def imprime(self):
        print('Coordenada x: ', self.x) 
        print('Coordenada y: ', self.y)

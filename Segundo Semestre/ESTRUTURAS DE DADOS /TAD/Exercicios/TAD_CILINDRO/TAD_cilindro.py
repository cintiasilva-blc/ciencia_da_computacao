from __future__ import annotations
from dataclasses import dataclass

class Cilindro:
    altura: float
    raio: float
    
    def __init__(self, alt: float, r: float):
        self.altura = alt
        self.raio = r
        print('Cilindro criado com: ','\nAltura = ',self.altura, '\nRaio = ', self.raio)

    def cria_cilindro(h: float, r: float) -> Cilindro:
        C = Cilindro(h, r)
        return C

    def imprime_altura(self):
        print('Altura: ', self.altura)

    def imprime_raio(self):
        print('Raio: ', self.raio)

    def area_cilindro(self) -> float:
        return (2 * 3.14 * self.raio * (self.raio + self.altura))
    
    def volume_cilindro(self) -> float:
        return (3.14 * (self.raio * self.raio) * self.altura)
    
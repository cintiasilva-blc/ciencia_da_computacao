from __future__ import annotations
from dataclasses import dataclass

class Cilindro:
    h: float
    r: float

    def __init__(self, alt: float, raio: float):
        self.h = alt
        self.r = raio

    def cria_cilindro(a: float, b: float) -> Cilindro:
        c = Cilindro(a, b)
        return c

    def imprime_alt(self):
        print('Altura do cilindro: ', self.h)

    def imprime_raio(self):
        print('Raio do cilindro: ', self.r)

    def area(self):
        return (2*3.14*self.r*(self.r + self.h)) 
    
    def volume(self):
        return (3.14*(self.r**2)*self.h)
    

def main():
    a = 4
    b = 2

    c = Cilindro.cria_cilindro(a, b)

    c.imprime_alt()
    c.imprime_raio()
    print("Area do cilindro: ", c.area())
    print('Volume do cilindro: ', c.volume())


main()



        
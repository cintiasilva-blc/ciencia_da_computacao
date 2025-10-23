from TAD_ponto import *

def input():
    x: float = 2
    y: float = 3
    a: float = 4
    b: float = 5

    p3 = Ponto(5, 5) # Exemlo a não ser usado
    p1 = Ponto.cria_ponto(x, y)
    p2 = Ponto.cria_ponto(a, b)
    print('Distância entre os pontos: ', p1.distancia(p2))

    p1.imprime()

input()
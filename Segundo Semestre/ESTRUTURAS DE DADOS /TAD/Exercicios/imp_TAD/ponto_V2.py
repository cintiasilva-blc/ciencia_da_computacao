from TAD_ponto_v2 import *

def input():
    x: float = 1
    y: float = 2
    a: float = 3
    b: float = 4

    p1 = Ponto.cria_ponto(x, y)
    p2 = Ponto.cria_ponto(a, b)
    print('Distãncia entre dois pontos: ' , p1.distancia(p2))

    p1.imprime()

input()
from Revisao.TAD_cilindro import *


def input():
    alt: float = 5
    raio: float = 2

    c1 = Cilindro.cria_cilindro(alt, raio)
    c1.imprime_altura()
    c1.imprime_raio()
    
    print('Area do cilindro: ', c1.area_cilindro())
    print('Volume do cilindro: ', c1.volume_cilindro())

input()


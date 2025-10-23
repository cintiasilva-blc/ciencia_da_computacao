'''Considere um jogo onde o personagem está em um tabuleiro (semelhante a um tabuleiro de jogo
de xadrez). As linhas e colunas do tabuleiro são enumeradas de 1 a 10, dessa forma, é possível
representar a posição (casa) do personagem pelo número da linha e da coluna que ele se encontra. O
personagem fica virado para uma das direções: norte, sul, leste ou oeste. O jogador pode avançar o
seu personagem qualquer número de casas na direção que ele está virado, mas é claro, não pode sair do
tabuleiro. Projete uma função que indique a partir das informações do personagem, qual é o número
máximo de casas que ele pode avançar na direção que ele está virado'''

from dataclasses import dataclass
from enum import Enum, auto


class Direcao(Enum):
    NORTE = auto()
    SUL = auto()
    LESTE = auto()
    OESTE = auto()

@dataclass
class Personagem:
    linha: int
    coluna: int
    direcao: Direcao

def tabuleiro(p: Personagem) -> int:
    '''Recebe um *personagem* e a partir de suas informações indica o numero maximo de casas ele ainda pode avançar na direçao em que ele esta virado.
     
    >>> tabuleiro(Personagem(linha=4, coluna=2, direcao=Direcao.NORTE))
    6
    >>> tabuleiro(Personagem(linha=10, coluna=2, direcao=Direcao.NORTE))
    0
    >>> tabuleiro(Personagem(linha=4, coluna=2, direcao=Direcao.SUL))
    3
    >>> tabuleiro(Personagem(linha=1, coluna=2, direcao=Direcao.SUL))
    0
    >>> tabuleiro(Personagem(linha=4, coluna=2, direcao=Direcao.LESTE))
    8
    >>> tabuleiro(Personagem(linha=4, coluna=10, direcao=Direcao.LESTE))
    0
    >>> tabuleiro(Personagem(linha=4, coluna=2, direcao=Direcao.OESTE))
    1
    >>> tabuleiro(Personagem(linha=4, coluna=1, direcao=Direcao.OESTE))
    0
    '''

    if p.direcao == Direcao.NORTE:
        rest = 10 - p.linha
    elif p.direcao == Direcao.SUL:
        rest = p.linha - 1
    elif p.direcao == Direcao.LESTE:
        rest = 10 - p.coluna
    else:
        rest = p.coluna - 1
    return rest


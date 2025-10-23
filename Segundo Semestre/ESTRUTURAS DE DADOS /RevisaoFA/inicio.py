'''Projeto de programas
    Quais são as principais atividades no projeto de um programa?
    • Análise (identificação do problema)
    • Especificação (descrição do que o programa deve fazer)
    • Implementação
    • Verificação (a implementação atende a especificação?)
    
    Projeto de funções
    Podemos detalhar esse processo para o projeto de uma função específica:
    • Análise: identificar o problema a ser resolvido
    • Definição dos tipos de dados: identificar e definir como as informações serão representadas
    • Especificação: especificar com precisão o que a função deve fazer
    • Implementação: implementar a função de acordo com a especificação
    • Verificação: verificar se a implementação está de acordo com a especificação
    • Revisão: identificar e fazer melhorias

    import math : importacao do modulo;
        Piso: Maior inteiro <= ao número dado   EX: math.floor(-2.3) == -3
        Teto: Menor inteiro >= ao número dado   EX: math.ceil(-2.3)  == -2

    strings: 
        Conversão maiuscula: 'José'.upper() == 'JOSÈ'
        Conversão minuscula: 'José'.lower() == 'jośe'

    int(False) == 0
    int(True)  == 1
    '''

'''Considere um jogo onde o personagem está em um tabuleiro (semelhante a um tabuleiro de
jogo de xadrez). As linhas e colunas do tabuleiro são enumeradas de 1 a 10, dessa forma, é
possível representar a posição (casa) do personagem pelo número da linha e da coluna que ele
se encontra. O personagem fica virado para uma das direções: norte, sul, leste ou oeste. O
jogador pode avançar o seu personagem qualquer número de casas na direção que ele está
virado, mas é claro, não pode sair do tabuleiro. Projete uma função que indique a partir das
informações do personagem, qual é o número máximo de casas que ele pode avançar na
direção que ele está virado.'''

from enum import Enum, auto
from dataclasses import dataclass

class Direcao(Enum):
    '''A direçao em que o personagem esta virado.
    Para o norte o número da linha aumenta, pra o sul diminui.
    Para o leste o número da coluna aumenta, para o oeste diminui.
    '''
    NORTE = auto()
    SUL = auto()
    LESTE = auto()
    OESTE = auto()

@dataclass
class Posicao:
    '''A posicao em que o personagem se encontra no tabuleiro.
    A linha, deve estar entre 1 e 10.
    A coluna, deve estar entre 1 e 10.
    '''
    linha: int
    coluna: int

@dataclass
class Personagem:
    '''A posicao e a direçao em que o personagem se encontra.
    '''
    posicao: Posicao
    direcao: Direcao


def numero_max_direcao_tabuleiro(personagem: Personagem) -> int:
    '''Indica o número maximo de casas que o *personagem* pode avançar na direcao a qual ele esta virado de acordo com a posicao dele no tabuleiro.

    Exemplos:
    >>> numero_max_direcao_tabuleiro(Personagem(posicao=Posicao(linha=4, coluna=2), direcao=Direcao.NORTE))
    6
    >>> numero_max_direcao_tabuleiro(Personagem(posicao=Posicao(linha=10, coluna=2), direcao=Direcao.NORTE))
    0
    >>> numero_max_direcao_tabuleiro(Personagem(posicao=Posicao(linha=4, coluna=2), direcao=Direcao.SUL))
    3
    >>> numero_max_direcao_tabuleiro(Personagem(posicao=Posicao(linha=1, coluna=2), direcao=Direcao.SUL))
    0
    >>> numero_max_direcao_tabuleiro(Personagem(posicao=Posicao(linha=4, coluna=2), direcao=Direcao.LESTE))
    8
    >>> numero_max_direcao_tabuleiro(Personagem(posicao=Posicao(linha=4, coluna=10), direcao=Direcao.LESTE))
    0
    >>> numero_max_direcao_tabuleiro(Personagem(posicao=Posicao(linha=4, coluna=2), direcao=Direcao.OESTE))
    1
    >>> numero_max_direcao_tabuleiro(Personagem(posicao=Posicao(linha=4, coluna=1), direcao=Direcao.OESTE))
    0
    '''

    if personagem.direcao == Direcao.NORTE:
        casas = 10 - personagem.posicao.linha
    elif personagem.direcao == Direcao.SUL:
        casas = personagem.posicao.linha - 1
    elif personagem.direcao == Direcao.LESTE:
        casas = 10 - personagem.posicao.coluna
    else:
        casas = personagem.posicao.coluna - 1
    return casas
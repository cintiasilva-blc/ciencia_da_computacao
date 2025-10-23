'''Projete uma enumeração para representar as direções norte, leste, sul e oeste. Em seguida,
a) Projete uma função que indique a direção oposta de uma direção.
b) Projete uma função que indique qual é direção que está a 90 graus no sentido horário de outra
direção.
c) Projete uma função que indique qual é direção que está a 90 graus no sentido anti-horário de
outra direção. Use a função do item b para fazer a implementação (não use seleção nem operações
aritméticas nessa implementação).
'''

from enum import Enum, auto

class Direcao(Enum):
    NORTE = auto()
    SUL = auto()
    LESTE = auto()
    OESTE = auto()

def direcao_oposta(direcao: Direcao) -> Direcao:
    '''Recebe uma *direcao* e retorna sua oposta.

    Exemplos:
    >>> direcao_oposta(Direcao.NORTE).name
    'SUL'
    >>> direcao_oposta(Direcao.SUL).name
    'NORTE'
    >>> direcao_oposta(Direcao.LESTE).name
    'OESTE'
    >>> direcao_oposta(Direcao.OESTE).name
    'LESTE'
    '''

    if direcao == Direcao.NORTE:
        return Direcao.SUL
    elif direcao == Direcao.SUL:
        return Direcao.NORTE
    elif direcao == Direcao.LESTE:
        return Direcao.OESTE
    else:
        return Direcao.LESTE
    

def direcao_angular(direcao: Direcao) -> Direcao:
    '''Recebe uma *direcao* e retorna a que estiver 90 graus sentido horario da direcao dada.
    
    Exemplos:
    >>> direcao_angular(Direcao.NORTE).name
    'OESTE'
    >>> direcao_angular(Direcao.SUL).name
    'LESTE'
    >>> direcao_angular(Direcao.LESTE).name
    'NORTE'
    >>> direcao_angular(Direcao.OESTE).name
    'SUL'
    '''

    if direcao == Direcao.NORTE:
        return Direcao.OESTE
    elif direcao == Direcao.SUL:
        return Direcao.LESTE
    elif direcao == Direcao.LESTE:
        return Direcao.NORTE
    else:
        return Direcao.SUL
    

def direcao_anti_angular(direcao: Direcao) -> Direcao:
    '''Recebe uma *direcao* e retorna a que estiver 90 graus sentido anti-horario da direcao dada.
    
    Exemplos:
    >>> direcao_anti_angular(Direcao.NORTE).name
    'LESTE'
    >>> direcao_anti_angular(Direcao.SUL).name
    'OESTE'
    >>> direcao_anti_angular(Direcao.LESTE).name
    'SUL'
    >>> direcao_anti_angular(Direcao.OESTE).name
    'NORTE'
    '''

    dir = direcao_angular(direcao)
    return direcao_oposta(dir)
    
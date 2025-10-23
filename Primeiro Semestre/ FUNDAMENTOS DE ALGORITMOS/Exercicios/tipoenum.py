'''1)Projete uma fun ̧c ̃ao que receba como entrada a cor atual de um sem ́aforo de trˆansito e devolva
a pr ́oxima cor que ser ́a ativada (considere um sem ́aforo com trˆes cores: verde, amarelo e
vermelho).'''

from enum import Enum, auto
from dataclasses import dataclass

class Semaforo(Enum):
    VERDE = auto()
    AMARELO = auto()
    VERMELHO = auto()

def CorSemaforo(cor: Semaforo) -> str:
    '''Exemplos:
    >>> CorSemaforo(Semaforo.VERDE).name
    'AMARELO'
    >>> CorSemaforo(Semaforo.VERMELHO).name
    'VERDE'
    >>> CorSemaforo(Semaforo.AMARELO).name
    'VERMELHO'
    '''

    if cor == Semaforo.AMARELO:
        sem = Semaforo.VERMELHO
    elif cor == Semaforo.VERDE:
        sem = Semaforo.AMARELO
    else:
        sem = Semaforo.VERDE
    return sem

'''2)Dizemos que o nome de uma pessoa  ́e curto se tem no m ́aximo quatro letras e longo se tem
mais que 8 letras. Um nome que n ̃ao  ́e nem curto e nem longo  ́e mediano. Projete uma fun ̧c ̃ao
que classifique um nome de acordo com seu n ́umero de letras.'''

class TamanhoNome(Enum):
    LONGO = auto()
    MEDIANO = auto()
    CURTO = auto()


def ClassificaCompNome(nome: str) -> str:
    '''Exemplos:
    >>> ClassificaCompNome("cintia")
    'MEDIANO'
    >>> ClassificaCompNome("Maria Clara")
    'LONGO'    
    >>> ClassificaCompNome("ana")
    'CURTO'
    '''

    if len(nome) <= 4:
        tam = TamanhoNome.CURTO.name
    elif len(nome) > 8:
        tam = TamanhoNome.LONGO.name
    else:
        tam = TamanhoNome.MEDIANO.name
    return tam

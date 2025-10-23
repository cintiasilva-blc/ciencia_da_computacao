'''Projete uma função que determine o sinal de um número, produzindo -1 para valores negativos, 1 para
valores positivos e 0 para o 0.'''

def determina_sinal(num: int) -> int:
    '''Determina o sinal de *num* e retorna:
     1 se num > 0
    -1 se num < 0
     0 se num = 0

    Exemplos:
    >>> determina_sinal(-5)
    -1
    >>> determina_sinal(10)
    1
    >>> determina_sinal(0)
    0
    '''

    if num > 0:
        sinal = 1
    elif num < 0:
        sinal = -1
    else:
        sinal = 0
    return sinal
'''O Brasil institui há algum tempo um sistema de bandeira tarifária para sinalizar ao consumidores
os custos reais de geração de energia. Nesse sistema, a bandeira verde indica condições favoráveis
de geração de energia e a tarifa não sofre acréscimo. Já a bandeira amarela indica condições menor
favoráveis e por isso a tarifa sofre um acréscimo de R$ 0,01874 para cada quilowatt-hora. A bandeira
vermelha - patamar 1 indica condições mais custosas de geração e o acréscimo na tarifa é de R$ 0,03971
para cada quilowatt-hora consumido. Por fim, a bandeira vermelha - patamar 2 indica condições ainda
mais custosas e o acréscimo na tarifa é de R$ 0,09492 para cada quilowatt-hora consumido. Projete
uma função que determine o valor final que o consumidor tem que pagar dado o seu consumo em
quilowatt-hora, a tarifa básica do quilowatt-hora e a bandeira tarifária.'''

from enum import Enum, auto

class Bandeira(Enum):
    VERDE = 0
    AMARELA = 0.01874
    VERMELHA_1 = 0.03971
    VERMELHA_2 = 0.09492

def valor_final_consumidor(consumo_kw: int, bandeira: Bandeira, tarifa_basica: float) -> float:
    '''Recebe o consumo em quilowatt-hora, a tarifa basica do quilowatt-hora e a bandeira tarifária,
    calcula o valor final que o consumidor deve pagar.
    
    Exemplos:
    >>> valor_final_consumidor(230, Bandeira.VERDE, 0.725)
    166.75
    >>> valor_final_consumidor(230, Bandeira.AMARELA, 0.725)
    171.06
    >>> valor_final_consumidor(230, Bandeira.VERMELHA_1, 0.725)
    175.88
    >>> valor_final_consumidor(230, Bandeira.VERMELHA_2, 0.725)
    188.58
    '''

    if bandeira == Bandeira.VERDE:
        valor_final = consumo_kw * tarifa_basica
    elif bandeira == Bandeira.AMARELA:
        valor_final = consumo_kw * (Bandeira.AMARELA.value + tarifa_basica)
    elif bandeira == Bandeira.VERMELHA_1:
        valor_final = consumo_kw * (Bandeira.VERMELHA_1.value + tarifa_basica)
    else:
        valor_final = consumo_kw * (Bandeira.VERMELHA_2.value + tarifa_basica)

    return round(valor_final, 2)
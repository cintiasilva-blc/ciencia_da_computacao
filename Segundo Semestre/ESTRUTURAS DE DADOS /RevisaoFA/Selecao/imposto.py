'''Cada cidadão de um país, cuja moeda chama dinheiro, tem que pagar imposto sobre a sua renda.
Cidadãos que recebem até 1000 dinheiros pagam 5% de imposto. Cidadãos que recebem entre 1000 e
5000 dinheiros pagam 5% de imposto sobre 1000 dinheiros e 10% sobre o que passar de 1000. Cidadãos
que recebem mais do 5000 dinheiros pagam 5% de imposto sobre 1000 dinheiros, 10% de imposto sobre
4000 dinheiros e 20% sobre o que passar de 5000. Projete uma função que calcule o imposto que um
cidadão deve pagar dado a sua renda.'''

def calcula_imposto(renda: float) -> float:
    ''' Calcula o imposto aplicado dado a *renda*.
    
    Exemplos:
    >>> calcula_imposto(855.43)
    42.77
    >>> calcula_imposto(2750.0)
    225.0
    >>> calcula_imposto(8932.5)
    1629.75
    '''

    if renda <= 1000:
        imposto = renda * 0.05
    elif renda > 1000 and renda <= 5000:
        imposto = 50 + ((renda - 1000) * 0.1)
    else:
        imposto = 50 + ((renda - 1000) * 0.1) + ((renda - 5000) * 0.2)
    return round(imposto, 2)


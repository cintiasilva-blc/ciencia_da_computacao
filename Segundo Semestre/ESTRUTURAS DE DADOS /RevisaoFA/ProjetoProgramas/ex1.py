'''2) Implemente a função de acordo com a especificação a seguir. Corrija a especificação se necessário.'''

def isento_tarifa(idade: int) -> bool:
    ''' Produz True se uma pessoa de *idade* anos é isento da tarifa de transporte
    público, isto é, tem menos que 18 anos ou 65 ou mais. Produz False caso
    contrário.
    Exemplos
    >>> isento_tarifa(17)
    True
    >>> isento_tarifa(18)
    False
    >>> isento_tarifa(50)
    False
    >>> isento_tarifa(65)
    True
    >>> isento_tarifa(70)
    True
    '''

    if idade < 18 or idade >= 65:
        return True
    else:
        return False
    
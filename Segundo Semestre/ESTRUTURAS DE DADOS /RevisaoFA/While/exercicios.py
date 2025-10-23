'''Projete uma função que verifique se uma lista de números é dobrada, isto é, pode ser obtida pela
concatenação de duas listas iguais (não use operações de sublista).'''

def verifa_lista_dobrada(lista: list[int]) -> bool:
    '''Recebe uma lista de numeros e retorna True se ela pode ser obtida atraves da concatenação de duas listas iguais
    
    Exemplos:           
    >>> verifa_lista_dobrada([4, 8, 12])
    False
    >>> verifa_lista_dobrada([1, 2, 1, 2])
    True
    '''

    if len(lista) % 2 != 0:
        return False

    metade = len(lista) // 2
    i = 0
    while i < metade:
        if lista[i] != lista[i + metade]:
            return False
        i += 1
    return True


'''Projete uma função que determine qual é a menor quantidade de elementos de uma lista que precisam
ser somados (a partir do início da lista) para que a soma seja maior que um dado valor. Se não for
possível atingir a soma desejada, a função deve devolver -1.'''

def determina_soma(lista: list[int], num: int) -> int:
    '''Recebe uma lista de numeros e um valor, retorna a soma dos elementos da lista até que ultrapasse o valor dado, Caso contrario retorna -1
    
    Exemplos:
    >>> determina_soma([1,2,3,4], 10)
    -1
    >>> determina_soma([1,2,3,4], 5)
    3
    '''

    i = 0
    soma = 0

    while i < len(lista):
        soma += lista[i]
        if soma > num:
            return i + 1
        i += 1
    return -1
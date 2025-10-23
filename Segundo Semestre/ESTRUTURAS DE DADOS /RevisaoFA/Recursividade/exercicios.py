'''Projete uma função recursiva que concatene todas as strings de uma lista de strings.'''

def concatena_list_str(lista: list[str]) -> str:
    '''Recebe um lista de strings e concatena todos esses elementos em uma unica str
    
    Exemplos:
    >>> concatena_list_str(['a', 'b', 'c'])
    'abc'
    >>> concatena_list_str(['bom', ' dia'])
    'bom dia'
    '''

    if len(lista) == 0:
        return ''
    elif len(lista) == 1:
        return lista[0]
    else:
        rec = concatena_list_str(lista[1:])
        return lista[0] + rec

''' Uma lista de números é chamada de lista binária se todos os seus elementos são 0 ou 1. Projete uma função recursiva que verifique se uma lista é binária.'''

def verifica_lista_bin(lista: list[int]) -> bool:
    '''Recebe uma lista de numeros e verifica de todos os elementos sao 0 ou 1
    
    Exemplos:
    >>> verifica_lista_bin([0])
    True
    >>> verifica_lista_bin([1, 0, 1, 0])
    True
    >>> verifica_lista_bin([1, 2, 3, 4])
    False
    >>> verifica_lista_bin([2, 1, 0])
    False'''

    if len(lista) == 0:
        return True
    elif len(lista) == 1:
        if lista[0] == 1 or lista[0] == 0:
            return True
        else:
            return False
    else:
        if lista[0] == 0 or lista[0] == 1:
            return verifica_lista_bin(lista[1:])
        else:
            return False
           
''' Projete uma função recursiva que receba como entrada uma string e um número inteiro positivo n e
gere uma nova string adicionando n vezes o símbolo de exclamação no final da string da entrada. Por
exemplo, se a string for 'Gol' e n = 4, a saída deve ser 'Gol!!!!'. Não use o operador de repetição
de string (*)!. '''

def exclamacao(palavra: str, n: int) -> str:
    '''Recebe uma palavra e um numero n, gera uma nova string add '!' *n*vezes a direita da *palavra*
    
    Exemplos:
    >>> exclamacao('Gol', 5)
    'Gol!!!!!'
    >>> exclamacao('Gol', 3)
    'Gol!!!'
    >>> exclamacao('Gol', 1)
    'Gol!'
    >>> exclamacao('Gol', 0)
    'Gol'
    '''

    if n == 0:
        return palavra 
    else:
        return exclamacao(palavra + '!', n -1)


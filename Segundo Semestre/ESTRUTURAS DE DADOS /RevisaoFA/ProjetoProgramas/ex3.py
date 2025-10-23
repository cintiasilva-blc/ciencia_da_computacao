'''Você está fazendo um programa e precisa verificar se um texto digitado pelo usuário está de acordo
com algumas regras. A regra “sem espaços extras” requer que o texto não comece e não termine com
espaços. Projete uma função que verifique se um texto qualquer está de acordo com a regra “sem
espaços extras”.
'''

def sem_espaços_extras(text: str) -> bool:
    '''Verifica se nao tem espaços no começo ou no final do *text*.
    Retorna False, caso contrario.
    
    Exemplos:
    >>> sem_espaços_extras('Ana Paula')
    True
    >>> sem_espaços_extras(' Ola, Bom dia! ')
    False
    >>> sem_espaços_extras(' Ana Paula')
    False
    >>> sem_espaços_extras('Ana Paula ')
    False
    '''

    if text[0] == ' ' or text[-1] == ' ':
        return False
    else: 
        return True

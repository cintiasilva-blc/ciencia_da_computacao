'''Projete uma função que transforme uma string para que ela tenha uma quantidade n caracteres. Se a
string tem mais caracteres que n, os caracteres excedentes do final devem ser removidos. Se a string
tem menos caracteres que n, espaços em branco deve ser adicionados no final.'''

def transforma_string(texto: str, n: int) -> str:
    '''Transforma *texto* para uma quantidade de caracteres igual a *n*.
    
    Exemplos:
    >>> transforma_string('ola', 5)
    'ola  '
    >>> transforma_string('Bom dia', 3)
    'Bom'
    >>> transforma_string('Cintia', 6)
    'Cintia'
    '''

    if len(texto) != n:
        if len(texto) < n:
            return texto + ((n - len(texto)) * ' ')
        else:
            return texto[:n]
    else:
        return texto
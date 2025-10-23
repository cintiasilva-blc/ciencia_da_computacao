from TADPilha import *

def aplica_op(op: str, a: int, b: int) -> int:
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        return a // b
def avalia_posfixa(expr: list[str]) -> int:
    '''Recebe uma lista de operadoeres e operandos, avalia a expressão e aplica

    Exemplos:
    >>> avalia_posfixa(['102'])
    102
    >>> avalia_posfixa(['55', '5', '/'])
    11
    >>> avalia_posfixa(['5', '6', '*', '3', '+'])
    33
    >>> avalia_posfixa(['5', '-6', '*', '3', '+', '10', '-'])
    -37
    '''

    operadores = ['+', '-', '*', '/']
    p = pilha(20)

    for i in expr:
        if i not in operadores:
            p.empilha(item(int(i)))
        else:
            v1 = p.consulta_topo().valor
            p.desempilha()
            v2 = p.consulta_topo().valor
            p.desempilha()
            result = aplica_op(i, v2, v1)
            p.empilha(item(result)) 
    return p.consulta_topo().valor         

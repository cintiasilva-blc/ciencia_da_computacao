def SomaNaturais(n: int) -> int:
    '''Recebe um numero *n* natural e retorna a soma da decomposição do mesmo
    Exemplos:
    >>> SomaNaturais(5)
    15
    >>> SomaNaturais(0)
    0
    '''

    if n == 0:
        return 0
    else:
        return n + SomaNaturais(n-1)
    


def Fatorial(n: int) -> int:
    '''Recebe um numero *n* e retorna seu fatorial
    Exemplos:
    >>> Fatorial(5)
    120
    >>> Fatorial(1)
    1
    >>> Fatorial(0)
    1
    '''

    if n == 0:
        return 1
    else:
        return n * Fatorial(n-1)
    
def main():
    n = int(input("Digite um número natural: "))
    a = int(input("Digite um número: "))
    print()
    print('Soma: ', SomaNaturais(n))
    print('Fatorial: ', Fatorial(n))
    print('Exponencia: ', Exponencial(a, n))

if __name__ == '__main__':
    main()
    


def Exponencial(a: float, n: int) -> float:
    '''Recebe um numero *a* maior que 0 e um numero natural *n*, calcula o exponencial de *n* elevado a *a* (a ** n)
    Exemplos:
    >>> Exponencial(3, 0)           
    1
    >>> Exponencial(0, 2)           # 0 * 0 = 0
    0
    >>> Exponencial(2, 3)           # 2 * 2 * 2 = 8
    8
    '''

    if n == 0:
        return 1
    else:
        return a * Exponencial(a, n-1)
'''1. Projete uma fun ̧c ̃ao recursiva que some todos os n ́umeros naturais menores ou
iguais que um determinado n.'''

def SomaMenoresN(n: int) -> int:
    '''Recebe um numero natural *n* e soma todos os numeros menores ou iguais a ele
    Exemplos:
    >>> SomaMenoresN(5)
    15
    >>> SomaMenoresN(2)
    3
    >>> SomaMenoresN(0)
    0
    '''

    if n == 0:
        return 0
    else:
        return n + SomaMenoresN(n - 1)
    

'''2. Projete uma fun ̧c ̃ao recursiva que receba como entrada um n ́umero a 6= 0 e um
n ́umero natural n e calcule o valor a**n
'''

def Potencia(n: int, a: int) -> int:
    '''Recebe um numero natrural *n* e um numero *a* diferente de zero
    Exemplos:
    >>> Potencia(2, 3)
    9
    >>> Potencia(0, 2)
    1
    '''

    if n == 0:
        return 1
    else:
        return a * Potencia(n - 1, a)
    

'''3. Projete uma fun ̧c ̃ao recursiva que calcule o fatorial de n, isto  ́e, o produto dos
n primeiros n ́umeros naturais maiores que 0.'''

def Fatorial(n: int) -> int:
    '''Recebe um numero inteiro *n* e retorna seu fatorial
    Exemplos:
    >>> Fatorial(5)
    120
    >>> Fatorial(2)
    2
    '''

    if n == 1:
        return 1
    else:
        return n * Fatorial(n - 1)
    

'''4. Fa ̧ca uma fun ̧c ̃ao recursiva, que calcule o valor da s ́erie S descrita a seguir para
um valor n > 0 a ser fornecido como parˆametro para a mesma: S = 1 + 1/1!
+ 1/2! + 1/3! + ... + 1 /n!.'''

def S(n: int) -> float:
    '''Recebe uma valor *n* maior que zero e retorna a serie *S = 1 + 1/ 1! + 1/2! ... + 1/n!*\n
    Exemplos:
    >>> S(1)
    2
    >>> S(3)
    2.66666667
    '''


    

'''5. Fa ̧ca uma fun ̧c ̃ao recursiva para multiplica ̧c ̃ao de dois n ́umeros naturais, atrav ́es
de somas sucessivas (Ex.:6 ∗ 4 = 4 + 4 + 4 + 4 + 4 + 4).'''

def MultiplicaporSoma(a: int, b: int) -> int:
    '''Recebe dois numeros naturais e retorna o produto deles por meio de somas consecutivas.\n
    Exemplos:
    >>> MultiplicaporSoma(6, 4)             # 4 + 4 + 4 + 4 + 4 + 4
    24
    >>> MultiplicaporSoma(0, 5)             # 0
    0
    >>> MultiplixaporSoma(3, 1)             # 1 + 1 + 1 
    1
    '''


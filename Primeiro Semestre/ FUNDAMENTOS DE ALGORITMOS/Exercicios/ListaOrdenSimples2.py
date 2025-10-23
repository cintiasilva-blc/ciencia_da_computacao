'''1) Considera uma string como sendo a entrada de uma fun ̧c ̃ao. Ordena as letras da string em
ordem alfab ́etica utilizando a ordena ̧c ̃ao por inser ̧c ̃ao.'''

def OrdenacaoString(palavra: str) -> list:
    '''Recebe uma palavra e ordena em ordem alfabetica
    Exemplos:
    >>> OrdenacaoString('ola')
    'alo'
    >>> OrdenacaoString('cintia')
    'aciint'
    >>> OrdenacaoString('hoje')
    'ehjo'
    '''

    lista = list(palavra)

    for i in range(1, len(lista)):
        pivo = palavra[i]
        j = i - 1
        while j >= 0 and pivo < lista[j]:
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = pivo
    
    palv = ''
    for a in lista:
        palv = palv + a
    return palv

'''2) Considere o m ́etodo BubbleSort visto em sala. desenvolva uma fun ̧c ̃ao que utilize o mesmo
princ ́ıpio, por ́em com sucessivas passagens em dire ̧c ̃oes opostas.'''

def BubbleSortOposto(arranjo: list) -> list:
    '''Recebe uma lista de números e ordena do menor para o maior em direções opostas até se encontrarem
    Exemplos:
    >>> BubbleSortOposto([3,4,9,2,10,5,8,1,7,6])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    '''
     
    n = len(arranjo)
    for i in range(n):
        for j in range(0, n-i-1):
            if arranjo[j] > arranjo[j + 1]:
                aux = arranjo[j]
                arranjo[j] = arranjo[j + 1]
                arranjo[j + 1] = aux
            if arranjo[-1] < arranjo[j - 1]:
                aux = arranjo[-1]
                arranjo[-1] = arranjo[j - 1]
                arranjo[j - 1] = aux
    return arranjo
    

'''3) Uma fun ̧c ̃ao recebe dois arranjos num ́ericos ordenados. A fun ̧c ̃ao deve retornar um arranjo
ordenado que seja o resultado da intercala ̧c ̃ao desses dois arranjos.'''

def OrdenaArranjosOrd(array1: list, array2: list) -> list:
    ''' Recebe dois arranjos ordenados e intercala os dois retornando outro arranjo ainda ordenado
    Exemplos:
    >>> OrdenaArranjosOrd([3,4,9,2,10], [5,8,1,7,6])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> OrdenaArranjosOrd([5,4,3],[2,1])
    [1, 2, 3, 4, 5]
    '''
    
    arranjo = []
    if array1[0] < array2[0]:
            arranjo.append(array1[0])
    for a in array:
        array1.append(array2[a])
    arranjo.append(array1)

    n = len(arranjo)
    for i in range(n):
        for j in range(0, n-i-1):
            if arranjo[j] > arranjo[j + 1]:
                aux: int = arranjo[j]
                arranjo[j] = arranjo[j + 1]
                arranjo[j + 1] = aux

    return arranjo

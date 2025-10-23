'''Projete uma função que receba como parâmetros uma lista e um índice i e modifique a lista removendo
o elemento do índice i.
Dica: mova o elemento do índice i até o final e depois use list.pop para removê-lo. A função list.pop
funciona da seguinte forma
'''

def remove_indice(lista: list[int], i: int):
    '''Recebe uma lista de numeros e um indice, remove o elemento do indice dado
    
    Exemplos:
    >>> lst = [7, 1, 8, 9]
    >>> remove_indice(lst, 2)
    >>> lst
    [7, 1, 9]
    >>> lista = [1, 2, 3]
    >>> remove_indice(lista, 0)
    >>> lista
    [2, 3]
    '''

    for j in range(i, len(lista)-1):
        lista[j] = lista[j + 1]

    lista.pop()

    


            

        
            

            
        
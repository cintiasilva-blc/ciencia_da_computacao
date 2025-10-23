def SomaElementos(lista: list[int]) -> int:
    '''Retorna a soma de todos os elementos da *lista*
    Exemplos:
    >>> SomaElementos([3, 5, 2, 4])
    14
    >>> SomaElementos([1, 6])
    7
    '''

    if len(lista) == 0:
        return 0
    else:
        return SomaElementos(lista[1:]) + lista[0]
    



def MaiorElemento(lista: list[int]) -> int:
    '''Retorna o maior elemento da *lista*
    Exemplos:
    >>> MaiorElemento([1, 2, 3, 4])
    4
    >>> MaiorElemento([8, 2, 5, 3])
    8
    '''

    if len(lista) == 1:
        return lista[0]
    else:
        maior: int = MaiorElemento(lista[1:])
        if lista[0] > maior:
            return lista[0]
        else:
            return maior
        

def QuantoAparece(lista: list[int], elemento: int) -> int:
    '''Retorna quantas vezes o *elemento* aparece na *lista*
    Exemplos:
    >>> QuantoAparece([1, 2, 3, 1, 1], 1)
    3
    >>> QuantoAparece([8, 2, 3, 7], 4)
    0
    >>> QuantoAparece([2, 2, 2, 2, 2], 2)
    5
    '''

    if lista == []:
        return 0
    else:
        contador = 1 + QuantoAparece(lista[1:], elemento)
        if elemento == lista[0]:
            return contador
        else:
            return QuantoAparece(lista[1:], elemento)


def main():

    print(lista)
    lista = [8, 2, 3, 7]
    elemento: int = input(("Digite um número inteiro: "))
    
    print("Maior Elemento: ", MaiorElemento(lista))
    print("Soma dos Elementos: ",SomaElementos(lista))
    print("Quanto aparece:",QuantoAparece(lista, elemento))

if __name__ == '__main__':
    main()
    
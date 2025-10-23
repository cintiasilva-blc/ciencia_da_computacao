''' Em um determinado jogo de construção de itens, cada item tem uma classe que varia de 1 a 10. Os
item de classe 1 surgem conforme o jogador explorar os baús. Um item de classe 2 ou superior precisa
ser construídos unindo dois itens da classe anterior. Por exemplo, para construir um item de classe
2 é necessário unir dois item de classe 1. Para construir um item de classe 10 é necessário unir dois
item de classe 9. Projete uma função que receba como entrada um número n (de 1 a 10), e determine
quantos itens de classe 1 são necessário para construir um item de classe n. Suponha que a únicas
operações aritméticas disponíveis seja a soma e a multiplicação.'''

def determina_itens(n: int) -> int:
    '''Recebe um numero e determina a quantidade de itens de classe 1 necessarios para construir um item de classe *n* 
    
    Exemplos:
    >>> determina_itens(1)
    1
    >>> determina_itens(2) 
    2
    >>> determina_itens(3)
    4
    >>> determina_itens(4)
    8
    '''

    i = 2
    result = 1
    while i <= n:
        i += 1
        result *=  2
    return result





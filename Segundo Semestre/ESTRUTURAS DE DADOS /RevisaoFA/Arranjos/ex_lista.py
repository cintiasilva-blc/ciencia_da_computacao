'''Projete uma função que concatene todos os elementos de uma lista de strings.'''

def concatena_lista(lista: list[str]) -> str:
    ''' Recebe uma lista de strings e concatena todos os elementos da mesma
    
    Exemplos:
    >>> concatena_lista(['bom', 'dia'])
    'bomdia'
    >>> concatena_lista(['abc', 'de', 'fghi'])
    'abcdefghi'
    '''

    palavra = ''

    for i in lista:
        palavra += i
    return palavra

'''Projete uma função que conte quantas vezes o valor mínimo de uma lista de inteiros não vazia aparece
na lista.
a) Esboce uma solução em duas etapas e depois implemente a função.
b) Faça uma implementação alternativa que use apenas uma repetição.
c) Avalie qual das implementações é mais simples.'''

'''Solucao:
    - Criar um contador e percorrer a lista procurando por n.
'''

def conta_ocorrências(lista: list[int], n: int) -> int:
    '''Recebe uma *lista* de números inteiros e conta quantas vezes *n* aparece na lista.
    
    EXemplos:
    >>> conta_ocorrências([1,2,3,3,3], 1)
    1
    >>> conta_ocorrências([1,2,4,6,2,2,1], 2)
    3
    >>> conta_ocorrências([1,2,3,3,3,1], 9)
    0
    '''

    cont = 0
    for i in lista:
        if i == n:
            cont += 1
    return cont

'''Projete uma função que receba como entrada uma lista lst de números e crie uma nova lista colocando
os valores negativos de lst antes dos positivos.'''

def ordem_crescente(lista: list[int]) -> list[int]:
    '''Recebe uma lisat de números inteiros e reorganiza os negativos antes dos positivos.
    
    Exemplos:
    >>> ordem_crescente([1,2,3, -1,-2,-3])
    [-1, -2, -3, 1, 2, 3]
    '''

    pos = []
    neg = []

    for i in lista:
        if i < i + 1 and i < 0:
            neg.append(i)
        if i < i + 1 and i > 0:
            pos.append(i)
    return neg + pos
    

'''Projete uma função que encontre as posições de todas as ocorrências de um nome em uma lista de
nomes.'''

def encontra_ocorrencias_nome(lista: list[str], nome: str) -> list[int]:
    '''Recebe uma lista de nomes e retorna todas as posiçoes em que *nome* for encontrado

    Exemplos:
    >>> encontra_ocorrencias_nome(['cintia', 'giovana', 'cintia', 'nikolas'], 'nikolas')
    [3]
    >>> encontra_ocorrencias_nome(['cintia', 'giovana', 'nikolas'], 'cintia')
    [0]
    >>> encontra_ocorrencias_nome(['cintia', 'giovana', 'cintia', 'nikolas'], 'cintia')
    [0, 2]
    >>> encontra_ocorrencias_nome(['cintia', 'cintia', 'cintia', 'cintia'], 'cintia')
    [0, 1, 2, 3]
    '''

    result = []
    cont = -1

    for i in lista:
        cont += 1
        if i == nome:
            result.append(cont)     
    return result

'''A Láurea Acadêmica é uma homenagem prestada a alunos que tiveram elevado nível de aproveitamento
no curso de graduação. Na UEM, todos os alunos que tiveram mais do que 2/3 das notas finais das
disciplinas maiores do que 9,0 recebem esta homenagem. Projete um programa que receba as notas
finais de um aluno e determine se ele receberá a Láurea Acadêmica.'''

def verifica_laurea(notas: list[float]) -> bool:
    '''Recebe uma lista de notas e verifica se pelo menos 2/3 dessas notas estao acima de 9.0,
    Caso contrario retorna False
    
    Exemplos:
    >>> verifica_laurea([10, 9.5, 9.9, 8.0])
    True
    >>> verifica_laurea([5.0, 9.5, 9.0])
    False
    >>> verifica_laurea([6.0, 7.5, 9.0, 6.7])
    False
    '''

    nova_lista = []

    for i in notas:
        if i > 9.0:
            nova_lista.append(i)
    
    if len(nova_lista) >= (2/3) * len(notas):
        return True
    else: 
        return False
        
    
'''Ordenação por seleção é um algoritmo para ordenar uma lista de valores. A ideia do algoritmo é
selecionar um valor mínimo da lista a partir da posição 0 e colocá-lo na posição 0, depois encontrar
um valor mínimo da lista a partir da posição 1 e colocá-lo na posição 1, depois encontrar um valor
mínimo da lista a partir da posição 2 … e assim por diante. Por exemplo, vamos considerar a lista
[8, 5, 4, 1, 2].
O valor mínimo a partir da posição 0 é 1 (que está no índice 3), colocando 1 na posição 0, obtemos
[1, 5, 4, 8, 2].
O valor mínimo a partir da posição 1 é 2 (que está no índice 4), colocando 2 na posição 1, obtemos
[1, 2, 4, 8, 5].
O valor mínimo a partir da posição 2 é 4 (que está no índice 2), colocando 4 na posição 2, obtemos
[1, 2, 4, 8, 5].
O valor mínimo a partir da posição 3 é 5 (que está no índice 4), colocando 5 na posição 3, obtemos
[1, 2, 4, 5, 8].
Baseado nesta descrição, projete uma função que faça a ordenação dos valores usando o algoritmo de
ordenação por seleção.'''

def ordenacao_selecao(lista: list[int]):
    '''Recebe uma lista de valores e os ordena do menor ao maior
    
    Exemplos:
    >>> lst = [8, 5, 4, 1, 2]
    >>> ordenacao_selecao(lst)
    >>> lst
    [1, 2, 4, 5, 8]
    '''

    n = len(lista)

    for i in range(0, n):
        menor = i
        for j in range(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j
        aux = lista[i]
        lista[i] = lista[menor]
        lista[menor] = aux
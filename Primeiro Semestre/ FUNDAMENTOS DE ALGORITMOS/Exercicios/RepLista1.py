'''1. Projete uma fun ̧c ̃ao que receba como entrada uma lista lst de n ́umeros e crie uma nova lista
colocando os valores negativos de lst antes dos positivos'''

def ListaNumCrescentes(lst: list[int]) -> list:
    '''Coloca os valores negativos de uma lista antes dos positivos
    Exemplos:
    >>> ListaNumCrescentes([1, -1, 3, 2])
    [-1, 1, 3, 2]
    >>> ListaNumCrescentes([-1, 2, 3, 4])
    [-1, 2, 3, 4]
    >>> ListaNumCrescentes([1, 2, 3, -4])
    [-4, 1, 2, 3]
    '''

    nova_lista = []

    for i in lst:
        if i < 0:
            nova_lista.append(i)
    for i in lst:
        if i > 0:
            nova_lista.append(i)

    return nova_lista


'''2) Uma elei ̧c ̃ao  ́e realizada com apenas dois candidatos. Cada eleitor pode votar ou no primeiro
candidato, ou no segundo candidato, ou ainda, votar em branco. O candidato que tiver mais
votos ganha a elei ̧c ̃ao. Se os votos em branco forem mais do que 50% do total de votos, novas
elei ̧c ̃oes devem ser convocadas. Projete uma fun ̧c ̃ao que receba como entrada uma lista n ̃ao
vazia de votos e determine qual foi o resultado da elei ̧c ̃ao. Dica: suponha a existˆencia de
uma fun ̧c ̃ao auxiliar que conte votos de um tipo especificado por parˆametro. Em um segundo
momento, desenvolva essa fun ̧c ̃ao.'''

from enum import Enum, auto
from dataclasses import dataclass

class Voto:
    CANDIDATO1 = 1
    CANDIDATO2 = 2
    BRANCO = 3

def ContaVotos(lista: list[Voto], quem: Voto) -> int:
    '''Conta os votos da lista de acordo com o parametro *quem*
    Exemplos:
    >>> ContaVotos([Voto.CANDIDATO1, Voto.CANDIDATO2, Voto.BRANCO, Voto.CANDIDATO1,Voto.CANDIDATO1], Voto.CANDIDATO1)
    3
    >>> ContaVotos([Voto.CANDIDATO1, Voto.CANDIDATO2, Voto.BRANCO, Voto.CANDIDATO1, Voto.CANDIDATO2, Voto.CANDIDATO2], Voto.BRANCO)
    1
    >>> ContaVotos([Voto.CANDIDATO1, Voto.BRANCO, Voto.CANDIDATO1, Voto.CANDIDATO1, Voto.CANDIDATO1], Voto.CANDIDATO2)
    0
    '''

    contador = 0

    for i in lista:
        if i == quem:
            contador += 1
    return contador
            
def GanhadorEleicao(votos: list[Voto]) -> Voto:
    '''Exemplos: 
    >>> GanhadorEleicao([Voto.CANDIDATO1, Voto.CANDIDATO2, Voto.BRANCO, Voto.CANDIDATO1,Voto.CANDIDATO1])
    'CANDIDATO1'
    >>> GanhadorEleicao([Voto.CANDIDATO1, Voto.BRANCO, Voto.BRANCO, Voto.BRANCO,Voto.CANDIDATO1])
    'Novas eleições devem ser convocadas!'
    >>> GanhadorEleicao([Voto.CANDIDATO1, Voto.CANDIDATO2, Voto.BRANCO, Voto.CANDIDATO2,Voto.CANDIDATO1])
    'Novas eleições devem ser convocadas!'
    '''
    

    for v in votos:
        if ContaVotos(votos, Voto.BRANCO) > ContaVotos(votos, Voto.CANDIDATO1) and ContaVotos(votos,Voto.BRANCO) > ContaVotos(votos, Voto.CANDIDATO2) or ContaVotos(votos, Voto.CANDIDATO1) == ContaVotos(votos, Voto.CANDIDATO2):
            return 'Novas eleições devem ser convocadas!'
        elif ContaVotos(votos, Voto.CANDIDATO1) > ContaVotos(votos, Voto.CANDIDATO2):
            return 'CANDIDATO1'
        else:
            return 'CANDIDATO2'
        
        
        

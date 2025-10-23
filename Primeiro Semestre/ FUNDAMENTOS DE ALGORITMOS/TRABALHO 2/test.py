from enum import Enum, auto
from dataclasses import dataclass

class Resultado(Enum):
    VITORIA = 3
    EMPATE = 1
    DERROTA = 0

@dataclass
class Jogo:
    anfitriao: str
    gols_anfi: int
    visitante: str
    gols_visitante: int

@dataclass 
class DadosTime:
    nome: str
    pontos_totais: int
    vitorias: int
    saldo_gols: int
    gols_sofridos: int
    jogos_anfi: int
    pontos_anfi: int   

def NomeTime(times: list[Jogo],) -> list[str]:
    '''Recebe uma lista de jogos(do tipo *Jogo*), separa somente o nome dos times e verifica se há repetiçao,
    Retorna uma lista com o nome dos times sem repetir.

    Exemplo:
    >>> NomeTime([Jogo(anfitriao='Sao-Paulo', gols_anfi=1, visitante='Atletico-MG', gols_visitante=2), Jogo(anfitriao='Flamengo', gols_anfi=2, visitante='Palmeiras', gols_visitante=1)])
    ['Sao-Paulo', 'Atletico-MG', 'Flamengo', 'Palmeiras']
    >>> NomeTime([Jogo(anfitriao='Sao-Paulo', gols_anfi=1, visitante='Atletico-MG', gols_visitante=2), Jogo(anfitriao='Sao-Paulo', gols_anfi=2, visitante='Palmeiras', gols_visitante=1)])
    ['Sao-Paulo', 'Atletico-MG', 'Palmeiras']
    '''

    nomes = []

    ''' 
    while i < len(times):
        jogo = times[i]
        if jogo.anfitriao not in nomes:
            nomes.append(jogo.anfitriao)
        if jogo.visitante not in nomes:
            nomes.append(jogo.visitante)
        i += 1
        
    return nomes'''


    if len(times) == 0:
        return []
    else:
        jogo = times[0]

        if jogo.anfitriao not in nomes:
            nomes.append(jogo.anfitriao)
        if jogo.visitante not in nomes:
            nomes.append(jogo.visitante)

    return NomeTime[1:]

'''result = []
NomeTime(jogos,result)
print(result)

def NomeTime(jogos: list, times: list, n: int=0):

    if len(jogos) > 0:
        append times (ogo.anfitriao)
        append times (jogo.visitante)
        NomeTime(jogos[1:], times)'''
    
    


    
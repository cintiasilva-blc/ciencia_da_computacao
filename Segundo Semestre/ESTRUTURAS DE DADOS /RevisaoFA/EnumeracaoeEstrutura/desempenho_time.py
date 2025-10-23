'''O desempenho de um time de futebol em um determinado campeonato é dado pelo número de pontos,
número de vitórias e saldo de gols (diferenças entre todos os gols marcados e sofridos), nessa ordem.
Caso dois times empatem nesse critérios, a ordem alfabética dos nomes é usado para desempate.
a) Projete uma função que determine qual de dois times tem o melhor desempenho.
b) Considerando que cada jogo ganho pelo time dá 3 pontos e empate 1 ponto, projete uma função
que atualize o desempenho de um time dado o resultado de um jogo.'''


from dataclasses import dataclass
from enum import Enum, auto

@dataclass
class Time:
    nome: str
    numero_pontos: int
    numero_vitorias: int
    gols_feitos: int
    gols_sofridos: int

@dataclass
class Jogo:
    time1: str
    gols_time1: int
    time2: str
    gols_time2: int

class Resultado(Enum):
    VITORIA = 3
    EMPATE = 1
    DERROTA = 0

def melhor_desempenho(time1: Time, time2: Time) -> Time:
    '''Recebe dois times e deterimina qual o melhor entre eles.
    Retorna o melhor.
    
    Exemplos:
    >>> melhor_desempenho(Time(nome='Santos', numero_pontos=10, numero_vitorias=3, gols_feitos=5, gols_sofridos=3), Time(nome='Flamengo', numero_pontos=6, numero_vitorias=2, gols_feitos=3, gols_sofridos=5))
    Time(nome='Santos', numero_pontos=10, numero_vitorias=3, gols_feitos=5, gols_sofridos=3)
    '''

    if time1.numero_pontos > time2.numero_pontos:
        melhor = time1
    elif time2.numero_pontos > time1.numero_pontos:
        melhor = time2
    else: 
        if time1.numero_vitorias > time2.numero_vitorias:
            melhor = time1
        elif time2.numero_vitorias > time1.numero_vitorias:
            melhor = time2
        else: 
            if (time1.gols_feitos - time1.gols_sofridos) > (time2.gols_feitos - time2.gols_sofridos):
                melhor = time1
            elif (time2.gols_feitos - time2.gols_sofridos) > (time1.gols_feitos - time1.gols_sofridos):
                melhor = time2
            else:
                if time1.nome > time2.nome:
                    melhor = time1
                else:
                    melhor = time2

    return melhor

def atualiza_time(time: Time, jogo: Jogo) -> Time:
    '''Recebe um time e o resultado de um jogo e atualiza as informaçoes do time.
    
    Exemplo:
    >>> atualiza_time(Time(nome="Vasco", numero_pontos=3, numero_vitorias=1, gols_feitos=1, gols_sofridos=0), Jogo('Flamengo', 0, 'Vasco', 2))
    Time(nome='Vasco', numero_pontos=6, numero_vitorias=2, gols_feitos=3, gols_sofridos=0)
    '''

    pontos = 0
    vitorias = 0
    gols_feitos = 0
    gols_sofridos = 0

    if time.nome == jogo.time1:
        gols_feitos += jogo.gols_time1
        gols_sofridos += jogo.gols_time2
        if jogo.gols_time1 > jogo.gols_time2:
            pontos += Resultado.VITORIA.value
            vitorias += 1
        elif jogo.gols_time1 == jogo.gols_time2:
            pontos += Resultado.EMPATE.value
        return Time(jogo.time2, pontos, vitorias, gols_feitos, gols_sofridos)
    else:
        gols_feitos += jogo.gols_time2
        gols_sofridos += jogo.gols_time1
        if jogo.gols_time2 > jogo.gols_time1:
            pontos += Resultado.VITORIA.value
            vitorias += 1
        elif jogo.gols_time2 == jogo.gols_time1:
            pontos += Resultado.EMPATE.value
        return Time(jogo.time2, pontos, vitorias, gols_feitos, gols_sofridos)

    
# 1. Qual a classifica¸c˜ao dos times no campeonato?
    # Descobrir os nomes dos times                  # FEITO
    # Calcular os pontos, n´umero de vit´orias e saldo de gols de um time por vez       # FEITO
    # Classificar os times
from enum import Enum, auto
from dataclasses import dataclass

class Resultado(Enum):
    VITORIA = 3
    EMPATE = 1
    DERROTA = 0

@dataclass 
class Estatisticas:
    nome: str
    pontos_totais: int
    vitorias: int
    saldo_gols: int
    gols_sofridos: int
    jogos_anfi: int
    pontos_anfi: int


@dataclass
class Jogo:
    anfitriao: str
    gols_anfi: int
    visitante: str
    gols_visitante: int

def BubbleSort(arranjo: list) -> list:
    '''Recebe uma lista de números e ordena do menor para o maior em direções opostas até se encontrarem
    Exemplos:
    >>> BubbleSort(['Sao-Paulo', 'Atletico-MG', 'Flamengo', 'Palmeiras'])
    ['Atletico-MG', 'Flamengo', 'Palmeiras', 'Sao-Paulo']
    '''
     
    n = len(arranjo)
    for i in range(n):
        for j in range(0, n-i-1):
            if arranjo[j] > arranjo[j + 1]:
                aux = arranjo[j]
                arranjo[j] = arranjo[j + 1]
                arranjo[j + 1] = aux
    return arranjo

def meu_split(palavra: str) -> list:
    '''Recebe uma palavra ou texto e divide em uma lista de strings separadas
    Exemplos:
    >>> meu_split('ola mundo python')
    ['ola', 'mundo', 'python']
    >>> meu_split('Cintia da Silva Bulcão')
    ['Cintia', 'da', 'Silva', 'Bulcão']
    >>> meu_split(' ')
    []
    '''

    final = []
    palavra_atual = ''

    for i in palavra:
        if i == ' ' or i == '\n':
            if palavra_atual:
                final.append(palavra_atual)
                palavra_atual = ''
        else:
            palavra_atual += i

    if palavra_atual:
        final.append(palavra_atual)


    return final


def AtribuiJogo(jogos: list[str]) -> list[Jogo]:
    '''Recebe uma linha do arquivo texto e retorna um valor do tipo Jogo
    Exemplos:
    >>> AtribuiJogo(['Sao-Paulo 1 Atletico-MG 2', 'Flamengo 2 Palmeiras 1'])
    [Jogo(anfitriao='Sao-Paulo', gols_anfi=1, visitante='Atletico-MG', gols_visitante=2), Jogo(anfitriao='Flamengo', gols_anfi=2, visitante='Palmeiras', gols_visitante=1)]
    '''
    result = []

    # uma linha é um elemento da lista 
    for a in jogos:         #percorre a lista *jogos*
        separa = meu_split(a)    # usa split em cada indice da lista *jogos*  : [['Sao-Paulo, '1', 'Atletico-MG', '2'], ['Flamengo', '2', 'Palmeiras', '1']]
        for i in separa:            
            anfitriao = separa[0]
            gols_anfi = int(separa[1])
            visitante = separa[2]
            gols_visitante = int(separa[3])
        result.append(Jogo(anfitriao, gols_anfi, visitante, gols_visitante))
    return result


def NomeTimes(times: list[Jogo]) -> list[str]:
    '''Recebe a lista de jogos e retorne uma lista de nomes de times sem repetição
    Exemplo:
    >>> NomeTimes([Jogo(anfitriao='Sao-Paulo', gols_anfi=1, visitante='Atletico-MG', gols_visitante=2), Jogo(anfitriao='Sao-Paulo', gols_anfi=2, visitante='Palmeiras', gols_visitante=1)])
    ['Sao-Paulo', 'Atletico-MG', 'Palmeiras']
    '''

    nomes = []

    for j in times:
        ja_existe = False
        i = 0
        while i < len(nomes) and ja_existe == False:
            if nomes[i] == j.anfitriao:
                ja_existe = True
            i += 1

        if ja_existe == False:
           nomes.append(j.anfitriao)


        ja_existe = False
        i = 0
        while i < len(nomes) and ja_existe == False:
            if nomes[i] == j.visitante:
                ja_existe = True
            i += 1

        if ja_existe == False:
           nomes.append(j.visitante)

    return nomes


def AtualizaEstatisticas(time: Estatisticas, jogo_qlr: Jogo) -> Estatisticas:
    '''Recebe as estatisticas atuais de um time, um novo jogo desse mesmo time e atualiza suas estatisticas
    Exemplos:
    >>> AtualizaEstatisticas(Estatisticas(nome='Flamengo', pontos_totais=0, vitorias=0, saldo_gols=0, gols_sofridos=0, jogos_anfi=0, pontos_anfi=0), Jogo(anfitriao='Flamengo', gols_anfi=2, visitante='Palmeiras', gols_visitante=1))
    Estatisticas(nome='Flamengo', pontos_totais=3, vitorias=1, saldo_gols=1, gols_sofridos=1, jogos_anfi=1, pontos_anfi=3)
    >>> AtualizaEstatisticas(Estatisticas(nome='Palmeiras', pontos_totais=0, vitorias=0, saldo_gols=0, gols_sofridos=0, jogos_anfi=0, pontos_anfi=0), Jogo(anfitriao='Flamengo', gols_anfi=2, visitante='Palmeiras', gols_visitante=1))
    Estatisticas(nome='Palmeiras', pontos_totais=0, vitorias=0, saldo_gols=-1, gols_sofridos=2, jogos_anfi=0, pontos_anfi=0)
    '''

    # Eh anfritrião
    if time.nome == jogo_qlr.anfitriao:
        time.jogos_anfi += 1
        if jogo_qlr.gols_anfi > jogo_qlr.gols_visitante:
            time.vitorias += 1
            time.pontos_totais += Resultado.VITORIA.value
            time.saldo_gols += (jogo_qlr.gols_anfi - jogo_qlr.gols_visitante)
            time.pontos_anfi += Resultado.VITORIA.value
        elif jogo_qlr.gols_anfi == jogo_qlr.gols_visitante:
            time.pontos_totais += Resultado.EMPATE.value
            time.saldo_gols += (jogo_qlr.gols_anfi - jogo_qlr.gols_visitante)
            time.pontos_anfi += Resultado.EMPATE.value 
        else:
            time.saldo_gols += (jogo_qlr.gols_anfi - jogo_qlr.gols_visitante) 


    # Nao eh anfitrião
    if time.nome == jogo_qlr.visitante:
        if jogo_qlr.gols_visitante > jogo_qlr.gols_anfi:
            time.vitorias += 1
            time.pontos_totais += Resultado.VITORIA.value
            time.saldo_gols += (jogo_qlr.gols_visitante - jogo_qlr.gols_anfi)
        elif jogo_qlr.gols_visitante == jogo_qlr.gols_anfi:
            time.pontos_totais += Resultado.EMPATE.value
            time.saldo_gols += (jogo_qlr.gols_visitante - jogo_qlr.gols_anfi)
        else:
            time.saldo_gols += (jogo_qlr.gols_visitante - jogo_qlr.gols_anfi) 

    # Atualiza gols sofridos
    if time.nome == jogo_qlr.anfitriao:
        time.gols_sofridos += jogo_qlr.gols_visitante
    else:
        time.gols_sofridos += jogo_qlr.gols_anfi

    return time

def ComparaMelhorTime(time1: Estatisticas, time2: Estatisticas) -> Estatisticas:
    '''Recebe dois times e os compara pelos seguintes critérios
    1. Pontos (maior primeiro)
    2. Vitórias (maior primeiro)
    3. Saldo de gols (maior primeiro)
    4. Nome (ordem alfabética)
    e retorna o melhor entre todos os requisitos.

    >>> ComparaMelhorTime(Estatisticas(nome='Flamengo', pontos_totais=11, vitorias=3, saldo_gols=3, gols_sofridos=4, jogos_anfi=2, pontos_anfi=6), Estatisticas(nome='Sao-Paulo', pontos_totais=7, vitorias=2, saldo_gols=1, gols_sofridos=5, jogos_anfi=1, pontos_anfi=3))
    Estatisticas(nome='Flamengo', pontos_totais=11, vitorias=3, saldo_gols=3, gols_sofridos=4, jogos_anfi=2, pontos_anfi=6)
    >>> ComparaMelhorTime(Estatisticas(nome='Atletico-MG', pontos_totais=9, vitorias=3, saldo_gols=2, gols_sofridos=4, jogos_anfi=1, pontos_anfi=3), Estatisticas(nome='Corinthians', pontos_totais=13, vitorias=4, saldo_gols=1, gols_sofridos=7, jogos_anfi=2, pontos_anfi=6))
    Estatisticas(nome='Corinthians', pontos_totais=13, vitorias=4, saldo_gols=1, gols_sofridos=7, jogos_anfi=2, pontos_anfi=6)
    '''

    # Compara pontos
    if time1.pontos_totais > time2.pontos_totais:
        melhor = time1
    elif time1.vitorias > time2.vitorias:
        melhor = time1
    elif time1.saldo_gols > time2.saldo_gols:
        melhor = time1
    elif BubbleSort([time1.nome, time2.nome]) == time1.nome:
        melhor = time1
    

    if time2.pontos_totais > time1.pontos_totais:
        melhor = time2
    elif time2.vitorias > time1.vitorias:
        melhor = time2
    elif time2.saldo_gols > time1.saldo_gols:
        melhor = time2
    elif BubbleSort([time1.nome, time2.nome]) == time2.nome:
        melhor = time2

    return melhor

def TamanhoMaxNomes(lista: list) -> int:
    '''Recebe uma lista com o nome de todos os times e retorna o tamanho maximo entre eles
    Exemplos:
    >>> TamanhoMaxNomes(['Sao-Paulo', 'Atletico-MG', 'Palmeiras', 'Corinthians'])
    11
    >>> TamanhoMaxNomes(['Vasco-da-Gama', 'Flamengo', 'Palmeiras', 'Sao-Paulo'])
    13
    '''

    maior = len(lista[0])

    for i in lista:
        if len(i) > maior:
            maior = len(i)
    return maior



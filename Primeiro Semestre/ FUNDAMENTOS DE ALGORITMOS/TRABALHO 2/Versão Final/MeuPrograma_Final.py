import sys
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

def OrdenaString(lista_str: list[str]) -> list[str]:
    '''Recebe uma lista de palavras e ordena em ordem alfabetica,
    Retorna as palavras da lista em ordem alfabetica.

    Exemplos:
    >>> OrdenaString(['ola', 'bom', 'dia'])
    ['alo', 'bmo', 'adi']
    >>> OrdenaString(['cintia', 'hoje'])
    ['aciint', 'ehjo']
    '''
    
    result = []

    for palavra in lista_str:
        letras = list(palavra)
        for i in range(1, len(letras)):
            pivo = letras[i]
            j = i - 1
            while j >= 0 and pivo < letras[j]:
                letras[j + 1] = letras[j]
                j -= 1
            letras[j + 1] = pivo

        palavra_ordenada = ''
        for letra in letras:
            palavra_ordenada += letra
        result.append(palavra_ordenada)

    return result

def MaiorTamanho(lista: list[str]) -> int:
    '''Recebe uma lista de nomes, encontra o maior tamanho,
    Retorna o valor do maior tamanho.

    Exemplos:
    >>> MaiorTamanho(['Flamengo', 'Santos'])
    8
    >>> MaiorTamanho(['Cintia', 'Giovana', 'Nikolas', 'Ana-Paula'])
    9
    '''

    if len(lista) == 0:
        return 0
    elif len(lista) == 1:
        return len(lista[0])
    else:
        rest = MaiorTamanho(lista[1:])
        
        if len(lista[0]) > rest:
            return len(lista[0])
        else:
            return rest

def MeuSplit(palavra: str) -> list[str]:
    '''Recebe uma string e separa em substrings,
    Retorna uma lista de substrings.

    Exemplos:
    >>> MeuSplit('Campeonato de Futebol Brasileiro')
    ['Campeonato', 'de', 'Futebol', 'Brasileiro']
    >>> MeuSplit('Cintia da Silva Bulcão')
    ['Cintia', 'da', 'Silva', 'Bulcão']
    >>> MeuSplit(' ')
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

def MeuRound(num: float, casas: int) -> float:
    '''Recebe um numero *num* decimal e limita suas casas decimais após a virgula,
    Retorna ainda um numero decimal, porem 'arredondado'.

    Exemplos:                                            
    >>> MeuRound(7.1234, 1)
    7.1
    >>> MeuRound(7, 4)
    7.0
    >>> MeuRound(3.1415, 2)
    3.14
    '''

    fat = 10 ** casas
    num_temp = num * fat + 0.5
    round = int(num_temp) / fat

    return round
    
def AtribuiJogo(jogos: list[str]) -> list[Jogo]:
    '''Recebe uma lista de jogos(anfitriao, gols do anfitriao, visitante, gols do visitante) e atribui suas informações ao tipo composto *Jogo*,
    Retorna uma lista do tipo Jogo,
    anfitriao: str
    gols_anfi: int
    visitante: str
    gols_visitante: int

    Exemplos:
    >>> AtribuiJogo(['Sao-Paulo 1 Atletico-MG 2', 'Flamengo 2 Palmeiras 1'])
    [Jogo(anfitriao='Sao-Paulo', gols_anfi=1, visitante='Atletico-MG', gols_visitante=2), Jogo(anfitriao='Flamengo', gols_anfi=2, visitante='Palmeiras', gols_visitante=1)]
    >>> AtribuiJogo(['Cuiaba 2 Juventude 2', 'Bahia 3 Santos 0'])
    [Jogo(anfitriao='Cuiaba', gols_anfi=2, visitante='Juventude', gols_visitante=2), Jogo(anfitriao='Bahia', gols_anfi=3, visitante='Santos', gols_visitante=0)]
    >>> AtribuiJogo(['Botafogo 2 Palmeiras 1'])
    [Jogo(anfitriao='Botafogo', gols_anfi=2, visitante='Palmeiras', gols_visitante=1)]
    '''

    result = []
    i = 0

    while i < len(jogos):
        separa: list[str] = MeuSplit(jogos[i])          
        result.append(Jogo(separa[0], int(separa[1]), separa[2], int(separa[3])))
        i += 1

    return result

def AddAnfitriao(times: list[DadosTime]) -> list[str]:
    '''Recebe uma lista de times e adiciona os nomes dos anfitriões, sem repetir, em uma nova lista
    Retorna uma lista com os nomes dos anfitriões sem repetição.
    
    Exemplos:
    >>> AddAnfitriao([Jogo(anfitriao='Sao-Paulo', gols_anfi=1, visitante='Atletico-MG', gols_visitante=2), Jogo(anfitriao='Flamengo', gols_anfi=2, visitante='Palmeiras', gols_visitante=1)])
    ['Sao-Paulo', 'Flamengo']
    >>> AddAnfitriao([Jogo(anfitriao='Sao-Paulo', gols_anfi=1, visitante='Santos', gols_visitante=2), Jogo(anfitriao='Sao-Paulo', gols_anfi=2, visitante='Ceara', gols_visitante=1)])
    ['Sao-Paulo']
    '''

    nomes = []
    for jogo in times:
        cont = 0
        for nome in nomes:
            if nome == jogo.anfitriao:
                cont += 1
        if cont == 0:
            nomes.append(jogo.anfitriao)
            
    return nomes

def AddVisit(times: list[DadosTime], nomes: list[str]) -> list[str]:
    '''Recebe uma lista de times e uma lista nao vazia de nomes, add os nomes dos visitantes nessa lista,
    Retorna uma lista com os nomes dos times, sem repetir.
    
    Exemplos:
    >>> nomes = ['Sao-Paulo', 'Flamengo']
    >>> AddVisit([Jogo(anfitriao='Sao-Paulo', gols_anfi=1, visitante='Atletico-MG', gols_visitante=2), Jogo(anfitriao='Flamengo', gols_anfi=2, visitante='Palmeiras', gols_visitante=1)], nomes)
    ['Sao-Paulo', 'Flamengo', 'Atletico-MG', 'Palmeiras']
    >>> nomes = ['Sao-Paulo']
    >>> AddVisit([Jogo(anfitriao='Sao-Paulo', gols_anfi=1, visitante='Atletico-MG', gols_visitante=2), Jogo(anfitriao='Sao-Paulo', gols_anfi=2, visitante='Palmeiras', gols_visitante=1)], nomes)
    ['Sao-Paulo', 'Atletico-MG', 'Palmeiras']
    '''
    
    for jogo in times:
        cont = 0
        for nome in nomes:
            if nome == jogo.visitante:
                cont += 1
        if cont == 0:
            nomes.append(jogo.visitante)

    return nomes

def NomeTime(times: list[Jogo]) -> list[str]:
    '''Recebe uma lista de jogos(do tipo *Jogo*), add os nomes dos times usando funçoes auxiliares para que não haja repetição,
    Retorna uma lista com o nome dos times sem repetir.

    Exemplo:
    >>> NomeTime([Jogo(anfitriao='Sao-Paulo', gols_anfi=1, visitante='Atletico-MG', gols_visitante=2), Jogo(anfitriao='Flamengo', gols_anfi=2, visitante='Palmeiras', gols_visitante=1)])
    ['Sao-Paulo', 'Flamengo', 'Atletico-MG', 'Palmeiras']
    >>> NomeTime([Jogo(anfitriao='Sao-Paulo', gols_anfi=1, visitante='Atletico-MG', gols_visitante=2), Jogo(anfitriao='Sao-Paulo', gols_anfi=2, visitante='Palmeiras', gols_visitante=1)])
    ['Sao-Paulo', 'Atletico-MG', 'Palmeiras']
    >>> NomeTime([Jogo(anfitriao='Chapecoense', gols_anfi=1, visitante='Atletico-MG', gols_visitante=2), Jogo(anfitriao='Atletico-MG', gols_anfi=2, visitante='Chapecoense', gols_visitante=1)])
    ['Chapecoense', 'Atletico-MG']
    '''

    nomes = []
    nomes = AddAnfitriao(times)
    nomes = AddVisit(times, nomes)

    return nomes

def CalculaAnfi(jogos: list[Jogo], anfi: DadosTime) -> DadosTime:
    ''' Recebe uma lista de jogos e um time especificado por parâmetro, sendo esse um anfitriao
    Retorna a pontuaçao exata desse time apos os jogos.

    Exemplos:
    >>> CalculaAnfi([Jogo(anfitriao='Sao-Paulo', gols_anfi=1, visitante='Atletico-MG', gols_visitante=2),Jogo(anfitriao='Flamengo', gols_anfi=2, visitante='Sao-Paulo', gols_visitante=1)], DadosTime(nome='Sao-Paulo', pontos_totais=0, vitorias=0, saldo_gols=0, gols_sofridos=0, jogos_anfi=0, pontos_anfi=0))
    DadosTime(nome='Sao-Paulo', pontos_totais=0, vitorias=0, saldo_gols=-1, gols_sofridos=2, jogos_anfi=1, pontos_anfi=0)
    >>> CalculaAnfi([Jogo(anfitriao='Chapecoense', gols_anfi=1, visitante='Atletico-MG', gols_visitante=2), Jogo(anfitriao='Chapecoense', gols_anfi=2, visitante='Santos', gols_visitante=1)],DadosTime(nome='Chapecoense', pontos_totais=0, vitorias=0, saldo_gols=-1, gols_sofridos=2, jogos_anfi=1, pontos_anfi=0))
    DadosTime(nome='Chapecoense', pontos_totais=3, vitorias=1, saldo_gols=-1, gols_sofridos=5, jogos_anfi=3, pontos_anfi=3)
    '''

    for jogo in jogos:
        if anfi.nome == jogo.anfitriao:
            anfi.jogos_anfi += 1
            anfi.gols_sofridos += jogo.gols_visitante
            anfi.saldo_gols += (jogo.gols_anfi - jogo.gols_visitante)
            if jogo.gols_anfi > jogo.gols_visitante:
                anfi.vitorias += 1
                anfi.pontos_totais += Resultado.VITORIA.value
                anfi.pontos_anfi += Resultado.VITORIA.value
            elif jogo.gols_anfi == jogo.gols_visitante:
                anfi.pontos_totais += Resultado.EMPATE.value
                anfi.pontos_anfi += Resultado.EMPATE.value

    return anfi

def CalculaVisit(jogos: list[Jogo], visit: DadosTime) -> DadosTime:
    ''' Recebe uma lista de jogos e um time especificado por parâmetro, sendo esse um visitante
    Retorna a pontuaçao exata desse time apos os jogos.

    Exemplos:
    >>> CalculaVisit([Jogo(anfitriao='Sao-Paulo', gols_anfi=1, visitante='Atletico-MG', gols_visitante=2),Jogo(anfitriao='Flamengo', gols_anfi=2, visitante='Sao-Paulo', gols_visitante=1)], DadosTime(nome='Atletico-MG', pontos_totais=0, vitorias=0, saldo_gols=0, gols_sofridos=0, jogos_anfi=0, pontos_anfi=0))
    DadosTime(nome='Atletico-MG', pontos_totais=3, vitorias=1, saldo_gols=1, gols_sofridos=1, jogos_anfi=0, pontos_anfi=0)
    >>> CalculaVisit([Jogo(anfitriao='Chapecoense', gols_anfi=1, visitante='Atletico-MG', gols_visitante=2), Jogo(anfitriao='Chapecoense', gols_anfi=2, visitante='Santos', gols_visitante=1)],DadosTime(nome='Santos', pontos_totais=0, vitorias=0, saldo_gols=0, gols_sofridos=0, jogos_anfi=0, pontos_anfi=0))
    DadosTime(nome='Santos', pontos_totais=0, vitorias=0, saldo_gols=-1, gols_sofridos=2, jogos_anfi=0, pontos_anfi=0)
    '''
    
    for jogo in jogos:
        if visit.nome == jogo.visitante:
            visit.gols_sofridos += jogo.gols_anfi
            visit.saldo_gols += (jogo.gols_visitante - jogo.gols_anfi)
            if jogo.gols_visitante > jogo.gols_anfi:
                visit.vitorias += 1
                visit.pontos_totais += Resultado.VITORIA.value
            elif jogo.gols_visitante == jogo.gols_anfi:
                visit.pontos_totais += Resultado.EMPATE.value

    return visit

def AtribuiDadosTime(jogos: list[Jogo]) -> list[DadosTime]:
    '''Recebe uma lista de jogos, calcula seus dados e atualiza/atribui ao tipo composto *DadosTime*.
    
    Exemplos:
    >>> AtribuiDadosTime([Jogo(anfitriao='Flamengo',gols_anfi=0,visitante='Palmeiras', gols_visitante=0)])
    [DadosTime(nome='Flamengo', pontos_totais=1, vitorias=0, saldo_gols=0, gols_sofridos=0, jogos_anfi=1, pontos_anfi=1), DadosTime(nome='Palmeiras', pontos_totais=1, vitorias=0, saldo_gols=0, gols_sofridos=0, jogos_anfi=0, pontos_anfi=0)]
    >>> AtribuiDadosTime([Jogo(anfitriao='Flamengo',gols_anfi=0,visitante='Palmeiras', gols_visitante=0), Jogo(anfitriao='Cuiaba',gols_anfi=0,visitante='Santos', gols_visitante=3)])
    [DadosTime(nome='Flamengo', pontos_totais=1, vitorias=0, saldo_gols=0, gols_sofridos=0, jogos_anfi=1, pontos_anfi=1), DadosTime(nome='Cuiaba', pontos_totais=0, vitorias=0, saldo_gols=-3, gols_sofridos=3, jogos_anfi=1, pontos_anfi=0), DadosTime(nome='Palmeiras', pontos_totais=1, vitorias=0, saldo_gols=0, gols_sofridos=0, jogos_anfi=0, pontos_anfi=0), DadosTime(nome='Santos', pontos_totais=3, vitorias=1, saldo_gols=3, gols_sofridos=0, jogos_anfi=0, pontos_anfi=0)]
    '''

    result = []
    nomes_times = NomeTime(jogos)  

    for nome in nomes_times:
        time = DadosTime(nome, 0, 0, 0, 0, 0, 0)
        time  = CalculaAnfi(jogos, time)
        time = CalculaVisit(jogos, time)
        result.append(time)

    return result

def ComparaMelhorTime(time1: DadosTime, time2: DadosTime) -> bool:
    '''Recebe dois times, compara se o segundo é melhor que o primeiro,
    Retorna True se o *time2* for melhor que o *time1*.

    Exemplos:
    >>> ComparaMelhorTime(DadosTime(nome='Flamengo', pontos_totais=11, vitorias=3, saldo_gols=3, gols_sofridos=4, jogos_anfi=2, pontos_anfi=6), DadosTime(nome='Sao-Paulo', pontos_totais=7, vitorias=2, saldo_gols=1, gols_sofridos=5, jogos_anfi=1, pontos_anfi=3))
    False
    >>> ComparaMelhorTime(DadosTime(nome='Atletico-MG', pontos_totais=9, vitorias=3, saldo_gols=2, gols_sofridos=4, jogos_anfi=1, pontos_anfi=3), DadosTime(nome='Corinthians', pontos_totais=13, vitorias=4, saldo_gols=1, gols_sofridos=7, jogos_anfi=2, pontos_anfi=6))
    True
    '''

    if time1.pontos_totais < time2.pontos_totais:
        return True
    elif time1.pontos_totais == time2.pontos_totais:
        if time1.vitorias < time2.vitorias:
            return True
        elif time1.vitorias == time2.vitorias:
            if time1.saldo_gols < time2.saldo_gols:
                return True
            elif time1.saldo_gols == time2.saldo_gols:
                nomes_ordenados = OrdenaString([time1.nome, time2.nome])
                if nomes_ordenados[0] == time2.nome:
                    return True
                
    return False

def ListaMelhoresTimes(times: list[DadosTime]) -> list[DadosTime]:
    '''Recebe uma lista de times e ordena do melhor ao pior seguindo os seguintes critérios:
    1. Pontos
    2. Vitórias
    3. Saldo de gols 
    4. Nome (ordem alfabetica)
    Retorna uma lista ordenada pelos criterios.

    Exemplos:
    >>> ListaMelhoresTimes([DadosTime(nome='Flamengo', pontos_totais=14, vitorias=4, saldo_gols=5, gols_sofridos=3, jogos_anfi=3, pontos_anfi=9),DadosTime(nome='Palmeiras', pontos_totais=14, vitorias=4, saldo_gols=4, gols_sofridos=4, jogos_anfi=3, pontos_anfi=9),DadosTime(nome='Gremio', pontos_totais=11, vitorias=3, saldo_gols=2, gols_sofridos=5, jogos_anfi=2, pontos_anfi=6),DadosTime(nome='Cruzeiro', pontos_totais=11, vitorias=3, saldo_gols=3, gols_sofridos=6, jogos_anfi=2, pontos_anfi=6)])
    [DadosTime(nome='Flamengo', pontos_totais=14, vitorias=4, saldo_gols=5, gols_sofridos=3, jogos_anfi=3, pontos_anfi=9), DadosTime(nome='Palmeiras', pontos_totais=14, vitorias=4, saldo_gols=4, gols_sofridos=4, jogos_anfi=3, pontos_anfi=9), DadosTime(nome='Cruzeiro', pontos_totais=11, vitorias=3, saldo_gols=3, gols_sofridos=6, jogos_anfi=2, pontos_anfi=6), DadosTime(nome='Gremio', pontos_totais=11, vitorias=3, saldo_gols=2, gols_sofridos=5, jogos_anfi=2, pontos_anfi=6)]
    >>> ListaMelhoresTimes([DadosTime(nome='Flamengo', pontos_totais=14, vitorias=4, saldo_gols=5, gols_sofridos=3, jogos_anfi=3, pontos_anfi=9),DadosTime(nome='Palmeiras', pontos_totais=14, vitorias=4, saldo_gols=4, gols_sofridos=4, jogos_anfi=3, pontos_anfi=7),DadosTime(nome='Vasco', pontos_totais=8, vitorias=2, saldo_gols=-2, gols_sofridos=7, jogos_anfi=3, pontos_anfi=6)])
    [DadosTime(nome='Flamengo', pontos_totais=14, vitorias=4, saldo_gols=5, gols_sofridos=3, jogos_anfi=3, pontos_anfi=9), DadosTime(nome='Palmeiras', pontos_totais=14, vitorias=4, saldo_gols=4, gols_sofridos=4, jogos_anfi=3, pontos_anfi=7), DadosTime(nome='Vasco', pontos_totais=8, vitorias=2, saldo_gols=-2, gols_sofridos=7, jogos_anfi=3, pontos_anfi=6)]'''
    
    tam_nome: int = len(times)

    for i in range(tam_nome):
        for j in range(0, tam_nome - i - 1):
            if ComparaMelhorTime(times[j], times[j + 1]):
                aux: int = times[j]
                times[j] = times[j + 1]
                times[j + 1] = aux

    return times

def AjustaNomes(times: list[str]) -> list[str]:
    '''Recebe uma lista com os nomes dos times, encontra o maior nome e ajusta todos para o mesmo tamanho add *' '* a direita,
    Retorna a mesma lista, porem com os nomes ajustados.

    Exemplos:
    >>> AjustaNomes(['Sao-Paulo', 'Atletico-MG', 'Palmeiras', 'Corinthians'])
    ['Sao-Paulo  ', 'Atletico-MG', 'Palmeiras  ', 'Corinthians']
    >>> AjustaNomes(['America-MG', 'Fortaleza', 'Internacional'])
    ['America-MG   ', 'Fortaleza    ', 'Internacional']
    '''

    for i in range(len(times)):
        while len(times[i]) < MaiorTamanho(times):
            times[i] += ' '

    return times

def AjustaNum(num: int) -> str:
    ''' Recebe um numero inteiro, tranforma en *str* e ajusta para no max 3 caracteres
    Retorna uma str de 3 caracteres.

    Exemplo:
    >>> AjustaNum(7)
    '  7'
    >>> AjustaNum(17)
    ' 17'
    >>> AjustaNum(-15)
    '-15'
    '''

    caracter_num = str(num)
    num_carc = len(caracter_num)

    if num >= 0:
        if num_carc == 1:
            return '  ' + caracter_num
        elif num_carc == 2:
            return ' ' + caracter_num
    else:
        if num_carc == 2:
            return ' ' + caracter_num
        elif num_carc == 3:
            return caracter_num
        
def FormataNomesT(times: list[DadosTime]) -> list[str]:
    '''Recebe uma lista de times e tem basicamente a mesma funçao de *AjustaNomes* porém para uma lista do tipo composto *DadosTime*
    Retorna uma lista com os nomes dos times ajustados para o mesmo tamanho.
    
    Exemplo:
    >>> FormataNomesT([DadosTime(nome='Flamengo', pontos_totais=14, vitorias=4, saldo_gols=5, gols_sofridos=3, jogos_anfi=4, pontos_anfi=12), DadosTime(nome='Palmeiras', pontos_totais=13, vitorias=4, saldo_gols=4, gols_sofridos=5, jogos_anfi=4, pontos_anfi=9), DadosTime(nome='Cruzeiro', pontos_totais=12, vitorias=3, saldo_gols=1, gols_sofridos=7, jogos_anfi=3, pontos_anfi=5)])
    ['Flamengo ', 'Palmeiras', 'Cruzeiro ']
    >>> FormataNomesT([DadosTime(nome='Ceara', pontos_totais=14, vitorias=4, saldo_gols=5, gols_sofridos=3, jogos_anfi=3, pontos_anfi=9), DadosTime(nome='Palmeiras', pontos_totais=14, vitorias=4, saldo_gols=4, gols_sofridos=4, jogos_anfi=3, pontos_anfi=7), DadosTime(nome='Vasco', pontos_totais=8, vitorias=2, saldo_gols=-2,gols_sofridos=7, jogos_anfi=3, pontos_anfi=6)])
    ['Ceara    ', 'Palmeiras', 'Vasco    ']
    '''

    nomes = []

    for i in times:
        nomes.append(i.nome)

    return AjustaNomes(nomes)        

def TabelaClassificacao(lista: list[DadosTime]) -> list[str]:
    '''Recebe um lista de times, ajusta o tamanho dos nomes e dos numeros(quntidade de pontos, o numero de vitorias e o saldo de gols),
    Retorna uma lista de substrings com essas informações formatadas.

    Exemplos:
    >>> TabelaClassificacao([DadosTime(nome='Flamengo', pontos_totais=14, vitorias=4, saldo_gols=5, gols_sofridos=3, jogos_anfi=3, pontos_anfi=9), DadosTime(nome='Palmeiras', pontos_totais=14, vitorias=4, saldo_gols=4, gols_sofridos=4, jogos_anfi=3, pontos_anfi=9), DadosTime(nome='Cruzeiro', pontos_totais=11, vitorias=3, saldo_gols=3, gols_sofridos=6, jogos_anfi=2, pontos_anfi=6), DadosTime(nome='Gremio', pontos_totais=11, vitorias=3, saldo_gols=2, gols_sofridos=5, jogos_anfi=2, pontos_anfi=6)])
    ['Flamengo      14     4       5', 'Palmeiras     14     4       4', 'Cruzeiro      11     3       3', 'Gremio        11     3       2']
    >>> TabelaClassificacao([DadosTime(nome='Flamengo', pontos_totais=14, vitorias=4, saldo_gols=5, gols_sofridos=3, jogos_anfi=3, pontos_anfi=9), DadosTime(nome='Palmeiras', pontos_totais=14, vitorias=4, saldo_gols=4, gols_sofridos=4, jogos_anfi=3, pontos_anfi=7), DadosTime(nome='Vasco', pontos_totais=8, vitorias=2, saldo_gols=-2,gols_sofridos=7, jogos_anfi=3, pontos_anfi=6)])
    ['Flamengo      14     4       5', 'Palmeiras     14     4       4', 'Vasco          8     2      -2']
    '''

    melhores: list[DadosTime] = ListaMelhoresTimes(lista)

    nomes = []
    for t in melhores:
        nomes.append(t.nome)
    
    nomes_ajust: list[str] = AjustaNomes(nomes)

    pontos_totais = []
    vitorias = []
    saldo_gols = []
    for time in melhores:
        pontos_totais.append(AjustaNum(time.pontos_totais))
        vitorias.append(AjustaNum(time.vitorias))
        saldo_gols.append(AjustaNum(time.saldo_gols))

    linhas_tab = []
    for i in range(len(melhores)):
        linha = nomes_ajust[i] + '    ' + pontos_totais[i] + '   ' + vitorias[i] + '     ' + saldo_gols[i]
        linhas_tab.append(linha)
    
    return linhas_tab
#--------------------------------------------------------------------------------------

def CalculaAproveitamento(lista_times: list[DadosTime])-> list[float]:
    '''Recebe uma lista de times e calcula o aproveitamento de cada time jogando como anfitrião,
    Retorna uma lista com os resultados.

    Exemplo:
    >>> CalculaAproveitamento([DadosTime(nome='Flamengo', pontos_totais=14, vitorias=4, saldo_gols=5, gols_sofridos=3, jogos_anfi=3, pontos_anfi=9), DadosTime(nome='Palmeiras', pontos_totais=14, vitorias=4, saldo_gols=4, gols_sofridos=4, jogos_anfi=3, pontos_anfi=9), DadosTime(nome='Cruzeiro', pontos_totais=11, vitorias=3, saldo_gols=3, gols_sofridos=6, jogos_anfi=2, pontos_anfi=6), DadosTime(nome='Gremio', pontos_totais=11, vitorias=3, saldo_gols=2, gols_sofridos=5, jogos_anfi=2, pontos_anfi=6)])
    [100.0, 100.0, 100.0, 100.0]
    >>> CalculaAproveitamento([DadosTime(nome='Flamengo', pontos_totais=14, vitorias=4, saldo_gols=5, gols_sofridos=3, jogos_anfi=4, pontos_anfi=12), DadosTime(nome='Palmeiras', pontos_totais=13, vitorias=4, saldo_gols=4, gols_sofridos=5, jogos_anfi=4, pontos_anfi=9), DadosTime(nome='Cruzeiro', pontos_totais=12, vitorias=3, saldo_gols=1, gols_sofridos=7, jogos_anfi=3, pontos_anfi=5)])
    [100.0, 75.0, 55.56]
    '''

    result = []

    for time in lista_times:       
        if time.jogos_anfi > 0:
            aproveitamento = time.pontos_anfi / (time.jogos_anfi * Resultado.VITORIA.value) * 100
            result.append(MeuRound(aproveitamento, 2))

    return result

def EncontraMelhorAp(lista: list[DadosTime]) -> list[int]:
    '''Recebe uma lista de times e encontra o(s) os melhores aproveitamentos(valor) como anfi,
    Retorna uma lista com esses valores.

    Exemplos:
    >>> EncontraMelhorAp([DadosTime(nome='Flamengo', pontos_totais=14, vitorias=4, saldo_gols=5, gols_sofridos=3, jogos_anfi=3, pontos_anfi=9), DadosTime(nome='Palmeiras', pontos_totais=14, vitorias=4, saldo_gols=4, gols_sofridos=4, jogos_anfi=3, pontos_anfi=9), DadosTime(nome='Cruzeiro', pontos_totais=11, vitorias=3, saldo_gols=3, gols_sofridos=6, jogos_anfi=2, pontos_anfi=6), DadosTime(nome='Gremio', pontos_totais=11, vitorias=3, saldo_gols=2, gols_sofridos=5, jogos_anfi=2, pontos_anfi=6)])
    [100.0, 100.0, 100.0, 100.0]
    >>> EncontraMelhorAp([DadosTime(nome='Flamengo', pontos_totais=14, vitorias=4, saldo_gols=5, gols_sofridos=3, jogos_anfi=4, pontos_anfi=12), DadosTime(nome='Palmeiras', pontos_totais=13, vitorias=4, saldo_gols=4, gols_sofridos=5, jogos_anfi=4, pontos_anfi=9), DadosTime(nome='Cruzeiro', pontos_totais=12, vitorias=3, saldo_gols=1, gols_sofridos=7, jogos_anfi=3, pontos_anfi=5)])
    [100.0]
    >>> EncontraMelhorAp([DadosTime(nome='Palmeiras', pontos_totais=13, vitorias=4, saldo_gols=4, gols_sofridos=5, jogos_anfi=4, pontos_anfi=9), DadosTime(nome='Cruzeiro', pontos_totais=12, vitorias=3, saldo_gols=1, gols_sofridos=7, jogos_anfi=3, pontos_anfi=5)])
    [75.0]
    '''

    aprovt: list[int] = CalculaAproveitamento(lista)
    result = []
    maior = 0

    for i in aprovt:      
        if i > maior:                  
            maior = i
        if i == maior:
            result.append(i)

    return result

def TabelaMelhorAnfi(lista: list[DadosTime]) -> list[str]:
    '''Recebe uma lista de times, e encontra o(s) times com melhor aproveitamneto como anfitrião,
    Retorna uma lista com o o nome desses times e a porcentagem de aproveitamento.

    >>> TabelaMelhorAnfi([DadosTime(nome='Flamengo', pontos_totais=14, vitorias=4, saldo_gols=5, gols_sofridos=3, jogos_anfi=3, pontos_anfi=9), DadosTime(nome='Palmeiras', pontos_totais=14, vitorias=4, saldo_gols=4, gols_sofridos=4, jogos_anfi=3, pontos_anfi=9), DadosTime(nome='Cruzeiro', pontos_totais=11, vitorias=3, saldo_gols=3, gols_sofridos=6, jogos_anfi=2, pontos_anfi=6), DadosTime(nome='Gremio', pontos_totais=11, vitorias=3, saldo_gols=2, gols_sofridos=5, jogos_anfi=2, pontos_anfi=6)])
    ['Flamengo     100.0%', 'Palmeiras    100.0%', 'Cruzeiro     100.0%', 'Gremio       100.0%']
    >>> TabelaMelhorAnfi([DadosTime(nome='Flamengo', pontos_totais=14, vitorias=4, saldo_gols=5, gols_sofridos=3, jogos_anfi=4, pontos_anfi=12), DadosTime(nome='Palmeiras', pontos_totais=13, vitorias=4, saldo_gols=4, gols_sofridos=5, jogos_anfi=4, pontos_anfi=9), DadosTime(nome='Cruzeiro', pontos_totais=12, vitorias=3, saldo_gols=1, gols_sofridos=7, jogos_anfi=3, pontos_anfi=5)])
    ['Flamengo     100.0%']
    >>> TabelaMelhorAnfi([DadosTime(nome='Palmeiras', pontos_totais=13, vitorias=4, saldo_gols=4, gols_sofridos=5, jogos_anfi=4, pontos_anfi=9), DadosTime(nome='Cruzeiro', pontos_totais=12, vitorias=3, saldo_gols=1, gols_sofridos=7, jogos_anfi=3, pontos_anfi=5)])
    ['Palmeiras    75.0%']
    '''

    aprovt = CalculaAproveitamento(lista)
    melhores = EncontraMelhorAp(lista)
    nomes_ajust = FormataNomesT(lista)
    tabela = []

    for i in range(len(lista)):
        if aprovt[i] in melhores:
            linha = nomes_ajust[i] + '    ' + str(aprovt[i]) + '%'
            tabela.append(linha)

    return tabela

#--------------------------------------------------------------------------------------------------------------

def MenorGolsSofridos(times: list[DadosTime]) -> int:
    '''Recebe uma lista de de times e encontra o time com o menr numero de gols sofridos
    Retorna o  valor do menor número de gols sofridos
    
    Exemplos:
    >>> MenorGolsSofridos([DadosTime(nome='Flamengo', pontos_totais=14, vitorias=4, saldo_gols=5, gols_sofridos=3, jogos_anfi=3, pontos_anfi=9), DadosTime(nome='Palmeiras', pontos_totais=14, vitorias=4, saldo_gols=4, gols_sofridos=4, jogos_anfi=3, pontos_anfi=9), DadosTime(nome='Cruzeiro', pontos_totais=11, vitorias=3, saldo_gols=3, gols_sofridos=6, jogos_anfi=2, pontos_anfi=6), DadosTime(nome='Gremio', pontos_totais=11, vitorias=3, saldo_gols=2, gols_sofridos=5, jogos_anfi=2, pontos_anfi=6)])
    3
    >>> MenorGolsSofridos([DadosTime(nome='Grêmio', pontos_totais=11, vitorias=3, saldo_gols=2, gols_sofridos=4, jogos_anfi=4, pontos_anfi=6),DadosTime(nome='São Paulo', pontos_totais=10, vitorias=2, saldo_gols=1, gols_sofridos=2, jogos_anfi=3, pontos_anfi=7),DadosTime(nome='Athletico-PR', pontos_totais=12, vitorias=4, saldo_gols=3, gols_sofridos=2, jogos_anfi=4, pontos_anfi=9),DadosTime(nome='Botafogo', pontos_totais=9, vitorias=2, saldo_gols=0, gols_sofridos=5, jogos_anfi=4, pontos_anfi=5)])
    2
    '''

    if len(times) == 0:
        return 0
    elif len(times) == 1:
        return times[0].gols_sofridos
    else:
        menor_restante = MenorGolsSofridos(times[1:])
        if times[0].gols_sofridos < menor_restante:
            return times[0].gols_sofridos
        else:
            return menor_restante

def TabelaMelhorDef(lista: list[DadosTime]) -> list[str]:
    '''Recebe uma lista de times e retorna uma lista com o nome e o numeros de gols do(s) times com menor num de gols sofridos

    Exemplos:
    >>> TabelaMelhorDef([DadosTime(nome='Flamengo', pontos_totais=14, vitorias=4, saldo_gols=5, gols_sofridos=3, jogos_anfi=4, pontos_anfi=12), DadosTime(nome='Palmeiras', pontos_totais=13, vitorias=4, saldo_gols=4, gols_sofridos=5, jogos_anfi=4, pontos_anfi=9), DadosTime(nome='Cruzeiro', pontos_totais=12, vitorias=3, saldo_gols=1, gols_sofridos=7, jogos_anfi=3, pontos_anfi=5)])
    ['Flamengo    3']
    >>> TabelaMelhorDef([DadosTime(nome='Grêmio', pontos_totais=11, vitorias=3, saldo_gols=2, gols_sofridos=4, jogos_anfi=4, pontos_anfi=6),DadosTime(nome='São Paulo', pontos_totais=10, vitorias=2, saldo_gols=1, gols_sofridos=2, jogos_anfi=3, pontos_anfi=7),DadosTime(nome='Athletico-PR', pontos_totais=12, vitorias=4, saldo_gols=3, gols_sofridos=2, jogos_anfi=4, pontos_anfi=9),DadosTime(nome='Botafogo', pontos_totais=9, vitorias=2, saldo_gols=0, gols_sofridos=5, jogos_anfi=4, pontos_anfi=5)])
    ['São Paulo    2', 'Athletico-PR    2']
    '''

    tabela = []
    menor = MenorGolsSofridos(lista)
    nomes_ajust = FormataNomesT(lista)
  
    for i in lista:
        if i.gols_sofridos == menor:
            nomes_ajust = AjustaNomes([i.nome]) 
            linha = nomes_ajust[0] + '    ' + str(i.gols_sofridos)
            tabela.append(linha)

    return tabela

#--------------------------------------------------------------------------------------------------------------
def main():
    if len(sys.argv) < 2:
        print('Nenhum nome de arquivo informado.')
        sys.exit(1)
    if len(sys.argv) > 2:
        print('Muitos parâmetro. Informe apenas um nome de arquivo.')
        sys.exit(1)

    jogos = le_arquivo('resultados.txt')

    # TODO: Qual a classificação dos times no campeonato?
    print()
    print("CLASSIFICAÇÃO DOS TIMES NO CAMPEONATO ")
    print()
    print('TIMES             P      V       G')
    atribui_jogo = AtribuiJogo(jogos)
    atribui_times = AtribuiDadosTime(atribui_jogo)
    tabela = TabelaClassificacao(atribui_times)
    for l in tabela:
        print(l)
    print()

    # TODO: Qual o time com melhor aproveitamento jogando como anfitrião?
    print("MELHOR(ES) ANFITRIÃO(S)")
    tabela_mvp_anfi = TabelaMelhorAnfi(atribui_times)
    for l in tabela_mvp_anfi:
        print(l)
    print()

    # TODO: Qual o time com a defesa menos vazada?
    print("DEFESA MENOS VAZADA")
    tabela_def = TabelaMelhorDef(atribui_times)
    for l in tabela_def:
        print(l)

def le_arquivo(nome: str) -> list[str]:
    '''
    Lê o conteúdo do arquivo *nome* e devolve uma lista onde cada elemento
    representa uma linha.
    Por exemplo, se o conteúdo do arquivo for
    Sao-Paulo 1 Atletico-MG 2
    Flamengo 2  Palmeiras 1
    a resposta produzida  ́e ['Sao-Paulo 1 Atletico-MG 2’, 'Flamengo 2 Palmeiras 1’]
    '''

    try:
        with open(nome) as f:
            return f.readlines()
        
    except IOError as e:
        print(f'Erro na leitura do arquivo "{nome}": {e.errno} - {e.strerror}.');
        sys.exit(1)

if __name__ == '__main__':
    main()



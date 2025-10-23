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

'''def OrdenacaoString(palavra: str) -> str:
    ''Recebe uma palavra e ordena em ordem alfabetica,
    Retorna uma a palavra em ordem alfabetica.
    Exemplos:
    >>> OrdenacaoString('ola')
    'alo'
    >>> OrdenacaoString('cintia')
    'aciint'
    >>> OrdenacaoString('hoje')
    'ehjo'
    ''

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
    '''

# do professor
def BubbleSort(arranjo: list) -> list:
    '''Recebe uma lista de números e ordena do menor ao maior utilizando a troca de pares,
    Retorna a mesma lista, porém ordenada.

    Exemplos:
    >>> BubbleSort([3,4,9,2,10,5,8,1,7,6])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    '''

    n: int = len(arranjo)

    for i in range(n):
        for j in range(0, n-i-1):
            if arranjo[j] > arranjo[j + 1]:
                aux = arranjo[j]
                arranjo[j] = arranjo[j + 1]
                arranjo[j + 1] = aux

    return arranjo
    
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
    palavra_atual: str = ''

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
    '''Recebe um numero *num* decimal e um numero desejado de *casas* decimais após a virgula,
    Retorna ainda um numero decimal, porem 'arredondado'.

    Exemplos:
    >>> MeuRound(3.14159, 3)
    3.141
    >>> MeuRound(7.1234, 1)
    7.1
    >>> MeuRound(7, 4)
    7.0
    '''

    fator = 10 ** casas
    num_temp = int(num * fator + 0.5)  

    return num_temp / fator

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
    '''

    result = []
    i = 0

    while i < len(jogos):
        separa: list[str] = MeuSplit(jogos[i])              
        result.append(Jogo(separa[0], int(separa[1]), separa[2], int(separa[3])))
        i += 1

    return result

def NomeTime(times: list[Jogo]) -> list[str]:
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
        continua = NomeTime(times[1:])
        jogo = times[0]

        if jogo.anfitriao not in nomes:
            nomes.append(jogo.anfitriao)
        if jogo.visitante not in nomes:
            nomes.append(jogo.visitante)

        return nomes

    
        


# olhar se da pra simplificar esta funçao em duas, talvez uma para atribuir e outra para calcular, como no tipo Jogo
def AtribuiDadosTime(jogos: list[Jogo]) -> list[DadosTime]:
    '''Recebe uma lista de jogos do tipo *Jogo*, calcula a pontuaçao, saldo, etc. e atribui suas ao tipo composto *DadosTime*,
    Retorna uma lista do tipo DadosTime
    nome: str
    pontos_totais: int
    vitorias: int
    saldo_gols: int
    gols_sofridos: int
    jogos_anfi: int
    pontos_anfi: int        

    Exemplos:
    >>> AtribuiDadosTime([Jogo(anfitriao='Sao-Paulo', gols_anfi=1, visitante='Atletico-MG', gols_visitante=2),Jogo(anfitriao='Flamengo', gols_anfi=2, visitante='Palmeiras', gols_visitante=1)])
    [DadosTime(nome='Sao-Paulo', pontos_totais=0, vitorias=0, saldo_gols=-1, gols_sofridos=2, jogos_anfi=1, pontos_anfi=0), DadosTime(nome='Atletico-MG', pontos_totais=3, vitorias=1, saldo_gols=1, gols_sofridos=1, jogos_anfi=0, pontos_anfi=0), DadosTime(nome='Flamengo', pontos_totais=3, vitorias=1, saldo_gols=1, gols_sofridos=1, jogos_anfi=1, pontos_anfi=3), DadosTime(nome='Palmeiras', pontos_totais=0, vitorias=0, saldo_gols=-1, gols_sofridos=2, jogos_anfi=0, pontos_anfi=0)]
    '''

    dados_times = []
    nomes_times: list[str] = NomeTime(jogos)
    
    for nome in nomes_times:
        pontos_totais = 0
        vitorias = 0
        saldo_gols = 0
        gols_sofridos = 0
        jogos_anfi = 0
        pontos_anfi = 0

        for i in jogos:
            if nome == i.anfitriao:
                jogos_anfi += 1
                gols_sofridos += i.gols_visitante
                saldo_gols += (i.gols_anfi - i.gols_visitante)
                if i.gols_anfi > i.gols_visitante:
                    vitorias += 1
                    pontos_totais += Resultado.VITORIA.value
                    pontos_anfi += Resultado.VITORIA.value
                elif i.gols_anfi == i.gols_visitante:
                    pontos_totais += Resultado.EMPATE.value
                    pontos_anfi += Resultado.EMPATE.value 
            elif nome == i.visitante:
                gols_sofridos += i.gols_anfi
                saldo_gols += (i.gols_visitante - i.gols_anfi) 
                if i.gols_visitante > i.gols_anfi:
                    vitorias += 1
                    pontos_totais += Resultado.VITORIA.value
                elif i.gols_visitante == i.gols_anfi:
                    pontos_totais += Resultado.EMPATE.value
                
        dados_times.append(DadosTime(nome,pontos_totais,vitorias,saldo_gols,gols_sofridos,jogos_anfi,pontos_anfi))

    return dados_times

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
                nomes_ordenados = BubbleSort([time1.nome, time2.nome]) # def OrdenaString (adaptar pra devolver lista)
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
    
    # msm estrutura do bubblrsort, tentar fzr de outra forma ou só aplicar bubble direwto aq
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

    maior: int = 0

    for t in times :
        if len(t) > maior:
            maior = len(t)

    for i in range(len(times)):
        while len(times[i]) < maior:
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
    num_carc: int = len(caracter_num)

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
        
def TabelaClassificaçao(lista: list[DadosTime]) -> list[str]:
    '''Recebe um lista de times, ajusta o tamanho dos nomes e dos numeros(quntidade de pontos, o numero de vitorias e o saldo de gols),
    Retorna uma lista de substrings com essas informações formatadas.

    Exemplos:
    >>> TabelaClassificaçao([DadosTime(nome='Flamengo', pontos_totais=14, vitorias=4, saldo_gols=5, gols_sofridos=3, jogos_anfi=3, pontos_anfi=9), DadosTime(nome='Palmeiras', pontos_totais=14, vitorias=4, saldo_gols=4, gols_sofridos=4, jogos_anfi=3, pontos_anfi=9), DadosTime(nome='Cruzeiro', pontos_totais=11, vitorias=3, saldo_gols=3, gols_sofridos=6, jogos_anfi=2, pontos_anfi=6), DadosTime(nome='Gremio', pontos_totais=11, vitorias=3, saldo_gols=2, gols_sofridos=5, jogos_anfi=2, pontos_anfi=6)])
    ['Flamengo      14     4       5', 'Palmeiras     14     4       4', 'Cruzeiro      11     3       3', 'Gremio        11     3       2']
    >>> TabelaClassificaçao([DadosTime(nome='Flamengo', pontos_totais=14, vitorias=4, saldo_gols=5, gols_sofridos=3, jogos_anfi=3, pontos_anfi=9), DadosTime(nome='Palmeiras', pontos_totais=14, vitorias=4, saldo_gols=4, gols_sofridos=4, jogos_anfi=3, pontos_anfi=7), DadosTime(nome='Vasco', pontos_totais=8, vitorias=2, saldo_gols=-2,gols_sofridos=7, jogos_anfi=3, pontos_anfi=6)])
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

#--------------------------------------------------------------------------------------------------------------

def CalculaAproveitamento(lista_times: list[DadosTime])-> list[float]:
    '''Recebe uma lista de times e calcula o aproveitamento de cada time jogando como anfitrião,
    Retorna uma lista com os resultados.

    Exemplo:
    >>> CalculaAproveitamento([DadosTime(nome='Flamengo', pontos_totais=14, vitorias=4, saldo_gols=5, gols_sofridos=3, jogos_anfi=3, pontos_anfi=9), DadosTime(nome='Palmeiras', pontos_totais=14, vitorias=4, saldo_gols=4, gols_sofridos=4, jogos_anfi=3, pontos_anfi=9), DadosTime(nome='Cruzeiro', pontos_totais=11, vitorias=3, saldo_gols=3, gols_sofridos=6, jogos_anfi=2, pontos_anfi=6), DadosTime(nome='Gremio', pontos_totais=11, vitorias=3, saldo_gols=2, gols_sofridos=5, jogos_anfi=2, pontos_anfi=6)])
    [100.0, 100.0, 100.0, 100.0]
    >>> CalculaAproveitamento([DadosTime(nome='Flamengo', pontos_totais=14, vitorias=4, saldo_gols=5, gols_sofridos=3, jogos_anfi=4, pontos_anfi=12), DadosTime(nome='Palmeiras', pontos_totais=13, vitorias=4, saldo_gols=4, gols_sofridos=5, jogos_anfi=4, pontos_anfi=9), DadosTime(nome='Cruzeiro', pontos_totais=12, vitorias=3, saldo_gols=1, gols_sofridos=7, jogos_anfi=3, pontos_anfi=5)])
    [100.0, 75.0, 55.55]
    '''

    result = []
    i = 0

    while i < len(lista_times):
        time = lista_times[i]
        if time.jogos_anfi > 0:
            aproveitamento = time.pontos_anfi / (time.jogos_anfi * Resultado.VITORIA.value) * 100
            result.append(MeuRound(aproveitamento, 2))
        i += 1
    return result

def EncontraMelhorAp(lista: list[DadosTime]) -> list[int]:
    '''Recebe uma lista de times e encontra o(s) os melhores aproveitamentos(valor)
    Retorna uma lista com esses valores.

    Exemplos:
    >>> EncontraMelhorAp([DadosTime(nome='Flamengo', pontos_totais=14, vitorias=4, saldo_gols=5, gols_sofridos=3, jogos_anfi=3, pontos_anfi=9), DadosTime(nome='Palmeiras', pontos_totais=14, vitorias=4, saldo_gols=4, gols_sofridos=4, jogos_anfi=3, pontos_anfi=9), DadosTime(nome='Cruzeiro', pontos_totais=11, vitorias=3, saldo_gols=3, gols_sofridos=6, jogos_anfi=2, pontos_anfi=6), DadosTime(nome='Gremio', pontos_totais=11, vitorias=3, saldo_gols=2, gols_sofridos=5, jogos_anfi=2, pontos_anfi=6)])
    [100.0, 100.0, 100.0, 100.0]
    >>> EncontraMelhorAp([DadosTime(nome='Flamengo', pontos_totais=14, vitorias=4, saldo_gols=5, gols_sofridos=3, jogos_anfi=4, pontos_anfi=12), DadosTime(nome='Palmeiras', pontos_totais=13, vitorias=4, saldo_gols=4, gols_sofridos=5, jogos_anfi=4, pontos_anfi=9), DadosTime(nome='Cruzeiro', pontos_totais=12, vitorias=3, saldo_gols=1, gols_sofridos=7, jogos_anfi=3, pontos_anfi=5)])
    [100.0]
    '''

    aprovt: list[int] = CalculaAproveitamento(lista)
    result = []
    maior: int = 0

    for i in aprovt:      
        if i > maior:                  
            maior = i
        if i == maior:
            result.append(i)

    return result

def TabelaMelhorAp(lista: list[DadosTime]) -> list[str]:
    '''Recebe uma lista de times, e encontra o(s) times com melhor aproveitamneto como anfitrião,
    Retorna uma lista com o o nome desses times e a porcentagem de aproveitamento.

    >>> TabelaMelhorAp([DadosTime(nome='Flamengo', pontos_totais=14, vitorias=4, saldo_gols=5, gols_sofridos=3, jogos_anfi=3, pontos_anfi=9), DadosTime(nome='Palmeiras', pontos_totais=14, vitorias=4, saldo_gols=4, gols_sofridos=4, jogos_anfi=3, pontos_anfi=9), DadosTime(nome='Cruzeiro', pontos_totais=11, vitorias=3, saldo_gols=3, gols_sofridos=6, jogos_anfi=2, pontos_anfi=6), DadosTime(nome='Gremio', pontos_totais=11, vitorias=3, saldo_gols=2, gols_sofridos=5, jogos_anfi=2, pontos_anfi=6)])
    ['Flamengo    100.0%', 'Palmeiras    100.0%', 'Cruzeiro    100.0%', 'Gremio    100.0%']
    >>> TabelaMelhorAp([DadosTime(nome='Flamengo', pontos_totais=14, vitorias=4, saldo_gols=5, gols_sofridos=3, jogos_anfi=4, pontos_anfi=12), DadosTime(nome='Palmeiras', pontos_totais=13, vitorias=4, saldo_gols=4, gols_sofridos=5, jogos_anfi=4, pontos_anfi=9), DadosTime(nome='Cruzeiro', pontos_totais=12, vitorias=3, saldo_gols=1, gols_sofridos=7, jogos_anfi=3, pontos_anfi=5)])
    ['Flamengo    100.0%']
    '''

    aprovt: list[int] = CalculaAproveitamento(lista)
    melhores: list[Jogo] = EncontraMelhorAp(lista)
    tabela = []
    
    for i in range(len(aprovt)):
        if aprovt[i] in melhores:
            nomes_ajust = AjustaNomes(lista[i].nome)
            linha = nomes_ajust + '    ' + str(aprovt[i]) + '%'
            tabela.append(linha)

    return tabela

#--------------------------------------------------------------------------------------------------------------
# pronto, não acho viavel colocar rec. aqui
def TabelaMelhorDef(lista: list[DadosTime]) -> list[str]:
    '''Recebe uma lista de times e encontra o time com o menor numero de gols sofridos,
    Retorna uma lista com o nome e o número de gols desse(s) time(s).

    Exemplos:
    >>> TabelaMelhorDef([DadosTime(nome='Flamengo', pontos_totais=14, vitorias=4, saldo_gols=5, gols_sofridos=3, jogos_anfi=4, pontos_anfi=12), DadosTime(nome='Palmeiras', pontos_totais=13, vitorias=4, saldo_gols=4, gols_sofridos=5, jogos_anfi=4, pontos_anfi=9), DadosTime(nome='Cruzeiro', pontos_totais=12, vitorias=3, saldo_gols=1, gols_sofridos=7, jogos_anfi=3, pontos_anfi=5)])
    ['Flamengo    3']
    >>> TabelaMelhorDef([DadosTime(nome='Grêmio', pontos_totais=11, vitorias=3, saldo_gols=2, gols_sofridos=4, jogos_anfi=4, pontos_anfi=6),DadosTime(nome='São Paulo', pontos_totais=10, vitorias=2, saldo_gols=1, gols_sofridos=2, jogos_anfi=3, pontos_anfi=7),DadosTime(nome='Athletico-PR', pontos_totais=12, vitorias=4, saldo_gols=3, gols_sofridos=2, jogos_anfi=4, pontos_anfi=9),DadosTime(nome='Botafogo', pontos_totais=9, vitorias=2, saldo_gols=0, gols_sofridos=5, jogos_anfi=4, pontos_anfi=5)])
    ['São Paulo    2', 'Athletico-PR    2']
    '''

    result = []
    menor: int = lista[0].gols_sofridos
    # tentar dnv fzr só um for
    for i in lista:
        if i.gols_sofridos < menor:
            menor = i.gols_sofridos

    for i in lista:
        if i.gols_sofridos == menor:
            linha = i.nome + '    ' + str(i.gols_sofridos)
            result.append(linha)

    return result

#--------------------------------------------------------------------------------------------------------------
def main():
    if len(sys.argv) < 2:
        print('Nenhum nome de arquivo informado.')
        sys.exit(1)
    if len(sys.argv) > 2:
        print('Muitos parâmetro. Informe apenas um nome de arquivo.')
        sys.exit(1)

    jogos = le_arquivo('resultados.txt')

    #1. Qual a classificação dos times no campeonato?
    # TODO: solução da pergunta 1
    print()
    print("CLASSIFICAÇÃO DOS TIMES NO CAMPEONATO ")
    atribui_jogo = AtribuiJogo(jogos)
    atribui_times = AtribuiDadosTime(atribui_jogo)
    tabela = TabelaClassificaçao(atribui_times)
    print()
    for l in tabela:
        print(l)
    print()

    #2. Qual o time com melhor aproveitamento jogando como anfitrião?
    # TODO: solução da pergunta 2
    print("MELHOR(ES) ANFITRIÃO(S)")
    tabela_mvp = TabelaMelhorAp(atribui_times)
    for l in tabela_mvp:
        print(l)
    print()

    #3. Qual o time com a defesa menos vazada?
    # TODO: solução da pergunta 3
    print("DEFESA MENOS VAZADA")
    tabelaDefMvp = TabelaMelhorDef(atribui_times)
    for l in tabelaDefMvp:
        print(l)
    print()

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

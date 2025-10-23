'''Projete um estrutura para representar uma data com dia, ano e mês. Em seguida
a) Projete uma função que verifique se uma data é o último dia do ano.
b) Projete uma função que receba duas datas e produza verdadeiro se a primeira vem antes que a
segunda'''

from dataclasses import dataclass

@dataclass
class Data:
    dia: int
    mes: int
    ano: int

def verifica_ultimo_dia_ano(data: Data) -> bool:
    '''Recebe uma *data* e verifica se o dia é o ultimo do ano.
    
    Exemplos:
    >>> verifica_ultimo_dia_ano(Data(dia=27, mes=11, ano=2007))
    False
    >>> verifica_ultimo_dia_ano(Data(dia=31, mes=12, ano=2025))
    True
    '''

    if data.dia == 31 and data.mes == 12:
        return True
    else:
        return False

def verifica_data_antescedente(data1: Data, data2: Data) -> bool:
    '''Recebe duas datas e retorna True se *data1* vir antes de *data2*.
    
    Exemplos:
    >>> verifica_data_antescedente(Data(dia=27, mes=11, ano=2007), Data(dia=1, mes=1, ano=2007))
    False
    >>> verifica_data_antescedente(Data(dia=27, mes=11, ano=2007), Data(dia=1, mes=1, ano=2025))
    True
    >>> verifica_data_antescedente(Data(dia=1, mes=1, ano=2007), Data(dia=1, mes=1, ano=2007))
    False
    >>> verifica_data_antescedente(Data(dia=27, mes=11, ano=2007), Data(dia=27, mes=12, ano=2007))
    True
    '''

    if data1.ano < data2.ano:
        eh_menor = True
    elif data1.mes < data2.mes:
        eh_menor = True
    elif data1.dia < data2.dia:
        eh_menor = True
    else:
        eh_menor = False
    return eh_menor


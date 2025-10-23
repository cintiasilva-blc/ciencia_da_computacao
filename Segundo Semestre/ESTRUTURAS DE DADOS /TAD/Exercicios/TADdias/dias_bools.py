from enum import Enum


class Dia(Enum):
    '''
    Um dia da semana.
    '''
    DOM = False 
    SEG = True
    TER = True * 2
    QUA = True * 3
    QUI = True * 4
    SEX = True * 5
    SAB = True * 6

class Dias:
    '''
    Um conjunto de dias da semana que um evento deve se repetir.
    '''

    dias: list[Dia]

    def __init__(self) -> None:
        '''
        Cria um novo conjunto vazio de dias.

        Exemplos
        >>> c = Dias()
        >>> c.lista()
        []
        '''

        self.dias = []

    def alterna(self, d: Dia) -> None:
        '''
        Alterna a pertinencia do dia *d* em *self*, isto é, se *d* está em
        *self*, *d* é removido. Se *d* não está em *self*, *d* é adicionado.

        Exemplos
        >>> c = Dias()
        >>> c.alterna(Dia.SEX)
        >>> c.lista()
        ['sex']
        >>> c.alterna(Dia.SEG)
        >>> c.lista()
        ['seg', 'sex']
        >>> c.alterna(Dia.SEX)
        >>> c.lista()
        ['seg']
        '''

        nova_lista = []

        if d in self.dias:
            for i in self.dias:
                if i != d:
                    nova_lista.append(i)
                    self.dias = nova_lista
        else:
            self.dias.append(d)


    def lista(self) -> list[str]:
        '''
        Devolve uma lista com os dias (abreviações) em ordem da semana que
        estão em *self*.

        Exemplos
        >>> c = Dias()
        >>> c.lista()
        []
        >>> c.alterna(Dia.TER)
        >>> c.lista()
        ['ter']
        >>> c.alterna(Dia.DOM)
        >>> c.lista()
        ['dom', 'ter']
        >>> c.alterna(Dia.QUI)
        >>> c.alterna(Dia.SEG)
        >>> c.alterna(Dia.SAB)
        >>> c.alterna(Dia.QUA)
        >>> c.alterna(Dia.SEX)
        >>> c.lista()
        ['dom', 'seg', 'ter', 'qua', 'qui', 'sex', 'sab']
        '''

        nomes = []
        for i in self.dias:
            if i == Dia.SEG:
                i = 'seg'
            elif i == Dia.TER:
                i = 'ter'
            elif i == Dia.QUA:
                i = 'qua'
            elif i == Dia.QUI:
                i = 'qui'
            elif i == Dia.SEX:
                i = 'sex'
            elif i == Dia.SAB:
                i = 'sab'
            else:
                i = 'dom'
            nomes.append(i)
        return nomes


    def lista(self) -> list[str]:
        '''
        Devolve uma lista com os dias (abreviações) em ordem da semana que
        estão em *self*.

        Exemplos
        >>> c = Dias()
        >>> c.lista()
        []
        >>> c.alterna(Dia.TER)
        >>> c.lista()
        ['ter']
        >>> c.alterna(Dia.DOM)
        >>> c.lista()
        ['dom', 'ter']
        >>> c.alterna(Dia.QUI)
        >>> c.alterna(Dia.SEG)
        >>> c.alterna(Dia.SAB)
        >>> c.alterna(Dia.QUA)
        >>> c.alterna(Dia.SEX)
        >>> c.lista()
        ['dom', 'seg', 'ter', 'qua', 'qui', 'sex', 'sab']
        '''

        ordenados = ['dom', 'seg', 'ter', 'qua', 'qui', 'sex', 'sab']
        nomes = []
        for i in self.dias:
            if i == Dia.SEG:
                nomes.append('seg')
            elif i == Dia.TER:
                nomes.append('ter')
            elif i == Dia.QUA:
                nomes.append('qua')
            elif i == Dia.QUI:
                nomes.append('qui')
            elif i == Dia.SEX:
                nomes.append('sex')
            elif i == Dia.SAB:
                nomes.append('sab')
            else:
                nomes.append('dom')

        result = []
        for d in ordenados:
            if d in nomes:
                result.append(d)
        return result
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()

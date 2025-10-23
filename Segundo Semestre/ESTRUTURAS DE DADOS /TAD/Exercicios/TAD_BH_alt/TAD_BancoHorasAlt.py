from __future__ import annotations
from dataclasses import dataclass

class BancoHoras:
    Minutos: int

    def __init__(self, horas: int, minutos: int):
        '''Cria um novo banco de horas com a quantidade 
        de *horas* e *minutos*'''
        
        self.Minutos = (horas * 60) + minutos

    def DepositaHorasMinutos(self, horas: int, minutos: int):
        '''Adiciona a quantidade de *horas* e *minutos* em um 
        banco de horas existente
        >>> b = BancoHoras(2,30)
        >>> b.DepositaHorasMinutos(1,10)
        >>> b.consulta()
        '3:40'
        '''

        self.Minutos += (horas * 60) + minutos
        
    def SaqueHorasMinutos(self, horas: int, minutos: int):
        '''Diminui a quantidade de *horas* e *minutos* do saldo
        existente no banco de horas. Caso o saldo seja insuficiente
        não faz nada
        >>> b = BancoHoras(3,20)
        >>> b.SaqueHorasMinutos(1,30)
        >>> b.consulta()
        '1:50'
        >>> b1 = BancoHoras(3,20)
        >>> b1.SaqueHorasMinutos(3,30)
        >>> b1.consulta()
        '3:20'
        '''

        total_min = (horas * 60) + minutos
        if self.Minutos >= total_min:
            self.Minutos -= total_min


    def consulta(self):
        '''Retorna a quantidade de horas e minutos do banco de horas
        transformados em uma string
        Exemplos:
        >>> b = BancoHoras(1,20)
        >>> b.consulta()
        '1:20'
        >>> b1 = BancoHoras(2,45)
        >>> b1.consulta()
        '2:45'
        '''

        hr = self.Minutos // 60
        min = self.Minutos % 60
        return str(hr) + ':' + str(min)
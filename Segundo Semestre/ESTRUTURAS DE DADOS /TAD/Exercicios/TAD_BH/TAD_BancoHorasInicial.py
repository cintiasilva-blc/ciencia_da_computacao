from __future__ import annotations
from dataclasses import dataclass

class BancoHoras:
    Horas: int
    Minutos: int

    def __init__(self, horas: int, minutos: int):
        '''Cria um novo banco de horas com a quantidade 
        de *horas* e *minutos*'''
        
        if minutos < 60:
            self.Horas = horas
            self.Minutos = minutos
        else:
            self.Horas = horas + (minutos // 60)
            self.Minutos = minutos % 60

    def DepositaHorasMinutos(self, horas: int, minutos: int):
        '''Adiciona a quantidade de *horas* e *minutos* em um 
        banco de horas existente
        >>> b = BancoHoras(2,30)
        >>> b.DepositaHorasMinutos(1,10)
        >>> b.consulta()
        '3:40'
        '''

        hr = self.Horas + horas
        min = self.Minutos + minutos

        if min > 60:
            hr = min // 60
            min = min % 60

        self.Horas = hr
        self.Minutos = min

        
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

        total_min = (self.Horas * 60) + self.Minutos
        saque_total = total_min - ((horas * 60) + minutos)

        if saque_total > 0:
            self.Horas = saque_total // 60
            self.Minutos = saque_total % 60
        else:
            self.Horas = self.Horas
            self.Minutos = self.Minutos


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

        return str(self.Horas) + ':' + str(self.Minutos)
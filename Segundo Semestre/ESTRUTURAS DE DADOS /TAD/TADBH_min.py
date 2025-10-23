from __future__ import annotations
from dataclasses import dataclass

class BancoHoras:
    Minutos: int

    def __init__(self, min: int):
        self.Minutos = min 
    
    def DepositaHorasMinutos(self, horas: int, minutos: int):
        '''Adiciona a quantidade de *horas* e *minutos* em um 
        banco de horas existente
        >>> b = BancoHoras(2,30)
        >>> b.DepositaHorasMinutos(1,10)
        >>> b.consulta()
        '3:40'
        '''
        
        

        
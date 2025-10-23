'''Fa ̧ca uma implementa ̧c ̃ao alternativa (diferente do exerc ́ıcio anterior) da classe BancoHoras
usando um campo para armazenar o saldo em minutos. Fa ̧ca a sua implementa ̧c ̃ao no arquivo
bancohoras min.py. Compare as duas implementa ̧c ̃oes e discuta qual  ́e a mais adequada.'''

from TAD_BancoHorasAlt import *

def input():
    hr: int = 0
    min: int = 0
    add_hr: int = 3
    add_min: int = 28
    saque_hr: int = 1
    saque_min: int = 11

    b = BancoHoras(hr, min)
    b.consulta()
    b.DepositaHorasMinutos(add_hr, add_min)
    b.consulta()
    b.SaqueHorasMinutos(saque_hr, saque_min)
    b.consulta()

input()
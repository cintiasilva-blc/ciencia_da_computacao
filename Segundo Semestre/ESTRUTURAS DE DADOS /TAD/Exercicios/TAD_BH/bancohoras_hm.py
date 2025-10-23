'''Em alguns empresas  ́e comum o uso de um banco de horas, que  ́e um esquema de compensa ̧c ̃ao
de horas extras. Quando um funcion ́ario trabalha al ́em da sua jornada normal, as horas e

minutos extras trabalhados s ̃ao “depositados” em um banco de horas. Posteriormente o fun-
cion ́ario pode usar o saldo no banco de horas para se ausentar do trabalho. Projete um TAD

BancoHoras com opera ̧c ̃oes para dep ́osito de horas e minutos, “saque” de horas e minutos (o
saldo deve ser suficiente) e consulta de saldo (que deve gerar uma string no formato HH:MM).

Em qualquer opera ̧c ̃ao a quantidade de minutos n ̃ao podem ser maior que 60. Fa ̧ca uma imple-
menta ̧c ̃ao da classe BancoHoras usando dois campos, uma para horas e outros para minutos.

Fa ̧ca a sua implementa ̧c ̃ao no arquivo bancohoras hm.py.'''


from TAD_BancoHorasInicial import *

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
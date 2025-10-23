'''1. Vocˆe  ́e um programador contratado para desenvolver um sistema de c ́alculo de pre ̧cos para uma
pizzaria. O propriet ́ario forneceu as seguintes regras para calcular o pre ̧co de uma pizza:
(a) Pre ̧co Base:
• M ̃ao de obra do pizzaiolo: R$ 10,00
• Massa b ́asica: R$ 5,00
(b) Tamanho da Pizza (aumenta o pre ̧co base):
• Pequena: acr ́escimo de 10%
• M ́edia: acr ́escimo de 20%
• Grande: acr ́escimo de 30%
(c) Ingredientes (pre ̧co por unidade):
• Queijo: R$ 3,00
• Bacon: R$ 4,00
• Cebola: R$ 1,00
• Azeitona: R$ 2,00
S ̃ao sempre trˆes ingrediente. Valor da pizza  ́e a soma dos custos. DICA: use o valor dos
ingredientes como o “value” do tipo enumerado.'''

from enum import Enum, auto
from dataclasses import dataclass

class Ingredientes(Enum):
    QUEIJO = 3
    BACON = 4
    CEBOLA = 1
    AZEITONA = 2

class Tamanho(Enum):
    PEQUENA = 0.1
    MEDIA = 0.2
    GRANDE = 0.3

def CalculaPreçoPizza(tam: Tamanho, ing1: Ingredientes, ing2: Ingredientes, ing3: Ingredientes) -> float:
    '''Exemplos:
    >>> CalculaPreçoPizza(Tamanho.PEQUENA, Ingredientes.QUEIJO, Ingredientes.BACON, Ingredientes.CEBOLA)
    23.8
    >>> CalculaPreçoPizza(Tamanho.GRANDE, Ingredientes.AZEITONA, Ingredientes.BACON, Ingredientes.CEBOLA)
    24.1
    '''

    preco_base = 15
    soma_ing = ing1.value + ing2.value + ing3.value
    adicional = (soma_ing) * tam.value
    valor_total = (preco_base + soma_ing) + adicional

    return valor_total



'''2) 2. Uma empresa de e-commerce precisa gerenciar um cat ́alogo de produtos. Cada produto tem
um c ́odigo, nome, pre ̧co, categoria e estoque dispon ́ıvel. A empresa tamb ́em precisa calcular o
valor do frete com base no peso e dimens ̃oes do produto.
Regras de neg ́ocio:
• O frete base  ́e calculado com base no peso do produto = peso X 0.5
• O frete por volume  ́e calculado com base no volume do produto = volume X 0.001
• O frete por seguro  ́e calculado com base no valor do produto = valor do produto X 0.01
Al ́em disso o valor do frete varia conforme a regi ̃ao onde ser ́a a entrega conforme a seguinte
regra:
• Sul = 1.0
• Sudeste = 1.1
• Centro-Oeste = 1.2
• Nordeste = 1.3
• Norte = 1.4
Valor final  ́e a soma dos pre ̧cos vezes o multiplicador regional.’'''



@dataclass
class Produto:
    Codigo: str
    Nome: str
    Preco: float
    Categoria: str
    Estoque: int

class Regiao(Enum):
    SUL = 1.0
    SUDESTE = 1.1
    CENTRO_OESTE = 1.2
    NORDESTE = 1.3
    NORTE = 1.4



def ValorFinalFrete(peso: float, volume: float, vl_produto: Produto, reg: Regiao) -> float:
    '''Exemplos:
    >>> ValorFinalFrete(2, 1000, 100, Regiao.SUDESTE)
    3.3
    >>> ValorFinalFrete(5, 1500, 200, Regiao.NORDESTE)
    7.8
    >>> ValorFinalFrete(0.5, 2000, 50, Regiao.SUL)
    2.75
    '''

    frete_base = peso * 0.5
    frete_volume = volume * 0.001
    frete_produto = vl_produto * 0.01

    valor_final = (frete_produto + frete_base + frete_volume) * reg.value
    return round(valor_final, 2)







    

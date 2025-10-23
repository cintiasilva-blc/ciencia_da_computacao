'''2) Escreva os exemplos e implemente a função de acordo com a assinatura e o propósito a seguir.'''

def dma_para_amd(data: str) -> str:
    '''
    Transforma *data*, que deve estar no formato "dia/mes/ano",
    onde dia e mes tem dois dígitos e ano tem quatro dígitos,
    para o formato "ano/mes/dia".

    Exemplos: 
    >>> dma_para_amd('27/11/2007')
    '2007/11/27'
    >>> dma_para_amd('29/03/2007')
    '2007/03/29'
    '''

    ano = data[6:]
    dia = data[:2]
    mes = data[2:6]

    return ano + mes + dia
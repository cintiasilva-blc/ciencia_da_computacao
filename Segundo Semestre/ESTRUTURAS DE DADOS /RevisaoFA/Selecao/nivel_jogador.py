'''Em um determinado jogo os jogadores são classificados em níveis de 0 a 25 e este nível é atualizado
semanalmente baseado na quantidade de horas que o jogador jogou o jogo. Os jogadores que jogaram
entre 4 e 5 horas permanecem no mesmo nível. Os jogadores que jogaram menos que 4 horas diminuem
um nível a cada 1 hora que faltou para alcançar as 4 horas. Os jogadores que jogaram mais de 5 horas
aumentam um nível a cada hora jogada além das 5 horas respeitando o limite máximo de 7 níveis.
Projete uma função que recebe o nível atual do jogador e a quantidade de horas jogadas em uma
semana e calcule o novo nível do jogador.'''

def nivel_jogador(nivel_atual: int, horas_jogadas: int) -> int:
    ''' Recebe o nivel atual de um jogador, a quantidade de horas jogas na semana e calcula o novo nivel do jogador.
    
    Exemplos:
    >>> nivel_jogador(22, 2)
    20
    >>> nivel_jogador(22, 24)
    29
    >>> nivel_jogador(22, 5)
    22
    '''


    if horas_jogadas < 4: 
        hr_faltante = 4 - horas_jogadas
        nivel_atual = nivel_atual - hr_faltante
    elif horas_jogadas > 5:
        if horas_jogadas >= 7:
            nivel_atual = nivel_atual + 7
        else: 
            hr_excedente = horas_jogadas - 5
            nivel_atual =nivel_atual + hr_excedente
    else:
        nivel_atual = nivel_atual
    return nivel_atual





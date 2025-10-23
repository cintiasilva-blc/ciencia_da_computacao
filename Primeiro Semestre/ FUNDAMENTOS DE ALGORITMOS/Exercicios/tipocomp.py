from dataclasses import dataclass

'''1)Projete trˆes fun ̧c ̃oes: a fun ̧c ̃ao main deve cadastrar como entrada o RA, o nome e o curso de um
aluno. Essas informa ̧c ̃oes ser ̃ao passadas para uma fun ̧c ̃ao que deve atribuir essas informa ̧c ̃oes
a um dado composto. Depois de retornar a estrutura cadastrada, chame a terceira fun ̧c ̃ao para
imprimir o dado composto que foi cadastrado.'''
@dataclass
class Aluno:
    ra: str
    nome: str
    curso: str

def AtribuiComp(RA, Nome, Curso) -> Aluno:
    '''Exemplos:
    >>> AtribuiComp('145107', 'cintia', 'ciencia da computação')
    Aluno(ra='145107', nome='cintia', curso='ciencia da computação')
    >>> AtribuiComp('145217', 'ana', 'enfermagem')
    Aluno(ra='145217', nome='ana', curso='enfermagem')
    '''
    aluno = Aluno(RA, Nome, Curso)
    return aluno


def main():
    RA = str(input("Digite um RA: "))
    Nome = str(input("Digite um nome: "))
    Curso = str(input("Digite um curso: "))

    aluno = AtribuiComp(RA, Nome, Curso)


if __name__ == '__main__':
    main()




'''2) Escreva uma fun ̧c ̃ao que receba um n ́umero inteiro que representa um intervalo de tempo medido
em minutos e devolva uma estrutura contendo o n ́umero equivalente de horas e minutos (por
exemplo, 131 minutos equivalem a 2 horas e 11 minutos). Use um tipo composto que tenha
um campo horas(inteiro) e minutos(inteiro).'''

@dataclass
class Tempo:
    hora: int
    minuto: int

def RepresentaHrMin(qtd_tempo: int) -> Tempo:
    '''Exemplos:
    >>> RepresentaHrMin(131)
    Tempo(hora=2, minuto=11)
    '''

    hr = qtd_tempo // 60
    min =  qtd_tempo - (hr * 60)
    tempo = Tempo(hr, min)

    return tempo

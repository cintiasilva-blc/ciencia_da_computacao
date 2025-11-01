from TADColecaoFigurinhas_D import *


def testa_basico():
    print('==== TESTE DE INSERÇÃO E LISTAGEM ===')
    c1 = ColecaoFigurinhas()
    lst = [1,1,1,2,3,4,4,6,8,60,60,8,8,7,7]
    for i in lst:
        c1.insere_fig(figurinha(i))
    print('Coleção C1 inteira: ', c1.mostra_colecao())
    print('Coleção C1 sem considerar repetidas: ', c1.figurinhas_unicas())
    print('Figurinhas repetidas: ', c1.figurinhas_rep())



def testa_remocao():
    print('==== TESTE DE REMOÇÃO =======')
    c = ColecaoFigurinhas()
    c.insere_fig(figurinha(1))
    c.insere_fig(figurinha(2))
    c.insere_fig(figurinha(3))
    c.insere_fig(figurinha(4))
    c.insere_fig(figurinha(5))

    print('Antes:', c.figurinhas_unicas())
    c.remove_fig(figurinha(3))
    print('Depois:', c.figurinhas_unicas())

def troca_maxima():
    print('==== TESTE DE TROCA MÁXIMA ====')
    c1 = ColecaoFigurinhas()
    c2 = ColecaoFigurinhas()

    lst = [1, 1, 2, 3, 3, 4, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]
    for i in lst:
        c1.insere_fig(figurinha(i))

    lst1 =  [3, 4, 5, 5, 6, 6, 7, 7, 8, 8, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27]
    for j in lst1:
        c2.insere_fig(figurinha(j))


    print('Coleção C1 (antes/sem considerar repetições):', c1.figurinhas_unicas())
    print('Coleção C2 (antes/sem considerar repetições):', c2.figurinhas_unicas())

    trocas = c1.determina_trocas(c2)

    print('Foram realizadas' ,trocas ,'trocas.')
    print('\nColeção C1 (depois):', c1.figurinhas_unicas())
    print('Coleção C2 (depois):', c2.figurinhas_unicas())

def main():
    testa_basico()
    print()
    testa_remocao()
    print()
    troca_maxima()

if __name__ == '__main__':
    main()
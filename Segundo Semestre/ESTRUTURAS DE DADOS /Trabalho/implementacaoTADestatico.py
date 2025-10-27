from TADColecaoFIg_estatico import *

def main():
    '''Implementação do TADColecao de figurinhas estatico, contendo as seguintes operações:
        - Criação de uma coleção;
        - Inserção de figurinhas;
        - Remoção de figurinhas;
        - Listagem de figurinhas unicas;
        - Listagem de figurinhas e suas repetições na coleção;
        - Troca maxima entre duas coleções.
        '''

    c1 = Colecao(10)
    c2 = Colecao(10)

    print('Inserção de figurinhas na coleção 1: ')
    figC = [6, 6, 4, 9, 10, 10, 10, 10, 3]
    for i in figC:
        print('Figurinha: ', i)
        c1.insere_figurinha(fig(i))
    print()
    print('Inserção de figurinhas na coleção 2: ')
    figC2 = [1, 1, 1, 4, 7, 2, 2, 5,]
    for i in figC2:
        print('Figurinha: ', i)
        c2.insere_figurinha(fig(i))
    print()
    
    print("Coleção 1:", c1.lista_figurinhas())
    print("Repetidas C1:", c1.figurinhas_rep())
    print()
    print('Coleçao 2: ', c2.lista_figurinhas())
    print('Repetidas C2: ', c2.figurinhas_rep())
    print()

    trocas = c1.troca_maxima(c2)
    print('Trocas realizadas: ', trocas)
    
    print('Após trocas: ')
    print("Coleção 1:", c1.lista_figurinhas())
    print("Coleção 2:", c2.lista_figurinhas())
    print()

    print('Remove C1: ', c1.remove_valor(4))
    print('C1:', c1.lista_figurinhas())
    print()

    print('Remove C2: ', c2.remove_valor(5))
    print('C2:', c2.lista_figurinhas())


main()
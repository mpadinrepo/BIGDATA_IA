def imprimir_tabuleiro():
    for linha in tabuleiro:
        print('|'.join(linha))
        print('-' * 5)
        imprimir_tabuleiro()
import pygame
import tela_inicial
from jogo import *

def main():
    pygame.init()

    while True:
        acao = tela_inicial.iniciar_tela()  # Exibe a tela inicial e espera ação

        if acao == "jogar":
            iniciar_jogo()  # Inicia o jogo
        elif acao == "sair":
            pygame.quit()
            exit()

if __name__ == '__main__':
    main()
import pygame
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'

class Map:
    def __init__(self, tamanho_bloco, tela): # Corrigi os parâmetros utilizados.
        self.mapa = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,1],
        [1,0,1,1,1,0,0,0,1,0,0,0,1,0,1,1,0,0,0,1,0,0,0,0,1],
        [1,0,0,0,0,1,0,1,1,1,0,0,1,0,0,0,1,0,1,0,0,0,1,0,1],
        [1,1,0,1,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,1,1,1,0,1],
        [1,0,0,1,0,1,1,0,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,1,0,0,1,1,0,1,1,0,0,0,0,0,1,0,1,0,1,1,0,1,1,1],
        [1,0,0,0,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,1],
        [1,0,1,1,0,0,1,0,1,0,0,0,1,0,0,0,0,1,1,0,1,1,1,0,1],
        [0,0,1,1,0,1,0,0,0,0,1,0,0,1,0,1,1,1,0,0,0,0,1,0,0],
        [1,0,1,1,0,1,0,1,1,1,0,1,0,0,0,0,1,0,0,1,0,0,1,0,1],
        [1,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,1,1,0,1],
        [1,1,1,1,0,1,1,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,1],
        [1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1]]

        self.tamanho_do_bloco = tamanho_bloco # Corrigi o tamanhao do bloco.
        self.tela = tela # Corrigi o parâmetro para o tamanho da tela ser chamado no ´player.py´.
        self.LARGURA = len(self.mapa[0]) * self.tamanho_do_bloco
        self.ALTURA = len(self.mapa) * self.tamanho_do_bloco

        self.parede = pygame.image.load("assets/parede.png") 
        self.parede = pygame.transform.scale(self.parede, (self.tamanho_do_bloco, self.tamanho_do_bloco))

        self.chao  = pygame.image.load("assets/chão.png") 
        self.chao  = pygame.transform.scale(self.chao, (self.tamanho_do_bloco, self.tamanho_do_bloco))

        #pygame.init()
        self.tela = pygame.display.set_mode((self.LARGURA, self.ALTURA))
        pygame.display.set_caption("Mapa")

        # Fundo

    def desenhar(self):
        # Configurações do Pygame
        for coluna in range(len(self.mapa)):
            for linha in range(len(self.mapa[coluna])):
                if self.mapa[coluna][linha] == 1:  # Se for parede
                    self.tela.blit(self.parede,(linha * self.tamanho_do_bloco, coluna * self.tamanho_do_bloco))
                else:
                    self.tela.blit(self.chao,(linha * self.tamanho_do_bloco, coluna * self.tamanho_do_bloco))
    pygame.quit()
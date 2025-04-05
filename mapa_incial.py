import pygame
class Map:
    def __init__(self, tamanho_do_bloco, mapa, LARGURA, ALTURA, parede, chao, tela):
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

        self.tamanho_do_bloco = 34
        self.LARGURA = len(self.mapa[0]) * self.tamanho_do_bloco
        self.ALTURA = len(self.mapa) * self.tamanho_do_bloco

        self.parede = pygame.image.load(r"assets\parede.png", "r") 
        self.parede = pygame.transform.scale(self.parede, (self.tamanho_do_bloco, self.tamanho_do_bloco))

        self.chao  = pygame.image.load(r"assets\chão.png", "r") 
        self.chao  = pygame.transform.scale(self.chao, (self.tamanho_do_bloco, self.tamanho_do_bloco))

        pygame.init()
        self.tela = pygame.display.set_mode((self.LARGURA, self.ALTURA))
        pygame.display.set_caption("Nine vs Bozo")

         # Fundo

    def desenhar(self):
        # Configurações do Pygame
        
        rodando = True
        while rodando:
            self.tela.fill(150, 200, 200)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False

            for coluna in range(len(self.mapa)):
                for linha in range(len(self.mapa[coluna])):
                    if self.mapa[coluna][linha] == 1:  # Se for parede
                        self.tela.blit(self.parede,(linha * self.tamanho_do_bloco, coluna * self.tamanho_do_bloco))
                    else:
                        self.tela.blit(self.chao,(linha * self.tamanho_do_bloco, coluna * self.tamanho_do_bloco) )
            pygame.display.flip()
            
        pygame.quit()

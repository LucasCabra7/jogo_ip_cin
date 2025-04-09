import pygame
import math
from colisoes import Colisao
class Inimigo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidade = 1

        # Carregando várias sprites por direção
        self.sprites = {
            "baixo": [pygame.image.load(f"assets/frente_passo{i}.png") for i in range(1, 3)],
            "cima": [pygame.image.load(f"assets/costa_policial_{i}.png") for i in range(1, 3)],
            "esquerda": [pygame.image.load(f"assets/esquerda_policial_{i}.png") for i in range(1, 4)],
            "direita": [pygame.image.load(f"assets/direita_policial_{i}.png") for i in range(1, 4)],
        }

        self.direcao = "baixo"
        self.frame_atual = 0
        self.contador_frames = 0
        self.sprite_atual = self.sprites[self.direcao][self.frame_atual]

    def atualizar_sprite(self):
        self.contador_frames += 1
        if self.contador_frames >= 10:
            sprites_direcao = self.sprites[self.direcao]
            self.frame_atual = (self.frame_atual + 1) % len(sprites_direcao)
            self.sprite_atual = sprites_direcao[self.frame_atual]
            self.contador_frames = 0

    def desenhar(self, tela):
        tela.blit(self.sprite_atual, (self.x, self.y))

    def checar_colisao(self, x_player, y_player, largura_player, altura_player):
        rect_inimigo = pygame.Rect(self.x, self.y, self.sprite_atual.get_width(), self.sprite_atual.get_height())
        rect_player = pygame.Rect(x_player, y_player, largura_player, altura_player)
        return rect_inimigo.colliderect(rect_player)

    def mover_em_direcao(self, x_player, y_player):
        direcoes = ["esquerda", "direita", "cima", "baixo"]
        dst_init = math.sqrt((x_player - self.x)**2 + (y_player - self.y)**2)
        distancias = [math.sqrt((x_player - (self.x - self.velocidade))**2 + (y_player - self.y)**2),
                        math.sqrt((x_player - (self.x + self.velocidade))**2 + (y_player - self.y)**2),
                         math.sqrt((x_player - self.x)**2 + (y_player - (self.y - self.velocidade))**2),
                          math.sqrt((x_player - self.x)**2 + (y_player - (self.y + self.velocidade))**2)]
        distancias_copy = distancias.copy()
        direcoes_copy = direcoes.copy()
        for dst in range(len(distancias_copy)):
            novo_x, novo_y, bateu = Colisao.verificar_colisao_parede(self.x, self.y, self.velocidade, direcoes_copy[dst]) 
            if bateu == True:
                distancias.remove(distancias_copy[dst])
                direcoes.remove(direcoes_copy[dst])
        menor = min(distancias)
        melhor_direcao = direcoes[distancias.index(menor)]
        self.x, self.y, bateu = Colisao.verificar_colisao_parede(self.x, self.y, self.velocidade, melhor_direcao)
        self.direcao = melhor_direcao
        self.atualizar_sprite()


    
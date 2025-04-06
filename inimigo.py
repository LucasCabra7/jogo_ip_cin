import pygame
import math

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

    def mover_em_direcao(self, x_player, y_player):
        dx = x_player - self.x
        dy = y_player - self.y
        distancia = math.hypot(dx, dy)

        if distancia != 0:
            self.x += self.velocidade * (dx / distancia)
            self.y += self.velocidade * (dy / distancia)

        self.atualizar_direcao(dx, dy)
        self.atualizar_sprite()

    def atualizar_direcao(self, dx, dy):
        if abs(dx) > abs(dy):
            self.direcao = "direita" if dx > 0 else "esquerda"
        else:
            self.direcao = "baixo" if dy > 0 else "cima"

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

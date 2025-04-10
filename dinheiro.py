import pygame
import math
from colisoes import Colisao
pygame.init()
pygame.mixer.init()
class Dinheiro:
    def __init__(self, x, y):
        self.x, self.y, self.velocidade = x, y, 0
        self.carregar_sprites()  # Corrigido: precisa ser chamado antes de usar self.sprites
        self.direcao = "1"
        self.sprite_atual = self.sprites[self.direcao][0]
        self.indice_sprite = 0
        self.frame_atual = 0
        self.intervalo_sprite = 10

    def carregar_sprites(self):
        self.sprites = {
            '1': [pygame.image.load(f"assets/bolsa_{i}.png") for i in range(1, 5)],
            '2': [pygame.image.load(f"assets/bolsa_{i}.png") for i in range(1, 5)],
            '3': [pygame.image.load(f"assets/bolsa_{i}.png") for i in range(1, 5)],
            '4': [pygame.image.load(f"assets/bolsa_{i}.png") for i in range(1, 5)],
            '5': [pygame.image.load(f"assets/bolsa_{i}.png") for i in range(1, 5)]
        }

    def atualizar_sprite(self):
        self.frame_atual += 1
        if (self.frame_atual >= self.intervalo_sprite):
            self.sprite_atual = self.sprites[self.direcao][self.indice_sprite]
            self.indice_sprite = (self.indice_sprite + 1) % 4
            self.frame_atual = 0

    def checar_colisao(self, x_player, y_player, largura_player, altura_player):
        rect_dinheiro = pygame.Rect(self.x, self.y, self.sprite_atual.get_width(), self.sprite_atual.get_height())
        rect_player = pygame.Rect(x_player, y_player, largura_player, altura_player)
        return rect_dinheiro.colliderect(rect_player)

    def desenhar(self, tela):
        tela.blit(self.sprite_atual, (self.x, self.y))

    
        self.atualizar_sprite()
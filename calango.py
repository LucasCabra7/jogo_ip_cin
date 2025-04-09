import pygame
import math
from colisoes import Colisao
pygame.init()
pygame.mixer.init()
class Calango:
    def __init__(self, x, y):
        self.x, self.y, self.velocidade = x, y, 2
        self.carregar_sprites()  # Corrigido: precisa ser chamado antes de usar self.sprites
        self.direcao = "cima"
        self.sprite_atual = self.sprites[self.direcao][0]
        self.indice_sprite = 0
        self.frame_atual = 0
        self.intervalo_sprite = 10

    def carregar_sprites(self):
        self.sprites = {
            'esquerda': [pygame.image.load(f"assets/calango_esquerda_{i}.png") for i in range(1, 5)],
            'direita': [pygame.image.load(f"assets/calango_direita_{i}.png") for i in range(1, 5)],
            'cima': [pygame.image.load(f"assets/calango_cima_{i}.png") for i in range(1, 5)],
            'baixo': [pygame.image.load(f"assets/calango_baixo_{i}.png") for i in range(1, 5)]
        }

    def atualizar_sprite(self):
        self.frame_atual += 1
        if self.frame_atual >= self.intervalo_sprite:
            self.sprite_atual = self.sprites[self.direcao][self.indice_sprite]
            self.indice_sprite = (self.indice_sprite + 1) % 4
            self.frame_atual = 0

    def checar_colisao(self, x_player, y_player, largura_player, altura_player):
        rect_calango = pygame.Rect(self.x, self.y, self.sprite_atual.get_width(), self.sprite_atual.get_height())
        rect_player = pygame.Rect(x_player, y_player, largura_player, altura_player)
        return rect_calango.colliderect(rect_player)

    def desenhar(self, tela):
        tela.blit(self.sprite_atual, (self.x, self.y))

    def fugir(self, x_player, y_player):
        direcoes = ["esquerda", "direita", "cima", "baixo"]
        dict_direcao = {}

        for direcao in direcoes:
            novo_x, novo_y, bateu = Colisao.verificar_colisao_parede(self.x, self.y, self.velocidade, direcao)
            if not bateu:
                distancia = math.sqrt((x_player - novo_x)**2 + (y_player - novo_y)**2)
                dict_direcao[direcao] = distancia

        if dict_direcao:
            self.direcao = max(dict_direcao, key=dict_direcao.get)
            self.x, self.y, _ = Colisao.verificar_colisao_parede(self.x, self.y, self.velocidade, self.direcao)
            pygame.mixer.music.load("assets/calango correndo.mp3")
            pygame.mixer.music.set_volume(0.3)
            pygame.mixer.music.play()

        self.atualizar_sprite()
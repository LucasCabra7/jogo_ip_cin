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
        dict_direcao = {}
        
        # Primeiro: verificar todas as direções possíveis
        for direcao in direcoes:
            novo_x, novo_y, bateu = Colisao.verificar_colisao_parede(self.x, self.y, self.velocidade, direcao)
            if not bateu:
                # Calcula a distância até o jogador para esta direção válida
                distancia = math.sqrt((x_player - novo_x)**2 + (y_player - novo_y)**2)
                dict_direcao[direcao] = distancia
        
        # Se houver direções válidas
        if dict_direcao:
            # Encontra a direção que mais aproxima do jogador ou mais se distancia
            melhor_direcao = min(dict_direcao.keys(), key=lambda k: dict_direcao[k])
            self.x, self.y, _ = Colisao.verificar_colisao_parede(self.x, self.y, self.velocidade, melhor_direcao)
            self.direcao = melhor_direcao
        
        self.atualizar_sprite()
import pygame
import random
import math

class Inimigo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidade = 2 #velocidade do inimigo
        
        #carrega as duas sprites de frente para a animação
        self.sprites = [
            pygame.image.load("assets/frente_passo1.png"),
            pygame.image.load("assets/frente_passo2.png")
        ]
        
        self.sprite_atual = self.sprites[0] #começa com a primeira sprite
        self.frame_atual = 0 #indice da sprite atual
        self.contador_frames = 0 #contador para alternar sprites
    
    def mover_em_direcao(self, x_player, y_player):
        """Move o inimigo em direção ao jogador"""
        distancia_x = x_player - self.x
        distancia_y = y_player - self.y
        distancia = math.sqrt(distancia_x**2 + distancia_y**2)

        if distancia != 0:
            self.x += self.velocidade * (distancia_x / distancia)
            self.y += self.velocidade * (distancia_y / distancia)

        #atualiza a sprite para simular o movimento
        self.atualizar_sprite()
    
    def atualizar_sprite(self):
        """Alterna entre os dois sprites de frente para simular caminhada"""
        self.contador_frames += 1
        if self.contador_frames >= 10: #altera a cada 10 frames
            self.frame_atual = 1 - self.frame_atual #alterna entre 0 e 1
            self.sprite_atual = self.sprites[self.frame_atual]
            self.contador_frames = 0 #reseta o contador
    
    def desenhar(self, tela):
        """Desenha o inimigo na tela"""
        tela.blit(self.sprite_atual, (self.x, self.y)) #usa a sprite animada
    
    def checar_colisao(self, x_player, y_player, largura_player, altura_player):
        """Verifica colisão com o jogador"""
        rect_inimigo = pygame.Rect(self.x, self.y, self.sprite_atual.get_width(), self.sprite_atual.get_height())
        rect_player = pygame.Rect(x_player, y_player, largura_player, altura_player)

        return rect_inimigo.colliderect(rect_player)

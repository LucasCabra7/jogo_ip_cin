import pygame
import random
from inimigo import Inimigo #vai importar a classe do inimigo
import colisoes
from mapa_inicial import Map

pygame.init()

class Player:
    def __init__(self): # Criando a função principal com parâmetros:
        self.x_player = 100 # Largura do boneco
        self.y_player = 100 # Altura do boneco
        self.velocidade = 1
        self.direcao_player = "parado" # Inicia com a direção parado.
        self.carregar_sprites() # Função e carregar os sprites a cada interação.

    def carregar_sprites(self):
        #carrega os sprites do boneco
        self.sprite_parado = pygame.image.load("assets/boneco_parado.png")
        self.sprite_esquerda = [pygame.image.load(f"assets/esquerda_{i}.png") for i in range(1, 4)]
        self.sprite_direita = [pygame.image.load(f"assets/direita_{i}.png") for i in range(1, 4)]
        self.sprite_cima = [pygame.image.load(f"assets/cima_{i}.png") for i in range(1, 4)]
        self.sprite_baixo = [pygame.image.load(f"assets/baixo_{i}.png") for i in range(1, 4)]
        self.largura_player, self.altura_player = self.sprite_parado.get_width(), self.sprite_parado.get_height() #INVESTIGAR 
        self.indice_sprite = 0 # Controla a troca dos sprites
        self.sprite_atual = self.sprite_parado # Estado inicial

    def mover_player(self, teclas): # Função para verificar as teclas e controlar a velocidade:  
        if teclas[pygame.K_LEFT]:
            self.x_player -= self.velocidade
            self.direcao_player = "esquerda"
        elif teclas[pygame.K_RIGHT]:
            self.x_player += self.velocidade
            self.direcao_player = "direita"
        elif teclas[pygame.K_UP]:
            self.y_player -= self.velocidade
            self.direcao_player = "cima"
        elif teclas[pygame.K_DOWN]:
            self.y_player += self.velocidade
            self.direcao_player = "baixo"
        else:
            self.direcao_player = "parado"

        self.atualizar_sprite() # Chama função de atualizar os Sprites a cada interação nas Teclas.

    def atualizar_sprite(self):
        # Escolhe qual sprite exibir
        if self.direcao_player == "esquerda":
            self.sprite_atual = self.sprite_esquerda[self.indice_sprite]
        elif self.direcao_player == "direita":
            self.sprite_atual = self.sprite_direita[self.indice_sprite]
        elif self.direcao_player == "cima":
            self.sprite_atual = self.sprite_cima[self.indice_sprite]
        elif self.direcao_player == "baixo":
            self.sprite_atual = self.sprite_baixo[self.indice_sprite]
        else:
            self.sprite_atual = self.sprite_parado

        if self.direcao_player != "parado":
            self.indice_sprite = (self.indice_sprite + 1) % 3
    
    def desenhar(self, tela): # Função para desenhar na tela o player:
        tela.blit(self.sprite_atual, (self.x_player, self.y_player)) # Desenhar o sprite atual, ´largura e altura´.
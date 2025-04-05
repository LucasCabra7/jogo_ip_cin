import pygame
import random
from inimigo import Inimigo #vai importar a classe do inimigo
import colisoes
pygame.init()

class Player:
    def __init__(self, x_player, y_player, direcao_player):
        self.x_player, self.y_player, self.direcao_player = x_player, y_player, direcao_player
    pygame.time.delay(100) #controla a velocidade da animação

    def carregar_sprites(self):
        #carrega os sprites do boneco
        self.sprite_parado = pygame.image.load("assets/boneco_parado.png")
        self.sprite_esquerda = [pygame.image.load(f"assets/esquerda_{i}.png") for i in range(1, 4)]
        self.sprite_direita = [pygame.image.load(f"assets/direita_{i}.png") for i in range(1, 4)]
        self.sprite_cima = [pygame.image.load(f"assets/cima_{i}.png") for i in range(1, 4)]
        self.sprite_baixo = [pygame.image.load(f"assets/baixo_{i}.png") for i in range(1, 4)]
        self.largura_player, self.altura_player = self.sprite_parado.get_width(), self.sprite_parado.get_height() #INVESTIGAR 
        self.indice_sprite = 0 #Controla a troca dos sprites
        self.direcao_player = "parado" #Estado inicial
        #captura self.teclas pressionadas

    def mover_player(self):    
        self.teclas = pygame.key.get_pressed()
        self.velocidade = 15 #velocidade do personagem
        #bloco de teclas:
        if self.teclas[pygame.K_LEFT]:  
            self.direcao_player = "esquerda"
            sprite_parado = pygame.image.load("assets/esquerda_1.png")
        elif self.teclas[pygame.K_RIGHT]:   
            self.direcao_player = "direita"
            sprite_parado = pygame.image.load("assets/direita_1.png")
        elif self.teclas[pygame.K_UP]:   
            self.direcao_player = "cima"
            sprite_parado = pygame.image.load("assets/cima_1.png")
        elif self.teclas[pygame.K_DOWN]:  
            self.direcao_player = "baixo"
            sprite_parado = pygame.image.load("assets/boneco_parado.png")
        else:
            self.direcao_player = "parado"
            sprite_parado = pygame.image.load("assets/boneco_parado.png") 
        # self.x_player, self.y_player = chamar função verificar colisão(self.x_player, self.y_player, self.velocidade, self.direcao_player)
        # atualiza o sprite do inimigo com base na direção do jogador
        inimigo.atualizar_sprite()     

        inimigo.mover_em_self.direcao_player(self.x_player, self.y_player) 

        #Atualiza o índice do sprite para a animação
        if self.direcao_player in ["esquerda", "direita", "cima", "baixo"]:
            self.indice_sprite = (self.indice_sprite + 1) % 3
        else:
            self.indice_sprite = 0

        # Escolhe qual sprite exibir
        if self.direcao_player == "esquerda":
            self.player = self.sprite_esquerda[self.indice_sprite]
        elif self.direcao_player == "direita":
            self.player = self.sprite_direita[self.indice_sprite]
        elif self.direcao_player == "cima":
            self.player = self.sprite_cima[self.indice_sprite]
        elif self.direcao_player == "baixo":
            self.player = self.sprite_baixo[self.indice_sprite]
        else:
            self.player= sprite_parado

            #(PARTE INIMIGO)
            #movendo o inimigo em direção ao jogador
            inimigo.mover_em_self.direcao_player(self.x_player, self.y_player)

            #verificando se o inimigo colidiu com o jogador
            if inimigo.checar_colisao(self.x_player, self.y_player, largura_player, altura_player):
                print("O jogador foi pego! Fim de jogo!")
                rodando = False #encerra o jogo
            
            # Desenha boneco atualizado
            tela.blit(self.player, (self.x_player, self.y_player))
            inimigo.desenhar(tela) #desenha o inimigo

            pygame.display.update() #atualiza a tela
     
     #(PARTE INIMIGO)
        #vai criar o inimigo em uma posição aleatória
        inimigo = Inimigo(random.randint(200, 1920), random.randint(200, 1080))

if __name__ == "__main__":
    player_game()
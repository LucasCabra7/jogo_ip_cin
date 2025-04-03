import pygame
import random
from inimigo import Inimigo #vai importar a classe do inimigo

def player_game():
    #vai inicializar o Pygame
    pygame.init()
    pygame.mixer.init()

    class Tela():
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def proporcao(self):
            return pygame.display.set_mode((self.width, self.height)) #cria a tela do jogo

    #cria a instância da classe Tela
    tela_jogo = Tela(1920, 1080)
    #configura a janela do jogo
    tela = tela_jogo.proporcao()
    pygame.display.set_caption("player Game")

    #carrega os sprites do boneco
    sprite_parado = pygame.image.load("assets/boneco_parado.png")
    sprite_esquerda = [pygame.image.load(f"assets/esquerda_{i}.png") for i in range(1, 4)]
    sprite_direita = [pygame.image.load(f"assets/direita_{i}.png") for i in range(1, 4)]
    sprite_cima = [pygame.image.load(f"assets/cima_{i}.png") for i in range(1, 4)]
    sprite_baixo = [pygame.image.load(f"assets/baixo_{i}.png") for i in range(1, 4)]
    
    largura_player, altura_player = sprite_parado.get_width(), sprite_parado.get_height()

    #posição inicial do boneco
    x_player, y_player = 960, 540
    velocidade = 15
    indice_sprite = 0 #Controla a troca dos sprites
    direcao = "parado" #Estado inicial

    #carrega a imagem da joia
    joia = pygame.image.load("assets/joia.png")
    #posicao aleatória da joia
    def posicao_joia():
        x_joia = random.randint(0, 1920)
        y_joia = random.randint(0, 1080)
        return (x_joia, y_joia)
    
    local_joia = posicao_joia()

    #(PARTE INIMIGO)
    #vai criar o inimigo em uma posição aleatória
    inimigo = Inimigo(random.randint(200, 1920), random.randint(200, 1080))

    #loop principal do jogo
    rodando = True
    while rodando:
        pygame.time.delay(100) #controla a velocidade da animação

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False #Fecha o jogo se clicar no "X" 

        #captura teclas pressionadas
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_LEFT]:  
            x_player -= velocidade
            direcao = "esquerda"
            sprite_parado = pygame.image.load("assets/esquerda_1.png")

        elif teclas[pygame.K_RIGHT]:  
            x_player += velocidade
            direcao = "direita"
            sprite_parado = pygame.image.load("assets/direita_1.png")

        elif teclas[pygame.K_UP]:  
            y_player -= velocidade
            direcao = "cima"
            sprite_parado = pygame.image.load("assets/cima_1.png")

        elif teclas[pygame.K_DOWN]:  
            y_player += velocidade
            direcao = "baixo"
            sprite_parado = pygame.image.load("assets/boneco_parado.png")

        else:
            direcao = "parado"
            sprite_parado = pygame.image.load("assets/boneco_parado.png") 

        #atualiza o sprite do inimigo com base na direção do jogador
        inimigo.atualizar_sprite()     

        inimigo.mover_em_direcao(x_player, y_player) 

        #Atualiza o índice do sprite para a animação
        if direcao in ["esquerda", "direita", "cima", "baixo"]:
            indice_sprite = (indice_sprite + 1) % 3
        else:
            indice_sprite = 0

        # Escolhe qual sprite exibir
        if direcao == "esquerda":
            player = sprite_esquerda[indice_sprite]
        elif direcao == "direita":
            player = sprite_direita[indice_sprite]
        elif direcao == "cima":
            player = sprite_cima[indice_sprite]
        elif direcao == "baixo":
            player = sprite_baixo[indice_sprite]
        else:
            player = sprite_parado

        #player pegou a joia
        rect_player = player.get_rect(topleft=(x_player, y_player))
        rect_joia = joia.get_rect(topleft=local_joia)
        
        if rect_player.colliderect(rect_joia):
            local_joia = posicao_joia()

        #(PARTE INIMIGO)
        #movendo o inimigo em direção ao jogador
        inimigo.mover_em_direcao(x_player, y_player)

        #verificando se o inimigo colidiu com o jogador
        if inimigo.checar_colisao(x_player, y_player, largura_player, altura_player):
            print("O jogador foi pego! Fim de jogo!")
            rodando = False #encerra o jogo
        
        # fundo da tela
        tela.fill((255, 255, 255)) #fundo branco

        # Desenha boneco atualizado
        tela.blit(sprite_parado, (x_player, y_player))
        tela.blit(joia, local_joia)
        pygame.draw.rect(tela, (255, 0, 0), rect_player, 2)  # Retângulo do boneco (vermelho)
        pygame.draw.rect(tela, (0, 255, 0), rect_joia, 2)  # Retângulo da joia (verde)
        inimigo.desenhar(tela) #desenha o inimigo

        pygame.display.update() #atualiza a tela

    #encerra o Pygame
    pygame.quit()

if __name__ == "__main__":
    player_game()
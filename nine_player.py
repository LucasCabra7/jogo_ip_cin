import pygame
import random
def player_game():
    # Inicializar o Pygame
    pygame.init()
    pygame.mixer.init()

    class Tela():
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def proporcao(self):
            return pygame.display.set_mode((self.width, self.height))  # Cria a tela do jogo

    # Cria a instância da classe Tela
    tela_jogo = Tela(1920, 1080)

    # Configura a janela do jogo
    tela = tela_jogo.proporcao()
    pygame.display.set_caption("player Game")

    # Carrega os sprites do boneco
    sprite_parado = pygame.image.load("assets/boneco_parado.png")
    sprite_esquerda = [pygame.image.load(f"assets/esquerda_{i}.png") for i in range(1, 4)]
    sprite_direita = [pygame.image.load(f"assets/direita_{i}.png") for i in range(1, 4)]
    sprite_cima = [pygame.image.load(f"assets/cima_{i}.png") for i in range(1, 4)]
    sprite_baixo = [pygame.image.load(f"assets/baixo_{i}.png") for i in range(1, 4)]

    # Posição inicial do boneco
    x_player, y_player = 960, 540
    velocidade = 15
    indice_sprite = 0  # Controla a troca dos sprites
    direcao = "parado"  # Estado inicial

    #carrega a imagem da joia
    joia = pygame.image.load("assets/joia.png")
    # posicao aleatória da joia
    def posicao_joia():
        x_joia = random.randint(0, 1920)
        y_joia = random.randint(0, 1080)
        return (x_joia, y_joia)

    local_joia = posicao_joia()

    # Loop principal do jogo
    rodando = True
    while rodando:
        pygame.time.delay(100)  # Controla a velocidade da animação

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False  # Fecha o jogo se clicar no "X"

        # Captura teclas pressionadas
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
        # Atualiza o índice do sprite para a animação
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

        # fundo da tela
        tela.fill((255, 255, 255))

        # Desenha boneco atualizado
        tela.blit(player, (x_player, y_player))
        tela.blit(joia, local_joia)
        pygame.draw.rect(tela, (255, 0, 0), rect_player, 2)  # Retângulo do boneco (vermelho)
        pygame.draw.rect(tela, (0, 255, 0), rect_joia, 2)  # Retângulo da joia (verde)
        # Atualiza a tela
        pygame.display.update()

    # Encerra o Pygame
    pygame.quit()

if __name__ == "__main__":
    player_game()
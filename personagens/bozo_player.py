import pygame
import random
def bozo_game():
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
    pygame.display.set_caption("Modo bozo")

    # Carrega os sprites do boneco
    sprite_parado = pygame.image.load("assets/boneco_parado.png")
    sprite_esquerda = [pygame.image.load(f"assets/esquerda_{i}.png") for i in range(1, 4)]
    sprite_direita = [pygame.image.load(f"assets/direita_{i}.png") for i in range(1, 4)]
    sprite_cima = [pygame.image.load(f"assets/cima_{i}.png") for i in range(1, 4)]
    sprite_baixo = [pygame.image.load(f"assets/baixo_{i}.png") for i in range(1, 4)]

    # som quando pegar joia

    # Posição inicial do boneco
    x_bozo, y_bozo = 960, 540
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
            x_bozo -= velocidade
            direcao = "esquerda"
            sprite_parado = pygame.image.load("assets/esquerda_1.png")
        elif teclas[pygame.K_RIGHT]:  
            x_bozo += velocidade
            direcao = "direita"
            sprite_parado = pygame.image.load("assets/direita_1.png")
        elif teclas[pygame.K_UP]:  
            y_bozo -= velocidade
            direcao = "cima"
            sprite_parado = pygame.image.load("assets/cima_1.png")
        elif teclas[pygame.K_DOWN]:  
            y_bozo += velocidade
            direcao = "baixo"
            sprite_parado = pygame.image.load("assets/baixo_3.png")
        else:
            direcao = "parado"

        # Atualiza o índice do sprite para a animação
        if direcao in ["esquerda", "direita", "cima", "baixo"]:
            indice_sprite = (indice_sprite + 1) % 3
        else:
            indice_sprite = 0

        # Escolhe qual sprite exibir
        if direcao == "esquerda":
            bozo = sprite_esquerda[indice_sprite]
        elif direcao == "direita":
            bozo = sprite_direita[indice_sprite]
        elif direcao == "cima":
            bozo = sprite_cima[indice_sprite]
        elif direcao == "baixo":
            bozo = sprite_baixo[indice_sprite]
        else:
            bozo = sprite_parado

        #bozo pegou a joia
        rect_bozo = bozo.get_rect(topleft=(x_bozo, y_bozo))
        rect_joia = joia.get_rect(topleft=local_joia)
        
        if rect_bozo.colliderect(rect_joia):
            local_joia = posicao_joia()

        # fundo da tela
        tela.fill((255, 255, 255))

        # Desenha boneco atualizado
        tela.blit(bozo, (x_bozo, y_bozo))
        tela.blit(joia, local_joia)

        # Atualiza a tela
        pygame.display.update()

    # Encerra o Pygame
    pygame.quit()
bozo_game()
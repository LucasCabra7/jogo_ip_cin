import pygame
import botao

def iniciar_tela():
    pygame.init()
    pygame.mixer.init()

    window = pygame.display.set_mode([1280, 800]) # Tamanho da Tela Inicial.
    pygame.display.set_caption("Tela Inicial") # Nome da tela.

    # Carregar imagens
    background = pygame.image.load("assets/CAPA.jpeg")
    button1_img = pygame.image.load("assets/botao_sair.png") # Botão de ´SAIR´.
    button2_img = pygame.image.load("assets/botao_jogar.png") # Botão de ´JOGAR´.

    # Criar botões
    button1 = botao.Button(650, 30, button1_img, 0.4) # ´Eixo X, Eixo Y, Imagem e Escala´.
    button2 = botao.Button(950, 30, button2_img, 0.4) # ´Eixo X, Eixo Y, Imagem e Escala´.

    # Música de fundo
    pygame.mixer.music.load("assets/leila.mp3")
    pygame.mixer.music.set_volume(0.3) # Volume da Música.
    pygame.mixer.music.play(-1) # Loop para continuar a música sempre que acabar.

    loop = True
    while loop:
        window.blit(background, (0, 0))

        if button1.draw(window): # Botão "Sair"
            pygame.mixer.music.stop() # Finaliza a música de tela inicial.
            return "sair"

        if button2.draw(window): # Botão "Jogar"
            pygame.mixer.music.stop() # Finaliza a música de tela inicial.
            return "jogar"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop() # Finaliza a música de tela inicial.
                return "sair"

        pygame.display.update()
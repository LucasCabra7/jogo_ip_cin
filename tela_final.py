import os
import pygame
import time

os.environ['SDL_VIDEO_CENTERED'] = '1' # Manter a tela no centro

def imagem_final():
    pygame.init()
    pygame.mixer.init()

    window = pygame.display.set_mode([1280, 800])
    pygame.display.set_caption("Fim de Jogo")

    background = pygame.image.load("assets/tela_final.png")
    background = pygame.transform.scale(background, (1280, 800))
    pygame.mixer.music.load("assets/a-risada-do-kiko.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play()

    window.blit(background, (0, 0))
    pygame.display.update()

    # Início do temporizador
    start_time = pygame.time.get_ticks()

    # Loop para manter a janela ativa e escutar eventos
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                return  # Encerra a função se clicar no "X"

        # Calcula o tempo decorrido
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000  # em segundos
        if elapsed_time >= 10:
            running = False

        pygame.time.delay(100)  # Alivia o uso de CPU

    pygame.mixer.music.stop()

def imagem_vitoria():
    pygame.init()
    pygame.mixer.init()

    window = pygame.display.set_mode([1280, 800])
    pygame.display.set_caption("Você Venceu!")

    vencedor = pygame.image.load(f"assets/vencedor.jpeg")
    pygame.mixer.music.load("assets/vitoria_efeitosonoro.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play()

    window.blit(vencedor, (0, 0))
    pygame.display.update()

    start_time = pygame.time.get_ticks()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                return

        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
        if elapsed_time >= 10:
            running = False

        pygame.time.delay(100)

    pygame.mixer.music.stop()
import pygame
import tela_inicial
import time

def imagem_final():
    pygame.init()
    pygame.mixer.init()

    window = pygame.display.set_mode([1280, 800])
    pygame.display.set_caption("Fim de Jogo")

    # Carregar imagem de fundo da tela final
    background = pygame.image.load("assets/tela_final.png")  # Imagem de game over

    # Reproduzir a mesma música da tela inicial
    pygame.mixer.music.load("assets/tiringa-me-perdoe-meu-amigo-veio.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play()

    # Mostrar imagem por 2 segundos
    window.blit(background, (0, 0))
    pygame.display.update()

    time.sleep(17)

    pygame.mixer.music.stop()
    # esta chamando apenas a tela inicial e não a funçao main. por isso quando volta para a tela nao consegue apertar em jogar novamente. obs: não sei chamar a funçao main aqui.
    tela_inicial.iniciar_tela()

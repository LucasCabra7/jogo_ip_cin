import os
import pygame
import time

os.environ['SDL_VIDEO_CENTERED'] = '1'

def imagem_final():
    pygame.init()
    pygame.mixer.init()

    window = pygame.display.set_mode([1280, 800])
    pygame.display.set_caption("Fim de Jogo")

    background = pygame.image.load("assets/tela_final.png")
    pygame.mixer.music.load("assets/tiringa-me-perdoe-meu-amigo-veio.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play()

    window.blit(background, (0, 0))
    pygame.display.update()

    time.sleep(17)
    pygame.mixer.music.stop()

    # Agora só volta pro main automaticamente


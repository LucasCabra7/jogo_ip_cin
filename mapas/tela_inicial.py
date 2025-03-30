import pygame
import botao

def play1(): # Entrar como personagem NINE:
    print("Iniciando Jogo 1...")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

def play2(): # Entrar como personagem BOZO:
    print("Iniciando Jogo 2...")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

pygame.init()

# Configuração da janela
window = pygame.display.set_mode([1280, 800])
pygame.display.set_caption("Tela Inicial")

# Carregar imagens
background = pygame.image.load("assets/capa do jogo.jpeg")
button1_img = pygame.image.load("assets/botão nine.png")
button2_img = pygame.image.load("assets/botão bozo.png")

# Criar botões
button1 = botao.Button(100, 540, button1_img, 1)
button2 = botao.Button(1000, 555, button2_img, 1)

loop = True
while loop:
    window.blit(background, (0, 0))  # Desenha o fundo
    
    if button1.draw(window):
        play1()
    if button2.draw(window):
        play2()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    
    pygame.display.update()

pygame.quit()

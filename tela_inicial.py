import pygame
import subprocess
import botao
import player

def play2():  # Função que inicia o jogo quando clicar no botão "Jogar"
    print("Iniciando Jogo 2...")
    pygame.quit()  # Fecha a tela inicial antes de iniciar o jogo
    subprocess.run(["python", "nine_player.py"])  # Executa o jogo separadamente

def iniciar_tela():
    # Configuração da janela
    pygame.init()
    pygame.mixer.init()
    window = pygame.display.set_mode([1280, 800])
    pygame.display.set_caption("Tela Inicial")

    # Carregar imagens
    background = pygame.image.load("assets/CAPA.jpeg")
    button1_img = pygame.image.load("assets/botao_sair.png")
    button2_img = pygame.image.load("assets/botao_jogar.png")

    # Criar botões
    button1 = botao.Button(650, 30, button1_img, 0.4)
    button2 = botao.Button(950, 30, button2_img, 0.4)

    pygame.mixer.music.load("assets/toque leila.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

    loop = True
    while loop:
        window.blit(background, (0, 0))  # Desenha o fundo
        
        if button1.draw(window):
            loop = False
        
        if button2.draw(window):
            play2()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
        
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    iniciar_tela()
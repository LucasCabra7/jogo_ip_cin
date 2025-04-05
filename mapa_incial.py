import pygame

matriz = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,1],
[1,0,1,1,1,0,0,0,1,0,0,0,1,0,1,1,0,0,0,1,0,0,0,0,1],
[1,0,0,0,0,1,0,1,1,1,0,0,1,0,0,0,1,0,1,0,0,0,1,0,1],
[1,1,0,1,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,1,1,1,0,1],
[1,0,0,1,0,1,1,0,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,1],
[1,0,1,0,0,1,1,0,1,1,0,0,0,0,0,1,0,1,0,1,1,0,1,1,1],
[1,0,0,0,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,1],
[1,0,1,1,0,0,1,0,1,0,0,0,1,0,0,0,0,1,1,0,1,1,1,0,1],
[0,0,1,1,0,1,0,0,0,0,1,0,0,1,0,1,1,1,0,0,0,0,1,0,0],
[1,0,1,1,0,1,0,1,1,1,0,1,0,0,0,0,1,0,0,1,0,0,1,0,1],
[1,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,1,1,0,1],
[1,1,1,1,0,1,1,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,1],
[1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1]]

mapa = matriz

# Configurações do Pygame
tamanho_do_bloco = 35
LARGURA = len(mapa[0]) * tamanho_do_bloco
ALTURA = len(mapa) * tamanho_do_bloco

parede = pygame.image.load(r"assets\parede.png", "r") 
parede = pygame.transform.scale(parede, (tamanho_do_bloco, tamanho_do_bloco))

chao  = pygame.image.load(r"assets\chão.png", "r") 
chao  = pygame.transform.scale(chao, (tamanho_do_bloco, tamanho_do_bloco))

pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Nine vs Bozo")

CINZA =  (150, 200, 200),  # Fundo

rodando = True
while rodando:
    tela.fill(CINZA)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    for coluna in range(len(mapa)):
        for linha in range(len(mapa[coluna])):
            if mapa[coluna][linha] == 1:  # Se for parede
                tela.blit(parede,(linha * tamanho_do_bloco, coluna * tamanho_do_bloco))
            else:
                tela.blit(chao,(linha * tamanho_do_bloco, coluna * tamanho_do_bloco) )
    pygame.display.flip()
    
pygame.quit()

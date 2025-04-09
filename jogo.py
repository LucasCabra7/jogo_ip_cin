import pygame
import tela_final
from inimigo import Inimigo #vai importar a classe do inimigo
import colisoes
from mapa_inicial import Map
from player import Player


def iniciar_jogo(): # Função para iniciar o jogo com as importações do Mapa, inimigo (com colisão) e ´coletaveis (ainda falta).´
    print('Função iniciar_jogo() foi chamada!') # Print para verificar que está funcionando.

    pygame.display.set_caption("Jogo Princial") # Nome da tela.
    tela = pygame.display.set_mode((1280, 800)) # Tamanho da tela.

    mapa = Map(32, tela) # Chamando a classe ´Map´ com ´tamanho do mapa e tela´.
    jogador = Player() # Chamando a classe do ´Player´.
    inimigo = Inimigo(800, 300) # Chmando a classe do ´Inimigo´ com ´largura e altura´.

    rodando = True # Booleano.
    relogio = pygame.time.Clock() # Clock do fps.

    while rodando: # Loop para rodar a tela:
        relogio.tick(60) # Clock fixo em 60fps.
        tela.fill((0, 0, 0)) # Fundo da tela ´TALVEZ CORRIGIR´.

        for evento in pygame.event.get(): # Caso aperte em ´X´
            if evento.type == pygame.QUIT:
                rodando = False # Sai da tela.
        
        teclas = pygame.key.get_pressed() # Verificar o pressionamento das teclas ´Direita, Esquerda, Frente e Trás´.
        jogador.mover_player(teclas) # Verifica qual tecla foi pressioanda o ´Player()´.
        inimigo.mover_em_direcao(jogador.x_player, jogador.y_player) # Verifica a qual é lugar que se encontra ´Player()´ para o ´Inimigo()´ segui-lo.

        mapa.desenhar() # Desenhar o mapa na tela.
        jogador.desenhar(tela) # Desenhar o ´Player()´ na tela. (FALTA CORRIGIR)
        inimigo.desenhar(tela) # Desenha o ´Inimigo()´ na tela. (FALTA CORRIGIR)

        if inimigo.checar_colisao(jogador.x_player, jogador.y_player, jogador.largura_player, jogador.altura_player): # Checar a colisão entre o ´Inimigo()´ e o ´Player()´.
            print('O jogador foi pego! Fim de jogo!') # Imprime caso aconteça.
            rodando = False # Finaliza o jogo.
            tela_final.imagem_final()
        
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    iniciar_jogo()
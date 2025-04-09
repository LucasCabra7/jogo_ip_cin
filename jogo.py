import pygame
import tela_final
from inimigo import Inimigo
from calango import Calango
from mapa_inicial import Map
from player import Player
import random
pygame.mixer.init()

def iniciar_jogo():
    print('Função iniciar_jogo() foi chamada!')

    pygame.display.set_caption("Jogo Principal")
    tela = pygame.display.set_mode((1280, 800))

    mapa = Map(34, tela)
    jogador = Player()
    inimigo = Inimigo(800, 300)
    calango = Calango(170, 204)
    calango.carregar_sprites()
    rodando = True
    relogio = pygame.time.Clock()

    pontuacao = 0
    calango_ativo = True
    tempo_desaparecimento = 0

    while rodando:
        relogio.tick(60)
        tela.fill((0, 0, 0))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        teclas = pygame.key.get_pressed()
        jogador.mover_player(teclas)

        if calango_ativo:
            calango.fugir(jogador.x_player, jogador.y_player)

        inimigo.mover_em_direcao(jogador.x_player, jogador.y_player)
        mapa.desenhar()
        jogador.desenhar(tela)

        if calango_ativo:
            calango.desenhar(tela)

        if inimigo.checar_colisao(jogador.x_player, jogador.y_player, jogador.largura_player, jogador.altura_player):
            print('O jogador foi pego! Fim de jogo!')
            pygame.mixer.music.load("assets/alerta-policia.mp3")
            pygame.mixer.music.set_volume(0.3)
            pygame.mixer.music.play()
            pygame.time.delay(3000)
            rodando = False
            tela_final.imagem_final()

        inimigo.desenhar(tela)

        # Checar colisão com o calango
        if calango_ativo and calango.checar_colisao(jogador.x_player, jogador.y_player, jogador.largura_player, jogador.altura_player):
            print('Pegou o calanguinho!')
            pygame.mixer.music.load("assets/uepa-ratinho.mp3")
            pygame.mixer.music.set_volume(0.3)
            pygame.mixer.music.play()
            pontuacao += 1
            print(f"Pontuação: {pontuacao}")
            calango_ativo = False
            tempo_desaparecimento = pygame.time.get_ticks()

            if pontuacao >= 5:
                print("Você venceu! Pegou todos os calangos!")
                pygame.time.delay(3000)
                rodando = False
                tela_final.imagem_final()

        # Verifica se o calango deve reaparecer
        if not calango_ativo and pygame.time.get_ticks() - tempo_desaparecimento > 2000:
            calango.x, calango.y = random.choice([(34, 34), (102, 68), (170, 204), (340, 136), (476, 442)]) #escolhe uma posição aleatória para o calango aparecer
            calango_ativo = True

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    iniciar_jogo()
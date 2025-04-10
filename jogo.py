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
    inimigo = Inimigo(800, 300) #Posição inicial do inimigo
    calango = Calango(170, 204) #Posição inicial do calango
    calango.carregar_sprites()
    rodando = True
    relogio = pygame.time.Clock()

    calangos_coletados = 0
    calango_ativo = True
    tempo_desaparecimento = 0
    boost = False
    tempo_boost = 0
    fonte = pygame.font.Font(None, 36)
    cor = (0, 0, 0)  
    pygame.mixer.music.load("assets/negroyazul.mp3") #musica de fundo
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)  # -1 para tocar em loop
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
        inimigo.desenhar(tela)

        if calango_ativo:
            calango.desenhar(tela)

        if inimigo.checar_colisao(jogador.x_player, jogador.y_player, jogador.largura_player, jogador.altura_player):
            print('O jogador foi pego! Fim de jogo!')
            pygame.mixer_music.stop()
            policia_pegou = pygame.mixer.Sound("assets/alerta-policia.mp3")
            policia_pegou.set_volume(0.3)
            policia_pegou.play()
            pygame.time.delay(3000)
            rodando = False
            tela_final.imagem_final()

        # Checar colisão com o calango
        if calango_ativo and calango.checar_colisao(jogador.x_player, jogador.y_player, jogador.largura_player, jogador.altura_player):
            print('Pegou um calanguinho!')
            pegou_calanguinho = pygame.mixer.Sound("assets/calanguinho.mp3")
            pegou_calanguinho.set_volume(0.4)
            pegou_calanguinho.play()
            calangos_coletados += 1
            calango_ativo = False
            tempo_desaparecimento = pygame.time.get_ticks()      
            jogador.velocidade += 0.5 # Ativa boost de velocidade por 2 segundos
            boost = True
            tempo_boost = pygame.time.get_ticks()

        # Verifica se o calango deve reaparecer
        if not calango_ativo and pygame.time.get_ticks() - tempo_desaparecimento > 2000:
            calango.x, calango.y = random.choice([(34, 34), (102, 68), (170, 204), (340, 136), (476, 442)]) #escolhe uma posição aleatória para o calango aparecer
            calango_ativo = True
            calango_sound = pygame.mixer.Sound("assets/calango correndo.mp3")
            calango_sound.set_volume(0.3)
            calango_sound.play()

        texto = fonte.render(f"Calangos coletados: {calangos_coletados}", True, cor) # Texto que vai aparecer da pontuação
        tela.blit(texto, (20, 20))  # Desenha o texto na posição (20, 20)
        
        if boost and pygame.time.get_ticks() - tempo_boost > 2000:
            jogador.velocidade = 1
            boost = False
            print('Boost acabou. Velocidade normal.')
        
        if calangos_coletados >= 5:
            print("Você venceu! Pegou todos os calangos!")
            pygame.time.delay(3000)
            rodando = False
            tela_final.imagem_vitoria()

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    iniciar_jogo()
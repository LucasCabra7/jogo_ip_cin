import pygame
import tela_final
from inimigo import Inimigo
from calango import Calango
from mapa_inicial import Map
from player import Player
from dinheiro import Dinheiro
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
    
    dinheiro = Dinheiro(145, 150)
    dinheiro.carregar_sprites()
    
    
    rodando = True
    relogio = pygame.time.Clock()
    
    
    dinheiro_coletado = 0
    dinheiro_ativo = True
    
    calangos_coletados = 0
    calango_ativo = True
    tempo_desaparecimento_calango = 0
    tempo_desaparecimento_dinheiro = 0
    
    boost = False
    
    prisao_policial = False 
    
    tempo_boost = 0
    
    tempo_prisao = 0
    
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
        
        #deubg
        if(dinheiro_ativo): #todos dinheiros ainda presentes
            dinheiro.desenhar(tela)
            
        #debug colisao dinheiro
        if dinheiro_ativo and dinheiro.checar_colisao(jogador.x_player, jogador.y_player, jogador.largura_player, jogador.altura_player):
            print('Pegou o dinheiro!')
            pegou_dinheiro = pygame.mixer.Sound("assets/dinheiro_pego.mp3")
            pegou_dinheiro.set_volume(0.3)
            pegou_dinheiro.play()
            dinheiro_coletado += 1
            dinheiro_ativo = False
            tempo_desaparecimento_dinheiro = pygame.time.get_ticks() 
            inimigo.velocidade -= 0.9 #prende inimigo por x segundos     
            prisao_policial = True
            
            tempo_prisao = pygame.time.get_ticks()    
        
        #debug
        if not dinheiro_ativo and pygame.time.get_ticks() - tempo_desaparecimento_dinheiro > 1000 and dinheiro_coletado !=5:
            dinheiro.x, dinheiro.y = random.choice([(64, 64), (65, 66), (67, 78), (70, 71), (150, 200)]) #escolhe uma posição aleatória para o dinheiro aparecer
            dinheiro_ativo = True
        
        

        if calango_ativo:
            calango.desenhar(tela)
      

        if inimigo.checar_colisao(jogador.x_player, jogador.y_player, jogador.largura_player, jogador.altura_player):
            print('O jogador foi pego! Fim de jogo!')
            policia_pegou = pygame.mixer.Sound("assets/alerta-policia.mp3")
            policia_pegou.set_volume(0.3)
            policia_pegou.play()
            pygame.time.delay(3000)
            rodando = False
            tela_final.imagem_final()

        # Checar colisão com o calango
        if calango_ativo and calango.checar_colisao(jogador.x_player, jogador.y_player, jogador.largura_player, jogador.altura_player):
            print('Pegou o calanguinho!')
            pegou_calanguinho = pygame.mixer.Sound("assets/calanguinho.mp3")
            pegou_calanguinho.set_volume(0.4)
            pegou_calanguinho.play()
            calangos_coletados += 1
            calango_ativo = False
            tempo_desaparecimento_calango = pygame.time.get_ticks()      
            jogador.velocidade += 0.5 # Ativa boost de velocidade por 2 segundos
            boost = True
            tempo_boost = pygame.time.get_ticks()
            
            
            

        # Verifica se o calango deve reaparecer
        if not calango_ativo and pygame.time.get_ticks() - tempo_desaparecimento_calango > 2000:
            calango.x, calango.y = random.choice([(34, 34), (102, 68), (170, 204), (340, 136), (476, 442)]) #escolhe uma posição aleatória para o calango aparecer
            calango_ativo = True
            calango_sound = pygame.mixer.Sound("assets/calango correndo.mp3")
            calango_sound.set_volume(0.3)
            calango_sound.play()

        texto = fonte.render(f"Calangos coletados: {calangos_coletados}", True, cor) # Texto que vai aparecer da pontuação
        tela.blit(texto, (20, 20))  # Desenha o texto na posição (20, 20)
        
        if boost and pygame.time.get_ticks() - tempo_boost > 2000: #quando acaba o tempo do boost
            jogador.velocidade = 1
            boost = False
            print('Boost acabou. Velocidade normal.')
            
        if prisao_policial and pygame.time.get_ticks() - tempo_prisao > 2000: #quando acaba o tempo do boost
            inimigo.velocidade = 1
            prisao_policial = False
            print('Policial solto')
        
       

        if calangos_coletados >= 5:
            print("Você venceu! Pegou todos os calangos!")
            pygame.time.delay(3000)
            rodando = False
            tela_final.imagem_vitoria()
            
        

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    iniciar_jogo()
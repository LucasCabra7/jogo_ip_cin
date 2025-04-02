import pygame

tela = pygame.display.set_mode((1920, 1080))  # Cria a tela do jogo
pygame.display.set_caption("teste calango")

def movimentar():    
    pygame.init()
    from nine_player import player_game
    # Carrega os sprites do calango
    sprite_parado = pygame.image.load("assets/boneco_parado.png")
    sprite_esquerda = [pygame.image.load(f"assets/calango/calango_esquerda/quadro-{i}.png") for i in range(1, 5)]
    sprite_direita = [pygame.image.load(f"assets/calango/calango_direita/quadro-{i}.png") for i in range(1, 5)]
    sprite_cima = [pygame.image.load(f"assets/calango/calango_cima/quadro-{i}.png") for i in range(1, 5)]
    sprite_baixo = [pygame.image.load(f"assets/calango/calango_baixo/quadro-{i}.png") for i in range(1, 5)]
 
    x_calango, y_calango = 960, 540 # Posição inicial do calango
    velocidade = 10
    indice_sprite = 0  # Controla a troca dos sprites
    direcao = "parado"  # Estado inicial
    posicao_anterior = [x_calango, y_calango]
    movimentos = ((0, -velocidade), (0, velocidade), (velocidade, 0), (-velocidade, 0)) #baixo, cima, direito, esquerdo

    rect_player  = calango.get_rect(topleft=(player_game.x_player, player_game.y_player))
    rect_calango = calango.get_rect(topleft=(posicao_anterior[0], posicao_anterior[1]))

    while not rect_player.colliderect(rect_calango):
        
        for m in movimentos:
            if posicao_anterior[0] + m[0] != 1900  or posicao_anterior[1] + m[1] != 1000:
                posicao_anterior[0] += m[0]
                posicao_anterior[1] += m[1]
                if posicao_anterior[0] > x_calango:
                    direcao = "direita"
                elif posicao_anterior[0] < x_calango:
                    direcao = "esquerda"
                elif posicao_anterior[1] > y_calango:
                    direcao = "cima"
                elif posicao_anterior[0] > y_calango:
                    direcao = "baixo"
                x_calango, y_calango = posicao_anterior[0], posicao_anterior[1]
                break

        if direcao in ["esquerda", "direita", "cima", "baixo"]:
            indice_sprite = (indice_sprite + 1) % 4
        else:
            indice_sprite = 0

        # Escolhe qual sprite exibir
        if direcao == "esquerda":
            calango = sprite_esquerda[indice_sprite]
        elif direcao == "direita":
            calango = sprite_direita[indice_sprite]
        elif direcao == "cima":
            calango = sprite_cima[indice_sprite]
        elif direcao == "baixo":
            calango = sprite_baixo[indice_sprite]
        else:
            calango = sprite_parado

        #calango pegou a calango
        rect_player  = calango.get_rect(topleft=(player_game.x_player, player_game.y_player))
        rect_calango = calango.get_rect(topleft=(posicao_anterior[0], posicao_anterior[1]))
        
        if rect_calango.colliderect(rect_player):
            pygame.quit() # Encerra o Pygame

        tela.fill((255, 255, 255))  # fundo da tela
        tela.blit(calango, (x_calango, y_calango)) # Desenha o calango atualizado
        pygame.draw.rect(tela, (255, 0, 0), rect_calango, 2)  # Retângulo do calango (vermelho)
        pygame.display.update() # Atualiza a tela
     

if __name__ == "__main__":
    movimentar()
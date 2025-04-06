import mapa_inicial

class Colisao:
    def verificar_colisao_parede(self, eixo_x, eixo_y, velocidade, direcao):
        # Tamanho do personagem (ajuste conforme sua imagem)
        personagem_largura = 30
        personagem_altura = 30
        
        # Calcula os pontos de colisão (4 cantos do personagem)
        if direcao == 'esquerda':
            if (eixo_x - velocidade)//personagem_altura == 0:
                eixo_x = mapa_inicial.Map.LARGURA - mapa_inicial.Map.tamanho_bloco

            personagem_largura = 18
            personagem_altura = 18
            
            # Verifica o lado esquerdo do personagem
            novo_x = eixo_x - velocidade
            bloco_x_esquerda = int(novo_x / mapa_inicial.Map.tamanho_bloco)
            bloco_y_cima = int(eixo_y / mapa_inicial.Map.tamanho_bloco)
            bloco_y_baixo = int((eixo_y + personagem_altura - 1) / mapa_inicial.Map.tamanho_bloco)
            
            # Verifica os dois pontos (canto superior e inferior esquerdo)
            if (mapa_inicial.Map.mapa[bloco_y_cima][bloco_x_esquerda] == 0 and 
                mapa_inicial.Map.mapa[bloco_y_baixo][bloco_x_esquerda] == 0):
                eixo_x = novo_x
                
        if direcao == 'direita':
            # Verifica o lado direito do personagem
            if (eixo_x + velocidade)//personagem_largura == len(mapa_inicial.Map.mapa[1]) + 2:
                eixo_x = 0

            personagem_largura = 18
            personagem_altura = 18

            novo_x = eixo_x + velocidade
            bloco_x_direita = int((novo_x + personagem_largura - 1) / mapa_inicial.Map.tamanho_bloco)
            bloco_y_cima = int(eixo_y / mapa_inicial.mapa.tamanho_bloco)
            bloco_y_baixo = int((eixo_y + personagem_altura - 1) / mapa_inicial.Map.tamanho_bloco)
            
            if (mapa_inicial.Map.mapa[bloco_y_cima][bloco_x_direita] == 0 and 
                mapa_inicial.Map.mapa[bloco_y_baixo][bloco_x_direita] == 0):
                eixo_x = novo_x
                
        if direcao == 'cima':
            
            # Verifica a base do personagem
            if (eixo_y - velocidade)//personagem_altura == 0:
                eixo_y = mapa_inicial.Map.ALTURA - mapa_inicial.Map.tamanho_bloco

            personagem_largura = 18
            personagem_altura = 18

            novo_y = eixo_y - velocidade
            bloco_y_cima = int(novo_y / mapa_inicial.Map.tamanho_bloco)
            bloco_x_esquerda = int(eixo_x / mapa_inicial.Map.tamanho_bloco)
            bloco_x_direita = int((eixo_x + personagem_largura - 1) / mapa_inicial.Map.tamanho_bloco)
            
            if (mapa_inicial.Map.mapa[bloco_y_cima][bloco_x_esquerda] == 0 and 
                mapa_inicial.Map.mapa[bloco_y_cima][bloco_x_direita] == 0):
                eixo_y = novo_y
                
        if direcao == 'baixo':
            # Verifica a base do personagem
            if (eixo_y + velocidade)//personagem_altura > len(mapa_inicial.Map.mapa):
                eixo_y = 0
            
            personagem_largura = 18
            personagem_altura = 18

            novo_y = eixo_y + velocidade
            bloco_y_baixo = int((novo_y + personagem_altura - 1) / mapa_inicial.Map.tamanho_bloco)
            bloco_x_esquerda = int(eixo_x / mapa_inicial.Map.tamanho_bloco)
            bloco_x_direita = int((eixo_x + personagem_largura - 1) / mapa_inicial.Map.tamanho_bloco)

            if (mapa_inicial.Map.mapa[bloco_y_baixo][bloco_x_esquerda] == 0 and 
                mapa_inicial.Map.mapa[bloco_y_baixo][bloco_x_direita] == 0):
                eixo_y = novo_y
            
        return eixo_x, eixo_y
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


class Colisao:
    def verificar_colisao_parede(eixo_x, eixo_y, velocidade, direcao):
        # Tamanho do personagem (ajuste conforme sua imagem)
        bateu = True
        personagem_largura = 18
        personagem_altura = 18
        
        # Calcula os pontos de colisão (4 cantos do personagem)
        if direcao == 'esquerda':
            if (eixo_x - velocidade)//personagem_altura < -2:
                eixo_x = (34*len(matriz[0])) - 34

            # Verifica o lado esquerdo do personagem
            novo_x = eixo_x - velocidade
            bloco_x_esquerda = int(novo_x / 34)
            bloco_y_cima = int(eixo_y / 34)
            bloco_y_baixo = int((eixo_y + personagem_altura - 1) /34)
            
            # Verifica os dois pontos (canto superior e inferior esquerdo)
            if (matriz[bloco_y_cima][bloco_x_esquerda] == 0 and 
                matriz[bloco_y_baixo][bloco_x_esquerda] == 0):
                eixo_x = novo_x
                bateu = False
                
        if direcao == 'direita':
            # Verifica o lado direito do personagem
            if (eixo_x + velocidade)//personagem_largura > len(matriz[1]) + 20:
                eixo_x = 0

            novo_x = eixo_x + velocidade
            bloco_x_direita = int((novo_x + personagem_largura - 1) /34)
            bloco_y_cima = int(eixo_y /34)
            bloco_y_baixo = int((eixo_y + personagem_altura - 1) /34)
            
            if (matriz[bloco_y_cima][bloco_x_direita] == 0 and 
                matriz[bloco_y_baixo][bloco_x_direita] == 0):
                eixo_x = novo_x
                bateu = False 
                
        if direcao == 'cima':
            
            # Verifica a base do personagem
            if (eixo_y - velocidade)//personagem_altura < -2:
                eixo_y = (len(matriz)*34) - 34

            novo_y = eixo_y - velocidade
            bloco_y_cima = int(novo_y /34)
            bloco_x_esquerda = int(eixo_x /34)
            bloco_x_direita = int((eixo_x + personagem_largura - 1) /34)
            
            if (matriz[bloco_y_cima][bloco_x_esquerda] == 0 and 
                matriz[bloco_y_cima][bloco_x_direita] == 0):
                eixo_y = novo_y
                bateu = False
                
        if direcao == 'baixo':
            # Verifica a base do personagem
            if (eixo_y + velocidade)//personagem_altura > len(matriz) + 11:
                eixo_y = 0

            novo_y = eixo_y + velocidade
            bloco_y_baixo = int((novo_y + personagem_altura - 1) /34)
            bloco_x_esquerda = int(eixo_x /34)
            bloco_x_direita = int((eixo_x + personagem_largura - 1) /34)

            if (matriz[bloco_y_baixo][bloco_x_esquerda] == 0 and 
                matriz[bloco_y_baixo][bloco_x_direita] == 0):
                eixo_y = novo_y
                bateu = False
            
        return eixo_x, eixo_y, bateu 
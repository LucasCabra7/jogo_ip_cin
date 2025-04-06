import pygame
import tela_inicial
from player import iniciar_jogo

pygame.init()

acao = tela_inicial.iniciar_tela() # Chamando a função de tela inicial.

# Condicinal para verifica a ação do botão.
if acao == "jogar": # Se o botão pressionado for ´JOGAR´:
    iniciar_jogo()  # Chama a função ´iniciar_jogo()´ em ´player.py´.
elif acao == "sair": # Se o botão pressionado for ´SAIR´:
    pygame.quit() # Aqui sai do jogo.
    exit() # Fecha a tela geral.
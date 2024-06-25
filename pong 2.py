# mar.almeida@discente.ufma.br
# Marcos André Rodrigues Almeida
# 25.06.24 (9:00 am)
# 2024.1

# importando as bibliotecas
import pygame
from pygame.locals import *
from sys import exit

#iniciando o pygame
pygame.init()
 
 #tela (janela)
largura = 640
altura = 480
janela = pygame.display.set_mode((largura, altura))

#nome do jogo no canto superior direito da tela
pygame.display.set_caption('Pong 2: O Atirador')

#Configs do jogo
import pygame
from pygame.locals import *
from sys import exit


pygame.init()

#tamanho da tela
largura = 1080
altura = 720
janela = pygame.display.set_mode((largura, altura))
 

#tiros
altura_bala = 2
largura_bala = 2
velo_bala = 7


#DIMENSOES DAS NAVES
nave1_x = 100
nave1_y = altura /2

nave2_x = largura - 140 #40 da nave e 100 do espaçamento
nave2_y = altura /2

alt_nav = 15
lar_nav = 15
vel_nav = 20

alt_nav2 = 15
lar_nav2 = 15
vel_nav2 = 20

#DIMENSOES DOS TIROS
tiros_nave1 = []
tiros_nave2 = []

alt_tiro = 15
lar_tiro = 15
vel_tiro = 15

#nome do jogo no canto superior esquerdo da tela
pygame.display.set_caption('Nav Battle!')

#cores(RGB)
branco = (255, 255, 255)
preto = (0, 0, 0)
azul = (65, 6, 190)
vermelho = (255, 100, 30)







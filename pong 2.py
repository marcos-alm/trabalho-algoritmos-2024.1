import pygame
from pygame.locals import *
from sys import exit

pygame.init()
 
 #tela (janela)
largura = 640
altura = 480

janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Pong 2: O Atirador')

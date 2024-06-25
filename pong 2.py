# mar.almeida@discente.ufma.br
# Marcos André Rodrigues Almeida
# 25.06.24 (9:00 am)
# 2024.1

# importando as bibliotecas
import pygame
from pygame. locals import *
from config_do_game.config import*
from sys import exit

#iniciando o pygame
pygame.init()

#loop principal
while not fim:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim = True

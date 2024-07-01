# mar.almeida@discente.ufma.br
# Marcos André Rodrigues Almeida
# 25.06.24 (9:00 am)
# 2024.1  

#importando as bibliotecas
import pygame
from pygame. locals import *
from config import*
from sys import exit 


#iniciando o pygame
pygame.init()
fim = False


pontuacao_nave1 = 0
pontuacao_nave2 = 0

tiros_nave1 = []
tiros_nave2 = []

pygame.mixer.music.set_volume(0.10)
music_back= pygame.mixer.music.load('trabalho_game/mega.mp3')
pygame.mixer.music.play(-1)


music_coli= pygame.mixer.Sound('trabalho_game/beep1.wav')
music_coli.set_volume(1)



laser = pygame.mixer.Sound('trabalho_game/1.wav')
# def reinicia():
#     jogando = False
#     pontuacao_nave1 =0
#     pontuacao_nave2 =0


verifica = False

def desenhar_pontuacao(janela, pontuacao_nave1, pontuacao_nave2):
    font = pygame.font.SysFont(None, 36)
    texto_nave1 = font.render(f'NAVE 1: {pontuacao_nave1}', True, branco)
    texto_nave2 = font.render(f'NAVE 2: {pontuacao_nave2}', True, branco)
    janela.blit(texto_nave1, (10, 10))
    janela.blit(texto_nave2, (largura - texto_nave2.get_width() - 10, 10))


pontuacao_nave1 = 0
pontuacao_nave2 = 0

font2 = pygame.font.SysFont('arial',14, True, False)
font_over = pygame.font.SysFont('arial',30, True, False)
font_tecla = pygame.font.SysFont('arial',14, True, False)

relogio = pygame.time.Clock()
restart = False
cena = 'jogar'            

#loop principal do jogo
while not fim:
    if cena == 'jogar':
        janela.fill((0, 0, 0))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim = True
                exit()
                #evento que "mapea" a tecla do tiro
            if evento.type == pygame.KEYDOWN:
                if evento.key == K_SPACE: 
                    tiros_nave1.append(pygame.Rect(nave1_x + lar_nav, nave1_y + alt_nav // 2 - lar_tiro // 2, lar_tiro, alt_tiro))
                    laser.play()
                if evento.key == K_KP_ENTER: 
                    tiros_nave2.append(pygame.Rect(nave2_x - lar_tiro, nave2_y + alt_nav // 2 - lar_tiro // 2, lar_tiro, alt_tiro))
                    laser.play()

        mensagem = (f'Atire na cabine da Nave adversária!')
        texto_form = font2.render(mensagem, True, (200,200,200))    
        
        back = pygame.image.load('trabalho_game\px1.jpg')
        img = pygame.transform.scale(back,(largura, altura))
        janela.blit(img, (0,0))


        #nave1
    
        nave1 = pygame.draw.rect(janela, branco, (nave1_x, nave1_y, alt_nav, lar_nav))

        if pygame.key.get_pressed()[K_a] and nave1_x - 15 > 0:
            nave1_x = nave1_x - vel_nav
        if pygame.key.get_pressed()[K_d] and nave1_x + vel_nav < 560 - vel_nav: 
            nave1_x =  nave1_x + vel_nav
        if pygame.key.get_pressed()[K_w] and nave1_y - vel_nav + 20 > 0:
            nave1_y = nave1_y - vel_nav
        if pygame.key.get_pressed()[K_s] and nave1_y + vel_nav < 720 - 20:
            nave1_y = nave1_y + vel_nav

        #nave2       
        nave2 = pygame.draw.rect(janela, (100,100,100), (nave2_x,nave2_y, alt_nav2, lar_nav2))
        
        if pygame.key.get_pressed()[K_LEFT] and nave2_x - 15 > 0 and nave2_x > largura * 0.5 + 40 :    
            nave2_x = nave2_x - vel_nav2
        if pygame.key.get_pressed()[K_RIGHT]and nave2_x + 15 < 1080 - 40 :
            nave2_x =  nave2_x + vel_nav2
        if pygame.key.get_pressed()[K_UP] and nave2_y - 15 > 0 :
            nave2_y = nave2_y - vel_nav2
        if pygame.key.get_pressed()[K_DOWN] and nave2_y + 15 < 720 - 40:
            nave2_y = nave2_y + vel_nav2   

        tiro_red = pygame.image.load('trabalho_game/tirored.png')
        #carregando a imagem da nave vermelha
        nav_img = pygame.image.load('trabalho_game/navred.png')
        pygame.transform.scale(nav_img, (lar_nav*3, alt_nav*3))

        #carregando a imagem da nave azul
        nav2_img = pygame.image.load('trabalho_game/nav_blue.png')
        pygame.transform.scale(nav2_img, (lar_nav2*3, alt_nav2*3))

        #carregando a imagem do tiro 1
        tiro_red = pygame.image.load('trabalho_game/tirored.png')

        #carregando a imagem do tiro 2
        tiro_blue = pygame.image.load('trabalho_game/tiro_blue.png')


        
        #tiros nav 1
        tiro_1= tiros_nave1
        for tiro in tiros_nave1:
            tiro.x += vel_tiro              #posição do tiro
            if tiro.colliderect(nave2):
                tiros_nave1.remove(tiro)
                pontuacao_nave1 += 1
                music_coli.play()
            elif tiro.x < 0:
                tiros_nave1.remove(tiro)

        for tiro in tiros_nave1:
            janela.blit(tiro_red, tiro)
            


        #tiros nav 2
        
        for tiro in tiros_nave2:
            tiro.x -= vel_tiro 
            if tiro.colliderect(nave1):
                tiros_nave2.remove(tiro)
                pontuacao_nave2 += 1
                music_coli.play()
            elif tiro.x < 0:
                tiros_nave2.remove(tiro)
        for tiro in tiros_nave2:
            janela.blit(tiro_blue, tiro)



        for tiro1 in tiros_nave1[:]:
            for tiro2 in tiros_nave2[:]:
                if tiro1.colliderect(tiro2):
                    tiros_nave1.remove(tiro1)
                    tiros_nave2.remove(tiro2)
                    break
            

        #janelas de vitoria
        restart = False    
        if pontuacao_nave1 >= 25:
            
            mensagem1 = (f'A NAVE 1 venceu!')
            texto_form1 = font_over.render(mensagem1, True, (200,200,200))
            janela.blit(texto_form1, (415, 330))
            
            pressione = (f'tecla c para continuar')
            texto_form1_1= font_tecla.render(pressione, True, vermelho )
            janela.blit(texto_form1_1, (470, 370))
            restart= True


            
        if pontuacao_nave2 >=25:
            
            mensagem2 = (f'A NAVE 2 venceu!')
            texto_form2 = font_over.render(mensagem2, True, (200,200,200))
            janela.blit(texto_form2, (415, 330))


            pressione2 = (f'tecla c para continuar')
            texto_form2_2 = font_tecla.render(pressione2, True, azul )

            janela.blit(texto_form2_2, (470, 370))
            restart= True



        #evento para reiniciar tudo
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == K_c  and restart== True:
                    pontuacao_nave1 = 0
                    pontuacao_nave2 = 0
                    
                    nave1_x = 100
                    nave1_y = altura /2
                    nave2_x = largura - 140
                    nave2_y = altura /2
          


        
        janela.blit(nav_img,(nave1_x -34, nave1_y-34))
        janela.blit(nav2_img,(nave2_x -34, nave2_y -34))
        janela.blit(texto_form,(430,12))



        desenhar_pontuacao(janela, pontuacao_nave1, pontuacao_nave2)

        relogio.tick(60)
        pygame.display.flip() 
        

        
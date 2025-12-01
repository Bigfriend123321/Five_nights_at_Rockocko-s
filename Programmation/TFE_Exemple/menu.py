import pygame
import time
from config import WIDTH,HEIGHT
from main import chargement,mini_jeu
from options import options
from aide_mini_jeu import aide_mini_jeu

pygame.init()

ecran = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arda.py")

continuer = True
mode_de_jeu = ['menu1', 'menu2', 'menu3', 'menu4']
background_list = ["TFE_Exemple/images/menu1.png", "TFE_Exemple/images/menu2.png", "TFE_Exemple/images/menu3.png", "TFE_Exemple/images/menu4.png"]
i = 0
j = 0

while continuer:
    rect_bouton_minijeu = pygame.draw.rect(ecran, (255, 0, 0), (20, 215, 310, 70), 3)
    rect_bouton_a_venir1 = pygame.draw.rect(ecran, (255, 0, 0), (20, 300, 310, 70), 3)
    rect_bouton_a_venir2 = pygame.draw.rect(ecran, (255, 0, 0), (20, 390, 310, 70), 3)
    rect_bouton_option = pygame.draw.rect(ecran, (255, 0, 0), (710, 535, 180, 50), 3)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        elif rect_bouton_minijeu.collidepoint(pygame.mouse.get_pos()):
            i = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                mode_de_jeu = 'mini_jeu'
        elif rect_bouton_a_venir1.collidepoint(pygame.mouse.get_pos()):
            i = 1
        elif rect_bouton_a_venir2.collidepoint(pygame.mouse.get_pos()):
            i = 2
        elif rect_bouton_option.collidepoint(pygame.mouse.get_pos()):
            i = 3
            if event.type == pygame.MOUSEBUTTONDOWN:
                mode_de_jeu = 'options'
    background = pygame.image.load(background_list[i])
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    ecran.fill((0,0,0))
    ecran.blit(background, (0,0))
    pygame.display.flip()
    
    if mode_de_jeu == 'mini_jeu':
        chargement()
        aide_mini_jeu()
        mini_jeu()
        mode_de_jeu = ['menu1', 'menu2', 'menu3', 'menu4']
    elif mode_de_jeu == 'options' :
        options()
        mode_de_jeu = ['menu1', 'menu2', 'menu3', 'menu4']
pygame.quit
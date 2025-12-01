import pygame
from config import WIDTH, HEIGHT,ecran

def aide_mini_jeu() :
    pygame.init()

    ecran = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Arda.py")

    continuer = True
    options_list = ["TFE_Exemple/images/mini_jeu_touche.png"]
    i = 0
    while continuer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_RETURN and i == 0 :
                    continuer = False
                    
        background = pygame.image.load(options_list[i])
        background = pygame.transform.scale(background, (WIDTH, HEIGHT))

        ecran.fill((0,0,0))
        ecran.blit(background, (0,0))

        pygame.display.flip()
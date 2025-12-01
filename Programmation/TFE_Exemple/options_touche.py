import pygame
from config import WIDTH, HEIGHT,ecran

def options_touches() :
    pygame.init()

    ecran = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Arda.py")

    continuer = True
    options_list = ["TFE_Exemple/images/option_touche.png"]
    i = 0
    while continuer:
        rect_bouton_retour = pygame.draw.rect(ecran, (255, 0, 0), (10, 15, 90, 40), 3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
            elif rect_bouton_retour.collidepoint(pygame.mouse.get_pos()):
                i = 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    continuer = False
                    
        background = pygame.image.load(options_list[i])
        background = pygame.transform.scale(background, (WIDTH, HEIGHT))

        ecran.fill((0,0,0))
        ecran.blit(background, (0,0))
        pygame.display.flip()
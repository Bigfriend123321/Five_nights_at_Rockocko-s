import pygame
from config import WIDTH, HEIGHT,ecran
from options_touche import options_touches

def options() :
    pygame.init()

    ecran = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Arda.py")

    continuer = True
    background_list = ["TFE_Exemple/images/option1.png", "TFE_Exemple/images/option2.png", "TFE_Exemple/images/option3.png"]
    i = 0
    j = 0
    while continuer:
        rect_bouton_retour = pygame.draw.rect(ecran, (255, 0, 0), (0, 45, 150, 40), 3)
        rect_bouton_touche = pygame.draw.rect(ecran, (255, 0, 0), (270, 160, 250, 60), 3)
        rect_bouton_param_video = pygame.draw.rect(ecran, (255, 0, 0), (250, 290, 310, 70), 3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
            elif rect_bouton_retour.collidepoint(pygame.mouse.get_pos()):
                i = 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    continuer = False
            elif rect_bouton_touche.collidepoint(pygame.mouse.get_pos()):
                i = 1
                if event.type == pygame.MOUSEBUTTONDOWN:
                    options_touches()
            elif rect_bouton_param_video.collidepoint(pygame.mouse.get_pos()):
                i = 2

        background = pygame.image.load(background_list[i])
        background = pygame.transform.scale(background, (WIDTH, HEIGHT))

        ecran.fill((0,0,0))
        ecran.blit(background, (0,0))
        pygame.display.flip()
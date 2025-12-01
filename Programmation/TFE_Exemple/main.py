import pygame
from time import time
from personnage import Personnage
from config import WIDTH,HEIGHT,ecran,background_list,frame_list,minigame_winbg_list
from monstre import Monstre
from projectile import Projectile


def chargement(duration=5.0, frame_interval=0.5):
    if not pygame.get_init():
        pygame.init()

    frames = []
    for p in frame_list:
        frames.append(pygame.transform.scale(pygame.image.load(p), (WIDTH, HEIGHT)))

    clock = pygame.time.Clock()
    start = time()
    idx = 0
    last_switch = start

    while True:
        now = time()
        elapsed = now - start
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        if now - last_switch >= frame_interval:
            idx = (idx + 1) % len(frames)
            last_switch = now

        ecran.fill((0, 0, 0))
        ecran.blit(frames[idx], (0, 0))
        pygame.display.flip()

        if elapsed >= duration:
            break

        clock.tick(60)


def mini_jeu() :
    #initialisation de pygame
    pygame.init()
    pygame.display.set_caption("Arda.py")

    #variables true/false du mini jeu
    continuer = True

    #les differents elements mobiles du mini jeu
    joueur = Personnage(10,10,150,150)
    monstres = [Monstre(500, 200, True)]
    projectiles = []
    crying_child = 0

    #gestion du rechargement des coeurs
    recharger = 0
    munition = 0

    #gestion du temps dans le mini jeu
    temps = time()
    bg_time = 0
    TIMER = time()

    #hitbox du timer
    timer_rect = pygame.Rect(WIDTH - 150, 20, 130, 50)
    font = pygame.font.SysFont("Arial", 30)


    while continuer:
        #dessiner le timer
        texte = font.render(str(time()-TIMER), True, (255,255,255))
        texte_rect = texte.get_rect(center=timer_rect.center)
        ecran.blit(texte, texte_rect)

        if time() - TIMER > 5 :
            continuer = False
        else :
            #le background
            if bg_time > 1:
                if recharger < len(background_list) - 1:
                    recharger += 1
                else:
                    recharger = 6
                bg_time = 0
                temps = time()

            #hitbox de la table avec les coeurs
            hitbox_tableheart_surface = pygame.Surface((170, 200), pygame.SRCALPHA)
            hitbox_tableheart = pygame.draw.rect(hitbox_tableheart_surface, (0, 0, 0, 0), (40, 23, 130, 177),1)

            #l'image du background
            background = pygame.image.load(background_list[recharger])
            background = pygame.transform.scale(background, (WIDTH, HEIGHT))

            #maj des elements du jeu
            ecran.fill((0,0,0))
            ecran.blit(background, (0,0))
            ecran.blit(hitbox_tableheart_surface, (0,0))

            #monstres
            for monstre in monstres : 
                if monstre.boss :
                    if time() - monstre.time_lastMovement > 3: 
                        if crying_child < 10 :
                            monstre.time_lastMovement = time()
                            monstres.append(Monstre(monstre.position['x'], monstre.position['y']))

                            crying_child += 1
                monstre.move()
                ecran.blit(monstre.image, (monstre.position['x'], monstre.position['y']))

            #joueur
            joueur.move()
            surfaceJoueur = joueur.get()
            ecran.blit(joueur.image, (joueur.position['x'], joueur.position['y']))
            
            for event in pygame.event.get():
                #quand on essaye de quitter
                if event.type == pygame.QUIT:
                    continuer = False
                
                #quand on appuie sur une touche
                elif event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_z : 
                        joueur.direction["up"] = True
                    elif event.key == pygame.K_s : 
                        joueur.direction["down"] = True
                    elif event.key == pygame.K_q : 
                        joueur.direction["left"] = True
                    elif event.key == pygame.K_d : 
                        joueur.direction["right"] = True
                    elif event.key == pygame.K_e :
                        if recharger > 0 :
                            if surfaceJoueur.colliderect(hitbox_tableheart):
                                recharger -= 1
                                munition += 1 
                    elif event.key == pygame.K_SPACE :
                        if munition > 0 :
                            p = Projectile(joueur.position['x'] + 75, joueur.position['y'] + 75, 40, 40)
                            p.direction['right'] = True
                            projectiles.append(p)
                            munition -= 1

                #quand on relache une touche
                elif event.type == pygame.KEYUP :
                    if event.key == pygame.K_z : 
                        joueur.direction["up"] = False
                    elif event.key == pygame.K_s : 
                        joueur.direction["down"] = False
                    elif event.key == pygame.K_q : 
                        joueur.direction["left"] = False
                    elif event.key == pygame.K_d : 
                        joueur.direction["right"] = False
                        
            #projectiles
            if projectiles:
                for projectile in projectiles[:]:
                    projectile.move(background)
                    ecran.blit(projectile.image, (projectile.position['x'], projectile.position['y']))
                    rect_p = projectile.get(background)
                    for monstre in monstres[:]:
                        if rect_p.colliderect(monstre.get()):
                            if monstre.vie > 0:
                                monstre.vie -= projectile.degat
                                if projectile in projectiles:
                                    projectiles.remove(projectile)
                                if monstre.vie <= 0:
                                    if monstre.boss:
                                        monstres.clear()
                                        projectiles.clear()
                                        i = time()
                                        j = 0
                                        while time() - i < 5 :
                                            if j == 0 :
                                                winbg = pygame.image.load(minigame_winbg_list[0])
                                                winbg = pygame.transform.scale(winbg, (WIDTH, HEIGHT))
                                                ecran.fill((0,0,0))
                                                ecran.blit(winbg, (0,0))
                                                pygame.display.flip()
                                                j += 1
                                            elif j == 1 :
                                                winbg = pygame.image.load(minigame_winbg_list[1])
                                                winbg = pygame.transform.scale(winbg, (WIDTH, HEIGHT))
                                                ecran.fill((0,0,0))
                                                ecran.blit(winbg, (0,0))
                                                j -= 1
                                                pygame.display.flip()
                                        pygame.display.flip()
                                        chargement(5,0.5)
                                        continuer = False
                                    else:
                                        if monstre in monstres:
                                            monstres.remove(monstre)
                            else:
                                if monstre in monstres:
                                    monstres.remove(monstre)
                            break
                    
            #mettre a jour le temps
            new_time = time()
            bg_time = new_time - temps

            #rafraichir l'ecran
            pygame.display.flip()
import sys, pygame

import Constants as Const
from GameInit import screen, background, ship_imgs, proj1_imgs
from PlayerShipObject import PlayerShipObject as PlayerShip
from ProjectileObject import ProjectileObject as Projectile
from Support import directions

#-----------------------------------------------------------------------------

# Game will be more in Asteroids type:
# keys left/right - ship rotation
# keys up/down - accelerate/break
# spaceship won't stop moving until player stops it

#-----------------------------------------------------------------------------

screen.blit(background, (0, 0))
screen_center = ((Const.disp_width - Const.ship_size[0]) // 2, (Const.disp_height - Const.ship_size[1]) // 2)

spaceship = PlayerShip(ship_imgs[0], screen_center)
old_center = ship_imgs[0].get_rect().center
projectiles = []

while 1:
    for event in pygame.event.get():
        if event.type in (pygame.QUIT,):
            sys.exit()

    screen.blit(background, spaceship.pos, spaceship.pos)
    for proj in projectiles:
        screen.blit(background, proj.pos, proj.pos)

    for x in range(len(projectiles)-1, -1, -1):
        if projectiles[x].dist > projectiles[x].max_dist:
            projectiles.remove(projectiles[x])

    r = pygame.key.get_pressed()[pygame.K_RIGHT]
    l = pygame.key.get_pressed()[pygame.K_LEFT]
    u = pygame.key.get_pressed()[pygame.K_UP]
    d = pygame.key.get_pressed()[pygame.K_DOWN]
    sp = pygame.key.get_pressed()[pygame.K_SPACE]

    if r:
        spaceship.direc -= 1
        if spaceship.direc < 0:
            spaceship.direc += len(directions)
        spaceship.change_direc(spaceship.direc)

    if l:
        spaceship.direc += 1
        spaceship.direc %= len(directions)
        spaceship.change_direc(spaceship.direc)

    if u:
        spaceship.move_sp(spaceship.direc)

    # if r and not (u or d):
    #     spaceship.move_sp(directions['r'])
    #
    # if l and not (u or d):
    #     spaceship.move_sp(directions['l'])
    #
    # if u and not (r or l):
    #     spaceship.move_sp(directions['u'])
    #
    # if d and not (r or l):
    #     spaceship.move_sp(directions['d'])
    #
    # if r and u:
    #     spaceship.move_sp(directions['ru'])
    #
    # if r and d:
    #     spaceship.move_sp(directions['rd'])
    #
    # if l and u:
    #     spaceship.move_sp(directions['lu'])
    #
    # if l and d:
    #     spaceship.move_sp(directions['ld'])

    if sp:
        n_projs = len(projectiles)
        if n_projs == 0 or projectiles[n_projs-1].dist > Const.proj_delay:
            b = Projectile(proj1_imgs[0], spaceship.pos.center, ship=spaceship, direc=spaceship.direc)
            projectiles.append(b)

    for proj in projectiles:
        proj.move_sp()
        proj.dist += 1

    screen.blit(spaceship.image, spaceship.pos)
    for proj in projectiles:
        screen.blit(proj.image, proj.pos)

    pygame.display.update()
    pygame.time.delay(Const.time_delay)
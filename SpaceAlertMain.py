import sys, pygame
from numpy import array, arange

import Constants as Const
from GameInit import screen, background, ship_imgs, proj1_imgs
from PlayerShipObject import PlayerShipObject as PlayerShip
from ProjectileObject import ProjectileObject as Projectile
from Support import directions, unit_speeds

#-----------------------------------------------------------------------------

# Game will be more in Asteroids type:
# keys left/right - ship rotation
# keys up/down - accelerate/break
# spaceship won't stop moving until player stops it

#-----------------------------------------------------------------------------

screen.blit(background, (0, 0))
screen_center = ((Const.disp_width - Const.ship_size[0]) // 2, (Const.disp_height - Const.ship_size[1]) // 2)

spaceship = PlayerShip(ship_imgs[0], screen_center, speed=0)
old_center = ship_imgs[0].get_rect().center
projectiles = []

rot_delay = 1

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

    spaceship.move_sp()

    if spaceship.pos.left > Const.disp_width:
        spaceship.pos.right = 0
    if spaceship.pos.top > Const.disp_height:
        spaceship.pos.bottom = 0
    if spaceship.pos.right < 0:
        spaceship.pos.left = Const.disp_width
    if spaceship.pos.bottom < 0:
        spaceship.pos.top = Const.disp_height

    r = pygame.key.get_pressed()[pygame.K_RIGHT]
    l = pygame.key.get_pressed()[pygame.K_LEFT]
    u = pygame.key.get_pressed()[pygame.K_UP]
    d = pygame.key.get_pressed()[pygame.K_DOWN]
    sp = pygame.key.get_pressed()[pygame.K_SPACE]

    if rot_delay > 0:
        rot_delay -= 1

    if r and not rot_delay:
        rot_delay = Const.rot_delay
        spaceship.orient -= 1
        if spaceship.orient < 0:
            spaceship.orient += len(directions)
        spaceship.change_orient(spaceship.orient)

    if l and not rot_delay:
        rot_delay = Const.rot_delay
        spaceship.orient += 1
        spaceship.orient %= len(directions)
        spaceship.change_orient(spaceship.orient)

    if u:
        last_speed = spaceship.speed
        spaceship.increase_speed_xy()
        if spaceship.speed > Const.ship_max_speed:
            spaceship.speed = last_speed
            # update speed_xy so that the old direction is not lost
            # add dv(x, y) insted of setting new v(x, y)
            spaceship.update_speed_xy()

    if sp:
        n_projs = len(projectiles)
        if n_projs == 0 or projectiles[n_projs-1].dist > Const.proj_delay:
            proj_speed = Const.proj_speed + spaceship.speed     # ???
            b = Projectile(proj1_imgs[0], spaceship.pos.center, ship=spaceship, speed=proj_speed, orient=spaceship.orient)
            projectiles.append(b)

    for proj in projectiles:
        proj.move_sp()
        proj.dist += 1

    screen.blit(spaceship.image, spaceship.pos)
    for proj in projectiles:
        screen.blit(proj.image, proj.pos)

    pygame.display.update()
    pygame.time.delay(Const.time_delay)
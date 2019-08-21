import pygame
import Constants as Const

screen = pygame.display.set_mode((Const.disp_width, Const.disp_height))
background = pygame.image.load(Const.sprites_dir + 'space.png').convert()

ship_up_img = pygame.image.load(Const.sprites_dir + 'ship_u.png').convert()
ship_up_img.set_colorkey(pygame.color.Color('white'))

proj1_up_img = pygame.image.load(Const.sprites_dir + 'bull_u.png').convert()
proj1_up_img.set_colorkey(pygame.color.Color('white'))

ship_imgs = [ship_up_img]
proj1_imgs = [proj1_up_img]

for ang in range(45, 359, 45):
    ship_imgs.append(pygame.transform.rotate(ship_up_img, ang).convert())
    proj1_imgs.append(pygame.transform.rotate(proj1_up_img, ang).convert())

# for ang in sup.frange(22.5, 359, 22.5):
#     ship_imgs.append(transform.rotate(ship_up_img, ang).convert())
#     proj1_imgs.append(transform.rotate(proj1_up_img, ang).convert())
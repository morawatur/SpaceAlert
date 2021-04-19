import pygame
from numpy import radians, sin, cos

import Constants as Const
import Support as Sup

screen = pygame.display.set_mode((Const.disp_width, Const.disp_height))
background = pygame.image.load(Const.sprites_dir + 'space.png').convert()

ship_right_img = pygame.image.load(Const.sprites_dir + 'ship_right.png').convert()
ship_right_img.set_colorkey(pygame.color.Color('white'))

proj1_right_img = pygame.image.load(Const.sprites_dir + 'proj1_right.png').convert()
proj1_right_img.set_colorkey(pygame.color.Color('white'))

ship_imgs = []
proj1_imgs = []

d_rot_ang = Const.rot_ang_increment

for ang in Sup.frange(0, 359, d_rot_ang):
    ang_rad = radians(ang)
    Sup.unit_speeds.append((cos(ang_rad), -sin(ang_rad)))

    ship_imgs.append(pygame.transform.rotate(ship_right_img, ang).convert())
    proj1_imgs.append(pygame.transform.rotate(proj1_right_img, ang).convert())

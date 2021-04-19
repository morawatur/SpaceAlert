import numpy as np

import Constants as Const
from GameObject import GameObject
from GameInit import proj1_imgs
from Support import directions, unit_speeds

class ProjectileObject(GameObject):
    def __init__(self, image, pos=(0, 0), ship=None, speed=Const.proj_speed, orient=directions['r'], max_dist=Const.proj_max_dist):
        super(ProjectileObject, self).__init__(image, pos)
        self.ship = ship
        self.orient = orient
        self.speed = speed
        self.speed_xy = [0, 0]
        self.start_pos = pos
        self.max_dist = max_dist
        self.dist = 0
        self.set_img_from_direc()
        self.set_speed_xy_from_orient()

    def set_img_from_direc(self):
        self.set_image(proj1_imgs[self.orient])
        hbs = [ n // 2 for n in self.image.get_size() ]                 # half_bullet_size
        # hss = [ n // 2 for n in self.ship.image.get_size() ]          # half_ship_size
        if not self.orient % 2:
            hss = [ n // 2 for n in self.ship.image.get_size() ]
        else:
            hss = [ n // 6 for n in self.ship.image.get_size() ]

        if self.orient == directions['u']:
            self.pos = self.pos.move(-hbs[0], -hss[1] - 2 * hbs[1])
        elif self.orient == directions['lu']:
            self.pos = self.pos.move(-hss[0] - 2 * hbs[0], -hss[1] - 2 * hbs[1])
        elif self.orient == directions['l']:
            self.pos = self.pos.move(-hss[0] - 2 * hbs[0], -hbs[1])
        elif self.orient == directions['ld']:
            self.pos = self.pos.move(-hss[0] - 2 * hbs[0], hss[1])
        elif self.orient == directions['d']:
            self.pos = self.pos.move(-hbs[0], hss[1])
        elif self.orient == directions['rd']:
            self.pos = self.pos.move(hss[0], hss[1])
        elif self.orient == directions['r']:
            self.pos = self.pos.move(hss[0], -hbs[1])
        elif self.orient == directions['ru']:
            self.pos = self.pos.move(hss[0], -hss[1] - 2 * hbs[1])

    def set_speed_xy_from_orient(self):
        self.speed_xy = list(self.speed * np.array(unit_speeds[self.orient]))

    def move_sp(self):
        super(ProjectileObject, self).move(self.speed_xy)

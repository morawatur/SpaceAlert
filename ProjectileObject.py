import numpy as np

import Constants as Const
from GameObject import GameObject
from GameInit import proj1_imgs
from Support import directions, unit_speeds

class ProjectileObject(GameObject):
    def __init__(self, image, pos=(0, 0), ship=None, speed=Const.proj_speed, direc=directions['u'], max_dist=Const.proj_max_dist):
        super(ProjectileObject, self).__init__(image, pos)
        self.ship = ship
        self.direc = direc
        self.speed = speed
        self.speed_xy = [0, 0]
        self.start_pos = pos
        self.max_dist = max_dist
        self.dist = 0
        self.set_img_from_direc()
        self.set_speed_xy_from_direc()

    def set_img_from_direc(self):
        self.set_image(proj1_imgs[self.direc])
        hbs = [ n // 2 for n in self.image.get_size() ]                 # half_bullet_size
        # hss = [ n // 2 for n in self.ship.image.get_size() ]          # half_ship_size
        if not self.direc % 2:
            hss = [ n // 2 for n in self.ship.image.get_size() ]
        else:
            hss = [ n // 6 for n in self.ship.image.get_size() ]

        if self.direc == directions['u']:
            self.pos = self.pos.move(-hbs[0], -hss[1] - 2 * hbs[1])
        elif self.direc == directions['lu']:
            self.pos = self.pos.move(-hss[0] - 2 * hbs[0], -hss[1] - 2 * hbs[1])
        elif self.direc == directions['l']:
            self.pos = self.pos.move(-hss[0] - 2 * hbs[0], -hbs[1])
        elif self.direc == directions['ld']:
            self.pos = self.pos.move(-hss[0] - 2 * hbs[0], hss[1])
        elif self.direc == directions['d']:
            self.pos = self.pos.move(-hbs[0], hss[1])
        elif self.direc == directions['rd']:
            self.pos = self.pos.move(hss[0], hss[1])
        elif self.direc == directions['r']:
            self.pos = self.pos.move(hss[0], -hbs[1])
        elif self.direc == directions['ru']:
            self.pos = self.pos.move(hss[0], -hss[1] - 2 * hbs[1])

    def set_speed_xy_from_direc(self):
        self.speed_xy = list(self.speed * np.array(unit_speeds[self.direc]))

    def move_sp(self):
        super(ProjectileObject, self).move(self.speed_xy)
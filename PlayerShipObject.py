import numpy as np

import Constants as Const
from GameObject import GameObject
from GameInit import ship_imgs
from Support import directions, unit_speeds

class PlayerShipObject(GameObject):
    def __init__(self, image, pos=(0, 0), speed=Const.ship_speed, orient=directions['r']):
        super(PlayerShipObject, self).__init__(image, pos)
        self.orient = orient
        self.direc = orient
        self.speed = speed
        self.speed_xy = [0, 0]
        self.set_img_from_orient()
        self.update_speed_xy()

    def change_orient(self, orient):
        self.orient = orient
        self.set_img_from_orient()

    def set_img_from_orient(self):
        center = self.pos.center
        self.set_image(ship_imgs[self.orient])
        half_size = [n // 2 for n in self.image.get_size()]
        self.pos = self.image.get_rect().move(center[0]-half_size[0], center[1]-half_size[1])

    def update_speed(self):
        self.speed = np.abs(np.complex(self.speed_xy[0], self.speed_xy[1]))

    def update_speed_xy(self):
        self.speed_xy = list(self.speed * np.array(unit_speeds[self.direc]))

    def increase_speed_xy(self):
        dv = [ dvi for dvi in unit_speeds[self.orient] ]
        if self.direc != self.orient:
            dec_v = [ 0.1 * dvi for dvi in unit_speeds[self.direc] ]
            dv = [ dvi - dvj for dvi, dvj in zip(dv, dec_v) ]
        self.change_speed_xy_by(dv)
        self.update_speed()

    def decrease_speed_xy(self):
        dv = [ -dvi for dvi in unit_speeds[self.direc] ]
        self.change_speed_xy_by(dv)
        self.update_speed()

    def change_speed_xy_by(self, dv=(0, 0)):
        self.speed_xy = [ vi + dvi for vi, dvi in zip(self.speed_xy, dv) ]
        self.update_speed()
        cos_check = self.speed_xy[0] / self.speed
        if np.abs(cos_check - unit_speeds[self.orient][0]) < 1e-3:
            self.direc = self.orient

    def move_sp(self):
        """
        This method takes into account the rules by which the ship/projectile is able to move in space.
        On the other hand the 'move()' super method is used to arbitrary position objects on screen.
        """
        super(PlayerShipObject, self).move(self.speed_xy)
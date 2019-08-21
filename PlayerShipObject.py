import numpy as np

import Constants as Const
from GameObject import GameObject
from GameInit import ship_imgs
from Support import directions, unit_speeds

class PlayerShipObject(GameObject):
    def __init__(self, image, pos=(0, 0), speed=Const.ship_speed, direc=directions['u']):
        super(PlayerShipObject, self).__init__(image, pos)
        self.direc = direc
        self.speed = speed
        self.speed_xy = [0, 0]
        self.set_img_from_direc()
        self.set_speed_xy_from_direc()

    def change_direc(self, direc):
        self.direc = direc
        self.set_img_from_direc()
        self.set_speed_xy_from_direc()

    def set_img_from_direc(self):
        center = self.pos.center
        self.set_image(ship_imgs[self.direc])
        half_size = [n // 2 for n in self.image.get_size()]
        self.pos = self.image.get_rect().move(center[0]-half_size[0], center[1]-half_size[1])

    def set_speed_xy_from_direc(self):
        self.speed_xy = list(self.speed * np.array(unit_speeds[self.direc]))

    def move_sp(self, direc=directions['u']):
        """
        This method takes into account the rules by which the ship/projectile is able to move in space.
        On the other hand the 'move()' super method is used to arbitrary position objects on screen.
        """
        if self.direc != direc:
            self.direc = direc
            self.set_img_from_direc()
            self.set_speed_xy_from_direc()

        super(PlayerShipObject, self).move(self.speed_xy)

        if self.pos.right > Const.disp_width:
            self.pos.left = 0
        if self.pos.bottom > Const.disp_height:
            self.pos.top = 0
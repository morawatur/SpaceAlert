class GameObject:
    def __init__(self, image, pos=(0, 0)):
        self.image = image
        self.pos = image.get_rect().move(pos[0], pos[1])

    def move(self, speed_xy=(0, 0)):
        self.pos = self.pos.move(speed_xy[0], speed_xy[1])

    def set_image(self, image):
        self.image = image
        self.pos = self.image.get_rect().move(self.pos[0], self.pos[1])

    def get_w_h(self):
        return self.image.get_width(), self.image.get_height()
from pygame import Color, Rect, Surface

class Scene():
    def __init__(self):
        self.started = False
        self.area_info = (0, 0, 450, 450)
        self.cell_amt = 18
        self.back_colour = Color(255, 255, 255)
        self.cell_colour = Color(245, 242, 222)

    def start(self):
        self.started = True
        return self.started

    def update(self, delta):
        pass

    def render(self, target):
        pass

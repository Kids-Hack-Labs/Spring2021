from pygame import Color, Rect, Surface

class Scene():
    def __init__(self):
        self.started = False
        self.area_info = (0, 0, 450, 450)
        self.cell_amt = 18
        self.back_colour = Color(255, 255, 255)
        self.cell_colour = Color(245, 242, 222)

        self.cell_size = (int(self.area_info[2]/self.cell_amt),
                          int(self.area_info[3]/self.cell_amt))
        self.play_rect = Rect(self.area_info)
        self.play_surf = Surface(self.play_rect.size)
        self.play_surf.fill(self.back_colour)

            #checkerboard draw
        from pygame.draw import rect
        for x in range(self.cell_amt):
            for y in range(self.cell_amt):
                if (x%2==0)^(y%2==0):
                    rect(self.play_surf, self.cell_colour,
                         Rect((x*self.cell_size[0],
                               y*self.cell_size[1]),
                              self.cell_size))

    def start(self):
        self.started = True
        return self.started

    def update(self, delta):
        pass

    def render(self, target):
        target.blit(self.play_surf, self.play_rect)

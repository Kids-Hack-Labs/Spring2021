"""
    Collectible class:
    Just a circle that jumps around when collected
"""
from random import randrange
from pygame import Surface

class Collectible():
    def __init__(self, size, max_cells):
        self.started = False
        #Basic setup
        self.max_cells = max_cells #int
        self.current_cell = (0,0)
        self.surf = Surface(size) #size also tuple
        self.rect = self.surf.get_rect()

        #Graphical setup
        colorkey = (0,255,0)
        self.surf.fill(colorkey)
        from pygame.draw import circle
        circle(self.surf, (255, 0, 0), self.rect.center, -1+self.rect.width/2)
        self.surf.set_colorkey(colorkey)

        #positioning
        self.reposition()

    def start(self):
        self.started = self.surf is not None and self.surf.get_colorkey() is not None
        return self.started
    
    def update(self,delta):
        pass

    def render(self, target):
        target.blit(self.surf, self.rect)

    def reposition(self):
        self.current_cell = (randrange(self.max_cells),
                             randrange(self.max_cells))
        self.rect.left = self.current_cell[0]*self.rect.width
        self.rect.top = self.current_cell[1]*self.rect.height

    def get_current_cell(self):
        return self.current_cell

import random
import pygame
from pygame.locals import *
from pygame.time import Clock

class Game():
    class __Game():
        __FPS = 0
        def __init__(self, defaults, window_attributes):
            random.seed()

            Game.__Game.__FPS = defaults["FPS"]

            pygame.init()
            self.time_since_started = pygame.time.get_ticks()
            self.clock = Clock()
            self.delta = 0
            
            self.screen = pygame.display.set_mode(window_attributes["size"])
            pygame.display.set_caption(window_attributes["caption"])

            from src.scene import Scene
            self.scene = Scene()

            self.is_start = False
            self.is_run = False

        def start(self):
            scene_started = self.scene.start()
            self.is_run = True
            return self.is_run and scene_started
        
        def process_events(self):
            for evt in pygame.event.get():
                if evt.type == QUIT:
                    self.quit()

        def update(self, delta):
            self.scene.update(delta)

        def render(self, target):
            #target.fill((200, 200, 200))
            self.scene.render(target)
            pygame.display.flip()
                    
        def run(self):
            if self.is_start:
                return
            self.is_start = self.start()
            if not self.is_start:
                raise RuntimeError("could not start")

            while self.is_run:
                self.process_events()
                self.update(self.delta)
                self.render(self.screen)
                self.delta = self.clock.tick(Game.instance.__FPS)
                self.time_since_started = pygame.time.get_ticks()

            pygame.quit()

        def quit(self):
            self.is_run = False

    #singleton
    instance = None
    def __init__(self, defaults, window_attributes):
        if not Game.instance:
            Game.instance = Game.__Game(defaults, window_attributes)

    def __getattr__(self, name):
        return getattr(self.instance, name)

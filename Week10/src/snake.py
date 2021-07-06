from enum import Enum

from pygame import Surface
import pygame.key as pk
from pygame.locals import *

class Directions(Enum):
    NORTH = ( 0,-1)
    EAST  = ( 1, 0)
    SOUTH = ( 0, 1)
    WEST  = (-1, 0)

class Snake():
    def __init__(self, size, num_cells, wraparound = True):
        self.started = False
        #Basic setup
        self.part_size = size #tuple
        self.num_cells = num_cells #int
        self.wrap = wraparound

        #Graphics setup
        self.head_surf = Surface(size)
        self.head_surf.fill((255, 0, 0))
        self.body_surf = Surface(size)
        self.body_surf.fill((0,255,0))
        self.dead_surf = Surface(size)
        self.dead_surf.fill((50, 50, 50))
        
        #Positions setup
        self.coords = []
        self.coords.append([num_cells//2, num_cells//2])
        self.coords.append((-1+num_cells//2, num_cells//2))

        #Movement setup
            #Time variables (in ms)
        self.max_time = 500  #reference
        self.cur_max  = 500  #decreases
        self.cur_time = 500  #current time
        self.speed_rate = 50 #change rate
        self.speed_change = False
        self.has_changed = False
            #Space variables
        self.cur_direction = Directions.EAST.value
        self.command_queue = []

        #Growth variables
        self.growth = False

        #Snake alive
        self.alive = True

    def start(self):
        self.started = self.head_surf is not None and self.body_surf is not None
        return self.started

    def update(self, delta):
        if not self.alive: #no point updating if dead
            return

        #Key presses:
        keys = pk.get_pressed()
        north = keys[K_w] or keys[K_UP]
        south = keys[K_s] or keys[K_DOWN]
        east = keys[K_d] or keys[K_RIGHT]
        west = keys[K_a] or keys[K_LEFT]

        self.turn((north, east, south, west))
        self.shift(delta)

    def render(self, target):
        target.blit(self.head_surf,(self.coords[0][0]*self.part_size[0],
                                    self.coords[0][1]*self.part_size[1]))
        for coord in self.coords[1::]:
            target.blit(self.body_surf, (coord[0]*self.part_size[0],
                                         coord[1]*self.part_size[1]))

    def turn(self, directions):
        if len(self.command_queue) < 2: #if there are enough input slots available
            if self.cur_direction[0] != 0: #if it's currently moving horizontally
                #if there are no inputs queued or if the last input is queued for a horizontal movement
                #This basically makes it impossible for the user to try and "backtrack"
                if len(self.command_queue) == 0 or self.command_queue[-1][0] != 0:
                    if directions[0]: #if vertical input NORTH
                        self.command_queue.append(Directions.NORTH.value)
                    elif directions[2]:
                        self.command_queue.append(Directions.SOUTH.value)
            elif self.cur_direction[1] != 0: #if it's currently moving vertically
                #if there are no inputs queued or if the last input is queued for a vertical movement
                #This basically makes it impossible for the user to try and "backtrack"
                if len(self.command_queue) == 0 or self.command_queue[-1][1] !=0:
                    if directions[1]:
                        self.command_queue.append(Directions.EAST.value)
                    elif directions[3]:
                        self.command_queue.append(Directions.WEST.value)

    def shift(self, delta):
        self.cur_time -= delta
        if self.cur_time <= 0:
            self.cur_time += self.cur_max
            self.move()
            self.alive = self.check_alive() #does this check have to be here?

        if self.speed_change and not self.has_changed:
            self.speed_change = False
            self.has_changed = True
            self.cur_max -= self.speed_rate
        
    def move(self):
        temp_growth = None
        if self.growth:
            self.growth = False
            temp_growth = self.coords[-1]
        for i in range(len(self.coords)-1, 0, -1):
            self.coords[i] = tuple(self.coords[i-1])
        if temp_growth is not None:
            self.coords.append(temp_growth)
        if len(self.command_queue) > 0:
            self.cur_direction = self.command_queue.pop(0)
        self.coords[0][0] += self.cur_direction[0]
        self.coords[0][1] += self.cur_direction[1]

        if self.wrap:
            self.coords[0][0] %= self.num_cells
            self.coords[0][1] %= self.num_cells

    def check_alive(self):
        #The first four conditions are always True if self.wrap is True
        return self.coords[0][0] >= 0 and self.coords[0][0]<self.num_cells and\
               self.coords[0][1] >= 0 and self.coords[0][1]<self.num_cells and\
               (tuple(self.coords[0]) not in self.coords[1::])

    def get_head(self):
        return tuple(self.coords[0])

    def get_snake(self):
        return [tuple(self.coords[0])]+self.coords[1::]

    def set_growth(self):
        self.growth = True

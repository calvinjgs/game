import pygame
from pygame.locals import *

from EventManager import *

class model_object:
    """The model_object class represents an object in the model. It has
    position in space and has a rectangular footprint. The position is the
    point at the centre of the footprint."""
    
    def __init__(self, pos, size):
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.width = size[0]
        self.height = size[1]
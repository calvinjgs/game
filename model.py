import pygame
from pygame.locals import *
from EventManager import *

import numpy as np


class model:
    """The model class is a 2D arrray of dictionaries. The indices of the array
correspond to grid locations. Each dictionary contains model_objects that have
positions within the the grid location. If the object changes position such
that it lies outside that location, it will be removed from that dictionary and
into the appropriate one. 
"""

    def __init__(self, sec_shape, sec_size):
        self.sectors = np.empty(sec_shape, dtype=dict)
        for j in range(sectors):
            for i in range(sectors[j]):
                self.sectors[i, j] = {}
        self.sector_width = sec_size[0]
        self.sector_height = sec_size[1]
        self.evManager.registerListener(self,[ModelObjectMoveRequest, ModelObjectMoveEvent])

    
    #returns sector indices based on position
    def to_index(self, pos):
        i = pos[0]//self.sector_width
        j = pos[1]//self.sector_height
        i = min(i, self.sectors.shape[0])
        i = max(i, 0)
        j = min(j, self.sectors.shape[1])
        j = max(j, 0)
        
        return (i, j)

    #inserts a model object into a sector based on its position
    def insert(self, m_o):
        i, j = self.to_index(m_o.pos)
        self.sectors[i, j][str(id(m_o))] = m_o
    #remove model object
    def remove(self, m_o):
        i, j = self.to_index(m_o.pos)
        del self.sectors[i, j][str(id(m_o))]
    
    #move object from one old position to new position
    def move(self, m_o, from_pos, to_pos):
        i_0, j_0 = self.to_index(from_pos)
        del self.sectors[i_0, j_0][str(id(m_o))]
        i, j = self.to_index(from_pos)
        self.sectors[i, j][str(id(m_o))] = m_o

    def notify(event):
        if Event.is_a(ModelObjectMoveRequest):
        	#ModelObjectMoveRequest
        	#ev = ModelObjectMoveEvent(obj, from_pos, to_pos):
        	#self.evManager.post(ev)
        	
        if Event.is_a(ModelObjectMoveEvent):
            move(event.m_obj, event.from_pos, event.to_pos)

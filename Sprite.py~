import pygame
from pygame.locals import *

from EventManager import *
from SpriteSheet import *
from MySprite import *
#	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	SpriteState

#	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	Sector Sprite
class SectorSprite(MySprite):
	def __init__(self, sector, group=None):
		pygame.sprite.Sprite.__init__(self, group)
		self.image = pygame.Surface((128,128), flags=pygame.SRCALPHA)
		self.image.fill((0,128,128))

		self.sector = sector
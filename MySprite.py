import pygame
from pygame.locals import *

from SpriteSheet import *

class MySprite(pygame.sprite.Sprite):
#Parent class for sprites
	def __init__(self):
		self.imageWidth		=	50
		self.imageHeight	=	100
		self.width			=	100
		self.height			=	200

	def getImage():
		return self.states[self.state].getImage()

	def loadSpriteSheet(self, sheet, width, height):
		self.spriteSheet = SpriteSheet(sheet)
		#self.image = self.spriteSheet.image_at((0, 0, width, height))
		#self.images = []
		# Load two images into an array, their transparent bit is (255, 255, 255)
		#self.images = self.spriteSheet.images_at((0, 0, 16, 16),(17, 0, 16,16), colorkey=(255, 255, 255))
		
	def scale(self):
		#...
		return

#	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	SpriteState
class SpriteState(object):
	'''
	Contains and iterates over a strip of images
	This could be expanded to take an optional framesLong map which tells a particular frame to hold for a number of ticks
	'''
	def __init__(self, spriteSheet, rect, framesWide, row):
		self.frame = 0
		self.rect = rect
		self.framesWide = framesWide
		self.row = row
		self.strip = spriteSheet.load_strip(self.rect, self.framesWide, self.row)
		self.frames = len(self.strip)
		
	def getImage(self):
		image = self.strip[self.frame]
		self.frame += 1
		if self.frame >= self.frames:
			self.frame = 0
		return image
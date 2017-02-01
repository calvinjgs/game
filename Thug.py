##		** Everything relating to "sector", "new sector", and "STATE_...TIVE" is from tutorial
'''
Upon SELF.PLACEing the modelentity, the viewentity is instanciated (through an event).
The viewentity has reference to it's modelentity and listens for the modelentity's events.
'''


import pygame
from pygame.locals import *

from EventManager import *
from Entity import *

class ThugModelEntity(ModelEntity):

	def __init__(self, evManager):
		self.evManager = evManager
		
		#List every event for which this object listens
		self.evManager.registerListener(self, [GameStatePlayEvent, CreatureMoveRequest])
		self.sector = None

	def __str__(self):
		return '<Thug %s>' % id(self)
		
	def place(self, pos): #pos = (x, y)
		self.pos = pos
		ev = CreateCreatureViewEntityEvent(self) 
		self.evManager.post(ev)

	def move(self, deltaX, deltaY):
			self.evManager.post(CreatureMoveEvent(self))
			self.evManager.post(SpriteStateChangeEvent(self, 'idle'))

	def notify(self, event):
		if event.is_a(GameStatePlayEvent):
			gameMap = event.levelMap
			self.place(gameMap.sectors[gameMap.startSectorIndex])

		elif event.is_a(CreatureMoveRequest):
			self.move(event.direction)

#	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	Thug Sprite
class ThugViewEntity(ViewEntity):
	def __init__(self, evManager, entity, group=None,):
		self.evManager = evManager
		self.entity = entity
		#List every event for which this object listens
		self.evManager.registerListener(self,[CreatureMoveEvent, SpriteStateChangeEvent])
		pygame.sprite.Sprite.__init__(self, group)
		self.state = 'idle'
		#self.spriteSheet = SpriteSheet('dude_animation_sheet_2(130,152).png')
		#self.imageWidth		=	130
		#self.imageHeight	=	152
		self.spriteSheet = SpriteSheet('ken-sprite-sheet(,).png')
		self.imageWidth		=	102
		self.imageHeight	=	133
		self.width			=	self.imageWidth
		self.height			=	self.imageHeight

		self.image = self.spriteSheet.image_at((0, 0, self.width, self.height))
		#self.image.set_alpha(128)
		self.rect = self.image.get_rect()
		self.states = {
			'idle':SpriteState(self.spriteSheet, self.rect, 10, 0),
			'walk':SpriteState(self.spriteSheet, self.rect, 10, 1),
			'shoot':SpriteState(self.spriteSheet, self.rect, 11, 2),
			'jump':SpriteState(self.spriteSheet, self.rect, 7, 5)
		}
		self.moveTo = None
		#self.evManager.post(ThugViewEntityStateChange(self, 'run'))

	def update(self):
		if self.moveTo:
			self.rect.center = self.moveTo
			self.moveTo = None
		self.image = self.states['idle'].getImage()
		
	def notify(self, event):
		if event.is_a(SpriteStateChangeEvent):
			if event.entity == self.entity:
				self.state = event.state
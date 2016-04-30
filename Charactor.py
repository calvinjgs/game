import pygame
from pygame.locals import *

from EventManager import *
from MySprite import *


#move similar methods into an "Entity" superclass, and MySprite super class
class CharactorEntity:
	STATE_INACTIVE = 0
	STATE_ACTIVE = 1

	def __init__(self, evManager, playerNumber):
		self.evManager = evManager
		
		#List every event for which this object listens
		self.evManager.registerListener(self,[GameStatePlayEvent,CharactorMoveRequest])
		self.playerNumber = playerNumber
		self.sector = None
		self.state = CharactorEntity.STATE_INACTIVE

	def __str__(self):
		return '<Charactor %s>' % id(self)

	def move(self, direction):
		if self.state == CharactorEntity.STATE_INACTIVE:
			return

		if self.sector.movePossible( direction ):
			newSector = self.sector.neighbors[direction]
			self.sector = newSector
			self.evManager.post(CharactorMoveEvent(self))
			self.evManager.post(SpriteStateChangeEvent(self, 'idle'))

	def place(self, sector):
		self.sector = sector
		self.state = CharactorEntity.STATE_ACTIVE

		ev = CreateCharactorSpriteEvent(self, self.playerNumber)
		self.evManager.post(ev)

	def notify(self, event):
		if event.is_a(GameStatePlayEvent):
			gameMap = event.levelMap
			self.place(gameMap.sectors[gameMap.startSectorIndex])

		elif event.is_a(CharactorMoveRequest):
			self.move(event.direction)

#	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	Charactor Sprite
class CharactorSprite(MySprite):
	def __init__(self, evManager, entity, playerNumber, group=None,):
		self.evManager = evManager
		self.entity = entity
		#List every event for which this object listens
		self.evManager.registerListener(self,[CharactorMoveEvent])
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

		self.playerNumber = playerNumber
		self.image = self.spriteSheet.image_at((0, 0, self.width, self.height))
		#self.image.set_alpha(128)
		self.rect = self.image.get_rect()
		self.states = {
			'idle':SpriteState(self.spriteSheet, self.rect, 10, 0),
			'walk':SpriteState(self.spriteSheet, self.rect, 10, 1),
			'hadouken':SpriteState(self.spriteSheet, self.rect, 11, 2),
			'jump':SpriteState(self.spriteSheet, self.rect, 7, 5)
		}
		self.moveTo = None
		#self.evManager.post(CharactorSpriteStateChange(self, 'run'))

	def update(self):
		if self.moveTo:
			self.rect.center = self.moveTo
			self.moveTo = None
		self.image = self.states['idle'].getImage()
		
	def notify(self, event):
		if event.is_a(SpriteStateChangeEvent):
			if event.entity == self.entity:
				self.state = event.state
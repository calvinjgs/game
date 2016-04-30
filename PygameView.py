import pygame
from pygame.locals import *

from EventManager import *
from Charactor import CharactorSprite
from Sprite import *

class PygameView:
	def __init__(self, evManager):
		self.evManager = evManager
		
		#List every event for which this object listens
		self.evManager.registerListener(self,[TickEvent,MapBuiltEvent,CreateCharactorSpriteEvent,CharactorMoveEvent])
		pygame.init()
		self.window = pygame.display.set_mode((424,440))
		pygame.display.set_caption('Example Game')
		self.background = pygame.Surface(self.window.get_size(), flags=pygame.SRCALPHA)
		self.background.fill((0,0,0))
		font = pygame.font.Font(None, 30)
		text = """STARTING"""
		textImg = font.render( text, 1, (255,0,0))
		self.background.blit( textImg, (0,0) )
		self.window.blit( self.background, (0,0) )
		pygame.display.flip()

		self.backSprites = pygame.sprite.RenderUpdates()
		self.frontSprites = pygame.sprite.RenderUpdates()


	#----------------------------------------------------------------------
	def showMap(self, gameMap):
		# clear the screen first
		self.background.fill((0,0,0))
		self.window.blit(self.background,(0,0))
		pygame.display.flip()

		# use this squareRect as a cursor and go through the
		# columns and rows and assign the rect 
		# positions of the SectorSprites
		squareRect = pygame.Rect( (-128,10, 128,128 ) )

		column = 0
		for sector in gameMap.sectors:
			if column < 3:
				squareRect = squareRect.move( 138,0 )
			else:
				column = 0
				squareRect = squareRect.move( -(138*2), 138 )
			column += 1
			newSprite = SectorSprite( sector, self.backSprites )
			newSprite.rect = squareRect
			newSprite = None

	#----------------------------------------------------------------------
	def createCharactorSprite(self, entity, playerNumber):
		sector = entity.sector
		charactorSprite = CharactorSprite(self.evManager, entity, playerNumber, self.frontSprites)
		sectorSprite = self.getSectorSprite( sector )
		charactorSprite.rect.center = sectorSprite.rect.center

	#----------------------------------------------------------------------
	def moveCharactor(self, charactor):
		charactorSprite = self.getCharactorSprite(charactor)

		sector = charactor.sector
		sectorSprite = self.getSectorSprite(sector)

		charactorSprite.moveTo = sectorSprite.rect.center

	#----------------------------------------------------------------------
	def getCharactorSprite(self, charactor):
		#there will be only one
		for s in self.frontSprites:
			return s
		return None

	#----------------------------------------------------------------------
	def getSectorSprite(self, sector):
		for s in self.backSprites:
			if hasattr(s, "sector") and s.sector == sector:
				return s


	#----------------------------------------------------------------------
	def notify(self, event):
		if event.is_a(TickEvent):
			#Draw Everything
			self.backSprites.clear(self.window, self.background)
			self.frontSprites.clear(self.window, self.background)

			self.backSprites.update()
			self.frontSprites.update()

			dirtyRects1 = self.backSprites.draw( self.window )
			dirtyRects2 = self.frontSprites.draw( self.window )
			
			dirtyRects = dirtyRects1 + dirtyRects2
			pygame.display.update(dirtyRects)

		elif event.is_a(MapBuiltEvent):
			levelMap = event.levelMap
			self.showMap(levelMap)

		elif event.is_a(CreateCharactorSpriteEvent):
			self.createCharactorSprite(event.entity, event.playerNumber)

		elif event.is_a(CharactorMoveEvent):
			self.moveCharactor(event.entity)
			

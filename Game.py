import pygame
from pygame.locals import *

from EventManager import *
from Player import *
from Map import *

class Game:
	def __init__(self, evManager):
		self.evManager = evManager
		#List every event for which this object listens
		self.evManager.registerListener(self,[TickEvent])
		self.state = GameStatePrepareEvent()
		self.evManager.post(self.state)
		#self.state = Game.STATE_PREPARING
		self.maxPlayers = 4
		self.players = [None] * self.maxPlayers #creates a [None, None, None...]
		self.addPlayer(1)
		self.level = Map(self.evManager)
				
	def addPlayer(self, playerNumber):
		self.players[playerNumber] = Player(self.evManager, playerNumber)
		#self.players[playerNumber] = Player(self.evManager, playerNumber, controller)

	def start(self):
		self.level.build()
		self.state = GameStatePlayEvent(self.level)
		self.evManager.post(self.state)

	def notify(self, event):				
		if event.is_a(gameStateEvents):
			self.state = event


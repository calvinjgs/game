'''
Game is the M in MVC (MODEL)
'''

import pygame
from random import randint
from pygame.locals import *

from EventManager import *
from Player import *
from Map import *
from Thug import ThugModelEntity

class Game:
	def __init__(self, evManager):
		self.evManager = evManager
		#List every event for which this object listens
		self.evManager.registerListener(self, gameStateEvents + [TickEvent])
		self.state = GameStatePrepareEvent()
		self.evManager.post(self.state)
		#self.state = Game.STATE_PREPARING
		self.maxPlayers = 4
		self.players = [None] * self.maxPlayers #creates a [None, None, None...]
		self.addPlayer(1)
		self.level = Map(self.evManager)
		
		
		#TEMPORARY
		self.model
		self.creatures = [ThugModelEntity(self.evManager), ThugModelEntity(self.evManager)]
		for creature in self.creatures:
			creature.place((randint(0,200),randint(0,200)))
		#/TEMPORARY
		
		
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
		


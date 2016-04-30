import pygame
from pygame.locals import *

from EventManager import *
from Charactor import CharactorEntity

class Player(object):
	def __init__(self, evManager, playerNumber):
		self.evManager = evManager
		self.evManager.registerListener(self,[])
		self.playerNumber = playerNumber
		self.game = None
		self.name = "Player Number" + str(self.playerNumber)
		self.charactors = []
		self.makeCharactor()

	def __str__(self):
		return '<Player %s %s>' % (self.name, id(self))

	def makeCharactor(self):
		self.charactors.append(CharactorEntity(self.evManager, self.playerNumber))
		
	def setController(self, controller):
		pass

	def notify(self, event):
		pass


import sys
import pygame
from pygame.locals import *
from gameclock import GameClock

from EventManager import *


class CPUSpinnerController:
	"""..."""
	def __init__(self, evManager):
		self.evManager = evManager
		
		#List every event for which this object listens
		self.evManager.registerListener(self,[QuitEvent])
		self.keepGoing = 1

	#----------------------------------------------------------------------
	def run(self):
		def callback(time):
			self.evManager.post(TickEvent())
			return
		clock = GameClock()
		clock.schedule_interval(callback, 0.042)
		#clock.schedule_interval(callback, 0.25)
		
		while self.keepGoing:
			clock.tick()
	#----------------------------------------------------------------------
	def notify(self, event):
		if event.is_a(QuitEvent):
			#this will stop the while loop from running
			self.keepGoing = False
			pygame.quit()
			sys.exit() 

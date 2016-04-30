#! /usr/bin/env python
import pygame
from pygame.locals import *
import sys
from myFunctions import *

from EventManager import *
from KeyboardMouseGameContController import *
from ControlMapper import *
from CPUSpinnerController import *
from PygameView import *
from Game import *

def main():
	"""..."""
	evManager = EventManager()
	keyboardMouseGameContController = KeyboardMouseGameContController(evManager)
	controlMapper = ControlMapper(evManager)
	spinner = CPUSpinnerController(evManager)
	pygameView = PygameView(evManager)
	game = Game(evManager)
	game.start()
	spinner.run()

if __name__ == "__main__":
	main()

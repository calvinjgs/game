import pygame
from pygame.locals import *

from EventManager import *
from KeyboardMouseRef import *
from XboxContRef import *

class KeyboardMouseGameContController:
	"""KeyboardController takes Pygame events and notifies the control mapper
	"""
	def __init__(self, evManager):
		self.evManager = evManager
		#List every event for which this object listens
		self.evManager.registerListener(self,[TickEvent])
		
		pygame.joystick.init()
		#print("JOYSTICK COUNT ", pygame.joystick.get_count())
		gamepads = []
		for gamepadNumber in range (pygame.joystick.get_count()):
			newGamepad = pygame.joystick.Joystick(gamepadNumber)
			# try:
				# newGamepad = pygame.joystick.Joystick(gamepadNumber)
			# except pygame.error as message:
				# raise ErrorType(message)
			newGamepad.init()
			gamepads =+ [newGamepad]
			
		# if gamepads:
			# evManager.post()
			
		# joystickNo = 0
		# joy = pygame.joystick.Joystick(joystickNo)
		# joy.init()

	#----------------------------------------------------------------------
	def notify(self, event):
		if event.is_a(TickEvent ):
			#Handle Input Events
			for event in pygame.event.get():
				ev = None
				if event.type == QUIT:
					ev = QuitEvent()
				elif event.type == KEYDOWN and event.key == K_ESCAPE:
					ev = QuitEvent()
				elif event.type == KEYDOWN:
					ev = KeyboardInputEvent(event.key, 1)
				elif event.type == KEYUP:
					ev = KeyboardInputEvent(event.key, 0)
				elif event.type == MOUSEBUTTONDOWN:
					ev = MouseInputEvent(event.button, event.pos)
					#TOTRY pygame.mouse.get_pos()
				elif event.type == MOUSEBUTTONUP:
					ev = MouseInputEvent(event.button, event.pos)
				elif event.type == JOYAXISMOTION:
					#event.joy tells us which player
					if event.axis in xboxContRef.pygameAxisInt_xboxInt:
						ev = GameContInputEvent(
							event.joy,
							xboxContRef.pygameAxisInt_xboxInt[event.axis],
							event.value)
				elif event.type == JOYHATMOTION:
					ev = GameContInputEvent(event.joy, 16, event.value)
					#TOTRY event.hat I think this should always be synonomous with event.joy. Or it's for joypads with multiple dpads
				elif event.type == JOYBUTTONUP:
					ev = GameContInputEvent(event.joy, xboxContRef.pygameButtonInt_xboxInt[event.button], 0)
				elif event.type == JOYBUTTONDOWN:
					ev = GameContInputEvent(event.joy, xboxContRef.pygameButtonInt_xboxInt[event.button], 1)

				if ev:
					self.evManager.post(ev)

from EventManager import *

from XboxContRef import *
from KeyboardMouseRef import *

DIRECTION_UP = 0
DIRECTION_DOWN = 1
DIRECTION_LEFT = 2
DIRECTION_RIGHT = 3

class ControlMapper:            
	"""ControlMapper takes input controller events and uses them to
	control the model, by sending Requests
	"""
	def __init__(self, evManager):
		self.evManager = evManager
		
		#List every event for which this object listens
		self.evManager.registerListener(self, gameStateEvents + inputEvents)
	def notify(self, event):
		if event.is_a(gameStateEvents):
			self.gameState = event
#	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	GameStatePrepareEvent
		elif self.gameState.is_a(GameStatePrepareEvent):
			if event.is_a(KeyboardInputEvent):
				pass
			elif event.is_a(MouseInputEvent):
				pass
			elif event.is_a(GameContInputEvent):
				pass
#	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	GameStateMainMenuEvent
		elif self.gameState.is_a(GameStateMainMenuEvent):
			if event.is_a(KeyboardInputEvent):
				pass
			elif event.is_a(MouseInputEvent):
				pass
			elif event.is_a(GameContInputEvent):
				pass	
#	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	GameStateGetControllersEvent
		elif self.gameState.is_a(GameStateGetControllersEvent):
			if event.is_a(KeyboardInputEvent):
				pass
			elif event.is_a(MouseInputEvent):
				pass
			elif event.is_a(GameContInputEvent):
				pass #Create Player()s here. send them to Game an Event
			
#	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	GameStatePlayEvent
		elif self.gameState.is_a(GameStatePlayEvent):
			if event.is_a(KeyboardInputEvent):
				direction = None
				if (event.value == 1):
					#print("event button :", event.button, "    dict: ", )
					if (event.button == keyboardMouseRef.PygameString_IntASCII["K_UP"]):
						direction = DIRECTION_UP
					elif (event.button == keyboardMouseRef.PygameString_IntASCII["K_DOWN"]):
						direction = DIRECTION_DOWN
					elif (event.button == keyboardMouseRef.PygameString_IntASCII["K_LEFT"]):
						direction = DIRECTION_LEFT
					elif (event.button == keyboardMouseRef.PygameString_IntASCII["K_RIGHT"]):
						direction = DIRECTION_RIGHT
					
				if direction in [0,1,2,3]:
					self.evManager.post(CharactorMoveRequest(direction))
	
			elif event.is_a(MouseInputEvent):
				pass
				#self.evManager.post(   )
#	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	GameStatePauseEvent
		elif self.gameState.is_a(GameStatePauseEvent):
			if event.is_a(KeyboardInputEvent):
				pass
			elif event.is_a(MouseInputEvent):
				pass
			elif event.is_a(GameContInputEvent):
				pass #Create Player()s here. send them to Game an Event
			
			elif event.is_a(GameContInputEvent):
				direction = None
				if event.joy == 0 and event.button == xboxContRef.xboxString_xboxInt["DPAD"]:
					if (event.value[1]== 1):
						direction = DIRECTION_UP
					elif (event.value[1]== -1):
						direction = DIRECTION_DOWN
					elif (event.value[0]== -1):
						direction = DIRECTION_LEFT
					elif (event.value[0]== 1):
						direction = DIRECTION_RIGHT
					
				if direction in [0,1,2,3]:
					self.evManager.post(CharactorMoveRequest(direction))
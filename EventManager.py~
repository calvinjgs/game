import pygame
from pygame.locals import *

from XboxContRef import *

#TODO Make this an error logging object or console
def debug(msg):
	print(msg)

class Event(object):
	def __init__(self):
		self.name = "Generic Event"

	def is_a(self, events):
		if type(events) == list:
			for event in events:
				if isinstance(self, event):
					return True
		else:
			if isinstance(self, events):
				return True

class TickEvent(Event):
	def __init__(self):
		self.name = "CPU Tick Event"

class QuitEvent(Event):
	def __init__(self):
		self.name = "Program Quit Event"

class MapBuiltEvent(Event):
	def __init__(self, levelMap):
		self.name = "Map Finished Building Event"
		self.levelMap = levelMap
#	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-		
class CreateCharactorSpriteEvent(Event):
	def __init__(self, entity, playerNumber):
		self.name = "Charactor Placement Event"
		self.entity = entity
		self.playerNumber = playerNumber

class CharactorMoveRequest(Event):
	def __init__(self, direction):
		self.name = "Charactor Move Request"
		self.direction = direction

class CharactorMoveEvent(Event):
	def __init__(self, entity):
		self.name = "Charactor Move Event"
		self.entity = entity

class SpriteStateChangeEvent(Event):
	def __init__(self, entity, state):
		self.name = "Sprite State Change Event"
		self.entity = entity
		self.state = state

#	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	INPUTS
class KeyboardInputEvent(Event):
	def __init__(self, button, value):
		self.name = "Keyboard Input Event"
		self.button = button		
		self.value = value

class MouseInputEvent(Event):
	def __init__(self, button, value):
		self.name = "Mouse Input Event"
		self.button = button
		self.value = value	

class GameContInputEvent(Event):
	def __init__(self, gamepadNumber, button, value):
		self.name = "Game Controller Input Event"
		self.gamepadNumber = gamepadNumber
		self.button = button
		self.value = value
inputEvents = [
	KeyboardInputEvent,
	MouseInputEvent,
	GameContInputEvent
]
#	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	GAME STATES
class GameStatePrepareEvent(Event):
	def __init__(self):
		self.name = 'Game State Prepare Event'
class GameStateOpenEvent(Event):
	def __init__(self):
		self.name = 'Game State Open Event'
class GameStateMainMenuEvent(Event):
	def __init__(self):
		self.name = 'Game State Main Menu Event'
class GameStateGetControllersEvent(Event):
	def __init__(self):
		self.name = 'Game State Get Controllers Event'
class GameStatePlayEvent(Event):
	def __init__(self, levelMap):
		self.name = 'Game State Play Event'
		self.levelMap = levelMap
class GameStatePauseEvent(Event):
	def __init__(self):
		self.name = 'Game State Pause Event'
gameStateEvents = [
	GameStatePrepareEvent,
	GameStateOpenEvent,
	GameStateMainMenuEvent,
	GameStateGetControllersEvent,
	GameStatePlayEvent,
	GameStatePauseEvent
]
#------------------------------------------------------------------------------
class EventManager:
	"""this object is responsible for coordinating most communication
	between the Model, View, and Controller."""
	def __init__(self):
		from weakref import WeakKeyDictionary
		self.allEventTypes = [
			TickEvent,
			QuitEvent,
			MapBuiltEvent,

			CreateCharactorSpriteEvent,
			CharactorMoveRequest,
			CharactorMoveEvent,
			SpriteStateChangeEvent,

			KeyboardInputEvent,
			MouseInputEvent,
			GameContInputEvent,

			GameStatePrepareEvent,
			GameStateOpenEvent,
			GameStateMainMenuEvent,
			GameStateGetControllersEvent,
			GameStatePlayEvent,
			GameStatePauseEvent
		]
		for e in self.allEventTypes:
			e.listeners = WeakKeyDictionary()
		#self.eventQueue = [] This was included in the original MVC tutorial. I don't see what it does..
	#----------------------------------------------------------------------
	def registerListener(self, listener, registeringObjectsEventTypes):
		for e in self.allEventTypes:
			for re in registeringObjectsEventTypes:
				if e == re:
					e.listeners[listener] = 1

	#----------------------------------------------------------------------
	def unregisterListener(self, listener, registerEventTypes):
		for e in self.allEventTypes:
			if listener in e.listeners:
				del e.listeners[ listener ]

	#----------------------------------------------------------------------
	def post(self, event):
		'''
		-	-	-	-	-	DEBUGING SECTION	-	-	-	-	-	-
		'''
		#if not event.is_a(TickEvent):

		if not event.is_a(TickEvent) and not event.is_a(inputEvents):
				debug("     Message: " + event.name)
		#if event.is_a(GameContInputEvent):
			#print(event.name, "     Player: ",event.joy," ",xboxContRef.xboxInt_moduleString[event.button],": ", event.value)
		'''
		-	-	-	-	-	NOTIFY()	-	-	-	-	-	-	-	-
		'''
		if hasattr(event, 'listeners'):
			for listener in event.listeners:
				#NOTE: If the weakref has died, it will be automatically removed, so we don't have to worry about it.
				listener.notify(event)

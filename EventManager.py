import pygame
from pygame.locals import *

from XboxContRef import *
from weakref import WeakKeyDictionary
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
TickEvent.listeners = WeakKeyDictionary()

class QuitEvent(Event):
	def __init__(self):
		self.name = "Program Quit Event"
QuitEvent.listeners = WeakKeyDictionary()

class MapBuiltEvent(Event):
	def __init__(self, levelMap):
		self.listeners = WeakKeyDictionary()
		self.name = "Map Built Event"
		self.levelMap = levelMap
MapBuiltEvent.listeners = WeakKeyDictionary()
#	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-		
class CreateCharactorViewEntityEvent(Event):
	def __init__(self, entity, playerNumber):
		self.listeners = WeakKeyDictionary()
		self.name = "Create Charactor ViewEntity Event"
		self.entity = entity
		self.playerNumber = playerNumber
CreateCharactorViewEntityEvent.listeners = WeakKeyDictionary()

class CharactorMoveRequest(Event):
	def __init__(self, direction):
		self.listeners = WeakKeyDictionary()
		self.name = "Charactor Move Request"
		self.direction = direction
CharactorMoveRequest.listeners = WeakKeyDictionary()

class CharactorMoveEvent(Event):
	def __init__(self, entity):
		self.listeners = WeakKeyDictionary()
		self.name = "Charactor Move Event"
		self.entity = entity
CharactorMoveEvent.listeners = WeakKeyDictionary()

class SpriteStateChangeEvent(Event):
	def __init__(self, entity, state):
		self.listeners = WeakKeyDictionary()
		self.name = "Sprite State Change Event"
		self.entity = entity
		self.state = state
SpriteStateChangeEvent.listeners = WeakKeyDictionary()

class ModelObjectMoveRequest(Event):
	def __init__(self, obj, from_pos, to_pos):
		self.listeners = WeakKeyDictionary()
		self.name = "Model Object Move Request"
		self.m_obj = m_obj
		self.from_pos
		self.to_pos
ModelObjectMoveRequest.listeners = WeakKeyDictionary()

class ModelObjectMoveEvent(Event):
	def __init__(self, obj, from_pos, to_pos):
		self.listeners = WeakKeyDictionary()
		self.name = "Model Object Move Event"
		self.m_obj = m_obj
		self.from_pos
		self.to_pos
ModelObjectMoveEvent.listeners = WeakKeyDictionary()

#	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	INPUTS
class KeyboardInputEvent(Event):
	def __init__(self, button, value):
		self.listeners = WeakKeyDictionary()
		self.name = "Keyboard Input Event"
		self.button = button		
		self.value = value
KeyboardInputEvent.listeners = WeakKeyDictionary()

class MouseInputEvent(Event):
	def __init__(self, button, value):
		self.listeners = WeakKeyDictionary()
		self.name = "Mouse Input Event"
		self.button = button
		self.value = value	
MouseInputEvent.listeners = WeakKeyDictionary()

class GameContInputEvent(Event):
	def __init__(self, gamepadNumber, button, value):
		self.listeners = WeakKeyDictionary()
		self.name = "Game Controller Input Event"
		self.gamepadNumber = gamepadNumber
		self.button = button
		self.value = value
GameContInputEvent.listeners = WeakKeyDictionary()

inputEvents = [
	KeyboardInputEvent,
	MouseInputEvent,
	GameContInputEvent
]
#	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	GAME STATES
class GameStatePrepareEvent(Event):
	listeners = WeakKeyDictionary()
	def __init__(self):
		self.name = 'Game State Prepare Event'
GameStatePrepareEvent.listeners = WeakKeyDictionary()

class GameStateOpenEvent(Event):
	listeners = WeakKeyDictionary()
	def __init__(self):
		self.name = 'Game State Open Event'
GameStateOpenEvent.listeners = WeakKeyDictionary()

class GameStateMainMenuEvent(Event):
	listeners = WeakKeyDictionary()
	def __init__(self):
		self.name = 'Game State Main Menu Event'
GameStateMainMenuEvent.listeners = WeakKeyDictionary()

class GameStateGetControllersEvent(Event):
	listeners = WeakKeyDictionary()
	def __init__(self):
		self.name = 'Game State Get Controllers Event'
GameStateGetControllersEvent.listeners = WeakKeyDictionary()

class GameStatePlayEvent(Event):
	listeners = WeakKeyDictionary()
	def __init__(self, levelMap):
		self.name = 'Game State Play Event'
		self.levelMap = levelMap
GameStatePlayEvent.listeners = WeakKeyDictionary()

class GameStatePauseEvent(Event):
	listeners = WeakKeyDictionary()
	def __init__(self):
		self.name = 'Game State Pause Event'
GameStatePauseEvent.listeners = WeakKeyDictionary()

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
        pass
		#self.eventQueue = [] This was included in the original MVC tutorial. I don't see what it does..
    #----------------------------------------------------------------------
    def registerListener(self, listener, registeringObjectsEventTypes):
        for re in registeringObjectsEventTypes:
            re.listeners[listener] = 1

    #----------------------------------------------------------------------
    def unregisterListener(self, listener, registerEventTypes):
        for re in registerEventTypes:
            if listener in re.listeners:
                del re.listeners[ listener ]

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

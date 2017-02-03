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
	listeners = WeakKeyDictionary()
	def __init__(self):
		self.name = "CPU Tick Event"

class QuitEvent(Event):
    listeners = WeakKeyDictionary()
    def __init__(self):
        self.name = "Program Quit Event"idle

class MapBuiltEvent(Event):
    listeners = WeakKeyDictionary()
    def __init__(self, levelMap):
        self.name = "Map Finished Building Event"
        self.levelMap = levelMap
#	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-		
class CreateCharactorViewEntityEvent(Event):
    listeners = WeakKeyDictionary()
    def __init__(self, entity, playerNumber):
        self.name = "Charactor Placement Event"
        self.entity = entity
        self.playerNumber = playerNumber

class CharactorMoveRequest(Event):
    listeners = WeakKeyDictionary()
    def __init__(self, direction):
        self.name = "Charactor Move Request"
        self.direction = direction

class CharactorMoveEvent(Event):
    listeners = WeakKeyDictionary()
    def __init__(self, entity):
        self.name = "Charactor Move Event"
        self.entity = entity

class SpriteStateChangeEvent(Event):
    listeners = WeakKeyDictionary()
    def __init__(self, entity, state):
        self.name = "Sprite State Change Event"
        self.entity = entity
        self.state = state
        



#	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	Jason's conflicting
class CreaureMoveRequest(Event):
    listeners = WeakKeyDictionary()
    def __init__(self, obj, deltaX, deltaY):
        self.name = "Creatures Move Request"
       
class CreaureMoveEvent(Event):
    listeners = WeakKeyDictionary()
    def __init__(self, obj, deltaX, deltaY):
        self.name = "Creatures Move Event"
        
#	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	Calvin's conflicting
class ModelObjectMoveRequest(Event):
    listeners = WeakKeyDictionary()
    def __init__(self, obj, from_pos, to_pos):
        self.name = "Model Object Move Request"
        self.m_obj = m_obj
        self.from_pos
        self.to_pos

class ModelObjectMoveEvent(Event):
    listeners = WeakKeyDictionary()
    def __init__(self, obj, from_pos, to_pos):
        self.name = "Model Object Move Event"
        self.m_obj = m_obj
        self.from_posg
        self.to_pos




#	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	INPUTS
class KeyboardInputEvent(Event):
    listeners = WeakKeyDictionary()
    def __init__(self, button, value):
        self.name = "Keyboard Input Event"
        self.button = button		
        self.value = value

class MouseInputEvent(Event):
    listeners = WeakKeyDictionary()
    def __init__(self, button, value):
        self.name = "Mouse Input Event"
        self.button = button
        self.value = value	

class GameContInputEvent(Event):
	listeners = WeakKeyDictionary()
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
    listeners = WeakKeyDictionary()
    def __init__(self):
        self.name = 'Game State Prepare Event'
class GameStateOpenEvent(Event):
    listeners = WeakKeyDictionary()
    def __init__(self):
        self.name = 'Game State Open Event'
class GameStateMainMenuEvent(Event):
    listeners = WeakKeyDictionary()
    def __init__(self):
        self.name = 'Game State Main Menu Event'
class GameStateGetControllersEvent(Event):
    listeners = WeakKeyDictionary()
    def __init__(self):
        self.name = 'Game State Get Controllers Event'
class GameStatePlayEvent(Event):
    listeners = WeakKeyDictionary()
    def __init__(self, levelMap):
        self.name = 'Game State Play Event'
        self.levelMap = levelMap
class GameStatePauseEvent(Event):
    listeners = WeakKeyDictionary()
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

#import pygame
#from pygame.locals import *
import XboxControllerModule
from EventManager import *
from XboxContRef import *


class XboxController:
	"""XboxController takes creates callbacks for each button and 
	uses them to control the model, by sending Requests
	"""
	def __init__(self, evManager):
		self.evManager = evManager
		
		#List every event for which this object listens
		self.evManager.registerListener(self,[TickEvent])
		self.xboxCont = XboxControllerModule.XboxController(
			controllerCallBack = None,
			joystickNo = 0,
			deadzone = 0.1,
			scale = 1,
			invertYAxis = False)
		
		moduleString_moduleButtonReference = {
			"LTHUMBX": self.xboxCont.XboxControls.LTHUMBX,
			"LTHUMBY": self.xboxCont.XboxControls.LTHUMBY,
			"RTHUMBX": self.xboxCont.XboxControls.RTHUMBX,
			"RTHUMBY": self.xboxCont.XboxControls.RTHUMBY,
			"TRIGGER": self.xboxCont.XboxControls.RTRIGGER,
			"A": self.xboxCont.XboxControls.A,
			"B": self.xboxCont.XboxControls.B,
			"X": self.xboxCont.XboxControls.X,
			"Y": self.xboxCont.XboxControls.Y,
			"LB": self.xboxCont.XboxControls.LB,
			"RB": self.xboxCont.XboxControls.RB,
			"BACK": self.xboxCont.XboxControls.BACK,
			"START": self.xboxCont.XboxControls.START,
			"XBOX": self.xboxCont.XboxControls.XBOX,
			"LEFTTHUMB": self.xboxCont.XboxControls.LEFTTHUMB,
			"RIGHTTHUMB": self.xboxCont.XboxControls.RIGHTTHUMB,
			"DPAD": self.xboxCont.XboxControls.DPAD
		}

		for button in xboxContRef.moduleString_xboxInt:
			def callback(value):
				self.evManager.post(GameControllerInputEvent(button, value))
				#print(button,"\tButton number: ",xboxContRef.moduleString_xboxInt, "\tValue: ", value)
					
			self.xboxCont.setupControlCallback(
				moduleString_moduleButtonReference[button],
				callback)
	#----------------------------------------------------------------------
	def notify(self, event):
		if event.is_a(QuitEvent):
			self.xboxCont.stop()
			
	#TOTRY if callbacks eat up processing, use...
		#elif event.is_a(TickEvent ):
			#self.controller.LTHUMBX
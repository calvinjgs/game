'''
Dictionaries and Arrays between
	xboxString,
	xboxInt,
	pygameAxisInt,
	pygameButtonInt,
	moduleButtonReference
'''
#TODEL import XboxControllerModule

class XboxContRef:
	def __init__(self):
		self.pygameAxisInt_xboxInt = [
			0,
			1,
			4,
			3,
			2
		]
		
		self.pygameButtonInt_xboxInt = [
			5,
			6,
			7,
			8,
			9,
			10,
			11,
			12,
			14,
			15,
			13
		]
		
		self.pygameAxisInt_xboxString = [
			"LTHUMBX",
			"LTHUMBY",
			"RTRIGGER",
			"RTHUMBX",
			"RTHUMBY"
		]
		
		self.pygameButtonInt_xboxString = [
			"A",
			"B",
			"X",
			"Y",
			"LB",
			"RB",
			"BACK",
			"START",
			"LEFTTHUMB",
			"RIGHTTHUMB",
			"XBOX"
		]
		
		self.xboxInt_xboxString = [
			"LTHUMBX",
			"LTHUMBY",
			"RTHUMBX",
			"RTHUMBY",
			"RTRIGGER",
			"A",
			"B",
			"X",
			"Y",
			"LB",
			"RB",
			"BACK",
			"START",
			"XBOX",
			"LEFTTHUMB",
			"RIGHTTHUMB",
			"DPAD"
		]

		self.xboxString_pygameInt = {
			"LTHUMBX": 0,
			"LTHUMBY": 1,
			"TRIGGER": 2,
			"RTHUMBY": 3,
			"RTHUMBX": 4,
		}

		self.xboxString_pygameButtonInt = {
			"A": 0,
			"B": 1,
			"X": 2,
			"Y": 3,
			"LB": 4,
			"RB": 5,
			"BACK": 6,
			"START": 7,
			"LEFTTHUMB": 8,
			"RIGHTTHUMB": 9,
			"XBOX": 10
		}

		self.xboxString_xboxInt = {
			"LTHUMBX": 0,
			"LTHUMBY": 1,
			"RTHUMBX": 2,
			"RTHUMBY": 3,
			"TRIGGER": 4,
			"A": 5,
			"B": 6,
			"X": 7,
			"Y": 8,
			"LB": 9,
			"RB": 10,
			"BACK": 11,
			"START": 12,
			"XBOX": 13,
			"LEFTTHUMB": 14,
			"RIGHTTHUMB": 15,
			"DPAD": 16
		}
		
		self.int_xboxString = [
			"LTHUMBX",
			"LTHUMBY",
			"RTHUMBX",
			"RTHUMBY",
			"TRIGGER",
			"A",
			"B",
			"X",
			"Y",
			"LB",
			"RB",
			"BACK",
			"START",
			"XBOX",
			"LEFTTHUMB",
			"RIGHTTHUMB",
			"DPAD",
		]
		
		#TODEL	See XboxController.py for this reference dictionary because it needs to refer to the instance (not class) of XboxCont.
		#self.xboxString_moduleButtonReference = {
			#"LTHUMBX": xboxCont.XboxControls.LTHUMBX,	...

xboxContRef = XboxContRef()
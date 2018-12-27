from enum import Enum
model = Enum('car','lorry')
class car:
	def __init__(self):
		self.model=model('car')
		self.carryCapicity=0
		self.pMaxChargePower=0
		self.wBatteryCapicity=0
		self.pEnablingEfficacy=0
		self.wLeft=0
		

class node:
	def __init__(self, ** omega):
		self.nQuickCharger = 0
		self.etaQuickCharger = 0
		self.nSlowCharger = 0
		self.etaSlowCharger = 0
		self.p = 0
		self.pLog = []
		self.sigma = 0
		self.omega = 0
		if omega:
			self.omega = omega

	def calcP(self):
		sum = 0
		mult = 1
		multsum = 0
		multseed = 0.95
		for i in self.pLog:
			sum += i*mult
			multsum += mult
			mult = mult*multseed
		return sum/multsum

if __name__=='__main__':
	a=node()
	a.calcP()
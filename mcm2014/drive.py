class car:
	def __init__(self):
		self.speed = 0	# m/s
		self.length = 0	# m
		self.size = None # 车型 [0:桥车 1：大客、货运]（影响限速）
		self.capcity = 0	#等效载荷（客运；人/货运：吨）（载荷由公式给出）
		self.MAX_SPEED =0#最大速度 m/s
		self.prior = 5 # 优先级

	def saftyDistence(self):	#安全跟车距离 m
		if (self.speed>=100):
			return 100
		elif (self.speed>=50):
			return self.speed
		elif (self.speed>=10):
			return 50
		else:
			return 5
	def load(** key):
		if (speed in key):
			self.speed = speed
		elif(length in key):
			self.length = length
		elif(size in key):
			pass
		pass
		

	def speedConv(self):
		return self.speed*3.6
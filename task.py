class Car:
	"""docstring for Car"""
	def __init__(self, wheel_angle = 0, speed = 0):
		self.wheel_angle = wheel_angle
		self.speed = speed
		self.engineStatus = False
		self.seconds = 0
	def loop(self):
		while self.seconds < 200:
			self.seconds += 1
			self.speed -= 1
			self.wheel_angle = -1
			print("speed = {}".format(self.speed))
			print("wheel_angle = {}".format(self.wheel_angle))
	def startEngine(self, time):
		if self.engineStatus == False:
			print("WRRRR (on {}sec)".format(time))
		else:
			print("<engine is already running>")
	def stopEngine(self, time):
		if self.engineStatus == False:
			print("<engine is not running>".format(time))
		else:
			print("UUUuum (on {}sec)".format(time))
	def obsticleHandler(self, time):
		pass
	def act(self, event):
		time = event[1]
		event = event[0]
		if event == 'stat the engine' :
			self.startEngine(time)
		elif event == 'stop the engine' :
			self.stopEngine(time)
		elif event == 'obsticle' :
			self.obsticleHandler(time)


car1 = Car()
car1.act(('stat the engine', 10))
car1.act(('stop the engine', 10))

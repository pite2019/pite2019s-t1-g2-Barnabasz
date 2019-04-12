#!/usr/bin/env python3
from time import sleep
from statistics import mean
from types import FunctionType
import keyboard

class Car(object):
	"""docstring forP Car"""
	def __init__(self, speed = 0, wheel_angle = 0):
		super(Car, self).__init__()
		self.speed = speed
		self.wheel_angle = wheel_angle
		self.stop = False
		self.time = 0
		self.events = {}

	def spedEndAngle(self) :
		if self.speed  > 4 :
			self.speed -= 5
		else:
			self.speed = 0
		if self.wheel_angle > 4 :q
			self.wheel_angle -= 5
		elif self.wheel_angle < -4 :
			self.wheel_angle -= 5
		else :
			self.wheel_angle = 0
	
	def timer(self):
		for _ in range(100):
			if keyboard.is_pressed('q'):
				return False
			elif keyboard.is_pressed('a'):
				self.addEvent()
			sleep(0.01)
		else:
			self.time+=1
	def turnLeft(self) :
		self.wheel_angle += -50
	def turnRight(self) :
		self.wheel_angle += +50
	def startEngine(self) :
		if self.engine == False :
			print("Wrmmmmm")
			self.engine = False
		else :
			print("Engine is already running")
	def stopEngine(self) :
		if self.engine == True :
			print("YYyyyy")
			self.engine = False
		else :
			print("Engine is not running")
	def speedUP(self):
		if self.engine == True :
			self.speed += 50
		else :
			print("Engine is not running")
	def printEvent(self):
		if self.time in self.events.keys() :
			event = self.events[self.time]
			print("time: {}, speed: {}, wheel angle: {}, event: {}".format(self.time, self.speed, self.wheel_angle, event))
			if event == "turnLeft" :
				self.turnLeft()
			elif event == "turnRight":
				self.turnRight()
			elif event == "startEngine":
				self.startEngine()
			elif event == "stopEngine" :
				self.stopEngine()
		else :
			print("time: {}, speed: {}, wheel angle: {}".format(self.time, self.speed, self.wheel_angle))

	def infiniteLoop(self):
		while not self.stop:
			if keyboard.is_pressed('q'):
				break
			self.printEvent()
			self.spedEndAngle()
			self.timer()


	def addEvent(self, event = False):
		sleep(0.1)
		if event == False :
			nazwa = input("podaj nazwę eventu:")
			czas = input("podaj opuźnienie:")
			self.events = {self.time+int(czas):nazwa}
car1 = Car(50, 32)
car1.addEvent(("coś", 1))
car1.infiniteLoop()

import sys, random, argparse
import numpy as np
import math
import turtle
import random
from PIL import Image
from datetime import datetime
from fractions import gcd

#Draws Spirograph
class Spiro:
	#constructor
	def __init__(self, xc, yc, col, R, r, l):
		#create turtle object
		self.t = turtle.Turtle()
		#Set cursor shape
		self.t.shape('turtle')
		#set step in degrees
		self.step = 5
		#set the drawing complete flag
		self.drawingComplete = False

		#set parameters
		self.setparams(xc, yc, col, R, r, l)

		#initialize the drawing
		self.restart()

	#set parameters
	def setparams(self, xc, yc, col, R, r, l):
		#Spiro parameters
		self.xc = xc
		self.yc = yc
		self.R = R
		self.r = r
		self.l = l
		self.col = col
		#reduce r/R to smallest form using GCD
		gcdVal = gcd(self.r, self.R)
		self.nRot = self.r//gcdVal
		#get ratio of radii
		self.k = r/float(R)
		#set color
		self.t.color(*col)
		#store current angle
		self.a = 0

	#restart drawing
	def restart(self):
		#set flag
		self.drawingComplete = False
		#show turtle
		self.t.showturtle()
		#go to first point
		self.t.up()
		R, k, l = self.R, self.k, self.l
		a = 0.0
		x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
		y = R*((1-k)*math.sin(a) + l*k*math.sin((1-k)*a/k))
		


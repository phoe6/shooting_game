# -*- coding: utf-8 -*-
import sys, math
import pygame
from pygame.key import *
from pygame.locals import *
from .base_char import BaseCharactor

class PlayerBall(BaseCharactor):

	def __init__(self, w, h, move_x, move_y):
		super().__init__(w, h, move_x, move_y)


	def update(self):
		if self.rect.y+self.image.get_height() < 0:
			self.kill()
		else:
			self.rect.y -= 10


class EnemyBall(PlayerBall):

	def __init__(self, disp, w, h, move_x, move_y):
		super().__init__(w, h, move_x, move_y)
		self.disp = disp


	def update(self):
		if self.rect.y > self.disp.get_height():
			self.kill()
		else:
			self.rect.y += 10


class BossBall(EnemyBall):

	def __init__(self, disp, w, h, move_x, move_y, angle):
		super().__init__(disp, w, h, move_x, move_y)
		self.x_point = 0
		self.angle = angle
		self.slope = math.tan(math.radians(angle)) # tan


	def update(self):
		if 0 <= self.angle <=89:
			self.x_point += 0.1
			self.rect.x += self.x_point # cos
			self.rect.y -= self.slope * self.x_point # sin

		elif 91 <= self.angle <=179:
			self.x_point -= 0.1
			self.rect.x += self.x_point
			self.rect.y -= self.slope * self.x_point

		elif 181 <= self.angle <=269:
			self.x_point += 0.1
			self.rect.x -= self.x_point
			self.rect.y += self.slope * self.x_point
			
		elif 271 <= self.angle <=359:
			self.x_point -= 0.1
			self.rect.x -= self.x_point
			self.rect.y += self.slope * self.x_point
		
		if self.disp.get_height() < self.rect.y or self.rect.y < 0 or self.disp.get_width() < self.rect.x or self.rect.x < 0:
			self.kill()


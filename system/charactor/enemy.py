# -*- coding: utf-8 -*-
import random
import pygame
from .base_char import BaseCharactor
from .ball import *

class Enemy(BaseCharactor):
	
	prob_ball = 0.008
	move_limit = 100

	def __init__(self, disp, w, h, move_x, move_y):
		super().__init__(w, h, move_x, move_y)
		self.disp = disp
		self.move_flag = False
		self.limit_left = self.rect.x
		self.limit_right = self.limit_left + self.move_limit


	def update(self):
		pos = self.rect.x
		if pos <= self.limit_left:
			self.move_flag = False
		elif self.limit_right <= pos:
			self.move_flag = True
		if self.move_flag == False:
			self.rect.x += 2
		else:
			self.rect.x -= 2

		if random.random() < self.prob_ball:
			eball = EnemyBall(self.disp, 2, 15, self.rect.x+self.image.get_width()/2, self.rect.y+15)


class Boss(Enemy):

	prob_ball = None

	def __init__(self, disp, w, h, move_x, move_y, speed):
		super().__init__(disp, w, h, move_x, move_y)
		self.angle = 0
		self.speed = speed


	def image_rotation(self):
		after_image = pygame.transform.rotate(self.image, self.angle)
		offset_x = (self.image.get_width()-after_image.get_width()) / 2
		offset_y = (self.image.get_height()-after_image.get_height()) / 2
		self.disp.blit(after_image, (self.rect.x+offset_x, self.rect.y+offset_y))
		self.angle += self.speed


	def update(self):
		if self.angle <= 360:
			self.image_rotation()
		else:
			self.angle = 0
		if Boss.prob_ball < random.random():
			bball = BossBall(self.disp, 3, 3, self.rect.x+self.image.get_width()/2, self.rect.y+self.image.get_height()/2, random.randint(180, 359))


class StartAnimation(Boss):

	def __init__(self, disp, w, h, move_x, move_y, speed):
		super().__init__(disp, w, h, move_x, move_y, speed)

	def update(self):
		self.image_rotation()


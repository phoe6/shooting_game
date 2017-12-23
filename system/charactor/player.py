# -*- coding: utf-8 -*-
import sys
import pygame
from pygame.key import *
from pygame.locals import *
from .base_char import BaseCharactor
from .ball import PlayerBall

'''
プレイヤーのクラス
横に移動するため、画面からはみ出ないようにする。
'''
class Player(BaseCharactor):

	reload_time = 50

	def __init__(self, disp, w, h, move_x, move_y):
		super().__init__(w, h, move_x, move_y)
		self.disp = disp
		self.reload_timer = self.reload_time


	def update(self):
		self.disp_protrude()


	def disp_protrude(self):
		img_w = self.image.get_width()
		disp_w = self.disp.get_width()
		for px in range(15):
			if 0 != self.rect.x and self.rect.x+img_w != disp_w:
				self.char_move()
			else:
				if self.rect.x == 0:
					self.char_move(True)
				else:
					self.char_move(False)


	def char_move(self, flag=None):
		key = pygame.key.get_pressed()
		if key[K_LEFT] and (flag == False or flag is None):
			self.rect.x -= 1
		if key[K_RIGHT] and (flag == True or flag is None):
			self.rect.x += 1
		if key[K_UP]:
			if self.reload_timer == 0:
				pball = PlayerBall(2, 15, self.rect.x+self.image.get_width()/2, self.rect.y-15)
				self.reload_timer = self.reload_time
			else:
				self.reload_timer -= 1


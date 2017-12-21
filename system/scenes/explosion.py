# -*- coding: utf-8 -*-
import pygame, sys

'''
エクスプロージョン！！
'''

class Explosion(pygame.sprite.Sprite):

	frame = 0
	animcycle = 2

	def __init__(self, pos):
		super().__init__(self.containers)
		self.image = self.images[0]
		self.rect = self.image.get_rect()
		self.rect.center = pos
		self.max_frame = len(self.images) * self.animcycle


	def update(self):
		self.image = self.images[self.frame // self.animcycle]
		self.frame += 1
		if self.frame == self.max_frame:
			self.kill()

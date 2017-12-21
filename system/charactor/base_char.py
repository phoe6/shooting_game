# -*- coding: utf-8 -*-
import pygame

class BaseCharactor(pygame.sprite.Sprite):
	
	def __init__(self, w, h, move_x, move_y):
		super().__init__(self.containers)
		self.image = pygame.transform.scale(self.path, (w, h))
		self.rect = self.image.get_rect()
		self.rect.x = move_x
		self.rect.y = move_y

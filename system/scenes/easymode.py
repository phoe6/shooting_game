# -*- coding: utf-8 -*-
import pygame
from ..charactor.player import *
from ..charactor.enemy import *
from ..charactor.ball import *

'''
イージー用のクラス
sceneモジュールで使う。
'''
class EasyMode:

	def __init__(self, screen): 
		self.screen = screen


	def game_init(self):
		self.load_image()
		self.make_group()
		self.contain_group()
		self.char_draw()


	def make_group(self):
		self.all = pygame.sprite.RenderUpdates()
		self.pball_group = pygame.sprite.Group()
		self.enemy_group = pygame.sprite.Group()
		self.eball_group = pygame.sprite.Group()


	def contain_group(self):
		Player.containers = self.all
		PlayerBall.containers = self.all, self.pball_group
		Enemy.containers = self.all, self.enemy_group
		EnemyBall.containers = self.all, self.eball_group


	def load_image(self):
		Player.path = pygame.image.load('./images/player.png')
		PlayerBall.path = pygame.image.load('./images/player_ball.png')
		Enemy.path = pygame.image.load('./images/enemy.png')
		EnemyBall.path = pygame.image.load('./images/enemy_ball.png')


	def char_draw(self):
		self.player = Player(self.screen, 100, 20, 350, 470)
		for i in range(0, 50):
			x = 20 + (i % 10) * 70
			y = 20 + (i // 10) * 40
			Enemy(self.screen, 30, 30, x, y)


# -*- coding: utf-8 -*-
import pygame
from ..charactor.player import *
from ..charactor.enemy import *
from ..charactor.ball import *

class NormalMode:

	def __init__(self, screen): 
		self.screen = screen


	def game_init(self):
		self.load_image()
		self.make_group()
		self.contain_group()
		self.char_draw()
		Boss.prob_ball = 0.84


	def make_group(self):
		self.all = pygame.sprite.RenderUpdates()
		self.pball_group = pygame.sprite.Group()
		self.boss_group = pygame.sprite.Group()
		self.bball_group = pygame.sprite.Group()


	def contain_group(self):
		Player.containers = self.all
		PlayerBall.containers = self.all, self.pball_group
		Boss.containers = self.all, self.boss_group
		BossBall.containers = self.all, self.bball_group


	def load_image(self):
		Player.path = pygame.image.load('./images/player.png')
		PlayerBall.path = pygame.image.load('./images/player_ball.png')
		Boss.path = pygame.image.load('./images/boss.png')
		BossBall.path = pygame.image.load('./images/enemy_ball.png')


	def char_draw(self):
		self.player = Player(self.screen, 100, 20, 350, 470)
		Boss(self.screen, 50, 50, self.screen.get_width()/8, self.screen.get_height()/5, 3)
		Boss(self.screen, 150, 150, self.screen.get_width()/3, self.screen.get_height()/4, 3)
		Boss(self.screen, 60, 60, self.screen.get_width()/1.3, self.screen.get_height()/1/2, 3)
		Boss(self.screen, 100, 100, self.screen.get_width()/1.2, self.screen.get_height()/4.5, 3)


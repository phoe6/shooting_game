# -*- coding: utf-8 -*-
import pygame
from ..charactor.player import *
from ..charactor.enemy import *
from ..charactor.ball import *
from .easymode import EasyMode
from .normalmode import NormalMode
from .hardmode import HardMode
from .explosion import Explosion
from .collision import Collision

START, PLAY, GAMEOVER, CLEAR = (0, 1, 2, 3)
EASY, NORMAL, HARD = (0, 1, 2)

class Scene:

	def __init__(self, screen):
		self.screen = screen
		self.easy_mode = EasyMode(screen)
		self.normal_mode = NormalMode(screen)
		self.hard_mode = HardMode(screen)
		self.all = pygame.sprite.RenderUpdates()
		StartAnimation.containers = self.all
		StartAnimation.path = pygame.image.load('./images/boss.png')
		Explosion.images = Collision.split_image('./images/bomb.png', 8, 2)
		self.animation_init()


	def animation_init(self):
		StartAnimation(self.screen, 60, 60, self.screen.get_width()/8, self.screen.get_height()/5, 3)
		StartAnimation(self.screen, 120, 120, self.screen.get_width()/8, self.screen.get_height()/1.5, 6)
		StartAnimation(self.screen, 200, 200, self.screen.get_width()/1.2, self.screen.get_height()/3, 5)


	def draw(self):
		self.screen.fill((255, 255, 255))
		title_font = pygame.font.SysFont(None, 50)

		if Scene.game_status == START:	
			title = title_font.render('INVADER GAME', False, (0, 0, 200))
			self.screen.blit(title, ((self.screen.get_width())/3, 100))
			mode_fnt = pygame.font.SysFont(None, 15)
			easy = title_font.render('>> easy (Press e)', False, (200, 0, 0))
			normal = title_font.render('>> normal (Press n)', False, (200, 0, 0))
			hard = title_font.render('>> hard (Press h)', False, (200, 0, 0))
			self.screen.blit(easy, ((self.screen.get_width())/3, 170))
			self.screen.blit(normal, ((self.screen.get_width())/3, 220))
			self.screen.blit(hard, ((self.screen.get_width())/3, 270))
			self.all.update()
			self.mode_change()

		elif Scene.game_status == PLAY:
			if Scene.game_mode == EASY:
				self.easy_mode.all.draw(self.screen)
				
			elif Scene.game_mode == NORMAL:
				self.normal_mode.all.draw(self.screen)
				
			elif Scene.game_mode == HARD:
				self.hard_mode.all.draw(self.screen)
				

		elif Scene.game_status == GAMEOVER:
			title = title_font.render('GAMEOVER', False, (0, 0, 200))
			self.screen.blit(title, ((self.screen.get_width())/2.65, 100))
			retry_font = pygame.font.SysFont(None, 50)
			retry = retry_font.render('>> continue ? (Press c)', False, (200, 0, 0))
			self.screen.blit(retry, ((self.screen.get_width())/3.5, 200))
			self.all.update()
			self.game_continue()

		elif Scene.game_status == CLEAR:
			title = title_font.render('CLEAR', False, (0, 0, 200))
			self.screen.blit(title, ((self.screen.get_width())/2.65, 100))
			retry_font = pygame.font.SysFont(None, 50)
			retry = retry_font.render('>> continue ? (Press c)', False, (200, 0, 0))
			self.screen.blit(retry, ((self.screen.get_width())/3.5, 200))
			self.all.update()
			self.game_continue()


	def mode_change(self):
		key = pygame.key.get_pressed()

		if key[K_e] or key[K_n] or key[K_h]:
			Scene.game_status = PLAY

		if key[K_e]:
			Scene.game_mode = EASY
			self.easy_mode.game_init()
			Explosion.containers = self.easy_mode.all

		elif key[K_n]:
			Scene.game_mode = NORMAL
			self.normal_mode.game_init()
			Explosion.containers = self.normal_mode.all
			
		elif key[K_h]:
			Scene.game_mode = HARD
			self.hard_mode.game_init()
			Explosion.containers = self.hard_mode.all


	def game_exit(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()


	def game_continue(self):
		key = pygame.key.get_pressed()
		if key[K_c]:
			Scene.game_status = START
			Scene.game_mode = None
			self.exp_flag = False


	def update(self):
		if Scene.game_status == PLAY:
			if Scene.game_mode == EASY:
				self.easy_mode.all.update()
				Collision.coll_easy(self.easy_mode.player, self.easy_mode.enemy_group, self.easy_mode.pball_group, self.easy_mode.eball_group)
				if len(self.easy_mode.enemy_group) == 0: 
					Scene.game_status = CLEAR
					Scene.game_mode = None

			elif Scene.game_mode == NORMAL:
				self.normal_mode.all.update()
				Collision.coll_normal(self.normal_mode.player, self.normal_mode.boss_group, self.normal_mode.pball_group, self.normal_mode.bball_group)
				if len(self.normal_mode.boss_group) == 0: 
					Scene.game_status = CLEAR
					Scene.game_mode = None

			elif Scene.game_mode == HARD:
				self.hard_mode.all.update()
				Collision.coll_hard(self.hard_mode.player, self.hard_mode.enemy_group, self.hard_mode.boss_group, self.hard_mode.pball_group, self.hard_mode.eball_group, self.hard_mode.bball_group)
				if len(self.hard_mode.boss_group) == len(self.hard_mode.enemy_group) == 0: 
					Scene.game_status = CLEAR
					Scene.game_mode = None


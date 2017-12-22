# -*- coding: utf-8 -*-
import pygame, sys
from pygame.locals import *
from . import scene, explosion

START, PLAY, GAMEOVER = (0, 1, 2)

class Collision:

	exp_action = lambda obj: list(map(lambda e: explosion.Explosion(e.rect.center), obj))

	@staticmethod
	def coll_easy(player, enemy, pball, eball):
		player_collided = pygame.sprite.spritecollide(player, eball, True)
		enemy_collided = pygame.sprite.groupcollide(enemy, pball, True, True)
		ball_collided = pygame.sprite.groupcollide(pball, eball, True, True)

		Collision.exp_action(enemy_collided)

		if player_collided:
			player.kill()
			scene.Scene.game_status = GAMEOVER
		
		

	@staticmethod
	def coll_normal(player, boss, pball, bball):
		player_collided = pygame.sprite.spritecollide(player, bball, True)
		boss_collided = pygame.sprite.groupcollide(boss, pball, True, True)
		ball_collided = pygame.sprite.groupcollide(pball, bball, True, True)

		Collision.exp_action(boss_collided)

		if player_collided:
			player.kill()
			scene.Scene.game_status = GAMEOVER


	@staticmethod
	def coll_hard(player, enemy, boss, pball, eball, bball):
		player_boss_collided = pygame.sprite.spritecollide(player, bball, True)
		boss_collided = pygame.sprite.groupcollide(boss, pball, True, True)
		bball_collided = pygame.sprite.groupcollide(pball, bball, True, True)
		player_enemy_collided = pygame.sprite.spritecollide(player, eball, True)
		enemy_collided = pygame.sprite.groupcollide(enemy, pball, True, True)
		ball_collided = pygame.sprite.groupcollide(pball, eball, True, True)

		Collision.exp_action(boss_collided)
		Collision.exp_action(enemy_collided)

		if player_boss_collided or player_enemy_collided:
			player.kill()
			scene.Scene.game_status = GAMEOVER


	@staticmethod
	def split_image(image, sp_wnum, sp_hnum):
		image_list = []
		image = pygame.image.load(image).convert()
		w = image.get_width()
		h = image.get_height()
		sp_w = w // sp_wnum
		sp_h = h // sp_hnum

		for i in range(sp_hnum):
			for j in range(0, w, sp_w):
				surface = pygame.Surface((sp_w, sp_h))
				surface.blit(image, (0, 0), (j, i*sp_h, sp_w, sp_h))
				surface.set_colorkey(surface.get_at((0, 0)), RLEACCEL)
				surface.convert()
				image_list.append(surface)
		return image_list


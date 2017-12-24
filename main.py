# -*- coding: utf-8 -*-
import sys, pygame
import system.scenes.scene as scene
from system.state import *

'''
Sceneクラスのインスタンスをつくって、ごにょごにょするだけ。
'''
if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Invaders game')
    screen = pygame.display.set_mode((800, 500))
    scene.Scene.game_status = START
    game = scene.Scene(screen)

    while True:
        game.draw()
        game.update()
        game.game_exit()
        pygame.display.update()
        pygame.time.wait(30)

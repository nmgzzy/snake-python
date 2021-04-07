import pygame
from pygame.sprite import Sprite
import copy

class Snake(Sprite):
	
	def __init__(self, ai_settings, screen):
		'''初始化飞船并设置初始位置'''
		super(Snake, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		# 加载飞船图像并获取其外接矩形
		self.head_image = pygame.image.load('img/head1.png')
		self.body_image = pygame.image.load('img/body1.png')
		self.body_rect = self.body_image.get_rect()
		self.screen_rect = screen.get_rect()

		# 移动标志
		self.moving_direction = 'R'
		self.body = []
		self.length = 1
		self.body.append(Node(0, 0))
		self.body_rect.x = self.body[0].x * self.ai_settings.node_size
		self.body_rect.y = self.body[0].y * self.ai_settings.node_size
		self.tail = Node(self.body[0].x, self.body[0].y)
		self.hit = False

	def update(self):
		'''根据移动标志调整飞船位置'''
		self.tail = copy.copy(self.body[-1])
		for i in range(self.length - 1, 0, -1):
			self.body[i] = copy.copy(self.body[i-1])
		if self.moving_direction == 'L':
			self.body[0].x = (self.body[0].x - 1) % self.ai_settings.grid_width
		elif self.moving_direction == 'R':
			self.body[0].x = (self.body[0].x + 1) % self.ai_settings.grid_width
		elif self.moving_direction == 'U':
			self.body[0].y = (self.body[0].y - 1) % self.ai_settings.grid_height
		elif self.moving_direction == 'D':
			self.body[0].y = (self.body[0].y + 1) % self.ai_settings.grid_height
		for i in range(1,self.length):
			if self.body[0].x == self.body[i].x and self.body[0].y == self.body[i].y:
				self.hit = True

	def grow(self):
		self.body.append(self.tail)
		self.length += 1

	def blitme(self):
		'''在指定位置绘制飞船'''
		for i in range(1, self.length):
			self.body_rect.x = self.body[i].x * self.ai_settings.node_size
			self.body_rect.y = self.body[i].y * self.ai_settings.node_size
			self.screen.blit(self.body_image, self.body_rect)
		self.body_rect.x = self.body[0].x * self.ai_settings.node_size
		self.body_rect.y = self.body[0].y * self.ai_settings.node_size
		self.screen.blit(self.head_image, self.body_rect)
		
	def reset(self):
		self.moving_direction = 'R'
		self.body = []
		self.length = 1
		self.body.append(Node(0, 0))
		self.body_rect.x = self.body[0].x * self.ai_settings.node_size
		self.body_rect.y = self.body[0].y * self.ai_settings.node_size
		self.tail = Node(self.body[0].x, self.body[0].y)
		self.hit = False


class Node:
	def __init__(self, x, y):
		self.x = x
		self.y = y
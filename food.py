import pygame
from pygame.sprite import Sprite
import random
from snake import Node

class Food(Sprite):
	"""表示单个食物的类"""
	def __init__(self, ai_settings, screen, snake):
		super(Food, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		self.snake = snake

		# 加载食物图像，设置rect属性
		self.image = pygame.image.load('img/food1.png')
		self.rect = self.image.get_rect()

		# 存储食物位置
		self.place = Node(0,0)
		self.place.x = random.randint(0,self.ai_settings.grid_width-1)
		self.place.y = random.randint(0,self.ai_settings.grid_height-1)
		self.rect.x = self.place.x * self.ai_settings.node_size
		self.rect.y = self.place.y * self.ai_settings.node_size

	def blitme(self):
		'''在指定位置绘制食物'''
		self.screen.blit(self.image, self.rect)

	def update(self):
		self.place.x = random.randint(0,self.ai_settings.grid_width-1)
		self.place.y = random.randint(0,self.ai_settings.grid_height-1)
		while True:
			if self.place in self.snake.body:
				self.x = random.randint(0,self.ai_settings.grid_width-1)
				self.y = random.randint(0,self.ai_settings.grid_height-1)
			else:
				break
		self.rect.x = self.place.x * self.ai_settings.node_size
		self.rect.y = self.place.y * self.ai_settings.node_size

	# def check_edges(self):
	# 	'''如果食物位于屏幕边缘，返回True'''
	# 	screen_rect = self.screen.get_rect()
	# 	if self.rect.right >= screen_rect.right:
	# 		return True
	# 	elif self.rect.left <= screen_rect.left:
	# 		return True
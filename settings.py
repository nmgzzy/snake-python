class Settings():
	"""存储此游戏所有设置的类"""
	def __init__(self):
		'''初始化游戏静态设置'''
		self.grid_width = 40
		self.grid_height = 30
		self.node_size = 20

		# 屏幕设置
		self.screen_width = self.grid_width * self.node_size
		self.screen_height = self.grid_height * self.node_size
		self.bg_color = (10,10,10)
		
		# 游戏加速度
		self.speedup_scale = 1
		self.score_scale = 1.5

		self.initialize_dynamic_settings()
		
	def initialize_dynamic_settings(self):
		'''初始化游戏并随游戏变化的设置'''
		self.snake_speed_factor = 2
		# 记分
		self.alien_points = 10

	def increase_speed(self):
		'''提高游戏速度设置和外星人点数'''
		self.snake_speed_factor *= self.speedup_scale

		self.alien_points = int(self.alien_points*self.score_scale)
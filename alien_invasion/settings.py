class Settings():
	"""存储此游戏所有设置的类"""
	def __init__(self):
		'''初始化游戏静态设置'''
		# 屏幕设置
		self.screen_width = 1200
		self.screen_height = 750
		self.bg_color = (230,230,230)

		# 飞船的设置
		self.ship_speed_factor = 2
		self.ship_limit = 3
		
		# 子弹设置
		self.bullet_speed_factor = 3
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3

		# 外星人设置
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		self.fleet_direction = 1 # 1=右移 ， 2=左移

		# 游戏加速度
		self.speedup_scale = 1.1
		self.score_scale = 1.5

		self.initialize_dynamic_settings()
		
	def initialize_dynamic_settings(self):
		'''初始化游戏并随游戏变化的设置'''
		self.ship_speed_factor = 2
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1
		self.fleet_direction = 1 # 1=右移 ， 2=左移
		# 记分
		self.alien_points = 10

	def increase_speed(self):
		'''提高游戏速度设置和外星人点数'''
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale

		self.alien_points = int(self.alien_points*self.score_scale)
class GameStats():
	"""跟踪游戏统计信息"""
	def __init__(self, ai_settings):
		# 初始化统计信息
		self.ai_settings = ai_settings
		self.reset_stats()
		# 游戏刚启动时处于非活跃状态
		self.game_active = False
		self.high_score = 0

	def reset_stats(self):
		'''初始化运行期间可能变化统计信息'''
		self.score = 0
		self.level = 1
		

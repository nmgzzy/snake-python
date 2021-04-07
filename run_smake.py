import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
# from scoreboard import Scoreboard
from button import Button
from snake import Snake
from food import Food
import game_functions as gf
import time

def run_game():
	# 初始化游戏并创建屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Snake")

	# 创建储存游戏统计信息的实例，并创建记分牌
	stats = GameStats(ai_settings)
	# gf.load_high_score(stats)
	# sb = Scoreboard(ai_settings, screen, stats)

	snake = Snake(ai_settings, screen)
	food = Food(ai_settings, screen, snake)

	# 创建PLAY按钮
	play_button = Button(ai_settings, screen, 'Play')

	snake_len = 0
	delay_time = 0.3

	# 开始游戏主循环
	while True:
		time_start = time.time()

		gf.check_events(ai_settings, screen, snake, play_button, stats)#, sb, , food

		if stats.game_active:
			snake.update()
			if gf.check_snake_eat_food(snake, food):
				food.update()
				snake.grow()
			gf.check_snake_hit(ai_settings, stats, snake)
		gf.update_screen(ai_settings, screen, snake, food, play_button, stats)

		time_end = time.time()
		t = time_end-time_start

		if snake.length <= 50 and snake.length >= 5:
			snake_len = snake.length - 5
			delay_time = ((45 - snake_len) / 45 * 0.25 + 0.05 - t)
			if delay_time < 0.05:
				delay_time = 0.05

		time.sleep(delay_time/ai_settings.speedup_scale)

run_game()

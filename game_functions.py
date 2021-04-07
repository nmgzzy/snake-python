import sys
from time import sleep
import pygame
# from food import Food

def check_keydown_events(event, snake, ai_settings):#, screen, stats, sb, food,
	if event.key == pygame.K_RIGHT and snake.moving_direction != 'L':
		snake.moving_direction = 'R'
	elif event.key == pygame.K_LEFT and snake.moving_direction != 'R':
		snake.moving_direction = 'L'
	elif event.key == pygame.K_UP and snake.moving_direction != 'D':
		snake.moving_direction = 'U'
	elif event.key == pygame.K_DOWN and snake.moving_direction != 'U':
		snake.moving_direction = 'D'
	if event.key == pygame.K_RIGHT and snake.moving_direction == 'R':
		ai_settings.speedup_scale = 2
	elif event.key == pygame.K_LEFT and snake.moving_direction == 'L':
		ai_settings.speedup_scale = 2
	elif event.key == pygame.K_UP and snake.moving_direction == 'U':
		ai_settings.speedup_scale = 2
	elif event.key == pygame.K_DOWN and snake.moving_direction == 'D':
		ai_settings.speedup_scale = 2

	elif event.key == pygame.K_q:
		#save_high_score(stats)
		sys.exit()


def check_events(ai_settings, screen, snake, play_button, stats):#ai_settings, screen, sb, , snake, food
	'''响应键盘和鼠标事件'''
	# 监视键盘和鼠标事件
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			# save_high_score(stats)
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, snake, ai_settings)
		elif event.type == pygame.KEYUP:
			ai_settings.speedup_scale = 1
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(ai_settings, screen, stats, play_button, snake, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, play_button, snake, mouse_x, mouse_y):#
	'''点击Play时开始游戏'''
	button_chicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_chicked and not stats.game_active:
		# 重置游戏设置
		ai_settings.initialize_dynamic_settings()
		start_game(ai_settings, screen, stats, snake)

def start_game(ai_settings, screen, stats, snake):#, sb, food
	# 隐藏光标
	pygame.mouse.set_visible(False)

	# 重置游戏统计信息
	stats.reset_stats()
	stats.game_active = True
	snake.reset()

	# 重置记分牌
	# sb.prep_score()
	# sb.prep_high_score()
	# sb.prep_level()
	# sb.prep_snakes()

def update_screen(ai_settings, screen, snake, food, play_button, stats):
	'''更新屏幕上的图像'''
	# 每次循环使都重绘屏幕
	screen.fill(ai_settings.bg_color)
	# 在飞船和外星人后面重绘所有子弹
	snake.blitme()
	food.blitme()
	
	# 显示得分
	# sb.show_score()

	# 如果游戏处于非活跃状态，绘制Play按钮
	if not stats.game_active:
		play_button.draw_button()

	# 让最近绘制的屏幕可见
	pygame.display.flip()


def check_snake_eat_food(snake, food):
	'''响应蛇吃到了失误'''
	return snake.body[0].x == food.place.x and snake.body[0].y == food.place.y

def check_snake_hit(ai_settings, stats, snake):
	'''响应蛇吃到自己'''
	if snake.hit or snake.length > ai_settings.grid_width*ai_settings.grid_height//10:
		stats.game_active = False
		pygame.mouse.set_visible(True)

# def check_high_score(stats, sb):
# 	'''检查是否诞生了新的最高分'''
# 	if stats.score > stats.high_score:
# 		stats.high_score = stats.score
# 		sb.prep_high_score()

# def save_high_score(stats):
# 	'''保存历史最高分到文件'''
# 	with open('hs.dat','w') as file_object:
# 		file_object.write(str(stats.high_score))

# def load_high_score(stats):
# 	'''加载历史最高分'''
# 	with open('hs.dat') as file_object:
# 		stats.high_score = int(file_object.read())

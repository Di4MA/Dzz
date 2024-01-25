import pygame
import random

# Инициализация игры
pygame.init()

# Установка размеров экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Простая игра на Python")

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)

# Параметры игрока
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 5

# Параметры врагов
enemy_width = 50
enemy_height = 50
enemy_x = random.randint(0, screen_width - enemy_width)
enemy_y = 0
enemy_speed = 3

# Функция отрисовки игрока
def draw_player(x, y):
    pygame.draw.rect(screen, white, [x, y, player_width, player_height])

# Функция отрисовки врагов
def draw_enemy(x, y):
    pygame.draw.rect(screen, white, [x, y, enemy_width, enemy_height])

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    # Движение врагов
    enemy_y += enemy_speed
    if enemy_y > screen_height:
        enemy_x = random.randint(0, screen_width - enemy_width)
        enemy_y = 0

    # Отрисовка игрока и врагов
    screen.fill(black)
    draw_player(player_x, player_y)
    draw_enemy(enemy_x, enemy_y)

    # Обновление экрана
    pygame.display.update()
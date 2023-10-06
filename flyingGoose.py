import pygame
import random

# Инициализация Pygame
pygame.init()

# Размеры игрового поля
WIDTH = 1200
HEIGHT = 600
# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
# Создание игрового окна
game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Управление гусаком')

max_goose_width = 85
max_goose_height = 45
goose_frames = [
    pygame.transform.scale(pygame.image.load('goose_frame1.png'), (max_goose_width, max_goose_height)),
    pygame.transform.scale(pygame.image.load('goose_frame2.png'), (max_goose_width, max_goose_height)),
    pygame.transform.scale(pygame.image.load('goose_frame3.png'), (max_goose_width, max_goose_height)),
    pygame.transform.scale(pygame.image.load('goose_frame4.png'), (max_goose_width, max_goose_height)),
    pygame.transform.scale(pygame.image.load('goose_frame5.png'), (max_goose_width, max_goose_height)),
]
current_frame = 0
frame_delay = 10  # Задержка между кадрами (в количестве игровых циклов)
frame_count = 0  # Счетчик циклов для отслеживания задержки


# Загрузка изображения гусака, жареного гуся, печки, яблок и background
goose_image = pygame.image.load('goose.png')
fried_goose_image = pygame.image.load('fried_goose.png')
microwave_image = pygame.image.load('oven.png')
apple_image = pygame.image.load('apple.png')
background_image = pygame.image.load('background.png')

# Масштабирование изображения фона
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Оригинальные размеры изображения гусака
goose_original_width = goose_image.get_width()
goose_original_height = goose_image.get_height()
microwave_original_width = microwave_image.get_width()
microwave_original_height = microwave_image.get_height()
apple_original_width = apple_image.get_width()
apple_original_height = apple_image.get_height()
# Ограничение размера изображения гусака

max_microwave_width = 100
max_microwave_height = 100
max_apple_width = 15
max_apple_height = 15
# Масштабирование изображения гусака
if goose_original_width > max_goose_width or goose_original_height > max_goose_height:
    goose_scale = min(max_goose_width / goose_original_width, max_goose_height / goose_original_height)
    goose_image = pygame.transform.scale(goose_image, (int(goose_original_width * goose_scale),
                                                       int(goose_original_height * goose_scale)))
# Масштабирование изображения микроволновки
if microwave_original_width > max_microwave_width or microwave_original_height > max_microwave_height:
    microwave_scale = min(max_microwave_width / microwave_original_width,
                          max_microwave_height / microwave_original_height)
    microwave_image = pygame.transform.scale(microwave_image, (int(microwave_original_width * microwave_scale),
                                                               int(microwave_original_height * microwave_scale)))
# Масштабирование изображения яблока
if apple_original_width > max_apple_width or apple_original_height > max_apple_height:
    apple_scale = min(max_apple_width / apple_original_width, max_apple_height / apple_original_height)
    apple_image = pygame.transform.scale(apple_image, (int(apple_original_width * apple_scale),
                                                       int(apple_original_height * apple_scale)))

# Получение прямоугольника, ограничивающего гусака и жареного гуся
goose_rect = goose_image.get_rect()
fried_goose_rect = fried_goose_image.get_rect()

# Позиция гусака
goose_pos = [WIDTH // 2 - goose_rect.width // 2, HEIGHT // 2 - goose_rect.height // 2]
goose_speed = 5 # Скорость гусака
# Соперники
enemies = []
enemy_size = 30
enemy_speed = 3
enemy_acceleration = 0.1  # Ускорение соперников
max_enemy_speed = 25    # Максимальная скорость соперников

# Бонусы (яблоки)
bonuses = []
bonus_size = 25
bonus_speed = 2
bonus_interval = 300  # Интервал времени (в миллисекундах) для генерации новых бонусов
last_bonus_time = pygame.time.get_ticks()  # Время последней генерации бонуса

# Очки
score = 0
font = pygame.font.Font(None, 36)

# Главный цикл игры
running = True
game_over = False
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()  # Время начала игры

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        keys = pygame.key.get_pressed()        # Получение состояния клавиш

        # Обработка управления гусаком
        if keys[pygame.K_UP] and goose_pos[1] > 0:
            goose_pos[1] -= goose_speed
        if keys[pygame.K_DOWN] and goose_pos[1] < HEIGHT - goose_rect.height:
            goose_pos[1] += goose_speed
        if keys[pygame.K_LEFT] and goose_pos[0] > 0:
            goose_pos[0] -= goose_speed
        if keys[pygame.K_RIGHT] and goose_pos[0] < WIDTH - goose_rect.width:
            goose_pos[0] += goose_speed

        # Генерация новых бонусов
        current_time = pygame.time.get_ticks()
        if current_time - last_bonus_time > bonus_interval:
            bonus_x = random.randint(0, WIDTH - bonus_size)
            bonus_y = 0
            bonuses.append(pygame.Rect(bonus_x, bonus_y, bonus_size, bonus_size))
            last_bonus_time = current_time

        # Обновление позиции и скорости бонусов
        for bonus in bonuses:
            bonus.y += bonus_speed

            # Проверка столкновения бонуса с гусаком
            if goose_rect.colliderect(bonus):
                score += 100  # Добавление очков
                bonuses.remove(bonus)  # Удаление бонуса

            # Удаление бонусов, достигших дна
            if bonus.y > HEIGHT:
                bonuses.remove(bonus)

        # Добавление новых соперников
        if len(enemies) < 5:
            if random.randint(0, 100) < 2:
                enemy_x = WIDTH
                enemy_y = random.randint(0, HEIGHT - enemy_size)
                enemies.append(pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size))

        # Обновление кадра анимации гусака
        frame_count += 1
        if frame_count >= frame_delay:
            current_frame = (current_frame + 1) % len(goose_frames)  # Переключение на следующий кадр
            frame_count = 0

        # Обновление позиции и скорости соперников
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - start_time) / 100000.0  # Прошедшее время в секундах
        enemy_speed += enemy_acceleration * elapsed_time

        # Ограничение на максимальную скорость соперников
        if enemy_speed > max_enemy_speed:
            enemy_speed = max_enemy_speed
            
        for enemy in enemies:
            enemy.x -= enemy_speed

            # Удаление соперников, достигших края экрана
            if enemy.x < -enemy_size:
                enemies.remove(enemy)

            # Проверка столкновения соперников с гусаком
            if goose_rect.colliderect(enemy):
                game_over = True

        # Обновление гусака
        goose_rect.x = goose_pos[0]
        goose_rect.y = goose_pos[1]

        # Очистка экрана
        game_display.blit(background_image, (0, 0))

        # Отрисовка гусака
        game_display.blit(goose_frames[current_frame], (goose_pos[0], goose_pos[1]))

        # Отрисовка соперников (микроволновок)
        for enemy in enemies:
            game_display.blit(microwave_image, (enemy.x, enemy.y))
            
        # Отрисовка бонусов
        for bonus in bonuses:
            game_display.blit(apple_image, (bonus.x, bonus.y))

        # Отрисовка очков
        score_text = font.render("Score: " + str(score), True, BLACK)
        game_display.blit(score_text, (WIDTH - score_text.get_width() - 10, 10))

        pygame.display.flip()        # Обновление экрана

    # Завершение игры
    if game_over:
        game_display.fill(WHITE)
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over", True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 5))
        final_score_text = font.render("Final score: " + str(score), True, BLACK)
        game_display.blit(final_score_text, (WIDTH - final_score_text.get_width() - 10, 10))
        game_display.blit(text, text_rect)
        game_display.blit(fried_goose_image, (WIDTH // 2 - fried_goose_rect.width // 2, HEIGHT // 2 - fried_goose_rect.height // 2))
        pygame.display.flip()

    # Ограничение FPS
    clock.tick(60)

# Завершение игры
pygame.quit()

import pygame
import random
import sys
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Clicker")
pygame_icon = pygame.image.load('game_icon_two.png')
pygame.display.set_icon(pygame_icon)
# VALUES
coins = 0
time_level = 1
speed_level = 1
strength_level = 1
playerX = 680
playerY = 500
playerX_change = 0
playerY_change = 0
time_count = 100

object_speed = 1

current_time = 0
press_time = 0
timed = False
drawn = False
printed_t = False
printed_sp = False
printed_str = False
full_screen = False
printed = False
is_taken_one = False
is_taken_two = False
is_taken_three = False
is_taken_four = False
is_taken_five = False
is_taken_six = False
is_taken_seven = False
is_taken_eight = False

running = False
settings = False
credit = False
main = True
fps = pygame.time.Clock()

clock = pygame.time.Clock()


# UI/fonts
font_one = pygame.font.Font(None, 150)
surface_one = font_one.render('You beat the game', True, 'Green')

circle = pygame.image.load('circle_enemy.png')
circle = pygame.transform.scale(circle, (30, 30))

rectangle = pygame.image.load('rectangle_enemy.png')
rectangle = pygame.transform.scale(rectangle, (30, 30))

triangle = pygame.image.load('triangle_enemy.png')
triangle = pygame.transform.scale(triangle, (30, 30))

hexagon = pygame.image.load('hexagon_enemy.png')
hexagon = pygame.transform.scale(hexagon, (30, 30))

enemies = [circle, rectangle, triangle, hexagon]

# ______________________
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
screen = pygame.display.set_mode((1350, 700), pygame.RESIZABLE)

# RANDOMS ABOT ENEMIES
random_x = random.randint(260, 1160)
random_y = random.randint(260, 730)
enemy_pos_x = random_x
enemy_pos_y = random_y
random_strength = random.randint(1, 3)

# BUTTON IMAGES
button_size_w = 260
button_size_h = 250

play_button = pygame.image.load('images.png').convert_alpha()
play_button = pygame.transform.scale(play_button, (button_size_w, button_size_h))

settings_button = pygame.image.load('settings.png').convert_alpha()
settings_button = pygame.transform.scale(settings_button, (button_size_w, button_size_h))

credits_button = pygame.image.load('credits.png').convert_alpha()
credits_button = pygame.transform.scale(credits_button, (button_size_w, button_size_h))

exit_button = pygame.image.load('exit.png').convert_alpha()
exit_button = pygame.transform.scale(exit_button, (button_size_w, button_size_h))

# DEF


def is_taken():
    if is_taken_one:
        pass
    elif is_taken_two:
        pass
    elif is_taken_three:
        pass
    elif is_taken_four:
        pass
    elif is_taken_five:
        pass
    elif is_taken_six:
        pass
    elif is_taken_seven:
        pass
    elif is_taken_eight:
        pass


class Enemy(object):
    def __init__(self, x, y, speed, strength):
        self.x = x
        self.y = y
        self.speed = speed
        self.strength = strength
        screen.blit(circle, (x, y))
        mini_level_enemy_surface = mini_level_font.render(f'{strength}', True, 'Black')
        screen.blit(mini_level_enemy_surface, (random_x + 11, random_y + 7))
        return


enemy = Enemy


class Player(object):
    def __init__(self, player_x, player_y, velocity, strength):
        self.player_x = player_x
        self.player_y = player_y
        self.velocity = velocity
        self.strength = strength
        pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, 20, 20))
        mini_level_surface = mini_level_font.render(f'{strength_level}', True, 'Black')
        screen.blit(mini_level_surface, (playerX + 5, playerY + 2))


player = Player


class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.scale = scale
        self.image = pygame.transform.scale(image, (int(width * self.scale), int(height * self.scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        mouse = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse):
            self.scale += 100

            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action


play_button = Button(545, 100, play_button, 1)
settings_button = Button(545, 220, settings_button, 1)
credits_button = Button(545, 350, credits_button, 1)
exit_button = Button(545, 480, exit_button, 1)


def ran_object(shape, x, y):
    screen.blit(shape, (x, y))


screenW = screen.get_width()
screenH = screen.get_height()

object_pos_x = random.randrange(1350)
object_pos_y = random.randrange(700)


# MAIN LOOPS
while main:
    main_digits = random.randint(1, 400)
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, 'Green', (0, 0, screenW + 15, screenH + 70), 10)

    # BUTTONS
    if play_button.draw():
        running = True
        main = False
    if settings_button.draw():
        settings = True
        main = False
    if credits_button.draw():
        credit = True
        main = False

    if exit_button.draw():
        pygame.quit()
        sys.exit()

    ran_enemy = (random.choice(enemies))
    ran_object(ran_enemy, object_pos_x, object_pos_y)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == VIDEORESIZE:
            if not full_screen:
                screen = pygame.display.set_mode((event.w, event.h), RESIZABLE)

        # KEY DOWN
        if event.type == pygame.KEYDOWN:

            if event.key == K_F11:
                if not full_screen:
                    screen = pygame.display.set_mode(monitor_size, FULLSCREEN)
                    full_screen = True
                elif full_screen:
                    screen = pygame.display.set_mode((1350, 700), pygame.RESIZABLE)
                    full_screen = not full_screen
    object_pos_x += object_speed
    object_pos_y += object_speed

    if object_pos_x >= screenW:
        object_pos_x = random.randrange(screenW)
        object_pos_y = random.randrange(screenH)

    if object_pos_y >= screenH:
        object_pos_x = random.randrange(screenW)
        object_pos_y = random.randrange(screenH)

    pygame.display.update()
while running:
    vel = 1 + speed_level
    digit = random.randint(1, 400)
    current_time = pygame.time.get_ticks()
    screen.fill((0, 0, 0))
    # FONTS
    coin_font = pygame.font.Font(None, 30)
    notification_font = pygame.font.Font(None, 50)
    notifications_font = pygame.font.Font(None, 20)
    mini_level_font = pygame.font.Font(None, 25)
    # SURFACE
    coin_surface = coin_font.render(f'You have: {coins}', True, 'Green')

    speed_surface = coin_font.render(f'Speed level: {speed_level}', True, 'Green')

    stamina_surface = coin_font.render(f'Stamina level: {time_level}', True, 'Green')

    strength_surface = coin_font.render(f'Strength level: {strength_level}', True, 'Green')

    notification_surface = notification_font.render('Notifications', True, 'Green')

    time_surface_bar = notification_font.render(f'{time_count}', True, 'Green')

    notifications_surface = notifications_font.render('You need more coins', True, 'Red')

    # BLIT
    screen.blit(coin_surface, (0, 0))
    screen.blit(speed_surface, (0, 630))
    screen.blit(stamina_surface, (0, 680))
    screen.blit(strength_surface, (0, 730))
    screen.blit(time_surface_bar, (664, 100))
    screen.blit(notification_surface, (1130, 20))

    # MORE IFS
    if playerX <= 255:
        playerX_change = 0
    elif playerX >= 1125:
        playerX_change = 0

    if playerY <= 255:
        playerY_change = 0
    elif playerY >= 726:
        playerY_change = 0

    if printed:
        is_taken_one = True
        screen.blit(notifications_surface, (1115, 60))
        if current_time - press_time >= 3000:
            printed = False

    # PLAYER
    player(playerX, playerY, vel, strength_level)

    # ENEMY
    if digit == 2:
        timed = True

    if timed:
        enemy(random_x, random_y, 3, random_strength)

    if playerX > random_x:
        random_x = random_x + 1

    if playerX < random_x:
        random_x = random_x - 1

    if playerY > random_y:
        random_y = random_y + 1

    if playerY < random_y:
        random_y = random_y - 1

    # KEYS
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # KEY DOWN
        if event.type == pygame.KEYDOWN:

            press_time = pygame.time.get_ticks()

            if event.type == VIDEORESIZE:
                if not full_screen:
                    screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

            if event.key == K_F11:
                full_screen = not full_screen
                if full_screen:
                    screen = pygame.display.set_mode(monitor_size, FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), RESIZABLE)

            if event.key == pygame.K_1 and coins >= 5:
                coins -= 5
                speed_level += 1
            elif event.key == pygame.K_1 and coins < 5:
                printed = True

            elif event.key == pygame.K_2 and coins >= 10:
                coins -= 10
                strength_level += 1
            elif event.key == pygame.K_2 and coins < 10:
                printed = True

            elif event.key == pygame.K_3 and coins >= 15:
                coins -= 15
                time_level += 1
            elif event.key == pygame.K_3 and coins < 15:
                printed = True
            else:
                pass

    # PLAYER
            if event.key == pygame.K_a and time_count > 0:
                playerX_change -= vel
            else:
                playerX_change -= 0
            if event.key == pygame.K_d and time_count > 0:
                playerX_change += vel
            else:
                playerX_change -= 0
            if event.key == pygame.K_s and time_count > 0:
                playerY_change += vel
            else:
                playerY_change -= 0
            if event.key == pygame.K_w and time_count > 0:
                playerY_change -= vel
            else:
                playerY_change -= 0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                playerX_change = 0
            elif event.key == pygame.K_s:
                playerX_change = 0
            elif event.key == pygame.K_w:
                playerY_change = 0
            elif event.key == pygame.K_a:
                playerY_change = 0
            else:
                pass

        playerX += playerX_change
        playerY += playerY_change

        # MOUSE BUTTON DOWN
        if event.type == pygame.MOUSEBUTTONDOWN:
            pressed_keys = pygame.mouse.get_pressed()
            if pressed_keys[0]:
                coins += 1
# SHOP
    if time_level == 30 and not printed_t:
        print("You maxed stamina")
        printed_s = True
    if speed_level == 30 and not printed_sp:
        print("You maxed speed")
        printed_sp = True
    if strength_level == 30 and not printed_str:
        print("You maxed strength")
        printed_str = True

    # DRAW
    pygame.draw.rect(screen, 'Green', (1100, 0, 300, 200), 5)
    pygame.draw.rect(screen, 'White', (250, 250, 900, 500), 5)

    # END
    if strength_level == 30 and speed_level == 30 and time_level == 30:
        screen.blit(surface_one, (250, 250))
    fps.tick(30)
    pygame.display.update()
while credit:
    main_digits = random.randint(1, 400)
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, 'Green', (0, 0, screenW + 15, screenH + 70), 10)

    ran_enemy = (random.choice(enemies))
    ran_object(ran_enemy, object_pos_x, object_pos_y)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == VIDEORESIZE:
            if not full_screen:
                screen = pygame.display.set_mode((event.w, event.h), RESIZABLE)

        # KEY DOWN
        if event.type == pygame.KEYDOWN:

            if event.key == K_F11:
                if not full_screen:
                    screen = pygame.display.set_mode(monitor_size, FULLSCREEN)
                    full_screen = True
                elif full_screen:
                    screen = pygame.display.set_mode((1350, 700), pygame.RESIZABLE)
                    full_screen = not full_screen

    object_pos_x += object_speed
    object_pos_y += object_speed

    if object_pos_x >= screenW:
        object_pos_x = random.randrange(screenW)
        object_pos_y = random.randrange(screenH)

    if object_pos_y >= screenH:
        object_pos_x = random.randrange(screenW)
        object_pos_y = random.randrange(screenH)

    pygame.display.update()
while settings:
    main_digits = random.randint(1, 400)
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, 'Green', (0, 0, screenW + 15, screenH + 70), 10)

    ran_enemy = (random.choice(enemies))
    ran_object(ran_enemy, object_pos_x, object_pos_y)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == VIDEORESIZE:
            if not full_screen:
                screen = pygame.display.set_mode((event.w, event.h), RESIZABLE)

        # KEY DOWN
        if event.type == pygame.KEYDOWN:

            if event.key == K_F11:
                if not full_screen:
                    screen = pygame.display.set_mode(monitor_size, FULLSCREEN)
                    full_screen = True
                elif full_screen:
                    screen = pygame.display.set_mode((1350, 700), pygame.RESIZABLE)
                    full_screen = not full_screen

    object_pos_x += object_speed
    object_pos_y += object_speed

    if object_pos_x >= screenW:
        object_pos_x = random.randrange(screenW)
        object_pos_y = random.randrange(screenH)

    if object_pos_y >= screenH:
        object_pos_x = random.randrange(screenW)
        object_pos_y = random.randrange(screenH)

    pygame.display.update()

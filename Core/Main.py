__author__ = 'crimsonSurfer'

import sys

import pygame

from Core.PlayerPackage.player import Player
from Core.PlayerPackage.MainCharacter import MainCharacter

displaySize = [500, 500]
padding = 8
level = {1, 2, 3}
current_level = 0
walkCount = 0
left = False
right = True
clock = pygame.time.Clock()

background = pygame.image.load('playerPackage/images/Background/treeBg.png')


def delay(time_in_milli_seconds):
    pygame.time.delay(time_in_milli_seconds)


def process_pygame_event(player):
    event_stream = pygame.event.get()
    for eachEvent in event_stream:
        if eachEvent.type == pygame.QUIT:
            print("%s%i" % ("Exiting with Event code : ", eachEvent.type))
            sys.exit()
        else:
            print("%s%i" % ("Event code ---> ", eachEvent.type))


def process_jump(player):
    print("in process_jump")
    print("_is_jump = " + str(player.is_jump))
    player.jump()


def move_player(player, speed):
    global walkCount, left, right
    pressed_key = pygame.key.get_pressed()

    if pressed_key[pygame.K_LEFT] and player.x_position > 0:
        left = True
        right = False
        player.set_x_position -= speed

    elif pressed_key[pygame.K_RIGHT] and player.x_position < displaySize[0] - player.width - padding:
        left = False
        right = True
        player.set_x_position += speed
        walkCount += 1
    else:
        left = False
        right = False
        walkCount = 0

    if not player.is_jump:
        if pressed_key[pygame.K_UP] and player.y_position > 0:  # y decreases as player moves up
            player.set_y_position -= speed
        elif pressed_key[pygame.K_DOWN] and player.y_position < displaySize[1] - player.height - padding:
            player.set_y_position += speed

        elif pressed_key[pygame.K_SPACE]:
            player.set_is_jump = True

    else:
        player.jump()


def redraw_game_screen(screen, current_stage, player):
    global walkCount, left, right
    if player.get__current_stage() == 0:
        screen.blit(background, (0, 0))  # redraws the background

    if walkCount + 1 >= 27:
        walkCount = 0
    if left:
        print("Here")
        list_left = player.get__walk_animation_left()
        screen.blit(list_left[walkCount // 3], (player.x_position, player.y_position))
        walkCount += 1
    elif right:
        list_right = player.get__walk_animation_right()
        screen.blit(list_right[walkCount // 3],( player.x_position, player.y_position))
        walkCount += 1
    else:
        screen.blit((player.get__standing_animation()), (player.x_position, player.y_position))
    # pygame.draw.rect(screen, (255, 56, 180), (
    # player.x_position, player.y_position, player.width, player.height))  # surface, color, rect, width

    print(player.print_position())
    pygame.display.update()


def main():
    # player_1 = Player(0,453, 33, 47)
    player_2 = Player(200, 100, 50, 60)
    global clock
    player_1 = MainCharacter()
    player_1.set__current_stage(0)

    speed = 10;
    pygame.init()
    screen = pygame.display.set_mode(displaySize)
    pygame.display.set_caption("Hello World Pygame!")
    gameIsRunning = True

    while gameIsRunning:
        clock.tick(27)
        delay(100)
        process_pygame_event(player_1)
        move_player(player_1, speed)
        redraw_game_screen(screen, player_1.get__current_stage(), player_1)
    pygame.quit()


if __name__ == '__main__':
    main()

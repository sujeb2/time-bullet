from pygame.locals import *

# Setup
WIDTH = 1280
HEIGHT = 720
DEF_FPS = 60
VER = '1.0.0'

# Player Setting
PLAYER_START_X = 150
PLAYER_START_Y = 150
# 1.0x, 1.5x, 2x
PLAYER_VIEW_SIZE = 2
PLAYER_SPEED = 10
PLAYER_DASH_SPEED = 20
PLAYER_SHOOT_COOLDOWN = 10
PLAYERMANA_REMOVE_VAL = 1
PLAYERMANA_COOLDOWN = 20
GUN_OFFSET_X = 45
GUN_OFFSET_Y = 5
SLOWSPEED_X = 3
SLOWSPEED_Y = -3
FASTSPEED_X = 2
FASTSPEED_Y = 2

# Setting
GAME_DEFAULTSOUND_PLAY = False
MUSIC_VOL = 20

# UI
UI_VIEWSIZE = 1

# Debug
SHOW_CURRENTFPS = False
DEBUG_FPSWARNING_VALUE = 15
SHOW_PLAYERMANA_CONSOLE = False
SCREEN_FLAGS = DOUBLEBUF
RUN_GAME_BEFORE_MENU = False
RUN_FULLSCREEN = False

# Bullet
BULLET_COOLDOWN = 10
BULLET_VIEWSIZE = 1.4
BULLET_SPEED = 13
BULLET_LIFETIME = 500


if RUN_FULLSCREEN:
    SCREEN_FLAGS = DOUBLEBUF | FULLSCREEN
else:
    SCREEN_FLAGS = DOUBLEBUF
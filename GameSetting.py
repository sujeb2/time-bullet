from pygame.locals import *

# Setup
WIDTH = 1280
HEIGHT = 720
DEF_FPS = 60
VER = '1.1'
MOTD = {
    '버그가 있거나, 피드백을 주고 싶으세요? 저의 디스코드에 들어와보세요!',
    '여전히 플레이 하고 있으시네요!',
    '여기엔 뭐가 있을까요...',
    '여기까지 오는데 총 3개월이 걸렸어요!',
    '개발자들은 현재 자고 있을수도..',
    '이거 보고 있으신가요?',
    '여전히 시간은 가고 있어요 *똑딱똑딱*',
    '혹시 이 메세지를 볼려고 게임을 계속 껐다가 키는건 아니죠?',
    '그거 아시나요? 이 메세지는 랜덤으로 정해지는거!',
    '누가 알겠어요, 원래 이 게임은 퍼즐게임으로 만들어졌지만 FPS로 변경된걸'
}
# Player Setting
PLAYER_START_X = 150
PLAYER_START_Y = 150
# 1.0x, 1.5x, 2x
PLAYER_VIEW_SIZE = 2
PLAYER_SPEED = 80
PLAYER_DASH_SPEED = 90
PLAYER_SHOOT_COOLDOWN = 10
PLAYER_DASH_REMOVE_MANA_VAL = 30
PLAYERMANA_REMOVE_VAL = 1
PLAYERMANA_COOLDOWN = 20
GUN_OFFSET_X = 45
GUN_OFFSET_Y = 5

# Setting
GAME_DEFAULTSOUND_PLAY = False
MUSIC_VOL = 20

# Debug
IFYOUKNOWWHATAREYOUDOINGRIGHTNOWTURNONTHISFORDEBUG = True
SHOW_CURRENTFPS = True
DEBUG_FPSWARNING_VALUE = 15
SHOW_PLAYERMANA_CONSOLE = False
SCREEN_FLAGS = DOUBLEBUF
RUN_GAME_BEFORE_MENU = False
RUN_FULLSCREEN = False
SHOW_TRIGGERS = False
DRAW_GREYBACKGROUND_ASVOID = True
YES_THIS_IS_DEBUGGER_IDC = False

# Bullet
BULLET_COOLDOWN = 10
BULLET_VIEWSIZE = 1.4
BULLET_SPEED = 13
BULLET_LIFETIME = 500

# Enemy
ENEMY_SPEED = 2.5
ENEMY_VIEWSIZE = 2

if RUN_FULLSCREEN:
    SCREEN_FLAGS = DOUBLEBUF | FULLSCREEN
else:
    SCREEN_FLAGS = DOUBLEBUF

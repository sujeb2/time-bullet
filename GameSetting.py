from pygame.locals import *

# Setup
WIDTH = 1280
HEIGHT = 720
DEF_FPS = 60
VER = '2.1'
MOTD = {
    '버그가 있거나, 피드백을 주고 싶으세요? 저희 디스코드에 들어와보세요!',
    '여전히 플레이 하고 있으시네요!',
    '여기엔 뭐가 있을까요...',
    '여기까지 오는데 총 3개월이 걸렸어요!',
    '개발자들은 현재 자고 있을수도..',
    '이거 보고 있으신가요?',
    '여전히 시간은 가고 있어요 *똑딱똑딱*',
    '혹시 이 메세지를 볼려고 게임을 계속 껐다가 키는건 아니죠?',
    '그거 아시나요? 이 메세지는 랜덤으로 정해지는거!',
    f'여전히 {VER} 버전을 사용하고 있으시네요!',
    '혹시 지금 쓰는 버전이 데모버전이라는건 알고게시나요?',
    '데모!',
    '이 게임은 원래 도전과제가 있다는걸 알고게시나요?',
    '이 메세지가 반복될수도 있을수도..',
    '이러한 메세지를 MOTD(Message Of The Day)이라고 불리는걸 아시나요?'
}
# Player Setting
PLAYER_VIEW_SIZE = 1
PLAYER_SPEED = 0.5
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
IFYOUKNOWWHATAREYOUDOINGRIGHTNOWTURNONTHISFORDEBUG = False
SHOW_CURRENTFPS = True
DEBUG_FPSWARNING_VALUE = 15
SHOW_PLAYERMANA_CONSOLE = False
SCREEN_FLAGS = DOUBLEBUF
VSYNC = 1
RUN_GAME_BEFORE_MENU = True
RUN_FULLSCREEN = False
SHOW_TRIGGERS = False
DRAW_GREYBACKGROUND_ASVOID = True
YES_THIS_IS_DEBUGGER_IDC = False
SHOW_DEBUGINFO_TOSCREEN = True
SHOW_COLLISION_BOXES = False
ISPRODUCTMODE = True
LOGLEVEL = 'DEBUG'

# Bullet
BULLET_COOLDOWN = 50
BULLET_VIEWSIZE = 1
BULLET_SPEED = 10
BULLET_LIFETIME = 450
FIST_LIFETIME = 100

# Enemy
ENEMY_SPEED = 2
ENEMY_VIEWSIZE = 1.25
ENEMY_RADIUS = 500
ENEMY_ROAMING_SPEED = 10
ENEMY_NUMBER = 5
ENEMY_DEAD_BULLET = 5
ENEMEY_SPAWN_RATE = 38

# Map
TILESIZE = 32

if RUN_FULLSCREEN:
    SCREEN_FLAGS = DOUBLEBUF | FULLSCREEN
else:
    SCREEN_FLAGS = DOUBLEBUF

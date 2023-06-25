import pygame, sys, math, GameSetting, os
from tkinter import messagebox

# Color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (97, 97, 97)

# bool
isMainGameScene = False
isMainMenuScene = True

# int
MaxHandgunBullet = 255
MaxMachineGunBullet = 255
MaxHandgunLoadBullet = 18
MaxMachinegunLoadBullet = 75

# str
str_MaxHandgunBullet = str(MaxHandgunBullet)
str_MaxMachineGunBullet = str(MaxMachineGunBullet)
str_MaxHandgunLoadBullet = str(MaxHandgunLoadBullet)
str_MaxMachinegunLoadBullet = str(MaxMachinegunLoadBullet)
str_SceneName = ''

def quitGame():
    print("Exiting..")
    pygame.quit()
    sys.exit() # to make sure that game is closed.

# Image
print("Reading Images..")
try:
    img_backgroundLoop = pygame.image.load('./src/img/background/game_default_background.png')
    img_backgroundLoop = pygame.transform.scale(img_backgroundLoop,(1280, 720))
    img_gameLogo = pygame.image.load('./src/img/gameicon_placeholder.png')

    icn_bulletFull = pygame.image.load('./src/img/icon/indiv_icon/Bullet.png')
    icn_bulletFull = pygame.transform.scale(icn_bulletFull, (32, 32))
    icn_bulletEmpty = pygame.image.load('./src/img/icon/indiv_icon/BulletEmpty.png')
    icn_bulletEmpty = pygame.transform.scale(icn_bulletEmpty, (32, 32))
    icn_GunSelect_handGun = pygame.image.load('./src/img/icon/indiv_icon/Handgun.png')
    icn_GunSelect_handGun = pygame.transform.scale(icn_GunSelect_handGun, (32, 32))
    icn_GunSelect_machineGun = pygame.image.load('./src/img/icon/indiv_icon/Machinegun.png')
    icn_GunSelect_machineGun = pygame.transform.scale(icn_GunSelect_machineGun, (32, 32))
    
    hud_HealthFull = pygame.image.load('./src/img/hud/Health1.png')
    hud_HealthFull = pygame.transform.scale(hud_HealthFull, (32, 32))
    hud_HealthHalf = pygame.image.load('./src/img/hud/Health1Half.png')
    hud_HealthHalf = pygame.transform.scale(hud_HealthHalf, (32, 32))
    hud_HealthEmpty = pygame.image.load('./src/img/hud/HealthEmpty.png')
    hud_HealthEmpty = pygame.transform.scale(hud_HealthEmpty, (32, 32))
    
    hudBackground_weaponSelect = pygame.image.load('./src/img/hud/weapon_select.png')

    csrImg_Crosshair = pygame.image.load('./src/img/cursor/default-crosshair.png')

    tile_mapDefaultBackground = pygame.image.load('.\\src\\img\\map_tile\\indiv_tile\\Tile7.png')
    print("Loaded.")
except:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(f"{exc_type}, {exc_obj}, {exc_tb}, {fname}")
    messagebox.showerror(title='Error occurred', message=f'{exc_type},\nObject: {exc_obj},\nLine: {exc_tb},\nType:{fname}')
    print("Error occurred while loading Images.")
    print("Is file even exists?")
    quitGame()

# 재설정
print("Initallizing..")
try:
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    dt = 0
    display = pygame.display
    pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
    tile_mapDefaultBackground = pygame.transform.scale(pygame.image.load('.\\src\\img\\map_tile\\indiv_tile\\Tile7.png').convert(), [1280, 720])

    print("Initallized.")
except:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(f"{exc_type}, {exc_obj}, {exc_tb}, {fname}")
    messagebox.showerror(title='Error occurred', message=f'{exc_type},\nObject: {exc_obj},\nLine: {exc_tb},\nType:{fname}')
    print("Error occurred while initallizing game.")
    print("May occurrs because of weird pygame bug lol")

# SFX / OST
print("Loading Sounds..")
try:
    # sfx
    sfx_Handgun = ['./src/sound/sfx/handgun/handgun_fire1.wav', './src/sound/sfx/handgun/handgun_noammo.wav', './src/sound/sfx/handgun/handgun_reload.wav']
    sfx_smg = ['./src/sound/sfx/smg/smg_startloop.wav', './src/sound/sfx/smg/smg_loop.wav', './src/sound/sfx/smg/smg_endloop.wav', './src/sound/sfx/smg/smg_noammo.wav', './src/sound/sfx/smg/smg_realod.wav']
    sfx_Click = ['']

    # ost
    ost_MainMenu = './src/sound/ost/background_ambient1.wav'

    print("Loaded.")
except:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(f"{exc_type}, {exc_obj}, {exc_tb}, {fname}")
    messagebox.showerror(title='Error occurred', message=f'{exc_type},\nObject: {exc_obj},\nLine: {exc_tb},\nType:{fname}')
    print("Error occurred while loading Sound.")
    print("Is file even exists?") # over 100!
    quitGame()

# 폰트및 타이틀 재설정
print("Resetting Font/Title..")
try:
    display.set_caption('spsroEngine Scene Replayer')
    display.set_icon(img_gameLogo)

    # Font
    defaultFont = pygame.font.Font("./src/font/PretendardVariable.ttf", 30)
    defaultCopyrightFont = pygame.font.Font("./src/font/PretendardVariable.ttf", 20)
    defaultBulletFont = pygame.font.Font("./src/font/PretendardVariable.ttf", 24)

    print("Loaded.")
except:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(f"{exc_type}, {exc_obj}, {exc_tb}, {fname}")
    messagebox.showerror(title='Error occurred', message=f'{exc_type},\nObject: {exc_obj},\nLine: {exc_tb},\nType:{fname}')
    print("Error occurred while reseting font/title.")
    print("May occurrs because of weird pygame bug lol")
finally:
    if display.get_caption == '':
        display.set_caption('Caption not set.')

# 텍스트
print("Resetting text object..")
text_MainLogoTitle = defaultFont.render('게임이름을여기에입력', True, WHITE)
text_MainStartGame = defaultFont.render('START', False, WHITE)
text_MainLoadGame = defaultFont.render('LOAD', False, WHITE)
text_MainSetting = defaultFont.render('SETTING', False, WHITE)
text_MainExit = defaultFont.render('EXIT', False, WHITE)
text_copyrightTeamName = defaultCopyrightFont.render('SONGRO STUDIO_', True, GRAY)

hud_bulletLeft = defaultBulletFont.render(str_MaxHandgunLoadBullet, False, WHITE)
hud_bulletMax = defaultBulletFont.render(str_MaxHandgunBullet, False, WHITE)
hud_bulletSlash = defaultBulletFont.render('/', True, WHITE)

class Player(pygame.sprite.Sprite): # main player class
    def __init__(self):
        super().__init__()
        print('Loading Player Sprite..')
        try:
            self.playerPos = pygame.math.Vector2(GameSetting.PLAYER_START_X, GameSetting.PLAYER_START_Y)
            self.playerSprite = pygame.transform.rotozoom(pygame.image.load('.\\src\\img\\animations\\entity\\player\\placeholder\\indiv_animation\\player_handgun_frame1.png').convert_alpha(), 0, GameSetting.PLAYER_VIEW_SIZE)
            self.basePlayerImage = self.playerSprite
            self.PlayerHitBoxRect = self.basePlayerImage.get_rect(center = self.playerPos)
            self.rect = self.PlayerHitBoxRect.copy()
            self.playerSpeed = GameSetting.PLAYER_SPEED
            self.playerDefaultDashSpeed = GameSetting.PLAYER_DASH_SPEED
            print("Loaded.")
        except:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f"{exc_type}, {exc_obj}, {exc_tb}, {fname}")
            messagebox.showerror(title='Error occurred', message=f'{exc_type},\nObject: {exc_obj},\nLine: {exc_tb},\nType:{fname}')
            print("Error occurred while loading Player Sprite.")
            print("Is file even exists?")
            quitGame()

    def playerRotation(self): # player rotation
        self.MouseCord = pygame.mouse.get_pos()
        self.playerMouseX = (self.MouseCord[0] - self.PlayerHitBoxRect.centerx)
        self.playerMouseY = (self.MouseCord[1] - self.PlayerHitBoxRect.centery)
        self.playerAngle = math.degrees(math.atan2(self.playerMouseY, self.playerMouseX))
        self.playerImg = pygame.transform.rotate(self.basePlayerImage, -self.playerAngle)
        self.rect = self.playerImg .get_rect(center = self.PlayerHitBoxRect.center)

    def userInput(self): # player movement
        self.velo_x = 0
        self.velo_y = 0

        userInputKey = pygame.key.get_pressed()

        if userInputKey[pygame.K_d]:
            self.velo_x = self.playerSpeed
        if userInputKey[pygame.K_a]:
            self.velo_x = -self.playerSpeed
        if userInputKey[pygame.K_w]:
            self.velo_y = -self.playerSpeed
        if userInputKey[pygame.K_s]:
            self.velo_y = self.playerSpeed

    def playerMove(self): # actual movement
        self.playerPos += pygame.math.Vector2(self.velo_x, self.velo_y)
        self.PlayerHitBoxRect.center = self.playerPos
        self.rect.center = self.PlayerHitBoxRect.center

    def playerUpdate(self): # player update
        self.userInput()
        self.playerMove()
        self.playerRotation()
        self.shoot()

player = Player()

# 메인
print(f"Replaying {str_SceneName}..")
try:
    while isMainMenuScene: # replay scene
        inputKey = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isMainMenuScene = False
                isMainGameScene = False

        screen.blit(tile_mapDefaultBackground, [0, 0])

        # render text
        #screen.blit(text_MainLogoTitle, [200, 300])
        #screen.blit(text_MainStartGame, [200, 342])
        #screen.blit(text_MainLoadGame, [200, 372])
        #screen.blit(text_MainSetting, [200, 402])
        #screen.blit(text_MainExit, [200, 432])
        #screen.blit(text_copyrightTeamName, [200, 465])

        # render hud
        screen.blit(hud_HealthFull, [30, 20])
        screen.blit(hud_HealthFull, [65, 20])
        screen.blit(hud_HealthFull, [100, 20]) # over 200!
        screen.blit(icn_GunSelect_handGun, [30, 60])
        screen.blit(hud_bulletLeft, [66, 60])
        screen.blit(hud_bulletMax, [108, 60])
        screen.blit(hud_bulletSlash, [95, 60])

        # render player
        screen.blit(player.playerSprite, player.rect)

        # Player Movement
        player.playerUpdate()

        pygame.display.flip()
        pygame.display.update()
        dt = clock.tick(60)
except:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(f"{exc_type}, {exc_obj}, {exc_tb}, {fname}")
    messagebox.showerror(title='Error occurred', message=f'{exc_type},\nObject: {exc_obj},\nLine: {exc_tb},\nType:{fname}')
    print("Error occurred while replaying scene.")
    quitGame()

pygame.quit()
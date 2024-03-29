############################
#  TIME / BULLET           #
#  FINAL DEMO VERSION      # DO NOT CONTRIBUTE IF YOU DONT HAVE PERMISSION
#  MADE BY. SONGRO STUDIO_ #
############################


# default imports
import pygame, sys, math, GameSetting, traceback, json, jsonschema, random, logging, spsroLightEngine
from tkinter import messagebox
from pygame.locals import *
from ButtonManager import Button
from csv import reader

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(' Initalizing logger..')
log = logging.getLogger()
if GameSetting.LOGLEVEL == 'INFO':
    log.setLevel(logging.INFO)
elif GameSetting.LOGLEVEL == 'WARN':
    log.setLevel(logging.WARN)
elif GameSetting.LOGLEVEL == 'CRITICAL':
    log.setLevel(logging.CRITICAL)
elif GameSetting.LOGLEVEL == 'DEBUG':
    log.setLevel(logging.DEBUG)
    print(f"{bcolors.WARNING}WARN: You're Currently using debug logging mode, it may contains debug messages.{bcolors.ENDC}")

format = logging.Formatter('%(asctime)s - %(name)s / %(levelname)s: %(message)s')
streamHandle = logging.StreamHandler()
streamHandle.setFormatter(format)
log.addHandler(streamHandle)
fileHandle = logging.FileHandler('./src/debug/debug-log.log')
fileHandle.setFormatter(format)
log.addHandler(fileHandle)

log.info(' Loading..')

# Color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (97, 97, 97)
DARK_GRAY = (23, 23, 23)
ORANGE = (252, 186, 3)
PURPLE = (119, 3, 252)
YELLOW = (252, 252, 3)
RED = (255, 0, 0)
BLUE = (66, 152, 245)

# bool
isMainGameScene = False
isMainMenuScene = True
isMainMenuToDemo = False
paused = False
menuState = "mainmenu"

# int
MaxHandgunBullet = 255
MaxMachineGunBullet = 255
MaxHandgunLoadBullet = 18
MaxMachinegunLoadBullet = 75
LoadedHandgunBullet = 18
LoadedMachineBullet = 75

# str
str_MaxHandgunBullet = str(MaxHandgunBullet)
str_MaxMachineGunBullet = str(MaxMachineGunBullet)
str_MaxHandgunLoadBullet = str(MaxHandgunLoadBullet)
str_MaxMachinegunLoadBullet = str(MaxMachinegunLoadBullet)
str_SceneName = ''

data = {
    'mxHandgunBullet': MaxHandgunBullet,
    'crtHandgunBullet': LoadedHandgunBullet,
    'crtScene': str_SceneName,
    'playerX': 0,
    'playerY': 0
}


flags = GameSetting.SCREEN_FLAGS

def validateJson(jsonData): # validate save file
    try:
        jsonschema.validate(instance=jsonData, schema=data)
    except jsonschema.ErrorTree.errors:
        log.fatal(f"{bcolors.FAIL} Failed to validate player save data, is File even exists?\nTraceBack: {traceback.format_exc()}{bcolors.ENDC}")
        return False
    return True

log.info(" Reading save file..")
try:
    with open('./src/save/0/playerSaveData.json', 'r+', encoding='utf-8') as svFile:
        data = json.load(svFile)
        log.info(f"{bcolors.OKGREEN} Loaded.{bcolors.ENDC}")
except:
    log.critical(f"{bcolors.FAIL} Error occurred while loading 'save/0/playeSaveData.json' file.")
    log.critical(f" This might happen when player changed some data.{bcolors.ENDC}")
    log.warning(f'{bcolors.WARNING}WARN: Returning Traceback:\n{traceback.format_exc()}{bcolors.ENDC}')
    messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')
    log.info(' Writting default save file...')
    with open('./src/save/0/playerSaveData.json', 'w') as writeSvFile:
        writeSvFile.write('{"mxHandgunBullet": 255, "crtHandgunBullet": 20000, "crtScene": "", "playerX": 0, "playerY": 0}')

log.info(" Checking save file requirements..")
try:
    with open('./src/save/0/playerSaveData.json', 'r') as pSv:
        mainData = str(json.load(pSv))
        isFileVaild = validateJson(mainData)

        if isFileVaild:
            log.info(f"{bcolors.OKCYAN} playerSaveData is vaild.{bcolors.ENDC}")
        else:
            log.warning(f"{bcolors.WARNING}WARN: playerSaveData isn't vaild as default state.{bcolors.ENDC}")
except FileNotFoundError:
    log.fatal(f"{bcolors.FAIL} Failed to read playerSaveData, is File even exists?\nTraceback: {traceback.format_exc()}{bcolors.ENDC}")
    messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')
    pygame.quit()
    sys.exit()

def quitGame():
    log.info(" Exiting..")
    pygame.quit()

# game init
log.info(" Initallizing..")
try:
    pygame.init()
    screen = pygame.display.set_mode((GameSetting.WIDTH, GameSetting.HEIGHT), flags, vsync=GameSetting.VSYNC)
    clock = pygame.time.Clock()
    dt = 0
    display = pygame.display
    running = True
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
    tile_mapDefaultBackground = pygame.transform.scale(pygame.image.load('./src/img/map_tile/indiv_tile/Tile7.png').convert(), [1280, 720])
    
    if GameSetting.IFYOUKNOWWHATAREYOUDOINGRIGHTNOWTURNONTHISFORDEBUG:
        if GameSetting.SHOW_PLAYERMANA_CONSOLE == True and GameSetting.SHOW_CURRENTFPS == True:
            log.debug(f'{bcolors.WARNING}Too many debug updates! it may slow down performance.{bcolors.ENDC}')
        else:
            pass
    else:
        pass

    playerDefaultLightSystem = spsroLightEngine.Light(1280, spsroLightEngine.pixel_shader(1280, (255, 255, 255), 1, False))
    playerDefaultLightShowObjects = [pygame.Rect(200, 200, 100 ,100)]

    log.info(f"{bcolors.OKGREEN}Initallized.{bcolors.ENDC}")
except:
    log.fatal(f"{traceback.format_exc()}")
    messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')
    log.fatal(f"{bcolors.FAIL}Error occurred while initallizing game.")
    log.fatal(f"May occurrs because of weird pygame bug lol{bcolors.ENDC}")

# Image
log.info(" Reading Images..")
try:
    # background / Favicon
    img_backgroundLoop = pygame.image.load('./src/img/background/game_default_background.png').convert_alpha()
    img_backgroundLoop = pygame.transform.scale(img_backgroundLoop,(GameSetting.WIDTH, GameSetting.HEIGHT))
    img_gameFavicon = pygame.image.load('./src/img/gameicon_placeholder.png').convert_alpha()
    img_gameLogo = pygame.image.load('./src/img/gamelogo.png').convert_alpha()
    img_gameLogo = pygame.transform.scale(img_gameLogo, (200, 100))

    # icon
    icn_GunSelect_handGun = pygame.image.load('./src/img/icon/indiv_icon/Handgun.png').convert_alpha()
    icn_GunSelect_handGun = pygame.transform.scale(icn_GunSelect_handGun, (32, 32))
    icn_GunSelect_machineGun = pygame.image.load('./src/img/icon/indiv_icon/Machinegun.png').convert_alpha()
    icn_GunSelect_machineGun = pygame.transform.scale(icn_GunSelect_machineGun, (32, 32))
    
    # hud
    hud_HealthFull = pygame.image.load('./src/img/hud/hud_health1.png').convert_alpha()
    hud_HealthFull = pygame.transform.scale(hud_HealthFull, (32, 32))
    hud_HealthHalf = pygame.image.load('./src/img/hud/hud_health_half.png').convert_alpha()
    hud_HealthHalf = pygame.transform.scale(hud_HealthHalf, (32, 32))
    hud_HealthEmpty = pygame.image.load('./src/img/hud/hud_health_empty.png').convert_alpha()
    hud_HealthEmpty = pygame.transform.scale(hud_HealthEmpty, (32, 32))
    hud_radiation = pygame.image.load('./src/img/hud/hud_radiation.png').convert_alpha()
    hud_radiation = pygame.transform.scale(hud_radiation, (32, 32))
    hudBackground_weaponSelect = pygame.image.load('./src/img/hud/weapon_select.png').convert_alpha()

    # button
    btn_Start = pygame.image.load('./src/img/button/menu/start_btn.png').convert_alpha()
    btn_Load = pygame.image.load('./src/img/button/menu/load_btn.png').convert_alpha()
    btn_Setting = pygame.image.load('./src/img/button/menu/setting_btn.png').convert_alpha()
    btn_Exit = pygame.image.load('./src/img/button/menu/exit_btn.png').convert_alpha()
    btn_Restart = pygame.image.load('./src/img/button/game/return_menu_btn.png').convert_alpha()
    btn_RestartBtn = pygame.image.load('./src/img/button/game/restart_btn.png').convert_alpha()

    # crosshair
    csrImg_Crosshair = pygame.image.load('./src/img/cursor/default-crosshair.png').convert_alpha()

    # background
    tile_mapDefaultBackground = pygame.image.load('./src/img/map_tile/indiv_tile/Tile7.png').convert_alpha()
    mainMenu_backgruond = pygame.image.load('./src/img/background/menu_background.png').convert_alpha()
    img_demoMapBackground = pygame.image.load('./src/maps/png/dev_test.png').convert_alpha()

    map_devTest = pygame.image.load('./src/maps/png/dev_test.png').convert_alpha()

    # map wall
    backgroundWall = pygame.image.load('./src/img/map_tile/indiv_tile/Tile7.png').convert_alpha()
    topWall = pygame.image.load('./src/img/map_tile/indiv_tile/Tile1.png').convert_alpha()
    topLeftDownWall = pygame.image.load('./src/img/map_tile/indiv_tile/Tile2.png').convert_alpha()
    rightStraightWall = pygame.image.load('./src/img/map_tile/indiv_tile/Tile3.png').convert_alpha()
    toprightDownWall = pygame.image.load('./src/img/map_tile/indiv_tile/Tile4.png').convert_alpha()
    straightWall = pygame.image.load('./src/img/map_tile/indiv_tile/Tile6.png').convert_alpha()
    straightNonDownWall = pygame.image.load('./src/img/map_tile/indiv_tile/Tile9.png').convert_alpha()
    topRightWall = pygame.image.load('./src/img/map_tile/indiv_tile/Tile10.png').convert_alpha()
    rightNonLeftWall = pygame.image.load('./src/img/map_tile/indiv_tile/Tile14.png').convert_alpha()
    topLeftWall = pygame.image.load('./src/img/map_tile/indiv_tile/Tile12.png').convert_alpha()
    leftNonRightWall = pygame.image.load('./src/img/map_tile/indiv_tile/Tile16.png').convert_alpha()
    nonWall = pygame.image.load('./src/img/map_tile/indiv_tile/Tile13.png').convert_alpha()
    voidWall = pygame.image.load('./src/img/map_tile/void.png').convert_alpha()

    entity_Bullet = pygame.image.load('./src/img/animations/object/bullet/BulletProjectile.png').convert_alpha()

    # overlay / etc
    img_overlayDeadScreenBlack = pygame.image.load('./src/img/hud/overlay/transparentBlack.png').convert_alpha()
    img_overlayBlackGradient = pygame.image.load('./src/img/hud/overlay/transparentGradient.png').convert_alpha()
    img_blackVoid = pygame.image.load('./src/img/map_tile/void.png').convert_alpha()
    img_blackVoid = pygame.transform.scale(img_blackVoid, (GameSetting.WIDTH, GameSetting.HEIGHT))
    img_overlayViggnete = pygame.image.load('./src/img/player_deco/vignette.png').convert_alpha()
    img_overlayViggnete = pygame.transform.scale(img_overlayViggnete, (1280, 1280))

    ui_rankS = pygame.image.load('./src/img/rank/s.png').convert_alpha()
    ui_rankS = pygame.transform.scale(ui_rankS, (128, 128))
    ui_rankA = pygame.image.load('./src/img/rank/a.png').convert_alpha()
    ui_rankA = pygame.transform.scale(ui_rankA, (128, 128))
    ui_rankB = pygame.image.load('./src/img/rank/b.png').convert_alpha()
    ui_rankB = pygame.transform.scale(ui_rankB, (128, 128))
    ui_rankC = pygame.image.load('./src/img/rank/c.png').convert_alpha()
    ui_rankC = pygame.transform.scale(ui_rankC, (128, 128))
    ui_rankD = pygame.image.load('./src/img/rank/d.png').convert_alpha()
    ui_rankD = pygame.transform.scale(ui_rankD, (128, 128))
    ui_rankF = pygame.image.load('./src/img/rank/f.png').convert_alpha()
    ui_rankF = pygame.transform.scale(ui_rankF, (128, 128))
    ui_rankP = pygame.image.load('./src/img/rank/p.png').convert_alpha()
    ui_rankP = pygame.transform.scale(ui_rankP, (128, 128))
    ui_rankX = pygame.image.load('./src/img/rank/x.png').convert_alpha()
    ui_rankX = pygame.transform.scale(ui_rankX, (128, 128))
    log.info(f"{bcolors.OKGREEN}Loaded.{bcolors.ENDC}")
except:
    log.critical(f"{traceback.format_exc}")
    messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')
    log.critical(f"{bcolors.FAIL} Error occurred while loading Images.")
    log.critical(f" Is file even exists?{bcolors.ENDC}")
    quitGame()

# SFX / OST
log.info(" Loading Sounds..")
try:
    # sfx
    sfx_handgunFire = pygame.mixer.Sound("./src/sound/sfx/handgun/handgun_fire.wav")
    sfx_handgunNoAmmo = pygame.mixer.Sound("./src/sound/sfx/handgun/handgun_noammo.wav")
    sfx_handgunReload = pygame.mixer.Sound("./src/sound/sfx/handgun/handgun_reload.wav")
    sfx_playerHurt = pygame.mixer.Sound("./src/sound/sfx/player/hurt.wav")
    sfx_playerDash = pygame.mixer.Sound("./src/sound/sfx/player/dash.wav")
    sfx_playerRadiation = pygame.mixer.Sound('./src/sound/sfx/player/radiation.wav')

    # ost
    ost_MainMenu = pygame.mixer.Sound('./src/sound/ost/background_ambient1.wav')

    log.info(f"{bcolors.OKGREEN} Loaded.{bcolors.ENDC}")
except:
    log.critical(f"{traceback.format_exc()}")
    messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')
    log.critical(f"{bcolors.FAIL} Error occurred while loading Sound.")
    log.critical(f" Is file even exists?{bcolors.ENDC}") # over 100!
    quitGame()

# font setup
log.info(" Resetting Font/Title..")
try:
    display.set_caption(f'TIME / BULLET - {GameSetting.VER}')
    display.set_icon(img_gameFavicon)

    # Font
    defaultFont = pygame.font.Font("./src/font/PretendardVariable.ttf", 30)
    defaultCopyrightFont = pygame.font.Font("./src/font/PretendardVariable.ttf", 20)
    defaultBulletFont = pygame.font.Font("./src/font/PretendardVariable.ttf", 24)
    mainTitleFont = pygame.font.Font("./src/font/PretendardVariable.ttf", 25)
    subTitleFont = pygame.font.Font("./src/font/PretendardVariable.ttf", 15)
    defaultBigFont = pygame.font.Font('./src/font/PretendardVariable.ttf', 40)

    log.info(f"{bcolors.OKGREEN} Loaded.{bcolors.ENDC}")
except:
    log.fatal(f"{traceback.format_exc()}")
    messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')
    log.fatal(f"{bcolors.FAIL} Error occurred while reseting font/title.")
    log.fatal(f" May occurrs because of weird pygame bug lol{bcolors.ENDC}")
finally: 
    if display.get_caption == '':
        display.set_caption('Caption not set.')

# font reset
log.info(" Resetting text object..")
text_MainLogoTitle = defaultFont.render('TIME \ BULLET', True, WHITE)
text_copyrightTeamName = defaultCopyrightFont.render('MADEBY. SONGRO STUDIO_', True, GRAY)
if list(GameSetting.MOTD) == '':
    text_mainMenuMotd = defaultCopyrightFont.render('지정되지 않은 메세지 입니다.', True, WHITE)
else:
    text_mainMenuMotd = defaultCopyrightFont.render(random.choice(list(GameSetting.MOTD)), True, WHITE)
text_autoSave = defaultFont.render('자동 저장중..', True, DARK_GRAY)
text_version = mainTitleFont.render(f'v {GameSetting.VER}', True, WHITE)

hud_bulletLeft = defaultBulletFont.render(str_MaxHandgunLoadBullet, True, WHITE)
hud_bulletMax = defaultBulletFont.render(str_MaxHandgunBullet, True, WHITE)
hud_bulletSlash = defaultBulletFont.render('/', True, WHITE)
hud_playerMana = defaultBulletFont.render('100%', True, WHITE)

debug_showFps = defaultFont.render('', True, WHITE)
showIfDebugging = defaultBulletFont.render('DEBUG MODE', True, ORANGE)
showIfNonProductMode = defaultBulletFont.render('완성된 제품이 아님', True, YELLOW)

pausedUI_text = defaultFont.render('일시중지됨', True, WHITE)

def autoSave():
    log.info(" AutoSaving..")
    Saving = 5
    try:
        with open('./src/save/0/playerSaveData.json', 'w+') as svFile:
            json.dump(data, svFile)
            log.info(f"{bcolors.OKGREEN} Saved.{bcolors.ENDC}")
        
        while Saving > 0:
            screen.blit(text_autoSave, [30, 650])
            Saving -= 1

        if Saving == 0:
            Saving = 5
    except:
        log.fatal(f"{bcolors.FAIL} Failed to save file to {svFile}.\n Is file even exist?")
        log.fatal(f"Traceback: {traceback.print_exc}{bcolors.ENDC}")

class Player(pygame.sprite.Sprite): # player
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.image = pygame.transform.rotozoom(pygame.image.load('./src/img/animations/entity/player/placeholder/indiv_animation/player_handgun_frame1.png').convert_alpha(), 0, GameSetting.PLAYER_VIEW_SIZE)
        self.basePlayerImage = self.image
        self.playerShootFrame = pygame.transform.rotozoom(pygame.image.load('./src/img/animations/entity/player/placeholder/indiv_animation/player_handgun_frame2.png').convert_alpha(), 0, GameSetting.PLAYER_VIEW_SIZE)
        self.hitboxRect = self.basePlayerImage.get_rect(center = pos)
        self.rect = self.hitboxRect.copy()
        self.lastTick = pygame.time.get_ticks()
        self.speed = GameSetting.PLAYER_SPEED
        self.DashSpeed = GameSetting.PLAYER_DASH_SPEED
        self.shoot = False
        self.isDashing = False
        self.shoot_cooldown = 0
        self.gunBarrelOffset = pygame.math.Vector2(GameSetting.GUN_OFFSET_X, GameSetting.GUN_OFFSET_Y)
        self.playerMana = 100       
        self.playerManaCooldown = 500
        self.playerVignette = pygame.image.load('./src/img/player_deco/vignette.png').convert_alpha()
        self.isDashAble = True
        self.health = 3
        self.hurtCooldown = 100
        self.bulletLeft = LoadedHandgunBullet
        self.vecPos = pygame.math.Vector2(pos)
        self.playerTimeMilli = 0
        self.playerTimeMin = 0
        self.playerTimeSec = 0
        self.mouse_coords = pygame.mouse.get_pos()
        self.xMouse = (self.mouse_coords[0] - GameSetting.WIDTH // 2)
        self.yMouse = (self.mouse_coords[1] - GameSetting.HEIGHT // 2)
        self.vec_pos = (self.hitboxRect.centerx, self.hitboxRect.centery)
        self.angle = math.degrees(math.atan2(self.yMouse, self.xMouse))
        self.isCheating = False
        self.gunList = ['default', 'shotgun', 'dev']

    def playerRotation(self):
        self.mouse_coords = pygame.mouse.get_pos()
        self.xMouse = (self.mouse_coords[0] - GameSetting.WIDTH // 2)
        self.yMouse = (self.mouse_coords[1] - GameSetting.HEIGHT // 2)
        self.angle = math.degrees(math.atan2(self.yMouse, self.xMouse))
        self.image = pygame.transform.rotate(self.basePlayerImage, -self.angle)
        self.rect = self.image.get_rect(center = self.hitboxRect.center)

    def drawPlayerMana(self):
        pygame.draw.rect(screen, BLUE, [30, 640, self.playerMana, 25])
       
    def user_input(self):
        self.velocity_x = 0
        self.velocity_y = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.velocity_y = -self.speed
        if keys[pygame.K_s]:
            self.velocity_y = self.speed
        if keys[pygame.K_d]:
            self.velocity_x = self.speed
        if keys[pygame.K_a]:
            self.velocity_x = -self.speed

        if self.velocity_x != 0 and self.velocity_y != 0: # moving diagonally
            self.velocity_x /= math.sqrt(2)
            self.velocity_y /= math.sqrt(2)

        if pygame.mouse.get_pressed() == (1, 0, 0):
            self.shoot = True
            self.checkShooting()
        else:
            self.shoot = False
    
        if keys[pygame.K_LCTRL]: # player slow
            self.playerMana -= GameSetting.PLAYERMANA_REMOVE_VAL
            self.speed = 1
        else:
            self.speed = 2

        if keys[pygame.K_LCTRL] and keys[pygame.K_RCTRL] and keys[pygame.K_LALT] and keys[pygame.K_RALT] and keys[pygame.K_LSHIFT] and keys[pygame.K_F3] and keys[pygame.K_SPACE] and keys[pygame.K_RSHIFT]:
            log.info('Cheat Mode activated.')
            self.shoot_cooldown = 0
            self.isCheating = True

        if GameSetting.SHOW_PLAYERMANA_CONSOLE == True:
            log.info(self.playerMana)
        else:
            pass

        if self.isCheating:
            self.shoot_cooldown = 0

        if keys[pygame.K_p]:
            log.debug(f'Enemy: {enemyGroup.sprites()}')

    def checkMana(self):
        if self.playerMana < 0:
            if self.playerManaCooldown > 0:
                self.playerManaCooldown -= self.lastTick
            else:
                log.info(" ReAdding Mana..")
                self.playerMana = 100
                self.playerManaCooldown = 500
        else:
            pass
    
    def checkMobStatus(self):
        if demoLevel.killedMob > 29:
            drawDeadScreen()

    def ui_playerStopWatch(self):
        ticks=pygame.time.get_ticks()
        millis=ticks%1000
        seconds=int(ticks/1000 % 60)
        minutes=int(ticks/60000 % 24)
        out=f'{minutes:02d}:{seconds:02d}:{millis}'.format(minutes=minutes, millis=millis, seconds=seconds)

        self.playerTimeMilli = millis
        self.playerTimeMin = minutes
        self.playerTimeSec = seconds

        playerUIStopWatch = defaultFont.render(out, True, GRAY)
        screen.blit(playerUIStopWatch, (30, 30))

    def checkColliedWithEnemy(self):
        if pygame.sprite.groupcollide(playerGroup, enemyGroup, True, False):
            self.hurtCooldown -= self.lastTick

            if self.hurtCooldown <= 0:
                self.health -= 1
                sfx_playerHurt.play()
                self.hurtCooldown == 100

            if self.health <= 0:
                self.pos = (400, 400)

    def checkCollisionWithWall(self, direction):
        if not GameSetting.NOCLIP:
            for sprite in obstaclesGroup:
                if sprite.rect.colliderect(self.hitboxRect):
                    if direction == "horizontal":
                        if self.velocity_x > 0:
                            self.hitboxRect.right = sprite.rect.left
                        if self.velocity_x < 0:
                            self.hitboxRect.left = sprite.rect.right
                    
                    if direction == "vertical":
                        if self.velocity_y < 0:
                            self.hitboxRect.top = sprite.rect.bottom
                        if self.velocity_y > 0:
                            self.hitboxRect.bottom = sprite.rect.top

    def checkShooting(self): 
        if self.shoot_cooldown == 0:
            spawnBulletPos = self.vec_pos + self.gunBarrelOffset.rotate(self.angle)
            self.bullet = Bullet(spawnBulletPos[0], spawnBulletPos[1], self.angle)
            self.shoot_cooldown = GameSetting.BULLET_COOLDOWN
            bulletGroup.add(self.bullet)
            allSpritesGroup.add(self.bullet)

    def move(self):
        self.hitboxRect.centerx += self.velocity_x
        self.checkCollisionWithWall("horizontal")

        self.hitboxRect.centery += self.velocity_y
        self.checkCollisionWithWall("vertical")

        self.hitboxRect.center = self.hitboxRect.center 
        
        self.vec_pos = (self.hitboxRect.centerx, self.hitboxRect.centery)
        
    def update(self):
        self.user_input()
        self.move()
        self.playerRotation()
        self.checkMana()
        self.checkColliedWithEnemy()
        self.drawPlayerMana()
        self.ui_playerStopWatch()
        self.checkMobStatus()

        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

class Bullet(pygame.sprite.Sprite): # bullet
    def __init__(self, x, y, angle): 
        super().__init__()
        self.image = entity_Bullet
        self.image = pygame.transform.rotozoom(self.image, 0, GameSetting.BULLET_VIEWSIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.x = x
        self.y = y
        self.speed = GameSetting.BULLET_SPEED
        self.angle = angle
        self.x_vel = math.cos(self.angle * (2*math.pi/360)) * self.speed
        self.y_vel = math.sin(self.angle * (2*math.pi/360)) * self.speed
        self.bulletLifeTime = GameSetting.BULLET_LIFETIME
        self.spawnTime = pygame.time.get_ticks()
        

    def bulletMovement(self): 
        self.x += self.x_vel
        self.y += self.y_vel

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

        if pygame.time.get_ticks() - self.spawnTime > self.bulletLifeTime: 
            self.kill()
            sfx_handgunFire.stop()

    def checkCollisionWithWall(self):         
        if pygame.sprite.spritecollide(self, obstaclesGroup, False): # wall collisions
            self.kill()

    def update(self):
        self.bulletMovement()
        self.checkCollisionWithWall()

class Enemy(pygame.sprite.Sprite): # enemy
    def __init__(self, position):
        super().__init__(enemyGroup, allSpritesGroup)
        self.image = pygame.image.load('./src/img/animations/entity/enemy/indiv_animation/zombie_frame1.png').convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, GameSetting.ENEMY_VIEWSIZE)
        self.steps = random.randint(3, 6) * GameSetting.TILESIZE

        self.rect = self.image.get_rect()
        self.rect.center = position

        self.directionIndex = random.randint(0, 3)

        self.direction = pygame.math.Vector2()
        self.velocity = pygame.math.Vector2()
        self.speed = GameSetting.ENEMY_SPEED

        self.position = pygame.math.Vector2(position)

        self.isPlayerAlive = True
        self.isEnemyAlive = True

        self.damage = 5
        self.directionList = [(1,1), (1,-1), (-1,1), (-1,-1)]

        self.enemyRadius = GameSetting.ENEMY_RADIUS
        self.roamingSpeed = GameSetting.ENEMY_ROAMING_SPEED

        self.hurt = 0
        self.killed = 0

    def getNewPathTrace(self):
        self.directionIndex = random.randint(0, len(self.directionList)-1)
        self.steps = random.randint(3, 6) * GameSetting.TILESIZE

    def roam(self):
        self.direction.x, self.direction.y = self.directionList[self.directionIndex] # gets a random direction
        self.velocity = self.direction * self.roamingSpeed
        self.position += self.velocity
        
        self.rect.centerx = self.position.x
        self.checkCollision("horizontal", "roam")

        self.rect.centery = self.position.y
        self.checkCollision("vertical", "roam")
        
        self.rect.center = self.rect.center
        self.position = (self.rect.centerx, self.rect.centery)

        self.steps -= 1

        if self.steps == 0:
            self.getNewPathTrace()

    def checkCollision(self, direction, move_state):
        for sprite in obstaclesGroup:
            if sprite.rect.colliderect(self.rect):
                self.collide = True
                if direction == "horizontal":
                    if self.velocity.x > 0:
                        self.rect.right = sprite.rect.left
                    if self.velocity.x < 0:
                        self.rect.left = sprite.rect.right 
                if direction == "vertical":
                    if self.velocity.y < 0:
                        self.rect.top = sprite.rect.bottom
                    if self.velocity.y > 0:
                        self.rect.bottom = sprite.rect.top
                if move_state == "roam":
                    self.getNewPathTrace()

    def getCollisionBox(self):
        baseEnemyRect = self.rect.move(-demoLevel.offset.x, -demoLevel.offset.y)
        pygame.draw.rect(screen, 'red', baseEnemyRect, width=2)
        baseEnemyRect = self.rect.move(-demoLevel.offset.x, -demoLevel.offset.y)
        pygame.draw.rect(screen, 'yellow', baseEnemyRect, width=2)

    def getVectorDistance(self, vector_1, vector_2):
        return (vector_1 - vector_2).magnitude()

    def pathTracePlayer(self): # path tracing
        if self.velocity.x > 0:
            self.current_movement_sprite = 0
        else:
            self.current_movement_sprite = 1
        
        player_vector = pygame.math.Vector2(player.rect.center)
        enemy_vector = pygame.math.Vector2(self.rect.center)
        distance = self.getVectorDistance(player_vector, enemy_vector)

        if distance > 0:
            self.direction = (player_vector - enemy_vector).normalize()
        else:
            self.direction = pygame.math.Vector2()

        self.velocity = self.direction * self.speed
        self.position += self.velocity

        self.rect.centerx = self.position.x
        self.checkCollision("horizontal", "hunt")

        self.rect.centery = self.position.y
        self.checkCollision("vertical", "hunt")

        self.rect.center = self.rect.center

        self.position = (self.rect.centerx, self.rect.centery)

    def getVectorDistance(self, vector_1, vector_2):
        return (vector_1 - vector_2).magnitude()

    def hunt_player(self):  
        if self.velocity.x > 0:
            self.current_movement_sprite = 0
        else:
            self.current_movement_sprite = 1
        
        player_vector = pygame.math.Vector2(player.rect.center)
        enemy_vector = pygame.math.Vector2(self.rect.center)
        distance = self.getVectorDistance(player_vector, enemy_vector)

        if distance > 0:
            self.direction = (player_vector - enemy_vector).normalize()
        else:
            self.direction = pygame.math.Vector2()

        self.velocity = self.direction * self.speed
        self.position += self.velocity

        self.rect.centerx = self.position.x
        self.checkCollision("horizontal", "hunt")

        self.rect.centery = self.position.y
        self.checkCollision("vertical", "hunt")

        self.rect.center = self.rect.center

        self.position = (self.rect.centerx, self.rect.centery)

    def checkCollisionWithBullet(self):
        if pygame.sprite.groupcollide(bulletGroup, enemyGroup, False, True):
            demoLevel.killedMob += 1
            demoLevel.lastMob -= 1

            log.debug(f'Killed Enemy: {demoLevel.killedMob}, {demoLevel.lastMob}')

        if self.hurt > 5:
            self.kill()
            self.hurt = 0

    def update(self):
        if self.isEnemyAlive:
            if self.getVectorDistance(pygame.math.Vector2(player.rect.center), pygame.math.Vector2(self.rect.center)) < self.enemyRadius:    # default = 400
                self.hunt_player()
            else:
                self.roam()
            self.checkCollisionWithBullet()

            if GameSetting.IFYOUKNOWWHATAREYOUDOINGRIGHTNOWTURNONTHISFORDEBUG:
                if GameSetting.SHOW_COLLISION_BOXES:
                    self.getCollisionBox()
        else:
            self.kill

class GameLevel(pygame.sprite.Group): # load level
    def __init__(self, map):
        super().__init__()
        self.offset = pygame.math.Vector2()
        self.floorRect = img_demoMapBackground.get_rect(topleft = (0,0))
        self.enemySpawnPos = []
        self.mapSelection = map
        self.createMap()
        self.killedMob = 0
        self.lastMob = GameSetting.ENEMEY_SPAWN_RATE

    def createMap(self):
        if self.mapSelection == 'demo':
            layouts = {
                    "boundary": self.importCsv("./src/maps/csv/dev_test/dev_test_Boundary.csv"),
                    "walls": self.importCsv("./src/maps/csv/dev_test/dev_test_Walls.csv"),
                    "enemies": self.importCsv("./src/maps/csv/dev_test/dev_test_Enemy.csv"),
                    }

            for style, layout in layouts.items():
                for row_index, row in enumerate(layout):
                    for col_index, col in enumerate(row):
                        if col != "-1":
                            x = col_index * GameSetting.TILESIZE
                            y = row_index * GameSetting.TILESIZE
                            if style == "boundary":
                                Tile((x,y), [obstaclesGroup], "boundary", col)
                            if style == "walls":
                                Tile((x,y), [allSpritesGroup], "walls", col)  
                            if style == "enemies":
                                self.enemySpawnPos.append((x, y))

            self.spawnEnemy()

    def importCsv(self, path):
        terrain_map = []
        with open(path) as level_map:
            layout = reader(level_map, delimiter=",")
            for row in layout:
                terrain_map.append(list(row))
            return terrain_map
    
    def spawnEnemy(self):
        for i in range(0, GameSetting.ENEMEY_SPAWN_RATE, 1):
            Enemy(random.choice(self.enemySpawnPos))
            log.debug(f'Spawned Enemy: {i}')

    def restartGame(self):
        playerGroup.empty()
        playerGroup.add(player)
        allSpritesGroup.add(player)
        bulletGroup.empty()

        self.spawnEnemy()

    def custom_draw(self): 
        self.offset.x = player.rect.centerx - (GameSetting.WIDTH // 2)
        self.offset.y = player.rect.centery - (GameSetting.HEIGHT // 2)

        # draw floor
        floor_offset_pos = self.floorRect.topleft - self.offset

        screen.blit(img_blackVoid, [0, 0])
        screen.blit(img_demoMapBackground, floor_offset_pos)

        # draw player hitbox for debug perpose
        if GameSetting.IFYOUKNOWWHATAREYOUDOINGRIGHTNOWTURNONTHISFORDEBUG:
            if GameSetting.SHOW_COLLISION_BOXES:
                base_rect = player.rect.copy().move(-self.offset.x, -self.offset.y)
                pygame.draw.rect(screen, "red", base_rect, width=2)
                rect = player.rect.copy().move(-self.offset.x, -self.offset.y)
                pygame.draw.rect(screen, "yellow", rect, width=2)

            for sprite in allSpritesGroup: 
                offset_pos = sprite.rect.topleft - self.offset
                screen.blit(sprite.image, offset_pos)

class Tile(pygame.sprite.Sprite): # load tile
    def __init__(self, pos, groups, type, unique_id):
        super().__init__(groups)
        if type == "void":
            self.image = voidWall
        elif type == "boundary":
            self.image = backgroundWall
        elif type == "walls":
            if unique_id == "0":
                self.image = topWall
            if unique_id == "1":
                self.image = topLeftDownWall
            if unique_id == "2":
                self.image = rightStraightWall
            if unique_id == "3":
                self.image = toprightDownWall
            if unique_id == "4":
                self.image = straightWall
            if unique_id == "5":
                self.image = straightWall
            if unique_id == "7":
                self.image = straightWall
            if unique_id == "8":
                self.image = straightNonDownWall
            if unique_id == "9":
                self.image = topRightWall
            if unique_id == "10":
                self.image = rightStraightWall
            if unique_id == "11":
                self.image = topLeftWall
            if unique_id == "12":
                self.image = nonWall
            if unique_id == "13":
                self.image = rightNonLeftWall
            if unique_id == "14":
                self.image = rightStraightWall
            if unique_id == "15":
                self.image = leftNonRightWall
        elif type == "void":
            if unique_id == "4":
                self.image = voidWall

        self.rect = self.image.get_rect(topleft = pos) 

player = Player((400, 400))

allSpritesGroup = pygame.sprite.Group()
bulletGroup = pygame.sprite.Group()
enemyGroup = pygame.sprite.Group()
obstaclesGroup = pygame.sprite.Group()
floorGroup = pygame.sprite.Group()
playerGroup = pygame.sprite.Group()
itemGroup = pygame.sprite.Group()

demoLevel = GameLevel('demo')
btnStart = Button(30, 620, btn_Start, 1)
btnExit = Button(30, 650, btn_Exit, 1)
btnRestart = Button(400, 400, btn_Restart, 1)
#btnGameRestart = Button(400, 400, btn_RestartBtn, 1)

allSpritesGroup.add(player)
playerGroup.add(player)

# main
if GameSetting.RUN_GAME_BEFORE_MENU:
    isMainGameScene = True
    isMainMenuScene = False
else:
    isMainGameScene = False
    isMainMenuScene = True

def drawDeadScreen():
    log.info('Player Killed.')
    game_over_screen_fade = pygame.Surface((GameSetting.WIDTH, GameSetting.HEIGHT))
    game_over_screen_fade.fill((0, 0, 0))
    game_over_screen_fade.set_alpha(160)
    screen.blit(game_over_screen_fade, (0, 0))

    if not demoLevel.lastMob == 0:
        ui_Dead = defaultBigFont.render('죽었습니다!', True, RED)
    elif demoLevel.lastMob == 0:
        ui_Dead = defaultBigFont.render('살아남았습니다!', True, BLUE)
    ui_SurvivedTime = mainTitleFont.render(f'{player.playerTimeMin}분 {player.playerTimeSec}초 동안 살아남았습니다!', True, WHITE)
    ui_KilledMob = mainTitleFont.render(f'{demoLevel.killedMob}마리의 좀비를 죽였습니다!', True, WHITE)
    ui_LastMob = mainTitleFont.render(f'여전히 {demoLevel.lastMob}마리의 좀비가 남아있습니다.', True, WHITE)
    ui_Rank = ui_rankS

    if demoLevel.lastMob > 0 and player.playerTimeMin <= 1 and player.playerTimeSec <= 0:
        ui_Rank = ui_rankA
    if demoLevel.lastMob == 0:
        ui_Rank = ui_rankA
    if demoLevel.lastMob >= 10 and player.playerTimeMin <= 1 and player.playerTimeSec <= 30:
        ui_Rank = ui_rankB
    if demoLevel.lastMob >= 20 and player.playerTimeMin <= 2 and player.playerTimeSec <= 0:
        ui_Rank = ui_rankC
    if demoLevel.lastMob >= 25 and player.playerTimeMin <= 2 and player.playerTimeSec <= 30:
        ui_Rank = ui_rankD
    if demoLevel.lastMob >= GameSetting.ENEMEY_SPAWN_RATE:
        ui_Rank = ui_rankF
    elif demoLevel.lastMob == 0 and player.playerTimeMin == 0 and player.playerTimeSec <= 30:
        ui_LastMob = mainTitleFont.render(f'모든 좀비를 처치하였습니다! 축하해요!!!', True, WHITE)
    if demoLevel.lastMob == 0 and player.playerTimeMin <= 0 and player.playerTimeSec <= 1:
        ui_Rank = ui_rankX
        ui_LastMob = mainTitleFont.render(f'이럴수가... 어떻게 이런 기록을 낼수 있죠???', True, WHITE)
    if demoLevel.lastMob == 0 and player.playerTimeMin == 0 and player.playerTimeSec <= 20:
        ui_Rank = ui_rankP
        ui_LastMob = mainTitleFont.render(f'PERFECT.', True, WHITE)
    if GameSetting.IFYOUKNOWWHATAREYOUDOINGRIGHTNOWTURNONTHISFORDEBUG:
        ui_Rank = ui_rankX
    
    screen.blit(ui_Rank, (250, 150))

    screen.blit(ui_Dead, (400, 150))
    screen.blit(ui_SurvivedTime, (400, 200))
    screen.blit(ui_KilledMob, (400, 300))
    screen.blit(ui_LastMob, (400, 340))

    if btnRestart.drawBtn(screen):
        mainMenu()
        game_over_screen_fade.fill((255, 255, 255))

    #if btnGameRestart.drawBtn(screen):
    #    demoLevel.restartGame()
    #    game_over_screen_fade.fill((255, 255, 255))

def gameDemo(): # main game
        log.info(' Starting..')
        ost_MainMenu.play()
        screen.fill((0, 0, 0))
        state = "game"
        pausedmotd = random.choice(list(GameSetting.PAUSED_MOTD))

        #restartGame()
        while True: # replay scene
            eventList = pygame.event.get()
            for event in eventList:
                if event.type == pygame.QUIT:
                    log.info("Saving..")
                    try:
                        with open('./src/save/0/playerSaveData.json', 'w+') as svFile:
                            json.dump(data, svFile)
                        svFile.close()
                        log.info(f"{bcolors.OKGREEN} Saved.{bcolors.ENDC}")
                    except:
                        log.fatal(f"{bcolors.FAIL} Failed to save file to {svFile}.\n Is file even exist?")
                        log.fatal(f"Traceback: {traceback.print_exc()}{bcolors.ENDC}")
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: 
                        state = "pause"
                    if event.key == pygame.K_l:
                        state = "game"

            if state == "game":
                demoLevel.custom_draw()

                if demoLevel.killedMob > GameSetting.ENEMEY_SPAWN_RATE:
                    drawDeadScreen()

                screen.blit(img_overlayDeadScreenBlack, [0, 0])
                screen.blit(img_overlayViggnete, [0, -293])
                # render
                allSpritesGroup.update()
                playerGroup.update()

                # debug info update
                hud_playerMana = subTitleFont.render(f'{str(player.playerMana)}%', True, WHITE)
                hud_debugFpsScreen = subTitleFont.render(f'{math.ceil(clock.get_fps())}FPS (반올림됨, 높을수록 좋음)', True, WHITE)
                hud_debugMilliTickScreen = subTitleFont.render(f'{math.ceil(clock.get_rawtime())}틱 처리중 (반올림됨, 낮을수록 좋음)', True, WHITE)
                hud_debugMapInfoScreen = subTitleFont.render(f'현재 "dev_test_Boundary.csv, dev_test_Enemy.csv, dev_test_Walls.csv" 불러와짐', True, WHITE)
                hud_debugVerInfoScreen = subTitleFont.render(f'spsro Engine ver {GameSetting.ENGINE_VER}, using some files from pygame 2.5.1 (SDL2)', True, WHITE)
                hud_debugScreenResInfoScreen = subTitleFont.render(f'{GameSetting.WIDTH} x {GameSetting.HEIGHT} 해당도로 플레이중 (최대 {GameSetting.DEF_FPS}FPS)', True, WHITE)
                hud_debugGameSettingInfoScreen = subTitleFont.render(f'{GameSetting.MUSIC_VOL}, {GameSetting.PLAYER_VIEW_SIZE}, {GameSetting.PLAYER_DASH_REMOVE_MANA_VAL}, {GameSetting.PLAYER_SPEED}, {GameSetting.PLAYER_DASH_SPEED}, {GameSetting.PLAYERMANA_COOLDOWN}, {GameSetting.PLAYERMANA_REMOVE_VAL}, {GameSetting.GUN_OFFSET_X}, {GameSetting.GUN_OFFSET_Y}, {GameSetting.GAME_DEFAULTSOUND_PLAY}, {GameSetting.IFYOUKNOWWHATAREYOUDOINGRIGHTNOWTURNONTHISFORDEBUG}, {GameSetting.SHOW_CURRENTFPS}, {GameSetting.DEBUG_FPSWARNING_VALUE}, {GameSetting.SHOW_PLAYERMANA_CONSOLE}, {GameSetting.SCREEN_FLAGS}, {GameSetting.VSYNC}, {GameSetting.RUN_GAME_BEFORE_MENU}, {GameSetting.RUN_FULLSCREEN}, {GameSetting.SHOW_TRIGGERS}, {GameSetting.DRAW_GREYBACKGROUND_ASVOID}, {GameSetting.YES_THIS_IS_DEBUGGER_IDC}, {GameSetting.SHOW_DEBUGINFO_TOSCREEN}, {GameSetting.SHOW_COLLISION_BOXES}, {GameSetting.ISPRODUCTMODE}, {GameSetting.LOGLEVEL}', True, WHITE)

                if clock.get_fps() <= 30:
                    hud_debugFpsScreen = subTitleFont.render(f'{math.ceil(clock.get_fps())}FPS (반올림됨, 높을수록 좋음)', True, ORANGE)
                elif clock.get_fps() <= 20:
                    hud_debugFpsScreen = subTitleFont.render(f'{math.ceil(clock.get_fps())}FPS (반올림됨, 높을수록 좋음)', True, (235, 232, 52))
                elif clock.get_fps() <= 10:
                    hud_debugFpsScreen = subTitleFont.render(f'{math.ceil(clock.get_fps())}FPS (반올림됨, 높을수록 좋음)', True, RED)

                if math.ceil(clock.get_rawtime()) >= 10:
                    hud_debugMilliTickScreen = subTitleFont.render(f'{math.ceil(clock.get_rawtime())}틱 처리중 (반올림됨, 낮을수록 좋음) 주의: 처리한 틱 갯수가 일반적인 상황보다 많음', True, ORANGE)
                elif math.ceil(clock.get_rawtime()) >= 19:
                    hud_debugMilliTickScreen = subTitleFont.render(f'{math.ceil(clock.get_rawtime())}틱 처리중 (반올림됨, 낮을수록 좋음) 경고: 처리한 틱 갯수가 많음', True, (235, 232, 52))
                elif math.ceil(clock.get_rawtime()) >= 29:
                    hud_debugMilliTickScreen = subTitleFont.render(f'{math.ceil(clock.get_rawtime())}틱 처리중 (반올림됨, 낮을수록 좋음) 경고: 처리한 틱 갯수가 정상적인 상황보다 많음, 최적화 필요', True, RED)
                screen.blit(icn_GunSelect_handGun, [30, 670])
                
                if GameSetting.IFYOUKNOWWHATAREYOUDOINGRIGHTNOWTURNONTHISFORDEBUG:
                    screen.blit(showIfDebugging, [30, 52])

                    if GameSetting.ISPRODUCTMODE == False:
                        screen.blit(showIfNonProductMode, [30, 640])

                    if GameSetting.SHOW_CURRENTFPS == True:
                            pygame.display.set_caption(f"FPS: {clock.get_fps()}")
                    else:
                        pass
                    if GameSetting.SHOW_DEBUGINFO_TOSCREEN == True:
                        screen.blit(hud_debugFpsScreen, [30, 97])
                        screen.blit(hud_debugMilliTickScreen, [30, 117])
                        screen.blit(hud_playerMana, [30, 135])
                        screen.blit(hud_debugMapInfoScreen, [30, 155])
                        screen.blit(hud_debugVerInfoScreen, [30, 215])
                        screen.blit(hud_debugScreenResInfoScreen, [30, 175])
                        screen.blit(hud_debugGameSettingInfoScreen, [30, 195])
                    else:
                        pass
                else:
                    pass

                if not playerGroup.has(player):
                    drawDeadScreen()

            if playerGroup:
                if state == "pause":
                        ost_MainMenu.stop()
                        ui_pausedTxt = defaultBigFont.render('일시중지됨', True, WHITE)
                        ui_unpauseTxt = defaultBulletFont.render('[L] 키를 눌러 일시중지 풀기', True, WHITE)
                        ui_pasuedTxtEaster = defaultBulletFont.render(pausedmotd, True, WHITE)

                        screen.blit(img_overlayDeadScreenBlack, [0, 0])
                        screen.blit(ui_pausedTxt, [400, 300])
                        screen.blit(ui_unpauseTxt, [400, 400])
                        screen.blit(ui_pasuedTxtEaster, [400, 350])
                else:
                    pass
            else:
                pass

            pygame.display.flip()

def mainMenu(): # main menu
    screen.fill((255, 255, 255))
    while True:
        pygame.mixer.stop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(mainMenu_backgruond, [0, 0])
        screen.blit(text_version, [32, 53])
        screen.blit(text_MainLogoTitle, [30, 20])
        screen.blit(text_copyrightTeamName, [985, 650])
        screen.blit(text_mainMenuMotd, [32, 83])

        if btnStart.drawBtn(screen):
            gameDemo()

        if btnExit.drawBtn(screen):
            sys.exit()

        pygame.display.update()
        dt = clock.tick(GameSetting.DEF_FPS)

while running:
    try:
        while isMainGameScene:
            gameDemo()

        while isMainMenuScene:
            mainMenu()
    except Exception:
        log.fatal(f"{traceback.format_exc()}")
        messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')
        log.fatal(f"{bcolors.FAIL} Error occurred while replaying scene.")
        log.fatal(f'{traceback.format_exc()}{bcolors.ENDC}')
        pygame.quit()
        sys.exit()

pygame.quit()
